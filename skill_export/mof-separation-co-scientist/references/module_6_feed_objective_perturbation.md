# Module 6 - Feed And Objective Perturbation Engine

## Purpose

Predict how the recommended configuration should change when feed composition or objective changes. The goal is to produce a configuration shift map, not to repeat the baseline recommendation.

## Inputs

- Baseline feed and baseline configuration.
- Perturbed feed compositions or partial pressures.
- Changed objectives: productivity-first, recovery-first, purity-first, robustness-first, low-energy, or low-cost.
- Experimental evidence for how each material behaves under component loading changes.

## Required Reasoning

1. Re-run Module 1 under the new feed condition.
2. Decide whether the dominant impurity or specification-limiting impurity changed.
3. Decide whether the same functional decomposition still holds.
4. Predict whether the material pair is invariant or should change.
5. Predict the ratio migration direction:
   - more front-layer mass if bulk impurity burden increases;
   - more downstream refining mass if the limiting impurity leaks early;
   - less strongly adsorbing mass if target productivity is being over-penalized.
6. Decide whether sequence remains stable.
7. State which experiment would verify the perturbation prediction.

## Output Schema

```text
Feed/Objective Perturbation Response
| case | role change? | invariant materials? | ratio migration | sequence stability | limiting impurity | recommended test |

Interpretation
- Why the ratio shifts:
- Why the sequence is stable or unstable:
- Metric likely to improve:
- Metric likely to worsen:
- Evidence level:
```

## Evidence Standard

- Level 0-1: perturbation map is a hypothesis from descriptors or isotherms.
- Level 2-3: perturbation map is supported by dynamic experiments under related conditions.
- Level 4: perturbation map is supported by direct ratio or sequence comparison.
- Level 5: perturbation map is supported by repeated or cyclic process validation.

## Failure Modes

- Assuming the same optimum holds after feed composition changes.
- Changing materials when only ratio migration is needed.
- Changing ratio without explaining which burden or limiting impurity changed.
- Ignoring objective changes: a productivity-first setting may require a different ratio than a purity-first setting.

## Paper-Facing Claim Boundary

Supported claims:
- "The co-scientist predicted configuration migration under feed or objective perturbation."
- "The ratio shift was linked to a changed impurity burden, target penalty, or limiting impurity."

Claims not supported by this module alone:
- "The perturbed-feed configuration is experimentally optimal."
- "The baseline optimum is robust across all compositions."
- "The pair is invariant under all operating conditions."

Safe wording:
- Use "configuration shift map", "ratio migration direction", and "robustness hypothesis".
- Avoid "robust optimum" unless direct perturbation experiments support it.
