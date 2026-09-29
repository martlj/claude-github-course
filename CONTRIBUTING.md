# Contributing

<!-- research-standards v1.0.0. Shared file: don't edit in a project. -->

Thanks for helping with this project. We follow shared research standards
(see [`STANDARDS.md`](STANDARDS.md)), so the way of working is the same as in
our other projects. You can do all of this by asking Claude.

## Before you start

1. Make sure you can access the repository (ask the owner to add you as a collaborator).
2. Read `README.md` (what the project is) and `CLAUDE.md` (project facts and exceptions).
3. Check the **Issues** tab: is someone already working on this? If not, open an issue first
   for anything bigger than a typo, so it can be discussed.

## Making a change

1. **Start from the latest `main`.**
2. **Work on a branch**, never directly on `main`. Claude does this for you.
3. **Keep it small:** one topic per branch and pull request.
4. **Commit with clear messages** that say what and why: `Exclude border nuclei from area measurements`.
5. **Open a pull request** using the template. Link the issue with `Fixes #N`.
6. **Wait for the automated checks** (✅). If one fails, ask Claude to explain and fix it.
   Never switch a check off to get past it.
7. **Ask for a review** from the owner or a collaborator listed in `CLAUDE.md`. For
   anything that could change results, a second person must review before merging.

Useful Claude requests: *"/review-changes"* before asking for review, and
*"/log-decision"* whenever you change an analysis parameter.

## Reviewing someone else's pull request

- Read the **Files changed** tab. Does it do what the description says, and only that?
- For analysis changes: were tests added? Is there a QC image or comparison? Is the decision logged?
- Comment on specific lines, and be kind and specific. Approve, or request changes.
- You can ask Claude: *"Review pull request #N against our standards and explain it to me."*

## Never commit

Raw or processed data, images (except tiny examples in `data/sample/`),
results, passwords/keys, or personal data. If this happens by accident, tell
the owner straight away. Deleting the file doesn't remove it from the history.

## Questions

Open an issue with the *Task or idea* template, or ask the owner.
