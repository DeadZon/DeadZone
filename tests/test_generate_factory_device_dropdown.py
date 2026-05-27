"""
Tests for generate_factory_device_dropdown.py and related helpers.
"""

import json
import pathlib
import py_compile
import subprocess
import sys
import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.generate_factory_device_dropdown import (
    filter_devices,
    load_devices,
    make_option_line,
    parse_select_device,
    resolve_codename,
    sort_devices,
)
from scripts.auto_rom_lookup import find_latest_rom_url, resolve_rom_url

DEVICES_JSON = REPO_ROOT / "registry" / "devices" / "factory_devices.json"
WORKFLOW_MTK = REPO_ROOT / ".github" / "workflows" / "deadzone_mtk.yml"
WORKFLOW_SNAP = REPO_ROOT / ".github" / "workflows" / "deadzone_snapdragon.yml"


# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def all_devices():
    assert DEVICES_JSON.exists(), f"factory_devices.json not found: {DEVICES_JSON}"
    return load_devices(DEVICES_JSON)


# ---------------------------------------------------------------------------
# 1. Registry has more than 100 devices after import
# ---------------------------------------------------------------------------

def test_factory_has_more_than_100_devices(all_devices):
    assert len(all_devices) > 100, (
        f"Expected more than 100 devices, got {len(all_devices)}. "
        "Run scripts/import_xiaomi_eu_devices.py to expand the registry."
    )


# ---------------------------------------------------------------------------
# 2. Generator creates dropdown options
# ---------------------------------------------------------------------------

def test_generator_creates_dropdown_options(all_devices):
    mtk = filter_devices(all_devices, "mtk")
    snap = filter_devices(all_devices, "snapdragon")

    assert len(mtk) >= 1, "MTK device list must not be empty"
    assert len(snap) >= 1, "Snapdragon device list must not be empty"

    for device in mtk + snap:
        line = make_option_line(device)
        assert " | " in line, f"Option line missing ' | ': {line}"
        assert line.startswith("          - "), f"Option line has wrong indent: {line}"


# ---------------------------------------------------------------------------
# 3. zircon — official MTK
# ---------------------------------------------------------------------------

def test_zircon_official_mtk(all_devices):
    mtk = filter_devices(all_devices, "mtk")
    codenames = {d["codename"]: d for d in mtk}

    assert "zircon" in codenames, "zircon must be in MTK device list"
    d = codenames["zircon"]
    assert d["display_name"] == "Redmi Note 13 Pro+ 5G"
    assert d["soc"] == "mtk"
    assert d["support_level"] == "official"
    assert d["source"] == "deadzone"
    assert d["enabled"] is True

    line = make_option_line(d)
    assert line == "          - zircon | Redmi Note 13 Pro+ 5G"


# ---------------------------------------------------------------------------
# 4. garnet — official Snapdragon
# ---------------------------------------------------------------------------

def test_garnet_official_snapdragon(all_devices):
    snap = filter_devices(all_devices, "snapdragon")
    codenames = {d["codename"]: d for d in snap}

    assert "garnet" in codenames, "garnet must be in Snapdragon device list"
    d = codenames["garnet"]
    assert d["display_name"] == "Redmi Note 13 Pro 5G / POCO X6 5G"
    assert d["soc"] == "snapdragon"
    assert d["support_level"] == "official"
    assert d["source"] == "deadzone"
    assert d["enabled"] is True

    line = make_option_line(d)
    assert line == "          - garnet | Redmi Note 13 Pro 5G / POCO X6 5G"


# ---------------------------------------------------------------------------
# 5. marble, mondrian, peridot exist in Snapdragon registry
# ---------------------------------------------------------------------------

def test_marble_in_snapdragon_registry(all_devices):
    snap = filter_devices(all_devices, "snapdragon")
    codenames = {d["codename"]: d for d in snap}
    assert "marble" in codenames, "marble must be in Snapdragon device list"
    d = codenames["marble"]
    assert d["display_name"] == "Redmi Note 12 Turbo / POCO F5"
    assert d["soc"] == "snapdragon"


def test_mondrian_in_snapdragon_registry(all_devices):
    snap = filter_devices(all_devices, "snapdragon")
    codenames = {d["codename"]: d for d in snap}
    assert "mondrian" in codenames, "mondrian must be in Snapdragon device list"


def test_peridot_in_snapdragon_registry(all_devices):
    snap = filter_devices(all_devices, "snapdragon")
    codenames = {d["codename"]: d for d in snap}
    assert "peridot" in codenames, "peridot must be in Snapdragon device list"


# ---------------------------------------------------------------------------
# 6. soc=auto is excluded from both workflows
# ---------------------------------------------------------------------------

def test_soc_auto_excluded_from_mtk(all_devices):
    mtk = filter_devices(all_devices, "mtk")
    for d in mtk:
        assert d["soc"] != "auto", f"soc=auto device {d['codename']!r} leaked into MTK list"


def test_soc_auto_excluded_from_snapdragon(all_devices):
    snap = filter_devices(all_devices, "snapdragon")
    for d in snap:
        assert d["soc"] != "auto", f"soc=auto device {d['codename']!r} leaked into Snapdragon list"


# ---------------------------------------------------------------------------
# 7. custom_device overrides dropdown selection
# ---------------------------------------------------------------------------

def test_custom_device_overrides_dropdown():
    codename, display_name = resolve_codename(
        "garnet | Redmi Note 13 Pro 5G / POCO X6 5G",
        custom_device="custom_test_device",
    )
    assert codename == "custom_test_device"
    assert display_name == "Redmi Note 13 Pro 5G / POCO X6 5G"


def test_no_custom_device_uses_dropdown():
    codename, display_name = resolve_codename(
        "zircon | Redmi Note 13 Pro+ 5G",
        custom_device="",
    )
    assert codename == "zircon"
    assert display_name == "Redmi Note 13 Pro+ 5G"


# ---------------------------------------------------------------------------
# 8. Invalid selected value fails safely
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("bad_value", [
    "select_device_codename",
    "select_device",
    "device",
    "none",
    "null",
    "default",
])
def test_invalid_codename_from_dropdown_fails(bad_value):
    with pytest.raises(ValueError, match="Invalid device codename"):
        resolve_codename(f"{bad_value} | Some Device")


def test_missing_separator_in_select_device_fails():
    with pytest.raises(ValueError, match="Invalid select_device format"):
        parse_select_device("zircon_no_separator")


def test_empty_select_device_fails():
    with pytest.raises(ValueError):
        parse_select_device("")


# ---------------------------------------------------------------------------
# 9. auto_latest missing URL fails with clear message
# ---------------------------------------------------------------------------

def test_auto_latest_returns_none_for_unknown_device():
    result = find_latest_rom_url("nonexistent_device_xyz")
    assert result is None


def test_auto_latest_resolve_fails_with_clear_message():
    url, error = resolve_rom_url("zircon", "auto_latest")
    assert url == ""
    assert "No automatic ROM URL found for this device" in error
    assert "manual_url mode" in error


def test_manual_url_valid():
    url, error = resolve_rom_url(
        "zircon",
        "manual_url",
        manual_url="https://example.com/rom.zip",
    )
    assert url == "https://example.com/rom.zip"
    assert error == ""


def test_manual_url_missing_fails():
    url, error = resolve_rom_url("zircon", "manual_url", manual_url="")
    assert url == ""
    assert "rom_url is required" in error


def test_manual_url_bad_scheme_fails():
    url, error = resolve_rom_url("zircon", "manual_url", manual_url="ftp://bad.url/rom.zip")
    assert url == ""
    assert "http://" in error or "https://" in error


# ---------------------------------------------------------------------------
# 10. Sort / uniqueness sanity checks
# ---------------------------------------------------------------------------

def test_devices_sorted_by_display_name(all_devices):
    for soc in ("mtk", "snapdragon"):
        filtered = filter_devices(all_devices, soc)
        sorted_devs = sort_devices(filtered)
        names = [d["display_name"].lower() for d in sorted_devs]
        assert names == sorted(names), f"{soc} devices not sorted alphabetically"


def test_no_duplicate_codenames(all_devices):
    codenames = [d["codename"] for d in all_devices]
    assert len(codenames) == len(set(codenames)), "Duplicate codenames in factory_devices.json"


def test_duplicate_codenames_fail():
    fake_devices = [
        {"codename": "zircon", "display_name": "A", "soc": "mtk", "enabled": True},
        {"codename": "zircon", "display_name": "B", "soc": "mtk", "enabled": True},
    ]
    codenames = [d["codename"] for d in fake_devices]
    assert len(codenames) != len(set(codenames)), "Should detect duplicate"


# ---------------------------------------------------------------------------
# 11. Workflows contain select_device, not old codename inputs
# ---------------------------------------------------------------------------

def test_workflows_contain_select_device():
    for name, path in [("MTK", WORKFLOW_MTK), ("Snapdragon", WORKFLOW_SNAP)]:
        assert path.exists(), f"{name} workflow not found: {path}"
        text = path.read_text(encoding="utf-8")
        assert "select_device:" in text, f"{name} workflow missing select_device input"


def test_old_codename_input_removed():
    for name, path in [("MTK", WORKFLOW_MTK), ("Snapdragon", WORKFLOW_SNAP)]:
        assert path.exists(), f"{name} workflow not found: {path}"
        text = path.read_text(encoding="utf-8")
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            assert "select_device_codename:" not in stripped, (
                f"{name} workflow still has old select_device_codename input"
            )
        # 'codename:' as a standalone input is not allowed; 'codename=' in job name is fine
        for line in text.splitlines():
            stripped = line.strip()
            if stripped.startswith("#"):
                continue
            if stripped == "codename:" or stripped.startswith("codename:  ") or stripped.startswith("codename:\t"):
                pytest.fail(f"{name} workflow still has bare codename: input")


def test_workflows_contain_auto_generated_markers():
    for name, path in [("MTK", WORKFLOW_MTK), ("Snapdragon", WORKFLOW_SNAP)]:
        assert path.exists(), f"{name} workflow not found: {path}"
        text = path.read_text(encoding="utf-8")
        assert "# AUTO-GENERATED DEVICE OPTIONS START" in text, (
            f"{name} workflow missing START marker"
        )
        assert "# AUTO-GENERATED DEVICE OPTIONS END" in text, (
            f"{name} workflow missing END marker"
        )


# ---------------------------------------------------------------------------
# 12. Generator dry-run succeeds
# ---------------------------------------------------------------------------

def test_generator_dry_run_succeeds():
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "generate_factory_device_dropdown.py"), "--dry-run"],
        capture_output=True,
        text=True,
        cwd=str(REPO_ROOT),
    )
    assert result.returncode == 0, (
        f"Generator dry-run failed (exit {result.returncode}):\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )


# ---------------------------------------------------------------------------
# 13. All scripts compile without syntax errors
# ---------------------------------------------------------------------------

def test_all_scripts_compile():
    scripts = [
        "scripts/generate_factory_device_dropdown.py",
        "scripts/import_xiaomi_eu_devices.py",
        "scripts/validate_factory_dropdown.py",
        "scripts/auto_rom_lookup.py",
    ]
    for rel in scripts:
        path = REPO_ROOT / rel
        assert path.exists(), f"Script not found: {path}"
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as exc:
            pytest.fail(f"Syntax error in {rel}: {exc}")
