# Experimental Controls And Uncertainty

Use this file when planning experiments, interpreting breakthrough data, preparing figures, writing Methods/SI, or defending claims about performance improvement.

## Purpose

Publication-grade co-scientist recommendations must be tied to experimental controls and uncertainty. A strong configuration hypothesis is not enough; the study must show that observed differences are not artifacts of activation, packing, flow, detector response, normalization, or one-off experimental scatter.

## Minimum Control Experiments

### Blank And System Controls

Use these controls when feasible:

- blank tube or empty column response;
- inert packing control when dead volume is significant;
- carrier-gas baseline;
- detector baseline and drift check;
- bypass or no-adsorbent response for retention-time calibration.

Purpose:
- separate true adsorption delay from system dead volume, detector lag, or tubing effects.

### Single-Bed Controls

For every material used in a serial configuration, preserve or request:

- single-bed breakthrough under comparable feed;
- bed mass, flow rate, temperature, pressure;
- activation condition;
- particle size or pellet form;
- curve normalization method.

Purpose:
- prove that a material performs the assigned function before claiming serial-bed synergy.

### Sequence And Ratio Controls

For configuration claims, use:

- baseline best prior ratio;
- reversed sequence when sequence is part of the claim;
- ratio perturbation around the proposed ratio;
- single-function control if the downstream layer is claimed to refine a specific impurity.

Purpose:
- distinguish real sequence/ratio effects from total-bed-mass or capacity effects.

## Replicate Guidance

Minimum reporting:

- at least duplicate runs for the final claimed best configuration when material/time allows;
- repeat one key control if full replication is too costly;
- report activation, packing, and flow reproducibility.

If only one run exists:

- call the result a "single-run observation" or "configuration hypothesis test";
- do not claim statistical superiority;
- state the exact follow-up replicate needed.

## Uncertainty Sources

Track these sources explicitly:

- flow-rate uncertainty;
- bed-mass uncertainty;
- detector calibration and response factor;
- curve digitization uncertainty;
- baseline drift;
- feed composition uncertainty;
- activation-state variation;
- particle-size and packing variation;
- temperature or pressure variation;
- integration-window selection.

## Metric Uncertainty

### Breakthrough Time

Report:

```text
t5/t50/t95 = value +/- replicate or detection uncertainty
```

If uncertainty is not known, label the value as approximate and avoid over-precise comparisons.

### Collection Window

For clean-window metrics:

```text
collection window = first impurity breakthrough - target breakthrough
```

State which threshold was used, such as `t5`, `t10`, detector limit, or user-defined specification.

### Curve-Integral Proxy

For normalized curves:

```text
proxy = integral(C_A/C_A0 dt over selected window) / Delta t
```

Report:
- integration window;
- normalization basis;
- whether impurity curves are available;
- whether flow rate and absolute calibration are available.

Do not present this as true purity, recovery, or molar productivity unless the required calibration and flow data exist.

## Claim Thresholds

Use these boundaries:

- A single successful serial-bed run supports "promising configuration hypothesis".
- A sequence comparison supports "sequence-dependent performance".
- A ratio series supports "ratio-sensitive performance" or "locally improved ratio".
- Replicated final configuration supports "reproducible improvement under tested conditions".
- Regeneration/cycle tests support "process-validation outlook".

Do not claim:

- "statistically significant improvement" without replicate statistics;
- "global optimum" without systematic search or validated optimizer;
- "process-ready" without regeneration/cycling and practical material data.

## Figure And SI Requirements

For breakthrough figures:

- show raw or normalized curves with consistent axes;
- include feed condition, bed mass, flow rate, and temperature in caption or SI;
- label target and limiting impurity;
- mark collection window;
- show replicate or uncertainty when available;
- state whether curves are single-run or replicated.

For comparison tables:

| configuration | run count | bed mass | flow rate | target window | limiting impurity | metric basis | uncertainty |
|---|---:|---:|---:|---|---|---|---|

## Co-Scientist Use

When recommending the next experiment, the co-scientist should specify:

- whether the experiment is a performance test, control, replicate, or uncertainty-reduction test;
- what control is most important if only one additional run is possible;
- which claim the experiment would enable or falsify;
- what uncertainty remains even if the result succeeds.

## Paper-Facing Claim Boundary

Supported claims:
- "Experimental controls and uncertainty sources were identified and linked to the strength of configuration claims."
- "Reported performance metrics were labeled by calculation basis and replicate status."

Claims not supported without additional evidence:
- "The improvement is statistically significant."
- "The configuration is globally optimal."
- "The process is ready for scale-up."

Safe wording:
- Use "single-run observation", "replicated under tested conditions", "sequence-dependent performance", and "locally improved configuration".
- Avoid "significant", "optimal", or "process-ready" unless the corresponding evidence threshold is met.
