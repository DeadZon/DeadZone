from __future__ import annotations

import tempfile
from pathlib import Path

from factory.reports.app_inventory import _parse_apps_list, compare_app_policy


SAMPLE_APPS_LIST = """\
system/system/priv-app/

BackupRestoreConfirmation
com.android.backupconfirm

Shell
com.android.shell

Telecom
com.android.server.telecom


system/system/app

BluetoothMidiService
com.android.bluetoothmidiservice

EasterEgg
com.android.egg

product / app

Calculator
com.miui.calculator

FileExplorer
com.android.fileexplorer
"""

SCANNED_APPS = [
    {
        "partition": "system",
        "name": "BackupRestoreConfirmation",
        "path": "priv-app/BackupRestoreConfirmation",
        "type": "priv-app",
        "package_name": "com.android.backupconfirm",
        "size": 1000,
    },
    {
        "partition": "system",
        "name": "Shell",
        "path": "priv-app/Shell",
        "type": "priv-app",
        "package_name": "com.android.shell",
        "size": 500,
    },
    {
        "partition": "system",
        "name": "BluetoothMidiService",
        "path": "app/BluetoothMidiService",
        "type": "app",
        "package_name": "com.android.bluetoothmidiservice",
        "size": 800,
    },
    {
        "partition": "product",
        "name": "Calculator",
        "path": "app/Calculator",
        "type": "app",
        "package_name": "com.miui.calculator",
        "size": 2000,
    },
    {
        "partition": "product",
        "name": "ExtraUnwantedApp",
        "path": "app/ExtraUnwantedApp",
        "type": "app",
        "package_name": "com.some.extra.app",
        "size": 3000,
    },
]


def _write_apps_list(tmp: Path, content: str) -> Path:
    p = tmp / "apps.list"
    p.write_text(content, encoding="utf-8")
    return p


def test_parse_apps_list_returns_entries():
    tmp = Path(tempfile.mkdtemp())
    p = _write_apps_list(tmp, SAMPLE_APPS_LIST)
    entries = _parse_apps_list(p)
    packages = {e["package"] for e in entries}
    assert "com.android.backupconfirm" in packages
    assert "com.android.shell" in packages
    assert "com.android.bluetoothmidiservice" in packages
    assert "com.miui.calculator" in packages


def test_parse_apps_list_skips_section_headers():
    tmp = Path(tempfile.mkdtemp())
    p = _write_apps_list(tmp, SAMPLE_APPS_LIST)
    entries = _parse_apps_list(p)
    names = {e["name"] for e in entries}
    assert "system" not in names
    assert "product" not in names
    assert "or" not in names


def test_parse_apps_list_normalizes_expected_paths():
    tmp = Path(tempfile.mkdtemp())
    p = _write_apps_list(
        tmp,
        """\
system/system/app
BluetoothMidiService
com.android.bluetoothmidiservice

product/product/priv-app/ProductPriv
com.example.productpriv
""",
    )
    entries = _parse_apps_list(p)
    by_package = {e["package"]: e for e in entries}

    assert by_package["com.android.bluetoothmidiservice"]["expected_path"] == "system/app/BluetoothMidiService"
    assert by_package["com.example.productpriv"]["partition"] == "product"
    assert by_package["com.example.productpriv"]["app_type"] == "priv-app"
    assert by_package["com.example.productpriv"]["expected_path"] == "product/priv-app/ProductPriv"


def test_compare_finds_default_found():
    tmp = Path(tempfile.mkdtemp())
    apps_list_path = _write_apps_list(tmp, SAMPLE_APPS_LIST)
    import os
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list_path)
    try:
        result = compare_app_policy(tmp / "reports", SCANNED_APPS)
        counters = result["counters"]
        assert counters["default_found"] >= 3
    finally:
        del os.environ["LISTMEZO_APPS_LIST"]


def test_compare_marks_missing_apps():
    tmp = Path(tempfile.mkdtemp())
    apps_list_path = _write_apps_list(tmp, SAMPLE_APPS_LIST)
    import os
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list_path)
    try:
        result = compare_app_policy(tmp / "reports", SCANNED_APPS)
        missing = result["missing"]
        missing_packages = {m["package"] for m in missing}
        # EasterEgg and FileExplorer are in apps.list but not in SCANNED_APPS
        assert "com.android.egg" in missing_packages or "com.android.fileexplorer" in missing_packages
    finally:
        del os.environ["LISTMEZO_APPS_LIST"]


def test_compare_marks_delete_candidates():
    tmp = Path(tempfile.mkdtemp())
    apps_list_path = _write_apps_list(tmp, SAMPLE_APPS_LIST)
    import os
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list_path)
    try:
        result = compare_app_policy(tmp / "reports", SCANNED_APPS)
        extra = result["extra"]
        extra_packages = {e["package"] for e in extra}
        assert "com.some.extra.app" in extra_packages
        assert all(e["status"] == "DELETE_CANDIDATE" for e in extra)
    finally:
        del os.environ["LISTMEZO_APPS_LIST"]


def test_compare_writes_txt_report():
    tmp = Path(tempfile.mkdtemp())
    apps_list_path = _write_apps_list(tmp, SAMPLE_APPS_LIST)
    import os
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list_path)
    try:
        compare_app_policy(tmp / "reports", SCANNED_APPS)
        report = tmp / "reports" / "app_inventory_report.txt"
        assert report.is_file()
        content = report.read_text(encoding="utf-8")
        assert "DEFAULT FOUND" in content
        assert "DELETE CANDIDATE" in content or "EXTRA" in content
        assert "MISSING" in content
    finally:
        del os.environ["LISTMEZO_APPS_LIST"]


def test_compare_writes_json_report():
    tmp = Path(tempfile.mkdtemp())
    apps_list_path = _write_apps_list(tmp, SAMPLE_APPS_LIST)
    import os, json
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list_path)
    try:
        compare_app_policy(tmp / "reports", SCANNED_APPS)
        json_report = tmp / "reports" / "app_inventory_report.json"
        assert json_report.is_file()
        data = json.loads(json_report.read_text(encoding="utf-8"))
        assert "counters" in data
        assert "found" in data
        assert "extra" in data
        assert "missing" in data
    finally:
        del os.environ["LISTMEZO_APPS_LIST"]


def test_compare_updates_build_state_counters():
    tmp = Path(tempfile.mkdtemp())
    apps_list_path = _write_apps_list(tmp, SAMPLE_APPS_LIST)
    import os
    os.environ["LISTMEZO_APPS_LIST"] = str(apps_list_path)
    from factory.state.build_state import create_build_state
    state = create_build_state(tmp)
    try:
        compare_app_policy(tmp / "reports", SCANNED_APPS, build_state=state)
        assert state.counters.default_found >= 1
        assert state.counters.delete_candidates >= 1
    finally:
        del os.environ["LISTMEZO_APPS_LIST"]


def test_compare_skips_gracefully_without_apps_list():
    tmp = Path(tempfile.mkdtemp())
    import os
    # Point env var at a guaranteed non-existent path
    nonexistent = str(tmp / "no_such_apps.list")
    os.environ["LISTMEZO_APPS_LIST"] = nonexistent
    # Temporarily override absolute fallback by patching the module constant
    import factory.reports.app_inventory as mod
    orig = mod._APPS_LIST_ABSOLUTE
    mod._APPS_LIST_ABSOLUTE = str(tmp / "also_nonexistent.list")
    try:
        result = compare_app_policy(tmp / "reports", SCANNED_APPS)
        assert result["status"] in ("skipped", "failed")
    finally:
        del os.environ["LISTMEZO_APPS_LIST"]
        mod._APPS_LIST_ABSOLUTE = orig
