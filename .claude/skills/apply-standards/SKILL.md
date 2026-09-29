---
name: apply-standards
description: Audit an existing project folder or repository against the lab standards and propose a step-by-step plan to bring it in line (structure, missing files, data in Git, hard-coded paths, missing tests). Use when someone brings an existing or messy project, or asks "does this follow our standards?".
---
<!-- research-standards v1.1.0 -->

# Apply the standards to an existing project

Don't change anything until the researcher agrees the plan.

## 1. Audit

Survey the project and report a table with one row per area and status ✅/⚠️/❌:

| Area | What to look for |
|------|------------------|
| Required files | README, CLAUDE.md, CONTRIBUTING, LICENSE, CHANGELOG, CITATION.cff, data/README.md, docs/decisions.md |
| Structure | Code mixed with data? Versions encoded in file names (`_v2_FINAL`)? |
| Data in Git | Large or raw image files tracked (`git ls-files`, sizes), and whether they're in history |
| Paths | Hard-coded personal paths in macros/scripts |
| Headers & docs | Macros and scripts missing headers or docstrings |
| Environment | Dependencies recorded? |
| Tests & CI | Any known-answer tests? Workflows? |
| Sensitive data | Anything that looks personal or confidential. **Stop and flag it** |

## 2. Plan

Propose small, ordered steps, each a separate pull request. The safest and most valuable come first:

1. Add `.gitignore` and stop tracking data (flag if history needs cleaning, which is a job for an expert).
2. Add the standards files (`update-standards`) and a project `CLAUDE.md`.
3. Reorganise folders (`fiji/macros`, `python`, `data`, `results`, `docs`, `tests`) with `git mv` so history is kept. Collapse `_v2_FINAL` copies into one file, and record in the commit message which copy was kept and why.
4. Add headers, and replace hard-coded paths with parameters.
5. Add the environment file, then known-answer tests and CI.
6. Fill in README, data/README.md and decisions (ask for facts, don't invent them).

## 3. Execute

Only after agreement, one step at a time, with the researcher reviewing each pull request.
