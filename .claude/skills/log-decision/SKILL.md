---
name: log-decision
description: Record an analysis decision (threshold, parameter, exclusion rule, method choice, tolerance change) as a dated entry in docs/decisions.md. Use whenever a choice that affects results is made or changed, or when the researcher says "note that down".
---
<!-- research-standards v1.0.0 -->

# Log an analysis decision

Add an entry at the **top** of `docs/decisions.md` (create the file with a
short intro if it doesn't exist):

```markdown
## YYYY-MM-DD: <short title>

- **Decision:** what was chosen (with values and units).
- **Why:** the reasoning and the evidence (pilot images, a paper, a comparison).
- **Alternatives considered:** what else was tried or rejected, and why.
- **Checked by:** tests, manual comparison, who reviewed it.
- **Affects:** files and versions (e.g. `fiji/macros/x.ijm` v1.1.0), and whether earlier results need re-running.
- **Links:** issue / pull request numbers.
```

Use today's date. Ask the researcher for the *why* if you don't know it. Don't
invent a justification. Commit it together with the code change it describes.
