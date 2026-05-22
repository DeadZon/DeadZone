"""
New factory super collector for zircon / MTK HyperOS OTA payload extraction.

Responsibilities
----------------
1. Split extracted payload images into:
   - dynamic_super_partitions  → packed into super.img via lpmake
   - standalone_fastboot_images → remain as individual .img files

2. Build super.img with correct VAB layout using lpmake.

3. Validate super.img using the Python lpunpack library.

4. Write reports: output/reports/super_build_report.{json,txt}

Zircon profile
--------------
    SUPER_SIZE           = 9126805504  (~8.5 GiB)
    SUPER_GROUP_BASENAME = "qti_dynamic_partitions"
    slot_mode            = "vab"
    metadata_slots       = 3
"""
from __future__ import annotations

import json
import os
import platform
import shutil
import stat
import subprocess
import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[2]
_LEGACY_ROOT = _REPO_ROOT / "third_party" / "mezo_core"
_LEGACY_SRC = _LEGACY_ROOT / "src"

if str(_LEGACY_SRC) not in sys.path:
    sys.path.insert(0, str(_LEGACY_SRC))

try:
    from core.lpunpack import get_info as _lpunpack_get_info  # type: ignore
except Exception:
    _lpunpack_get_info = None  # type: ignore

# ── Zircon device profile ──────────────────────────────────────────────────────
ZIRCON_SUPER_SIZE: int = 9126805504
ZIRCON_SUPER_GROUP_BASENAME: str = "qti_dynamic_partitions"
ZIRCON_METADATA_SLOTS: int = 3
ZIRCON_METADATA_MAX_SIZE: int = 65536

# LP metadata overhead reserved before usable data space.
# 4 MiB covers geometry blocks ×2 + metadata slots ×3 ×2 with alignment headroom.
_LP_METADATA_OVERHEAD: int = 4 * 1024 * 1024

# ── Dynamic partitions that MUST be packed inside super.img ───────────────────
DYNAMIC_SUPER_PARTITIONS: list[str] = [
    "system",
    "product",
    "system_ext",
    "vendor",
    "vendor_dlkm",
    "system_dlkm",
    "odm",
    "odm_dlkm",
    "mi_ext",
]

# ── Standalone firmware images (sit beside super.img in fastboot package) ──────
STANDALONE_FIRMWARE_IMAGES: list[str] = [
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "dtbo.img",
    "vbmeta.img",
    "vbmeta_system.img",
    "vbmeta_vendor.img",
    "logo.img",
    "lk.img",
    "md1img.img",
    "audio_dsp.img",
    "scp.img",
    "sspm.img",
    "tee.img",
    "gz.img",
    "dpm.img",
    "pi_img.img",
    "mcf_ota.img",
    "preloader_raw.img",
    "apusys.img",
    "ccu.img",
    "connsys_bt.img",
    "connsys_gnss.img",
    "connsys_wifi.img",
    "gpueb.img",
    "mcupm.img",
    "mvpu_algo.img",
    "spmfw.img",
    "vcp.img",
]

_DYNAMIC_PARTITION_NAMES_SET: frozenset[str] = frozenset(DYNAMIC_SUPER_PARTITIONS)
_FORBIDDEN_STANDALONE: frozenset[str] = frozenset(
    f"{p}.img" for p in DYNAMIC_SUPER_PARTITIONS
)


# ── Image collection ───────────────────────────────────────────────────────────

def collect_partition_images(
    payload_images_dir: Path,
) -> tuple[dict[str, Path], dict[str, Path]]:
    """Split extracted payload images into dynamic and standalone categories.

    Scans ``payload_images_dir`` for *.img files and classifies each as:
    - dynamic  — one of the 9 dynamic super partitions (system/vendor/…)
    - standalone — every other image (boot/vbmeta/firmware/…)

    Slot-suffixed images (_a/_b) are normalised: the _a image is accepted as
    the canonical source; _b images are skipped (zero-size VAB metadata slots).

    Returns:
        dynamic    — {partition_name: path_to_img}
        standalone — {image_filename: path_to_img}
    """
    payload_images_dir = Path(payload_images_dir).resolve()
    dynamic: dict[str, Path] = {}
    standalone: dict[str, Path] = {}

    if not payload_images_dir.is_dir():
        return dynamic, standalone

    for img_path in sorted(payload_images_dir.glob("*.img")):
        if not img_path.is_file():
            continue
        stem = img_path.stem.lower()
        name = img_path.name.lower()

        base_stem = stem
        is_b_slot = False
        if stem.endswith("_a"):
            base_stem = stem[:-2]
        elif stem.endswith("_b"):
            base_stem = stem[:-2]
            is_b_slot = True

        if base_stem in _DYNAMIC_PARTITION_NAMES_SET:
            if is_b_slot:
                continue
            if base_stem not in dynamic:
                dynamic[base_stem] = img_path
        else:
            if name not in standalone:
                standalone[name] = img_path

    return dynamic, standalone


# ── Super profile loading ──────────────────────────────────────────────────────

def _load_payload_manifest_super(
    payload_dir: Path,
) -> tuple[str | None, list[str], list[str]]:
    """Extract group_basename and partition_names from payload.bin manifest.

    Returns (group_basename, partition_names, warnings).
    """
    warnings: list[str] = []
    try:
        from core.payload_extract import init_payload_info  # type: ignore
    except Exception as exc:
        warnings.append(f"payload_extract not available: {exc}")
        return None, [], warnings

    payload_candidates: list[Path] = []
    for root in [payload_dir, payload_dir / "payload_extracted", payload_dir / "rom"]:
        if root.is_dir():
            try:
                payload_candidates.extend(p for p in root.rglob("payload.bin") if p.is_file())
            except Exception:
                pass

    if not payload_candidates:
        warnings.append(f"No payload.bin found under {payload_dir}")
        return None, [], warnings

    for payload_path in payload_candidates:
        try:
            with payload_path.open("rb") as fh:
                manifest = init_payload_info(fh)
            dpm = getattr(manifest, "dynamic_partition_metadata", None)
            if not dpm or not dpm.groups:
                continue
            main_group = max(
                (g for g in dpm.groups if g.name and g.name != "default"),
                key=lambda g: g.size,
                default=None,
            )
            if main_group is None:
                continue
            group_name = str(main_group.name)
            if group_name.endswith("_a") or group_name.endswith("_b"):
                group_name = group_name[:-2]

            raw_parts = list(main_group.partition_names or [])
            normalised: list[str] = []
            seen: set[str] = set()
            for p in raw_parts:
                base = p[:-2] if (p.endswith("_a") or p.endswith("_b")) else p
                if base not in seen:
                    seen.add(base)
                    normalised.append(base)

            if normalised:
                return group_name, normalised, warnings
        except Exception as exc:
            warnings.append(f"Could not parse payload manifest {payload_path.name}: {exc}")

    return None, [], warnings


def load_device_super_profile(
    payload_dir: Path,
    device: str | None = None,
) -> dict[str, Any]:
    """Load the super partition profile for the target device.

    Priority:
      1. payload.bin manifest → group name and partition list
      2. Zircon defaults for super_size (always 9126805504 for zircon; used as
         the universal fallback when no device-specific registry entry exists)

    Returns a dict with all fields needed to drive lpmake:
      super_size, group_size, group_basename, group_a_name, group_b_name,
      metadata_slots, metadata_max_size, partition_names, slot_mode,
      virtual_ab, output_format, warnings.
    """
    warnings: list[str] = []
    device_key = (device or "").strip().lower()

    group_basename, part_names_from_manifest, manifest_warnings = _load_payload_manifest_super(payload_dir)
    warnings.extend(manifest_warnings)

    # Super block-device size: always use the zircon verified value for zircon;
    # fall back to the same constant for unknown devices (no registry present).
    super_size = ZIRCON_SUPER_SIZE
    if device_key and device_key != "zircon":
        warnings.append(
            f"No device-specific super_size profile for '{device_key}'; "
            f"using zircon fallback {ZIRCON_SUPER_SIZE}"
        )

    if not group_basename:
        group_basename = ZIRCON_SUPER_GROUP_BASENAME
        warnings.append(
            f"Could not read group name from payload manifest; "
            f"using fallback: {group_basename}"
        )

    if part_names_from_manifest:
        # Keep manifest order, restrict to known dynamic partitions, append any missing.
        part_names = [p for p in part_names_from_manifest if p in _DYNAMIC_PARTITION_NAMES_SET]
        for p in DYNAMIC_SUPER_PARTITIONS:
            if p not in part_names:
                part_names.append(p)
    else:
        part_names = list(DYNAMIC_SUPER_PARTITIONS)
        warnings.append("Using default dynamic partition list (no manifest partition names found)")

    group_size = super_size - _LP_METADATA_OVERHEAD

    return {
        "super_size": super_size,
        "group_size": group_size,
        "group_basename": group_basename,
        "group_a_name": f"{group_basename}_a",
        "group_b_name": f"{group_basename}_b",
        "metadata_slots": ZIRCON_METADATA_SLOTS,
        "metadata_max_size": ZIRCON_METADATA_MAX_SIZE,
        "partition_names": part_names,
        "slot_mode": "vab",
        "virtual_ab": True,
        "output_format": "sparse",
        "warnings": warnings,
    }


# ── lpmake binary resolution ───────────────────────────────────────────────────

def resolve_lpmake_binary(root_dir: Path | None = None) -> Path | None:
    """Resolve the lpmake binary for the current platform."""
    root = Path(root_dir).resolve() if root_dir else _LEGACY_ROOT.resolve()
    tool = "lpmake.exe" if os.name == "nt" else "lpmake"
    candidates = [
        root / "bin" / platform.system() / platform.machine() / tool,
        root / "bin" / tool,
        root / "bin" / "lpmake",
        Path("lpmake"),
    ]
    for c in candidates:
        if c.is_file():
            if os.name == "posix":
                try:
                    c.chmod(c.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                except Exception:
                    pass
            return c
    found = shutil.which("lpmake") or shutil.which(tool)
    return Path(found) if found else None


# ── lpmake command construction ────────────────────────────────────────────────

def build_lpmake_command(
    payload_images_dir: Path,
    output_super: Path,
    profile: dict[str, Any],
    dynamic_parts: dict[str, Path],
    lpmake_path: Path | None,
) -> tuple[list[str], list[str], list[str]]:
    """Build the lpmake VAB command for super.img.

    VAB layout:
      For each dynamic partition ``p``:
        - ``p_a`` → real image from dynamic_parts[p]
        - ``p_b`` → zero-size metadata slot

    Returns (command, warnings, errors).
    """
    warnings: list[str] = []
    errors: list[str] = []

    super_size = int(profile["super_size"])
    group_size = int(profile["group_size"])
    group_a = profile["group_a_name"]
    group_b = profile["group_b_name"]
    metadata_slots = int(profile["metadata_slots"])
    metadata_max_size = int(profile["metadata_max_size"])

    if super_size <= 0:
        errors.append("super_size is 0 or negative — cannot build super.img")
        return [], warnings, errors

    if lpmake_path is None:
        errors.append("lpmake binary not found — cannot build super.img")
        return [], warnings, errors

    cmd: list[str] = [
        str(lpmake_path),
        "--metadata-size", str(metadata_max_size),
        "--super-name", "super",
        "--metadata-slots", str(metadata_slots),
        "--device", f"super:{super_size}",
        "--sparse",
        "--group", f"{group_a}:{group_size}",
    ]

    # _a slot: real dynamic partition images
    selected_parts = [p for p in profile["partition_names"] if p in dynamic_parts]
    missing_parts = [p for p in profile["partition_names"] if p not in dynamic_parts]
    if missing_parts:
        warnings.append(f"Dynamic partitions absent from payload images: {', '.join(missing_parts)}")

    for part in selected_parts:
        img = dynamic_parts[part]
        if not img.is_file():
            errors.append(f"Dynamic partition image not found: {img}")
            continue
        size = img.stat().st_size
        if size <= 0:
            errors.append(f"Dynamic partition image is empty (0 bytes): {img}")
            continue
        cmd += [
            "--partition", f"{part}_a:readonly:{size}:{group_a}",
            "--image", f"{part}_a={img}",
        ]

    # _b slot: zero-size VAB metadata entries
    cmd += ["--group", f"{group_b}:{group_size}"]
    for part in selected_parts:
        cmd += ["--partition", f"{part}_b:readonly:0:{group_b}"]

    cmd += ["--virtual-ab"]
    cmd += ["--out", str(output_super)]

    return cmd, warnings, errors


# ── lpunpack-based super.img validation ───────────────────────────────────────

def validate_super_with_lpunpack(
    super_path: Path,
    expected_partitions: list[str],
    expected_super_size: int | None = None,
) -> dict[str, Any]:
    """Validate super.img LP metadata using the Python lpunpack library.

    Checks:
      - super.img is readable by lpunpack
      - Block device size matches expected_super_size (if provided)
      - All expected _a-slot partitions are present in the metadata

    Returns a result dict with ``status`` in {"PASSED", "FAILED", "SKIPPED"}.
    """
    result: dict[str, Any] = {
        "status": "SKIPPED",
        "super_path": str(super_path),
        "lpdump_summary": None,
        "device_size_in_super": None,
        "partitions_in_super": [],
        "missing_partitions": [],
        "errors": [],
        "warnings": [],
    }

    if not super_path.is_file():
        result["errors"].append(f"super.img not found: {super_path}")
        result["status"] = "FAILED"
        return result

    if _lpunpack_get_info is None:
        result["warnings"].append(
            "lpunpack.get_info not available — skipping LP metadata validation"
        )
        result["status"] = "SKIPPED"
        return result

    try:
        info = _lpunpack_get_info(str(super_path))
        if not info:
            result["errors"].append("lpunpack.get_info returned empty result — super.img may be corrupt")
            result["status"] = "FAILED"
            return result

        block_devices = info.get("block_devices", [])
        device_size = int(block_devices[0].get("size", 0)) if block_devices else 0
        result["device_size_in_super"] = device_size

        partition_table = info.get("partition_table", [])
        parts_in_super = [str(p.get("name", "")) for p in partition_table]
        result["partitions_in_super"] = parts_in_super

        group_table = info.get("group_table", [])
        summary_lines = [
            f"metadata_slot_count: {info.get('metadata_slot_count')}",
            f"block_device_size: {device_size}",
            f"groups: {[g.get('name') for g in group_table]}",
            f"partitions: {parts_in_super}",
        ]
        result["lpdump_summary"] = "\n".join(summary_lines)

        validation_errors: list[str] = []

        if expected_super_size and device_size != expected_super_size:
            validation_errors.append(
                f"super.img device_size={device_size} "
                f"but expected {expected_super_size} (zircon profile)"
            )

        expected_a_slots = [f"{p}_a" for p in expected_partitions]
        missing = [p for p in expected_a_slots if p not in parts_in_super]
        result["missing_partitions"] = missing
        if missing:
            validation_errors.append(
                f"Missing _a-slot partitions in super metadata: {', '.join(missing)}"
            )

        result["errors"].extend(validation_errors)
        result["status"] = "PASSED" if not validation_errors else "FAILED"

    except Exception as exc:
        result["errors"].append(f"lpunpack validation exception: {exc}")
        result["status"] = "FAILED"

    return result


# ── Final images validation ────────────────────────────────────────────────────

def check_final_images_dir(
    final_images_dir: Path,
    debug_mode: bool = False,
) -> dict[str, Any]:
    """Verify final_images_dir layout constraints.

    Checks:
      - super.img is present
      - Dynamic partition images are NOT present as standalone files (unless debug)
      - Expected standalone firmware images are present

    Returns a result dict.
    """
    final_images_dir = Path(final_images_dir).resolve()
    present = {p.name for p in final_images_dir.glob("*.img") if p.is_file()} if final_images_dir.is_dir() else set()
    errors: list[str] = []
    warnings: list[str] = []

    super_present = "super.img" in present

    forbidden = sorted(_FORBIDDEN_STANDALONE & present) if not debug_mode else []
    if forbidden:
        errors.append(
            f"Forbidden standalone dynamic partition images in final_images_dir "
            f"(must be inside super.img): {', '.join(forbidden)}"
        )

    missing_standalone = sorted(
        img for img in STANDALONE_FIRMWARE_IMAGES
        if img not in present
    )
    if missing_standalone:
        warnings.append(
            f"Standalone firmware images not present in final_images_dir: "
            f"{', '.join(missing_standalone)}"
        )

    return {
        "super_img_present": super_present,
        "forbidden_dynamic_images": forbidden,
        "missing_standalone_firmware": missing_standalone,
        "final_images_manifest": sorted(present),
        "errors": errors,
        "warnings": warnings,
    }


# ── Main orchestration ─────────────────────────────────────────────────────────

def collect_and_build_super(
    payload_images_dir: Path,
    output_super: Path,
    final_images_dir: Path,
    profile: dict[str, Any],
    execute: bool = False,
    debug_mode: bool = False,
) -> dict[str, Any]:
    """Orchestrate the full super.img collection and build.

    Steps (in execute mode):
      1. Split payload images into dynamic vs standalone.
      2. Copy standalone images to final_images_dir.
      3. Build super.img from dynamic partitions via lpmake.
      4. Validate super.img with lpunpack.
      5. Check final_images_dir for forbidden standalone dynamic images.

    vendor.img is included in super because it is a dynamic partition, but its
    contents are packed as-is — Legend mods must NOT modify vendor files.
    """
    payload_images_dir = Path(payload_images_dir).resolve()
    output_super = Path(output_super).resolve()
    final_images_dir = Path(final_images_dir).resolve()

    result: dict[str, Any] = {
        "status": "DRY_RUN" if not execute else "FAILED",
        "payload_images_dir": str(payload_images_dir),
        "output_super": str(output_super),
        "final_images_dir": str(final_images_dir),
        "dynamic_super_partitions": {},
        "standalone_fastboot_images": {},
        "super_size": profile["super_size"],
        "group_name": profile["group_basename"],
        "slot_mode": profile["slot_mode"],
        "output_format": profile["output_format"],
        "lpmake_command": [],
        "lpmake_executed": False,
        "lpmake_return_code": None,
        "lpmake_output": None,
        "super_img_created": False,
        "super_img_size": None,
        "lpdump_summary": None,
        "validation_status": "NOT_RUN",
        "missing_dynamic_partitions": [],
        "forbidden_standalone_dynamic_images": [],
        "final_images_manifest": [],
        "warnings": list(profile.get("warnings", [])),
        "errors": [],
    }

    # Step 1: Split images
    dynamic_parts, standalone_images = collect_partition_images(payload_images_dir)
    result["dynamic_super_partitions"] = {k: str(v) for k, v in dynamic_parts.items()}
    result["standalone_fastboot_images"] = {k: str(v) for k, v in standalone_images.items()}

    missing_dynamic = [p for p in DYNAMIC_SUPER_PARTITIONS if p not in dynamic_parts]
    result["missing_dynamic_partitions"] = missing_dynamic
    if missing_dynamic:
        result["warnings"].append(
            f"Dynamic partitions absent from payload images dir: {', '.join(missing_dynamic)}"
        )

    # Build lpmake command
    lpmake_path = resolve_lpmake_binary()
    command, cmd_warnings, cmd_errors = build_lpmake_command(
        payload_images_dir=payload_images_dir,
        output_super=output_super,
        profile=profile,
        dynamic_parts=dynamic_parts,
        lpmake_path=lpmake_path,
    )
    result["lpmake_command"] = command
    result["warnings"].extend(cmd_warnings)
    result["errors"].extend(cmd_errors)

    if not execute:
        result["status"] = "DRY_RUN" if not cmd_errors else "FAILED"
        return result

    if cmd_errors:
        result["status"] = "FAILED"
        return result

    # Step 2: Copy standalone images to final_images_dir
    final_images_dir.mkdir(parents=True, exist_ok=True)
    for img_name, img_path in standalone_images.items():
        dest = final_images_dir / img_name
        try:
            shutil.copy2(img_path, dest)
            print(f"[super_collector] copied standalone: {img_name}")
        except Exception as exc:
            result["warnings"].append(f"Could not copy standalone image {img_name}: {exc}")

    # Step 3: Build super.img
    output_super.parent.mkdir(parents=True, exist_ok=True)
    if output_super.exists():
        output_super.unlink()

    print(f"[super_collector] running lpmake → {output_super}")
    try:
        proc = subprocess.run(
            command,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0) if os.name == "nt" else 0,
        )
        result["lpmake_executed"] = True
        result["lpmake_return_code"] = proc.returncode
        result["lpmake_output"] = proc.stdout.decode("utf-8", errors="replace")
        if proc.returncode != 0:
            result["errors"].append(
                f"lpmake exited with return code {proc.returncode}"
            )
    except FileNotFoundError as exc:
        result["lpmake_executed"] = True
        result["lpmake_return_code"] = 2
        result["lpmake_output"] = f"[FileNotFoundError] {exc}"
        result["errors"].append(f"lpmake binary not found: {exc}")

    result["super_img_created"] = output_super.is_file()
    if result["super_img_created"]:
        result["super_img_size"] = output_super.stat().st_size
        print(f"[super_collector] super.img created: {result['super_img_size']} bytes")
    else:
        result["errors"].append("lpmake did not produce super.img")

    if not result["super_img_created"]:
        result["status"] = "FAILED"
        return result

    # Step 4: Validate with lpunpack
    validation = validate_super_with_lpunpack(
        super_path=output_super,
        expected_partitions=[p for p in DYNAMIC_SUPER_PARTITIONS if p in dynamic_parts],
        expected_super_size=profile["super_size"],
    )
    result["validation_status"] = validation["status"]
    result["lpdump_summary"] = validation.get("lpdump_summary")
    if validation.get("missing_partitions"):
        result["missing_dynamic_partitions"] = validation["missing_partitions"]
    result["warnings"].extend(validation.get("warnings", []))
    result["errors"].extend(validation.get("errors", []))
    print(f"[super_collector] lpunpack_validation={validation['status']}")

    # Step 5: Verify final_images_dir layout
    # super.img is now written to output_super; ensure it's in final_images_dir
    super_in_final = final_images_dir / "super.img"
    if not super_in_final.is_file() and output_super != super_in_final:
        try:
            shutil.copy2(output_super, super_in_final)
        except Exception as exc:
            result["warnings"].append(f"Could not copy super.img to final_images_dir: {exc}")

    dir_check = check_final_images_dir(final_images_dir, debug_mode=debug_mode)
    result["forbidden_standalone_dynamic_images"] = dir_check["forbidden_dynamic_images"]
    result["final_images_manifest"] = dir_check["final_images_manifest"]
    result["warnings"].extend(dir_check.get("warnings", []))
    result["errors"].extend(dir_check.get("errors", []))

    result["status"] = "FAILED" if result["errors"] else "APPLIED"
    return result


# ── Report writer ──────────────────────────────────────────────────────────────

def write_super_build_reports(
    report: dict[str, Any],
    reports_dir: Path,
) -> tuple[Path, Path]:
    """Write super_build_report.json and super_build_report.txt to reports_dir."""
    reports_dir = Path(reports_dir).resolve()
    reports_dir.mkdir(parents=True, exist_ok=True)

    json_path = reports_dir / "super_build_report.json"
    txt_path = reports_dir / "super_build_report.txt"

    json_path.write_text(
        json.dumps(report, indent=4, ensure_ascii=False, default=str) + "\n",
        encoding="utf-8",
    )

    lpmake_cmd = report.get("lpmake_command") or []
    lines = [
        "DeadZone Super Build Report",
        "===========================",
        f"Status:                    {report.get('status')}",
        f"Payload images dir:        {report.get('payload_images_dir')}",
        f"Output super:              {report.get('output_super')}",
        f"Final images dir:          {report.get('final_images_dir')}",
        f"Super size:                {report.get('super_size')}",
        f"Group name:                {report.get('group_name')}",
        f"Slot mode:                 {report.get('slot_mode')}",
        f"Output format:             {report.get('output_format')}",
        f"lpmake executed:           {report.get('lpmake_executed')}",
        f"lpmake return code:        {report.get('lpmake_return_code')}",
        f"super.img created:         {report.get('super_img_created')}",
        f"super.img size:            {report.get('super_img_size')}",
        f"Validation status:         {report.get('validation_status')}",
        "",
        "Dynamic super partitions:",
    ]
    dyn = report.get("dynamic_super_partitions") or {}
    for name in DYNAMIC_SUPER_PARTITIONS:
        path_str = dyn.get(name, "(missing)")
        lines.append(f"  - {name}: {path_str}")

    lines += ["", "Standalone fastboot images:"]
    standalone = report.get("standalone_fastboot_images") or {}
    if standalone:
        for img_name in sorted(standalone):
            lines.append(f"  - {img_name}: {standalone[img_name]}")
    else:
        lines.append("  (none)")

    lines += ["", "Missing dynamic partitions:"]
    missing = report.get("missing_dynamic_partitions") or []
    lines.append("  (none)" if not missing else "\n".join(f"  - {m}" for m in missing))

    lines += ["", "Forbidden standalone dynamic images:"]
    forbidden = report.get("forbidden_standalone_dynamic_images") or []
    lines.append("  (none)" if not forbidden else "\n".join(f"  - {f}" for f in forbidden))

    lines += ["", "Final images manifest:"]
    manifest = report.get("final_images_manifest") or []
    lines.append("  (none)" if not manifest else "\n".join(f"  - {m}" for m in manifest))

    lines += [
        "",
        "lpdump summary:",
    ]
    lpdump = report.get("lpdump_summary") or "(not available)"
    for ln in lpdump.splitlines():
        lines.append(f"  {ln}")

    lines += [
        "",
        "lpmake command:",
        (f"  {' '.join(str(t) for t in lpmake_cmd)}" if lpmake_cmd else "  (none)"),
        "",
        "Warnings:",
    ]
    warnings = report.get("warnings") or []
    lines.append("  (none)" if not warnings else "\n".join(f"  - {w}" for w in warnings))

    lines += ["", "Errors:"]
    errors = report.get("errors") or []
    lines.append("  (none)" if not errors else "\n".join(f"  - {e}" for e in errors))
    lines.append("")

    txt_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"[super_collector] Report JSON: {json_path}")
    print(f"[super_collector] Report TXT : {txt_path}")
    return json_path, txt_path
