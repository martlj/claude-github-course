<!-- research-standards v1.0.0. Shared standard: don't edit in a project; propose changes to the research-standards repository. -->

# Testing and checking

Tests are the controls of computational work: small checks against a
**known answer**, run automatically every time something changes.

## What to test

- **Known-answer tests:** run the analysis on synthetic or reference data where the correct result is known (e.g. an image with exactly 6 nuclei of known size), and assert the result with a sensible tolerance.
- **Edge cases:** empty inputs, a single object, touching objects, saturated pixels, wrong dimensions (the code should fail with a clear message, not a wrong number).
- **Housekeeping:** required headers and documentation present, no hard-coded paths, no large or raw data files committed, links resolve (for websites).

Use the `add-known-answer-test` skill to create these.

## Rules

- New analysis functions get at least one known-answer test in the same pull request.
- Run the tests before saying something works, and report what you ran and the outcome. If you couldn't run them, say so plainly.
- **Never delete, skip or loosen a failing test to make it pass** without the researcher's explicit agreement. A failing test is information: explain what it's telling you.
- Loosening a tolerance counts as a scientific decision. Log it in `docs/decisions.md`.
- Tests must be fast (seconds) and use only small files committed in the repository, or data generated in the test.

## "It runs" is not "it's right"

For image analysis, passing tests is necessary but not sufficient. Always
suggest a visual check (masks or ROIs overlaid on the original image) and a
comparison with manual measurements on a few images, including a difficult one.

## Continuous integration

- Automated checks live in `.github/workflows/`. Keep them passing on `main`.
- Scheduled (weekly) checks catch problems caused by the outside world: package updates, websites moving. When they fail, the workflow opens a GitHub issue. Treat it like any other bug.
