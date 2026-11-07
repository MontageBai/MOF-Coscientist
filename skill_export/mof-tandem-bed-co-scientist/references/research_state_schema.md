# Research State Schema

Use this file when the user wants iterative optimization, multi-round co-scientist reasoning, experiment logs, manuscript traceability, or reproducible decision records.

## Purpose

Record each co-scientist turn as a structured research state. This prevents the LLM from forgetting why a configuration was recommended, which evidence level supported it, what failed, and how the next experiment was chosen.

The schema should be lightweight enough to use during real experimental work and rigorous enough to support a paper's Methods, Supporting Information, or reviewer response.

For a full per-run audit trail, pair this research state with `run_logging_protocol.md`. The research state records the current scientific state; the run log records the input snapshot, module execution trace, reasoning summaries, evidence links, decision log, metric log, final output snapshot, and human interventions for a specific run.

## Required State Fields

```text
Research State
- project_id:
- date:
- target:
- feed_condition:
- target_recovery_mode:
- objective_priority:
- experiment_budget:
- available_materials:
- current_best_configuration:
- current_evidence_level:
- weakest_evidence_link:
- current_limiting_impurity:
- metric_basis:
- next_experiment:
- decision_rationale:
- overturning_result:
```

## Module-Level State

```text
Module State
- module_1_mixture_role:
  - dominant_impurity_class:
  - specification_limiting_impurity:
  - collection_implication:
- module_2_functional_decomposition:
  - bed_functions:
  - falsification_conditions:
- module_3_candidate_map:
  - function_to_candidates:
  - per_function_priority:
- module_4_calibration:
  - calibrated_functions:
  - observed_breakthrough_order:
  - failure_mode:
- module_5_configuration:
  - material_set:
  - bed_order:
  - mass_ratio:
  - collection_window:
- module_6_perturbation:
  - ratio_migration:
  - sequence_stability:
  - changed_limiting_impurity:
```

## Evidence Log

Every major decision should point to evidence:

```text
Evidence Log Entry
- evidence_id:
- data_type: descriptor / simulation / isotherm / single-component breakthrough / multicomponent breakthrough / serial breakthrough / ratio comparison / replicate
- source_file_or_note:
- condition:
- observation:
- supported_function:
- evidence_level:
- limitation:
```

## Decision Log

Use this when updating recommendations after a new experiment:

```text
Decision Log Entry
- decision_id:
- previous_configuration:
- new_data:
- updated_limiting_impurity:
- function_update:
- recommendation_change:
- why_changed:
- why_not_changed:
- next_experiment:
- biggest_risk:
```

## Metric Log

```text
Metric Log Entry
- metric_name:
- value:
- unit:
- calculation_basis: measured / curve-integral proxy / time-window proxy / qualitative estimate
- integration_window:
- required_raw_data:
- missing_data:
- interpretation:
```

## One-Shot Experiment Record

When only one experiment can be run:

```text
One-Shot Recommendation
- primary_configuration:
- order:
- mass_ratio:
- total_mass:
- collection_window:
- objective_priority:
- expected_gain:
- single_biggest_risk:
- result_that_would_overturn:
- backup_interpretation_if_failed:
```

## Publication Traceability

For each manuscript claim, record:

```text
Claim Trace
- claim:
- supporting_module:
- evidence_level:
- supporting_data:
- metric_basis:
- safe_wording:
- unsupported_extension:
- reviewer_risk:
```

## Update Rules

- Never overwrite the previous best configuration without recording why it changed.
- When new data contradict the current hypothesis, update the function assignment before updating the material ranking.
- When the objective changes, keep the old recommendation and create a new objective-specific state.
- When feed composition changes, re-run Module 1 and Module 6 before changing ratios.
- When a metric is only a proxy, preserve the proxy label in later summaries.
- When a claim moves from Level 3 to Level 4, record the exact ratio, sequence, or replicate evidence.

## Paper-Facing Claim Boundary

Supported claims:
- "The co-scientist maintained a reproducible research state across iterative experiments."
- "Recommendations were updated based on explicit evidence logs and decision rationales."
- "Manuscript claims were linked to evidence levels and metric calculation bases."

Claims not supported by the schema alone:
- "The recommendations are experimentally correct."
- "The configuration is optimized."
- "The workflow is autonomous."

Safe wording:
- Use "traceable decision record", "evidence-linked recommendation", and "iterative research state".
- Avoid implying that a log proves performance without experimental outcome data.
