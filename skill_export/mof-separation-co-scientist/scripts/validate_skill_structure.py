#!/usr/bin/env python3
"""Validate the MOF separation co-scientist skill structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required to validate SKILL.md frontmatter") from exc


MODULE_FILES = [
    "module_1_mixture_role_analyzer.md",
    "module_2_functional_decomposer.md",
    "module_3_sorbent_screening_engine.md",
    "module_4_experimental_calibration_loop.md",
    "module_5_configuration_optimizer.md",
    "module_6_feed_objective_perturbation.md",
    "module_7_process_validation_engine.md",
]

REFERENCE_FILES = [
    *MODULE_FILES,
    "data_input_contract.md",
    "early_stage_structural_target_protocol.md",
    "material_recommendation_input_protocol.md",
    "molecule_size_reference.md",
    "manual_pore_size_reference.md",
    "mof_pld_lcd_gld_reference.md",
    "oms_reference.md",
    "experimental_controls_uncertainty.md",
    "regeneration_scaleup_tea_protocol.md",
    "metric_requirements.md",
    "co_scientist_evaluation_protocol.md",
    "research_state_schema.md",
    "run_logging_protocol.md",
    "manuscript_methods_si_template.md",
    "reproducibility_reporting_checklist.md",
    "forward_test_protocol.md",
    "seven_module_framework.md",
    "co_scientist_prompt_template.md",
]

SKILL_REQUIRED_SNIPPETS = [
    "module_1_mixture_role_analyzer.md",
    "data_input_contract.md",
    "early_stage_structural_target_protocol.md",
    "material_recommendation_input_protocol.md",
    "molecule_size_reference.md",
    "manual_pore_size_reference.md",
    "mof_pld_lcd_gld_reference.md",
    "oms_reference.md",
    "experimental_controls_uncertainty.md",
    "regeneration_scaleup_tea_protocol.md",
    "co_scientist_evaluation_protocol.md",
    "research_state_schema.md",
    "run_logging_protocol.md",
    "manuscript_methods_si_template.md",
    "reproducibility_reporting_checklist.md",
    "forward_test_protocol.md",
]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def fail(message: str) -> None:
    raise AssertionError(message)


def validate(root: Path) -> list[str]:
    errors: list[str] = []

    skill_path = root / "SKILL.md"
    if not skill_path.exists():
        return ["SKILL.md is missing"]

    skill_text = read_text(skill_path)
    match = re.match(r"^---\n(.*?)\n---\n", skill_text, re.S)
    if not match:
        errors.append("SKILL.md frontmatter is missing or malformed")
    else:
        meta = yaml.safe_load(match.group(1)) or {}
        if meta.get("name") != "mof-separation-co-scientist":
            errors.append("SKILL.md name must be mof-separation-co-scientist")
        if not meta.get("description"):
            errors.append("SKILL.md description is missing")

    refs = root / "references"
    for filename in REFERENCE_FILES:
        if not (refs / filename).exists():
            errors.append(f"missing reference: {filename}")

    for filename in MODULE_FILES:
        path = refs / filename
        if path.exists() and "Paper-Facing Claim Boundary" not in read_text(path):
            errors.append(f"module lacks Paper-Facing Claim Boundary: {filename}")

    for snippet in SKILL_REQUIRED_SNIPPETS:
        if snippet not in skill_text:
            errors.append(f"SKILL.md does not mention {snippet}")

    framework = refs / "seven_module_framework.md"
    if framework.exists():
        framework_text = read_text(framework)
        for snippet in [
            "Module Index",
            "Publication-support protocols",
            "Forward testing",
        ]:
            if snippet not in framework_text:
                errors.append(f"seven_module_framework.md missing '{snippet}'")

    for script in [
        "validate_skill_structure.py",
        "score_forward_test.py",
        "extract_agent_prompt.py",
    ]:
        if not (root / "scripts" / script).exists():
            errors.append(f"missing script: {script}")

    return errors


def main(argv: list[str]) -> int:
    root = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("mof-separation-co-scientist structure ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
