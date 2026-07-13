# Forward-Test Fixture - C6 / nHEX Case

Use this file as a C6 test fixture for the forward-test protocol. When giving the task to an independent agent, provide only the "Agent-Facing Prompt" section. Keep the evaluator section separate.

## Agent-Facing Prompt

```text
You are given a C6 adsorptive separation case.

Target:
- nHEX

Feed partial pressures:
- 22DMB = 1.51 kPa
- 23DMB = 1.05 kPa
- 2MP = 0.89 kPa
- 3MP = 0.74 kPa
- 1HEX = 1.52 kPa
- nHEX = 18.91 kPa

Available qualitative experimental observations:
- Single-component breakthrough experiments were performed at the above feed-relevant partial-pressure basis.
- HKUST-1 shows strong ability to delay or remove 1HEX relative to the target-oriented collection goal.
- UiO-66 and UiO-66-NH2 are the main tested candidates that can further separate the remaining components after the strongest 1HEX-removal role is considered.
- UiO-66 and UiO-66-NH2 show different outlet-order behavior for the remaining components.
- Prior serial-bed experiments suggest a 100 mg + 10 mg type combination is more promising than equal-mass assumptions.

Experimental budget:
- One experiment only.

Objective:
- Favor performance over conservative exploration.
- Still state the evidence level, metric basis, biggest risk, and what result would overturn the hypothesis.

Task:
- Use the MOF separation co-scientist skill.
- Convert the input into usable tables.
- Run the relevant modules.
- Recommend exactly one primary next experiment.
- Do not claim a global optimum.
- Do not report purity/recovery without labeling the calculation basis.
```

## Evaluator Rubric

Expected high-quality behavior:

- Converts feed data into a table and recognizes that `nHEX` is the high-partial-pressure target.
- Assigns a target recovery mode or explicitly states the assumption if the collection mode is not given.
- Defines at least two functions, such as front sequence-shaping or bulk impurity control and downstream refining.
- Maps HKUST-1, UiO-66, UiO-66-NH2, and Zn-MOF-74/replacement candidates by function, not global ranking.
- Uses the 100 mg + 10 mg prior as a ratio anchor rather than restarting from equal masses.
- Gives one primary configuration because the budget is one experiment and performance is prioritized.
- Labels evidence level, likely Level 2-3 unless serial/multicomponent comparison evidence is supplied.
- Labels metrics as qualitative estimate or time-window/curve-integral proxy unless raw curves are available.
- States the biggest risk and the result that would overturn the hypothesis.
- Provides publication-safe language: configuration hypothesis, not global optimum.

Common failure modes:

- Outputting three or more options despite one-experiment budget.
- Saying HKUST-1 is the best MOF globally.
- Ignoring UiO-66 vs UiO-66-NH2 outlet-order differences.
- Assuming true purity/recovery can be calculated without raw curves.
- Ignoring the 100 mg + 10 mg ratio anchor.
- Claiming process feasibility without regeneration or cycle evidence.

## Expected Report Fields

```text
Research State
- Target:
- Feed condition:
- Target recovery mode:
- Objective:
- Evidence level:
- Weakest link:

Converted Data
- Feed table:
- Material evidence table:
- Missing data:

Functional Design
- Bed A:
- Bed B:

Candidate Map
| function | candidates | evidence | risk |

One-Shot Configuration Hypothesis
- Primary configuration:
- Order:
- Mass ratio:
- Collection window:
- Metric basis:
- Biggest risk:
- Overturning result:

Publication Boundary
- Supported claim:
- Unsupported claim:
```
