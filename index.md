---
layout: home
title: Home
nav_order: 0
permalink: /
---

# Claude + GitHub for Biologists
{: .fs-9 }

Keep your analysis code safe, shareable and reproducible, and use Claude to
do the fiddly parts. No coding experience needed.
{: .fs-6 .fw-300 }

[Start here: before the course]({{ '/01-setup/' | relative_url }}){: .btn .btn-primary .fs-5 .mb-4 .mb-md-0 .mr-2 }
[Prompt cheat-sheet]({{ '/reference/prompts/' | relative_url }}){: .btn .fs-5 .mb-4 .mb-md-0 }

---

## What you'll leave with

1. **A personal research website** at `https://YOUR-USERNAME.github.io`, which you'll change by asking Claude.
2. **An analysis repository** for your Fiji macros and Python scripts, laid out the way good computational labs do it, with automated tests.
3. **Shared standards files** that make Claude follow the same good practice in every project, for you and your collaborators.
4. **The habits behind version control**: commits, history, pull requests, issues. You'll also know how to get Claude to follow them.

## Course outline

| Module | You will… | Time |
|--------|-----------|------|
| [1. Before the course]({{ '/01-setup/' | relative_url }}) | Choose a good username, create your GitHub account, connect Claude, and (optionally) read a gentle introduction to version control | 30 min + optional reading (before the session) |
| [2. Version control]({{ '/02-version-control/' | relative_url }}) | Learn the six ideas you actually need | 20 min |
| [3. Your website]({{ '/03-website/' | relative_url }}) | Create your site from the template and make your first commit | 25 min |
| [4. Changing things with Claude]({{ '/04-prompting/' | relative_url }}) | Change colours, layout and content by describing what you want | 40 min |
| [5. Testing]({{ '/05-testing/' | relative_url }}) | Break a link on purpose and watch the automated test catch it | 25 min |
| [6. Your analysis repository]({{ '/06-analysis-repo/' | relative_url }}) | Set up a repository for your macros and scripts | 30 min |
| [7. Standards files]({{ '/07-standards-files/' | relative_url }}) | Learn how a few Markdown files make Claude follow good practice, in every project and for every collaborator | 40 min |
| [8. Image analysis with Claude]({{ '/08-image-analysis/' | relative_url }}) | Write and test a Fiji macro together with Claude | 45 min |
| [9. Project management]({{ '/09-project-management/' | relative_url }}) | Track your work with Issues and a Project board | 25 min |

Modules 1–5 make a good first half-day session, and 6–9 a second.

{: .concept }
> Throughout the course you make changes **by asking Claude**. You won't need to
> learn HTML, CSS or programming. Your job is to say clearly what you want, check
> the result, and keep a clean record of what changed and why. Git and GitHub
> make that record possible. **Claude writes the code, and you stay the scientist.**

## Two ways to work with Claude

The exercises show both routes. Use whichever one you have access to.

| | **Route A: Claude Code** | **Route B: Claude chat + GitHub editor** |
|---|---|---|
| Where | [claude.ai/code](https://claude.ai/code) or the *Code* tab in the Claude desktop app | [claude.ai](https://claude.ai) chat, and GitHub's website |
| How it works | Claude opens your repository, edits the files, commits, and offers you a pull request | You paste a file into chat, Claude gives back a changed version, you paste it into GitHub and commit |
| Good for | Changes to several files; anything with tests | Learning exactly what changed; small edits |
