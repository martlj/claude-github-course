---
name: add-known-answer-test
description: Add an automated test that checks analysis code against synthetic or reference data with a known correct answer. Use when new analysis code is written, when a bug is fixed (to stop it coming back), or when asked "how do we know this is right?".
---
<!-- research-standards v1.0.0 -->

# Add a known-answer test

## Steps

1. **Pick the property to check:** count, area, intensity, position, classification. Choose whatever the researcher cares about.
2. **Build the input with a known answer**, as small as possible:
   - Prefer generating it in code (e.g. discs of known radius on a noisy background with a fixed random seed) in a helper such as `tools/make_sample_data.py`, so the "truth" is explicit.
   - Include at least one difficulty the method must handle (a speck below the size cut-off, two touching objects, an uneven background).
   - If a committed file is needed, keep it in `data/sample/`, tiny (KB, not MB), and make sure `.gitignore` allows it.
3. **Write the test** in `tests/test_<module>.py` (pytest for Python, testthat for R):
   - one behaviour per test, with a descriptive name (`test_small_specks_are_ignored`);
   - justify tolerances in a comment (e.g. "±15%: blur and thresholding shift edges");
   - add an edge-case test that expects a clear error for invalid input.
4. **For bug fixes**, first write a test that reproduces the bug and fails, then fix the code and show it passes.
5. **For Fiji macros** (which CI can't easily run), put the expected result in the macro's `@test` header, and if there's a Python equivalent, test that on the same sample.
6. **Run the tests** and report the results. Never weaken an existing test to make a new change pass.
