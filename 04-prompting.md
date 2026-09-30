---
title: 4. Changing things with Claude
nav_order: 4
permalink: /04-prompting/
---

# 4. Changing things with Claude
{: .no_toc }

Describe the change you want, let Claude make it, check the diff, commit.
{: .fs-5 }

1. TOC
{:toc}

---

## The loop

```
  Describe  ──►  Claude edits  ──►  You review the diff  ──►  Commit / merge  ──►  Check the live site
     ▲                                                                                       │
     └───────────────────────────────  not quite right? say what's wrong  ◄──────────────────┘
```

{: .concept }
> **You're responsible for what gets committed**, not Claude. Always look at the
> diff before you merge. After a few rounds you'll start to recognise which
> changes are safe and which need a closer look.

## Route A: Claude Code

1. Open [claude.ai/code](https://claude.ai/code) (or the **Code** tab in the desktop app).
2. Select your `YOUR-USERNAME.github.io` repository. If it isn't listed, add it to
   the repositories the Claude GitHub app may access.
3. Type your request (see the exercises below) and send it.
4. Claude reads the repository, including `CLAUDE.md` and the shared rules in `.claude/`, makes the change on a new
   **branch**, and explains what it did.
5. Review the changes it shows you. When you're happy, ask it to **create a pull request**
   (or click the button offered).
6. On GitHub, open the pull request, check the **Files changed** tab, wait for the
   link checker to go green ✅, then click **Merge pull request**.

## Route B: Claude chat + GitHub editor

1. On GitHub, open the file you want to change (e.g. `assets/css/style.css`) and
   click the **copy raw file** icon.
2. In [claude.ai](https://claude.ai), paste it with your request:

   > Here is the CSS file for my Jekyll website. Change the background to a very
   > pale blue and make the links dark blue. Give me back the complete updated file
   > and list exactly which lines you changed.

3. Back on GitHub, click the pencil ✏️, select everything, paste Claude's version.
4. Click **Commit changes…**. This time choose **Create a new branch** and
   **Propose changes**. This opens a pull request, so the tests run first.
5. Check **Files changed**. Only the lines Claude listed should differ. Then merge.

{: .warning }
In Route B, Claude only sees what you paste. If a change involves several
files (e.g. adding a page *and* its menu entry), paste all of them, or ask
Claude which files it needs to see.

---

## Exercises

Do them in order. Each one teaches a different kind of change.

### 1. Change the background colour

> Change the website background to a very pale blue-grey, and make the
> header underline and links a dark teal that goes with it. Keep the text
> easy to read.

**Check:** the diff should only touch the variables at the top of
`style.css`. Why? Because a rule tells Claude to use them. Open
`.claude/rules/topic-websites.md` and find it. There's more about these rule files in
[module 7]({{ '/07-standards-files/' | relative_url }}).

### 2. Change the fonts and layout

> Use a sans-serif font for headings too, make the main text column a bit
> wider, and put a little more space between paragraphs.

### 3. Add a new page

> Add a "Teaching" page listing two courses I've taught (placeholder text is
> fine for now) and add it to the menu between Publications and Code.

**Check:** this change should touch *two* files: a new `teaching.md` and
`_data/navigation.yml`. Why does it need both?

### 4. Add real content

> Add these papers to my publications page, newest first, bolding my name
> (J. Smith): 10.1038/s41586-020-2649-2, 10.7554/eLife.xxxxx

{: .warning }
Claude may not be able to look up a paper from its DOI, and it can get details
wrong. **Check every author list, year and journal** against the real paper.
Never publish a publication list you haven't verified.

### 5. Replace the profile picture

Upload a photo: on GitHub, go to `assets/img/`, then **Add file → Upload files**.
Then ask:

> I've uploaded my photo as assets/img/jane.jpg. Use it as the profile picture
> instead of profile.svg, with suitable alt text.

### 6. Your choice

Ideas: a dark-mode version, a "News" section, a two-column layout on wide
screens, an embedded map to your institute, a table of lab members.

---

## Prompting well

{: .tip }
The [AI terms cheat-sheet]({{ '/reference/ai-terms/' | relative_url }}) explains
tokens, context, model versions and memory, and has a longer side-by-side of weak
and strong prompts. Worth ten minutes at some point.


| Instead of… | Try… | Why |
|-------------|------|-----|
| "Make it look nicer" | "Make the header more compact and use a warmer colour scheme. Show me 3 options first." | Vague requests get random results. Asking for options keeps you in charge |
| "Fix the website" | "The menu overlaps the title on my phone. Fix it without changing the desktop layout." | Say what's wrong, where, and what must stay the same |
| One giant request | One change per request | Small changes are easy to review, and easy to undo |
| Accepting the first answer | "That's too dark. Go lighter, and explain which line controls it." | Iterating is normal, and asking *why* is how you learn |

Useful phrases:

- *"Explain what you changed, file by file, in plain language."*
- *"Don't change anything else."*
- *"Before changing anything, tell me your plan."*
- *"What would you check to make sure this works?"*

## Undoing a change

- **Before merging:** just close the pull request. Nothing reaches `main`.
- **After merging:** open the merged pull request and click **Revert**. GitHub
  creates a new pull request that undoes it. The history keeps both, which is
  what you want: nothing is ever lost.
- **Route A:** you can simply ask *"Undo the last change you made to the menu."*
