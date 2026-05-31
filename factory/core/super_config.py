"""DeadZone SuperConfig — HyperUR_Build_CN_V21 imported reference.

Provides lookup of known super partition layout for devices whose SuperConfig
was imported from HyperUR_Build_CN_V21. SuperConfig data lives under:
    third_party/mezo_core/SuperConfig/<codename>/super
    third_party/mezo_core/SuperConfig/<codename>/parts_info

Priority in super_profile resolution:
    1. Explicit device registry config (if complete and verified)
    2. HyperUR/MEZO SuperConfig by codename  ← this module
    3. Payload/super metadata inspection
    4. Safe fallback only if verified
    5. BLOCKED if not enough data

Developer: Mezo
SuperConfig source: HyperUR_Build_CN_V21 imported reference
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

_SUPERCONFIG_ROOT = Path(__file__).parent.parent.parent / "third_party" / "mezo_core" / "SuperConfig"

_DYNAMIC_PARTITION_NAMES = {
    "system", "product", "vendor", "system_ext", "mi_ext",
    "odm", "vendor_dlkm", "system_dlkm", "odm_dlkm",
}

STATUS_READY = "READY_SUPERCONFIG"
STATUS_NEEDS_INSPECTION = "NEEDS_INSPECTION"
STATUS_BLOCKED = "BLOCKED"


def _base_name(name: str) -> str:
    return name.removesuffix("_a").removesuffix("_b")


def _load_super_json(codename: str) -> dict[str, Any]:
    """Load raw super JSON for codename. Tries parts_info (super_info key) then super file."""
    codename_clean = codename.strip().lower()
    device_dir = _SUPERCONFIG_ROOT / codename_clean
    if not device_dir.is_dir():
        return {}

    # parts_info has super_info embedded
    parts_info_path = device_dir / "parts_info"
    if parts_info_path.is_file():
        try:
            data = json.loads(parts_info_path.read_text(encoding="utf-8"))
            if isinstance(data, dict) and "super_info" in data:
                return data["super_info"]
        except Exception:
            pass

    # Fall back to standalone super file
    super_path = device_dir / "super"
    if super_path.is_file():
        try:
            data = json.loads(super_path.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except Exception:
            pass

    return {}


def _load_fs_types(codename: str) -> dict[str, str]:
    """Load filesystem type map from parts_info for a codename."""
    codename_clean = codename.strip().lower()
    parts_info_path = _SUPERCONFIG_ROOT / codename_clean / "parts_info"
    if not parts_info_path.is_file():
        return {}
    try:
        data = json.loads(parts_info_path.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            return {}
        return {k: v for k, v in data.items() if k != "super_info" and isinstance(v, str)}
    except Exception:
        return {}


def _parse_super_info(super_info: dict[str, Any], codename: str) -> dict[str, Any]:
    """Parse raw lpdump-format super JSON into a normalized SuperConfig dict."""
    if not super_info:
        return {}

    block_devices: list[dict[str, Any]] = super_info.get("block_devices") or []
    group_table: list[dict[str, Any]] = super_info.get("group_table") or []
    partition_table: list[dict[str, Any]] = super_info.get("partition_table") or []
    header_flags: str = str(super_info.get("header_flags") or "")
    metadata_slot_count: int = int(super_info.get("metadata_slot_count") or 0)
    metadata_max_size: int = int(super_info.get("metadata_max_size") or 65536)

    # Super size from first block device
    super_size = 0
    block_device_name = "super"
    if block_devices:
        bd = block_devices[0]
        super_size = int(bd.get("size") or 0)
        block_device_name = str(bd.get("name") or "super")

    # Slot mode: VAB if virtual_ab_device in flags or metadata_slot_count == 3
    is_vab = "virtual_ab" in header_flags.lower() or metadata_slot_count == 3
    slot_mode = "VAB" if is_vab else ("A/B" if metadata_slot_count == 2 else "A-only")
    metadata_slots = metadata_slot_count if metadata_slot_count >= 2 else (3 if is_vab else 2)

    # Group name: first non-default group, strip _a/_b
    group_name = "qti_dynamic_partitions"
    group_size = 0
    for grp in group_table:
        name = str(grp.get("name") or "")
        if name and name.lower() != "default":
            group_name = _base_name(name)
            group_size = int(grp.get("maximum_size") or 0)
            break

    # Partitions: collect _a entries (real images); _b entries are VAB placeholders
    partitions: dict[str, dict[str, Any]] = {}
    vab_placeholders: list[str] = []

    for entry in partition_table:
        raw_name = str(entry.get("name") or "")
        base = _base_name(raw_name)
        if base not in _DYNAMIC_PARTITION_NAMES:
            continue
        size = int(entry.get("size") or 0)
        extents = entry.get("extents") or []

        if raw_name.endswith("_b"):
            # VAB placeholder — size may be 0, that is valid
            vab_placeholders.append(base)
            partitions.setdefault(base, {})
            partitions[base]["vab_b_size"] = size
            partitions[base]["vab_b_extents_empty"] = (len(extents) == 0)
        else:
            entry_group = str(entry.get("group_name") or group_name)
            partitions[base] = {
                **partitions.get(base, {}),
                "name": base,
                "size": size,
                "group_name": _base_name(entry_group),
                "readonly": "readonly" in str(entry.get("attributes") or ""),
                "has_extents": bool(extents),
            }

    # Validate: partitions must have at least system
    if "system" not in partitions:
        return {}

    has_vab_placeholders = bool(vab_placeholders)

    return {
        "codename": codename.strip().lower(),
        "super_size": super_size,
        "block_device_name": block_device_name,
        "metadata_slots": metadata_slots,
        "metadata_size": metadata_max_size,
        "slot_mode": slot_mode,
        "is_vab": is_vab,
        "dynamic_group_name": group_name,
        "group_name": group_name,
        "group_size": group_size,
        "partitions": partitions,
        "partition_names": sorted(partitions.keys()),
        "partition_count": len(partitions),
        "has_vab_placeholders": has_vab_placeholders,
        "vab_placeholder_partitions": sorted(set(vab_placeholders)),
    }


def load_super_config(codename: str) -> dict[str, Any]:
    """Load and parse SuperConfig for a device codename. Returns {} if not found."""
    raw = _load_super_json(codename)
    if not raw:
        return {}
    return _parse_super_info(raw, codename)


def list_known_codenames() -> list[str]:
    """Return all codenames that have a SuperConfig entry."""
    if not _SUPERCONFIG_ROOT.is_dir():
        return []
    return sorted(d.name for d in _SUPERCONFIG_ROOT.iterdir() if d.is_dir())


def resolve_super_config_for_device(
    codename: str,
    soc: str = "",
    rom_metadata: Any = None,
) -> dict[str, Any]:
    """Resolve super config for a device.

    Returns a standardized dict with keys:
        source, codename, slot_mode, super_size, group_name,
        metadata_slots, partitions, status, is_vab, ...

    Status values:
        READY_SUPERCONFIG  — full config found and valid
        NEEDS_INSPECTION   — no SuperConfig entry; must inspect payload
        BLOCKED            — entry exists but is incomplete/invalid
    """
    codename_clean = str(codename or "").strip().lower()
    if not codename_clean:
        return {
            "source": "none",
            "codename": "",
            "status": STATUS_NEEDS_INSPECTION,
            "reason": "no codename provided",
        }

    config = load_super_config(codename_clean)

    if not config:
        return {
            "source": "none",
            "codename": codename_clean,
            "soc": soc,
            "status": STATUS_NEEDS_INSPECTION,
            "reason": f"no SuperConfig entry for '{codename_clean}'",
        }

    # Validate minimum required fields
    if not config.get("super_size") or not config.get("partitions"):
        return {
            "source": "hyperur_superconfig",
            "codename": codename_clean,
            "soc": soc,
            "status": STATUS_BLOCKED,
            "reason": "SuperConfig entry exists but is missing super_size or partitions",
            "raw_config": config,
        }

    fs_types = _load_fs_types(codename_clean)

    return {
        "source": "hyperur_superconfig",
        "source_label": "HyperUR_Build_CN_V21 imported reference",
        "codename": codename_clean,
        "soc": soc,
        "slot_mode": config["slot_mode"],
        "is_vab": config["is_vab"],
        "super_size": config["super_size"],
        "block_device_name": config.get("block_device_name", "super"),
        "group_name": config["group_name"],
        "dynamic_group_name": config["group_name"],
        "group_size": config.get("group_size", 0),
        "metadata_slots": config["metadata_slots"],
        "metadata_size": config.get("metadata_size", 65536),
        "partitions": config["partitions"],
        "partition_names": config["partition_names"],
        "partition_count": config["partition_count"],
        "has_vab_placeholders": config.get("has_vab_placeholders", False),
        "vab_placeholder_partitions": config.get("vab_placeholder_partitions", []),
        "fs_types": fs_types,
        "status": STATUS_READY,
        "reason": "full SuperConfig found",
    }


def build_super_config_matrix() -> list[dict[str, Any]]:
    """Build device matrix for all known SuperConfig codenames."""
    rows: list[dict[str, Any]] = []
    for codename in list_known_codenames():
        config = load_super_config(codename)
        if config:
            rows.append({
                "codename": codename,
                "soc": "",
                "super_config_source": "hyperur_superconfig",
                "slot_mode": config.get("slot_mode", ""),
                "dynamic_group": config.get("group_name", ""),
                "super_size": config.get("super_size", 0),
                "partition_count": config.get("partition_count", 0),
                "has_vab_placeholders": config.get("has_vab_placeholders", False),
                "status": STATUS_READY,
            })
        else:
            rows.append({
                "codename": codename,
                "soc": "",
                "super_config_source": "none",
                "slot_mode": "",
                "dynamic_group": "",
                "super_size": 0,
                "partition_count": 0,
                "has_vab_placeholders": False,
                "status": STATUS_BLOCKED,
            })
    return rows


def write_super_config_matrix_reports(output_dir: Path) -> tuple[Path, Path]:
    """Write superconfig_device_matrix.txt and .json to output_dir.

    Returns (txt_path, json_path).
    """
    import json as _json
    output_dir.mkdir(parents=True, exist_ok=True)
    matrix = build_super_config_matrix()

    json_path = output_dir / "superconfig_device_matrix.json"
    json_path.write_text(
        _json.dumps(
            {
                "report": "DeadZone SuperConfig Device Matrix",
                "developer": "Mezo",
                "super_config_source": "HyperUR_Build_CN_V21 imported reference",
                "total_devices": len(matrix),
                "ready_count": sum(1 for r in matrix if r["status"] == STATUS_READY),
                "needs_inspection_count": sum(1 for r in matrix if r["status"] == STATUS_NEEDS_INSPECTION),
                "blocked_count": sum(1 for r in matrix if r["status"] == STATUS_BLOCKED),
                "devices": matrix,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    lines = [
        "DeadZone SuperConfig Device Matrix",
        "===================================",
        "Developer: Mezo",
        "SuperConfig source: HyperUR_Build_CN_V21 imported reference",
        f"Total devices: {len(matrix)}",
        f"READY_SUPERCONFIG: {sum(1 for r in matrix if r['status'] == STATUS_READY)}",
        f"NEEDS_INSPECTION:  {sum(1 for r in matrix if r['status'] == STATUS_NEEDS_INSPECTION)}",
        f"BLOCKED:           {sum(1 for r in matrix if r['status'] == STATUS_BLOCKED)}",
        "",
        f"{'codename':<20} {'slot_mode':<10} {'dynamic_group':<30} {'super_size':<15} {'parts':<6} {'vab_ph':<7} status",
        "-" * 110,
    ]
    for row in matrix:
        lines.append(
            f"{row['codename']:<20} {row['slot_mode']:<10} {row['dynamic_group']:<30} "
            f"{row['super_size']:<15} {row['partition_count']:<6} {str(row['has_vab_placeholders']):<7} {row['status']}"
        )

    txt_path = output_dir / "superconfig_device_matrix.txt"
    txt_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    return txt_path, json_path
