"""Tests for final ZIP compression behaviour in factory.output.final_zip_legacy.

Covers:
  1. Default env (no DEADZONE_ZIP_LEVEL / DEADZONE_ZIP_COMPRESSION) → ZIP_DEFLATED level 6
  2. Absent env vars never default to ZIP_STORED
  3. DEADZONE_ZIP_COMPRESSION=stored → ZIP_STORED
  4. DEADZONE_ZIP_LEVEL=0 → ZIP_STORED
  5. Fallback to ZIP_STORED only when deflate raises an exception
  6. Final report contains all required compression fields with actual values
  7. upload_file_path points to the compressed ZIP
  8. DeadZone_Mezo template_source is preserved after compression fix
  9. exactly_one_super_img is True after compression fix
"""
from __future__ import annotations

import io
import os
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from factory.output.final_zip_legacy import build_final_fastboot_zip


# ── Minimal staging helpers ───────────────────────────────────────────────────

def _write(path: Path, content: bytes = b"x" * 1024) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


def _make_images_dir(tmp: Path) -> Path:
    """Create output/images/final with the minimum required images."""
    img_dir = tmp / "output" / "images" / "final"
    img_dir.mkdir(parents=True, exist_ok=True)
    for name in ["super.img", "boot.img", "init_boot.img", "vendor_boot.img",
                 "vbmeta.img", "vbmeta_system.img", "dtbo.img",
                 "lk.img", "tee.img", "logo.img"]:
        _write(img_dir / name)
    return img_dir


def _make_dz_mezo_dir(tmp: Path) -> Path:
    """Create a minimal DeadZone_Mezo directory tree expected by the template patcher."""
    dz = tmp / "DeadZone_Mezo"
    for sub in ["bin/windows", "bin/linux", "bin/macos", "META-INF/com/google/android"]:
        (dz / sub).mkdir(parents=True, exist_ok=True)
    for fname in ["fastboot.exe", "AdbWinApi.dll", "AdbWinUsbApi.dll"]:
        _write(dz / "bin" / "windows" / fname)
    _write(dz / "bin" / "linux" / "fastboot")
    _write(dz / "bin" / "macos" / "fastboot")
    _write(dz / "META-INF" / "com" / "google" / "android" / "updater-script", b"# meta")
    for script in [
        "windows_install_and_format_data.bat",
        "windows_install_upgrade.bat",
        "windows_format_data_only.bat",
        "linux_install_and_format_data.sh",
        "linux_install_upgrade.sh",
        "linux_format_data_only.sh",
        "macos_install_and_format_data.sh",
        "macos_install_upgrade.sh",
        "macos_format_data_only.sh",
    ]:
        _write(dz / script, b"#!/bin/sh\necho hello")
    return dz


def _patch_template_patcher(staging_dir: Path, dz_dir: Path) -> Any:
    """Return a mock for patch_deadzone_template that copies the minimal tree."""
    import shutil

    def _fake_patch(**kwargs) -> dict:
        _staging = Path(kwargs["staging_dir"])
        _staging.mkdir(parents=True, exist_ok=True)
        # Copy full dz_dir tree into staging
        for src in dz_dir.rglob("*"):
            if src.is_file():
                rel = src.relative_to(dz_dir)
                dst = _staging / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
        return {
            "status": "APPLIED",
            "scripts_patched": [
                "windows_install_and_format_data.bat",
                "windows_install_upgrade.bat",
                "windows_format_data_only.bat",
                "linux_install_and_format_data.sh",
                "linux_install_upgrade.sh",
                "linux_format_data_only.sh",
                "macos_install_and_format_data.sh",
                "macos_install_upgrade.sh",
                "macos_format_data_only.sh",
            ],
            "warnings": [],
            "errors": [],
        }

    return _fake_patch


def _run_build(tmp: Path, env_overrides: dict | None = None) -> dict:
    """Run build_final_fastboot_zip with a fully mocked template patcher."""
    img_dir = _make_images_dir(tmp)
    dz_dir = _make_dz_mezo_dir(tmp)
    out_dir = tmp / "output" / "final"
    out_dir.mkdir(parents=True, exist_ok=True)

    fake_patch = _patch_template_patcher(tmp, dz_dir)
    env = {k: v for k, v in os.environ.items()}
    # Remove defaults so tests control env cleanly
    env.pop("DEADZONE_ZIP_LEVEL", None)
    env.pop("DEADZONE_ZIP_COMPRESSION", None)
    if env_overrides:
        env.update(env_overrides)

    with patch(
        "factory.output.final_zip_legacy._find_deadzone_mezo_dir",
        return_value=dz_dir,
    ), patch(
        "factory.output.deadzone_template_patcher.patch_deadzone_template",
        side_effect=fake_patch,
    ), patch.dict(os.environ, env, clear=True):
        report = build_final_fastboot_zip(
            images_dir=img_dir,
            output_dir=out_dir,
            build_name="TestBuild",
            device="zircon",
            flavor="free",
            soc="snapdragon",
            android_version="15",
            build_incremental="OS3.0.1.0.TEST",
            region="global",
            execute=True,
        )
    return report


# ═══════════════════════════════════════════════════════════════════
# 1. Default env → ZIP_DEFLATED level 6
# ═══════════════════════════════════════════════════════════════════

class TestDefaultCompression:
    def test_default_uses_deflated(self, tmp_path):
        report = _run_build(tmp_path)
        assert report["actual_compression_method"] == "ZIP_DEFLATED", (
            f"Expected ZIP_DEFLATED but got {report.get('actual_compression_method')!r}. "
            f"compression_mode={report.get('compression_mode')}"
        )

    def test_default_level_is_6(self, tmp_path):
        report = _run_build(tmp_path)
        assert report["actual_compression_level"] == 6

    def test_default_no_fallback(self, tmp_path):
        report = _run_build(tmp_path)
        assert report["compression_fallback"] is False
        assert report["fallback_reason"] is None


# ═══════════════════════════════════════════════════════════════════
# 2. Absent env never defaults to ZIP_STORED
# ═══════════════════════════════════════════════════════════════════

class TestNoEnvNotStored:
    def test_no_env_not_stored(self, tmp_path):
        report = _run_build(tmp_path, env_overrides={})
        assert report["actual_compression_method"] != "ZIP_STORED", (
            "With no env vars set, compression must not be ZIP_STORED"
        )

    def test_no_env_compression_ratio_below_one(self, tmp_path):
        report = _run_build(tmp_path, env_overrides={})
        ratio = report.get("compression_ratio", 1.0)
        # Compressible test data (repeated bytes) should deflate well
        assert ratio <= 1.0


# ═══════════════════════════════════════════════════════════════════
# 3. DEADZONE_ZIP_COMPRESSION=stored → ZIP_STORED
# ═══════════════════════════════════════════════════════════════════

class TestExplicitStored:
    def test_compression_env_stored(self, tmp_path):
        report = _run_build(tmp_path, env_overrides={"DEADZONE_ZIP_COMPRESSION": "stored"})
        assert report["actual_compression_method"] == "ZIP_STORED"

    def test_compression_env_stored_level_is_zero(self, tmp_path):
        report = _run_build(tmp_path, env_overrides={"DEADZONE_ZIP_COMPRESSION": "stored"})
        assert report["actual_compression_level"] == 0

    def test_compression_env_stored_no_fallback(self, tmp_path):
        report = _run_build(tmp_path, env_overrides={"DEADZONE_ZIP_COMPRESSION": "stored"})
        assert report["compression_fallback"] is False


# ═══════════════════════════════════════════════════════════════════
# 4. DEADZONE_ZIP_LEVEL=0 → ZIP_STORED
# ═══════════════════════════════════════════════════════════════════

class TestZipLevelZeroStored:
    def test_level_zero_gives_stored(self, tmp_path):
        report = _run_build(tmp_path, env_overrides={"DEADZONE_ZIP_LEVEL": "0"})
        assert report["actual_compression_method"] == "ZIP_STORED"

    def test_level_zero_no_fallback(self, tmp_path):
        report = _run_build(tmp_path, env_overrides={"DEADZONE_ZIP_LEVEL": "0"})
        assert report["compression_fallback"] is False


# ═══════════════════════════════════════════════════════════════════
# 5. Fallback only on real exception from deflate
# ═══════════════════════════════════════════════════════════════════

class TestFallback:
    def test_fallback_on_deflate_exception(self, tmp_path):
        img_dir = _make_images_dir(tmp_path)
        dz_dir = _make_dz_mezo_dir(tmp_path)
        out_dir = tmp_path / "output" / "final"
        out_dir.mkdir(parents=True, exist_ok=True)
        fake_patch = _patch_template_patcher(tmp_path, dz_dir)

        _deflate_call_count = [0]
        _real_ZipFile = zipfile.ZipFile

        def _failing_ZipFile(path, mode, compression=0, *args, **kwargs):
            if compression == zipfile.ZIP_DEFLATED:
                _deflate_call_count[0] += 1
                raise OSError("simulated deflate failure")
            return _real_ZipFile(path, mode, compression, *args, **kwargs)

        env = {k: v for k, v in os.environ.items()}
        env.pop("DEADZONE_ZIP_LEVEL", None)
        env.pop("DEADZONE_ZIP_COMPRESSION", None)

        with patch("factory.output.final_zip_legacy._find_deadzone_mezo_dir", return_value=dz_dir), \
             patch("factory.output.deadzone_template_patcher.patch_deadzone_template", side_effect=fake_patch), \
             patch("factory.output.final_zip_legacy.zipfile.ZipFile", side_effect=_failing_ZipFile), \
             patch.dict(os.environ, env, clear=True):
            report = build_final_fastboot_zip(
                images_dir=img_dir,
                output_dir=out_dir,
                build_name="FallbackBuild",
                device="zircon",
                flavor="free",
                soc="snapdragon",
                android_version="15",
                build_incremental="OS3.0.1.0.TEST",
                region="global",
                execute=True,
            )

        assert report["compression_fallback"] is True, "fallback must be True when deflate raises"
        assert report["actual_compression_method"] == "ZIP_STORED"
        assert "simulated deflate failure" in (report.get("fallback_reason") or "")
        assert report.get("original_requested_compression") == "ZIP_DEFLATED"
        assert report.get("final_compression_method") == "ZIP_STORED"

    def test_no_fallback_without_exception(self, tmp_path):
        report = _run_build(tmp_path)
        assert report["compression_fallback"] is False


# ═══════════════════════════════════════════════════════════════════
# 6. Report fields are complete and accurate
# ═══════════════════════════════════════════════════════════════════

class TestReportFields:
    def test_required_fields_present(self, tmp_path):
        report = _run_build(tmp_path)
        required = [
            "requested_compression_method",
            "requested_compression_level",
            "actual_compression_method",
            "actual_compression_level",
            "compression_fallback",
            "fallback_reason",
            "uncompressed_size_mib",
            "compressed_zip_size_mib",
            "compression_ratio",
        ]
        for field in required:
            assert field in report, f"Missing report field: {field}"

    def test_actual_method_matches_zip_content(self, tmp_path):
        report = _run_build(tmp_path)
        zip_path = Path(report["upload_file_path"])
        assert zip_path.is_file()
        with zipfile.ZipFile(zip_path) as zf:
            infos = zf.infolist()
        assert infos, "ZIP must not be empty"
        # All non-empty entries should use deflated compression (method=8)
        for info in infos:
            if info.file_size > 0:
                assert info.compress_type == zipfile.ZIP_DEFLATED, (
                    f"Entry {info.filename} uses compress_type={info.compress_type}, "
                    "expected ZIP_DEFLATED (8)"
                )

    def test_compression_ratio_reflects_actual(self, tmp_path):
        report = _run_build(tmp_path)
        ratio = report["compression_ratio"]
        assert ratio is not None
        assert 0 < ratio <= 1.0

    def test_stored_ratio_not_below_deflated(self, tmp_path):
        deflated = _run_build(tmp_path)
        stored = _run_build(tmp_path, env_overrides={"DEADZONE_ZIP_COMPRESSION": "stored"})
        # Stored file size >= deflated file size (deflate can only help or be neutral)
        assert stored["compressed_zip_size_mib"] >= deflated["compressed_zip_size_mib"]


# ═══════════════════════════════════════════════════════════════════
# 7. upload_file_path points to the final ZIP
# ═══════════════════════════════════════════════════════════════════

class TestUploadFilePath:
    def test_upload_file_path_set(self, tmp_path):
        report = _run_build(tmp_path)
        assert report.get("upload_file_path") is not None

    def test_upload_file_path_is_zip(self, tmp_path):
        report = _run_build(tmp_path)
        p = Path(report["upload_file_path"])
        assert p.suffix == ".zip"
        assert p.is_file()

    def test_upload_file_path_is_compressed_zip(self, tmp_path):
        report = _run_build(tmp_path)
        p = Path(report["upload_file_path"])
        with zipfile.ZipFile(p) as zf:
            infos = [i for i in zf.infolist() if i.file_size > 0]
        deflated = [i for i in infos if i.compress_type == zipfile.ZIP_DEFLATED]
        assert deflated, "upload_file_path ZIP must contain at least one DEFLATED entry"


# ═══════════════════════════════════════════════════════════════════
# 8. DeadZone_Mezo template_source preserved
# ═══════════════════════════════════════════════════════════════════

class TestTemplatePersistence:
    def test_template_source_is_deadzone_mezo(self, tmp_path):
        report = _run_build(tmp_path)
        assert report.get("template_source") == "DeadZone_Mezo"

    def test_template_source_preserved_with_stored(self, tmp_path):
        report = _run_build(tmp_path, env_overrides={"DEADZONE_ZIP_COMPRESSION": "stored"})
        assert report.get("template_source") == "DeadZone_Mezo"


# ═══════════════════════════════════════════════════════════════════
# 9. exactly_one_super_img preserved
# ═══════════════════════════════════════════════════════════════════

class TestSuperImgIntegrity:
    def test_exactly_one_super_img_true(self, tmp_path):
        report = _run_build(tmp_path)
        assert report.get("exactly_one_super_img") is True

    def test_exactly_one_super_img_true_with_deflated(self, tmp_path):
        report = _run_build(tmp_path, env_overrides={"DEADZONE_ZIP_LEVEL": "6"})
        assert report.get("exactly_one_super_img") is True

    def test_super_img_in_final_zip(self, tmp_path):
        report = _run_build(tmp_path)
        zip_path = Path(report["upload_file_path"])
        with zipfile.ZipFile(zip_path) as zf:
            names = zf.namelist()
        assert any("super.img" in n for n in names), (
            f"super.img not found in ZIP entries: {names}"
        )
