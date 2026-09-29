# Claude + GitHub for Biologists: course materials

Source for the course website: **https://YOUR-ORG.github.io/claude-github-course/**

A hands-on course teaching researchers with little or no coding experience to:

1. use Git and GitHub for version control,
2. build a personal website with GitHub Pages,
3. change it by prompting Claude,
4. use automated tests (link checking) that raise errors and open GitHub Issues,
5. keep Fiji macros and Python scripts in a well-structured, tested analysis repository,
6. use shared standards files so Claude follows the same good practice in every project and for every collaborator,
7. manage research tasks with Issues and Projects.

Companion templates:

- [`personal-website-template`](https://github.com/YOUR-ORG/personal-website-template)
- [`analysis-repo-template`](https://github.com/YOUR-ORG/analysis-repo-template)
- [`research-standards`](https://github.com/YOUR-ORG/research-standards): shared Claude rules, skills and checks, installed in all of the above

## Why a Pages site (and not a wiki or README)?

- **It's version-controlled like everything else.** Changes go through commits
  and pull requests, so the course practises what it teaches. A GitHub wiki is
  a separate repository, with no pull requests or Actions.
- **It's tested.** The same link checker the participants use runs on these
  pages, which gives you a working example to point at.
- **Navigation and search.** The course has nine modules and a reference
  section. A single README gets unwieldy.
- **Anyone can suggest fixes:** participants open an Issue or a pull request.

## Editing

Pages are Markdown files in the repository root (`01-setup.md` …), `reference/`
and `instructor/`. The theme is [Just the Docs](https://just-the-docs.com/),
loaded as a remote theme. Callout boxes use:

```markdown
{: .tip }
Text of the tip.
```

Available callouts: `note`, `tip`, `warning`, `exercise`, `concept`.

Before running the course, follow `instructor/index.md` → *One-off preparation*.

## Licence

Text: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code snippets: MIT.
