# Evidence Fusion And Mass Reasoning

## Goal

Convert heterogeneous adsorption evidence into an explainable material choice and bounded mass recommendation without hiding judgment inside a single score.

## Evidence Matrix

Create one row per material-layer pairing and record:

| Dimension | Preferred evidence | Decision use |
|---|---|---|
| Feed-relevant capacity | mixture isotherm or breakthrough integral | mass requirement |
| Selectivity | mixture selectivity, displacement order, or justified IAST | role compatibility |
| Front sharpness | `t5/t50/t95`, MTZ width, slope | leakage and safety margin |
| Kinetics | uptake rate or dynamic curve | usable capacity and cycle time |
| Target penalty | target uptake and target breakthrough delay | recovery penalty |
| Regeneration | cyclic capacity and desorption severity | operating feasibility |
| Stability | humid/thermal/chemical cycling | hard constraint |
| Form factor | pellet density, pressure drop, packing | scale and geometry correction |

For every cell, label the source, condition, evidence level, and whether the direction is favorable, unfavorable, mixed, or unknown.

## Reasoning Order

1. Apply hard exclusions: instability, unacceptable target loss, no regeneration, unsafe synthesis, or missing essential capacity.
2. Use feed-matched dynamic capacity for the numerical baseline.
3. Compare equilibrium evidence at feed-relevant partial pressure, not only saturation uptake.
4. Check whether kinetic or front-shape evidence contradicts equilibrium ranking.
5. Check target-retention penalty and product-window consequence.
6. Apply practical constraints and tandem calibration.
7. Recommend a central ratio plus bracketing ratios when uncertainty remains.

## Directional Mass Logic

All else equal, more feed-relevant usable duty capacity and sharper fronts support lower mass. Weaker capacity, broader fronts, early leakage, stronger target co-adsorption, poor regeneration, or low pellet utilization support more mass or rejection. Favorable static uptake with poor dynamic utilization must not be treated as superior.

## Transparent Corrections

If a numerical factor is used, show it separately:

```text
m_recommended = m_equation * k_front * k_target * k_operation * k_calibration
```

Each factor needs a definition, evidence source, range, and direction. Avoid false precision. If a factor cannot be estimated, bracket it and make the bracket part of the experiment plan.

## Conflict Handling

When isotherm and breakthrough evidence disagree, dynamic evidence has priority for operating mass, while isotherms remain useful for diagnosing competition or capacity reserve. When two tandem tests use unequal masses, compare the tested configurations only; do not infer an intrinsic material ranking.

## Required Narrative

```text
The equation gives [baseline] from [dynamic evidence].
[Material A] receives [less/more] mass because [specific evidence].
[Material B] receives [less/more] mass because [specific evidence].
The conclusion is a [calculated ratio / calibrated estimate / test range], not a global optimum.
```
