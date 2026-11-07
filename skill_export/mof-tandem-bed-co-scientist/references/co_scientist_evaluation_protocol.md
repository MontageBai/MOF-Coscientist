# Co-Scientist Evaluation Protocol

Use this file when the user asks whether the MOF separation co-scientist is publication-grade, how to validate it, how to compare it with baselines, or how to defend it in a manuscript or response to reviewers.

## Purpose

Define how to evaluate the co-scientist as a research assistant for MOF adsorption separation. The evaluation should test whether it improves structured reasoning, experiment prioritization, and configuration hypothesis generation under realistic data constraints.

The evaluation is not meant to prove that the LLM replaces physical simulation, domain experts, or breakthrough experiments. It should show that the co-scientist organizes evidence, generates testable hypotheses, and improves the efficiency of experimental planning.

## Evaluation Tasks

Use at least three task types:

1. Problem decomposition:
   - Input: feed composition, target molecule, impurity list.
   - Expected output: target recovery mode, limiting impurity, bed-function decomposition.

2. Candidate-function mapping:
   - Input: MOF descriptors, isotherms, or candidate materials.
   - Expected output: function-compatible candidate map without global best-MOF ranking.

3. Configuration hypothesis:
   - Input: breakthrough/isotherm evidence, candidate pool, objective, experiment budget.
   - Expected output: adsorbent set, order, ratio, collection window, evidence level, risk.

4. Iterative update:
   - Input: new breakthrough result or feed perturbation.
   - Expected output: revised function assignment, ratio migration, changed limiting impurity, next experiment.

5. Publication translation:
   - Input: final experimental evidence.
   - Expected output: publication-safe claims, figure plan, unsupported claims, reviewer risks.

## Baselines

Compare the co-scientist with transparent baselines:

- Descriptor-only heuristic:
  - ranks materials by pore size, uptake, or functional sites without dynamic calibration.

- Isotherm-only heuristic:
  - uses feed-relevant uptake/selectivity but does not use breakthrough order or bed functions.

- Single-material ranking:
  - outputs one best MOF instead of function-specific candidate mapping.

- Human-rule baseline:
  - uses a short expert-written decision tree without iterative state tracking.

- Ablated co-scientist:
  - remove one module at a time, such as no functional decomposition, no evidence levels, no experiment-budget strategy, or no claim boundary.

Do not set up strawman baselines. State what each baseline can reasonably do well and where it is limited.

## Scoring Rubric

Use a 0-3 score for each dimension:

| dimension | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| role analysis | missing or wrong target role | identifies target but not limiting impurity | identifies target mode and likely impurity | links target mode, limiting impurity, and collection implication |
| function decomposition | material-first | vague bed roles | clear functions | clear functions plus falsification criteria |
| candidate mapping | global ranking only | partial function mapping | function-specific candidates | function-specific candidates plus evidence and risk |
| experimental calibration | ignores experiments | describes experiments | updates roles from data | updates roles, evidence level, and next experiment |
| configuration hypothesis | vague recommendation | order or material only | order, ratio, and risk | order, ratio, window, objective tradeoff, and overturning result |
| metric discipline | unsupported metrics | labels some proxies | labels metric basis | labels metric basis and data sufficiency |
| claim discipline | overclaims | partial caveats | safe claims | safe claims plus reviewer-risk anticipation |

Report both total score and failure modes. A high score means the reasoning is publishable and experimentally actionable, not that the recommendation is guaranteed correct.

## Experimental Success Metrics

When experiments are run, compare recommendations by:

- product collection window;
- target recovery or curve-integral recovery proxy;
- purity or impurity leakage in the selected window;
- productivity proxy, such as collected target per bed mass per time;
- adsorbent utilization;
- number of experiments required to reach a better configuration;
- robustness under feed perturbation.

Always label metrics as measured, curve-integral proxy, time-window proxy, or qualitative estimate.

## Blind And Forward Tests

Use blind tests when possible:

1. Hide the final best configuration from the co-scientist.
2. Provide only the data available at that stage.
3. Ask for one recommendation under a stated experiment budget.
4. Compare the recommendation with the later experimental result.
5. Record whether the co-scientist identified the correct limiting impurity, function map, and ratio direction.

Avoid leaking the expected answer into the prompt. The evaluation should test transferable reasoning rather than pattern recovery from hidden context.

## Ablation Tests

Recommended ablations:

- no Module 1: remove target recovery mode and limiting impurity analysis.
- no Module 2: recommend materials without functional decomposition.
- no Module 4: use descriptors/isotherms without breakthrough calibration.
- no evidence level: remove Level 0-5 claim discipline.
- no budget strategy: let the model output many options even when only one experiment is possible.
- no case protocol: evaluate a held-out case without case-specific data conversion or hidden interpretation notes.

Report which ablation causes the largest degradation in actionable recommendation quality.

## Reviewer-Risk Checklist

Before using co-scientist outputs in a manuscript, check:

- Are LLM outputs clearly described as hypotheses or planning support?
- Is every strong claim tied to an evidence level?
- Are productivity, recovery, and purity labeled by calculation basis?
- Are baselines fair and nontrivial?
- Is the physical simulation or breakthrough experiment still the evidence foundation?
- Are negative or failed recommendations discussed when relevant?
- Is the prompt or workflow reproducible enough for readers?
- Is the held-out case presented as a case study rather than universal proof?

## Paper-Facing Claim Boundary

Supported claims:
- "The co-scientist improves structured hypothesis generation and experiment prioritization under constrained experimental budgets."
- "The framework can be evaluated by role-analysis accuracy, function mapping, evidence calibration, metric discipline, and experimental outcome."
- "Ablation analysis identifies which reasoning modules are critical."

Claims not supported by this protocol alone:
- "The LLM is a universal optimizer."
- "The co-scientist guarantees the best configuration."
- "The framework replaces physical simulation, experiments, or expert interpretation."

Safe wording:
- Use "decision-support framework", "configuration hypothesis generation", "experiment prioritization", and "evidence-calibrated reasoning".
- Avoid "autonomous discovery" unless the workflow actually executed closed-loop experiments without hidden human intervention.
