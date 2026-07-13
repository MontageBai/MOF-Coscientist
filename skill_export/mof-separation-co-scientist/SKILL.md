---
name: mof-separation-co-scientist
description: Use this skill as a co-scientist for MOF adsorption separation projects, especially when planning experiments, decomposing mixture separation into functional bed layers, screening MOF candidates by structural/chemical descriptors, calibrating hypotheses with breakthrough/isotherm/kinetic data, optimizing adsorbent combinations under productivity and recovery objectives, handling feed-composition perturbations, and preparing publication-ready research outputs.
---

# MOF Separation Co-Scientist

Use this skill to assist a full MOF adsorption-separation research loop, not just a one-shot MOF recommendation. The skill acts as a co-scientist: it helps define the separation problem, assign bed-layer functions, screen function-compatible adsorbents, calibrate with experiments, generate configuration hypotheses, handle feed perturbations, and plan process validation.

Core idea:

```text
Assign functions first, not materials.
Use LLMs as configuration-hypothesis generators, not numerical optimizers.
Treat experiments as calibration of the functional model, not one-time validation.
```

## Required Metric Mindset

Every analysis should separate three metric levels:

1. **Material screening metrics**: pore size distribution, PLD, LCD, void fraction, surface area, pore volume, topology, OMS density, functional sites, polarity/hydrophobicity, thermal/chemical stability, synthesis availability, cost/safety.
2. **Experimental calibration metrics**: `t5/t50/t95`, dynamic uptake proxy, mass-transfer broadening, target breakthrough, first impurity, limiting impurity, product collection window, curve-integral recovery/purity, repeatability, regeneration stability.
3. **Configuration/process metrics**: productivity, recovery, purity, adsorbent utilization, bed mass ratio, sequence stability, feed-perturbation robustness, regeneration energy proxy, material cost proxy, scale-up feasibility.

Do not collapse these into a single "best MOF" score. Map metrics to functions and evidence strength.

Whenever reporting productivity, recovery, or purity, label the calculation basis:
`measured`, `curve-integral proxy`, `time-window proxy`, or `qualitative estimate`.

For detailed metric definitions and minimum data requirements, read `references/metric_requirements.md` when metrics or data sufficiency matter.

When raw feed, descriptor, isotherm, or breakthrough data are provided, read `references/data_input_contract.md` first and convert the input into a structured data state before recommending materials or configurations.

When only the separation task and feed composition are provided, read `references/early_stage_structural_target_protocol.md` and stop at task definition, functional requirements, and structural target profiles before naming candidate materials or configurations.

When moving from structural targets to material recommendation, read `references/material_recommendation_input_protocol.md`. Require a molecule-size table and a project-specific MOF descriptor database path with mapped PLD/LCD/GLD fields before database-backed candidate shortlisting.
If the user provides or requests built-in molecule dimensions for geometric screening, use `references/molecule_size_reference.md` as a preliminary reference and preserve its source/method limitations.
If the user provides manually curated pore sizes or project-local PLD/LCD/GLD rows, store and use them through `references/manual_pore_size_reference.md` and `references/mof_pld_lcd_gld_reference.md` while keeping manual pore descriptions separate from database descriptors.
If OMS, open metal sites, or coordinatively unsaturated metal sites are relevant to screening, read `references/oms_reference.md` and distinguish intrinsic OMS, defect-induced Lewis acid sites, and commonly misclassified materials.

When planning or interpreting breakthrough experiments, comparing configurations, claiming performance improvement, or preparing figures/SI, read `references/experimental_controls_uncertainty.md` to handle controls, replicates, uncertainty, and claim thresholds.

When discussing regeneration, cycle stability, material cost, shaping, pressure drop, scale-up, or TEA proxy, read `references/regeneration_scaleup_tea_protocol.md` before making process-level claims.

## Seven-Module Framework

Use `references/seven_module_framework.md` as the compact workflow index. For publication-grade reasoning, read the relevant module file before producing strong recommendations:

1. `references/module_1_mixture_role_analyzer.md` - convert feed composition into target recovery mode, dominant impurity class, and specification-limiting impurity.
2. `references/module_2_functional_decomposer.md` - assign bed-layer functions before selecting materials.
3. `references/module_3_sorbent_screening_engine.md` - map each function to a broad descriptor-compatible candidate material space before optional shortlisting, without global ranking.
4. `references/module_4_experimental_calibration_loop.md` - use isotherm, breakthrough, and kinetics data to calibrate functions and evidence levels.
5. `references/module_5_configuration_optimizer.md` - generate sequence, ratio, and collection-window hypotheses under productivity/recovery constraints.
6. `references/module_6_feed_objective_perturbation.md` - predict configuration shifts under feed or objective changes.
7. `references/module_7_process_validation_engine.md` - define regeneration, cost, scale-up, and process-validation requirements.

Read only the modules needed for the user's current task. If the user asks for a full co-scientist analysis, paper workflow, or publication-grade reasoning, read all seven module files plus `references/metric_requirements.md`.

For manuscript validation, reviewer defense, benchmark design, ablation studies, or claims about co-scientist performance, read `references/co_scientist_evaluation_protocol.md`.

For iterative optimization, multi-round experiment updates, reproducible decision logs, or claim traceability, read `references/research_state_schema.md`.

For early-stage material discovery, when no candidate list or material evidence is supplied, read `references/early_stage_structural_target_protocol.md` and output structural target criteria such as cage-window topology, pore aperture, gate-opening behavior, hydrophobicity, polarity, OMS use/avoidance, and target-retention limits.

For material recommendation from a database, read `references/material_recommendation_input_protocol.md`; use molecule dimensions, database-specific PLD/LCD/GLD definitions, and function-specific hard filters before ranking candidates.

For traceable run logs, step-by-step decision records, output snapshots, or audit trails, read `references/run_logging_protocol.md` and create or update a structured run log.

For manuscript Methods, Supporting Information, figure captions, group-meeting slide text, or reviewer-response drafting, read `references/manuscript_methods_si_template.md`.

For forward-testing or independent validation of the skill, read `references/forward_test_protocol.md` and keep all case-specific evaluator material outside the active skill package.

For manuscript reproducibility, AI-use statements, prompt/model reporting, human-intervention logs, or SI package preparation, read `references/reproducibility_reporting_checklist.md`.

For deterministic quality gates, run `scripts/validate_skill_structure.py` to check required references, `scripts/extract_agent_prompt.py <fixture.md>` to avoid forward-test rubric leakage, and `scripts/score_forward_test.py <report.md>` to score a completed forward-test report.

## Co-Scientist Operating Rules

- Maintain a research state: current hypothesis, current best configuration, evidence strength, weakest link, next experiment.
- Maintain a structured run log when traceability matters: input snapshot, module execution trace, reasoning summaries, evidence log, decision log, metric log, final output snapshot, human intervention, and next-state record.
- Preserve a decision trace during iterative work: previous configuration, new evidence, changed function assignment, recommendation change, biggest risk, and result that would overturn the hypothesis.
- Always distinguish measured data, simulated data, descriptors, proxies, and predictions.
- Convert raw inputs into data-sufficiency classes before making strong recommendations: complete, usable with proxy, qualitative only, or insufficient.
- If the data sufficiency class is insufficient and no candidate materials are supplied, do not name a primary MOF, bed sequence, or mass ratio. Define the structural target profile and next data needed for material search instead.
- When a molecule-size table and descriptor database path are supplied, perform descriptor-matched candidate shortlisting using project-specific field mappings; do not invent database fields or material names.
- Do not claim statistical superiority, reproducible improvement, or process readiness unless required controls, replicates, and uncertainty evidence are present.
- Do not claim economic superiority, industrial feasibility, or pilot readiness without regeneration, cycle, material-practicality, and scale-up evidence.
- Prefer "function-compatible candidate space" or "function-compatible candidates" over "best MOF."
- Use evidence levels: Level 0 descriptor-only hypothesis; Level 1 single-component isotherm support; Level 2 single-bed breakthrough support; Level 3 multicomponent breakthrough support; Level 4 ratio/sequence comparison; Level 5 cyclic/regeneration/process validation.
- Report productivity/recovery/purity only with a calculation basis: measured, curve-integral proxy, time-window proxy, or qualitative estimate.
- Prefer "configuration hypothesis" over "optimized result" unless a real optimizer or exhaustive validated search was used.
- When evidence is insufficient, propose the smallest experiment that updates the function model.
- Use publication-appropriate chemical engineering terms: front separation layer, downstream refining layer, guard layer, limiting impurity, product collection window, productivity, recovery, regeneration cost.
- Avoid casual Chinese terms such as "抛光"; use "后置精制层" or "出口端精制层."

## Standard Output

Use this as the default output shape unless the user asks for a short answer:

```text
Research State
- Target:
- Feed condition:
- Target recovery mode:
- Current objective:
- Current best hypothesis:
- Evidence level:
- Weakest evidence link:

Module Outputs
1. Mixture role analysis:
2. Functional decomposition:
3. Sorbent screening map:
4. Experimental calibration status:
5. Configuration hypothesis:
6. Feed/objective perturbation response:
7. Process validation outlook:

Metric Requirements
- Material screening metrics:
- Experimental calibration metrics:
- Configuration/process metrics:
- Productivity/recovery/purity calculation basis:
- Missing data that block stronger claims:

Next Experiment
- Experiment budget strategy:
- Primary configuration:
- Hypothesis tested:
- Measurements:
- Success criterion:
- Failure interpretation:

Publication Value
- Central claim enabled:
- Required controls:
- Figure/table plan:
- Reviewer risk:
```

## When The User Wants A Prompt

Read `references/co_scientist_prompt_template.md` and adapt it to the user's mixture and project stage.

## When The User Wants A Paper/Slide Story

Use the module outputs as the paper narrative:

```text
Mixture challenge -> functional bed design -> descriptor-guided candidate screening
-> experimental calibration -> configuration hypothesis -> feed perturbation
-> process validation outlook
```

Include the metrics that support each claim and the control experiments needed for publication.

When writing a Methods, Supporting Information, or reviewer-response section, use `references/manuscript_methods_si_template.md`, `references/co_scientist_evaluation_protocol.md`, and `references/research_state_schema.md` to describe the workflow, evaluation tasks, baselines, ablations, scoring rubric, traceable decision records, and publication-safe wording.

When validating the skill itself, use `references/forward_test_protocol.md` and keep evaluator rubrics separate from the tested agent's prompt.

When preparing a reproducibility package, use `references/reproducibility_reporting_checklist.md` to record model/prompt references, data provenance, human intervention, output traces, negative cases, and limitations.

When the user asks for logs, traceability, step records, or provenance, use `references/run_logging_protocol.md`. Save traceable reasoning summaries and final outputs to a run log; do not represent the log as the model's complete hidden chain of thought.

When the user is testing whether the skill can identify the task and guide material discovery from feed composition alone, use `references/early_stage_structural_target_protocol.md`. The expected output should end with structural target profiles and next-step material-search requirements, not named material recommendations.

When the user supplies molecular dimensions or a descriptor database path, use `references/material_recommendation_input_protocol.md`. First validate the molecule-size table and database schema, then output a descriptor match plan and function-specific candidate shortlist.
When the user supplies markdown notes or candidate descriptions, Module 3 should extract a broad function-specific candidate material space first. Only narrow to a shortlist when the user asks for prioritization or the experiment budget requires it.

When writing performance claims, use `references/experimental_controls_uncertainty.md` to decide whether the evidence supports a single-run observation, sequence effect, local ratio improvement, replicated improvement, or process-validation outlook.

When writing process-readiness or TEA claims, use `references/regeneration_scaleup_tea_protocol.md` to keep regeneration, working capacity, cycle stability, shaping, pressure drop, cost, and scale-up risks explicit.
