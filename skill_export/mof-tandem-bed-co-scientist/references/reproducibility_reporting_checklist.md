# Reproducibility And Reporting Checklist

Use this file when preparing a manuscript, Supporting Information, repository package, reviewer response, or group report involving the MOF separation co-scientist.

## Purpose

Make the co-scientist workflow reproducible and defensible. A publication-grade AI-assisted workflow should report what data were provided, which prompt or skill version was used, how outputs were evaluated, what human decisions were made, and which claims remain experimentally unsupported.

## Minimum Reporting Items

### Skill And Model Record

```text
Co-Scientist Record
- skill_name:
- skill_path_or_repository:
- skill_version_or_date:
- model_name:
- model_provider:
- run_date:
- temperature_or_sampling_setting:
- system_or_skill_prompt_reference:
- additional user prompt:
```

If exact model settings are unavailable, state that limitation.

### Data Provenance Record

```text
Data Provenance
- feed_data_source:
- descriptor_data_source:
- simulation_source:
- isotherm_source:
- breakthrough_source:
- preprocessing_steps:
- excluded_data:
- known_uncertainties:
```

### Human Intervention Record

```text
Human Intervention
- human-provided assumptions:
- manual data cleaning:
- manual selection among alternatives:
- experimental feasibility constraints:
- changes made after expert review:
```

Human intervention is not a flaw; hiding it is. Report it clearly.

### Output Trace Record

```text
Output Trace
- target recovery mode:
- limiting impurity:
- functional bed assignment:
- candidate map:
- recommended configuration:
- evidence level:
- metric basis:
- biggest risk:
- overturning result:
```

### Run Log Record

```text
Run Log
- log_file:
- run_id:
- input_snapshot_recorded:
- module_execution_trace_recorded:
- evidence_log_recorded:
- decision_log_recorded:
- metric_log_recorded:
- final_output_snapshot_recorded:
- human_intervention_recorded:
- next_state_recorded:
```

The run log should contain traceable reasoning summaries and decision rationales, not a claim of complete hidden chain-of-thought capture.

## Reproducibility Package Contents

For SI or a shared repository, include:

- feed composition table;
- descriptor/isotherm/breakthrough input tables;
- prompt or skill version reference;
- co-scientist output;
- structured run log;
- evidence-level assignment;
- metric calculation basis;
- forward-test report if available;
- baseline or ablation comparison if claiming co-scientist value;
- manuscript claim trace.

## Reviewer-Ready Statements

### AI Use Statement

```text
An LLM-based co-scientist workflow was used to structure the adsorption-separation problem, assign functional bed roles, map candidate MOFs to functions, and generate testable serial-bed configuration hypotheses. The LLM output was treated as decision support and was not used as a substitute for physical simulation, adsorption measurements, or breakthrough experiments.
```

### Reproducibility Statement

```text
For each co-scientist run, we recorded the input data state, prompt/skill reference, module execution trace, reasoning summaries, target recovery mode, functional bed assignment, recommended configuration, evidence level, metric calculation basis, final output snapshot, and human decisions. Claims in the manuscript were linked to the corresponding evidence level and experimental support.
```

### Limitation Statement

```text
The co-scientist recommendations are configuration hypotheses constrained by the available descriptors, isotherms, breakthrough data, and experimental budget. They should not be interpreted as global optima unless supported by systematic sequence/ratio comparison or numerical optimization.
```

## Negative And Failed Cases

Report negative cases when they affect the claim:

- failed recommendation;
- wrong limiting impurity prediction;
- ratio migration that reduced productivity;
- metric overestimated by proxy;
- material unavailable or unstable;
- strong-retention or desorption penalty not captured by breakthrough data.

Publication value often improves when failed cases are used to show how the research state was updated.

## Checklist Before Submission

- The skill or prompt used for analysis is identified.
- A structured run log is included or traceable.
- Input data tables are included or traceable.
- Target recovery mode is explicit.
- Evidence levels are defined and applied.
- Productivity/recovery/purity metrics state their calculation basis.
- Human assumptions and manual decisions are recorded.
- Baselines or ablations are included if claiming co-scientist performance.
- The LLM is described as a decision-support or hypothesis-generation layer.
- Physical simulation and experiments remain the evidence foundation.
- Unsupported claims are moved to outlook or future work.

## Paper-Facing Claim Boundary

Supported claims:
- "The AI-assisted workflow was documented with traceable inputs, prompts, outputs, evidence levels, and human decisions."
- "The reported recommendations are reproducible as decision-support outputs."

Claims not supported by reporting alone:
- "The recommendations are experimentally correct."
- "The workflow is autonomous."
- "The final configuration is globally optimal."

Safe wording:
- Use "reproducible co-scientist run", "traceable AI-assisted decision support", and "hypothesis-generation record".
- Avoid "autonomous optimization" unless there is a closed-loop experimental system and clear evidence.
