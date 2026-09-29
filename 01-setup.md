---
title: 1. Setup
nav_order: 1
permalink: /01-setup/
---

# 1. Setup
{: .no_toc }

Please do this **before** the first session. It takes about 20 minutes.
{: .fs-5 }

1. TOC
{:toc}

---

## Create a GitHub account

1. Go to [github.com/signup](https://github.com/signup).
2. **Use your personal email address** and add your institute email as a
   second address afterwards (*Settings → Emails*). The account belongs to you,
   not your job, so your code and website move with you when you change institutes.
3. **Choose your username carefully.** It becomes your website address
   (`username.github.io`) and appears on everything you publish. Something like
   `janesmith` or `jsmith-lab` works. Avoid `xXcellbio99Xx`.
4. Turn on **two-factor authentication** when GitHub asks (it's required). An
   authenticator app on your phone is the easiest option.
5. Send your username to the course organiser so you can be added to the course organisation.

{: .tip }
Fill in your GitHub profile (name, photo, affiliation, ORCID). Reviewers and
collaborators will look at it.

## Get access to Claude

You'll use Claude through the institute's team licence. Accept the invitation
email, then sign in at [claude.ai](https://claude.ai) with your institute email.

## Connect GitHub to Claude

**Route A (Claude Code):** open [claude.ai/code](https://claude.ai/code), or
the Claude desktop app's **Code** tab, and follow the prompt to connect
GitHub. GitHub then asks which repositories Claude may access. Pick **Only
select repositories**. You'll add each repository as you create it, which
means Claude can only touch what you've chosen.

**Route B (chat only):** nothing to connect. You'll copy and paste between
Claude and GitHub.

{: .note }
Menus and button names in Claude and GitHub change from time to time. If
something here doesn't match what you see, look for the nearest equivalent,
or [open an issue](https://github.com/martlj/claude-github-course/issues) on
this course so it can be fixed.

## Optional: install software on your own computer

You don't need any of this for modules 1–5, because everything happens in the browser.

| Software | Why | Needed for |
|----------|-----|-----------|
| [GitHub Desktop](https://desktop.github.com/) | Copy repositories to your computer without the command line | Module 6+ |
| [Fiji](https://imagej.net/software/fiji/) | Image analysis | Module 7 |
| [Miniforge](https://github.com/conda-forge/miniforge) | Python environments (conda) | Python parts of module 6–7 |

## Checklist

- [ ] GitHub account created, 2FA on, username sent to the organiser
- [ ] Signed in to Claude with your institute account
- [ ] (Route A) GitHub connected to Claude Code
