from __future__ import annotations

import struct
from pathlib import Path
from unittest.mock import MagicMock, call, patch

import pytest

from factory.core import final_zip as fz_module
from factory.core.final_zip import (
    CORE_IMAGES,
    OPTIONAL_CORE_IMAGES,
    _copy_images,
    _validate_zip,
    build_final_zip,
)
from factory.core.workspace import Workspace

# ── helpers ───────────────────────────────────────────────────────────────────

def _make_vbmeta(flags: int = 0, size: int = 256) -> bytes:
    data = bytearray(size)
    data[0:4] = b"AVB0"
    struct.pack_into(">I", data, 120, flags)
    return bytes(data)


def _read_flags(path: Path) -> int:
    data = path.read_bytes()
    (val,) = struct.unpack_from(">I", data, 120)
    return val


def _make_ws(tmp_path: Path) -> Workspace:
    dirs = {
        "root": tmp_path / "ws",
        "input": tmp_path / "ws/input",
        "extracted": tmp_path / "ws/extracted",
        "images": tmp_path / "ws/images",
        "partitions": tmp_path / "ws/partitions",
        "meta": tmp_path / "ws/meta",
        "reports": tmp_path / "ws/reports",
        "logs": tmp_path / "ws/logs",
        "final": tmp_path / "final",
    }
    for p in dirs.values():
        Path(p).mkdir(parents=True, exist_ok=True)
    return Workspace(**{k: Path(v) for k, v in dirs.items()})


# ── integration: build_final_zip calls patch_vbmeta_images ───────────────────

def test_build_final_zip_calls_vbmeta_patch(tmp_path):
    """build_final_zip must call patch_vbmeta_images with ws.images."""
    ws = _make_ws(tmp_path)
    info = MagicMock()
    info.codename = "zircon"
    info.android_version = "14"
    info.build = "V816.0.8.0.UNACNXM"
    info.soc = "mtk"
    info.slot_mode = "VAB"

    captured = {}

    def fake_patch(image_dir, reports_dir=None, meta_dir=None):
        captured["image_dir"] = image_dir
        captured["reports_dir"] = reports_dir
        captured["meta_dir"] = meta_dir
        return []

    with patch.object(fz_module, "patch_vbmeta_images", side_effect=fake_patch):
        with patch.object(fz_module, "_load_profile", return_value={"super": {}}):
            with patch.object(fz_module, "load_policy", return_value={}):
                with patch.object(fz_module, "_copy_images", return_value=([], [])):
                    with patch.object(fz_module, "_copy_windows_tools", return_value=[]):
                        with patch.object(fz_module, "_write_scripts", return_value=[]):
                            with patch.object(fz_module, "_validate_zip", return_value=[]):
                                with patch.object(fz_module, "_write_report"):
                                    with patch.object(fz_module, "_sha256", return_value="abc"):
                                        with patch.object(fz_module, "_write_sidecars"):
                                            with patch.object(fz_module, "write_json"):
                                                try:
                                                    build_final_zip(ws, info, "legend")
                                                except Exception:
                                                    pass  # zip creation may fail in tmp env

    assert "image_dir" in captured, "patch_vbmeta_images was never called"
    assert Path(captured["image_dir"]) == ws.images


def test_build_final_zip_propagates_vbmeta_patch_failure(tmp_path):
    """build_final_zip must propagate RuntimeError from patch_vbmeta_images."""
    ws = _make_ws(tmp_path)
    info = MagicMock()
    info.codename = "zircon"
    info.android_version = "14"
    info.build = "V816.0.8.0.UNACNXM"
    info.soc = "mtk"
    info.slot_mode = "VAB"

    def fail_patch(image_dir, reports_dir=None, meta_dir=None):
        raise RuntimeError("required vbmeta image missing: vbmeta.img")

    with patch.object(fz_module, "patch_vbmeta_images", side_effect=fail_patch):
        with patch.object(fz_module, "_load_profile", return_value={"super": {}}):
            with patch.object(fz_module, "load_policy", return_value={}):
                with pytest.raises(RuntimeError, match="vbmeta"):
                    build_final_zip(ws, info, "legend")


def test_build_final_zip_passes_reports_and_meta_dirs(tmp_path):
    """patch_vbmeta_images must receive ws.reports and ws.meta."""
    ws = _make_ws(tmp_path)
    info = MagicMock()
    info.codename = "zircon"
    info.android_version = "14"
    info.build = "V816.0.8.0.UNACNXM"
    info.soc = "mtk"
    info.slot_mode = "VAB"

    captured: dict = {}

    def fake_patch(image_dir, reports_dir=None, meta_dir=None):
        captured.update(
            image_dir=Path(image_dir),
            reports_dir=Path(reports_dir) if reports_dir else None,
            meta_dir=Path(meta_dir) if meta_dir else None,
        )
        return []

    with patch.object(fz_module, "patch_vbmeta_images", side_effect=fake_patch):
        with patch.object(fz_module, "_load_profile", return_value={"super": {}}):
            with patch.object(fz_module, "load_policy", return_value={}):
                with patch.object(fz_module, "_copy_images", return_value=([], [])):
                    with patch.object(fz_module, "_copy_windows_tools", return_value=[]):
                        with patch.object(fz_module, "_write_scripts", return_value=[]):
                            with patch.object(fz_module, "_validate_zip", return_value=[]):
                                with patch.object(fz_module, "_write_report"):
                                    with patch.object(fz_module, "_sha256", return_value="abc"):
                                        with patch.object(fz_module, "_write_sidecars"):
                                            with patch.object(fz_module, "write_json"):
                                                try:
                                                    build_final_zip(ws, info, "legend")
                                                except Exception:
                                                    pass

    assert captured.get("reports_dir") == ws.reports
    assert captured.get("meta_dir") == ws.meta


# ── vbmeta image is patched before packaging ──────────────────────────────────

def test_vbmeta_is_patched_before_packaging(tmp_path):
    """After patch_vbmeta_images runs, vbmeta.img in ws.images has flags=3."""
    ws = _make_ws(tmp_path)
    vbmeta = ws.images / "vbmeta.img"
    vbmeta.write_bytes(_make_vbmeta(flags=0))

    from factory.core.vbmeta_patch import patch_vbmeta_images
    patch_vbmeta_images(ws.images, ws.reports, ws.meta)

    assert _read_flags(vbmeta) == 3


def test_vbmeta_patch_report_written_via_full_patch_call(tmp_path):
    """patch_vbmeta_images writes vbmeta_patch_report.txt to reports_dir."""
    ws = _make_ws(tmp_path)
    (ws.images / "vbmeta.img").write_bytes(_make_vbmeta(flags=0))

    from factory.core.vbmeta_patch import patch_vbmeta_images
    patch_vbmeta_images(ws.images, ws.reports, ws.meta)

    assert (ws.reports / "vbmeta_patch_report.txt").is_file()


def test_vbmeta_patch_json_written_via_full_patch_call(tmp_path):
    """patch_vbmeta_images writes vbmeta_patch.json to meta_dir."""
    ws = _make_ws(tmp_path)
    (ws.images / "vbmeta.img").write_bytes(_make_vbmeta(flags=0))

    from factory.core.vbmeta_patch import patch_vbmeta_images
    patch_vbmeta_images(ws.images, ws.reports, ws.meta)

    assert (ws.meta / "vbmeta_patch.json").is_file()


# ── optional vbmeta images ────────────────────────────────────────────────────

_REQUIRED_IMAGES = [img for img in CORE_IMAGES if img not in OPTIONAL_CORE_IMAGES]


def _make_required_images(directory: Path) -> None:
    """Write 1-byte placeholder files for every non-optional CORE_IMAGE."""
    for name in _REQUIRED_IMAGES:
        (directory / name).write_bytes(b"\x00")


def test_copy_images_does_not_fail_when_optional_vbmeta_absent(tmp_path):
    """_copy_images must not raise when vbmeta_system.img/vbmeta_vendor.img are missing."""
    ws = _make_ws(tmp_path)
    _make_required_images(ws.images)
    # optional vbmeta images intentionally absent
    assert not (ws.images / "vbmeta_system.img").exists()
    assert not (ws.images / "vbmeta_vendor.img").exists()

    stage = tmp_path / "stage"
    (stage / "images").mkdir(parents=True)
    included, excluded = _copy_images(ws, stage, {})
    # required images were copied; optional ones are simply absent — no error
    assert "vbmeta.img" in included


def test_copy_images_includes_optional_vbmeta_when_present(tmp_path):
    """_copy_images copies optional vbmeta images when they exist."""
    ws = _make_ws(tmp_path)
    _make_required_images(ws.images)
    (ws.images / "vbmeta_system.img").write_bytes(b"\x00")
    (ws.images / "vbmeta_vendor.img").write_bytes(b"\x00")

    stage = tmp_path / "stage"
    (stage / "images").mkdir(parents=True)
    included, _ = _copy_images(ws, stage, {})
    assert "vbmeta_system.img" in included
    assert "vbmeta_vendor.img" in included


def test_validate_zip_passes_without_optional_vbmeta(tmp_path):
    """_validate_zip must not report missing optional vbmeta images."""
    import zipfile

    ws = _make_ws(tmp_path)
    _make_required_images(ws.images)

    # Build a minimal ZIP that contains only the required (non-optional) images.
    stage = tmp_path / "stage"
    (stage / "images").mkdir(parents=True)
    for name in _REQUIRED_IMAGES:
        (stage / "images" / name).write_bytes(b"\x00")

    zip_path = tmp_path / "test.zip"
    with zipfile.ZipFile(zip_path, "w") as zf:
        for name in _REQUIRED_IMAGES:
            zf.write(stage / "images" / name, f"images/{name}")

    errors = _validate_zip(zip_path, _REQUIRED_IMAGES, {}, has_super=True)
    optional_errors = [e for e in errors if "vbmeta_system" in e or "vbmeta_vendor" in e]
    assert optional_errors == [], f"optional vbmeta images must not be required: {optional_errors}"


def test_vbmeta_patch_report_in_ws_reports_on_patch_failure(tmp_path):
    """When vbmeta patching fails, vbmeta_patch_report.txt exists in ws.reports."""
    ws = _make_ws(tmp_path)
    # vbmeta.img intentionally absent — patch will fail and write report
    with pytest.raises(RuntimeError, match="vbmeta"):
        from factory.core.vbmeta_patch import patch_vbmeta_images
        patch_vbmeta_images(ws.images, ws.reports, ws.meta)

    assert (ws.reports / "vbmeta_patch_report.txt").is_file()
