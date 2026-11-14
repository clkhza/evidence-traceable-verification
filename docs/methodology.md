# Methodology

## 1. Research design

This study conducts a structural audit of evidence traceability in AI fact-checking records. It uses AVeriTeC as a case study to examine how clearly individual records connect claims, evidence, sources, and verdicts.

The audit focuses on the documentation available in the benchmark records. It does not assess the complete internal reasoning process of the original fact-checkers or independently establish the truth of every underlying claim.

## 2. Dataset and sampling

The study uses the AVeriTeC development dataset.

A stratified sample of 120 records was selected, comprising 30 records from each of four verdict categories:

- Supported
- Refuted
- Conflicting Evidence / Cherrypicking
- Not Enough Evidence

The sampling procedure used random seed 42.

The sample is intended to support a balanced structural examination across verdict categories. It should not be interpreted as a population-representative estimate of all AVeriTeC records or fact-checking systems.

## 3. Annotation procedure

All 120 records were annotated using Claude Sonnet 5.5.

Each record was assessed across six dimensions:

| Dimension | Abbreviation | Assessment focus |
|---|---|---|
| Claim-component coverage | CC | Whether the relevant components of the claim are addressed |
| Counterevidence addressed | CE | Whether evidence that challenges the presented conclusion is acknowledged |
| Alternative explanations | AE | Whether plausible alternative interpretations are considered |
| Context and scope | CS | Whether relevant temporal, geographical, and contextual boundaries are documented |
| Uncertainty acknowledged | UA | Whether limitations and unresolved uncertainty are made explicit |
| Justification-to-evidence linkage | JL | Whether the reasoning connecting evidence to the assessment is traceable |

The completed annotation sheet is `data/ai_annotation_master_sheet_Claude.csv`. The corresponding unannotated records are provided in `data/ai_annotation_master_sheet.csv`.

## 4. Coding scheme

Each dimension uses the following codes:

- **1 — Documented:** The record provides identifiable documentation for the dimension.
- **0 — Omission:** The dimension is applicable, but the record does not provide identifiable documentation.
- **U — Unclear / insufficient information:** The available record does not permit a determinate assessment.
- **N/A — Not applicable:** The dimension does not apply to the record.

A code of 0 represents an omission in the available documentation. It does not establish that the original fact-checker failed to consider the issue during the investigation.

## 5. Quantitative analysis

For each dimension, coverage is calculated using records with determinate binary assessments (0 or 1).

Let \(E_j\) denote the set of records with an applicable and determinate code for dimension \(j\). Let \(x_{ij}\) be the binary code for record \(i\) and dimension \(j\).

**Coverage:**

\[
C_j = \frac{\sum_{i \in E_j} x_{ij}}{|E_j|}
\]

**Omission rate:**

\[
O_j = \frac{\sum_{i \in E_j} \mathbb{1}(x_{ij}=0)}{|E_j|}\times 100
\]

Codes U and N/A are excluded from these binary denominators and should be reported separately. Each dimension may therefore have a different denominator.

## 6. Interpretation

The audit measures the traceability and completeness of documentation in the sampled records. It does not directly measure factual accuracy, source reliability, or the quality of the original investigative process.

The results should be interpreted as descriptive findings from a limited sample and a model-assisted annotation procedure. They do not establish causal relationships or demonstrate that the proposed ETVM framework improves verification performance.

## 7. Reproducibility

The repository provides the annotation sheets, coding rubric, and methodological documentation to support inspection of the procedure. Quantitative results should be checked against the completed annotation sheet before publication or reuse.
