# Regeneration, Scale-Up, And TEA Proxy Protocol

Use this file when a recommendation, manuscript, slide deck, or reviewer response discusses process validation, regeneration, cyclic stability, material practicality, scale-up, or techno-economic relevance.

## Purpose

Breakthrough performance alone does not establish process feasibility. A publication-grade co-scientist must separate laboratory separation promise from process readiness by checking regeneration route, working capacity, cycle stability, material cost, shaping, pressure drop, and scale-up synthesis risk.

## Minimum Process-Relevance Inputs

```text
Process-Relevance Input
- best_configuration:
- target_recovery_mode:
- adsorption_condition:
- regeneration_condition:
- cycle_count:
- material_form: powder / pellet / granule / monolith / unknown
- synthesis_batch_size:
- material_cost_or_precursor_proxy:
- moisture_or_contaminant_tolerance:
- pressure_drop_or_particle_size_proxy:
- safety_or_handling_constraint:
```

If these fields are missing, report "process-validation outlook" rather than "process feasibility".

## Regeneration Assessment

### Required Fields

```text
Regeneration Record
| material | retained species | regeneration method | temperature | pressure | purge gas | desorption completeness | evidence |
|---|---|---|---:|---:|---|---|---|
```

Methods:
- thermal swing;
- pressure/vacuum swing;
- purge gas;
- solvent or displacement regeneration;
- combined route.

Key questions:
- Does regeneration release the target or impurity without damaging the MOF?
- Does the required temperature conflict with framework stability?
- Does strong adsorption improve purity but raise regeneration energy?
- Is desorption complete enough for repeat cycles?

## Working Capacity Proxy

Preferred:

```text
working capacity = q_adsorption(condition) - q_regeneration(condition)
```

If full isotherms are missing:

- use feed-relevant uptake and a qualitative regeneration penalty;
- label as qualitative or proxy;
- do not report absolute energy-normalized productivity.

## Cycle Stability

Minimum cycle table:

```text
Cycle Stability
| material/configuration | cycle | activation/regeneration condition | target window | limiting impurity | capacity retention | note |
|---|---:|---|---|---|---:|---|
```

Claim boundary:
- 1 cycle: regeneration feasibility observation.
- 3 cycles: preliminary cycle stability.
- 5+ cycles: stronger lab-scale cyclic stability claim.
- Long-term process stability requires more extensive cycling and shaped material data.

## Material Practicality

Track:

- synthesis yield;
- batch size;
- precursor cost and availability;
- activation complexity;
- moisture stability;
- air stability;
- pelletization or shaping feasibility;
- particle attrition;
- binder effects;
- safety or solvent concerns.

Do not assume a high-performing powder is process-ready.

## Pressure Drop And Shaping Proxy

Minimum fields:

```text
Shaping/Pressure-Drop Proxy
| material | form | particle_size | binder | bed_length | flow_rate | pressure_drop | note |
|---|---|---:|---|---:|---:|---:|---|
```

If pressure drop is unavailable:
- state that scale-up pressure-drop risk is unquantified;
- avoid process-ready wording.

## TEA Proxy

Use proxy-level TEA only when detailed process simulation is absent.

Recommended proxy metrics:

- adsorbent cost proxy per kg;
- regeneration energy proxy per mol target recovered;
- target productivity per bed mass or bed volume;
- cycle time;
- replacement frequency or capacity-retention proxy;
- synthesis scale risk;
- shaping/pressure-drop risk.

Output:

```text
TEA Proxy Summary
- productivity basis:
- recovery/purity basis:
- regeneration energy proxy:
- adsorbent cost proxy:
- cycle-time proxy:
- material lifetime risk:
- pressure-drop/shaping risk:
- strongest economic advantage:
- largest economic uncertainty:
```

## Decision Rules

- If separation improves but regeneration is severe, state the productivity-purity-energy tradeoff.
- If material cost or synthesis is unknown, do not claim economic advantage.
- If only powder data exist, state shaped-bed validation is required.
- If no cycles exist, claim process-validation plan, not process readiness.
- If the target is retained strongly, require desorption evidence before recommending scale-up.

## Paper-Facing Claim Boundary

Supported claims:
- "The optimized lab configuration was extended into a process-validation plan."
- "Regeneration route, working-capacity proxy, cycle stability, material practicality, and TEA proxy were identified as required process checks."
- "The analysis distinguishes lab-scale separation performance from process readiness."

Claims not supported without evidence:
- "The process is economically superior."
- "The adsorbent is industrially viable."
- "The configuration is pilot-ready."
- "The material can be regenerated cheaply."

Safe wording:
- Use "TEA proxy", "process-validation outlook", "scale-up risk", "regeneration penalty", and "working-capacity proxy".
- Avoid "industrially feasible", "economically optimal", or "pilot-ready" unless supported by Level 5 evidence and practical material data.
