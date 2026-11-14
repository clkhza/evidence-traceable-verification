# Ethics, Limitations, and Responsible Use

## 1. Scope of the audit

This research examines the traceability of evidence in AI fact-checking records. It evaluates the documentation visible in the records, not the complete internal reasoning or investigative work of the original fact-checkers.

An undocumented consideration should not automatically be interpreted as a consideration that never occurred.

## 2. Model-assisted annotation

All 120 records were annotated using Claude Sonnet 5.5.

Model-assisted annotation introduces potential risks, including:
- Misinterpreting claim components or source passages.
- Missing relevant counterevidence.
- Applying coding criteria inconsistently.
- Treating incomplete documentation as evidence of absence.
- Producing confident assessments where the record is ambiguous.

The annotation results should not be interpreted as independently replicated human judgments. The model used, coding rubric, and annotation outputs are documented to make the procedure inspectable.

## 3. Sampling limitations

The study uses a stratified sample of 120 records, with 30 records from each of four verdict categories.

This design supports comparison across the selected categories, but it does not establish population-wide rates for AVeriTeC or other fact-checking systems.

The findings are descriptive and should not be generalized beyond the scope of the sample without further research.

## 4. Measurement limitations

The six audit dimensions are an operational framework for examining documentation quality. They do not capture every aspect of epistemic quality or investigative rigor.

In particular:
- A well-documented record can still reach an incorrect verdict.
- A poorly documented record may reflect incomplete benchmark reporting rather than poor original investigation.
- Source quantity does not establish source quality.
- Citation presence does not establish evidential support.
- The coding process may involve judgment, especially for ambiguous or context-dependent records.

## 5. Risks of misuse

Evidence-traceability scores could be misused as simple rankings of fact-checkers, sources, or AI systems.

Such interpretations would exceed what this study establishes. The scores should be treated as diagnostic indicators of documentation, not standalone measures of truthfulness, reliability, or institutional quality.

The proposed ETVM framework is a conceptual proposal. Its effectiveness and practical impact require further evaluation.

## 6. Data handling and redistribution

The repository should distinguish original research materials from third-party benchmark content.

The AVeriTeC dataset remains subject to its original licensing and access conditions. The presence of annotations in this repository does not grant permission to redistribute underlying benchmark content.

Before public release, annotation files should be checked for personal information, confidential material, restricted source content, and any data that cannot lawfully or ethically be shared.

## 7. Responsible use

The framework is intended to support more transparent and inspectable AI-assisted verification.

It should complement, not replace:
- Human review of consequential claims.
- Inspection of original sources.
- Contextual and domain-specific expertise.
- Explicit communication of uncertainty.
- Independent evaluation of factual conclusions.

## 8. Future work

Further research should examine:
- Independent human annotation and inter-annotator agreement.
- Replication on larger and more diverse samples.
- Validation of the six dimensions.
- Testing ETVM on real verification workflows.
- Whether improved evidence traceability leads to better human oversight or more reliable verification outcomes.
