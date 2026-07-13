# Run Logging Protocol

Use this file whenever the co-scientist performs analysis, generates a recommendation, updates a research state, prepares manuscript text, or runs an evaluation. The goal is to preserve a reproducible trace of what was provided, what modules were applied, what evidence supported each decision, and what final output was produced.

## Boundary

The log should capture traceable reasoning summaries, decisions, evidence, assumptions, and outputs. It should not claim to contain the model's private hidden chain of thought. Use "reasoning summary", "decision rationale", or "traceable decision record" rather than "full internal thought process".

## Default Log Location

If the user provides a project folder, write logs under:

```text
logs/
```

Recommended filename:

```text
co_scientist_run_YYYYMMDD_HHMMSS.md
```

For iterative projects, also maintain or update:

```text
logs/research_state_latest.md
```

If file writing is not available, include the same log structure in the response so the user can save it.

## Required Log Sections

```text
# Co-Scientist Run Log

## Run Metadata
- run_id:
- date_time:
- skill_name:
- skill_version_or_path:
- model_name_if_available:
- user_request:
- project_folder:
- output_files:

## Input Snapshot
- data_sources:
- files_read:
- tables_or_curves_provided:
- assumptions_from_user:
- missing_information:
- data_sufficiency_class:

## Module Execution Trace
| step | module_or_protocol | why_used | input_used | reasoning_summary | output_summary | evidence_refs | limitations |
|---:|---|---|---|---|---|---|---|

## Evidence Log
| evidence_id | data_type | source_file_or_note | condition | observation | supports | evidence_level | limitation |
|---|---|---|---|---|---|---:|---|

## Decision Log
| decision_id | decision | alternatives_considered | decision_rationale | evidence_refs | risk | overturning_result |
|---|---|---|---|---|---|---|

## Metric Log
| metric | value | unit | calculation_basis | window_or_condition | missing_raw_data | interpretation |
|---|---:|---|---|---|---|---|

## Claim Trace
| claim | evidence_refs | evidence_level | metric_basis | safe_wording | unsupported_extension | reviewer_risk |
|---|---|---:|---|---|---|---|

## Final Output Snapshot
```text
<paste the final user-facing output or the manuscript/experiment recommendation here>
```

## Human Intervention And Changes
- human_constraints:
- manual_data_cleaning:
- user_selected_alternative:
- expert_review_changes:

## Next-State Record
- current_best_configuration:
- weakest_evidence_link:
- next_experiment:
- result_that_would_change_the_plan:
```

## Logging Rules

- Record every module that materially changed the recommendation.
- Record why unused modules were skipped when a full seven-module analysis was not performed.
- Link every strong recommendation to at least one evidence entry.
- Preserve missing data and proxy labels; do not silently upgrade proxy metrics into measured metrics.
- When updating a previous recommendation, keep the previous configuration and explain why it changed or stayed the same.
- When writing manuscript text, log claim boundaries and reviewer risks.
- When running a forward test, keep evaluator rubrics outside the tested agent's prompt and log only whether the rubric was withheld.
- If a result is based on qualitative evidence only, state that in the evidence log and final output.

## Minimal Log For Short Tasks

For a small request, the log may be shortened to:

```text
Run Metadata
Input Snapshot
Module Execution Trace
Decision Log
Final Output Snapshot
Next-State Record
```

Do not omit evidence level, metric basis, or missing-data limitations when they affect the claim.

## Paper-Facing Claim Boundary

Supported claims:
- "Each co-scientist run was documented using a structured run log that captured inputs, module use, evidence references, decision rationales, metric bases, final outputs, and human interventions."
- "The run log provides a traceable decision record for reproducing AI-assisted recommendations."

Claims not supported by the log alone:
- "The log contains the model's complete internal reasoning."
- "The logged recommendation is experimentally correct."
- "The workflow is autonomous."

Safe wording:
- Use "structured run log", "traceable decision record", "reasoning summary", and "decision rationale".
- Avoid "full chain of thought" or "complete internal thought process" in manuscript claims.
