---
title: 7. Standards files
nav_order: 7
permalink: /07-standards-files/
---

# 7. Standards files: teaching Claude your lab's rules
{: .no_toc }

A handful of Markdown files make Claude follow the same good practice in
every project, for everyone who works on it.
{: .fs-5 }

1. TOC
{:toc}

---

## The problem

Every Claude session starts fresh. Without instructions, Claude has to guess:
Where do macros go? Should it commit straight to `main`? Is it fine to hard-code
that path? Should it write a test? Different people asking in different ways
get different answers, and a shared project slowly turns into a mess.

## The solution: instruction files

Claude Code automatically reads certain Markdown files in a repository **before
it does anything**. They work like the SOPs and protocol book of a lab.

| File | Lab equivalent | Read | Shared? |
|------|----------------|------|---------|
| `.claude/rules/*.md` | Institute SOPs | Every session. Some rules only load when working on matching files (e.g. the Fiji rules only for `.ijm` files) | ✅ Identical in every project |
| `.claude/skills/*/SKILL.md` | Step-by-step protocols | When your request matches, or when you type `/name` | ✅ Identical in every project |
| `CLAUDE.md` | The project's page in the lab book | Every session | ✅ With everyone on *this* project |
| `CLAUDE.local.md` | Your own bench notes | Every session, on your machine only | ❌ Just you (Git ignores it) |

{: .concept }
> **Three layers.** The shared standards say *how we work*. `CLAUDE.md` says
> *what this project is* and any *deliberate exceptions*. `CLAUDE.local.md`
> says *how I like to work*. Only the middle one is written per project, which
> is why it should stay short.

## The research-standards kit

All our templates come with the same kit already installed, from the
[research-standards](https://github.com/YOUR-ORG/research-standards) repository.
Open `STANDARDS.md` in your analysis repository for the overview.

**Rules (always on):** working with researchers · Git and GitHub · data management ·
reproducibility · testing · documentation · scientific integrity

**Rules (only for matching files):** Fiji macros · Python · R · image analysis · websites

**Skills (type `/` in Claude Code to list them):**

| Skill | What it does |
|-------|--------------|
| `/start-analysis` | Interviews you about a new analysis and records the plan as an issue. No code yet |
| `/new-fiji-macro` | Writes a macro with header, parameters, CSV and QC outputs, and a test |
| `/new-python-script` | The same for Python, with tests |
| `/add-known-answer-test` | Adds a test against data with a known answer |
| `/log-decision` | Records a threshold or parameter decision in `docs/decisions.md` |
| `/review-changes` | Checks a pull request against the standards before you merge |
| `/prepare-release` | Tags the exact version used for a paper |
| `/apply-standards` | Audits an old or messy project and plans how to tidy it |
| `/update-standards` | Installs the latest version of the standards |
| `/progress-summary` | Summarises recent work for your PI |

You rarely need to type the names. *"I want to count puncta per cell"* is
enough for Claude to pick `start-analysis` by itself.

## Exercise 1: see the rules at work

{: .exercise }
> In your **analysis repository** (Route A), ask:
>
> > What standards are you following in this repository, and where do they come from?
>
> Then ask for something the rules cover:
>
> > Write a quick macro that measures the mean intensity of every image in a folder.
>
> Look at what Claude does *without being told*: a branch, the header block, `#@`
> parameters instead of a hard-coded path, a CSV output, an entry in
> `fiji/README.md`, a question about your images before it starts. Find the rule
> file behind each behaviour.
>
> **Compare:** ask the same thing in a plain Claude chat with no project or files.
> What's different?

## Exercise 2: fill in your project's CLAUDE.md

{: .exercise }
> > Interview me to fill in the ✏️ placeholders in CLAUDE.md. Ask one group of
> > questions at a time, and don't guess.
>
> Review the pull request. The **Standards** check shows a ⚠️ warning while
> placeholders remain, and it disappears once they're filled.

## Exercise 3: a skill from start to finish

{: .exercise }
> 1. `/start-analysis`: describe a real analysis you need. Claude interviews you and opens an issue.
> 2. Ask Claude to go ahead. It follows `new-fiji-macro` or `new-python-script`.
> 3. `/log-decision`: record why you chose the threshold method.
> 4. `/review-changes`: Claude reviews its own pull request against the checklist. Read the ✅/⚠️/❌ list.
>    Would you have spotted the ⚠️ items yourself?

## Exceptions go in CLAUDE.md, not in the rules

Sometimes a project needs to break a rule. Your website's `CLAUDE.md`, for
example, allows small text edits straight to `main`.

{: .exercise }
> Try it the wrong way first. On a branch, ask Claude to edit
> `.claude/rules/02-git-and-github.md` to allow direct commits. The
> **Standards** check warns *"Shared standard file edited locally"*. Close that
> pull request, and instead ask:
>
> > Add an exception to CLAUDE.md: in this repository, typo fixes can go straight to main.

Why does it matter? If everyone edits the shared rules, the projects drift apart
and the next update overwrites the edits. Exceptions in `CLAUDE.md` are visible,
explained, and survive updates.

## Collaborating with the same standards

Because every project carries the same files:

- **A collaborator's Claude behaves like yours.** Whoever opens a pull request,
  it arrives with the same structure, tests and documentation.
- **Reviews are easier.** Everyone knows what a good pull request looks like
  (`CONTRIBUTING.md`, and the pull-request template checklist).
- **Moving between projects is painless.** Same folders, same skills, same checks.
- **Improvements spread.** Suggest a change by opening an issue on the
  research-standards repository. When a new version is released, every project's
  weekly **Standards** check opens an issue: *"Research standards vX available"*.
  Reply with `/update-standards` and Claude shows what changed and opens a pull request.

### Starting a new project, or rescuing an old one

- **New project:** start from a template. The standards are already there.
- **Existing repository or folder of macros:**

  > Install the research standards from https://github.com/YOUR-ORG/research-standards
  > into this repository with the "analysis" profile. Then run /apply-standards and
  > show me the plan before changing anything.

## Route B: Claude chat

Claude chat doesn't read repository files by itself. Set up a **claude.ai
Project** once, using the kit's [chat setup guide](https://github.com/YOUR-ORG/research-standards/blob/main/docs/claude-chat-setup.md):
upload `standards-for-claude-chat.md` (all the rules and procedures in one file)
and your project's `CLAUDE.md`, and paste in the suggested project instructions.
Share the Project with collaborators.

## Writing good instructions (for when you propose one)

| ❌ Vague | ✅ Specific and checkable |
|---------|--------------------------|
| Write good code. | Every function has a docstring stating parameter units. |
| Be careful with data. | Never commit files in `data/` except `data/README.md` and `data/sample/`. |
| Use best practice for thresholds. | Use a named automatic method (Otsu, Triangle…) and log the choice in `docs/decisions.md`. |

- **Short.** Every line is read in every session.
- **Say why** when it isn't obvious. Claude applies a rule better when it knows the reason.
- **Checkable.** If possible, back the rule with an automated check, like the macro header test.
