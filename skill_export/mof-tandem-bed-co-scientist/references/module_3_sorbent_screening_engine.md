# Module 3 - Sorbent Screening Engine

## Purpose

Map each bed function to a function-compatible candidate material space using structural descriptors, chemical functionality, simulations, literature, user-provided markdown notes, and available experiments. This module does not produce a global best-MOF ranking; it first builds a broad per-function candidate space, then optionally narrows it to a shortlist when the user asks for prioritization or when the experiment budget requires it.

## Inputs

- Functional decomposition from Module 2.
- MOF database, descriptor table, simulated adsorption data, literature, or user-provided candidate set.
- User-provided markdown notes or reference files that describe pore size, topology, OMS status, known adsorption behavior, synthesis availability, or experimental observations.
- Molecule-size table for target and impurity molecules when geometric screening is requested.
- Descriptor fields such as PLD, LCD, GLD or equivalent transport/path descriptor, pore size distribution, accessible surface area, pore volume, void fraction, channel dimensionality, topology, OMS, functional groups, and polarity.
- Project-specific database path and descriptor-field mapping when using a local or user-provided database.
- Practical constraints: synthesis availability, activation, stability under the feed, and safety.

## Required Reasoning

1. Translate each function into descriptor requirements.
   - If no candidate list, database, descriptor table, isotherms, or literature set is provided, stop at structural target profiles and do not name candidate MOFs.
   - If molecule dimensions and a database path are supplied, apply `material_recommendation_input_protocol.md` before candidate shortlisting.
2. Build a candidate space before narrowing:
   - include all materials that plausibly satisfy at least one required function;
   - group materials by function rather than forcing one winner;
   - mark inclusion reason, evidence type, uncertainty, and the next validation needed.
3. Apply hard exclusions only for clear failures:
   - impossible geometric accessibility under the stated descriptor definitions;
   - obvious incompatibility with the feed or activation condition;
   - unavailable or unsafe materials when practical availability is part of the task.
4. Use soft priorities only inside each function layer. Soft priorities should guide human selection, not prematurely discard plausible candidates.
5. Keep equilibrium capacity, selectivity, kinetics, target-retention penalty, and practicality separate.
6. Prefer a candidate space with complementary roles over one material with a high aggregate score.
7. If high-throughput simulation is available, recommend screening filters and control materials.
8. If the user provides markdown notes, extract candidate names, pore descriptions, OMS status, known risks, and evidence statements into a structured candidate-space table before ranking.

## Output Schema

```text
Function-Compatible Candidate Map
| function | required descriptors | candidate MOFs | evidence type | per-function priority | risk |

Candidate Material Space
| function | candidate | inclusion_reason | matching_features | evidence_type | evidence_level | uncertainty | human_selection_note |

Descriptor Match Plan
| function | molecule dimension constraint | PLD/LCD/GLD logic | chemistry requirement | hard exclusions | soft priorities |

Candidate Shortlist
| function | material_id | matched_descriptors | why_candidate | evidence_level | risk | next_validation |

Structural Target Profile
| function | desired structure/chemistry | avoid | reason | data needed to search |

Screening Notes
- Hard filters:
- Candidate-space inclusion rule:
- Soft priorities:
- Human selection handles:
- Controls:
- Data needed before experiments:
```

## Evidence Standard

- Level 0: descriptor-only candidate.
- Level 1: descriptor plus single-component isotherm.
- Level 2: candidate has single-bed breakthrough support.
- Level 3: candidate has multicomponent support.

## Failure Modes

- Producing one global MOF ranking.
- Prematurely reducing a broad candidate space to a tiny list when the user only asked for possible candidates.
- Naming specific MOFs when the input contains only a feed composition and no candidate evidence.
- Running geometric screening without a molecule-size table or without mapping database-specific PLD/LCD/GLD fields.
- Treating high uptake as high separation performance.
- Ignoring kinetic broadening, diffusion limits, and target-retention penalty.
- Comparing candidates at irrelevant pressures rather than feed-relevant partial pressures.
- Ignoring material availability and activation practicality.

## Paper-Facing Claim Boundary

Supported claims:
- "Descriptor-guided screening identified a function-compatible candidate material space."
- "Candidates were prioritized within each functional layer, not by a global best-MOF ranking."

Claims not supported by this module alone:
- "The top candidate will outperform all other MOFs experimentally."
- "Equilibrium uptake proves dynamic separation."
- "The screened configuration is optimized."

Safe wording:
- Use "candidate space", "candidate", "screening priority", "function-compatible", and "human selection note".
- Use "structural target profile" when candidate evidence is not yet supplied.
- Use "descriptor-matched shortlist" when molecule dimensions and database descriptors are supplied.
- Avoid "best MOF" unless the ranking scope and evidence basis are explicitly defined.
