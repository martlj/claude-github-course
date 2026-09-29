# Research standards

<!-- research-standards v1.1.0. Shared file: don't edit in a project. -->

This repository follows a shared set of **research standards**: the same
rules, checks and Claude instructions used across all our projects. That way
anyone can pick up anyone else's project, and Claude works the same way
everywhere.

## The files, and who reads them

| File / folder | Read by | What it's for | Edit it? |
|---------------|---------|---------------|----------|
| `CLAUDE.md` | Claude (every session) | Facts about **this** project, and any deliberate exceptions | ✅ Yes. It's yours |
| `CLAUDE.local.md` | Claude (only on your computer) | Your personal preferences. Ignored by Git, so it isn't shared | ✅ Yes, if you want one |
| `.claude/rules/*.md` | Claude (automatically) | The shared standards (see below) | ❌ No. Propose changes upstream |
| `.claude/skills/*/SKILL.md` | Claude (when relevant, or when you type `/name`) | Step-by-step procedures for common jobs | ❌ No. Propose changes upstream |
| `STANDARDS.md` | People | This overview | ❌ |
| `CONTRIBUTING.md` | People | How to work on this project with others | ❌ |
| `.github/` | GitHub | Issue and pull-request templates, and automated checks | ❌ (the shared parts) |
| `.claude/research-standards.yml` | The update tools | Which version of the standards is installed | Only `profile` / `strict` |

## The rules (always followed)

| Rule | In one line |
|------|-------------|
| `01-working-with-researchers` | Plan first, change only what was asked, never invent facts, explain what changed |
| `02-git-and-github` | Branches and pull requests, small commits with clear messages, link issues |
| `03-data-management` | Code in Git, data on storage, raw data read-only, no personal data |
| `04-reproducibility` | Environments recorded, no hard-coded paths, versions, decision log, releases |
| `05-testing` | Known-answer tests, never weaken a failing test, "it runs" ≠ "it's right" |
| `06-documentation` | Required files, headers, docstrings, plain language, units |
| `07-scientific-integrity` | No fabrication, image-processing ethics, report exclusions |

These load only when Claude works on matching files:

| Rule | Applies to |
|------|-----------|
| `lang-fiji-macros` | `.ijm`, `fiji/` |
| `lang-python` | `.py`, `.ipynb`, environment files |
| `lang-r` | `.R`, `.Rmd`, `.qmd` |
| `topic-image-analysis` | analysis code and notebooks |
| `topic-websites` | Jekyll / GitHub Pages files |

## The skills (type `/` in Claude Code to see them)

| Skill | Use it to… |
|-------|-----------|
| `/start-analysis` | Plan a new analysis and record it as an issue before any code |
| `/new-fiji-macro` | Write a Fiji macro that follows the standards |
| `/new-python-script` | Write a Python analysis script with tests |
| `/add-known-answer-test` | Add a test that checks code against a known answer |
| `/log-decision` | Record a threshold/parameter/exclusion decision with the date and reason |
| `/review-changes` | Check a branch or pull request against the standards before merging |
| `/prepare-release` | Tag the exact version used for a paper, with changelog and citation |
| `/apply-standards` | Audit an existing or messy project and plan how to tidy it |
| `/update-standards` | Install the latest version of these standards |
| `/progress-summary` | Summarise recent work for your PI or a lab meeting |
| `/propose-standards-change` | Suggest an improvement to these standards (drafts an issue for the maintainers) |

Claude also picks the right skill by itself when your request matches, so you
don't have to remember the names.

## Exceptions

If this project needs to break a rule (e.g. "commits straight to `main` are
fine, it's a personal sketchbook"), write the exception and the reason in
`CLAUDE.md` under *Exceptions to the shared standards*. **Don't edit the
shared files.** The weekly standards check flags edited shared files, and
the next update would overwrite them.

## Suggesting a change to the standards

Ask Claude **`/propose-standards-change`**. It checks whether the idea is
already covered, helps you decide whether it belongs in the shared standards or
only in this project's `CLAUDE.md`, and drafts an issue for the
**research-standards** repository (the address is in `.claude/research-standards.yml`).
You can also fill in the *Propose a change* form there yourself.

Maintainers review every proposal and reply with a decision and a reason. Not
every proposal is accepted, and that's normal. When accepted changes are
released as a new version, every project gets an automatic issue offering the update.
