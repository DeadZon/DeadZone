"""
Legend JAR mod — miui_framework/mezo_core

Metadata wrapper for the mezo_core class-level patches targeting
miui-framework.jar. Actual patches are auto-discovered by the MTCR runner
via the existing mtcr/miui_framework/ module tree.

Config gate: mezo_core (default: True)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

MOD_ID = "mezo_core"
TARGET_JAR = "miui-framework.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes":     ["(auto-discovered via mtcr/miui_framework/ modules)"],
    "target_methods":     ["(see individual mtcr rule modules)"],
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
        "mezo_core patches for miui-framework.jar are applied via MTCR class-level "
        "auto-discovery (mtcr/miui_framework/ modules). This entry confirms the mod is enabled."
    )
    return report
