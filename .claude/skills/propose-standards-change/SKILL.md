---
name: propose-standards-change
description: Help a researcher propose a change or addition to the shared research standards (a rule, skill, template, check or new project type) and submit it as an issue on the upstream research-standards repository. Use when someone says the standards should change, something is missing, a rule got in the way, or they want to suggest a convention.
---
<!-- research-standards v1.1.0 -->

# Propose a change to the shared standards

Help the researcher turn an idea into a clear proposal that the maintainers can
review. **Don't edit the shared files in this project.** The proposal goes upstream.

## Steps

1. **Understand the idea.** Ask what prompted it: a real situation, a mistake that
   happened, something a collaborator did differently, a journal or funder requirement.
   A concrete example is the most persuasive part of any proposal.
2. **Check what already exists.** Read `.claude/rules/`, `.claude/skills/` and
   `STANDARDS.md` here. Tell the researcher if the idea is already covered, partly
   covered, or conflicts with an existing rule, and quote the relevant lines.
3. **Decide where it belongs**, and explain the choice:
   - *Shared standard:* useful to most projects and most people. Propose upstream.
   - *Project exception:* only this project needs it. Suggest adding it to this project's
     `CLAUDE.md` instead, and offer to do that now. It can still be proposed upstream too.
   - *Personal preference:* suggest `CLAUDE.local.md`.
4. **Classify the proposal:** new or changed **rule** · new or changed **skill** · new
   **check** (automated test) · new **template or profile** (e.g. for R, CellProfiler,
   napari or MATLAB projects) · **documentation** fix · **removal** of something unhelpful.
5. **Draft it** using the headings of the upstream *Propose a change* issue template:
   - **Summary:** one sentence.
   - **Type:** from step 4.
   - **Problem or motivation:** what happens now and why it's a problem, with the example.
   - **Proposed wording or behaviour:** the actual text of the rule or the steps of the
     skill. Keep rules short, imperative and checkable (see "Writing good rules" below).
   - **Who it affects:** all projects, or only some (e.g. only Python, or only imaging).
   - **Could it be checked automatically?** Suggest how, if so.
   - **Costs and downsides:** extra effort, conflicts, and projects where it wouldn't fit.
   - **Alternatives considered.**
6. **Show the draft to the researcher** and revise until they're happy.
7. **Submit it.** Read the upstream address from `source:` in
   `.claude/research-standards.yml`. If you can create issues there (e.g. `gh issue create
   --repo OWNER/research-standards --label proposal`), do so and give the link. Otherwise,
   give the researcher the finished text and the link `<source>/issues/new/choose`, so they
   can paste it into the *Propose a change* form.
8. **Set expectations.** Maintainers review proposals, may ask questions, and may decline
   or adapt them. Declined proposals are still useful: the reasons are recorded in the issue.

## Writing good rules

- One idea per rule, with specific and checkable wording ("Name image files
  `YYYY-MM-DD_sample_condition_rep.ext`", not "use sensible names").
- Give the reason when it isn't obvious.
- Every line of a rule is read in every session of every project, so keep it short.
  Put long procedures in a skill, and language-specific advice in a path-scoped rule.
- No project names, people, paths or anything institute-specific that won't apply everywhere.
