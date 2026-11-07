# Material Recommendation Input Protocol

Use this file when the workflow moves from early-stage structural targets to candidate material recommendation. This protocol defines the minimum inputs needed to recommend candidate MOFs from a user-provided or project-specific database.

## Purpose

Material recommendation should be database-backed and descriptor-matched. The co-scientist should not rely on memory or generic famous-material lists when the user can provide a candidate database.

The intended progression is:

```text
structural target profile
-> molecule size table
-> user-provided markdown notes and/or MOF descriptor database path
-> descriptor schema mapping
-> broad function-specific candidate space
-> optional shortlist only when needed
-> evidence gaps and next experiments
```

## Required Inputs

### Molecule Size Table

Use a molecule-size table for all target and impurity molecules. The user may provide calculated, literature, or software-derived dimensions.

```text
Molecule Size Table
| component | role | length_A | width_A | thickness_A | limiting_dimension_A | source_or_method | note |
|---|---|---:|---:|---:|---:|---|---|
```

Guidance:

- The middle or limiting dimension is often the most useful for pore-window matching.
- Record the method used to estimate dimensions, such as DFT geometry, force-field optimized geometry, kinetic diameter, van der Waals bounding box, or literature value.
- Do not mix dimension definitions without labeling them.
- If dimensions are uncertain or method-mismatched, use them only as screening priors.

### MOF Descriptor Database

The database path is project-specific and should be supplied by the user or configured for the project.

```text
MOF Descriptor Database
- database_path:
- file_format: csv / xlsx / parquet / sqlite / json / other
- material_id_field:
- descriptor_fields:
  - PLD:
  - LCD:
  - GLD:
  - pore_size_distribution:
  - surface_area:
  - pore_volume:
  - topology:
  - dimensionality:
  - OMS:
  - functional_groups:
  - polarity_or_charge:
  - hydrophobicity:
  - OMS_status:
  - stability:
  - availability:
- units:
- source:
- filters_or_exclusions:
```

Notes:

- Treat `PLD`, `LCD`, and `GLD` as database-defined fields unless the user defines them. Record the database definition and unit before filtering.
- Typical use: `PLD` for aperture accessibility, `LCD` for cavity accommodation, and `GLD` or an equivalent path/window descriptor for transport through the pore network.
- If a database uses different names, map them explicitly in `descriptor_fields`.
- If the database lacks `GLD`, use the closest available transport descriptor and label the substitution.

## Hard Filter Logic

Apply hard filters before ranking:

1. Geometric accessibility:
   - reject materials whose aperture/path descriptor is clearly smaller than the component that must enter;
   - reject materials whose cavities are too small for the target or relevant impurity;
   - keep a tolerance band for flexible frameworks and uncertain molecular dimensions.

2. Function matching:
   - for target breakthrough-product mode, avoid structures predicted to strongly retain the target unless the function is impurity capture with minimal target penalty;
   - for adsorbed/desorption-product mode, prioritize structures that can retain the target and later release it.

3. Practical constraints:
   - remove materials that are unavailable, unstable under the feed or activation conditions, unsafe, or not synthesizable at the project stage.

## Function-Specific Matching

Use this table before any final candidate list:

```text
Descriptor Match Plan
| function | molecule dimension constraint | PLD/LCD/GLD logic | chemistry requirement | hard exclusions | soft priorities |
|---|---|---|---|---|---|
```

First output a broad candidate space:

```text
Candidate Material Space
| function | candidate | inclusion_reason | matching_features | evidence_type | evidence_level | uncertainty | human_selection_note |
|---|---|---|---|---|---:|---|---|
```

Then, only if the user asks for prioritization or the experiment budget requires narrowing, output:

```text
Candidate Shortlist
| function | material_id | matched_descriptors | why_candidate | evidence_level | risk | next_validation |
|---|---|---|---|---:|---|---|
```

## Ranking Discipline

- Rank only within a function, not globally across all MOFs.
- Build a candidate space before ranking; do not discard plausible candidates just because their evidence is preliminary.
- Separate hard-filter pass/fail from soft ranking.
- Keep geometric fit, adsorption affinity, kinetics, target-retention penalty, and practicality as separate columns.
- If only descriptors are available, evidence level is Level 0.
- If feed-relevant isotherms are available, evidence may become Level 1.
- If breakthrough data are available, evidence may become Level 2 or higher.

## Missing-Data Behavior

If molecule dimensions are missing:

- ask for the molecule-size table;
- if the user wants to use the built-in preliminary table, read `molecule_size_reference.md` and verify that the relevant molecules and dimension methods are acceptable;
- or state which dimension method will be used;
- do not run geometric matching silently.

If the database path is missing:

- ask for the project-specific database path;
- if the user wants to use the built-in project-local descriptor reference, read `mof_pld_lcd_gld_reference.md`;
- or output the required database schema;
- do not invent a material list from memory unless the user explicitly asks for literature examples.

If manually curated pore sizes are provided:

- record them in or read from `manual_pore_size_reference.md`;
- keep manual cage/window/channel descriptions separate from database PLD/LCD/GLD descriptors;
- state which source is used for each screening step.

If user-provided markdown notes are supplied:

- parse them for material names, pore descriptions, OMS status, qualitative adsorption behavior, synthesis availability, and warnings;
- preserve the note-derived evidence separately from database descriptors;
- include plausible materials in the candidate space with an uncertainty label rather than silently dropping them.

If OMS status matters:

- read `oms_reference.md`;
- distinguish classic intrinsic OMS, defect-induced sites, and materials that are often misclassified as OMS;
- treat OMS as activation-state dependent;
- do not infer accessible OMS only from solvated CIFs.

If `PLD/LCD/GLD` definitions are unclear:

- ask for the database documentation or column definitions;
- treat filters as preliminary.

## Paper-Facing Claim Boundary

Supported claims:
- "Candidate MOFs were organized into a function-specific candidate space using project-specific molecular dimensions, markdown notes, and/or descriptor databases."
- "The screening separated hard geometric filters from function-specific soft priorities."

Claims not supported:
- "The shortlisted candidate is optimal."
- "Geometric fit alone proves separation."
- "The ranking predicts breakthrough performance without dynamic validation."

Safe wording:
- Use "candidate material space", "descriptor-matched candidates", "geometric screening", "function-specific shortlist", and "screening priority."
- Avoid "best MOF" unless the ranking basis and evidence level are explicitly defined.
