---
paths:
  - "**/*.R"
  - "**/*.r"
  - "**/*.Rmd"
  - "**/*.qmd"
  - "renv.lock"
  - "DESCRIPTION"
---
<!-- research-standards v1.1.0. Shared standard: don't edit in a project; propose changes to the research-standards repository. -->

# R

- Scripts live in `R/`, reports in `reports/` (Quarto `.qmd` or R Markdown `.Rmd`), tests in `tests/testthat/`.
- Record packages with `renv` (`renv::init()`, `renv::snapshot()`) and commit `renv.lock`.
- Use the `here` package for paths relative to the project root (`here::here("data", "sample")`). Never `setwd()` to a personal path.
- Start each script with a header comment: title, author, version, date, description, inputs, outputs.
- Prefer tidyverse-style, readable code (`dplyr`, `ggplot2`) unless the project uses base R throughout. Be consistent with the existing code.
- Write functions for repeated steps, with roxygen-style comments (`#' @param`).
- Save figures with `ggsave()` from code, with explicit size and resolution.
- Report statistical tests fully: test used, assumptions checked, n (and what n is: cells, images or biological replicates), effect size and exact p-values.
- Test functions with `testthat` against known answers.
