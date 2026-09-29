<!-- research-standards v1.1.0. Shared standard: don't edit in a project; propose changes to the research-standards repository. -->

# Documentation

Write documentation for a new lab member who has the repository and the data but nobody to ask.

## Required files in every repository

| File | Contents |
|------|----------|
| `README.md` | What the project is (1–2 sentences), who owns it, how to install, how to run, where the data is, how to cite |
| `CLAUDE.md` | Project-specific facts and exceptions for Claude (keep it short, because the shared rules are in `.claude/rules/`) |
| `CONTRIBUTING.md` | How collaborators work on the project |
| `LICENSE` | Reuse terms. MIT is suggested for code, CC BY 4.0 for text/figures (the researcher decides) |
| `CHANGELOG.md` | Notable changes by version (analysis repositories) |
| `CITATION.cff` | How to cite (analysis repositories) |
| `data/README.md` | Where the data lives (analysis repositories) |
| `docs/decisions.md` | Dated analysis decisions (analysis repositories) |

## Code documentation

- Every script or macro starts with a header block: title, author, version, date, description, inputs, outputs, requirements, and how to test it. Follow the format in the language-specific rules.
- Every function has a docstring saying what it does, its parameters (with units), and what it returns.
- Comments explain *why*, not *what*: `# Otsu fails on sparse images, so use Triangle`, not `# threshold`.
- Folder-level `README.md` files list the scripts in that folder with one line each. Update them when adding a script.

## Writing style

- Plain language, short sentences, UK English unless the project says otherwise.
- Units always (µm, px, s, frames).
- Keep the README "Quick start" working: if you change how something runs, update it in the same commit.
- Keep `docs/methods.md` (if present) consistent with the code, so it's ready for the paper.
