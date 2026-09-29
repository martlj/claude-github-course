---
name: new-python-script
description: Create a new Python analysis script that follows the lab standards, with testable functions, a command-line interface, docstrings, dependencies in environment.yml and known-answer tests. Use when asked to write a Python script, convert a Fiji macro or notebook to Python, or batch-process data in Python.
---
<!-- research-standards v1.0.0 -->

# Create a Python analysis script

Follow `.claude/rules/lang-python.md`, `05-testing.md` and `topic-image-analysis.md`.

## Steps

1. **Confirm the task** (issue or plan). Ask about anything missing that changes the result: dimensions, channels, units, output level.
2. **Create `python/<verb>_<thing>.py`** with:
   - a module docstring (what, how to run, author) and `__version__ = "1.0.0"`;
   - pure functions for each step (load, segment, measure, summarise), with NumPy-style docstrings, units and type hints;
   - a `process_folder()` (or equivalent) that reads inputs, writes CSVs and QC images to an output folder, and never writes to the input location;
   - `main()` using `argparse`, exposing every parameter that affects results.
3. **Dependencies:** add any new package to `environment.yml` (or the project's equivalent).
4. **Tests:** add `tests/test_<script>.py` with known-answer tests on synthetic data and edge cases (`add-known-answer-test`). If converting from a Fiji macro, add a test that both give the same result on `data/sample/` where feasible, or document the expected agreement.
5. **Run** `pytest` and `ruff check .` if available. Report the results truthfully.
6. **Document:** a row in `python/README.md`, a changelog entry, and decisions for parameter choices.
7. **Hand over** with the exact command to run it on their data, and what to check in the QC output.
