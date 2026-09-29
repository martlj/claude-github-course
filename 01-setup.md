---
title: 1. Before the course
nav_order: 1
permalink: /01-setup/
---

# 1. Before the course
{: .no_toc }

Please do this **before the first session**. Setting up your account takes about
**30 minutes**. The suggested reading takes another 30–60 minutes, depending on how much you do.
{: .fs-5 }

1. TOC
{:toc}

---

## What you'll need

- A computer with a modern web browser (Chrome, Firefox, Safari or Edge).
- Your phone, to set up two-factor authentication.
- About 30 minutes somewhere quiet to choose your username. **It's the one
  decision in this course that's hard to undo.**

You **don't** need to install anything or learn the command line. In the course,
you'll make changes by asking Claude.

---

## Step 1: Choose your username (read this first)

Your GitHub username appears everywhere you share work:

| Where | What it looks like |
|-------|--------------------|
| Your personal website (built in module 3) | `https://janesmith.github.io` |
| Your GitHub profile | `https://github.com/janesmith` |
| Code and data availability statements in papers | `https://github.com/janesmith/nuclear-size-screen` |
| Every change you make, in the project history | `janesmith committed 3 days ago` |

{: .warning }
> **You can change your username later, but it's disruptive.** GitHub redirects
> links to your repositories only until someone else claims your old name. Your
> website's address changes with the username, so links to your old site stop
> working, including any on posters, CVs or slides. Choose a name you'd be happy
> to put on a grant application in ten years.

### The rules

- Letters (a–z), numbers (0–9) and single hyphens (`-`) only. **No underscores, dots or spaces.**
- It can't start or end with a hyphen, or contain two hyphens in a row.
- 39 characters at most.
- Capital letters don't matter: `JaneSmith` and `janesmith` are the same account, and web addresses always appear in lower case.

### What makes a good research username

1. **It's your name, recognisably.** Colleagues, editors and reviewers should be able to connect it to you.
2. **It's easy to say and spell.** Imagine reading it out at a conference, or typing it from a slide.
3. **It's short enough for a figure legend.** `github.com/jsmith/...` fits much better than `github.com/dr-jane-elizabeth-smith-phd/...`.
4. **It doesn't depend on where you work now.** You'll probably move institutes. Your account (and website) should move with you.
5. **It's professional.** It will sit next to your publications.

### Patterns that work well

Using a fictional researcher, **Aisha Okafor-Reyes**:

| Pattern | Example | Notes |
|---------|---------|-------|
| firstnamelastname | `aishaokafor` | The classic. Short surnames only |
| first-last | `aisha-okafor` | Hyphens make it easy to read |
| initial + surname | `aokafor` | Short, but more likely to be taken |
| full name, double-barrelled | `aisha-okafor-reyes` | Fine if your publications use both names |
| add a middle initial | `aishamokafor` | A good fix if your name is taken |
| add your field | `aokafor-bio`, `aisha-okafor-imaging` | Also a good fix if taken. Pick something broad enough to last |

**Match how you publish.** If your papers say "Okafor-Reyes A", people will
search for that, so `aokafor-reyes` may serve you better than `aishaokafor`.

### Patterns to avoid

| Avoid | Example | Why |
|-------|---------|-----|
| The institute or lab name | `crick-aisha`, `smithlab-aisha` | You'll leave, but the name stays |
| Your job title | `postdoc-aisha`, `phd-aokafor` | It'll be out of date in a few years |
| Birth years or random numbers | `aisha1991`, `aokafor4827` | It looks like a spam account and is hard to remember |
| Nicknames and jokes | `mitochondria-queen`, `pipette-ninja` | Fun now, awkward on a grant application |
| Underscores | `aisha_okafor` | Not allowed, so GitHub rejects them |
| Something only you can spell | `aishaokfrrys` | Nobody will find you |

{: .tip }
> **Check whether a name is free** by visiting `https://github.com/NAME-YOU-WANT`.
> If GitHub shows a *404 – page not found* error, it's available (the sign-up form
> also tells you). Have two or three options ready in case your first choice is taken.

{: .note }
> **Already have a GitHub account?** Great. Check that its username passes the
> tests above. If it doesn't and you haven't used it much, now is the best time
> to rename it (**Settings → Account → Change username**). Please don't create a second account.

---

## Step 2: Create the account

1. Go to [github.com/signup](https://github.com/signup).
2. **Email:** use a **personal** email address you'll still have if you change jobs.
   You'll add your institute address as a second email in step 4.
3. **Password:** a long, unique one. A password manager helps.
4. **Username:** the one you chose in step 1.
5. Complete the verification puzzle, then enter the code GitHub emails to you.
   **You must verify your email**, because GitHub won't let you create repositories until you do.
6. If GitHub asks about plans, choose **Free**. You can skip the questions about how you'll use GitHub.

## Step 3: Turn on two-factor authentication (2FA)

2FA means that signing in needs your password **and** a code from your phone.
GitHub requires it for anyone who contributes code, and it will ask you anyway,
so it's easiest to do it now.

1. On your phone, install an **authenticator app**. Microsoft Authenticator,
   Google Authenticator and the one built into most password managers all work.
2. On GitHub, click your profile picture (top right) → **Settings** →
   **Password and authentication** → **Enable two-factor authentication**.
3. Scan the QR code with the app and type in the 6-digit code it shows.
4. **Save your recovery codes.** Download them and keep them somewhere safe
   (a password manager, or printed in a drawer). If you lose your phone, they're the
   only way back into your account.
5. Optional but recommended: add a **passkey** as a backup (same settings page).

## Step 4: Set up your profile

In **Settings → Public profile**:

- **Name:** as you publish it.
- **Profile picture:** a clear photo of your face works best.
- **Bio:** one line, e.g. *Postdoc studying nuclear mechanics · Fiji & Python*.
- **Company / affiliation:** your institute.
- **Social accounts:** add your ORCID URL (e.g. `https://orcid.org/0000-0002-1825-0097`).

In **Settings → Emails**:

- **Add your institute email** as a second address and verify it.
- Leave **Keep my email addresses private** ticked. Changes you make will then show
  a private GitHub address instead of your real email, which reduces spam.

## Step 5: Tell us your username

Send your GitHub username to the course organiser, so we can give you access to
the course templates.

## Step 6: Get access to Claude

Accept the invitation email for the institute's Claude team licence, then sign
in at [claude.ai](https://claude.ai) with your institute email.

**If you'll use Claude Code (Route A):** open [claude.ai/code](https://claude.ai/code),
or the **Code** tab in the Claude desktop app, and follow the prompts to connect GitHub.
When GitHub asks which repositories Claude may access, choose **Only select
repositories**. You'll add each one as you create it during the course.

{: .note }
Menus and button names in Claude and GitHub change from time to time. If
something here doesn't match what you see, look for the nearest equivalent,
and tell us at the start of the session so we can update this page.

---

## Step 7: Learn a little about version control (optional, recommended)

You don't need to know any of this before the course. We cover everything from
scratch in [module 2]({{ '/02-version-control/' | relative_url }}). But a little
reading beforehand makes the sessions much easier to follow. Pick a level:

### ⏱ 15 minutes: why bother?

- **Jenny Bryan, [*Excuse me, do you have a moment to talk about version control?*](https://peerj.com/preprints/3159/)**
  (PeerJ Preprints 2017, later published in *The American Statistician*).
  A friendly, jargon-light case for why researchers should use Git and GitHub. Read
  the introduction and the section on why Git and GitHub matter, and skim the rest.
- **The Turing Way, [*Version Control*](https://book.the-turing-way.org/reproducible-research/vcs/).**
  A short, well-illustrated chapter from a community handbook on reproducible research.

### ⏱ 30–45 minutes: the core ideas (our top recommendation)

- **Blischak, Davenport & Wilson (2016), [*A Quick Introduction to Version Control with Git and GitHub*](https://doi.org/10.1371/journal.pcbi.1004668)**,
  *PLOS Computational Biology*. Written for biologists, and it covers exactly the ideas
  we use in the course: repositories, commits, history, GitHub and collaborating.
- **GitHub Docs, [*Hello World*](https://docs.github.com/en/get-started/start-your-journey/hello-world).**
  A 10–15 minute hands-on walk-through, entirely in the browser: create a repository,
  make a branch, commit a change, and merge a pull request. **If you only do one thing, do this.**

### ⏱ 1 hour: hands-on practice

- **GitHub Skills, [*Introduction to GitHub*](https://github.com/skills/introduction-to-github).**
  An interactive exercise (under an hour) that runs inside GitHub. A bot guides you
  step by step through branches, commits and pull requests as you build a profile README.

### Going further (after the course, if you're curious)

These use the command line, which you **won't** need for the course, because Claude
handles it. They're useful if you want to understand what Claude is doing under the bonnet.

- **Software Carpentry, [*Version Control with Git*](https://swcarpentry.github.io/git-novice/).**
  The standard half-day researcher lesson, with a story about two collaborators.
- **[*Learn Git Branching*](https://learngitbranching.js.org/).** A visual, game-like tool
  that runs in your browser and shows what branches and merges actually do.
- **Perez-Riverol et al. (2016), [*Ten Simple Rules for Taking Advantage of Git and GitHub*](https://doi.org/10.1371/journal.pcbi.1004947)**,
  *PLOS Computational Biology*. Good habits for research projects, several of which are
  built into our templates.
- **[*Pro Git*](https://git-scm.com/book/en/v2).** The free, comprehensive reference book.

---

## Optional: software for later modules

You won't need any of this for modules 1–5, which all happen in the browser.

| Software | Why | Needed for |
|----------|-----|-----------|
| [GitHub Desktop](https://desktop.github.com/) | Copy repositories to your computer without the command line | Module 6 onwards |
| [Fiji](https://imagej.net/software/fiji/) | Image analysis | Module 8 |
| [Miniforge](https://github.com/conda-forge/miniforge) | Python environments (conda) | Python parts of modules 6 and 8 |

If your computer is managed by the institute, you may need to request these through IT.

---

## Checklist

- [ ] Username chosen using the guidance above (and said out loud once!)
- [ ] GitHub account created and email verified
- [ ] Two-factor authentication on, **recovery codes saved**
- [ ] Profile filled in, and institute email added
- [ ] Username sent to the course organiser
- [ ] Signed in to Claude with your institute account (and, for Route A, GitHub connected)
- [ ] At least the *Hello World* walk-through done (recommended)
