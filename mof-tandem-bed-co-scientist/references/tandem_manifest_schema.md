# Tandem Analysis Manifest

The deterministic script accepts UTF-8 JSON. Paths are relative to the manifest unless absolute. Curve files may be CSV, XLSX, or XLSM.

```json
{
  "threshold": 0.05,
  "coordinate_column": "time_min",
  "capacity_normalization": "divide_by_mass",
  "upstream_material": "U",
  "upstream_curve": {
    "path": "U.csv",
    "mass_g": 0.100,
    "response_columns": {"impurity_a": "a_c_c0", "duty_g": "g_c_c0"}
  },
  "upstream_duty_components": ["impurity_a"],
  "downstream_duty_components": ["duty_g"],
  "component_load_rates": {"impurity_a": 0.20, "duty_g": 0.10},
  "downstream_candidates": [
    {
      "material": "D1",
      "curve": {
        "path": "D1.csv",
        "mass_g": 0.030,
        "response_columns": {"duty_g": "g_c_c0"}
      }
    }
  ],
  "integration_mode": "raw",
  "downstream_cutoff_mode": "own_threshold",
  "observed_tandem": [
    {"material": "D1", "upstream_mass_g": 0.100, "downstream_mass_g": 0.030}
  ],
  "feed_transfer": {
    "layers": [
      {
        "name": "downstream:D1",
        "baseline_mass_g": 0.030,
        "duty_multiplier": 1.50,
        "material_factor": {"low": 0.90, "base": 1.00, "high": 1.15},
        "operation_factor": 1.00,
        "uncertainty_factor": {"low": 0.90, "base": 1.00, "high": 1.20},
        "basis": "experimentally anchored transfer"
      }
    ]
  }
}
```

`component_load_rates` must use a common basis. Set `capacity_normalization` to `divide_by_mass` when the curve coordinate is ordinary time; the script then divides integrated loading by `mass_g`. Set it to `coordinate_already_mass_normalized` when the horizontal axis is already time per sorbent mass; it will not divide by mass again. The choice is mandatory scientific metadata even though the script defaults to `divide_by_mass` for backward compatibility.

Masses, required component load rates, and transfer factors must be finite and positive. Duty lists must be nonempty, contain unique components, and not overlap. At least one downstream candidate is required, with a unique material name for each candidate. A component retained by the upstream bed can still belong to the downstream residual-duty set; it should not also be counted in the upstream-duty set.

`integration_mode` may be `raw` or `clamp_0_1`. Use raw for the primary result and clamped only as a sensitivity check.

`downstream_cutoff_mode` may be `own_threshold` or `common_earliest`. The former is the default componentwise-capacity interpretation; the latter matches a common product cutoff.

Response columns must contain normalized `C/C0` values. CSV columns use header names. Excel columns may use header names or one-based numeric indices; optional curve fields are `sheet`, `header_row`, `start_row`, and `coordinate_column`. Missing or nonnumeric rows are rejected rather than silently imputed.

The optional `feed_transfer` block multiplies baseline layer mass by explicit duty, material, operation, and uncertainty factors. Each factor may be one number or a `low/base/high` object. These scenarios are kept separate from the direct breakthrough calculation.
