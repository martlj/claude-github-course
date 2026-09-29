#!/usr/bin/env python3
"""Check this repository follows the shared research standards.

Run from the repository root:   python .github/scripts/check_standards.py

Errors (exit code 1) are things that must be fixed. Warnings are things to
look at. Part of research-standards. Don't edit in a project.
Only uses the Python standard library.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()
IN_CI = os.environ.get("GITHUB_ACTIONS") == "true"

REQUIRED = {
    "general": ["README.md", "CLAUDE.md", "CONTRIBUTING.md", ".gitignore",
                ("LICENSE", "LICENSE.md", "LICENSE.txt")],
    "analysis": ["CHANGELOG.md", "CITATION.cff", "data/README.md", "docs/decisions.md",
                 ("environment.yml", "requirements.txt", "pyproject.toml", "renv.lock")],
    "website": ["_config.yml"],
    "course": ["_config.yml"],
}
RAW_TYPES = {".czi", ".nd2", ".lif", ".lsm", ".ims", ".oib", ".oif", ".vsi", ".sld", ".svs"}
MAX_MB = 5
PERSONAL_PATH = re.compile(r"""["'](/Users/[^/"']+/|/home/[^/"']+/|[A-Za-z]:\\\\Users)""")
CODE_SUFFIXES = {".ijm", ".py", ".R", ".r", ".groovy", ".bsh", ".m"}

errors: list[str] = []
warnings: list[str] = []


def error(msg, file=None):
    errors.append(msg)
    if IN_CI:
        print(f"::error{' file=' + str(file) if file else ''}::{msg}")


def warn(msg, file=None):
    warnings.append(msg)
    if IN_CI:
        print(f"::warning{' file=' + str(file) if file else ''}::{msg}")


def read_config() -> dict:
    cfg = {}
    p = ROOT / ".claude" / "research-standards.yml"
    if p.exists():
        for line in p.read_text().splitlines():
            if ":" in line and not line.lstrip().startswith("#"):
                k, v = line.split(":", 1)
                cfg[k.strip()] = v.split("#")[0].strip().strip('"')
    return cfg


def tracked_files() -> list[Path]:
    try:
        out = subprocess.run(["git", "ls-files"], capture_output=True, text=True,
                             check=True, cwd=ROOT).stdout
        return [ROOT / f for f in out.splitlines() if (ROOT / f).is_file()]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line and not line.startswith(" "):
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm


def main() -> int:
    cfg = read_config()
    if not cfg:
        error("Missing .claude/research-standards.yml. Install the standards with install.py.")
    profile = cfg.get("profile", "general")
    strict = cfg.get("strict", "false").lower() == "true"

    # 1. Required files
    for req in REQUIRED["general"] + REQUIRED.get(profile, []):
        options = req if isinstance(req, tuple) else (req,)
        if not any((ROOT / o).exists() for o in options):
            error(f"Required file missing: {' or '.join(options)}")

    # 2. Shared rules and skills present and unmodified
    rules = list((ROOT / ".claude" / "rules").glob("**/*.md"))
    if not rules:
        error("No shared rules found in .claude/rules/")
    lock_path = ROOT / ".claude" / "research-standards.lock.json"
    if lock_path.exists():
        lock = json.loads(lock_path.read_text())
        for rel, digest in lock.get("files", {}).items():
            f = ROOT / rel
            if not f.exists():
                warn(f"Shared file deleted: {rel}. "
                     "Re-install the standards if this wasn't intended.")
            elif hashlib.sha256(f.read_bytes()).hexdigest() != digest:
                msg = (f"Shared standard file edited locally: {rel}. Put project-specific "
                       "exceptions in CLAUDE.md instead, or propose the change upstream.")
                (error if strict else warn)(msg, rel)

    # 3. Skills have the frontmatter Claude needs
    for skill in (ROOT / ".claude" / "skills").glob("*/SKILL.md"):
        fm = frontmatter(skill.read_text(encoding="utf-8"))
        if not fm.get("description"):
            error(f"Skill {skill.parent.name} has no 'description' in its frontmatter", skill)

    # 4. CLAUDE.md is short and filled in
    claude_md = ROOT / "CLAUDE.md"
    if claude_md.exists():
        text = claude_md.read_text(encoding="utf-8")
        if len(text.splitlines()) > 200:
            warn("CLAUDE.md is over 200 lines. Keep it to project-specific facts; "
                 "shared standards belong in .claude/rules/.", "CLAUDE.md")
        if "✏️" in text:
            warn("CLAUDE.md still contains ✏️ placeholders. Fill in the project facts.", "CLAUDE.md")

    # 5. Data hygiene and hard-coded paths in tracked files
    for f in tracked_files():
        rel = f.relative_to(ROOT)
        if f.suffix.lower() in RAW_TYPES:
            error(f"Raw microscope file tracked by Git: {rel}. Data belongs on storage.", rel)
        elif f.stat().st_size > MAX_MB * 1024 * 1024:
            error(f"File larger than {MAX_MB} MB tracked by Git: {rel}", rel)
        if f.suffix in CODE_SUFFIXES and ".claude" not in rel.parts and ".github" not in rel.parts:
            try:
                if PERSONAL_PATH.search(f.read_text(encoding="utf-8", errors="ignore")):
                    error(f"Hard-coded personal path in {rel}. Use a parameter instead.", rel)
            except OSError:
                pass

    # Report
    print(f"\nResearch standards check (profile: {profile}, version {cfg.get('version', '?')})")
    for e in errors:
        print(f"  ❌ {e}")
    for w in warnings:
        print(f"  ⚠️  {w}")
    if not errors and not warnings:
        print("  ✅ All checks passed")
    elif not errors:
        print("  ✅ No errors (see warnings above)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
