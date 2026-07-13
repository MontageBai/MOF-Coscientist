# Module 7 - Process Validation Engine

## Purpose

Translate a promising lab configuration into a process-validation plan. This module keeps publication claims balanced: breakthrough performance can support a strong research hypothesis, but process feasibility requires regeneration, cycling, material handling, and cost evidence.

## Inputs

- Best configuration and evidence level.
- Repeat breakthrough results.
- Regeneration or desorption conditions.
- Cycle stability.
- Pelletization or particle-size information.
- Synthesis batch size, yield, cost, and availability.
- Flow rate, pressure drop proxy, and bed-volume information when available.

## Required Reasoning

1. Separate lab separation performance from process readiness.
2. Identify the regeneration method and energy proxy.
3. Estimate working capacity between adsorption and regeneration conditions.
4. Assess material practicality: stability, moisture tolerance, activation, pelletization, and cost.
5. Define what must be shown for pilot readiness.
6. State which claims are currently publication-safe and which require additional validation.

For detailed regeneration, scale-up, and TEA proxy requirements, read `regeneration_scaleup_tea_protocol.md`.

## Output Schema

```text
Process Validation Outlook
- Best lab configuration:
- Current evidence level:
- Repeatability status:
- Regeneration route:
- Regeneration energy proxy:
- Working capacity evidence:
- Material cost/synthesis risk:
- Pelletization/pressure-drop risk:
- Cycle stability:
- Working-capacity proxy:
- Shaping/pressure-drop risk:
- Largest TEA uncertainty:
- Pilot validation experiment:
- Publication-safe claim:
- Claim not yet supported:
```

## Evidence Standard

- Level 3: multicomponent performance supports a promising separation configuration.
- Level 4: ratio/sequence comparison supports configuration optimization claims.
- Level 5: cycling, regeneration, and practical validation support process-readiness claims.

## Failure Modes

- Claiming scale-up feasibility from one breakthrough curve.
- Ignoring regeneration energy when a material strongly adsorbs the target or impurity.
- Ignoring material cost, synthesis difficulty, moisture sensitivity, or shaping.
- Presenting machine learning or LLM reasoning as replacing physical simulation or experiments.

## Paper-Facing Claim Boundary

Supported claims:
- "The optimized lab configuration defines a process-validation plan."
- "Regeneration, cycling, material practicality, and cost were identified as scale-up requirements."
- "The co-scientist framework extends high-throughput prediction into experimental planning."

Claims not supported without Level 5 evidence:
- "The process is industrially feasible."
- "The adsorbent is economically superior."
- "The configuration is pilot-ready."

Safe wording:
- Use "process-validation outlook", "pilot-ready hypothesis", or "scale-up requirements".
- State clearly that machine learning and LLM reasoning complement, rather than replace, physical simulation and experiments.
