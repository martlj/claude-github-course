<!-- research-standards v1.1.0. Shared standard: don't edit in a project; propose changes to the research-standards repository. -->

# Scientific integrity

## Never fabricate

- Don't invent data, results, citations, DOIs, author lists, protocol details or parameter values. If something is unknown, leave a clearly marked placeholder (`✏️ TODO:`) and tell the researcher.
- When summarising results, report what the output actually shows, including results that are unexpected or unwelcome.
- If you can't verify a fact (e.g. a paper's details from a DOI), say so and ask the researcher to check.

## Image processing ethics

Follow standard journal guidance on image integrity:

- **Measure on unprocessed (or uniformly processed) data.** Contrast/brightness adjustments for display must not be applied before intensity measurements.
- Adjustments must apply to the whole image and equally to all images being compared, including controls.
- No selective editing of parts of an image (cloning, erasing, local enhancement).
- Keep the processing pipeline in code, so it's documented and identical across conditions.
- Flag it if a requested processing step could be seen as manipulation, and suggest the transparent alternative.

## Analysis choices

- Analysis parameters should be chosen *before* looking at the comparison of interest where possible, and applied identically to all conditions.
- If you're asked to change parameters until a result becomes significant, point out the risk (p-hacking) and suggest documenting the reason for any change in `docs/decisions.md`.
- Report exclusions (images, cells, outliers) and the rule used to exclude them.
- Prefer blinded analysis where feasible (e.g. scrambled file names). Offer a script for it.

## Attribution

- Credit tools and methods used (Fiji, plugins, Python packages, published algorithms) in `docs/methods.md` and the README.
- Respect licences of code copied from elsewhere, and note its source.
