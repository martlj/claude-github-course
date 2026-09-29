---
title: Troubleshooting
parent: Reference
nav_order: 3
permalink: /reference/troubleshooting/
---

# Troubleshooting

| Problem | Likely cause and fix |
|---------|----------------------|
| My site shows a 404 | Pages isn't turned on (Settings → Pages), or the repository isn't named exactly `username.github.io`. Wait 2 minutes after the first deploy |
| My change isn't showing | Check the Actions tab: is the *pages build* still running, or red? Then hard-refresh the browser (Cmd/Ctrl+Shift+R) |
| *pages build* is red ❌ | Usually a YAML mistake in `_config.yml` or `navigation.yml`, such as a missing space after a colon or wrong indentation. Paste the error into Claude |
| The site has no styling | The CSS path is wrong, or the repository name doesn't match. The link checker will also flag this |
| Link checker fails on a link that works | The site blocks bots. Check it by hand, then add it to `.lycheeignore` |
| Claude Code can't see my repository | Add the repository to the Claude GitHub app: GitHub → Settings → Applications → Claude → Configure |
| GitHub Desktop says "rejected / fetch first" | Someone (or Claude) changed GitHub since you last pulled. **Fetch origin → Pull**, then push again |
| "Merge conflict" | The same lines changed in two places. GitHub shows both versions. Keep the right one, or ask Claude to resolve it and explain |
| Fiji: *Unrecognized command* | The command doesn't exist or needs a plugin. Use the Macro Recorder to get the exact command name |
| Standards check: "Shared standard file edited locally" | Someone changed a file in `.claude/rules/` or `.claude/skills/`. Undo it, and put project-specific exceptions in `CLAUDE.md` instead |
| Standards check: required file missing | Ask Claude to create it, e.g. *"Add a CONTRIBUTING.md from the research standards"* (or `/update-standards`) |
| Tests fail after I added a macro | Read the message. It's usually the missing header or a hard-coded path |
| I committed a data file by mistake | Remove it and add a `.gitignore` rule. If it's sensitive or large, **tell the course organiser**, because it's still in the history and needs cleaning |
