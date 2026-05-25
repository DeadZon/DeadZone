"""
Legend-only legacy Kaori Toolbox JAR patch stage.

Carries exact behavior of MEZOBuildRom.py functions:
  - copy_kaorios_folder(work_dir)                lines 3973-4009
  - modify_application_package_manager_kaori(file_path) lines 4012-4127
  - modify_instrumentation_kaori(file_path)      lines 4130-4184
  - modify_keystore2_kaori(file_path)            lines 4187-4222
  - modify_android_keystore_spi_kaori(file_path) lines 4225-4277
  - kaori_toolbox(work_dir)                      lines 4280-4341

Flavor guard: only runs for legend / deadzone_legend / DeadZone_Legend.
All other flavors exit with status SKIPPED_NON_LEGEND.

This stage assumes jars are already unpacked into framework_unpacked /
services_unpacked by the central jar pipeline. It does NOT rebuild jars.

Allowed changes from source:
  - log() -> print()  (log was just print() in MEZOBuildRom.py)
  - ROOT_DIR -> _LEGACY_ROOT  (path fix: third_party/mezo_core)
  - imports reorganised at module level
  - report wrapper before/after execution
  - dry-run guard

Not changed:
  - logic, smali strings, regex, method signatures, class names,
    inserted code snippets, patch order, search strategy

CLI:
  # dry-run:
  python -m factory.patch.mods.legend.kaori_legacy \\
      --work-dir "path/to/jar_work_dir" \\
      --flavor legend

  # execute:
  python -m factory.patch.mods.legend.kaori_legacy \\
      --work-dir "path/to/jar_work_dir" \\
      --flavor legend \\
      --execute

  # with android major:
  python -m factory.patch.mods.legend.kaori_legacy \\
      --work-dir "path/to/jar_work_dir" \\
      --flavor legend \\
      --android-major 16 \\
      --execute

Integration hook (called from factory/patch/legend/jar_patch.py after
jar_misc_legacy and before rebuild/restore):
  from factory.patch.mods.legend.kaori_legacy import apply_kaori_legacy_patch
  apply_kaori_legacy_patch(work_dir, flavor="legend", android_major=16, execute=True)
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

# _LEGACY_ROOT = third_party/mezo_core (where MEZO/kaorios lives)
_LEGACY_ROOT = Path(__file__).resolve().parents[3] / "third_party" / "mezo_core"

_REPO_ROOT   = Path(__file__).resolve().parents[3]
_OUTPUT_ROOT = _REPO_ROOT / "output"
_REPORTS_DIR = _OUTPUT_ROOT / "reports"

_LEGEND_FLAVORS = {"legend", "deadzone_legend"}

_REPORT_JSON = "06_legend_kaori_legacy_report.json"
_REPORT_TXT  = "06_legend_kaori_legacy_report.txt"

_EXPECTED_FOLDERS = [
    "framework_unpacked",
    "services_unpacked",
]

# Smali hook tokens used for guide-compatibility precheck (warning only)
_HOOK_TOKENS = [
    "KaoriPropsUtils",
    "KaoriFeatureOverrides",
    "KaoriFeatureBlock",
    "KaoriKeyboxHooks",
    "KaoriGetKeyEntry",
    "KaoriGetCertificateChain",
    "kaorios",
]


def _normalise_flavor(flavor: str) -> str:
    return flavor.lower().replace("-", "_")


# ── Legacy patch functions ────────────────────────────────────────────────────
# Exact copy of MEZOBuildRom.py:copy_kaorios_folder (lines 3973-4009)
# Path fix: ROOT_DIR -> _LEGACY_ROOT
def copy_kaorios_folder(work_dir: Path) -> bool:
    """Copy kaorios folder from MEZO to framework_unpacked"""
    try:
        source = _LEGACY_ROOT / "MEZO" / "kaorios"
        if not source.exists():
            print(f"    ❌ Không có thư mục nguồn {source}")
            return False

        framework_base = work_dir / "framework_unpacked"
        if not framework_base.exists():
            print("    ❌ Không tìm thấy thư mục framework_unpacked")
            return False

        # Kiểm tra xem có smali_classes6 không, nếu có thì dùng, nếu không thì dùng smali_classes5
        smali_classes6 = framework_base / "smali_classes6"
        if smali_classes6.exists() and smali_classes6.is_dir():
            target_base = smali_classes6
        else:
            target_base = framework_base / "smali_classes5"

        target = (
            target_base
            / "com"
            / "android"
            / "internal"
            / "util"
            / "kaorios"
        )

        if target.exists():
            shutil.rmtree(target)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target)
        return True
    except Exception as exc:
        print(f"    ❌ Lỗi copy kaorios: {exc}")
        return False


# Exact copy of MEZOBuildRom.py:modify_application_package_manager_kaori (lines 4012-4127)
def modify_application_package_manager_kaori(file_path: Path) -> bool:
    """Modify ApplicationPackageManager.smali - add Kaorios toolbox modifications"""
    try:
        with file_path.open("r", encoding="utf-8", errors="ignore") as handle:
            lines = handle.readlines()

        new_lines = []
        modifications = {
            "field_added": False,
            "constructor_added": False,
            "method1_replaced": False,
            "method2_modified": False,
        }

        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()

            if stripped.startswith(".method") and "hasSystemFeature(Ljava/lang/String;)Z" in stripped and not modifications["method1_replaced"]:
                replacement = [
                    ".method public hasSystemFeature(Ljava/lang/String;)Z\n",
                    "    .registers 3\n",
                    "\n",
                    "    const/4 v0, 0x0\n",
                    "\n",
                    "    invoke-virtual {p0, p1, v0}, Landroid/app/ApplicationPackageManager;->hasSystemFeature(Ljava/lang/String;I)Z\n",
                    "\n",
                    "    move-result p0\n",
                    "\n",
                    "    :try_start_kousei\n",
                    "    invoke-static {p0, p1}, Lcom/android/internal/util/kaorios/KaoriPropsUtils;->KaoriFeatureBlock(ZLjava/lang/String;)Z\n",
                    "\n",
                    "    move-result p0\n",
                    "    :try_end_kaorios\n",
                    "    .catchall {:try_start_kousei .. :try_end_kaorios} :catchall_kaorios\n",
                    "\n",
                    "    :catchall_kaorios\n",
                    "    return p0\n",
                    ".end method\n",
                ]
                new_lines.extend(replacement)
                i += 1
                while i < len(lines) and not lines[i].strip().startswith(".end method"):
                    i += 1
                i += 1
                modifications["method1_replaced"] = True
                continue

            if stripped.startswith(".method") and "hasSystemFeature(Ljava/lang/String;I)Z" in stripped and not modifications["method2_modified"]:
                new_lines.append(line)
                i += 1
                override_code_already_present = False
                while i < len(lines) and not lines[i].strip().startswith(".end method"):
                    current_line = lines[i]
                    current_stripped = current_line.strip()
                    # Kiểm tra xem code override đã được chèn chưa
                    if "KaoriFeatureOverrides;->getOverride" in current_stripped:
                        override_code_already_present = True
                    # Tìm dòng .registers và chèn code ngay sau đó
                    if current_stripped.startswith(".registers") and not override_code_already_present:
                        new_lines.append(current_line)
                        i += 1
                        # Lấy indent từ dòng .registers
                        indent = re.match(r"^(\s*)", current_line)[1]
                        # Chèn code override ngay sau dòng .registers
                        new_lines.append(
                            f"{indent}invoke-static {{}}, Landroid/app/ActivityThread;->currentPackageName()Ljava/lang/String;\n"
                            "\n"
                            f"{indent}move-result-object v0\n"
                            "\n"
                            f"{indent}:try_start_kaori_override\n"
                            f"{indent}iget-object v1, p0, Landroid/app/ApplicationPackageManager;->mContext:Landroid/app/ContextImpl;\n"
                            "\n"
                            f"{indent}invoke-static {{v1, p1, v0}}, Lcom/android/internal/util/kaorios/KaoriFeatureOverrides;->getOverride(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/Boolean;\n"
                            "\n"
                            f"{indent}move-result-object v0\n"
                            f"{indent}:try_end_kaori_override\n"
                            f"{indent}.catchall {{:try_start_kaori_override .. :try_end_kaori_override}} :catchall_kaori_override\n"
                            "\n"
                            f"{indent}goto :goto_kaori_override\n"
                            "\n"
                            f"{indent}:catchall_kaori_override\n"
                            f"{indent}const/4 v0, 0x0\n"
                            "\n"
                            f"{indent}:goto_kaori_override\n"
                            f"{indent}if-eqz v0, :cond_kaori_override\n"
                            "\n"
                            f"{indent}invoke-virtual {{v0}}, Ljava/lang/Boolean;->booleanValue()Z\n"
                            "\n"
                            f"{indent}move-result p0\n"
                            "\n"
                            f"{indent}return p0\n"
                            "\n"
                            f"{indent}:cond_kaori_override\n"
                        )
                        continue
                    new_lines.append(current_line)
                    i += 1
                if i < len(lines):
                    new_lines.append(lines[i])
                    i += 1
                modifications["method2_modified"] = True
                continue

            new_lines.append(line)
            i += 1

        if any(modifications.values()):
            file_path.write_text("".join(new_lines), encoding="utf-8")
            return True
        return False
    except Exception as exc:
        print(f"    ❌ Lỗi sửa {file_path.name}: {exc}")
        return False


# Exact copy of MEZOBuildRom.py:modify_instrumentation_kaori (lines 4130-4184)
def modify_instrumentation_kaori(file_path: Path) -> bool:
    """Modify Instrumentation.smali - add KaoriosProps calls before return-object v0 in newApplication methods"""
    try:
        with file_path.open("r", encoding="utf-8", errors="ignore") as handle:
            lines = handle.readlines()

        new_lines = []
        in_method1 = False
        in_method2 = False
        method1_patched = False
        method2_patched = False

        for line in lines:
            stripped = line.strip()
            # AOSP/MIUI cũ: ".method public static whitelist newApplication(..."
            # A13 mới:     ".method public static newApplication(..."
            if (
                stripped.startswith(".method")
                and "static" in stripped
                and "newApplication(Ljava/lang/Class;Landroid/content/Context;)Landroid/app/Application;" in stripped
            ):
                in_method1 = True
                new_lines.append(line)
                continue
            if (
                stripped.startswith(".method")
                and "newApplication(Ljava/lang/ClassLoader;Ljava/lang/String;Landroid/content/Context;)Landroid/app/Application;" in stripped
            ):
                in_method2 = True
                new_lines.append(line)
                continue
            if in_method1 and stripped == ".end method":
                in_method1 = False
            if in_method2 and stripped == ".end method":
                in_method2 = False

            if in_method1 and stripped.startswith("return-object") and not method1_patched:
                indent = re.match(r"^(\s*)", line)[1]
                new_lines.append(f"{indent}invoke-static {{p1}}, Lcom/android/internal/util/kaorios/KaoriPropsUtils;->KaoriProps(Landroid/content/Context;)V\n")
                method1_patched = True
            if in_method2 and stripped.startswith("return-object") and not method2_patched:
                indent = re.match(r"^(\s*)", line)[1]
                new_lines.append(f"{indent}invoke-static {{p3}}, Lcom/android/internal/util/kaorios/KaoriPropsUtils;->KaoriProps(Landroid/content/Context;)V\n")
                method2_patched = True

            new_lines.append(line)

        if method1_patched or method2_patched:
            file_path.write_text("".join(new_lines), encoding="utf-8")
            return True
        return False
    except Exception as exc:
        print(f"    ❌ Lỗi sửa {file_path.name}: {exc}")
        return False


# Exact copy of MEZOBuildRom.py:modify_keystore2_kaori (lines 4187-4222)
def modify_keystore2_kaori(file_path: Path) -> bool:
    """Modify KeyStore2.smali - add KaoriosKeybox call before return-object v0 in getKeyEntry method"""
    try:
        with file_path.open("r", encoding="utf-8", errors="ignore") as handle:
            lines = handle.readlines()

        new_lines = []
        in_method = False
        patched = False

        for line in lines:
            stripped = line.strip()
            # Tìm method với signature đầy đủ, không phụ thuộc vào modifier (blacklist, whitelist, etc.)
            if stripped.startswith(".method") and "getKeyEntry(Landroid/system/keystore2/KeyDescriptor;)Landroid/system/keystore2/KeyEntryResponse;" in stripped:
                in_method = True
                new_lines.append(line)
                continue
            if in_method and stripped == ".end method":
                in_method = False

            if in_method and stripped == "return-object v0" and not patched:
                indent = re.match(r"^(\s*)", line)[1]
                new_lines.append(f"{indent}invoke-static {{v0}}, Lcom/android/internal/util/kaorios/KaoriKeyboxHooks;->KaoriGetKeyEntry(Landroid/system/keystore2/KeyEntryResponse;)Landroid/system/keystore2/KeyEntryResponse;\n")
                new_lines.append(f"{indent}move-result-object v0\n")
                patched = True

            new_lines.append(line)

        if patched:
            file_path.write_text("".join(new_lines), encoding="utf-8")
            return True
        return False
    except Exception as exc:
        print(f"    ❌ Lỗi sửa {file_path.name}: {exc}")
        return False


# Exact copy of MEZOBuildRom.py:modify_android_keystore_spi_kaori (lines 4225-4277)
def modify_android_keystore_spi_kaori(file_path: Path) -> bool:
    """Modify AndroidKeyStoreSpi.smali - add KaoriosPropsEngineGetCertificateChain call after .registers in engineGetCertificateChain method"""
    try:
        with file_path.open("r", encoding="utf-8", errors="ignore") as handle:
            lines = handle.readlines()

        new_lines = []
        in_method = False
        props_patched = False
        keybox_patched = False

        for line in lines:
            stripped = line.strip()
            # AOSP/MIUI cũ: ".method public whitelist test-api engineGetCertificateChain..."
            # A13 mới:     ".method public engineGetCertificateChain..."
            if stripped.startswith(".method") and "engineGetCertificateChain(Ljava/lang/String;)[Ljava/security/cert/Certificate;" in stripped:
                in_method = True
                new_lines.append(line)
                continue
            if in_method and stripped == ".end method":
                in_method = False

            # Hook 1: gọi KaoriosPropsEngineGetCertificateChain ngay sau khai báo .registers
            if in_method and "registers" in stripped and not props_patched:
                indent = re.match(r"^(\s*)", line)[1]
                new_lines.append(line)
                new_lines.append(f"{indent}invoke-static {{}}, Lcom/android/internal/util/kaorios/KaoriPropsUtils;->KaoriGetCertificateChain()V\n")
                props_patched = True
                continue

            # Hook 2: bọc kết quả certificate chain bằng KaoriosKeybox
            if in_method and "aput-object v2, v3, v4" in stripped and not keybox_patched:
                indent = re.match(r"^(\s*)", line)[1]
                # Ghi lại dòng aput-object trước
                new_lines.append(line)
                # Thêm code hook bên dưới
                new_lines.append(
                    f"{indent}invoke-static {{v3}}, Lcom/android/internal/util/kaorios/KaoriKeyboxHooks;->KaoriGetCertificateChain([Ljava/security/cert/Certificate;)[Ljava/security/cert/Certificate;\n"
                )
                new_lines.append(f"{indent}move-result-object v3\n")
                keybox_patched = True
                continue

            new_lines.append(line)

        if props_patched or keybox_patched:
            file_path.write_text("".join(new_lines), encoding="utf-8")
            return True
        return False
    except Exception as exc:
        print(f"    ❌ Lỗi sửa {file_path.name}: {exc}")
        return False


# Exact copy of MEZOBuildRom.py:kaori_toolbox (lines 4280-4341)
# Path fix: ROOT_DIR -> _LEGACY_ROOT (via copy_kaorios_folder which uses _LEGACY_ROOT)
def kaori_toolbox(work_dir: Path) -> None:
    """Kaori Toolbox - Apply kaorios modifications"""
    print("\n🎨 Mezo mod...")
    operations = 0

    if copy_kaorios_folder(work_dir):
        operations += 1
        print("    ✅ Copy kaorios hoàn tất")

    framework_root = work_dir / "framework_unpacked"

    # Tìm theo tên file thay vì đường dẫn cố định để phù hợp nhiều phiên bản framework
    def find_first_by_name(root: Path, filename: str) -> Path | None:
        if not root.exists():
            return None
        for path in root.rglob(filename):
            if path.is_file():
                return path
        return None

    app_pkg_mgr = find_first_by_name(framework_root, "ApplicationPackageManager.smali")
    if app_pkg_mgr:
        if modify_application_package_manager_kaori(app_pkg_mgr):
            operations += 1
            print(f"    ✅ ApplicationPackageManager patched")
        else:
            print(f"    ℹ️ ApplicationPackageManager không cần/không thể sửa")
    else:
        print("    ⚠️ Không tìm thấy ApplicationPackageManager.smali")

    instrumentation = find_first_by_name(framework_root, "Instrumentation.smali")
    if instrumentation:
        if modify_instrumentation_kaori(instrumentation):
            operations += 1
            print(f"    ✅ Instrumentation patched")
        else:
            print(f"    ℹ️ Instrumentation không cần/không thể sửa")
    else:
        print("    ⚠️ Không tìm thấy Instrumentation.smali")

    keystore2 = find_first_by_name(framework_root, "KeyStore2.smali")
    if keystore2:
        if modify_keystore2_kaori(keystore2):
            operations += 1
            print(f"    ✅ KeyStore2 patched")
        else:
            print(f"    ℹ️ KeyStore2 không cần/không thể sửa")
    else:
        print("    ⚠️ Không tìm thấy KeyStore2.smali")

    android_keystore_spi = find_first_by_name(framework_root, "AndroidKeyStoreSpi.smali")
    if android_keystore_spi:
        if modify_android_keystore_spi_kaori(android_keystore_spi):
            operations += 1
            print(f"    ✅ AndroidKeyStoreSpi patched")
        else:
            print(f"    ℹ️ AndroidKeyStoreSpi không cần/không thể sửa")
    else:
        print("    ⚠️ Không tìm thấy AndroidKeyStoreSpi.smali")

    print(f"\n🎉 Hoàn tất Mezo mod ({operations} thao tác).")


# ── Dry-run helpers ────────────────────────────────────────────────────────────

def _check_target_files(work_dir: Path) -> list[dict]:
    """
    Check expected smali target files for dry-run reporting.
    Uses rglob to mirror kaori_toolbox's find_first_by_name approach.
    """
    framework_root = work_dir / "framework_unpacked"
    services_root  = work_dir / "services_unpacked"

    targets = [
        ("framework_unpacked", "ApplicationPackageManager.smali", framework_root),
        ("framework_unpacked", "Instrumentation.smali",           framework_root),
        ("services_unpacked",  "KeyStore2.smali",                 services_root),
        ("framework_unpacked", "AndroidKeyStoreSpi.smali",        framework_root),
    ]

    results = []
    for folder, filename, root in targets:
        found_path: Path | None = None
        if root.is_dir():
            for p in root.rglob(filename):
                if p.is_file():
                    found_path = p
                    break
        results.append({
            "filename": filename,
            "search_root": folder,
            "found": found_path is not None,
            "path": str(found_path) if found_path else None,
        })
    return results


def _guide_compat_precheck(work_dir: Path) -> list[str]:
    """
    Warn-only precheck: detect if target smali files already contain
    Kaori/custom hooks. Does NOT modify anything.
    Returns a list of warning strings.
    """
    warnings: list[str] = []
    framework_root = work_dir / "framework_unpacked"
    if not framework_root.is_dir():
        return warnings

    check_files = [
        "ApplicationPackageManager.smali",
        "Instrumentation.smali",
        "KeyStore2.smali",
        "AndroidKeyStoreSpi.smali",
    ]

    for filename in check_files:
        for p in framework_root.rglob(filename):
            if not p.is_file():
                continue
            try:
                content = p.read_text(encoding="utf-8", errors="ignore")
                for token in _HOOK_TOKENS:
                    if token in content:
                        warnings.append(
                            f"Existing Kaori/custom hooks detected in {p.name} "
                            f"(token: {token!r}); Kaorios guide recommends checking/"
                            "removing conflicting hooks before patching."
                        )
                        break
            except Exception:
                pass

    # Also check services_unpacked for KeyStore2
    services_root = work_dir / "services_unpacked"
    if services_root.is_dir():
        for p in services_root.rglob("KeyStore2.smali"):
            if not p.is_file():
                continue
            try:
                content = p.read_text(encoding="utf-8", errors="ignore")
                for token in _HOOK_TOKENS:
                    if token in content:
                        warnings.append(
                            f"Existing Kaori/custom hooks detected in {p.name} "
                            f"(services_unpacked, token: {token!r}); Kaorios guide "
                            "recommends checking/removing conflicting hooks before patching."
                        )
                        break
            except Exception:
                pass

    return warnings


# ── Orchestrator ───────────────────────────────────────────────────────────────

def apply_kaori_legacy_patch(
    work_dir: Path,
    flavor: str,
    android_major: int | None = None,
    execute: bool = False,
) -> dict:
    """
    Run (or dry-run) the Kaori Toolbox legacy patch stage.

    Flavor guard: only runs for legend / deadzone_legend / DeadZone_Legend.
    Safe to call from jar_patch.py after jar_misc_legacy and before rebuild/restore.
    """
    norm_flavor = _normalise_flavor(flavor)

    if norm_flavor not in _LEGEND_FLAVORS:
        report = {
            "stage": "kaori_toolbox",
            "flavor": flavor,
            "dry_run": not execute,
            "work_dir": str(work_dir),
            "android_major": android_major,
            "mezo_kaorios_source_exists": False,
            "folders_checked": [],
            "target_files_checked": [],
            "functions_planned": [],
            "functions_executed": [],
            "patched_files": [],
            "skipped_files": [],
            "warnings": [f"Flavor '{flavor}' is not Legend; skipped."],
            "errors": [],
            "status": "SKIPPED_NON_LEGEND",
        }
        return report

    # ── Common checks ─────────────────────────────────────────────────────────
    mezo_kaorios_src = _LEGACY_ROOT / "MEZO" / "kaorios"
    mezo_kaorios_exists = mezo_kaorios_src.is_dir()

    folders_checked: list[dict] = []
    for folder_name in _EXPECTED_FOLDERS:
        folder_path = work_dir / folder_name
        folders_checked.append({
            "folder": folder_name,
            "exists": folder_path.is_dir(),
        })

    target_files = _check_target_files(work_dir)
    compat_warnings = _guide_compat_precheck(work_dir)

    functions_planned = [
        "copy_kaorios_folder",
        "modify_application_package_manager_kaori",
        "modify_instrumentation_kaori",
        "modify_keystore2_kaori",
        "modify_android_keystore_spi_kaori",
    ]

    warnings: list[str] = []
    errors: list[str] = []

    if not mezo_kaorios_exists:
        warnings.append(
            f"MEZO/kaorios source folder not found at: {mezo_kaorios_src}; "
            "copy_kaorios_folder will fail at execute time."
        )

    warnings.extend(compat_warnings)

    # ── Dry-run ───────────────────────────────────────────────────────────────
    if not execute:
        report = {
            "stage": "kaori_toolbox",
            "flavor": flavor,
            "dry_run": True,
            "work_dir": str(work_dir),
            "android_major": android_major,
            "mezo_kaorios_source_exists": mezo_kaorios_exists,
            "folders_checked": folders_checked,
            "target_files_checked": target_files,
            "functions_planned": functions_planned,
            "functions_executed": [],
            "patched_files": [],
            "skipped_files": [],
            "warnings": warnings,
            "errors": errors,
            "status": "DRY_RUN",
        }
        return report

    # ── Execute ───────────────────────────────────────────────────────────────
    functions_executed: list[str] = []
    patched_files: list[str] = []
    skipped_files: list[dict] = []

    try:
        kaori_toolbox(work_dir)
        functions_executed.append("kaori_toolbox")

        # Collect patched/skipped file info for the report
        framework_root = work_dir / "framework_unpacked"

        def _find_first(root: Path, name: str) -> Path | None:
            if not root.is_dir():
                return None
            for p in root.rglob(name):
                if p.is_file():
                    return p
            return None

        for fname in [
            "ApplicationPackageManager.smali",
            "Instrumentation.smali",
            "KeyStore2.smali",
            "AndroidKeyStoreSpi.smali",
        ]:
            p = _find_first(framework_root, fname)
            if p:
                patched_files.append(str(p))
            else:
                skipped_files.append({"file": fname, "reason": "not found in framework_unpacked"})

    except Exception as exc:
        errors.append(f"kaori_toolbox: {exc}")

    status = "FAILED" if errors else "APPLIED"

    report = {
        "stage": "kaori_toolbox",
        "flavor": flavor,
        "dry_run": False,
        "work_dir": str(work_dir),
        "android_major": android_major,
        "mezo_kaorios_source_exists": mezo_kaorios_exists,
        "folders_checked": folders_checked,
        "target_files_checked": target_files,
        "functions_planned": functions_planned,
        "functions_executed": functions_executed,
        "patched_files": patched_files,
        "skipped_files": skipped_files,
        "warnings": warnings,
        "errors": errors,
        "status": status,
    }
    return report


# ── Report writer ──────────────────────────────────────────────────────────────

def _format_text_report(report: dict) -> str:
    mode = "DRY RUN" if report.get("dry_run") else "EXECUTE"
    lines: list[str] = [
        f"DeadZone Legend Kaori Legacy Report  [{mode}]",
        "=" * 60,
        f"Status:          {report.get('status', '?')}",
        f"Stage:           {report.get('stage', 'kaori_toolbox')}",
        f"Flavor:          {report.get('flavor', '?')}",
        f"Work dir:        {report.get('work_dir', '?')}",
        f"Android major:   {report.get('android_major') if report.get('android_major') is not None else '(unknown)'}",
        f"Dry run:         {report.get('dry_run', True)}",
        f"MEZO/kaorios source exists: {report.get('mezo_kaorios_source_exists', False)}",
        "",
        "Folders checked:",
    ]
    for fc in report.get("folders_checked", []):
        mark = "OK" if fc.get("exists") else "MISSING"
        lines.append(f"  [{mark}] {fc.get('folder')}")

    lines.append("")
    lines.append("Target files checked:")
    for tf in report.get("target_files_checked", []):
        mark = "FOUND" if tf.get("found") else "MISSING"
        path_info = f"  -> {tf.get('path')}" if tf.get("path") else ""
        lines.append(f"  [{mark}] {tf.get('filename')}  (in {tf.get('search_root')}){path_info}")

    lines.append("")
    lines.append("Functions planned:")
    for fn in report.get("functions_planned", []):
        lines.append(f"  - {fn}")

    lines.append("")
    lines.append("Functions executed:")
    executed = report.get("functions_executed", [])
    if executed:
        for fn in executed:
            lines.append(f"  + {fn}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Patched files:")
    patched = report.get("patched_files", [])
    if patched:
        for pf in patched:
            lines.append(f"  OK  {pf}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Skipped files:")
    skipped = report.get("skipped_files", [])
    if skipped:
        for sf in skipped:
            lines.append(f"  --  {sf.get('file')}  ({sf.get('reason')})")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Warnings:")
    warnings = report.get("warnings", [])
    if warnings:
        for w in warnings:
            lines.append(f"  ! {w}")
    else:
        lines.append("  (none)")

    lines.append("")
    lines.append("Errors:")
    errors = report.get("errors", [])
    if errors:
        for e in errors:
            lines.append(f"  X {e}")
    else:
        lines.append("  (none)")

    lines.append("")
    return "\n".join(lines)


def _write_reports(report: dict) -> None:
    _REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    json_path = _REPORTS_DIR / _REPORT_JSON
    txt_path  = _REPORTS_DIR / _REPORT_TXT

    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    txt_path.write_text(_format_text_report(report), encoding="utf-8")

    print(f"[kaori_legacy] JSON: {json_path}")
    print(f"[kaori_legacy] TXT : {txt_path}")


# ── CLI ────────────────────────────────────────────────────────────────────────

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Legend Kaori Toolbox legacy patch stage (DeadZone factory)",
    )
    p.add_argument("--work-dir", dest="work_dir", required=True,
                   help="Path to JAR work directory (contains framework_unpacked, services_unpacked)")
    p.add_argument("--flavor", required=True,
                   help="ROM flavor (e.g. legend, deadzone_legend)")
    p.add_argument("--android-major", dest="android_major", type=int, default=None,
                   help="Android major version (e.g. 14, 15, 16)")
    p.add_argument("--execute", action="store_true",
                   help="Apply patches (default is dry-run)")
    return p


def _main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    work_dir = Path(args.work_dir).resolve()
    if not work_dir.is_dir():
        print(f"[kaori_legacy] ERROR: work directory not found: {work_dir}", file=sys.stderr)
        return 2

    mode = "EXECUTE" if args.execute else "DRY-RUN"
    print(f"[kaori_legacy] mode={mode}  flavor={args.flavor}  android={args.android_major}  work={work_dir}")

    report = apply_kaori_legacy_patch(
        work_dir=work_dir,
        flavor=args.flavor,
        android_major=args.android_major,
        execute=args.execute,
    )

    _write_reports(report)

    print(f"[kaori_legacy] status={report['status']}")
    if report["warnings"]:
        for w in report["warnings"]:
            print(f"[kaori_legacy] WARNING: {w}")
    if report["errors"]:
        for e in report["errors"]:
            print(f"[kaori_legacy] ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(_main())
