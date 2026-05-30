from __future__ import annotations

from typing import Any


_SIGNATURES: list[dict[str, Any]] = [
    {
        "error_type": "MISSING_ROM",
        "stage_hint": "download",
        "patterns": ["404", "not found", "no such file", "download failed", "connection refused", "urlopen error", "http error"],
        "cause": "ROM file not found or download failed",
        "suggested_fix": "Verify the ROM URL is accessible and the download source is online",
    },
    {
        "error_type": "PAYLOAD_UNPACK_FAILED",
        "stage_hint": "unpack",
        "patterns": ["payload.bin", "payload", "brotli", "zstandard", "unpack failed", "extraction failed", "ota package"],
        "cause": "ROM payload.bin extraction failed",
        "suggested_fix": "Check that the ROM URL points to a complete OTA zip and it is not corrupted",
    },
    {
        "error_type": "IMAGE_MOUNT_FAILED",
        "stage_hint": "image_extraction",
        "patterns": ["image_extraction", "mount failed", "ext4", "erofs", "sparse", "could not extract", "partition image"],
        "cause": "Partition image extraction or mount failed",
        "suggested_fix": "Check partition image format and that the required tools are installed",
    },
    {
        "error_type": "APP_SCAN_FAILED",
        "stage_hint": "app_inventory",
        "patterns": ["app_inventory", "scan failed", "inventory", "apk scan"],
        "cause": "App inventory scan failed",
        "suggested_fix": "Check that partition images were extracted correctly before the scan",
    },
    {
        "error_type": "PATCH_FAILED",
        "stage_hint": "style",
        "patterns": ["patch failed", "apply_style", "style runner", "legend patch", "gaming patch", "epic patch", "stable patch"],
        "cause": "Style patch application failed",
        "suggested_fix": "Check the style runner and the partition tree for unexpected state",
    },
    {
        "error_type": "SUPER_INFO_MISSING",
        "stage_hint": "super_profile",
        "patterns": ["no metadata allocation", "super info missing", "super profile", "missing super", "no allocation"],
        "cause": "Super partition metadata or allocation is missing",
        "suggested_fix": "Check super_profile_report.txt and payload metadata for the device",
    },
    {
        "error_type": "LPMAKE_FAILED",
        "stage_hint": "super",
        "patterns": ["lpmake", "super image build", "super build", "lpunpack", "lpadd"],
        "cause": "lpmake super image build failed",
        "suggested_fix": "Check super_build_report.txt, verify lpmake binary, and review partition sizes",
    },
    {
        "error_type": "VBMETA_PATCH_FAILED",
        "stage_hint": "final_zip",
        "patterns": ["vbmeta", "avb", "verification failed", "boot image"],
        "cause": "vbmeta patching or AVB verification failed",
        "suggested_fix": "Check vbmeta patch logic and ensure the correct vbmeta flags are set",
    },
    {
        "error_type": "FASTBOOT_VALIDATION_FAILED",
        "stage_hint": "size_policy",
        "patterns": ["size policy", "exceeds", "too large", "final zip", "zip size"],
        "cause": "Final ZIP exceeds the configured size policy limit",
        "suggested_fix": "Enable size reduction or increase the final_zip_max_gb limit",
    },
    {
        "error_type": "ZIP_VALIDATION_FAILED",
        "stage_hint": "final_zip",
        "patterns": ["zip validation", "zip build", "final_zip", "zip integrity", "zip failed"],
        "cause": "Final ZIP assembly or validation failed",
        "suggested_fix": "Check final_zip_report.txt and available disk space",
    },
    {
        "error_type": "PIXELDRAIN_UPLOAD_FAILED",
        "stage_hint": "upload",
        "patterns": ["pixeldrain", "upload failed", "pixeldrain api", "api key", "pixeldrain error"],
        "cause": "PixelDrain upload failed",
        "suggested_fix": "Check PIXELDRAIN_API_KEY environment variable and network connectivity",
    },
    {
        "error_type": "TELEGRAM_FAILED",
        "stage_hint": "telegram",
        "patterns": ["telegram", "bot token", "chat_id", "sendmessage", "telegram api"],
        "cause": "Telegram notification failed",
        "suggested_fix": "Check TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID environment variables",
    },
]


def classify_error(error: str, stage: str = "") -> dict[str, Any]:
    raw = str(error or "").strip()
    lower = raw.lower()
    stage_lower = stage.lower()

    for sig in _SIGNATURES:
        stage_hint = sig["stage_hint"]
        patterns: list[str] = sig["patterns"]

        stage_match = stage_hint in stage_lower or not stage_lower
        pattern_match = any(p in lower for p in patterns)

        if pattern_match or (stage_match and stage_hint in stage_lower):
            return {
                "error_type": sig["error_type"],
                "stage": stage or stage_hint,
                "cause": sig["cause"],
                "suggested_fix": sig["suggested_fix"],
                "raw_error": raw[:800],
            }

    return {
        "error_type": "BUILD_FAILED",
        "stage": stage or "unknown",
        "cause": raw[:400] or "Unexpected build failure",
        "suggested_fix": "Check reports and logs artifacts for the failing stage",
        "raw_error": raw[:800],
    }


def classify_from_context(ctx: object) -> dict[str, Any]:
    error = str(getattr(ctx, "failure_error", "") or "")
    stage = str(getattr(ctx, "failed_stage", "") or "")
    return classify_error(error, stage)
