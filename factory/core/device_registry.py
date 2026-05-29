from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Any

from factory.core.workspace import Workspace, read_json, write_json

DEVICE_ROOT = Path("devices")
PROFILE_ROOT = Path("profiles")
SOCS = ("mtk", "snapdragon")


class DeviceRegistryError(RuntimeError):
    pass


def _load_yaml(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {}
    try:
        import yaml  # type: ignore
    except Exception as exc:  # pragma: no cover - surfaced by validation command
        raise DeviceRegistryError("PyYAML is required to load device registry files") from exc
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise DeviceRegistryError(f"registry file is not a mapping: {path}")
    return data


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        elif value is not None:
            merged[key] = deepcopy(value)
    return merged


def _rom_dict(rom_metadata: Any | None) -> dict[str, Any]:
    if rom_metadata is None:
        return {}
    if isinstance(rom_metadata, dict):
        return dict(rom_metadata)
    if is_dataclass(rom_metadata):
        return asdict(rom_metadata)
    return {}


def _detected_codename(rom_metadata: dict[str, Any], ws: Workspace | None) -> str:
    for source in (rom_metadata, read_json(ws.meta / "device_info.json", {}) if ws else {}, read_json(ws.meta / "rom_info.json", {}) if ws else {}):
        value = str(source.get("codename") or "").strip().lower()
        if value and value != "unknown":
            return value
    return ""


def _load_soc_profile(soc: str) -> dict[str, Any]:
    profile = _load_yaml(PROFILE_ROOT / f"{soc}.yml")
    profile.setdefault("soc", soc)
    profile["profile_source"] = str(PROFILE_ROOT / f"{soc}.yml")
    return profile


def load_devices() -> dict[str, dict[str, Any]]:
    devices: dict[str, dict[str, Any]] = {}
    for soc in SOCS:
        directory = DEVICE_ROOT / soc
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.yml")):
            data = _load_yaml(path)
            codename = str(data.get("codename") or path.stem).strip().lower()
            if not codename:
                raise DeviceRegistryError(f"device file has no codename: {path}")
            data["codename"] = codename
            data.setdefault("soc", soc)
            data["device_source"] = str(path)
            if codename in devices:
                raise DeviceRegistryError(f"duplicate device codename: {codename}")
            devices[codename] = data
    return devices


def list_devices() -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {soc: [] for soc in SOCS}
    for device in load_devices().values():
        soc = str(device.get("soc") or "unknown").lower()
        grouped.setdefault(soc, []).append(device)
    for values in grouped.values():
        values.sort(key=lambda item: str(item.get("codename") or ""))
    return grouped


def resolve_device(
    codename: str | None = None,
    *,
    rom_metadata: Any | None = None,
    custom_codename: str = "",
    ws: Workspace | None = None,
    write_report: bool = True,
) -> dict[str, Any]:
    rom = _rom_dict(rom_metadata)
    devices = load_devices()
    selected = str(codename or "").strip().lower()
    detected = str(_detected_codename(rom, ws) or "").strip().lower()
    fallback = custom_codename.strip().lower()
    if selected and selected != "custom":
        resolved_codename = selected
        resolution_source = "selected"
    elif selected == "custom":
        if not fallback:
            raise DeviceRegistryError("device_codename is custom, but no custom_codename was provided")
        resolved_codename = fallback
        resolution_source = "custom_codename"
    elif detected:
        resolved_codename = detected
        resolution_source = "detected"
    else:
        resolved_codename = ""
        resolution_source = "detected"
    if not resolved_codename:
        raise DeviceRegistryError("unknown device codename and no custom_codename fallback was provided")
    if resolved_codename not in devices:
        raise DeviceRegistryError(f"unknown device codename: {resolved_codename}")

    device = devices[resolved_codename]
    soc = str(device.get("soc") or rom.get("soc") or "").lower()
    soc_profile = _load_soc_profile(soc)
    merged = _deep_merge(soc_profile, device)
    merged["rom_metadata"] = rom
    merged["_soc_super"] = deepcopy(soc_profile.get("super") or {})
    merged["_device_super"] = deepcopy(device.get("super") or {})
    merged["resolved_codename"] = resolved_codename
    merged["detected_codename"] = detected or "unknown"
    merged["selected_codename"] = selected or "unknown"
    merged["custom_codename"] = fallback
    merged["profile_source"] = soc_profile.get("profile_source")
    merged["device_source"] = device.get("device_source")
    merged["resolution_source"] = resolution_source

    if ws and write_report:
        write_json(ws.meta / "device_registry.json", merged)
        write_device_report(ws, merged)
    return merged


def write_device_report(ws: Workspace, resolved: dict[str, Any]) -> None:
    lines = [
        "DeadZone Device Registry Report",
        "===============================",
        f"codename: {resolved.get('resolved_codename')}",
        f"name: {resolved.get('name')}",
        f"soc: {resolved.get('soc')}",
        f"profile source: {resolved.get('profile_source')}",
        f"device source: {resolved.get('device_source')}",
        f"resolution source: {resolved.get('resolution_source')}",
        f"selected codename: {resolved.get('selected_codename')}",
        f"detected codename: {resolved.get('detected_codename')}",
        f"custom fallback: {resolved.get('custom_codename') or '(none)'}",
        "",
        "super:",
    ]
    for key, value in (resolved.get("super") or {}).items():
        lines.append(f"  {key}: {value}")
    lines.append("")
    (ws.reports / "device_registry_report.txt").write_text("\n".join(lines), encoding="utf-8")
