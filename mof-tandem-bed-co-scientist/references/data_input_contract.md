# Data Input Contract

Use this file when raw experimental, simulation, descriptor, isotherm, or breakthrough data are provided to the co-scientist. The goal is to convert heterogeneous research notes into a consistent, auditable input state before reasoning.

## Purpose

Publication-grade co-scientist reasoning requires a stable data contract. The LLM should not jump from raw notes to a MOF recommendation. It must first convert the inputs into explicit tables, label missing fields, and classify what level of inference the data can support.

## Required Input Blocks

### Project Block

```text
Project
- project_id:
- target_molecule:
- target_recovery_mode: breakthrough product / adsorbed product / desorption product / unknown
- objective_priority: productivity / recovery / purity / robustness
- experiment_budget:
- total_bed_mass_constraint:
- allowed_materials:
```

### Feed Composition Block

```text
Feed Composition
| component | partial_pressure_kPa | mole_fraction | role | note |
|---|---:|---:|---|---|
```

Minimum requirements:
- component names;
- either partial pressure or mole fraction;
- target component;
- total pressure and temperature when available.

If only ratios are available, normalize them and state the normalization basis. If partial pressures are available, use them as the primary feed-relevant basis.

### Material Descriptor Block

```text
Material Descriptors
| material | PLD | LCD | GLD | PSD | surface_area | pore_volume | OMS | functional_group | polarity | stability | availability |
|---|---:|---:|---:|---|---:|---:|---|---|---|---|---|
```

Minimum requirements for descriptor-based screening:
- material name;
- at least one structural descriptor or literature-based function rationale;
- practical availability or synthesis status.

For database-backed material recommendation, also provide or configure:

```text
Molecule Size Table
| component | role | length_A | width_A | thickness_A | limiting_dimension_A | source_or_method | note |
|---|---|---:|---:|---:|---:|---|---|

MOF Descriptor Database
- database_path:
- file_format:
- material_id_field:
- PLD_field:
- LCD_field:
- GLD_field:
- units:
- source:
```

Use `material_recommendation_input_protocol.md` when molecule dimensions and a descriptor database are supplied.

### Isotherm Block

```text
Isotherm Data
| material | component | temperature | pressure_range | uptake_at_feed_pressure | unit | model_or_raw | source |
|---|---|---:|---|---:|---|---|---|
```

Minimum requirements for Level 1 evidence:
- material;
- component;
- temperature;
- uptake at or near feed-relevant partial pressure;
- unit and source.

Do not compare isotherms across materials unless temperature, activation, pressure basis, and units are aligned or explicitly corrected.

### Breakthrough Block

```text
Breakthrough Data
| material_or_config | component | feed_basis | bed_mass | flow_rate | temperature | t5 | t50 | t95 | outlet_order | source |
|---|---|---|---:|---:|---:|---:|---:|---:|---|---|
```

Minimum requirements for Level 2 evidence:
- material or configuration;
- feed basis;
- bed mass;
- component breakthrough order or target/impurity breakthrough time.

If only qualitative descriptions are available, record them as qualitative observations and do not report measured recovery or purity.

### Serial-Bed Configuration Block

```text
Serial-Bed Configuration
| configuration_id | bed_order | material_1_mass | material_2_mass | total_mass | feed_condition | objective | observed_result |
|---|---|---:|---:|---:|---|---|---|
```

Minimum requirements for Level 4 configuration comparison:
- at least two sequence or ratio configurations;
- same or comparable feed and operating conditions;
- explicit objective metric or proxy.

## Data Sufficiency Classes

Use these classes before recommending a configuration:

- `complete`: required fields are present for the requested claim.
- `usable with proxy`: enough data exist for directional reasoning, but metrics must be labeled as proxies.
- `qualitative only`: only qualitative observations exist; recommend experiments but avoid quantitative claims.
- `insufficient`: key fields are missing and a strong recommendation would be misleading.

When the class is `insufficient` because only feed composition and target are available, the correct next output is an early-stage structural target profile, not a named MOF recommendation or configuration. Use `early_stage_structural_target_protocol.md`.

## Conversion Output

Every analysis should start with:

```text
Input Conversion
- data sufficiency:
- normalized feed basis:
- target recovery mode:
- evidence blocks available:
- missing fields:
- claims allowed:
- claims not allowed:
```

## Missing-Data Questions

Ask only questions that change the decision. High-value questions:

- Is the target collected from breakthrough, retained adsorption, or desorption?
- What are the bed mass, flow rate, and temperature for each breakthrough curve?
- Are curves normalized as `C/C0`, detector signal, or calibrated molar flow?
- What collection window is experimentally practical?
- Is the objective productivity-first, recovery-first, or purity-first?
- Can only one experiment be run, or is ratio/sequence comparison possible?

## Paper-Facing Claim Boundary

Supported claims:
- "Raw feed, isotherm, descriptor, and breakthrough data were converted into a structured input state before co-scientist reasoning."
- "Missing fields and proxy-level metrics were explicitly labeled."

Claims not supported by the contract alone:
- "The recommended configuration is correct."
- "The configuration is optimized."
- "The reported proxy equals true recovery or purity."

Safe wording:
- Use "structured input conversion", "data sufficiency class", and "proxy-labeled metric".
- Avoid quantitative performance claims unless the required raw data are present.
