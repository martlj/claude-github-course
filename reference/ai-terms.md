---
title: AI terms cheat-sheet
parent: Reference
nav_order: 2
permalink: /reference/ai-terms/
---

# AI terms cheat-sheet
{: .no_toc }

What the jargon means, in plain language, and what it means for you at the bench.
{: .fs-5 }

1. TOC
{:toc}

---

## The one idea everything else hangs off

Claude has no memory of you between conversations. Each time you start a new
chat, it begins from nothing. Everything it knows about your work in that moment
is the text sitting in front of it: your messages, the files it has read, and
any instruction files in your repository.

{: .concept }
> **Think of a rotating bench visitor.** Every morning a very capable, very
> well-read scientist arrives who has never met you, never seen your project,
> and remembers nothing from yesterday. They can read anything you put in front
> of them, and they work fast. Your job is to brief them well. `CLAUDE.md` and the
> shared rules are the standing briefing note you don't want to rewrite each morning.

Almost every confusing thing about working with AI follows from this. "Why did it
forget?" "Why did it do it differently this time?" "Why does it need the file
again?" Because the briefing changed.

---

## Tokens and context

### Token

The unit AI models read and write in. Roughly a word or a chunk of one: common
words are one token, longer or unusual words split into several.

**Rule of thumb:** 1 token ≈ ¾ of a word in English. So 1,000 tokens ≈ 750 words
≈ 1.5 pages. Code and file paths use more tokens per line than prose, because
punctuation and symbols split up.

You don't need to count tokens. You just need to know they're the unit of
"how much" — of how much fits in, and of what you're charged or rate-limited on.

### Context window

The total amount of text a model can hold at once: your messages, its replies,
and every file it has read, all together. Measured in tokens.

Current Claude models have large windows (Opus and Sonnet hold about a million
tokens, which is thousands of pages), so in normal use you're unlikely to hit it.
But it is finite, and it fills up with everything, including large files and long
outputs.

{: .tip }
**Signs the context is full or cluttered:** Claude starts forgetting what you
agreed earlier in the same conversation, repeats itself, or contradicts a decision
from twenty messages ago. The fix is simple: start a new conversation and give it
a short summary of where you got to. Nothing is lost, because the real record of
your work is in Git.

### Context (the word on its own)

Everything Claude can currently see. "It doesn't have that in context" means it
hasn't been shown the file. "Adding it to context" means pasting it in, attaching
it, or letting Claude read it from the repository.

{: .warning }
In **Route B** (Claude chat, without your repository connected), Claude only sees
what you paste. If you ask it to change a page and it doesn't know about the menu
file, it can't update the menu. Paste everything relevant, or ask *"which files do
you need to see?"*

### Session / conversation

One continuous chat. Context lasts for the session. When you start a new one, you
start from a blank briefing again.

---

## Models and versions

### Model

The AI itself. Different models have different capability, speed and cost.

### How the names work

Claude models come in families, named from most to least capable:

| Family | What it's for |
|--------|---------------|
| **Opus** | Hardest work: long multi-step tasks, tricky code, careful reasoning |
| **Sonnet** | The everyday workhorse: fast, and strong enough for most tasks |
| **Haiku** | Quick, cheap, simple jobs |

Each family carries a version number that goes up over time (Sonnet 4 → 4.5 → 5 →
5.5). Higher is newer and generally better. Other families appear from time to
time; the documentation linked below always has the full current list. A dated suffix like
`claude-haiku-4-5-20251001` names one exact frozen version, which matters if you
need results to be reproducible.

{: .note }
Model names and numbers change every few months. The live list is at
[the Claude models documentation](https://platform.claude.com/docs/en/models/overview).
Don't memorise version numbers. Do understand the Opus / Sonnet / Haiku pattern,
because that's the choice you'll actually make.

**Which to use for this course?** Whatever your Claude plan gives you by default is
fine. If a task is long and fiddly (a whole analysis pipeline) and you have the
choice, pick the most capable model available. For "change this colour", any
model will do.

### Knowledge cutoff

The date the model's training data stops. It knows nothing later than that from
memory. If you ask about a Fiji plugin released last month, it may not know it
exists, or may guess.

**This is why Claude searches the web** for anything current, and why you should
ask it to. *"Search for the current documentation before you answer"* is a useful
instruction.

### Reasoning / thinking

Some models can work through a problem step by step before answering. It's slower
but better for hard problems. You'll sometimes see this as "thinking" in the
interface. Asking *"think it through before you answer"* often improves results.

---

## Prompts: good and bad

A **prompt** is simply what you ask. Prompt quality is the single biggest thing
under your control.

### The pattern that works

A good prompt usually has four parts. Not every prompt needs all four, but the
more of them you include, the better the result:

1. **Context:** what this is and why. *"This is a Fiji macro for counting nuclei in DAPI images."*
2. **Task:** what you want, specifically. *"Add an option to exclude nuclei touching the image border."*
3. **Constraints:** what must not change, or must be true. *"Don't change the existing default behaviour. Keep the macro runnable headless."*
4. **Check:** how you'll know it worked. *"Run it on data/sample and tell me how the count changes."*

### Side by side

| ❌ Weak prompt | ✅ Better prompt | Why |
|---------------|-----------------|-----|
| "Make my website nicer." | "Make the header more compact and use a warmer colour scheme. Show me three options before changing anything." | Vague requests get arbitrary results. Asking for options keeps you deciding |
| "Fix the analysis." | "The macro counts 200 nuclei in an image where I counted 150 by hand. Debris is being included. Suggest what's wrong before changing anything." | Says what's wrong, gives evidence, asks for diagnosis first |
| "Count the cells in my images." | "2D confocal, 3 channels (DAPI/GFP/mCherry), 0.108 µm/px, .czi files. I want nuclei counts per image as a CSV. Some nuclei touch. How would you approach this?" | The details change the answer completely |
| "Write a script to analyse this." | "/start-analysis" then answer its questions | The skill knows which questions matter |
| "Is this right?" | "Compare this macro's output with my hand counts in counts.csv and tell me where they disagree most." | Gives something concrete to check against |
| "Add my papers." | "Add these papers to publications.md: [DOIs]. Look each one up and tell me if you can't verify the details." | Invites Claude to admit uncertainty rather than invent |

### Phrases worth keeping in your pocket

- *"Before changing anything, tell me your plan and which files you'll touch."*
- *"Make only this change. Don't touch anything else."*
- *"Explain what you changed, file by file, in plain language."*
- *"What assumptions does this make about my images? When would it give wrong answers?"*
- *"What would you check to convince yourself this is correct?"*
- *"I don't understand X. Explain it as if I've never programmed."*
- *"That's not right because […]. Try again."* — correcting is normal, not failure.

{: .warning }
**Don't ask leading questions about results.** *"This shows a significant effect,
doesn't it?"* invites agreement. Ask *"what does this output actually show?"*
instead. AI models tend to go along with what you seem to want, which is exactly
what you don't want from an analysis.

### Iterating

Nobody writes the perfect prompt first time. The loop is: ask → look at what you
got → say what's wrong → repeat. Two or three rounds is normal and quick.

If it's going badly after a few rounds, **start a new conversation** rather than
pushing on. A cluttered conversation with three abandoned approaches in it tends
to produce muddled results.

---

## The Markdown files

Markdown (`.md`) is plain text with light formatting. It's used for instructions
to Claude because both people and machines can read it. Here are the ones you'll meet:

| File | Who reads it | What it's for |
|------|--------------|---------------|
| `README.md` | People (and Claude) | What the project is and how to run it. The front page on GitHub |
| `CLAUDE.md` | Claude, every session | Facts about **this** project, and deliberate exceptions to the shared rules. Keep it short |
| `CLAUDE.local.md` | Claude, on your machine only | Your personal preferences. Git ignores it, so it isn't shared |
| `.claude/rules/*.md` | Claude, automatically | The shared lab standards. Some load only for matching file types |
| `.claude/skills/*/SKILL.md` | Claude, when relevant or when you type `/name` | Step-by-step procedures for common jobs |
| `STANDARDS.md` | People | Human-readable summary of the shared standards |
| `CONTRIBUTING.md` | People | How collaborators work on the project |
| `CHANGELOG.md` | People | What changed, by version |
| `docs/decisions.md` | People (written by Claude) | Dated record of analysis decisions and why |
| `AGENTS.md` | Some AI tools | An emerging cross-tool equivalent of `CLAUDE.md`. You may see it in other people's repositories |

{: .concept }
> **Three layers of instruction.** Shared rules say *how we work* (same in every
> project). `CLAUDE.md` says *what this project is* (written per project).
> `CLAUDE.local.md` says *how I like to work* (just you). Module 7 covers this in full.

### Front matter

The block between `---` lines at the top of a Markdown file. It holds settings
rather than content — a page title, or which file types a rule applies to. YAML
format, so indentation and the space after each colon matter.

---

## Memory, context and knowledge: what persists where

This is the most common source of confusion. Four different things sound similar:

| Thing | Lasts | Shared with others? | Claude sees it… |
|-------|-------|--------------------|-----------------|
| **Context** (this conversation) | Until you close the chat | No | Always, within the session |
| **Instruction files** (`CLAUDE.md`, rules, skills) | Permanently, in the repository | Yes, with everyone on the project | At the start of every session in that repository |
| **Project knowledge** (a claude.ai Project) | Until you change it | With anyone you share the Project with | In every chat inside that Project |
| **Memory** (if your Claude has it turned on) | Across conversations | No, it's personal | Automatically, where available |

**What this means in practice:** if you want Claude to behave the same way next
week, or for your collaborator, **write it in a file in the repository**. Don't
rely on having told it once in a chat.

### Project (claude.ai)

A folder in claude.ai chat holding several conversations plus shared knowledge
(uploaded files and standing instructions). Used in **Route B** to give Claude
chat your standards without a repository connection.

---

## Where things go wrong

### Hallucination / confabulation

The model states something false with complete confidence. Most often: invented
references and DOIs, Fiji commands or plugin names that don't exist, function
arguments that were never in the library, and plausible-looking numbers.

{: .warning }
> **It is not lying and it is not broken.** It is producing likely-looking text,
> and sometimes likely-looking is wrong. This is why the course insists on:
> checking every citation yourself, running code before believing it, and testing
> against data with a known answer.

### Fluency ≠ correctness

A confident, well-written, well-organised answer is not evidence of a correct
answer. This is genuinely hard to internalise, because with people the two usually
go together.

### Going along with you (sycophancy)

If you push back, models often cave, even when they were right. If you hint at the
answer you want, they tend to produce it. Guard against this by asking neutral
questions and by checking against data rather than argument.

### Doing more than you asked

Claude may "helpfully" tidy unrelated code in the same change. This is why you read
the diff before merging, and why the rules tell it to make the smallest change that
does the job.

### Non-determinism

Ask the same question twice, get two slightly different answers. Normal. It's also
why *the code* is the reproducible artefact, not the conversation, and why analysis
code gets version-tagged for a paper.

### Stale knowledge

See *knowledge cutoff* above. Software, menus and best practice move on. Ask
Claude to search rather than recall, for anything current.

---

## Agents, tools and connections

### Agent / agentic

An AI that doesn't just reply, but takes actions in a loop: reads a file, runs a
command, looks at the result, decides what to do next. Claude Code works this way,
which is why it can actually edit your repository rather than just tell you what to type.

### Tool / tool use

An action the model can take beyond writing text: read a file, search the web, run
a script, open a pull request. When you see Claude "reading" your files, that's a tool.

### Skill

A written procedure Claude follows for a recurring job, stored as a `SKILL.md` file.
Yours are in `.claude/skills/`. Claude picks the right one when your request matches
its description, or you invoke it by name with `/start-analysis`.

### MCP / connector

A standard way of plugging an AI into another system: GitHub, a database, an image
repository like OMERO. Someone sets it up once, and then Claude can work with that
system directly. You'll mostly meet this as "connect GitHub to Claude".

### Claude Code vs Claude chat

| | Claude Code | Claude chat |
|---|---|---|
| Sees your repository | Yes, directly | Only what you paste or upload |
| Reads `CLAUDE.md`, rules and skills automatically | Yes | No — use a claude.ai Project instead |
| Makes changes | Edits files, commits, opens pull requests | Gives you text to paste |
| Where | claude.ai/code, desktop app, or terminal | claude.ai |

This is the Route A / Route B distinction used throughout the course.

---

## Usage and cost

### Rate limit / usage limit

A cap on how much you can use in a period. On a team plan you'll usually only meet
it during a heavy session. Reading very large files and running long agentic tasks
uses much more than a quick question.

### Why prompts affect cost

Everything in context is re-read on every turn. A conversation where Claude has read
twenty large files costs more per message than a fresh one. Another reason to start
a new conversation for a new task.

---

## Data, privacy and integrity

{: .warning }
> **Before sharing data with any AI tool, check your institute's policy.** As a
> default for this course: no personal or patient-identifiable data, no
> unpublished collaborator data, no credentials. Code, public data and synthetic
> examples are fine. If you're unsure, ask before uploading.

### Attribution and honesty

- Using AI to write analysis code is a tool choice, like using Fiji. You still own the results.
- Check what journals and funders require about declaring AI use. Policies vary and change.
- Your `docs/decisions.md` and Git history are your record of what was done and why — which is a better answer to "how was this analysed?" than any memory of a chat.
- Never present AI-generated text or figures as verified when you haven't verified them.

---

## Thirty-second summary

1. **No memory between chats.** Put anything that should persist in a file.
2. **Context is everything it can see.** If it doesn't know, it probably wasn't shown.
3. **Tokens** are the unit of how much. Roughly ¾ of a word each.
4. **Opus / Sonnet / Haiku** = most capable / balanced / fastest. Numbers go up over time.
5. **Good prompts** give context, a specific task, constraints, and a way to check.
6. **Confident ≠ correct.** Verify citations, run the code, test against known answers.
7. **Ask for a plan first** on anything non-trivial, and **read the diff** before merging.
8. **Start a new conversation** when things get muddled. Git holds the real record.

---

*See also: the [prompt cheat-sheet]({{ '/reference/prompts/' | relative_url }}) for
copy-paste prompts, the [glossary]({{ '/reference/glossary/' | relative_url }}) for
Git and GitHub terms, and [module 7]({{ '/07-standards-files/' | relative_url }}) for
the instruction files in detail.*
