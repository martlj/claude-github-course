---
name: progress-summary
description: Summarise recent progress in the repository (commits, merged pull requests, closed and open issues, decisions logged) in plain language for a PI, lab meeting or collaborator. Use when asked what changed, what was done this week or month, or for a status update.
---
<!-- research-standards v1.1.0 -->

# Progress summary

1. Ask for (or assume and state) the period, e.g. "the last 7 days", and the audience.
2. Gather: `git log --since=...` on `main`, merged pull requests and closed/opened issues (via `gh` if available), and new entries in `docs/decisions.md` and `CHANGELOG.md`.
3. Write at most one page:
   - **Headline:** one or two sentences.
   - **Done:** grouped by theme, not by commit, with issue/PR links.
   - **Decisions made:** from decisions.md, with the reason.
   - **Results that may need re-running** (version bumps that change results).
   - **Blocked / waiting:** open issues labelled `waiting` or similar.
   - **Next:** top open issues.
4. Use plain language, with no commit hashes unless asked. Don't overstate: report what the records show.
