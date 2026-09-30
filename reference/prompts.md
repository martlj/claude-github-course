---
title: Prompt cheat-sheet
parent: Reference
nav_order: 1
permalink: /reference/prompts/
---

# Prompt cheat-sheet

Copy, paste, adapt. For what the jargon means, see the
[AI terms cheat-sheet]({{ '/reference/ai-terms/' | relative_url }}).

## Skills (Claude Code: type `/` to see them all)

`/start-analysis` · `/new-fiji-macro` · `/new-python-script` · `/add-known-answer-test` ·
`/log-decision` · `/review-changes` · `/prepare-release` · `/apply-standards` ·
`/update-standards` · `/progress-summary` · `/propose-standards-change`

## Getting started in a repository

- *Read the README and CLAUDE.md and summarise what this repository does and its rules.*
- *Explain the folder structure to me as if I've never programmed.*
- *What standards are you following here, and where do they come from?*
- *Install the research standards into this repository with the analysis profile, then /apply-standards.*
- *Add an exception to CLAUDE.md: …*
- */propose-standards-change I think every project should …*

## Asking for a change

- *Before changing anything, tell me your plan and which files you'll touch.*
- *Make only this change. Don't touch anything else.*
- *Explain what you changed, file by file, in plain language.*
- *Give me 3 options with a short description of each, and don't change anything yet.*

## Website

- *Change the colour scheme to [description]. Keep the contrast accessible.*
- *Add a [name] page with [content] and put it in the menu after [page].*
- *The site looks wrong on my phone: [describe]. Fix it without changing the desktop layout.*
- *Fix the broken links in issue #N and close the issue in the commit message.*

## Image analysis

- *Here's what my images are: [dimensions, channels, pixel size, format]. I want [output]. Propose an approach, don't write code yet.*
- *Turn this Macro Recorder output into a macro following CLAUDE.md conventions.*
- *What assumptions does this macro make? When would it give wrong results?*
- *Add a step that saves the segmentation outlines overlaid on the original so I can check them.*
- *Make a synthetic test image with a known answer and a test that checks it.*
- *Fiji says: [paste error]. What's wrong?*

## Git and GitHub

- *Write a commit message for these changes.*
- *Undo the last change you made to [file].*
- *The tests failed on my pull request. Explain why in plain language, and fix it.*
- *What changed in this repository since [date]? Summarise for my PI.*

## Project management

- *Turn these meeting notes into GitHub issues, one per action item.*
- *Break issue #N into smaller steps.*
- *Draft a CHANGELOG entry and a release note for version 1.1.0.*
