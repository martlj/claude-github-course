---
title: 7. Image analysis with Claude
nav_order: 7
permalink: /07-image-analysis/
---

# 7. Image analysis with Claude
{: .no_toc }

Claude is good at writing Fiji macros and Python scripts. It **can't see your
images** unless you show it, and it can be confidently wrong. This module is
about getting good code *and* knowing it's right.
{: .fs-5 }

1. TOC
{:toc}

---

## The workflow

1. **Describe the biology and the images** precisely (use the *Analysis task* issue template).
2. **Ask for a plan** before any code.
3. **Get the code** following the repo's conventions.
4. **Test on something with a known answer**: synthetic data, hand counts, a control.
5. **Look at the output images**, not just the numbers. Overlay the masks on the originals.
6. **Record decisions** in `docs/decisions.md` and commit.

## 1. Describe the task well

Claude's code is only as good as your description. Include:

| Tell Claude… | Example |
|--------------|---------|
| Dimensions | 2D, single z-plane; *or* 3D z-stacks, 40 slices; *or* time-lapse, 120 frames |
| Channels and what they show | C1 = DAPI (nuclei), C2 = GFP-LC3 (autophagosomes, appear as puncta) |
| Pixel size | 0.108 µm/px, from the metadata |
| File format | .czi from the Zeiss LSM 980 (open with Bio-Formats) |
| What counts as an object | Puncta are 3–10 px bright spots inside cells |
| What you want out | Number of puncta per cell, one row per cell, CSV |
| Difficulties | Some cells touch; background varies across the field |

{: .tip }
Upload a **screenshot** of a representative image (and a difficult one) into
Claude chat. It helps Claude choose sensible approaches. Only share images
your data-handling policies allow.

## 2. Start from the Macro Recorder

If you already know which Fiji menu commands you'd click, record them:
**Plugins → Macros → Record…**, do the steps by hand on one image, then give
the recording to Claude:

> Here's a recording of what I do by hand in Fiji. Turn it into a macro in
> fiji/macros/count_puncta.ijm that processes every .czi file in a folder,
> following the conventions in CLAUDE.md (header, #@ parameters, batch mode,
> CSV output). Explain each step.

This is the most reliable route, because the commands in a recording are
guaranteed to exist in *your* Fiji.

## 3. Exercise: a puncta-counting macro

{: .exercise }
> Open an **Analysis task** issue in your repository (**Issues → New issue →
> Analysis task**) describing a puncta-per-cell analysis on your own images (or
> invent one). Then:
>
> - *Route A:* "Read issue #N and propose a plan. Don't write code yet."
>   Review the plan, then: "Go ahead. Also add a synthetic test image with a known number
>   of puncta to data/sample, and a test that checks the count."
> - *Route B:* paste the issue text and `fiji/macros/measure_nuclei.ijm` (as a
>   style example) into Claude chat and ask for the macro.
>
> Run it in Fiji on the sample, then on one of your real images.

## 4. Verify, verify, verify

{: .warning }
> Common ways AI-written image analysis goes wrong:
> - **Commands that don't exist**, or plugin commands from a plugin you haven't
>   installed. Fiji reports *"Unrecognized command"*. Paste the error back to Claude.
> - **Wrong threshold direction**: it measured the background instead of the objects.
> - **Units**: areas in pixels when you assumed µm², or the reverse.
> - **Silent edge cases**: empty images, saturated images, one channel missing.
> - **Plausible numbers that are wrong.** Code that runs isn't the same as code that's correct.

Checks worth doing every time:

- Compare with **hand counts** on 3–5 images, including a hard one.
- Save and **look at the masks/ROIs** overlaid on the original. Ask Claude to add this.
- Try a **positive and a negative control** image.
- Ask Claude: *"What assumptions does this macro make about my images? When would it give wrong answers?"*

## 5. Python for the bigger jobs

Fiji is great for interactive work. Python is better for batch processing
thousands of images, statistics and figures. The template includes
`python/count_nuclei.py`, which does the same analysis as the Fiji macro, and
tests for it.

> Convert fiji/macros/count_puncta.ijm to a Python script in python/ using
> scikit-image, with tests in tests/ like the ones for count_nuclei.py.
> Check both give the same counts on the sample image.

Two independent implementations that agree give you much more confidence
than one.

## 6. Record the decision

> Add an entry to docs/decisions.md for today explaining the puncta detection
> parameters we chose and how we checked them. Update docs/methods.md too.

When you write the paper, the methods section is already half-written, and
you can point reviewers to the exact tagged version of the code.

{: .tip }
**Tag a release** when you submit: on GitHub, **Releases → Draft a new release**,
tag `v1.0.0`. Connecting the repository to [Zenodo](https://zenodo.org/) gives
each release a citable DOI.
