# Workflow Map

Use this reference when a request is broad, ambiguous, or spans the full research lifecycle.

## Research Modes

- Literature-only: answer, review, or evidence brief grounded in sources.
- Computational: code, data, benchmarks, simulations, reproducible outputs.
- Observational: study design around existing or collected observations.
- Human-subjects or clinical: protocol, ethics, consent, and risk review only unless approvals are already in place and the task is non-operational.
- Manuscript/report: structured writing, review, revision, disclosure, and reproducibility package.

## Stage Map

1. Intake
   - Identify field, audience, time horizon, artifact type, and constraints.
   - Ask only for missing information that blocks progress. Otherwise state assumptions and proceed.

2. Research contract
   - Question or claim.
   - Scope and exclusions.
   - Evidence required to support, weaken, or falsify the claim.
   - Deliverables and file names.
   - Safety, ethics, privacy, and resource constraints.

3. Evidence grounding
   - Search or inspect sources when factual accuracy, literature currency, or legal/medical/policy relevance matters.
   - Record source quality, not just source existence.
   - Track contradictions and uncertainty.

4. Hypothesis search
   - Generate candidates.
   - Score candidates.
   - Expand promising branches.
   - Preserve rejected branches and reasons.

5. Protocol or execution
   - For executable computational work, make commands reproducible and isolate outputs.
   - For regulated or physical-world work, produce protocol and ethics artifacts rather than executing.

6. Analysis
   - Validate data provenance, assumptions, leakage risks, and uncertainty.
   - Separate measured results from interpretation.

7. Communication
   - Match the output to the audience: brief, plan, report, manuscript, review, or reproducibility package.
   - Add AI-use disclosure for publishable artifacts.

## Default Artifact Directory

When the user wants files, create a directory such as:

```text
research_artifacts/<slug>/
```

Recommended contents:

```text
research_contract.md
hypothesis_portfolio.json
evidence_ledger.md
experiment_protocol.md
analysis_report.md
report.md
review.md
revision_log.md
```

Use only the files needed for the task.

## Stop Conditions

Pause and ask before:

- Installing dependencies.
- Running expensive compute, GPU jobs, or large downloads.
- Reading private or sensitive data not clearly supplied for the task.
- Executing external automation code.
- Moving from protocol design to real-world human, animal, clinical, field, or wet-lab action.
