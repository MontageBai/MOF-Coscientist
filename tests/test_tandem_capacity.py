"""Analytically checkable synthetic curves; no experimental case data."""

import copy
import csv
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skill_export/mof-tandem-bed-co-scientist/scripts/tandem_capacity_analysis.py"
EXAMPLE = ROOT / "examples/tandem_synthetic/manifest.json"
spec = importlib.util.spec_from_file_location("tandem", SCRIPT)
tandem = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tandem)


class TandemCapacityTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self.scratch.cleanup)
        self.folder = Path(self.scratch.name)
        self.manifest = json.loads(EXAMPLE.read_text(encoding="utf-8"))
        for name in ("U.csv", "D.csv"):
            (self.folder / name).write_bytes((EXAMPLE.parent / name).read_bytes())

    def analyze(self, manifest=None):
        path = self.folder / "manifest.json"
        path.write_text(json.dumps(manifest or self.manifest), encoding="utf-8")
        return tandem.analyze(path)

    def test_hand_integrated_capacity_and_controlling_component(self):
        result = self.analyze()
        # Linear B crossing at 1.5 min: area = 1 + 0.5*(1+0.95)*0.5.
        self.assertAlmostEqual(result["upstream_common_cutoff"], 1.5)
        q = result["upstream_dynamic_capacities_per_g_sorbent"]
        self.assertAlmostEqual(q["B"], 2.975)
        self.assertAlmostEqual(q["G1"], 0.675)
        self.assertAlmostEqual(q["G2"], 0.25)
        residual = result["residual_downstream_duty_per_g_upstream_sorbent"]
        self.assertAlmostEqual(residual["G1"], 0.8125)
        self.assertAlmostEqual(residual["G2"], 0.49375)
        candidate = result["downstream_candidates"][0]
        self.assertAlmostEqual(candidate["dynamic_capacities_per_g_sorbent"]["G1"], 2.975)
        self.assertAlmostEqual(candidate["dynamic_capacities_per_g_sorbent"]["G2"], 0.975)
        self.assertEqual(candidate["controlling_component"], "G2")
        self.assertAlmostEqual(candidate["downstream_mass_per_upstream_mass"], 0.49375 / 0.975)

    def test_mass_normalized_coordinate_has_identical_capacities(self):
        baseline = self.analyze()
        for name, mass in (("U.csv", 0.1), ("D.csv", 0.05)):
            path = self.folder / name
            with path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.reader(handle))
            for row in rows[1:]:
                row[0] = str(float(row[0]) / mass)
            with path.open("w", newline="", encoding="utf-8") as handle:
                csv.writer(handle).writerows(rows)
        self.manifest["capacity_normalization"] = "coordinate_already_mass_normalized"
        normalized = self.analyze()
        for component, q in baseline["upstream_dynamic_capacities_per_g_sorbent"].items():
            self.assertAlmostEqual(normalized["upstream_dynamic_capacities_per_g_sorbent"][component], q)
        self.assertAlmostEqual(
            normalized["downstream_candidates"][0]["downstream_mass_per_upstream_mass"],
            baseline["downstream_candidates"][0]["downstream_mass_per_upstream_mass"],
        )

    def test_earliest_common_downstream_cutoff(self):
        self.manifest["downstream_cutoff_mode"] = "common_earliest"
        candidate = self.analyze()["downstream_candidates"][0]
        self.assertAlmostEqual(candidate["dynamic_capacities_per_g_sorbent"]["G1"], 2.0)
        self.assertAlmostEqual(candidate["dynamic_capacities_per_g_sorbent"]["G2"], 0.975)

    def test_raw_overshoot_and_quality_flag(self):
        self.assertAlmostEqual(tandem.integrate_retention([0, 1, 2], [0, 1.2, 1.2], 2, "raw"), 0.2)
        self.assertAlmostEqual(tandem.integrate_retention([0, 1, 2], [0, 1.2, 1.2], 2, "clamp_0_1"), 0.5)
        self.assertIn("overshoot_above_1.05", tandem.quality_flags([0, 1, 2], [0, 1.2, 1.2], 0.05))

    def test_transfer_is_separate_scenario(self):
        result = self.analyze()
        masses = result["feed_transfer_scenarios"][0]["transferred_mass_g"]
        for bound, expected in (("low", 0.09), ("base", 0.1), ("high", 0.11)):
            self.assertAlmostEqual(masses[bound], expected)
        manifest = copy.deepcopy(self.manifest)
        del manifest["feed_transfer"]
        self.assertEqual(result["downstream_candidates"], self.analyze(manifest)["downstream_candidates"])

    def test_rejects_invalid_duties_missing_candidates_and_nonfinite_inputs(self):
        changes = [
            ("upstream_duty_components", ["B", "B"], "duplicates"),
            ("downstream_duty_components", ["B"], "overlap"),
            ("downstream_candidates", [], "at least one"),
            ("component_load_rates", {"B": float("nan"), "G1": 0.1, "G2": 0.05}, "finite"),
        ]
        for field, value, message in changes:
            with self.subTest(field=field):
                manifest = copy.deepcopy(self.manifest)
                manifest[field] = value
                with self.assertRaisesRegex(ValueError, message):
                    self.analyze(manifest)
        manifest = copy.deepcopy(self.manifest)
        manifest["upstream_curve"]["mass_g"] = float("inf")
        with self.assertRaisesRegex(ValueError, "finite"):
            self.analyze(manifest)
        with self.assertRaisesRegex(ValueError, "finite"):
            tandem.factor_triplet(float("nan"), "test")

    def test_missing_crossing_and_decreasing_coordinates_fail(self):
        path = self.folder / "D.csv"
        path.write_text("time_min,g1_c_c0,g2_c_c0\n0,0,0\n1,0,0\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "does not cross"):
            self.analyze()
        path.write_text("time_min,g1_c_c0,g2_c_c0\n1,0,0\n0,0.1,0.1\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "strictly increasing"):
            self.analyze()

    def test_cli_writes_json_from_another_directory(self):
        output = self.folder / "output.json"
        process = subprocess.run(
            [sys.executable, str(SCRIPT), str(EXAMPLE), str(output)],
            cwd=self.folder, capture_output=True, text=True,
        )
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["analysis_type"], "tandem_capacity_matching")

    def test_excel_header_mapping_matches_csv(self):
        from openpyxl import Workbook

        baseline = self.analyze()
        for config in (self.manifest["upstream_curve"], self.manifest["downstream_candidates"][0]["curve"]):
            csv_path = self.folder / config["path"]
            workbook = Workbook()
            with csv_path.open(newline="", encoding="utf-8") as handle:
                rows = list(csv.reader(handle))
            workbook.active.append(rows[0])
            for row in rows[1:]:
                workbook.active.append([float(value) for value in row])
            config["path"] = csv_path.with_suffix(".xlsx").name
            workbook.save(self.folder / config["path"])
            workbook.close()
        excel = self.analyze()
        self.assertEqual(excel["upstream_dynamic_capacities_per_g_sorbent"], baseline["upstream_dynamic_capacities_per_g_sorbent"])
        self.assertAlmostEqual(excel["downstream_candidates"][0]["downstream_mass_per_upstream_mass"], baseline["downstream_candidates"][0]["downstream_mass_per_upstream_mass"])


if __name__ == "__main__":
    unittest.main()
