"""
Legend JAR mod — miui_services/shortcut_settings_observer

Reserved mod slot. Disabled by default — no patches applied until
this mod is explicitly implemented and enabled.

Config gate: shortcut_settings_observer (default: False)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

MOD_ID = "shortcut_settings_observer"
TARGET_JAR = "miui-services.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes":     [],
    "target_methods":     [],
    "enabled_by_default": False,
    "security_sensitive": False,
    "report_keys":        ["status", "enabled"],
}


def apply(unpack_dir: Path, config: dict, dry_run: bool = True) -> dict[str, Any]:
    enabled = config.get(MOD_ID, False)
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

    report["status"] = "SKIPPED"
    report["warnings"].append("shortcut_settings_observer mod is not yet implemented.")
    return report
