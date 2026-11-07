# Manuscript Methods And SI Template

Use this file when the user wants to write a manuscript Methods section, Supporting Information, figure captions, reviewer response, or group-meeting slide text for the MOF separation co-scientist workflow.

## Purpose

Convert the co-scientist workflow into publication-ready writing. The writing must be accurate, balanced, and defensible: the LLM supports structured reasoning and configuration hypothesis generation, while physical simulation, descriptors, isotherms, and breakthrough experiments remain the evidence foundation.

## Core Manuscript Positioning

Recommended wording:

```text
We developed a co-scientist workflow to assist MOF adsorptive separation studies by converting feed composition, adsorbent descriptors, adsorption isotherms, and breakthrough data into functional bed-layer assignments and experimentally testable serial-bed configuration hypotheses.
```

Relationship to simulation and experiments:

```text
The co-scientist does not replace physical simulation or breakthrough experiments. Instead, it uses simulation and experimental data to organize evidence, update functional hypotheses, and prioritize the next experiment under productivity and recovery constraints.
```

Avoid:
- "The LLM autonomously discovered the optimal configuration" unless a closed-loop autonomous platform actually did this.
- "The model replaces RUPTURA/physical simulation."
- "The recommended configuration is globally optimal" without exhaustive optimization or Level 4-5 evidence.

## Methods Section Template

### Co-Scientist Workflow

```text
The co-scientist workflow consisted of six modules: mixture role analysis, functional bed decomposition, function-compatible sorbent screening, experimental calibration, configuration hypothesis generation, and feed/objective perturbation analysis. The workflow first converted the feed composition and target molecule into a target recovery mode and a specification-limiting impurity. It then assigned bed-layer functions before selecting materials, thereby separating the chemical separation problem from the material-selection problem.
```

### Mixture Role Analysis

```text
For each feed condition, the target molecule, impurity list, and component partial pressures were converted into a mixture-role table. The target recovery mode was assigned as breakthrough product, adsorbed product, or desorption product. The dominant impurity class and likely specification-limiting impurity were then identified based on feed burden, expected affinity, and available dynamic breakthrough evidence.
```

### Functional Bed Decomposition

```text
The separation task was decomposed into bed-layer functions before adsorbent assignment. Typical functions included front separation or sequence-shaping, downstream refining of the limiting impurity, guard-layer protection, and capacity support. For each function, the required material behavior and a falsification criterion were recorded.
```

### Sorbent Screening

```text
Candidate MOFs were screened by function rather than ranked globally. For each bed function, descriptors such as pore size distribution, PLD, LCD, pore volume, accessible surface area, open metal sites, functional groups, polarity, hydrophobicity, stability, and synthesis availability were mapped to candidate materials. When isotherm or simulation data were available, uptake and selectivity were evaluated at feed-relevant partial pressures.
```

### Experimental Calibration

```text
Breakthrough and isotherm data were used to calibrate, rather than merely validate, the functional assignments. Dynamic features including target breakthrough, first impurity breakthrough, clean collection window, curve broadening, and dynamic uptake proxies were extracted when available. Each experimental observation was linked to an evidence level and used to update the material function, limiting impurity, and next experiment.
```

### Controls And Uncertainty

```text
Breakthrough comparisons were interpreted together with control and uncertainty records, including blank or system response where available, single-bed controls, activation and packing conditions, bed mass, flow rate, detector normalization, replicate status, and integration-window selection. Single-run observations were treated as configuration hypothesis tests, whereas replicated comparisons were required for claims of reproducible improvement.
```

### Configuration Hypothesis Generation

```text
The LLM was used as a configuration hypothesis generator rather than a numerical optimizer. Given the candidate pool, functional labels, experimental evidence, and constraints on total bed mass, material availability, sequence, ratio, and experiment budget, the workflow proposed a serial-bed material set, bed order, mass ratio, collection window, expected limiting impurity, and failure mode. Productivity, recovery, and purity were reported only with the corresponding calculation basis: measured, curve-integral proxy, time-window proxy, or qualitative estimate.
```

### Iterative Update

```text
After each new experiment, the research state was updated by recording the previous configuration, new evidence, changed function assignment, updated limiting impurity, recommendation change, and the result that would overturn the current hypothesis. Feed or objective changes triggered re-analysis of mixture roles and ratio migration rather than direct reuse of the previous best configuration.
```

### Evaluation Protocol

```text
The co-scientist was evaluated using task-level criteria including role-analysis accuracy, functional decomposition quality, function-specific candidate mapping, experimental calibration, configuration hypothesis quality, metric discipline, and claim discipline. Baselines included descriptor-only heuristics, isotherm-only heuristics, single-material ranking, human-rule decision trees, and ablated versions of the co-scientist workflow.
```

## Supporting Information Tables

### Table S1. Feed Role Table

| component | partial pressure | role | expected separation issue | evidence |
|---|---:|---|---|---|
| target |  |  |  |  |
| impurity 1 |  |  |  |  |

### Table S2. Function-Compatible Candidate Map

| bed function | required behavior | candidate MOFs | descriptor evidence | experimental evidence | risk |
|---|---|---|---|---|---|
| front separation layer |  |  |  |  |  |
| downstream refining layer |  |  |  |  |  |

### Table S3. Evidence-Level Assignment

| claim | supporting data | evidence level | metric basis | safe wording |
|---|---|---:|---|---|
|  |  |  |  |  |

### Table S4. Configuration Hypotheses

| configuration | order | mass ratio | objective | expected limiting impurity | biggest risk | evidence level |
|---|---|---|---|---|---|---:|
|  |  |  |  |  |  |  |

### Table S5. Iterative Decision Log

| round | new evidence | previous configuration | recommendation change | reason changed/not changed | next experiment |
|---:|---|---|---|---|---|
|  |  |  |  |  |  |

### Table S6. Controls And Uncertainty

| experiment | blank/system control | single-bed control | replicate count | uncertainty source | claim allowed |
|---|---|---|---:|---|---|
|  |  |  |  |  |  |

### Table S7. Evaluation Rubric

| task | baseline | co-scientist output | score dimension | outcome |
|---|---|---|---|---|
| role analysis |  |  |  |  |
| configuration hypothesis |  |  |  |  |

## Figure Caption Templates

### Workflow Figure

```text
Figure X. Co-scientist workflow for MOF adsorptive separation. Feed composition and target specification are first converted into mixture roles and target recovery mode. Functional bed layers are then assigned before material selection. Descriptor-guided screening and experimental calibration produce function-compatible candidates, which are used by the LLM to generate serial-bed configuration hypotheses under productivity and recovery constraints. Feed or objective changes trigger renewed role analysis and iterative experimental calibration, while physical simulation and breakthrough experiments remain the evidence foundation.
```

## Reviewer Response Templates

### Concern: The LLM Replaces Physical Simulation

```text
We agree that physical simulation and breakthrough experiments are essential. Our workflow does not replace them. The LLM is used as a structured reasoning layer that organizes simulation and experimental evidence, assigns bed-layer functions, and generates testable configuration hypotheses. We have revised the manuscript to clarify that simulation and experiments remain the evidence foundation.
```

### Concern: The Recommended Configuration Is Not Globally Optimized

```text
We have revised the wording from "optimized configuration" to "configuration hypothesis" where only hypothesis generation or limited experimental comparison is available. Claims of configuration improvement are restricted to cases with ratio, sequence, or replicated evidence under comparable conditions.
```

### Concern: Metrics Are Proxies

```text
We now explicitly label productivity, recovery, and purity values by calculation basis. When only normalized breakthrough curves are available, the reported values are described as curve-integral proxies or time-window proxies rather than absolute measured quantities.
```

## Language Guardrails

Prefer:
- co-scientist workflow
- decision-support framework
- configuration hypothesis
- function-compatible candidates
- experimentally calibrated function
- evidence level
- curve-integral proxy

Avoid unless fully supported:
- autonomous discovery
- global optimum
- universal best MOF
- replacement of physical simulation

## Completion Checklist

Before using text in a manuscript:

- Every configuration claim has an evidence level.
- Every productivity/recovery/purity statement has a metric basis.
- Every performance-improvement claim states control and replicate status.
- The LLM is described as a hypothesis generator or decision-support layer.
- Physical simulation and experiments remain the evidence foundation.
- Baselines and ablations are described when claiming co-scientist value.
- Case-study demonstrations are framed as case-specific evidence, not universal proof.
- Unsupported claims are moved to outlook or future validation.
