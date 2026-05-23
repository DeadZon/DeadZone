"""
Tests for the Legend OS3 debloat profile system.

All 12 required cases:
  1.  Legend profile runs only for Legend OS3.
  2.  Does NOT run for Gaming.
  3.  Does NOT run for EPiC.
  4.  Does NOT run for base/common.
  5.  Path traversal is blocked.
  6.  Missing paths are skipped and do not fail.
  7.  Protected telephony apps are not removed.
  8.  Report is generated.
  9.  mi_ext/product/etc move happens before mi_ext delete.
  10. product/data-app filtering happens before moving remainder to product/app.
  11. dry-run changes nothing on disk.
  12. execute mode changes only inside ROM root.

Run:
    python -m pytest factory/patches/legend/os3/tests/test_legend_os3_debloat.py -v
    # or without pytest:
    python -m unittest factory.patches.legend.os3.tests.test_legend_os3_debloat -v
"""
from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from factory.patches.legend.os3.legend_profile import matches_profile, guard
from factory.patches.legend.os3.debloat_executor import (
    LegendOS3DebloatExecutor,
    _path_is_safe,
    _is_traversal,
)

_MANIFEST = Path(__file__).resolve().parents[1] / "debloat_manifest.yml"


# ── helpers ────────────────────────────────────────────────────────────────────

def _make_rom(base: Path, *rel_paths: str) -> None:
    """Create stub files/dirs inside a temp ROM root."""
    for rel in rel_paths:
        p = base / rel
        if rel.endswith("/"):
            p.mkdir(parents=True, exist_ok=True)
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text("stub")


def _executor(rom_root: Path, execute: bool = False, **kwargs) -> LegendOS3DebloatExecutor:
    return LegendOS3DebloatExecutor(
        rom_root=rom_root,
        flavor=kwargs.get("flavor", "legend"),
        os_family=kwargs.get("os_family", "OS3"),
        debloat_profile=kwargs.get("debloat_profile", "legend_os3"),
        execute=execute,
        manifest_path=_MANIFEST,
    )


# ── test cases ─────────────────────────────────────────────────────────────────

class TestProfileGuard(unittest.TestCase):
    """Case 1-4: profile guard fires correctly for all flavor/os combinations."""

    def test_1_legend_os3_matches(self):
        """Case 1: Legend + OS3 + legend_os3 should match."""
        self.assertTrue(matches_profile("legend", "OS3", "legend_os3"))
        self.assertTrue(matches_profile("deadzone_legend", "HyperOS3", "legend_os3"))
        self.assertTrue(matches_profile("legend", "hyperos3", "legend_os3"))

    def test_2_gaming_does_not_match(self):
        """Case 2: Gaming flavor must not match."""
        self.assertFalse(matches_profile("gaming", "OS3", "legend_os3"))
        self.assertFalse(matches_profile("deadzone_gaming", "OS3", "legend_os3"))

    def test_3_epic_does_not_match(self):
        """Case 3: EPiC flavor must not match."""
        self.assertFalse(matches_profile("epic", "OS3", "legend_os3"))
        self.assertFalse(matches_profile("deadzone_epic", "OS3", "legend_os3"))

    def test_4_base_common_does_not_match(self):
        """Case 4: Base/common profiles must not match."""
        self.assertFalse(matches_profile("base", "OS3", "legend_os3"))
        self.assertFalse(matches_profile("common", "OS3", "legend_os3"))
        self.assertFalse(matches_profile("deadzone", "OS3", "legend_os3"))
        # Wrong debloat_profile key
        self.assertFalse(matches_profile("legend", "OS3", "common"))
        self.assertFalse(matches_profile("legend", "OS3", "base"))
        # Wrong OS family
        self.assertFalse(matches_profile("legend", "OS4", "legend_os3"))
        self.assertFalse(matches_profile("legend", "MIUI", "legend_os3"))

    def test_guard_raises_for_wrong_profile(self):
        """guard() must raise ValueError for non-matching config."""
        with self.assertRaises(ValueError) as ctx:
            guard("gaming", "OS3", "legend_os3")
        self.assertIn("Profile skipped", str(ctx.exception))

    def test_guard_passes_for_legend_os3(self):
        """guard() must NOT raise for a valid Legend OS3 config."""
        guard("legend", "OS3", "legend_os3")  # should not raise


class TestPathSafety(unittest.TestCase):
    """Case 5: path traversal is blocked at the _path_is_safe / executor level."""

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self.rom_root = Path(self._tmp) / "rom"
        self.rom_root.mkdir()

    def tearDown(self):
        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_5_traversal_dotdot_blocked(self):
        """Case 5a: ../outside_rom must be blocked."""
        self.assertTrue(_is_traversal(self.rom_root, "../outside"))
        self.assertFalse(_path_is_safe(self.rom_root, "../outside"))

    def test_5_traversal_deep_dotdot_blocked(self):
        """Case 5b: product/../../outside must be blocked."""
        self.assertFalse(_path_is_safe(self.rom_root, "product/../../outside"))

    def test_5_absolute_path_blocked(self):
        """Case 5c: absolute paths outside ROM root must be blocked."""
        self.assertFalse(_path_is_safe(self.rom_root, "/etc/passwd"))

    def test_5_valid_relative_allowed(self):
        """Case 5d: normal relative paths inside ROM root must be allowed."""
        self.assertTrue(_path_is_safe(self.rom_root, "product/app/SomeApp"))
        self.assertTrue(_path_is_safe(self.rom_root, "system/priv-app/X"))

    def test_5_executor_blocks_traversal_in_run(self):
        """Case 5e: executor skips and warns when manifest would traverse."""
        import yaml
        # Build a minimal manifest with a traversal attempt
        bad_manifest = {
            "profile": {"flavor": "legend", "os_family": ["OS3"], "debloat_profile": "legend_os3"},
            "move_paths": [{"src": "../escape", "dst": "product/app/X"}],
            "rename_paths": [],
            "remove_paths": [],
            "remove_packages": {},
            "move_data_app_to_app": {"enabled": False},
            "clean_patterns": {},
            "overlay_patches": [],
            "protected_paths": [],
        }
        manifest_path = self.rom_root.parent / "bad_manifest.yml"
        manifest_path.write_text(yaml.dump(bad_manifest), encoding="utf-8")
        ex = LegendOS3DebloatExecutor(
            rom_root=self.rom_root,
            execute=False,
            manifest_path=manifest_path,
        )
        result = ex.run()
        # Should complete (not crash) but log a warning
        blocked = any("BLOCKED" in w for w in result.get("warnings", []))
        self.assertTrue(blocked, "Expected a BLOCKED warning for traversal path")


class TestMissingPathsSkipped(unittest.TestCase):
    """Case 6: missing files/folders are skipped, never fatal."""

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self.rom_root = Path(self._tmp) / "rom"
        self.rom_root.mkdir()

    def tearDown(self):
        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_6_missing_paths_skip_not_fail(self):
        """Case 6: running against an empty ROM root must not crash."""
        ex = _executor(self.rom_root, execute=False)
        result = ex.run()
        # Must not be FAILED just because paths are missing
        self.assertNotEqual(result.get("final_status"), "FAILED")

    def test_6_missing_paths_in_execute_mode_skip_not_fail(self):
        """Case 6b: execute mode on empty ROM root also skips gracefully."""
        ex = _executor(self.rom_root, execute=True)
        result = ex.run()
        self.assertNotEqual(result.get("final_status"), "FAILED")


class TestProtectedTelephony(unittest.TestCase):
    """Case 7: protected telephony apps are never removed."""

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self.rom_root = Path(self._tmp) / "rom"
        self.rom_root.mkdir()
        # Create some telephony-critical stubs
        _make_rom(
            self.rom_root,
            "system/priv-app/TeleService/TeleService.apk",
            "system/priv-app/Telecom/Telecom.apk",
            "system/priv-app/TelephonyProvider/TelephonyProvider.apk",
            "system/priv-app/MtkTeleService/MtkTeleService.apk",
            "system/priv-app/MtkTelecom/MtkTelecom.apk",
            "system_ext/priv-app/GbaService/GbaService.apk",
            "system_ext/priv-app/CapCtrl/CapCtrl.apk",
        )

    def tearDown(self):
        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_7_telephony_apps_not_removed_in_execute(self):
        """Case 7: execute mode must not touch protected telephony folders."""
        ex = _executor(self.rom_root, execute=True)
        ex.run()
        # These must still exist
        self.assertTrue((self.rom_root / "system/priv-app/TeleService").exists())
        self.assertTrue((self.rom_root / "system/priv-app/Telecom").exists())
        self.assertTrue((self.rom_root / "system/priv-app/TelephonyProvider").exists())
        self.assertTrue((self.rom_root / "system/priv-app/MtkTeleService").exists())
        self.assertTrue((self.rom_root / "system_ext/priv-app/GbaService").exists())
        self.assertTrue((self.rom_root / "system_ext/priv-app/CapCtrl").exists())


class TestReportGenerated(unittest.TestCase):
    """Case 8: report is generated at output/reports/deadzone_patch_report.txt."""

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self.rom_root = Path(self._tmp) / "rom"
        self.rom_root.mkdir()

    def tearDown(self):
        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_8_report_file_created(self):
        """Case 8: dry-run must produce the report file."""
        from factory.patches.legend.os3 import debloat_executor as mod
        orig = mod._REPORTS_DIR
        reports_dir = Path(self._tmp) / "reports"
        mod._REPORTS_DIR = reports_dir
        try:
            ex = _executor(self.rom_root, execute=False)
            ex.run()
            report_path = reports_dir / "deadzone_patch_report.txt"
            self.assertTrue(report_path.exists(), "Report file not created")
            content = report_path.read_text(encoding="utf-8")
            self.assertIn("[LEGEND OS3 PATCH PROFILE]", content)
            self.assertIn("[REMOVED]", content)
            self.assertIn("[MOVED]", content)
            self.assertIn("[WARNINGS]", content)
        finally:
            mod._REPORTS_DIR = orig


class TestMiExtMoveBeforeDelete(unittest.TestCase):
    """Case 9: mi_ext/product/etc/permissions is moved before mi_ext is cleaned."""

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self.rom_root = Path(self._tmp) / "rom"
        self.rom_root.mkdir()
        _make_rom(
            self.rom_root,
            "mi_ext/product/etc/permissions/vendor_miui.xml",
            "mi_ext/product/bin/some_binary",
        )

    def tearDown(self):
        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_9_permissions_moved_before_mi_ext_bin_deleted(self):
        """Case 9: vendor_miui.xml ends up in product/etc/permissions; mi_ext/product/bin is gone."""
        ex = _executor(self.rom_root, execute=True)
        ex.run()
        # permissions file must have moved
        dst = self.rom_root / "product/etc/permissions/vendor_miui.xml"
        self.assertTrue(dst.exists(), "Permissions file was not moved to product/etc/permissions")
        # mi_ext/product/bin must be removed
        self.assertFalse(
            (self.rom_root / "mi_ext/product/bin").exists(),
            "mi_ext/product/bin should have been removed"
        )


class TestDataAppFilterThenMove(unittest.TestCase):
    """Case 10: product/data-app is filtered BEFORE remainder is moved to product/app."""

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self.rom_root = Path(self._tmp) / "rom"
        self.rom_root.mkdir()
        _make_rom(
            self.rom_root,
            # CN bloat to be removed
            "product/data-app/BaiduIME/BaiduIME.apk",
            "product/data-app/SmartHome/SmartHome.apk",
            # Neutral app to be moved to product/app
            "product/data-app/SomeNeutralApp/SomeNeutralApp.apk",
        )
        (self.rom_root / "product/app").mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_10_cn_packages_removed_neutral_moved(self):
        """Case 10: BaiduIME and SmartHome removed; SomeNeutralApp moved to product/app."""
        ex = _executor(self.rom_root, execute=True)
        ex.run()
        # CN bloat must be gone
        self.assertFalse(
            (self.rom_root / "product/data-app/BaiduIME").exists(),
            "BaiduIME should have been filtered from data-app"
        )
        self.assertFalse(
            (self.rom_root / "product/data-app/SmartHome").exists(),
            "SmartHome should have been filtered from data-app"
        )
        # Neutral app must be in product/app
        self.assertTrue(
            (self.rom_root / "product/app/SomeNeutralApp").exists(),
            "SomeNeutralApp should have been moved to product/app"
        )


class TestDryRunChangesNothing(unittest.TestCase):
    """Case 11: dry-run must not change anything on disk."""

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self.rom_root = Path(self._tmp) / "rom"
        self.rom_root.mkdir()
        _make_rom(
            self.rom_root,
            "product/app/MIUICalculator/MIUICalculator.apk",
            "product/data-app/BaiduIME/BaiduIME.apk",
            "mi_ext/product/etc/permissions/vendor_miui.xml",
            "mi_ext/product/bin/binary",
        )

    def tearDown(self):
        shutil.rmtree(self._tmp, ignore_errors=True)

    def _snapshot(self) -> set[str]:
        return {
            str(p.relative_to(self.rom_root))
            for p in self.rom_root.rglob("*")
        }

    def test_11_dry_run_no_disk_changes(self):
        """Case 11: all paths must be identical before and after a dry-run."""
        before = self._snapshot()
        ex = _executor(self.rom_root, execute=False)
        result = ex.run()
        after = self._snapshot()
        self.assertEqual(before, after, "Dry-run modified files on disk")
        self.assertIn(result.get("final_status"), {"DRY_RUN", "SKIPPED"})


class TestExecuteModeStaysInsideRoot(unittest.TestCase):
    """Case 12: execute mode changes only inside ROM root."""

    def setUp(self):
        self._tmp = tempfile.mkdtemp()
        self.rom_root = Path(self._tmp) / "rom"
        self.rom_root.mkdir()
        # Create a file outside the ROM root
        self.outside_file = Path(self._tmp) / "outside.txt"
        self.outside_file.write_text("untouched")
        _make_rom(
            self.rom_root,
            "product/app/MIUICalculator/MIUICalculator.apk",
        )

    def tearDown(self):
        shutil.rmtree(self._tmp, ignore_errors=True)

    def test_12_execute_does_not_touch_outside_root(self):
        """Case 12: file outside ROM root must survive execute mode."""
        ex = _executor(self.rom_root, execute=True)
        ex.run()
        self.assertTrue(
            self.outside_file.exists(),
            "execute mode must not touch files outside the ROM root"
        )
        self.assertEqual(self.outside_file.read_text(), "untouched")


if __name__ == "__main__":
    unittest.main()
