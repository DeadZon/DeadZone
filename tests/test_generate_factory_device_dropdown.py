"""
Tests for generate_factory_device_dropdown.py and related helpers.
"""

import json
import pathlib
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


# ---------------------------------------------------------------------------
# Fixture
# ---------------------------------------------------------------------------

@pytest.fixture(scope="module")
def all_devices():
    assert DEVICES_JSON.exists(), f"factory_devices.json not found: {DEVICES_JSON}"
    return load_devices(DEVICES_JSON)


# ---------------------------------------------------------------------------
# 1. Generator creates dropdown options
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
# 2. zircon resolves correctly (MTK, official)
# ---------------------------------------------------------------------------

def test_zircon_resolves_correctly(all_devices):
    mtk = filter_devices(all_devices, "mtk")
    codenames = {d["codename"]: d for d in mtk}

    assert "zircon" in codenames, "zircon must be in MTK device list"
    d = codenames["zircon"]
    assert d["display_name"] == "Redmi Note 13 Pro+ 5G"
    assert d["soc"] == "mtk"
    assert d["support_level"] == "official"
    assert d["enabled"] is True

    line = make_option_line(d)
    assert line == "          - zircon | Redmi Note 13 Pro+ 5G"


# ---------------------------------------------------------------------------
# 3. garnet resolves correctly (Snapdragon, official)
# ---------------------------------------------------------------------------

def test_garnet_resolves_correctly(all_devices):
    snap = filter_devices(all_devices, "snapdragon")
    codenames = {d["codename"]: d for d in snap}

    assert "garnet" in codenames, "garnet must be in Snapdragon device list"
    d = codenames["garnet"]
    assert d["display_name"] == "Redmi Note 13 Pro 5G / POCO X6 5G"
    assert d["soc"] == "snapdragon"
    assert d["support_level"] == "official"
    assert d["enabled"] is True

    line = make_option_line(d)
    assert line == "          - garnet | Redmi Note 13 Pro 5G / POCO X6 5G"


# ---------------------------------------------------------------------------
# 4. marble resolves correctly from Snapdragon registry
# ---------------------------------------------------------------------------

def test_marble_resolves_in_snapdragon_registry(all_devices):
    snap = filter_devices(all_devices, "snapdragon")
    codenames = {d["codename"]: d for d in snap}

    assert "marble" in codenames, "marble must be in Snapdragon device list"
    d = codenames["marble"]
    assert d["display_name"] == "Redmi Note 12 Turbo / POCO F5"
    assert d["soc"] == "snapdragon"
    assert d["source"] == "deadzone"


# ---------------------------------------------------------------------------
# 5. custom_device overrides dropdown selection
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
# 6. Invalid selected value fails safely
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
# 7. auto_latest missing URL fails with clear message
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
# Sort / uniqueness sanity checks
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
