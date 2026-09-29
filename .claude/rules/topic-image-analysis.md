---
paths:
  - "**/*.ijm"
  - "**/*.py"
  - "**/*.ipynb"
  - "**/*.R"
  - "**/*.qmd"
  - "fiji/**"
  - "python/**"
  - "notebooks/**"
---
<!-- research-standards v1.0.0. Shared standard: don't edit in a project; propose changes to the research-standards repository. -->

# Image analysis practice

## Understand the images first

Before writing analysis code, make sure you know, or ask:

- dimensions (2D, 3D z-stack, time-lapse, multi-position) and their order;
- channels and what each shows;
- pixel/voxel size and time interval (from metadata where possible);
- bit depth and file format;
- what counts as an object, and roughly how big and how many per image;
- what output is wanted (per object, per cell, per image, per condition);
- how the result will be checked (hand counts, controls, expected range).

If the researcher is using Claude chat, ask for a screenshot of a typical image
and a difficult one.

## Good practice

- Keep a copy of the original intensities. Filter and threshold a duplicate, and measure intensities on the original (or a uniformly background-corrected version).
- Prefer automatic, documented threshold methods (Otsu, Triangle, Li…) or trained models over manual thresholds. If a manual value is used, make it a parameter and log it in `docs/decisions.md`.
- Apply identical processing to all conditions, including controls.
- Handle objects touching the image border explicitly (exclude them or flag them) and say which.
- Report measurements in calibrated units where calibration exists, and say so in column names (`area_um2`).
- Always produce a **QC output**: segmentation outlines/labels overlaid on the original, saved alongside results, so a human can check a sample.
- Distinguish technical from biological replicates in outputs (keep image, field, well, experiment and date as columns).

## Choosing methods

- Start simple (filter, threshold, watershed) and only escalate (StarDist, Cellpose, trained classifiers) when simple methods demonstrably fail on the researcher's images.
- For deep-learning tools, record the model name/version and any retraining, and validate on held-out manually annotated images.
- Name established tools and cite them in `docs/methods.md`.

## Validation

Suggest (and help build) a small validation set: 3–10 images with manual
counts or annotations, including hard cases. Report agreement (e.g. counts
difference, or F1/IoU for segmentation) before the analysis runs on the full dataset.
