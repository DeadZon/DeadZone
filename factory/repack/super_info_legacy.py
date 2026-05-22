"""Legacy-compatible super metadata loading helpers."""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[2]
_LEGACY_ROOT = _REPO_ROOT / "third_party" / "mezo_core"
_LEGACY_SRC = _LEGACY_ROOT / "src"

if str(_LEGACY_ROOT) not in sys.path:
    sys.path.insert(0, str(_LEGACY_ROOT))
if str(_LEGACY_SRC) not in sys.path:
    sys.path.insert(0, str(_LEGACY_SRC))

try:
    from core.lpunpack import get_info as lpunpack_get_info  # type: ignore
except Exception:  # pragma: no cover - reported at runtime
    lpunpack_get_info = None  # type: ignore


_ZIRCON_SUPER_SIZE: int = 9126805504
_ZIRCON_SUPER_GROUP_BASENAME: str = "qti_dynamic_partitions"
_LP_METADATA_OVERHEAD: int = 4 * 1024 * 1024

# Devices with a hardcoded super profile (no SuperConfig / registry entry required).
_DEVICE_SUPER_PROFILES: dict[str, dict[str, object]] = {
    "zircon": {
        "super_size": _ZIRCON_SUPER_SIZE,
        "group_basename": _ZIRCON_SUPER_GROUP_BASENAME,
        "metadata_slots": 3,
        "slot_mode": "vab",
        "output_format": "sparse",
    },
}


def _read_json(path: Path) -> dict[str, Any] | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    return data if isinstance(data, dict) else None


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=4, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def _read_parts_info(project_dir: Path) -> dict[str, Any]:
    return _read_json(project_dir / "config" / "parts_info") or {}


def _find_super_img(search_dir: Path) -> Path | None:
    exact_matches: list[Path] = []
    partial_matches: list[Path] = []
    if not search_dir.is_dir():
        return None
    for path in search_dir.rglob("*"):
        if not path.is_file():
            continue
        lower_name = path.name.lower()
        if lower_name == "super.img":
            exact_matches.append(path)
        elif lower_name.startswith("super") and lower_name.endswith(".img"):
            partial_matches.append(path)
    if exact_matches:
        return exact_matches[0]
    if partial_matches:
        return partial_matches[0]
    return None


def _save_super_config_files(project_dir: Path, super_info: dict[str, Any]) -> None:
    config_dir = project_dir / "config"
    _write_json(config_dir / "super", super_info)
    parts_info_path = config_dir / "parts_info"
    parts_info = _read_json(parts_info_path) or {}
    if "super_info" not in parts_info:
        parts_info["super_info"] = super_info
        _write_json(parts_info_path, parts_info)


def _load_super_info_from_payload_manifest(
    project_dir: Path,
    super_size_override: int | None = None,
) -> tuple[dict[str, Any] | None, list[str]]:
    """Extract dynamic partition metadata from payload.bin manifest.

    ``super_size_override`` — when provided, this value is used as the block
    device size instead of the manifest's group size.  Pass the device-specific
    verified super partition size (e.g., 9126805504 for zircon) so that lpmake
    receives the correct block-device capacity.  Without this the group size
    (logical group capacity) would be used as the block-device size, which is
    typically a few MiB short of the actual partition.
    """
    warnings: list[str] = []
    try:
        from core.payload_extract import init_payload_info  # type: ignore
    except Exception as exc:
        warnings.append(f"Could not import payload_extract: {exc}")
        return None, warnings

    search_roots = [project_dir / "rom", project_dir]
    payload_candidates: list[Path] = []
    for root in search_roots:
        if root.is_dir():
            try:
                payload_candidates.extend(p for p in root.rglob("payload.bin") if p.is_file())
            except Exception:
                pass

    seen: set[str] = set()
    unique_payloads: list[Path] = []
    for path in payload_candidates:
        key = str(path)
        if key not in seen:
            seen.add(key)
            unique_payloads.append(path)

    if not unique_payloads:
        warnings.append("No payload.bin found for dynamic partition metadata recovery")
        return None, warnings

    for payload_path in unique_payloads:
        try:
            with payload_path.open("rb") as file:
                manifest = init_payload_info(file)
            dpm = getattr(manifest, "dynamic_partition_metadata", None)
            if dpm is None or not dpm.groups:
                warnings.append(f"Payload manifest has no dynamic partition metadata: {payload_path}")
                continue

            main_group = None
            for group in dpm.groups:
                if not group.name or group.name == "default":
                    continue
                if main_group is None or group.size > main_group.size:
                    main_group = group

            if main_group is None or main_group.size <= 0:
                warnings.append(f"Payload manifest has no valid dynamic partition group: {payload_path}")
                continue

            group_name = str(main_group.name)
            # Strip _a/_b suffix from group name if present
            if group_name.endswith("_a") or group_name.endswith("_b"):
                group_name = group_name[:-2]

            manifest_group_size = int(main_group.size)
            part_names = list(main_group.partition_names) if main_group.partition_names else []
            if not part_names:
                warnings.append(f"Payload manifest group has no partition names: {payload_path}")
                continue

            # Use the caller-supplied device size when available; otherwise fall back
            # to the manifest group size (legacy behaviour, may be slightly too small).
            block_device_size = super_size_override if super_size_override and super_size_override > 0 else manifest_group_size
            if super_size_override and super_size_override != manifest_group_size:
                warnings.append(
                    f"Using super_size_override={super_size_override} "
                    f"(manifest group size was {manifest_group_size})"
                )

            # Normalise partition names: strip slot suffix, deduplicate.
            normalised: list[str] = []
            seen_parts: set[str] = set()
            for p in part_names:
                base = p[:-2] if (p.endswith("_a") or p.endswith("_b")) else p
                if base not in seen_parts:
                    seen_parts.add(base)
                    normalised.append(base)

            return {
                "metadata_slot_count": 3,
                "block_devices": [{"name": "super", "size": block_device_size}],
                "group_table": [{"name": f"{group_name}_a"}, {"name": f"{group_name}_b"}],
                "partition_table": [{"name": f"{part}_a"} for part in normalised],
                "_manifest_group_size": manifest_group_size,
            }, warnings
        except Exception as exc:
            warnings.append(f"Could not parse payload manifest {payload_path.name}: {exc}")

    return None, warnings


def _load_device_hardcoded_fallback(device: str | None) -> tuple[dict[str, Any] | None, list[str]]:
    """Return a hardcoded super profile for devices not in SuperConfig / registry.

    Covers zircon and any other device added to _DEVICE_SUPER_PROFILES.
    """
    warnings: list[str] = []
    key = (device or "").strip().lower()
    if not key or key not in _DEVICE_SUPER_PROFILES:
        return None, warnings
    prof = _DEVICE_SUPER_PROFILES[key]
    super_size = int(prof["super_size"])  # type: ignore[arg-type]
    group_basename = str(prof["group_basename"])
    metadata_slots = int(prof.get("metadata_slots", 3))  # type: ignore[arg-type]
    warnings.append(
        f"Using hardcoded super profile for device '{key}': "
        f"super_size={super_size}, group={group_basename}"
    )
    return {
        "metadata_slot_count": metadata_slots,
        "block_devices": [{"name": "super", "size": super_size}],
        "group_table": [{"name": f"{group_basename}_a"}, {"name": f"{group_basename}_b"}],
        "partition_table": [],
        "slot_mode": str(prof.get("slot_mode", "vab")),
        "virtual_ab": str(prof.get("slot_mode", "vab")).lower() == "vab",
        "output_format": str(prof.get("output_format", "sparse")),
    }, warnings


def _load_registry_super(device: str | None, soc: str | None) -> tuple[dict[str, Any] | None, list[str]]:
    warnings: list[str] = []
    factory_codename = (device or os.environ.get("DEADZONE_DEVICE_CODENAME", "")).strip()
    factory_soc = (soc or os.environ.get("DEADZONE_SOC", "")).strip()
    if not factory_codename or not factory_soc:
        return None, warnings

    reg_path = _REPO_ROOT / "registry" / "devices" / factory_soc / f"{factory_codename}.yml"
    if not reg_path.is_file():
        warnings.append(f"Registry device profile not found: {reg_path}")
        return None, warnings

    try:
        import yaml  # type: ignore
    except Exception as exc:
        warnings.append(f"yaml is not available; skipping registry super profile: {exc}")
        return None, warnings

    try:
        reg_data = yaml.safe_load(reg_path.read_text(encoding="utf-8"))
        reg_super = reg_data.get("super", {}) if isinstance(reg_data, dict) else {}
        verified_size = reg_super.get("super_size") or reg_super.get("verified_size")
        if verified_size and int(verified_size) > 0:
            group = reg_super.get("dynamic_group", "qti_dynamic_partitions")
            return {
                "metadata_slot_count": int(reg_super.get("metadata_slots", 3)),
                "block_devices": [{"name": "super", "size": int(verified_size)}],
                "group_table": [{"name": f"{group}_a"}, {"name": f"{group}_b"}],
                "partition_table": [],
                "slot_mode": reg_super.get("slot_mode"),
                "virtual_ab": str(reg_super.get("slot_mode", "")).lower() == "vab",
                "output_format": reg_super.get("output_format"),
            }, warnings
        warnings.append(f"Registry profile has no verified super_size: {reg_path}")
    except Exception as exc:
        warnings.append(f"Registry super profile check failed: {exc}")
    return None, warnings


def _load_superconfig(device: str | None) -> tuple[dict[str, Any] | None, list[str]]:
    warnings: list[str] = []
    device_name = (device or os.environ.get("DEADZONE_DEVICE_CODENAME", "")).strip()
    if not device_name:
        return None, warnings
    device_dir = _LEGACY_ROOT / "SuperConfig" / device_name
    super_path = device_dir / "super"
    if super_path.is_file():
        data = _read_json(super_path)
        if data is not None:
            return data, warnings
        warnings.append(f"Could not read SuperConfig super file: {super_path}")
    parts_info_path = device_dir / "parts_info"
    parts_info = _read_json(parts_info_path)
    if isinstance(parts_info, dict) and isinstance(parts_info.get("super_info"), dict):
        return parts_info["super_info"], warnings
    return None, warnings


def _annotate_super_info(info: dict[str, Any], source: str) -> dict[str, Any]:
    result = dict(info)
    result["_super_info_source"] = source
    return result


def load_super_info_legacy(
    project_dir: Path,
    images_dir: Path,
    device: str | None = None,
    soc: str | None = None,
    platform: str | None = None,
    execute: bool = False,
) -> dict[str, Any]:
    """Load super metadata using the legacy fallback order."""
    project_dir = Path(project_dir).resolve()
    images_dir = Path(images_dir).resolve()
    warnings: list[str] = []
    errors: list[str] = []
    platform = platform

    parts_info = _read_parts_info(project_dir)
    super_info = parts_info.get("super_info")
    if isinstance(super_info, dict):
        return _annotate_super_info(super_info, "existing_config")

    super_config = project_dir / "config" / "super"
    data = _read_json(super_config) if super_config.exists() else None
    if data is not None:
        return _annotate_super_info(data, "existing_config")

    for candidate in [project_dir / "super_raw.img", project_dir / "super.img"]:
        if candidate.exists():
            if lpunpack_get_info is None:
                errors.append("lpunpack get_info is not available")
                break
            info = lpunpack_get_info(str(candidate))
            if execute:
                _save_super_config_files(project_dir, info)
            return _annotate_super_info(info, "manual")

    for search_dir in [project_dir / "rom", project_dir / "rom" / "payload_extracted", images_dir]:
        found = _find_super_img(search_dir)
        if found and found.is_file() and found.stat().st_size > 0:
            if lpunpack_get_info is None:
                errors.append("lpunpack get_info is not available")
                break
            info = lpunpack_get_info(str(found))
            if execute:
                _save_super_config_files(project_dir, info)
            return _annotate_super_info(info, "manual")

    # When the device has a known hardcoded profile (e.g., zircon), use that
    # super_size to override the block device size reported by the payload manifest.
    device_profile, _ = _load_device_hardcoded_fallback(device)
    super_size_override: int | None = None
    if device_profile:
        bd = device_profile.get("block_devices") or []
        if bd and isinstance(bd[0], dict):
            super_size_override = int(bd[0].get("size", 0) or 0) or None

    payload_info, payload_warnings = _load_super_info_from_payload_manifest(
        project_dir, super_size_override=super_size_override
    )
    warnings.extend(payload_warnings)
    if payload_info is not None:
        if execute:
            _save_super_config_files(project_dir, payload_info)
        return _annotate_super_info(payload_info, "payload_manifest")

    superconfig_info, superconfig_warnings = _load_superconfig(device)
    warnings.extend(superconfig_warnings)
    if superconfig_info is not None:
        if execute:
            _save_super_config_files(project_dir, superconfig_info)
        return _annotate_super_info(superconfig_info, "existing_config")

    registry_info, registry_warnings = _load_registry_super(device, soc)
    warnings.extend(registry_warnings)
    if registry_info is not None:
        if execute:
            _save_super_config_files(project_dir, registry_info)
        return _annotate_super_info(registry_info, "registry")

    # Last resort: use the hardcoded device profile (covers zircon and other
    # devices not yet in SuperConfig or the registry).
    if device_profile is not None:
        if execute:
            _save_super_config_files(project_dir, device_profile)
        return _annotate_super_info(device_profile, "device_hardcoded_fallback")

    return {
        "_super_info_source": "missing",
        "warnings": warnings,
        "errors": errors,
    }
