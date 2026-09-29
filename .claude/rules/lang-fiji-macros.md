---
paths:
  - "**/*.ijm"
  - "**/*.bsh"
  - "**/*.groovy"
  - "fiji/**"
---
<!-- research-standards v1.1.0. Shared standard: don't edit in a project; propose changes to the research-standards repository. -->

# Fiji / ImageJ macros

## File layout

- Macros live in `fiji/macros/` (Groovy/Jython scripts in `fiji/scripts/`), named in `snake_case.ijm` after what they do: `count_puncta_per_cell.ijm`.
- Each macro is listed with a one-line description in `fiji/README.md`.

## Required header

Every macro starts with this block, and the housekeeping tests check for it:

```
// ================================================================
// @title        Human-readable name
// @author       Name <email>
// @version      1.0.0
// @date         YYYY-MM-DD
// @description  What it does, in one to three lines.
// @input        What images it expects (dimensions, channels, format).
// @output       What files it writes.
// @requires     Fiji / ImageJ version, and any plugins with update sites.
// @test         How to check it: e.g. "Run on data/sample/: expect 6 nuclei".
// ================================================================
```

## Inputs and parameters

- Use **SciJava script parameters** (`#@ File (style = "directory") input`, `#@ Double (value = 2.0) sigma`) for every input and tunable value. They produce a dialog, work headless, and remove hard-coded paths.
- Never hard-code paths, file names or user names.
- Build paths with `File.separator` so macros work on Windows, macOS and Linux.

## Structure

- Process folders in `setBatchMode(true)`, and restore it at the end.
- Put per-image work in a `function processFile(...)`.
- Work on duplicates (`run("Duplicate...", ...)`) so the original stays available for intensity measurements. Use `redirect=` in *Set Measurements* to measure intensities on the original image.
- Set options explicitly rather than relying on the user's Fiji settings: `setOption("BlackBackground", true)`, `run("Set Measurements...", ...)`, and calibration where relevant.
- Save results as CSV (`saveAs("Results", ...)`), one file per image plus a summary. Also save ROIs (`roiManager("Save", ...)`) or an overlay image for visual QC.
- Close images and clear the ROI Manager/Results between files, so one image can't leak into the next.
- Exit with a clear message (`exit("...")`) when inputs are missing or wrong.

## Correctness

- Only use commands you're confident exist in standard Fiji. Prefer commands captured with the Macro Recorder (*Plugins → Macros → Record…*), and ask the researcher to record a step if unsure.
- State plugin dependencies (e.g. Bio-Formats for `.czi`/`.nd2`/`.lif`, which ships with Fiji, and StarDist/MorphoLibJ, which need update sites) in `@requires`.
- Check the calibration: report whether measurements are in pixels or calibrated units, and say which.
