# Methodology

## 1. Research Design

This study conducts a structural audit of evidence traceability in AI fact-checking records, using the AVeriTeC benchmark as a case study. Rather than evaluating verdict accuracy alone, the audit examines whether the information documented in each record makes the evidential basis of its assessment visible and inspectable.

The analysis focuses on six dimensions: claim-component coverage, counterevidence, alternative explanations, context and scope, acknowledged uncertainty, and justification-to-evidence linkage.

The unit of analysis is an individual AVeriTeC fact-checking record. The audit evaluates the documentation available in the benchmark record; it does not reconstruct the original fact-checker's complete investigative process, establish the truth of every underlying claim, or directly measure the factual accuracy of the assigned verdict.

## 2. Dataset and Sampling

The study uses the AVeriTeC development dataset. A stratified random sample of 120 records was selected from four verdict categories:

- Supported
- Refuted
- Conflicting Evidence / Cherrypicking
- Not Enough Evidence

The sample contains 30 records from each category, producing an equal allocation across the four strata. Sampling was conducted using a fixed random seed of 42 to support reproducibility.

The sampling script groups records by their original verdict label, randomly selects 30 records from each category, and exports the selected records to an unannotated CSV master sheet. It also retains the original dataset row index to support record-level traceability.

The equal allocation was chosen to enable descriptive comparison across verdict categories. It is not proportional to the distribution of verdicts in the full development dataset and should not be interpreted as a population-representative sample.

## 3. Record Preparation and Annotation

The sampling script extracts the principal record fields, including the claim, claim date, speaker, fact-checking article, original claim URL, and justification. It also extracts the nested questions and answers, together with available source URLs and related source metadata.

The resulting master sheet provides the record-level material for annotation. Two versions are included in the repository:

- `data/ai_annotation_master_sheet.csv`: the unannotated master sheet containing the 120 sampled records.
- `data/ai_annotation_master_sheet_Claude.csv`: the completed annotation sheet containing the model-generated assessments.

All 120 sampled records were annotated using Claude Sonnet 5.5 as a model-assisted annotation instrument. The assessments followed a predefined six-dimensional rubric. The model-generated annotations were treated as analytical outputs to be examined, not as ground truth.

The six dimensions are:

| Dimension | Code | Assessment focus |
|---|---|---|
| Claim-component coverage | CC | Whether the material components of the claim are addressed |
| Counterevidence addressed | CE | Whether relevant contradictory or qualifying evidence is acknowledged |
| Alternative explanations | AE | Whether plausible alternative interpretations are considered |
| Context and scope | CS | Whether relevant temporal, geographical, definitional, and measurement boundaries are documented |
| Uncertainty acknowledged | UA | Whether material limitations and unresolved questions are made explicit |
| Justification-to-evidence linkage | JL | Whether the reasoning connecting evidence to the assessment is traceable |

The full operational definitions and coding guidance are provided in `docs/annotation-rubric.md`.

The annotation process did not include independent human double-coding or a formal inter-annotator reliability assessment. Consequently, the results describe a model-assisted audit and should not be interpreted as independently validated human judgments.

## 4. Coding Scheme

Each record receives one code for each of the six dimensions:

| Code | Meaning | Application |
|---|---|---|
| 1 | Documented coverage | Identifiable documentation addressing the dimension is present |
| 0 | Identifiable omission | The dimension is applicable, but identifiable documentation is absent |
| U | Insufficient information | The available record does not permit a determinate assessment |
| N/A | Not applicable | The dimension does not apply to the record |

The distinction between omission and insufficient information is important. A code of 0 indicates that an applicable element is not identifiable in the available record. A code of U indicates that the record does not provide enough information to determine whether the element is present. N/A is reserved for cases in which the dimension genuinely does not apply.

A code of 0 does not establish that the original fact-checker failed to consider the issue during the investigation. It indicates only that the relevant consideration is not identifiable in the documentation examined.

## 5. Quantitative Analysis

The analysis calculates documented coverage and omission rates separately for each of the six dimensions.

For each dimension j:

- E_j represents the set of records receiving a determinate and applicable binary assessment (0 or 1).
- |E_j| represents the number of records in that set.
- x_ij represents the binary code assigned to record i for dimension j.

**Documented coverage (%)** is calculated as:

```text
C_j = (Number of records coded 1 / |E_j|) × 100
```

Equivalently:

```text
C_j = (Σ x_ij for i ∈ E_j / |E_j|) × 100
```

**Omission rate (%)** is calculated as:

```text
O_j = (Number of records coded 0 / |E_j|) × 100
```

Equivalently:

```text
O_j = (Σ 1(x_ij = 0) for i ∈ E_j / |E_j|) × 100
```

Codes U and N/A are excluded from the binary denominators. Their frequencies should be reported separately to make the extent of indeterminate and non-applicable assessments visible. Because the number of determinate, applicable records may differ across dimensions, each dimension may have a different denominator.

For each dimension, coverage and omission rates sum to 100%, subject to rounding, because the binary denominator contains only codes 0 and 1.

The analysis is descriptive. It summarizes the documentation observed in the sampled records and does not establish causal relationships or support statistical generalization to the entire AVeriTeC dataset.

## 6. Interpretation and Limitations

The audit measures the visibility and traceability of evidence-related documentation in the sampled benchmark records. It does not directly evaluate:

- The factual accuracy of the original verdicts.
- The reliability or independence of every cited source.
- The complete investigative work performed by the original fact-checkers.
- The internal reasoning processes of the original fact-checkers or annotation model.
- The causal effect of evidence-traceability practices on verification performance.

The findings are also subject to limitations arising from the sample design and annotation procedure. The equal-sized strata support descriptive examination across verdict categories but do not reproduce the category distribution of the full dataset. In addition, the annotations were generated using a single AI model and were not independently validated through human double-coding or formal reliability testing.

Accordingly, the results should be interpreted as a structured, model-assisted assessment of the documentation available in a limited set of AVeriTeC records.

The Evidence-Traceable Verification Model (ETVM) is proposed as a conceptual, model-independent framework informed by the audit. It is not implemented or empirically validated in this study. The present analysis therefore does not demonstrate that ETVM improves factual accuracy, evidence retrieval, or verification performance.

## 7. Reproducibility and Research Materials

The repository provides the sampling script, annotation rubric, completed annotation sheet, unannotated master sheet, and ethics statement.

The sampling script is located at `scripts/averitec_audit.py`. It expects the AVeriTeC development dataset to be available locally at `data/dev.json` and uses Python with the pandas package to generate `data/ai_annotation_master_sheet.csv`.

To reproduce the sample, place the development dataset at the expected path, install the required dependency, and run the script:

```bash
pip install pandas
python scripts/averitec_audit.py
```

The script uses random seed 42 and selects 30 records from each of the four specified verdict categories. It checks that the resulting sample contains exactly 120 records, that the selected dataset row indices are unique, and that each category contains 30 records.

The completed Claude annotation sheet is provided separately to make the assessed records and annotations inspectable. Reproducing the sampling procedure does not independently reproduce or validate the model-generated annotations.

The original AVeriTeC benchmark is available at:

https://github.com/MichSchli/AVeriTeC

Quantitative results should be checked against the completed annotation sheet, including the counts of codes 0, 1, U, and N/A, before publication or reuse.
