# Evidence-Traceable Verification

**Auditing evidence traceability in AI fact-checking**

This project examines how AI fact-checking systems document and connect claims, evidence, sources, and verification judgments. Using AVeriTeC as a case study, it audits the traceability of evidence in a sample of 120 records and proposes the **Evidence-Traceable Verification Model (ETVM)**.

## Research objectives

- Assess how thoroughly fact-checking records document the evidence behind their verdicts.
- Identify gaps in claim coverage, counterevidence, alternative explanations, context, uncertainty, and justification.
- Propose a structured framework for making AI-assisted verification more transparent and auditable.

## Dataset and annotation

The study examines a stratified sample of 120 records from the AVeriTeC development dataset, with 30 records from each of four verdict categories.

The records were annotated using **Claude Sonnet 5.5** across six dimensions:

1. Claim-component coverage (CC)
2. Counterevidence addressed (CE)
3. Alternative explanations (AE)
4. Context and scope (CS)
5. Uncertainty acknowledged (UA)
6. Justification-to-evidence linkage (JL)

The repository includes the completed annotation sheet and a blank annotation template. See [`data/README.md`](data/README.md) for details.

## Proposed framework

ETVM organizes verification around traceable relationships between claims, evidence passages, source provenance, and assessment. It is proposed as a framework for auditability; its effectiveness has not yet been experimentally validated.

## Repository structure

```text
├── README.md
├── CITATION.cff
├── paper/
│   └── paper.pdf
├── docs/
│   ├── methodology.md
│   ├── annotation-rubric.md
│   └── ethics.md
└── data/
    ├── README.md
    ├── ai_annotation_master_sheet_Claude.csv
    └── ai_annotation_master_sheet.csv
```

## Reproducibility and limitations

The methodology, annotation rubric, and data documentation describe the sampling and coding procedures. Reported quantitative results should be interpreted in light of the study's sample size and model-assisted annotation process. The audit evaluates the documentation available in benchmark records, not the complete internal reasoning or investigative process behind the original fact-checks.

## Acknowledgements

This research uses the AVeriTeC benchmark. Please consult the original dataset and its licensing terms before redistributing underlying benchmark materials.

## Author

Hazal Celik — Independent Researcher
