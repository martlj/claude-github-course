---
title: 2. Version control
nav_order: 2
permalink: /02-version-control/
---

# 2. Version control: the six ideas you need
{: .no_toc }

1. TOC
{:toc}

---

## Why bother?

You've probably seen a folder like this:

```
measure_nuclei.ijm
measure_nuclei_v2.ijm
measure_nuclei_v2_FINAL.ijm
measure_nuclei_v2_FINAL_fixed_threshold.ijm
measure_nuclei_USE_THIS_ONE.ijm
```

Which one produced Figure 3? What changed between them? Did the "fix"
affect the earlier results? **Version control** answers these questions.
It keeps **one** copy of each file, plus a complete, dated history of every
change, who made it and why.

{: .concept }
> Version control is a **lab notebook for files**. Each entry records what
> changed, when, by whom and why. You never tear pages out, and you can
> always turn back to see exactly what was there before.

*Git* is the version-control software. *GitHub* is a website that stores Git
repositories online, and adds collaboration tools, websites (GitHub Pages)
and automation (GitHub Actions).

## 1. Repository

A **repository** ("repo") is a project folder whose history is tracked. It
contains your files plus the complete history of every change to them.

## 2. Commit

A **commit** is a saved snapshot of changes, with a message explaining them.
It's the basic unit of history.

```
a1b2c3d  Raise minimum nucleus area to 50 px to exclude debris   (Jane, 3 Oct)
e4f5a6b  Add watershed to split touching nuclei                   (Jane, 1 Oct)
c7d8e9f  First version of nuclei macro                            (Jane, 29 Sep)
```

A good commit message finishes the sentence *"If applied, this commit will…"*:

| ❌ Unhelpful | ✅ Helpful |
|-------------|-----------|
| `update` | `Change background colour to pale grey` |
| `fixed it` | `Fix crash when folder contains non-image files` |
| `stuff` | `Add publications page with 2024 papers` |

## 3. History and diffs

Every commit can be compared with the one before. A **diff** shows exactly
which lines were removed (red, `-`) and added (green, `+`):

```diff
- --background: #fdfdfb;
+ --background: #eef4fb;
```

Learning to **read a diff** is the most important skill in this course.
When Claude makes a change, the diff is how you check what it actually did.

## 4. Branch

A **branch** is a parallel copy where you can try changes without affecting
the main version. The main version lives on a branch called `main`.

```
main:        ●───●───●───────────●   (live website)
                      \         /
new-colours:           ●───●───●     (trying things out)
```

## 5. Pull request

A **pull request** (PR) is a proposal to merge a branch into `main`. It shows
the diff, runs the automated tests, and gives you (or a colleague) a place
to review before anything goes live. Claude Code usually delivers its work as
a pull request.

## 6. Issue

An **issue** is a to-do item, bug report or idea attached to a repository.
Issues can be discussed, assigned, labelled, and **closed automatically by a
commit** that says `Fixes #12`. You'll use them in modules 5 and 8.

---

## Glossary quick-check

{: .exercise }
> With your neighbour, match each term to its lab equivalent:
>
> | Git | Lab |
> |-----|-----|
> | Repository | ? |
> | Commit | ? |
> | Commit message | ? |
> | Branch | ? |
> | Pull request | ? |
> | Issue | ? |
>
> *Suggested answers:* project folder + notebook, a dated notebook entry, the
> written description in that entry, a pilot experiment, asking your PI to sign
> off before it goes in the paper, a sticky note / to-do list.
