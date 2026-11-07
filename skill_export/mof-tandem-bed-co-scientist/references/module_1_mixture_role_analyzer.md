# Module 1 - Mixture Role Analyzer

## Purpose

Convert the feed separation problem from a chemical list into a structured separation role map. This module determines what must be removed, what must be collected, which impurity limits the product window, and whether the target is an outlet product or a retained/desorbed product.

## Inputs

- Target molecule.
- Impurity list.
- Feed mole fraction or partial pressure for every component.
- Total pressure, temperature, flow rate, and carrier gas when available.
- Product specification or collection goal.
- Known safety, condensation, or analytical constraints.

## Required Reasoning

1. Normalize the feed into comparable quantities: mole fraction, partial pressure, or normalized burden.
2. Identify the dominant impurity class by feed burden and expected adsorption strength.
3. Identify the specification-limiting impurity: the impurity most likely to enter the target collection window first.
4. Assign exactly one target recovery mode:
   - `breakthrough product`: collect the target from the outlet before impurity breakthrough.
   - `adsorbed product`: intentionally retain the target and recover it later.
   - `desorption product`: recover the target from a controlled desorption step.
5. Translate the chemistry into separation challenges: size similarity, branching/isomerism, polarity, volatility, competitive adsorption, and kinetic diffusion.

Do not assume the target recovery mode from the molecule name alone. If the intended collection route is missing, state the assumption and ask for confirmation before making strong claims.

## Output Schema

```text
Mixture Role Analysis
- Target:
- Feed condition:
- Target recovery mode:
- Collection/desorption implication:
- Dominant impurity class:
- Specification-limiting impurity:
- Main separation challenge:
- Missing information:
```

## Evidence Standard

- Level 0: role assignment from descriptors or general chemistry only.
- Level 1: role assignment supported by single-component isotherms at feed-relevant partial pressures.
- Level 2: role assignment supported by single-bed breakthrough.
- Level 3+: role assignment supported by multicomponent breakthrough or serial-bed breakthrough.

## Failure Modes

- Treating the highest concentration impurity as automatically specification-limiting.
- Ignoring target recovery mode and designing the wrong cut window.
- Confusing equilibrium selectivity with dynamic separation order.
- Forgetting that low-concentration, high-affinity impurities can dominate product specification.

## Paper-Facing Claim Boundary

Supported claims:
- "The feed was decomposed into target recovery mode, dominant impurity burden, and specification-limiting impurity."
- "This role analysis defines the downstream bed-function requirements."

Claims not supported by this module alone:
- "A specific MOF is optimal."
- "A bed configuration is experimentally validated."
- "Product purity or recovery is achieved."

Safe wording:
- Use "role analysis suggests" or "the mixture role defines".
- Avoid "proves separation performance" unless dynamic experiments are included from later modules.
