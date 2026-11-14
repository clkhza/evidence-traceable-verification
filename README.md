# Evidence-Traceable Verification

**Auditing evidence traceability in AI fact-checking**

## Overview

This project investigates how AI fact-checking records document the relationship between claims, evidence, sources, and verification judgments. Using the AVeriTeC benchmark as a case study, it conducts a structural audit of 120 records and introduces the **Evidence-Traceable Verification Model (ETVM)**, a proposed framework for more transparent and auditable verification.

## Research objectives

- Examine how effectively fact-checking records document the evidence supporting their verdicts.
- Identify documentation gaps across six dimensions of evidence traceability.
- Develop a structured framework for representing and auditing evidence-to-claim relationships.

## Dataset and annotation

The study uses a stratified sample of 120 records from the AVeriTeC development dataset, comprising 30 records from each of four verdict categories:

- Supported
- Refuted
- Conflicting Evidence / Cherrypicking
- Not Enough Evidence

All 120 records were annotated using **Claude Sonnet 5.5** across six dimensions:

| Dimension | Code |
|---|---|
| Claim-component coverage | CC |
| Counterevidence addressed | CE |
| Alternative explanations | AE |
| Context and scope | CS |
| Uncertainty acknowledged | UA |
| Justification-to-evidence linkage | JL |

The `data/` directory contains the completed Claude annotation sheet and the corresponding unannotated records. See [`data/README.md`](data/README.md) for details.

## Evidence-Traceable Verification Model (ETVM)

ETVM proposes a structured approach to connecting claims with evidence passages, source provenance, evidential relationships, and verification assessments. Its purpose is to make the basis of a verification judgment easier to inspect and audit.

ETVM is a proposed framework; its effectiveness has not yet been empirically validated.

## Repository structure

```text
evidence-traceable-verification/
├── README.md
├── CITATION.cff
├── data/
│   ├── README.md
│   ├── ai_annotation_master_sheet_Claude.csv
│   └── ai_annotation_master_sheet.csv
└── docs/
    ├── methodology.md
    ├── annotation-rubric.md
    └── ethics.md
```

## Reproducibility and limitations

The repository documents the sampling procedure, annotation criteria, and coding scheme. The findings are descriptive and should be interpreted in light of the sample size and model-assisted annotation process.

The audit evaluates the evidence documentation available in benchmark records. It does not establish the factual accuracy of every verdict or reconstruct the complete investigative process behind the original fact-checks.

## Acknowledgements

This research uses the [AVeriTeC benchmark](https://github.com/MichSchli/AVeriTeC). The original dataset remains subject to its own licensing and access conditions. Users should consult those terms before redistributing benchmark materials.

## Author

**Hazal Celik**  
Independent Researcher
