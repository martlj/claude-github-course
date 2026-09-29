---
title: 3. Your website
nav_order: 3
permalink: /03-website/
---

# 3. Create your website
{: .no_toc }

You'll make your own copy of the website template, publish it, and make your
first commit by hand, so you know what Claude will be doing for you later.
{: .fs-5 }

1. TOC
{:toc}

---

## Create your repository from the template

1. Open the [personal website template](https://github.com/YOUR-ORG/personal-website-template).
2. Click the green **Use this template** button, then **Create a new repository**.
3. **Owner:** you. **Repository name:** `YOUR-USERNAME.github.io`, with your
   username exactly as it appears, in lower case.
4. Choose **Public**. Free GitHub Pages sites must be public.
5. Click **Create repository**.

{: .warning }
If the name isn't exactly `your-username.github.io`, the site still works but
lives at a longer address (`your-username.github.io/repo-name`), and the
internal links in this template will break. The link checker in module 5 will spot it.

## Turn on GitHub Pages

1. In your new repository, go to **Settings → Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Choose branch **main**, folder **/ (root)**, and click **Save**.
4. Open the **Actions** tab. You'll see a *pages build and deployment* run. When
   it turns green ✅ (about a minute), visit `https://YOUR-USERNAME.github.io`.

🎉 You have a website. It still says "Your Name", so let's fix that.

## A tour of the files

| File | What it controls |
|------|------------------|
| `_config.yml` | Your name, title, email, profile links |
| `index.md` | The home page |
| `research.md`, `publications.md`, `code.md` | The other pages |
| `_data/navigation.yml` | The menu |
| `assets/css/style.css` | Colours, fonts and layout |
| `CLAUDE.md` | Facts about your site that Claude reads before changing anything |
| `.claude/`, `STANDARDS.md` | Shared lab standards that Claude follows (module 7) |

Files ending `.md` are **Markdown**: plain text with light formatting
(`**bold**`, `*italic*`, `- lists`, `## headings`). GitHub turns them into web pages.

## Your first commit (by hand)

1. Click `_config.yml`, then the **pencil icon** ✏️ (*Edit this file*).
2. Change `title: Your Name` to your name, and update `tagline` and `email`.
3. Click **Commit changes…**.
4. Write a message such as `Add my name and job title`. Leave **Commit directly
   to the main branch** selected, and confirm.
5. Wait for the Actions run to go green, then refresh your site.

{: .tip }
Press the `.` key while viewing your repository to open **github.dev**, a
full editor in the browser. It's handy for editing several files in one commit.

## Look at the history

1. Go back to the repository's front page and click **Commits** (the clock icon near the top right of the file list).
2. Click your commit. You'll see its **diff**: red lines removed, green lines added.

{: .exercise }
> Make **two more commits by hand**: edit the *About me* paragraph in
> `index.md`, and add one research interest. Use a clear message each time.
> Then open the commit history and find each change.

{: .concept }
> Every change to your website is now recorded. If you (or Claude) break
> something, you can see exactly what changed and undo it.
