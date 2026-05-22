"""
Legend JAR mod — miui_services/multi_floating_window

Patches MiuiFreeFormStackDisplayStrategy.smali in miui-services.jar to
increase the maximum number of floating (freeform) windows.

Target method: getMaxMiuiFreeFormStackCount
Patch: replace the const instruction that returns the limit with the
       configured value (default 50).

Config gate: multi_floating_window (default: True)
Config key:  freeform_max_count (default: 50)
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from factory.patch.legend.mods._shared import find_first, smali_const

MOD_ID = "multi_floating_window"
TARGET_JAR = "miui-services.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes":     ["MiuiFreeFormStackDisplayStrategy.smali"],
    "target_methods":     ["getMaxMiuiFreeFormStackCount"],
    "enabled_by_default": True,
    "security_sensitive": False,
    "report_keys":        ["status", "enabled", "freeform_max_count",
                           "patched_classes", "patched_methods"],
}

_TARGET_FILE = "MiuiFreeFormStackDisplayStrategy.smali"
_TARGET_METHOD = "getMaxMiuiFreeFormStackCount"


def apply(unpack_dir: Path, config: dict, dry_run: bool = True) -> dict[str, Any]:
    enabled   = config.get(MOD_ID, True)
    max_count = int(config.get("freeform_max_count", 50))

    report: dict[str, Any] = {
        "mod_id":           MOD_ID,
        "target_jar":       TARGET_JAR,
        "status":           "UNKNOWN",
        "enabled":          enabled,
        "freeform_max_count": max_count,
        "patched_classes":  [],
        "patched_methods":  [],
        "warnings":         [],
        "errors":           [],
    }

    if not enabled:
        report["status"] = "SKIPPED_CONFIG_DISABLED"
        return report

    if not unpack_dir.is_dir():
        report["status"] = "SKIPPED"
        report["warnings"].append(f"unpack_dir not found: {unpack_dir}")
        return report

    tgt = find_first(unpack_dir, _TARGET_FILE)
    if not tgt:
        report["status"] = "SKIPPED"
        report["warnings"].append(f"{_TARGET_FILE} not found in {unpack_dir}")
        return report

    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, in_method, changed = [], False, False

    for line in lines:
        s = line.strip()
        if s.startswith(".method") and _TARGET_METHOD in s:
            in_method = True
        elif in_method and s.startswith(".end method"):
            in_method = False

        if in_method and s.startswith("const") and not s.startswith("const-string"):
            parts = s.split(",", 1)
            if len(parts) == 2:
                reg = parts[0].split()[-1].strip()
                replacement = smali_const(reg, max_count)
                out.append(f"    {replacement}\n")
                changed = True
                continue

        out.append(line)

    if changed:
        if not dry_run:
            tgt.write_text("".join(out), encoding="utf-8")
        report["patched_classes"] = [_TARGET_FILE]
        report["patched_methods"] = [f"{_TARGET_FILE}::{_TARGET_METHOD}"]
        report["status"] = "DRY_RUN" if dry_run else "APPLIED"
    else:
        report["status"] = "SKIPPED"
        report["warnings"].append(
            f"{_TARGET_METHOD} not found or no const instruction to patch in {_TARGET_FILE}."
        )

    return report
