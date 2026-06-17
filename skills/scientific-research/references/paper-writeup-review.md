# Paper Writeup And Review

Use this reference for manuscripts, reports, peer-review simulation, revisions, rebuttals, and final integrity checks.

## Default Structure

For empirical papers, use:

```text
Title
Abstract
Introduction
Related Work
Methods
Results
Discussion
Limitations
Ethics, Safety, And AI Use
Conclusion
References
```

For technical reports or evidence briefs, use:

```text
Executive Summary
Question
Methods
Evidence
Findings
Limitations
Recommendations
Disclosure
Appendix
```

## Claim-Evidence Discipline

Every important claim should be traceable to:

- A cited source.
- A user-provided document or dataset.
- A result produced in the current workflow.
- A clearly labeled assumption or hypothesis.

Avoid:

- Inflated novelty claims.
- Unsupported broad generalizations.
- Citations attached to claims they do not support.
- Hiding negative results.
- Overstating benchmark results as real-world impact.

## Internal Review Pass

Review from multiple perspectives:

- Field expert: method validity and contribution.
- Statistician or methods reviewer: design, power, uncertainty, leakage, and robustness.
- Skeptical reviewer: alternative explanations and overclaims.
- Safety and ethics reviewer: privacy, human subjects, dual use, clinical risk, and disclosure.
- Reproducibility reviewer: data, code, commands, environment, and artifact completeness.

Findings should be concrete and ranked by severity.

## Revision Pattern

For each issue:

```text
Issue
Severity
Evidence
Required change
Resolution
Residual risk
```

Keep `revision_log.md` when the user wants a durable artifact.

## AI-Use Disclosure

For publishable scientific artifacts, include disclosure appropriate to the venue. A conservative default:

```text
AI-use disclosure: This artifact was prepared with assistance from an AI system for research planning, drafting, analysis support, and/or editorial review. The human user is responsible for verifying sources, results, interpretations, and compliance with applicable publication, ethics, and institutional requirements.
```

Adjust wording to match the actual workflow and venue rules. Do not claim the work was unaided if AI assistance was used.
