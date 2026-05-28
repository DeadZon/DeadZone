"""Tests for factory.super.payload_super_metadata and the payload OTA super rebuild path.

Covers the requirements from the Smart Base Engine task:
  - payload OTA with dynamic partitions but no super.img recovers metadata
  - zircon-like MTK payload dynamic images choose rebuild_with_lpmake
  - missing payload manifest uses device registry super profile
  - VAB _b 0-size placeholders accepted and not treated as missing
  - mi_ext_a real image + mi_ext_b zero accepted
  - lpmake command includes all dynamic partitions when rebuild_super is called
  - no hardcoded zircon-only logic — codename is generic
  - reports show metadata_source and lpmake command
  - if no metadata and no profile, failure message lists attempted sources
  - universal_super_engine passes payload_super_metadata to rebuild_super
  - super_rebuilder uses super_profile for group name and super size
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from factory.super.payload_super_metadata import (
    recover_super_metadata_from_payload,
    _read_registry_super_profile,
    _DYNAMIC_BASES,
    _DEFAULT_SUPER_SIZE,
    _DEFAULT_GROUP_NAME,
)
from factory.super.universal_super_engine import (
    execute_super_strategy,
    STRATEGY_REBUILD_LPMAKE,
    STRATEGY_REBUILD_MODIFIED,
    STRATEGY_PRESERVE_ORIGINAL,
)


# ── Helpers ───────────────────────────────────────────────────────────────────

def _write(path: Path, content: bytes = b"fake_img_data_1234") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


_DYNAMIC_BASES_LIST = [
    "system", "system_ext", "product", "vendor",
    "odm", "mi_ext", "vendor_dlkm", "odm_dlkm", "system_dlkm",
]


def _fake_manifest_sizes(bases: list[str], size: int = 200_000_000) -> dict[str, int]:
    return {b: size for b in bases}


# ═══════════════════════════════════════════════════════════════════
# 1. recover_super_metadata_from_payload — no payload.bin
# ═══════════════════════════════════════════════════════════════════

class TestRecoverWithoutPayloadBin:
    """When payload.bin is absent we fall back to registry then defaults."""

    def test_returns_defaults_when_no_bin_no_registry(self, tmp_path):
        src = tmp_path / "source_images"
        src.mkdir()
        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="genericdevice",
            registry_path=None,
        )
        assert isinstance(result, dict)
        assert "metadata_source" in result
        assert result["super_size"] > 0
        assert result["group_name"]
        assert isinstance(result["partition_sizes"], dict)
        assert isinstance(result["warnings"], list)
        assert isinstance(result["errors"], list)

    def test_uses_image_file_sizes_as_fallback_when_no_manifest(self, tmp_path):
        src = tmp_path / "source_images"
        for part in ["system", "vendor", "product"]:
            _write(src / f"{part}.img", b"x" * 1_000_000)
        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="anydevice",
        )
        # Should have picked up sizes from image files
        assert result["partition_sizes"].get("system") == 1_000_000
        assert result["partition_sizes"].get("vendor") == 1_000_000
        assert result["partition_sizes"].get("product") == 1_000_000

    def test_metadata_source_is_calculated_fallback_without_registry(self, tmp_path):
        src = tmp_path / "source_images"
        _write(src / "system.img")
        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="testdevice",
        )
        assert result["metadata_source"] == "calculated_fallback"

    def test_no_partition_images_produces_error(self, tmp_path):
        src = tmp_path / "source_images"
        src.mkdir()
        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="anydevice",
        )
        assert result["errors"]
        assert any("attempted" in e.lower() or "no partition" in e.lower() or "metadata" in e.lower()
                   for e in result["errors"])

    def test_attempted_sources_listed_in_error(self, tmp_path):
        src = tmp_path / "source_images"
        src.mkdir()
        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="anydevice",
        )
        assert result["attempted_sources"]


# ═══════════════════════════════════════════════════════════════════
# 2. recover_super_metadata_from_payload — with mocked manifest
# ═══════════════════════════════════════════════════════════════════

class TestRecoverWithManifest:
    """Simulate payload.bin being present with various manifest scenarios."""

    def _mock_sizes(self, parts=None, group="qti_dynamic_partitions"):
        parts = parts or _DYNAMIC_BASES_LIST
        mock_fn = MagicMock(return_value={p: 200_000_000 for p in parts})
        mock_group = MagicMock(return_value=(group, []))
        return mock_fn, mock_group

    def test_partition_sizes_taken_from_manifest(self, tmp_path):
        src = tmp_path / "source_images"
        payload_bin = tmp_path / "payload.bin"
        payload_bin.write_bytes(b"fake")

        with patch(
            "factory.super.payload_super_metadata._read_manifest_partition_sizes",
            return_value={"system": 500_000_000, "vendor": 300_000_000},
        ), patch(
            "factory.super.payload_super_metadata._read_manifest_group_name",
            return_value=("qti_dynamic_partitions", []),
        ):
            result = recover_super_metadata_from_payload(
                payload_manifest_path=payload_bin,
                source_images_dir=src,
                selected_codename="testdevice",
            )

        assert result["partition_sizes"]["system"] == 500_000_000
        assert result["partition_sizes"]["vendor"] == 300_000_000

    def test_group_name_taken_from_manifest(self, tmp_path):
        src = tmp_path / "source_images"
        payload_bin = tmp_path / "payload.bin"
        payload_bin.write_bytes(b"fake")

        with patch(
            "factory.super.payload_super_metadata._read_manifest_partition_sizes",
            return_value={"system": 100_000_000},
        ), patch(
            "factory.super.payload_super_metadata._read_manifest_group_name",
            return_value=("main", []),
        ):
            result = recover_super_metadata_from_payload(
                payload_manifest_path=payload_bin,
                source_images_dir=src,
                selected_codename="testdevice",
            )

        assert result["group_name"] == "main"

    def test_metadata_source_payload_manifest_when_sizes_and_group_available(self, tmp_path):
        payload_bin = tmp_path / "payload.bin"
        payload_bin.write_bytes(b"fake")
        src = tmp_path / "source_images"

        with patch(
            "factory.super.payload_super_metadata._read_manifest_partition_sizes",
            return_value={"system": 100_000_000, "vendor": 50_000_000},
        ), patch(
            "factory.super.payload_super_metadata._read_manifest_group_name",
            return_value=("qti_dynamic_partitions", []),
        ):
            result = recover_super_metadata_from_payload(
                payload_manifest_path=payload_bin,
                source_images_dir=src,
                selected_codename="testdevice",
            )

        assert result["metadata_source"] == "payload_manifest"

    def test_vab_layout_creates_b_placeholders(self, tmp_path):
        payload_bin = tmp_path / "payload.bin"
        payload_bin.write_bytes(b"fake")
        src = tmp_path / "source_images"

        with patch(
            "factory.super.payload_super_metadata._read_manifest_partition_sizes",
            return_value={"system": 100_000_000, "mi_ext": 50_000_000},
        ), patch(
            "factory.super.payload_super_metadata._read_manifest_group_name",
            return_value=("qti_dynamic_partitions", []),
        ):
            result = recover_super_metadata_from_payload(
                payload_manifest_path=payload_bin,
                source_images_dir=src,
                selected_codename="testdevice",
            )

        # VAB: _a partitions should be real, _b should be zero-size
        assert "system_a" in result["partitions"]
        assert "system_b" in result["partitions"]
        assert result["partitions"]["system_b"]["size"] == 0
        assert "mi_ext_a" in result["partitions"]
        assert "mi_ext_b" in result["partitions"]
        assert result["partitions"]["mi_ext_b"]["size"] == 0

    def test_mi_ext_a_real_mi_ext_b_zero_accepted(self, tmp_path):
        """mi_ext_a real partition + mi_ext_b zero-size must both appear."""
        payload_bin = tmp_path / "payload.bin"
        payload_bin.write_bytes(b"fake")
        src = tmp_path / "source_images"
        _write(src / "mi_ext.img", b"x" * 4_000_000)

        with patch(
            "factory.super.payload_super_metadata._read_manifest_partition_sizes",
            return_value={"mi_ext": 4_000_000},
        ), patch(
            "factory.super.payload_super_metadata._read_manifest_group_name",
            return_value=("qti_dynamic_partitions", []),
        ):
            result = recover_super_metadata_from_payload(
                payload_manifest_path=payload_bin,
                source_images_dir=src,
                selected_codename="testdevice",
            )

        assert result["partition_sizes"]["mi_ext"] == 4_000_000
        assert result["partitions"]["mi_ext_a"]["size"] == 4_000_000
        assert result["partitions"]["mi_ext_b"]["size"] == 0
        # mi_ext_b zero is valid — should not appear in errors
        assert not any("mi_ext_b" in e for e in result["errors"])

    def test_all_nine_zircon_dynamic_partitions_accepted(self, tmp_path):
        """All 9 dynamic partitions for zircon-like MTK devices should be accepted."""
        payload_bin = tmp_path / "payload.bin"
        payload_bin.write_bytes(b"fake")
        src = tmp_path / "source_images"

        zircon_parts = [
            "system", "system_ext", "product", "vendor",
            "odm", "mi_ext", "vendor_dlkm", "odm_dlkm", "system_dlkm",
        ]
        sizes = {p: 100_000_000 for p in zircon_parts}

        with patch(
            "factory.super.payload_super_metadata._read_manifest_partition_sizes",
            return_value=sizes,
        ), patch(
            "factory.super.payload_super_metadata._read_manifest_group_name",
            return_value=("qti_dynamic_partitions", []),
        ):
            result = recover_super_metadata_from_payload(
                payload_manifest_path=payload_bin,
                source_images_dir=src,
                selected_codename="zircon",
            )

        for p in zircon_parts:
            assert p in result["partition_sizes"], f"Missing {p} in partition_sizes"
            assert f"{p}_a" in result["partitions"]
            assert f"{p}_b" in result["partitions"]


# ═══════════════════════════════════════════════════════════════════
# 3. Device registry super profile
# ═══════════════════════════════════════════════════════════════════

class TestRegistryProfile:
    """Registry YAML provides super_size and group_name fallback."""

    def _write_registry_yml(self, path: Path, super_size=9126805504,
                             group="qti_dynamic_partitions", metadata_slots=3,
                             slot_mode="vab"):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"codename: testdevice\n"
            f"super:\n"
            f"  super_size: {super_size}\n"
            f"  dynamic_group: {group}\n"
            f"  metadata_slots: {metadata_slots}\n"
            f"  slot_mode: {slot_mode}\n",
            encoding="utf-8",
        )

    def test_registry_super_size_used_when_manifest_absent(self, tmp_path):
        reg_yml = tmp_path / "testdevice.yml"
        self._write_registry_yml(reg_yml, super_size=8_589_934_592)

        src = tmp_path / "source_images"
        _write(src / "system.img", b"x" * 200_000_000)

        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="testdevice",
            registry_path=reg_yml,
        )

        assert result["super_size"] == 8_589_934_592

    def test_registry_group_name_used_when_manifest_absent(self, tmp_path):
        reg_yml = tmp_path / "testdevice.yml"
        self._write_registry_yml(reg_yml, group="main")

        src = tmp_path / "source_images"
        _write(src / "system.img")

        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="testdevice",
            registry_path=reg_yml,
        )

        assert result["group_name"] == "main"

    def test_registry_virtual_ab_from_slot_mode_vab(self, tmp_path):
        reg_yml = tmp_path / "testdevice.yml"
        self._write_registry_yml(reg_yml, slot_mode="vab")
        src = tmp_path / "source_images"
        _write(src / "system.img")

        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="testdevice",
            registry_path=reg_yml,
        )

        assert result["virtual_ab"] is True

    def test_manifest_group_overrides_registry_group(self, tmp_path):
        """Manifest group name takes priority over registry group name."""
        reg_yml = tmp_path / "testdevice.yml"
        self._write_registry_yml(reg_yml, group="registry_group")

        payload_bin = tmp_path / "payload.bin"
        payload_bin.write_bytes(b"fake")
        src = tmp_path / "source_images"

        with patch(
            "factory.super.payload_super_metadata._read_manifest_partition_sizes",
            return_value={"system": 100_000_000},
        ), patch(
            "factory.super.payload_super_metadata._read_manifest_group_name",
            return_value=("manifest_group", []),
        ):
            result = recover_super_metadata_from_payload(
                payload_manifest_path=payload_bin,
                source_images_dir=src,
                selected_codename="testdevice",
                registry_path=reg_yml,
            )

        assert result["group_name"] == "manifest_group"

    def test_registry_path_none_uses_default_group(self, tmp_path):
        src = tmp_path / "source_images"
        _write(src / "system.img")

        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="unknowndevice",
            registry_path=None,
        )

        # Should still return a valid group name (default or from images)
        assert result["group_name"]


# ═══════════════════════════════════════════════════════════════════
# 4. No hardcoded zircon-only logic
# ═══════════════════════════════════════════════════════════════════

class TestNoHardcodedDevice:
    """The module must not hardcode zircon, garnet or any specific codename."""

    def _run_for_codename(self, codename: str, tmp_path: Path) -> dict:
        src = tmp_path / "source_images"
        for p in ["system", "vendor", "product"]:
            _write(src / f"{p}.img", b"x" * 50_000_000)
        return recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename=codename,
        )

    @pytest.mark.parametrize("codename", [
        "zircon", "garnet", "aristotle", "aurora", "anydevice", "genericmtk"
    ])
    def test_any_codename_produces_valid_result(self, codename, tmp_path):
        result = self._run_for_codename(codename, tmp_path)
        assert result["super_size"] > 0
        assert result["group_name"]
        assert isinstance(result["partition_sizes"], dict)

    def test_source_code_contains_no_zircon_literal(self):
        """Ensure payload_super_metadata.py has no hardcoded 'zircon' string."""
        module_path = REPO_ROOT / "factory" / "super" / "payload_super_metadata.py"
        content = module_path.read_text(encoding="utf-8")
        assert "zircon" not in content.lower(), (
            "payload_super_metadata.py must not hardcode the 'zircon' codename"
        )


# ═══════════════════════════════════════════════════════════════════
# 5. super_rebuilder uses super_profile
# ═══════════════════════════════════════════════════════════════════

class TestSuperRebuilderProfile:
    """super_rebuilder.rebuild_super must use super_profile for group name and size."""

    def test_rebuild_super_accepts_super_profile(self, tmp_path):
        """rebuild_super signature accepts super_profile parameter."""
        from factory.super.super_rebuilder import rebuild_super
        import inspect
        sig = inspect.signature(rebuild_super)
        assert "super_profile" in sig.parameters

    def test_rebuild_super_uses_profile_group_name(self, tmp_path):
        """When super_profile is provided, group_name should appear in lpmake command."""
        from factory.super.super_rebuilder import rebuild_super

        parts_dir = tmp_path / "super_parts"
        parts_dir.mkdir()
        _write(parts_dir / "system.img", b"x" * 100_000)

        profile = {
            "super_size": 9_126_805_504,
            "group_name": "main",
            "metadata_slots": 3,
            "virtual_ab": True,
        }

        with patch("factory.super.super_rebuilder.resolve_lpmake_binary_legacy") as mock_lp:
            mock_lp.return_value = Path("/fake/lpmake")
            result = rebuild_super(
                super_parts_dir=parts_dir,
                output_super=tmp_path / "super.img",
                reports_dir=tmp_path / "reports",
                original_partition_sizes={"system": 200_000_000},
                execute=False,
                super_profile=profile,
            )

        cmd = result.get("lpmake_command") or []
        cmd_str = " ".join(str(c) for c in cmd)
        assert "main_a" in cmd_str or "main" in cmd_str, (
            f"lpmake command should reference 'main' group, got: {cmd_str}"
        )

    def test_rebuild_super_uses_profile_super_size(self, tmp_path):
        """When super_profile.super_size is set, it overrides the estimated size."""
        from factory.super.super_rebuilder import rebuild_super

        parts_dir = tmp_path / "super_parts"
        parts_dir.mkdir()
        _write(parts_dir / "system.img", b"x" * 100_000)

        custom_size = 8_589_934_592  # 8 GiB — different from default 9 GiB
        profile = {
            "super_size": custom_size,
            "group_name": "qti_dynamic_partitions",
            "metadata_slots": 3,
            "virtual_ab": True,
        }

        with patch("factory.super.super_rebuilder.resolve_lpmake_binary_legacy") as mock_lp:
            mock_lp.return_value = Path("/fake/lpmake")
            result = rebuild_super(
                super_parts_dir=parts_dir,
                output_super=tmp_path / "super.img",
                reports_dir=tmp_path / "reports",
                original_partition_sizes={"system": 200_000_000},
                execute=False,
                super_profile=profile,
            )

        cmd = result.get("lpmake_command") or []
        cmd_str = " ".join(str(c) for c in cmd)
        assert str(custom_size) in cmd_str, (
            f"Expected super_size {custom_size} in lpmake command, got: {cmd_str}"
        )

    def test_rebuild_super_vab_b_slots_in_command(self, tmp_path):
        """lpmake command must include _b zero-size slots for VAB."""
        from factory.super.super_rebuilder import rebuild_super

        parts_dir = tmp_path / "super_parts"
        parts_dir.mkdir()
        for p in ["system", "vendor"]:
            _write(parts_dir / f"{p}.img", b"x" * 100_000)

        profile = {
            "super_size": 9_126_805_504,
            "group_name": "qti_dynamic_partitions",
            "metadata_slots": 3,
            "virtual_ab": True,
        }

        with patch("factory.super.super_rebuilder.resolve_lpmake_binary_legacy") as mock_lp:
            mock_lp.return_value = Path("/fake/lpmake")
            result = rebuild_super(
                super_parts_dir=parts_dir,
                output_super=tmp_path / "super.img",
                reports_dir=tmp_path / "reports",
                original_partition_sizes={"system": 200_000_000, "vendor": 150_000_000},
                execute=False,
                super_profile=profile,
            )

        cmd = result.get("lpmake_command") or []
        cmd_str = " ".join(str(c) for c in cmd)
        # _b partitions must appear as zero-size placeholders
        assert "system_b:readonly:0" in cmd_str
        assert "vendor_b:readonly:0" in cmd_str
        # --virtual-ab flag must be present
        assert "--virtual-ab" in cmd_str


# ═══════════════════════════════════════════════════════════════════
# 6. universal_super_engine passes payload_super_metadata through
# ═══════════════════════════════════════════════════════════════════

class TestUniversalSuperEngineMetadataPassthrough:
    """execute_super_strategy must accept and forward payload_super_metadata."""

    def test_execute_super_strategy_accepts_payload_super_metadata(self):
        import inspect
        sig = inspect.signature(execute_super_strategy)
        assert "payload_super_metadata" in sig.parameters

    def test_execute_with_payload_metadata_no_original_super(self, tmp_path):
        """rebuild_with_lpmake + payload_super_metadata should not fail on empty partitions."""
        from factory.super.super_rebuilder import rebuild_super as _orig_rebuild

        parts_dir = tmp_path / "super_parts"
        parts_dir.mkdir()
        _write(parts_dir / "system.img", b"x" * 100_000)

        reports = tmp_path / "reports"
        output_super = tmp_path / "super.img"

        psm = {
            "metadata_source": "payload_manifest",
            "super_size": 9_126_805_504,
            "group_name": "qti_dynamic_partitions",
            "group_size": 9_126_805_504 - 4 * 1024 * 1024,
            "metadata_slots": 3,
            "virtual_ab": True,
            "partition_sizes": {"system": 200_000_000},
            "warnings": [],
            "errors": [],
        }

        rebuild_called_with: dict = {}

        def _fake_rebuild(**kwargs):
            rebuild_called_with.update(kwargs)
            return {
                "status": "DRY_RUN",
                "lpmake_command": [],
                "lpmake_executed": False,
                "super_img_created": False,
                "super_img_size": None,
                "super_metadata_source": "device_registry_profile",
                "validation_status": "NOT_RUN",
                "vab_b_slots_valid": False,
                "partitions_in_final": [],
                "missing_partitions": [],
                "warnings": [],
                "errors": [],
            }

        with patch("factory.super.super_rebuilder.rebuild_super", side_effect=_fake_rebuild):
            execute_super_strategy(
                strategy=STRATEGY_REBUILD_LPMAKE,
                original_super_img=None,
                super_parts_dir=parts_dir,
                output_super=output_super,
                reports_dir=reports,
                execute=False,
                payload_super_metadata=psm,
            )

        # original_partition_sizes must have been extracted from psm
        assert rebuild_called_with.get("original_partition_sizes") == {"system": 200_000_000}
        # super_profile must carry group_name and super_size
        sp = rebuild_called_with.get("super_profile") or {}
        assert sp.get("group_name") == "qti_dynamic_partitions"
        assert sp.get("super_size") == 9_126_805_504

    def test_metadata_source_appears_in_super_metadata_report(self, tmp_path):
        """super_metadata_report.txt must include the metadata_source field."""
        from factory.super.universal_super_engine import _write_super_metadata_report

        reports = tmp_path / "reports"
        psm = {
            "metadata_source": "payload_manifest",
            "super_size": 9_126_805_504,
            "group_name": "qti_dynamic_partitions",
            "group_size": 9_000_000_000,
            "virtual_ab": True,
        }
        fake_result = {
            "lpmake_executed": True,
            "lpmake_return_code": 0,
            "lpmake_command": ["/bin/lpmake", "--out", "/tmp/super.img"],
            "super_img_size": 9_126_805_504,
            "super_metadata_source": "device_registry_profile",
            "validation_status": "PASSED",
            "vab_b_slots_valid": True,
            "vab_b_slots_are_zero_size": True,
            "partitions_in_final": ["system_a", "system_b"],
            "errors": [],
            "warnings": [],
        }

        _write_super_metadata_report(
            reports_dir=reports,
            strategy=STRATEGY_REBUILD_LPMAKE,
            original_super_img=None,
            output_super=tmp_path / "super.img",
            rebuild_result=fake_result,
            payload_super_metadata=psm,
        )

        report_txt = (reports / "super_metadata_report.txt").read_text(encoding="utf-8")
        assert "payload_manifest" in report_txt
        assert "qti_dynamic_partitions" in report_txt

    def test_lpmake_command_in_super_metadata_report(self, tmp_path):
        """lpmake command must appear in super_metadata_report.txt."""
        from factory.super.universal_super_engine import _write_super_metadata_report

        reports = tmp_path / "reports"
        fake_result = {
            "lpmake_executed": True,
            "lpmake_return_code": 0,
            "lpmake_command": ["/bin/lpmake", "--device", "super:9126805504", "--out", "/x/super.img"],
            "super_img_size": 9_126_805_504,
            "super_metadata_source": "payload_manifest",
            "validation_status": "PASSED",
            "vab_b_slots_valid": True,
            "vab_b_slots_are_zero_size": True,
            "partitions_in_final": [],
            "errors": [],
            "warnings": [],
        }

        _write_super_metadata_report(
            reports_dir=reports,
            strategy=STRATEGY_REBUILD_LPMAKE,
            original_super_img=None,
            output_super=tmp_path / "super.img",
            rebuild_result=fake_result,
            payload_super_metadata=None,
        )

        report_txt = (reports / "super_metadata_report.txt").read_text(encoding="utf-8")
        assert "lpmake" in report_txt
        assert "super:9126805504" in report_txt


# ═══════════════════════════════════════════════════════════════════
# 7. super_rebuilder report
# ═══════════════════════════════════════════════════════════════════

class TestSuperRebuildReport:
    """super_rebuild_report.txt must show relevant fields."""

    def test_rebuild_report_shows_metadata_source(self, tmp_path):
        """super_rebuild_report.txt must include metadata source."""
        from factory.super.super_rebuilder import _write_report

        reports = tmp_path / "reports"
        result = {
            "status": "APPLIED",
            "strategy": "rebuild_with_lpmake",
            "super_metadata_source": "device_registry_profile",
            "super_img_created": True,
            "super_img_size": 9_000_000_000,
            "original_super_img": None,
            "output_super": str(tmp_path / "super.img"),
            "lpmake_executed": True,
            "lpmake_return_code": 0,
            "validation_status": "PASSED",
            "vab_b_slots_valid": True,
            "partitions_in_final": ["system_a", "system_b"],
            "missing_partitions": [],
            "lpmake_command": ["/bin/lpmake", "--partition", "system_a:readonly:200000000:grp"],
            "warnings": [],
            "errors": [],
        }

        _write_report(result, reports)

        txt = (reports / "super_rebuild_report.txt").read_text(encoding="utf-8")
        assert "device_registry_profile" in txt
        assert "lpmake" in txt.lower()

    def test_rebuild_report_shows_lpmake_command(self, tmp_path):
        from factory.super.super_rebuilder import _write_report

        reports = tmp_path / "reports"
        cmd = ["/bin/lpmake", "--device", "super:9126805504", "--partition", "system_a:readonly:200000000:grp_a"]
        result = {
            "status": "APPLIED",
            "strategy": "rebuild_with_lpmake",
            "super_metadata_source": "payload_manifest",
            "super_img_created": True,
            "super_img_size": 9_000_000_000,
            "original_super_img": None,
            "output_super": str(tmp_path / "super.img"),
            "lpmake_executed": True,
            "lpmake_return_code": 0,
            "validation_status": "PASSED",
            "vab_b_slots_valid": True,
            "partitions_in_final": [],
            "missing_partitions": [],
            "lpmake_command": cmd,
            "warnings": [],
            "errors": [],
        }

        _write_report(result, reports)

        txt = (reports / "super_rebuild_report.txt").read_text(encoding="utf-8")
        assert "super:9126805504" in txt
        assert "system_a" in txt


# ═══════════════════════════════════════════════════════════════════
# 8. Failure message quality
# ═══════════════════════════════════════════════════════════════════

class TestFailureMessages:
    """When metadata cannot be recovered, errors must be informative."""

    def test_error_lists_attempted_sources_when_all_fail(self, tmp_path):
        src = tmp_path / "source_images"
        src.mkdir()
        # No payload.bin, no registry, no images -> should produce error listing sources

        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="unknowndevice",
            registry_path=None,
        )

        # errors should be non-empty
        assert result["errors"]
        # attempted_sources should be populated
        assert result["attempted_sources"]

    def test_error_mentions_registry_suggestion_when_no_profile(self, tmp_path):
        src = tmp_path / "source_images"
        src.mkdir()

        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="unknowndevice",
            registry_path=None,
        )

        combined = " ".join(result["errors"] + result["warnings"])
        # Should mention registry or profile somewhere
        assert any(
            kw in combined.lower()
            for kw in ["registry", "profile", "super_size", "attempted"]
        )


# ═══════════════════════════════════════════════════════════════════
# 9. Zircon registry file integration
# ═══════════════════════════════════════════════════════════════════

class TestZirconRegistry:
    """The actual zircon.yml registry file must be readable by the profile reader."""

    def test_zircon_registry_readable(self):
        zircon_yml = REPO_ROOT / "registry" / "devices" / "mtk" / "zircon.yml"
        if not zircon_yml.is_file():
            pytest.skip("zircon.yml not found")

        profile = _read_registry_super_profile(zircon_yml, "zircon")

        assert profile.get("super_size") == 9_126_805_504
        assert profile.get("group_name") == "qti_dynamic_partitions"
        assert profile.get("metadata_slots") == 3
        assert profile.get("virtual_ab") is True

    def test_zircon_registry_integration_with_recover(self, tmp_path):
        """End-to-end: recover with zircon registry, manifest absent."""
        zircon_yml = REPO_ROOT / "registry" / "devices" / "mtk" / "zircon.yml"
        if not zircon_yml.is_file():
            pytest.skip("zircon.yml not found")

        src = tmp_path / "source_images"
        zircon_parts = [
            "system", "system_ext", "product", "vendor",
            "odm", "mi_ext", "vendor_dlkm", "odm_dlkm", "system_dlkm",
        ]
        for p in zircon_parts:
            _write(src / f"{p}.img", b"x" * 50_000_000)

        result = recover_super_metadata_from_payload(
            payload_manifest_path=None,
            source_images_dir=src,
            selected_codename="zircon",
            registry_path=zircon_yml,
        )

        assert result["super_size"] == 9_126_805_504
        assert result["group_name"] == "qti_dynamic_partitions"
        assert result["virtual_ab"] is True
        # Partition sizes should come from image files as fallback
        for p in zircon_parts:
            assert p in result["partition_sizes"]


# ── Runner ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import traceback
    tests = [(k, v) for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    passed = failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  PASS  {name}")
            passed += 1
        except Exception as exc:
            print(f"  FAIL  {name}: {exc}")
            traceback.print_exc()
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    import sys
    sys.exit(1 if failed else 0)
