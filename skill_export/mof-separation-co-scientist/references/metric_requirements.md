# Metric Requirements For MOF Separation Co-Scientist

Use this file when deciding what metrics to request, compute, or report.

## 1. Mixture Role Metrics

Minimum:
- target molecule
- impurity list
- feed mole fraction or partial pressure
- total pressure and temperature if available
- product specification or collection goal

Derived outputs:
- dominant impurity class: highest feed load or strongest expected affinity
- spec-limiting impurity: most likely to enter product window first
- target recovery mode: exactly one of breakthrough product, adsorbed product, or desorption product
- collection implication: outlet collection window, adsorption-retention window, or desorption/recovery step
- separation difficulty: size similarity, branching/isomerism, polarity, volatility, competitive adsorption

Target recovery mode definitions:
- breakthrough product: target is collected from the outlet before the limiting impurity enters the collection window.
- adsorbed product: target is intentionally retained in the bed and recovered by a later operation.
- desorption product: target is recovered from the regeneration/desorption step rather than the initial effluent.
- If this mode is unknown, ask for the intended collection strategy before making strong configuration claims.

## 2. Sorbent Screening Metrics

Structural:
- PLD: pore limiting diameter
- LCD: largest cavity diameter
- pore size distribution
- channel dimensionality and topology
- void fraction
- accessible surface area
- pore volume

Chemical:
- open metal sites (OMS)
- functional groups
- polarity and electrostatic environment
- hydrophobicity/hydrophilicity
- framework flexibility

Practical:
- thermal/chemical stability
- moisture sensitivity
- activation/regeneration conditions
- synthesis scalability
- estimated cost and availability
- pelletization/forming compatibility

Function matching:
- front separation layer: high capacity for bulk impurities, target pass-through, adequate kinetics
- downstream refining layer: high affinity/selectivity for limiting impurity, moderate target retention
- guard layer: strong retention of trace/high-affinity contaminants, stability under feed exposure
- capacity-support layer: high working capacity with acceptable target penalty

## 3. Experimental Calibration Metrics

Breakthrough:
- `t5`, `t50`, `t95` for target and impurities
- target breakthrough time
- first impurity breakthrough time
- product collection window: `t_first impurity - t_target`
- limiting impurity identity
- breakthrough curve slope or broadening
- bed utilization: dynamic capacity vs equilibrium capacity when possible

Curve integrals:
- dynamic uptake proxy: `∫(1 - C/C0)dt`
- collected target amount: `∫(C_A/C_A0)dt` over the selected collection interval
- purity/recovery-like target metric: `x/y ≈ ∫(C_A/C_A0)dt / (1 × Δt)` for normalized target curve

Productivity/recovery/purity calculation basis:
- measured: calculated from real integrated outlet curves with flow rate, feed composition, bed mass, and collection window.
- curve-integral proxy: estimated from normalized breakthrough curves and an explicit integration interval.
- time-window proxy: inferred only from breakthrough times or clean-window length; label as a window index, not true purity or recovery.
- qualitative estimate: directionally inferred from descriptors, isotherms, or incomplete curves; do not present as a calculated metric.

Isotherm:
- uptake at feed-relevant partial pressure
- Henry-region slope where appropriate
- selectivity proxy at feed pressure
- working capacity between adsorption and regeneration conditions

Kinetics:
- time to breakthrough
- mass-transfer zone width
- curve steepness
- diffusion limitation or tailing

Repeatability:
- replicate variation
- material activation state
- particle size and bed packing consistency
- blank/system control status
- detector calibration and baseline drift
- flow-rate and bed-mass uncertainty
- integration-window uncertainty

## 4. Configuration Metrics

Configuration:
- materials included
- bed order
- bed mass ratio
- total mass
- flow rate, temperature, pressure
- collection cut window

Objectives:
- productivity: collected target per bed mass per time, or proxy if raw amount missing
- recovery: collected target amount divided by theoretical target feed amount in the collection interval
- purity: target fraction in collected product interval when impurity curves are available
- relative clean-window index: window divided by first impurity time; label as window index, not purity
- limiting impurity
- robustness to feed perturbation

Tradeoff:
- target delay penalty
- impurity leakage risk
- adsorbent utilization
- productivity vs recovery vs purity
- sensitivity to ratio changes

## 5. Process Validation Metrics

Regeneration:
- desorption temperature or pressure swing requirement
- regeneration energy proxy
- working capacity after regeneration
- cyclic stability

Scale-up:
- synthesis yield and batch size
- material price or precursor cost proxy
- pelletization stability
- pressure drop proxy
- moisture/contaminant tolerance
- cycle time

TEA proxy:
- adsorbent cost per kg
- regeneration energy per mol target recovered
- productivity per bed volume or bed mass
- replacement frequency or degradation risk

## Minimum Evidence Standards

To claim a material is a good candidate:
- at least descriptor or isotherm support plus one experimental or simulation reason.

To claim a bed function:
- breakthrough or dynamic evidence that supports the function under relevant feed or partial pressure.

To claim a configuration is optimized:
- ratio/sequence comparison, objective definition, and at least one direct or calibrated validation experiment.

To claim process promise:
- performance plus regeneration and practical feasibility discussion.

To claim reproducible improvement:
- replicated final configuration or justified repeat of the key control, comparable operating conditions, and uncertainty discussion.

To claim statistical superiority:
- replicate statistics or another explicit statistical basis. A single-run breakthrough comparison is not enough.

## Evidence Strength Levels

Use these levels whenever recommending a configuration or writing a publication-style claim:

- Level 0: descriptor-only hypothesis.
- Level 1: single-component isotherm support.
- Level 2: single-bed breakthrough support.
- Level 3: multicomponent breakthrough support.
- Level 4: ratio/sequence comparison under a defined objective.
- Level 5: cyclic, regeneration, or process-validation support.

The evidence level limits the wording. Level 0-1 supports "candidate" or "hypothesis"; Level 2-3 supports "experimentally supported function"; Level 4 supports "configuration comparison"; Level 5 supports "process validation outlook."
