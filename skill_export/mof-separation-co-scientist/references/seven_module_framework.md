# Seven-Module Co-Scientist Framework

Use this file as the compact workflow index. For detailed publication-grade reasoning, open the specific module file listed below.

## Workflow Logic

```text
Mixture role analysis
-> functional bed decomposition
-> function-compatible sorbent screening
-> experimental calibration
-> configuration hypothesis generation
-> feed/objective perturbation
-> process validation
```

The framework should support the central research claim:

```text
RUPTURA or physical simulation -> high-quality simulation/experimental data
-> co-scientist reasoning and surrogate-model support
-> rapid batch prediction and configuration hypotheses
-> operating-condition exploration and adsorbent screening.
```

Machine learning and LLM reasoning do not replace physical simulation or breakthrough experiments. They use those data sources to accelerate hypothesis generation, screening, and experimental planning.

## Module Index

| module | file | primary decision |
|---|---|---|
| 1. Mixture Role Analyzer | `module_1_mixture_role_analyzer.md` | What is the target recovery mode and limiting impurity? |
| 2. Functional Decomposer | `module_2_functional_decomposer.md` | What functions must the bed layers perform? |
| 3. Sorbent Screening Engine | `module_3_sorbent_screening_engine.md` | Which candidates fit each function? |
| 4. Experimental Calibration Loop | `module_4_experimental_calibration_loop.md` | What did breakthrough/isotherm data calibrate? |
| 5. Configuration Hypothesis Generator | `module_5_configuration_optimizer.md` | What order, ratio, and collection window should be tested? |
| 6. Feed And Objective Perturbation Engine | `module_6_feed_objective_perturbation.md` | How does the configuration shift under new feed/objective? |
| 7. Process Validation Engine | `module_7_process_validation_engine.md` | What regeneration, cost, cycling, and scale-up evidence is needed? |

Publication-support protocols:

| support need | file | use when |
|---|---|---|
| Data input contract | `data_input_contract.md` | converting raw feed, descriptor, isotherm, breakthrough, or serial-bed data into auditable input tables |
| Experimental controls and uncertainty | `experimental_controls_uncertainty.md` | controls, replicate design, uncertainty sources, error bars, claim thresholds |
| Regeneration/scale-up/TEA proxy | `regeneration_scaleup_tea_protocol.md` | regeneration route, working capacity, cycles, material cost, shaping, pressure drop, TEA proxy |
| Co-scientist evaluation | `co_scientist_evaluation_protocol.md` | benchmark design, baselines, ablation studies, scoring rubric, reviewer defense |
| Research-state traceability | `research_state_schema.md` | iterative optimization, experiment logs, decision records, claim-to-evidence traceability |
| Manuscript/SI writing | `manuscript_methods_si_template.md` | Methods text, Supporting Information tables, figure captions, reviewer responses, slide text |
| Reproducibility reporting | `reproducibility_reporting_checklist.md` | AI-use statement, model/prompt reporting, data provenance, human intervention logs, SI package |
| Forward testing | `forward_test_protocol.md` | independent validation, blind-style tests, pass/fail scoring |

## Full Co-Scientist Output

```text
Research State
- Target:
- Feed condition:
- Target recovery mode:
- Current objective:
- Current hypothesis:
- Evidence level:
- Weakest link:

Module Updates
- Module 1 mixture role:
- Module 2 functional decomposition:
- Module 3 candidate map:
- Module 4 experimental calibration:
- Module 5 configuration hypothesis:
- Module 6 perturbation response:
- Module 7 process validation:

Decision
- Recommended next experiment:
- Experiment budget strategy:
- Why this experiment is highest value:
- What result would change the plan:

Publication Angle
- Claim supported now:
- Claim not yet supported:
- Figure/table to prepare:
- Reviewer risk:
```

## Cross-Module Guardrails

- Assign functions before materials.
- Do not produce a global MOF ranking unless explicitly requested.
- Treat experiments as calibration of the functional model.
- Treat LLM outputs as configuration hypotheses unless a real optimizer or exhaustive validated search was used.
- Label productivity, recovery, and purity by calculation basis.
- State evidence level for every strong recommendation.
- Convert raw data into structured input tables and data-sufficiency classes before recommending configurations.
- Tie performance claims to controls, replicate status, metric uncertainty, and claim thresholds.
- When the user has only one experiment and asks for performance, give one bold primary configuration plus the biggest risk.
- For manuscript claims about co-scientist performance, include evaluation baselines, ablations, scoring dimensions, and reviewer-risk boundaries.
- For multi-round optimization, maintain a structured research state rather than recomputing from scratch each turn.
- For manuscript writing, use publication-safe wording and preserve the distinction between hypothesis generation, experimental calibration, and process validation.
- For forward testing, do not leak evaluator rubrics or expected reasoning into the tested agent's prompt.
- For reproducibility reporting, record the skill/prompt reference, model run details, data provenance, human decisions, and negative cases.
- For process-readiness claims, distinguish lab separation performance from regeneration, cycling, shaping, pressure-drop, cost, and scale-up evidence.
