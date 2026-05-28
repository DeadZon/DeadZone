"""Tests for DeadZone Free edition — registry, routing, and pipeline behaviour.

Covers:
  - Free edition registry exists with correct fields
  - Free edition disables all mod flags
  - Both workflows include free as an option and as the default
  - Unknown ROM format fails before any patching
  - images_zip path creates output/images/final/
  - split_super_zip unpacking produces merged super.img
  - Dynamic partition images are excluded from the final assembled dir
  - Legend/Gaming/EPIC mods are skipped in free (no mod runner invoked)
  - free_build_report.txt and rom_intake_report.txt are created
  - Cleanup removes output/work temp folders
"""
import io
import sys
import tarfile
import tempfile
import zipfile
from pathlib import Path
from unittest.mock import patch

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.input.rom_detector import (
    FORMAT_FASTBOOT_TAR,
    FORMAT_FASTBOOT_TGZ,
    FORMAT_IMAGES_ZIP,
    FORMAT_PAYLOAD_OTA,
    FORMAT_RAW_SUPER_ZIP,
    FORMAT_SPLIT_SUPER_ZIP,
    FORMAT_UNKNOWN,
    detect_rom_format,
)
from factory.input.rom_unpacker import unpack_rom
from factory.images.source_image_collector import DYNAMIC_PARTITION_IMAGES
from factory.images.final_image_assembler import assemble_final_images


# ── Archive helpers ────────────────────────────────────────────────────────────

def _make_zip(path: Path, members: dict) -> Path:
    with zipfile.ZipFile(str(path), "w") as zf:
        for name, content in members.items():
            zf.writestr(name, content)
    return path


def _write(path: Path, content: bytes = b"fake_img_data") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


# ═══════════════════════════════════════════════════════════════════
# 1. REGISTRY
# ═══════════════════════════════════════════════════════════════════

class TestFreeEditionRegistry:
    _FREE_YML = Path(__file__).resolve().parents[1] / "registry" / "editions" / "free.yml"

    def test_free_yml_exists(self):
        assert self._FREE_YML.is_file(), "registry/editions/free.yml must exist"

    def test_free_yml_parses(self):
        data = yaml.safe_load(self._FREE_YML.read_text(encoding="utf-8"))
        assert data is not None

    def test_free_edition_id(self):
        data = yaml.safe_load(self._FREE_YML.read_text(encoding="utf-8"))
        assert data.get("id") == "free"

    def test_free_edition_enabled(self):
        data = yaml.safe_load(self._FREE_YML.read_text(encoding="utf-8"))
        assert data.get("enabled") is True

    def test_free_edition_disables_all_mods(self):
        data = yaml.safe_load(self._FREE_YML.read_text(encoding="utf-8"))
        for flag in [
            "apply_mods",
            "apply_legend_mods",
            "apply_gaming_mods",
            "apply_epic_mods",
            "debloat",
            "patch_apks",
            "patch_jars",
            "patch_smali",
        ]:
            assert data.get(flag) is False, f"registry flag {flag!r} must be False"

    def test_free_edition_uses_universal_intake(self):
        data = yaml.safe_load(self._FREE_YML.read_text(encoding="utf-8"))
        assert data.get("use_universal_intake") is True

    def test_free_edition_keeps_stock(self):
        data = yaml.safe_load(self._FREE_YML.read_text(encoding="utf-8"))
        assert data.get("keep_rom_close_to_stock") is True


# ═══════════════════════════════════════════════════════════════════
# 2. WORKFLOW OPTIONS
# ═══════════════════════════════════════════════════════════════════

class TestFreeWorkflowOption:
    _MTK_YML  = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "deadzone_mtk.yml"
    _SNAP_YML = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "deadzone_snapdragon.yml"

    def _load(self, path: Path) -> dict:
        return yaml.safe_load(path.read_text(encoding="utf-8"))

    def _edition_input(self, data: dict) -> dict:
        # PyYAML parses "on:" as boolean True key
        trigger = data.get("on") or data.get(True)
        return trigger["workflow_dispatch"]["inputs"]["edition"]

    def test_mtk_workflow_has_free_option(self):
        ed = self._edition_input(self._load(self._MTK_YML))
        assert "free" in ed["options"], "MTK workflow must list 'free' as an edition option"

    def test_snapdragon_workflow_has_free_option(self):
        ed = self._edition_input(self._load(self._SNAP_YML))
        assert "free" in ed["options"], "Snapdragon workflow must list 'free' as an edition option"

    def test_mtk_default_edition_is_free(self):
        ed = self._edition_input(self._load(self._MTK_YML))
        assert ed.get("default") == "free", "MTK default edition must be 'free'"

    def test_snapdragon_default_edition_is_free(self):
        ed = self._edition_input(self._load(self._SNAP_YML))
        assert ed.get("default") == "free", "Snapdragon default edition must be 'free'"

    def test_mtk_includes_legend_gaming_epic(self):
        ed = self._edition_input(self._load(self._MTK_YML))
        for opt in ["legend", "gaming", "epic"]:
            assert opt in ed["options"]

    def test_snapdragon_includes_legend_gaming_epic(self):
        ed = self._edition_input(self._load(self._SNAP_YML))
        for opt in ["legend", "gaming", "epic"]:
            assert opt in ed["options"]


# ═══════════════════════════════════════════════════════════════════
# 3. ORCHESTRATOR ROUTING
# ═══════════════════════════════════════════════════════════════════

class TestFreePipelineRouting:
    def test_orchestrator_routes_free_to_free_pipeline(self):
        """run_factory with edition='free' must call run_free_pipeline, not mod runners."""
        import importlib
        called = []

        # Patch free_pipeline so we can verify it's called
        import factory.pipeline.free_pipeline as fp_mod
        original_fn = fp_mod.run_free_pipeline

        def _fake_free(ctx, notifier, soc, source, output_dir, template_zip, pipeline_start):
            called.append("free_pipeline")
            return {
                "final_status": "DRY_RUN",
                "build_id": None,
                "build_name": f"DeadZone_{ctx.codename}_V1",
                "codename": ctx.codename,
                "edition": "free",
                "soc": ctx.soc,
                "final_zip": None,
                "pixeldrain_link": None,
                "telegram_message_id": None,
                "warnings": [],
                "errors": [],
                "stage_reports": {},
                "report_files": {},
            }

        fp_mod.run_free_pipeline = _fake_free
        try:
            from factory.pipeline.orchestrator import run_factory
            result = run_factory(
                codename="garnet",
                edition="free",
                mode="dry_run",
                notify_telegram=False,
            )
            assert "free_pipeline" in called, "orchestrator must delegate to free_pipeline for edition='free'"
        finally:
            fp_mod.run_free_pipeline = original_fn

    def test_orchestrator_does_not_route_legend_to_free_pipeline(self):
        """Legend edition must not call run_free_pipeline."""
        import factory.pipeline.free_pipeline as fp_mod
        called = []
        original_fn = fp_mod.run_free_pipeline

        def _fake_free(*a, **kw):
            called.append("free_pipeline")
            raise AssertionError("run_free_pipeline must NOT be called for legend edition")

        fp_mod.run_free_pipeline = _fake_free
        try:
            from factory.pipeline.orchestrator import run_factory
            # legend edition in dry_run — should not call free pipeline
            result = run_factory(
                codename="garnet",
                edition="legend",
                mode="dry_run",
                notify_telegram=False,
            )
        except AssertionError:
            raise
        except Exception:
            pass  # other failures are OK; we only care free_pipeline was NOT called
        finally:
            fp_mod.run_free_pipeline = original_fn

        assert "free_pipeline" not in called


# ═══════════════════════════════════════════════════════════════════
# 4. UNKNOWN ROM FAILS EARLY (before any patching)
# ═══════════════════════════════════════════════════════════════════

class TestUnknownRomFailsEarly:
    def test_unknown_format_detected_as_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "garbage.zip",
                {"readme.txt": b"nothing useful", "some_file.txt": b"random"},
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_UNKNOWN
        assert result.confidence == 0.0

    def test_unknown_format_unpack_returns_unsupported(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(Path(tmp) / "bad.zip", {"junk.txt": b"junk"})
            work_dir = Path(tmp) / "work"
            result = unpack_rom(rom, FORMAT_UNKNOWN, work_dir)
        assert result["status"] == "UNSUPPORTED"
        assert result["errors"]

    def test_free_pipeline_detect_stage_fails_on_unknown(self):
        """free_pipeline detect stage must fail and populate errors for unknown ROMs."""
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(Path(tmp) / "bad.zip", {"junk.txt": b"junk"})
            output_dir = Path(tmp) / "output"

            ctx = BuildContext(
                codename="garnet",
                edition="free",
                rom_url="https://example.com/bad.zip",
                mode="execute",
                soc="snapdragon",
                rom_path=rom,
                output_dir=output_dir,
            )
            result = run_free_pipeline(
                ctx=ctx,
                notifier=None,
                soc="snapdragon",
                source="test",
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
            )

        assert result["final_status"] == "FAILED"
        assert result["errors"], "errors list must be non-empty for unknown ROM"
        assert not result["stage_reports"].get("unpack_rom") or \
            result["stage_reports"].get("detect_rom", {}).get("status") == "FAILED"


# ═══════════════════════════════════════════════════════════════════
# 5. images_zip PATH CREATES output/images/final/
# ═══════════════════════════════════════════════════════════════════

class TestImagesZipCreatesOutputFinal:
    def test_images_zip_detected_correctly(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "rom.zip",
                {
                    "images/boot.img": b"boot",
                    "images/vendor_boot.img": b"vboot",
                    "images/vbmeta.img": b"vbmeta",
                    "images/dtbo.img": b"dtbo",
                },
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_IMAGES_ZIP

    def test_assemble_creates_final_dir(self):
        """assemble_final_images must create output/images/final/ with super + standalone images."""
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "source_images"
            for name in ["boot.img", "vendor_boot.img", "vbmeta.img", "dtbo.img"]:
                _write(source_dir / name)
            # Dynamic images that must NOT appear in final/
            for name in ["system.img", "vendor.img", "product.img"]:
                _write(source_dir / name)

            super_img = Path(tmp) / "super.img"
            _write(super_img, b"SPARSE_SUPER")
            final_dir = Path(tmp) / "output" / "images" / "final"

            result = assemble_final_images(
                super_img=super_img,
                source_images_dir=source_dir,
                final_dir=final_dir,
                execute=True,
            )

            assert result["status"] == "APPLIED"
            assert final_dir.is_dir()
            final_names = {p.name for p in final_dir.glob("*.img")}
            assert "super.img" in final_names
            assert "boot.img" in final_names
            # Dynamic partitions must be absent
            for forbidden in ["system.img", "vendor.img", "product.img"]:
                assert forbidden not in final_names


# ═══════════════════════════════════════════════════════════════════
# 6. split_super_zip CREATES final super.img
# ═══════════════════════════════════════════════════════════════════

class TestSplitSuperZipCreatesSuperImg:
    def test_split_super_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "eu.zip",
                {"super.img.0": b"AAAA", "super.img.1": b"BBBB", "boot.img": b"boot"},
            )
            result = detect_rom_format(rom)
        assert result.rom_format == FORMAT_SPLIT_SUPER_ZIP
        assert result.has_split_super is True

    def test_split_super_parts_merged_to_super_img(self):
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

    def test_split_super_img_placed_in_source_images(self):
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_zip(
                Path(tmp) / "eu.zip",
                {"super.img.0": b"PART0", "super.img.1": b"PART1"},
            )
            work_dir = Path(tmp) / "work"
            result = unpack_rom(rom, FORMAT_SPLIT_SUPER_ZIP, work_dir)
            # The merged super.img must appear somewhere in work_dir
            merged_path = Path(result["split_super_path"])
            assert merged_path.is_file()


# ═══════════════════════════════════════════════════════════════════
# 7. DYNAMIC PARTITION IMAGES EXCLUDED FROM final/
# ═══════════════════════════════════════════════════════════════════

class TestDynamicPartitionsExcludedFromFree:
    def test_all_dynamic_images_excluded(self):
        """None of the DYNAMIC_PARTITION_IMAGES may appear in the assembled final dir."""
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "source"
            for name in DYNAMIC_PARTITION_IMAGES:
                _write(source_dir / name)
            _write(source_dir / "boot.img")

            super_img = Path(tmp) / "super.img"
            _write(super_img)
            final_dir = Path(tmp) / "final"

            result = assemble_final_images(super_img, source_dir, final_dir, execute=True)
            assert result["status"] == "APPLIED"

            final_names = {p.name for p in final_dir.glob("*.img")}
            for dynamic_name in DYNAMIC_PARTITION_IMAGES:
                assert dynamic_name not in final_names, (
                    f"{dynamic_name} must never appear as standalone in final dir (it belongs inside super.img)"
                )

    def test_dynamic_constant_names_are_correct(self):
        for expected in ["system.img", "vendor.img", "product.img", "mi_ext.img", "odm.img"]:
            assert expected in DYNAMIC_PARTITION_IMAGES
        # super.img itself is NOT a dynamic partition
        assert "super.img" not in DYNAMIC_PARTITION_IMAGES


# ═══════════════════════════════════════════════════════════════════
# 8. LEGEND/GAMING/EPIC MODS SKIPPED IN FREE
# ═══════════════════════════════════════════════════════════════════

class TestModsSkippedInFree:
    def test_free_pipeline_does_not_import_mod_runners(self):
        """run_free_pipeline must not call any edition mod runner."""
        import importlib
        mod_runners_called = []

        # Patch the mod runner modules to detect if they're called
        for mod_name in ["legend", "gaming", "epic"]:
            module_path = f"factory.patch.mods.{mod_name}.runner"
            try:
                mod = importlib.import_module(module_path)
                original = getattr(mod, "run_mod", None)
                if original:
                    def _spy(name=mod_name, *a, **kw):
                        mod_runners_called.append(name)
                        return {"status": "APPLIED"}
                    mod.run_mod = _spy
            except ImportError:
                pass  # module doesn't exist — that's fine, it won't be called

        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="garnet",
                edition="free",
                mode="dry_run",
                soc="snapdragon",
                output_dir=output_dir,
            )
            run_free_pipeline(
                ctx=ctx,
                notifier=None,
                soc="snapdragon",
                source="test",
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
            )

        assert not mod_runners_called, (
            f"Free edition must not call any mod runner. Called: {mod_runners_called}"
        )

    def test_free_build_report_lists_skipped_mods(self):
        """free_build_report.txt must mention all skipped mod categories."""
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="garnet",
                edition="free",
                mode="dry_run",
                soc="snapdragon",
                output_dir=output_dir,
            )
            run_free_pipeline(
                ctx=ctx,
                notifier=None,
                soc="snapdragon",
                source="test",
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
            )

            report_path = output_dir / "reports" / "free_build_report.txt"
            assert report_path.is_file()
            content = report_path.read_text(encoding="utf-8")

        for mod_label in ["Legend", "Gaming", "EPIC"]:
            assert mod_label in content, f"free_build_report.txt must mention {mod_label} as skipped"


# ═══════════════════════════════════════════════════════════════════
# 9. REPORTS CREATED
# ═══════════════════════════════════════════════════════════════════

class TestReportsCreated:
    def test_free_build_report_created_on_dry_run(self):
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="garnet",
                edition="free",
                mode="dry_run",
                soc="snapdragon",
                output_dir=output_dir,
            )
            run_free_pipeline(
                ctx=ctx,
                notifier=None,
                soc="snapdragon",
                source="test",
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
            )
            assert (output_dir / "reports" / "free_build_report.txt").is_file()

    def test_pipeline_report_created_on_dry_run(self):
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="garnet",
                edition="free",
                mode="dry_run",
                soc="snapdragon",
                output_dir=output_dir,
            )
            result = run_free_pipeline(
                ctx=ctx,
                notifier=None,
                soc="snapdragon",
                source="test",
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
            )
            assert (output_dir / "reports" / "deadzone_patch_report.txt").is_file()
            assert (output_dir / "reports" / "pipeline_report.json").is_file()

    def test_free_build_report_contains_device_and_edition(self):
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="garnet",
                edition="free",
                mode="dry_run",
                soc="snapdragon",
                output_dir=output_dir,
            )
            run_free_pipeline(
                ctx=ctx,
                notifier=None,
                soc="snapdragon",
                source="test",
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
            )
            content = (output_dir / "reports" / "free_build_report.txt").read_text(encoding="utf-8")

        assert "garnet" in content
        assert "Free" in content


# ═══════════════════════════════════════════════════════════════════
# 10. CLEANUP REMOVES output/work TEMP FOLDERS
# ═══════════════════════════════════════════════════════════════════

class TestCleanupRemovesTempFolders:
    def test_cleanup_removes_super_parts(self):
        from factory.cleanup.cleanup_workspace import cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            super_parts = out / "work" / "super_parts"
            super_workspace = out / "work" / "super_workspace"
            super_parts.mkdir(parents=True)
            super_workspace.mkdir(parents=True)
            _write(super_parts / "system.img")
            _write(super_workspace / "scratch.img")

            result = cleanup(out)

        assert result["status"] == "APPLIED"
        assert not super_parts.exists()
        assert not super_workspace.exists()

    def test_cleanup_removes_unpacked_rom(self):
        from factory.cleanup.cleanup_workspace import cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            unpacked = out / "work" / "unpacked_rom"
            unpacked.mkdir(parents=True)
            _write(unpacked / "payload.bin")

            cleanup(out)
        assert not unpacked.exists()

    def test_cleanup_removes_source_images_work(self):
        from factory.cleanup.cleanup_workspace import cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            src_images = out / "work" / "source_images"
            src_images.mkdir(parents=True)
            _write(src_images / "boot.img")

            cleanup(out)
        assert not src_images.exists()

    def test_cleanup_preserves_reports(self):
        from factory.cleanup.cleanup_workspace import cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            reports = out / "reports"
            reports.mkdir(parents=True)
            _write(reports / "free_build_report.txt", b"report content")
            (out / "work" / "super_parts").mkdir(parents=True)

            cleanup(out)
            assert (reports / "free_build_report.txt").is_file()


# ═══════════════════════════════════════════════════════════════════
# 11. PAYLOAD OTA SUPPORT IN FREE PIPELINE
# ═══════════════════════════════════════════════════════════════════

def _make_payload_ota_zip(path: Path) -> Path:
    """Write a minimal payload_ota ZIP (fake payload.bin content)."""
    with zipfile.ZipFile(str(path), "w") as zf:
        zf.writestr("payload.bin", b"OTA_FAKE")
        zf.writestr("payload_properties.txt", b"FILE_HASH=abc\n")
    return path


def _dump_ok(output_dir, images):
    """Return a successful dump_payload result, writing fake images to disk."""
    for name in images:
        img = Path(output_dir) / name
        img.parent.mkdir(parents=True, exist_ok=True)
        img.write_bytes(b"fake_img_data")
    return {
        "status": "OK",
        "payload_bin": "payload.bin",
        "output_dir": str(output_dir),
        "dumped_images": images,
        "dumped_count": len(images),
        "tool_used": "payload_extract (internal)",
        "errors": [],
        "warnings": [],
    }


_DUMP_FAIL = {
    "status": "FAILED",
    "payload_bin": "payload.bin",
    "output_dir": "",
    "dumped_images": [],
    "dumped_count": 0,
    "tool_used": "unknown",
    "errors": ["payload.bin was extracted but could not be dumped into images."],
    "warnings": [],
}

# Images that cover both standalone and dynamic partition sets.
_FULL_DUMP_IMAGES = [
    "boot.img", "vendor_boot.img", "vbmeta.img", "dtbo.img",
    "system.img", "product.img", "vendor.img", "mi_ext.img",
    "odm.img", "system_ext.img",
]


class TestPayloadOtaFreePipeline:
    """payload_ota ROM in the Free pipeline must dump before collecting images."""

    def test_payload_ota_calls_dump_payload_in_unpack(self):
        """unpack_rom must invoke dump_payload for payload_ota format."""
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_payload_ota_zip(Path(tmp) / "ota.zip")
            work_dir = Path(tmp) / "work"
            called = []

            def _fake_dump(payload_bin, output_dir, partitions=None):
                called.append(True)
                return _dump_ok(output_dir, ["boot.img"])

            with patch("factory.input.rom_unpacker.dump_payload", side_effect=_fake_dump):
                result = unpack_rom(rom, FORMAT_PAYLOAD_OTA, work_dir)

            assert called, "dump_payload must be called for payload_ota"
            assert result["status"] == "OK"

    def test_payload_dump_fail_stops_pipeline_before_super_rebuilder(self):
        """When payload dump fails the Free pipeline must fail and not reach super_rebuilder."""
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_payload_ota_zip(Path(tmp) / "ota.zip")
            output_dir = Path(tmp) / "output"

            ctx = BuildContext(
                codename="zircon",
                edition="free",
                mode="execute",
                soc="mtk",
                rom_path=rom,
                output_dir=output_dir,
            )

            rebuild_called = []

            def _fake_rebuild(*a, **kw):
                rebuild_called.append(True)
                return {"status": "APPLIED", "warnings": [], "errors": []}

            with (
                patch("factory.input.rom_unpacker.dump_payload", return_value=_DUMP_FAIL),
                patch("factory.super.super_rebuilder.rebuild_super", side_effect=_fake_rebuild),
            ):
                result = run_free_pipeline(
                    ctx=ctx,
                    notifier=None,
                    soc="mtk",
                    source="test",
                    output_dir=output_dir,
                    template_zip=None,
                    pipeline_start=time.monotonic(),
                )

            assert result["final_status"] == "FAILED"
            assert not rebuild_called, "super_rebuilder must NOT run when payload dump fails"

    def test_payload_dump_writes_boot_system_product_vendor_to_source_images(self):
        """After a successful dump, source_images/ must contain the dumped .img files."""
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_payload_ota_zip(Path(tmp) / "ota.zip")
            work_dir = Path(tmp) / "work"

            def _fake_dump(payload_bin, output_dir, partitions=None):
                return _dump_ok(output_dir, _FULL_DUMP_IMAGES)

            with patch("factory.input.rom_unpacker.dump_payload", side_effect=_fake_dump):
                result = unpack_rom(rom, FORMAT_PAYLOAD_OTA, work_dir)

            source_images = work_dir / "source_images"
            assert result["status"] == "OK"
            for name in ["boot.img", "system.img", "product.img", "vendor.img"]:
                assert (source_images / name).is_file(), (
                    f"{name} must be present in source_images/ after payload dump"
                )

    def test_payload_dump_report_written_in_free_pipeline(self):
        """payload_dump_report.txt must be written under output/reports/."""
        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_payload_ota_zip(Path(tmp) / "ota.zip")
            work_dir = Path(tmp) / "work"

            def _fake_dump(payload_bin, output_dir, partitions=None):
                return _dump_ok(output_dir, ["boot.img"])

            with patch("factory.input.rom_unpacker.dump_payload", side_effect=_fake_dump):
                unpack_rom(rom, FORMAT_PAYLOAD_OTA, work_dir)

            report = work_dir.parent / "reports" / "payload_dump_report.txt"
            assert report.is_file(), "payload_dump_report.txt must be written"

    def test_no_zip_packaged_if_payload_dump_fails(self):
        """The final_zip stage must not run if the payload dump failed."""
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_payload_ota_zip(Path(tmp) / "ota.zip")
            output_dir = Path(tmp) / "output"

            ctx = BuildContext(
                codename="zircon",
                edition="free",
                mode="execute",
                soc="mtk",
                rom_path=rom,
                output_dir=output_dir,
            )

            zip_called = []

            def _fake_zip(*a, **kw):
                zip_called.append(True)
                return {"status": "APPLIED", "final_zip": "/fake.zip", "warnings": [], "errors": []}

            with (
                patch("factory.input.rom_unpacker.dump_payload", return_value=_DUMP_FAIL),
                patch("factory.output.final_zip_legacy.build_final_fastboot_zip", side_effect=_fake_zip),
            ):
                result = run_free_pipeline(
                    ctx=ctx,
                    notifier=None,
                    soc="mtk",
                    source="test",
                    output_dir=output_dir,
                    template_zip=None,
                    pipeline_start=time.monotonic(),
                )

            assert result["final_status"] == "FAILED"
            assert not zip_called, "final_zip must NOT be packaged when payload dump fails"

    def test_free_build_report_includes_payload_dump_section(self):
        """free_build_report.txt must mention payload dump status for payload_ota ROMs."""
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            rom = _make_payload_ota_zip(Path(tmp) / "ota.zip")
            output_dir = Path(tmp) / "output"

            ctx = BuildContext(
                codename="zircon",
                edition="free",
                mode="execute",
                soc="mtk",
                rom_path=rom,
                output_dir=output_dir,
            )

            def _fake_dump(payload_bin, output_dir, partitions=None):
                return _dump_ok(output_dir, ["boot.img"])

            # Patch downstream stages so we don't need real images.
            with (
                patch("factory.input.rom_unpacker.dump_payload", side_effect=_fake_dump),
                patch("factory.images.source_image_collector.collect_source_images",
                      return_value={"status": "APPLIED", "standalone_images": {}, "dynamic_images": {}, "missing_required": [], "warnings": [], "errors": []}),
                patch("factory.super.super_input_collector.collect_super_inputs",
                      return_value={"status": "APPLIED", "found_dynamic_partitions": [], "vab_b_placeholders": [], "warnings": [], "errors": []}),
                patch("factory.super.super_rebuilder.rebuild_super",
                      return_value={"status": "APPLIED", "warnings": [], "errors": []}),
                patch("factory.images.final_image_assembler.assemble_final_images",
                      return_value={"status": "APPLIED", "final_images": ["super.img", "boot.img"], "excluded_dynamic": [], "warnings": [], "errors": []}),
            ):
                run_free_pipeline(
                    ctx=ctx,
                    notifier=None,
                    soc="mtk",
                    source="test",
                    output_dir=output_dir,
                    template_zip=None,
                    pipeline_start=time.monotonic(),
                )

            report_path = output_dir / "reports" / "free_build_report.txt"
            assert report_path.is_file()
            content = report_path.read_text(encoding="utf-8")
            assert "Payload Dump" in content, "free_build_report.txt must contain Payload Dump section"
            assert "OK" in content


# ═══════════════════════════════════════════════════════════════════
# 12. ZORN FIX — fastboot TGZ + preserve_original_super
# ═══════════════════════════════════════════════════════════════════

class TestZornFastbootTgzPreserveSuperImg:
    """
    Covers the zorn bug:
      - fastboot TGZ with super.img detected correctly
      - Free edition with original super.img preserves it (no lpmake)
      - preserve_original_super does not require dynamic partitions
      - super_rebuild_report records the correct strategy
    """

    def test_fastboot_tgz_with_super_img_detected_as_fastboot_tgz(self):
        """Zorn ROM (fastboot TGZ with images/super.img) must be fastboot_tgz."""
        import io
        import tarfile as _tarfile

        with tempfile.TemporaryDirectory() as tmp:
            tgz_path = Path(tmp) / "zorn.tgz"
            with _tarfile.open(str(tgz_path), "w:gz") as tf:
                for name, content in {
                    "images/boot.img":        b"boot",
                    "images/vendor_boot.img": b"vb",
                    "images/init_boot.img":   b"ib",
                    "images/vbmeta.img":      b"vm",
                    "images/dtbo.img":        b"dtbo",
                    "images/super.img":       b"SUPER",
                }.items():
                    info = _tarfile.TarInfo(name=name)
                    info.size = len(content)
                    tf.addfile(info, io.BytesIO(content))
            result = detect_rom_format(tgz_path)

        assert result.rom_format == FORMAT_FASTBOOT_TGZ, (
            f"Expected fastboot_tgz but got {result.rom_format!r}. "
            "fastboot TGZ containing super.img must not be raw_super_zip."
        )

    def test_preserve_original_super_does_not_call_lpmake(self):
        """rebuild_super(preserve_original_super=True) must copy the file without calling lpmake."""
        from factory.super.super_rebuilder import rebuild_super

        with tempfile.TemporaryDirectory() as tmp:
            original_super = Path(tmp) / "source_images" / "super.img"
            original_super.parent.mkdir(parents=True)
            original_super.write_bytes(b"ORIGINAL_SUPER_CONTENT")

            super_parts = Path(tmp) / "super_parts"
            super_parts.mkdir()
            # No dynamic partition images in super_parts — this is the zorn scenario

            output_super = Path(tmp) / "final" / "super.img"
            output_super.parent.mkdir(parents=True)
            reports_dir = Path(tmp) / "reports"

            result = rebuild_super(
                super_parts_dir=super_parts,
                output_super=output_super,
                reports_dir=reports_dir,
                original_super_img=original_super,
                execute=True,
                preserve_original_super=True,
            )

            assert result["status"] == "APPLIED", f"Expected APPLIED but got {result['status']}: {result['errors']}"
            assert result["lpmake_executed"] is False, "lpmake must NOT be executed for preserve strategy"
            assert output_super.is_file(), "output super.img must exist after preserve"
            assert output_super.read_bytes() == b"ORIGINAL_SUPER_CONTENT"

    def test_preserve_original_super_does_not_require_dynamic_partitions(self):
        """preserve_original_super must succeed even when super_parts_dir is empty."""
        from factory.super.super_rebuilder import rebuild_super

        with tempfile.TemporaryDirectory() as tmp:
            original_super = Path(tmp) / "super.img"
            original_super.write_bytes(b"STOCK_SUPER")

            super_parts = Path(tmp) / "super_parts"
            super_parts.mkdir()
            # Deliberately empty — no .img files

            result = rebuild_super(
                super_parts_dir=super_parts,
                output_super=Path(tmp) / "final" / "super.img",
                reports_dir=Path(tmp) / "reports",
                original_super_img=original_super,
                execute=True,
                preserve_original_super=True,
            )

        assert result["status"] == "APPLIED"
        assert not result["errors"], f"Unexpected errors: {result['errors']}"

    def test_preserve_original_super_copies_to_final(self):
        """The copied super.img must match the original byte-for-byte."""
        from factory.super.super_rebuilder import rebuild_super

        original_bytes = b"FAKE_SPARSE_SUPER_" + b"\x00" * 64
        with tempfile.TemporaryDirectory() as tmp:
            original_super = Path(tmp) / "super_orig.img"
            original_super.write_bytes(original_bytes)
            output_super = Path(tmp) / "final" / "super.img"
            output_super.parent.mkdir()

            rebuild_super(
                super_parts_dir=Path(tmp) / "parts",
                output_super=output_super,
                reports_dir=Path(tmp) / "reports",
                original_super_img=original_super,
                execute=True,
                preserve_original_super=True,
            )

            assert output_super.read_bytes() == original_bytes

    def test_super_rebuild_report_says_preserve_original_super(self):
        """super_rebuild_report.txt must record strategy=preserve_original_super."""
        from factory.super.super_rebuilder import rebuild_super

        with tempfile.TemporaryDirectory() as tmp:
            original_super = Path(tmp) / "super.img"
            original_super.write_bytes(b"SUPER")
            reports_dir = Path(tmp) / "reports"

            rebuild_super(
                super_parts_dir=Path(tmp) / "parts",
                output_super=Path(tmp) / "final" / "super.img",
                reports_dir=reports_dir,
                original_super_img=original_super,
                execute=True,
                preserve_original_super=True,
            )

            report_path = reports_dir / "super_rebuild_report.txt"
            assert report_path.is_file(), "super_rebuild_report.txt must be written"
            content = report_path.read_text(encoding="utf-8")

        assert "preserve_original_super" in content, (
            "super_rebuild_report.txt must contain 'preserve_original_super' strategy"
        )
        assert "lpmake executed        : False" in content

    def test_free_pipeline_uses_smart_base_engine(self):
        """run_free_pipeline must call run_smart_base_engine with edition='free'."""
        import factory.engine.smart_base_engine as engine_mod

        called_with = []
        original = engine_mod.run_smart_base_engine

        def _spy(context, edition="free", apply_mods=False, force_codename=False, **kw):
            called_with.append({
                "edition": edition,
                "apply_mods": apply_mods,
            })
            return {
                "final_status": "DRY_RUN",
                "build_id": None,
                "build_name": f"DeadZone_{context.codename}_V1",
                "codename": context.codename,
                "edition": edition,
                "soc": context.soc,
                "final_zip": None,
                "pixeldrain_link": None,
                "telegram_message_id": None,
                "warnings": [],
                "errors": [],
                "stage_reports": {},
                "report_files": {},
            }

        engine_mod.run_smart_base_engine = _spy
        try:
            from factory.pipeline.free_pipeline import run_free_pipeline
            from factory.pipeline.context import BuildContext
            import time

            with tempfile.TemporaryDirectory() as tmp:
                output_dir = Path(tmp) / "output"
                ctx = BuildContext(
                    codename="zorn",
                    edition="free",
                    mode="dry_run",
                    soc="snapdragon",
                    output_dir=output_dir,
                )
                run_free_pipeline(
                    ctx=ctx,
                    notifier=None,
                    soc="snapdragon",
                    source="test",
                    output_dir=output_dir,
                    template_zip=None,
                    pipeline_start=time.monotonic(),
                )
        finally:
            engine_mod.run_smart_base_engine = original

        assert called_with, "run_smart_base_engine must be called by run_free_pipeline"
        assert called_with[0]["edition"] == "free"
        assert called_with[0]["apply_mods"] is False, (
            "Free pipeline must pass apply_mods=False to the smart engine"
        )

    def test_free_pipeline_passes_apply_mods_false(self):
        """run_free_pipeline must always pass apply_mods=False to smart engine."""
        import factory.engine.smart_base_engine as engine_mod

        apply_mods_values = []
        original = engine_mod.run_smart_base_engine

        def _spy(context, edition="free", apply_mods=False, **kw):
            apply_mods_values.append(apply_mods)
            return {
                "final_status": "DRY_RUN", "build_id": None,
                "build_name": f"DZ_{context.codename}",
                "codename": context.codename, "edition": edition,
                "soc": context.soc, "final_zip": None,
                "pixeldrain_link": None, "telegram_message_id": None,
                "warnings": [], "errors": [],
                "stage_reports": {}, "report_files": {},
            }

        engine_mod.run_smart_base_engine = _spy
        try:
            from factory.pipeline.free_pipeline import run_free_pipeline
            from factory.pipeline.context import BuildContext
            import time

            with tempfile.TemporaryDirectory() as tmp:
                ctx = BuildContext(
                    codename="zorn", edition="free", mode="dry_run",
                    soc="snapdragon", output_dir=Path(tmp) / "output",
                )
                run_free_pipeline(ctx=ctx, notifier=None, soc="snapdragon",
                                  source="test", output_dir=Path(tmp) / "output",
                                  template_zip=None, pipeline_start=time.monotonic())
        finally:
            engine_mod.run_smart_base_engine = original

        assert apply_mods_values, "run_smart_base_engine was not called"
        assert all(v is False for v in apply_mods_values), (
            f"apply_mods must always be False for Free, got: {apply_mods_values}"
        )


# ═══════════════════════════════════════════════════════════════════
# 13. WORKFLOW CONCURRENCY & TIMEOUT GUARDS
# ═══════════════════════════════════════════════════════════════════

class TestWorkflowConcurrencyAndTimeout:
    """Workflow files must include concurrency group and ≤120min timeout."""

    _MTK  = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "deadzone_mtk.yml"
    _SNAP = Path(__file__).resolve().parents[1] / ".github" / "workflows" / "deadzone_snapdragon.yml"

    def _text(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")

    def test_mtk_workflow_has_concurrency(self):
        assert "concurrency:" in self._text(self._MTK), \
            "deadzone_mtk.yml must define a concurrency group"

    def test_snapdragon_workflow_has_concurrency(self):
        assert "concurrency:" in self._text(self._SNAP), \
            "deadzone_snapdragon.yml must define a concurrency group"

    def test_mtk_workflow_timeout_at_most_120(self):
        import re
        text = self._text(self._MTK)
        m = re.search(r"timeout-minutes:\s*(\d+)", text)
        assert m, "deadzone_mtk.yml must define timeout-minutes"
        assert int(m.group(1)) <= 120, (
            f"timeout-minutes must be ≤120 but found {m.group(1)}"
        )

    def test_snapdragon_workflow_timeout_at_most_120(self):
        import re
        text = self._text(self._SNAP)
        m = re.search(r"timeout-minutes:\s*(\d+)", text)
        assert m, "deadzone_snapdragon.yml must define timeout-minutes"
        assert int(m.group(1)) <= 120, (
            f"timeout-minutes must be ≤120 but found {m.group(1)}"
        )

    def test_mtk_workflow_sets_deadzone_fast_mode(self):
        assert "DEADZONE_FAST_MODE" in self._text(self._MTK), \
            "deadzone_mtk.yml execute step must set DEADZONE_FAST_MODE"

    def test_snapdragon_workflow_sets_deadzone_fast_mode(self):
        assert "DEADZONE_FAST_MODE" in self._text(self._SNAP), \
            "deadzone_snapdragon.yml execute step must set DEADZONE_FAST_MODE"

    def test_mtk_workflow_sets_deadzone_zip_level(self):
        assert "DEADZONE_ZIP_LEVEL" in self._text(self._MTK), \
            "deadzone_mtk.yml execute step must set DEADZONE_ZIP_LEVEL"

    def test_snapdragon_workflow_sets_deadzone_zip_level(self):
        assert "DEADZONE_ZIP_LEVEL" in self._text(self._SNAP), \
            "deadzone_snapdragon.yml execute step must set DEADZONE_ZIP_LEVEL"


# ═══════════════════════════════════════════════════════════════════
# 14. PREFLIGHT CLEANUP
# ═══════════════════════════════════════════════════════════════════

class TestPreflightCleanup:
    def test_preflight_cleanup_removes_work(self):
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            work = out / "work"
            work.mkdir(parents=True)
            (work / "source_images").mkdir()
            (work / "source_images" / "super.img").write_bytes(b"old")

            preflight_cleanup(out)
        assert not work.exists()

    def test_preflight_cleanup_removes_images_final(self):
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            img_final = out / "images" / "final"
            img_final.mkdir(parents=True)
            (img_final / "super.img").write_bytes(b"old_super")

            preflight_cleanup(out)
        assert not img_final.exists()

    def test_preflight_cleanup_removes_input_roms(self):
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            out.mkdir()
            input_roms = Path(tmp) / "_input_roms"
            input_roms.mkdir()
            (input_roms / "source_rom.tgz").write_bytes(b"big_rom")

            preflight_cleanup(out, project_root=Path(tmp))
        assert not input_roms.exists()

    def test_preflight_cleanup_preserves_reports(self):
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            reports = out / "reports"
            reports.mkdir(parents=True)
            report_file = reports / "previous_build_report.txt"
            report_file.write_bytes(b"old report")
            (out / "work").mkdir()

            preflight_cleanup(out)
            assert report_file.is_file(), "output/reports/ must be preserved by preflight_cleanup"

    def test_preflight_cleanup_writes_report(self):
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            out.mkdir()
            preflight_cleanup(out)
            assert (out / "reports" / "preflight_cleanup_report.txt").is_file()

    def test_preflight_cleanup_returns_status_applied(self):
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            result = preflight_cleanup(Path(tmp) / "output")
        assert result["status"] == "APPLIED"


# ═══════════════════════════════════════════════════════════════════
# 15. RUNTIME GUARD — stage timeout config exists
# ═══════════════════════════════════════════════════════════════════

class TestRuntimeGuardConfig:
    def test_stage_timeout_config_exists(self):
        from factory.pipeline.legacy_engine_runner import STAGE_TIMEOUTS_MINUTES
        assert isinstance(STAGE_TIMEOUTS_MINUTES, dict)
        assert len(STAGE_TIMEOUTS_MINUTES) > 0
        for stage, minutes in STAGE_TIMEOUTS_MINUTES.items():
            assert isinstance(minutes, int) and minutes > 0, (
                f"Timeout for {stage!r} must be a positive int, got {minutes}"
            )

    def test_required_stages_have_timeouts(self):
        from factory.pipeline.legacy_engine_runner import STAGE_TIMEOUTS_MINUTES
        for required in ["detect_rom", "unpack_rom", "super_rebuild", "final_zip"]:
            assert required in STAGE_TIMEOUTS_MINUTES, (
                f"Stage {required!r} must have a timeout configured"
            )

    def test_runtime_guard_report_written_on_dry_run(self):
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="zorn",
                edition="free",
                mode="dry_run",
                soc="snapdragon",
                output_dir=output_dir,
            )
            run_free_pipeline(
                ctx=ctx,
                notifier=None,
                soc="snapdragon",
                source="test",
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
            )
            assert (output_dir / "reports" / "runtime_guard_report.txt").is_file(), (
                "runtime_guard_report.txt must be written after every pipeline run"
            )


# ═══════════════════════════════════════════════════════════════════
# 16. CLEANUP ORDER — ROM PRESERVED WHEN DOWNLOADED BEFORE PIPELINE
# ═══════════════════════════════════════════════════════════════════

class TestCleanupOrderPreservesDownloadedRom:
    """
    Covers the zorn bug: preflight_cleanup deleted _input_roms/ after the
    workflow had already downloaded the ROM there, so detect_rom received a
    missing file and reported FORMAT_UNKNOWN / "file not found".

    Fix: free_pipeline passes preserve_paths=[ctx.rom_path] to preflight_cleanup
    so that _input_roms/ is kept when the active ROM lives there.
    """

    def test_preflight_cleanup_before_download_deletes_input_roms(self):
        """Without preserve_paths, preflight_cleanup removes _input_roms/ (pre-download case)."""
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            out.mkdir()
            input_roms = Path(tmp) / "_input_roms"
            input_roms.mkdir()
            (input_roms / "old_rom.tgz").write_bytes(b"stale")

            result = preflight_cleanup(out, project_root=Path(tmp))

        assert not input_roms.exists(), "_input_roms must be deleted in pre-download mode"
        assert result["input_roms_preserved"] is False
        assert result["cleanup_phase"] == "pre_download"

    def test_preflight_cleanup_after_download_preserves_active_rom_path(self):
        """When preserve_paths contains a path inside _input_roms/, that dir is kept."""
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            out.mkdir()
            input_roms = Path(tmp) / "_input_roms"
            input_roms.mkdir()
            rom_file = input_roms / "source_rom.tgz"
            rom_file.write_bytes(b"big_rom_data")

            result = preflight_cleanup(
                out,
                project_root=Path(tmp),
                preserve_paths=[rom_file],
            )

            assert input_roms.exists(), "_input_roms must be preserved when ROM is inside it"
            assert rom_file.is_file(), "active ROM file must still exist after cleanup"
            assert result["input_roms_preserved"] is True
            assert result["cleanup_phase"] == "post_download"

    def test_preflight_cleanup_report_shows_preserved_active_rom_path(self):
        """preflight_cleanup_report.txt must record the active ROM path and preservation status."""
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            out.mkdir()
            input_roms = Path(tmp) / "_input_roms"
            input_roms.mkdir()
            rom_file = input_roms / "source_rom.tgz"
            rom_file.write_bytes(b"data")

            preflight_cleanup(out, project_root=Path(tmp), preserve_paths=[rom_file])

            report = (out / "reports" / "preflight_cleanup_report.txt").read_text(encoding="utf-8")

        assert "source_rom.tgz" in report, "report must include active ROM path"
        assert "_input_roms preserved: True" in report
        assert "post_download" in report

    def test_detect_rom_fails_with_clear_error_when_rom_path_missing(self):
        """legacy_engine detect stage must fail with a clear message when ROM file is gone."""
        from factory.pipeline.context import BuildContext
        from factory.pipeline.legacy_engine_runner import run_legacy_engine
        import time

        with tempfile.TemporaryDirectory() as tmp:
            missing_rom = Path(tmp) / "_input_roms" / "source_rom.tgz"
            # Deliberately do NOT create the file — simulate cleanup having deleted it
            output_dir = Path(tmp) / "output"

            ctx = BuildContext(
                codename="zorn",
                edition="free",
                mode="execute",
                soc="snapdragon",
                rom_path=missing_rom,
                output_dir=output_dir,
            )

            result = run_legacy_engine(
                context=ctx,
                notifier=None,
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
                edition="free",
                apply_mods=False,
            )

        assert result["final_status"] == "FAILED"
        errors_text = " ".join(result["errors"])
        assert "missing after cleanup" in errors_text or "Cleanup must run before" in errors_text, (
            f"Error must explain the cleanup ordering problem. Got: {errors_text}"
        )

    def test_free_pipeline_does_not_call_detect_rom_after_deleting_input_rom(self):
        """run_free_pipeline must not delete the input ROM before analysis.

        Simulates the zorn failure: ROM downloaded to _input_roms/ before the pipeline
        starts.  Smart Base Engine must preserve the ROM so analyze_rom sees it.
        """
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import factory.input.universal_rom_intake as _intake_mod
        import time

        with tempfile.TemporaryDirectory() as tmp:
            # Simulate workflow: ROM already downloaded
            input_roms = Path(tmp) / "_input_roms"
            input_roms.mkdir()
            rom_file = input_roms / "source_rom.tgz"
            import tarfile as _tarfile
            import io as _io
            with _tarfile.open(str(rom_file), "w:gz") as tf:
                for name, content in {
                    "images/boot.img": b"boot",
                    "images/vbmeta.img": b"vm",
                    "images/dtbo.img": b"dtbo",
                }.items():
                    info = _tarfile.TarInfo(name=name)
                    info.size = len(content)
                    tf.addfile(info, _io.BytesIO(content))

            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="zorn",
                edition="free",
                mode="execute",
                soc="snapdragon",
                rom_path=rom_file,
                output_dir=output_dir,
            )

            # Spy on analyze_rom — the smart engine's detection entry point.
            # Verify the ROM file still exists when analysis is invoked, proving
            # that preflight_cleanup did NOT delete _input_roms/ before detection.
            analyze_called_with_existing_file: list[bool] = []
            _orig_analyze = _intake_mod.analyze_rom

            def _spy_analyze(rom_path, **kw):
                analyze_called_with_existing_file.append(Path(rom_path).exists())
                return _orig_analyze(rom_path, **kw)

            _intake_mod.analyze_rom = _spy_analyze
            try:
                run_free_pipeline(
                    ctx=ctx,
                    notifier=None,
                    soc="snapdragon",
                    source="test",
                    output_dir=output_dir,
                    template_zip=None,
                    pipeline_start=time.monotonic(),
                )
            finally:
                _intake_mod.analyze_rom = _orig_analyze

        assert analyze_called_with_existing_file, "analyze_rom must have been called"
        assert analyze_called_with_existing_file[0] is True, (
            "ROM file must exist when analyze_rom is called. "
            "preflight_cleanup must not have deleted _input_roms/ before detection."
        )

    def test_zorn_fastboot_tgz_path_exists_before_detect(self):
        """Simulate the exact zorn failure: ROM in _input_roms, pipeline preserves it."""
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            # Workflow step: download ROM to _input_roms/
            input_roms = Path(tmp) / "_input_roms"
            input_roms.mkdir()
            rom_file = input_roms / "source_rom.tgz"
            rom_file.write_bytes(b"zorn_fastboot_tgz_content")

            # Stale leftovers from a previous build that cleanup SHOULD delete
            out = Path(tmp) / "output"
            (out / "work" / "source_images").mkdir(parents=True)
            (out / "work" / "source_images" / "old_boot.img").write_bytes(b"old")

            # Run preflight_cleanup with the active ROM preserved
            result = preflight_cleanup(out, project_root=Path(tmp), preserve_paths=[rom_file])

            # ROM must survive
            assert rom_file.is_file(), "zorn ROM must exist after preflight_cleanup"
            # Stale work/ must be gone
            assert not (out / "work").exists(), "stale work/ must be removed"
            # Report must be clear
            assert result["input_roms_preserved"] is True

    def test_runtime_guard_report_contains_rom_integrity_fields(self):
        """runtime_guard_report.txt must include ROM integrity check fields."""
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="zorn",
                edition="free",
                mode="dry_run",
                soc="snapdragon",
                output_dir=output_dir,
            )
            run_free_pipeline(
                ctx=ctx,
                notifier=None,
                soc="snapdragon",
                source="test",
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
            )

            report = (output_dir / "reports" / "runtime_guard_report.txt").read_text(
                encoding="utf-8"
            )

        assert "cleanup ran before download" in report
        assert "input ROM exists before detect" in report
        assert "input ROM path" in report

    def test_free_engine_report_contains_input_rom_fields(self):
        """free_engine_report.txt must include Input ROM path and exists fields."""
        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="zorn",
                edition="free",
                mode="dry_run",
                soc="snapdragon",
                output_dir=output_dir,
            )
            run_free_pipeline(
                ctx=ctx,
                notifier=None,
                soc="snapdragon",
                source="test",
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
            )

            report = (output_dir / "reports" / "free_engine_report.txt").read_text(
                encoding="utf-8"
            )

        assert "Input ROM path" in report
        assert "Input ROM exists" in report

    def test_workflow_cleanup_before_download_does_not_need_preserve(self):
        """If cleanup ran before the download, no preserve_paths needed — _input_roms is empty."""
        from factory.cleanup.preflight_cleanup import preflight_cleanup

        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "output"
            out.mkdir()
            # _input_roms does NOT exist yet — this is pre-download
            result = preflight_cleanup(out, project_root=Path(tmp))

        assert result["status"] == "APPLIED"
        assert result["input_roms_preserved"] is False
        assert result["cleanup_phase"] == "pre_download"


# ═══════════════════════════════════════════════════════════════════
# 17. SAME-FILE SUPER.IMG COPY — preserve_original_super path
# ═══════════════════════════════════════════════════════════════════

class TestSameFileSuperCopy:
    """
    Covers the zorn bug where preserve_original_super placed super.img in
    output/images/final/ and then assemble_final_images tried to copy the
    same file onto itself, raising "are the same file".
    """

    def test_same_file_copy_is_skipped_not_failed(self):
        """assemble_final_images must skip same-file super.img copy without error."""
        with tempfile.TemporaryDirectory() as tmp:
            final_dir = Path(tmp) / "output" / "images" / "final"
            final_dir.mkdir(parents=True)
            # Simulate preserve_original_super: super.img already in final_dir
            super_img = final_dir / "super.img"
            super_img.write_bytes(b"PRESERVED_SUPER")

            source_dir = Path(tmp) / "source_images"
            _write(source_dir / "boot.img")

            result = assemble_final_images(
                super_img=super_img,
                source_images_dir=source_dir,
                final_dir=final_dir,
                execute=True,
            )

        assert result["status"] == "APPLIED", (
            f"Same-file copy must be treated as APPLIED, not FAILED. Got: {result['status']}\n"
            f"Errors: {result.get('errors')}"
        )
        assert not result["errors"], f"No errors expected for same-file skip: {result['errors']}"
        any_same_file_warn = any("same-file" in w.lower() or "skipping" in w.lower() for w in result.get("warnings", []))
        assert any_same_file_warn, (
            "A warning about skipping same-file copy must appear in warnings"
        )

    def test_same_file_copy_super_img_still_in_final_manifest(self):
        """After a same-file skip, super.img must appear in final_manifest."""
        with tempfile.TemporaryDirectory() as tmp:
            final_dir = Path(tmp) / "final"
            final_dir.mkdir()
            super_img = final_dir / "super.img"
            super_img.write_bytes(b"SUPER")

            result = assemble_final_images(
                super_img=super_img,
                source_images_dir=Path(tmp) / "source",
                final_dir=final_dir,
                execute=True,
            )

        assert "super.img" in (result.get("final_manifest") or []), (
            "super.img must appear in final_manifest after same-file skip"
        )
        assert "super.img" in (result.get("final_images") or []), (
            "super.img must appear in final_images after same-file skip"
        )

    def test_same_file_copy_warning_not_error(self):
        """Same-file copy must produce a warning, not an error."""
        with tempfile.TemporaryDirectory() as tmp:
            final_dir = Path(tmp) / "final"
            final_dir.mkdir()
            super_img = final_dir / "super.img"
            super_img.write_bytes(b"SUPER")

            result = assemble_final_images(
                super_img=super_img,
                source_images_dir=Path(tmp) / "source",
                final_dir=final_dir,
                execute=True,
            )

        assert not result["errors"], f"Errors must be empty for same-file skip: {result['errors']}"
        assert result["warnings"], "At least one warning must be present for same-file skip"

    def test_zorn_preserve_super_then_assemble_no_failure(self):
        """Full zorn scenario: super_rebuilder preserves super into final/, then assembler skips same-file."""
        from factory.super.super_rebuilder import rebuild_super

        with tempfile.TemporaryDirectory() as tmp:
            original_super = Path(tmp) / "source_images" / "super.img"
            original_super.parent.mkdir(parents=True)
            original_super.write_bytes(b"ZORN_SUPER_CONTENT")

            final_dir = Path(tmp) / "output" / "images" / "final"
            final_dir.mkdir(parents=True)
            reports_dir = Path(tmp) / "reports"
            super_parts = Path(tmp) / "super_parts"
            super_parts.mkdir()

            # super_rebuilder places super.img in final_dir
            output_super = final_dir / "super.img"
            sr = rebuild_super(
                super_parts_dir=super_parts,
                output_super=output_super,
                reports_dir=reports_dir,
                original_super_img=original_super,
                execute=True,
                preserve_original_super=True,
            )
            assert sr["status"] == "APPLIED", f"super_rebuilder must succeed: {sr['errors']}"
            assert output_super.is_file()

            # Now assemble — source path is the same as destination
            source_dir = Path(tmp) / "source_images"
            _write(source_dir / "boot.img")

            result = assemble_final_images(
                super_img=output_super,
                source_images_dir=source_dir,
                final_dir=final_dir,
                execute=True,
            )

        assert result["status"] == "APPLIED", (
            f"Full zorn path must succeed. Status={result['status']}, Errors={result['errors']}"
        )
        assert "super.img" in (result.get("final_manifest") or [])

    def test_normal_copy_still_works_when_src_differs(self):
        """When source != destination, shutil.copy2 must still run normally."""
        with tempfile.TemporaryDirectory() as tmp:
            src_super = Path(tmp) / "source" / "super.img"
            src_super.parent.mkdir()
            src_super.write_bytes(b"SOURCE_SUPER")

            final_dir = Path(tmp) / "final"
            final_dir.mkdir()

            result = assemble_final_images(
                super_img=src_super,
                source_images_dir=Path(tmp) / "source_images",
                final_dir=final_dir,
                execute=True,
            )

            assert result["status"] == "APPLIED"
            assert (final_dir / "super.img").read_bytes() == b"SOURCE_SUPER"
            # No same-file warning for a genuine copy
            same_file_warnings = [w for w in result.get("warnings", []) if "same-file" in w.lower()]
            assert not same_file_warnings, f"No same-file warning expected for genuine copy: {same_file_warnings}"

    def test_final_zip_staging_includes_super_img(self):
        """final_manifest must list super.img when already present in final dir."""
        with tempfile.TemporaryDirectory() as tmp:
            final_dir = Path(tmp) / "final"
            final_dir.mkdir()
            # super.img was placed by preserve_original_super
            super_img = final_dir / "super.img"
            super_img.write_bytes(b"SUPER")
            _write(final_dir / "boot.img")

            result = assemble_final_images(
                super_img=super_img,
                source_images_dir=Path(tmp) / "empty_source",
                final_dir=final_dir,
                execute=True,
            )

        manifest = result.get("final_manifest") or []
        assert "super.img" in manifest
        assert "boot.img" in manifest

    def test_final_zip_does_not_include_dynamic_partition_images(self):
        """Dynamic partition images must never appear in final assembled dir."""
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "source"
            for name in ["system.img", "vendor.img", "product.img", "odm.img"]:
                _write(source_dir / name)
            _write(source_dir / "boot.img")

            final_dir = Path(tmp) / "final"
            final_dir.mkdir()
            super_img = final_dir / "super.img"
            super_img.write_bytes(b"SUPER")

            result = assemble_final_images(
                super_img=super_img,
                source_images_dir=source_dir,
                final_dir=final_dir,
                execute=True,
            )

        manifest = set(result.get("final_manifest") or [])
        for dyn in ["system.img", "vendor.img", "product.img", "odm.img"]:
            assert dyn not in manifest, f"{dyn} must not be in final assembled dir"


class TestSmartSourceImageManifest:
    def test_unknown_source_image_is_copied(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "work" / "source_images"
            _write(source_dir / "random_firmware.img")
            super_img = Path(tmp) / "super.img"
            _write(super_img, b"SUPER")
            final_dir = Path(tmp) / "output" / "images" / "final"

            result = assemble_final_images(super_img, source_dir, final_dir, execute=True)

        assert result["status"] == "APPLIED"
        assert "random_firmware.img" in set(result["final_manifest"])

    def test_zorn_style_source_images_are_copied(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "work" / "source_images"
            names = [
                "userdata.img", "metadata.img", "misc.img",
                "persist.img", "rescue.img", "vm-bootsys.img",
            ]
            for name in names:
                _write(source_dir / name)
            super_img = Path(tmp) / "super.img"
            _write(super_img, b"SUPER")
            final_dir = Path(tmp) / "output" / "images" / "final"

            result = assemble_final_images(super_img, source_dir, final_dir, execute=True)

        manifest = set(result["final_manifest"])
        for name in names:
            assert name in manifest

    def test_super_exactly_once_excludes_temp_and_chunks(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "work" / "source_images"
            _write(source_dir / "boot.img")
            _write(source_dir / "super.img", b"SOURCE_SUPER")
            _write(source_dir / "super.unsparse.img", b"TEMP")
            _write(source_dir / "super.img.0", b"PART0")
            super_img = source_dir / "super.img"
            final_dir = Path(tmp) / "output" / "images" / "final"

            result = assemble_final_images(super_img, source_dir, final_dir, execute=True)

        manifest = set(result["final_manifest"])
        assert result["exactly_one_super_img"] is True
        assert "super.img" in manifest
        assert "super.unsparse.img" not in manifest
        assert "super.img.0" not in manifest

    def test_split_super_chunks_merge_to_one_super(self):
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "work" / "source_images"
            _write(source_dir / "super.img.0", b"AA")
            _write(source_dir / "super.img.1", b"BB")
            final_dir = Path(tmp) / "output" / "images" / "final"

            result = assemble_final_images(
                super_img=Path(tmp) / "missing_super.img",
                source_images_dir=source_dir,
                final_dir=final_dir,
                execute=True,
            )
            merged = (final_dir / "super.img").read_bytes()

        assert result["status"] == "APPLIED"
        assert merged == b"AABB"
        assert result["final_manifest"] == ["super.img"]

    def test_super_workspace_dynamic_and_unknown_are_not_copied(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp) / "work"
            source_dir = work / "source_images"
            _write(source_dir / "boot.img")
            for name in ["system.img", "product.img", "vendor.img", "mystery.img"]:
                _write(work / "super_parts" / name)
            super_img = Path(tmp) / "super.img"
            _write(super_img, b"SUPER")
            final_dir = Path(tmp) / "output" / "images" / "final"

            result = assemble_final_images(super_img, source_dir, final_dir, execute=True)

        manifest = set(result["final_manifest"])
        assert "boot.img" in manifest
        for name in ["system.img", "product.img", "vendor.img", "mystery.img"]:
            assert name not in manifest

    def test_source_manifest_report_contains_required_fields(self):
        import json

        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "work" / "source_images"
            _write(source_dir / "boot.img")
            super_img = Path(tmp) / "super.img"
            _write(super_img, b"SUPER")
            final_dir = Path(tmp) / "output" / "images" / "final"

            result = assemble_final_images(super_img, source_dir, final_dir, execute=True)
            report = Path(tmp) / "reports" / "source_image_manifest.json"
            report_exists = report.is_file()
            data = json.loads(report.read_text(encoding="utf-8"))

        assert report_exists
        assert data["super_handling"]["exactly_one_super_img"] is True
        assert result["exactly_one_super_img"] is True
        for image in data["images"]:
            for key in ["role", "origin", "include_in_final", "reason"]:
                assert key in image

    def test_final_zip_sweeps_split_super_chunk_and_succeeds(self):
        """super.img.0 (split super chunk) must be swept before the exactly_one_super check.
        After sweep, packaging must succeed — not fail — because super.img is still present."""
        from factory.output.final_zip_legacy import build_final_fastboot_zip

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            images_dir = root / "output" / "images" / "final"
            for name in ["super.img", "boot.img", "random_firmware.img"]:
                _write(images_dir / name)
            _write(images_dir / "super.img.0")
            template_zip = root / "template.zip"
            with zipfile.ZipFile(template_zip, "w") as zf:
                zf.writestr("bin/windows/fastboot.exe", b"")
                zf.writestr("bin/windows/AdbWinApi.dll", b"")
                zf.writestr("bin/windows/AdbWinUsbApi.dll", b"")

            result = build_final_fastboot_zip(
                images_dir=images_dir,
                output_dir=root / "output" / "final",
                build_name="DeadZone_Test",
                device="zorn",
                flavor="deadzone",
                soc="snapdragon",
                template_zip=template_zip,
                device_model="Test Device",
                android_version="16",
                build_incremental="OS3.0.1.0.WNOCNXM",
                execute=False,
            )

        # super.img.0 is swept before the check; exactly one super.img remains → DRY_RUN
        assert result["exactly_one_super_img"] is True, (
            "exactly_one_super_img must be True after super.img.0 is swept"
        )
        assert result["final_status"] == "DRY_RUN", (
            f"Expected DRY_RUN after sweep, got {result['final_status']}. Errors: {result['errors']}"
        )
        # The swept chunk must be recorded in the skipped list
        assert "super.img.0" in result.get("skipped_duplicate_super_images", []), (
            "super.img.0 must appear in skipped_duplicate_super_images"
        )

    def test_final_zip_plans_all_final_source_images(self):
        from factory.output.final_zip_legacy import build_final_fastboot_zip

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            images_dir = root / "output" / "images" / "final"
            for name in ["super.img", "boot.img", "random_firmware.img", "misc.img"]:
                _write(images_dir / name)
            template_zip = root / "template.zip"
            with zipfile.ZipFile(template_zip, "w") as zf:
                zf.writestr("bin/windows/fastboot.exe", b"")
                zf.writestr("bin/windows/AdbWinApi.dll", b"")
                zf.writestr("bin/windows/AdbWinUsbApi.dll", b"")

            result = build_final_fastboot_zip(
                images_dir=images_dir,
                output_dir=root / "output" / "final",
                build_name="DeadZone_Test",
                device="zorn",
                flavor="deadzone",
                soc="snapdragon",
                template_zip=template_zip,
                device_model="Test Device",
                android_version="16",
                build_incremental="OS3.0.1.0.WNOCNXM",
                execute=False,
            )

        assert result["final_status"] == "DRY_RUN"
        assert result["exactly_one_super_img"] is True
        assert result["final_image_count"] == 4
        for name in ["super.img", "boot.img", "random_firmware.img", "misc.img"]:
            assert f"images/{name}" in result["zip_entries"]
        assert not any("output/work" in e for e in result["zip_entries"])
        assert not result["forbidden_entries"]


# ═══════════════════════════════════════════════════════════════════
# 18. SUPER.UNSPARSE.IMG MANAGED — never in final images or ZIP
# ═══════════════════════════════════════════════════════════════════

class TestSuperUnsparseManagedClean:
    """Verifies that super.unsparse.img (lpunpack validation artifact) is kept
    out of the public final-images folder and final ZIP."""

    # ── 1. super_rebuilder cleans unsparse from the final dir ──────────────

    def test_rebuild_super_preserve_cleans_unsparse_from_final_dir(self):
        """After preserve_original_super, super.unsparse.img must NOT remain in output_super.parent."""
        from factory.super.super_rebuilder import rebuild_super
        import factory.super.super_rebuilder as _sr_mod

        with tempfile.TemporaryDirectory() as tmp:
            original_super = Path(tmp) / "source_images" / "super.img"
            original_super.parent.mkdir(parents=True)
            original_super.write_bytes(b"SUPER_BYTES")

            final_dir = Path(tmp) / "output" / "images" / "final"
            final_dir.mkdir(parents=True)
            output_super = final_dir / "super.img"
            reports_dir = Path(tmp) / "reports"

            # Simulate lpunpack creating super.unsparse.img next to the output super
            original_get_info = _sr_mod._lpunpack_get_info

            def _fake_get_info(path):
                # Create the unsparse sibling, as lpunpack would do for sparse images
                p = Path(path)
                (p.parent / f"{p.stem}.unsparse.img").write_bytes(b"UNSPARSE_DATA")
                return None  # return None so validation is skipped gracefully

            _sr_mod._lpunpack_get_info = _fake_get_info
            try:
                result = rebuild_super(
                    super_parts_dir=Path(tmp) / "super_parts",
                    output_super=output_super,
                    reports_dir=reports_dir,
                    original_super_img=original_super,
                    execute=True,
                    preserve_original_super=True,
                )
            finally:
                _sr_mod._lpunpack_get_info = original_get_info

            # Assertions must be inside the `with` block while the temp dir still exists
            assert result["status"] == "APPLIED"
            assert not (final_dir / "super.unsparse.img").exists(), (
                "super.unsparse.img must be removed from final dir after lpunpack validation"
            )
            assert output_super.is_file(), "super.img must still be present"

    # ── 2. final_image_assembler sweeps unsparse before manifest ────────────

    def test_assembler_sweeps_unsparse_before_manifest(self):
        """assemble_final_images must move super.unsparse.img out of final_dir before manifest."""
        with tempfile.TemporaryDirectory() as tmp:
            final_dir = Path(tmp) / "output" / "images" / "final"
            final_dir.mkdir(parents=True)
            super_img = final_dir / "super.img"
            super_img.write_bytes(b"SUPER")
            # Simulate the lpunpack artifact appearing in final_dir
            (final_dir / "super.unsparse.img").write_bytes(b"UNSPARSE")

            source_dir = Path(tmp) / "work" / "source_images"
            _write(source_dir / "boot.img")

            result = assemble_final_images(
                super_img=super_img,
                source_images_dir=source_dir,
                final_dir=final_dir,
                execute=True,
            )

        assert result["status"] == "APPLIED"
        assert "super.unsparse.img" not in (result.get("final_manifest") or []), (
            "super.unsparse.img must not appear in final_manifest"
        )
        assert result.get("exactly_one_super_img") is True
        assert not (final_dir / "super.unsparse.img").exists(), (
            "super.unsparse.img must be moved out of final_dir"
        )

    # ── 3. final_dir has exactly one super.img after cleanup ────────────────

    def test_final_dir_exactly_one_super_after_cleanup(self):
        """After assemble, exactly_one_super_img must be True even if unsparse was present."""
        with tempfile.TemporaryDirectory() as tmp:
            final_dir = Path(tmp) / "final"
            final_dir.mkdir()
            (final_dir / "super.img").write_bytes(b"SUPER")
            (final_dir / "super.unsparse.img").write_bytes(b"UNSPARSE")
            # super.img.0 is a split chunk (extension .0, not .img) — still swept
            (final_dir / "super.img.0").write_bytes(b"CHUNK")

            source_dir = Path(tmp) / "src"
            _write(source_dir / "boot.img")

            result = assemble_final_images(
                super_img=final_dir / "super.img",
                source_images_dir=source_dir,
                final_dir=final_dir,
                execute=True,
            )

            assert result["exactly_one_super_img"] is True
            # Only super.img (and boot.img) must remain; forbidden artifacts swept
            remaining = {p.name for p in final_dir.iterdir() if p.is_file()}
            assert "super.unsparse.img" not in remaining
            assert "super.img.0" not in remaining
            assert "super.img" in remaining

    # ── 4. final_zip_legacy sweeps unsparse before packaging check ──────────

    def test_final_zip_sweeps_unsparse_before_exactly_one_super_check(self):
        """build_final_fastboot_zip must remove super.unsparse.img and not fail the super check."""
        from factory.output.final_zip_legacy import build_final_fastboot_zip

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            images_dir = root / "output" / "images" / "final"
            images_dir.mkdir(parents=True)
            _write(images_dir / "super.img")
            _write(images_dir / "boot.img")
            # This artifact should be swept before the exactly_one_super check
            _write(images_dir / "super.unsparse.img", b"UNSPARSE_ARTIFACT")

            template_zip = root / "template.zip"
            with zipfile.ZipFile(str(template_zip), "w") as zf:
                zf.writestr("bin/windows/fastboot.exe", b"")
                zf.writestr("bin/windows/AdbWinApi.dll", b"")
                zf.writestr("bin/windows/AdbWinUsbApi.dll", b"")

            result = build_final_fastboot_zip(
                images_dir=images_dir,
                output_dir=root / "output" / "final",
                build_name="DeadZone_Test",
                device="zorn",
                flavor="free",
                soc="snapdragon",
                template_zip=template_zip,
                execute=False,
            )

        assert result["exactly_one_super_img"] is True, (
            "exactly_one_super_img must be True after super.unsparse.img is swept"
        )
        assert not (images_dir / "super.unsparse.img").exists(), (
            "super.unsparse.img must be removed from images_dir"
        )
        assert not any("super.unsparse" in e for e in result.get("errors", [])), (
            f"No error about super.unsparse.img expected after sweep. Errors: {result['errors']}"
        )

    # ── 5. ZIP staging and entries exclude super.unsparse.img ───────────────

    def test_zip_entries_exclude_super_unsparse(self):
        """dry-run zip_entries must not contain any super.unsparse.img entry."""
        from factory.output.final_zip_legacy import build_final_fastboot_zip

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            images_dir = root / "output" / "images" / "final"
            images_dir.mkdir(parents=True)
            for name in ["super.img", "boot.img"]:
                _write(images_dir / name)
            _write(images_dir / "super.unsparse.img", b"UNSPARSE")

            template_zip = root / "template.zip"
            with zipfile.ZipFile(str(template_zip), "w") as zf:
                zf.writestr("bin/windows/fastboot.exe", b"")
                zf.writestr("bin/windows/AdbWinApi.dll", b"")
                zf.writestr("bin/windows/AdbWinUsbApi.dll", b"")

            result = build_final_fastboot_zip(
                images_dir=images_dir,
                output_dir=root / "output" / "final",
                build_name="DeadZone_Test",
                device="zorn",
                flavor="deadzone",
                soc="snapdragon",
                template_zip=template_zip,
                device_model="Xiaomi Zorn",
                android_version="16",
                build_incremental="OS3.0.1.0.WNOCNXM",
                execute=False,
            )

        for entry in result.get("zip_entries", []):
            assert "unsparse" not in entry.lower(), (
                f"super.unsparse.img must not appear in ZIP entries, found: {entry}"
            )
        assert "images/super.img" in result.get("zip_entries", [])

    # ── 6. Source images (userdata, metadata, vm-bootsys) remain included ───

    def test_source_images_not_affected_by_unsparse_sweep(self):
        """userdata.img / metadata.img / vm-bootsys.img must still be included after sweep."""
        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "work" / "source_images"
            for name in ["userdata.img", "metadata.img", "misc.img", "persist.img",
                         "rescue.img", "vm-bootsys.img"]:
                _write(source_dir / name)
            super_img = Path(tmp) / "super.img"
            _write(super_img, b"SUPER")
            # Also put a forbidden artifact in the source_dir — must NOT end up in final
            _write(source_dir / "super.unsparse.img", b"UNSPARSE")

            final_dir = Path(tmp) / "output" / "images" / "final"
            result = assemble_final_images(super_img, source_dir, final_dir, execute=True)

        manifest = set(result["final_manifest"])
        for name in ["userdata.img", "metadata.img", "misc.img",
                     "persist.img", "rescue.img", "vm-bootsys.img"]:
            assert name in manifest, f"{name} must be in final manifest"
        assert "super.unsparse.img" not in manifest

    # ── 7. source_image_manifest marks super.unsparse.img as validation/temp ─

    def test_source_manifest_marks_unsparse_as_validation(self):
        """build_source_image_manifest must assign role='validation' and include_in_final=False
        to super.unsparse.img."""
        from factory.images.source_image_manifest import build_source_image_manifest

        with tempfile.TemporaryDirectory() as tmp:
            source_dir = Path(tmp) / "work" / "source_images"
            _write(source_dir / "boot.img")
            _write(source_dir / "super.unsparse.img", b"UNSPARSE_DATA")
            super_img = Path(tmp) / "super.img"
            _write(super_img, b"SUPER")
            work_root = Path(tmp) / "work"

            manifest = build_source_image_manifest(
                source_roots=[source_dir],
                work_root=work_root,
                final_super_path=super_img,
            )

        unsparse_entries = [
            e for e in manifest["images"]
            if e["name"].lower() == "super.unsparse.img"
        ]
        assert unsparse_entries, "super.unsparse.img must appear in manifest"
        entry = unsparse_entries[0]
        assert entry["include_in_final"] is False, (
            "super.unsparse.img must have include_in_final=False"
        )
        assert entry["role"] in {"validation", "temp"}, (
            f"super.unsparse.img must have role='validation' or 'temp', got {entry['role']!r}"
        )

    # ── 8. final_image_manifest.json has exactly_one_super_img=true ─────────

    def test_final_image_manifest_exactly_one_super_true(self):
        """final_image_manifest.json must have exactly_one_super_img=true even when
        super.unsparse.img was present in final_dir."""
        import json

        with tempfile.TemporaryDirectory() as tmp:
            # _write_final_image_manifest uses final_dir.parents[1] / "reports"
            # final_dir = output/images/final → parents[1] = output
            final_dir = Path(tmp) / "output" / "images" / "final"
            final_dir.mkdir(parents=True)
            (final_dir / "super.img").write_bytes(b"SUPER")
            (final_dir / "super.unsparse.img").write_bytes(b"UNSPARSE")

            source_dir = Path(tmp) / "work" / "source_images"
            _write(source_dir / "boot.img")

            result = assemble_final_images(
                super_img=final_dir / "super.img",
                source_images_dir=source_dir,
                final_dir=final_dir,
                execute=True,
            )

            # Report goes to final_dir.parents[1] / "reports" = output/reports
            report_path = Path(tmp) / "output" / "reports" / "final_image_manifest.json"
            assert report_path.is_file(), "final_image_manifest.json must be written"
            data = json.loads(report_path.read_text(encoding="utf-8"))

            assert data["exactly_one_super_img"] is True, (
                "final_image_manifest.json must have exactly_one_super_img=true"
            )
            assert "super.unsparse.img" not in data.get("included_images", []), (
                "super.unsparse.img must not appear in included_images"
            )
            moved = data.get("moved_forbidden_artifacts", [])
            assert "super.unsparse.img" in moved, (
                "super.unsparse.img must appear in moved_forbidden_artifacts"
            )

    # ── 9. Zorn-style final images pass packaging validation ────────────────

    def test_zorn_style_final_images_pass_packaging(self):
        """Final-images folder with only super.img + standard standalone images must pass
        build_final_fastboot_zip validation (the zorn scenario)."""
        from factory.output.final_zip_legacy import build_final_fastboot_zip

        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            images_dir = root / "output" / "images" / "final"
            images_dir.mkdir(parents=True)
            for name in ["super.img", "boot.img", "vbmeta.img", "dtbo.img"]:
                _write(images_dir / name)
            # No super.unsparse.img — clean zorn scenario

            template_zip = root / "template.zip"
            with zipfile.ZipFile(str(template_zip), "w") as zf:
                zf.writestr("bin/windows/fastboot.exe", b"")
                zf.writestr("bin/windows/AdbWinApi.dll", b"")
                zf.writestr("bin/windows/AdbWinUsbApi.dll", b"")

            result = build_final_fastboot_zip(
                images_dir=images_dir,
                output_dir=root / "output" / "final",
                build_name="DeadZone_Test",
                device="zorn",
                flavor="deadzone",
                soc="snapdragon",
                template_zip=template_zip,
                device_model="Xiaomi Zorn",
                android_version="16",
                build_incremental="OS3.0.1.0.WNOCNXM",
                execute=False,
            )

        assert result["exactly_one_super_img"] is True
        assert result["final_status"] == "DRY_RUN", (
            f"Zorn-style packaging must produce DRY_RUN. Got: {result['final_status']}\n"
            f"Errors: {result['errors']}"
        )
        assert not result["forbidden_entries"], (
            f"No forbidden entries expected: {result['forbidden_entries']}"
        )


# ═══════════════════════════════════════════════════════════════════
# 19. EDITION ENGINE UNIFICATION
#     Verifies the architecture rule: all editions share the same
#     legacy engine; only the mod layer (apply_mods flag) differs.
# ═══════════════════════════════════════════════════════════════════

class TestEditionEngineUnification:
    """Free uses apply_mods=False; Legend/Gaming/EPIC use apply_mods=True.
    The same run_legacy_engine() powers all of them."""

    def _run_engine(self, apply_mods: bool, edition: str = "free") -> dict:
        """Run run_legacy_engine in dry_run mode and return result."""
        from factory.pipeline.context import BuildContext
        from factory.pipeline.legacy_engine_runner import run_legacy_engine
        import time

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="garnet",
                edition=edition,
                mode="dry_run",
                soc="snapdragon",
                output_dir=output_dir,
            )
            return run_legacy_engine(
                context=ctx,
                notifier=None,
                output_dir=output_dir,
                template_zip=None,
                pipeline_start=time.monotonic(),
                edition=edition,
                apply_mods=apply_mods,
            )

    def test_free_uses_apply_mods_false_via_engine(self):
        """run_legacy_engine with apply_mods=False must produce DRY_RUN for Free."""
        result = self._run_engine(apply_mods=False, edition="free")
        assert result["final_status"] == "DRY_RUN"

    def test_legend_engine_path_uses_apply_mods_true(self):
        """run_legacy_engine with apply_mods=True (Legend) must also produce DRY_RUN
        (same shared engine, only mod flag differs)."""
        result = self._run_engine(apply_mods=True, edition="legend")
        assert result["final_status"] == "DRY_RUN", (
            f"Legend path must reach DRY_RUN through the same engine. Got: {result['final_status']}"
        )

    def test_gaming_edition_reaches_dry_run_same_engine(self):
        """Gaming edition uses the same engine and must reach DRY_RUN."""
        result = self._run_engine(apply_mods=True, edition="gaming")
        assert result["final_status"] == "DRY_RUN"

    def test_epic_edition_reaches_dry_run_same_engine(self):
        """EPIC edition uses the same engine and must reach DRY_RUN."""
        result = self._run_engine(apply_mods=True, edition="epic")
        assert result["final_status"] == "DRY_RUN"

    def test_apply_mods_false_picks_preserve_super_for_free(self):
        """With apply_mods=False and an original super.img, strategy must be preserve."""
        from factory.super.universal_super_engine import (
            STRATEGY_PRESERVE_ORIGINAL,
            select_super_strategy,
        )
        with tempfile.TemporaryDirectory() as tmp:
            super_img = Path(tmp) / "super.img"
            _write(super_img, b"SUPER")
            strategy = select_super_strategy(
                original_super_img=super_img,
                split_super_merged=False,
                has_dynamic_partitions=False,
                apply_mods=False,
            )
        assert strategy == STRATEGY_PRESERVE_ORIGINAL

    def test_apply_mods_true_always_picks_rebuild_modified(self):
        """With apply_mods=True, strategy must always be rebuild_modified_super
        — even when an original super.img is present."""
        from factory.super.universal_super_engine import (
            STRATEGY_REBUILD_MODIFIED,
            select_super_strategy,
        )
        with tempfile.TemporaryDirectory() as tmp:
            super_img = Path(tmp) / "super.img"
            _write(super_img, b"SUPER")
            strategy = select_super_strategy(
                original_super_img=super_img,
                split_super_merged=False,
                has_dynamic_partitions=True,
                apply_mods=True,
            )
        assert strategy == STRATEGY_REBUILD_MODIFIED

    def test_only_mod_layer_differs_between_free_and_legend(self):
        """Free and Legend both route through run_smart_base_engine — only apply_mods differs."""
        import factory.engine.smart_base_engine as engine_mod
        import time

        calls: list[dict] = []
        original = engine_mod.run_smart_base_engine

        def _spy(context, edition="free", apply_mods=False, **kw):
            calls.append({"edition": edition, "apply_mods": apply_mods})
            return {
                "final_status": "DRY_RUN",
                "build_id": None,
                "build_name": f"DZ_{context.codename}",
                "codename": context.codename,
                "edition": edition,
                "soc": context.soc,
                "final_zip": None,
                "pixeldrain_link": None,
                "telegram_message_id": None,
                "warnings": [], "errors": [],
                "stage_reports": {}, "report_files": {},
            }

        engine_mod.run_smart_base_engine = _spy
        try:
            from factory.pipeline.free_pipeline import run_free_pipeline
            from factory.pipeline.context import BuildContext

            with tempfile.TemporaryDirectory() as tmp:
                output_dir = Path(tmp) / "output"
                ctx = BuildContext(
                    codename="garnet", edition="free", mode="dry_run",
                    soc="snapdragon", output_dir=output_dir,
                )
                run_free_pipeline(
                    ctx=ctx, notifier=None, soc="snapdragon",
                    source="test", output_dir=output_dir,
                    template_zip=None, pipeline_start=time.monotonic(),
                )
        finally:
            engine_mod.run_smart_base_engine = original

        assert calls, "run_smart_base_engine must have been called by run_free_pipeline"
        assert calls[0]["apply_mods"] is False, (
            "Free edition must pass apply_mods=False to run_smart_base_engine"
        )

    def test_free_pipeline_does_not_call_legend_mod_runner(self):
        """Free edition must never invoke legend/gaming/epic mod runners."""
        import importlib
        mod_runners_called: list[str] = []

        for mod_name in ["legend", "gaming", "epic"]:
            try:
                mod = importlib.import_module(f"factory.patch.mods.{mod_name}.runner")
                if hasattr(mod, "run_mod"):
                    def _spy(name=mod_name, *a, **kw):
                        mod_runners_called.append(name)
                        return {"status": "APPLIED"}
                    mod.run_mod = _spy
            except ImportError:
                pass

        from factory.pipeline.context import BuildContext
        from factory.pipeline.free_pipeline import run_free_pipeline
        import time

        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp) / "output"
            ctx = BuildContext(
                codename="garnet", edition="free",
                mode="dry_run", soc="snapdragon", output_dir=output_dir,
            )
            run_free_pipeline(
                ctx=ctx, notifier=None, soc="snapdragon", source="test",
                output_dir=output_dir, template_zip=None, pipeline_start=time.monotonic(),
            )

        assert not mod_runners_called, (
            f"Free edition must not invoke any mod runner. Called: {mod_runners_called}"
        )


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
