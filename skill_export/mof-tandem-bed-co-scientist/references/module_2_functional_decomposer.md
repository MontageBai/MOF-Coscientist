# Module 2 - Functional Decomposer

## Purpose

Assign bed-layer functions before assigning materials. The output should be a functional architecture that explains why a bed layer exists, what impurity or product behavior it controls, and what evidence would falsify that function.

## Inputs

- Module 1 mixture role analysis.
- Target recovery mode and collection/desorption implication.
- Feed composition and objective.
- Known breakthrough order or single-component breakthrough.
- Candidate adsorbents if already available.

## Required Reasoning

1. Start from functions, not material names.
2. Decide whether the first layer should remove bulk impurities, delay a limiting impurity, protect a downstream layer, or shape target pass-through.
3. Decide whether a downstream refining layer is needed to close the final product window.
4. Add a guard layer only when there is a trace or high-affinity impurity that can poison or prematurely occupy downstream capacity.
5. Add a capacity-support layer only when selectivity is adequate but the target or impurity breaks through too early.
6. For every function, define the required sorbent properties and the falsification test.

## Output Schema

```text
Functional Decomposition
- Bed A / front separation layer:
  - Function:
  - Required material behavior:
  - Falsification condition:
- Bed B / downstream refining layer:
  - Function:
  - Required material behavior:
  - Falsification condition:
- Optional Bed C / guard or capacity-support layer:
  - Function:
  - Required material behavior:
  - Falsification condition:
- Why this architecture fits the target recovery mode:
```

## Evidence Standard

- Level 0: function proposed from mixture roles and descriptors.
- Level 2: function supported by single-bed breakthrough.
- Level 3: function supported by multicomponent breakthrough.
- Level 4: function supported by sequence or ratio comparison.

## Failure Modes

- Assigning materials before assigning bed functions.
- Using vague labels such as "polishing" without specifying which impurity is refined.
- Treating a strong adsorbent as automatically suitable for a front layer; excessive target retention may reduce productivity.
- Adding more bed layers without a functional reason.

## Paper-Facing Claim Boundary

Supported claims:
- "The separation problem was decomposed into functional bed layers before material assignment."
- "Each layer was assigned a specific role and falsification criterion."

Claims not supported by this module alone:
- "The selected MOF combination is optimal."
- "The proposed sequence has been experimentally confirmed."

Safe wording:
- Use "functional decomposition motivates" or "we assigned candidate functions".
- Avoid saying "designed bed is optimal" before Module 4-5 evidence.
