# Brief Change Summary

Date: 2026-07-13

## Main Direction

The skill was upgraded from a C6-specific or prompt-like workflow into a more general MOF adsorption-separation co-scientist package. The active skill now emphasizes staged reasoning:

```text
feed/target definition
-> data input contract
-> early structural target profile
-> candidate material space
-> descriptor-backed material screening
-> breakthrough/isotherm calibration
-> configuration hypothesis
-> process validation
-> manuscript/reproducibility trace
```

## Major Changes

1. Active skill decontaminated for held-out testing
   - Removed C6-specific protocol and C6 forward-test fixture from the active skill.
   - Moved C6 files to `private_cases/`.
   - Active skill no longer contains `nHEX`, `HKUST/UiO/Zn-MOF` case-specific hints from the original C6 fixture.

2. Chinese reading aids added
   - Added `cn/` documentation for easier reading.
   - Chinese files are explanatory only; the formal skill remains English.

3. Structured run logging added
   - Added `references/run_logging_protocol.md`.
   - Logs capture input snapshot, module trace, reasoning summaries, evidence log, decision log, metric log, final output snapshot, human intervention, and next-state record.
   - Logs are not described as hidden chain-of-thought.

4. Early-stage structural target protocol added
   - Added `references/early_stage_structural_target_protocol.md`.
   - When only feed and target are supplied, the skill stops at task definition, functional requirements, and structural target profile.
   - It does not name candidate materials, bed order, or mass ratio too early.

5. Material recommendation input protocol added
   - Added `references/material_recommendation_input_protocol.md`.
   - Requires molecule-size table plus project-specific descriptor database path or built-in project-local references.
   - Uses mapped `PLD/LCD/GLD` fields before descriptor-backed screening.

6. Candidate material space behavior added to Module 3
   - Module 3 now first builds a broad function-specific `Candidate Material Space`.
   - Shortlisting is optional and only used when the user requests prioritization or the experiment budget requires narrowing.
   - User-provided markdown notes are parsed into candidate names, pore descriptions, OMS status, risks, and evidence labels.

7. Reference tables added
   - `references/molecule_size_reference.md`: user-provided molecular dimensions with intermediate dimension.
   - `references/manual_pore_size_reference.md`: manually curated pore-size notes and cage/channel descriptions.
   - `references/mof_pld_lcd_gld_reference.md`: project-local PLD/LCD/GLD rows.
   - `references/oms_reference.md`: OMS families, classic examples, misclassified materials, and practical checks.

8. Module and protocol updates
   - Updated `SKILL.md`, `data_input_contract.md`, `module_3_sorbent_screening_engine.md`, `module_5_configuration_optimizer.md`, `co_scientist_prompt_template.md`, and validation script.
   - Added stricter claim discipline for insufficient data.
   - Added database/source separation between manual pore notes and computed descriptors.

## Current Validation

Validated on Mac with:

```bash
python3 scripts/validate_skill_structure.py .
```

Result:

```text
mof-separation-co-scientist structure ok
```

## Important Use Boundary

The active skill should be treated as general. Private case files should not be copied into the active skill during blind or held-out validation.
