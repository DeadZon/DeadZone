from __future__ import annotations

import os
import shutil
import tarfile
import zipfile
from pathlib import Path

from factory.core.detector import RomInfo
from factory.core.workspace import Workspace, write_json


def _safe_destination(root: Path, member_name: str) -> Path:
    root_abs = root.resolve()
    target = (root / member_name).resolve()
    if os.path.commonpath([str(root_abs), str(target)]) != str(root_abs):
        raise RuntimeError(f"archive member escapes workspace: {member_name}")
    return target


def _extract_zip_safe(src: Path, dst: Path) -> None:
    with zipfile.ZipFile(src) as zf:
        for info in zf.infolist():
            _safe_destination(dst, info.filename)
        zf.extractall(dst)


def _extract_tar_safe(src: Path, dst: Path) -> None:
    with tarfile.open(src, "r:*") as tf:
        for member in tf.getmembers():
            _safe_destination(dst, member.name)
        tf.extractall(dst)


def _extract_archive(src: Path, dst: Path) -> None:
    dst.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    elif zipfile.is_zipfile(src):
        _extract_zip_safe(src, dst)
    elif tarfile.is_tarfile(src):
        _extract_tar_safe(src, dst)
    else:
        shutil.copy2(src, dst / src.name)


def unpack_rom(source: Path, info: RomInfo, ws: Workspace) -> dict:
    """Compatibility wrapper: delegates to deadzone_smart_unpack (Phase 5).

    Old callers that pass a RomInfo continue to work.  The RomInfo argument
    is accepted but not used for routing — deadzone_smart_unpack auto-detects
    the input type and selects the correct route, so the two paths no longer
    compete.

    Returns a legacy-compatible dict with keys:
      adapter         – "smart_unpack:<route>"
      images          – list of image filenames found in ws.images
      partition_sizes – {} (sizes are not carried through the smart unpack path;
                        inspect_workspace falls back to workspace_scan mode)
      smart_unpack    – full deadzone_smart_unpack result dict

    Raises RuntimeError with a clear message if the input is unsupported or
    required partitions are missing.
    """
    from factory.core.smart_unpack import deadzone_smart_unpack as _smart_unpack
    print("[UNPACK] delegating to deadzone_smart_unpack")
    result = _smart_unpack(source, ws)
    status = result.get("status", "FAILED")
    if status in ("FAILED", "UNSUPPORTED"):
        error = result.get("error") or f"smart unpack status: {status}"
        missing = result.get("missing_required") or []
        if missing:
            error += f" — missing required: {', '.join(sorted(missing))}"
        raise RuntimeError(f"[UNPACK] {error}")
    images_dict = result.get("images") or {}
    images_list = [Path(v).name for v in images_dict.values() if v]
    legacy = {
        "adapter": f"smart_unpack:{result.get('route', 'unknown')}",
        "images": images_list,
        "partition_sizes": {},
        "smart_unpack": result,
    }
    write_json(ws.meta / "unpack_result.json", legacy)
    print(f"[UNPACK] Adapter: {legacy['adapter']}")
    print(f"[UNPACK] Images: {len(images_list)}")
    return legacy
