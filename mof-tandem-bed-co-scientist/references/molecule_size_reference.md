# Molecule Size Reference

This file stores user-provided molecular dimensions for geometric screening. Dimensions are in Angstrom.

Use this as a preliminary reference only. Before publication-grade screening, record the source or method for each dimension, such as DFT-optimized bounding box, force-field geometry, kinetic diameter, van der Waals bounding box, or literature value.

For pore-window matching, the `intermediate_dimension_A` column is often the most useful first-pass limiting dimension, but it is still only a screening prior. Do not treat geometric matching as proof of breakthrough separation.

## Schema

| field | meaning |
|---|---|
| record_id | unique record identifier |
| molecule | English molecule name |
| length_A | provided first dimension |
| width_A | provided second dimension |
| thickness_A | provided third dimension |
| intermediate_dimension_A | middle value after sorting the three dimensions |
| min_dimension_A | smallest value after sorting |
| max_dimension_A | largest value after sorting |
| source_or_method | source or method label |
| note |

## Size Table

| record_id | molecule | length_A | width_A | thickness_A | intermediate_dimension_A | min_dimension_A | max_dimension_A | source_or_method | note |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| propane_cn | propane | 6.479 | 4.601 | 4.043 | 4.601 | 4.043 | 6.479 | user-provided | preliminary; verify method/source |
| propylene_cn | propylene | 6.518 | 5.104 | 3.920 | 5.104 | 3.920 | 6.518 | user-provided | preliminary; verify method/source |
| isobutane_cn | isobutane | 6.245 | 6.220 | 4.471 | 6.220 | 4.471 | 6.245 | user-provided | preliminary; verify method/source |
| n-butane_cn | n-butane | 7.633 | 4.813 | 4.496 | 4.813 | 4.496 | 7.633 | user-provided | preliminary; verify method/source |
| trans-2-butene_cn | trans-2-butene | 7.788 | 5.131 | 4.094 | 5.131 | 4.094 | 7.788 | user-provided | preliminary; verify method/source |
| isobutene_cn | isobutene | 6.129 | 5.383 | 4.044 | 5.383 | 4.044 | 6.129 | user-provided | preliminary; verify method/source |
| 1-butene_cn | 1-butene | 7.651 | 4.980 | 3.995 | 4.980 | 3.995 | 7.651 | user-provided | preliminary; verify method/source |
| cis-2-butene_cn | cis-2-butene | 7.644 | 4.935 | 4.017 | 4.935 | 4.017 | 7.644 | user-provided | preliminary; verify method/source |
| 1-butene | 1-butene | 7.585 | 4.583 | 4.535 | 4.583 | 4.535 | 7.585 | user-provided | duplicate molecule; keep source distinction |
| 1-chloropropane | 1-chloropropane | 7.100 | 5.721 | 5.044 | 5.721 | 5.044 | 7.100 | user-provided | preliminary; verify method/source |
| 1-hexene | 1-hexene | 10.108 | 4.725 | 4.937 | 4.937 | 4.725 | 10.108 | user-provided | preliminary; verify method/source |
| 1-octene | 1-octene | 12.648 | 4.729 | 4.980 | 4.980 | 4.729 | 12.648 | user-provided | preliminary; verify method/source |
| 1-pentene | 1-pentene | 8.847 | 4.995 | 4.897 | 4.995 | 4.897 | 8.847 | user-provided | preliminary; verify method/source |
| 2,2,4-trimethylpentane | 2,2,4-trimethylpentane | 9.068 | 6.315 | 6.099 | 6.315 | 6.099 | 9.068 | user-provided | preliminary; verify method/source |
| 2,2-dimethylbutane | 2,2-dimethylbutane | 7.829 | 5.502 | 6.545 | 6.545 | 5.502 | 7.829 | user-provided | preliminary; verify method/source |
| 2,2-dimethylhexane | 2,2-dimethylhexane | 10.395 | 5.648 | 6.545 | 6.545 | 5.648 | 10.395 | user-provided | preliminary; verify method/source |
| 2,3-dimethylbutane | 2,3-dimethylbutane | 7.778 | 6.170 | 5.399 | 6.170 | 5.399 | 7.778 | user-provided | preliminary; verify method/source |
| 2-methylpentane | 2-methylpentane | 9.023 | 6.376 | 4.923 | 6.376 | 4.923 | 9.023 | user-provided | preliminary; verify method/source |
| 3,3-dimethylpentane | 3,3-dimethylpentane | 7.269 | 6.397 | 5.724 | 6.397 | 5.724 | 7.269 | user-provided | preliminary; verify method/source |
| 3-methylpentane | 3-methylpentane | 9.052 | 6.008 | 4.985 | 6.008 | 4.985 | 9.052 | user-provided | preliminary; verify method/source |
| acetylene | acetylene | 5.538 | 3.200 | 3.200 | 3.200 | 3.200 | 5.538 | user-provided | preliminary; verify method/source |
| ammonia | ammonia | 3.826 | 3.610 | 3.060 | 3.610 | 3.060 | 3.826 | user-provided | preliminary; verify method/source |
| benzene | benzene | 7.134 | 6.762 | 3.200 | 6.762 | 3.200 | 7.134 | user-provided | preliminary; verify method/source |
| butadiene | butadiene | 7.663 | 5.161 | 3.200 | 5.161 | 3.200 | 7.663 | user-provided | preliminary; verify method/source |
| butane | butane | 7.709 | 4.532 | 3.969 | 4.532 | 3.969 | 7.709 | user-provided | preliminary; verify method/source |
| carbon_dioxide | carbon dioxide | 5.198 | 3.200 | 3.200 | 3.200 | 3.200 | 5.198 | user-provided | preliminary; verify method/source |
| carbon_monoxide | carbon monoxide | 4.168 | 3.200 | 3.200 | 3.200 | 3.200 | 4.168 | user-provided | preliminary; verify method/source |
| carbon_tetrafluoride | carbon tetrafluoride | 4.906 | 4.704 | 4.636 | 4.704 | 4.636 | 4.906 | user-provided | preliminary; verify method/source |
| cis-2-butene | cis-2-butene | 6.702 | 5.310 | 3.960 | 5.310 | 3.960 | 6.702 | user-provided | duplicate molecule; keep source distinction |
| cis-piperylene | cis-piperylene | 8.015 | 5.476 | 3.960 | 5.476 | 3.960 | 8.015 | user-provided | preliminary; verify method/source |
| cyclohexane | cyclohexane | 6.949 | 7.090 | 4.855 | 6.949 | 4.855 | 7.090 | user-provided | preliminary; verify method/source |
| cyclohexene | cyclohexene | 6.976 | 6.561 | 5.022 | 6.561 | 5.022 | 6.976 | user-provided | preliminary; verify method/source |
| cyclooctene | cyclooctene | 7.560 | 7.240 | 5.303 | 7.240 | 5.303 | 7.560 | user-provided | preliminary; verify method/source |
| ethane | ethane | 4.731 | 4.175 | 4.170 | 4.175 | 4.170 | 4.731 | user-provided | preliminary; verify method/source |
| ethylbenzene | ethylbenzene | 9.426 | 6.501 | 4.703 | 6.501 | 4.703 | 9.426 | user-provided | preliminary; verify method/source |
| ethylene | ethylene | 4.679 | 4.047 | 3.200 | 4.047 | 3.200 | 4.679 | user-provided | preliminary; verify method/source |
| heptane | heptane | 11.685 | 4.366 | 3.971 | 4.366 | 3.971 | 11.685 | user-provided | preliminary; verify method/source |
| hexane | hexane | 10.359 | 4.607 | 3.969 | 4.607 | 3.969 | 10.359 | user-provided | preliminary; verify method/source |
| isobutane | isobutane | 6.404 | 6.393 | 4.866 | 6.393 | 4.866 | 6.404 | user-provided | duplicate molecule; keep source distinction |
| isobutene | isobutene | 6.527 | 5.566 | 3.960 | 5.566 | 3.960 | 6.527 | user-provided | duplicate molecule; keep source distinction |
| krypton | krypton | 3.680 | 3.680 | 3.680 | 3.680 | 3.680 | 3.680 | user-provided | preliminary; verify method/source |
| methane | methane | 3.877 | 3.849 | 3.918 | 3.877 | 3.849 | 3.918 | user-provided | preliminary; verify method/source |
| nitrogen | nitrogen | 4.165 | 3.060 | 3.060 | 3.060 | 3.060 | 4.165 | user-provided | preliminary; verify method/source |
| nitrous_oxide | nitrous oxide | 5.287 | 3.060 | 3.060 | 3.060 | 3.060 | 5.287 | user-provided | preliminary; verify method/source |
| nonane | nonane | 14.253 | 4.366 | 3.970 | 4.366 | 3.970 | 14.253 | user-provided | preliminary; verify method/source |
| octane | octane | 12.948 | 4.592 | 3.969 | 4.592 | 3.969 | 12.948 | user-provided | preliminary; verify method/source |
| oxygen | oxygen | 4.076 | 2.860 | 2.860 | 2.860 | 2.860 | 4.076 | user-provided | preliminary; verify method/source |
| perfluoropropane | perfluoropropane | 7.468 | 5.147 | 4.967 | 5.147 | 4.967 | 7.468 | user-provided | preliminary; verify method/source |
| propane | propane | 6.552 | 4.354 | 3.970 | 4.354 | 3.970 | 6.552 | user-provided | duplicate molecule; keep source distinction |
| propylene | propylene | 6.257 | 5.051 | 3.961 | 5.051 | 3.961 | 6.257 | user-provided | duplicate molecule; keep source distinction |
| propyne | propyne | 6.433 | 3.818 | 3.961 | 3.961 | 3.818 | 6.433 | user-provided | preliminary; verify method/source |
| styrene | styrene | 9.542 | 6.849 | 3.200 | 6.849 | 3.200 | 9.542 | user-provided | preliminary; verify method/source |
| toluene | toluene | 8.117 | 6.501 | 3.750 | 6.501 | 3.750 | 8.117 | user-provided | preliminary; verify method/source |
| trans-2-butene | trans-2-butene | 7.219 | 5.151 | 3.961 | 5.151 | 3.961 | 7.219 | user-provided | duplicate molecule; keep source distinction |
| trans-2-hexene | trans-2-hexene | 9.950 | 4.809 | 4.561 | 4.809 | 4.561 | 9.950 | user-provided | preliminary; verify method/source |
| trans-3-hexene | trans-3-hexene | 9.758 | 5.260 | 5.060 | 5.260 | 5.060 | 9.758 | user-provided | preliminary; verify method/source |
| trans-butene | trans-butene | 7.219 | 5.151 | 3.961 | 5.151 | 3.961 | 7.219 | user-provided | preliminary; verify method/source |
| xenon | xenon | 4.320 | 4.320 | 4.320 | 4.320 | 4.320 | 4.320 | user-provided | preliminary; verify method/source |
| xylene | xylene | 7.487 | 7.317 | 3.961 | 7.317 | 3.961 | 7.487 | user-provided | preliminary; verify method/source |
| cis-2-pentene | cis-2-pentene | 8.080 | 5.540 | 5.180 | 5.540 | 5.180 | 8.080 | user-provided | preliminary; verify method/source |
| 1-pentene_alt | 1-pentene | 8.880 | 4.980 | 4.860 | 4.980 | 4.860 | 8.880 | user-provided | duplicate molecule; keep source distinction |
| trans-2-pentene | trans-2-pentene | 8.790 | 4.730 | 4.620 | 4.730 | 4.620 | 8.790 | user-provided | preliminary; verify method/source |
| isoprene | isoprene | 7.746 | 6.093 | 3.963 | 6.093 | 3.963 | 7.746 | user-provided | preliminary; verify method/source |
| n-pentane | n-pentane | 9.118 | 4.364 | 3.969 | 4.364 | 3.969 | 9.118 | user-provided | preliminary; verify method/source |

## C6 Feed Coverage Check

For the current C6 hydrocarbon feed commonly discussed with this skill, the following molecule-size records are present:

| component | matching record_id | status |
|---|---|---|
| 2,2-dimethylbutane | `2,2-dimethylbutane` | present |
| 2,3-dimethylbutane | `2,3-dimethylbutane` | present |
| 2-methylpentane | `2-methylpentane` | present |
| 3-methylpentane | `3-methylpentane` | present |
| 1-hexene | `1-hexene` | present |
| n-hexane / hexane | `hexane` | present |
| nitrogen | `nitrogen` | present |

Missing C6 feed molecules: none in the listed feed set.
