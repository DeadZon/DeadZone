"""Recover super partition metadata for payload OTA ROMs without original super.img.

When a payload OTA ROM is unpacked it yields individual dynamic partition images
(system.img, vendor.img, …) but no super.img.  The Smart Base Engine then chooses
the rebuild_with_lpmake strategy — but lpmake needs:

  - partition allocation sizes  (NOT the extracted image file sizes)
  - group name                  (e.g. ``qti_dynamic_partitions`` or ``main``)
  - total super size            (block device size)
  - VAB layout flag

This module recovers those values from three sources, tried in priority order:

  1. payload.bin manifest    — most accurate; contains original partition sizes
                               and the dynamic_partition_metadata group names.
  2. Device registry YAML    — device-specific super profile (super_size, group
                               name, virtual_ab, metadata_slots).
  3. Calculated fallback     — sum of partition sizes × 2, capped at default GiB.

Public API
----------
recover_super_metadata_from_payload(
    payload_manifest_path, source_images_dir, selected_codename, registry_path
) -> dict

The returned dict carries ``partition_sizes`` (base_name → bytes), which is
the value expected by ``rebuild_super(original_partition_sizes=…)``, together
with a ``super_profile`` sub-dict that ``rebuild_super`` uses when it must
synthesise an LP metadata block from scratch.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[2]
_LEGACY_SRC = _REPO_ROOT / "third_party" / "mezo_core" / "src"
if str(_LEGACY_SRC) not in sys.path:
    sys.path.insert(0, str(_LEGACY_SRC))

# ── Constants ─────────────────────────────────────────────────────────────────

_LP_METADATA_OVERHEAD: int = 4 * 1024 * 1024        # 4 MiB geometry overhead
_DEFAULT_SUPER_SIZE: int   = 9_126_805_504            # ~8.5 GiB
_DEFAULT_GROUP_NAME: str   = "qti_dynamic_partitions"
_DEFAULT_METADATA_SLOTS: int = 3

_DYNAMIC_BASES: frozenset[str] = frozenset([
    "system", "system_ext", "product", "vendor",
    "odm", "mi_ext", "vendor_dlkm", "odm_dlkm", "system_dlkm",
])


# ── Step 1 — payload.bin manifest ────────────────────────────────────────────

def _read_manifest_partition_sizes(payload_bin: Path) -> dict[str, int]:
    """Return {base_partition_name: size_bytes} from payload.bin manifest."""
    try:
        from factory.unpack.payload import parse_manifest_partition_sizes  # noqa: PLC0415
        raw = parse_manifest_partition_sizes(payload_bin)
    except Exception as exc:
        print(f"[payload_super_metadata] Warning: parse_manifest_partition_sizes failed: {exc}")
        return {}

    # Normalise: strip _a suffix, keep only dynamic bases
    sizes: dict[str, int] = {}
    for name, sz in (raw or {}).items():
        base = name[:-2] if (name.endswith("_a") or name.endswith("_b")) else name
        if base in _DYNAMIC_BASES and sz > 0 and base not in sizes:
            sizes[base] = sz
    return sizes


def _read_manifest_group_name(payload_bin: Path) -> tuple[str | None, list[str]]:
    """Return (group_basename, warnings) from payload.bin dynamic_partition_metadata."""
    warnings: list[str] = []
    try:
        from src.core.payload_extract import init_payload_info  # type: ignore  # noqa: PLC0415
    except Exception as exc:
        warnings.append(f"payload_extract not available for group-name scan: {exc}")
        return None, warnings

    try:
        with payload_bin.open("rb") as fh:
            manifest = init_payload_info(fh)
        dpm = getattr(manifest, "dynamic_partition_metadata", None)
        if not dpm or not dpm.groups:
            return None, warnings
        # Pick the largest non-default group
        main_group = max(
            (g for g in dpm.groups if g.name and g.name not in ("default", "")),
            key=lambda g: g.size,
            default=None,
        )
        if main_group is None:
            return None, warnings
        name = str(main_group.name)
        # Strip slot suffix
        if name.endswith("_a") or name.endswith("_b"):
            name = name[:-2]
        return name, warnings
    except Exception as exc:
        warnings.append(f"Could not parse manifest group name: {exc}")
        return None, warnings


# ── Step 2 — device registry YAML ────────────────────────────────────────────

def _read_registry_super_profile(
    registry_path: Path | None,
    codename: str,
) -> dict[str, Any]:
    """Return super profile fields from device registry YAML.

    Accepts optional fields in registry ``super:`` block:
      super_size, dynamic_group, group_size, metadata_slots, virtual_ab,
      slot_mode (vab|ab|a-only), dynamic_partitions (list of base names).
    """
    profile: dict[str, Any] = {}
    if not registry_path:
        return profile

    path = Path(registry_path)
    if not path.is_file():
        # Try conventional location relative to repo root
        for soc in ("mtk", "snapdragon"):
            cand = _REPO_ROOT / "registry" / "devices" / soc / f"{codename}.yml"
            if cand.is_file():
                path = cand
                break
        else:
            return profile

    try:
        try:
            import yaml  # noqa: PLC0415
        except ImportError:
            # Minimal YAML key:value parser — enough for flat super block
            return _parse_simple_yaml_super(path)

        with path.open("r", encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        super_block = (doc or {}).get("super") or {}

        if super_block.get("super_size"):
            profile["super_size"] = int(super_block["super_size"])
        if super_block.get("dynamic_group"):
            profile["group_name"] = str(super_block["dynamic_group"])
        if super_block.get("group_size"):
            profile["group_size"] = int(super_block["group_size"])
        if super_block.get("metadata_slots"):
            profile["metadata_slots"] = int(super_block["metadata_slots"])
        slot_mode = (super_block.get("slot_mode") or "").lower()
        if slot_mode == "vab":
            profile["virtual_ab"] = True
        elif slot_mode in ("ab", "a-only"):
            profile["virtual_ab"] = False
        dynamic_parts = super_block.get("dynamic_partitions")
        if dynamic_parts and isinstance(dynamic_parts, list):
            profile["dynamic_partitions"] = [str(p) for p in dynamic_parts]
    except Exception as exc:
        print(f"[payload_super_metadata] Warning: registry read failed for {path}: {exc}")

    return profile


def _parse_simple_yaml_super(path: Path) -> dict[str, Any]:
    """Minimal YAML ``super:`` block parser that works without PyYAML."""
    profile: dict[str, Any] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
        in_super = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("super:"):
                in_super = True
                continue
            if in_super:
                if stripped and not stripped.startswith("#"):
                    indent = len(line) - len(line.lstrip())
                    if indent == 0:
                        break  # new top-level key
                    if ":" in stripped:
                        k, _, v = stripped.partition(":")
                        k = k.strip()
                        v = v.strip()
                        if k == "super_size" and v.isdigit():
                            profile["super_size"] = int(v)
                        elif k == "dynamic_group":
                            profile["group_name"] = v
                        elif k == "metadata_slots" and v.isdigit():
                            profile["metadata_slots"] = int(v)
                        elif k == "slot_mode" and v.lower() == "vab":
                            profile["virtual_ab"] = True
                        elif k == "slot_mode" and v.lower() in ("ab", "a-only"):
                            profile["virtual_ab"] = False
    except Exception:
        pass
    return profile


# ── Public API ────────────────────────────────────────────────────────────────

def recover_super_metadata_from_payload(
    payload_manifest_path: Path | None,
    source_images_dir: Path,
    selected_codename: str,
    registry_path: Path | None = None,
) -> dict:
    """Recover super partition metadata for a payload OTA build.

    Parameters
    ----------
    payload_manifest_path:
        Path to the payload.bin file.  May be None when unavailable.
    source_images_dir:
        Directory containing extracted .img files (for size fallback if needed).
    selected_codename:
        Device codename — used to locate the registry YAML when registry_path
        is not supplied.
    registry_path:
        Optional direct path to the device's registry YAML file.

    Returns
    -------
    dict with keys::

        metadata_source   — "payload_manifest" | "device_registry" | "calculated_fallback"
        super_size        — int (bytes)
        group_name        — str
        group_size        — int (bytes, super_size minus LP overhead)
        block_size        — 4096
        metadata_slots    — int (usually 3 for VAB)
        virtual_ab        — bool
        partition_sizes   — {base_name: size_bytes}  ← pass to rebuild_super
        partitions        — {part_a: {image, size}, part_b: {size: 0}, …}
        warnings          — list[str]
        errors            — list[str]
        attempted_sources — list[str]
    """
    warnings: list[str] = []
    errors: list[str] = []
    attempted: list[str] = []

    # ── Step 1: payload manifest ──────────────────────────────────────────────
    manifest_sizes: dict[str, int] = {}
    manifest_group: str | None = None

    if payload_manifest_path and Path(payload_manifest_path).is_file():
        attempted.append("payload_manifest")
        manifest_sizes = _read_manifest_partition_sizes(Path(payload_manifest_path))
        manifest_group, manifest_warnings = _read_manifest_group_name(Path(payload_manifest_path))
        warnings.extend(manifest_warnings)
        if not manifest_sizes:
            warnings.append(
                f"payload manifest at {payload_manifest_path} yielded no dynamic partition sizes"
            )
        if not manifest_group:
            warnings.append("payload manifest did not expose dynamic group name")
    else:
        warnings.append(
            "payload.bin not available — skipping manifest metadata extraction"
        )

    # ── Step 2: device registry ───────────────────────────────────────────────
    attempted.append("device_registry")
    registry_profile = _read_registry_super_profile(registry_path, selected_codename)

    # ── Step 3: merge, with manifest taking priority over registry ────────────
    partition_sizes = dict(manifest_sizes)  # possibly empty

    group_name: str = (
        manifest_group
        or registry_profile.get("group_name")
        or _DEFAULT_GROUP_NAME
    )

    super_size_raw: int = registry_profile.get("super_size", 0)

    if super_size_raw <= 0:
        # Estimate from partition sizes if both manifest and registry are silent
        if partition_sizes:
            total = sum(partition_sizes.values())
            super_size_raw = max(total * 2, _DEFAULT_SUPER_SIZE)
            warnings.append(
                f"super_size unknown — estimated as max(2×partitions, default): {super_size_raw}"
            )
        else:
            super_size_raw = _DEFAULT_SUPER_SIZE
            warnings.append(
                f"super_size unknown and no partition sizes available — using default: {super_size_raw}"
            )

    metadata_slots: int = registry_profile.get("metadata_slots", _DEFAULT_METADATA_SLOTS)
    virtual_ab: bool = registry_profile.get("virtual_ab", True)  # assume VAB by default
    group_size: int = max(0, super_size_raw - _LP_METADATA_OVERHEAD)

    # ── Determine metadata_source ─────────────────────────────────────────────
    if manifest_sizes and (manifest_group or registry_profile.get("group_name")):
        metadata_source = "payload_manifest"
    elif registry_profile:
        metadata_source = "device_registry"
        if not partition_sizes:
            errors.append(
                f"Cannot rebuild super.img: no partition sizes in payload manifest "
                f"and no device registry super profile has dynamic_partitions sizes. "
                f"Attempted sources: {', '.join(attempted)}. "
                f"Dynamic images found: {sorted(source_images_dir.glob('*.img')) if Path(source_images_dir).is_dir() else '(dir missing)'}. "
                f"Suggestion: add partition sizes to registry or ensure payload.bin is accessible."
            )
    else:
        metadata_source = "calculated_fallback"
        attempted.append("calculated_fallback")
        if not partition_sizes:
            errors.append(
                f"Metadata recovery failed — no partition sizes could be determined. "
                f"Attempted sources: {', '.join(attempted)}. "
                f"Add a super profile with dynamic_partitions sizes to "
                f"registry/devices/<soc>/{selected_codename}.yml."
            )

    # If we still have no partition sizes, try image file sizes as last resort
    # (only if the caller can accept that — we warn clearly)
    if not partition_sizes and Path(source_images_dir).is_dir():
        fallback_sizes: dict[str, int] = {}
        for img in Path(source_images_dir).glob("*.img"):
            base = img.stem.lower()
            if base.endswith("_a"):
                base = base[:-2]
            if base in _DYNAMIC_BASES:
                sz = img.stat().st_size
                if sz > 0:
                    fallback_sizes[base] = sz
        if fallback_sizes:
            partition_sizes = fallback_sizes
            warnings.append(
                "Using extracted image file sizes as partition allocation fallback — "
                "these may differ from original LP allocations. "
                "Prefer payload manifest or device registry for accurate sizes."
            )
            metadata_source = "calculated_fallback"

    # ── Build partitions map ──────────────────────────────────────────────────
    partitions: dict[str, dict] = {}
    for base, sz in partition_sizes.items():
        img_path = Path(source_images_dir) / f"{base}.img"
        partitions[f"{base}_a"] = {
            "image": f"{base}.img",
            "size": sz,
            "image_exists": img_path.is_file(),
        }
        if virtual_ab:
            partitions[f"{base}_b"] = {"size": 0}

    return {
        "metadata_source":   metadata_source,
        "super_size":        super_size_raw,
        "group_name":        group_name,
        "group_size":        group_size,
        "block_size":        4096,
        "metadata_slots":    metadata_slots,
        "virtual_ab":        virtual_ab,
        "partition_sizes":   partition_sizes,
        "partitions":        partitions,
        "warnings":          warnings,
        "errors":            errors,
        "attempted_sources": attempted,
    }
