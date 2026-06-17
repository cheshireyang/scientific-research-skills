---
name: scientific-research
description: Use when conducting structured scientific research across domains, including research question formulation, literature grounding, hypothesis generation, experiment or study planning, evidence-guided iteration, data analysis, manuscript/report drafting, peer review simulation, revision, AI-use disclosure, or turning a broad research goal into a rigorous reproducible workflow.
---

# Scientific Research

## Overview

This is a Codex-native research workflow skill. It helps users move from a research goal to evidence, experiments or study protocols, analysis, and a report or manuscript without requiring external model API keys beyond the active Codex environment.

The skill uses structured research workflows for scoping, evidence tracking, candidate exploration, experiment planning, writing, and review.

## Reference Routing

When this skill activates, choose and read the relevant reference files before acting:

- Broad or unclear research request: `references/workflow-map.md`
- Idea generation, ranking, or search over alternatives: `references/hypothesis-exploration.md`
- Literature review, novelty check, or citation grounding: `references/literature-and-novelty.md`
- Experiment, study, survey, benchmark, or protocol design: `references/experiment-protocol.md`
- Dataset, results, statistics, visualization, or evidence synthesis: `references/data-analysis-and-evidence.md`
- Paper, technical report, peer review, rebuttal, or revision: `references/paper-writeup-review.md`
- Human subjects, medical/clinical claims, dual use, wet lab, privacy, safety, or AI disclosure: `references/safety-ethics-and-disclosure.md`

Read more than one reference when the request crosses boundaries. If the user asks only for a quick answer, use the minimum reference set and keep the workflow lightweight.

## Core Workflow

1. Scope the research goal.
   - Restate the research question, target field, intended output, and constraints.
   - Separate known facts, assumptions, unknowns, and user-provided materials.
   - Identify whether the task is literature-only, computational, data-analysis, protocol-only, or manuscript-oriented.

2. Build a research contract.
   - Define the claim or question under investigation.
   - Define acceptance criteria, falsification criteria, required evidence, and expected artifact names.
   - Record limitations early instead of hiding them in the conclusion.

3. Ground the work in evidence.
   - Use available web/search/library access when current or source-backed claims matter.
   - Never invent citations, datasets, results, author names, venue details, or measured values.
   - Maintain an evidence ledger with source, date accessed when relevant, claim supported, confidence, and limitations.

4. Generate and rank hypotheses or plans.
   - Create a small portfolio of candidate hypotheses, methods, or study designs.
   - Score each candidate on novelty, feasibility, evidence fit, risk, expected information gain, and cost.
   - Expand the most promising branch while preserving rejected alternatives and reasons.

5. Execute only appropriate work.
   - For computational work, inspect the workspace, isolate outputs, and run reproducible commands when feasible.
   - For human-subjects, clinical, wet-lab, field, or regulated work, produce a protocol and ethics checklist only unless the user provides evidence of approval and asks for non-actionable writing support.
   - Ask before expensive compute, GPU runs, package installation, destructive edits, large downloads, or use of private data.

6. Analyze and synthesize.
   - Tie every result back to the research contract.
   - Report uncertainty, negative results, robustness checks, and failure modes.
   - Distinguish evidence from inference.

7. Write, review, and revise.
   - Produce the requested artifact: research plan, protocol, evidence brief, manuscript, report, review, rebuttal, or reproducibility package.
   - Run an internal review pass for unsupported claims, citation integrity, methodological weaknesses, safety issues, and missing disclosure.
   - Revise before finalizing when issues are found.

## Required Safety Rules

- Do not request or require external service, model, literature database, or cloud API keys for this skill. Use only tools available in the active Codex session. If a capability is unavailable, state the gap and continue with an offline workflow.
- Do not read or expose secrets such as `.env` files, private keys, tokens, credentials, unpublished private data, or unrelated personal files.
- Do not fabricate literature, data, experiments, peer reviews, or results. Mark speculative content clearly.
- Do not present machine-generated scientific writing as human-authored. Include an AI-use disclosure when producing papers, reports, or publishable research artifacts.
- Do not provide instructions that enable unsafe wet-lab execution, clinical self-experimentation, privacy invasion, or harmful dual-use applications. Redirect to high-level risk analysis, literature review, or safety protocol design.
- Do not run external automation code unless the user explicitly asks, understands the sandboxing risk, and accepts the dependency and credential requirements.

## Artifact Templates

Use these artifact names by default when the user wants files:

- `research_contract.md`: question, scope, assumptions, acceptance criteria, risks, and deliverables.
- `hypothesis_portfolio.json` or `hypothesis_portfolio.md`: candidate ideas, scores, status, evidence, and decisions.
- `evidence_ledger.md`: sources, supported claims, reliability notes, and limitations.
- `experiment_protocol.md`: reproducible computational plan or non-executed study protocol.
- `analysis_report.md`: methods, results, checks, uncertainty, and interpretation.
- `report.md` or `manuscript.md`: final narrative artifact.
- `review.md`: internal peer-review style critique.
- `revision_log.md`: changes made in response to review.

## Quality Gates

Before finalizing, check:

- The answer directly addresses the research contract.
- Every factual or literature claim is either cited, sourced from user-provided material, or marked as an assumption.
- Results are not overstated beyond the method and data.
- Limitations and negative evidence are visible.
- The AI-use disclosure is present for publishable artifacts.
- Computational outputs can be reproduced from the provided commands, environment notes, and input paths.

## Helper Scripts

- `scripts/validate_research_artifacts.py`: validates a research artifact directory for required files, disclosure, and obvious placeholders.
- `scripts/summarize_hypotheses.py`: summarizes a JSON hypothesis portfolio and highlights top-ranked candidates.

Run scripts with Python 3 and no extra dependencies.
