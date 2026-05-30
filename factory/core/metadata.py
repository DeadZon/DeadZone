from __future__ import annotations

from typing import Any

ALLOWED_STYLES: frozenset[str] = frozenset({"stable", "legend", "gaming", "epic"})

STYLE_LABELS: dict[str, str] = {
    "stable": "Stable",
    "legend": "Legend",
    "gaming": "Gaming",
    "epic": "EPiC",
}

STYLE_DISPLAY: dict[str, str] = {k: v for k, v in STYLE_LABELS.items()}


def validate_style(style: str) -> tuple[str, str]:
    key = style.strip().lower()
    if key not in ALLOWED_STYLES:
        raise ValueError(
            f"Invalid style {style!r}. Must be one of: stable, legend, gaming, epic"
        )
    return key, STYLE_LABELS[key]


def os_family_from_build(build: str) -> str:
    b = (build or "").strip().upper()
    if b.startswith("OS"):
        return "HyperOS"
    if b.startswith("V") or "MIUI" in b:
        return "MIUI"
    return "Unknown"


def _pick(*values: Any) -> str:
    for v in values:
        s = str(v or "").strip()
        if s and s.lower() not in ("unknown", "none", "null", "detecting..."):
            return s
    return ""


def normalize_build_metadata(
    *,
    device_profile: dict[str, Any] | None = None,
    rom_info: Any | None = None,
    soc: str = "",
    style_key: str = "",
    style_label: str = "",
) -> dict[str, str]:
    """Return a canonical metadata dict from the best available sources.

    All missing values are 'Unknown' — never a fake default.
    """
    dp = device_profile or {}

    def _attr(key: str) -> str:
        if rom_info is None:
            return ""
        return str(getattr(rom_info, key, "") or "")

    device_codename = _pick(
        dp.get("resolved_codename"),
        dp.get("codename"),
        _attr("codename"),
    )
    device_name = _pick(dp.get("name"))
    soc_val = (_pick(dp.get("soc"), soc, _attr("soc")) or "").upper()
    android_version = _pick(_attr("android_version"))
    rom_version = _pick(_attr("build"))
    region = _pick(_attr("region"))
    label = style_label or STYLE_LABELS.get(style_key, "")
    os_fam = os_family_from_build(rom_version)

    return {
        "device_codename": device_codename or "Unknown",
        "device_name": device_name or "Unknown",
        "soc": soc_val or "Unknown",
        "edition": label or "Unknown",
        "android_version": android_version or "Unknown",
        "rom_version": rom_version or "Unknown",
        "os_family": os_fam,
        "region": region or "Unknown",
    }
