"""Tests for factory.pipeline.resolver."""
import sys
import os
from pathlib import Path

# Allow running from repo root without install
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from factory.pipeline.resolver import (
    resolve_device,
    resolve_edition,
    resolve_super_size,
    resolve_output_name,
)


def test_resolve_zircon():
    device = resolve_device("zircon")
    assert device["codename"] == "zircon", f"Expected codename zircon, got {device}"
    assert device.get("soc", "").lower() in ("mtk", ""), f"Expected mtk soc, got {device}"
    assert "_warning" not in device or device["_warning"] == "", \
        f"Unexpected warning for known device: {device.get('_warning')}"


def test_resolve_garnet():
    device = resolve_device("garnet")
    assert device["codename"] == "garnet"
    assert device.get("soc", "").lower() in ("snapdragon", "")


def test_resolve_unknown_device():
    device = resolve_device("doesnotexist123")
    assert "_warning" in device
    assert "not found" in device["_warning"]


def test_resolve_edition_base():
    edition = resolve_edition("base")
    assert edition.get("id") == "base"
    assert "_warning" not in edition


def test_resolve_edition_legend():
    edition = resolve_edition("legend")
    assert edition.get("id") == "legend"
    assert "_warning" not in edition


def test_resolve_edition_gaming():
    edition = resolve_edition("gaming")
    assert edition.get("id") == "gaming"


def test_resolve_edition_epic():
    edition = resolve_edition("epic")
    assert edition.get("id") == "epic"


def test_resolve_edition_unknown():
    edition = resolve_edition("phantom")
    assert "_warning" in edition


def test_default_super_size():
    device = {"codename": "zircon", "soc": "mtk"}
    size = resolve_super_size(device, "mtk")
    assert size == 9126805504, f"Expected 9126805504, got {size}"


def test_super_size_device_override():
    device = {"codename": "custom", "soc": "mtk", "super_size": "12345678"}
    size = resolve_super_size(device, "mtk")
    assert size == 12345678


def test_output_name_base():
    name = resolve_output_name("zircon", "base")
    assert name == "DeadZone_zircon_V1", f"Got: {name}"


def test_output_name_legend():
    name = resolve_output_name("zircon", "legend")
    assert name == "DeadZone_zircon_Legend_V1", f"Got: {name}"


def test_output_name_gaming():
    name = resolve_output_name("zircon", "gaming")
    assert name == "DeadZone_zircon_Gaming_V1", f"Got: {name}"


def test_output_name_epic():
    name = resolve_output_name("zircon", "epic")
    assert name == "DeadZone_zircon_Epic_V1", f"Got: {name}"


if __name__ == "__main__":
    tests = [v for k, v in globals().items() if k.startswith("test_") and callable(v)]
    passed = failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except Exception as exc:
            print(f"  FAIL  {t.__name__}: {exc}")
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)
