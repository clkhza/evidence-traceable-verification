### Coverage and Omission Calculations

For each dimension \(j\), let \(E_j\) denote the set of records with a determinate and applicable annotation (coded as either 0 or 1). Let \(x_{ij}\) represent the annotation for record \(i\) on dimension \(j\).

Documented coverage (%) is calculated as:

\[
C_j = \left( \frac{\sum_{i \in E_j} x_{ij}}{|E_j|} \right) \times 100
\]

The omission rate (%) is:

\[
O_j = \left( \frac{\sum_{i \in E_j} \mathbb{1}(x_{ij}=0)}{|E_j|} \right) \times 100
\]

Annotations coded as U (insufficient information) or N/A (not applicable) are excluded from both calculations and reported separately. Therefore, coverage and omission rates sum to 100% for each dimension, subject to rounding.
