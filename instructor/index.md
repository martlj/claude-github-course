---
title: For instructors
nav_order: 30
permalink: /instructor/
---

# Instructor notes
{: .no_toc }

1. TOC
{:toc}

---

## One-off preparation

1. **Create a GitHub organisation** for the course or the institute (e.g. `crick-claude-course`).
   Put the three repositories in it:
   - `claude-github-course` (this site)
   - `personal-website-template`
   - `analysis-repo-template`
2. In each template repository, go to **Settings** and tick **Template repository**.
3. Replace every `YOUR-ORG` in this course (`_config.yml` and the module pages).
   Ask Claude: *"Replace YOUR-ORG with crick-claude-course throughout this repository."*
   Then remove the `github\.com/YOUR-ORG` line from `.lycheeignore`, so those links get checked too.
4. Turn on Pages for this repository (**Settings → Pages → Deploy from a branch → main / root**).
   If you rename the repository, update `baseurl` in `_config.yml`.
5. **Do a dry run with a fresh GitHub account.** Menus change. Update the pages where they differ.
6. Check how Claude seats and Claude Code access work on the institute's licence,
   and whether the Claude GitHub app is allowed by any organisation policies.
7. Check the institute's data and AI-tool policy, and add a line to modules 1 and 7 on
   what images/data may be shared with Claude.

## A week before

- Collect GitHub usernames. Add participants to the organisation (they can then
  use the templates even if you make them private).
- Send module 1 as homework. Budget 10 minutes at the start to rescue people who didn't do it.
- Have 2–3 helpers for 15–20 participants. The bottlenecks are account set-up and 2FA.

## Suggested timings

| Session | Content | Notes |
|---------|---------|-------|
| **Session 1** (3 h) | Modules 2–5 | Break after module 3 once everyone has a live site. That's the morale boost |
| **Session 2** (3 h) | Modules 6–8 | Ask people to bring 2–3 of their own images (non-sensitive) |
| **Follow-up** (1 h, 2 weeks later) | Drop-in clinic | Look at real repos and problems |

## Common snags

| Snag | Fix |
|------|-----|
| Repository named `Username.github.io` with capitals, or a typo | Settings → rename. The link checker catches the resulting broken links, which makes a good teaching moment |
| Pages not enabled, or site 404 | Settings → Pages. The first deploy can take a few minutes |
| People commit straight to `main` and skip PRs | Fine in module 3. From module 4, encourage "Create a new branch". Optionally add a branch protection rule |
| Claude changes more than asked | A good discussion point: review the diff, ask for a smaller change, point to `CLAUDE.md` |
| Claude invents publication details | Deliberate lesson in module 4. Stress verification |
| Fiji macro fails on `.czi` | Needs Bio-Formats (`run("Bio-Formats Importer", ...)`), which Fiji includes. Suggest the Macro Recorder |
| Link checker flags external sites (rate limits) | Rerun. `429` is already accepted, and persistent offenders go in `.lycheeignore` |

## Demonstrations that work well

- **Live-break the site:** put a YAML indentation error in `_config.yml`, show the
  red build, read the error together, fix it with Claude.
- **Diff reading:** show a Claude PR that also "tidied" unrelated lines. Ask the room
  whether they'd merge it.
- **Time travel:** open a file's **History** and **Blame** views, to show who changed a line and when.

## Extending the course

- **Branch protection** on `main` (require PRs + passing checks) for shared lab repos.
- **Collaborating:** pairs add each other as collaborators and review each other's PRs.
- **Headless Fiji in CI:** run macros automatically in GitHub Actions (advanced).
- **Zenodo DOIs** for releases.
- **OMERO**: record dataset IDs in `data/README.md`, and fetch data from scripts.
