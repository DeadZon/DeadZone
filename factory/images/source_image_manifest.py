"""Smart source image manifest for DeadZone Factory.

The manifest records every discovered ``*.img`` and decides whether it is a
source image that should be copied into the final fastboot image folder.
Classification is based on where an image came from and on broad artifact
patterns, not on a small allowlist of known device image names.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Iterable


DYNAMIC_PARTITION_NAMES: frozenset[str] = frozenset({
    "system",
    "system_ext",
    "product",
    "vendor",
    "odm",
    "mi_ext",
    "vendor_dlkm",
    "odm_dlkm",
    "system_dlkm",
})

TEMP_SUPER_IMAGE_NAMES: frozenset[str] = frozenset({
    "super.unsparse.img",
    "super_raw.img",
    "super_sparse.img",
    "super_metadata.img",
    "lpdump.img",
    "lpdump_validation.img",
})


def _norm(path: Path) -> str:
    return str(path).replace("\\", "/").lower()


def _sha256(path: Path) -> str | None:
    try:
        h = hashlib.sha256()
        with path.open("rb") as fh:
            for chunk in iter(lambda: fh.read(1024 * 1024), b""):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return None


def _is_split_super(name: str) -> bool:
    lower = name.lower()
    return bool(
        re.fullmatch(r"super\.img\.\d+", lower)
        or re.fullmatch(r"super_.*\.chunk", lower)
        or re.fullmatch(r"super.*\.chunk", lower)
        or re.fullmatch(r"super\.chunk\.\d+", lower)
    )


def _is_temp_or_validation(name: str) -> bool:
    lower = name.lower()
    return (
        lower in TEMP_SUPER_IMAGE_NAMES
        or lower.endswith(".unsparse.img")
        or "lpdump" in lower
        or "validation" in lower
    )


def _is_dynamic_name(name: str) -> bool:
    lower = name.lower()
    if not lower.endswith(".img"):
        return False
    stem = lower[:-4]
    if stem in DYNAMIC_PARTITION_NAMES:
        return True
    if stem.endswith("_a") or stem.endswith("_b"):
        return True
    return False


def _origin_for(path: Path, work_root: Path) -> str:
    p = _norm(path)
    wr = _norm(work_root)
    if f"{wr}/super_parts/" in p or f"{wr}/super_workspace/" in p:
        return "super_workspace"
    if f"{wr}/eu_adapter/" in p:
        return "generated"
    if f"{wr}/source_images/" in p:
        return "source_rom"
    if f"{wr}/unpacked_rom/images/" in p or f"{wr}/unpacked_rom/firmware-update/" in p:
        return "source_rom"
    if f"{wr}/unpacked_rom/" in p:
        return "source_rom"
    if "payload" in p:
        return "payload_dump"
    if "fastboot" in p and "images" in p:
        return "fastboot_images"
    if "validation" in p or "lpdump" in p:
        return "validation"
    return "source_rom"


def _role_for(path: Path, work_root: Path, origin: str) -> tuple[str, str]:
    name = path.name
    lower = name.lower()
    p = _norm(path)
    wr = _norm(work_root)

    if lower == "super.img":
        return "super", "super image"
    if _is_split_super(lower):
        return "split_super", "split super chunk"
    if _is_temp_or_validation(lower):
        return "validation", "validation/temp image"
    if _is_dynamic_name(lower) and (
        origin in {"super_workspace", "payload_dump"}
        or f"{wr}/super_parts/" in p
        or f"{wr}/super_workspace/" in p
    ):
        return "dynamic_partition", "dynamic partition inside super"
    if _is_dynamic_name(lower):
        return "dynamic_partition", "dynamic partition inside super"
    return "standalone", "original source image"


def _scan_roots(source_roots: Iterable[Path], work_root: Path) -> list[Path]:
    roots: list[Path] = []
    for root in source_roots:
        root = Path(root)
        if root not in roots:
            roots.append(root)

    for root in [
        work_root / "source_images",
        work_root / "unpacked_rom" / "images",
        work_root / "unpacked_rom" / "firmware-update",
        work_root / "unpacked_rom",
        work_root / "super_parts",
        work_root / "super_workspace",
        work_root / "eu_adapter",
        work_root / "fastboot_images",
    ]:
        if root not in roots:
            roots.append(root)

    found: list[Path] = []
    seen: set[str] = set()
    for root in roots:
        if not root.is_dir():
            continue
        for img in sorted(path for path in root.rglob("*") if path.is_file()):
            lower = img.name.lower()
            if not (lower.endswith(".img") or _is_split_super(lower) or lower.endswith(".chunk")):
                continue
            key = str(img.resolve())
            if key in seen:
                continue
            seen.add(key)
            found.append(img)
    return found


def _write_reports(manifest: dict, reports_dir: Path) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    json_path = reports_dir / "source_image_manifest.json"
    txt_path = reports_dir / "source_image_manifest.txt"
    json_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    included = [e for e in manifest["images"] if e["include_in_final"] and e["role"] != "super"]
    skipped = [e for e in manifest["images"] if not e["include_in_final"]]
    super_info = manifest["super_handling"]

    lines = [
        "Source Image Manifest",
        "=====================",
        "",
        "Included source images:",
    ]
    lines.extend(f"- {e['name']}" for e in sorted(included, key=lambda x: x["name"].lower()))
    if not included:
        lines.append("- (none)")
    lines += [
        "",
        "Super handling:",
        f"- original super found: {str(super_info['original_super_found']).lower()}",
        f"- final super path: {super_info.get('final_super_path') or '(none)'}",
        f"- strategy: {super_info.get('strategy')}",
        f"- exactly one super: {str(super_info.get('exactly_one_super_img')).lower()}",
        "",
        "Skipped images:",
    ]
    for e in sorted(skipped, key=lambda x: (x["role"], x["name"].lower())):
        lines.append(f"- {e['name']} - {e['reason']}")
    if not skipped:
        lines.append("- (none)")
    txt_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_source_image_manifest(
    source_roots: list[Path],
    work_root: Path,
    final_super_path: Path | None = None,
) -> dict:
    """Build and report a smart manifest for source ROM images."""
    work_root = Path(work_root)
    final_super_path = Path(final_super_path) if final_super_path else None
    final_super_exists = bool(final_super_path and final_super_path.is_file())

    entries: list[dict] = []
    original_super_found = False
    split_super_found = False
    included_names: set[str] = set()

    for img in _scan_roots(source_roots, work_root):
        origin = _origin_for(img, work_root)
        role, reason = _role_for(img, work_root, origin)
        include = role == "standalone" and origin in {
            "source_rom",
            "payload_dump",
            "fastboot_images",
        }
        if role == "super" and origin in {"source_rom", "payload_dump", "fastboot_images", "generated"}:
            original_super_found = True
        if role == "split_super":
            split_super_found = True
        if role == "dynamic_partition" and final_super_exists:
            reason = "dynamic partition inside super"
        if role in {"split_super", "validation", "temp"}:
            include = False
        if origin == "super_workspace" and role != "super":
            include = False
            if role == "standalone":
                role = "unknown"
                reason = "work/super workspace image is not source_rom"
        if include and img.name.lower() in included_names:
            include = False
            reason = "duplicate source image name"
        if include:
            included_names.add(img.name.lower())

        try:
            size = img.stat().st_size
        except OSError:
            size = 0
        entries.append({
            "name": img.name,
            "path": str(img),
            "size_bytes": size,
            "sha256": _sha256(img),
            "origin": origin,
            "role": role,
            "include_in_final": include,
            "reason": reason,
        })

    if final_super_exists and not any(
        Path(e["path"]).resolve() == final_super_path.resolve() for e in entries
    ):
        entries.append({
            "name": "super.img",
            "path": str(final_super_path),
            "size_bytes": final_super_path.stat().st_size,
            "sha256": _sha256(final_super_path),
            "origin": "generated",
            "role": "super",
            "include_in_final": True,
            "reason": "super.img already present; keeping final super",
        })

    super_entries = [e for e in entries if e["role"] == "super"]
    strategy = "rebuild_with_lpmake"
    if final_super_exists and original_super_found:
        strategy = "preserve_original_super"
    elif final_super_exists and split_super_found:
        strategy = "preserve_merged_super"
    elif final_super_exists:
        strategy = "rebuild_with_lpmake"

    manifest = {
        "work_root": str(work_root),
        "source_roots": [str(Path(p)) for p in source_roots],
        "images": sorted(entries, key=lambda e: (e["name"].lower(), e["path"])),
        "super_handling": {
            "original_super_found": original_super_found,
            "split_super_found": split_super_found,
            "final_super_path": str(final_super_path) if final_super_path else None,
            "strategy": strategy,
            "exactly_one_super_img": final_super_exists,
            "super_entry_count": len(super_entries),
        },
    }

    _write_reports(manifest, work_root.parent / "reports")
    return manifest
