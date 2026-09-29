# Notes for Claude

This repository is a course website (Jekyll, Just the Docs remote theme,
GitHub Pages "deploy from a branch") that teaches biologists with no coding
background to use Git, GitHub and Claude.

- Audience: bench scientists. Use plain language, UK English, short sentences, and explain jargon on first use or link to `reference/glossary.md`.
- Each module page has front matter (`title`, `nav_order`, `permalink`). Keep numbering consistent across pages, `index.md` and the outline table.
- Internal links use `{{ '/permalink/' | relative_url }}` so they work under the `baseurl`.
- Callouts: `{: .note }`, `{: .tip }`, `{: .warning }`, `{: .exercise }`, `{: .concept }` on the line before a paragraph or `>` block.
- Every exercise should offer Route A (Claude Code) and Route B (Claude chat + GitHub web editor) where they differ.
- Keep instructions in step with the two template repositories (file names, folder layout, test names).
- Don't describe UI details you're unsure of as certain. Menus change, so prefer "look for…" wording.
- Link checking runs in `.github/workflows/check-links.yml`. Don't add real sites to `.lycheeignore` to hide failures.
