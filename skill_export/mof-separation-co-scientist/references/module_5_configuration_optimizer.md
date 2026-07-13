# Module 5 - Configuration Hypothesis Generator

## Purpose

Generate a testable adsorbent configuration hypothesis: material set, sequence, mass ratio, collection window, expected limiting impurity, and performance-risk tradeoff. The LLM is not a numerical optimizer unless coupled to a real optimization engine; it is a configuration hypothesis generator.

## Inputs

- Candidate pool from Module 3.
- Experimental calibration from Module 4.
- Functional labels from Module 2.
- Target recovery mode from Module 1.
- Constraints: total bed mass, available materials, allowed sequence, ratio bounds, number of experiments, feed condition, and objective priority.
- Objective: productivity-first, recovery-first, purity-first, robustness-first, low-energy, or low-cost.

## Required Reasoning

0. Apply the stage gate: if no candidate pool or dynamic evidence exists, do not generate a material set, bed order, or mass ratio. Return a "not ready for configuration" status and specify the structural target profiles and minimum data needed for the next step.
1. Select materials by complementary functions, not by global score.
2. Choose order from the functional architecture:
   - front layer handles bulk load, sequence shaping, or protection;
   - downstream layer refines the limiting impurity or protects target quality.
3. Choose ratio by expected capacity burden and target-retention penalty.
4. Define the collection window and expected limiting impurity.
5. State the performance tradeoff:
   - productivity can drop if target is delayed too much;
   - recovery can drop if the collection window is too narrow;
   - purity can drop if the limiting impurity leaks early.
6. Label productivity, recovery, and purity as measured, curve-integral proxy, time-window proxy, or qualitative estimate.
7. Use the experiment budget strategy:
   - `1-shot`: one bold primary configuration. If the user says performance is the priority, choose the most likely high-performing configuration; if learning is the priority, choose highest information gain.
   - `3-shot`: primary configuration, ratio perturbation, and sequence-control experiment.
   - `5-shot`: add single-function control and feed/objective perturbation.

## Output Schema

```text
Configuration Hypothesis
- Objective priority:
- Experiment budget:
- Primary configuration:
- Bed order:
- Mass ratio:
- Total mass:
- Collection/desorption window:
- Expected limiting impurity:
- Productivity expectation:
- Recovery expectation:
- Purity expectation:
- Metric calculation basis:
- Evidence level:
- Single biggest risk:
- Result that would overturn the hypothesis:
```

## Evidence Standard

- Level 2 can support a first configuration hypothesis when only single-bed breakthrough exists.
- Level 3 can support a stronger serial or multicomponent hypothesis.
- Level 4 is required before saying one ratio or sequence is experimentally better than another.
- Level 5 is required before implying process validation or scale-up readiness.

## Failure Modes

- Saying "optimized" when only one configuration was tested.
- Generating a bed order or mass ratio before candidate materials and dynamic evidence exist.
- Giving multiple timid options when the user explicitly has only one experiment and wants performance.
- Ignoring bed mass ratio and only recommending order.
- Optimizing purity while sacrificing all productivity without saying so.
- Hiding uncertainty instead of naming the single biggest risk.

## Paper-Facing Claim Boundary

Supported claims:
- "The co-scientist generated a testable configuration hypothesis under explicit productivity/recovery constraints."
- "The proposed sequence and ratio reflect calibrated functional roles and experimental budget."
- "A one-shot recommendation was selected for expected performance or information gain, as specified."

Claims not supported by this module alone:
- "The configuration is a global optimum."
- "The ratio is universally optimal across feed compositions."
- "The configuration has process-level feasibility."

Safe wording:
- Use "configuration hypothesis", "recommended test", or "experimentally prioritized configuration".
- Use "optimized" only after Level 4 evidence or when a real numerical optimizer/exhaustive validated search is used.
