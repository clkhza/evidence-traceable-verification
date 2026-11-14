# Annotation Data

This directory contains the annotation materials used in the evidence-traceability audit.

## Files

### `ai_annotation_master_sheet_Claude.csv`

Contains the completed annotations for the 120 sampled AVeriTeC records.

- Annotation model: Claude Sonnet 5.5
- Sample size: 120 records
- Verdict categories: 30 records per category
- Audit dimensions: CC, CE, AE, CS, UA, and JL

This file represents the completed model-assisted annotation output used in the study.

### `ai_annotation_master_sheet.csv`

Contains the unannotated version of the sampled records, preserving the original record information and annotation columns without completed annotation entries.

It can be used as the starting point for future annotation, replication, or extension of the study.

## Coding reference

The annotation codes are:

| Code | Meaning |
|---|---|
| 1 | Documented |
| 0 | Omission |
| U | Unclear / insufficient information |
| N/A | Not applicable |

See [`../docs/annotation-rubric.md`](../docs/annotation-rubric.md) for the full coding definitions.

## Data interpretation

The annotations evaluate evidence traceability in the information available in each benchmark record. They do not independently establish the truth of the underlying claims or measure the complete investigative process.

Quantitative results should be interpreted alongside the methodology and limitations described in the research paper.

## Data provenance and access

The study uses the AVeriTeC development dataset. The original benchmark is available at:

https://github.com/MichSchli/AVeriTeC

The original dataset's licensing and access conditions remain applicable. This repository does not grant additional redistribution rights for third-party benchmark content.

Before public distribution, ensure that both annotation files comply with the relevant dataset terms and contain no restricted or confidential information.
