---
title: 8. Project management
nav_order: 8
permalink: /08-project-management/
---

# 8. Project management with Issues and Projects
{: .no_toc }

The same tools that track code can track your research tasks, keeping each
to-do right next to the code that does it.
{: .fs-5 }

1. TOC
{:toc}

---

## Issues as a to-do list

Your analysis repo has two **issue templates** (see `.github/ISSUE_TEMPLATE/`):

- **Analysis task**: a new analysis, with the question, images, expected
  output and how you'll check it, plus a checklist.
- **Something's not working**: a bug report that asks for the error message and version.

Good issues are **small and finishable**. "Analyse screen" is too big.
"Count puncta in plate 1 controls" is about right.

### Labels and milestones

- **Labels** group issues by type: `analysis`, `bug`, `figure`, `waiting-on-data`, `question`.
- **Milestones** group issues towards a deadline: *Lab meeting 14 Nov*, *Paper submission*.

### Linking work to issues

- In a commit message or pull request: `Fixes #12` closes issue 12 when merged.
  `Part of #12` or `See #12` links it without closing.
- In an issue comment, `#12` links to another issue, and `@username` notifies a colleague.

## A Project board

**Projects** gives you a Kanban board across one or more repositories.

1. On your GitHub profile, open **Projects → New project → Board**.
2. Name it, e.g. *Nuclear size screen*.
3. Columns: **To do**, **In progress**, **Waiting** (on data/people/equipment), **Done**.
4. Add issues from your analysis repo (and your website repo) to the board.

{: .exercise }
> 1. Create three issues in your analysis repo using the templates: one real
>    analysis task, one figure to make, and one "update website with new paper".
> 2. Create a Project board and add all three.
> 3. Move one to **In progress**, and close one with a commit that says `Fixes #N`.
>    Watch it move to **Done** automatically. (Set this under the board's
>    **Workflows** menu if it doesn't happen.)

## Using Claude for project management

Claude can help with the planning as well as the code.

- *"Here are my notes from lab meeting. Turn them into GitHub issues using the
  Analysis task template, one issue per action item, with labels."* (Route A can
  create them for you. In Route B, paste each one in yourself.)
- *"Look at the open issues in this repository and suggest what to do first for
  next week's lab meeting."*
- *"Break issue #7 into smaller issues."*
- *"Write a summary of what changed in this repository in the last month, for my PI."*
  (Claude reads the commit history, which is another reason to write good commit messages.)

## A weekly routine

| When | What |
|------|------|
| Monday | Check the board. Check for automated issues (broken links, failed weekly tests). Pull in GitHub Desktop |
| During the week | One issue at a time, small commits, `Fixes #N` |
| Friday | Push everything. Update `docs/decisions.md`. Move cards |
| Before a lab meeting | Ask Claude for a summary of the week's commits and closed issues |
