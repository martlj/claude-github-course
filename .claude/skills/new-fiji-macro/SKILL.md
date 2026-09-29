---
name: new-fiji-macro
description: Create a new Fiji/ImageJ macro (.ijm) that follows the lab standards, including a header, script parameters, batch processing, CSV and QC outputs, and a test. Use when asked to write, convert or tidy up a Fiji macro, including from Macro Recorder output.
---
<!-- research-standards v1.1.0 -->

# Create a Fiji macro

Follow `.claude/rules/lang-fiji-macros.md` and `topic-image-analysis.md`.

## Steps

1. **Check the task is defined.** If there's no issue or plan, run the `start-analysis` steps briefly first: dimensions, channels, objects, output, validation.
2. **Start from what the researcher does by hand** if possible: ask for Macro Recorder output (*Plugins → Macros → Record…*) of the steps on one image. Recorded commands are guaranteed to exist in their Fiji.
3. **Choose a name** (`snake_case`, verb first: `count_puncta_per_cell.ijm`) and create it in `fiji/macros/`.
4. **Write the macro:**
   - the full header block (title, author, version 1.0.0, date, description, input, output, requires, test);
   - `#@` script parameters for input folder, output folder, file extension and every tunable value;
   - `setBatchMode(true)`, a `processFile()` function, and explicit `Set Measurements`/options;
   - work on a duplicate, and measure on the original via `redirect=`;
   - save a CSV per image, a summary CSV, and a QC overlay or ROI set per image;
   - clear the Results table and ROI Manager and close images between files, and give a clear `exit()` message on bad input.
5. **Add test data** if none fits: create (or extend) a synthetic image in `data/sample/` with a known answer (see `add-known-answer-test`), and put the expected result in the `@test` header line.
6. **Document it:** add a row to `fiji/README.md`, a `CHANGELOG.md` entry under *Unreleased*, and a `docs/decisions.md` entry for the parameter choices (`log-decision`).
7. **Hand over** with instructions to run it: *Plugins → Macros → Run…*, which folders to choose, and the expected result on the sample. Ask the researcher to report the result and any Fiji error messages. You can't run Fiji yourself unless the environment has it, so say so.
