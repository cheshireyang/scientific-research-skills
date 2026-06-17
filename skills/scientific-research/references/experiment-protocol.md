# Experiment Protocol

Use this reference for computational experiments, simulations, benchmarks, observational studies, surveys, and protocol-only lab or clinical planning.

## Protocol Skeleton

```text
Title
Research question
Hypotheses
Study type
Data sources or materials
Variables and measurements
Controls and baselines
Procedure
Analysis plan
Acceptance and falsification criteria
Risks and mitigations
Reproducibility notes
Ethics and approvals
```

## Computational Work

Before running code:

- Inspect the repository or data layout.
- Identify environment requirements.
- Isolate outputs under a task-specific directory.
- Record exact commands and versions when possible.
- Prefer small smoke tests before expensive runs.
- Ask before installing packages, using GPU, launching long jobs, downloading large data, or modifying shared state.

Minimum reproducibility fields:

```text
Command
Working directory
Inputs
Outputs
Environment
Random seeds
Expected runtime
Failure handling
```

## Benchmarks

Include:

- Baseline methods.
- Metrics and why they match the research question.
- Dataset splits and leakage controls.
- Statistical comparison or uncertainty intervals.
- Ablations that distinguish mechanisms.
- Negative controls where feasible.

## Observational Studies

Specify:

- Population and sampling frame.
- Exposure, outcome, and confounders.
- Missing data plan.
- Bias risks.
- Sensitivity checks.
- Causal language limits.

## Surveys And Human Subjects

Do not execute recruitment, intervention, or data collection unless the user provides appropriate approval and the request is limited to writing or analysis support.

For protocol design, include:

- Consent language.
- Privacy and retention plan.
- Risk-benefit assessment.
- Inclusion and exclusion criteria.
- Compensation and coercion considerations.
- Review board or ethics approval requirements.

## Wet Lab, Clinical, And Field Work

Provide high-level protocol structure, safety considerations, literature review, and ethics checklist only. Do not provide operational steps, optimization guidance, or troubleshooting that enables unsafe execution.
