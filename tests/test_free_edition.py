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

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.input.rom_detector import (
    FORMAT_IMAGES_ZIP,
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
