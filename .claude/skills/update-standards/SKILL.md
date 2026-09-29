---
name: update-standards
description: Install or update the shared research-standards files (.claude/rules, .claude/skills, CONTRIBUTING.md, templates) in this repository from the upstream research-standards repository.
disable-model-invocation: true
---
<!-- research-standards v1.0.0 -->

# Install or update the shared standards

The upstream source and installed version are recorded in
`.claude/research-standards.yml`. If that file is missing, ask the researcher
for the research-standards repository URL.

1. Read `.claude/research-standards.yml` (`source`, `version`).
2. Clone or download the upstream repository at its latest release tag (or `main` if there are no tags) into a temporary folder **outside** this repository.
3. Show what would change: for each file under `.claude/rules/`, `.claude/skills/`, `CONTRIBUTING.md`, `.github/pull_request_template.md`, `.github/ISSUE_TEMPLATE/`, `.github/scripts/check_standards.py` and `.github/workflows/standards.yml`, say whether it's new, changed or unchanged, and summarise changes from the upstream `CHANGELOG.md`.
4. **Local edits:** if a shared file here differs from the *installed* upstream version, it has been edited locally. Don't overwrite it silently. Show the difference and ask whether the edit should move into the project's `CLAUDE.md` (the right place for project-specific exceptions) or be proposed upstream.
5. With agreement, run the upstream `install.py` (or copy the files), updating `version` in `.claude/research-standards.yml`. **Never** overwrite the project's `CLAUDE.md`, `README.md` or other project files.
6. Commit on a branch `update-standards-vX.Y.Z` with message `Update research standards to vX.Y.Z` and open a pull request listing the changes.
