---
name: mof-tandem-bed-co-scientist
description: Use this skill to design, analyze, transfer, and experimentally refine general serial or tandem adsorption beds for multicomponent separations. It combines isotherms, single-bed breakthrough curves, kinetics, target retention, prior tandem experiments, and an explicit capacity-matching equation to infer adsorbent roles, order, mass ratios, uncertainty, and the next decisive experiment without treating static uptake as dynamic capacity or hard-coding a chemistry, material, or feed.
metadata:
  version: "2.0.0"
---

# MOF Tandem-Bed Co-Scientist

Use this skill as a general decision-support workflow for layered or serial adsorption beds. The task is not to find one globally "best" material. It is to assign separation functions, calculate a transparent dynamic-capacity baseline when the data permit it, reason over the remaining evidence, and learn from tandem experiments.

Core principle:

```text
Function assignment -> dynamic calculation -> evidence-based correction
-> bounded configuration hypothesis -> experiment -> calibrated update
```

The workflow is chemistry-agnostic. Never hard-code a component family, material name, bed order, or mass ratio. A project-specific case may be used as a validation fixture, but never as an instruction that controls a new project.

## Required Data Hierarchy

Keep each evidence source in its proper role:

1. **Feed and product specification** define component duties and success criteria.
2. **Feed-matched multicomponent single-bed breakthrough** is the primary source for dynamic loading, front order, limiting impurity, target retention, and capacity matching.
3. **Existing tandem experiments** calibrate usable capacity, sequence interaction, packing, and model discrepancy.
4. **Single-component or mixture isotherms** support material-role assignment and feed-relevant relative capacity/selectivity. They do not silently replace dynamic capacity.
5. **Kinetic and curve-shape evidence** supplies penalties for slow uptake, broad mass-transfer zones, early leakage, and co-adsorption.
6. **Descriptors, simulations, and chemical intuition** support hypotheses when experiments are sparse; label them as lower-level evidence.

Use these evidence levels:

- Level 0: descriptors, literature analogy, or qualitative chemistry.
- Level 1: isotherm or equilibrium-mixture support.
- Level 2: feed-relevant single-bed breakthrough support.
- Level 3: multicomponent or tandem breakthrough support.
- Level 4: replicated ratio/sequence comparisons or validated transfer across conditions.

Always distinguish measured, calculated, inferred, assumed, and predicted values.

## First Route The Task

1. Parse the feed, pressure, temperature, flow, bed geometry, target product, purity threshold, recovery objective, candidate materials, and available data.
2. Assign component roles rather than relying on component names:
   - target product;
   - upstream-duty impurity group `B`;
   - downstream residual-duty component or group `G`;
   - inert or weakly interacting carrier;
   - possible competitive or target-retention penalty components.
3. Assign layer functions before assigning materials: front separation, downstream refining, and optional guard layer.
4. Classify data sufficiency:
   - **A — direct dynamic**: feed-matched multicomponent curves exist for the relevant materials;
   - **B — experimentally anchored transfer**: a validated tandem configuration exists at a nearby condition, but new feed-matched curves do not;
   - **C — proxy-supported**: isotherms/kinetics exist but no suitable dynamic anchor;
   - **D — insufficient**: only general descriptors or incomplete conditions exist.
5. Select the matching calculation and claim strength. Do not output a precise mass ratio under class C or D unless the user explicitly requests an assumption-defined scenario.

When raw data are provided, first read `references/data_input_contract.md`. For general function assignment and material screening, use the six original modules indexed by `references/six_module_framework.md`. For tandem calculations and transfer reasoning, read the three protocols below.

## Capacity-Matching Baseline

Read `references/tandem_capacity_matching.md` and use `scripts/tandem_capacity_analysis.py` for reproducible calculations.
Read `references/tandem_manifest_schema.md` to map curve files, component columns, flow rates, units, and mass normalization. Run `python scripts/tandem_capacity_analysis.py MANIFEST.json OUTPUT.json`. The CSV calculation uses the Python standard library; Excel input additionally requires `openpyxl`.

For upstream material `U`, define a common cutoff at threshold `theta` from the earliest breakthrough among the upstream-duty components:

```text
x_B(theta) = min_i x_U,i(theta),  i in B
q_U,i(theta) = F_i * integral[0 to x_B] (1 - C_i/C_i,0) dx
q_U,B(theta) = sum_i q_U,i(theta)
tau_U = q_U,B / L_B
```

For each downstream-duty component `g`:

```text
b_g,res = max(0, L_g * tau_U - q_U,g)
```

For downstream material `D`, use its feed-matched dynamic capacity `q_D,g` and calculate the conservative componentwise mass requirement:

```text
m_D/m_U = max_g (b_g,res / q_D,g)
m_U/m_D = 1 / max_g (b_g,res / q_D,g)
```

The component producing the maximum is the controlling downstream duty. A group-sum formulation is allowed only when component interchangeability is physically justified and documented.

This result is a **capacity-matching baseline**, not a universal optimum. Report the threshold, integration convention, units, controlling component, interpolation method, and curve-quality flags.

## Evidence-Based Material And Mass Reasoning

Read `references/evidence_fusion_and_mass_reasoning.md` whenever more than one candidate material is compared or the calculated ratio is adjusted.

For every layer and material, build an evidence matrix covering feed-relevant equilibrium capacity, selectivity, dynamic capacity, front sharpness, kinetics, target retention, regeneration, stability, and packing constraints.

Reason in two visibly separate stages:

1. **Calculation stage:** report the equation-derived baseline or explain why it is unavailable.
2. **Judgment stage:** apply material-specific corrections or choose a test range, with one explicit reason for each change.

Useful qualitative direction:

- stronger feed-relevant duty-component capacity, sharper breakthrough, and lower target penalty support less downstream mass;
- weaker capacity, broader fronts, competitive displacement, or stronger target retention support more downstream mass;
- a high static uptake alone does not justify less mass if dynamic utilization is poor.

Do not average incomparable evidence into an opaque score. Use hard constraints first, then ordered reasoning, then a small experiment matrix.

## Feed Or Operating-Condition Transfer

When feed composition, pressure, temperature, flow, or objective changes and no new feed-matched breakthrough curves exist, read `references/feed_transfer_protocol.md`.

Prefer an experimentally validated baseline configuration. For each functional layer, estimate a transparent burden multiplier:

```text
s_duty = [(L_duty / L_reference)_new] / [(L_duty / L_reference)_base]
m_layer,new = m_layer,base * s_duty * k_material * k_operation * k_uncertainty
```

Choose `L_reference` to match the operating objective: target molar flow for a recovery window, total flow for fixed service time, or another explicitly justified basis. Every multiplier must be defined and traceable.

- `k_material` reflects material-specific isotherm, kinetics, selectivity, or dynamic-utilization evidence.
- `k_operation` reflects flow, pressure, temperature, geometry, or pellet effects.
- `k_uncertainty` expands the test range when extrapolation is weak; it is not a hidden fitting constant.

If no defensible numerical correction exists, report low/base/high scenarios and a minimal confirmation matrix rather than a single exact ratio.

## Learning From Tandem Experiments

Treat each tandem experiment as calibration data, not as proof of global optimality. Record the prediction, tested ratio, conditions, collection rule, purity, recovery, productivity, limiting impurity, model discrepancy, and likely cause.

Prefer updating an interpretable utilization factor or bounded correction range. Do not present model retraining unless an actual statistical or machine-learning model was fitted and validated.

## Required Safety And Claim Boundaries

- Never substitute isotherm uptake for `q_D,g` without an explicit conversion assumption and uncertainty label.
- Never infer a global material ranking from unequal mass allocations or one condition per material.
- Never call a configuration globally optimal without a defined search space and adequate ratio/sequence coverage.
- Never use downstream breakthrough data measured under a different upstream effluent composition as if feed-matched.
- Keep target-retention penalties visible even when impurity capture is excellent.
- Check curve overshoot, non-monotonicity, missing pre-breakthrough baseline, inconsistent units, and insufficient run length.
- Preserve negative and ambiguous results; they are calibration evidence.

## Standard Output

```text
Research State
- Target product and specification:
- Feed and operating condition:
- Functional component groups:
- Available evidence and data class:
- Current experimentally validated configuration:

Function Map
- Layer duties and failure modes:
- Candidate materials by function:

Evidence Matrix
- Isotherm evidence:
- Single-bed breakthrough evidence:
- Kinetic/front-shape evidence:
- Target-retention evidence:
- Tandem calibration evidence:
- Stability and process constraints:

Capacity-Matching Baseline
- Threshold and common cutoff:
- Integrated dynamic capacities:
- Residual downstream duties:
- Controlling duty component:
- Equation-derived mass ratio or reason unavailable:

Reasoned Adjustment
- Material-specific correction and evidence:
- Feed/operation transfer factors:
- Low/base/high mass range:
- What is calculated vs inferred:

Configuration Hypothesis
- Bed order and primary mass allocation:
- Comparison configurations and collection rule:
- Expected tradeoff:

Next Decisive Experiment
- Smallest experiment matrix:
- Measurements and success criterion:
- Result that would reverse the recommendation:

Claim Boundary
- Supported claim:
- Unsupported claim:
- Main uncertainty:
```

## Related General Protocols

- `references/module_1_mixture_role_analyzer.md`: mixture roles and limiting impurities.
- `references/module_2_functional_decomposer.md`: layer-function decomposition.
- `references/module_3_sorbent_screening_engine.md`: descriptor-guided candidate space.
- `references/module_4_experimental_calibration_loop.md`: isotherm, breakthrough, and kinetic calibration.
- `references/module_5_configuration_optimizer.md`: sequence and ratio hypotheses.
- `references/module_6_feed_objective_perturbation.md`: general perturbation analysis.
- `references/experimental_controls_uncertainty.md`: controls, repeats, and claim strength.
- `references/research_state_schema.md`: traceable iterative research state.
- `references/run_logging_protocol.md`: auditable run logs.
- `references/manuscript_methods_si_template.md`: publication-ready Methods and SI wording.

When a manuscript-specific case is supplied, keep its numbers in the project data or an external fixture. Do not edit the reusable skill to encode the expected conclusion.
