---
name: review-changes
description: Review a set of changes (a branch, pull request or uncommitted work) against the lab standards before merging, and report problems in plain language. Use when asked to review or check changes, before opening a pull request, or when asked "is this ready?".
---
<!-- research-standards v1.1.0 -->

# Review changes before merging

Look at the full diff (`git diff main...HEAD`, the pull request's files, or
uncommitted changes) and check each point. Report findings as ✅ / ⚠️ / ❌
with one line each, most important first, then offer to fix the problems.

## Checklist

**Scope**
- Does the change do what was asked, and only that? Flag unrelated edits.

**Data and safety**
- No data, images, results, large files, secrets or personal data added.
- `.gitignore` rules not weakened.

**Correctness**
- Tests exist for new analysis code, and they pass (run them).
- No test deleted, skipped or loosened without a logged reason.
- Parameters are not hard-coded, and there are no personal paths.
- Units are consistent and stated.

**Reproducibility**
- New dependencies added to the environment file.
- Version bumped and `CHANGELOG.md` updated if results could change.
- Decisions logged in `docs/decisions.md`.

**Documentation**
- Headers and docstrings present, folder READMEs and the main README updated if usage changed.

**Integrity**
- No fabricated facts, references or placeholder values presented as real.
- Image processing applied uniformly, with measurements on unadjusted data.

**Git**
- Clear commit messages, on a branch, and the PR description says what, why and how it was checked, with issue links.

Finish with a one-line verdict: *Ready to merge*, *Ready after small fixes*, or *Needs discussion*, with the reason.
