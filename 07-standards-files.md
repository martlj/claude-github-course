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
[research-standards](https://github.com/martlj/research-standards) repository.
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
| `/propose-standards-change` | Drafts a suggestion for improving the standards themselves (exercise 4) |

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
- **Improvements spread.** Anyone can propose a change ([exercise 4](#exercise-4-propose-a-change-to-the-standards)).
  When a new version is released, every project's weekly **Standards** check opens an
  issue: *"Research standards vX available"*. Reply with `/update-standards`, and
  Claude shows what changed and opens a pull request.

### Starting a new project, or rescuing an old one

- **New project:** start from a template. The standards are already there.
- **Existing repository or folder of macros:**

  > Install the research standards from https://github.com/martlj/research-standards
  > into this repository with the "analysis" profile. Then run /apply-standards and
  > show me the plan before changing anything.

## Writing good instructions

| ❌ Vague | ✅ Specific and checkable |
|---------|--------------------------|
| Write good code. | Every function has a docstring stating parameter units. |
| Be careful with data. | Never commit files in `data/` except `data/README.md` and `data/sample/`. |
| Use best practice for thresholds. | Use a named automatic method (Otsu, Triangle…) and log the choice in `docs/decisions.md`. |

- **Short.** Every line is read in every session.
- **Say why** when it isn't obvious. Claude applies a rule better when it knows the reason.
- **Checkable.** If possible, back the rule with an automated check, like the macro header test.

## Exercise 4: propose a change to the standards

The standards aren't fixed. They're meant to improve as people use them, and
**you** are the people who know where they help and where they get in the way.
In this exercise everyone drafts and submits at least one proposal.

{: .concept }
> **Not every proposal is accepted, and that's fine.** The maintainers may accept
> it, adapt it, suggest it belongs in your project's `CLAUDE.md` instead, keep it
> for later, or decline it with a reason. Each outcome is recorded on the issue, so
> the next person with the same idea can see the discussion.

### 1. Pick an idea

Think about your own work. What would you like every project to do the same way?
What has gone wrong before? Some starting points:

| Area | Questions to ask yourself |
|------|---------------------------|
| **File naming** | Should image files follow a pattern such as `2026-09-29_HeLa_siRNA-KD_rep2_fov03.czi`? Dates as `YYYY-MM-DD`? No spaces? Zero-padded numbers (`plate_03`, not `plate_3`)? |
| **Folder layout** | How should raw data be organised on storage, and what should `data/README.md` always record? |
| **Templates for other software** | Do you use R/Quarto, CellProfiler, QuPath, napari, MATLAB, Imaris, Snakemake or Nextflow? What would a good starter repository for that tool contain? |
| **Metadata** | Which fields should every sample sheet have? Should published images carry REMBI/OME metadata? |
| **Statistics and figures** | Should Claude always ask what *n* is (cells, fields or biological replicates)? Require scale bars on every micrograph? Colour-blind-safe palettes? |
| **Data sharing** | When and where to deposit images (BioImage Archive, IDR, Zenodo)? A standard data availability statement? |
| **Checks** | Is there a mistake the automated checks should catch, such as passwords committed by accident or notebooks saved with outputs? |
| **Claude's behaviour** | Does Claude ask too many questions, or too few? Explain too much, or not enough? |
| **Removal** | Is there a rule that got in your way and doesn't earn its place? Proposing to *remove* something is just as valuable. |

### 2. Draft it with Claude

In any repository that has the standards (your analysis repository is ideal), ask:

> /propose-standards-change I think every project should use the same naming
> pattern for raw image files, because in my last project we couldn't tell
> which files were replicates.

Claude will:

1. ask what prompted the idea (a concrete example makes a proposal much stronger);
2. check whether the standards already cover it, and quote the relevant rule if so;
3. help you decide whether it's a **shared** standard, or better as an **exception** in your
   project's `CLAUDE.md`;
4. draft the proposal: summary, motivation, proposed wording, who it affects, whether it could
   be checked automatically, and the downsides;
5. submit it as an issue on the `research-standards` repository, or give you the text and
   the link to the *Propose a change* form.

**Route B:** paste your idea into your claude.ai Project (which has the standards bundle)
with *"Help me write a proposal to change our research standards"*, then paste the result into
the *Propose a change* form on the `research-standards` repository's **Issues** tab.

{: .exercise }
> 1. Submit at least one proposal. Aim for a mix across the room: at least one new rule, one
>    template for another tool, and one removal or relaxation.
> 2. Read two other people's proposals on the **Issues** tab. Add a 👍 reaction if you'd
>    want it, or a comment with a concrete example, a concern, or an improvement to the wording.
> 3. Discuss as a group: which proposals are *general* (good for everyone), and which are
>    really *project exceptions*?

{: .tip }
A good proposal is **specific** (the exact wording, not "better file names"),
**motivated** (a real example of the problem) and **honest about costs** (more work? does it
conflict with anything?). Claude's draft will prompt you for all three.

## Aside: behind the scenes, how proposals are reviewed

{: .note }
> This part is the **maintainers'** job, not yours. It's here so you know what happens
> to your proposal after you press *Submit*. The full process is in
> [`MAINTAINING.md`](https://github.com/martlj/research-standards/blob/main/MAINTAINING.md).

```
 your proposal ──► triage ──► discussion (if needed) ──► decision
                                                           │
     ┌───────────────┬──────────────────┬─────────────┬────┴──────┐
  accepted    project-exception       later        declined    duplicate
     │
  pull request ──► review ──► merge ──► new release ──► every project gets an "update available" issue
```

1. **Triage.** A maintainer reads the proposal and asks: Is the problem real and clear? Is it
   already covered? Is it general enough for everyone? Can it be checked automatically? Is it
   worth the cost? (Every line of a rule is read in every Claude session, so shorter is better.)
2. **Label and reply.** Each proposal gets a label, such as `accepted`, `project-exception`,
   `later`, `declined` or `duplicate`, and **always a reason**. The maintainer might also ask
   you a question (`needs-info`).
3. **Implement.** For accepted proposals, the maintainer asks Claude to make the change on a
   branch, and reviews the pull request against a checklist. It needs to be general, short and
   checkable, not conflict with other rules, and have the listings and changelog updated. You
   may be asked to review it too.
4. **Release.** Accepted changes are grouped into a new version (e.g. v1.2.0) and tagged. Within
   a week, every project's **Standards** check opens an *"update available"* issue, and
   `/update-standards` brings the change in. That includes the proposer's own projects, so your
   idea comes back to you as a pull request.

{: .exercise }
> **Instructor demo (10 min):** the instructor picks two or three proposals from the room
> and reviews them live: one to accept, one to redirect to a project `CLAUDE.md`, and one to
> decline or park. For the accepted one, they ask Claude to implement it and show the pull
> request, the checks, and the release.

## Route B: Claude chat

Claude chat doesn't read repository files by itself. Set up a **claude.ai
Project** once, using the kit's [chat setup guide](https://github.com/martlj/research-standards/blob/main/docs/claude-chat-setup.md):
upload `standards-for-claude-chat.md` (all the rules and procedures in one file)
and your project's `CLAUDE.md`, and paste in the suggested project instructions.
Share the Project with collaborators.
