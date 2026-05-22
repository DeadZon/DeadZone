"""
Legend JAR mod — framework/invoke_custom_handling

Scans framework.jar smali files for invoke-custom instructions and applies
safe compatibility stubs. Targets only well-known safe method signatures:
  equals   → return false
  hashCode → return 0
  toString → return null

Does NOT delete classes. Does NOT touch methods it cannot safely stub.

Config gate: invoke_custom_handling (default: True)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from factory.patch.legend.mods._shared import invoke_custom_scan_dir

MOD_ID = "invoke_custom_handling"
TARGET_JAR = "framework.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes":     ["(any *.smali in framework unpack_dir with invoke-custom)"],
    "target_methods":     ["equals", "hashCode", "toString"],
    "enabled_by_default": True,
    "security_sensitive": False,
    "report_keys":        ["status", "enabled", "invoke_custom_files_found",
                           "invoke_custom_files_patched", "skipped_files"],
}


def apply(unpack_dir: Path, config: dict, dry_run: bool = True) -> dict[str, Any]:
    enabled = config.get(MOD_ID, True)

    report: dict[str, Any] = {
        "mod_id":                      MOD_ID,
        "target_jar":                  TARGET_JAR,
        "status":                      "UNKNOWN",
        "enabled":                     enabled,
        "invoke_custom_files_found":   0,
        "invoke_custom_files_patched": 0,
        "skipped_files":               [],
        "patched_classes":             [],
        "patched_methods":             [],
        "warnings":                    [],
        "errors":                      [],
    }

    if not enabled:
        report["status"] = "SKIPPED_CONFIG_DISABLED"
        return report

    if not unpack_dir.is_dir():
        report["status"] = "SKIPPED"
        report["warnings"].append(f"unpack_dir not found: {unpack_dir}")
        return report

    details = invoke_custom_scan_dir(unpack_dir, dry_run)
    found   = len(details)
    patched = sum(1 for d in details if d["status"] in ("PATCHED", "WOULD_PATCH"))
    skipped = [d["path"] for d in details if d["status"] in ("SKIPPED_UNSAFE", "SKIPPED_UNHANDLED", "ERROR")]
    errors  = [f"{d['file']}: {d['error']}" for d in details if d.get("error")]

    report["invoke_custom_files_found"]   = found
    report["invoke_custom_files_patched"] = patched
    report["skipped_files"]               = skipped
    report["patched_classes"]             = [d["file"] for d in details if d["status"] in ("PATCHED", "WOULD_PATCH")]
    report["patched_methods"]             = [
        f"{d['file']}::{m}" for d in details for m in d.get("methods_patched", [])
    ]
    report["errors"].extend(errors)

    if errors:
        report["status"] = "FAILED"
    elif found == 0:
        report["status"] = "SKIPPED"
        report["warnings"].append("No smali files with invoke-custom found in framework unpack_dir.")
    elif dry_run:
        report["status"] = "DRY_RUN"
    elif patched:
        report["status"] = "APPLIED"
    else:
        report["status"] = "SKIPPED"
        report["warnings"].append(f"Found {found} invoke-custom file(s) but none had safe patchable methods.")

    return report
