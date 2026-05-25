"""
Legend JAR mod — framework/mezo_core

Metadata wrapper for the existing class-level MEZO patches applied to
framework.jar. The actual patching is done by the auto-discovery mechanism
that loads every module from factory/patch/legend/mtcr/framework/.

This mod's apply() reports that class-level patches are active; it does
NOT duplicate any patch logic.
"""
from __future__ import annotations

from pathlib import Path

MOD_ID = "mezo_core"
TARGET_JAR = "framework.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes":     ["(auto-discovered from mtcr/framework/)"],
    "target_methods":     ["(see individual class modules)"],
    "enabled_by_default": True,
    "security_sensitive": False,
    "report_keys":        ["status", "enabled", "patched_classes", "patched_methods"],
}


def apply(unpack_dir: Path, config: dict, dry_run: bool = True) -> dict:
    enabled = config.get(MOD_ID, True)
    return {
        "mod_id":          MOD_ID,
        "target_jar":      TARGET_JAR,
        "status":          "ACTIVE" if enabled else "SKIPPED_CONFIG_DISABLED",
        "enabled":         enabled,
        "patched_classes": ["(handled by mtcr/framework/ class-level discovery)"],
        "patched_methods": [],
        "warnings":        [] if enabled else [f"{MOD_ID} disabled in config."],
        "errors":          [],
        "note":            "Class-level patches run via auto-discovery; "
                           "this entry is a registry placeholder.",
    }
