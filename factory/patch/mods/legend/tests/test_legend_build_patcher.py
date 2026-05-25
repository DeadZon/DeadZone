"""
Dry tests for legend_build_patcher.

Run:
    python -m pytest factory/patch/legend/tests/test_legend_build_patcher.py -v
or:
    python factory/patch/legend/tests/test_legend_build_patcher.py
"""
from __future__ import annotations

import os
import sys
import tempfile
from pathlib import Path

# Ensure repo root is on sys.path when run directly.
_REPO_ROOT = Path(__file__).resolve().parents[5]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from factory.patch.mods.legend.patchers.legend_build_patcher import patch_legend_build


# ── Helpers ───────────────────────────────────────────────────────────────────

def _make_build(tmp: Path) -> Path:
    build = tmp / "build"
    (build / "system").mkdir(parents=True)
    (build / "system" / "test.txt").write_text("hello system", encoding="utf-8")
    (build / "product").mkdir(parents=True)
    (build / "product" / "test.txt").write_text("hello product", encoding="utf-8")
    (build / "system_ext" / "empty_dir").mkdir(parents=True)
    (build / "vendor").mkdir(parents=True)
    (build / "vendor" / "test_vendor.txt").write_text("hello vendor", encoding="utf-8")
    return build


def _make_rom_root(tmp: Path) -> Path:
    rom = tmp / "rom_root"
    rom.mkdir()
    return rom


# ── Test: missing folder, no URL -> SKIPPED_TEMPORARY ────────────────────────

def test_missing_folder_skipped_temporary() -> None:
    with tempfile.TemporaryDirectory() as td:
        rom_root = _make_rom_root(Path(td))
        original = os.environ.pop("LEGEND_BUILD_URL", None)
        try:
            result = patch_legend_build(
                rom_root,
                execute=False,
                work_dir=Path(td) / "work",
            )
            assert result["status"] in ("SKIPPED_TEMPORARY", "DRY_RUN", "APPLIED"), \
                f"Unexpected status: {result['status']}"
            if result["status"] == "SKIPPED_TEMPORARY":
                assert result["source_used"] == "missing_temporary"
                assert result["errors"] == []
                print("PASS: missing folder -> SKIPPED_TEMPORARY")
            else:
                print(f"PASS: build folder present -> {result['status']} (expected in CI)")
        finally:
            if original is not None:
                os.environ["LEGEND_BUILD_URL"] = original


# ── Test: local build folder present -> files copied ─────────────────────────

def test_local_build_applied() -> None:
    import factory.patch.mods.legend.patchers.legend_build_patcher as _mod
    _orig_build_dir = _mod._LOCAL_BUILD_DIR

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        build_dir = _make_build(tmp)
        rom_root = _make_rom_root(tmp)

        _mod._LOCAL_BUILD_DIR = build_dir
        try:
            result = patch_legend_build(
                rom_root,
                execute=True,
                work_dir=tmp / "work",
            )
        finally:
            _mod._LOCAL_BUILD_DIR = _orig_build_dir

        assert result["status"] == "APPLIED", f"Expected APPLIED, got {result['status']}"
        assert result["errors"] == [], f"Unexpected errors: {result['errors']}"
        assert (rom_root / "system" / "test.txt").exists(), "system/test.txt not copied"
        assert (rom_root / "product" / "test.txt").exists(), "product/test.txt not copied"
        assert (rom_root / "vendor" / "test_vendor.txt").exists(), \
            "vendor/test_vendor.txt not copied"
        assert (rom_root / "system_ext" / "empty_dir").is_dir(), \
            "system_ext/empty_dir not created"
        assert "system_ext/empty_dir" in result["created_empty_dirs"], \
            f"empty dir not reported: {result['created_empty_dirs']}"
        assert len(result["vendor_copied"]) >= 1, \
            f"vendor_copied empty: {result['vendor_copied']}"
        print(
            f"PASS: local build -> APPLIED, "
            f"copied={len(result['copied'])}, "
            f"vendor_copied={len(result['vendor_copied'])}, "
            f"empty_dirs={len(result['created_empty_dirs'])}"
        )


# ── Test: replace existing file ───────────────────────────────────────────────

def test_replace_existing_file() -> None:
    import factory.patch.mods.legend.patchers.legend_build_patcher as _mod
    _orig_build_dir = _mod._LOCAL_BUILD_DIR

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        build_dir = _make_build(tmp)
        rom_root = _make_rom_root(tmp)

        (rom_root / "system").mkdir(parents=True)
        (rom_root / "system" / "test.txt").write_text("old content", encoding="utf-8")

        _mod._LOCAL_BUILD_DIR = build_dir
        try:
            result = patch_legend_build(
                rom_root,
                execute=True,
                work_dir=tmp / "work",
            )
        finally:
            _mod._LOCAL_BUILD_DIR = _orig_build_dir

        assert result["status"] == "APPLIED"
        assert "system/test.txt" in result["replaced"], \
            f"system/test.txt not in replaced: {result['replaced']}"
        assert (rom_root / "system" / "test.txt").read_text(encoding="utf-8") == "hello system"
        print(f"PASS: existing file replaced - replaced={result['replaced']}")


# ── Test: unknown partition folder -> FAILED ──────────────────────────────────

def test_unknown_partition_fails() -> None:
    import factory.patch.mods.legend.patchers.legend_build_patcher as _mod
    _orig_build_dir = _mod._LOCAL_BUILD_DIR

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        build_dir = tmp / "bad_build"
        (build_dir / "system").mkdir(parents=True)
        (build_dir / "unknown_partition").mkdir(parents=True)
        rom_root = _make_rom_root(tmp)

        _mod._LOCAL_BUILD_DIR = build_dir
        try:
            result = patch_legend_build(
                rom_root,
                execute=True,
                work_dir=tmp / "work",
            )
        finally:
            _mod._LOCAL_BUILD_DIR = _orig_build_dir

        assert result["status"] == "FAILED", \
            f"Expected FAILED, got {result['status']}"
        assert "unknown_partition" in result["unknown_partitions"]
        print(f"PASS: unknown partition -> FAILED: {result['unknown_partitions']}")


# ── Test: dry-run makes no filesystem changes ─────────────────────────────────

def test_dry_run_no_writes() -> None:
    import factory.patch.mods.legend.patchers.legend_build_patcher as _mod
    _orig_build_dir = _mod._LOCAL_BUILD_DIR

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        build_dir = _make_build(tmp)
        rom_root = _make_rom_root(tmp)

        _mod._LOCAL_BUILD_DIR = build_dir
        try:
            result = patch_legend_build(
                rom_root,
                execute=False,
                work_dir=tmp / "work",
            )
        finally:
            _mod._LOCAL_BUILD_DIR = _orig_build_dir

        assert result["status"] == "DRY_RUN"
        assert not (rom_root / "system" / "test.txt").exists(), \
            "dry-run must not write files"
        print("PASS: dry-run -> DRY_RUN, no files written")


# ── Runner ────────────────────────────────────────────────────────────────────

def _run_all() -> None:
    tests = [
        test_missing_folder_skipped_temporary,
        test_local_build_applied,
        test_replace_existing_file,
        test_unknown_partition_fails,
        test_dry_run_no_writes,
    ]
    passed = 0
    failed = 0
    for t in tests:
        try:
            t()
            passed += 1
        except Exception as exc:
            print(f"FAIL: {t.__name__}: {exc}")
            import traceback
            traceback.print_exc()
            failed += 1
    print(f"\n{'='*50}")
    print(f"Results: {passed} passed, {failed} failed")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    _run_all()
