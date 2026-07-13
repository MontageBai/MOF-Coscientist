# Manual Pore Size Reference

This file stores user-provided pore descriptions for selected MOFs. These values are literature-style or manually curated pore-size notes, not necessarily the same as database-calculated PLD/LCD/GLD values.

Use this file as a qualitative or semi-quantitative reference when interpreting cage-window structures, one-dimensional channels, and manually reported aperture/cage sizes. For database-backed geometric screening, use `mof_pld_lcd_gld_reference.md`.

## Schema

| field | meaning |
|---|---|
| material | material name |
| structure_type | cage, one-dimensional channel, three-dimensional channel, or mixed |
| manual_pore_description | user-provided pore-size description |
| parsed_windows_A | aperture/window values parsed from the note when clear |
| parsed_cages_or_channels_A | cavity/channel values parsed from the note when clear |
| screening_comment | first-pass interpretation for size-based screening |
| source_or_method |

## Table

| material | structure_type | manual_pore_description | parsed_windows_A | parsed_cages_or_channels_A | screening_comment | source_or_method |
|---|---|---|---|---|---|---|
| CopzNi | one-dimensional channel | 4.1 x 5.2 | 4.1 x 5.2 | 1D channel | tight anisotropic channel; possible directional/kinetic screen | user-provided |
| MOF-808 | cage | 4.8 and 18.4 | 4.8 | 18.4 | window near n-hexane intermediate dimension; large cage | user-provided |
| HKUST-1 | cage | (5.3) 10.8 / 6.9 | 5.3 | 10.8 / 6.9 | larger cage-window material; likely admits multiple C6 species | user-provided |
| UiO-66 | cage | (6.0) 8.4 / 7.4 | 6.0 | 8.4 / 7.4 | window larger than n-hexane and many impurities; weaker pure size exclusion | user-provided |
| UiO-66-NH2 | cage | (5.6) 8.4 / 7.4 | 5.6 | 8.4 / 7.4 | moderate window; may restrict bulkier C6 species more than n-hexane | user-provided |
| BUT-315 | three-dimensional channel | 1.0 x 5.2, 4.4 x 6.0, and 5.4 x 5.4 A | 1.0 x 5.2; 4.4 x 6.0; 5.4 x 5.4 | 3D channel network | multiple apertures; possible anisotropic or pathway-dependent transport | user-provided |
| Ni-BTP | cage + one-dimensional channel | 6 and ~10 | 6.0 | ~10 | open enough for several C6 molecules; use as broader-window comparator | user-provided |
| MOF-801 | cage | (4.7 A) 5.6 / 7.4 | 4.7 | 5.6 / 7.4 | tight cage-window near n-hexane intermediate dimension | user-provided |
| Al-Fum | one-dimensional channel | 6.8 A | 6.8 | 1D channel | aperture larger than listed C6 intermediate dimensions; likely weak pure size exclusion | user-provided |

## Notes

- Parentheses are interpreted as window/aperture values when the note follows a cage-window style, such as `(4.7 A) 5.6 / 7.4`.
- Manual pore descriptions may use different definitions than Zeo++ or database PLD/LCD/GLD values. Do not merge them without noting the source.
- Use manual values to explain structural intuition; use database PLD/LCD/GLD for reproducible filtering.
