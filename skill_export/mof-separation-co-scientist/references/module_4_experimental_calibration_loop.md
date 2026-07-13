# Module 4 - Experimental Calibration Loop

## Purpose

Use experiments to calibrate the functional model. Experiments are not only validation; they update the assigned function, limiting impurity, failure mode, and next experiment.

## Inputs

- Single-component breakthrough curves.
- Multicomponent breakthrough curves.
- Serial-bed breakthrough curves.
- Adsorption isotherms at feed-relevant partial pressures.
- Kinetic information, cycle tests, or regeneration data when available.
- Experimental metadata: bed mass, flow rate, temperature, pressure, activation, particle size, packing, and detector normalization.

## Required Reasoning

1. Convert raw curves into comparable dynamic features:
   - `t5`, `t50`, `t95`;
   - first impurity breakthrough;
   - target breakthrough;
   - clean collection window;
   - curve broadening or tailing;
   - dynamic uptake proxy.
2. Compare breakthrough behavior against the intended function.
3. Use isotherms to explain capacity and affinity, but let breakthrough decide dynamic function.
4. Identify whether failure is caused by insufficient capacity, weak selectivity, slow kinetics, co-adsorption, target retention, or sequence mismatch.
5. Update the evidence level and the functional role of each material.

## Output Schema

```text
Experimental Calibration Update
- Experiment:
- Conditions:
- Intended function:
- Observed breakthrough order:
- Target window:
- Limiting impurity:
- Metric calculation basis:
- Function score update:
- Revised role:
- Failure mode:
- Next calibration experiment:
```

## Evidence Standard

- Level 1: isotherm supports a likely affinity/capacity role.
- Level 2: single-bed breakthrough supports a dynamic function.
- Level 3: multicomponent or serial breakthrough supports the function under competitive conditions.
- Level 4: ratio or sequence comparison supports a configuration-level conclusion.

## Failure Modes

- Calling a material validated because it worked once.
- Using single-component breakthrough to claim multicomponent selectivity without caution.
- Ignoring flow rate, bed mass, particle size, or activation differences.
- Reporting purity or recovery without saying whether it is measured or a proxy.
- Treating broad breakthrough curves as equal to sharp separations.

## Paper-Facing Claim Boundary

Supported claims:
- "Breakthrough and isotherm data calibrated the assigned bed functions."
- "The limiting impurity and failure mode were updated from experimental evidence."
- "A material was experimentally supported for a specific function under stated conditions."

Claims not supported by this module alone:
- "The full serial configuration is optimized" unless ratio/sequence comparisons are included.
- "The process is scalable" without regeneration and practical validation.
- "Single-component breakthrough proves multicomponent product purity."

Safe wording:
- Use "calibrated", "supported under these conditions", and "updated the role assignment".
- Avoid "validated material" without specifying the function and condition.
