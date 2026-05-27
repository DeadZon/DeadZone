"""Source ROM image collector for DeadZone Factory.

Collects flashable firmware images from extracted ROM source directories.
Separates dynamic partition images (for super.img) from standalone
fastboot images (boot.img, dtbo.img, vbmeta.img, firmware, etc.).

Output
------
    output/images/source/   — all collected images (audit reference)

The caller is responsible for later passing:
    standalone_images → final_image_assembler
    dynamic_images    → super_input_collector / super_rebuilder
"""
from __future__ import annotations

import shutil
from pathlib import Path


# ── Dynamic partition images — must go into super.img, never final ZIP ────────
DYNAMIC_PARTITION_IMAGES: frozenset[str] = frozenset({
    "system.img",
    "system_ext.img",
    "product.img",
    "vendor.img",
    "odm.img",
    "mi_ext.img",
    "vendor_dlkm.img",
    "odm_dlkm.img",
    "system_dlkm.img",
})

# ── Standalone images — common to all platforms ───────────────────────────────
COMMON_STANDALONE: frozenset[str] = frozenset({
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vendor_kernel_boot.img",
    "dtbo.img",
    "vbmeta.img",
    "vbmeta_system.img",
    "vbmeta_vendor.img",
    "logo.img",
    "recovery.img",
    "cust.img",
    "persist.img",
})

# ── Snapdragon-specific firmware ──────────────────────────────────────────────
SNAPDRAGON_FIRMWARE: frozenset[str] = frozenset({
    "abl.img",
    "aop.img",
    "bluetooth.img",
    "cpucp.img",
    "devcfg.img",
    "dsp.img",
    "featenabler.img",
    "hyp.img",
    "imagefv.img",
    "keymaster.img",
    "modem.img",
    "qupfw.img",
    "shrm.img",
    "tz.img",
    "uefi.img",
    "xbl.img",
    "xbl_config.img",
})

# ── MTK-specific firmware ─────────────────────────────────────────────────────
MTK_FIRMWARE: frozenset[str] = frozenset({
    "preloader_raw.img",
    "preloader.img",
    "lk.img",
    "mcupm.img",
    "pi_img.img",
    "spmfw.img",
    "sspm.img",
    "tee.img",
    "gz.img",
    "apusys.img",
    "audio_dsp.img",
    "ccu.img",
    "connsys_bt.img",
    "connsys_gnss.img",
    "connsys_wifi.img",
    "dpm.img",
    "gpueb.img",
    "mcf_ota.img",
    "mcupm.img",
    "md1img.img",
    "mvpu_algo.img",
    "scp.img",
    "vcp.img",
})

# ── Required boot chain (hard fail if missing) ────────────────────────────────
REQUIRED_BOOT_CHAIN: tuple[str, ...] = (
    "boot.img",
    "vendor_boot.img",
    "vbmeta.img",
)

REQUIRED_BOOT_CHAIN_A13: tuple[str, ...] = (
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "vbmeta.img",
)


def _scan_dirs(dirs: list[Path]) -> dict[str, Path]:
    """Scan directories for *.img files; first occurrence wins per name."""
    found: dict[str, Path] = {}
    for d in dirs:
        if not d.is_dir():
            continue
        try:
            for img in sorted(d.rglob("*.img")):
                key = img.name.lower()
                if img.is_file() and key not in found:
                    found[key] = img
        except Exception:
            continue
    return found


def collect_source_images(
    source_dirs: list[Path],
    output_dir: Path,
    soc: str | None = None,
    execute: bool = False,
) -> dict:
    """Collect and classify flashable images from source ROM directories.

    Parameters
    ----------
    source_dirs:
        Directories to search (searched in order; first match wins).
    output_dir:
        Destination: output/images/source/
    soc:
        "mtk" or "snapdragon" — determines which firmware set to include.
        None → include both MTK and Snapdragon sets (safe default).
    execute:
        False → dry-run (no files copied). True → copy files.

    Returns
    -------
    dict:
        status                — "DRY_RUN" | "APPLIED" | "FAILED"
        standalone_images     — {name: path_str} standalone fastboot images
        dynamic_images        — {name: path_str} dynamic partition images
        missing_required      — list of missing boot-chain image names
        all_found_count       — total .img files found across all dirs
        warnings, errors
    """
    source_dirs = [Path(d) for d in source_dirs]
    output_dir = Path(output_dir)
    is_mtk = str(soc or "").lower() == "mtk"
    is_snap = str(soc or "").lower() in ("snapdragon", "qcom", "snap")

    platform_firmware: frozenset[str]
    if is_mtk:
        platform_firmware = MTK_FIRMWARE
    elif is_snap:
        platform_firmware = SNAPDRAGON_FIRMWARE
    else:
        platform_firmware = MTK_FIRMWARE | SNAPDRAGON_FIRMWARE

    standalone_set = COMMON_STANDALONE | platform_firmware

    all_found = _scan_dirs(source_dirs)

    standalone_images: dict[str, Path] = {}
    dynamic_images: dict[str, Path] = {}

    for name_lower, path in all_found.items():
        if name_lower in DYNAMIC_PARTITION_IMAGES:
            dynamic_images[name_lower] = path
        elif name_lower != "super.img":
            # Collect any .img that is not a dynamic partition or bare super.img
            standalone_images[name_lower] = path

    # Determine required set (init_boot.img implies Android 13+ GKI)
    required = REQUIRED_BOOT_CHAIN_A13 if "init_boot.img" in all_found else REQUIRED_BOOT_CHAIN
    missing_required = [r for r in required if r.lower() not in all_found]

    warnings: list[str] = []
    errors: list[str] = []

    for m in missing_required:
        warnings.append(f"required boot chain image missing: {m}")

    result = {
        "status": "DRY_RUN",
        "source_dirs": [str(d) for d in source_dirs],
        "output_dir": str(output_dir),
        "soc": soc,
        "standalone_images": {k: str(v) for k, v in standalone_images.items()},
        "dynamic_images": {k: str(v) for k, v in dynamic_images.items()},
        "all_found_count": len(all_found),
        "standalone_count": len(standalone_images),
        "dynamic_count": len(dynamic_images),
        "missing_required": missing_required,
        "warnings": warnings,
        "errors": errors,
    }

    if not execute:
        return result

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except Exception as exc:
        errors.append(f"create output_dir: {exc}")
        result.update({"status": "FAILED", "errors": errors})
        return result

    copied: list[str] = []
    all_to_copy = {**standalone_images, **dynamic_images}
    for _name, src in all_to_copy.items():
        target = output_dir / src.name
        try:
            if not target.exists():
                shutil.copy2(src, target)
                copied.append(src.name)
        except Exception as exc:
            errors.append(f"copy {src.name}: {exc}")

    result["copied"] = copied
    result["status"] = "FAILED" if errors else "APPLIED"
    result["errors"] = errors
    result["warnings"] = warnings
    return result
