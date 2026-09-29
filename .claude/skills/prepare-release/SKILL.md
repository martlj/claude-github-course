---
name: prepare-release
description: Prepare a tagged release of an analysis repository, for example for a paper submission, thesis or report, covering the version, changelog, citation and methods text.
disable-model-invocation: true
---
<!-- research-standards v1.1.0 -->

# Prepare a release

1. **Check the repository is clean:** tests pass on `main`, there are no open pull requests the researcher wants included, and no ✏️ placeholders remain in README, CITATION.cff or data/README.md (list any that do).
2. **Choose the version** with the researcher: MAJOR if results changed since the last release, MINOR for new analyses, PATCH for fixes only. Explain the choice.
3. **Update files** on a branch `release-vX.Y.Z`:
   - `CHANGELOG.md`: move *Unreleased* items under `## [X.Y.Z] - YYYY-MM-DD`;
   - `CITATION.cff`: `version`, `date-released`;
   - script and macro versions, if they changed;
   - `docs/methods.md`: make sure it matches the code and cites the release.
4. Open a pull request, and after it's merged…
5. **Tag the release:** create a GitHub release `vX.Y.Z` from `main` with the changelog section as notes (use `gh release create` if available, otherwise give the researcher the steps: *Releases → Draft a new release*).
6. **Suggest archiving:** if the repository is connected to Zenodo, the release gets a DOI. Remind the researcher to put the DOI in the paper and the README.
