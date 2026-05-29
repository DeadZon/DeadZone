"""Tests for factory.input.xiaomi_rom_metadata and rom_detector filename fallback.

Covers:
  - parse zorn fastboot TGZ filename
  - parse zircon OTA filename
  - parse garnet fastboot TGZ filename
  - detect CN region from _cn_ suffix
  - detect CN region from CNXM code in build_incremental
  - detect Global from MIXM code
  - detect HyperOS 3 from OS3 prefix
  - rom_detector fills metadata from filename fallback (no build.prop in archive)
  - flash script metadata accepts values parsed from filename
  - zorn final_zip no longer fails due to missing android/build/region
"""
import io
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.input.xiaomi_rom_metadata import (
    parse_xiaomi_rom_metadata,
    parse_xiaomi_rom_metadata_from_sources,
)
from factory.input.rom_detector import detect_rom_format, FORMAT_FASTBOOT_TGZ
from factory.output.flash_scripts import FlashScriptMetadata, generate_windows_flash_scripts


# ── Archive helpers ────────────────────────────────────────────────────────────

def _make_tgz(path: Path, members: dict) -> Path:
    with tarfile.open(str(path), "w:gz") as tf:
        for name, content in members.items():
            info = tarfile.TarInfo(name=name)
            info.size = len(content)
            tf.addfile(info, io.BytesIO(content))
    return path


def _write(path: Path, content: bytes = b"fake_img") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


# ═══════════════════════════════════════════════════════════════════
# 1. FILENAME PARSER — basic parse
# ═══════════════════════════════════════════════════════════════════

class TestParseZornFastbootFilename:
    _NAME = "zorn_images_OS3.0.303.0.WOKCNXM_20260425.0000.00_16.0_cn_e6cf5ef711.tgz"

    def test_codename(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["codename"] == "zorn"

    def test_build_incremental(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["build_incremental"] == "OS3.0.303.0.WOKCNXM"

    def test_android_version(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["android_version"] == "16.0"

    def test_region(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["region"] == "CN"

    def test_os_name(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["os_name"] == "HyperOS 3"

    def test_os_family(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["os_family"] == "HyperOS"

    def test_os_major(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["os_major"] == "3"

    def test_build_date(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["build_date"] == "20260425.0000.00"


class TestParseZirconOtaFilename:
    _NAME = "zircon-ota_full-OS3.0.303.0.WNOCNXM-user-16.0-09c35a83d6.zip"

    def test_codename(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["codename"] == "zircon"

    def test_build_incremental(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["build_incremental"] == "OS3.0.303.0.WNOCNXM"

    def test_android_version(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["android_version"] == "16.0"

    def test_region_from_cnxm(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["region"] == "CN"

    def test_os_name(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["os_name"] == "HyperOS 3"


class TestParseGarnetFastbootFilename:
    _NAME = "garnet_images_OS3.0.304.0.WNRCNXM_20260428.0000.00_16.0_cn_aabbccddee.tgz"

    def test_codename(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["codename"] == "garnet"

    def test_build_incremental(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["build_incremental"] == "OS3.0.304.0.WNRCNXM"

    def test_android_version(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["android_version"] == "16.0"

    def test_region(self):
        result = parse_xiaomi_rom_metadata(self._NAME)
        assert result["region"] == "CN"


# ═══════════════════════════════════════════════════════════════════
# 2. REGION DETECTION
# ═══════════════════════════════════════════════════════════════════

class TestRegionDetection:
    def test_cn_from_cn_suffix(self):
        result = parse_xiaomi_rom_metadata(
            "zorn_images_OS3.0.303.0.WOKCNXM_20260425.0000.00_16.0_cn_abc123.tgz"
        )
        assert result["region"] == "CN"

    def test_cn_from_cnxm_in_build_incremental(self):
        result = parse_xiaomi_rom_metadata(
            "zircon-ota_full-OS3.0.303.0.WNOCNXM-user-16.0-09c35a83d6.zip"
        )
        assert result["region"] == "CN"

    def test_global_from_mixm(self):
        result = parse_xiaomi_rom_metadata(
            "zorn_images_OS3.0.303.0.WOKMIXM_20260425.0000.00_16.0_global_abc123.tgz"
        )
        assert result["region"] == "Global"

    def test_eea_from_euxm(self):
        result = parse_xiaomi_rom_metadata(
            "garnet_images_OS3.0.304.0.WNREUXM_20260428.0000.00_16.0_eu_abc123.tgz"
        )
        assert result["region"] == "EEA"

    def test_unknown_region_returns_empty(self):
        result = parse_xiaomi_rom_metadata(
            "zorn_images_OS3.0.303.0.WOKXXXM_20260425.0000.00_16.0_uk_abc123.tgz"
        )
        # XXXM is not a known suffix and uk is not cn
        assert result.get("region", "") == ""


# ═══════════════════════════════════════════════════════════════════
# 3. OS DETECTION
# ═══════════════════════════════════════════════════════════════════

class TestOsDetection:
    def test_hyperos3_from_os3(self):
        result = parse_xiaomi_rom_metadata(
            "zorn_images_OS3.0.303.0.WOKCNXM_20260425.0000.00_16.0_cn_abc123.tgz"
        )
        assert result["os_name"] == "HyperOS 3"
        assert result["os_family"] == "HyperOS"
        assert result["os_major"] == "3"

    def test_hyperos2_from_os2(self):
        result = parse_xiaomi_rom_metadata(
            "garnet_images_OS2.0.1.0.TNRCNXM_20251010.0000.00_14.0_cn_abc123.tgz"
        )
        assert result["os_name"] == "HyperOS 2"
        assert result["os_major"] == "2"

    def test_hyperos1_from_os1(self):
        result = parse_xiaomi_rom_metadata(
            "garnet_images_OS1.0.1.0.TNRCNXM_20240101.0000.00_14.0_cn_abc123.tgz"
        )
        assert result["os_name"] == "HyperOS 1"
        assert result["os_major"] == "1"


class TestUnknownFilenameReturnsEmpty:
    def test_generic_name_returns_empty(self):
        result = parse_xiaomi_rom_metadata("random_rom.zip")
        assert result == {}

    def test_full_path_uses_basename(self):
        result = parse_xiaomi_rom_metadata(
            "/data/roms/zorn_images_OS3.0.303.0.WOKCNXM_20260425.0000.00_16.0_cn_e6cf5ef711.tgz"
        )
        assert result["codename"] == "zorn"

    def test_empty_string_returns_empty(self):
        result = parse_xiaomi_rom_metadata("")
        assert result == {}


class TestParseMetadataFromSources:
    _URL = (
        "https://bigota.d.miui.com/OS3.0.303.0.WOKCNXM/"
        "zorn_images_OS3.0.303.0.WOKCNXM_20260425.0000.00_16.0_cn_e6cf5ef711.tgz"
    )

    def test_parse_metadata_from_url(self):
        result = parse_xiaomi_rom_metadata_from_sources(self._URL)
        assert result["codename"] == "zorn"
        assert result["android_version"] == "16.0"
        assert result["build_incremental"] == "OS3.0.303.0.WOKCNXM"
        assert result["region"] == "CN"
        assert result["metadata_source"] == "rom_url_filename"

    def test_url_fills_when_local_filename_is_source_rom(self):
        result = parse_xiaomi_rom_metadata_from_sources("source_rom.tgz", self._URL)
        assert result["android_version"] == "16.0"
        assert result["build_incremental"] == "OS3.0.303.0.WOKCNXM"
        assert result["metadata_source"] == "rom_url_filename"

    def test_local_source_rom_alone_has_no_metadata(self):
        assert parse_xiaomi_rom_metadata("source_rom.tgz") == {}


# ═══════════════════════════════════════════════════════════════════
# 4. ROM DETECTOR FILENAME FALLBACK
# ═══════════════════════════════════════════════════════════════════

class TestRomDetectorFilenameFallback:
    """detect_rom_format must fill metadata from filename when build.prop is absent."""

    def test_zorn_tgz_without_build_prop_gets_metadata(self):
        """A fastboot TGZ with no build.prop must still populate metadata from filename."""
        with tempfile.TemporaryDirectory() as tmp:
            rom_path = Path(tmp) / "zorn_images_OS3.0.303.0.WOKCNXM_20260425.0000.00_16.0_cn_e6cf5ef711.tgz"
            _make_tgz(rom_path, {
                "images/boot.img":        b"boot",
                "images/vendor_boot.img": b"vboot",
                "images/init_boot.img":   b"ib",
                "images/vbmeta.img":      b"vbmeta",
                "images/dtbo.img":        b"dtbo",
                "images/super.img":       b"SUPER",
            })
            result = detect_rom_format(rom_path)

        assert result.rom_format == FORMAT_FASTBOOT_TGZ
        assert result.detected_android_version == "16.0", (
            f"Expected android_version=16.0 but got {result.detected_android_version!r}"
        )
        assert result.detected_hyperos_or_miui_version == "OS3.0.303.0.WOKCNXM", (
            f"Expected build_incremental=OS3.0.303.0.WOKCNXM but got "
            f"{result.detected_hyperos_or_miui_version!r}"
        )
        assert result.detected_region == "CN", (
            f"Expected region=CN but got {result.detected_region!r}"
        )

    def test_fallback_does_not_override_build_prop_values(self):
        """If build.prop provides metadata, filename fallback must NOT overwrite it."""
        build_prop_content = (
            b"ro.product.device=garnet\n"
            b"ro.build.version.release=15\n"
            b"ro.build.version.incremental=OS2.9.1.0.TNRCNXM\n"
            b"ro.miui.region=CN\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            # Filename says OS3/16.0 but build.prop says OS2/15
            rom_path = Path(tmp) / "zorn_images_OS3.0.303.0.WOKCNXM_20260425.0000.00_16.0_cn_abc.tgz"
            _make_tgz(rom_path, {
                "images/boot.img":   b"boot",
                "images/vbmeta.img": b"vbmeta",
                "images/dtbo.img":   b"dtbo",
                "images/super.img":  b"SUPER",
                "system/build.prop": build_prop_content,
            })
            result = detect_rom_format(rom_path)

        # build.prop values take precedence
        assert result.detected_android_version == "15"
        assert result.detected_hyperos_or_miui_version == "OS2.9.1.0.TNRCNXM"


# ═══════════════════════════════════════════════════════════════════
# 5. FLASH SCRIPT METADATA ACCEPTS PARSED VALUES
# ═══════════════════════════════════════════════════════════════════

class TestFlashScriptAcceptsParsedMetadata:
    def test_zorn_metadata_builds_without_error(self):
        parsed = parse_xiaomi_rom_metadata(
            "zorn_images_OS3.0.303.0.WOKCNXM_20260425.0000.00_16.0_cn_e6cf5ef711.tgz"
        )
        meta = FlashScriptMetadata.build(
            edition="deadzone",
            device_codename="zorn",
            device_model="zorn",
            android_version=parsed["android_version"],
            build_incremental=parsed["build_incremental"],
            image_count=13,
        )
        assert meta.android_version == "16.0"
        assert meta.build_incremental == "OS3.0.303.0.WOKCNXM"
        assert meta.region == "China"
        assert meta.os_name == "HyperOS 3"

    def test_zircon_ota_metadata_builds_without_error(self):
        parsed = parse_xiaomi_rom_metadata(
            "zircon-ota_full-OS3.0.303.0.WNOCNXM-user-16.0-09c35a83d6.zip"
        )
        meta = FlashScriptMetadata.build(
            edition="deadzone",
            device_codename="zircon",
            device_model="zircon",
            android_version=parsed["android_version"],
            build_incremental=parsed["build_incremental"],
            image_count=10,
        )
        assert meta.android_version == "16.0"
        assert meta.region == "China"
        assert meta.os_name == "HyperOS 3"


# ═══════════════════════════════════════════════════════════════════
# 6. ZORN FINAL ZIP — end-to-end: no failure due to missing metadata
# ═══════════════════════════════════════════════════════════════════

class TestZornFinalZipDoesNotFailOnMetadata:
    """generate_windows_flash_scripts must succeed with parsed zorn metadata."""

    def test_generate_scripts_with_zorn_parsed_metadata(self):
        parsed = parse_xiaomi_rom_metadata(
            "zorn_images_OS3.0.303.0.WOKCNXM_20260425.0000.00_16.0_cn_e6cf5ef711.tgz"
        )
        with tempfile.TemporaryDirectory() as tmp:
            staging = Path(tmp) / "staging"
            images_dir = Path(tmp) / "images"
            images_dir.mkdir()
            # Place minimal required images
            for name in ["boot.img", "vbmeta.img", "super.img"]:
                _write(images_dir / name)

            result = generate_windows_flash_scripts(
                staging_dir=staging,
                images_dir=images_dir,
                device="zorn",
                device_model="zorn",
                edition="deadzone",
                android_version=parsed["android_version"],
                build_incremental=parsed["build_incremental"],
                execute=False,
            )

        assert result["status"] != "FAILED", (
            f"Flash script generation must not fail for zorn with parsed metadata.\n"
            f"Error: {result.get('error', '')}"
        )
        assert len(result["scripts_generated"]) == 3

    def test_flash_script_generation_fails_without_metadata(self):
        """Control test: confirm generation fails when metadata is empty."""
        with tempfile.TemporaryDirectory() as tmp:
            staging = Path(tmp) / "staging"
            images_dir = Path(tmp) / "images"
            images_dir.mkdir()
            _write(images_dir / "boot.img")

            result = generate_windows_flash_scripts(
                staging_dir=staging,
                images_dir=images_dir,
                device="zorn",
                device_model="zorn",
                edition="deadzone",
                android_version=None,
                build_incremental=None,
                execute=False,
            )

        assert result["status"] == "FAILED"
        assert "android_version is missing" in result.get("error", "")


# ═══════════════════════════════════════════════════════════════════
# 7. ZIRCON OTA FILENAME FALLBACK — end-to-end pipeline metadata test
# ═══════════════════════════════════════════════════════════════════

class TestZirconOtaFilenameMetadataFallback:
    """Filename fallback for local payload OTA builds.

    Given: zircon-ota_full-OS3.0.303.0.WNOCNXM-user-16.0-09c35a83d6.zip
    Expected:
      - codename=zircon
      - android_version=16.0
      - mi_incremental/build_incremental=OS3.0.303.0.WNOCNXM
      - final zip metadata validation passes (FlashScriptMetadata.build succeeds)
    """
    _FILENAME = "zircon-ota_full-OS3.0.303.0.WNOCNXM-user-16.0-09c35a83d6.zip"

    def test_codename(self):
        result = parse_xiaomi_rom_metadata_from_sources(self._FILENAME)
        assert result.get("codename") == "zircon"

    def test_android_version(self):
        result = parse_xiaomi_rom_metadata_from_sources(self._FILENAME)
        assert result.get("android_version") == "16.0"

    def test_mi_incremental(self):
        result = parse_xiaomi_rom_metadata_from_sources(self._FILENAME)
        assert result.get("build_incremental") == "OS3.0.303.0.WNOCNXM"

    def test_sources_attempted_always_present_on_match(self):
        """metadata_sources_attempted must be in the result when a filename matches."""
        result = parse_xiaomi_rom_metadata_from_sources(self._FILENAME)
        assert "metadata_sources_attempted" in result
        assert self._FILENAME in result["metadata_sources_attempted"]

    def test_sources_attempted_always_present_on_no_match(self):
        """metadata_sources_attempted must be present even when no pattern matches."""
        result = parse_xiaomi_rom_metadata_from_sources("some_unknown_rom.zip")
        assert "metadata_sources_attempted" in result
        assert "some_unknown_rom.zip" in result["metadata_sources_attempted"]

    def test_final_zip_metadata_validation_passes(self):
        """Metadata from zircon OTA filename must satisfy FlashScriptMetadata.build()."""
        result = parse_xiaomi_rom_metadata_from_sources(self._FILENAME)
        meta = FlashScriptMetadata.build(
            edition="deadzone",
            device_codename=result["codename"],
            device_model=result["codename"],
            android_version=result["android_version"],
            build_incremental=result["build_incremental"],
            image_count=10,
        )
        assert meta.android_version == "16.0"
        assert meta.build_incremental == "OS3.0.303.0.WNOCNXM"
        assert meta.device_codename == "zircon"
        assert meta.os_name == "HyperOS 3"
        assert meta.region == "China"

    def test_from_path_extracts_filename(self):
        """Full local path must resolve to the filename and still parse correctly."""
        full_path = f"/tmp/roms/{self._FILENAME}"
        result = parse_xiaomi_rom_metadata_from_sources(full_path)
        assert result.get("android_version") == "16.0"
        assert result.get("build_incremental") == "OS3.0.303.0.WNOCNXM"
        assert result.get("codename") == "zircon"


# ── Runner ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import traceback

    passed = failed = 0
    for cls_name, cls_obj in sorted(globals().items()):
        if not (isinstance(cls_obj, type) and cls_name.startswith("Test")):
            continue
        instance = cls_obj()
        for method_name in sorted(dir(instance)):
            if not method_name.startswith("test_"):
                continue
            method = getattr(instance, method_name)
            if not callable(method):
                continue
            try:
                method()
                print(f"  PASS  {cls_name}.{method_name}")
                passed += 1
            except Exception as exc:
                print(f"  FAIL  {cls_name}.{method_name}: {exc}")
                traceback.print_exc()
                failed += 1

    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
