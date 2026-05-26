# EU Reference Audit — DeadZone Porting Guide

Source repo: DeadZon/eu (NothingsVN Xiaomi AutoBuild)
Local copy: `third_party/eu_reference/`
Scan report: `output/reports/eu_reference_scan.json`
Migration plan: `output/reports/eu_migration_plan.json`

---

## 1. What is safe to port

### Priority 1 (port first)

| EU source | DeadZone target | Action | Notes |
|-----------|----------------|--------|-------|
| `Universal/privapp_whitelist_hyperos.xml` | `factory/patch/mods/legend/eu_import/universal_gms/` | file_copy | Copy to `/system/etc/permissions/` via patch.yml overlay |
| `Universal/gmsservices` | `factory/patch/mods/legend/eu_import/universal_gms/` | file_copy | Enumerate APK list; verify against product manifest |
| `package/DEBLOAT` | `factory/patch/mods/legend/eu_import/debloat_profiles/` | debloat YAML | Convert shell rm list to DeadZone debloat YAML; do NOT use eu shell script |
| `package/NOTIFICATION_FIX` | `factory/patch/mods/legend/eu_import/notification_fix/` | prop_patch / smali | Audit smali targets; port only prop/permission changes |
| `package/RefreshRate` | `factory/patch/mods/legend/eu_import/refresh_rate/` | prop_patch | Extract property keys; apply via build_prop patcher |
| `OS3/security` | `factory/patch/mods/legend/eu_import/` | apk_patch | Requires smali audit per ROM version |
| `OS3/systemplugins` | `factory/patch/mods/legend/eu_import/` | file_copy | Verify plugin signatures match ROM fingerprint |
| `OS3/launcher` | `factory/patch/mods/legend/eu_import/` | apk_patch | Medium risk; validate smali per ROM version |

### Priority 2 (port after P1 is stable)

| EU source | Action | Notes |
|-----------|--------|-------|
| `OS3/gallery` | apk_patch | Safe, low impact |
| `OS3/thememanager` | apk_patch | Verify against ThemeManager version |
| `OS3/weather` | apk_patch | Cosmetic; low priority |
| `package/KouseiPatcher` | smali_patch | Framework smali; validate per ROM |
| `package/COREPATCH` | smali_patch | Port signature-bypass portion only |

---

## 2. What must NEVER be ported

| EU item | Reason |
|---------|--------|
| `bin/script2flash/packROM.sh` lpmake sizing | Uses `du -sb` for partition sizes. DeadZone **must** use `payload_manifest` / original metadata sizes only. Importing this would corrupt super layout on any ROM where the EROFS image shrinks after repack. |
| `bin/script2flash/uploadROM.sh` | Uses `super.img.zst` + OneDrive upload. DeadZone uses uncompressed fastboot ZIP + PixelDrain. Mixing these breaks the flash pipeline. |
| `package/DISABLE_AVB` fstab logic | Patches fstab to disable AVB verification and data encryption. DeadZone handles vbmeta via `factory/images/vbmeta_legacy.py`; fstab patching would conflict and could brick devices on A/B slot. |
| `functions.sh` (`disable_avb_verify` / `remove_data_encrypt`) | Same reason as above — fstab_patch is incompatible with DeadZone super/repack pipeline. |
| Any eu `.github/workflows/*.yml` | eu CI is designed for a different pipeline. Importing workflow YAMLs would break DeadZone's Fly.io dispatch and create rogue build jobs. |

---

## 3. How to convert eu shell mods into DeadZone patch.yml modules

### Step 1 — identify the mod's effect

Determine what the eu shell script actually does:

- **File copy** (`cp src dest`) → DeadZone `file_copy` action in patch.yml
- **Property set** (`sed -i` on build.prop) → DeadZone `build_prop` patcher entry
- **APK replace** (`cp new.apk system/app/...`) → DeadZone `apk_patch` with ApkEditor
- **Smali patch** (baksmali + patch + smali) → DeadZone `smali_patch` via `factory/patch/common/smali_tools.py`
- **Debloat** (`rm -rf system/app/Foo`) → DeadZone debloat YAML list

### Step 2 — write a patch.yml module

```yaml
# factory/patch/mods/legend/eu_import/<mod_name>/patch.yml
name: eu_import/<mod_name>
description: "Ported from eu repo: <eu_path>"
target_partition: system   # or product / system_ext / vendor
actions:
  - type: file_copy
    src: eu_import/<mod_name>/files/
    dest: /system/etc/permissions/
  # OR
  - type: prop_patch
    props:
      persist.sys.refresh_rate: "120"
```

### Step 3 — do NOT call eu scripts

Never use `subprocess.run` on any file inside `third_party/eu_reference/`.
The validator (`scripts/validate_eu_reference.py`) will fail the build if it detects this.

### Step 4 — register the module in the edition runner

Add the new module to `factory/patch/mods/legend/actions/run_legend.py` under the appropriate
patch group. Mark it `optional=True` until validated on a real ROM.

---

## 4. Priority order summary

```
1. privapp_whitelist_hyperos.xml  — unblock GMS on day 1
2. gmsservices                    — GMS service layer
3. DEBLOAT                        — clean bloat before other mods
4. NOTIFICATION_FIX               — fix notification grants
5. RefreshRate                    — simple prop, high user value
6. OS3/security                   — reduce telemetry
7. OS3/systemplugins              — safe overlay
8. OS3/launcher                   — visible UX improvement
-------- validate P1 on real ROM before proceeding to P2 --------
9.  OS3/gallery
10. OS3/thememanager
11. OS3/weather
12. KouseiPatcher
13. COREPATCH (signature-bypass portion only)
```

---

## 5. Validation

Run before any commit that touches `factory/` or `third_party/eu_reference/`:

```
python scripts/validate_eu_reference.py
```

This checks:
- No eu script has `direct_execution_allowed=true` in the scan report
- `du -sb` is not used as lpmake sizing in `factory/repack`
- No image file-size fallback in super code
- No eu workflow YAML in `.github/workflows/`
- Scanner does not execute eu scripts via subprocess
