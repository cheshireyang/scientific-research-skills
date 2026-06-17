#!/usr/bin/env python3
"""Validate artifacts produced by the scientific-research skill."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_GROUPS = {
    "research_contract": ["research_contract.md"],
    "hypothesis_portfolio": [
        "hypothesis_portfolio.json",
        "hypothesis_portfolio.md",
        "hypothesis_tree.json",
        "hypothesis_tree.md",
    ],
    "evidence_ledger": ["evidence_ledger.md"],
    "final_report": ["report.md", "manuscript.md", "analysis_report.md"],
}

RECOMMENDED_FILES = ["review.md", "revision_log.md"]

DISCLOSURE_PATTERNS = [
    re.compile(r"\bAI[- ]use disclosure\b", re.IGNORECASE),
    re.compile(r"\bAI[- ]assisted\b", re.IGNORECASE),
    re.compile(r"\bmachine[- ]generated\b", re.IGNORECASE),
    re.compile(r"\bCodex\b", re.IGNORECASE),
    re.compile(r"\bAI system\b", re.IGNORECASE),
]

PLACEHOLDER_PATTERNS = [
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\[citation needed\]", re.IGNORECASE),
    re.compile(r"\blorem ipsum\b", re.IGNORECASE),
]


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="replace")


def find_any(root: Path, names: list[str]) -> Path | None:
    for name in names:
        candidate = root / name
        if candidate.exists():
            return candidate
    return None


def validate_hypothesis_json(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        return [f"{path.name}: invalid JSON at line {exc.lineno}: {exc.msg}"]

    if not isinstance(data, dict):
        return [f"{path.name}: root must be a JSON object"]

    nodes = data.get("nodes")
    if isinstance(nodes, dict):
        node_list = list(nodes.values())
    elif isinstance(nodes, list):
        node_list = nodes
    else:
        return [f"{path.name}: expected 'nodes' as a list or object"]

    if not node_list:
        errors.append(f"{path.name}: contains no nodes")

    for index, node in enumerate(node_list):
        if not isinstance(node, dict):
            errors.append(f"{path.name}: node {index} is not an object")
            continue
        if not node.get("id"):
            errors.append(f"{path.name}: node {index} is missing id")
        if not (node.get("hypothesis") or node.get("title") or node.get("question")):
            errors.append(f"{path.name}: node {node.get('id', index)} lacks hypothesis/title/question")
    return errors


def scan_placeholders(root: Path) -> list[str]:
    warnings: list[str] = []
    for path in sorted(root.glob("*.md")):
        text = read_text(path)
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(text):
                warnings.append(f"{path.name}: contains placeholder pattern '{pattern.pattern}'")
    return warnings


def has_disclosure(root: Path) -> bool:
    candidates = [root / "report.md", root / "manuscript.md", root / "analysis_report.md"]
    text = "\n".join(read_text(path) for path in candidates if path.exists())
    return any(pattern.search(text) for pattern in DISCLOSURE_PATTERNS)


def validate(root: Path) -> dict[str, list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not root.exists():
        return {"errors": [f"root does not exist: {root}"], "warnings": []}
    if not root.is_dir():
        return {"errors": [f"root is not a directory: {root}"], "warnings": []}

    for group, names in REQUIRED_GROUPS.items():
        found = find_any(root, names)
        if found is None:
            errors.append(f"missing {group}: expected one of {', '.join(names)}")

    for name in ("hypothesis_portfolio.json", "hypothesis_tree.json"):
        candidate_path = root / name
        if candidate_path.exists():
            errors.extend(validate_hypothesis_json(candidate_path))

    for name in RECOMMENDED_FILES:
        if not (root / name).exists():
            warnings.append(f"recommended file is missing: {name}")

    if find_any(root, REQUIRED_GROUPS["final_report"]) and not has_disclosure(root):
        warnings.append("final report exists but no AI-use disclosure was detected")

    warnings.extend(scan_placeholders(root))
    return {"errors": errors, "warnings": warnings}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="Artifact directory to validate")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    result = validate(root)

    if args.format == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"Validating: {root}")
        if result["errors"]:
            print("\nErrors:")
            for item in result["errors"]:
                print(f"- {item}")
        else:
            print("\nErrors: none")

        if result["warnings"]:
            print("\nWarnings:")
            for item in result["warnings"]:
                print(f"- {item}")
        else:
            print("\nWarnings: none")

    if result["errors"] or (args.strict and result["warnings"]):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
