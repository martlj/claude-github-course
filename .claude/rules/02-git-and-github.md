<!-- research-standards v1.0.0. Shared standard: don't edit in a project; propose changes to the research-standards repository. -->

# Git and GitHub

## Branches and pull requests

- Don't commit directly to `main` unless the researcher explicitly asks. Work on a branch and open a pull request so automated checks run before anything goes live.
- Branch names: short, lower case, hyphenated, describing the change: `fix-broken-doi-link`, `add-puncta-macro`, `issue-12-teaching-page`.
- One topic per branch and pull request.
- Pull request descriptions follow `.github/pull_request_template.md` if present. At minimum they say what changed, why, whether results could change, and how it was checked.
- Link issues: `Fixes #12` (closes it on merge) or `Part of #12` (links without closing).
- Check the status of automated checks on the pull request. If one fails, explain why in plain language and fix the cause. Never weaken a check to make it pass.

## Commits

- Small and focused: one logical change per commit.
- Message format: a summary line under ~70 characters in the imperative mood ("Add…", "Fix…", "Change…"). Add a blank line and a short body for *why* when it isn't obvious.

  ```
  Raise minimum nucleus area to 50 px

  30 px let debris through in plate 2 images (see issue #14).
  Results for plates 1-3 need re-running.
  ```

- Never commit secrets (passwords, API keys, tokens), personal data, or large/raw data files. Check `git status` / the diff before committing.
- Don't rewrite published history (`git push --force`, amending pushed commits) unless the researcher asks and understands the consequence.

## Issues

- Use the repository's issue templates when they exist.
- Good issues are small and finishable, with a clear "done" condition.
- When asked to create issues from notes, create one issue per action item, with labels, and list what you created.

## Collaboration

- Before starting work, make sure you have the latest `main` (pull or fetch).
- If a change touches someone else's recent work, mention it in the pull request so they can review.
- Resolve merge conflicts by explaining both versions to the researcher and asking which to keep when the choice isn't obvious.
