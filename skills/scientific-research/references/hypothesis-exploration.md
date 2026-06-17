# Hypothesis Exploration

Use this reference for idea generation, research planning, method selection, and iterative exploration.

## Candidate Schema

Represent each candidate as:

```json
{
  "id": "H1",
  "parent": null,
  "hypothesis": "Concise claim or method idea",
  "rationale": "Why this candidate is plausible",
  "evidence_for": [],
  "evidence_against": [],
  "tests": [],
  "risks": [],
  "scores": {
    "novelty": 0,
    "feasibility": 0,
    "evidence_fit": 0,
    "risk": 0,
    "expected_information_gain": 0,
    "cost": 0
  },
  "status": "open"
}
```

Use 1 to 5 scores unless the user specifies another scale. Higher `risk` and `cost` are worse.

## Candidate Generation

Generate candidates from multiple angles:

- Mechanism: what process could explain the phenomenon?
- Intervention: what controllable change could improve the outcome?
- Measurement: what proxy, benchmark, or metric would reveal the effect?
- Boundary: where should the claim fail?
- Negative result: what would disconfirm the attractive story?
- Simpler baseline: what mundane explanation must be ruled out?

## Ranking Formula

Use a transparent heuristic:

```text
priority = novelty + feasibility + evidence_fit + expected_information_gain - risk - cost
```

Do not treat the score as objective. Use it to make tradeoffs visible.

## Expansion Policy

- Start with 3 to 7 diverse root candidates.
- Expand the highest-priority candidate into specific tests, mechanisms, and failure modes.
- Keep at least one conservative baseline candidate.
- Keep at least one adversarial candidate that could invalidate the preferred direction.
- Mark nodes as `open`, `expanded`, `rejected`, `deferred`, or `selected`.

## Good Exploration Behavior

- Prefer candidates that can be tested with available evidence.
- Prefer experiments that distinguish between competing explanations.
- Reward negative controls and robustness checks.
- Penalize ideas that need inaccessible data, unclear measurement, or unsafe execution.
- Avoid optimizing for novelty alone.

## Output Pattern

For short answers, provide a table. For file artifacts, produce `hypothesis_portfolio.json` and optionally a short `hypothesis_portfolio.md` summary.
