from __future__ import annotations

import json
import struct
from pathlib import Path

import pytest

from factory.core.vbmeta_patch import (
    _AVB_FLAGS_OFFSET,
    _AVB_FLAGS_TARGET,
    _AVB_MIN_SIZE,
    patch_vbmeta_images,
)

# ── helpers ───────────────────────────────────────────────────────────────────

def _make_vbmeta(flags: int = 0, size: int = 256) -> bytes:
    """Build a minimal fake vbmeta image with the given flags."""
    data = bytearray(size)
    data[0:4] = b"AVB0"
    struct.pack_into(">I", data, _AVB_FLAGS_OFFSET, flags)
    return bytes(data)


def _read_flags(path: Path) -> int:
    data = path.read_bytes()
    (val,) = struct.unpack_from(">I", data, _AVB_FLAGS_OFFSET)
    return val


# ── patch logic ───────────────────────────────────────────────────────────────

def test_patch_sets_flags_to_3(tmp_path):
    img = tmp_path / "vbmeta.img"
    img.write_bytes(_make_vbmeta(flags=0))

    results = patch_vbmeta_images(tmp_path)

    assert results[0]["action"] == "patched"
    assert results[0]["final_flags"] == _AVB_FLAGS_TARGET
    assert _read_flags(img) == 3


def test_already_patched_passes(tmp_path):
    img = tmp_path / "vbmeta.img"
    img.write_bytes(_make_vbmeta(flags=_AVB_FLAGS_TARGET))

    results = patch_vbmeta_images(tmp_path)

    assert results[0]["action"] == "already_patched"
    assert results[0]["final_flags"] == _AVB_FLAGS_TARGET
    assert _read_flags(img) == 3


def test_missing_required_vbmeta_fails(tmp_path):
    with pytest.raises(RuntimeError, match="required vbmeta image missing"):
        patch_vbmeta_images(tmp_path)


def test_missing_optional_vbmeta_system_is_skipped(tmp_path):
    (tmp_path / "vbmeta.img").write_bytes(_make_vbmeta())
    # vbmeta_system.img is absent

    results = patch_vbmeta_images(tmp_path)

    system_result = next(r for r in results if r["image"] == "vbmeta_system.img")
    assert system_result["action"] == "skipped_missing_optional"
    assert system_result["found"] is False
    assert system_result["error"] is None


def test_missing_optional_vbmeta_vendor_is_skipped(tmp_path):
    (tmp_path / "vbmeta.img").write_bytes(_make_vbmeta())
    # vbmeta_vendor.img is absent

    results = patch_vbmeta_images(tmp_path)

    vendor_result = next(r for r in results if r["image"] == "vbmeta_vendor.img")
    assert vendor_result["action"] == "skipped_missing_optional"
    assert vendor_result["found"] is False
    assert vendor_result["error"] is None


def test_too_small_image_fails_clearly(tmp_path):
    img = tmp_path / "vbmeta.img"
    img.write_bytes(b"AVB0" + b"\x00" * 10)  # only 14 bytes

    with pytest.raises(RuntimeError, match="vbmeta patch failed"):
        patch_vbmeta_images(tmp_path)


def test_invalid_magic_fails_clearly(tmp_path):
    img = tmp_path / "vbmeta.img"
    data = bytearray(_make_vbmeta())
    data[0:4] = b"XXXX"
    img.write_bytes(bytes(data))

    with pytest.raises(RuntimeError, match="vbmeta patch failed"):
        patch_vbmeta_images(tmp_path)


def test_optional_images_patched_when_present(tmp_path):
    for name in ("vbmeta.img", "vbmeta_system.img", "vbmeta_vendor.img"):
        (tmp_path / name).write_bytes(_make_vbmeta(flags=0))

    results = patch_vbmeta_images(tmp_path)

    for r in results:
        assert r["action"] == "patched"
        assert r["final_flags"] == 3


# ── reports ───────────────────────────────────────────────────────────────────

def test_vbmeta_patch_report_is_written(tmp_path):
    img_dir = tmp_path / "images"
    img_dir.mkdir()
    (img_dir / "vbmeta.img").write_bytes(_make_vbmeta())

    reports_dir = tmp_path / "reports"
    patch_vbmeta_images(img_dir, reports_dir=reports_dir)

    report = reports_dir / "vbmeta_patch_report.txt"
    assert report.is_file()
    content = report.read_text(encoding="utf-8")
    assert "vbmeta.img" in content
    assert "patched" in content


def test_vbmeta_patch_json_is_written(tmp_path):
    img_dir = tmp_path / "images"
    img_dir.mkdir()
    (img_dir / "vbmeta.img").write_bytes(_make_vbmeta())

    meta_dir = tmp_path / "meta"
    patch_vbmeta_images(img_dir, meta_dir=meta_dir)

    meta_file = meta_dir / "vbmeta_patch.json"
    assert meta_file.is_file()
    data = json.loads(meta_file.read_text(encoding="utf-8"))
    assert "vbmeta_patch" in data
    assert isinstance(data["vbmeta_patch"], list)


def test_report_includes_all_three_candidates(tmp_path):
    img_dir = tmp_path / "images"
    img_dir.mkdir()
    (img_dir / "vbmeta.img").write_bytes(_make_vbmeta())

    reports_dir = tmp_path / "reports"
    meta_dir = tmp_path / "meta"
    results = patch_vbmeta_images(img_dir, reports_dir=reports_dir, meta_dir=meta_dir)

    names = [r["image"] for r in results]
    assert "vbmeta.img" in names
    assert "vbmeta_system.img" in names
    assert "vbmeta_vendor.img" in names


def test_result_has_required_fields(tmp_path):
    (tmp_path / "vbmeta.img").write_bytes(_make_vbmeta())

    results = patch_vbmeta_images(tmp_path)

    required_keys = {"image", "path", "required", "found", "original_flags",
                     "final_flags", "action", "method", "error"}
    for r in results:
        assert required_keys <= r.keys(), f"missing keys in {r}"


def test_vbmeta_img_is_marked_required(tmp_path):
    (tmp_path / "vbmeta.img").write_bytes(_make_vbmeta())

    results = patch_vbmeta_images(tmp_path)

    main = next(r for r in results if r["image"] == "vbmeta.img")
    assert main["required"] is True


def test_optional_images_marked_not_required(tmp_path):
    (tmp_path / "vbmeta.img").write_bytes(_make_vbmeta())

    results = patch_vbmeta_images(tmp_path)

    for r in results:
        if r["image"] in ("vbmeta_system.img", "vbmeta_vendor.img"):
            assert r["required"] is False


def test_report_written_when_vbmeta_img_missing(tmp_path):
    img_dir = tmp_path / "images"
    img_dir.mkdir()
    reports_dir = tmp_path / "reports"
    # vbmeta.img is absent — required, so patch_vbmeta_images must raise AND
    # write the report before raising.
    with pytest.raises(RuntimeError, match="required vbmeta image missing"):
        patch_vbmeta_images(img_dir, reports_dir=reports_dir)

    report = reports_dir / "vbmeta_patch_report.txt"
    assert report.is_file(), "vbmeta_patch_report.txt must be written before raising"
    content = report.read_text(encoding="utf-8")
    assert "vbmeta.img" in content
    assert "failed" in content
