# Early-Stage Structural Target Protocol

Use this file when the user provides a separation task and feed composition, but does not yet provide a candidate MOF list, descriptor table, isotherms, or breakthrough data.

## Purpose

At the earliest stage, the co-scientist should identify the separation problem and define structural/material-function targets. It should not jump directly to named materials, bed sequences, mass ratios, or optimization claims.

The intended progression is:

```text
task definition
-> target recovery mode
-> separation logic
-> bed-function requirements
-> structural target profile
-> data needed for material search
-> candidate material search in a later step
```

## Stage Gate

If only feed composition and target are available:

- allowed:
  - define the separation task;
  - identify the target recovery mode and objective;
  - identify likely impurity classes and uncertainties;
  - define bed-layer functions;
  - define structural targets such as cage-window topology, pore aperture range, gate-opening behavior, hydrophobicity, polarity, OMS avoidance or use, diffusion selectivity, and target-retention limits;
  - propose the next data needed for material search.

- not allowed:
  - name a best MOF;
  - name a primary material configuration;
  - give a bed mass ratio;
  - claim a limiting impurity as known;
  - claim productivity, recovery, or purity;
  - imply optimization.

## Structural Target Profile

Use this output before naming materials:

```text
Structural Target Profile
| function | desired structure/chemistry | avoid | reason | data needed to search |
|---|---|---|---|---|
```

Possible descriptors:

- pore limiting diameter (PLD);
- largest cavity diameter (LCD);
- cage-window architecture;
- one-dimensional channel vs cage network;
- gate-opening or flexible-window behavior;
- pore size distribution;
- hydrophobicity;
- polarity and electrostatic environment;
- OMS density or absence of strong OMS;
- functional groups;
- kinetic aperture and diffusion selectivity;
- framework rigidity/flexibility;
- C6 stability under the stated feed and activation conditions.

## Hydrocarbon Breakthrough-Product Caution

For hydrocarbon mixtures where a linear alkane target is requested as a breakthrough product, explicitly flag that many microporous adsorbents may preferentially retain the linear molecule. In that situation, the early-stage target should focus on structures that delay impurities while limiting target retention, rather than structures that simply maximize target uptake.

Safe wording:

```text
The current stage supports a structural target profile, not a material recommendation. The next step is to search candidate MOFs whose descriptors match this profile and then test whether their dynamic breakthrough order supports the intended recovery mode.
```

## Minimal Next Step

After the structural target profile, ask for or generate:

1. candidate database or allowed material list;
2. molecule-size table for target and impurity molecules, including length, width, thickness, and a limiting or middle dimension;
3. descriptor table or database path with mapped PLD, LCD, GLD or equivalent transport/path descriptor, topology, pore size distribution, OMS/functionality, hydrophobicity, stability, and availability;
4. feed-relevant single-component isotherms;
5. single-bed multicomponent breakthrough curves with `t5/t50/t95`;
6. carrier-gas adsorption assumption or evidence.

When the user supplies the molecule-size table and descriptor database path, move to `material_recommendation_input_protocol.md`.

## Paper-Facing Claim Boundary

Supported claims:
- "The co-scientist converted the feed and objective into a structural target profile for candidate discovery."
- "The early-stage output defined material search criteria before selecting named adsorbents."

Claims not supported:
- "A candidate material is optimal."
- "The bed sequence or mass ratio is selected."
- "The target product can be recovered at a given purity or productivity."

Safe wording:
- Use "structural target", "candidate search criteria", "function-derived descriptor requirements", and "early-stage hypothesis".
- Avoid "recommended MOF", "optimized configuration", or "best material" until candidate evidence is supplied.
