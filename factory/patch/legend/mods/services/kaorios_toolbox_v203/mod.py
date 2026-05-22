"""
Legend JAR mod — services/kaorios_toolbox_v203

Stub for services.jar. The Kaorios v2.0.3 DEX is injected into
framework.jar only (see mods/framework/kaorios_toolbox_v203/mod.py).
No separate injection is needed for services.jar.

Config gate: kaorios_toolbox_v203 (default: False)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

MOD_ID = "kaorios_toolbox_v203"
TARGET_JAR = "services.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes":     [],
    "target_methods":     [],
    "enabled_by_default": False,
    "security_sensitive": True,
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
    report["warnings"].append(
        "Kaorios v2.0.3 DEX is injected into framework.jar only. "
        "No action required for services.jar."
    )
    return report
