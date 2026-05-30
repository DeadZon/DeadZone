"""Tests for factory.core.stable_app_policy — Stable App Policy Enforcement."""
from __future__ import annotations

import json
import os
import shutil
import tempfile
import zipfile
from pathlib import Path

import pytest

import factory.reports.app_inventory as _inv_mod
from factory.core.stable_app_policy import (
    _classify,
    _apply_renames,
    _apply_deletes,
    _build_allowed_dirs,
    _extract_package,
    _find_apk,
    _is_in_allowed,
    _parse_expected_apps,
    enforce_stable_app_policy,
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

SAMPLE_APPS_LIST = """\
system/system/priv-app/

BackupRestoreConfirmation
com.android.backupconfirm

Shell
com.android.shell

system/system/app

BluetoothMidiService
com.android.bluetoothmidiservice

EasterEgg
com.android.egg

product / app

Calculator
com.miui.calculator
"""


def _write_apps_list(tmp: Path, content: str = SAMPLE_APPS_LIST) -> Path:
    p = tmp / "apps.list"
    p.write_text(content, encoding="utf-8")
    return p


def _make_app_folder(partitions_root: Path, partition: str, app_type: str, name: str) -> Path:
    """Create a dummy app folder with an APK."""
    folder = partitions_root / partition / app_type / name
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{name}.apk").write_bytes(b"PK\x03\x04")  # minimal APK stub
    return folder


def _scanned_app(
    partition: str,
    app_type: str,
    name: str,
    package: str,
    partitions_root: Path,
) -> dict:
    folder = partitions_root / partition / app_type / name
    return {
        "partition": partition,
        "name": name,
        "path": f"{app_type}/{name}",
        "absolute_path": str(folder),
        "type": app_type,
        "package_name": package,
        "size": 100,
    }


# ---------------------------------------------------------------------------
# _is_in_allowed
# ---------------------------------------------------------------------------

def test_is_in_allowed_returns_true_for_allowed_path(tmp_path):
    allowed = [tmp_path / "system" / "app"]
    assert _is_in_allowed(str(tmp_path / "system" / "app" / "MyApp"), allowed)


def test_is_in_allowed_returns_false_for_outside_path(tmp_path):
    allowed = [tmp_path / "system" / "app"]
    assert not _is_in_allowed(str(tmp_path / "odm" / "app" / "MyApp"), allowed)


# ---------------------------------------------------------------------------
# 1. Exact app found → FOUND / KEEP
# ---------------------------------------------------------------------------

def test_exact_app_found_keep(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    _make_app_folder(partitions_root, "system", "app", "BluetoothMidiService")

    scanned = [_scanned_app("system", "app", "BluetoothMidiService",
                            "com.android.bluetoothmidiservice", partitions_root)]
    allowed = _build_allowed_dirs(partitions_root)
    from factory.reports.app_inventory import _parse_apps_list
    expected = _parse_apps_list(apps_list)
    result = _classify(scanned, expected, allowed)

    kept_names = {a["name"] for a in result["kept"]}
    assert "BluetoothMidiService" in kept_names
    del os.environ["LISTMEZO_APPS_LIST"]


# ---------------------------------------------------------------------------
# 2. Same package, different folder name → FOUND_RENAMED
# ---------------------------------------------------------------------------

def test_same_package_different_folder_rename(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    partitions_root = tmp_path / "partitions"
    # Folder named "BTMidi" instead of "BluetoothMidiService"
    _make_app_folder(partitions_root, "system", "app", "BTMidi")
    scanned = [_scanned_app("system", "app", "BTMidi",
                            "com.android.bluetoothmidiservice", partitions_root)]
    allowed = _build_allowed_dirs(partitions_root)
    from factory.reports.app_inventory import _parse_apps_list
    expected = _parse_apps_list(apps_list)
    result = _classify(scanned, expected, allowed)

    rename_packages = {r["package"] for r in result["to_rename"]}
    assert "com.android.bluetoothmidiservice" in rename_packages
    entry = next(r for r in result["to_rename"] if r["package"] == "com.android.bluetoothmidiservice")
    assert entry["expected_name"] == "BluetoothMidiService"
    assert entry["actual_name"] == "BTMidi"


# ---------------------------------------------------------------------------
# 3. Missing expected app → MISSING, report only (no fake folder)
# ---------------------------------------------------------------------------

def test_missing_expected_app_report_only(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    partitions_root.mkdir(parents=True, exist_ok=True)

    # No apps scanned at all
    reports_dir = tmp_path / "reports"
    result = enforce_stable_app_policy(
        reports_dir=reports_dir,
        partitions_root=partitions_root,
        scanned_apps=[],
        style="stable",
    )

    missing_names = {m["name"] for m in result["missing_apps"]}
    assert "BluetoothMidiService" in missing_names
    # No fake folders created
    assert not (partitions_root / "system" / "app" / "BluetoothMidiService").exists()
    del os.environ["LISTMEZO_APPS_LIST"]


# ---------------------------------------------------------------------------
# 4. Extra app in allowed location → DELETE (stable enforces)
# ---------------------------------------------------------------------------

def test_extra_app_in_allowed_location_deleted(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    extra_folder = _make_app_folder(partitions_root, "system", "app", "WeirdExtra")

    scanned = [_scanned_app("system", "app", "WeirdExtra",
                            "com.some.weird.extra", partitions_root)]
    reports_dir = tmp_path / "reports"

    result = enforce_stable_app_policy(
        reports_dir=reports_dir,
        partitions_root=partitions_root,
        scanned_apps=scanned,
        style="stable",
    )

    deleted = [d for d in result["deleted_extra_apps"] if d.get("enacted")]
    assert any(d["name"] == "WeirdExtra" for d in deleted)
    assert not extra_folder.exists(), "Extra app folder should have been deleted"
    del os.environ["LISTMEZO_APPS_LIST"]


# ---------------------------------------------------------------------------
# 5. Extra app outside allowed location → SKIP, not deleted
# ---------------------------------------------------------------------------

def test_extra_app_outside_allowed_not_deleted(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    # odm is not in the allowed list
    odm_folder = _make_app_folder(partitions_root, "odm", "app", "OdmExtra")

    scanned = [_scanned_app("odm", "app", "OdmExtra",
                            "com.odm.extra", partitions_root)]
    reports_dir = tmp_path / "reports"

    result = enforce_stable_app_policy(
        reports_dir=reports_dir,
        partitions_root=partitions_root,
        scanned_apps=scanned,
        style="stable",
    )

    skipped = result["skipped_outside_allowed_locations"]
    assert any(s["name"] == "OdmExtra" for s in skipped)
    assert odm_folder.exists(), "App outside allowed location must not be deleted"
    del os.environ["LISTMEZO_APPS_LIST"]


# ---------------------------------------------------------------------------
# 6. Rename target already exists → CONFLICT → stage fails
# ---------------------------------------------------------------------------

def test_rename_conflict_fails_stage(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    # App with wrong name AND the expected name already exists
    _make_app_folder(partitions_root, "system", "app", "BTMidi")
    _make_app_folder(partitions_root, "system", "app", "BluetoothMidiService")

    scanned = [
        _scanned_app("system", "app", "BTMidi",
                     "com.android.bluetoothmidiservice", partitions_root),
    ]
    reports_dir = tmp_path / "reports"

    with pytest.raises(RuntimeError, match="CONFLICT"):
        enforce_stable_app_policy(
            reports_dir=reports_dir,
            partitions_root=partitions_root,
            scanned_apps=scanned,
            style="stable",
        )
    del os.environ["LISTMEZO_APPS_LIST"]


# ---------------------------------------------------------------------------
# 7. Stable style enforces delete and rename
# ---------------------------------------------------------------------------

def test_stable_style_enforces_rename(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    wrong_folder = _make_app_folder(partitions_root, "system", "app", "BTMidi")

    scanned = [_scanned_app("system", "app", "BTMidi",
                            "com.android.bluetoothmidiservice", partitions_root)]
    reports_dir = tmp_path / "reports"

    result = enforce_stable_app_policy(
        reports_dir=reports_dir,
        partitions_root=partitions_root,
        scanned_apps=scanned,
        style="stable",
    )

    enacted = [r for r in result["renamed_apps"] if r.get("enacted")]
    assert len(enacted) == 1
    assert not wrong_folder.exists()
    expected_folder = partitions_root / "system" / "app" / "BluetoothMidiService"
    assert expected_folder.exists()
    del os.environ["LISTMEZO_APPS_LIST"]


def test_stable_style_enforces_delete(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    extra = _make_app_folder(partitions_root, "product", "app", "Garbage")

    scanned = [_scanned_app("product", "app", "Garbage",
                            "com.garbage.app", partitions_root)]
    reports_dir = tmp_path / "reports"

    result = enforce_stable_app_policy(
        reports_dir=reports_dir,
        partitions_root=partitions_root,
        scanned_apps=scanned,
        style="stable",
    )

    assert not extra.exists()
    assert result["summary"]["deleted_extra"] == 1
    del os.environ["LISTMEZO_APPS_LIST"]


# ---------------------------------------------------------------------------
# 8. Legend/Gaming/Epic → report only, no enforce
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("style", ["legend", "gaming", "epic"])
def test_non_stable_style_report_only(style, tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    extra = _make_app_folder(partitions_root, "system", "app", "ShouldNotDelete")

    scanned = [_scanned_app("system", "app", "ShouldNotDelete",
                            "com.should.not.delete", partitions_root)]
    reports_dir = tmp_path / "reports"

    result = enforce_stable_app_policy(
        reports_dir=reports_dir,
        partitions_root=partitions_root,
        scanned_apps=scanned,
        style=style,
    )

    # No app should be deleted
    assert extra.exists(), f"Style '{style}' must not delete apps"
    # All extras should be marked as not enacted
    for item in result["deleted_extra_apps"]:
        assert not item.get("enacted"), f"Style '{style}' must not enact deletes"
    del os.environ["LISTMEZO_APPS_LIST"]


@pytest.mark.parametrize("style", ["legend", "gaming", "epic"])
def test_non_stable_style_no_rename(style, tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    wrong = _make_app_folder(partitions_root, "system", "app", "BTMidi")

    scanned = [_scanned_app("system", "app", "BTMidi",
                            "com.android.bluetoothmidiservice", partitions_root)]
    reports_dir = tmp_path / "reports"

    result = enforce_stable_app_policy(
        reports_dir=reports_dir,
        partitions_root=partitions_root,
        scanned_apps=scanned,
        style=style,
    )

    assert wrong.exists(), f"Style '{style}' must not rename folders"
    for item in result["renamed_apps"]:
        assert not item.get("enacted"), f"Style '{style}' must not enact renames"
    del os.environ["LISTMEZO_APPS_LIST"]


# ---------------------------------------------------------------------------
# 9. apps.list missing in stable → fail clearly
# ---------------------------------------------------------------------------

def test_apps_list_missing_stable_fails(tmp_path):
    partitions_root = tmp_path / "partitions"
    partitions_root.mkdir(parents=True, exist_ok=True)
    reports_dir = tmp_path / "reports"

    nonexistent = str(tmp_path / "no_such_apps.list")
    os.environ["LISTMEZO_APPS_LIST"] = nonexistent
    orig_abs = _inv_mod._APPS_LIST_ABSOLUTE
    _inv_mod._APPS_LIST_ABSOLUTE = str(tmp_path / "also_nonexistent.list")
    try:
        with pytest.raises(RuntimeError, match="apps.list"):
            enforce_stable_app_policy(
                reports_dir=reports_dir,
                partitions_root=partitions_root,
                scanned_apps=[],
                style="stable",
            )
    finally:
        del os.environ["LISTMEZO_APPS_LIST"]
        _inv_mod._APPS_LIST_ABSOLUTE = orig_abs


# ---------------------------------------------------------------------------
# 10. apps.list missing in non-stable → skip gracefully
# ---------------------------------------------------------------------------

def test_apps_list_missing_non_stable_skips(tmp_path):
    partitions_root = tmp_path / "partitions"
    partitions_root.mkdir(parents=True, exist_ok=True)
    reports_dir = tmp_path / "reports"

    nonexistent = str(tmp_path / "no_such_apps.list")
    os.environ["LISTMEZO_APPS_LIST"] = nonexistent
    orig_abs = _inv_mod._APPS_LIST_ABSOLUTE
    _inv_mod._APPS_LIST_ABSOLUTE = str(tmp_path / "also_nonexistent.list")
    try:
        result = enforce_stable_app_policy(
            reports_dir=reports_dir,
            partitions_root=partitions_root,
            scanned_apps=[],
            style="legend",
        )
        assert result["status"] == "skipped"
    finally:
        del os.environ["LISTMEZO_APPS_LIST"]
        _inv_mod._APPS_LIST_ABSOLUTE = orig_abs


# ---------------------------------------------------------------------------
# 11. Reports are written correctly
# ---------------------------------------------------------------------------

def test_reports_written_txt_and_json(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    partitions_root.mkdir(parents=True, exist_ok=True)
    reports_dir = tmp_path / "reports"

    enforce_stable_app_policy(
        reports_dir=reports_dir,
        partitions_root=partitions_root,
        scanned_apps=[],
        style="stable",
    )

    txt_path = reports_dir / "stable_app_policy_report.txt"
    json_path = reports_dir / "stable_app_policy_report.json"
    assert txt_path.is_file(), "TXT report must be written"
    assert json_path.is_file(), "JSON report must be written"

    data = json.loads(json_path.read_text(encoding="utf-8"))
    assert "kept_apps" in data
    assert "renamed_apps" in data
    assert "missing_apps" in data
    assert "deleted_extra_apps" in data
    assert "skipped_outside_allowed_locations" in data
    assert "errors" in data
    assert "summary" in data

    txt = txt_path.read_text(encoding="utf-8")
    assert "KEPT APPS" in txt
    assert "RENAMED APPS" in txt
    assert "MISSING APPS" in txt
    assert "DELETED EXTRA APPS" in txt
    assert "SKIPPED" in txt
    del os.environ["LISTMEZO_APPS_LIST"]


# ---------------------------------------------------------------------------
# 12. BuildState counters are updated
# ---------------------------------------------------------------------------

def test_build_state_counters_updated(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    _make_app_folder(partitions_root, "system", "app", "BluetoothMidiService")
    extra = _make_app_folder(partitions_root, "product", "app", "GarbageApp")

    scanned = [
        _scanned_app("system", "app", "BluetoothMidiService",
                     "com.android.bluetoothmidiservice", partitions_root),
        _scanned_app("product", "app", "GarbageApp",
                     "com.garbage.extra.app", partitions_root),
    ]

    from factory.state.build_state import create_build_state
    state = create_build_state(tmp_path)
    reports_dir = tmp_path / "reports"

    enforce_stable_app_policy(
        reports_dir=reports_dir,
        partitions_root=partitions_root,
        scanned_apps=scanned,
        style="stable",
        build_state=state,
    )

    assert state.counters.stable_kept_apps >= 1
    assert state.counters.stable_deleted_extra_apps >= 1
    del os.environ["LISTMEZO_APPS_LIST"]


# ---------------------------------------------------------------------------
# 13. _apply_renames — rename outside allowed is skipped even in enforce mode
# ---------------------------------------------------------------------------

def test_rename_outside_allowed_skipped_even_in_stable(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    partitions_root = tmp_path / "partitions"
    # odm is outside allowed
    wrong = _make_app_folder(partitions_root, "odm", "app", "BTMidi")

    to_rename = [{
        "status": "FOUND_RENAMED",
        "action": "RENAME_TO_EXPECTED",
        "expected_name": "BluetoothMidiService",
        "actual_name": "BTMidi",
        "package": "com.android.bluetoothmidiservice",
        "partition": "odm",
        "app_type": "app",
        "found_at": str(wrong),
        "in_allowed": False,
    }]

    done, errors = _apply_renames(to_rename, enforce=True)
    assert wrong.exists(), "Rename outside allowed must not happen"
    assert not errors
    assert done[0].get("reason") == "outside allowed location"


def test_package_match_wrong_partition_report_only_not_deleted(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    wrong = _make_app_folder(partitions_root, "product", "app", "BluetoothMidiService")
    scanned = [_scanned_app("product", "app", "BluetoothMidiService", "com.android.bluetoothmidiservice", partitions_root)]
    result = enforce_stable_app_policy(tmp_path / "reports", partitions_root, scanned, "stable")
    assert wrong.exists()
    assert result["found_wrong_location_apps"]
    assert result["deleted_extra_apps"] == []
    del os.environ["LISTMEZO_APPS_LIST"]


def test_unknown_package_is_reported_not_deleted(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    unknown = _make_app_folder(partitions_root, "system", "app", "Mystery")
    scanned = [_scanned_app("system", "app", "Mystery", "unknown", partitions_root)]
    result = enforce_stable_app_policy(tmp_path / "reports", partitions_root, scanned, "stable")
    assert unknown.exists()
    assert result["unknown_package_apps"]
    assert result["delete_candidates"] == []
    del os.environ["LISTMEZO_APPS_LIST"]


def test_same_package_different_apk_name_renames_apk_not_delete(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    folder = partitions_root / "system" / "app" / "BTMidi"
    folder.mkdir(parents=True)
    (folder / "Wrong.apk").write_bytes(b"PK\x03\x04")
    scanned = [_scanned_app("system", "app", "BTMidi", "com.android.bluetoothmidiservice", partitions_root)]
    result = enforce_stable_app_policy(tmp_path / "reports", partitions_root, scanned, "stable")
    target = partitions_root / "system" / "app" / "BluetoothMidiService"
    assert target.exists()
    assert (target / "BluetoothMidiService.apk").is_file()
    assert not result["deleted_extra_apps"]
    del os.environ["LISTMEZO_APPS_LIST"]


def test_same_package_exact_folder_different_apk_name_renames_apk(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    folder = partitions_root / "system" / "app" / "BluetoothMidiService"
    folder.mkdir(parents=True)
    (folder / "Wrong.apk").write_bytes(b"PK\x03\x04")
    scanned = [_scanned_app("system", "app", "BluetoothMidiService", "com.android.bluetoothmidiservice", partitions_root)]
    result = enforce_stable_app_policy(tmp_path / "reports", partitions_root, scanned, "stable")
    assert folder.exists()
    assert (folder / "BluetoothMidiService.apk").is_file()
    assert not (folder / "Wrong.apk").exists()
    assert len(result["renamed_apps"]) == 1
    assert not result["deleted_extra_apps"]
    del os.environ["LISTMEZO_APPS_LIST"]


def test_delete_candidate_path_missing_is_skipped_not_counted_deleted(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    missing = partitions_root / "product" / "app" / "Gone"
    scanned = [_scanned_app("product", "app", "Gone", "com.extra.gone", partitions_root)]
    result = enforce_stable_app_policy(tmp_path / "reports", partitions_root, scanned, "stable")
    assert not missing.exists()
    assert result["deleted_extra_apps"] == []
    assert result["skipped_delete_apps"]
    assert result["summary"]["deleted_extra_apps"] == 0
    del os.environ["LISTMEZO_APPS_LIST"]


def test_unsafe_matching_blocks_delete_in_execute_mode(tmp_path):
    apps_list = _write_apps_list(
        tmp_path,
        "\n".join(f"App{i}\ncom.example.expected{i}" for i in range(218)),
    )
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    _make_app_folder(partitions_root, "system", "app", "App0")
    extras = []
    for i in range(175):
        _make_app_folder(partitions_root, "product", "app", f"Extra{i}")
        extras.append(_scanned_app("product", "app", f"Extra{i}", f"com.extra.{i}", partitions_root))
    scanned = [_scanned_app("system", "app", "App0", "com.example.expected0", partitions_root)] + extras

    with pytest.raises(RuntimeError, match="STABLE_APP_MATCHING_UNSAFE"):
        enforce_stable_app_policy(tmp_path / "reports", partitions_root, scanned, "stable")

    assert (partitions_root / "product" / "app" / "Extra0").exists()
    report = json.loads((tmp_path / "reports" / "stable_app_policy_report.json").read_text(encoding="utf-8"))
    assert report["safety_guard"]["status"] == "failed"
    assert report["summary"]["kept_apps"] == 1
    assert report["summary"]["missing_apps"] == 217
    assert report["summary"]["delete_candidates"] == 175
    assert report["summary"]["deleted_extra_apps"] == 0
    del os.environ["LISTMEZO_APPS_LIST"]


def test_unsafe_matching_warns_only_in_dry_run(tmp_path):
    apps_list = _write_apps_list(tmp_path, "\n".join(f"App{i}\ncom.example.expected{i}" for i in range(101)))
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    extra = _make_app_folder(partitions_root, "product", "app", "Extra")
    scanned = [_scanned_app("product", "app", "Extra", "com.extra.app", partitions_root)]

    result = enforce_stable_app_policy(tmp_path / "reports", partitions_root, scanned, "stable", dry_run=True)

    assert result["safety_guard"]["status"] == "warning"
    assert extra.exists()
    assert result["skipped_delete_apps"][0]["reason"] == "report-only mode"
    del os.environ["LISTMEZO_APPS_LIST"]


def test_env_thresholds_override_safety_defaults(tmp_path, monkeypatch):
    apps_list = _write_apps_list(tmp_path, "\n".join(f"App{i}\ncom.example.expected{i}" for i in range(90)))
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    monkeypatch.setenv("DEADZONE_STABLE_MIN_KEPT_APPS", "0")
    monkeypatch.setenv("DEADZONE_STABLE_MAX_MISSING_APPS", "100")
    monkeypatch.setenv("DEADZONE_STABLE_MAX_DELETE_CANDIDATES", "200")
    monkeypatch.setenv("DEADZONE_STABLE_MIN_MATCH_RATIO", "0")
    partitions_root = tmp_path / "partitions"
    extra = _make_app_folder(partitions_root, "product", "app", "Extra")
    scanned = [_scanned_app("product", "app", "Extra", "com.extra.app", partitions_root)]

    result = enforce_stable_app_policy(tmp_path / "reports", partitions_root, scanned, "stable")

    assert result["safety_guard"]["status"] == "passed"
    assert not extra.exists()
    del os.environ["LISTMEZO_APPS_LIST"]


def test_apps_list_parser_normalizes_duplicate_partition_prefixes(tmp_path):
    apps_list = _write_apps_list(
        tmp_path,
        """\
system/system/app
BluetoothMidiService
com.android.bluetoothmidiservice

product/product/priv-app
PrivThing
com.example.privthing

system_ext/system_ext/app/SystemExtThing
com.example.systemext
""",
    )

    parsed = _parse_expected_apps(apps_list)
    by_package = {entry["package"]: entry for entry in parsed}

    assert by_package["com.android.bluetoothmidiservice"]["partition"] == "system"
    assert by_package["com.android.bluetoothmidiservice"]["app_type"] == "app"
    assert by_package["com.android.bluetoothmidiservice"]["expected_path"] == "system/app/BluetoothMidiService"
    assert by_package["com.example.privthing"]["expected_path"] == "product/priv-app/PrivThing"
    assert by_package["com.example.privthing"]["expected_folder_name"] == "PrivThing"
    assert by_package["com.example.privthing"]["expected_package"] == "com.example.privthing"
    assert by_package["com.example.systemext"]["expected_path"] == "system_ext/app/SystemExtThing"


def test_find_apk_prefers_folder_name_then_largest_then_first(tmp_path):
    folder = tmp_path / "system" / "app" / "MainApp"
    nested = folder / "nested"
    nested.mkdir(parents=True)
    (folder / "Other.apk").write_bytes(b"1" * 50)
    (folder / "MainApp.apk").write_bytes(b"1")
    (nested / "Large.apk").write_bytes(b"1" * 200)

    assert _find_apk(folder, "MainApp").name == "MainApp.apk"
    (folder / "MainApp.apk").unlink()
    assert _find_apk(folder, "MainApp").name == "Large.apk"


def test_extract_package_falls_back_to_inventory_when_tools_unavailable_or_fail(tmp_path, monkeypatch):
    apk = tmp_path / "Broken.apk"
    apk.write_bytes(b"not an apk")
    monkeypatch.setattr("factory.core.stable_app_policy._package_from_tool", lambda _apk: ("", "unknown", "low"))

    package, source, confidence = _extract_package(apk, "com.example.inventory")

    assert package == "com.example.inventory"
    assert source == "inventory"
    assert confidence == "medium"


def test_extract_package_reads_manifest_before_inventory(tmp_path, monkeypatch):
    apk = tmp_path / "Readable.apk"
    with zipfile.ZipFile(apk, "w") as zf:
        zf.writestr("AndroidManifest.xml", '<manifest package="com.example.manifest" />')
    monkeypatch.setattr("factory.core.stable_app_policy._package_from_tool", lambda _apk: ("", "unknown", "low"))

    package, source, confidence = _extract_package(apk, "com.example.inventory")

    assert package == "com.example.manifest"
    assert source == "manifest"
    assert confidence == "medium"


def test_missing_apk_becomes_unknown_and_not_deleted(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    folder = partitions_root / "system" / "app" / "NoApk"
    folder.mkdir(parents=True)

    result = enforce_stable_app_policy(tmp_path / "reports", partitions_root, [], "stable")

    assert folder.exists()
    assert result["unknown_package_apps"]
    assert result["delete_candidates"] == []
    del os.environ["LISTMEZO_APPS_LIST"]


def test_package_first_match_in_different_folder_is_rename_not_missing(tmp_path):
    apps_list = _write_apps_list(tmp_path)
    partitions_root = tmp_path / "partitions"
    _make_app_folder(partitions_root, "system", "app", "OtherFolder")
    scanned = [_scanned_app("system", "app", "OtherFolder", "com.android.bluetoothmidiservice", partitions_root)]

    result = _classify(scanned, _parse_expected_apps(apps_list), _build_allowed_dirs(partitions_root))

    assert any(item["package"] == "com.android.bluetoothmidiservice" for item in result["to_rename"])
    assert not any(item["package"] == "com.android.bluetoothmidiservice" for item in result["missing"])


def test_matching_debug_report_and_guard_details_are_written_on_unsafe(tmp_path):
    apps_list = _write_apps_list(tmp_path, "\n".join(f"App{i}\ncom.example.expected{i}" for i in range(218)))
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list)
    partitions_root = tmp_path / "partitions"
    _make_app_folder(partitions_root, "system", "app", "App0")
    scanned = [_scanned_app("system", "app", "App0", "com.example.expected0", partitions_root)]

    with pytest.raises(RuntimeError, match="matched 1 of 218 expected apps"):
        enforce_stable_app_policy(tmp_path / "reports", partitions_root, scanned, "stable")

    debug = (tmp_path / "reports" / "stable_matching_debug_report.txt").read_text(encoding="utf-8")
    report = json.loads((tmp_path / "reports" / "stable_app_policy_report.json").read_text(encoding="utf-8"))
    assert "first 50 scanned apps" in debug
    assert "common packages between scanned and expected" in debug
    assert report["safety_guard"]["scanned_apps_count"] == 1
    assert "matched_expected_ratio below threshold" in report["safety_guard"]["reasons"]
    assert "package_tools_available" in report["safety_guard"]
    del os.environ["LISTMEZO_APPS_LIST"]
