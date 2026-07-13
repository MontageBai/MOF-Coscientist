# C6 Case-Study Protocol

Use this file when the user asks the co-scientist to analyze, reproduce, extend, or write the C6 separation case study. This is a protocol, not a fixed answer. Apply it to the current evidence and clearly label assumptions.

## Case Scope

Target:
- `nHEX`

Representative feed partial pressures:

```text
22DMB / 23DMB / 2MP / 3MP / 1HEX / nHEX
= 1.51 / 1.05 / 0.89 / 0.74 / 1.52 / 18.91 kPa
```

Key candidate materials from the current case:
- HKUST-1
- UiO-66
- UiO-66-NH2
- Zn-MOF-74 or other replacement MOF candidates

Primary case-study goal:
- Recommend and experimentally test a serial-bed MOF configuration that improves `nHEX` product performance under productivity/recovery constraints.

## Required Input Conversion

Before reasoning, convert user-provided raw data into a usable state table:

```text
Feed Table
| component | partial pressure kPa | role | expected issue |

Material Evidence Table
| MOF | data type | component behavior | likely function | evidence level | risk |

Breakthrough Feature Table
| MOF/configuration | target breakthrough | first impurity | clean window | limiting impurity | metric basis |
```

If raw curves are available, compute or request:
- `t5`, `t50`, `t95` for target and impurities.
- clean collection window.
- curve broadening or tailing.
- integrated target collection proxy.
- impurity leakage in the selected collection window.

If only qualitative breakthrough descriptions are available, label the result as a qualitative or time-window proxy.

## C6 Reasoning Pattern

1. Use Module 1 to assign the target recovery mode for `nHEX`.
2. Use Module 2 to define at least two functions:
   - front separation or sequence-shaping layer;
   - downstream refining layer for the remaining limiting impurity.
3. Use Module 3 to map candidates to functions, not to rank all MOFs globally.
4. Use Module 4 to calibrate functions from single-component and serial breakthrough.
5. Use Module 5 to generate one primary configuration when the experimental budget is one run.
6. Use Module 6 when `nHEX` or impurity concentration changes.
7. Use Module 7 only for regeneration, cost, scale-up, or process-validation claims.

## Case-Specific Observations To Preserve

Preserve these observations when supported by the user's data:

- HKUST-1 can strongly remove or delay `1HEX` in the current C6 case.
- Among other tested MOFs, UiO-66 and UiO-66-NH2 are important candidates for separating the remaining components.
- UiO-66-NH2 and UiO-66 can produce different outlet ordering for the remaining components.
- A UiO-66-like layer followed by an HKUST-1-like layer can be a strong serial-bed hypothesis when the first layer shapes the outlet stream and the second layer removes a remaining `1HEX` burden.
- If prior experiments show a `100 mg + 10 mg` configuration is best, replacement-MOF ratio migration should start from that functional mass distribution rather than from an equal-mass assumption.

Do not treat these observations as universal facts. They are case evidence and must be tied to the feed, activation, flow rate, total mass, temperature, and breakthrough conditions.

## Productivity, Recovery, And Purification Metric

For normalized breakthrough data, use explicit calculation labels.

Approximate collected-target fraction or purification proxy:

```text
x / y ~= integral(C_A / C_A0 dt over selected window) / (1 * Delta t)
```

Where:
- `x` is collected amount of target-like component in the selected window.
- `y` is the ideal feed amount over the same window under normalized inlet concentration.
- `Delta t` is the integration time window.

Use this only as a curve-integral proxy unless flow rate, calibration, and absolute molar amounts are available. If only breakthrough times are available, report a time-window proxy, not true purity or recovery.

## One-Shot Recommendation Rule

When the user says they will run only one experiment and wants performance:

1. Give exactly one primary configuration.
2. State bed order, mass ratio, total mass if known, and collection window.
3. Explain the function of each layer.
4. State the single biggest risk.
5. State the result that would overturn the hypothesis.

Do not dilute the answer with many conservative alternatives. If uncertainty is high, put it in the risk statement.

## Replacement-MOF Ratio Migration

Use this when replacing one layer, such as replacing HKUST-1 with Zn-MOF-74 or replacing a UiO-66-like layer.

Required reasoning:
- Identify which function is being replaced.
- Compare evidence for the original and replacement material:
  - feed-relevant isotherm uptake;
  - breakthrough delay for the limiting component;
  - target retention penalty;
  - kinetic broadening;
  - regeneration or practical penalty.
- Preserve the functional ratio if the replacement has similar capacity and selectivity.
- Increase replacement mass if it has lower dynamic capacity or earlier impurity leakage.
- Decrease replacement mass if it strongly retains the target and hurts productivity.

Output:

```text
Replacement Ratio Hypothesis
- Original best configuration:
- Replaced function:
- Replacement material:
- Proposed new ratio:
- Why this ratio migrates:
- Expected benefit:
- Biggest risk:
- Evidence level:
```

## Publication Figure Plan

Recommended figures for the C6 case:

1. Feed and molecule-role schematic:
   - target, impurities, partial pressures, target recovery mode.
2. Functional bed design:
   - front layer, downstream refining layer, optional replacement layer.
3. Descriptor or isotherm support:
   - feed-relevant uptake/selectivity or descriptor-function map.
4. Single-component breakthrough calibration:
   - material-function evidence.
5. Serial-bed configuration comparison:
   - sequence and ratio comparison with productivity/recovery proxy.
6. One-shot or replacement-MOF prediction:
   - old best ratio to new ratio migration logic.
7. Process-validation outlook:
   - regeneration, cycling, cost, and scale-up requirements.

## Paper-Facing Claim Boundary

Supported claims:
- "The C6 case demonstrates a co-scientist workflow that converts raw feed and breakthrough data into function-specific MOF roles and serial-bed configuration hypotheses."
- "The LLM supports configuration hypothesis generation and experiment prioritization under explicit productivity/recovery constraints."

Claims not supported without further evidence:
- "The proposed configuration is globally optimal."
- "The replacement MOF will universally outperform the original material."
- "The process is ready for scale-up without regeneration and cycle data."

Safe wording:
- Use "case-study demonstration", "configuration hypothesis", "experimentally calibrated function", and "ratio migration hypothesis".
- Avoid claiming that machine learning or the LLM replaces RUPTURA, physical simulation, or breakthrough experiments.
