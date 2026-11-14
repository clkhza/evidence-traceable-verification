
# Data

This directory contains the annotation materials used in the structural audit of AVeriTeC.

## Files

### `ai_annotation_master_sheet_Claude.csv`

The completed annotation sheet containing Claude Sonnet 5.5 assessments of the 120 sampled AVeriTeC records across six dimensions:

- CC: Claim-component coverage
- CE: Counterevidence addressed
- AE: Alternative explanations
- CS: Context and scope
- UA: Uncertainty acknowledged
- JL: Justification-to-evidence linkage

### `ai_annotation_master_sheet.csv`

The unannotated master sheet containing the same 120 sampled records, with annotation fields left empty. It provides the corresponding starting point for reviewing or reproducing the annotation process.

## Dataset source

The records originate from the AVeriTeC development dataset.

Original benchmark:
https://github.com/MichSchli/AVeriTeC

## Annotation codes

- `1`: Documented coverage
- `0`: Identifiable omission
- `U`: Insufficient information
- `N/A`: Not applicable

Codes `U` and `N/A` are excluded from binary coverage and omission calculations and are reported separately.

## Important note

Claude Sonnet 5.5 was used as an annotation instrument, not as ground truth. The annotations were not independently validated through human double-coding or formal inter-annotator reliability testing.
