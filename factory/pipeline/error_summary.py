"""Error normalisation for DeadZone build failures.

Maps raw exception/error strings to human-readable summaries with hints,
used by Telegram failure notifications and pipeline reports.
"""
from __future__ import annotations

import re


def summarize_error(error: str, stage: str = "") -> dict:
    """Classify a raw error string into a structured human-readable summary.

    Parameters
    ----------
    error:
        Raw exception message or error string from the pipeline.
    stage:
        Stage ID where the error occurred (e.g. "ASSEMBLING_IMAGES").

    Returns
    -------
    dict with keys:
        title       — short title of the failure
        stage       — stage ID (passed through or inferred)
        reason      — human-readable explanation of what went wrong
        hint        — short fix suggestion
        raw_error   — original error string (truncated to 500 chars)
    """
    err = (error or "").strip()
    err_lower = err.lower()
    stage = (stage or "").upper()

    # ── Same-file copy ────────────────────────────────────────────────────────
    if "are the same file" in err_lower or "same file" in err_lower:
        name = "super.img"
        m = re.search(r"copy\s+(\S+\.img)", err_lower)
        if m:
            name = m.group(1)
        return {
            "title": "Final image assembly failed",
            "stage": stage or "ASSEMBLING_IMAGES",
            "reason": (
                f"{name} was already in the final images directory and was copied onto itself. "
                "preserve_original_super strategy places super.img directly in the final dir; "
                "the assembler must skip same-file copies."
            ),
            "hint": "Skip same-file copy and continue — super.img is already in place.",
            "raw_error": err[:500],
        }

    # ── Missing ROM / file not found ─────────────────────────────────────────
    if "missing after cleanup" in err_lower or "cleanup must run before" in err_lower:
        return {
            "title": "ROM file missing before detection",
            "stage": stage or "DETECTING_ROM",
            "reason": (
                "The downloaded ROM file was deleted by preflight_cleanup because the cleanup "
                "ran after the ROM was already downloaded. The pipeline must preserve the active "
                "ROM path during cleanup."
            ),
            "hint": "Ensure preflight_cleanup is called with preserve_paths=[rom_path].",
            "raw_error": err[:500],
        }

    if "no such file" in err_lower or "file not found" in err_lower or "filenotfounderror" in err_lower:
        return {
            "title": "Required file not found",
            "stage": stage or "DETECTING_ROM",
            "reason": "A required file was not found on disk. The ROM may not have been downloaded or a previous step failed to produce it.",
            "hint": "Check that the download step completed and that cleanup did not remove the file.",
            "raw_error": err[:500],
        }

    # ── Unknown ROM format ────────────────────────────────────────────────────
    if "unknown rom format" in err_lower or "format_unknown" in err_lower:
        return {
            "title": "Unknown ROM format",
            "stage": stage or "DETECTING_ROM",
            "reason": (
                "The ROM file was not recognised as any supported format. "
                "Supported formats: payload_ota, fastboot_tgz/tar, images_zip, "
                "xiaomi_eu_zip, split_super_zip, new_dat_br_zip, raw_super_zip."
            ),
            "hint": "Verify the ROM URL points to a valid Xiaomi HyperOS fastboot or OTA ROM.",
            "raw_error": err[:500],
        }

    # ── No dynamic partitions + no original super ─────────────────────────────
    if "no dynamic partition" in err_lower and "no original super" in err_lower:
        return {
            "title": "Cannot rebuild super — no source images",
            "stage": stage or "PRESERVING_SUPER",
            "reason": (
                "No dynamic partition images were found and no original super.img exists. "
                "Without either, super.img cannot be built."
            ),
            "hint": "Check the ROM format — it may not include super.img or dynamic partitions.",
            "raw_error": err[:500],
        }

    # ── No dynamic partitions (but original super exists) ────────────────────
    if "no dynamic partition" in err_lower:
        return {
            "title": "No dynamic partition images",
            "stage": stage or "PRESERVING_SUPER",
            "reason": (
                "No dynamic partition images (system.img, vendor.img, etc.) were extracted. "
                "If an original super.img exists, the preserve_original_super strategy should be used."
            ),
            "hint": "Use preserve_original_super=True when original super.img is present.",
            "raw_error": err[:500],
        }

    # ── Payload dump failed ───────────────────────────────────────────────────
    if "payload" in err_lower and ("dump" in err_lower or "extract" in err_lower or "failed" in err_lower):
        return {
            "title": "Payload extraction failed",
            "stage": stage or "UNPACKING_ROM",
            "reason": "payload.bin was found in the OTA ZIP but could not be extracted into partition images.",
            "hint": "Ensure payload-dumper or ota_extractor is available and the payload.bin is not corrupt.",
            "raw_error": err[:500],
        }

    # ── lpmake failed ─────────────────────────────────────────────────────────
    if "lpmake" in err_lower:
        if "not found" in err_lower:
            return {
                "title": "lpmake binary not found",
                "stage": stage or "BUILDING_SUPER",
                "reason": "lpmake binary is missing. It is required to rebuild super.img.",
                "hint": "Ensure the lpmake binary is in third_party/mezo_core or PATH.",
                "raw_error": err[:500],
            }
        return {
            "title": "Super rebuild failed (lpmake error)",
            "stage": stage or "BUILDING_SUPER",
            "reason": "lpmake exited with an error while rebuilding super.img from dynamic partition images.",
            "hint": "Check super_rebuild_report.txt for lpmake output and partition size details.",
            "raw_error": err[:500],
        }

    # ── Stage timeout ─────────────────────────────────────────────────────────
    if "timed out" in err_lower or "timeout" in err_lower:
        return {
            "title": "Stage timed out",
            "stage": stage,
            "reason": f"A pipeline stage exceeded its time limit: {err[:200]}",
            "hint": "Check for large ROM files, slow network, or missing binaries that cause hangs.",
            "raw_error": err[:500],
        }

    # ── Default ───────────────────────────────────────────────────────────────
    title_map = {
        "ASSEMBLING_IMAGES":    "Final image assembly failed",
        "PACKAGING_ZIP":        "ZIP packaging failed",
        "UNPACKING_ROM":        "ROM unpack failed",
        "DETECTING_ROM":        "ROM detection failed",
        "BUILDING_SUPER":       "Super rebuild failed",
        "PRESERVING_SUPER":     "Super preservation failed",
        "COLLECTING_IMAGES":    "Image collection failed",
        "UPLOADING_PIXELDRAIN": "PixelDrain upload failed",
        "VALIDATING_ZIP":       "ZIP validation failed",
        "CLEANUP":              "Cleanup failed",
    }
    title = title_map.get(stage, "Build failed")

    return {
        "title": title,
        "stage": stage,
        "reason": err[:300] if err else "Unknown error — check reports artifact for full logs.",
        "hint": "Check reports artifact for full logs.",
        "raw_error": err[:500],
    }
