<!-- research-standards v1.1.0. Shared standard: don't edit in a project; propose changes to the research-standards repository. -->

# Data management

## Code in Git, data on storage

- **Never commit raw or processed research data** (microscopy images, sequencing files, large tables) to Git. Git history is permanent: a committed file stays in the history even after deletion.
- Record *where* data lives in `data/README.md`: storage path or database ID (e.g. OMERO project/dataset), acquisition date, instrument and key settings, and who to ask.
- Only tiny, non-sensitive example files (≲ 5 MB total, ideally synthetic) may be committed, in `data/sample/`, to support tests and examples.
- Outputs go in `results/` (ignored by Git) and must be regenerable from code plus data.
- Keep `.gitignore` rules for data, image formats and results. Never remove them to "make a commit work".

## Sensitive and personal data

- Never put personal data (patient/donor identifiers, names linked to samples, animal licence details), credentials or unpublished collaborator data into the repository, issues, pull requests or commit messages.
- If you find such data already committed, stop, tell the researcher, and recommend they contact their data-protection or research-computing team. Deleting the file doesn't remove it from history.
- Follow the institute's policy on which data may be shared with AI tools. If unsure, ask before reading or uploading data files.

## Raw data is read-only

- Code must never modify, overwrite, move or delete raw data. Read from the raw location, write to `results/` or another output folder.
- Output file names should make clear what produced them (script name, date or version).

## Metadata and units

- Keep pixel size, time interval, channel names and units alongside results (in the CSV columns or a sidecar file), not only in someone's head.
- Prefer open, documented formats for outputs: CSV/TSV for tables, OME-TIFF/OME-Zarr for images, PNG/SVG/PDF for figures.
