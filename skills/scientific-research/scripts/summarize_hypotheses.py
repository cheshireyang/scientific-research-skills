#!/usr/bin/env python3
"""Summarize a JSON hypothesis portfolio for scientific-research artifacts."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


def load_nodes(path: Path) -> list[dict[str, Any]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON at line {exc.lineno}: {exc.msg}") from exc

    if not isinstance(data, dict):
        raise SystemExit("Expected a JSON object with a 'nodes' field")

    nodes = data.get("nodes")
    if isinstance(nodes, dict):
        values = list(nodes.values())
    elif isinstance(nodes, list):
        values = nodes
    else:
        raise SystemExit("Expected 'nodes' to be a list or object")

    normalized: list[dict[str, Any]] = []
    for index, node in enumerate(values):
        if not isinstance(node, dict):
            raise SystemExit(f"Node {index} is not an object")
        normalized.append(node)
    return normalized


def node_score(node: dict[str, Any]) -> float:
    if "priority" in node:
        return as_float(node["priority"])
    if "score" in node:
        return as_float(node["score"])

    scores = node.get("scores")
    if not isinstance(scores, dict):
        return 0.0

    positive = (
        as_float(scores.get("novelty"))
        + as_float(scores.get("feasibility"))
        + as_float(scores.get("evidence_fit"))
        + as_float(scores.get("expected_information_gain"))
    )
    negative = as_float(scores.get("risk")) + as_float(scores.get("cost"))
    return positive - negative


def as_float(value: Any) -> float:
    try:
        if value is None:
            return 0.0
        return float(value)
    except (TypeError, ValueError):
        return 0.0


def text_field(node: dict[str, Any]) -> str:
    value = node.get("hypothesis") or node.get("title") or node.get("question") or ""
    return str(value).replace("\n", " ").replace("|", "\\|").strip()


def truncate(text: str, limit: int = 120) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3].rstrip() + "..."


def print_summary(nodes: list[dict[str, Any]], top: int) -> None:
    statuses = Counter(str(node.get("status", "unknown")) for node in nodes)
    ranked = sorted(nodes, key=node_score, reverse=True)

    print("# Hypothesis Summary")
    print()
    print(f"- Nodes: {len(nodes)}")
    if statuses:
        status_text = ", ".join(f"{name}: {count}" for name, count in sorted(statuses.items()))
        print(f"- Statuses: {status_text}")
    print()
    print("## Top Candidates")
    print()
    print("| Rank | ID | Priority | Status | Parent | Hypothesis |")
    print("| ---: | --- | ---: | --- | --- | --- |")

    for rank, node in enumerate(ranked[:top], start=1):
        node_id = str(node.get("id", ""))
        parent = "" if node.get("parent") is None else str(node.get("parent"))
        status = str(node.get("status", "unknown"))
        print(
            f"| {rank} | {node_id} | {node_score(node):.2f} | "
            f"{status} | {parent} | {truncate(text_field(node))} |"
        )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to hypothesis_portfolio.json")
    parser.add_argument("--top", type=int, default=5, help="Number of top candidates to print")
    args = parser.parse_args(argv)

    if args.top < 1:
        raise SystemExit("--top must be at least 1")

    path = Path(args.input).resolve()
    if not path.exists():
        raise SystemExit(f"Input does not exist: {path}")

    print_summary(load_nodes(path), args.top)
    return 0


if __name__ == "__main__":
    sys.exit(main())
