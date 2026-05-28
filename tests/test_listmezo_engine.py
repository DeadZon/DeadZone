"""Tests for factory.apps.listmezo_engine — Phase 1."""
from __future__ import annotations

import json
import textwrap
from pathlib import Path

import pytest

from factory.apps.listmezo_engine import (
    GuideEntry,
    _normalize_header,
    apply_buildprop,
    extract_package_name,
    parse_guide,
    run_listmezo,
    run_matching,
    scan_rom,
)


# ── Fixtures ──────────────────────────────────────────────────────────────────

MINIMAL_GUIDE = textwrap.dedent("""\
    system/system/priv-app
    or
    system/priv-app

    MiuiSystemUI
    com.android.systemui

    system/system/app
    or
    system/ app

    BluetoothMidiService
    com.android.bluetoothmidiservice

    product / app

    SomeApp
    com.some.app

    product / priv-app

    GmsCore
    com.google.android.gms

    system_ext / app

    ExtApp
    com.ext.app

    system_ext / priv-app

    Settings
    com.android.settings

    system / build.prop
    fine lines and replace
    ro.build.host=
    ro.build.host=xiaomi.deadzone

    ro.product.locale=
    ro.product.locale=en-GB

    fine and remove
    ro.miui.has_security_keyboard=1
    ro.miui.support_miui_ime_bottom=1
""")

DIRTY_GUIDE = textwrap.dedent("""\
    system/system/app
    or
    system/ app

    CarrierDefaultApp
    CarrierDefaultApp

    miuix
    miuix.apk

    ValidApp
    com.valid.app
""")

ALLOWED_APKS_GUIDE = textwrap.dedent("""\
    system/system/priv-app

    DocumentsUIGoogle
    com.google.android.documentsui
    DocumentsUIGoogle-xhdpi.apk
    DocumentsUIGoogle-xxhdpi.apk
    DocumentsUIGoogle-xxxhdpi.apk
""")


def _make_guide_file(tmp_path: Path, content: str) -> Path:
    p = tmp_path / "apps.list"
    p.write_text(content, encoding="utf-8")
    return p


# ── Header alias normalisation ─────────────────────────────────────────────────

@pytest.mark.parametrize("raw,expected", [
    ("system/system/app",        "system/app"),
    ("system/ app",              "system/app"),
    ("system/system/priv-app",   "system/priv-app"),
    ("system / priv-app",        "system/priv-app"),
    ("product / app",            "product/app"),
    ("product / priv-app",       "product/priv-app"),
    ("system_ext / app",         "system_ext/app"),
    ("system_ext / priv-app",    "system_ext/priv-app"),
    ("system/system/build.prop", "system/build.prop"),
    ("system / build.prop",      "system/build.prop"),
    ("garbage line",             None),
    ("",                         None),
])
def test_header_alias_normalisation(raw, expected):
    assert _normalize_header(raw) == expected


# ── Guide parser ───────────────────────────────────────────────────────────────

def test_parse_minimal_guide(tmp_path):
    gf = _make_guide_file(tmp_path, MINIMAL_GUIDE)
    guide = parse_guide(gf)
    pkgs = {e.package for e in guide.entries}
    assert "com.android.systemui" in pkgs
    assert "com.android.bluetoothmidiservice" in pkgs
    assert "com.some.app" in pkgs
    assert "com.google.android.gms" in pkgs
    assert "com.ext.app" in pkgs
    assert "com.android.settings" in pkgs
    assert guide.buildprop_section is True


def test_parse_guide_locations(tmp_path):
    gf = _make_guide_file(tmp_path, MINIMAL_GUIDE)
    guide = parse_guide(gf)
    by_pkg = {e.package: e for e in guide.entries}
    assert by_pkg["com.android.systemui"].location == "system/priv-app"
    assert by_pkg["com.android.bluetoothmidiservice"].location == "system/app"
    assert by_pkg["com.some.app"].location == "product/app"
    assert by_pkg["com.google.android.gms"].location == "product/priv-app"
    assert by_pkg["com.ext.app"].location == "system_ext/app"
    assert by_pkg["com.android.settings"].location == "system_ext/priv-app"


def test_parse_allowed_apks(tmp_path):
    gf = _make_guide_file(tmp_path, ALLOWED_APKS_GUIDE)
    guide = parse_guide(gf)
    assert len(guide.entries) == 1
    e = guide.entries[0]
    assert e.package == "com.google.android.documentsui"
    assert "DocumentsUIGoogle-xhdpi.apk" in e.allowed_apks
    assert "DocumentsUIGoogle-xxhdpi.apk" in e.allowed_apks
    assert "DocumentsUIGoogle-xxxhdpi.apk" in e.allowed_apks


def test_parse_dirty_guide_warns_invalid(tmp_path):
    gf = _make_guide_file(tmp_path, DIRTY_GUIDE)
    guide = parse_guide(gf)
    # CarrierDefaultApp and miuix should warn, ValidApp should parse
    pkgs = {e.package for e in guide.entries}
    assert "com.valid.app" in pkgs
    assert "CarrierDefaultApp" not in pkgs
    assert "miuix.apk" not in pkgs
    assert len(guide.warnings) >= 2
    warn_reasons = [w.reason for w in guide.warnings]
    assert any("invalid_package_value" in r for r in warn_reasons)


def test_parse_guide_no_crash_on_empty(tmp_path):
    gf = _make_guide_file(tmp_path, "")
    guide = parse_guide(gf)
    assert guide.entries == []


# ── Matching logic ─────────────────────────────────────────────────────────────

def _fake_rom_index(entries: list[tuple[str, str, str, str]]) -> dict:
    """entries: (package, partition_dir, folder_name, apk_name)"""
    from factory.apps.listmezo_engine import RomApp
    idx = {}
    for pkg, pdir, fname, apk in entries:
        idx[pkg] = RomApp(
            package=pkg,
            partition_dir=pdir,
            folder_path=Path(f"/fake/{pdir}/{fname}"),
            folder_name=fname,
            apk_path=Path(f"/fake/{pdir}/{fname}/{apk}"),
            apk_name=apk,
        )
    return idx


def _fake_guide(entries: list[tuple[str, str, str]]) -> object:
    """entries: (location, folder, package)"""
    from factory.apps.listmezo_engine import ParsedGuide
    g = ParsedGuide()
    for loc, folder, pkg in entries:
        g.entries.append(GuideEntry(location=loc, folder=folder, package=pkg))
    return g


def test_match_found_ok(tmp_path):
    guide = _fake_guide([("system/priv-app", "MiuiSystemUI", "com.android.systemui")])
    rom_idx = _fake_rom_index([
        ("com.android.systemui", "system/priv-app", "MiuiSystemUI", "MiuiSystemUI.apk"),
    ])
    result = run_matching(guide, rom_idx, Path("/fake"), dry_run=True)
    assert len(result.found_ok) == 1
    assert result.found_ok[0]["package"] == "com.android.systemui"
    assert result.missing == []
    assert result.wrong_location == []
    assert result.extras == []


def test_match_missing_app(tmp_path):
    guide = _fake_guide([("product/priv-app", "GmsCore", "com.google.android.gms")])
    rom_idx = {}   # empty ROM
    result = run_matching(guide, rom_idx, Path("/fake"), dry_run=True)
    assert len(result.missing) == 1
    m = result.missing[0]
    assert m["package"] == "com.google.android.gms"
    assert m["location"] == "product/priv-app"
    assert m["folder"] == "GmsCore"
    assert m["reason"] == "package_not_found"


def test_match_wrong_location_not_deleted(tmp_path):
    guide = _fake_guide([("system_ext/priv-app", "MiuiSystemUI", "com.android.systemui")])
    rom_idx = _fake_rom_index([
        # Package exists but in wrong partition
        ("com.android.systemui", "product/priv-app", "MiuiSystemUI", "MiuiSystemUI.apk"),
    ])
    result = run_matching(guide, rom_idx, Path("/fake"), dry_run=True)
    assert len(result.wrong_location) == 1
    wl = result.wrong_location[0]
    assert wl["package"] == "com.android.systemui"
    assert wl["action"] == "kept_not_moved_phase_1"
    assert result.extras == []     # must NOT appear in extras


def test_match_extra_app_reported(tmp_path):
    guide = _fake_guide([("system/app", "BluetoothMidiService", "com.android.bluetoothmidiservice")])
    rom_idx = _fake_rom_index([
        ("com.android.bluetoothmidiservice", "system/app", "BluetoothMidiService", "BluetoothMidiService.apk"),
        ("com.example.extra", "system/app", "ExtraApp", "ExtraApp.apk"),
    ])
    result = run_matching(guide, rom_idx, Path("/fake"), dry_run=True)
    assert len(result.extras) == 1
    assert result.extras[0]["package"] == "com.example.extra"


def test_match_unknown_apk_not_deleted(tmp_path):
    """Apps with UNKNOWN package must never appear in extras."""
    guide = _fake_guide([])
    rom_idx = {}   # unknown apps don't appear in index (scan_rom puts them in unknown list)
    result = run_matching(guide, rom_idx, Path("/fake"), dry_run=True)
    assert result.extras == []


def test_dry_run_does_not_change_files(tmp_path):
    """In dry_run, no filesystem changes should occur."""
    # Set up a fake ROM tree
    app_dir = tmp_path / "system" / "app" / "OldName"
    app_dir.mkdir(parents=True)
    apk = app_dir / "OldName.apk"
    apk.write_bytes(b"fake")

    guide = _fake_guide([("system/app", "NewName", "com.test.pkg")])
    rom_idx = _fake_rom_index([
        ("com.test.pkg", "system/app", "OldName", "OldName.apk"),
    ])
    # Patch folder_path to real tmp path
    rom_idx["com.test.pkg"].folder_path = app_dir
    rom_idx["com.test.pkg"].apk_path = apk

    run_matching(guide, rom_idx, tmp_path, dry_run=True)

    assert app_dir.exists(), "dry_run must not rename folder"
    assert apk.exists(), "dry_run must not rename APK"


def test_execute_renames_folder_and_apk(tmp_path):
    """In execute mode, folder and APK should be renamed."""
    app_dir = tmp_path / "system" / "app" / "OldName"
    app_dir.mkdir(parents=True)
    apk = app_dir / "OldName.apk"
    apk.write_bytes(b"fake")

    guide = _fake_guide([("system/app", "NewName", "com.test.pkg")])
    rom_idx = _fake_rom_index([
        ("com.test.pkg", "system/app", "OldName", "OldName.apk"),
    ])
    rom_idx["com.test.pkg"].folder_path = app_dir
    rom_idx["com.test.pkg"].apk_path = apk

    result = run_matching(guide, rom_idx, tmp_path, dry_run=False)

    new_folder = tmp_path / "system" / "app" / "NewName"
    assert new_folder.exists(), "execute mode must rename folder"
    assert (new_folder / "NewName.apk").exists(), "execute mode must rename APK"
    assert not app_dir.exists(), "old folder should be gone"
    assert len(result.renamed) == 1


# ── Build.prop ────────────────────────────────────────────────────────────────

def _make_buildprop(tmp_path: Path, content: str) -> Path:
    bp = tmp_path / "system" / "build.prop"
    bp.parent.mkdir(parents=True)
    bp.write_text(content, encoding="utf-8")
    return bp


def test_buildprop_replace(tmp_path):
    _make_buildprop(tmp_path, "ro.build.host=old_value\n")
    changes = apply_buildprop(tmp_path, dry_run=False)
    bp = (tmp_path / "system" / "build.prop").read_text()
    assert "ro.build.host=xiaomi.deadzone" in bp
    assert "old_value" not in bp
    assert any("REPLACED" in c for c in changes)


def test_buildprop_add_missing(tmp_path):
    _make_buildprop(tmp_path, "ro.some.other=value\n")
    apply_buildprop(tmp_path, dry_run=False)
    bp = (tmp_path / "system" / "build.prop").read_text()
    assert "ro.build.host=xiaomi.deadzone" in bp
    assert "ro.product.locale=en-GB" in bp


def test_buildprop_remove_lines(tmp_path):
    _make_buildprop(
        tmp_path,
        "ro.miui.has_security_keyboard=1\nro.miui.support_miui_ime_bottom=1\nro.safe=1\n",
    )
    apply_buildprop(tmp_path, dry_run=False)
    bp = (tmp_path / "system" / "build.prop").read_text()
    assert "ro.miui.has_security_keyboard=1" not in bp
    assert "ro.miui.support_miui_ime_bottom=1" not in bp
    assert "ro.safe=1" in bp


def test_buildprop_dry_run_no_change(tmp_path):
    original = "ro.build.host=old_value\n"
    _make_buildprop(tmp_path, original)
    apply_buildprop(tmp_path, dry_run=True)
    bp = (tmp_path / "system" / "build.prop").read_text()
    assert bp == original


def test_buildprop_missing_file(tmp_path):
    changes = apply_buildprop(tmp_path, dry_run=False)
    assert any("SKIP" in c for c in changes)


# ── Full run_listmezo integration ─────────────────────────────────────────────

def test_run_listmezo_skips_unknown_edition(tmp_path):
    result = run_listmezo(
        rom_root=tmp_path,
        edition="nonexistent",
        listmezo_root=tmp_path / "ListMezo",
    )
    assert result["status"] == "SKIPPED"


def test_run_listmezo_dry_run_generates_reports(tmp_path):
    # Create a minimal guide
    guide_dir = tmp_path / "ListMezo" / "free"
    guide_dir.mkdir(parents=True)
    (guide_dir / "apps.list").write_text(MINIMAL_GUIDE, encoding="utf-8")

    result = run_listmezo(
        rom_root=tmp_path,
        edition="free",
        mode="dry_run",
        output_dir=tmp_path / "output",
        listmezo_root=tmp_path / "ListMezo",
    )

    assert result["status"] == "DRY_RUN"
    report_dir = Path(result["report_dir"])
    assert (report_dir / "missing_apps.json").exists()
    assert (report_dir / "removed_extras.json").exists()
    assert (report_dir / "wrong_location.json").exists()
    assert (report_dir / "renamed_apps.json").exists()
    assert (report_dir / "unknown_apks.json").exists()
    assert (report_dir / "guide_warnings.json").exists()
    assert (report_dir / "listmezo_report.txt").exists()


def test_run_listmezo_reports_valid_json(tmp_path):
    guide_dir = tmp_path / "ListMezo" / "free"
    guide_dir.mkdir(parents=True)
    (guide_dir / "apps.list").write_text(MINIMAL_GUIDE, encoding="utf-8")

    result = run_listmezo(
        rom_root=tmp_path,
        edition="free",
        mode="dry_run",
        output_dir=tmp_path / "output",
        listmezo_root=tmp_path / "ListMezo",
    )

    report_dir = Path(result["report_dir"])
    for name in ("missing_apps.json", "removed_extras.json", "wrong_location.json",
                  "renamed_apps.json", "unknown_apks.json", "guide_warnings.json"):
        data = json.loads((report_dir / name).read_text())
        assert isinstance(data, list)


def test_run_listmezo_all_missing_with_empty_rom(tmp_path):
    guide_dir = tmp_path / "ListMezo" / "free"
    guide_dir.mkdir(parents=True)
    (guide_dir / "apps.list").write_text(MINIMAL_GUIDE, encoding="utf-8")

    result = run_listmezo(
        rom_root=tmp_path,
        edition="free",
        mode="dry_run",
        output_dir=tmp_path / "output",
        listmezo_root=tmp_path / "ListMezo",
    )

    # With no ROM apps, all guide entries must be MISSING
    report_dir = Path(result["report_dir"])
    missing = json.loads((report_dir / "missing_apps.json").read_text())
    assert len(missing) == result["summary"]["total_guide_apps"]
    assert result["summary"]["found_ok"] == 0
    assert result["summary"]["removed_extras"] == 0
