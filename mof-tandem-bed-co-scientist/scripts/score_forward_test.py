#!/usr/bin/env python3
"""Score a forward-test report against the co-scientist rubric."""

from __future__ import annotations

import re
import sys
from pathlib import Path


DIMENSIONS = [
    "data conversion",
    "target role",
    "functional decomposition",
    "candidate mapping",
    "calibration",
    "configuration hypothesis",
    "metric discipline",
    "claim discipline",
]

MIN_TOTAL = 18
MIN_CRITICAL = 2
CRITICAL_DIMENSIONS = {
    "configuration hypothesis",
    "metric discipline",
    "claim discipline",
}


def parse_failure_flags(text: str) -> list[str]:
    """Return substantive items listed in the report's Failure Flags section."""
    match = re.search(
        r"^Failure Flags\s*$\s*(.*?)(?=^[A-Z][^\n]*\s*$|\Z)",
        text,
        re.M | re.S,
    )
    if not match:
        return []

    flags: list[str] = []
    for line in match.group(1).splitlines():
        item = re.sub(r"^[-*]\s*", "", line.strip()).strip(" .:").lower()
        if not item or item in {"none", "none observed", "no failure flags"}:
            continue
        if item.startswith(("no ", "not observed", "none ")):
            continue
        flags.append(item)
    return flags


def parse_scores(text: str) -> dict[str, int]:
    scores: dict[str, int] = {}
    for line in text.splitlines():
        normalized = line.strip().strip("|")
        if not normalized or "---" in normalized:
            continue
        parts = [part.strip().lower() for part in normalized.split("|")]
        joined = " ".join(parts)
        for dimension in DIMENSIONS:
            if dimension in joined:
                numbers = [int(n) for n in re.findall(r"\b[0-3]\b", joined)]
                if numbers:
                    scores[dimension] = numbers[0]
    return scores


def score_report(path: Path) -> tuple[bool, list[str]]:
    text = path.read_text(encoding="utf-8")
    scores = parse_scores(text)
    issues: list[str] = []

    for dimension in DIMENSIONS:
        if dimension not in scores:
            issues.append(f"missing score for '{dimension}'")
        elif scores[dimension] == 0:
            issues.append(f"zero score for '{dimension}'")

    total = sum(scores.values())
    if total < MIN_TOTAL:
        issues.append(f"total score {total} is below passing threshold {MIN_TOTAL}")

    for dimension in CRITICAL_DIMENSIONS:
        if scores.get(dimension, -1) < MIN_CRITICAL:
            issues.append(f"critical dimension '{dimension}' is below {MIN_CRITICAL}")

    for flag in parse_failure_flags(text):
        issues.append(f"failure flag reported: {flag}")

    return not issues, issues


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: score_forward_test.py <forward-test-report.md>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    passed, issues = score_report(path)
    if passed:
        print("forward-test report passes rubric gate")
        return 0
    for issue in issues:
        print(f"ERROR: {issue}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
