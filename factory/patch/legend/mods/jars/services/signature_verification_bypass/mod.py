"""
Legend JAR mod — services/signature_verification_bypass

Patches services.jar smali files to disable APK signature verification.

Target classes (found by rglob within unpack_dir):
  PackageManagerServiceUtils.smali — checkDowngrade → return-void
  KeySetManagerService.smali       — shouldCheckUpgradeKeySetLocked → false
  InstallPackageHelper.smali       — force v12=1 before isLeavingSharedUser()
  ReconcilePackageUtils.smali      — flip first const/4 v0, 0x0 → 0x1

Config gate: signature_verification_bypass (default: False)
Security sensitive: True
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from factory.patch.legend.mods._shared import find_first

MOD_ID = "signature_verification_bypass"
TARGET_JAR = "services.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes": [
        "PackageManagerServiceUtils.smali",
        "KeySetManagerService.smali",
        "InstallPackageHelper.smali",
        "ReconcilePackageUtils.smali",
    ],
    "target_methods": [
        "checkDowngrade",
        "shouldCheckUpgradeKeySetLocked",
        "isLeavingSharedUser (guard patch)",
        "v0 flip",
    ],
    "enabled_by_default": False,
    "security_sensitive": True,
    "report_keys": ["status", "enabled", "patched_classes", "patched_methods", "skipped_missing"],
}


def _ow(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def _patch_pms_utils(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    tgt = find_first(root, "PackageManagerServiceUtils.smali")
    if not tgt:
        return "MISSING", []
    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, in_m, changed = [], False, False
    for ln in lines:
        s = ln.strip()
        if s.startswith(".method") and "checkDowngrade" in s:
            in_m = True
            out.append(ln)
            out.append("    .locals 0\n    return-void\n")
            changed = True
            continue
        if in_m and s.startswith(".end method"):
            out.append(ln); in_m = False; continue
        if in_m:
            continue
        out.append(ln)
    if changed and not dry_run:
        _ow(tgt, "".join(out))
    return ("PATCHED" if changed else "SKIPPED"), (["PackageManagerServiceUtils.smali::checkDowngrade"] if changed else [])


def _patch_keyset(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    tgt = find_first(root, "KeySetManagerService.smali")
    if not tgt:
        return "MISSING", []
    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, in_m, changed = [], False, False
    for ln in lines:
        s = ln.strip()
        if s.startswith(".method") and "shouldCheckUpgradeKeySetLocked" in s:
            in_m = True
            out.append(ln)
            out.append("    .locals 1\n    const/4 v0, 0x0\n    return v0\n")
            changed = True
            continue
        if in_m and s.startswith(".end method"):
            out.append(ln); in_m = False; continue
        if in_m:
            continue
        out.append(ln)
    if changed and not dry_run:
        _ow(tgt, "".join(out))
    return ("PATCHED" if changed else "SKIPPED"), (["KeySetManagerService.smali::shouldCheckUpgradeKeySetLocked"] if changed else [])


def _patch_install_helper(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    tgt = find_first(root, "InstallPackageHelper.smali")
    if not tgt:
        return "MISSING", []
    lines = tgt.read_text(encoding="utf-8").splitlines(True)
    out, changed = [], 0
    i = 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if "if-eqz v12" in s:
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and "isLeavingSharedUser()Z" in lines[j]:
                # A14/15 uses {v7} → const/4 v12; A16 uses {p1} → const/4 v0
                if "{v7}" in lines[j]:
                    out.append("    const/4 v12, 0x1\n")
                else:
                    out.append("    const/4 v0, 0x1\n")
                changed += 1
        out.append(ln)
        i += 1
    if changed and not dry_run:
        _ow(tgt, "".join(out))
    return ("PATCHED" if changed else "SKIPPED"), (["InstallPackageHelper.smali::isLeavingSharedUser (guard)"] if changed else [])


def _patch_reconcile(root: Path, dry_run: bool) -> tuple[str, list[str]]:
    tgt = find_first(root, "ReconcilePackageUtils.smali")
    if not tgt:
        return "MISSING", []
    txt = tgt.read_text(encoding="utf-8")
    new = txt.replace("const/4 v0, 0x0", "const/4 v0, 0x1", 1)
    if new != txt:
        if not dry_run:
            _ow(tgt, new)
        return "PATCHED", ["ReconcilePackageUtils.smali::v0_flip"]
    return "SKIPPED", []


def apply(unpack_dir: Path, config: dict, dry_run: bool = True) -> dict[str, Any]:
    enabled = config.get(MOD_ID, False)

    report: dict[str, Any] = {
        "mod_id":          MOD_ID,
        "target_jar":      TARGET_JAR,
        "status":          "UNKNOWN",
        "enabled":         enabled,
        "patched_classes": [],
        "patched_methods": [],
        "skipped_missing": [],
        "warnings":        [],
        "errors":          [],
    }

    if not enabled:
        report["status"] = "SKIPPED_CONFIG_DISABLED"
        return report

    if not unpack_dir.is_dir():
        report["status"] = "FAILED"
        report["errors"].append(f"unpack_dir not found: {unpack_dir}")
        return report

    patched: list[str] = []
    missing: list[str] = []

    for fn, args in [
        (_patch_pms_utils,      (unpack_dir, dry_run)),
        (_patch_keyset,         (unpack_dir, dry_run)),
        (_patch_install_helper, (unpack_dir, dry_run)),
        (_patch_reconcile,      (unpack_dir, dry_run)),
    ]:
        try:
            st, methods = fn(*args)
            if st == "MISSING":
                missing.append(fn.__name__.replace("_patch_", ""))
            else:
                patched.extend(methods)
        except Exception as exc:
            report["errors"].append(f"{fn.__name__}: {exc}")

    report["patched_methods"] = patched
    report["patched_classes"] = list({m.split("::")[0] for m in patched})
    report["skipped_missing"] = missing

    if report["errors"]:
        report["status"] = "FAILED"
    elif dry_run:
        report["status"] = "DRY_RUN"
    elif patched:
        report["status"] = "APPLIED"
    else:
        report["status"] = "SKIPPED"

    return report
