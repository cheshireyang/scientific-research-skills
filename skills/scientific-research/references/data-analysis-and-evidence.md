# Data Analysis And Evidence

Use this reference for datasets, statistical analysis, model evaluation, visualizations, and result interpretation.

## Analysis Plan

Before analysis, define:

- Unit of analysis.
- Outcome variables.
- Predictors, interventions, or groups.
- Inclusion and exclusion rules.
- Missing data treatment.
- Primary and secondary metrics.
- Robustness checks.
- How uncertainty will be reported.

## Data Integrity Checks

Check for:

- Source and license.
- Duplicate records.
- Missingness patterns.
- Outliers and impossible values.
- Label leakage.
- Train/test contamination.
- Time ordering errors.
- Measurement drift.
- Privacy or re-identification risk.

## Statistical Discipline

- Do not infer causality from correlation without design support.
- Report effect sizes, uncertainty, and sample sizes.
- Correct or qualify multiple comparisons when relevant.
- Distinguish exploratory from confirmatory analysis.
- Treat non-significant results as evidence with uncertainty, not as proof of no effect.

## Model And Benchmark Evaluation

Include:

- Baselines.
- Data splits and seeds.
- Confidence intervals or repeated runs when feasible.
- Error analysis by subgroup or case type.
- Ablations.
- Failure examples.
- Resource and runtime reporting.

## Evidence Synthesis

For each finding, map:

```text
Finding | Evidence | Method | Uncertainty | Alternative explanation | Confidence
```

Confidence should be calibrated:

- High: converging high-quality evidence, direct measurement, strong controls.
- Medium: plausible evidence with some limitations.
- Low: indirect evidence, small sample, missing controls, or strong assumptions.

## Visualization

Use charts to answer specific questions:

- Trend: line chart with uncertainty if available.
- Distribution: histogram, density, box, or violin plot.
- Comparison: bar or dot plot with intervals.
- Relationship: scatter with careful scaling and sample size.
- Composition: stacked chart only when parts of a whole are clear.

Avoid charts that hide uncertainty or imply precision the data does not support.
