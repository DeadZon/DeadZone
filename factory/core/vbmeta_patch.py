from __future__ import annotations

import struct
from pathlib import Path
from typing import Any

from factory.core.workspace import write_json

# AVB vbmeta image header constants (AvbVBMetaImageHeader from libavb)
_AVB_MAGIC = b"AVB0"
_AVB_MAGIC_LEN = 4
_AVB_FLAGS_OFFSET = 120      # byte offset of flags uint32 in the header
_AVB_FLAGS_TARGET = 3        # HASHTREE_DISABLED (1) | VERIFICATION_DISABLED (2)
_AVB_MIN_SIZE = 128          # minimum valid vbmeta image size

# Ported from tiencv2006/nothingsvn_xiaomi-toolbuild bin/patch-vbmeta.py (GPL-3.0).
# That script writes b'\x03' at offset 123 (the LSB of the big-endian uint32 flags
# field at offset 120).  DeadZone writes the full 4-byte big-endian uint32 so that
# any pre-existing non-zero upper bytes are cleared, then validates by re-reading.
#
# Why the task's "little-endian 03 00 00 00 at 0x78" is incorrect:
#   The AVB header stores all multi-byte integers in big-endian (network) byte order.
#   Writing little-endian 0x03_00_00_00 at offset 0x78 would make the flags field
#   read as 0x03000000 (50331648), not 3.  The correct encoding is big-endian
#   0x00_00_00_03, which is what struct.pack(">I", 3) produces.

_CANDIDATES = [
    {"name": "vbmeta.img",        "required": True},
    {"name": "vbmeta_system.img", "required": False},
    {"name": "vbmeta_vendor.img", "required": False},
]


def _read_flags(data: bytes) -> int:
    (val,) = struct.unpack_from(">I", data, _AVB_FLAGS_OFFSET)
    return val


def _patch_image(path: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "image": path.name,
        "path": str(path),
        "original_flags": None,
        "final_flags": None,
        "action": "failed",
        "method": "ported_binary",
        "error": None,
    }

    try:
        data = bytearray(path.read_bytes())
    except OSError as exc:
        result["error"] = f"cannot read: {exc}"
        return result

    if len(data) < _AVB_MIN_SIZE:
        result["error"] = f"too small: {len(data)} bytes (minimum {_AVB_MIN_SIZE})"
        return result

    if bytes(data[:_AVB_MAGIC_LEN]) != _AVB_MAGIC:
        result["error"] = f"invalid magic: {bytes(data[:_AVB_MAGIC_LEN])!r}"
        return result

    original = _read_flags(bytes(data))
    result["original_flags"] = original

    if original == _AVB_FLAGS_TARGET:
        result["final_flags"] = original
        result["action"] = "already_patched"
        return result

    # Write big-endian flags=3 at offset 120, clearing any stale upper bytes.
    struct.pack_into(">I", data, _AVB_FLAGS_OFFSET, _AVB_FLAGS_TARGET)

    try:
        path.write_bytes(bytes(data))
    except OSError as exc:
        result["error"] = f"cannot write: {exc}"
        return result

    final = _read_flags(bytes(data))
    result["final_flags"] = final

    if final != _AVB_FLAGS_TARGET:
        result["error"] = f"post-patch validation failed: flags={final} expected={_AVB_FLAGS_TARGET}"
        return result

    result["action"] = "patched"
    return result


def patch_vbmeta_images(
    image_dir: Path,
    reports_dir: Path | None = None,
    meta_dir: Path | None = None,
) -> list[dict[str, Any]]:
    """Patch all vbmeta images in image_dir to disable AVB verification (flags=3).

    vbmeta.img is required; vbmeta_system.img and vbmeta_vendor.img are optional.
    Raises RuntimeError if required vbmeta.img is missing or its patch fails.
    Optional images that are missing are silently skipped.
    """
    image_dir = Path(image_dir)
    results: list[dict[str, Any]] = []

    for cand in _CANDIDATES:
        name: str = cand["name"]
        required: bool = cand["required"]
        path = image_dir / name

        if not path.is_file():
            entry: dict[str, Any] = {
                "image": name,
                "path": str(path),
                "required": required,
                "found": False,
                "original_flags": None,
                "final_flags": None,
                "action": "failed" if required else "skipped_missing_optional",
                "method": "ported_binary",
                "error": "file not found" if required else None,
            }
            results.append(entry)
            if required:
                _write_reports(results, reports_dir, meta_dir)
                raise RuntimeError(f"required vbmeta image missing: {path}")
            print(f"[VBMETA] {name}: optional, not found — skipped")
            continue

        entry = _patch_image(path)
        entry["required"] = required
        entry["found"] = True
        results.append(entry)

        action = entry["action"]
        if action == "already_patched":
            print(f"[VBMETA] {name}: already patched (flags={entry['final_flags']})")
        elif action == "patched":
            print(f"[VBMETA] {name}: patched flags {entry['original_flags']} → {entry['final_flags']}")
        else:
            print(f"[VBMETA] {name}: FAILED — {entry.get('error')}")
            if required:
                _write_reports(results, reports_dir, meta_dir)
                raise RuntimeError(
                    f"vbmeta patch failed for {name}: {entry.get('error', 'unknown')}"
                )

    _write_reports(results, reports_dir, meta_dir)
    return results


def _write_reports(
    results: list[dict[str, Any]],
    reports_dir: Path | None,
    meta_dir: Path | None,
) -> None:
    if reports_dir is not None:
        reports_dir = Path(reports_dir)
        reports_dir.mkdir(parents=True, exist_ok=True)
        lines = ["DeadZone vbmeta patch report", ""]
        for r in results:
            lines += [
                f"image:          {r['image']}",
                f"path:           {r['path']}",
                f"required:       {r.get('required', '?')}",
                f"found:          {r.get('found', '?')}",
                f"original_flags: {r.get('original_flags')}",
                f"final_flags:    {r.get('final_flags')}",
                f"action:         {r['action']}",
                f"method:         {r['method']}",
            ]
            if r.get("error"):
                lines.append(f"error:          {r['error']}")
            lines.append("")
        (reports_dir / "vbmeta_patch_report.txt").write_text(
            "\n".join(lines), encoding="utf-8"
        )

    if meta_dir is not None:
        meta_dir = Path(meta_dir)
        meta_dir.mkdir(parents=True, exist_ok=True)
        write_json(
            meta_dir / "vbmeta_patch.json",
            {"vbmeta_patch": results},
        )
