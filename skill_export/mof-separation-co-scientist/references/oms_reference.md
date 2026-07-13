# Open Metal Site Reference

OMS means open metal site, also called a coordinatively unsaturated metal site (CUS). In MOFs, an OMS usually forms after coordinated water or solvent is removed during activation, leaving a metal center that can directly coordinate gas molecules or reactants.

Use this file as a screening and interpretation reference. OMS presence must be treated as activation-state dependent. Do not infer accessible OMS only from a solvated CIF without checking whether the coordinated solvent can be removed without framework collapse and whether the resulting metal site is accessible.

## Classic OMS MOF Families

| MOF family or representative material | metal center | node or coordination unit | OMS formation route | OMS features and common uses |
|---|---|---|---|---|
| Mg-MOF-74 / Mg2(dobdc) | Mg2+ | one-dimensional Mg-O chain | activation removes coordinated water/solvent | strong oxophilic OMS; CO2, H2O, SO2, NH3 adsorption |
| Ni-MOF-74 / Ni2(dobdc) | Ni2+ | one-dimensional Ni-O chain | axial solvent removal | stronger interaction with CO, olefins, sulfur-containing molecules |
| Co-MOF-74 / Co2(dobdc) | Co2+ | one-dimensional Co-O chain | coordinated solvent removal | gas adsorption, oxidation, catalysis |
| Fe-MOF-74 / Fe2(dobdc) | Fe2+ | one-dimensional Fe-O chain | activation forms five-coordinate Fe2+ | O2, NO, hydrocarbon activation; often air-sensitive |
| Mn-MOF-74 / Mn2(dobdc) | Mn2+ | one-dimensional Mn-O chain | coordinated solvent removal | CO2, hydrocarbons, polar molecule adsorption |
| Zn-MOF-74 / Zn2(dobdc) | Zn2+ | one-dimensional Zn-O chain | coordinated solvent removal | relatively weaker OMS; adsorption and optical studies |
| Cu-MOF-74 | Cu2+ | one-dimensional Cu-O chain | solvent removal | can form unsaturated Cu sites; structure/stability should be verified |
| M2(m-dobdc), such as Mg2(m-dobdc), Co2(m-dobdc) | Mg2+, Co2+, etc. | MOF-74-like one-dimensional chain | coordinated solvent removal | stronger pore electric field; low-pressure CO2, olefin, and polar gas adsorption |
| HKUST-1 / Cu-BTC / Cu3(BTC)2 | Cu2+ | Cu2 paddlewheel cluster | removal of axial water on Cu | each Cu can expose one axial site; classic Cu-OMS material |
| MOF-505 | Cu2+ | Cu2 paddlewheel cluster | axial solvent removal | CO2, H2, light hydrocarbon adsorption |
| NOTT-100 | Cu2+ | Cu2 paddlewheel cluster | coordinated water/solvent removal | high-density Cu-OMS for gas adsorption |
| NOTT-101 | Cu2+ | Cu2 paddlewheel cluster | axial solvent removal | CH4, CO2 adsorption |
| NOTT-112 | Cu2+ | Cu2 paddlewheel cluster | axial solvent removal | porous structure plus Cu-OMS synergy |
| PCN-14 | Cu2+ | Cu2 paddlewheel cluster | axial solvent removal | high-pressure methane storage studies |
| NU-125 | Cu2+ | Cu2 paddlewheel cluster | axial ligand removal | gas storage and adsorption |
| Cu-TDPAT | Cu2+ | Cu2 paddlewheel cluster | axial solvent removal | CO2/N2 and CO2/CH4 separation |
| MIL-100(Fe) | Fe3+ | Fe3O trinuclear cluster | terminal H2O removal; site count depends on OH-/F- and charge balance | Lewis acid sites for adsorption and catalysis |
| MIL-100(Cr) | Cr3+ | Cr3O trinuclear cluster | coordinated water removal | relatively water-stable; acid catalysis and polar molecule adsorption |
| MIL-100(Al) | Al3+ | Al3O trinuclear cluster | terminal water removal | stronger Lewis acidity; relatively good environmental stability |
| MIL-101(Cr) | Cr3+ | Cr3O trinuclear cluster | terminal coordinated water removal | large pore, high surface area; catalysis, adsorption, post-synthetic modification |
| MIL-101(Fe) | Fe3+ | Fe3O trinuclear cluster | coordinated water removal | adsorption, photocatalysis, oxidation |
| MIL-101(Al) | Al3+ | Al3O trinuclear cluster | terminal water removal | Lewis acid catalysis and polar molecule adsorption |
| M-BTT, such as Cu-BTT, Mn-BTT | Cu2+, Mn2+, etc. | metal-triazolate cluster | coordinated solvent removal | high-density OMS; can coordinate CO, NO, olefins |
| M-BTTri, such as Co-BTTri, Fe-BTTri | Co2+, Fe2+, etc. | metal-triazolate node | water/solvent removal | tunable redox activity for gas binding and catalysis |
| MFU-4l derivatives | Zn, Co, Ni, Fe, etc. | Kuratowski-like cluster | metal substitution and ligand removal | well-defined single-metal OMS for small-molecule activation |
| NU-1000 | Zr4+ | 8-connected Zr6 node | dehydration, dehydroxylation, or terminal ligand removal creates accessible Zr sites | node post-modification and single-atom/cluster loading |
| MOF-808 | Zr4+ | 6-connected Zr6 node | removal of formate or other modulators exposes Zr-OH/H2O sites | strong Lewis acidity; hydrolysis and acid catalysis |
| MIP-177-LT and defective Zr-MOFs | Zr4+ | low-connected Zr cluster | removal of modulators or terminal ligands | high node accessibility; site identity depends strongly on activation state |

## Eight Classic OMS Categories To Remember

1. M-MOF-74 / CPO-27-M
2. HKUST-1
3. MIL-100(Fe/Cr/Al)
4. MIL-101(Cr/Fe/Al)
5. Cu2 paddlewheel materials, such as NOTT-100, MOF-505, PCN-14
6. M-BTT / M-BTTri
7. MOF-808
8. NU-1000

## Commonly Misclassified Materials

| material | classic intrinsic OMS MOF? | reason |
|---|---|---|
| UiO-66 | usually no | ideal Zr6 node is highly connected and saturated; missing-linker defects can create defect-associated Zr Lewis acid sites |
| UiO-66-NH2 | usually no | the amino group is not an OMS; OMS-like behavior still depends on defects and activation state |
| ZIF-8 | no | Zn2+ is normally saturated by four imidazolate nitrogens; no accessible intrinsic OMS in the normal structure |
| ZIF-67 | no | Co2+ is a saturated tetrahedral node; defect sites are not equivalent to regular intrinsic OMS |
| MIL-53 | use caution | adsorption capacity does not imply high-density accessible OMS; depends on metal, terminal ligands, and defects |
| MIL-88 series | case-specific | metal trimers may contain terminal water/OH/F, but exposure after activation and framework stability must be checked |
| defective UiO-66 | can generate sites | defect-induced Zr Lewis acid sites, not regularly arranged intrinsic OMS in the ideal crystal |

## Practical OMS Checks

Do not decide OMS presence only by seeing water near a metal in a CIF. Check:

1. Is the water or solvent directly coordinated to the metal?
2. Can it be removed under activation conditions without framework collapse?
3. Does removal leave an accessible coordination vacancy?
4. Is the site relevant under the actual feed, humidity, and regeneration conditions?
5. Is the site intrinsic and periodic, or defect-induced and sample-dependent?

## Use In Hydrocarbon Screening

OMS can help bind olefins, CO, NO, polar molecules, and sulfur-containing molecules, but may also create strong adsorption and regeneration penalties. For breakthrough-product recovery of a hydrocarbon target, OMS materials should often be treated as impurity-capture layers or functional controls rather than automatically as target-productivity materials.
