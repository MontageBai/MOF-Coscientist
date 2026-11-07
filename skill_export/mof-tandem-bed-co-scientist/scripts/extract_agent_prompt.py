#!/usr/bin/env python3
"""Extract only the Agent-Facing Prompt from a forward-test fixture."""

from __future__ import annotations

import re
import sys
from pathlib import Path


def extract_agent_prompt(text: str) -> str:
    match = re.search(
        r"## Agent-Facing Prompt\s+```text\s+(.*?)\s+```\s+## Evaluator Rubric",
        text,
        re.S,
    )
    if not match:
        raise ValueError("Could not find a bounded Agent-Facing Prompt before Evaluator Rubric")
    return match.group(1).strip() + "\n"


def main(argv: list[str]) -> int:
    if len(argv) not in {2, 3}:
        print("Usage: extract_agent_prompt.py <fixture.md> [output.txt]", file=sys.stderr)
        return 2

    fixture = Path(argv[1])
    prompt = extract_agent_prompt(fixture.read_text(encoding="utf-8"))

    if len(argv) == 3:
        Path(argv[2]).write_text(prompt, encoding="utf-8")
    else:
        print(prompt, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
