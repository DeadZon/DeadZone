"""Generate output/reports/eu_migration_plan.json from the eu_reference_scan.

Reads the scan report and classifies recommended imports by priority.
Does NOT import anything automatically — report only.

Run after scan_eu_reference.py.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "output" / "reports"
SCAN_FILE = REPORTS_DIR / "eu_reference_scan.json"
OUT_FILE = REPORTS_DIR / "eu_migration_plan.json"

# ── Priority classification ────────────────────────────────────────────────────
# Map: path_fragment → (priority, notes, deadzone_target_module)
PRIORITY_1: list[dict] = [
    {
        "eu_path_fragment": "Universal/privapp_whitelist_hyperos.xml",
        "reason": "Grants required privapp permissions for HyperOS GMS; safe file_copy to system/etc/permissions",
        "deadzone_target": "factory/patch/mods/legend/eu_import/universal_gms/",
        "action": "file_copy",
        "target_partition": "system",
        "notes": "Wrap in a patch.yml overlay module; copy to /system/etc/permissions/",
    },
    {
        "eu_path_fragment": "Universal/gmsservices",
        "reason": "GMS service overlays/APKs required for Play Services compatibility",
        "deadzone_target": "factory/patch/mods/legend/eu_import/universal_gms/",
        "action": "file_copy",
        "target_partition": "product",
        "notes": "Enumerate APK list, verify against target ROM product manifest before copying",
    },
    {
        "eu_path_fragment": "package/DEBLOAT",
        "reason": "Removes known bloatware; safe debloat list, well-tested across OS versions",
        "deadzone_target": "factory/patch/mods/legend/eu_import/debloat_profiles/",
        "action": "debloat",
        "target_partition": "system",
        "notes": "Convert shell rm list to DeadZone debloat YAML; do NOT use eu shell script",
    },
    {
        "eu_path_fragment": "package/NOTIFICATION_FIX",
        "reason": "Fixes broken notification permission grants on EU/HyperOS builds",
        "deadzone_target": "factory/patch/mods/legend/eu_import/notification_fix/",
        "action": "smali_patch or prop_patch",
        "target_partition": "system",
        "notes": "Audit smali targets; port only the prop/permission changes, not shell logic",
    },
    {
        "eu_path_fragment": "package/RefreshRate",
        "reason": "Unlocks high refresh rate via build.prop; low-risk prop_patch",
        "deadzone_target": "factory/patch/mods/legend/eu_import/refresh_rate/",
        "action": "prop_patch",
        "target_partition": "system",
        "notes": "Extract property keys; apply via DeadZone build_prop patcher",
    },
    {
        "eu_path_fragment": "OS3/security",
        "reason": "SecurityCenter patches for EU region; reduces telemetry calls",
        "deadzone_target": "factory/patch/mods/legend/eu_import/",
        "action": "apk_patch",
        "target_partition": "system",
        "notes": "Requires smali audit before porting; medium complexity",
    },
    {
        "eu_path_fragment": "OS3/systemplugins",
        "reason": "System plugin overlays; safe file_copy, high compat across OS3 variants",
        "deadzone_target": "factory/patch/mods/legend/eu_import/",
        "action": "file_copy",
        "target_partition": "system_ext",
        "notes": "Verify plugin signatures match target ROM build fingerprint",
    },
    {
        "eu_path_fragment": "OS3/launcher",
        "reason": "Launcher mod; improves default home experience on HyperOS OS3",
        "deadzone_target": "factory/patch/mods/legend/eu_import/",
        "action": "apk_patch",
        "target_partition": "system",
        "notes": "Medium risk; launcher smali changes must be validated per ROM version",
    },
]

PRIORITY_2: list[dict] = [
    {
        "eu_path_fragment": "OS3/gallery",
        "reason": "Gallery EU mod; safe apk_patch, minimal side effects",
        "deadzone_target": "factory/patch/mods/legend/eu_import/",
        "action": "apk_patch",
        "target_partition": "product",
        "notes": "Port after Priority 1 is stable",
    },
    {
        "eu_path_fragment": "OS3/thememanager",
        "reason": "Theme manager EU patches; unlocks global theme store",
        "deadzone_target": "factory/patch/mods/legend/eu_import/",
        "action": "apk_patch",
        "target_partition": "system",
        "notes": "Verify against ThemeManager version in target ROM",
    },
    {
        "eu_path_fragment": "OS3/weather",
        "reason": "Weather app EU mod; removes CN data endpoints",
        "deadzone_target": "factory/patch/mods/legend/eu_import/",
        "action": "apk_patch",
        "target_partition": "product",
        "notes": "Safe but low priority — weather mod is cosmetic",
    },
    {
        "eu_path_fragment": "package/KouseiPatcher",
        "reason": "Font/locale patcher; medium risk smali patches on framework",
        "deadzone_target": "factory/patch/mods/legend/eu_import/",
        "action": "smali_patch",
        "target_partition": "system",
        "notes": "Requires framework smali expertise; validate on each ROM version",
    },
    {
        "eu_path_fragment": "package/COREPATCH",
        "reason": "Core framework signature bypass helpers; useful for sideloading",
        "deadzone_target": "factory/patch/mods/legend/eu_import/",
        "action": "smali_patch",
        "target_partition": "system",
        "notes": "Medium risk; only port the signature-bypass portion, not full COREPATCH",
    },
]

NEVER_IMPORT: list[dict] = [
    {
        "eu_path_fragment": "bin/script2flash/packROM.sh",
        "reason": "Uses `du -sb` for lpmake partition sizing — DeadZone must use payload_manifest sizes only",
    },
    {
        "eu_path_fragment": "bin/script2flash/uploadROM.sh",
        "reason": "Uses super.img.zst + OneDrive — DeadZone uses fastboot ZIP + PixelDrain",
    },
    {
        "eu_path_fragment": "package/DISABLE_AVB",
        "reason": "fstab AVB/encrypt patching — DeadZone handles vbmeta via its own vbmeta_legacy flow",
    },
    {
        "eu_path_fragment": ".github/workflows/ (any eu workflow)",
        "reason": "eu workflow YAML must never be copied into DeadZone .github/workflows/",
    },
    {
        "eu_path_fragment": "functions.sh (disable_avb_verify / remove_data_encrypt)",
        "reason": "fstab_patch logic — incompatible with DeadZone super/repack pipeline",
    },
]


def main() -> None:
    if not SCAN_FILE.exists():
        print(
            f"[ERROR] Scan report not found: {SCAN_FILE}\n"
            "Run scripts/scan_eu_reference.py first.",
            file=sys.stderr,
        )
        sys.exit(1)

    scan = json.loads(SCAN_FILE.read_text(encoding="utf-8"))

    plan = {
        "schema_version": "1.0",
        "source_scan": str(SCAN_FILE.relative_to(REPO_ROOT)).replace("\\", "/"),
        "total_scanned": scan["summary"]["total"],
        "import_policy": "manual_only — no automatic imports; each item requires explicit DeadZone module implementation",
        "priority_1": PRIORITY_1,
        "priority_2": PRIORITY_2,
        "never_import": NEVER_IMPORT,
    }

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(plan, indent=2), encoding="utf-8")
    print(f"Migration plan written -> {OUT_FILE}")
    print(f"  Priority 1 items : {len(PRIORITY_1)}")
    print(f"  Priority 2 items : {len(PRIORITY_2)}")
    print(f"  Never-import list: {len(NEVER_IMPORT)}")


if __name__ == "__main__":
    main()
