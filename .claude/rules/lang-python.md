---
paths:
  - "**/*.py"
  - "**/*.ipynb"
  - "environment.yml"
  - "requirements*.txt"
  - "pyproject.toml"
---
<!-- research-standards v1.0.0. Shared standard: don't edit in a project; propose changes to the research-standards repository. -->

# Python

## Layout

- Analysis scripts in `python/` (or `src/<package>/` for larger projects), tests in `tests/`, exploratory notebooks in `notebooks/`.
- Put logic in small functions that can be tested (`segment_nuclei(image, sigma)`). Keep command-line handling in `main()` using `argparse`, guarded by `if __name__ == "__main__":`.
- Scripts are run from the repository root: `python python/script.py INPUT OUTPUT`.

## Style

- Start each module with a docstring: what it does, how to run it, author.
- Give functions docstrings (NumPy style) with parameter units, and type hints.
- Use `pathlib.Path` for paths. Never hard-code personal paths.
- Descriptive names (`nucleus_area_um2`, not `a2`). Keep units in names or docstrings.
- Format and lint with `ruff` (`ruff check .`, `ruff format .`) if the project configures it.

## Libraries

Prefer well-established scientific libraries over hand-written algorithms:
`numpy`, `scipy`, `pandas`, `scikit-image`, `tifffile`, `bioio`/`aicsimageio`
(microscopy formats), `matplotlib`/`seaborn` for figures, and `napari` for
interactive viewing. Add any new dependency to the environment file in the same commit.

## Data handling

- Read images with their metadata (pixel size, channel names) where the format allows, and carry the units through to the results.
- Be explicit about dtype conversions (e.g. `uint16` to `float`) and don't clip or rescale intensities before measuring.
- Write tables with `pandas.DataFrame.to_csv(index=False)`, one row per object, with clear column names including units.

## Notebooks

- Clear outputs before committing.
- Number notebooks in run order: `01_explore.ipynb`, `02_figure_2.ipynb`.
- Once the analysis in a notebook settles, move it into a tested function in `python/` and have the notebook call it.

## Tests

- `pytest`, in `tests/test_<module>.py`, with known-answer tests on synthetic data (see the testing rule).
