---
title: 5. Testing
nav_order: 5
permalink: /05-testing/
---

# 5. Testing: let the computer check for you
{: .no_toc }

1. TOC
{:toc}

---

## Why test?

When you change a protocol, you run a control. **Automated tests are controls
for code.** They're small checks that run every time something changes and
shout if the result is wrong.

For a website the most common problem is a **broken link**. Maybe you mistyped
a URL, renamed a page, or another site moved a paper. Your template already
has a test that checks every link.

## How the link checker works

The file `.github/workflows/check-links.yml` is a **GitHub Actions workflow**:
instructions GitHub follows on its own computers. Open it and read the comments.
It runs:

- on every push to `main`,
- on every **pull request**, before you merge,
- **every Monday morning**, because other people's websites change even when yours doesn't,
- whenever you click **Run workflow** on the Actions tab.

Each time, it builds your site, visits every link, and then:

| Result | What you see |
|--------|--------------|
| All links fine | Green ✅ next to the commit / on the pull request |
| Something broken | Red ❌ **and** a new **Issue** titled *Broken links found on the website*, listing each broken link and the page it's on |

{: .concept }
> A test doesn't just fail quietly: it **tells you** (red ❌, and an email from
> GitHub) and **leaves a record** (an Issue) that stays open until someone fixes the problem.

## Exercise: break it on purpose

{: .exercise }
> 1. Edit `code.md` by hand and add a link with a typo:
>    `[Fiji](https://imagej.net/software/fijj/)`. Commit it straight to `main`.
> 2. Open the **Actions** tab and watch the **Check links** run. It goes red ❌.
> 3. Click into the run, then the **Check every link** step, and find the broken URL in the log.
> 4. Open the **Issues** tab. There's a new issue listing the broken link. Note its number, e.g. **#1**.
> 5. Fix it **with Claude**:
>    - *Route A:* "Fix the broken link reported in issue #1. Put 'Fixes #1' in the commit message."
>    - *Route B:* paste `code.md` into Claude, ask it to fix the link, commit with the message `Fix Fiji link (Fixes #1)`.
> 6. Once merged, the checker runs again and goes green ✅, and issue #1 **closes automatically**
>    because of the words `Fixes #1`.

## Exercise: catch it *before* it goes live

{: .exercise }
> Ask Claude to add a link to a page that doesn't exist:
>
> > Add a link to my Teaching page at the bottom of the home page.
>
> …*before* you've created the Teaching page (or delete it first). Open the pull request
> and watch the check fail **on the pull request**, before anything reaches your live site.
> Don't merge it. Ask Claude to fix it in the same pull request, then watch the check go green.

This is why we prefer pull requests: **the test runs before the change goes live.**

## When the test is wrong

Some websites (LinkedIn is the usual culprit) block automated checkers
but work fine in a browser. If you've checked a link by hand and it works, add
the site to `.lycheeignore`.

{: .warning }
Don't "fix" a failing test by switching it off. Claude has been told not to do
this (see `.claude/rules/05-testing.md`), and you shouldn't either. A test you've silenced can't
protect you.

## Beyond links

The same idea scales up. In [module 6]({{ '/06-analysis-repo/' | relative_url }}),
your analysis repository comes with tests that check:

- the nuclei-counting script finds **exactly 6 nuclei** in a synthetic image where we *know* there are 6;
- every Fiji macro has a proper header describing what it does;
- nobody has accidentally committed a 2 GB `.czi` file.

Every repository also has a **Standards** check, which makes sure the shared
standards files are present and unedited ([module 7]({{ '/07-standards-files/' | relative_url }})).
