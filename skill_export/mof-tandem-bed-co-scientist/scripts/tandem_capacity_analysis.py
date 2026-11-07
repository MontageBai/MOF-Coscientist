#!/usr/bin/env python3
"""General tandem-bed capacity matching from normalized breakthrough curves."""

from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path
from typing import Any


def fail(message: str) -> None:
    raise ValueError(message)


def read_curve(manifest_dir: Path, config: dict[str, Any], coordinate: str | int) -> dict[str, Any]:
    path = Path(config["path"])
    if not path.is_absolute():
        path = manifest_dir / path
    mass = float(config["mass_g"])
    if not math.isfinite(mass) or mass <= 0:
        fail(f"mass_g must be finite and positive for {path}")
    columns = config.get("response_columns", {})
    if not columns:
        fail(f"response_columns is empty for {path}")

    x: list[float] = []
    responses: dict[str, list[float]] = {component: [] for component in columns}

    def append_row(row_number: int, xv_raw: Any, raw_values: dict[str, Any]) -> None:
        try:
            xv = float(xv_raw)
            values = {component: float(value) for component, value in raw_values.items()}
        except (TypeError, ValueError) as exc:
            fail(f"nonnumeric value in {path} row {row_number}: {exc}")
        if not math.isfinite(xv) or any(not math.isfinite(v) for v in values.values()):
            fail(f"nonfinite value in {path} row {row_number}")
        x.append(xv)
        for component, value in values.items():
            responses[component].append(value)

    suffix = path.suffix.lower()
    if suffix == ".csv":
        if not isinstance(coordinate, str) or any(not isinstance(v, str) for v in columns.values()):
            fail("CSV coordinate_column and response_columns must use header names")
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            required = {coordinate, *columns.values()}
            missing = required.difference(reader.fieldnames or [])
            if missing:
                fail(f"missing columns in {path}: {sorted(missing)}")
            for row_number, row in enumerate(reader, start=2):
                append_row(
                    row_number,
                    row[coordinate],
                    {component: row[column] for component, column in columns.items()},
                )
    elif suffix in {".xlsx", ".xlsm"}:
        try:
            from openpyxl import load_workbook
        except ImportError as exc:
            fail(f"openpyxl is required to read {path}: {exc}")
        workbook = load_workbook(path, read_only=True, data_only=True)
        worksheet = workbook[config.get("sheet", workbook.sheetnames[0])]
        header_row = int(config.get("header_row", 1))
        header_values = next(
            worksheet.iter_rows(min_row=header_row, max_row=header_row, values_only=True)
        )
        header_map = {str(value): index + 1 for index, value in enumerate(header_values) if value is not None}

        def resolve_column(value: str | int) -> int:
            if isinstance(value, int):
                if value < 1:
                    fail("Excel numeric columns are one-based and must be positive")
                return value
            if value not in header_map:
                fail(f"missing Excel column header in {path}: {value}")
            return header_map[value]

        x_column = resolve_column(config.get("coordinate_column", coordinate))
        response_columns = {
            component: resolve_column(column) for component, column in columns.items()
        }
        start_row = int(config.get("start_row", header_row + 1))
        for row_number, row in enumerate(
            worksheet.iter_rows(min_row=start_row, values_only=True), start=start_row
        ):
            max_index = max([x_column, *response_columns.values()])
            if len(row) < max_index:
                fail(f"row {row_number} in {path} is shorter than required columns")
            x_raw = row[x_column - 1]
            response_raw = {
                component: row[column - 1]
                for component, column in response_columns.items()
            }
            if x_raw is None and all(value is None for value in response_raw.values()):
                continue
            append_row(
                row_number,
                x_raw,
                response_raw,
            )
        workbook.close()
    else:
        fail(f"unsupported curve file type for {path}; use CSV, XLSX, or XLSM")

    if len(x) < 2:
        fail(f"at least two rows are required in {path}")
    if any(b <= a for a, b in zip(x, x[1:])):
        fail(f"coordinate must be strictly increasing in {path}")
    return {"path": str(path), "mass_g": mass, "x": x, "responses": responses}


def first_crossing(x: list[float], y: list[float], threshold: float) -> float | None:
    if y[0] >= threshold:
        return x[0]
    for xa, xb, ya, yb in zip(x, x[1:], y, y[1:]):
        if ya < threshold <= yb:
            if yb == ya:
                return xb
            return xa + (threshold - ya) * (xb - xa) / (yb - ya)
    return None


def interpolate(xa: float, xb: float, ya: float, yb: float, xq: float) -> float:
    if xb == xa:
        return ya
    return ya + (yb - ya) * (xq - xa) / (xb - xa)


def integrate_retention(
    x: list[float], y: list[float], cutoff: float, mode: str
) -> float:
    if cutoff < x[0] or cutoff > x[-1]:
        fail(f"cutoff {cutoff} lies outside curve range {x[0]} to {x[-1]}")

    def transform(value: float) -> float:
        if mode == "raw":
            return value
        if mode == "clamp_0_1":
            return min(1.0, max(0.0, value))
        fail(f"unsupported integration_mode: {mode}")

    area = 0.0
    for xa, xb, ya_raw, yb_raw in zip(x, x[1:], y, y[1:]):
        if xa >= cutoff:
            break
        end = min(xb, cutoff)
        ya = transform(ya_raw)
        y_end_raw = interpolate(xa, xb, ya_raw, yb_raw, end)
        y_end = transform(y_end_raw)
        area += 0.5 * ((1.0 - ya) + (1.0 - y_end)) * (end - xa)
        if xb >= cutoff:
            break
    return area


def quality_flags(x: list[float], y: list[float], threshold: float) -> list[str]:
    flags: list[str] = []
    if x[0] > 1e-12:
        flags.append("curve_does_not_start_at_zero")
    if y[0] >= threshold:
        flags.append("initial_response_at_or_above_threshold")
    if min(y) < -0.05:
        flags.append("negative_response_below_-0.05")
    if max(y) > 1.05:
        flags.append("overshoot_above_1.05")
    if any(b < a - 0.05 for a, b in zip(y, y[1:])):
        flags.append("nonmonotonic_drop_above_0.05")
    if first_crossing(x, y, threshold) is None:
        flags.append("threshold_not_crossed")
    return flags


def require_components(curve: dict[str, Any], components: list[str], label: str) -> None:
    missing = [component for component in components if component not in curve["responses"]]
    if missing:
        fail(f"{label} curve lacks components: {missing}")


def capacity_from_area(
    load_rate: float, area: float, curve: dict[str, Any], normalization: str
) -> float:
    if normalization == "divide_by_mass":
        return load_rate * area / curve["mass_g"]
    if normalization == "coordinate_already_mass_normalized":
        return load_rate * area
    fail(
        "capacity_normalization must be divide_by_mass or "
        "coordinate_already_mass_normalized"
    )


def factor_triplet(value: Any, label: str) -> dict[str, float]:
    if isinstance(value, (int, float)):
        v = float(value)
        if not math.isfinite(v) or v <= 0:
            fail(f"{label} factor must be finite and positive")
        return {"low": v, "base": v, "high": v}
    if not isinstance(value, dict):
        fail(f"{label} must be a number or low/base/high object")
    result = {key: float(value[key]) for key in ("low", "base", "high")}
    if any(not math.isfinite(v) or v <= 0 for v in result.values()):
        fail(f"{label} factors must be finite and positive")
    if not (result["low"] <= result["base"] <= result["high"]):
        fail(f"{label} factors must satisfy low <= base <= high")
    return result


def analyze_transfer(config: dict[str, Any]) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for layer in config.get("layers", []):
        baseline = float(layer["baseline_mass_g"])
        if not math.isfinite(baseline) or baseline <= 0:
            fail("baseline_mass_g must be finite and positive")
        factors = {
            "duty": factor_triplet(layer.get("duty_multiplier", 1.0), "duty_multiplier"),
            "material": factor_triplet(layer.get("material_factor", 1.0), "material_factor"),
            "operation": factor_triplet(layer.get("operation_factor", 1.0), "operation_factor"),
            "uncertainty": factor_triplet(layer.get("uncertainty_factor", 1.0), "uncertainty_factor"),
        }
        masses = {
            bound: baseline * math.prod(factor[bound] for factor in factors.values())
            for bound in ("low", "base", "high")
        }
        results.append(
            {
                "layer": layer["name"],
                "baseline_mass_g": baseline,
                "factors": factors,
                "transferred_mass_g": masses,
                "basis": layer.get("basis", "not_provided"),
            }
        )
    return results


def analyze(manifest_path: Path) -> dict[str, Any]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    base = manifest_path.parent
    threshold = float(manifest.get("threshold", 0.05))
    if not 0 < threshold < 1:
        fail("threshold must lie between 0 and 1")
    coordinate = manifest.get("coordinate_column", "time")
    mode = manifest.get("integration_mode", "raw")
    normalization = manifest.get("capacity_normalization", "divide_by_mass")
    if normalization not in {"divide_by_mass", "coordinate_already_mass_normalized"}:
        fail(
            "capacity_normalization must be divide_by_mass or "
            "coordinate_already_mass_normalized"
        )
    upstream_duty = list(manifest["upstream_duty_components"])
    downstream_duty = list(manifest["downstream_duty_components"])
    if not upstream_duty or not downstream_duty:
        fail("upstream and downstream duty component lists must be nonempty")
    if len(set(upstream_duty)) != len(upstream_duty) or len(set(downstream_duty)) != len(downstream_duty):
        fail("duty component lists must not contain duplicates")
    if set(upstream_duty).intersection(downstream_duty):
        fail("upstream and downstream duty component lists must not overlap")
    rates = {key: float(value) for key, value in manifest["component_load_rates"].items()}
    required_rates = set(upstream_duty + downstream_duty)
    missing_rates = required_rates.difference(rates)
    if missing_rates:
        fail(f"missing component_load_rates: {sorted(missing_rates)}")
    if any(not math.isfinite(rates[name]) or rates[name] <= 0 for name in required_rates):
        fail("all required component load rates must be finite and positive")
    downstream_candidates = manifest.get("downstream_candidates", [])
    if not downstream_candidates:
        fail("at least one downstream candidate is required")
    material_names = [candidate["material"] for candidate in downstream_candidates]
    if len(set(material_names)) != len(material_names):
        fail("downstream candidate material names must be unique")

    upstream = read_curve(base, manifest["upstream_curve"], coordinate)
    require_components(upstream, upstream_duty + downstream_duty, "upstream")
    upstream_crossings: dict[str, float] = {}
    upstream_flags: dict[str, list[str]] = {}
    for component in upstream_duty + downstream_duty:
        y = upstream["responses"][component]
        crossing = first_crossing(upstream["x"], y, threshold)
        upstream_flags[component] = quality_flags(upstream["x"], y, threshold)
        if component in upstream_duty and crossing is None:
            fail(f"upstream duty component {component} does not cross threshold")
        if crossing is not None:
            upstream_crossings[component] = crossing

    cutoff = min(upstream_crossings[name] for name in upstream_duty)
    q_upstream: dict[str, float] = {}
    for component in upstream_duty + downstream_duty:
        area = integrate_retention(
            upstream["x"], upstream["responses"][component], cutoff, mode
        )
        q_upstream[component] = capacity_from_area(
            rates[component], area, upstream, normalization
        )

    q_upstream_group = sum(q_upstream[name] for name in upstream_duty)
    upstream_load_rate = sum(rates[name] for name in upstream_duty)
    tau_per_upstream_mass = q_upstream_group / upstream_load_rate
    residual = {
        component: max(
            0.0,
            rates[component] * tau_per_upstream_mass - q_upstream[component],
        )
        for component in downstream_duty
    }

    candidates: list[dict[str, Any]] = []
    downstream_mode = manifest.get("downstream_cutoff_mode", "own_threshold")
    if downstream_mode not in {"own_threshold", "common_earliest"}:
        fail("downstream_cutoff_mode must be own_threshold or common_earliest")
    for candidate in downstream_candidates:
        curve = read_curve(base, candidate["curve"], coordinate)
        require_components(curve, downstream_duty, f"downstream {candidate['material']}")
        crossings: dict[str, float] = {}
        flags: dict[str, list[str]] = {}
        for component in downstream_duty:
            y = curve["responses"][component]
            flags[component] = quality_flags(curve["x"], y, threshold)
            crossing = first_crossing(curve["x"], y, threshold)
            if crossing is None:
                fail(
                    f"downstream component {component} for {candidate['material']} "
                    "does not cross threshold"
                )
            crossings[component] = crossing
        common_downstream_cutoff = min(crossings.values())
        capacities: dict[str, float] = {}
        requirements: dict[str, float] = {}
        for component in downstream_duty:
            component_cutoff = (
                crossings[component]
                if downstream_mode == "own_threshold"
                else common_downstream_cutoff
            )
            area = integrate_retention(
                curve["x"], curve["responses"][component], component_cutoff, mode
            )
            capacity = capacity_from_area(
                rates[component], area, curve, normalization
            )
            capacities[component] = capacity
            if capacity <= 0:
                fail(f"nonpositive downstream capacity for {candidate['material']} {component}")
            requirements[component] = residual[component] / capacity
        controlling = max(requirements, key=requirements.get)
        md_per_mu = requirements[controlling]
        ratio = None if md_per_mu == 0 else 1.0 / md_per_mu
        candidates.append(
            {
                "material": candidate["material"],
                "curve_path": curve["path"],
                "threshold_crossings": crossings,
                "dynamic_capacities_per_g_sorbent": capacities,
                "downstream_mass_per_upstream_mass_by_component": requirements,
                "controlling_component": controlling,
                "downstream_mass_per_upstream_mass": md_per_mu,
                "upstream_mass_per_downstream_mass": ratio,
                "quality_flags": flags,
            }
        )

    observations: list[dict[str, Any]] = []
    by_material = {item["material"]: item for item in candidates}
    for observed in manifest.get("observed_tandem", []):
        material = observed["material"]
        if material not in by_material:
            fail(f"observed_tandem material not found among candidates: {material}")
        mu = float(observed["upstream_mass_g"])
        md = float(observed["downstream_mass_g"])
        if not math.isfinite(mu) or not math.isfinite(md) or mu <= 0 or md <= 0:
            fail("observed tandem masses must be finite and positive")
        predicted_md = mu * by_material[material]["downstream_mass_per_upstream_mass"]
        observations.append(
            {
                "material": material,
                "observed_upstream_mass_per_downstream_mass": mu / md,
                "predicted_downstream_mass_g_at_observed_upstream_mass": predicted_md,
                "observed_downstream_mass_g": md,
                "observed_to_predicted_downstream_mass_factor": (
                    None if predicted_md == 0 else md / predicted_md
                ),
                "interpretation": "calibration discrepancy, not automatic proof of optimality",
            }
        )

    result: dict[str, Any] = {
        "analysis_type": "tandem_capacity_matching",
        "claim_boundary": "capacity-matching baseline; not a global optimum",
        "threshold": threshold,
        "integration_mode": mode,
        "capacity_normalization": normalization,
        "upstream_material": manifest.get("upstream_material", "U"),
        "upstream_curve_path": upstream["path"],
        "upstream_common_cutoff": cutoff,
        "upstream_threshold_crossings": upstream_crossings,
        "upstream_dynamic_capacities_per_g_sorbent": q_upstream,
        "upstream_group_capacity_per_g_sorbent": q_upstream_group,
        "tau_per_g_upstream_sorbent": tau_per_upstream_mass,
        "residual_downstream_duty_per_g_upstream_sorbent": residual,
        "upstream_quality_flags": upstream_flags,
        "downstream_cutoff_mode": downstream_mode,
        "downstream_candidates": candidates,
        "observed_tandem_calibration": observations,
    }
    if "feed_transfer" in manifest:
        result["feed_transfer_scenarios"] = analyze_transfer(manifest["feed_transfer"])
    return result


def main(argv: list[str]) -> int:
    if len(argv) not in {2, 3}:
        print(
            "usage: tandem_capacity_analysis.py MANIFEST.json [OUTPUT.json]",
            file=sys.stderr,
        )
        return 2
    manifest_path = Path(argv[1]).resolve()
    result = analyze(manifest_path)
    payload = json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False)
    if len(argv) == 3:
        Path(argv[2]).write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
