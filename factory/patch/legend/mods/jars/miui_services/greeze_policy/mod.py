"""
Legend JAR mod — miui_services/greeze_policy

Reserved mod slot. Disabled by default — no patches applied until
this mod is explicitly implemented and enabled.

Config gate: greeze_policy (default: False)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

MOD_ID = "greeze_policy"
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
    report["warnings"].append("greeze_policy mod is not yet implemented.")
    return report
