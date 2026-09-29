---
name: start-analysis
description: Plan a new image or data analysis with a researcher before any code is written. Use when someone describes a new analysis they want ("I want to count...", "measure...", "quantify...") or asks where to start.
---
<!-- research-standards v1.1.0 -->

# Start a new analysis

Turn a researcher's idea into a clear, checkable plan, recorded as a GitHub
issue, **before** writing code.

## Steps

1. **Interview.** Ask only what you don't already know, in one message, grouped:
   - *Question:* what biological question does this answer? What comparison matters?
   - *Images/data:* dimensions, channels (and what each shows), pixel size, format, roughly how many files, and where they're stored.
   - *Objects:* what counts as one, typical size and number, any difficult cases (touching, dim, debris).
   - *Output:* what numbers, at what level (per object/cell/image/condition), and in what format.
   - *Validation:* how will we know it's right (hand counts, controls, expected range)?
   Ask for a screenshot of a typical image and a hard one if the tool allows it.
2. **Propose an approach** in plain language: 3–6 steps, the tool (Fiji macro, Python or both), key parameters and the main risks. Offer a simpler and a more robust alternative if there's a real choice.
3. **Agree a validation plan:** a known-answer test on synthetic data, plus a small manual-annotation set (3–10 images, including hard ones).
4. **Record it** as a GitHub issue using the *Analysis task* template if present. Otherwise, use a body with the headings Question, Images, Output, Validation, Approach and a task checklist. If you can't create issues, give the researcher the text to paste.
5. **Stop and confirm** before writing code. Then suggest the next skill: `new-fiji-macro` or `new-python-script`.
