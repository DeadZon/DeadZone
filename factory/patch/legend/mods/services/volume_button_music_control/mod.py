"""
Legend JAR mod — services/volume_button_music_control

Metadata wrapper for the VolBtnMusicControl class-level patches.
Actual patches are auto-discovered by the MTCR runner via the existing
mtcr/services/ module tree. This mod entry provides registry visibility
and config-gate for the feature group.

Config gate: volume_button_music_control (default: True)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

MOD_ID = "volume_button_music_control"
TARGET_JAR = "services.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes":     ["MediaSessionService.smali", "AudioService.smali"],
    "target_methods":     ["dispatchMediaKeyEvent", "handleVolumeKey"],
    "enabled_by_default": True,
    "security_sensitive": False,
    "report_keys":        ["status", "enabled"],
}


def apply(unpack_dir: Path, config: dict, dry_run: bool = True) -> dict[str, Any]:
    enabled = config.get(MOD_ID, True)
    report: dict[str, Any] = {
        "mod_id":          MOD_ID,
        "target_jar":      TARGET_JAR,
        "status":          "UNKNOWN",
        "enabled":         enabled,
        "patched_classes": [],
        "patched_methods": [],
        "warnings":        [],
        "errors":          [],
    }

    if not enabled:
        report["status"] = "SKIPPED_CONFIG_DISABLED"
        return report

    report["status"] = "ACTIVE"
    report["warnings"].append(
        "volume_button_music_control patches are applied via MTCR class-level "
        "auto-discovery (mtcr/services/ modules). This entry confirms the mod is enabled."
    )
    return report
