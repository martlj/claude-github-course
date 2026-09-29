---
title: 6. Your analysis repository
nav_order: 6
permalink: /06-analysis-repo/
---

# 6. Your analysis repository
{: .no_toc }

A home for your Fiji macros, Python scripts and notebooks, laid out so that
someone else (or you, in three years) can understand and rerun them.
{: .fs-5 }

1. TOC
{:toc}

---

## Why a separate repository?

| | Website repo | Analysis repo |
|---|---|---|
| Visibility | Must be **public** | Can be **private** until you publish |
| Contents | About you | About one project |
| How many | One per person | **One per project/paper** is ideal (plus maybe a personal "toolbox") |

{: .note }
Private repositories are free on GitHub. Make the analysis repository public
when the paper comes out, and link it from your website and the methods section.

## Create it

1. Open the [analysis repository template](https://github.com/YOUR-ORG/analysis-repo-template).
2. **Use this template → Create a new repository**. Name it after the project,
   e.g. `nuclear-size-screen`. Choose **Private**.
3. **Route A:** add the new repository to the Claude GitHub app's allowed list.

## The layout, and why

```
├── README.md            what, why, how to run          → the first thing anyone reads
├── CLAUDE.md            rules for Claude                → consistent, good-practice changes
├── CHANGELOG.md         what changed, by version        → which version made Figure 3?
├── CITATION.cff         how to cite                     → a "Cite this repository" button
├── LICENSE              how others may reuse it         → no licence means nobody can legally reuse it
├── environment.yml      exact software needed           → "works on my machine" → works anywhere
├── fiji/macros/         .ijm macros
├── python/              .py scripts
├── notebooks/           exploration and figures
├── data/README.md       WHERE the data lives            → data is NOT in Git
├── data/sample/         one tiny test image             → known answer for tests
├── results/             outputs (not in Git)            → regenerate from code
├── docs/decisions.md    dated analysis decisions        → why Otsu? why 30 px?
├── docs/methods.md      methods text for the paper
├── tests/               automated checks
└── .github/             tests workflow, issue & PR templates
```

{: .concept }
> The three big rules:
> 1. **Code in Git, data on storage.** Record *where* the data is in `data/README.md`.
> 2. **Results come from code.** Anything in `results/` can be regenerated, so it isn't tracked.
> 3. **Decisions are written down.** Thresholds and exclusions go in `docs/decisions.md`, with the date.

## Exercise: fill in the README

{: .exercise }
> Using Claude (either route):
>
> > This is my analysis repository for [one-sentence project description].
> > Fill in the ✏️ placeholders in README.md, data/README.md and CITATION.cff.
> > Ask me for anything you don't know. Don't make things up.
>
> Notice that Claude should *ask* you for the data location and your ORCID
> rather than inventing them.

## Get it onto your computer (for Fiji)

To run macros in Fiji, you need the files locally:

1. Install [GitHub Desktop](https://desktop.github.com/) and sign in.
2. **File → Clone repository**, pick your analysis repo, and choose a folder
   (e.g. `Documents/GitHub/`).
3. Now the files exist on your computer *and* on GitHub. After you edit a macro
   in Fiji, GitHub Desktop shows the change. Write a message, click **Commit**, then
   **Push origin** to send it to GitHub.
4. If Claude has made changes on GitHub, click **Fetch origin**, then **Pull**, to get them.

{: .warning }
Always **pull before you start working** and **push when you finish**. It
stops your copy and the GitHub copy from drifting apart.

## Exercise: run the example macro

{: .exercise }
> 1. In Fiji: **Plugins → Macros → Run…** and choose `fiji/macros/measure_nuclei.ijm`.
> 2. Input folder: `data/sample`. Output folder: `results`.
> 3. Open `results/summary.csv`. You should get **6** nuclei.
> 4. In GitHub Desktop: notice that the new files in `results/` **don't** appear as changes.
>    That's the `.gitignore` file at work. Open it and find the rule that does it.

## Exercise: see the tests protect you

{: .exercise }
> Ask Claude (Route A) or use the GitHub editor to add a new macro,
> `fiji/macros/quick_test.ijm`, containing only:
>
> ```
> open("/Users/me/Desktop/image.tif");
> run("Measure");
> ```
>
> Commit it on a new branch and open a pull request. The **Tests** check fails
> ❌ twice: the macro has no header, and it has a hard-coded path. Read the
> failure messages. They tell you how to fix it. Then ask Claude:
>
> > The tests are failing on quick_test.ijm. Fix it following the conventions in CLAUDE.md.
