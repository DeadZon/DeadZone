"""Registry resolver — maps codename + edition to a full BuildContext."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Optional

_REPO_ROOT = Path(__file__).resolve().parents[2]
_REGISTRY = _REPO_ROOT / "registry"

_EDITION_SUFFIX: dict[str, str] = {
    "base": "",
    "gaming": "Gaming",
    "legend": "Legend",
    "epic": "Epic",
}


def resolve_output_name(codename: str, edition: str) -> str:
    """Return canonical output name: DeadZone_<codename>[_<Edition>]_V1."""
    suffix = _EDITION_SUFFIX.get(edition.lower(), edition.capitalize())
    if suffix:
        return f"DeadZone_{codename}_{suffix}_V1"
    return f"DeadZone_{codename}_V1"


def _load_yaml_simple(path: Path) -> dict:
    """Minimal YAML loader (key: value only, no deps) for registry files."""
    try:
        import yaml
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except ImportError:
        pass
    data: dict = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            v = v.strip()
            if v and not v.startswith("{") and not v.startswith("["):
                data[k.strip()] = v
    return data


def resolve_device(codename: str, soc_hint: Optional[str] = None) -> dict[str, Any]:
    """Resolve device profile from registry.

    Search order:
    1. registry/devices/<soc>/<codename>.yml (if soc_hint or auto-detect)
    2. registry/device_groups/mtk.yml + snapdragon.yml
    3. Fallback: codename only, soc unknown
    """
    codename = codename.strip().lower()

    # Try device-specific file
    for soc_dir in ["mtk", "snapdragon"]:
        if soc_hint and soc_dir != soc_hint.lower():
            continue
        device_file = _REGISTRY / "devices" / soc_dir / f"{codename}.yml"
        if device_file.is_file():
            data = _load_yaml_simple(device_file)
            data.setdefault("codename", codename)
            data.setdefault("soc", soc_dir)
            data["_source"] = str(device_file)
            return data

    # Search device_groups
    for group_file in [_REGISTRY / "device_groups" / "mtk.yml",
                       _REGISTRY / "device_groups" / "snapdragon.yml"]:
        if not group_file.is_file():
            continue
        try:
            import yaml
            group = yaml.safe_load(group_file.read_text(encoding="utf-8")) or {}
        except ImportError:
            group = {}
        soc_id = group_file.stem  # "mtk" or "snapdragon"
        for entry in group.get("devices", []):
            if isinstance(entry, dict) and entry.get("codename", "").lower() == codename:
                entry = dict(entry)
                entry.setdefault("soc", soc_id)
                entry["_source"] = str(group_file)
                return entry

    # Unknown device — return minimal stub so pipeline can still attempt
    return {
        "codename": codename,
        "soc": soc_hint or "unknown",
        "_source": "fallback",
        "_warning": f"Device '{codename}' not found in registry",
    }


def resolve_edition(edition: str) -> dict[str, Any]:
    """Load edition profile from registry/editions/<edition>.yml."""
    edition = edition.strip().lower()
    edition_file = _REGISTRY / "editions" / f"{edition}.yml"
    if edition_file.is_file():
        data = _load_yaml_simple(edition_file)
        data.setdefault("id", edition)
        return data
    return {
        "id": edition,
        "_warning": f"Edition '{edition}' not found in registry/editions/",
    }


def resolve_super_size(device_profile: dict, soc: str) -> int:
    """Return super_size: device override > soc default > hardcoded fallback."""
    if "super_size" in device_profile:
        try:
            return int(device_profile["super_size"])
        except (ValueError, TypeError):
            pass
    soc_file = _REGISTRY / "soc" / f"{soc.lower()}.yml"
    if soc_file.is_file():
        soc_data = _load_yaml_simple(soc_file)
        defaults = soc_data.get("defaults", {})
        if isinstance(defaults, dict) and "super_size" in defaults:
            try:
                return int(defaults["super_size"])
            except (ValueError, TypeError):
                pass
    return 9126805504
