---
paths:
  - "_config.yml"
  - "_layouts/**"
  - "_includes/**"
  - "_data/**"
  - "_sass/**"
  - "assets/**"
  - "*.html"
  - "**/*.html"
---
<!-- research-standards v1.1.0. Shared standard: don't edit in a project; propose changes to the research-standards repository. -->

# Websites (GitHub Pages / Jekyll)

- The site must keep building with GitHub Pages. For "Deploy from a branch" sites, use only [plugins GitHub Pages supports](https://pages.github.com/versions/) and no custom build step. If a change needs a build step, explain the trade-off first.
- Keep styling centralised: colours, fonts and sizes as CSS variables (custom properties) in one place. Don't scatter hard-coded colours.
- **Accessibility:** text contrast at least 4.5:1 (WCAG AA), meaningful `alt` text on every image, headings in order (one `h1` per page), links with descriptive text (not "click here"), and layouts that work on a phone. Warn the researcher if a requested design breaks these.
- Internal links use `{{ '/path/' | relative_url }}` in HTML/Liquid, so they work with any `baseurl`.
- New pages need front matter (`layout`, `title`, `permalink`) and, if they belong in the menu, an entry in the navigation data file.
- Keep images small (resize to display size, ≲ 500 KB each) and put them in `assets/img/`.
- Never publish unverified personal or publication details. Ask the researcher, and check DOIs and author lists.
- Don't include tracking or analytics scripts, or third-party embeds, unless the researcher asks and understands the privacy implications.
- After adding or changing links, the link-check workflow must pass. Only add a site to `.lycheeignore` after the researcher confirms it works in a browser.
