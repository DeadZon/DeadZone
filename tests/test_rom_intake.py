"""Tests for the Universal ROM Intake pipeline.

Covers:
  rom_detector     — detect_rom_format(), check_codename_match()
  rom_unpacker     — unpack_rom()
  source_image_collector — collect_source_images()
  super_input_collector  — collect_super_inputs()
  final_image_assembler  — assemble_final_images(), write_intake_report()
  cleanup_workspace      — cleanup() removes super_parts / super_workspace
  safety rules           — unknown format fails, codename mismatch fails
"""
import io
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.input.rom_detector import (
    FORMAT_FASTBOOT_TAR,
    FORMAT_FASTBOOT_TGZ,
    FORMAT_IMAGES_ZIP,
    FORMAT_NEW_DAT_BR_ZIP,
    FORMAT_PAYLOAD_OTA,
    FORMAT_RAW_SUPER_ZIP,
    FORMAT_SPLIT_SUPER_ZIP,
    FORMAT_UNKNOWN,
    FORMAT_XIAOMI_EU_ZIP,
    detect_rom_format,
    check_codename_match,
)
from factory.input.rom_unpacker import unpack_rom
from factory.images.source_image_collector import (
    DYNAMIC_PARTITION_IMAGES,
    collect_source_images,
)
from factory.super.super_input_collector import collect_super_inputs
from factory.images.final_image_assembler import (
    assemble_final_images,
    write_intake_report,
)
from factory.cleanup.cleanup_workspace import cleanup


# ── Archive construction helpers ──────────────────────────────────────────────

def _make_zip(path: Path, members: dict[str, bytes]) -> Path:
    """Write a ZIP file at path with given {member_name: content} dict."""
    with zipfile.ZipFile(str(path), "w") as zf:
        for name, content in members.items():
            zf.writestr(name, content)
    return path


def _make_tgz(path: Path, members: dict[str, bytes]) -> Path:
    """Write a .tgz file at path with given {member_name: content} dict."""
    with tarfile.open(str(path), "w:gz") as tf:
        for name, content in members.items():
            info = tarfile.TarInfo(name=name)
            info.size = len(content)
            tf.addfile(info, io.BytesIO(content))
    return path


def _make_tar(path: Path, members: dict[str, bytes]) -> Path:
    """Write a plain .tar file at path."""
    with tarfile.open(str(path), "w") as tf:
        for name, content in members.items():
            info = tarfile.TarInfo(name=name)
            info.size = len(content)
            tf.addfile(info, io.BytesIO(content))
    return path


def _write(path: Path, content: bytes = b"fake_img_data") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


# ═══════════════════════════════════════════════════════════════════
# 1. ROM FORMAT DETECTION
# ═══════════════════════════════════════════════════════════════════

class TestDetectPayloadOtaZip:
    def test_zip_with_payload_bin(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "ota.zip",
                {"payload.bin": b"OTA", "payload_properties.txt": b""},
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_PAYLOAD_OTA
        assert result.has_payload_bin is True
        assert result.confidence == 1.0

    def test_payload_inside_subdirectory(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "nested.zip",
                {"META-INF/com/android/otacert": b"cert", "payload.bin": b"OTA"},
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_PAYLOAD_OTA


class TestDetectFastbootTgz:
    def test_tgz_with_images_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_tgz(
                Path(tmp) / "fastboot.tgz",
                {
                    "images/boot.img": b"boot",
                    "images/vendor_boot.img": b"vboot",
                    "images/vbmeta.img": b"vbmeta",
                    "images/dtbo.img": b"dtbo",
                },
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_FASTBOOT_TGZ
        assert result.has_images_dir is True

    def test_tar_gz_extension_gives_tgz_archive_type(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_tgz(
                Path(tmp) / "rom.tar.gz",
                {"images/boot.img": b"x", "images/vbmeta.img": b"x"},
            )
            result = detect_rom_format(rom)
        assert result.archive_type == "tgz"

    def test_plain_tar_gives_fastboot_tar(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_tar(
                Path(tmp) / "rom.tar",
                {"images/boot.img": b"x", "images/vendor.img": b"x",
                 "images/system.img": b"x"},
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_FASTBOOT_TAR


class TestDetectImagesZip:
    def test_zip_with_images_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "rom.zip",
                {
                    "images/boot.img": b"boot",
                    "images/vendor_boot.img": b"vb",
                    "images/vbmeta.img": b"vm",
                },
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_IMAGES_ZIP
        assert result.has_images_dir is True

    def test_zip_with_firmware_update_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "fw.zip",
                {"firmware-update/boot.img": b"x", "firmware-update/modem.img": b"x",
                 "firmware-update/tz.img": b"x"},
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_IMAGES_ZIP


class TestDetectSplitSuperZip:
    def test_zip_with_split_super_parts(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "eu.zip",
                {
                    "super.img.0": b"A" * 16,
                    "super.img.1": b"B" * 16,
                    "super.img.2": b"C" * 16,
                    "boot.img": b"boot",
                },
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_SPLIT_SUPER_ZIP
        assert result.has_split_super is True

    def test_tgz_with_split_super_parts(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_tgz(
                Path(tmp) / "rom.tgz",
                {"super.img.0": b"A", "super.img.1": b"B"},
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_SPLIT_SUPER_ZIP

    def test_single_split_part_not_enough(self):
        """One part alone must not classify as split_super."""
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "one.zip",
                {"super.img.0": b"A", "boot.img": b"b", "vbmeta.img": b"v"},
            )
            result = detect_rom_format(rom)
        assert result.rom_format != FORMAT_SPLIT_SUPER_ZIP


class TestDetectNewDatBrZip:
    def test_zip_with_new_dat_br_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "rom.zip",
                {
                    "system.new.dat.br": b"br",
                    "vendor.new.dat.br": b"br",
                    "system.transfer.list": b"4\n0\n0\n",
                },
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_NEW_DAT_BR_ZIP
        assert result.has_new_dat_br is True


class TestDetectXiaomiEuZip:
    def test_eu_zip_with_super_img(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "xiaomi.eu_multilang_garnet.zip",
                {
                    "META-INF/com/miui/update-binary": b"eu_script",
                    "super.img": b"super_data",
                    "boot.img": b"boot",
                },
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_XIAOMI_EU_ZIP


class TestDetectUnknownFormat:
    def test_unknown_returns_unknown_format(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "random.zip",
                {"readme.txt": b"nothing useful", "changelog.txt": b"changes"},
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_UNKNOWN
        assert result.confidence == 0.0

    def test_nonexistent_file_returns_unknown(self):
        result = detect_rom_format(Path("/nonexistent/path/rom.zip"))
        assert result.rom_format == FORMAT_UNKNOWN
        assert result.errors

    def test_not_a_file_returns_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = detect_rom_format(Path(tmp))  # directory, not file
        assert result.rom_format == FORMAT_UNKNOWN
        assert result.errors


# ═══════════════════════════════════════════════════════════════════
# 2. ROM UNPACKING
# ═══════════════════════════════════════════════════════════════════

class TestUnpackPayloadOta:
    def test_payload_ota_zip_extracts_payload(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "ota.zip",
                {"payload.bin": b"OTA_PAYLOAD", "payload_properties.txt": b"prop=1"},
            )
            work_dir = Path(tmp) / "work"
            result = unpack_rom(rom, FORMAT_PAYLOAD_OTA, work_dir)
            assert result["status"] == "OK"
            payload = list((work_dir / "unpacked_rom").rglob("payload.bin"))
            assert payload, "payload.bin must be extracted to unpacked_rom/"


class TestUnpackSplitSuperZip:
    def test_split_super_parts_are_merged(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "eu.zip",
                {
                    "super.img.0": b"AAAA",
                    "super.img.1": b"BBBB",
                    "super.img.2": b"CCCC",
                    "boot.img": b"boot_data",
                },
            )
            work_dir = Path(tmp) / "work"
            result = unpack_rom(rom, FORMAT_SPLIT_SUPER_ZIP, work_dir)
            assert result["status"] == "OK"
            assert result["split_super_merged"] is True
            merged = Path(result["split_super_path"])
            assert merged.is_file()
            assert merged.read_bytes() == b"AAAABBBBCCCC"
            # super.img must appear in source_images/
            assert (work_dir / "source_images" / "super.img").is_file()


class TestUnpackUnknownFormat:
    def test_unknown_format_fails_safely(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(Path(tmp) / "rom.zip", {"readme.txt": b"hi"})
            work_dir = Path(tmp) / "work"
            result = unpack_rom(rom, FORMAT_UNKNOWN, work_dir)
        assert result["status"] == "UNSUPPORTED"
        assert result["errors"]


# ═══════════════════════════════════════════════════════════════════
# 3. SOURCE IMAGE COLLECTION
# ═══════════════════════════════════════════════════════════════════

class TestCollectNormalImages:
    def test_standalone_images_collected(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "rom_images"
            for name in ["boot.img", "init_boot.img", "vendor_boot.img",
                         "vbmeta.img", "dtbo.img", "logo.img"]:
                _write(src / name)
            out = Path(tmp) / "output" / "images" / "source"
            result = collect_source_images([src], out, execute=False)

        assert "boot.img" in result["standalone_images"]
        assert "vbmeta.img" in result["standalone_images"]
        assert result["missing_required"] == []

    def test_dynamic_images_classified_separately(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "rom_images"
            for name in ["boot.img", "vendor_boot.img", "vbmeta.img",
                         "system.img", "vendor.img", "product.img"]:
                _write(src / name)
            out = Path(tmp) / "output" / "source"
            result = collect_source_images([src], out, execute=False)

        assert "system.img" in result["dynamic_images"]
        assert "vendor.img" in result["dynamic_images"]
        assert "product.img" in result["dynamic_images"]
        # Dynamic images must NOT appear in standalone set
        assert "system.img" not in result["standalone_images"]
        assert "vendor.img" not in result["standalone_images"]

    def test_missing_required_reported_as_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "rom_images"
            _write(src / "dtbo.img")  # only dtbo, missing boot chain
            out = Path(tmp) / "output" / "source"
            result = collect_source_images([src], out, execute=False)

        assert result["missing_required"]
        assert any("boot.img" in w for w in result["warnings"])


# ═══════════════════════════════════════════════════════════════════
# 4. SUPER INPUT COLLECTION
# ═══════════════════════════════════════════════════════════════════

class TestCollectSuperInputs:
    def test_dynamic_images_collected(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "source"
            for name in ["system.img", "vendor.img", "product.img", "odm.img"]:
                _write(src / name)
            parts_dir = Path(tmp) / "super_parts"
            reports_dir = Path(tmp) / "reports"
            result = collect_super_inputs([src], parts_dir, reports_dir, execute=False)

        assert "system" in result["found_dynamic_partitions"]
        assert "vendor" in result["found_dynamic_partitions"]
        assert "product" in result["found_dynamic_partitions"]

    def test_vab_b_zero_size_placeholder_accepted(self):
        """_b slot with 0 bytes must be accepted as a valid VAB placeholder."""
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "source"
            _write(src / "system_a.img", b"system_data")
            _write(src / "system_b.img", b"")  # 0-byte _b placeholder
            _write(src / "vendor_a.img", b"vendor_data")
            _write(src / "vendor_b.img", b"")
            parts_dir = Path(tmp) / "super_parts"
            reports_dir = Path(tmp) / "reports"
            result = collect_super_inputs([src], parts_dir, reports_dir, execute=False)

        assert "system" in result["found_dynamic_partitions"]
        assert "vendor" in result["found_dynamic_partitions"]
        # _b placeholders must be captured
        assert "system" in result["vab_b_placeholders"]
        assert "vendor" in result["vab_b_placeholders"]
        # No errors for zero-size _b slots
        assert not result["errors"]

    def test_report_is_written(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "source"
            _write(src / "system.img")
            parts_dir = Path(tmp) / "super_parts"
            reports_dir = Path(tmp) / "reports"
            collect_super_inputs([src], parts_dir, reports_dir, execute=False)
            assert (reports_dir / "super_input_report.txt").is_file()


# ═══════════════════════════════════════════════════════════════════
# 5. FINAL IMAGE ASSEMBLY
# ═══════════════════════════════════════════════════════════════════

class TestFinalImageAssembler:
    def test_dynamic_images_excluded_from_final(self):
        """system/product/vendor/mi_ext must not appear as standalone files."""
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "source_images"
            # Mix of standalone and dynamic images in source dir
            for name in ["boot.img", "vendor_boot.img", "vbmeta.img",
                         "system.img", "vendor.img", "product.img",
                         "mi_ext.img", "odm.img"]:
                _write(source_dir / name)
            # Create a fake super.img
            super_img = Path(tmp) / "work" / "super.img"
            _write(super_img, b"SPARSE_SUPER")

            final_dir = Path(tmp) / "output" / "images" / "final"
            result = assemble_final_images(
                super_img=super_img,
                source_images_dir=source_dir,
                final_dir=final_dir,
                execute=True,
            )

            assert result["status"] == "APPLIED"
            final_names = {p.name.lower() for p in final_dir.glob("*.img")}

            # super.img must be present
            assert "super.img" in final_names

            # Dynamic partition images must NOT be present as standalone files
            for forbidden in ["system.img", "vendor.img", "product.img",
                              "mi_ext.img", "odm.img"]:
                assert forbidden not in final_names, (
                    f"{forbidden} must not appear as standalone file in final ZIP"
                )

            # Boot chain images must be present
            assert "boot.img" in final_names
            assert "vendor_boot.img" in final_names
            assert "vbmeta.img" in final_names

    def test_excluded_dynamic_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "source_images"
            _write(source_dir / "system.img")
            _write(source_dir / "vendor.img")
            super_img = Path(tmp) / "super.img"
            _write(super_img)
            final_dir = Path(tmp) / "final"
            result = assemble_final_images(super_img, source_dir, final_dir, execute=True)

        assert "system.img" in result["excluded_dynamic"] or "System.img" in [
            e.lower() for e in result["excluded_dynamic"]
        ] or any("system" in e.lower() for e in result["excluded_dynamic"])

    def test_missing_super_img_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "source_images"
            _write(source_dir / "boot.img")
            super_img = Path(tmp) / "nonexistent_super.img"  # does not exist
            final_dir = Path(tmp) / "final"
            result = assemble_final_images(super_img, source_dir, final_dir, execute=True)

        assert result["status"] == "FAILED"
        assert result["errors"]

    def test_patched_images_override_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "source"
            _write(source_dir / "vbmeta.img", b"original_vbmeta")
            _write(source_dir / "boot.img", b"original_boot")

            patched_vbmeta = Path(tmp) / "patched" / "vbmeta.img"
            _write(patched_vbmeta, b"patched_vbmeta")

            super_img = Path(tmp) / "super.img"
            _write(super_img, b"SUPER")

            final_dir = Path(tmp) / "final"
            result = assemble_final_images(
                super_img=super_img,
                source_images_dir=source_dir,
                final_dir=final_dir,
                patched_images={"vbmeta.img": patched_vbmeta},
                execute=True,
            )

            assert result["status"] == "APPLIED"
            assert (final_dir / "vbmeta.img").read_bytes() == b"patched_vbmeta"


# ═══════════════════════════════════════════════════════════════════
# 6. CLEANUP
# ═══════════════════════════════════════════════════════════════════

class TestCleanupRemovesSuperParts:
    def test_super_parts_removed(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            # Create super_parts and super_workspace
            (out / "work" / "super_parts").mkdir(parents=True)
            (out / "work" / "super_workspace").mkdir(parents=True)
            _write(out / "work" / "super_parts" / "system.img")
            _write(out / "work" / "super_workspace" / "scratch.img")

            result = cleanup(out)

        assert result["status"] == "APPLIED"
        assert not (out / "work" / "super_parts").exists()
        assert not (out / "work" / "super_workspace").exists()

    def test_unpacked_rom_removed(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            (out / "work" / "unpacked_rom").mkdir(parents=True)
            _write(out / "work" / "unpacked_rom" / "payload.bin")
            cleanup(out)
        assert not (out / "work" / "unpacked_rom").exists()

    def test_reports_preserved(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            (out / "reports").mkdir(parents=True)
            _write(out / "reports" / "rom_intake_report.txt", b"report")
            (out / "work" / "super_parts").mkdir(parents=True)
            cleanup(out)
            assert (out / "reports" / "rom_intake_report.txt").is_file()


# ═══════════════════════════════════════════════════════════════════
# 7. SAFETY RULES
# ═══════════════════════════════════════════════════════════════════

class TestCodenameSafety:
    def test_matching_codenames_pass(self):
        ok, msg = check_codename_match("garnet", "garnet")
        assert ok is True

    def test_mismatch_fails_without_force(self):
        ok, msg = check_codename_match("garnet", "zircon", force=False)
        assert ok is False
        assert "mismatch" in msg.lower()

    def test_mismatch_passes_with_force(self):
        ok, msg = check_codename_match("garnet", "zircon", force=True)
        assert ok is True
        assert "FORCED" in msg

    def test_unknown_detected_codename_passes(self):
        """When we can't detect the codename, we should not fail."""
        ok, msg = check_codename_match(None, "garnet", force=False)
        assert ok is True

    def test_case_insensitive_match(self):
        ok, _ = check_codename_match("Garnet", "garnet")
        assert ok is True


# ═══════════════════════════════════════════════════════════════════
# 8. REPORTS
# ═══════════════════════════════════════════════════════════════════

class TestIntakeReportWritten:
    def test_rom_intake_report_created(self):
        with tempfile.TemporaryDirectory() as tmp:
            reports_dir = Path(tmp) / "reports"
            path = write_intake_report(
                reports_dir=reports_dir,
                rom_url_or_path="https://example.com/rom.zip",
                detected_format=FORMAT_PAYLOAD_OTA,
                detected_codename="garnet",
                selected_codename="garnet",
                codename_match=True,
                detected_android_version="14",
                detected_miui_hyper_version="HyperOS 2.0",
                detected_region="Global",
                found_images_count=18,
                found_dynamic_count=9,
                original_super_exists=True,
                split_super_merged=False,
                super_rebuilt=True,
                final_image_list=["super.img", "boot.img", "vbmeta.img"],
                cleanup_status="APPLIED",
            )
            assert path.is_file()
            content = path.read_text(encoding="utf-8")
            assert "garnet" in content
            assert "HyperOS 2.0" in content
            assert "super.img" in content
            assert "APPLIED" in content

    def test_report_shows_mismatch_warning(self):
        with tempfile.TemporaryDirectory() as tmp:
            reports_dir = Path(tmp) / "reports"
            path = write_intake_report(
                reports_dir=reports_dir,
                rom_url_or_path="/path/to/rom.zip",
                detected_format=FORMAT_SPLIT_SUPER_ZIP,
                detected_codename="garnet",
                selected_codename="zircon",
                codename_match=False,
                detected_android_version=None,
                detected_miui_hyper_version=None,
                detected_region=None,
                found_images_count=0,
                found_dynamic_count=0,
                original_super_exists=False,
                split_super_merged=True,
                super_rebuilt=False,
                final_image_list=[],
                cleanup_status="NOT_RUN",
            )
            content = path.read_text(encoding="utf-8")
            assert "MISMATCH" in content


# ═══════════════════════════════════════════════════════════════════
# 9. DYNAMIC vs STANDALONE SEPARATION (end-to-end checks)
# ═══════════════════════════════════════════════════════════════════

class TestDynamicImagesNeverInFinalZip:
    """Verify the invariant that no dynamic partition image appears standalone."""

    _DYNAMIC_NAMES = list(DYNAMIC_PARTITION_IMAGES)

    def test_dynamic_partition_constant_names(self):
        """Sanity-check: DYNAMIC_PARTITION_IMAGES contains expected names."""
        assert "system.img" in DYNAMIC_PARTITION_IMAGES
        assert "vendor.img" in DYNAMIC_PARTITION_IMAGES
        assert "product.img" in DYNAMIC_PARTITION_IMAGES
        assert "mi_ext.img" in DYNAMIC_PARTITION_IMAGES
        # super.img itself is NOT a dynamic partition image
        assert "super.img" not in DYNAMIC_PARTITION_IMAGES

    def test_assemble_never_includes_dynamic_even_if_in_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "source"
            # Put ALL dynamic partition images in source dir
            for name in DYNAMIC_PARTITION_IMAGES:
                _write(source_dir / name)
            _write(source_dir / "boot.img")

            super_img = Path(tmp) / "super.img"
            _write(super_img)
            final_dir = Path(tmp) / "final"

            result = assemble_final_images(super_img, source_dir, final_dir, execute=True)
            assert result["status"] == "APPLIED"

            final_names = {p.name.lower() for p in final_dir.glob("*.img")}
            for dynamic_name in DYNAMIC_PARTITION_IMAGES:
                assert dynamic_name not in final_names, (
                    f"{dynamic_name} must never appear as standalone in final dir"
                )


# ── Runner ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import traceback

    tests = [
        *[m for name, cls in sorted(globals().items()) if isinstance(cls, type)
          for mname, m in sorted(vars(cls).items())
          if mname.startswith("test_") and callable(m)],
    ]

    # Flat runner: collect all test methods from test classes
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
