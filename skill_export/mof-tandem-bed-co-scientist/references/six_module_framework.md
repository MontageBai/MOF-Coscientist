# Six-Module Co-Scientist Framework

Use this file as the compact workflow index. The workflow is an iterative research loop, not a one-way material-ranking pipeline.

## Workflow Logic

```text
Mixture role analysis
-> functional bed decomposition
-> function-compatible sorbent screening
-> experimental calibration
-> configuration hypothesis generation
-> feed/objective perturbation
-> next experiment and recalibration
```

Physical simulation, descriptors, isotherms, and breakthrough experiments remain the evidence foundation. The co-scientist organizes that evidence, assigns functions, and generates testable configuration hypotheses.

## Module Index

| module | file | primary decision |
|---|---|---|
| 1. Mixture Role Analyzer | `module_1_mixture_role_analyzer.md` | What is the target recovery mode and limiting impurity? |
| 2. Functional Decomposer | `module_2_functional_decomposer.md` | What functions must the bed layers perform? |
| 3. Sorbent Screening Engine | `module_3_sorbent_screening_engine.md` | Which candidates fit each function? |
| 4. Experimental Calibration Loop | `module_4_experimental_calibration_loop.md` | What did breakthrough, isotherm, and kinetic data change? |
| 5. Configuration Hypothesis Generator | `module_5_configuration_optimizer.md` | What material set, order, ratio, and collection window should be tested? |
| 6. Feed And Objective Perturbation Engine | `module_6_feed_objective_perturbation.md` | How should the hypothesis change under a new feed or objective? |

Publication-support protocols:

| support need | file | use when |
|---|---|---|
| Data input contract | `data_input_contract.md` | converting raw inputs into auditable tables and data-sufficiency classes |
| Experimental controls and uncertainty | `experimental_controls_uncertainty.md` | controls, replicates, uncertainty sources, and claim thresholds |
| Co-scientist evaluation | `co_scientist_evaluation_protocol.md` | benchmark design, baselines, ablations, and reviewer defense |
| Research-state traceability | `research_state_schema.md` | iterative optimization, experiment logs, and decision records |
| Manuscript/SI writing | `manuscript_methods_si_template.md` | Methods text, SI tables, figure captions, and reviewer responses |
| Reproducibility reporting | `reproducibility_reporting_checklist.md` | model/prompt reporting, data provenance, and human intervention |
| Forward testing | `forward_test_protocol.md` | independent validation and blind-style tests |

## Primary Feedback Loops

1. **Experiment loop:** Module 5 proposes a configuration; the next experiment returns to Module 4 for calibration.
2. **Function-update loop:** Module 4 may revise the limiting impurity or failure mode, which sends the workflow back to Modules 2-3.
3. **Perturbation loop:** Module 6 sends a changed feed or objective back to Module 1 before ratios or materials are changed.

## Full Co-Scientist Output

```text
Research State
- Target and feed:
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
- Convert raw inputs into structured tables and a data-sufficiency class before recommending configurations.
- Build a function-compatible candidate space before optional shortlisting.
- Treat experiments as calibration of the functional model.
- Treat LLM outputs as configuration hypotheses unless a real optimizer or exhaustive validated search was used.
- Label productivity, recovery, and purity by calculation basis.
- State an evidence level for every strong recommendation.
- Tie performance claims to controls, replicate status, and uncertainty.
- Maintain a research state across experimental rounds rather than recomputing from scratch.
- For forward testing, keep evaluator rubrics and expected reasoning outside the tested prompt.
