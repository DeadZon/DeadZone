"""
Pure build.prop reader — NO side effects, NO patching.

IMPORTANT: The legacy MEZOBuildRom.find_and_read_build_props() (lines 439-607)
does far more than read — it also:
  1. Writes DeadZone_firmware.txt to the output directory
  2. Moves files from rom/payload_extracted/ to the images/ folder
  3. Patches vbmeta.img (re-signs it with dm-verity disabled)

None of those steps belong in the unpack stage.  This module provides a clean
equivalent that ONLY reads and returns values.

parse_build_prop() is copied from MEZOBuildRom.py lines 417-436.
BUILD_PROP_KEYS is taken from MEZOBuildRom.py lines 44-51.
"""
from __future__ import annotations

from pathlib import Path

# Keys read from build.prop files — kept in sync with MEZOBuildRom.BUILD_PROP_KEYS.
BUILD_PROP_KEYS: tuple[str, ...] = (
    "ro.product.odm.brand",
    "ro.product.odm.device",
    "ro.product.odm.model",
    "ro.product.odm.marketname",
    "ro.mi.os.version.incremental",
    "ro.system.build.version.release",
)

# Codenames that are build-system placeholders, not real device codenames.
# When build.prop returns one of these AND DEADZONE_DEVICE_CODENAME is set,
# the factory device takes precedence.
GENERIC_CODENAMES: frozenset[str] = frozenset({
    "",
    "generic",
    "qssi",
    "system",
    "unknown",
    "mgvi_64_armv82",
})


# ── legacy-extracted from MEZOBuildRom.py:parse_build_prop (lines 417-436) ──
def parse_build_prop(path: Path) -> dict[str, str]:
    """
    Read a single build.prop file and return a dict of recognised key→value
    pairs.  Lines that do not contain '=' or start with '#' are skipped.
    Only keys in BUILD_PROP_KEYS are collected; later duplicates are ignored.
    """
    props: dict[str, str] = {}
    if not path.is_file():
        return props
    try:
        with path.open("r", encoding="utf-8", errors="ignore") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                key = key.strip()
                value = value.strip()
                if key in BUILD_PROP_KEYS and key not in props:
                    props[key] = value
    except Exception as exc:
        print(f"[build_prop] Error reading '{path}': {exc}")
    return props


def read_build_props(project_dir: Path) -> dict[str, str | None]:
    """
    Aggregate build.prop values from all build.prop files found under
    project_dir.  Returns a flat dict with the same keys as BUILD_PROP_KEYS.
    First occurrence of each key wins (matches MEZOBuildRom behaviour).

    Returns all keys with None values when no build.prop file is found.
    """
    aggregated: dict[str, str] = {}

    for bp_path in project_dir.rglob("build.prop"):
        props = parse_build_prop(bp_path)
        for key in BUILD_PROP_KEYS:
            if key not in aggregated and props.get(key):
                aggregated[key] = props[key]

    result: dict[str, str | None] = {k: aggregated.get(k) for k in BUILD_PROP_KEYS}
    return result


def resolve_effective_device(
    detected_device: str | None,
    factory_device: str | None,
) -> tuple[str | None, str]:
    """
    Apply the CRITICAL DEVICE RULE:

    If the build.prop codename is a known generic placeholder AND a factory
    device is specified (via --device or DEADZONE_DEVICE_CODENAME), use the
    factory device as the effective codename.

    Returns (effective_device, decision_reason).
    """
    if not detected_device or detected_device.lower() in GENERIC_CODENAMES:
        if factory_device:
            return (
                factory_device,
                f"build.prop returned generic '{detected_device}'; "
                f"using DEADZONE_DEVICE_CODENAME '{factory_device}'",
            )
        return (
            None,
            f"build.prop returned generic '{detected_device}' and no factory device set",
        )

    if factory_device and factory_device != detected_device:
        # Factory device explicitly overrides build.prop even when build.prop
        # looks real — the operator knows the target device better than the ROM.
        return (
            factory_device,
            f"factory device '{factory_device}' overrides build.prop '{detected_device}'",
        )

    return (detected_device, f"using build.prop device '{detected_device}'")
