"""
Legend-only legacy JAR misc patches.

Carries exact behavior of MEZOBuildRom.py functions:
  - fix_specific_smali_file(smali_file)       lines 2009-2085 (helper)
  - fix_bootloop_a15(work_dir)                lines 2088-2149
  - tricky_wukong_a15(work_dir)               lines 4344-4558
  - tricky_wukong_a16(work_dir)               lines 4561-4758
  - enhanced_keyboard(work_dir)               lines 4761-4861
  - enable_floating_window_all_app(work_dir)  lines 4864-4955
  - increase_number_of_floating_windows(work_dir) lines 4958-5019
  - fix_theme_reset(work_dir)                 lines 5135-5187

Flavor guard: only runs for legend / deadzone_legend / DeadZone_Legend.
All other flavors exit with status SKIPPED_NON_LEGEND.

Execute order (when execute=True):
  if android_major == 15:
      fix_bootloop_a15(work_dir)
  if android_major in (14, 15):
      tricky_wukong_a15(work_dir)
  elif android_major == 16:
      tricky_wukong_a16(work_dir)
  enhanced_keyboard(work_dir)
  enable_floating_window_all_app(work_dir)
  increase_number_of_floating_windows(work_dir)
  fix_theme_reset(work_dir)

IMPORTANT: This module does NOT rebuild jars. It assumes jars are already
unpacked into framework_unpacked / services_unpacked / miui_services_unpacked.

Allowed changes from source:
  - log() -> print()  (log was just print in MEZOBuildRom.py)
  - ROOT_DIR -> _LEGACY_ROOT (module-path fix for WukongFrameworkBridge.smali)
  - imports added
  - report wrapper

Not changed:
  - logic, strings, regex, smali paths, conditions, inserted snippets, algorithm

CLI:
  # dry-run:
  python -m factory.patch.mods.legend.jar_misc_legacy \\
      --work-dir "path/to/jar_work_dir" \\
      --flavor legend \\
      --android-major 16

  # execute:
  python -m factory.patch.mods.legend.jar_misc_legacy \\
      --work-dir "path/to/jar_work_dir" \\
      --flavor legend \\
      --android-major 16 \\
      --execute
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

# _LEGACY_ROOT = third_party/mezo_core (where MEZO/WukongFrameworkBridge.smali lives)
_LEGACY_ROOT = Path(__file__).resolve().parents[3] / "third_party" / "mezo_core"

_REPO_ROOT   = Path(__file__).resolve().parents[3]
_OUTPUT_ROOT = _REPO_ROOT / "output"
_REPORTS_DIR = _OUTPUT_ROOT / "reports"

_LEGEND_FLAVORS = {"legend", "deadzone_legend"}

_EXPECTED_FOLDERS = [
    "framework_unpacked",
    "services_unpacked",
    "miui_services_unpacked",
]

_REPORT_JSON = "05_legend_jar_misc_legacy_report.json"
_REPORT_TXT  = "05_legend_jar_misc_legacy_report.txt"


def _normalise_flavor(flavor: str) -> str:
    return flavor.lower().replace("-", "_")


# ── helper ────────────────────────────────────────────────────────────────────
# Exact copy of MEZOBuildRom.py:fix_specific_smali_file (lines 2009-2085)
def fix_specific_smali_file(smali_file: Path) -> bool:
    """Fix a specific smali file by replacing methods containing invoke-custom"""
    try:
        with smali_file.open('r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        new_lines = []
        in_method = False
        method_lines = []
        clear_this_method = False
        method_name = None
        file_modified = False

        for line in lines:
            if line.strip().startswith('.method'):
                in_method = True
                method_lines = [line]
                clear_this_method = False
                # Lấy tên method
                parts = line.strip().split()
                if len(parts) > 1:
                    method_name = parts[-1]
                else:
                    method_name = None
            elif in_method and 'invoke-custom' in line:
                clear_this_method = True
                method_lines.append(line)
            elif in_method and line.strip().startswith('.end method'):
                if clear_this_method and method_name:
                    file_modified = True
                    if 'equals' in method_name:
                        new_lines.append(method_lines[0])
                        new_lines.append('    .registers 2\n')
                        new_lines.append('    const/4 v0, 0x0\n')
                        new_lines.append('    return v0\n')
                        new_lines.append('.end method\n')
                    elif 'hashCode' in method_name:
                        new_lines.append(method_lines[0])
                        new_lines.append('    .registers 1\n')
                        new_lines.append('    const/4 v0, 0x0\n')
                        new_lines.append('    return v0\n')
                        new_lines.append('.end method\n')
                    elif 'toString' in method_name:
                        new_lines.append(method_lines[0])
                        new_lines.append('    .registers 1\n')
                        new_lines.append('    const/4 v0, 0x0\n')
                        new_lines.append('    return-object v0\n')
                        new_lines.append('.end method\n')
                    else:
                        new_lines.extend(method_lines)
                        new_lines.append(line)
                else:
                    new_lines.extend(method_lines)
                    new_lines.append(line)

                # Reset method state
                in_method = False
                method_lines = []
                clear_this_method = False
                method_name = None
            elif in_method:
                method_lines.append(line)
            else:
                new_lines.append(line)

        # Write back to file if modified
        if file_modified:
            with smali_file.open('w', encoding='utf-8') as f:
                f.writelines(new_lines)
            return True

        return False

    except Exception as e:
        print(f"    ❌ Loi khi xu ly {smali_file.name}: {e}")
        return False


# ── legacy patch functions ─────────────────────────────────────────────────────
# Exact copy of MEZOBuildRom.py:fix_bootloop_a15 (lines 2088-2149)
def fix_bootloop_a15(work_dir: Path) -> None:
    """Fix bootloop for A15 devices by handling invoke-custom methods in specific files"""
    print("\n🔧 Processing bootloop fix (a15)...")
    print("📝 Tim kiem va sua cac method chua 'invoke-custom' trong cac file cu the...")

    # Define target files to fix
    target_files = {
        "framework_unpacked/smali_classes2": [
            "android/hardware/input/KeyboardLayoutPreviewDrawable$GlyphDrawable.smali",
            "android/hardware/input/PhysicalKeyLayout$EnterKey.smali",
            "android/hardware/input/PhysicalKeyLayout$LayoutKey.smali",
            "android/media/MediaRouter2$InstanceInvalidatedCallbackRecord.smali",
            "android/media/MediaRouter2$PackageNameUserHandlePair.smali"
        ],
        "services_unpacked/smali_classes": [
            "com/android/server/BinaryTransparencyService$Digest.smali"
        ],
        "services_unpacked/smali_classes2": [
            "com/android/server/inputmethod/AdditionalSubtypeMapRepository$WriteTask.smali",
            "com/android/server/policy/PhoneWindowManager$SwitchKeyboardLayoutMessageObject.smali",
            "com/android/server/policy/SingleKeyGestureDetector$MessageObject.smali"
        ],
        "miui_services_unpacked/smali_classes": [
            "com/android/server/am/BroadcastQueueModernStubImpl$ActionCount.smali",
            "com/android/server/input/InputDfsReportStubImpl$MessageObject.smali",
            "com/android/server/input/InputOneTrackUtil$TrackEventListData.smali",
            "com/android/server/input/InputOneTrackUtil$TrackEventStringData.smali",
            "com/android/server/policy/MiuiScreenOnProximityLock$AcquireMessageObject.smali",
            "com/android/server/policy/MiuiScreenOnProximityLock$ReleaseMessageObject.smali"
        ]
    }

    total_files_processed = 0

    # Process each directory and its target files
    for directory, files in target_files.items():
        dir_path = work_dir / directory
        if not dir_path.exists():
            print(f"❌ Thu muc {directory} khong ton tai")
            continue

        print(f"\n📁 Processing directory: {directory}")
        print(f"📄 Tim thay {len(files)} file can xu ly")

        for file_path in files:
            # Convert forward slashes to proper path separators for the current OS
            file_path_parts = file_path.split('/')
            full_file_path = dir_path.joinpath(*file_path_parts)

            if not full_file_path.exists():
                print(f"  ⚠️  File {file_path} khong ton tai tai: {full_file_path}")
                continue

            print(f"  🔍 Processing: {file_path}")
            if fix_specific_smali_file(full_file_path):
                total_files_processed += 1
                print(f"    ✅ Da sua thanh cong")
            else:
                print(f"    ℹ️  Khong co method nao can sua")

    print(f"\n🎉 Bootloop fix complete!")
    print(f"📊 Tong so file da xu ly: {total_files_processed}")


# Exact copy of MEZOBuildRom.py:tricky_wukong_a15 (lines 4344-4558)
# Path fix: ROOT_DIR -> _LEGACY_ROOT
def tricky_wukong_a15(work_dir: Path) -> None:
    """Apply Wukong hooks to framework KeyStore2 and copy bridge smali for Android 15."""
    print("\n🐒 Processing Tricky Wukong...")

    bridge_src = _LEGACY_ROOT / "MEZO" / "WukongFrameworkBridge.smali"
    bridge_dst_dir = work_dir / "framework_unpacked" / "smali_classes5" / "android" / "security"
    bridge_dst = bridge_dst_dir / "WukongFrameworkBridge.smali"

    if not bridge_src.is_file():
        print(f"    ⚠️ Khong tim thay file nguon: {bridge_src}")
    else:
        try:
            bridge_dst_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(bridge_src, bridge_dst)
            print(f"    ✅ Da copy WukongFrameworkBridge.smali -> {bridge_dst}")
        except Exception as exc:
            print(f"    ❌ Loi khi copy WukongFrameworkBridge.smali: {exc}")

    keystore2_path = (
        work_dir
        / "framework_unpacked"
        / "smali_classes3"
        / "android"
        / "security"
        / "KeyStore2.smali"
    )
    if not keystore2_path.is_file():
        print(f"    ⚠️ Khong tim thay file: {keystore2_path}")
        return

    try:
        content = keystore2_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        print(f"    ❌ Loi khi doc KeyStore2.smali: {exc}")
        return

    def patch_method_block(
        text: str,
        method_signature: str,
        anchor: str,
        snippet: str,
        insert_after_anchor: bool = True,
    ) -> tuple[str, bool]:
        method_start = text.find(method_signature)
        if method_start < 0:
            return text, False

        method_end = text.find(".end method", method_start)
        if method_end < 0:
            return text, False
        method_end += len(".end method")

        method_block = text[method_start:method_end]
        if snippet.strip() in method_block:
            return text, False

        anchor_idx = method_block.find(anchor)
        if anchor_idx < 0:
            return text, False

        if insert_after_anchor:
            insert_pos = anchor_idx + len(anchor)
        else:
            insert_pos = anchor_idx

        updated_method = (
            method_block[:insert_pos] + "\n" + snippet + method_block[insert_pos:]
        )
        updated_text = text[:method_start] + updated_method + text[method_end:]
        return updated_text, True

    changed = False

    delete_sig = ".method public blacklist deleteKey(Landroid/system/keystore2/KeyDescriptor;)V"
    delete_anchor = "invoke-static {}, Landroid/os/StrictMode;->noteDiskWrite()V"
    delete_snippet = (
        "    invoke-static {p1}, "
        "Landroid/security/WukongFrameworkBridge;->deleteKey(Landroid/system/keystore2/KeyDescriptor;)V"
    )
    content, patched_delete = patch_method_block(
        content, delete_sig, delete_anchor, delete_snippet, insert_after_anchor=True
    )
    changed = changed or patched_delete

    get_sig = (
        ".method public blacklist "
        "getKeyEntry(Landroid/system/keystore2/KeyDescriptor;)Landroid/system/keystore2/KeyEntryResponse;"
    )
    get_anchor_read = "invoke-static {}, Landroid/os/StrictMode;->noteDiskRead()V"
    get_pre_snippet = (
        "    invoke-static {p1}, "
        "Landroid/security/WukongFrameworkBridge;->preGetKeyEntry(Landroid/system/keystore2/KeyDescriptor;)Landroid/system/keystore2/KeyEntryResponse;\n\n"
        "    move-result-object v0\n\n"
        "    if-nez v0, :cond_1c"
    )
    content, patched_pre = patch_method_block(
        content, get_sig, get_anchor_read, get_pre_snippet, insert_after_anchor=True
    )
    changed = changed or patched_pre

    get_anchor_return = "return-object v0"
    get_post_snippet = (
        "    invoke-static {p1, v0}, "
        "Landroid/security/WukongFrameworkBridge;->postGetKeyEntry(Landroid/system/keystore2/KeyDescriptor;Landroid/system/keystore2/KeyEntryResponse;)Landroid/system/keystore2/KeyEntryResponse;\n\n"
        "    move-result-object v0\n\n"
        "    :cond_1c\n"
    )
    content, patched_post = patch_method_block(
        content, get_sig, get_anchor_return, get_post_snippet, insert_after_anchor=False
    )
    changed = changed or patched_post

    try:
        if changed:
            keystore2_path.write_text(content, encoding="utf-8")
            print("    ✅ Da patch KeyStore2.smali voi tricky_wukong")
        else:
            print("    ℹ️ KeyStore2.smali khong can/khong the patch them")
    except Exception as exc:
        print(f"    ❌ Loi khi ghi KeyStore2.smali: {exc}")

    keypair_spi_path = (
        work_dir
        / "framework_unpacked"
        / "smali_classes3"
        / "android"
        / "security"
        / "keystore2"
        / "AndroidKeyStoreKeyPairGeneratorSpi.smali"
    )
    if not keypair_spi_path.is_file():
        print(f"    ⚠️ Khong tim thay file: {keypair_spi_path}")
        return

    try:
        keypair_content = keypair_spi_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        print(f"    ❌ Loi khi doc AndroidKeyStoreKeyPairGeneratorSpi.smali: {exc}")
        return

    keypair_changed = False

    old_if_line_1 = "if-eq v12, v13, :cond_89"
    new_if_block_1 = "const/4 v14, 0x7\n\n    if-eq v12, v14, :cond_89"
    if old_if_line_1 in keypair_content and new_if_block_1 not in keypair_content:
        keypair_content = keypair_content.replace(old_if_line_1, new_if_block_1, 1)
        keypair_changed = True

    old_if_line_2 = "if-eq v8, v13, :cond_d1"
    new_if_block_2 = "const/4 v14, 0x7\n\n    if-eq v8, v14, :cond_d1"
    if old_if_line_2 in keypair_content and new_if_block_2 not in keypair_content:
        keypair_content = keypair_content.replace(old_if_line_2, new_if_block_2, 1)
        keypair_changed = True

    generate_sig = ".method public whitelist test-api generateKeyPair()Ljava/security/KeyPair;"
    generate_start = keypair_content.find(generate_sig)
    if generate_start >= 0:
        generate_end = keypair_content.find(".end method", generate_start)
        if generate_end > generate_start:
            generate_end += len(".end method")
            generate_block = keypair_content[generate_start:generate_end]

            registers_idx = generate_block.find(".registers ")
            if registers_idx >= 0:
                registers_end = generate_block.find("\n", registers_idx)
                current_registers = generate_block[registers_idx:registers_end]
                if current_registers != ".registers 16":
                    generate_block = generate_block.replace(current_registers, ".registers 16", 1)
                    keypair_changed = True

            pre_anchor = "move-object v12, v4"
            pre_snippet = (
                "    move v13, v2\n\n"
                "    invoke-static/range {v8 .. v13}, "
                "Landroid/security/WukongFrameworkBridge;->maybeGenerateKey(Landroid/system/keystore2/KeyDescriptor;Landroid/system/keystore2/KeyDescriptor;Ljava/util/Collection;I[BI)Landroid/system/keystore2/KeyMetadata;\n\n"
                "    move-result-object v14\n\n"
                "    if-nez v14, :cond_wukong_generated\n"
            )
            if pre_snippet not in generate_block:
                pre_idx = generate_block.find(pre_anchor)
                if pre_idx >= 0:
                    insert_after = pre_idx + len(pre_anchor)
                    generate_block = (
                        generate_block[:insert_after] + "\n" + pre_snippet + generate_block[insert_after:]
                    )
                    keypair_changed = True

            post_anchor = "move-result-object v7"
            post_snippet = (
                "    goto :cond_wukong_end\n\n"
                "    :cond_wukong_generated\n"
                "    move-object v7, v14\n\n"
                "    :cond_wukong_end\n"
            )
            if post_snippet not in generate_block:
                post_idx = generate_block.find(post_anchor)
                if post_idx >= 0:
                    insert_after = post_idx + len(post_anchor)
                    generate_block = (
                        generate_block[:insert_after] + "\n" + post_snippet + generate_block[insert_after:]
                    )
                    keypair_changed = True

            keypair_content = (
                keypair_content[:generate_start] + generate_block + keypair_content[generate_end:]
            )

    try:
        if keypair_changed:
            keypair_spi_path.write_text(keypair_content, encoding="utf-8")
            print("    ✅ Da patch AndroidKeyStoreKeyPairGeneratorSpi.smali")
        else:
            print("    ℹ️ AndroidKeyStoreKeyPairGeneratorSpi.smali khong can/khong the patch them")
    except Exception as exc:
        print(f"    ❌ Loi khi ghi AndroidKeyStoreKeyPairGeneratorSpi.smali: {exc}")


# Exact copy of MEZOBuildRom.py:tricky_wukong_a16 (lines 4561-4758)
# Path fix: ROOT_DIR -> _LEGACY_ROOT
def tricky_wukong_a16(work_dir: Path) -> None:
    """Apply Wukong hooks to framework KeyStore2 and copy bridge smali."""
    print("\n🐒 Processing Tricky Wukong...")

    bridge_src = _LEGACY_ROOT / "MEZO" / "WukongFrameworkBridge.smali"
    bridge_dst_dir = work_dir / "framework_unpacked" / "smali_classes6" / "android" / "security"
    bridge_dst = bridge_dst_dir / "WukongFrameworkBridge.smali"

    if not bridge_src.is_file():
        print(f"    ⚠️ Khong tim thay file nguon: {bridge_src}")
    else:
        try:
            bridge_dst_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(bridge_src, bridge_dst)
            print(f"    ✅ Da copy WukongFrameworkBridge.smali -> {bridge_dst}")
        except Exception as exc:
            print(f"    ❌ Loi khi copy WukongFrameworkBridge.smali: {exc}")

    keystore2_path = (
        work_dir
        / "framework_unpacked"
        / "smali_classes3"
        / "android"
        / "security"
        / "KeyStore2.smali"
    )
    if not keystore2_path.is_file():
        print(f"    ⚠️ Khong tim thay file: {keystore2_path}")
        return

    try:
        content = keystore2_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        print(f"    ❌ Loi khi doc KeyStore2.smali: {exc}")
        return

    def patch_method_block(
        text: str,
        method_signature: str,
        anchor: str,
        snippet: str,
        insert_after_anchor: bool = True,
    ) -> tuple[str, bool]:
        method_start = text.find(method_signature)
        if method_start < 0:
            return text, False

        method_end = text.find(".end method", method_start)
        if method_end < 0:
            return text, False
        method_end += len(".end method")

        method_block = text[method_start:method_end]
        if snippet.strip() in method_block:
            return text, False

        anchor_idx = method_block.find(anchor)
        if anchor_idx < 0:
            return text, False

        if insert_after_anchor:
            insert_pos = anchor_idx + len(anchor)
        else:
            insert_pos = anchor_idx

        updated_method = (
            method_block[:insert_pos] + "\n" + snippet + method_block[insert_pos:]
        )
        updated_text = text[:method_start] + updated_method + text[method_end:]
        return updated_text, True

    changed = False

    # 1) deleteKey: chen hook ngay duoi noteDiskWrite()
    delete_sig = ".method public blacklist deleteKey(Landroid/system/keystore2/KeyDescriptor;)V"
    delete_anchor = "invoke-static {}, Landroid/os/StrictMode;->noteDiskWrite()V"
    delete_snippet = (
        "    invoke-static {p1}, "
        "Landroid/security/WukongFrameworkBridge;->deleteKey(Landroid/system/keystore2/KeyDescriptor;)V"
    )
    content, patched_delete = patch_method_block(
        content, delete_sig, delete_anchor, delete_snippet, insert_after_anchor=True
    )
    changed = changed or patched_delete

    # 2) getKeyEntry: chen preGet ngay duoi noteDiskRead()
    get_sig = (
        ".method public blacklist "
        "getKeyEntry(Landroid/system/keystore2/KeyDescriptor;)Landroid/system/keystore2/KeyEntryResponse;"
    )
    get_anchor_read = "invoke-static {}, Landroid/os/StrictMode;->noteDiskRead()V"
    get_pre_snippet = (
        "    invoke-static {p1}, "
        "Landroid/security/WukongFrameworkBridge;->preGetKeyEntry(Landroid/system/keystore2/KeyDescriptor;)Landroid/system/keystore2/KeyEntryResponse;\n\n"
        "    move-result-object v0\n\n"
        "    if-nez v0, :cond_1c"
    )
    content, patched_pre = patch_method_block(
        content, get_sig, get_anchor_read, get_pre_snippet, insert_after_anchor=True
    )
    changed = changed or patched_pre

    # 3) getKeyEntry: chen postGet ngay tren return-object v0
    get_anchor_return = "return-object v0"
    get_post_snippet = (
        "    invoke-static {p1, v0}, "
        "Landroid/security/WukongFrameworkBridge;->postGetKeyEntry(Landroid/system/keystore2/KeyDescriptor;Landroid/system/keystore2/KeyEntryResponse;)Landroid/system/keystore2/KeyEntryResponse;\n\n"
        "    move-result-object v0\n\n"
        "    :cond_1c\n"
    )
    content, patched_post = patch_method_block(
        content, get_sig, get_anchor_return, get_post_snippet, insert_after_anchor=False
    )
    changed = changed or patched_post

    try:
        if changed:
            keystore2_path.write_text(content, encoding="utf-8")
            print("    ✅ Da patch KeyStore2.smali voi tricky_wukong")
        else:
            print("    ℹ️ KeyStore2.smali khong can/khong the patch them")
    except Exception as exc:
        print(f"    ❌ Loi khi ghi KeyStore2.smali: {exc}")

    keypair_spi_path = (
        work_dir
        / "framework_unpacked"
        / "smali_classes3"
        / "android"
        / "security"
        / "keystore2"
        / "AndroidKeyStoreKeyPairGeneratorSpi.smali"
    )
    if not keypair_spi_path.is_file():
        print(f"    ⚠️ Khong tim thay file: {keypair_spi_path}")
        return

    try:
        keypair_content = keypair_spi_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        print(f"    ❌ Loi khi doc AndroidKeyStoreKeyPairGeneratorSpi.smali: {exc}")
        return

    keypair_changed = False

    old_if_line = "if-eq v10, v13, :cond_87"
    new_if_block = "const/4 v11, 0x7\n\n    if-eq v10, v11, :cond_87"
    if old_if_line in keypair_content and new_if_block not in keypair_content:
        keypair_content = keypair_content.replace(old_if_line, new_if_block, 1)
        keypair_changed = True

    generate_sig = ".method public whitelist test-api generateKeyPair()Ljava/security/KeyPair;"
    generate_start = keypair_content.find(generate_sig)
    if generate_start >= 0:
        generate_end = keypair_content.find(".end method", generate_start)
        if generate_end > generate_start:
            generate_end += len(".end method")
            generate_block = keypair_content[generate_start:generate_end]

            pre_anchor = "move-result-object v10"
            pre_snippet = (
                "    \n\nmove v13, v5\n\n"
                "    invoke-static/range {v8 .. v13}, "
                "Landroid/security/WukongFrameworkBridge;->maybeGenerateKey(Landroid/system/keystore2/KeyDescriptor;Landroid/system/keystore2/KeyDescriptor;Ljava/util/Collection;I[BI)Landroid/system/keystore2/KeyMetadata;\n\n"
                "    move-result-object v0\n\n"
                "    if-nez v0, :cond_6a"
            )
            if pre_snippet not in generate_block:
                pre_idx = generate_block.find(pre_anchor)
                if pre_idx >= 0:
                    insert_after = pre_idx + len(pre_anchor)
                    generate_block = (
                        generate_block[:insert_after] + "\n" + pre_snippet + generate_block[insert_after:]
                    )
                    keypair_changed = True

            post_anchor = "move-object v4, v0"
            post_label_line = "    :cond_6a"
            if post_label_line not in generate_block:
                post_idx = generate_block.find(post_anchor)
                if post_idx >= 0:
                    generate_block = (
                        generate_block[:post_idx] + f"{post_label_line}\n" + generate_block[post_idx:]
                    )
                    keypair_changed = True

            keypair_content = (
                keypair_content[:generate_start] + generate_block + keypair_content[generate_end:]
            )

    try:
        if keypair_changed:
            keypair_spi_path.write_text(keypair_content, encoding="utf-8")
            print("    ✅ Da patch AndroidKeyStoreKeyPairGeneratorSpi.smali")
        else:
            print("    ℹ️ AndroidKeyStoreKeyPairGeneratorSpi.smali khong can/khong the patch them")
    except Exception as exc:
        print(f"    ❌ Loi khi ghi AndroidKeyStoreKeyPairGeneratorSpi.smali: {exc}")


# Exact copy of MEZOBuildRom.py:enhanced_keyboard (lines 4761-4861)
def enhanced_keyboard(work_dir: Path) -> None:
    """Enhanced Keyboard - Replace Baidu input method with Google Keyboard"""
    print("\n⌨️ Processing Enhanced Keyboard...")
    print("📝 Tim kiem va thay the com.baidu.input_mi thanh com.google.android.inputmethod.latin...")

    # Tim theo ten file thay vi duong dan co dinh
    def find_first_by_name(root: Path, filename: str) -> Path | None:
        if not root.exists():
            return None
        for path in root.rglob(filename):
            if path.is_file():
                return path
        return None

    old_string = "com.baidu.input_mi"
    new_string = "com.google.android.inputmethod.latin"

    total_files_processed = 0
    total_replacements = 0

    # Xu ly miui_services_unpacked
    print("\n📁 Xu ly miui_services_unpacked...")
    miui_services_root = work_dir / "miui_services_unpacked"
    if miui_services_root.exists():
        target_files_services = [
            "DevicePolicyManagerServiceStubImpl.smali",
            "InputManagerServiceStubImpl.smali",
            "InputMethodManagerServiceImpl.smali",
            "ActivityTaskSupervisorImpl.smali",
            "MiuiSplitInputMethodImpl.smali"
        ]

        for filename in target_files_services:
            file_path = find_first_by_name(miui_services_root, filename)
            if file_path:
                print(f"\n  🔍 Processing: {filename}")
                try:
                    # Doc noi dung file
                    content = file_path.read_text(encoding='utf-8', errors='ignore')

                    # Dem so lan xuat hien
                    count = content.count(old_string)

                    if count > 0:
                        # Thay the
                        new_content = content.replace(old_string, new_string)
                        file_path.write_text(new_content, encoding='utf-8')
                        total_files_processed += 1
                        total_replacements += count
                        print(f"    ✅ Da thay the {count} lan trong {filename}")
                    else:
                        print(f"    ℹ️ Khong tim thay '{old_string}' trong {filename}")
                except Exception as e:
                    print(f"    ❌ Loi khi xu ly {filename}: {e}")
            else:
                print(f"  ⚠️ Khong tim thay {filename}")
    else:
        print("  ⚠️ miui_services_unpacked directory not found")

    # Xu ly miui_framework_unpacked
    print("\n📁 Xu ly miui_framework_unpacked...")
    miui_framework_root = work_dir / "miui_framework_unpacked"
    if miui_framework_root.exists():
        target_files_framework = [
            "InputMethodServiceInjector.smali",
            "DisplayInfoInjector$2.smali",
            "InputMethodManagerStubImpl.smali",
            "AnrEnhanceImpl.smali",
            "HapticFeedbackUtil.smali"
        ]

        for filename in target_files_framework:
            file_path = find_first_by_name(miui_framework_root, filename)
            if file_path:
                print(f"\n  🔍 Processing: {filename}")
                try:
                    # Doc noi dung file
                    content = file_path.read_text(encoding='utf-8', errors='ignore')

                    # Dem so lan xuat hien
                    count = content.count(old_string)

                    if count > 0:
                        # Thay the
                        new_content = content.replace(old_string, new_string)
                        file_path.write_text(new_content, encoding='utf-8')
                        total_files_processed += 1
                        total_replacements += count
                        print(f"    ✅ Da thay the {count} lan trong {filename}")
                    else:
                        print(f"    ℹ️ Khong tim thay '{old_string}' trong {filename}")
                except Exception as e:
                    print(f"    ❌ Loi khi xu ly {filename}: {e}")
            else:
                print(f"  ⚠️ Khong tim thay {filename}")
    else:
        print("  ⚠️ miui_framework_unpacked directory not found")

    print(f"\n🎉 Enhanced Keyboard complete!")
    print(f"📊 Tong so file da xu ly: {total_files_processed}")
    print(f"📊 Tong so lan thay the: {total_replacements}")


# Exact copy of MEZOBuildRom.py:enable_floating_window_all_app (lines 4864-4955)
def enable_floating_window_all_app(work_dir: Path) -> None:
    """Enable floating window for all apps by modifying MiuiMultiWindowAdapter.smali"""
    print("\n🪟 Processing Enable Floating Window All App...")
    print("📝 Chinh sua file MiuiMultiWindowAdapter.smali...")

    # Path to MiuiMultiWindowAdapter.smali
    miui_multi_window_path = work_dir / "miui_framework_unpacked" / "smali_classes" / "android" / "util" / "MiuiMultiWindowAdapter.smali"

    if not miui_multi_window_path.exists():
        print(f"❌ MiuiMultiWindowAdapter.smali not found at: {miui_multi_window_path}")
        print("⚠️  Make sure miui-framework.jar has been extracted first")
        return

    print(f"📁 Processing: {miui_multi_window_path}")

    try:
        with miui_multi_window_path.open('r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        new_lines = []
        file_modified = False

        i = 0
        total_lines = len(lines)
        while i < total_lines:
            line = lines[i]

            # Replace body of getFreeformBlackList, ensuring we add .end method and skip original body
            if '.method public static blacklist getFreeformBlackList()Ljava/util/List;' in line:
                # Write method declaration
                new_lines.append(line)
                # New minimal body
                new_lines.append('    .registers 1\n')
                new_lines.append('    sget-object v0, Landroid/util/MiuiMultiWindowAdapter;->sEmptyList:Ljava/util/List;\n')
                new_lines.append('    return-object v0\n')
                # Explicitly close method
                new_lines.append('    .end method\n')

                # Skip original method body until the original .end method
                j = i + 1
                while j < total_lines and '.end method' not in lines[j]:
                    j += 1
                # Skip the original .end method line as well (since we already added one)
                i = j + 1
                file_modified = True
                print("    ✅ Da sua method getFreeformBlackList thanh cong")
                continue

            # Replace body of getFreeformBlackListFromCloud similarly
            if '.method public static blacklist getFreeformBlackListFromCloud(Landroid/content/Context;)Ljava/util/List;' in line:
                new_lines.append(line)
                new_lines.append('    .registers 7\n')
                new_lines.append('    .annotation system Ldalvik/annotation/Signature;\n')
                new_lines.append('        value = {\n')
                new_lines.append('            "(",\n')
                new_lines.append('            "Landroid/content/Context;",\n')
                new_lines.append('            ")",\n')
                new_lines.append('            "Ljava/util/List<",\n')
                new_lines.append('            "Ljava/lang/String;",\n')
                new_lines.append('            ">;"\n')
                new_lines.append('        }\n')
                new_lines.append('    .end annotation\n')
                new_lines.append('    const-string v0, "MiuiMultiWindowAdapter"\n')
                new_lines.append('    new-instance v1, Ljava/util/ArrayList;\n')
                new_lines.append('    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V\n')
                new_lines.append('    return-object v1\n')
                new_lines.append('    .end method\n')

                j = i + 1
                while j < total_lines and '.end method' not in lines[j]:
                    j += 1
                i = j + 1
                file_modified = True
                print("    ✅ Da sua method getFreeformBlackListFromCloud thanh cong")
                continue

            # Non-target lines
            new_lines.append(line)
            i += 1

        # Write back to file if modified
        if file_modified:
            miui_multi_window_path.write_text("".join(new_lines), encoding='utf-8')
            print("✅ Da chinh sua MiuiMultiWindowAdapter.smali thanh cong")
        else:
            print("⚠️  Khong tim thay method nao can sua")

    except Exception as e:
        print(f"❌ Loi khi chinh sua MiuiMultiWindowAdapter.smali: {e}")
        return

    print(f"\n🎉 Enable Floating Window All App complete!")


# Exact copy of MEZOBuildRom.py:increase_number_of_floating_windows (lines 4958-5019)
def increase_number_of_floating_windows(work_dir: Path) -> None:
    """Tăng số lượng floating windows"""
    print("\n=== TANG SO LUONG FLOATING WINDOWS ===")

    # Kiểm tra thư mục miui_services_unpacked
    miui_services_dir = work_dir / "miui_services_unpacked"
    if not miui_services_dir.exists():
        print("❌ Khong tim thay thuc muc miui_services_unpacked")
        return

    # Tìm file MiuiFreeFormStackDisplayStrategy.smali
    target_file = miui_services_dir / "smali_classes" / "com" / "android" / "server" / "wm" / "MiuiFreeFormStackDisplayStrategy.smali"
    if not target_file.exists():
        print("❌ Khong tim thay file MiuiFreeFormStackDisplayStrategy.smali")
        return

    try:
        # Đọc nội dung file
        with target_file.open('r', encoding='utf-8') as f:
            lines = f.readlines()

        # Tìm method getMaxMiuiFreeFormStackCount
        method_start = -1
        method_end = -1
        method_found = False

        for i, line in enumerate(lines):
            if line.lstrip().startswith('.method') and ' getMaxMiuiFreeFormStackCount(' in line:
                method_start = i
                method_found = True
            elif method_found and '.end method' in line:
                method_end = i
                break

        if not method_found:
            print("❌ Khong tim thay method getMaxMiuiFreeFormStackCount")
            return

        if method_end == -1:
            print("❌ Khong tim thay ket thuc method getMaxMiuiFreeFormStackCount")
            return

        # Thay thế nội dung method
        new_content = [
            '    .registers 3\n',
            '\n',
            '    const/4 p0, 0x4\n',
            '\n',
            '    return p0\n'
        ]

        # Tạo nội dung mới
        new_lines = lines[:method_start + 1] + new_content + lines[method_end:]

        # Ghi lại file
        target_file.write_text("".join(new_lines), encoding='utf-8')

        print("✅ Da sua thanh cong method getMaxMiuiFreeFormStackCount")
        print("✅ So luong floating windows da duoc tang len")

    except Exception as e:
        print(f"❌ Loi khi sua MiuiFreeFormStackDisplayStrategy.smali: {e}")


# Exact copy of MEZOBuildRom.py:fix_theme_reset (lines 5135-5187)
def fix_theme_reset(work_dir: Path) -> None:
    """Remove smali lines from nearest `.line` down to DRM broadcast call."""
    print("\n🔧 Processing theme reset fix...")
    target_file = (
        work_dir
        / "miui_services_unpacked"
        / "smali_classes"
        / "com"
        / "android"
        / "server"
        / "am"
        / "ActivityManagerServiceImpl.smali"
    )

    if not target_file.exists():
        print(f"❌ Khong tim thay file: {target_file}")
        return

    try:
        lines = target_file.read_text(encoding="utf-8").splitlines(keepends=True)
    except Exception as exc:
        print(f"❌ Loi khi doc file {target_file}: {exc}")
        return

    broadcast_idx = -1
    for idx, line in enumerate(lines):
        if "Lmiui/drm/DrmBroadcast;->broadcast()V" in line:
            broadcast_idx = idx
            break

    if broadcast_idx == -1:
        print("ℹ️ Khong tim thay dong chua 'Lmiui/drm/DrmBroadcast;->broadcast()V'")
        return

    line_marker_idx = -1
    for idx in range(broadcast_idx, -1, -1):
        if "line" in lines[idx]:
            line_marker_idx = idx
            break

    if line_marker_idx == -1:
        print("⚠️ Tim thay dong broadcast, nhung khong tim thay dong chua 'line' o phia tren.")
        return

    # Xoa doan tu dong '.line' gan nhat den dong goi broadcast (bao gom ca hai dau).
    del lines[line_marker_idx : broadcast_idx + 1]

    try:
        target_file.write_text("".join(lines), encoding="utf-8")
        removed_count = broadcast_idx - line_marker_idx + 1
        print(f"✅ Da xoa {removed_count} dong trong {target_file.name}")
    except Exception as exc:
        print(f"❌ Loi khi ghi file {target_file}: {exc}")


# ── orchestrator ──────────────────────────────────────────────────────────────
def apply_legend_jar_misc_legacy_patches(
    work_dir: Path,
    android_major: int | None,
    flavor: str,
    execute: bool = False,
) -> dict:
    """
    Run (or dry-run) all Legend JAR misc legacy patches in MEZOBuildRom order.

    Flavor guard: only runs for legend / deadzone_legend / DeadZone_Legend.
    """
    norm_flavor = _normalise_flavor(flavor)
    if norm_flavor not in _LEGEND_FLAVORS:
        report = {
            "work_dir": str(work_dir),
            "flavor": flavor,
            "android_major": android_major,
            "dry_run": not execute,
            "status": "SKIPPED_NON_LEGEND",
            "folders_checked": [],
            "version_specific_function": None,
            "common_jar_functions": [],
            "warnings": [f"Flavor '{flavor}' is not Legend; skipped."],
            "errors": [],
        }
        return report

    # Folder checks
    folders_checked: list[dict] = []
    for folder_name in _EXPECTED_FOLDERS:
        folder_path = work_dir / folder_name
        folders_checked.append({
            "folder": folder_name,
            "exists": folder_path.is_dir(),
        })

    # Determine which version-specific function will run
    version_specific: str | None = None
    android_warning: str | None = None

    if android_major == 15:
        version_specific = "fix_bootloop_a15 + tricky_wukong_a15"
    elif android_major == 14:
        version_specific = "tricky_wukong_a15"
    elif android_major == 16:
        version_specific = "tricky_wukong_a16"
    elif android_major is None:
        android_warning = "android_major not provided; version-specific functions will be skipped"
    else:
        android_warning = f"android_major={android_major} is not 14/15/16; version-specific functions will be skipped"

    common_jar_functions = [
        "enhanced_keyboard",
        "enable_floating_window_all_app",
        "increase_number_of_floating_windows",
        "fix_theme_reset",
    ]

    warnings: list[str] = []
    errors: list[str] = []
    if android_warning:
        warnings.append(android_warning)

    if not execute:
        report = {
            "work_dir": str(work_dir),
            "flavor": flavor,
            "android_major": android_major,
            "dry_run": True,
            "status": "DRY_RUN",
            "folders_checked": folders_checked,
            "version_specific_function": version_specific,
            "common_jar_functions": common_jar_functions,
            "warnings": warnings,
            "errors": errors,
        }
        return report

    # Execute in MEZOBuildRom order
    if android_major == 15:
        try:
            fix_bootloop_a15(work_dir)
        except Exception as exc:
            errors.append(f"fix_bootloop_a15: {exc}")

    if android_major in (14, 15):
        try:
            tricky_wukong_a15(work_dir)
        except Exception as exc:
            errors.append(f"tricky_wukong_a15: {exc}")
    elif android_major == 16:
        try:
            tricky_wukong_a16(work_dir)
        except Exception as exc:
            errors.append(f"tricky_wukong_a16: {exc}")

    try:
        enhanced_keyboard(work_dir)
    except Exception as exc:
        errors.append(f"enhanced_keyboard: {exc}")

    try:
        enable_floating_window_all_app(work_dir)
    except Exception as exc:
        errors.append(f"enable_floating_window_all_app: {exc}")

    try:
        increase_number_of_floating_windows(work_dir)
    except Exception as exc:
        errors.append(f"increase_number_of_floating_windows: {exc}")

    try:
        fix_theme_reset(work_dir)
    except Exception as exc:
        errors.append(f"fix_theme_reset: {exc}")

    status = "FAILED" if errors else "APPLIED"

    report = {
        "work_dir": str(work_dir),
        "flavor": flavor,
        "android_major": android_major,
        "dry_run": False,
        "status": status,
        "folders_checked": folders_checked,
        "version_specific_function": version_specific,
        "common_jar_functions": common_jar_functions,
        "warnings": warnings,
        "errors": errors,
    }
    return report


# ── report writer ──────────────────────────────────────────────────────────────
def _format_text_report(report: dict) -> str:
    mode = "DRY RUN" if report.get("dry_run") else "EXECUTE"
    lines: list[str] = [
        f"DeadZone Legend JAR Misc Legacy Report  [{mode}]",
        "=" * 60,
        f"Status:          {report.get('status', '?')}",
        f"Flavor:          {report.get('flavor', '?')}",
        f"Work dir:        {report.get('work_dir', '?')}",
        f"Android major:   {report.get('android_major') if report.get('android_major') is not None else '(unknown)'}",
        f"Dry run:         {report.get('dry_run', True)}",
        "",
        f"Version-specific function: {report.get('version_specific_function') or '(none)'}",
        "",
        "Common JAR functions:",
    ]
    for fn in report.get("common_jar_functions", []):
        lines.append(f"  - {fn}")

    lines.append("")
    lines.append("Folders checked:")
    for fc in report.get("folders_checked", []):
        mark = "OK" if fc.get("exists") else "MISSING"
        lines.append(f"  [{mark}] {fc.get('folder')}")

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

    print(f"[jar_misc_legacy] JSON: {json_path}")
    print(f"[jar_misc_legacy] TXT : {txt_path}")


# ── CLI ────────────────────────────────────────────────────────────────────────
def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Legend JAR misc legacy patches (DeadZone factory)",
    )
    p.add_argument("--work-dir", dest="work_dir", required=True,
                   help="Path to JAR work directory (contains *_unpacked dirs)")
    p.add_argument("--flavor", required=True,
                   help="ROM flavor (e.g. legend)")
    p.add_argument("--android-major", dest="android_major", type=int, default=None,
                   help="Android major version (14, 15, or 16)")
    p.add_argument("--execute", action="store_true",
                   help="Apply patches (default is dry-run)")
    return p


def _main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    work_dir = Path(args.work_dir).resolve()
    if not work_dir.is_dir():
        print(f"[jar_misc_legacy] ERROR: work directory not found: {work_dir}", file=sys.stderr)
        return 2

    mode = "EXECUTE" if args.execute else "DRY-RUN"
    print(f"[jar_misc_legacy] mode={mode}  flavor={args.flavor}  android={args.android_major}  work={work_dir}")

    report = apply_legend_jar_misc_legacy_patches(
        work_dir=work_dir,
        android_major=args.android_major,
        flavor=args.flavor,
        execute=args.execute,
    )

    _write_reports(report)

    print(f"[jar_misc_legacy] status={report['status']}")
    if report["warnings"]:
        for w in report["warnings"]:
            print(f"[jar_misc_legacy] WARNING: {w}")
    if report["errors"]:
        for e in report["errors"]:
            print(f"[jar_misc_legacy] ERROR: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(_main())
