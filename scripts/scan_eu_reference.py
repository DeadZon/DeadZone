"""Scan third_party/eu_reference and produce a structured JSON audit report.

Output: output/reports/eu_reference_scan.json

Each entry reports:
  path, category, target_os, target_partition, risk_level,
  action_type, executable_script_found, direct_execution_allowed
"""
from __future__ import annotations

import json
import os
import stat
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
EU_ROOT = REPO_ROOT / "third_party" / "eu_reference"
REPORTS_DIR = REPO_ROOT / "output" / "reports"

SCAN_ROOTS = [
    EU_ROOT / "bin" / "modfile",
    EU_ROOT / "bin" / "package",
    EU_ROOT / "bin" / "ddevice",
    EU_ROOT / "bin" / "script2flash",
]

# ── OS detection from path components ─────────────────────────────────────────
OS_TAGS = {"MIUI13", "MIUI14", "OS1", "OS2", "OS3"}

# ── Partition inference from known app/dir names ───────────────────────────────
_PRODUCT_APPS = {
    "appvault", "gallery", "weather", "thememanager", "launcher",
    "gmsservices", "enhancedkeyboard", "packageinstaller",
}
_SYSTEM_EXT_APPS = {"systemplugins"}
_SYSTEM_APPS = {"security", "joyose"}
_VENDOR_APPS: set[str] = set()

# ── Risk classification ────────────────────────────────────────────────────────
_HIGH_RISK_NAMES = {"DISABLE_AVB", "fstab", "avb_verify", "remove_data_encrypt"}
_MEDIUM_RISK_NAMES = {
    "COREPATCH", "KouseiPatcher", "packageinstaller", "launcher",
    "appvault", "security", "joyose",
}
_FLASH_SCRIPT_NAMES = {"script2flash", "packROM.sh", "flash-all.sh", "updater-script"}

# ── Action type inference ──────────────────────────────────────────────────────
_SMALI_EXTS = {".smali"}
_APK_EXTS = {".apk", ".jar"}
_PROP_NAMES = {"build.prop", "system.prop", "default.prop"}
_FSTAB_NAMES_SUB = {"fstab", "avb", "encrypt"}
_DEBLOAT_NAMES = {"DEBLOAT", "debloat"}


def _detect_target_os(parts: tuple[str, ...]) -> str | None:
    for p in parts:
        if p in OS_TAGS:
            return p
    return None


def _detect_partition(parts: tuple[str, ...]) -> str | None:
    for p in parts:
        pl = p.lower()
        if pl in _PRODUCT_APPS:
            return "product"
        if pl in _SYSTEM_EXT_APPS:
            return "system_ext"
        if pl in _SYSTEM_APPS:
            return "system"
        if pl in _VENDOR_APPS:
            return "vendor"
    return None


def _detect_risk(parts: tuple[str, ...]) -> str:
    joined = "/".join(parts)
    for h in _HIGH_RISK_NAMES:
        if h.lower() in joined.lower():
            return "high"
    for m in _MEDIUM_RISK_NAMES:
        if m.lower() in joined.lower():
            return "medium"
    return "safe"


def _detect_action(path: Path, parts: tuple[str, ...]) -> str:
    name_lower = path.name.lower()
    joined_lower = "/".join(parts).lower()
    if path.suffix in _SMALI_EXTS:
        return "smali_patch"
    if path.suffix in _APK_EXTS:
        return "apk_patch"
    if name_lower in _PROP_NAMES:
        return "prop_patch"
    for f in _FSTAB_NAMES_SUB:
        if f in name_lower or f in joined_lower:
            return "fstab_patch"
    for d in _DEBLOAT_NAMES:
        if d in joined_lower:
            return "debloat"
    # directory-level inference
    if path.is_dir():
        return "file_copy"
    # shell / scripts
    if path.suffix in {".sh", ".py", ".pl"}:
        return "unknown"
    if path.suffix in {".xml", ".txt", ""}:
        return "file_copy"
    return "unknown"


def _detect_category(scan_root: Path, parts: tuple[str, ...]) -> str:
    root_name = scan_root.name
    if root_name == "modfile":
        for p in parts:
            if p in OS_TAGS:
                return "os_mod"
        if "Universal" in parts:
            return "universal_mod"
        if "UpdateFile" in parts:
            return "flash_script"
        return "os_mod"
    if root_name == "package":
        return "package_patch"
    if root_name == "ddevice":
        return "device_metadata"
    if root_name == "script2flash":
        return "flash_script"
    return "tool"


def _is_executable(path: Path) -> bool:
    if not path.is_file():
        return False
    if path.suffix in {".sh", ".py", ".pl", ".bash"}:
        return True
    try:
        mode = path.stat().st_mode
        return bool(mode & (stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH))
    except OSError:
        return False


def scan_path(p: Path, scan_root: Path) -> dict:
    rel = p.relative_to(EU_ROOT)
    parts = tuple(rel.parts)
    return {
        "path": str(rel).replace("\\", "/"),
        "category": _detect_category(scan_root, parts),
        "target_os": _detect_target_os(parts),
        "target_partition": _detect_partition(parts),
        "risk_level": _detect_risk(parts),
        "action_type": _detect_action(p, parts),
        "executable_script_found": _is_executable(p),
        "direct_execution_allowed": False,
    }


def main() -> None:
    if not EU_ROOT.exists():
        print(f"[ERROR] EU reference tree not found: {EU_ROOT}", file=sys.stderr)
        sys.exit(1)

    results: list[dict] = []
    for scan_root in SCAN_ROOTS:
        if not scan_root.exists():
            print(f"[WARN] Scan root missing, skipping: {scan_root}")
            continue
        for root, dirs, files in os.walk(scan_root):
            root_path = Path(root)
            # Always record directories as entries (they represent mod units)
            if root_path != scan_root:
                results.append(scan_path(root_path, scan_root))
            for fname in sorted(files):
                fp = root_path / fname
                results.append(scan_path(fp, scan_root))

    # Sort by path for deterministic output
    results.sort(key=lambda e: e["path"])

    summary = {
        "total": len(results),
        "by_category": {},
        "by_risk": {"safe": 0, "medium": 0, "high": 0},
        "executable_scripts": 0,
    }
    for e in results:
        cat = e["category"]
        summary["by_category"][cat] = summary["by_category"].get(cat, 0) + 1
        summary["by_risk"][e["risk_level"]] = summary["by_risk"].get(e["risk_level"], 0) + 1
        if e["executable_script_found"]:
            summary["executable_scripts"] += 1

    report = {
        "schema_version": "1.0",
        "source": "third_party/eu_reference",
        "summary": summary,
        "entries": results,
    }

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = REPORTS_DIR / "eu_reference_scan.json"
    out_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Scan complete: {len(results)} entries -> {out_path}")


if __name__ == "__main__":
    main()
