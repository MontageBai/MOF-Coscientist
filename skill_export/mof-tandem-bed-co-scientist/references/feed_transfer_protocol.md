# Feed And Operating-Condition Transfer Protocol

## When To Use

Use this protocol when a validated configuration exists at a baseline condition but feed-matched breakthrough curves are absent at the new condition. This is transfer reasoning, not a direct application of the capacity-matching equation.

## Step 1: Preserve The Experimental Anchor

Record baseline feed, conditions, bed order, masses, geometry, collection rule, purity, recovery, productivity, and uncertainty. Identify which layer function each mass supported.

## Step 2: Define Functional Burden

Choose a denominator consistent with the objective: target flow for maintaining a target-recovery product window, total flow for maintaining service time, or upstream bed mass/cycle inventory for a fixed hardware comparison.

```text
s_duty = [(L_duty/L_reference)_new] / [(L_duty/L_reference)_base]
```

For multiple non-interchangeable duty components, calculate separate multipliers and let the controlling constraint set the mass.

## Step 3: Apply Material-Specific Evidence

Estimate a bounded `k_material` using, in order: feed-relevant mixture or competitive isotherms; single-component isotherms at relevant partial pressures; kinetic uptake and breakthrough-front shape; chemically justified descriptor or literature analogy.

Do not convert a static uptake ratio directly into a dynamic-capacity ratio without labeling the assumption. Stronger relevant capacity or selectivity may lower `k_material`; broad fronts, slow kinetics, or stronger target retention raise it.

## Step 4: Correct Operating Differences

Use `k_operation` for changes in total flow, superficial velocity, pressure, temperature, geometry, pellet form, humidity, or regeneration state. If a correction is not validated, use a range.

## Step 5: Express Extrapolation Uncertainty

Use `k_uncertainty` to widen the tested range, not to force agreement with a preferred result:

```text
m_new = m_base * s_duty * k_material * k_operation * k_uncertainty
```

Provide low/base/high cases and show which factor drives each bound.

## Step 6: Design The Smallest Confirmation Matrix

At minimum, test the central estimate and one bracketing mass on the uncertainty-dominant side. If material order is uncertain, include a sequence control. Measure product-window width, purity, recovery, productivity, limiting impurity, and target loss.

## Claim Boundary

Acceptable: "The baseline experiment, burden scaling, and material evidence motivate this test range."

Not acceptable without new data: "The new ratio is uniquely predicted," "the material is intrinsically superior," or "the transferred configuration is globally optimal."
