"""
Legend JAR mod — miui_services/gboard_replace_baidu

Replaces the Baidu IME package name with Gboard in miui-services.jar smali files.

Searches for: com.baidu.input_mi
Replaces with: com.google.android.inputmethod.latin

Target files:
  DevicePolicyManagerServiceStubImpl.smali
  InputManagerServiceStubImpl.smali
  InputMethodManagerServiceImpl.smali
  ActivityTaskSupervisorImpl.smali
  MiuiSplitInputMethodImpl.smali

Config gate: gboard_replace_baidu (default: True)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from factory.patch.legend.mods._shared import gboard_replace_in_dir

MOD_ID = "gboard_replace_baidu"
TARGET_JAR = "miui-services.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes": [
        "DevicePolicyManagerServiceStubImpl.smali",
        "InputManagerServiceStubImpl.smali",
        "InputMethodManagerServiceImpl.smali",
        "ActivityTaskSupervisorImpl.smali",
        "MiuiSplitInputMethodImpl.smali",
    ],
    "target_methods":     ["(string constant replacement)"],
    "enabled_by_default": True,
    "security_sensitive": False,
    "report_keys":        ["status", "enabled", "files_patched", "files_not_found", "occurrences_replaced"],
}

_TARGET_FILES = [
    "DevicePolicyManagerServiceStubImpl.smali",
    "InputManagerServiceStubImpl.smali",
    "InputMethodManagerServiceImpl.smali",
    "ActivityTaskSupervisorImpl.smali",
    "MiuiSplitInputMethodImpl.smali",
]


def apply(unpack_dir: Path, config: dict, dry_run: bool = True) -> dict[str, Any]:
    enabled = config.get(MOD_ID, True)

    report: dict[str, Any] = {
        "mod_id":               MOD_ID,
        "target_jar":           TARGET_JAR,
        "status":               "UNKNOWN",
        "enabled":              enabled,
        "files_patched":        [],
        "files_not_found":      [],
        "occurrences_replaced": 0,
        "patched_classes":      [],
        "patched_methods":      [],
        "warnings":             [],
        "errors":               [],
    }

    if not enabled:
        report["status"] = "SKIPPED_CONFIG_DISABLED"
        return report

    if not unpack_dir.is_dir():
        report["status"] = "SKIPPED"
        report["warnings"].append(f"unpack_dir not found: {unpack_dir}")
        return report

    details = gboard_replace_in_dir(unpack_dir, _TARGET_FILES, dry_run)
    patched   = [d["path"] for d in details if d["status"] in ("REPLACED", "WOULD_REPLACE")]
    not_found = [d.get("file", "") for d in details if d["status"] == "MISSING"]
    total_occ = sum(d.get("occurrences", 0) for d in details)
    errors    = [f"{d.get('file', '?')}: {d['error']}" for d in details if d.get("error")]

    report["files_patched"]        = patched
    report["files_not_found"]      = not_found
    report["occurrences_replaced"] = total_occ
    report["patched_classes"]      = patched
    report["errors"].extend(errors)

    if errors:
        report["status"] = "FAILED"
    elif not patched and not_found:
        report["status"] = "SKIPPED"
        report["warnings"].append("All target files missing from miui-services unpack_dir.")
    elif not patched:
        report["status"] = "SKIPPED"
        report["warnings"].append("No Baidu IME strings found in target files.")
    elif dry_run:
        report["status"] = "DRY_RUN"
    else:
        report["status"] = "APPLIED"

    return report
