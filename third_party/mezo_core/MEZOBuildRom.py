#!/usr/bin/env python3
import builtins
import json
import os
import re
import stat
import subprocess
import shutil
import sys
import tarfile
import time
import zipfile
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = ROOT_DIR / "src"
REFERENCE_PROJECT_DIR = ROOT_DIR / "mio"
REFERENCE_CONFIG_DIR = REFERENCE_PROJECT_DIR / "config"
CONTEXT_RULES_FILE = ROOT_DIR / "bin" / "context_rules.json"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

os.chdir(ROOT_DIR)

from src.core.lpunpack import unpack as lpunpack_unpack  # noqa: E402
from src.core.lpunpack import SparseImage  # noqa: E402
from src.core.lpunpack import get_info as lpunpack_get_info  # noqa: E402
from src.core.imgextractor import Extractor  # noqa: E402
from src.core.posix import symlink as posix_symlink  # noqa: E402
from src.core import contextpatch, fspatch  # noqa: E402
from src.core.utils import call, gettype, simg2img, JsonEdit, tool_bin  # noqa: E402


SUPPORTED_ARCHIVES = (".zip", ".tgz", ".tar.gz", ".tar")
MIUI_SYSTEM_UI_APK_NAME = "MiuiSystemUI.apk"
MIUI_SYSTEM_UI_SRC_DIR_NAME = "MiuiSystemUI_apk_src"
PROVISION_APK_NAME = "Provision.apk"
PROVISION_APK_SRC_DIR_NAME = "Provision_apk_src"
APK_EDITOR_JAR_NAME = "APKEditor.jar"
APK_EDITOR_FRAMEWORK_VERSION = 35
MEZO_UI_DIR_NAME = "MEZO_UI"
BUILD_PROP_KEYS = [
    "ro.product.odm.brand",
    "ro.product.odm.device",
    "ro.product.odm.model",
    "ro.product.odm.marketname",
    "ro.mi.os.version.incremental",
    "ro.system.build.version.release",
]


def _android_major(android_release: str | None) -> int | None:
    if not android_release:
        return None

    match = re.search(r"\d+", str(android_release))
    return int(match.group()) if match else None


def mezo_android_major(android_release: str | None) -> int | None:
    return _android_major(android_release)


def log(message: str) -> None:
    print(message)


def pause_if_needed() -> None:
    if os.name == "nt":
        try:
            input("\nPress Enter to exit...")
        except EOFError:
            pass


def choose_path() -> Path | None:
    try:
        import tkinter as tk
        from tkinter import filedialog
    except Exception:
        return None

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select ROM file, super.img, or cancel to choose a project folder",
        filetypes=[
            ("ROM files", "*.zip *.tgz *.tar.gz *.tar *.img"),
            ("All files", "*.*"),
        ],
    )
    if file_path:
        root.destroy()
        return Path(file_path)

    dir_path = filedialog.askdirectory(title="Choose project folder to repack")
    root.destroy()
    return Path(dir_path) if dir_path else None


def ensure_clean_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def remove_path_force(path: Path) -> bool:
    if not path.exists():
        return True

    def del_rw(target: str) -> None:
        try:
            os.chmod(target, stat.S_IWRITE)
        except OSError:
            pass
        os.remove(target)

    try:
        if path.is_file():
            del_rw(str(path))
        else:
            shutil.rmtree(path, onerror=lambda _, fn, __: del_rw(fn))
    except Exception:
        pass

    if path.exists() and os.name == "nt":
        # Fallback for stubborn Windows paths that remain locked/read-only.
        os.system(f'cmd /c rd /s /q "{path}" >nul 2>nul')

    return not path.exists()


def extract_tar_safe(archive: tarfile.TarFile, dest: Path) -> None:
    dest_abs = dest.resolve()
    for member in archive.getmembers():
        member_path = (dest / member.name).resolve()
        if os.path.commonpath([str(dest_abs), str(member_path)]) != str(dest_abs):
            raise RuntimeError(f"Invalid tar entry: {member.name}")
    archive.extractall(dest)


def extract_rom(rom_path: Path, output_dir: Path) -> Path:
    rom_extract_dir = output_dir / "rom"
    ensure_clean_dir(rom_extract_dir)

    name_lower = rom_path.name.lower()
    log(f"[1/3] Extracting ROM: {rom_path.name}")

    if name_lower.endswith(".zip"):
        with zipfile.ZipFile(rom_path, "r") as zip_file:
            zip_file.extractall(rom_extract_dir)
        return rom_extract_dir

    if name_lower.endswith((".tgz", ".tar.gz")):
        with tarfile.open(rom_path, "r:gz") as tar_file:
            extract_tar_safe(tar_file, rom_extract_dir)
        return rom_extract_dir

    if name_lower.endswith(".tar"):
        with tarfile.open(rom_path, "r") as tar_file:
            extract_tar_safe(tar_file, rom_extract_dir)
        return rom_extract_dir

    copied_path = rom_extract_dir / rom_path.name
    shutil.copy2(rom_path, copied_path)
    return rom_extract_dir


def resolve_magiskboot_exe() -> Path | None:
    if os.name != "nt":
        return None

    arch_candidates = ["AMD64", "x86"]
    if os.environ.get("PROCESSOR_ARCHITECTURE", "").lower() == "x86" and not os.environ.get("PROCESSOR_ARCHITEW6432"):
        arch_candidates = ["x86", "AMD64"]

    for arch in arch_candidates:
        candidate = ROOT_DIR / "bin" / "Windows" / arch / "magiskboot.exe"
        if candidate.is_file():
            return candidate
    return None


def _cpio_aligned_size(size: int) -> int:
    return (4 - (size % 4)) % 4


def _resolve_cpio_entry_path(output_dir: Path, entry_name: str) -> Path:
    normalized = entry_name.replace("\\", "/").lstrip("/")
    while normalized.startswith("./"):
        normalized = normalized[2:]

    target_path = (output_dir / normalized).resolve()
    output_dir_resolved = output_dir.resolve()
    if os.path.commonpath([str(output_dir_resolved), str(target_path)]) != str(output_dir_resolved):
        raise RuntimeError(f"Invalid CPIO path: {entry_name}")
    return target_path


def extract_cpio_without_toml(cpio_path: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    with cpio_path.open("rb") as file:
        while True:
            header = file.read(110)
            if not header:
                break
            if len(header) != 110:
                raise RuntimeError(f"Invalid CPIO header in {cpio_path}")

            magic = header[:6]
            if magic not in (b"070701", b"070702"):
                raise RuntimeError(f"Unsupported CPIO magic in {cpio_path}: {magic!r}")

            fields = [int(header[offset:offset + 8], 16) for offset in range(6, 110, 8)]
            mode = fields[1]
            file_size = fields[6]
            name_size = fields[11]

            name_bytes = file.read(name_size)
            if len(name_bytes) != name_size:
                raise RuntimeError(f"Could not read full entry name in {cpio_path}")

            entry_name = name_bytes[:-1].decode("utf-8", errors="ignore")
            file.read(_cpio_aligned_size(110 + name_size))

            if entry_name == "TRAILER!!!":
                break

            file_data = file.read(file_size)
            if len(file_data) != file_size:
                raise RuntimeError(f"Could not read full data for entry {entry_name} in {cpio_path}")
            file.read(_cpio_aligned_size(file_size))

            if not entry_name or entry_name == ".":
                continue

            target_path = _resolve_cpio_entry_path(output_dir, entry_name)
            file_type = mode & 0o170000

            if file_type == 0o040000:
                target_path.mkdir(parents=True, exist_ok=True)
                continue

            target_path.parent.mkdir(parents=True, exist_ok=True)

            if file_type == 0o120000:
                if target_path.exists():
                    remove_path_force(target_path)
                posix_symlink(file_data.decode("utf-8", errors="ignore"), str(target_path))
                continue

            if file_type == 0o100000:
                with target_path.open("wb") as out_file:
                    out_file.write(file_data)
                try:
                    os.chmod(target_path, mode & 0o7777)
                except OSError:
                    pass
                continue

            log(f"    Warning: skipping unsupported CPIO entry {entry_name} (mode={oct(mode)})")



def find_super_img(search_dir: Path) -> Path | None:
    exact_matches = []
    partial_matches = []

    for path in search_dir.rglob("*"):
        if not path.is_file():
            continue
        lower_name = path.name.lower()
        if lower_name == "super.img":
            exact_matches.append(path)
        elif lower_name.startswith("super") and lower_name.endswith(".img"):
            partial_matches.append(path)

    if exact_matches:
        return exact_matches[0]
    if partial_matches:
        return partial_matches[0]
    return None


def try_extract_super_from_payload(
    extracted_dir: Path,
    project_dir: Path,
    search_roots: list[Path],
) -> bool:
    """
    Thử giải nén payload.bin để:
    1) tạo ra `super.img` (nếu có)
    2) hoặc nếu không có super.img thì giải nén các partition img từ payload:
       mi_ext.img, odm.img, product.img, system.img, system_dlkm.img, system_ext.img,
       vendor.img, vendor_dlkm.img

    Đồng thời ghi thông tin giải nén vào `project_dir/config`.
    Sau khi giải nén xong, sẽ xóa các file `*.img` vừa copy sang `project_dir`.

    - Tìm payload.bin trong các `search_roots`
    - Giải nén bằng src/core/payload_extract.py
    - Trả về True nếu sau khi giải nén có thể tìm thấy super.img HOẶC ít nhất 1 partition img đã được giải nén
    """
    try:
        from src.core.payload_extract import extract_partitions_from_payload
    except Exception as exc:
        log(f"Could not import payload_extract (warning): {exc}")
        return False

    payload_candidates: list[Path] = []
    for root in search_roots:
        if not root.exists():
            continue
        try:
            payload_candidates.extend([p for p in root.rglob("payload.bin") if p.is_file()])
        except Exception:
            pass

    # Unique by path string
    seen: set[str] = set()
    unique_payloads: list[Path] = []
    for p in payload_candidates:
        s = str(p)
        if s in seen:
            continue
        seen.add(s)
        unique_payloads.append(p)

    if not unique_payloads:
        log("payload.bin not found for extraction.")
        return False

    payload_out_dir = extracted_dir / "payload_extracted"
    required_imgs = [
        "mi_ext.img",
        "odm.img",
        "product.img",
        "system.img",
        "system_dlkm.img",
        "system_ext.img",
        "vendor.img",
        "vendor_dlkm.img",
    ]

    for idx, payload_path in enumerate(unique_payloads, start=1):
        try:
            log(f"[Payload] [{idx}/{len(unique_payloads)}] Attempting extraction: {payload_path}")
            if payload_out_dir.exists():
                remove_path_force(payload_out_dir)
            payload_out_dir.mkdir(parents=True, exist_ok=True)

            with payload_path.open("rb") as f:
                extract_partitions_from_payload(
                    reader=f,
                    partitions_name=[],
                    out_dir=str(payload_out_dir),
                    max_workers=32,
                )

            # Nếu payload_extract đã không tạo super.img thì vẫn cố gắng giải nén các partition img cụ thể.
            payload_partition_extracted_any = False
            parts_info_from_payload: dict[str, str] = {}
            for img_name in required_imgs:
                src_img = payload_out_dir / img_name
                if not src_img.is_file():
                    continue

                payload_partition_extracted_any = True
                dst_img = project_dir / img_name
                try:
                    if dst_img.exists():
                        remove_path_force(dst_img)
                    # Move thay vi copy de tranh duplicate va giam mat dung luong
                    shutil.move(src_img, dst_img)

                    # Dùng chung logic extract partition để tạo config/_file_contexts/_fs_config và update parts_info.
                    extract_single_partition(dst_img, project_dir, parts_info_from_payload)
                finally:
                    # Xóa các img vừa copy sang project_dir theo yêu cầu.
                    if dst_img.exists():
                        remove_path_force(dst_img)

            # Ghi lại parts_info vào project_dir/config (nếu có gì đó được giải nén)
            if payload_partition_extracted_any and parts_info_from_payload:
                config_dir = project_dir / "config"
                config_dir.mkdir(parents=True, exist_ok=True)
                parts_info_path = config_dir / "parts_info"
                existing_parts_info: dict = {}
                try:
                    if parts_info_path.exists():
                        existing_parts_info = JsonEdit(str(parts_info_path)).read()
                except Exception:
                    existing_parts_info = {}

                if isinstance(existing_parts_info, dict):
                    existing_parts_info.update(parts_info_from_payload)
                    JsonEdit(str(parts_info_path)).write(existing_parts_info)
                else:
                    JsonEdit(str(parts_info_path)).write(parts_info_from_payload)

            found_super = find_super_img(extracted_dir) is not None
            if found_super:
                log("[Payload] super.img created from payload.bin.")
                return True
            else:
                log("[Payload] Extraction complete but super.img not found.")
                if payload_partition_extracted_any:
                    log("[Payload] Partition images extracted from payload (continuing).")
                    return True
        except Exception as exc:
            log(f"[Payload] Error extracting {payload_path.name}: {exc}")

    return False


def parse_build_prop(path: Path) -> dict[str, str]:
    props: dict[str, str] = {}
    if not path.is_file():
        return props

    try:
        with path.open("r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()
                if key in BUILD_PROP_KEYS and key not in props:
                    props[key] = value
    except Exception as exc:
        log(f"Error reading '{path}': {exc}")

    return props


def find_and_read_build_props(project_dir: Path) -> tuple[str | None, str | None]:
    aggregated: dict[str, str] = {}
    found_any_file = False

    for build_prop_path in project_dir.rglob("build.prop"):
        found_any_file = True
        props = parse_build_prop(build_prop_path)
        if not props:
            continue

        for key in BUILD_PROP_KEYS:
            if key not in aggregated and props.get(key):
                aggregated[key] = props[key]

    if not found_any_file:
        log("No build.prop file found in project.")
        return None, None

    if not aggregated:
        log("No build.prop values found for required keys.")
        return None, None

    log("ROM info:")

    brand = aggregated.get("ro.product.odm.brand")
    device = aggregated.get("ro.product.odm.device")
    model = aggregated.get("ro.product.odm.model")
    marketname = aggregated.get("ro.product.odm.marketname")
    mi_incremental = aggregated.get("ro.mi.os.version.incremental")
    android_release = aggregated.get("ro.system.build.version.release")

    if brand:
        log(f"    Brand: {brand}")
    if device:
        log(f"    Device: {device}")
    if marketname:
        log(f"    Market name: {marketname}")
    if model:
        log(f"    Model: {model}")
    if mi_incremental:
        log(f"    MI version: {mi_incremental}")
    if android_release:
        log(f"    Android version: {android_release}")

    # Ghi thong tin vao file DeadZone_firmware.txt trong thu muc output
    try:
        output_dir = build_repack_output_dir(project_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        firmware_info_path = output_dir / "DeadZone_firmware.txt"
        with firmware_info_path.open("w", encoding="utf-8") as f:
            f.write(f"Codename={device or ''}\n")
            f.write(f"Device name={marketname or ''}\n")
            f.write(f"MI version={mi_incremental or ''}\n")
            f.write(f"Android release={android_release or ''}\n")
        log(f"    Firmware info written: {firmware_info_path}")
    except Exception as exc:
        log(f"    Error writing DeadZone_firmware.txt: {exc}")
    
    #chuyển file từ rom/payload_extracted vào images
    payload_extracted_dir = project_dir / "rom" / "payload_extracted"
    payload_images_dir = project_dir / f"DeadZone_{device}_{mi_incremental}_{android_release}" / "images"
    if payload_extracted_dir.is_dir():
        payload_images_dir.mkdir(parents=True, exist_ok=True)
        moved_count = 0
        try:
            for entry in sorted(payload_extracted_dir.iterdir(), key=lambda item: item.name.lower()):
                target = payload_images_dir / entry.name
                if target.exists():
                    if remove_path_force(target):
                        log(f"    Removed duplicate target: {target}")
                    else:
                        log(f"    Warning: could not remove duplicate target: {target}")
                        continue
                shutil.move(str(entry), str(target))
                log(f"    Moved {entry.name} -> {payload_images_dir}")
                moved_count += 1
            if moved_count > 0:
                shutil.rmtree(payload_extracted_dir.parent, ignore_errors=True)
                log(f"Moved {moved_count} file(s) from payload_extracted to images, removed rom directory.")
            else:
                log("No files to move from payload_extracted.")
        except Exception as exc:
            log(f"Error processing payload_extracted: {exc}")

    # vo hieu hoa vbmeta ben trong thu muc images_dir
    images_dir: Path | None = None
    if device and mi_incremental and android_release:
        images_dir = project_dir / f"DeadZone_{device}_{mi_incremental}_{android_release}" / "images"

    if images_dir is None or not images_dir.is_dir():
        candidates = sorted(project_dir.rglob("vbmeta.img"))
        if candidates:
            images_dir = candidates[0].parent
            log(f"[DEBUG] Tu dong tim thay images_dir: {images_dir}")
        else:
            log("[INFO] vbmeta.img not found in project.")
            return mi_incremental, android_release

    vbmeta_img = images_dir / "vbmeta.img"
    avbtool_path = ROOT_DIR / "vbmeta" / "avbtool.py"
    avb_key_path = ROOT_DIR / "vbmeta" / "testkey_rsa2048.pem"
    vbmeta_tmp = images_dir / "vbmeta_patched.img"

    if not images_dir.is_dir():
        log(f"[INFO] images directory not found: {images_dir}")
        return mi_incremental, android_release

    if not vbmeta_img.is_file():
        log(f"[INFO] vbmeta.img not found in images: {images_dir}")
        return mi_incremental, android_release

    if not avbtool_path.is_file():
        log(f"[ERROR] avbtool not found: {avbtool_path}")
        return mi_incremental, android_release

    if not avb_key_path.is_file():
        log(f"[ERROR] AVB key not found: {avb_key_path}")
        return mi_incremental, android_release

    openssl_bin_dir = ROOT_DIR / "bin" / "openssl"
    if not (openssl_bin_dir / "openssl.exe").is_file():
        log(f"[ERROR] openssl.exe not found in {openssl_bin_dir}!")
        return mi_incremental, android_release

    log("\n==========================================")
    log("   DEADZONE VBMeta Generator")
    log("   VO HIEU HOA VBMETA - dm-verity Disabled")
    log("==========================================")
    log("[INFO] Patching vbmeta file...")
    log(f"       Ke thua cau truc tu: {vbmeta_img.name}")
    log("       Trang thai: AVB Enable, dm-verity Disabled")
    log("       Thu muc:  " + str(images_dir))

    try:
        if vbmeta_tmp.exists():
            remove_path_force(vbmeta_tmp)

        cmd = [
            sys.executable,
            str(avbtool_path),
            "make_vbmeta_image",
            "--output",
            str(vbmeta_tmp),
            "--algorithm",
            "SHA256_RSA2048",
            "--key",
            str(avb_key_path),
            "--include_descriptors_from_image",
            str(vbmeta_img),
            "--padding_size",
            "4096",
            "--set_hashtree_disabled_flag",
        ]
        env = os.environ.copy()
        env["PATH"] = str(openssl_bin_dir) + os.pathsep + env.get("PATH", "")
        subprocess.run(cmd, check=True, cwd=str(ROOT_DIR / "vbmeta"), env=env)
        shutil.move(str(vbmeta_tmp), str(vbmeta_img))
        log(f"[OK] vbmeta patched: {vbmeta_img.name}")
        log("[INFO] To flash to device, boot into Fastboot and run:")
        log(f"       fastboot flash vbmeta {images_dir / 'vbmeta.img'}")
    except subprocess.CalledProcessError as exc:
        log(f"[ERROR] Error patching vbmeta (exit code {exc.returncode}).")
        log("[FIX] Check that the 'bin' directory contains the openssl files.")
    except Exception as exc:
        log(f"[ERROR] Error patching vbmeta: {exc}")
    finally:
        if vbmeta_tmp.exists():
            remove_path_force(vbmeta_tmp)
    return mi_incremental, android_release


def read_debloat_list(debloat_path: Path) -> list[str]:
    names: list[str] = []

    if not debloat_path.is_file():
        log(f"Debloat file not found: {debloat_path}")
        return names

    try:
        with debloat_path.open("r", encoding="utf-8", errors="ignore") as file:
            for line in file:
                name = line.strip()
                if not name or name.startswith("#"):
                    continue
                names.append(name)
    except Exception as exc:
        log(f"Error reading debloat list: {exc}")

    return names


def _safe_collect_dirs(project_dir: Path) -> list[Path]:
    dirs: list[Path] = []

    def _onerror(_: OSError) -> None:
        return

    for root, dirnames, _filenames in os.walk(
        project_dir,
        topdown=True,
        followlinks=False,
        onerror=_onerror,
    ):
        root_path = Path(root)
        for dir_name in dirnames:
            dirs.append(root_path / dir_name)

    return dirs


def debloat_project(project_dir: Path, debloat_path: Path) -> None:
    names = read_debloat_list(debloat_path)
    if not names:
        return

    log("Starting debloat from debloat.txt list...")

    # Thu thap truoc de tranh loi do vua duyet vua xoa.
    all_dirs = _safe_collect_dirs(project_dir)

    for name in names:
        log(f"- Searching and removing directories related to: {name}")
        found_any = False
        needle = name.lower()

        for path in all_dirs:
            try:
                if path.is_dir() and path.name.lower() == needle:
                    found_any = True
                    if remove_path_force(path):
                        log(f"    Removed: {path}")
                    else:
                        log(f"    Warning: could not remove {path}")
            except OSError as exc:
                log(f"    Skipping (inaccessible): {path} ({exc})")
            except Exception as exc:
                log(f"    Error removing {path}: {exc}")

        if not found_any:
            log("    No matching directories found.")

    log("Debloat complete.")


def resolve_partition_root(project_dir: Path, partition_name: str) -> Path | None:
    direct_root = project_dir / partition_name
    nested_root = direct_root / partition_name

    if nested_root.is_dir():
        return nested_root
    if direct_root.is_dir():
        return direct_root
    return None


def resolve_partition_file(project_dir: Path, partition_name: str, *parts: str) -> Path | None:
    partition_root = resolve_partition_root(project_dir, partition_name)
    if partition_root is None:
        return None
    return partition_root.joinpath(*parts)


def export_and_decompile_miui_systemui(project_dir: Path, work_dir: Path | None = None) -> None:
    dest_dir = work_dir or project_dir
    system_ext_root = resolve_partition_root(project_dir, "system_ext")
    if system_ext_root is None:
        log("system_ext partition not found for MiuiSystemUI.apk processing.")
        return

    apk_candidates = sorted(system_ext_root.rglob(MIUI_SYSTEM_UI_APK_NAME))
    if not apk_candidates:
        log("MiuiSystemUI.apk not found in system_ext after unpack.")
        return

    src_apk = apk_candidates[0]
    dest_apk = dest_dir / MIUI_SYSTEM_UI_APK_NAME
    dest_apk_src = dest_dir / MIUI_SYSTEM_UI_SRC_DIR_NAME
    apk_editor_src = ROOT_DIR / APK_EDITOR_JAR_NAME
    apk_editor_dst = dest_dir / APK_EDITOR_JAR_NAME

    log(f"Found {MIUI_SYSTEM_UI_APK_NAME}: {src_apk}")

    try:
        if dest_apk.exists():
            remove_path_force(dest_apk)
        shutil.copy2(src_apk, dest_apk)
        log(f"    Exported {MIUI_SYSTEM_UI_APK_NAME} -> {dest_apk}")
    except Exception as exc:
        log(f"    Error extracting {MIUI_SYSTEM_UI_APK_NAME}: {exc}")
        return

    if not apk_editor_src.is_file():
        log(f"{APK_EDITOR_JAR_NAME} not found at {apk_editor_src}")
        return

    try:
        if apk_editor_dst.exists():
            remove_path_force(apk_editor_dst)
        shutil.copy2(apk_editor_src, apk_editor_dst)
        log(f"    Copied {APK_EDITOR_JAR_NAME} -> {apk_editor_dst}")
    except Exception as exc:
        log(f"    Error copying {APK_EDITOR_JAR_NAME}: {exc}")
        return

    try:
        if dest_apk_src.exists():
            remove_path_force(dest_apk_src)

        cmd = [
            "java",
            "-jar",
            str(apk_editor_dst),
            "d",
            "-framework-version",
            str(APK_EDITOR_FRAMEWORK_VERSION),
            "-i",
            str(dest_apk),
            "-o",
            str(dest_apk_src),
        ]
        log(f"Decompiling {MIUI_SYSTEM_UI_APK_NAME} -> {dest_apk_src} ...")
        subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=dest_dir)
        if dest_apk_src.is_dir():
            log(f"    Decompile complete: {MIUI_SYSTEM_UI_APK_NAME}")
        else:
            log(f"    Warning: decompile ran but did not create directory {dest_apk_src}")
    except subprocess.CalledProcessError as exc:
        err = (exc.stderr or exc.stdout or "").strip()
        if err:
            log(f"    Error decompiling {MIUI_SYSTEM_UI_APK_NAME}: {err}")
        else:
            log(f"    Error decompiling {MIUI_SYSTEM_UI_APK_NAME} (exit code {exc.returncode})")
    except FileNotFoundError:
        log(f"Java not found to run {APK_EDITOR_JAR_NAME}.")
    except Exception as exc:
        log(f"    Error decompiling {MIUI_SYSTEM_UI_APK_NAME}: {exc}")


def recompile_apk(work_dir: Path) -> bool:
    apk_src_dir = _miui_systemui_src_dir(work_dir)
    output_apk = work_dir / MIUI_SYSTEM_UI_APK_NAME
    apk_editor_in_workdir = work_dir / APK_EDITOR_JAR_NAME
    apk_editor_jar = apk_editor_in_workdir if apk_editor_in_workdir.is_file() else ROOT_DIR / APK_EDITOR_JAR_NAME

    if not apk_src_dir.is_dir():
        log(f"Source directory not found: {apk_src_dir} (cannot rebuild APK).")
        return False

    if not apk_editor_jar.is_file():
        log(f"{APK_EDITOR_JAR_NAME} not found to rebuild APK.")
        return False

    try:
        if output_apk.exists():
            remove_path_force(output_apk)

        cmd = [
            "java",
            "-jar",
            str(apk_editor_jar),
            "b",
            "-framework-version",
            str(APK_EDITOR_FRAMEWORK_VERSION),
            "-i",
            str(apk_src_dir),
            "-o",
            str(output_apk),
        ]

        log(f"Rebuilding {MIUI_SYSTEM_UI_APK_NAME} from {apk_src_dir} ...")
        subprocess.run(cmd, check=True, capture_output=True, text=True, cwd=work_dir)

        if not output_apk.is_file():
            log(f"Rebuild of {MIUI_SYSTEM_UI_APK_NAME} failed: could not create output file.")
            return False

        log(f"    Rebuild successful -> {output_apk}")

        if remove_path_force(apk_src_dir):
            log(f"    Removed temporary source directory: {apk_src_dir}")
        else:
            log(f"    Warning: could not remove temporary source directory: {apk_src_dir}")

        return True
    except subprocess.CalledProcessError as exc:
        err = (exc.stderr or exc.stdout or "").strip()
        if err:
            log(f"    Error rebuilding {MIUI_SYSTEM_UI_APK_NAME}: {err}")
        else:
            log(f"    Error rebuilding {MIUI_SYSTEM_UI_APK_NAME} (exit code {exc.returncode})")
        return False
    except FileNotFoundError:
        log(f"Java not found to run {APK_EDITOR_JAR_NAME}.")
        return False
    except Exception as exc:
        log(f"    Error rebuilding {MIUI_SYSTEM_UI_APK_NAME}: {exc}")
        return False


def restore_recompiled_miui_systemui_to_project(project_dir: Path, work_dir: Path) -> bool:
    rebuilt_apk = work_dir / MIUI_SYSTEM_UI_APK_NAME
    if not rebuilt_apk.is_file():
        log(f"Rebuilt APK not found at {rebuilt_apk}.")
        return False

    system_ext_root = resolve_partition_root(project_dir, "system_ext")
    if system_ext_root is None:
        log("system_ext partition not found to restore MiuiSystemUI.apk.")
        return False

    apk_candidates = sorted(system_ext_root.rglob(MIUI_SYSTEM_UI_APK_NAME))
    if not apk_candidates:
        log("MiuiSystemUI.apk target not found in system_ext to overwrite.")
        return False

    target_apk = apk_candidates[0]
    try:
        if target_apk.exists():
            remove_path_force(target_apk)
        shutil.move(str(rebuilt_apk), str(target_apk))
        log(f"    Moved rebuilt {MIUI_SYSTEM_UI_APK_NAME} -> {target_apk}")
        return True
    except Exception as exc:
        log(f"    Error restoring {MIUI_SYSTEM_UI_APK_NAME} to system_ext: {exc}")
        return False


def export_and_decompile_provision(project_dir: Path, work_dir: Path | None = None) -> bool:
    dest_dir = work_dir or project_dir
    system_ext_root = resolve_partition_root(project_dir, "system_ext")
    if system_ext_root is None:
        log("system_ext partition not found for Provision.apk processing.")
        return False

    apk_candidates = sorted(system_ext_root.rglob(PROVISION_APK_NAME))
    if not apk_candidates:
        log("Provision.apk not found in system_ext after unpack.")
        return False

    src_apk = apk_candidates[0]
    dest_apk = dest_dir / PROVISION_APK_NAME
    dest_apk_src = dest_dir / PROVISION_APK_SRC_DIR_NAME
    apk_editor_src = ROOT_DIR / APK_EDITOR_JAR_NAME
    apk_editor_dst = dest_dir / APK_EDITOR_JAR_NAME

    log(f"Found {PROVISION_APK_NAME}: {src_apk}")

    try:
        if dest_apk.exists():
            remove_path_force(dest_apk)
        shutil.copy2(src_apk, dest_apk)
        log(f"    Exported {PROVISION_APK_NAME} -> {dest_apk}")
    except Exception as exc:
        log(f"    Error extracting {PROVISION_APK_NAME}: {exc}")
        return False

    if not apk_editor_src.is_file():
        log(f"{APK_EDITOR_JAR_NAME} not found at {apk_editor_src}")
        return False

    try:
        if apk_editor_dst.exists():
            remove_path_force(apk_editor_dst)
        shutil.copy2(apk_editor_src, apk_editor_dst)
        log(f"    Copied {APK_EDITOR_JAR_NAME} -> {apk_editor_dst}")
    except Exception as exc:
        log(f"    Error copying {APK_EDITOR_JAR_NAME}: {exc}")
        return False

    try:
        if dest_apk_src.exists():
            remove_path_force(dest_apk_src)

        cmd = [
            "java",
            "-jar",
            str(apk_editor_dst),
            "d",
            "-framework-version",
            str(APK_EDITOR_FRAMEWORK_VERSION),
            "-i",
            str(dest_apk),
            "-o",
            str(dest_apk_src),
        ]
        log(f"Decompiling {PROVISION_APK_NAME} -> {dest_apk_src} ...")
        subprocess.run(cmd, capture_output=True, text=True, check=True, cwd=dest_dir)
        if dest_apk_src.is_dir():
            log(f"    Decompile complete: {PROVISION_APK_NAME}")
            return True
        log(f"    Warning: decompile ran but did not create directory {dest_apk_src}")
        return False
    except subprocess.CalledProcessError as exc:
        err = (exc.stderr or exc.stdout or "").strip()
        if err:
            log(f"    Error decompiling {PROVISION_APK_NAME}: {err}")
        else:
            log(f"    Error decompiling {PROVISION_APK_NAME} (exit code {exc.returncode})")
        return False
    except FileNotFoundError:
        log(f"Java not found to run {APK_EDITOR_JAR_NAME}.")
        return False
    except Exception as exc:
        log(f"    Error decompiling {PROVISION_APK_NAME}: {exc}")
        return False


def patch_provision_utils(work_dir: Path) -> bool:
    apk_src_dir = work_dir / PROVISION_APK_SRC_DIR_NAME
    utils_file = (
        apk_src_dir
        / "smali"
        / "classes"
        / "com"
        / "android"
        / "provision"
        / "Utils.smali"
    )
    invoke_pattern = re.compile(
        r"invoke-virtual \{v0, v\d+\}, "
        r"Landroid/content/pm/PackageManager;->getApplicationEnabledSetting\(Ljava/lang/String;\)I"
    )

    if not utils_file.is_file():
        log(f"File to patch not found: {utils_file}")
        return False

    try:
        lines = utils_file.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
        method_start = -1
        method_end = -1

        for idx, line in enumerate(lines):
            if line.startswith(".method "):
                method_start = idx
                method_end = -1
                continue

            if method_start != -1 and ".end method" in line:
                method_end = idx
                block_text = "".join(lines[method_start:method_end + 1])
                if "setGmsAppEnabledStateForCn" not in block_text:
                    method_start = -1
                    continue

                for block_idx in range(method_start, method_end):
                    if not invoke_pattern.search(lines[block_idx]):
                        continue

                    move_result_idx = -1
                    for scan_idx in range(block_idx + 1, method_end):
                        if "move-result" in lines[scan_idx]:
                            move_result_idx = scan_idx
                            break

                    if move_result_idx == -1:
                        log("    move-result after getApplicationEnabledSetting not found in Utils.smali")
                        return False

                    for scan_idx in range(move_result_idx + 1, method_end):
                        if "if-ne" in lines[scan_idx]:
                            log("    Skipping Provision Utils patch: content already present.")
                            return True
                        if "if-eq" not in lines[scan_idx]:
                            continue

                        lines[scan_idx] = re.sub(r"\bif-eqz?\b", "if-ne", lines[scan_idx], count=1)
                        utils_file.write_text("".join(lines), encoding="utf-8", errors="ignore")
                        log("    Patched Utils.smali for setGmsAppEnabledStateForCn")
                        return True

                    log("    if-eq/if-eqz line after move-result not found in Utils.smali")
                    return False

                log("    getApplicationEnabledSetting call not found in target method of Utils.smali")
                return False

        log("    Method containing setGmsAppEnabledStateForCn not found in Utils.smali")
        return False
    except Exception as exc:
        log(f"    Error patching Utils.smali: {exc}")
        return False


def recompile_provision_apk(work_dir: Path) -> bool:
    apk_src_dir = work_dir / PROVISION_APK_SRC_DIR_NAME
    output_apk = work_dir / PROVISION_APK_NAME
    apk_editor_in_workdir = work_dir / APK_EDITOR_JAR_NAME
    apk_editor_jar = apk_editor_in_workdir if apk_editor_in_workdir.is_file() else ROOT_DIR / APK_EDITOR_JAR_NAME

    if not apk_src_dir.is_dir():
        log(f"Source directory not found: {apk_src_dir} (cannot rebuild APK).")
        return False

    if not apk_editor_jar.is_file():
        log(f"{APK_EDITOR_JAR_NAME} not found to rebuild APK.")
        return False

    try:
        if output_apk.exists():
            remove_path_force(output_apk)

        cmd = [
            "java",
            "-jar",
            str(apk_editor_jar),
            "b",
            "-framework-version",
            str(APK_EDITOR_FRAMEWORK_VERSION),
            "-i",
            str(apk_src_dir),
            "-o",
            str(output_apk),
        ]

        log(f"Rebuilding {PROVISION_APK_NAME} from {apk_src_dir} ...")
        subprocess.run(cmd, check=True, capture_output=True, text=True, cwd=work_dir)

        if not output_apk.is_file():
            log(f"Rebuild of {PROVISION_APK_NAME} failed: could not create output file.")
            return False

        log(f"    Rebuild successful -> {output_apk}")

        if remove_path_force(apk_src_dir):
            log(f"    Removed temporary source directory: {apk_src_dir}")
        else:
            log(f"    Warning: could not remove temporary source directory: {apk_src_dir}")

        return True
    except subprocess.CalledProcessError as exc:
        err = (exc.stderr or exc.stdout or "").strip()
        if err:
            log(f"    Error rebuilding {PROVISION_APK_NAME}: {err}")
        else:
            log(f"    Error rebuilding {PROVISION_APK_NAME} (exit code {exc.returncode})")
        return False
    except FileNotFoundError:
        log(f"Java not found to run {APK_EDITOR_JAR_NAME}.")
        return False
    except Exception as exc:
        log(f"    Error rebuilding {PROVISION_APK_NAME}: {exc}")
        return False


def restore_recompiled_provision_to_project(project_dir: Path, work_dir: Path) -> bool:
    rebuilt_apk = work_dir / PROVISION_APK_NAME
    apk_editor_in_workdir = work_dir / APK_EDITOR_JAR_NAME
    if not rebuilt_apk.is_file():
        log(f"Rebuilt APK not found at {rebuilt_apk}.")
        return False

    system_ext_root = resolve_partition_root(project_dir, "system_ext")
    if system_ext_root is None:
        log("system_ext partition not found to restore Provision.apk.")
        return False

    apk_candidates = sorted(system_ext_root.rglob(PROVISION_APK_NAME))
    if not apk_candidates:
        log("Provision.apk target not found in system_ext to overwrite.")
        return False

    target_apk = apk_candidates[0]
    try:
        if target_apk.exists():
            remove_path_force(target_apk)
        shutil.move(str(rebuilt_apk), str(target_apk))
        log(f"    Moved rebuilt {PROVISION_APK_NAME} -> {target_apk}")
        if apk_editor_in_workdir.exists():
            if remove_path_force(apk_editor_in_workdir):
                log(f"    Removed temporary file: {apk_editor_in_workdir}")
            else:
                log(f"    Warning: could not remove temporary file: {apk_editor_in_workdir}")
        return True
    except Exception as exc:
        log(f"    Error restoring {PROVISION_APK_NAME} to system_ext: {exc}")
        return False


def process_provision_apk(project_dir: Path, work_dir: Path) -> None:
    if not export_and_decompile_provision(project_dir, work_dir):
        return
    if not patch_provision_utils(work_dir):
        return
    if not recompile_provision_apk(work_dir):
        return
    restore_recompiled_provision_to_project(project_dir, work_dir)


def _miui_systemui_src_dir(work_dir: Path) -> Path:
    return work_dir / MIUI_SYSTEM_UI_SRC_DIR_NAME


def _mezo_ui_dir() -> Path:
    return ROOT_DIR / MEZO_UI_DIR_NAME


def _insert_after_method_registers(file_path: Path, method_pattern: str, insert_lines: list[str], guard_text: str) -> bool:
    if not file_path.is_file():
        log(f"    File not found: {file_path}")
        return False

    try:
        lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
        content_str = "".join(lines)
        if guard_text in content_str:
            log(f"    Skipping {file_path.name}: patch already applied.")
            return True

        method_start = -1
        registers_line_idx = -1
        method_end = -1

        for idx, line in enumerate(lines):
            if method_start == -1:
                if re.search(method_pattern, line):
                    method_start = idx
                continue

            if registers_line_idx == -1 and re.search(r"\.(locals|registers)\s+\d+", line):
                registers_line_idx = idx
                continue

            if ".end method" in line:
                method_end = idx
                break

        if method_start == -1:
            log(f"    Target method not found in {file_path.name}")
            return False
        if registers_line_idx == -1:
            log(f"    .locals/.registers not found in {file_path.name}")
            return False
        if method_end == -1:
            log(f"    Method end not found in {file_path.name}")
            return False

        insert_pos = registers_line_idx + 1
        lines[insert_pos:insert_pos] = insert_lines
        file_path.write_text("".join(lines), encoding="utf-8", errors="ignore")
        return True
    except Exception as exc:
        log(f"    Error editing {file_path.name}: {exc}")
        return False


def _replace_method_body(file_path: Path, method_pattern: str, new_body_lines: list[str]) -> bool:
    if not file_path.is_file():
        log(f"    File not found: {file_path}")
        return False

    try:
        lines = file_path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
        method_start = -1
        method_end = -1

        for idx, line in enumerate(lines):
            if method_start == -1:
                if re.search(method_pattern, line):
                    method_start = idx
                continue

            if ".end method" in line:
                method_end = idx
                break

        if method_start == -1:
            log(f"    Khong tim thay method can thay trong {file_path.name}")
            return False
        if method_end == -1:
            log(f"    Method end not found in {file_path.name}")
            return False

        replacement = [lines[method_start], *new_body_lines, lines[method_end]]
        lines[method_start:method_end + 1] = replacement
        file_path.write_text("".join(lines), encoding="utf-8", errors="ignore")
        return True
    except Exception as exc:
        log(f"    Error replacing method content in {file_path.name}: {exc}")
        return False


def _ensure_public_entries(public_xml_path: Path, entry_type: str, names: list[str]) -> int:
    if not public_xml_path.is_file() or not names:
        return 0

    try:
        lines = public_xml_path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
        existing_names = set()
        first_idx = None
        first_id = None

        for idx, line in enumerate(lines):
            match_name = re.search(r'name="([^"]+)"', line)
            if match_name:
                existing_names.add(match_name.group(1))

            if entry_type in line and f'type="{entry_type}"' in line and first_idx is None:
                first_idx = idx
                match_id = re.search(r'id="([^"]+)"', line)
                if match_id:
                    first_id = match_id.group(1)

        if first_idx is None or first_id is None:
            return 0

        try:
            current_id = int(first_id, 16)
        except ValueError:
            return 0

        current_idx = first_idx
        while True:
            next_idx = current_idx + 1
            if next_idx >= len(lines):
                break
            next_line = lines[next_idx]
            if f'type="{entry_type}"' not in next_line:
                break
            match_next_id = re.search(r'id="([^"]+)"', next_line)
            if not match_next_id:
                break
            try:
                next_id = int(match_next_id.group(1), 16)
            except ValueError:
                break
            if next_id != current_id + 1:
                break
            current_idx = next_idx
            current_id = next_id

        insert_pos = current_idx + 1
        new_entries: list[str] = []
        next_id_value = current_id + 1
        for name in names:
            if name in existing_names:
                continue
            new_entries.append(
                f'  <public id="0x{next_id_value:08x}" type="{entry_type}" name="{name}" />\n'
            )
            next_id_value += 1

        if not new_entries:
            return 0

        lines[insert_pos:insert_pos] = new_entries
        public_xml_path.write_text("".join(lines), encoding="utf-8", errors="ignore")
        return len(new_entries)
    except Exception as exc:
        log(f"    Loi khi cap nhat public.xml ({entry_type}): {exc}")
        return 0


def _ensure_color_entry(colors_xml_path: Path, color_name: str, color_value: str) -> bool:
    if not colors_xml_path.is_file():
        return False

    try:
        lines = colors_xml_path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
        if any(f'name="{color_name}"' in line for line in lines):
            return False

        last_color_idx = -1
        for idx, line in enumerate(lines):
            if "color" in line.lower():
                last_color_idx = idx

        if last_color_idx < 0:
            return False

        lines[last_color_idx + 1:last_color_idx + 1] = [
            f'    <color name="{color_name}">{color_value}</color>\n'
        ]
        colors_xml_path.write_text("".join(lines), encoding="utf-8", errors="ignore")
        return True
    except Exception as exc:
        log(f"    Loi khi cap nhat colors.xml: {exc}")
        return False


def disable_private_chip(work_dir: Path) -> None:
    apk_src_dir = _miui_systemui_src_dir(work_dir)
    if not apk_src_dir.is_dir():
        log(f"Source directory not found: {apk_src_dir} (cannot disable private chip).")
        return

    settings_helper_source = _mezo_ui_dir() / "SettingsHelper.smali"
    settings_helper_target = apk_src_dir / "smali" / "classes4" / "android" / "preference" / "SettingsHelper.smali"
    legacy_settings_helper_target = apk_src_dir / "smali" / "classes3" / "android" / "preference" / "SettingsHelper.smali"
    privacy_controller_file = apk_src_dir / "smali" / "classes3" / "com" / "android" / "systemui" / "statusbar" / "privacy" / "MiuiPrivacyControllerImpl.smali"

    if not settings_helper_source.is_file():
        log(f"Source file not found: {settings_helper_source}")
        return

    try:
        settings_helper_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(settings_helper_source, settings_helper_target)
        log(f"    Da copy SettingsHelper.smali -> {settings_helper_target}")
        if legacy_settings_helper_target.is_file():
            legacy_settings_helper_target.unlink()
            log(f"    Removed legacy SettingsHelper.smali at {legacy_settings_helper_target}")
    except Exception as exc:
        log(f"    Error copying SettingsHelper.smali: {exc}")
        return

    inserted = _insert_after_method_registers(
        privacy_controller_file,
        r"\.method.*setStatus\(ILjava/lang/String;Landroid/os/Bundle;\)V",
        [
            '    const-string v0, "disable_privacy_chip"\n',
            "\n",
            '    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n',
            "\n",
            "    move-result v0\n",
            "\n",
            "    if-eqz v0, :cond_9999\n",
            "\n",
            "    return-void\n",
            "\n",
            "    :cond_9999\n",
        ],
        "disable_privacy_chip",
    )
    if inserted:
        log("    Patched MiuiPrivacyControllerImpl.smali")

def change_clock_format(work_dir: Path) -> None:
    apk_src_dir = _miui_systemui_src_dir(work_dir)
    if not apk_src_dir.is_dir():
        log(f"Source directory not found: {apk_src_dir} (clock format)")
        return

    settings_helper_source = _mezo_ui_dir() / "SettingsHelper.smali"
    settings_helper_target = apk_src_dir / "smali" / "classes4" / "android" / "preference" / "SettingsHelper.smali"
    legacy_settings_helper_target = apk_src_dir / "smali" / "classes3" / "android" / "preference" / "SettingsHelper.smali"
    if settings_helper_source.is_file() and not settings_helper_target.exists():
        try:
            settings_helper_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(settings_helper_source, settings_helper_target)
            log(f"    Da bo sung SettingsHelper.smali -> {settings_helper_target}")
            if legacy_settings_helper_target.is_file():
                legacy_settings_helper_target.unlink()
                log(f"    Removed legacy SettingsHelper.smali at {legacy_settings_helper_target}")
        except Exception as exc:
            log(f"    Loi khi bo sung SettingsHelper.smali: {exc}")

    date_utils_candidates = sorted(
        apk_src_dir.glob("smali/classes*/miuix/pickerwidget/date/DateUtils.smali")
    )
    if not date_utils_candidates:
        log("DateUtils.smali not found in MiuiSystemUI_apk_src.")
        return

    date_utils_path = date_utils_candidates[0]
    try:
        lines = date_utils_path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
        if "change_clock_format_t" in "".join(lines):
            log(f"    Skipping {date_utils_path.name}: patch already applied.")
            return

        method_start = -1
        move_result_indices: list[int] = []
        method_end = -1

        for idx, line in enumerate(lines):
            if method_start == -1:
                if re.search(
                    r"\.method.*formatDateTime\s*\(Landroid/content/Context;Ljava/lang/StringBuilder;J\s*I\s*Ljava/util/TimeZone;\)V",
                    line,
                ):
                    method_start = idx
                continue

            if "move-result-object v2" in line:
                move_result_indices.append(idx)

            if ".end method" in line:
                method_end = idx
                break

        if method_start == -1 or method_end == -1 or len(move_result_indices) < 2:
            log(f"    Khong patch duoc {date_utils_path.name}: khong tim thay vi tri chen.")
            return

        insert_pos = move_result_indices[1] + 1
        insert_code = [
            '    const-string v3, "change_clock_format_t"\n',
            "\n",
            '    invoke-static {v3}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n',
            "\n",
            "    move-result v3\n",
            "\n",
            "    if-eqz v3, :cond_1df\n",
            "\n",
            '    const-string v2, "hh:mm"\n',
            "\n",
            '    const-string v3, "clock_format_t"\n',
            "\n",
            '    invoke-static {v3, v2}, Landroid/preference/SettingsHelper;->getStringofSettings(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;\n',
            "\n",
            "    move-result-object v2\n",
            "\n",
            "    :cond_1df\n",
        ]
        lines[insert_pos:insert_pos] = insert_code
        date_utils_path.write_text("".join(lines), encoding="utf-8", errors="ignore")
        log(f"    Patched: {date_utils_path}")
    except Exception as exc:
        log(f"    Loi khi patch DateUtils.smali: {exc}")


def fix_recompile(work_dir: Path) -> None:
    apk_src_dir = _miui_systemui_src_dir(work_dir)
    targets = [
        apk_src_dir / "resources" / "package_1" / "res" / "values" / "styles.xml",
        apk_src_dir / "resources" / "package_1" / "res" / "values-night" / "styles.xml",
    ]

    for path in targets:
        if not path.is_file():
            log(f"    Skipping fix_recompile: path not found: {path}")
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="ignore")
            count = content.count("@style/null")
            if count == 0:
                continue
            path.write_text(content.replace("@style/null", "@null"), encoding="utf-8", errors="ignore")
            log(f"    Da thay {count} '@style/null' -> '@null' trong {path.name}")
        except Exception as exc:
            log(f"    Loi khi sua {path}: {exc}")


def icon_style(work_dir: Path) -> None:
    apk_src_dir = _miui_systemui_src_dir(work_dir)
    icon_style_source_dir = _mezo_ui_dir() / "iconStyle"
    icon_style_target_dir = apk_src_dir / "resources" / "package_1" / "res"
    public_xml_path = icon_style_target_dir / "values" / "public.xml"

    if not apk_src_dir.is_dir():
        log(f"Source directory not found: {apk_src_dir} (icon style)")
        return
    if not icon_style_source_dir.is_dir():
        log(f"iconStyle source directory not found: {icon_style_source_dir}")
        return

    copy_tasks = [
        (icon_style_source_dir / "drawable" / "battery_style.png", icon_style_target_dir / "drawable" / "battery_style.png"),
        (icon_style_source_dir / "drawable-night" / "battery_style.png", icon_style_target_dir / "drawable-night" / "battery_style.png"),
        (icon_style_source_dir / "drawable-nodpi" / "ic_signal_cellular_0_5_bar.xml", icon_style_target_dir / "drawable-nodpi" / "ic_signal_cellular_0_5_bar.xml"),
        (icon_style_source_dir / "drawable-nodpi" / "ic_signal_cellular_1_5_bar.xml", icon_style_target_dir / "drawable-nodpi" / "ic_signal_cellular_1_5_bar.xml"),
        (icon_style_source_dir / "drawable-nodpi" / "ic_signal_cellular_3_5_bar.xml", icon_style_target_dir / "drawable-nodpi" / "ic_signal_cellular_3_5_bar.xml"),
        (icon_style_source_dir / "drawable-nodpi" / "ic_signal_cellular_5_5_bar.xml", icon_style_target_dir / "drawable-nodpi" / "ic_signal_cellular_5_5_bar.xml"),
        (icon_style_source_dir / "drawable-nodpi" / "volte_style_img.xml", icon_style_target_dir / "drawable-nodpi" / "volte_style_img.xml"),
    ]

    for src, dst in copy_tasks:
        try:
            if not src.is_file():
                log(f"    Bo qua file icon style khong ton tai: {src}")
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            log(f"    Copied {src.name} -> {dst}")
        except Exception as exc:
            log(f"    Loi khi copy {src.name}: {exc}")

    added = _ensure_public_entries(
        public_xml_path,
        "drawable",
        [
            "battery_style",
            "volte_style_img",
            "ic_signal_cellular_0_5_bar",
            "ic_signal_cellular_1_5_bar",
            "ic_signal_cellular_3_5_bar",
            "ic_signal_cellular_5_5_bar",
        ],
    )
    if added:
        log(f"    Da them {added} drawable entry vao public.xml")


def pill_gesture(work_dir: Path) -> None:
    apk_src_dir = _miui_systemui_src_dir(work_dir)
    navigation_handle_dir = _mezo_ui_dir() / "NavigationHandle"
    if not apk_src_dir.is_dir():
        log(f"Source directory not found: {apk_src_dir} (pill gesture)")
        return
    if not navigation_handle_dir.is_dir():
        log(f"NavigationHandle directory not found: {navigation_handle_dir}")
        return

    copy_tasks = [
        (
            navigation_handle_dir / "MyUtils.smali",
            apk_src_dir / "smali" / "classes2" / "com" / "android" / "kevin" / "MyUtils.smali",
        ),
        (
            navigation_handle_dir / "NavigationHandle.smali",
            apk_src_dir / "smali" / "classes2" / "com" / "android" / "systemui" / "navigationbar" / "gestural" / "NavigationHandle.smali",
        ),
        (
            navigation_handle_dir / "NavigationHandle$1.smali",
            apk_src_dir / "smali" / "classes2" / "com" / "android" / "systemui" / "navigationbar" / "gestural" / "NavigationHandle$1.smali",
        ),
    ]

    for src, dst in copy_tasks:
        try:
            if not src.is_file():
                log(f"    Bo qua file pill gesture khong ton tai: {src}")
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            log(f"    Copied {src.name} -> {dst}")
        except Exception as exc:
            log(f"    Loi khi copy {src.name}: {exc}")


def clock_style(work_dir: Path) -> None:
    apk_src_dir = _miui_systemui_src_dir(work_dir)
    clock_style_dir = _mezo_ui_dir() / "clockStyle"
    if not apk_src_dir.is_dir():
        log(f"Source directory not found: {apk_src_dir} (clock style)")
        return
    if not clock_style_dir.is_dir():
        log(f"clockStyle directory not found: {clock_style_dir}")
        return

    helper_source = clock_style_dir / "helper.smali"
    helper_target = apk_src_dir / "smali" / "classes3" / "spider" / "ui" / "helper.smali"
    fragment_file = (
        apk_src_dir
        / "smali"
        / "classes3"
        / "com"
        / "android"
        / "systemui"
        / "statusbar"
        / "phone"
        / "MiuiCollapsedStatusBarFragment.smali"
    )
    public_xml_path = apk_src_dir / "resources" / "package_1" / "res" / "values" / "public.xml"
    colors_xml_path = apk_src_dir / "resources" / "package_1" / "res" / "values" / "colors.xml"

    try:
        if helper_source.is_file():
            helper_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(helper_source, helper_target)
            log(f"    Da copy helper.smali -> {helper_target}")
        else:
            log(f"    helper.smali not found: {helper_source}")
    except Exception as exc:
        log(f"    Loi khi copy helper.smali: {exc}")

    if fragment_file.is_file():
        try:
            lines = fragment_file.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
            content_str = "".join(lines)
            if "spider_clock_style" not in content_str:
                method_start = -1
                target_line_idx = -1
                method_end = -1

                for idx, line in enumerate(lines):
                    if method_start == -1:
                        if re.search(
                            r"\.method.*onCreateView\(Landroid/view/LayoutInflater;Landroid/view/ViewGroup;Landroid/os/Bundle;\)Landroid/view/View;",
                            line,
                        ):
                            method_start = idx
                        continue

                    if target_line_idx == -1 and re.search(r"const\s+(p0|v0),\s+0x7", line):
                        target_line_idx = idx

                    if ".end method" in line:
                        method_end = idx
                        break

                if method_start != -1 and target_line_idx != -1 and method_end != -1:
                    insert_code = """
    const-string/jumbo v1, "spider_clock_style"

    invoke-static {v1}, Lspider/ui/helper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    const v2, 0x0

    if-eq v1, v2, :cond_89

    const v2, 0x1

    if-eq v1, v2, :cond_8d

    const v2, 0x2

    if-eq v1, v2, :cond_91

    const v2, 0x3

    if-eq v1, v2, :cond_95

    const v2, 0x4

    if-eq v1, v2, :cond_99

    const v2, 0x5

    if-eq v1, v2, :cond_9d

    const v2, 0x6

    if-eq v1, v2, :cond_a1

    const v2, 0x7

    if-eq v1, v2, :cond_a5

    const v2, 0x8

    if-eq v1, v2, :cond_a9

    const v2, 0x9

    if-eq v1, v2, :cond_ad

    const v2, 0xa

    if-eq v1, v2, :cond_b1

    const v2, 0xb

    if-eq v1, v2, :cond_b5

    const v2, 0xc

    if-eq v1, v2, :cond_b9

    const v2, 0xd

    if-eq v1, v2, :cond_bd

    const v2, 0xe

    if-eq v1, v2, :cond_c1

    const v2, 0xf

    if-eq v1, v2, :cond_c5

    const v2, 0x10

    if-eq v1, v2, :cond_c9

    const v2, 0x11

    if-eq v1, v2, :cond_cd

    const v2, 0x12

    if-eq v1, v2, :cond_d1

    const v2, 0x13

    if-eq v1, v2, :cond_d5

    const v2, 0x14

    if-eq v1, v2, :cond_d9

    const v2, 0x15

    if-eq v1, v2, :cond_dd

    const v2, 0x16

    if-eq v1, v2, :cond_e1

    const v2, 0x17

    if-eq v1, v2, :cond_e5

    const v2, 0x18

    if-eq v1, v2, :cond_e9

    const v2, 0x19

    if-eq v1, v2, :cond_ed

    :cond_89
    const-string/jumbo v1, "layout/status_bar"

    goto :goto_f0

    :cond_8d
    const-string/jumbo v1, "layout/status_bar_1"

    goto :goto_f0

    :cond_91
    const-string/jumbo v1, "layout/status_bar_2"

    goto :goto_f0

    :cond_95
    const-string/jumbo v1, "layout/status_bar_3"

    goto :goto_f0

    :cond_99
    const-string/jumbo v1, "layout/status_bar_4"

    goto :goto_f0

    :cond_9d
    const-string/jumbo v1, "layout/status_bar_5"

    goto :goto_f0

    :cond_a1
    const-string/jumbo v1, "layout/status_bar_6"

    goto :goto_f0

    :cond_a5
    const-string/jumbo v1, "layout/status_bar_7"

    goto :goto_f0

    :cond_a9
    const-string/jumbo v1, "layout/status_bar_8"

    goto :goto_f0

    :cond_ad
    const-string/jumbo v1, "layout/status_bar_9"

    goto :goto_f0

    :cond_b1
    const-string/jumbo v1, "layout/status_bar_10"

    goto :goto_f0

    :cond_b5
    const-string/jumbo v1, "layout/status_bar_11"

    goto :goto_f0

    :cond_b9
    const-string/jumbo v1, "layout/status_bar_12"

    goto :goto_f0

    :cond_bd
    const-string/jumbo v1, "layout/status_bar_13"

    goto :goto_f0

    :cond_c1
    const-string/jumbo v1, "layout/status_bar_14"

    goto :goto_f0

    :cond_c5
    const-string/jumbo v1, "layout/status_bar_15"

    goto :goto_f0

    :cond_c9
    const-string/jumbo v1, "layout/status_bar_16"

    goto :goto_f0

    :cond_cd
    const-string/jumbo v1, "layout/status_bar_17"

    goto :goto_f0

    :cond_d1
    const-string/jumbo v1, "layout/status_bar_18"

    goto :goto_f0

    :cond_d5
    const-string/jumbo v1, "layout/status_bar_19"

    goto :goto_f0

    :cond_d9
    const-string/jumbo v1, "layout/status_bar_20"

    goto :goto_f0

    :cond_dd
    const-string/jumbo v1, "layout/status_bar_21"

    goto :goto_f0

    :cond_e1
    const-string/jumbo v1, "layout/status_bar_22"

    goto :goto_f0

    :cond_e5
    const-string/jumbo v1, "layout/status_bar_23"

    goto :goto_f0

    :cond_e9
    const-string/jumbo v1, "layout/status_bar_24"

    goto :goto_f0

    :cond_ed
    const-string/jumbo v1, "layout/status_bar_25"

    :goto_f0
    invoke-static {v1}, Lspider/ui/helper;->getIdentifier(Ljava/lang/String;)I

    move-result v0
""".splitlines(keepends=True)
                    lines[target_line_idx + 1:target_line_idx + 1] = insert_code
                    fragment_file.write_text("".join(lines), encoding="utf-8", errors="ignore")
                    log(f"    Da patch {fragment_file.name}")
                else:
                    log(f"    Khong patch duoc {fragment_file.name}: khong tim thay vi tri chen.")
            else:
                log(f"    Bo qua {fragment_file.name}: patch da ton tai.")
        except Exception as exc:
            log(f"    Loi khi patch {fragment_file.name}: {exc}")
    else:
        log(f"    Khong tim thay file: {fragment_file}")

    drawable_source_dir = clock_style_dir / "drawable"
    drawable_target_dir = apk_src_dir / "resources" / "package_1" / "res" / "drawable"
    layout_source_dir = clock_style_dir / "layout"
    layout_target_dir = apk_src_dir / "resources" / "package_1" / "res" / "layout"
    drawable_files: list[str] = []
    layout_files: list[str] = []

    if drawable_source_dir.is_dir():
        for file_path in sorted(drawable_source_dir.iterdir()):
            if not file_path.is_file():
                continue
            try:
                drawable_target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, drawable_target_dir / file_path.name)
                drawable_files.append(file_path.stem)
                log(f"    Copied drawable: {file_path.name}")
            except Exception as exc:
                log(f"    Loi khi copy drawable {file_path.name}: {exc}")

    if layout_source_dir.is_dir():
        for file_path in sorted(layout_source_dir.iterdir()):
            if not file_path.is_file():
                continue
            try:
                layout_target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file_path, layout_target_dir / file_path.name)
                layout_files.append(file_path.stem)
                log(f"    Copied layout: {file_path.name}")
            except Exception as exc:
                log(f"    Loi khi copy layout {file_path.name}: {exc}")

    added_drawables = _ensure_public_entries(public_xml_path, "drawable", drawable_files)
    if added_drawables:
        log(f"    Da them {added_drawables} drawable cho clock style vao public.xml")

    added_layouts = _ensure_public_entries(public_xml_path, "layout", layout_files)
    if added_layouts:
        log(f"    Da them {added_layouts} layout cho clock style vao public.xml")

    color_added = _ensure_color_entry(colors_xml_path, "statusbar_back_clock", "#fffbfaf7")
    if color_added:
        log("    Da them mau statusbar_back_clock vao colors.xml")

    added_colors = _ensure_public_entries(public_xml_path, "color", ["statusbar_back_clock"])
    if added_colors:
        log("    Da them statusbar_back_clock vao public.xml")


def fix_earlier_notification(work_dir: Path) -> None:
    apk_src_dir = _miui_systemui_src_dir(work_dir)
    if not apk_src_dir.is_dir():
        log(f"Source directory not found: {apk_src_dir} (earlier notification fix)")
        return

    fold_coordinator_file = (
        apk_src_dir
        / "smali"
        / "classes3"
        / "com"
        / "android"
        / "systemui"
        / "statusbar"
        / "notification"
        / "collection"
        / "coordinator"
        / "FoldCoordinator.smali"
    )
    miui_base_notif_util_file = (
        apk_src_dir
        / "smali"
        / "classes3"
        / "com"
        / "miui"
        / "systemui"
        / "notification"
        / "MiuiBaseNotifUtil.smali"
    )

    fold_coordinator_ok = _replace_method_body(
        fold_coordinator_file,
        r"\.method\s+public\s+final\s+attach\b",
        [
            "\n",
            "    .registers 2\n",
            "\n",
            "    return-void\n",
            "\n",
        ],
    )
    if fold_coordinator_ok:
        log("    Da patch FoldCoordinator.attach")

    miui_base_notif_ok = _replace_method_body(
        miui_base_notif_util_file,
        r"\.method\s+public\s+static\s+shouldSuppressFold\(\)Z",
        [
            "\n",
            "    .registers 1\n",
            "\n",
            "    const/4 v0, 0x1\n",
            "\n",
            "    return v0\n",
            "\n",
        ],
    )
    if miui_base_notif_ok:
        log("    Da patch MiuiBaseNotifUtil.shouldSuppressFold()Z")

def apply_miui_systemui_mods_android15(work_dir: Path) -> None:
    log("Applying MiuiSystemUI mod for Android 15...")
    disable_private_chip(work_dir)
    #change_clock_format(work_dir)
    fix_earlier_notification(work_dir)
    #fix_recompile(work_dir)
    #icon_style(work_dir)
    #pill_gesture(work_dir)
    #clock_style(work_dir)
    log("MiuiSystemUI mod complete for Android 15.")

def apply_miui_systemui_mods_android16(work_dir: Path) -> None:
    log("Applying MiuiSystemUI mod for Android 16...")
    disable_private_chip(work_dir)
    #change_clock_format(work_dir)
    fix_earlier_notification(work_dir)
    #fix_recompile(work_dir)
    #icon_style(work_dir)
    #pill_gesture(work_dir)
    #clock_style(work_dir)
    log("MiuiSystemUI mod complete for Android 16.")


def fix_specific_smali_file(smali_file: Path) -> bool:
    """Fix a specific smali file by replacing methods containing invoke-custom"""
    try:
        # Read the file
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
        log(f"    ❌ Loi khi xu ly {smali_file.name}: {e}")
        return False


def fix_bootloop_a15(work_dir: Path) -> None:
    """Fix bootloop for A15 devices by handling invoke-custom methods in specific files"""
    log("\n🔧 Processing bootloop fix (a15)...")
    log("📝 Tim kiem va sua cac method chua 'invoke-custom' trong cac file cu the...")
    
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
            log(f"❌ Thu muc {directory} khong ton tai")
            continue
        
        log(f"\n📁 Processing directory: {directory}")
        log(f"📄 Tim thay {len(files)} file can xu ly")
        
        for file_path in files:
            # Convert forward slashes to proper path separators for the current OS
            file_path_parts = file_path.split('/')
            full_file_path = dir_path.joinpath(*file_path_parts)
            
            if not full_file_path.exists():
                log(f"  ⚠️  File {file_path} khong ton tai tai: {full_file_path}")
                continue
            
            log(f"  🔍 Processing: {file_path}")
            if fix_specific_smali_file(full_file_path):
                total_files_processed += 1
                log(f"    ✅ Da sua thanh cong")
            else:
                log(f"    ℹ️  Khong co method nao can sua")
    
    log(f"\n🎉 Bootloop fix complete!")
    log(f"📊 Tong so file da xu ly: {total_files_processed}")


def disable_signature_verification_a14_15(work_dir: Path) -> None:
    """Disable Signature Verification by modifying various framework and service files"""
    import re
    
    log("\n🔏 Đang xử lý Disable Signature Verification (smali-only)...")
    
    def p(*a): log(" ".join(str(x) for x in a))
    def overwrite(path: Path, text: str) -> None:
        path.write_text(text, encoding="utf-8")
    
    # ---- Tiện ích tìm file đầu tiên theo tên trong 1 root ----
    def find_one(root: Path, filename: str) -> Path | None:
        for pth in root.rglob(filename):
            return pth
        return None
    
    # ---- Các patch cụ thể ----
    def patch_packageparser(smali_root: Path) -> None:
        # PackageParser.smali
        tgt = find_one(smali_root, "PackageParser.smali")
        if not tgt:
            p(f"  ⚠️ Không thấy PackageParser.smali trong {smali_root}")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_collect, in_common, changed = [], False, False, 0
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "collectCertificates(" in s and s.endswith("Z)V"):
                in_collect = True
            elif in_collect and s.startswith(".end method"):
                in_collect = False
            if in_collect and "if-eqz p2" in s:
                out.append("    const/4 p2, 0x1\n"); changed += 1
            if s.startswith(".method") and "parseBaseApkCommon(" in s:
                in_common = True
            elif in_common and s.startswith(".end method"):
                in_common = False
            if in_common and "if-nez v5" in s:
                out.append("    const/4 v5, 0x1\n"); changed += 1
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ PackageParser.smali patched:", changed, "spot(s)")
        else:
            p("  ℹ️ PackageParser.smali không cần thay đổi")
        # PackageParser$PackageParserException.smali
        tgt2 = find_one(smali_root, "PackageParser$PackageParserException.smali")
        if tgt2:
            lines = tgt2.read_text(encoding="utf-8").splitlines(True)
            out, changed2 = [], 0
            for line in lines:
                out.append(line)
                if "iput p1, p0, Landroid/content/pm/PackageParser$PackageParserException;->error:I" in line:
                    out.append("    const/4 p1, 0x0\n")
                    changed2 += 1
            if changed2:
                overwrite(tgt2, "".join(out))
                p("  ✅ PackageParser$PackageParserException.smali patched")
        # SigningDetails*.smali
        for fn in ("PackageParser$SigningDetails.smali", "SigningDetails.smali"):
            tgt3 = find_one(smali_root, fn)
            if not tgt3:
                continue
            txt = tgt3.read_text(encoding="utf-8")
            orig = txt
            txt = re.sub(
                r"(\.method[^\n]*checkCapability[^\n]*\n)(.*?)(\.end method)",
                r"\1    .registers 3\n    const/4 p0, 0x1\n    return p0\n\3",
                txt, flags=re.DOTALL
            )
            txt = re.sub(
                r"(\.method[^\n]*hasAncestorOrSelf[^\n]*\n)(.*?)(\.end method)",
                r"\1    .registers 2\n    const/4 p0, 0x1\n    return p0\n\3",
                txt, flags=re.DOTALL
            )
            if txt != orig:
                overwrite(tgt3, txt)
                p(f"  ✅ {fn} patched (capability/ancestor -> true)")
    
    def patch_v2_verifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureSchemeV2Verifier.smali")
        if not tgt: 
            p("  ⚠️ Không thấy ApkSignatureSchemeV2Verifier.smali"); 
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, idxs = [], False, []
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "verifySigner(Ljava/nio/ByteBuffer;Ljava/util/Map;Ljava/security/cert/CertificateFactory;)" in s:
                in_m = True
            elif in_m and s.startswith(".end method"):
                in_m = False
            if in_m and s == "move-result v0":
                idxs.append(len(out))
            out.append(line)
        if idxs:
            out[idxs[-1]] = "    const/4 v0, 0x1\n"
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureSchemeV2Verifier.smali patched (v0=1)")
    
    def patch_v3_verifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureSchemeV3Verifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureSchemeV3Verifier.smali"); 
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "verifySigner(Ljava/nio/ByteBuffer;Ljava/util/Map;Ljava/security/cert/CertificateFactory;)" in s:
                in_m = True
            elif in_m and s.startswith(".end method"):
                in_m = False
            if in_m and s == "move-result v0":
                # nhìn dòng ngay trên trong out
                k = len(out) - 1
                while k >= 0 and out[k].strip() == "":
                    k -= 1
                if k >= 0 and out[k].strip() == "invoke-static {v12, v6}, Ljava/security/MessageDigest;->isEqual([B[B)Z":
                    out.append("    const/4 v0, 0x1\n")
                    changed = True
                    continue
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureSchemeV3Verifier.smali patched (v0=1 sau isEqual)")
    
    def patch_apksignatureverifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureVerifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureVerifier.smali"); 
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "getMinimumSignatureSchemeVersionForTargetSdk" in s:
                in_m = True
                out.append(line)
                out.append("    .registers 1\n")
                out.append("    const/4 v0, 0x0\n")
                out.append("    return v0\n")
                changed = True
                continue
            elif in_m and s.startswith(".end method"):
                out.append(line); in_m = False; continue
            elif in_m:
                # bỏ thân cũ
                continue
            if "invoke-static {p0, p1, p3}, Landroid/util/apk/ApkSignatureVerifier;->verifyV1Signature(" in s:
                out.append("    const p3, 0x0\n")  # disable strict V1 fallback flag
                changed = True
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureVerifier.smali patched (minScheme=0, p3=0)")
    
    def patch_apksigningblockutils(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSigningBlockUtils.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSigningBlockUtils.smali"); 
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "verifyIntegrityFor1MbChunkBasedAlgorithm" in s:
                in_m = True
            elif in_m and s.startswith(".end method"):
                in_m = False
            if in_m and s == "move-result v7":
                out.append("    const/4 v7, 0x1\n"); changed = True; continue
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSigningBlockUtils.smali patched (v7=1)")
    
    def patch_strictjar(smali_root: Path) -> None:
        # StrictJarVerifier.smali -> verifyMessageDigest always true
        v = find_one(smali_root, "StrictJarVerifier.smali")
        if v:
            lines = v.read_text(encoding="utf-8").splitlines(True)
            out, in_m, changed = [], False, False
            for line in lines:
                s = line.strip()
                if s.startswith(".method") and "verifyMessageDigest" in s:
                    in_m = True
                    out.append(line)
                    out.append("    .registers 2\n")
                    out.append("    const/4 v0, 0x1\n")
                    out.append("    return v0\n")
                    changed = True
                    continue
                if in_m and s.startswith(".end method"):
                    out.append(line); in_m = False; continue
                if in_m:  # skip old body
                    continue
                out.append(line)
            if changed:
                overwrite(v, "".join(out))
                p("  ✅ StrictJarVerifier.smali patched (verifyMessageDigest -> true)")
        # StrictJarFile.smali: loại nhánh fail trong <init>(..., ZZ)V
        f = find_one(smali_root, "StrictJarFile.smali")
        if f:
            lines = f.read_text(encoding="utf-8").splitlines(True)
            out, in_m = [], False
            for line in lines:
                s = line.strip()
                if s.startswith(".method") and "<init>(Ljava/lang/String;Ljava/io/FileDescriptor;ZZ)V" in s:
                    in_m = True
                elif in_m and s.startswith(".end method"):
                    in_m = False
                if in_m and (s == "if-eqz v6, :cond_56" or s == ":cond_56"):
                    continue
                out.append(line)
            overwrite(f, "".join(out))
            p("  ✅ StrictJarFile.smali patched (<init> drop fail branch)")
    
    def patch_services(smali_root: Path) -> None:
        # PackageManagerServiceUtils.smali -> checkDowngrade() return-void
        f1 = find_one(smali_root, "PackageManagerServiceUtils.smali")
        if f1:
            lines = f1.read_text(encoding="utf-8").splitlines(True)
            out, in_m, changed = [], False, False
            for ln in lines:
                s = ln.strip()
                if s.startswith(".method") and "checkDowngrade" in s:
                    in_m = True; out.append(ln)
                    out.append("    .locals 0\n    return-void\n"); changed = True; continue
                if in_m and s.startswith(".end method"):
                    out.append(ln); in_m = False; continue
                if in_m:  # skip body
                    continue
                out.append(ln)
            if changed: overwrite(f1, "".join(out)); p("  ✅ PackageManagerServiceUtils.checkDowngrade() -> return-void")
        # KeySetManagerService.smali -> shouldCheckUpgradeKeySetLocked() -> 0
        f2 = find_one(smali_root, "KeySetManagerService.smali")
        if f2:
            lines = f2.read_text(encoding="utf-8").splitlines(True)
            out, in_m, changed = [], False, False
            for ln in lines:
                s = ln.strip()
                if s.startswith(".method") and "shouldCheckUpgradeKeySetLocked" in s:
                    in_m = True; out.append(ln)
                    out.append("    .locals 1\n    const/4 v0, 0x0\n    return v0\n"); changed = True; continue
                if in_m and s.startswith(".end method"):
                    out.append(ln); in_m = False; continue
                if in_m: continue
                out.append(ln)
            if changed: overwrite(f2, "".join(out)); p("  ✅ KeySetManagerService.shouldCheckUpgradeKeySetLocked() -> false")
        # InstallPackageHelper.smali: ép v12=1 trước isLeavingSharedUser()
        f3 = find_one(smali_root, "InstallPackageHelper.smali")
        if f3:
            lines = f3.read_text(encoding="utf-8").splitlines(True)
            out, changed = [], 0
            i = 0
            while i < len(lines):
                ln = lines[i]; s = ln.strip()
                if "if-eqz v12" in s:
                    j = i + 1
                    while j < len(lines) and lines[j].strip() == "":
                        j += 1
                    if j < len(lines) and lines[j].strip() == "invoke-interface {v7}, Lcom/android/server/pm/pkg/AndroidPackage;->isLeavingSharedUser()Z":
                        out.append("    const/4 v12, 0x1\n"); changed += 1
                out.append(ln); i += 1
            if changed:
                overwrite(f3, "".join(out)); p("  ✅ InstallPackageHelper: force v12=1 trước isLeavingSharedUser()")
        # ReconcilePackageUtils.smali: flip đầu tiên const/4 v0, 0x0 -> 0x1
        f4 = find_one(smali_root, "ReconcilePackageUtils.smali")
        if f4:
            txt = f4.read_text(encoding="utf-8")
            new = txt.replace("const/4 v0, 0x0", "const/4 v0, 0x1", 1)
            if new != txt:
                overwrite(f4, new); p("  ✅ ReconcilePackageUtils: v0 -> 1 (flip đầu tiên)")
    
    def patch_miui_pms_impl(smali_root: Path) -> None:
        f = find_one(smali_root, "PackageManagerServiceImpl.smali")
        if not f:
            p("  ⚠️ Không thấy PackageManagerServiceImpl.smali (miui)")
            return
        lines = f.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        current = ""
        for ln in lines:
            s = ln.strip()
            if s.startswith(".method") and "verifyIsolationViolation" in s:
                in_m = True; current = "vii"; out.append(ln)
                out.append("    .registers 3\n    return-void\n"); changed = True; continue
            if s.startswith(".method") and "canBeUpdate(" in s:
                in_m = True; current = "cbu"; out.append(ln)
                out.append("    .registers 2\n    return-void\n"); changed = True; continue
            if in_m and s.startswith(".end method"):
                out.append(ln); in_m = False; current = ""; continue
            if in_m: continue
            out.append(ln)
        if changed:
            overwrite(f, "".join(out))
            p("  ✅ PackageManagerServiceImpl.smali (miui) patched (2 method -> return-void)")
    
    # ---- Thư mục smali tương ứng trong dự án của bạn (đã có từ logic unpack hiện có) ----
    fw = work_dir / "framework_unpacked"
    sv = work_dir / "services_unpacked"
    mi = work_dir / "miui_services_unpacked"
    
    # framework classesN
    fw_smali = [
        fw / "smali_classes",   # classes.dex
        fw / "smali_classes4",  # classes4.dex
        fw / "smali_classes5",  # classes5.dex
    ]
    # services classes2
    sv_smali = [sv / "smali_classes2", sv / "smali_classes", sv / "smali_classes3"]
    # miui services
    mi_smali = [mi / "smali_classes"]
    
    # ---- Thực thi patch ----
    # 1) framework/smali_classes (PackageParser* + SigningDetails*)
    p("\n📁 Patching framework_unpacked/smali_classes ...")
    if fw_smali[0].exists():
        patch_packageparser(fw_smali[0])
    else:
        p("  ⚠️ Thiếu thư mục:", fw_smali[0])
    
    # 2) framework/smali_classes4 (ApkSignature*Verifier, ApkSigningBlockUtils, StrictJar*)
    p("\n📁 Patching framework_unpacked/smali_classes4 ...")
    if fw_smali[1].exists():
        patch_v2_verifier(fw_smali[1])
        patch_v3_verifier(fw_smali[1])
        patch_apksignatureverifier(fw_smali[1])
        patch_apksigningblockutils(fw_smali[1])
        patch_strictjar(fw_smali[1])
    else:
        p("  ⚠️ Thiếu thư mục:", fw_smali[1])
    
    # 3) framework/smali_classes5 (tuỳ ROM — thường không cần ở bước disable sig)
    if fw_smali[2].exists():
        p("\n📁 Kiểm tra framework_unpacked/smali_classes5 (nếu có file liên quan)...")
        # để trống — giữ chỗ nếu sau cần bổ sung
    else:
        p("  ℹ️ Bỏ qua smali_classes5 (không có)")
    
    # 4) services_unpacked/smali_classes2 (+ smali_classes, smali_classes3)
    p("\n📁 Patching services_unpacked ...")
    any_sv = False
    for d in sv_smali:
        if d.exists():
            patch_services(d); any_sv = True
    if not any_sv:
        p("  ⚠️ Thiếu toàn bộ thư mục smali trong services_unpacked")
    
    # 5) miui_services_unpacked/smali_classes
    p("\n📁 Patching miui_services_unpacked/smali_classes ...")
    if mi_smali[0].exists():
        patch_miui_pms_impl(mi_smali[0])
    else:
        p("  ⚠️ Thiếu thư mục:", mi_smali[0])
    
    log("\n🎉 Hoàn tất Disable Signature Verification (smali-only).")


def disable_signature_verification_a16(work_dir: Path) -> None:
    """Disable Signature Verification (Android 16 / a16.py logic): smali-only patches."""
    import re

    log("\n🔏 Đang xử lý Disable Signature Verification A16 (smali-only)...")

    def p(*a):
        log(" ".join(str(x) for x in a))

    def overwrite(path: Path, text: str) -> None:
        path.write_text(text, encoding="utf-8")

    def find_one(root: Path, filename: str) -> Path | None:
        for pth in root.rglob(filename):
            return pth
        return None

    def patch_packageparser(smali_root: Path) -> None:
        tgt = find_one(smali_root, "PackageParser.smali")
        if not tgt:
            p(f"  ⚠️ Không thấy PackageParser.smali trong {smali_root}")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_collect, in_common, changed = [], False, False, 0
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "collectCertificates(" in s and s.endswith("Z)V"):
                in_collect = True
            elif in_collect and s.startswith(".end method"):
                in_collect = False
            if in_collect and "if-eqz p2" in s:
                out.append("    const/4 v1, 0x1\n")
                changed += 1
            if s.startswith(".method") and "parseBaseApkCommon(" in s:
                in_common = True
            elif in_common and s.startswith(".end method"):
                in_common = False
            if in_common and "if-nez v14" in s:
                out.append("    const/4 v14, 0x1\n")
                changed += 1
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ PackageParser.smali patched")
        else:
            p("  ℹ️ PackageParser.smali không cần thay đổi")
        tgt2 = find_one(smali_root, "PackageParser$PackageParserException.smali")
        if tgt2:
            lines = tgt2.read_text(encoding="utf-8").splitlines(True)
            out, changed2 = [], 0
            for line in lines:
                out.append(line)
                if "iput p1, p0, Landroid/content/pm/PackageParser$PackageParserException;->error:I" in line:
                    out.append("    const/4 p1, 0x0\n")
                    changed2 += 1
            if changed2:
                overwrite(tgt2, "".join(out))
                p("  ✅ PackageParser$PackageParserException.smali patched")
        for fn in ("PackageParser$SigningDetails.smali", "SigningDetails.smali"):
            tgt3 = find_one(smali_root, fn)
            if not tgt3:
                continue
            txt = tgt3.read_text(encoding="utf-8")
            orig = txt
            txt = re.sub(
                r"(\.method[^\n]*checkCapability[^\n]*\n)(.*?)(\.end method)",
                r"\1    .registers 3\n    const/4 p0, 0x1\n    return p0\n\3",
                txt,
                flags=re.DOTALL,
            )
            txt = re.sub(
                r"(\.method[^\n]*hasAncestorOrSelf[^\n]*\n)(.*?)(\.end method)",
                r"\1    .registers 2\n    const/4 p0, 0x1\n    return p0\n\3",
                txt,
                flags=re.DOTALL,
            )
            if txt != orig:
                overwrite(tgt3, txt)
                p(f"  ✅ {fn} patched")

    def patch_v2_verifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureSchemeV2Verifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureSchemeV2Verifier.smali")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, idxs = [], False, []
        for line in lines:
            s = line.strip()
            if (
                s.startswith(".method")
                and "verifySigner(Ljava/nio/ByteBuffer;Ljava/util/Map;Ljava/security/cert/CertificateFactory;)" in s
            ):
                in_m = True
            elif in_m and s.startswith(".end method"):
                in_m = False
            if in_m and s == "move-result v0":
                idxs.append(len(out))
            out.append(line)
        if idxs:
            out[idxs[-1]] = "    const/4 v0, 0x1\n"
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureSchemeV2Verifier.smali patched")

    def patch_v3_verifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureSchemeV3Verifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureSchemeV3Verifier.smali")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if (
                s.startswith(".method")
                and "verifySigner(Ljava/nio/ByteBuffer;Ljava/util/Map;Ljava/security/cert/CertificateFactory;)" in s
            ):
                in_m = True
            elif in_m and s.startswith(".end method"):
                in_m = False
            if in_m and s == "move-result v0":
                k = len(out) - 1
                while k >= 0 and out[k].strip() == "":
                    k -= 1
                if (
                    k >= 0
                    and out[k].strip()
                    == "invoke-static {v9, v3}, Ljava/security/MessageDigest;->isEqual([B[B)Z"
                ):
                    out.append("    const/4 v0, 0x1\n")
                    changed = True
                    continue
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureSchemeV3Verifier.smali patched")

    def patch_apksignatureverifier(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSignatureVerifier.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSignatureVerifier.smali")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "getMinimumSignatureSchemeVersionForTargetSdk" in s:
                in_m = True
                out.append(line)
                out.append("    .registers 1\n")
                out.append("    const/4 v0, 0x0\n")
                out.append("    return v0\n")
                changed = True
                continue
            elif in_m and s.startswith(".end method"):
                out.append(line)
                in_m = False
                continue
            elif in_m:
                continue
            if "invoke-static {p0, p1, p3}, Landroid/util/apk/ApkSignatureVerifier;->verifyV1Signature(" in s:
                out.append("    const p3, 0x0\n")
                changed = True
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSignatureVerifier.smali patched")

    def patch_apksigningblockutils(smali_root: Path) -> None:
        tgt = find_one(smali_root, "ApkSigningBlockUtils.smali")
        if not tgt:
            p("  ⚠️ Không thấy ApkSigningBlockUtils.smali")
            return
        lines = tgt.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for line in lines:
            s = line.strip()
            if s.startswith(".method") and "verifyIntegrityFor1MbChunkBasedAlgorithm" in s:
                in_m = True
            elif in_m and s.startswith(".end method"):
                in_m = False
            if in_m and s == "move-result v7":
                out.append("    const/4 v7, 0x1\n")
                changed = True
                continue
            out.append(line)
        if changed:
            overwrite(tgt, "".join(out))
            p("  ✅ ApkSigningBlockUtils.smali patched")

    def patch_strictjar(smali_root: Path) -> None:
        # a16.py typo: StrictJarVerifier.smlali — dùng đúng tên file .smali
        v = find_one(smali_root, "StrictJarVerifier.smali")
        if v:
            lines = v.read_text(encoding="utf-8").splitlines(True)
            out, in_m, changed = [], False, False
            for line in lines:
                s = line.strip()
                if s.startswith(".method") and "verifyMessageDigest" in s:
                    in_m = True
                    out.append(line)
                    out.append("    .registers 2\n")
                    out.append("    const/4 v0, 0x1\n")
                    out.append("    return v0\n")
                    changed = True
                    continue
                if in_m and s.startswith(".end method"):
                    out.append(line)
                    in_m = False
                    continue
                if in_m:
                    continue
                out.append(line)
            if changed:
                overwrite(v, "".join(out))
                p("  ✅ StrictJarVerifier.smali patched")
        f = find_one(smali_root, "StrictJarFile.smali")
        if f:
            lines = f.read_text(encoding="utf-8").splitlines(True)
            out, in_m = [], False
            for line in lines:
                s = line.strip()
                if s.startswith(".method") and "<init>(Ljava/lang/String;Ljava/io/FileDescriptor;ZZ)V" in s:
                    in_m = True
                elif in_m and s.startswith(".end method"):
                    in_m = False
                if in_m and (s == "if-eqz v6, :cond_56" or s == ":cond_56"):
                    continue
                out.append(line)
            overwrite(f, "".join(out))
            p("  ✅ StrictJarFile.smali patched")

        parsing_file = find_one(smali_root, "ParsingPackageUtils.smali")
        if parsing_file:
            lines = parsing_file.read_text(encoding="utf-8").splitlines(True)
            out, in_method, in_parseSharedUser, found_if_eqz, changed = [], False, False, False, False
            for line in lines:
                s = line.strip()
                if s.startswith(".method") and "parseSharedUser" in s:
                    in_method = True
                    in_parseSharedUser = True
                    out.append(line)
                    continue
                if in_method and s.startswith(".end method"):
                    in_method = False
                    in_parseSharedUser = False
                    found_if_eqz = False
                    out.append(line)
                    continue
                if in_parseSharedUser and s == "if-eqz v4" and not found_if_eqz:
                    found_if_eqz = True
                    changed = True
                    out.append("    const/4 v4, 0x0\n")
                    out.append(line)
                    continue
                out.append(line)
            if changed:
                overwrite(parsing_file, "".join(out))
                p("  ✅ ParsingPackageUtils.smali patched")

    def patch_services(smali_root: Path) -> None:
        f1 = find_one(smali_root, "PackageManagerServiceUtils.smali")
        if f1:
            lines = f1.read_text(encoding="utf-8").splitlines(True)
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
                    out.append(ln)
                    in_m = False
                    continue
                if in_m:
                    continue
                out.append(ln)
            if changed:
                overwrite(f1, "".join(out))
                p("  ✅ PackageManagerServiceUtils.smali patched")
        f2 = find_one(smali_root, "KeySetManagerService.smali")
        if f2:
            lines = f2.read_text(encoding="utf-8").splitlines(True)
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
                    out.append(ln)
                    in_m = False
                    continue
                if in_m:
                    continue
                out.append(ln)
            if changed:
                overwrite(f2, "".join(out))
                p("  ✅ KeySetManagerService.smali patched")
        f3 = find_one(smali_root, "InstallPackageHelper.smali")
        if f3:
            lines = f3.read_text(encoding="utf-8").splitlines(True)
            out, changed = [], 0
            i = 0
            while i < len(lines):
                ln = lines[i]
                s = ln.strip()
                if "if-eqz v12" in s:
                    j = i + 1
                    while j < len(lines) and lines[j].strip() == "":
                        j += 1
                    if (
                        j < len(lines)
                        and lines[j].strip()
                        == "invoke-interface {p1}, Lcom/android/server/pm/pkg/AndroidPackage;->isLeavingSharedUser()Z"
                    ):
                        out.append("    const/4 v0, 0x1\n")
                        changed += 1
                out.append(ln)
                i += 1
            if changed:
                overwrite(f3, "".join(out))
                p("  ✅ InstallPackageHelper")
        f4 = find_one(smali_root, "ReconcilePackageUtils.smali")
        if f4:
            txt = f4.read_text(encoding="utf-8")
            new = txt.replace("const/4 v0, 0x0", "const/4 v0, 0x1", 1)
            if new != txt:
                overwrite(f4, new)
                p("  ✅ ReconcilePackageUtils.smali patched")

    def patch_miui_pms_impl(smali_root: Path) -> None:
        f = find_one(smali_root, "PackageManagerServiceImpl.smali")
        if not f:
            p("  ⚠️ Không thấy PackageManagerServiceImpl.smali (miui)")
            return
        lines = f.read_text(encoding="utf-8").splitlines(True)
        out, in_m, changed = [], False, False
        for ln in lines:
            s = ln.strip()
            if s.startswith(".method") and "verifyIsolationViolation" in s:
                in_m = True
                out.append(ln)
                out.append("    .registers 3\n    return-void\n")
                changed = True
                continue
            if s.startswith(".method") and "canBeUpdate(" in s:
                in_m = True
                out.append(ln)
                out.append("    .registers 2\n    return-void\n")
                changed = True
                continue
            if in_m and s.startswith(".end method"):
                out.append(ln)
                in_m = False
                continue
            if in_m:
                continue
            out.append(ln)
        if changed:
            overwrite(f, "".join(out))
            p("  ✅ PackageManagerServiceImpl.smali patched")

    fw = work_dir / "framework_unpacked"
    sv = work_dir / "services_unpacked"
    mi = work_dir / "miui_services_unpacked"

    fw_smali = [
        fw / "smali_classes",
        fw / "smali_classes4",
        fw / "smali_classes5",
    ]
    sv_smali = [sv / "smali_classes2", sv / "smali_classes", sv / "smali_classes3"]
    mi_smali = [mi / "smali_classes"]

    p("\n📁 Patching framework_unpacked/smali_classes ...")
    if fw_smali[0].exists():
        patch_packageparser(fw_smali[0])
    else:
        p("  ⚠️ Thiếu thư mục:", fw_smali[0])

    p("\n📁 Patching framework_unpacked/smali_classes4 ...")
    if fw_smali[1].exists():
        patch_v2_verifier(fw_smali[1])
        patch_v3_verifier(fw_smali[1])
        patch_apksignatureverifier(fw_smali[1])
        patch_apksigningblockutils(fw_smali[1])
        patch_strictjar(fw_smali[1])
    else:
        p("  ⚠️ Thiếu thư mục:", fw_smali[1])

    if fw_smali[2].exists():
        p("\n📁 Kiểm tra framework_unpacked/smali_classes5 (nếu có file liên quan)...")
    else:
        p("  ℹ️ Bỏ qua smali_classes5 (không có)")

    p("\n📁 Patching services_unpacked ...")
    any_sv = False
    for d in sv_smali:
        if d.exists():
            patch_services(d)
            any_sv = True
    if not any_sv:
        p("  ⚠️ Thiếu toàn bộ thư mục smali trong services_unpacked")

    p("\n📁 Patching miui_services_unpacked/smali_classes ...")
    if mi_smali[0].exists():
        patch_miui_pms_impl(mi_smali[0])
    else:
        p("  ⚠️ Thiếu thư mục:", mi_smali[0])

    log("\n🎉 Hoàn tất Disable Signature Verification A16 (smali-only).")


def copy_settings_helper(work_dir: Path) -> bool:
    """Copy SettingsHelper.smali from MEZO to framework_unpacked/smali_classes3/android/preference"""
    try:
        source_path = ROOT_DIR / "MEZO" / "SettingsHelper.smali"
        target_dir = work_dir / "framework_unpacked" / "smali_classes3" / "android" / "preference"
        target_path = target_dir / "SettingsHelper.smali"
        
        if not source_path.exists():
            log(f"    ❌ File nguon {source_path} khong ton tai")
            return False
        
        # Create target directory if it doesn't exist
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy the file
        shutil.copy2(source_path, target_path)
        return True
        
    except Exception as e:
        log(f"    ❌ Loi khi copy file: {e}")
        return False


def modify_window_manager_service_impl(file_path: Path) -> bool:
    """Modify WindowManagerServiceImpl.smali to add flag secure check"""
    try:
        with file_path.open('r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        new_lines = []
        in_method = False
        method_found = False
        has_param = False
        code_added = False
        
        # Đầu tiên, kiểm tra xem method có .param không
        for line in lines:
            if line.strip().startswith('.method public notAllowCaptureDisplay(Lcom/android/server/wm/RootWindowContainer;I)Z'):
                # Tìm method end để xác định phạm vi
                method_start = lines.index(line)
                method_end = len(lines)
                for j in range(method_start + 1, len(lines)):
                    if lines[j].strip().startswith('.end method'):
                        method_end = j
                        break
                
                # Kiểm tra có .param trong method không
                for j in range(method_start, method_end):
                    if lines[j].strip().startswith('.param'):
                        has_param = True
                        break
                break
        
        # Bây giờ xử lý từng dòng
        for line in lines:
            if line.strip().startswith('.method public notAllowCaptureDisplay(Lcom/android/server/wm/RootWindowContainer;I)Z'):
                in_method = True
                method_found = True
                new_lines.append(line)
                continue
            elif in_method and line.strip().startswith('.end method'):
                in_method = False
                new_lines.append(line)
                continue
            elif in_method:
                new_lines.append(line)
                # Nếu có .param, thêm code sau .param
                if line.strip().startswith('.param') and has_param and not code_added:
                    code_added = True
                    # Thêm code disable flag secure sau dòng .param
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure_a14_15"\n')
                    new_lines.append('    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n')
                    new_lines.append('    move-result v0\n')
                    new_lines.append('    if-eqz v0, :cond_984\n')
                    new_lines.append('    const/4 v0, 0x0\n')
                    new_lines.append('    return v0\n')
                    new_lines.append('    :cond_984\n')
                    continue
                # Nếu không có .param, thêm code sau .registers
                elif line.strip().startswith('.registers') and not has_param and not code_added:
                    code_added = True
                    # Thêm code disable flag secure sau dòng .registers
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure_a14_15"\n')
                    new_lines.append('    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n')
                    new_lines.append('    move-result v0\n')
                    new_lines.append('    if-eqz v0, :cond_984\n')
                    new_lines.append('    const/4 v0, 0x0\n')
                    new_lines.append('    return v0\n')
                    new_lines.append('    :cond_984\n')
                    continue
            else:
                new_lines.append(line)
        
        file_path.write_text("".join(new_lines), encoding='utf-8')
        
        return True
        
    except Exception as e:
        log(f"    ❌ Loi khi sua {file_path.name}: {e}")
        return False


def modify_device_policy_cache_impl(file_path: Path) -> bool:
    """Modify DevicePolicyCacheImpl.smali to add flag secure check"""
    try:
        with file_path.open('r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        new_lines = []
        in_method = False
        method_found = False
        has_param = False
        code_added = False
        
        # Đầu tiên, kiểm tra xem method có .param không
        for line in lines:
            if 'isScreenCaptureAllowed(I)Z' in line:
                # Tìm method end để xác định phạm vi
                method_start = lines.index(line)
                method_end = len(lines)
                for j in range(method_start + 1, len(lines)):
                    if lines[j].strip().startswith('.end method'):
                        method_end = j
                        break
                
                # Kiểm tra có .param trong method không
                for j in range(method_start, method_end):
                    if lines[j].strip().startswith('.param'):
                        has_param = True
                        break
                break
        
        # Bây giờ xử lý từng dòng
        for line in lines:
            if 'isScreenCaptureAllowed(I)Z' in line:
                in_method = True
                method_found = True
                new_lines.append(line)
                continue
            elif in_method and line.strip().startswith('.end method'):
                in_method = False
                new_lines.append(line)
                continue
            elif in_method:
                new_lines.append(line)
                # Nếu có .param, thêm code sau .param
                if line.strip().startswith('.param') and has_param and not code_added:
                    code_added = True
                    # Thêm code disable flag secure sau dòng .param
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure_a14_15"\n')
                    new_lines.append('    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n')
                    new_lines.append('    move-result v0\n')
                    new_lines.append('    if-eqz v0, :cond_b87\n')
                    new_lines.append('    const/4 v0, 0x1\n')
                    new_lines.append('    return v0\n')
                    new_lines.append('    :cond_b87\n')
                    continue
                # Nếu không có .param, thêm code sau .registers
                elif line.strip().startswith('.registers') and not has_param and not code_added:
                    code_added = True
                    # Thêm code disable flag secure sau dòng .registers
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure_a14_15"\n')
                    new_lines.append('    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n')
                    new_lines.append('    move-result v0\n')
                    new_lines.append('    if-eqz v0, :cond_b87\n')
                    new_lines.append('    const/4 v0, 0x1\n')
                    new_lines.append('    return v0\n')
                    new_lines.append('    :cond_b87\n')
                    continue
            else:
                new_lines.append(line)
        
        file_path.write_text("".join(new_lines), encoding='utf-8')
        
        return True
        
    except Exception as e:
        log(f"    ❌ Loi khi sua {file_path.name}: {e}")
        return False


def modify_device_policy_manager_service(file_path: Path) -> bool:
    """Modify DevicePolicyManagerService.smali to add flag secure checks"""
    try:
        with file_path.open('r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        new_lines = []
        in_method = False
        method_found = False
        current_method = ""
        has_param = False
        code_added = False
        
        # Đầu tiên, kiểm tra xem các method có .param không
        methods_info = {}
        for line in lines:
            if 'getScreenCaptureDisabled(Landroid/content/ComponentName;IZ)Z' in line:
                method_start = lines.index(line)
                method_end = len(lines)
                for j in range(method_start + 1, len(lines)):
                    if lines[j].strip().startswith('.end method'):
                        method_end = j
                        break
                
                has_param = False
                for j in range(method_start, method_end):
                    if lines[j].strip().startswith('.param'):
                        has_param = True
                        break
                methods_info['getScreenCaptureDisabled'] = has_param
            
            elif 'setScreenCaptureDisabled(Landroid/content/ComponentName;Ljava/lang/String;ZZ)V' in line:
                method_start = lines.index(line)
                method_end = len(lines)
                for j in range(method_start + 1, len(lines)):
                    if lines[j].strip().startswith('.end method'):
                        method_end = j
                        break
                
                has_param = False
                for j in range(method_start, method_end):
                    if lines[j].strip().startswith('.param'):
                        has_param = True
                        break
                methods_info['setScreenCaptureDisabled'] = has_param
        
        # Bây giờ xử lý từng dòng
        for line in lines:
            if 'getScreenCaptureDisabled(Landroid/content/ComponentName;IZ)Z' in line:
                in_method = True
                method_found = True
                current_method = 'getScreenCaptureDisabled'
                code_added = False
                new_lines.append(line)
                continue
            elif 'setScreenCaptureDisabled(Landroid/content/ComponentName;Ljava/lang/String;ZZ)V' in line:
                in_method = True
                method_found = True
                current_method = 'setScreenCaptureDisabled'
                code_added = False
                new_lines.append(line)
                continue
            elif in_method and line.strip().startswith('.end method'):
                in_method = False
                new_lines.append(line)
                continue
            elif in_method:
                new_lines.append(line)
                
                # Xử lý getScreenCaptureDisabled method
                if current_method == 'getScreenCaptureDisabled':
                    # Nếu có .param, thêm code sau dòng .param (vì .param xuất hiện sau .registers)
                    if line.strip().startswith('.param') and methods_info['getScreenCaptureDisabled'] and not code_added:
                        code_added = True
                        new_lines.append('    const-string/jumbo v0, "disable_flag_secure_a14_15"\n')
                        new_lines.append('    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n')
                        new_lines.append('    move-result v0\n')
                        new_lines.append('    if-eqz v0, :cond_b88\n')
                        new_lines.append('    const/4 v0, 0x0\n')
                        new_lines.append('    return v0\n')
                        new_lines.append('    :cond_b88\n')
                        continue
                    # Nếu không có .param, thêm code sau dòng .registers
                    elif line.strip().startswith('.registers') and not methods_info['getScreenCaptureDisabled'] and not code_added:
                        code_added = True
                        new_lines.append('    const-string/jumbo v0, "disable_flag_secure_a14_15"\n')
                        new_lines.append('    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n')
                        new_lines.append('    move-result v0\n')
                        new_lines.append('    if-eqz v0, :cond_b88\n')
                        new_lines.append('    const/4 v0, 0x0\n')
                        new_lines.append('    return v0\n')
                        new_lines.append('    :cond_b88\n')
                        continue
                
                # Xử lý setScreenCaptureDisabled method
                elif current_method == 'setScreenCaptureDisabled':
                    # Nếu có .param, thêm code sau dòng .param (vì .param xuất hiện sau .registers)
                    if line.strip().startswith('.param') and methods_info['setScreenCaptureDisabled'] and not code_added:
                        code_added = True
                        new_lines.append('    const-string/jumbo v0, "disable_flag_secure_a14_15"\n')
                        new_lines.append('    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n')
                        new_lines.append('    move-result v0\n')
                        new_lines.append('    if-eqz v0, :cond_a98\n')
                        new_lines.append('    return-void\n')
                        new_lines.append('    :cond_a98\n')
                        continue
                    # Nếu không có .param, thêm code sau dòng .registers
                    elif line.strip().startswith('.registers') and not methods_info['setScreenCaptureDisabled'] and not code_added:
                        code_added = True
                        new_lines.append('    const-string/jumbo v0, "disable_flag_secure_a14_15"\n')
                        new_lines.append('    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n')
                        new_lines.append('    move-result v0\n')
                        new_lines.append('    if-eqz v0, :cond_a98\n')
                        new_lines.append('    return-void\n')
                        new_lines.append('    :cond_a98\n')
                        continue
            else:
                new_lines.append(line)
        
        file_path.write_text("".join(new_lines), encoding='utf-8')
        
        return True
        
    except Exception as e:
        log(f"    ❌ Loi khi sua {file_path.name}: {e}")
        return False


def modify_window_manager_service(file_path: Path) -> bool:
    """Modify WindowManagerService.smali to add flag secure check using state tracking"""
    try:
        with file_path.open('r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()

        new_lines = []
        in_method = False
        after_annotation = False
        code_inserted = False
        skipping_premature_block = False

        for line in lines:
            stripped = line.strip()
            # Enter target method
            if stripped.startswith('.method public notifyScreenshotListeners(I)Ljava/util/List;'):
                in_method = True
                after_annotation = False
                code_inserted = False
                skipping_premature_block = False
                new_lines.append(line)
                continue
            # Exit target method
            if in_method and stripped.startswith('.end method'):
                in_method = False
                after_annotation = False
                code_inserted = False
                skipping_premature_block = False
                new_lines.append(line)
                continue

            if in_method:
                # If we detect an early inserted block before the annotation, skip it
                if not after_annotation:
                    if not skipping_premature_block and 'const-string/jumbo v0, "disable_flag_secure_a14_15"' in line:
                        skipping_premature_block = True
                        # Do not append this line (start skipping)
                        continue
                    if skipping_premature_block:
                        # Stop skipping when we pass the typical end label of the block
                        if stripped == ':cond_989':
                            skipping_premature_block = False
                            # Also skip this label line
                            continue
                        # Skip any lines inside the premature block
                        continue

                new_lines.append(line)

                # Detect the end of annotation and insert code exactly once after it
                if '.end annotation' in line and not code_inserted:
                    after_annotation = True
                    # Insert the disable block once right after annotation ends
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure_a14_15"\n')
                    new_lines.append('    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n')
                    new_lines.append('    move-result v0\n')
                    new_lines.append('    if-eqz v0, :cond_989\n')
                    new_lines.append('    invoke-static {}, Ljava/util/Collections;->emptyList()Ljava/util/List;\n')
                    new_lines.append('    move-result-object p1\n')
                    new_lines.append('    return-object p1\n')
                    new_lines.append('    :cond_989\n')
                    code_inserted = True
                continue

            # Outside method
            new_lines.append(line)

        file_path.write_text("".join(new_lines), encoding='utf-8')

        return True

    except Exception as e:
        log(f"    ❌ Loi khi sua {file_path.name}: {e}")
        return False


def modify_window_state(file_path: Path) -> bool:
    """Modify WindowState.smali to add flag secure check"""
    try:
        with file_path.open('r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
        
        new_lines = []
        in_method = False
        
        for line in lines:
            if line.strip().startswith('.method isSecureLocked()Z'):
                in_method = True
                new_lines.append(line)
                continue
            elif in_method and line.strip().startswith('.end method'):
                in_method = False
                new_lines.append(line)
                continue
            elif in_method:
                new_lines.append(line)
                # Insert right after .registers
                if '.registers' in line:
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure_a14_15"\n')
                    new_lines.append('    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n')
                    new_lines.append('    move-result v0\n')
                    new_lines.append('    if-eqz v0, :cond_888\n')
                    new_lines.append('    const/4 v0, 0x0\n')
                    new_lines.append('    return v0\n')
                    new_lines.append('    :cond_888\n')
                continue
            else:
                new_lines.append(line)
        
        file_path.write_text("".join(new_lines), encoding='utf-8')
        
        return True
        
    except Exception as e:
        log(f"    ❌ Loi khi sua {file_path.name}: {e}")
        return False


# --- Android 16: logic từ AutoPatchFramework a16.py (SettingsHelper → smali_classes6, key "disable_flag_secure") ---

def copy_settings_helper_a16(work_dir: Path) -> bool:
    """Copy SettingsHelper.smali vào framework_unpacked/smali_classes6/android/preference (a16)."""
    try:
        source_path = ROOT_DIR / "MEZO" / "SettingsHelper.smali"
        target_dir = work_dir / "framework_unpacked" / "smali_classes6" / "android" / "preference"
        target_path = target_dir / "SettingsHelper.smali"

        if not source_path.exists():
            log(f"    ❌ File nguon {source_path} khong ton tai")
            return False

        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)
        return True

    except Exception as e:
        log(f"    ❌ Loi khi copy file: {e}")
        return False


def modify_window_manager_service_impl_a16(file_path: Path) -> bool:
    """a16: notAllowCaptureDisplay + key disable_flag_secure"""
    try:
        with file_path.open("r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        new_lines: list[str] = []
        in_method = False
        has_param = False
        code_added = False

        for line in lines:
            if line.strip().startswith(
                ".method public notAllowCaptureDisplay(Lcom/android/server/wm/RootWindowContainer;I)Z"
            ):
                method_start = lines.index(line)
                method_end = len(lines)
                for j in range(method_start + 1, len(lines)):
                    if lines[j].strip().startswith(".end method"):
                        method_end = j
                        break
                has_param = False
                for j in range(method_start, method_end):
                    if lines[j].strip().startswith(".param"):
                        has_param = True
                        break
                break

        for line in lines:
            if line.strip().startswith(
                ".method public notAllowCaptureDisplay(Lcom/android/server/wm/RootWindowContainer;I)Z"
            ):
                in_method = True
                new_lines.append(line)
                continue
            if in_method and line.strip().startswith(".end method"):
                in_method = False
                new_lines.append(line)
                continue
            if in_method:
                new_lines.append(line)
                if line.strip().startswith(".param") and has_param and not code_added:
                    code_added = True
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure"\n')
                    new_lines.append(
                        "    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n"
                    )
                    new_lines.append("    move-result v0\n")
                    new_lines.append("    if-eqz v0, :cond_984\n")
                    new_lines.append("    const/4 v0, 0x0\n")
                    new_lines.append("    return v0\n")
                    new_lines.append("    :cond_984\n")
                    continue
                if line.strip().startswith(".registers") and not has_param and not code_added:
                    code_added = True
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure"\n')
                    new_lines.append(
                        "    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n"
                    )
                    new_lines.append("    move-result v0\n")
                    new_lines.append("    if-eqz v0, :cond_984\n")
                    new_lines.append("    const/4 v0, 0x0\n")
                    new_lines.append("    return v0\n")
                    new_lines.append("    :cond_984\n")
                    continue
            else:
                new_lines.append(line)

        file_path.write_text("".join(new_lines), encoding="utf-8")
        return True

    except Exception as e:
        log(f"    ❌ Loi khi sua {file_path.name}: {e}")
        return False


def modify_device_policy_cache_impl_a16(file_path: Path) -> bool:
    """a16: isScreenCaptureAllowed + disable_flag_secure"""
    try:
        with file_path.open("r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        new_lines: list[str] = []
        in_method = False
        has_param = False
        code_added = False

        for line in lines:
            if "isScreenCaptureAllowed(I)Z" in line:
                method_start = lines.index(line)
                method_end = len(lines)
                for j in range(method_start + 1, len(lines)):
                    if lines[j].strip().startswith(".end method"):
                        method_end = j
                        break
                has_param = False
                for j in range(method_start, method_end):
                    if lines[j].strip().startswith(".param"):
                        has_param = True
                        break
                break

        for line in lines:
            if "isScreenCaptureAllowed(I)Z" in line:
                in_method = True
                new_lines.append(line)
                continue
            if in_method and line.strip().startswith(".end method"):
                in_method = False
                new_lines.append(line)
                continue
            if in_method:
                new_lines.append(line)
                if line.strip().startswith(".param") and has_param and not code_added:
                    code_added = True
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure"\n')
                    new_lines.append(
                        "    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n"
                    )
                    new_lines.append("    move-result v0\n")
                    new_lines.append("    if-eqz v0, :cond_b87\n")
                    new_lines.append("    const/4 v0, 0x1\n")
                    new_lines.append("    return v0\n")
                    new_lines.append("    :cond_b87\n")
                    continue
                if line.strip().startswith(".registers") and not has_param and not code_added:
                    code_added = True
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure"\n')
                    new_lines.append(
                        "    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n"
                    )
                    new_lines.append("    move-result v0\n")
                    new_lines.append("    if-eqz v0, :cond_b87\n")
                    new_lines.append("    const/4 v0, 0x1\n")
                    new_lines.append("    return v0\n")
                    new_lines.append("    :cond_b87\n")
                    continue
            else:
                new_lines.append(line)

        file_path.write_text("".join(new_lines), encoding="utf-8")
        return True

    except Exception as e:
        log(f"    ❌ Loi khi sua {file_path.name}: {e}")
        return False


def modify_device_policy_manager_service_a16(file_path: Path) -> bool:
    """a16: getScreenCaptureDisabled / setScreenCaptureDisabled + disable_flag_secure"""
    try:
        with file_path.open("r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        new_lines: list[str] = []
        in_method = False
        current_method = ""
        code_added = False

        methods_info: dict[str, bool] = {}
        for line in lines:
            if "getScreenCaptureDisabled(Landroid/content/ComponentName;IZ)Z" in line:
                method_start = lines.index(line)
                method_end = len(lines)
                for j in range(method_start + 1, len(lines)):
                    if lines[j].strip().startswith(".end method"):
                        method_end = j
                        break
                hp = False
                for j in range(method_start, method_end):
                    if lines[j].strip().startswith(".param"):
                        hp = True
                        break
                methods_info["getScreenCaptureDisabled"] = hp
            elif "setScreenCaptureDisabled(Landroid/content/ComponentName;Ljava/lang/String;ZZ)V" in line:
                method_start = lines.index(line)
                method_end = len(lines)
                for j in range(method_start + 1, len(lines)):
                    if lines[j].strip().startswith(".end method"):
                        method_end = j
                        break
                hp = False
                for j in range(method_start, method_end):
                    if lines[j].strip().startswith(".param"):
                        hp = True
                        break
                methods_info["setScreenCaptureDisabled"] = hp

        for line in lines:
            if "getScreenCaptureDisabled(Landroid/content/ComponentName;IZ)Z" in line:
                in_method = True
                current_method = "getScreenCaptureDisabled"
                code_added = False
                new_lines.append(line)
                continue
            if "setScreenCaptureDisabled(Landroid/content/ComponentName;Ljava/lang/String;ZZ)V" in line:
                in_method = True
                current_method = "setScreenCaptureDisabled"
                code_added = False
                new_lines.append(line)
                continue
            if in_method and line.strip().startswith(".end method"):
                in_method = False
                new_lines.append(line)
                continue
            if in_method:
                new_lines.append(line)
                if current_method == "getScreenCaptureDisabled":
                    if (
                        line.strip().startswith(".param")
                        and methods_info.get("getScreenCaptureDisabled")
                        and not code_added
                    ):
                        code_added = True
                        new_lines.append('    const-string/jumbo v0, "disable_flag_secure"\n')
                        new_lines.append(
                            "    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n"
                        )
                        new_lines.append("    move-result v0\n")
                        new_lines.append("    if-eqz v0, :cond_b88\n")
                        new_lines.append("    const/4 v0, 0x0\n")
                        new_lines.append("    return v0\n")
                        new_lines.append("    :cond_b88\n")
                        continue
                    if (
                        line.strip().startswith(".registers")
                        and not methods_info.get("getScreenCaptureDisabled")
                        and not code_added
                    ):
                        code_added = True
                        new_lines.append('    const-string/jumbo v0, "disable_flag_secure"\n')
                        new_lines.append(
                            "    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n"
                        )
                        new_lines.append("    move-result v0\n")
                        new_lines.append("    if-eqz v0, :cond_b88\n")
                        new_lines.append("    const/4 v0, 0x0\n")
                        new_lines.append("    return v0\n")
                        new_lines.append("    :cond_b88\n")
                        continue
                elif current_method == "setScreenCaptureDisabled":
                    if (
                        line.strip().startswith(".param")
                        and methods_info.get("setScreenCaptureDisabled")
                        and not code_added
                    ):
                        code_added = True
                        new_lines.append('    const-string/jumbo v0, "disable_flag_secure"\n')
                        new_lines.append(
                            "    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n"
                        )
                        new_lines.append("    move-result v0\n")
                        new_lines.append("    if-eqz v0, :cond_a98\n")
                        new_lines.append("    return-void\n")
                        new_lines.append("    :cond_a98\n")
                        continue
                    if (
                        line.strip().startswith(".registers")
                        and not methods_info.get("setScreenCaptureDisabled")
                        and not code_added
                    ):
                        code_added = True
                        new_lines.append('    const-string/jumbo v0, "disable_flag_secure"\n')
                        new_lines.append(
                            "    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n"
                        )
                        new_lines.append("    move-result v0\n")
                        new_lines.append("    if-eqz v0, :cond_a98\n")
                        new_lines.append("    return-void\n")
                        new_lines.append("    :cond_a98\n")
                        continue
            else:
                new_lines.append(line)

        file_path.write_text("".join(new_lines), encoding="utf-8")
        return True

    except Exception as e:
        log(f"    ❌ Loi khi sua {file_path.name}: {e}")
        return False


def modify_window_manager_service_a16(file_path: Path) -> bool:
    """a16: notifyScreenshotListeners + disable_flag_secure (skip premature block)"""
    try:
        with file_path.open("r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        new_lines: list[str] = []
        in_method = False
        after_annotation = False
        code_inserted = False
        skipping_premature_block = False

        for line in lines:
            stripped = line.strip()
            if stripped.startswith(".method public notifyScreenshotListeners(I)Ljava/util/List;"):
                in_method = True
                after_annotation = False
                code_inserted = False
                skipping_premature_block = False
                new_lines.append(line)
                continue
            if in_method and stripped.startswith(".end method"):
                in_method = False
                after_annotation = False
                code_inserted = False
                skipping_premature_block = False
                new_lines.append(line)
                continue

            if in_method:
                if not after_annotation:
                    if (
                        not skipping_premature_block
                        and 'const-string/jumbo v0, "disable_flag_secure"' in line
                    ):
                        skipping_premature_block = True
                        continue
                    if skipping_premature_block:
                        if stripped == ":cond_989":
                            skipping_premature_block = False
                            continue
                        continue

                new_lines.append(line)

                if ".end annotation" in line and not code_inserted:
                    after_annotation = True
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure"\n')
                    new_lines.append(
                        "    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n"
                    )
                    new_lines.append("    move-result v0\n")
                    new_lines.append("    if-eqz v0, :cond_989\n")
                    new_lines.append(
                        "    invoke-static {}, Ljava/util/Collections;->emptyList()Ljava/util/List;\n"
                    )
                    new_lines.append("    move-result-object p1\n")
                    new_lines.append("    return-object p1\n")
                    new_lines.append("    :cond_989\n")
                    code_inserted = True
                continue

            new_lines.append(line)

        file_path.write_text("".join(new_lines), encoding="utf-8")
        return True

    except Exception as e:
        log(f"    ❌ Loi khi sua {file_path.name}: {e}")
        return False


def modify_window_state_a16(file_path: Path) -> bool:
    """a16: isSecureLocked + disable_flag_secure"""
    try:
        with file_path.open("r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()

        new_lines: list[str] = []
        in_method = False

        for line in lines:
            if line.strip().startswith(".method isSecureLocked()Z"):
                in_method = True
                new_lines.append(line)
                continue
            if in_method and line.strip().startswith(".end method"):
                in_method = False
                new_lines.append(line)
                continue
            if in_method:
                new_lines.append(line)
                if ".registers" in line:
                    new_lines.append('    const-string/jumbo v0, "disable_flag_secure"\n')
                    new_lines.append(
                        "    invoke-static {v0}, Landroid/preference/SettingsHelper;->getIntofSettings(Ljava/lang/String;)I\n"
                    )
                    new_lines.append("    move-result v0\n")
                    new_lines.append("    if-eqz v0, :cond_888\n")
                    new_lines.append("    const/4 v0, 0x0\n")
                    new_lines.append("    return v0\n")
                    new_lines.append("    :cond_888\n")
                continue
            new_lines.append(line)

        file_path.write_text("".join(new_lines), encoding="utf-8")
        return True

    except Exception as e:
        log(f"    ❌ Loi khi sua {file_path.name}: {e}")
        return False


def disable_flag_secure_a16(work_dir: Path) -> None:
    """Disable Flag Secure (Android 16 / a16.py): SettingsHelper → smali_classes6, paths như a16."""
    log("\n🔒 Processing Disable Flag Secure A16...")
    log("📝 Chinh sua cac file de vo hieu hoa Flag Secure (a16)...")

    total_files_processed = 0

    log("\n📁 Copying SettingsHelper.smali (smali_classes6)...")
    if copy_settings_helper_a16(work_dir):
        total_files_processed += 1
        log("    ✅ SettingsHelper.smali copied successfully")
    else:
        log("    ❌ Loi khi copy SettingsHelper.smali")

    log("\n📁 Processing: WindowManagerServiceImpl.smali")
    wms_impl_path = (
        work_dir
        / "miui_services_unpacked"
        / "smali_classes"
        / "com"
        / "android"
        / "server"
        / "wm"
        / "WindowManagerServiceImpl.smali"
    )
    if wms_impl_path.exists():
        if modify_window_manager_service_impl_a16(wms_impl_path):
            total_files_processed += 1
            log("    ✅ Da sua thanh cong")
        else:
            log("    ❌ Loi khi sua")
    else:
        log("    ⚠️  File WindowManagerServiceImpl.smali khong tim thay")

    log("\n📁 Processing: DevicePolicyCacheImpl.smali")
    dpc_impl_path = (
        work_dir
        / "services_unpacked"
        / "smali_classes2"
        / "com"
        / "android"
        / "server"
        / "devicepolicy"
        / "DevicePolicyCacheImpl.smali"
    )
    if dpc_impl_path.exists():
        if modify_device_policy_cache_impl_a16(dpc_impl_path):
            total_files_processed += 1
            log("    ✅ Da sua thanh cong")
        else:
            log("    ❌ Loi khi sua")
    else:
        log("    ⚠️  File DevicePolicyCacheImpl.smali khong tim thay")

    log("\n📁 Processing: DevicePolicyManagerService.smali")
    dpm_service_path = (
        work_dir
        / "services_unpacked"
        / "smali_classes2"
        / "com"
        / "android"
        / "server"
        / "devicepolicy"
        / "DevicePolicyManagerService.smali"
    )
    if dpm_service_path.exists():
        if modify_device_policy_manager_service_a16(dpm_service_path):
            total_files_processed += 1
            log("    ✅ Da sua thanh cong")
        else:
            log("    ❌ Loi khi sua")
    else:
        log("    ⚠️  File DevicePolicyManagerService.smali khong tim thay")

    log("\n📁 Processing: WindowManagerService.smali")
    wm_service_path = (
        work_dir
        / "services_unpacked"
        / "smali_classes3"
        / "com"
        / "android"
        / "server"
        / "wm"
        / "WindowManagerService.smali"
    )
    if wm_service_path.exists():
        if modify_window_manager_service_a16(wm_service_path):
            total_files_processed += 1
            log("    ✅ Da sua thanh cong")
        else:
            log("    ❌ Loi khi sua")
    else:
        log("    ⚠️  File WindowManagerService.smali khong tim thay")

    log("\n📁 Processing: WindowState.smali")
    window_state_path = (
        work_dir
        / "services_unpacked"
        / "smali_classes3"
        / "com"
        / "android"
        / "server"
        / "wm"
        / "WindowState.smali"
    )
    if window_state_path.exists():
        if modify_window_state_a16(window_state_path):
            total_files_processed += 1
            log("    ✅ Da sua thanh cong")
        else:
            log("    ❌ Loi khi sua")
    else:
        log("    ⚠️  File WindowState.smali khong tim thay")

    log(f"\n🎉 Disable Flag Secure A16 complete!")
    log(f"📊 Tong so file da xu ly: {total_files_processed}")


def disable_flag_secure_a14_15(work_dir: Path) -> None:
    """Disable Flag Secure by modifying various framework and service files"""
    log("\n🔒 Processing Disable Flag Secure...")
    log("📝 Chinh sua cac file de vo hieu hoa Flag Secure...")
    
    total_files_processed = 0
    
    # 1. Copy SettingsHelper.smali from MEZO to framework_unpacked/smali_classes3/android/preference
    log("\n📁 Copying SettingsHelper.smali...")
    if copy_settings_helper(work_dir):
        total_files_processed += 1
        log("    ✅ SettingsHelper.smali copied successfully")
    else:
        log("    ❌ Loi khi copy SettingsHelper.smali")
    
    # 2. Modify WindowManagerServiceImpl.smali in miui_services_unpacked
    log("\n📁 Processing: WindowManagerServiceImpl.smali")
    wms_impl_path = work_dir / "miui_services_unpacked" / "smali_classes" / "com" / "android" / "server" / "wm" / "WindowManagerServiceImpl.smali"
    if wms_impl_path.exists():
        if modify_window_manager_service_impl(wms_impl_path):
            total_files_processed += 1
            log("    ✅ Da sua thanh cong")
        else:
            log("    ❌ Loi khi sua")
    else:
        log("    ⚠️  File WindowManagerServiceImpl.smali khong tim thay")
    
    # 3. Modify DevicePolicyCacheImpl.smali in services_unpacked
    log("\n📁 Processing: DevicePolicyCacheImpl.smali")
    dpc_impl_path = work_dir / "services_unpacked" / "smali_classes" / "com" / "android" / "server" / "devicepolicy" / "DevicePolicyCacheImpl.smali"
    if dpc_impl_path.exists():
        if modify_device_policy_cache_impl(dpc_impl_path):
            total_files_processed += 1
            log("    ✅ Da sua thanh cong")
        else:
            log("    ❌ Loi khi sua")
    else:
        log("    ⚠️  File DevicePolicyCacheImpl.smali khong tim thay")
    
    # 4. Modify DevicePolicyManagerService.smali in services_unpacked
    log("\n📁 Processing: DevicePolicyManagerService.smali")
    dpm_service_path = work_dir / "services_unpacked" / "smali_classes" / "com" / "android" / "server" / "devicepolicy" / "DevicePolicyManagerService.smali"
    if dpm_service_path.exists():
        if modify_device_policy_manager_service(dpm_service_path):
            total_files_processed += 1
            log("    ✅ Da sua thanh cong")
        else:
            log("    ❌ Loi khi sua")
    else:
        log("    ⚠️  File DevicePolicyManagerService.smali khong tim thay")
    
    # 5. Modify WindowManagerService.smali in services_unpacked/smali_classes3
    log("\n📁 Processing: WindowManagerService.smali")
    wm_service_path = work_dir / "services_unpacked" / "smali_classes3" / "com" / "android" / "server" / "wm" / "WindowManagerService.smali"
    if wm_service_path.exists():
        if modify_window_manager_service(wm_service_path):
            total_files_processed += 1
            log("    ✅ Da sua thanh cong")
        else:
            log("    ❌ Loi khi sua")
    else:
        log("    ⚠️  File WindowManagerService.smali khong tim thay")
    
    # 6. Modify WindowState.smali in services_unpacked/smali_classes3
    log("\n📁 Processing: WindowState.smali")
    window_state_path = work_dir / "services_unpacked" / "smali_classes3" / "com" / "android" / "server" / "wm" / "WindowState.smali"
    if window_state_path.exists():
        if modify_window_state(window_state_path):
            total_files_processed += 1
            log("    ✅ Da sua thanh cong")
        else:
            log("    ❌ Loi khi sua")
    else:
        log("    ⚠️  File WindowState.smali khong tim thay")
    
    log(f"\n🎉 Disable Flag Secure complete!")
    log(f"📊 Tong so file da xu ly: {total_files_processed}")


def copy_kaorios_folder(work_dir: Path) -> bool:
    """Copy kaorios folder from MEZO to framework_unpacked"""
    try:
        source = ROOT_DIR / "MEZO" / "kaorios"
        if not source.exists():
            log(f"    ❌ Không có thư mục nguồn {source}")
            return False

        framework_base = work_dir / "framework_unpacked"
        if not framework_base.exists():
            log("    ❌ Không tìm thấy thư mục framework_unpacked")
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
        log(f"    ❌ Lỗi copy kaorios: {exc}")
        return False


def modify_application_package_manager_kaori(file_path: Path) -> bool:
    """Modify ApplicationPackageManager.smali - add Kaorios toolbox modifications"""
    import re
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
        log(f"    ❌ Lỗi sửa {file_path.name}: {exc}")
        return False


def modify_instrumentation_kaori(file_path: Path) -> bool:
    """Modify Instrumentation.smali - add KaoriosProps calls before return-object v0 in newApplication methods"""
    import re
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
        log(f"    ❌ Lỗi sửa {file_path.name}: {exc}")
        return False


def modify_keystore2_kaori(file_path: Path) -> bool:
    """Modify KeyStore2.smali - add KaoriosKeybox call before return-object v0 in getKeyEntry method"""
    import re
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
        log(f"    ❌ Lỗi sửa {file_path.name}: {exc}")
        return False


def modify_android_keystore_spi_kaori(file_path: Path) -> bool:
    """Modify AndroidKeyStoreSpi.smali - add KaoriosPropsEngineGetCertificateChain call after .registers in engineGetCertificateChain method"""
    import re
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
        log(f"    ❌ Lỗi sửa {file_path.name}: {exc}")
        return False


def kaori_toolbox(work_dir: Path) -> None:
    """Kaori Toolbox - Apply kaorios modifications"""
    import re
    log("\n🎨 Mezo mod...")
    operations = 0

    if copy_kaorios_folder(work_dir):
        operations += 1
        log("    ✅ Copy kaorios hoàn tất")

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
            log(f"    ✅ ApplicationPackageManager patched")
        else:
            log(f"    ℹ️ ApplicationPackageManager không cần/không thể sửa")
    else:
        log("    ⚠️ Không tìm thấy ApplicationPackageManager.smali")

    instrumentation = find_first_by_name(framework_root, "Instrumentation.smali")
    if instrumentation:
        if modify_instrumentation_kaori(instrumentation):
            operations += 1
            log(f"    ✅ Instrumentation patched")
        else:
            log(f"    ℹ️ Instrumentation không cần/không thể sửa")
    else:
        log("    ⚠️ Không tìm thấy Instrumentation.smali")

    keystore2 = find_first_by_name(framework_root, "KeyStore2.smali")
    if keystore2:
        if modify_keystore2_kaori(keystore2):
            operations += 1
            log(f"    ✅ KeyStore2 patched")
        else:
            log(f"    ℹ️ KeyStore2 không cần/không thể sửa")
    else:
        log("    ⚠️ Không tìm thấy KeyStore2.smali")

    android_keystore_spi = find_first_by_name(framework_root, "AndroidKeyStoreSpi.smali")
    if android_keystore_spi:
        if modify_android_keystore_spi_kaori(android_keystore_spi):
            operations += 1
            log(f"    ✅ AndroidKeyStoreSpi patched")
        else:
            log(f"    ℹ️ AndroidKeyStoreSpi không cần/không thể sửa")
    else:
        log("    ⚠️ Không tìm thấy AndroidKeyStoreSpi.smali")

    log(f"\n🎉 Hoàn tất Mezo mod ({operations} thao tác).")


def tricky_wukong_a15(work_dir: Path) -> None:
    """Apply Wukong hooks to framework KeyStore2 and copy bridge smali for Android 15."""
    log("\n🐒 Processing Tricky Wukong...")

    bridge_src = ROOT_DIR / "MEZO" / "WukongFrameworkBridge.smali"
    bridge_dst_dir = work_dir / "framework_unpacked" / "smali_classes5" / "android" / "security"
    bridge_dst = bridge_dst_dir / "WukongFrameworkBridge.smali"

    if not bridge_src.is_file():
        log(f"    ⚠️ Khong tim thay file nguon: {bridge_src}")
    else:
        try:
            bridge_dst_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(bridge_src, bridge_dst)
            log(f"    ✅ Da copy WukongFrameworkBridge.smali -> {bridge_dst}")
        except Exception as exc:
            log(f"    ❌ Loi khi copy WukongFrameworkBridge.smali: {exc}")

    keystore2_path = (
        work_dir
        / "framework_unpacked"
        / "smali_classes3"
        / "android"
        / "security"
        / "KeyStore2.smali"
    )
    if not keystore2_path.is_file():
        log(f"    ⚠️ Khong tim thay file: {keystore2_path}")
        return

    try:
        content = keystore2_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        log(f"    ❌ Loi khi doc KeyStore2.smali: {exc}")
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
            log("    ✅ Da patch KeyStore2.smali voi tricky_wukong")
        else:
            log("    ℹ️ KeyStore2.smali khong can/khong the patch them")
    except Exception as exc:
        log(f"    ❌ Loi khi ghi KeyStore2.smali: {exc}")

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
        log(f"    ⚠️ Khong tim thay file: {keypair_spi_path}")
        return

    try:
        keypair_content = keypair_spi_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        log(f"    ❌ Loi khi doc AndroidKeyStoreKeyPairGeneratorSpi.smali: {exc}")
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
            log("    ✅ Da patch AndroidKeyStoreKeyPairGeneratorSpi.smali")
        else:
            log("    ℹ️ AndroidKeyStoreKeyPairGeneratorSpi.smali khong can/khong the patch them")
    except Exception as exc:
        log(f"    ❌ Loi khi ghi AndroidKeyStoreKeyPairGeneratorSpi.smali: {exc}")


def tricky_wukong_a16(work_dir: Path) -> None:
    """Apply Wukong hooks to framework KeyStore2 and copy bridge smali."""
    log("\n🐒 Processing Tricky Wukong...")

    bridge_src = ROOT_DIR / "MEZO" / "WukongFrameworkBridge.smali"
    bridge_dst_dir = work_dir / "framework_unpacked" / "smali_classes6" / "android" / "security"
    bridge_dst = bridge_dst_dir / "WukongFrameworkBridge.smali"

    if not bridge_src.is_file():
        log(f"    ⚠️ Khong tim thay file nguon: {bridge_src}")
    else:
        try:
            bridge_dst_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(bridge_src, bridge_dst)
            log(f"    ✅ Da copy WukongFrameworkBridge.smali -> {bridge_dst}")
        except Exception as exc:
            log(f"    ❌ Loi khi copy WukongFrameworkBridge.smali: {exc}")

    keystore2_path = (
        work_dir
        / "framework_unpacked"
        / "smali_classes3"
        / "android"
        / "security"
        / "KeyStore2.smali"
    )
    if not keystore2_path.is_file():
        log(f"    ⚠️ Khong tim thay file: {keystore2_path}")
        return

    try:
        content = keystore2_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        log(f"    ❌ Loi khi doc KeyStore2.smali: {exc}")
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
            log("    ✅ Da patch KeyStore2.smali voi tricky_wukong")
        else:
            log("    ℹ️ KeyStore2.smali khong can/khong the patch them")
    except Exception as exc:
        log(f"    ❌ Loi khi ghi KeyStore2.smali: {exc}")

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
        log(f"    ⚠️ Khong tim thay file: {keypair_spi_path}")
        return

    try:
        keypair_content = keypair_spi_path.read_text(encoding="utf-8", errors="ignore")
    except Exception as exc:
        log(f"    ❌ Loi khi doc AndroidKeyStoreKeyPairGeneratorSpi.smali: {exc}")
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
            log("    ✅ Da patch AndroidKeyStoreKeyPairGeneratorSpi.smali")
        else:
            log("    ℹ️ AndroidKeyStoreKeyPairGeneratorSpi.smali khong can/khong the patch them")
    except Exception as exc:
        log(f"    ❌ Loi khi ghi AndroidKeyStoreKeyPairGeneratorSpi.smali: {exc}")


def enhanced_keyboard(work_dir: Path) -> None:
    """Enhanced Keyboard - Replace Baidu input method with Google Keyboard"""
    log("\n⌨️ Processing Enhanced Keyboard...")
    log("📝 Tim kiem va thay the com.baidu.input_mi thanh com.google.android.inputmethod.latin...")
    
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
    log("\n📁 Xu ly miui_services_unpacked...")
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
                log(f"\n  🔍 Processing: {filename}")
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
                        log(f"    ✅ Da thay the {count} lan trong {filename}")
                    else:
                        log(f"    ℹ️ Khong tim thay '{old_string}' trong {filename}")
                except Exception as e:
                    log(f"    ❌ Loi khi xu ly {filename}: {e}")
            else:
                log(f"  ⚠️ Khong tim thay {filename}")
    else:
        log("  ⚠️ miui_services_unpacked directory not found")
    
    # Xu ly miui_framework_unpacked
    log("\n📁 Xu ly miui_framework_unpacked...")
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
                log(f"\n  🔍 Processing: {filename}")
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
                        log(f"    ✅ Da thay the {count} lan trong {filename}")
                    else:
                        log(f"    ℹ️ Khong tim thay '{old_string}' trong {filename}")
                except Exception as e:
                    log(f"    ❌ Loi khi xu ly {filename}: {e}")
            else:
                log(f"  ⚠️ Khong tim thay {filename}")
    else:
        log("  ⚠️ miui_framework_unpacked directory not found")
    
    log(f"\n🎉 Enhanced Keyboard complete!")
    log(f"📊 Tong so file da xu ly: {total_files_processed}")
    log(f"📊 Tong so lan thay the: {total_replacements}")


def enable_floating_window_all_app(work_dir: Path) -> None:
    """Enable floating window for all apps by modifying MiuiMultiWindowAdapter.smali"""
    log("\n🪟 Processing Enable Floating Window All App...")
    log("📝 Chinh sua file MiuiMultiWindowAdapter.smali...")
    
    # Path to MiuiMultiWindowAdapter.smali
    miui_multi_window_path = work_dir / "miui_framework_unpacked" / "smali_classes" / "android" / "util" / "MiuiMultiWindowAdapter.smali"
    
    if not miui_multi_window_path.exists():
        log(f"❌ MiuiMultiWindowAdapter.smali not found at: {miui_multi_window_path}")
        log("⚠️  Make sure miui-framework.jar has been extracted first")
        return
    
    log(f"📁 Processing: {miui_multi_window_path}")
    
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
                log("    ✅ Da sua method getFreeformBlackList thanh cong")
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
                log("    ✅ Da sua method getFreeformBlackListFromCloud thanh cong")
                continue

            # Non-target lines
            new_lines.append(line)
            i += 1
        
        # Write back to file if modified
        if file_modified:
            miui_multi_window_path.write_text("".join(new_lines), encoding='utf-8')
            log("✅ Da chinh sua MiuiMultiWindowAdapter.smali thanh cong")
        else:
            log("⚠️  Khong tim thay method nao can sua")
        
    except Exception as e:
        log(f"❌ Loi khi chinh sua MiuiMultiWindowAdapter.smali: {e}")
        return
    
    log(f"\n🎉 Enable Floating Window All App complete!")


def increase_number_of_floating_windows(work_dir: Path) -> None:
    """Tăng số lượng floating windows"""
    log("\n=== TANG SO LUONG FLOATING WINDOWS ===")
    
    # Kiểm tra thư mục miui_services_unpacked
    miui_services_dir = work_dir / "miui_services_unpacked"
    if not miui_services_dir.exists():
        log("❌ Khong tim thay thuc muc miui_services_unpacked")
        return
    
    # Tìm file MiuiFreeFormStackDisplayStrategy.smali
    target_file = miui_services_dir / "smali_classes" / "com" / "android" / "server" / "wm" / "MiuiFreeFormStackDisplayStrategy.smali"
    if not target_file.exists():
        log("❌ Khong tim thay file MiuiFreeFormStackDisplayStrategy.smali")
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
            log("❌ Khong tim thay method getMaxMiuiFreeFormStackCount")
            return
        
        if method_end == -1:
            log("❌ Khong tim thay ket thuc method getMaxMiuiFreeFormStackCount")
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
        
        log("✅ Da sua thanh cong method getMaxMiuiFreeFormStackCount")
        log("✅ So luong floating windows da duoc tang len")
        
    except Exception as e:
        log(f"❌ Loi khi sua MiuiFreeFormStackDisplayStrategy.smali: {e}")


def fix_notification(work_dir: Path) -> None:
    """Fix notification delay by setting IS_INTERNATIONAL_BUILD to true and CN_MODEL to false (smali edits)."""
    import re
    
    log("\n🔧 Processing notification fix...")
    log("📝 Tim kiem va sua cac dong chua 'IS_INTERNATIONAL_BUILD' trong cac file...")
    
    base_dir = work_dir / "miui_services_unpacked" / "smali_classes" / "com" / "android" / "server" / "am"
    
    if not base_dir.exists():
        log(f"❌ Thu muc {base_dir} khong ton tai")
        return
    
    target_files = [
        "BroadcastQueueModernStubImpl.smali",
        "ProcessManagerService.smali",
        "ProcessSceneCleaner.smali"
    ]
    
    total_files_processed = 0
    total_lines_fixed = 0
    pattern = r'(\s*)sget-boolean\s+(v[0-3]),\s+Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z'
    
    for filename in target_files:
        file_path = base_dir / filename
        if not file_path.exists():
            log(f"  ⚠️  File {filename} khong ton tai tai: {file_path}")
            continue
        
        log(f"\n  🔍 Processing: {filename}")
        try:
            content = file_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            new_lines = []
            modified = False
            lines_fixed_in_file = 0
            i = 0
            while i < len(lines):
                line = lines[i]
                new_lines.append(line)
                match = re.search(pattern, line)
                if match:
                    indent = match.group(1)
                    reg = match.group(2)
                    if i + 1 < len(lines):
                        nxt = lines[i + 1].strip()
                        if not re.match(rf'const/4\s+{re.escape(reg)},\s+0x1', nxt):
                            new_lines.append(f"{indent}const/4 {reg}, 0x1")
                            modified = True
                            lines_fixed_in_file += 1
                            log(f"    ✅ Them const/4 {reg}, 0x1 tai dong {i+1}")
                    else:
                        new_lines.append(f"{indent}const/4 {reg}, 0x1")
                        modified = True
                        lines_fixed_in_file += 1
                        log(f"    ✅ Them const/4 {reg}, 0x1 tai dong {i+1}")
                i += 1
            if modified:
                file_path.write_text('\n'.join(new_lines), encoding='utf-8')
                total_files_processed += 1
                total_lines_fixed += lines_fixed_in_file
                log(f"    ✅ Da sua {lines_fixed_in_file} dong trong file {filename}")
            else:
                log(f"    ℹ️  Khong tim thay dong nao can sua trong {filename}")
        except Exception as e:
            log(f"    ❌ Loi khi xu ly file {filename}: {str(e)}")
            continue
    
    log("\n📝 Tim kiem va sua file PolicyManager.smali...")
    policy_manager_path = work_dir / "miui_services_unpacked" / "smali_classes" / "com" / "miui" / "server" / "greeze" / "PolicyManager.smali"
    if policy_manager_path.exists():
        log(f"\n  🔍 Processing: PolicyManager.smali")
        try:
            content = policy_manager_path.read_text(encoding='utf-8')
            lines = content.split('\n')
            new_lines = []
            modified = False
            pattern_sput = r'(\s*)sput-boolean\s+v0,\s+Lcom/miui/server/greeze/PolicyManager;->CN_MODEL:Z'
            i = 0
            while i < len(lines):
                line = lines[i]
                match = re.search(pattern_sput, line)
                if match:
                    indent = match.group(1)
                    if i > 0:
                        prev = lines[i - 1].strip()
                        if not re.match(r'const/4\s+v0,\s+0x0', prev):
                            new_lines.append(f"{indent}const/4 v0, 0x0")
                            modified = True
                            log(f"    ✅ Them const/4 v0, 0x0 truoc dong {i+1}")
                    else:
                        new_lines.append(f"{indent}const/4 v0, 0x0")
                        modified = True
                        log(f"    ✅ Them const/4 v0, 0x0 truoc dong {i+1}")
                new_lines.append(line)
                i += 1
            if modified:
                policy_manager_path.write_text('\n'.join(new_lines), encoding='utf-8')
                total_files_processed += 1
                total_lines_fixed += 1
                log(f"    ✅ Da sua thanh cong file PolicyManager.smali")
            else:
                log(f"    ℹ️  Khong tim thay dong can sua trong PolicyManager.smali")
        except Exception as e:
            log(f"    ❌ Loi khi xu ly file PolicyManager.smali: {str(e)}")
    else:
        log(f"  ⚠️  File PolicyManager.smali khong ton tai tai: {policy_manager_path}")
    
    log(f"\n🎉 Notification fix complete!")
    log(f"📊 Tong so file da xu ly: {total_files_processed}")
    log(f"📊 Tong so dong da sua: {total_lines_fixed}")


def fix_theme_reset(work_dir: Path) -> None:
    """Remove smali lines from nearest `.line` down to DRM broadcast call."""
    log("\n🔧 Processing theme reset fix...")
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
        log(f"❌ Khong tim thay file: {target_file}")
        return

    try:
        lines = target_file.read_text(encoding="utf-8").splitlines(keepends=True)
    except Exception as exc:
        log(f"❌ Loi khi doc file {target_file}: {exc}")
        return

    broadcast_idx = -1
    for idx, line in enumerate(lines):
        if "Lmiui/drm/DrmBroadcast;->broadcast()V" in line:
            broadcast_idx = idx
            break

    if broadcast_idx == -1:
        log("ℹ️ Khong tim thay dong chua 'Lmiui/drm/DrmBroadcast;->broadcast()V'")
        return

    line_marker_idx = -1
    for idx in range(broadcast_idx, -1, -1):
        if "line" in lines[idx]:
            line_marker_idx = idx
            break

    if line_marker_idx == -1:
        log("⚠️ Tim thay dong broadcast, nhung khong tim thay dong chua 'line' o phia tren.")
        return

    # Xoa doan tu dong '.line' gan nhat den dong goi broadcast (bao gom ca hai dau).
    del lines[line_marker_idx : broadcast_idx + 1]

    try:
        target_file.write_text("".join(lines), encoding="utf-8")
        removed_count = broadcast_idx - line_marker_idx + 1
        log(f"✅ Da xoa {removed_count} dong trong {target_file.name}")
    except Exception as exc:
        log(f"❌ Loi khi ghi file {target_file}: {exc}")


def copy_tree_contents(src_dir: Path, dest_dir: Path, label: str) -> None:
    if not src_dir.is_dir():
        return

    dest_dir.mkdir(parents=True, exist_ok=True)
    log(f"Copying directory {label} to {dest_dir} ...")

    try:
        for root, _dirnames, filenames in os.walk(src_dir):
            rel_root = Path(root).relative_to(src_dir)
            target_root = dest_dir / rel_root
            target_root.mkdir(parents=True, exist_ok=True)

            for filename in filenames:
                src_file = Path(root) / filename
                dst_file = target_root / filename
                shutil.copy2(src_file, dst_file)
                log(f"    Copied: {src_file.relative_to(src_dir)}")
    except Exception as exc:
        log(f"    Loi khi copy {label}: {exc}")


def move_product_data_app_to_app(project_dir: Path) -> None:
    product_root = resolve_partition_root(project_dir, "product")
    if product_root is None:
        log("Product partition not found for data-app to app migration.")
        return

    data_app_dir = product_root / "data-app"
    app_dir = product_root / "app"

    if not data_app_dir.is_dir():
        log(f"Directory to move not found: {data_app_dir}")
        return

    entries = sorted(data_app_dir.iterdir(), key=lambda item: item.name.lower())
    if not entries:
        log("Khong co ung dung nao trong product/data-app de chuyen.")
        return

    app_dir.mkdir(parents=True, exist_ok=True)
    moved_count = 0

    for entry in entries:
        target_entry = app_dir / entry.name
        try:
            if target_entry.exists():
                if remove_path_force(target_entry):
                    log(f"    Da xoa muc trung ten tai dich: {target_entry}")
                else:
                    log(f"    Canh bao: khong xoa duoc muc trung ten tai dich: {target_entry}")
                    continue
            shutil.move(str(entry), str(target_entry))
            log(f"    Da chuyen {entry} -> {target_entry}")
            moved_count += 1
        except Exception as exc:
            log(f"    Loi khi chuyen {entry.name} sang product/app: {exc}")

    if moved_count == 0:
        log("Khong chuyen duoc muc nao tu product/data-app sang product/app.")

def fix_nfc(project_dir: Path) -> None:
    src_dir = project_dir / "product" / "pangu" / "system" / "app"
    dest_dir = project_dir / "system" / "system" / "app"

    if not src_dir.is_dir():
        log(f"NFC source directory not found: {src_dir}")
        return

    dest_dir.mkdir(parents=True, exist_ok=True)
    entries = sorted(src_dir.iterdir(), key=lambda item: item.name.lower())
    if not entries:
        log("No applications in NFC source directory to move.")
        return

    moved_count = 0
    for entry in entries:
        target_entry = dest_dir / entry.name
        try:
            if target_entry.exists():
                if remove_path_force(target_entry):
                    log(f"    Da xoa muc trung ten tai dich: {target_entry}")
                else:
                    log(f"    Canh bao: khong xoa duoc muc trung ten tai dich: {target_entry}")
                    continue
            shutil.move(str(entry), str(target_entry))
            log(f"    Da chuyen NFC {entry} -> {target_entry}")
            moved_count += 1
        except Exception as exc:
            log(f"    Loi khi chuyen NFC {entry.name}: {exc}")

    if moved_count == 0:
        log("Khong chuyen duoc muc nao tu NFC nguon sang dich.")
    else:
        log(f"Da chuyen {moved_count} muc NFC sang system/app.")

def copy_mezo_app_product(project_dir: Path) -> None:
    script_dir = Path(__file__).parent
    src_dir = script_dir / "MEZO_APP" / "product"

    if not src_dir.is_dir():
        log(f"Source directory not found: {src_dir}")
        return

    product_root = resolve_partition_root(project_dir, "product")
    if product_root is None:
        log("Product partition not found for MEZO_APP/product copy.")
        return

    copy_tree_contents(src_dir, product_root, "MEZO_APP/product")

    thermal_src = script_dir / "MEZO_APP" / "thermallevel_to_fps.xml"
    if not thermal_src.is_file():
        log(f"thermallevel_to_fps.xml not found at {thermal_src}")
        return

    vendor_root = resolve_partition_root(project_dir, "vendor")
    if vendor_root is None:
        log("Vendor partition not found for thermallevel_to_fps.xml edit.")
        return

    thermal_dst = vendor_root / "etc" / "display" / "thermallevel_to_fps.xml"
    try:
        thermal_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(thermal_src, thermal_dst)
        log("    Da sua thermallevel_to_fps.xml")
    except Exception as exc:
        log(f"    Loi khi copy thermallevel_to_fps.xml: {exc}")


def copy_mezo_app_mod(project_dir: Path) -> None:
    """
    Copy các thư mục mod: MEZO_APP/appMod/<name>
    -> tìm thư mục cùng tên trong partition `product` và thay thế thư mục gốc.
    """
    script_dir = Path(__file__).parent
    app_mod_root = script_dir / "MEZO_APP" / "appMod"
    if not app_mod_root.is_dir():
        log(f"App mod source directory not found: {app_mod_root}")
        return

    product_root = resolve_partition_root(project_dir, "product")
    if product_root is None:
        log("Product partition not found for app mod application.")
        return

    mod_dirs = sorted(
        [p for p in app_mod_root.iterdir() if p.is_dir()],
        key=lambda p: p.name.lower(),
    )
    if not mod_dirs:
        log(f"No mod directories in: {app_mod_root}")
        return

    log("Applying app mods from MEZO_APP/appMod ...")
    replaced_count = 0

    for mod_dir in mod_dirs:
        targets = [p for p in product_root.rglob(mod_dir.name) if p.is_dir()]
        if not targets:
            log(f"    Directory '{mod_dir.name}' not found in product to replace")
            continue

        for target_dir in targets:
            try:
                if not remove_path_force(target_dir):
                    log(f"    Warning: could not remove target directory: {target_dir}")
                    continue
                shutil.copytree(mod_dir, target_dir)
                replaced_count += 1
                log(f"    Replaced directory: {target_dir}")
            except Exception as exc:
                log(f"    Loi khi thay the thu muc '{target_dir}' bang '{mod_dir}': {exc}")

    if replaced_count == 0:
        log("    No directories replaced from MEZO_APP/appMod.")


def copy_mezo_app_system(project_dir: Path) -> None:
    """
    Copy MEZO_APP/system -> project_dir/system/system (overlay).
    """
    script_dir = Path(__file__).parent
    src_dir = script_dir / "MEZO_APP" / "system"
    if not src_dir.is_dir():
        log(f"Source directory not found: {src_dir}")
        return

    # Theo yeu cau cua ban: project_dir\system\system
    dest_dir = project_dir / "system" / "system"
    copy_tree_contents(src_dir, dest_dir, "MEZO_APP/system")


Q_FIX_SELINUX_LINE = "/system/system/bin/q_fix u:object_r:q_fix_exec:s0"

# plat_file_contexts: tab giữa path và context (theo định dạng file gốc)
Q_FIX_PLAT_FILE_CONTEXTS_LINE = "/system/bin/q_fix\tu:object_r:q_fix_exec:s0"

# Nhận diện block đã chèn (tránh append trùng)
Q_FIX_INIT_RC_MARKER = "# MezoBuildRom_q_fix_BLOCK"

# Khối append init.rc; "nuwa-locked" được thay bằng {ro.product.odm.device}-locked khi chạy q_fix()
Q_FIX_INIT_RC_APPEND = f"""
on post-fs-data
    {Q_FIX_INIT_RC_MARKER}
    # =========================================================
    # ---- Verified Boot state ----
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.verifiedbootstate green
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.veritymode enforcing
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.vbmeta.device_state locked
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.flash.locked 1

    # ---- Xiaomi secure boot state ----
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.secureboot.lockstate locked
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.secureboot.devicelock 1

    # ---- Bootloader identity ----
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.bootloader nuwa-locked

    # ---- System security flags ----
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.secure 1
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.debuggable 0
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.adb.secure 1

    # ---- Build tags (important for banking apps) ----
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.build.tags release-keys
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.build.type user

    # ---- Optional: attestation props (Xiaomi specific) ----
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.product.brand_for_attestation Xiaomi
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.product.manufacturer_for_attestation Xiaomi

    #VBMETA FINGERPRINT ( eb89bd3c... ) ---
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.vbmeta.digest 2a2ae3f99d57f37a6ea9b071ae67f7fd1b376bb9beb29edf88b3b71c6ccd19ca
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.vbmeta.hash_alg sha256
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.vbmeta.size 2368
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.vbmeta.avb_version 1.3
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.vbmeta.invalidate_on_error yes
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.vbmeta.device /dev/block/by-name/vbmeta_a

    #ADDITIONAL ENV PARAMS ---
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.force_normal_boot 1
    exec u:r:init:s0 root root -- /system/bin/q_fix -n ro.boot.slot_suffix _a

    #VENDOR SYNC (FOR HYPEROS/NUWA) ---
    exec u:r:init:s0 root root -- /system/bin/q_fix -n vendor.boot.verifiedbootstate green
    exec u:r:init:s0 root root -- /system/bin/q_fix -n vendor.boot.vbmeta.device_state locked
    exec u:r:init:s0 root root -- /system/bin/q_fix -n vendor.boot.vbmeta.digest 2a2ae3f99d57f37a6ea9b071ae67f7fd1b376bb9beb29edf88b3b71c6ccd19ca
"""


def _q_fix_read_ro_product_odm_device(project_dir: Path) -> str | None:
    """Gom ro.product.odm.device từ mọi build.prop trong project (ưu tiên bản đầu tiên tìm thấy key)."""
    aggregated: dict[str, str] = {}
    try:
        for build_prop_path in project_dir.rglob("build.prop"):
            props = parse_build_prop(build_prop_path)
            if not props:
                continue
            for key, value in props.items():
                if key not in aggregated and value:
                    aggregated[key] = value
    except Exception:
        return None
    dev = aggregated.get("ro.product.odm.device")
    return dev.strip() if dev else None


def q_fix(project_dir: Path) -> None:
    """
    Copy MEZO/q_fix → system …/bin; system_file_contexts; plat_file_contexts; plat_sepolicy.cil
    (type q_fix_exec + typeattributeset exec_type); append khối init.rc.
    """
    src = ROOT_DIR / "MEZO" / "q_fix"
    if not src.exists():
        log("q_fix: bo qua — khong co MEZO/q_fix")
        return

    system_root = resolve_partition_root(project_dir, "system")
    if system_root is None:
        log("q_fix: khong tim thay partition system")
        return

    bin_dir = system_root / "bin"
    try:
        bin_dir.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        log(f"q_fix: khong tao duoc {bin_dir}: {exc}")
        return

    log("\n📌 q_fix: dang copy vao system .../bin ...")
    copied = 0
    try:
        if src.is_file():
            dst = bin_dir / src.name
            shutil.copy2(src, dst)
            copied = 1
            log(f"    Copied {src.name} -> {dst}")
        elif src.is_dir():
            for item in sorted(src.iterdir(), key=lambda p: p.name.lower()):
                if item.is_file():
                    dst = bin_dir / item.name
                    shutil.copy2(item, dst)
                    copied += 1
                    log(f"    Copied {item.name} -> {dst}")
        else:
            log("q_fix: skipped — MEZO/q_fix is not a file or directory")
            return
    except OSError as exc:
        log(f"q_fix: error copying: {exc}")
        return

    if copied == 0:
        log("q_fix: khong co file nao de copy trong MEZO/q_fix")
        return

    contexts_path = project_dir / "config" / "system_file_contexts"
    try:
        contexts_path.parent.mkdir(parents=True, exist_ok=True)
        if contexts_path.is_file():
            existing = contexts_path.read_text(encoding="utf-8", errors="ignore")
            lines = [ln.strip() for ln in existing.splitlines()]
            if Q_FIX_SELINUX_LINE.strip() in lines:
                log("q_fix: system_file_contexts da co dong q_fix, bo qua ghi them")
            else:
                with contexts_path.open("a", encoding="utf-8", newline="\n") as handle:
                    if existing and not existing.endswith("\n"):
                        handle.write("\n")
                    handle.write(Q_FIX_SELINUX_LINE)
                    if not Q_FIX_SELINUX_LINE.endswith("\n"):
                        handle.write("\n")
                log(f"    Da them dong q_fix vao {contexts_path}")
        else:
            contexts_path.write_text(Q_FIX_SELINUX_LINE + "\n", encoding="utf-8")
            log(f"    Da tao {contexts_path} voi dong q_fix")
    except OSError as exc:
        log(f"q_fix: error patching system_file_contexts: {exc}")
    normalize_unix_newlines(contexts_path)

    # plat_file_contexts: chèn sau dòng *cuối cùng* có chứa "/system/bin/"
    plat_fc_path = system_root / "etc" / "selinux" / "plat_file_contexts"
    log("\n📌 q_fix: dang cap nhat plat_file_contexts ...")
    try:
        if not plat_fc_path.is_file():
            log(f"    Canh bao: khong tim thay {plat_fc_path}")
        else:
            plat_text = plat_fc_path.read_text(encoding="utf-8", errors="ignore")
            if "/system/bin/q_fix" in plat_text and "q_fix_exec" in plat_text:
                log("    plat_file_contexts da co q_fix, bo qua")
            else:
                plat_lines = plat_text.splitlines(keepends=True)
                match_indices = [i for i, ln in enumerate(plat_lines) if "/system/bin/" in ln]
                if not match_indices:
                    log("    Canh bao: khong co dong nao chua /system/bin/ — bo qua chen plat_file_contexts")
                else:
                    last_idx = match_indices[-1]
                    insert_line = (
                        Q_FIX_PLAT_FILE_CONTEXTS_LINE + "\n"
                        if not Q_FIX_PLAT_FILE_CONTEXTS_LINE.endswith("\n")
                        else Q_FIX_PLAT_FILE_CONTEXTS_LINE
                    )
                    new_plat = plat_lines[: last_idx + 1] + [insert_line] + plat_lines[last_idx + 1 :]
                    plat_fc_path.write_text("".join(new_plat), encoding="utf-8")
                    log(f"    Da chen dong q_fix sau dong thu {last_idx + 1} trong {plat_fc_path.name}")
    except OSError as exc:
        log(f"q_fix: error patching plat_file_contexts: {exc}")
    normalize_unix_newlines(plat_fc_path)

    
    normalize_unix_newlines(system_root / "etc" / "selinux" / "plat_sepolicy.cil")

    # init.rc: etc/init/hw/init.rc trong partition system (system_root = …/system/system hoặc …/system)
    init_rc_path = system_root / "etc" / "init" / "hw" / "init.rc"
    log("\n📌 q_fix: dang cap nhat init.rc ...")
    device_codename = _q_fix_read_ro_product_odm_device(project_dir)
    init_block = Q_FIX_INIT_RC_APPEND
    if device_codename:
        init_block = init_block.replace("nuwa-locked", f"{device_codename}-locked", 1)
        log(f"    ro.bootloader -> {device_codename}-locked (ro.product.odm.device)")
    else:
        log("    Canh bao: khong doc duoc ro.product.odm.device, giu nguyen nuwa-locked")

    try:
        if not init_rc_path.is_file():
            log(f"    Canh bao: khong tim thay {init_rc_path}")
        else:
            existing_rc = init_rc_path.read_text(encoding="utf-8", errors="ignore")
            if Q_FIX_INIT_RC_MARKER in existing_rc:
                log("    init.rc da co block q_fix (marker), bo qua append")
            else:
                with init_rc_path.open("a", encoding="utf-8", newline="\n") as rc_handle:
                    if existing_rc and not existing_rc.endswith("\n"):
                        rc_handle.write("\n")
                    rc_handle.write(init_block)
                    if not init_block.endswith("\n"):
                        rc_handle.write("\n")
                log(f"    Da append khoi q_fix vao {init_rc_path}")
    except OSError as exc:
        log(f"q_fix: error patching init.rc: {exc}")
    normalize_unix_newlines(init_rc_path)

    log("🎉 q_fix complete.")


def clean_system_framework_arch_dirs(project_dir: Path) -> None:
    system_root = resolve_partition_root(project_dir, "system")
    if system_root is None:
        log("System partition not found; cannot clean framework arch directories.")
        return

    framework_dir = system_root / "framework"
    if not framework_dir.is_dir():
        log(f"Framework directory not found: {framework_dir}")
        return

    removed_any = False
    for dir_name in ("arm", "arm64", "oat"):
        target_dir = framework_dir / dir_name
        if not target_dir.exists():
            continue

        if remove_path_force(target_dir):
            log(f"    Removed framework/{dir_name}")
            removed_any = True
        else:
            log(f"    Warning: could not remove directory {target_dir}")

    if not removed_any:
        log("    No arm/arm64/oat directories in system/framework to remove.")


def resolve_tool_jar(tool_name: str) -> Path | None:
    tool_path = ROOT_DIR / tool_name
    if tool_path.is_file():
        return tool_path
    return None


def prepare_smali_tools(work_dir: Path) -> tuple[Path | None, Path | None]:
    baksmali_src = resolve_tool_jar("baksmali.jar")
    smali_src = resolve_tool_jar("smali.jar")
    baksmali_dst = work_dir / "baksmali.jar"
    smali_dst = work_dir / "smali.jar"

    for src, dst, label in (
        (baksmali_src, baksmali_dst, "baksmali.jar"),
        (smali_src, smali_dst, "smali.jar"),
    ):
        if src is None:
            log(f"{label} not found at {ROOT_DIR}")
            continue
        try:
            if not dst.exists():
                shutil.copy2(src, dst)
                log(f"    Copied {label} to {work_dir}")
        except Exception as exc:
            log(f"    Loi khi copy {label}: {exc}")

    return (
        baksmali_dst if baksmali_dst.is_file() else baksmali_src,
        smali_dst if smali_dst.is_file() else smali_src,
    )


def prepare_auxiliary_work_files(work_dir: Path) -> None:
    dex_redivision_src = ROOT_DIR / "DexRedivision.txt"
    dex_redivision_dst = work_dir / "DexRedivision.txt"
    if dex_redivision_src.is_file():
        try:
            if not dex_redivision_dst.exists():
                shutil.copy2(dex_redivision_src, dex_redivision_dst)
                log(f"    Copied DexRedivision.txt to {work_dir}")
        except Exception as exc:
            log(f"    Loi khi copy DexRedivision.txt: {exc}")


def dex_redivision(work_dir: Path) -> None:
    """
    Đọc DexRedivision.txt: copy các file .smali được liệt kê từ smali_classes … smali_classes5
    sang smali_classes6 (giữ cấu trúc thư mục), rồi xóa bản gốc ở thư mục nguồn.
    Logic theo AutoPatchFramework a16.py (bỏ input/pause, dùng log).
    """
    framework_unpacked_dir = work_dir / "framework_unpacked"
    if not framework_unpacked_dir.is_dir():
        log(f"    Dex redivision: bo qua — khong co {framework_unpacked_dir}")
        return

    dex_redivision_file = work_dir / "DexRedivision.txt"
    if not dex_redivision_file.is_file():
        log(f"    Dex redivision: bo qua — khong co {dex_redivision_file}")
        return

    log("\n📦 Processing Dex redivision...")
    log("📝 Doc DexRedivision.txt va copy sang framework_unpacked/smali_classes6...")

    try:
        text = dex_redivision_file.read_text(encoding="utf-8", errors="ignore")
        target_files = [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#")]
    except OSError as exc:
        log(f"    ❌ Loi khi doc DexRedivision.txt: {exc}")
        return

    if not target_files:
        log("    Dex redivision: bo qua — DexRedivision.txt rong hoac chi comment")
        return

    log(f"    Da doc {len(target_files)} ten file tu DexRedivision.txt")

    # smali_classes, smali_classes2 … smali_classes5 (khong dung smali_classes1)
    source_dir_names = ["smali_classes"] + [f"smali_classes{n}" for n in range(2, 6)]
    source_dirs: list[Path] = []
    for dir_name in source_dir_names:
        dir_path = framework_unpacked_dir / dir_name
        if dir_path.is_dir():
            source_dirs.append(dir_path)
            log(f"  ✅ Tim thay {dir_name}")
        else:
            log(f"  ⚠️  Khong tim thay {dir_name}")

    if not source_dirs:
        log("    ❌ smali_classes ... smali_classes5 not found")
        return

    target_dir = framework_unpacked_dir / "smali_classes6"
    target_dir.mkdir(parents=True, exist_ok=True)
    log(f"\n📁 Thu muc dich: smali_classes6")

    found_files: list[tuple[str, str]] = []
    not_found_files: list[str] = []
    files_to_delete: list[Path] = []
    copy_count = 0

    log("\n🔍 Searching and copying...")
    for filename in target_files:
        file_found = False
        for source_dir in source_dirs:
            for smali_file in source_dir.rglob(filename):
                if smali_file.is_file() and smali_file.name == filename:
                    relative_path = smali_file.relative_to(source_dir)
                    target_file_path = target_dir / relative_path
                    try:
                        target_file_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(smali_file, target_file_path)
                        found_files.append((filename, str(relative_path)))
                        files_to_delete.append(smali_file)
                        copy_count += 1
                        file_found = True
                        break
                    except OSError as exc:
                        log(f"  ❌ Loi khi copy {filename}: {exc}")
                        file_found = True
                        break
            if file_found:
                break
        if not file_found:
            not_found_files.append(filename)

    log(f"  ✅ Da copy {copy_count} file")

    if files_to_delete:
        log("\n🗑️  Removing old files in smali_classes … smali_classes5...")
        deleted_count = 0
        failed_count = 0
        for source_file in files_to_delete:
            try:
                if source_file.exists():
                    source_file.unlink()
                    deleted_count += 1
            except OSError as exc:
                log(f"  ⚠️  Khong the xoa {source_file}: {exc}")
                failed_count += 1
        log(f"  ✅ Da xoa: {deleted_count} file")
        if failed_count:
            log(f"  ⚠️  Khong the xoa: {failed_count} file")

    log(f"\n📊 Ket qua Dex redivision:")
    log(f"  ✅ Tim thay va copy: {len(found_files)} file")
    if not_found_files:
        log(f"  ❌ Khong tim thay: {len(not_found_files)} file")
        if len(not_found_files) <= 20:
            for name in not_found_files:
                log(f"    - {name}")
        else:
            for name in not_found_files[:20]:
                log(f"    - {name}")
            log(f"    ... va {len(not_found_files) - 20} file khac")

    if target_dir.exists():
        total_smali = len(list(target_dir.rglob("*.smali")))
        log(f"\n📁 Tong so file .smali trong smali_classes6: {total_smali}")

    log("\n🎉 Dex redivision complete!")


def move_framework_jars_to_cwd(project_dir: Path, work_dir: Path | None = None) -> None:
    dest_dir = work_dir or project_dir

    tasks = [
        (resolve_partition_file(project_dir, "system", "framework", "framework.jar"), "framework.jar"),
        (resolve_partition_file(project_dir, "system", "framework", "services.jar"), "services.jar"),
        (resolve_partition_file(project_dir, "system_ext", "framework", "miui-framework.jar"), "miui-framework.jar"),
        (resolve_partition_file(project_dir, "system_ext", "framework", "miui-services.jar"), "miui-services.jar"),
    ]

    log(f"Exporting framework/services jar files to: {dest_dir}")

    for src, label in tasks:
        try:
            if src is None or not src.is_file():
                log(f"    Not found: {label}")
                continue

            dst = dest_dir / label
            if dst.exists():
                remove_path_force(dst)

            # Giu lai file goc trong partition de tranh lam hong luong repack.
            shutil.copy2(src, dst)
            log(f"    Exported: {label} -> {dst}")
        except Exception as exc:
            log(f"    Loi khi xuat {label}: {exc}")


def unpack_framework_jars_and_classes(work_dir: Path | None = None) -> None:
    wd = work_dir or ROOT_DIR
    baksmali_jar, _smali_jar = prepare_smali_tools(wd)

    jar_to_unpack_dir = {
        "framework.jar": "framework_unpacked",
        "services.jar": "services_unpacked",
        "miui-framework.jar": "miui_framework_unpacked",
        "miui-services.jar": "miui_services_unpacked",
    }

    has_baksmali = baksmali_jar is not None and baksmali_jar.is_file()
    if not has_baksmali:
        log("baksmali.jar not found. Will only extract JAR, skipping DEX -> smali decompile.")

    for jar_name, out_dir_name in jar_to_unpack_dir.items():
        jar_path = wd / jar_name
        if not jar_path.is_file():
            continue

        out_dir = wd / out_dir_name
        log(f"Extracting {jar_name} -> {out_dir_name} ...")

        try:
            if out_dir.exists():
                remove_path_force(out_dir)
            out_dir.mkdir(parents=True, exist_ok=True)

            with zipfile.ZipFile(jar_path, "r") as zip_file:
                zip_file.extractall(out_dir)

            log(f"    Extracted: {jar_name}")
        except Exception as exc:
            log(f"    Error extracting {jar_name}: {exc}")
            continue

        dex_files = sorted(out_dir.rglob("*.dex"))
        if not dex_files:
            log("    No DEX files found in JAR")
            continue

        log(f"    Found {len(dex_files)} DEX file(s)")
        if not has_baksmali:
            continue

        for dex_path in dex_files:
            dex_stem = dex_path.stem
            smali_out = out_dir / f"smali_{dex_stem}"
            try:
                if smali_out.exists():
                    remove_path_force(smali_out)
                smali_out.mkdir(parents=True, exist_ok=True)

                cmd = [
                    "java",
                    "-jar",
                    str(baksmali_jar),
                    "d",
                    str(dex_path),
                    "-o",
                    str(smali_out),
                ]
                subprocess.run(cmd, capture_output=True, text=True, check=True)
                log(f"    Da decompile {dex_path.name} -> {smali_out.name}")
            except subprocess.CalledProcessError as exc:
                err = (exc.stderr or "").strip()
                if err:
                    log(f"    Loi baksmali {dex_path.name}: {err}")
                else:
                    log(f"    Loi baksmali {dex_path.name} (exit code {exc.returncode})")
            except Exception as exc:
                log(f"    Loi khi decompile {dex_path.name}: {exc}")


def restore_repacked_jars_to_project(project_dir: Path, work_dir: Path | None = None) -> None:
    wd = work_dir or project_dir
    tasks = [
        (wd / "framework.jar", resolve_partition_file(project_dir, "system", "framework", "framework.jar"), "framework.jar"),
        (wd / "services.jar", resolve_partition_file(project_dir, "system", "framework", "services.jar"), "services.jar"),
        (wd / "miui-framework.jar", resolve_partition_file(project_dir, "system_ext", "framework", "miui-framework.jar"), "miui-framework.jar"),
        (wd / "miui-services.jar", resolve_partition_file(project_dir, "system_ext", "framework", "miui-services.jar"), "miui-services.jar"),
    ]

    log("Khoi phuc cac file jar da repack ve lai project...")

    for src, dst, label in tasks:
        try:
            if not src.is_file():
                log(f"    Skipping {label}: source not found at {src}")
                continue
            if dst is None:
                log(f"    Skipping {label}: destination not found in partition")
                continue

            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            log(f"    Da khoi phuc {label} -> {dst}")
            if remove_path_force(src):
                log(f"    Da xoa file tam sau khi khoi phuc: {src}")
            else:
                log(f"    Warning: could not remove temp file after restore: {src}")
        except Exception as exc:
            log(f"    Loi khi khoi phuc {label} toi {dst}: {exc}")

    for extra_file in ("baksmali.jar", "smali.jar", "DexRedivision.txt"):
        extra_path = wd / extra_file
        if not extra_path.exists():
            continue
        if remove_path_force(extra_path):
            log(f"    Da xoa file tam: {extra_path}")
        else:
            log(f"    Warning: could not remove temp file: {extra_path}")

    # Don dep cac file jar du co the con sot lai o thu muc goc tu cac lan chay cu.
    if wd.resolve() != ROOT_DIR.resolve():
        for root_jar in (
            "framework.jar",
            "services.jar",
            "miui-framework.jar",
            "miui-services.jar",
        ):
            root_path = ROOT_DIR / root_jar
            if not root_path.exists():
                continue
            if remove_path_force(root_path):
                log(f"    Removed leftover jar from root directory: {root_path}")
            else:
                log(f"    Warning: could not remove leftover jar at root: {root_path}")


def repack_all_classes(work_dir: Path | None = None) -> None:
    wd = work_dir or ROOT_DIR
    _baksmali_jar, smali_jar = prepare_smali_tools(wd)
    if smali_jar is None or not smali_jar.is_file():
        log("smali.jar not found; cannot repack classes.")
        return

    log("Starting repack of all smali_classes directories...")
    unpacked_dirs: list[Path] = []
    for base_name in (
        "framework_unpacked",
        "services_unpacked",
        "miui_framework_unpacked",
        "miui_services_unpacked",
    ):
        base_dir = wd / base_name
        if not base_dir.exists():
            continue
        for item in sorted(base_dir.iterdir()):
            if item.is_dir() and item.name.startswith("smali_classes"):
                unpacked_dirs.append(item)

    if not unpacked_dirs:
        log("No smali_classes directory found to repack.")
        return

    for dir_path in unpacked_dirs:
        try:
            log(f"Repacking {dir_path.name}...")
            output_file = dir_path.name.replace("smali_", "") + ".dex"
            output_path = dir_path.parent / output_file
            cmd = [
                "java",
                "-jar",
                str(smali_jar),
                "a",
                str(dir_path),
                "-o",
                str(output_path),
                "--api",
                "33",
            ]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                log(f"    Repacked -> {output_file}")
                if remove_path_force(dir_path):
                    log(f"    Removed directory {dir_path}")
                else:
                    log(f"    Warning: could not remove directory {dir_path}")
            else:
                log(f"    Loi khi repack {dir_path.name}: {(result.stderr or '').strip()}")
        except Exception as exc:
            log(f"    Loi khi repack {dir_path.name}: {exc}")


def repack_all_jar_files(work_dir: Path | None = None) -> None:
    wd = work_dir or ROOT_DIR
    log("Starting repack of all *_unpacked directories...")

    unpacked_dirs = [
        ("framework.jar", wd / "framework_unpacked"),
        ("services.jar", wd / "services_unpacked"),
        ("miui-framework.jar", wd / "miui_framework_unpacked"),
        ("miui-services.jar", wd / "miui_services_unpacked"),
    ]

    found_any = False
    for jar_name, dir_path in unpacked_dirs:
        if not dir_path.exists():
            continue
        found_any = True
        try:
            log(f"Repacking {dir_path.name} into {jar_name}...")
            cmd = ["jar", "cfM", str(wd / jar_name), "-C", str(dir_path), "."]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                log(f"    Repacked -> {jar_name}")
                if remove_path_force(dir_path):
                    log(f"    Removed directory {dir_path}")
                else:
                    log(f"    Warning: could not remove directory {dir_path}")
            else:
                log(f"    Loi khi repack {dir_path.name}: {(result.stderr or '').strip()}")
        except Exception as exc:
            log(f"    Loi khi repack {dir_path.name}: {exc}")

    if not found_any:
        log("No unpacked directory found to repack.")


def apply_language_overlay(project_dir: Path, mi_incremental: str) -> None:
    if not mi_incremental or len(mi_incremental) < 3:
        return

    prefix = mi_incremental[:3]
    script_dir = Path(__file__).parent
    src_dirs = []

    os_lang_dir = script_dir / "MEZO_OVERLAY" / f"{prefix}_language"
    if os_lang_dir.is_dir():
        src_dirs.append(os_lang_dir)

    common_overlay_dir = script_dir / "MEZO_OVERLAY" / "overlay"
    if common_overlay_dir.is_dir():
        src_dirs.append(common_overlay_dir)

    if not src_dirs:
        return

    dest_dir = resolve_partition_file(project_dir, "vendor", "overlay")
    if dest_dir is None:
        log("Vendor/overlay partition not found for overlay addition.")
        return

    dest_dir.mkdir(parents=True, exist_ok=True)
    log("Them cac goi overlay...")

    for src_dir in src_dirs:
        apk_files = list(src_dir.glob("*.apk"))
        if not apk_files:
            continue

        for apk in apk_files:
            try:
                target = dest_dir / apk.name
                shutil.copy2(apk, target)
                log(f"    Da them: {apk.name}")
            except Exception as exc:
                log(f"    Loi khi copy {apk}: {exc}")


def apply_version_specific_apks(project_dir: Path, mi_incremental: str, major: int | None) -> None:
    if not mi_incremental or len(mi_incremental) < 3:
        return

    prefix = mi_incremental[:3]
    if major is not None:
        prefix = f"{prefix}_{major}"
    script_dir = Path(__file__).parent
    src_dir = script_dir / "MEZO_APP" / prefix
    if not src_dir.is_dir():
        return

    apk_files = list(src_dir.glob("*.apk"))
    if not apk_files:
        return

    log(f"Thay the apk theo phien ban {prefix} trong MEZO_APP/{prefix}...")

    for apk in apk_files:
        try:
            matches = list(project_dir.rglob(apk.name))
            if not matches:
                log(f"    Khong tim thay trong project: {apk.name}")
                continue

            for target in matches:
                try:
                    shutil.copy2(apk, target)
                    log(f"    Da thay the: {apk.name}")
                except Exception as exc:
                    log(f"    Loi khi thay the {target}: {exc}")
        except Exception as exc:
            log(f"    Loi khi xu ly {apk}: {exc}")


def normalize_unix_newlines(path: Path) -> None:
    try:
        if not path.is_file():
            return
        data = path.read_bytes()
        data = data.replace(b"\r\n", b"\n")
        data = data.replace(b"\r", b"\n")
        path.write_bytes(data)
    except Exception as exc:
        log(f"    Canh bao: khong chuan hoa duoc newline cho {path.name}: {exc}")


def append_custom_build_prop(project_dir: Path) -> None:
    script_dir = Path(__file__).parent
    src_prop = script_dir / "build.prop"
    dest_prop = resolve_partition_file(project_dir, "system", "build.prop")

    if not src_prop.is_file():
        log(f"Source build.prop not found: {src_prop}")
    elif dest_prop is None or not dest_prop.is_file():
        log("Khong tim thay file dich build.prop trong partition system.")
    else:
        try:
            src_content = src_prop.read_text(encoding="utf-8", errors="ignore")
            if src_content:
                with dest_prop.open("a", encoding="utf-8", errors="ignore") as dest_file:
                    dest_file.write("\n")
                    dest_file.write(src_content)
                log("    Da them noi dung build.prop tuy chinh")
        except Exception as exc:
            log(f"Error merging build.prop: {exc}")

    device_value: str | None = None
    try:
        aggregated: dict[str, str] = {}
        for build_prop_path in project_dir.rglob("build.prop"):
            props = parse_build_prop(build_prop_path)
            if not props:
                continue
            for key, value in props.items():
                if key not in aggregated and value:
                    aggregated[key] = value
        device_value = aggregated.get("ro.product.odm.device")
    except Exception:
        device_value = None

    device_features_dir = resolve_partition_file(project_dir, "product", "etc", "device_features")
    if device_features_dir is not None and device_features_dir.is_dir():
        fps_pattern = re.compile(
            r'(<integer-array\s+name="fpsList"[^>]*>)(.*?)(</integer-array>)',
            re.DOTALL,
        )

        for xml_path in device_features_dir.glob("*.xml"):
            try:
                content = xml_path.read_text(encoding="utf-8", errors="ignore")
                original_content = content
                changed = False

                def _add_fps_items(match: re.Match[str]) -> str:
                    header = match.group(1)
                    body = match.group(2)
                    footer = match.group(3)

                    if "<item>1</item>" not in body:
                        body = body.rstrip() + "\n        <item>1</item>\n"
                    if "<item>90</item>" not in body:
                        body = body.rstrip() + "\n        <item>90</item>\n"

                    return f"{header}{body}{footer}"

                new_content, count = fps_pattern.subn(_add_fps_items, content)
                if count > 0:
                    content = new_content
                    changed = True

                lines_to_ensure = [
                    '<bool name="support_video_idle_dim">true</bool>',
                    '<bool name="support_game_dim">true</bool>',
                    f'<string name="support_virtual_call">{device_value}</string>',
                    '<bool name="support_video_dfps">true</bool>',
                    '<bool name="support_aod_fullscreen">true</bool>',
                    '<bool name="support_power_save_new">true</bool>',
                    '<bool name="bluetooth_call_enable">true</bool>',
                    '<integer name="default_eyecare_mode">2</integer>',
                    '<bool name="support_smart_eyecare">true</bool>',
                    '<bool name="support_wild_boost">true</bool>',
                    '<bool name="support_wild_boost_bat_perf">true</bool>',
                ]

                need_insert_block = any(line not in content for line in lines_to_ensure)
                if need_insert_block and "Unkonwn properties BEGIN" in content:
                    insert_block = "".join(f"    {line}\n" for line in lines_to_ensure)
                    marker = "Unkonwn properties BEGIN"
                    new_lines: list[str] = []
                    inserted_here = False
                    for line in content.splitlines(keepends=True):
                        new_lines.append(line)
                        if (not inserted_here) and (marker in line):
                            new_lines.append(insert_block)
                            inserted_here = True

                    if inserted_here:
                        content = "".join(new_lines)
                        changed = True

                if changed and content != original_content:
                    xml_path.write_text(content, encoding="utf-8", errors="ignore")
                    log(f"    Da chinh sua device_features: {xml_path.name}")
            except Exception as exc:
                log(f"Error editing {xml_path}: {exc}")

    cust_keys_path = resolve_partition_file(project_dir, "system_ext", "etc", "cust_prop_white_keys_list")
    try:
        if cust_keys_path is not None and cust_keys_path.is_file():
            lines = cust_keys_path.read_text(encoding="utf-8", errors="ignore").splitlines()
            if "ro.crypto.state" not in (line.strip() for line in lines):
                lines.append("ro.crypto.state")
                cust_keys_path.write_text("\n".join(lines) + "\n", encoding="utf-8", errors="ignore")
                log("    Da them ro.crypto.state vao cust_prop_white_keys_list")
    except Exception as exc:
        log(f"Error editing cust_prop_white_keys_list: {exc}")

    fstab_path = resolve_partition_file(project_dir, "vendor", "etc", "fstab.qcom")
    try:
        if fstab_path is not None and fstab_path.is_file():
            fstab_content = fstab_path.read_text(encoding="utf-8", errors="ignore")
            to_remove = [
                "avb=vbmeta_system,",
                "avb_keys=/avb/q-gsi.avbpubkey:/avb/r-gsi.avbpubkey:/avb/s-gsi.avbpubkey:/avb/t-gsi.avbpubkey:/avb/u-gsi.avbpubkey",
                "avb=vbmeta,",
                "inlinecrypt,",
                ",atgc,age_extent_cache",
                "fileencryption=aes-256-xts:aes-256-cts:v2+inlinecrypt_optimized+wrappedkey_v0,keydirectory=/metadata/vold/metadata_encryption,metadata_encryption=aes-256-xts:wrappedkey_v0,quota,",
            ]

            lines_in = fstab_content.splitlines(keepends=True)
            processed_lines: list[str] = []
            target_line_substr = "/dev/block/bootdevice/by-name/userdata                  /data                  mifs"

            for line in lines_in:
                if target_line_substr in line:
                    continue

                if line.lstrip().startswith("overlay "):
                    if "camera" in line:
                        processed_lines.append(line)
                    continue

                body = line.rstrip("\r\n")
                newline = line[len(body):]

                for token in to_remove:
                    if token in body:
                        body = body.replace(token, "")

                while ",," in body:
                    body = body.replace(",,", ",")
                if body.endswith(","):
                    body = body[:-1]

                processed_lines.append(body + newline)

            new_fstab_content = "".join(processed_lines)
            lines = new_fstab_content.splitlines(keepends=True)

            def _ensure_ext4_mount(current_lines: list[str], erofs_substr: str, ext4_line: str) -> list[str]:
                has_erofs = any(erofs_substr in ln for ln in current_lines)
                if not has_erofs:
                    return current_lines

                ext4_tokens = ext4_line.split()
                for ln in current_lines:
                    tokens = ln.split()
                    if len(tokens) >= 3 and tokens[0:3] == ext4_tokens[0:3]:
                        return current_lines

                new_lines: list[str] = []
                inserted = False
                for ln in current_lines:
                    new_lines.append(ln)
                    if (not inserted) and (erofs_substr in ln):
                        new_lines.append(ext4_line + "\n")
                        inserted = True
                return new_lines

            lines = _ensure_ext4_mount(
                lines,
                "system_ext                                              /system_ext            erofs",
                "system_ext                                              /system_ext            ext4    ro,barrier=1,discard                                 wait,slotselect,logical,first_stage_mount",
            )
            lines = _ensure_ext4_mount(
                lines,
                "product                                                 /product               erofs",
                "product                                                 /product               ext4    ro,barrier=1,discard                                 wait,slotselect,logical,first_stage_mount",
            )
            lines = _ensure_ext4_mount(
                lines,
                "vendor                                                  /vendor                erofs",
                "vendor                                                  /vendor                ext4    ro,barrier=1,discard                                 wait,slotselect,logical,first_stage_mount",
            )
            lines = _ensure_ext4_mount(
                lines,
                "odm                                                     /odm                   erofs",
                "odm                                                     /odm                   ext4    ro,barrier=1,discard                                 wait,slotselect,logical,first_stage_mount",
            )

            vm_bootsys_line = (
                "/dev/block/bootdevice/by-name/vm-bootsys                /product/vm-system     ext4    ro,nosuid,nodev,barrier=1                            wait,slotselect\n"
            )
            vm_persist_line = (
                "/dev/block/bootdevice/by-name/vm-persist                /mnt/product/vm-persist     ext4    noatime,nosuid,nodev,barrier=1                  wait\n"
            )

            def _ensure_line(current_lines: list[str], line_text: str) -> list[str]:
                if line_text in current_lines:
                    return current_lines

                new_lines: list[str] = []
                inserted = False
                bluetooth_substr = "/dev/block/bootdevice/by-name/bluetooth"
                for current_line in current_lines:
                    if (not inserted) and (bluetooth_substr in current_line):
                        new_lines.append(line_text)
                        inserted = True
                    new_lines.append(current_line)

                if not inserted:
                    new_lines.append(line_text)
                return new_lines

            lines = _ensure_line(lines, vm_bootsys_line)
            lines = _ensure_line(lines, vm_persist_line)
            new_fstab_content = "".join(lines)

            if new_fstab_content != fstab_content:
                fstab_path.write_text(new_fstab_content, encoding="utf-8", errors="ignore")
                normalize_unix_newlines(fstab_path)
                log("    Da chinh sua fstab.qcom")
    except Exception as exc:
        log(f"Error editing fstab.qcom: {exc}")

    mi_ext_build_prop_path = resolve_partition_file(project_dir, "mi_ext", "etc", "build.prop")
    try:
        if mi_ext_build_prop_path is not None and mi_ext_build_prop_path.is_file():
            lines = mi_ext_build_prop_path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
            original_lines = lines
            lines = [
                line
                for line in lines
                if "ro.miui.support.system.app.uninstall.v2" not in line
            ]
            if lines != original_lines:
                with mi_ext_build_prop_path.open("w", encoding="utf-8", errors="ignore") as file:
                    file.writelines(lines)
                log("    Da xoa dong ro.miui.support.system.app.uninstall.v2 trong mi_ext build.prop")
    except Exception as exc:
        log(f"Error removing lines from mi_ext build.prop: {exc}")

    wifi_rc_dest = project_dir / "system" / "system" / "etc" / "init" / "wifi.rc"
    try:
        if wifi_rc_dest.is_file():
            wifi_rc_src = ROOT_DIR / "wifi.rc"
            if wifi_rc_src.is_file():
                src_content = wifi_rc_src.read_text(encoding="utf-8", errors="ignore")
                if src_content:
                    with wifi_rc_dest.open("a", encoding="utf-8", errors="ignore") as dest_file:
                        dest_file.write(src_content)
                    normalize_unix_newlines(wifi_rc_dest)
                    log("    Da noi noi dung wifi.rc vao system_a wifi.rc")
                else:
                    log("    File wifi.rc nguon rong, khong noi.")
            else:
                log(f"Khong tim thay file wifi.rc nguon: {wifi_rc_src}")
        else:
            log(f"Khong tim thay wifi.rc dich: {wifi_rc_dest}")
    except Exception as exc:
        log(f"Error processing wifi.rc: {exc}")

    perfinit_path = resolve_partition_file(project_dir, "system_ext", "etc", "perfinit.conf")
    try:
        if perfinit_path is not None and perfinit_path.is_file():
            content = perfinit_path.read_text(encoding="utf-8", errors="ignore")
            original_content = content

            old_text = '"swap_on": 1,\n        "global_swappiness": 100,\n        "page_cluster": -1,\n        "zram_size": {\n            "def":512,"2":1024,"3":1536,"4":2252,"6":4096,"8":6144,"10":6144,"12":8192,"16":14336,"18":14336,"20":15360,"24":15360,"32":16384\n        },\n        "extm_on": 1,\n        "extm_size": {\n            "def":1024, "high_device":3072, "3+64":1024, "4+64":1024, "6+64":2048, "4+128":2048, "6+128":2048\n        },'
            new_text = '"swap_on": 0,\n        "global_swappiness": 0,\n          "page_cluster": 0,\n         "zram_size": {\n            "def":0\n        },\n        "extm_on": 0,\n        "extm_size": {\n            "def":0\n        },'

            if old_text in content:
                content = content.replace(old_text, new_text)
            else:
                pattern = r'"swap_on":\s*1,\s*"global_swappiness":\s*100,\s*"page_cluster":\s*-1,\s*"zram_size":\s*\{\s*"def":512[^}]*\},\s*"extm_on":\s*1,\s*"extm_size":\s*\{\s*"def":1024[^}]*\},'
                if re.search(pattern, content, re.DOTALL):
                    content = re.sub(pattern, new_text, content, flags=re.DOTALL)

            if content != original_content:
                perfinit_path.write_text(content, encoding="utf-8", errors="ignore")
                normalize_unix_newlines(perfinit_path)
                log("    Da chinh sua perfinit.conf: tat swap va zram")
    except Exception as exc:
        log(f"Error editing perfinit.conf: {exc}")

    mcd_default_path = resolve_partition_file(project_dir, "system_ext", "etc", "mcd_default.conf")
    try:
        if mcd_default_path is not None and mcd_default_path.is_file():
            content = mcd_default_path.read_text(encoding="utf-8", errors="ignore")
            original_content = content

            old_memory_opt = '"memory_opt": {\n    "zram_device_num": 1,\n    "zram_size_MB": "512 1536:1024 2560:1536 3256:2252 4915:2560 6553:4048 8892:4048 12888:0",\n    "global_swappiness": 60,\n    "more_memory_swappiness":60\n},'
            new_memory_opt = '"memory_opt": {\n    "zram_device_num": 0,\n    "zram_size_MB": "0",\n    "global_swappiness": 0,\n    "more_memory_swappiness": 0\n},'

            if old_memory_opt in content:
                content = content.replace(old_memory_opt, new_memory_opt)
            else:
                pattern_memory = r'"memory_opt":\s*\{\s*"zram_device_num":\s*1,\s*"zram_size_MB":\s*"[^"]*",\s*"global_swappiness":\s*60,\s*"more_memory_swappiness":\s*60\s*\},'
                if re.search(pattern_memory, content, re.DOTALL):
                    content = re.sub(pattern_memory, new_memory_opt, content, flags=re.DOTALL)

            if content != original_content:
                mcd_default_path.write_text(content, encoding="utf-8", errors="ignore")
                normalize_unix_newlines(mcd_default_path)
                log("    Da chinh sua mcd_default.conf: tat memory_opt")
    except Exception as exc:
        log(f"Error editing mcd_default.conf: {exc}")


def convert_sparse_super_to_raw(super_img: Path, output_dir: Path) -> Path:
    raw_super = output_dir / "super_raw.img"

    with open(super_img, "rb") as fd:
        sparse = SparseImage(fd)
        if not sparse.check():
            log("super.img is not sparse; skipping conversion.")
            return super_img

    log("[3/4] super.img is sparse; converting to raw...")
    if raw_super.exists():
        raw_super.unlink()

    with open(super_img, "rb") as fd:
        sparse = SparseImage(fd)
        converted_path = Path(sparse.unsparse())

    shutil.move(str(converted_path), str(raw_super))
    log(f"Converted sparse super.img to raw: {raw_super}")
    return raw_super


def unpack_super(super_img: Path, output_dir: Path) -> Path:
    super_out_dir = output_dir / "super"
    ensure_clean_dir(super_out_dir)

    raw_super_img = convert_sparse_super_to_raw(super_img, output_dir)
    log(f"[4/4] Unpacking super.img: {raw_super_img}")
    lpunpack_unpack(str(raw_super_img), str(super_out_dir))
    temp_raw_super = output_dir / "super_raw.img"
    if raw_super_img == temp_raw_super and temp_raw_super.exists():
        temp_raw_super.unlink()
        log(f"Removed temporary raw super: {temp_raw_super}")
    return super_out_dir


def write_super_config(output_dir: Path, super_img: Path) -> None:
    config_dir = output_dir / "config"
    ensure_clean_dir(config_dir)

    super_info = lpunpack_get_info(str(super_img))
    JsonEdit(str(config_dir / "parts_info")).write({"super_info": super_info})
    with open(config_dir / "super", "w", encoding="utf-8", newline="\n") as super_file:
        json.dump(super_info, super_file, indent=4, ensure_ascii=False)

    reference_common_context = REFERENCE_CONFIG_DIR / "file_contexts"
    if reference_common_context.exists() and not (config_dir / "file_contexts").exists():
        shutil.copy2(reference_common_context, config_dir / "file_contexts")


def seed_partition_config(config_dir: Path, part_name: str, fs_type: str, part_dir: Path) -> None:
    fs_config_path = config_dir / f"{part_name}_fs_config"
    contexts_path = config_dir / f"{part_name}_file_contexts"
    fs_options_path = config_dir / f"{part_name}_fs_options"

    reference_fs_config = REFERENCE_CONFIG_DIR / fs_config_path.name
    reference_contexts = REFERENCE_CONFIG_DIR / contexts_path.name
    reference_fs_options = REFERENCE_CONFIG_DIR / fs_options_path.name

    if reference_fs_config.exists() and not fs_config_path.exists():
        shutil.copy2(reference_fs_config, fs_config_path)
    if reference_contexts.exists() and not contexts_path.exists():
        shutil.copy2(reference_contexts, contexts_path)
    if reference_fs_options.exists() and not fs_options_path.exists():
        shutil.copy2(reference_fs_options, fs_options_path)

    if not fs_config_path.exists():
        root_gid = "2000" if part_name == "vendor" else "0"
        with open(fs_config_path, "w", encoding="utf-8", newline="\n") as fs_file:
            fs_file.write(f"/ 0 {root_gid} 0755\n")
            fs_file.write(f"{part_name} 0 {root_gid} 0755\n")
            fs_file.write(f"{part_name}/ 0 {root_gid} 0755\n")
            fs_file.write(f"{part_name}/lost+found 0 {root_gid} 0700\n")

    if not contexts_path.exists():
        with open(contexts_path, "w", encoding="utf-8", newline="\n") as contexts_file:
            contexts_file.write("/ u:object_r:rootfs:s0\n")
            contexts_file.write(f"/{part_name} u:object_r:rootfs:s0\n")
            contexts_file.write(f"/{part_name}/ u:object_r:rootfs:s0\n")
            contexts_file.write(f"/{part_name}/lost\\+found u:object_r:rootfs:s0\n")
            contexts_file.write(f"/{part_name}(/.*)? u:object_r:system_file:s0\n")

    if not fs_options_path.exists():
        fs_options = [
            "Filesystem created:        unknown",
            "Filesystem UUID:           unknown",
        ]
        if fs_type == "erofs":
            fs_options.append(
                "mkfs.erofs options:        "
                f"-zlz4hc -T 0 --mount-point=/{part_name} "
                f"--fs-config-file={fs_config_path} "
                f"--file-contexts={contexts_path} "
                f"{part_name}_repack.img {part_dir}"
            )
        else:
            fs_options.append(
                f"filesystem:               {fs_type} mount-point=/{part_name}"
            )
        with open(fs_options_path, "w", encoding="utf-8", newline="\n") as fs_options_file:
            fs_options_file.write("\n".join(fs_options) + "\n")


def normalize_partition_images(super_out_dir: Path, output_dir: Path) -> list[Path]:
    normalized_images = []
    for img_path in sorted(super_out_dir.glob("*.img")):
        file_name = img_path.name
        if file_name.endswith("_b.img") and img_path.stat().st_size == 0:
            continue
        if not file_name.endswith("_a.img"):
            continue

        part_name = file_name[:-6]
        normalized_img = output_dir / f"{part_name}.img"
        if normalized_img.exists():
            normalized_img.unlink()
        shutil.copy2(img_path, normalized_img)
        normalized_images.append(normalized_img)

    return normalized_images


def extract_single_partition(img_path: Path, output_dir: Path, parts_info: dict) -> None:
    part_name = img_path.stem
    part_dir = output_dir / part_name
    config_dir = output_dir / "config"
    ensure_clean_dir(config_dir)

    fs_type = gettype(str(img_path))
    if fs_type == "sparse":
        log(f"Converting sparse partition to raw: {img_path.name}")
        simg2img(str(img_path))
        fs_type = gettype(str(img_path))

    log(f"Extracting partition: {part_name}.img [{fs_type}]")

    if fs_type == "ext":
        Extractor().main(str(img_path), str(part_dir), str(output_dir))
    elif fs_type == "erofs":
        def _clean_partial_erofs_extract() -> None:
            if part_dir.exists():
                shutil.rmtree(part_dir, ignore_errors=True)

        def _run_erofs_extract(label: str, command: list[str]) -> int | str:
            log(f"Thu extract erofs bang {label}: {' '.join(command)}")
            try:
                result = subprocess.run(
                    command,
                    capture_output=True,
                    text=True,
                )
            except FileNotFoundError as exc:
                log(f"{label} khong chay duoc: {exc}")
                return "not found"

            if result.stdout:
                print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
            if result.stderr:
                print(result.stderr, end="" if result.stderr.endswith("\n") else "\n")
            return result.returncode

        bundled_extract_erofs = ROOT_DIR / "bin" / "extract.erofs"
        erofs_attempts: list[tuple[str, list[str]]] = [
            (
                "bundled extract.erofs",
                [str(bundled_extract_erofs), "-i", str(img_path), "-o", str(output_dir), "-x"],
            ),
        ]

        system_extract_erofs = shutil.which("extract.erofs")
        if system_extract_erofs:
            erofs_attempts.append(
                (
                    "system extract.erofs",
                    [system_extract_erofs, "-i", str(img_path), "-o", str(output_dir), "-x"],
                )
            )
        else:
            log("Khong tim thay system extract.erofs trong PATH.")

        erofs_attempts.extend(
            [
                (
                    "fsck.erofs --extract=<dir>",
                    ["fsck.erofs", f"--extract={part_dir}", str(img_path)],
                ),
                (
                    "fsck.erofs --extract <dir>",
                    ["fsck.erofs", "--extract", str(part_dir), str(img_path)],
                ),
            ]
        )

        erofs_errors: list[str] = []
        for label, command in erofs_attempts:
            _clean_partial_erofs_extract()
            ret = _run_erofs_extract(label, command)
            erofs_errors.append(f"{label} (ret={ret})")
            if ret == 0 and part_dir.exists():
                break
        else:
            raise RuntimeError(
                f"extract.erofs failed for {img_path.name}: "
                + "; ".join(erofs_errors)
            )
    else:
        log(f"Skipping {img_path.name}: unsupported filesystem [{fs_type}]")
        return

    if not part_dir.exists():
        raise RuntimeError(f"Directory not found after extraction: {part_dir}")

    seed_partition_config(config_dir, part_name, fs_type, part_dir)

    fs_config_path = config_dir / f"{part_name}_fs_config"
    file_contexts_path = config_dir / f"{part_name}_file_contexts"
    fspatch.main(str(part_dir), str(fs_config_path))
    contextpatch.main(
        str(part_dir),
        str(file_contexts_path),
        str(CONTEXT_RULES_FILE) if CONTEXT_RULES_FILE.exists() else None,
    )

    parts_info[part_name] = fs_type


def extract_partitions_from_super(super_out_dir: Path, output_dir: Path, super_img: Path) -> None:
    log("[5/6] Preparing to extract _a partitions...")
    write_super_config(output_dir, super_img)

    normalized_images = normalize_partition_images(super_out_dir, output_dir)
    if not normalized_images:
        log("No _a partitions found in super directory.")
        return

    parts_info_path = output_dir / "config" / "parts_info"
    parts_info = JsonEdit(str(parts_info_path)).read()

    for img_path in normalized_images:
        extract_single_partition(img_path, output_dir, parts_info)

    JsonEdit(str(parts_info_path)).write(parts_info)
    log(f"[6/6] Extracted {len(normalized_images)} _a partitions and created config.")


def build_output_dir(input_path: Path) -> Path:
    base_name = input_path.name
    for suffix in (".tar.gz", ".tgz", ".zip", ".tar", ".img"):
        if base_name.lower().endswith(suffix):
            base_name = base_name[: -len(suffix)]
            break
    return input_path.parent / f"{base_name}_unpacked"


def zip_output_folder(images_output_dir: Path) -> Path | None:
    """
    Nen toan bo thu muc DeadZone_* (cha cua images) thanh file zip cung ten.
    Sau khi nen xong, di chuyen file zip ra ROOT_DIR va xoa thu muc giai nen ban dau.
    Tra ve duong dan file zip neu thanh cong, None neu that bai.
    """
    deadzone_dir = images_output_dir.parent
    zip_name = f"{deadzone_dir.name}.zip"
    zip_path = deadzone_dir / zip_name
    zip_dest = ROOT_DIR / zip_name

    if not deadzone_dir.is_dir():
        log(f"[ZIP] Source directory not found: {deadzone_dir}")
        return None

    if zip_path.exists():
        try:
            remove_path_force(zip_path)
            log(f"    Removed old zip file: {zip_path}")
        except Exception as exc:
            log(f"[ZIP] Could not delete old zip file: {exc}")
            return None

    # HyperUR legacy scripts must never appear in the final ZIP
    _EXCLUDED_FILENAMES = {"HyperUR Flash_2.bat", "HyperUR Flash MTK.bat"}

    log(f"[ZIP] Compressing {deadzone_dir.name} into {zip_name} (DEFLATE level 9)...")
    log(f"      Source directory: {deadzone_dir}")

    try:
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            file_count = 0
            for root, _, files in os.walk(deadzone_dir):
                for name in files:
                    if name.endswith(".zip"):
                        continue
                    if name in _EXCLUDED_FILENAMES:
                        log(f"[ZIP] Excluded from final ZIP: {name}")
                        continue
                    file_path = Path(root) / name
                    arcname = file_path.relative_to(deadzone_dir)
                    zf.write(file_path, arcname)
                    file_count += 1
                    if file_count % 100 == 0:
                        log(f"    Compressed {file_count} files so far...")

        zip_size = zip_path.stat().st_size
        zip_size_mb = zip_size / (1024 * 1024)
        log(f"[ZIP] Complete. Compressed {file_count} files -> {zip_path} ({zip_size_mb:.2f} MB)")

        # Di chuyen file zip ra ROOT_DIR
        if zip_dest.exists():
            remove_path_force(zip_dest)
        shutil.move(str(zip_path), str(zip_dest))
        log(f"[ZIP] Moved output zip to: {zip_dest}")

        remove_path_force(deadzone_dir)
        log(f"[ZIP] Removed extraction directory: {deadzone_dir}")

        return zip_dest
    except Exception as exc:
        log(f"[ZIP] Error creating zip file: {exc}")
        if zip_path.exists():
            remove_path_force(zip_path)
        return None


def build_repack_output_dir(project_dir: Path) -> Path:
    aggregated: dict[str, str] = {}
    try:
        for build_prop_path in project_dir.rglob("build.prop"):
            props = parse_build_prop(build_prop_path)
            for key, value in props.items():
                if key not in aggregated and value:
                    aggregated[key] = value
    except Exception:
        pass

    device = aggregated.get("ro.product.odm.device", "")
    mi_incremental = aggregated.get("ro.mi.os.version.incremental", "")
    release = aggregated.get("ro.system.build.version.release", "")

    if device and release:
        folder_name = f"DeadZone_{device}_{mi_incremental}_{release}"
    elif device:
        folder_name = f"DeadZone_{device}_{mi_incremental}"
    else:
        folder_name = f"DeadZone_{device}"

    return project_dir / folder_name / "images"


def is_repack_project(path: Path) -> bool:
    return path.is_dir() and (path / "config" / "parts_info").exists()


def calculate_dir_size(dir_path: Path) -> int:
    size = 0
    for root, _, files in os.walk(dir_path):
        for name in files:
            file_path = Path(root) / name
            try:
                if file_path.is_file():
                    size += file_path.stat().st_size
                else:
                    size += len(name)
            except OSError:
                size += 1
    size += int((size / 16384) * 256)
    if size > 100 * 1024 * 1024:
        size += 16 * 1024 * 1024
    if size <= 2 * 1024 * 1024:
        size = 2 * 1024 * 1024
    if size % 4096:
        size += 4096 - (size % 4096)
    return size


def build_erofs_commands(part_name: str, project_dir: Path, output_img: Path) -> list[list[str]]:
    fs_config = project_dir / "config" / f"{part_name}_fs_config"
    file_contexts = project_dir / "config" / f"{part_name}_file_contexts"
    fs_options = project_dir / "config" / f"{part_name}_fs_options"
    part_dir = project_dir / part_name

    commands = []

    if fs_options.exists():
        try:
            line = ""
            for raw_line in fs_options.read_text(encoding="utf-8").splitlines():
                if raw_line.startswith("mkfs.erofs options:"):
                    line = raw_line.split("mkfs.erofs options:", 1)[1].strip()
                    break

            if line:
                tokens = line.split()
                parsed_opts = []
                i = 0
                while i < len(tokens):
                    token = tokens[i]
                    if token.startswith("-z"):
                        parsed_opts.append(token)
                    elif token in {"-T", "-U", "-E"} and i + 1 < len(tokens):
                        parsed_opts.extend([token, tokens[i + 1]])
                        i += 1
                    elif token.startswith("--mount-point="):
                        parsed_opts.append(token)
                    elif token == "--mount-point" and i + 1 < len(tokens):
                        parsed_opts.extend([token, tokens[i + 1]])
                        i += 1
                    i += 1

                commands.append([
                    'mkfs.erofs',
                    *parsed_opts,
                    f'--fs-config-file={fs_config}',
                    f'--file-contexts={file_contexts}',
                    str(output_img),
                    str(part_dir),
                ])
        except Exception:
            pass

    commands.append([
        'mkfs.erofs',
        '-zlz4hc',
        '-T', '0',
        f'--mount-point=/{part_name}',
        f'--fs-config-file={fs_config}',
        f'--file-contexts={file_contexts}',
        str(output_img),
        str(part_dir),
    ])

    commands.append([
        'mkfs.erofs',
        '-zlz4',
        '-T', '0',
        f'--mount-point=/{part_name}',
        f'--fs-config-file={fs_config}',
        f'--file-contexts={file_contexts}',
        str(output_img),
        str(part_dir),
    ])

    unique_commands = []
    seen = set()
    for command in commands:
        key = tuple(command)
        if key not in seen:
            seen.add(key)
            unique_commands.append(command)
    return unique_commands


def resolve_mkfs_erofs_binary(original_binary: str) -> str:
    """
    Resolve the mkfs.erofs binary path using a safe fallback chain:
      1. original_binary if absolute and exists
      2. original_binary as relative path if exists
      3. tool_bin + "mkfs.erofs" if that path exists
      4. ROOT_DIR / "bin" / "mkfs.erofs" (bundled, no arch subdir)
      5. shutil.which("mkfs.erofs") (system PATH)
      6. original_binary as-is (let subprocess produce the normal error)
    """
    import stat as _stat

    def _try(path_str: str) -> str | None:
        p = Path(path_str)
        if p.exists():
            # Ensure bundled binary is executable on Linux
            if os.name == "posix" and not os.access(str(p), os.X_OK):
                try:
                    p.chmod(p.stat().st_mode | _stat.S_IXUSR | _stat.S_IXGRP | _stat.S_IXOTH)
                except Exception:
                    pass
            return str(p)
        return None

    # 1. Absolute existing path
    if Path(original_binary).is_absolute():
        if (found := _try(original_binary)):
            log(f"[EROFS TOOL] mkfs.erofs resolved to: {found}")
            return found

    # 2. Relative path exists from cwd
    if (found := _try(original_binary)):
        log(f"[EROFS TOOL] mkfs.erofs resolved to: {found}")
        return found

    # 3. tool_bin + basename (only if it exists — do NOT blindly trust tool_bin)
    tool_bin_candidate = f"{tool_bin}mkfs.erofs"
    if (found := _try(tool_bin_candidate)):
        log(f"[EROFS TOOL] mkfs.erofs resolved to: {found}")
        return found

    # 4. Bundled binary (no arch subdir)
    bundled = ROOT_DIR / "bin" / "mkfs.erofs"
    if (found := _try(str(bundled))):
        log(f"[EROFS TOOL] mkfs.erofs resolved to: {found}")
        return found

    # 5. System PATH
    which_result = shutil.which("mkfs.erofs")
    if which_result:
        log(f"[EROFS TOOL] mkfs.erofs resolved to: {which_result}")
        return which_result

    log("[EROFS TOOL] mkfs.erofs resolver could not find an existing binary; using original command.")
    return original_binary


def repack_erofs(part_name: str, project_dir: Path, output_img: Path) -> None:
    if output_img.exists():
        output_img.unlink()

    # ── Preflight checks ──────────────────────────────────────────────────────
    fs_config = project_dir / "config" / f"{part_name}_fs_config"
    file_contexts = project_dir / "config" / f"{part_name}_file_contexts"
    part_dir = project_dir / part_name

    def _dir_size(d: Path) -> str:
        try:
            return str(sum(f.stat().st_size for f in d.rglob("*") if f.is_file()))
        except Exception:
            return "error"

    log(f"[EROFS PREFLIGHT] partition={part_name}")
    log(f"  part_dir      : {part_dir} | exists={part_dir.exists()} | bytes={_dir_size(part_dir) if part_dir.exists() else 'N/A'}")
    log(f"  fs_config     : {fs_config} | exists={fs_config.exists()} | bytes={fs_config.stat().st_size if fs_config.exists() else 'N/A'}")
    log(f"  file_contexts : {file_contexts} | exists={file_contexts.exists()} | bytes={file_contexts.stat().st_size if file_contexts.exists() else 'N/A'}")

    if not part_dir.exists():
        raise RuntimeError(f"[EROFS PREFLIGHT FAIL] part_dir missing: {part_dir}")
    if not fs_config.exists() or fs_config.stat().st_size == 0:
        raise RuntimeError(f"[EROFS PREFLIGHT FAIL] fs_config missing or empty: {fs_config}")
    if not file_contexts.exists() or file_contexts.stat().st_size == 0:
        raise RuntimeError(f"[EROFS PREFLIGHT FAIL] file_contexts missing or empty: {file_contexts}")

    # ── Log directory ─────────────────────────────────────────────────────────
    log_dir = project_dir / "logs" / "mkfs_erofs"
    log_dir.mkdir(parents=True, exist_ok=True)

    commands = build_erofs_commands(part_name, project_dir, output_img)
    last_error = None
    for index, command in enumerate(commands, start=1):
        original_binary = command[0]
        resolved_binary = resolve_mkfs_erofs_binary(original_binary)

        resolved_cmd = list(command)
        resolved_cmd[0] = resolved_binary

        log(f"EROFS repack attempt {index}: {' '.join(resolved_cmd)}")
        try:
            result = subprocess.run(
                resolved_cmd,
                stdin=subprocess.DEVNULL,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                creationflags=subprocess.CREATE_NO_WINDOW if os.name != "posix" else 0,
            )
            ret = result.returncode
            combined_output = result.stdout.decode("utf-8", errors="replace")
        except FileNotFoundError as exc:
            ret = 2
            combined_output = f"[FileNotFoundError] {exc}\n"

        for line in combined_output.splitlines():
            print(line, flush=True)

        log_file = log_dir / f"{part_name}_attempt_{index}.log"
        try:
            with log_file.open("w", encoding="utf-8") as lf:
                lf.write(f"partition          : {part_name}\n")
                lf.write(f"attempt            : {index}\n")
                lf.write(f"original_binary    : {original_binary}\n")
                lf.write(f"resolved_binary    : {resolved_binary}\n")
                lf.write(f"resolved_binary_exists: {Path(resolved_binary).exists()}\n")
                lf.write(f"which_mkfs_erofs   : {shutil.which('mkfs.erofs') or 'not found'}\n")
                lf.write(f"PATH               : {os.environ.get('PATH', '')}\n")
                lf.write(f"command            : {' '.join(resolved_cmd)}\n")
                lf.write(f"return_code        : {ret}\n")
                lf.write(f"output_img    : {output_img} | exists={output_img.exists()} | bytes={output_img.stat().st_size if output_img.exists() else 'N/A'}\n")
                lf.write(f"part_dir      : {part_dir} | exists={part_dir.exists()} | bytes={_dir_size(part_dir) if part_dir.exists() else 'N/A'}\n")
                lf.write(f"fs_config     : {fs_config} | exists={fs_config.exists()} | bytes={fs_config.stat().st_size if fs_config.exists() else 'N/A'}\n")
                lf.write(f"file_contexts : {file_contexts} | exists={file_contexts.exists()} | bytes={file_contexts.stat().st_size if file_contexts.exists() else 'N/A'}\n")
                lf.write("\n--- stdout+stderr ---\n")
                lf.write(combined_output)
            log(f"[EROFS] attempt={index} ret={ret} log={log_file}")
        except Exception as write_err:
            log(f"[EROFS] attempt={index} ret={ret} (log write failed: {write_err})")

        if ret == 0 and output_img.exists() and output_img.stat().st_size > 0:
            return
        last_error = ret
        if output_img.exists():
            output_img.unlink()

    # ── All attempts failed: dump diagnostic info ─────────────────────────────
    log(f"[EROFS FAIL] All {len(commands)} attempt(s) failed for {part_name} (last_ret={last_error})")
    dump_file = log_dir / f"{part_name}_fail_dump.log"
    try:
        with dump_file.open("w", encoding="utf-8") as df:
            df.write(f"=== EROFS FAIL DUMP: {part_name} ===\n\n")
            df.write("--- fs_config (first 40 lines) ---\n")
            try:
                lines = fs_config.read_text(encoding="utf-8", errors="replace").splitlines()
                df.write("\n".join(lines[:40]) + "\n")
            except Exception as e:
                df.write(f"[ERROR reading fs_config] {e}\n")
            df.write("\n--- file_contexts (first 40 lines) ---\n")
            try:
                lines = file_contexts.read_text(encoding="utf-8", errors="replace").splitlines()
                df.write("\n".join(lines[:40]) + "\n")
            except Exception as e:
                df.write(f"[ERROR reading file_contexts] {e}\n")
            df.write("\n--- part_dir contents (first 80 entries) ---\n")
            try:
                entries = sorted(part_dir.rglob("*"))[:80]
                for entry in entries:
                    df.write(f"  {entry.relative_to(part_dir)}\n")
            except Exception as e:
                df.write(f"[ERROR listing part_dir] {e}\n")
        log(f"[EROFS FAIL DUMP] written to {dump_file}")
    except Exception as dump_err:
        log(f"[EROFS FAIL DUMP] could not write dump: {dump_err}")

    raise RuntimeError(f"EROFS repack failed: {part_name} (ret={last_error})")


def sync_partition_configs(part_dir: Path, fs_config: Path, file_contexts: Path) -> None:
    log(f"Syncing config with partition directory: {part_dir.name}")

    current_fs = fspatch.scanfs(str(fs_config.resolve()))
    new_fs, fs_added = fspatch.fs_patch(current_fs, str(part_dir))
    with fs_config.open("w", encoding="utf-8", newline="\n") as file:
        file.writelines(f"{path} {' '.join(new_fs[path])}\n" for path in sorted(new_fs.keys()))
    log(f"    fs_config: added {fs_added} new entries")

    if CONTEXT_RULES_FILE.exists():
        fix_permission = JsonEdit(str(CONTEXT_RULES_FILE)).read()
    else:
        fix_permission = {}
    current_contexts = contextpatch.scan_context(str(file_contexts.resolve()))
    new_contexts, context_added = contextpatch.context_patch(
        current_contexts,
        str(part_dir),
        fix_permission,
    )
    with file_contexts.open("w", encoding="utf-8", newline="\n") as file:
        file.writelines(f"{path} {new_contexts[path]}\n" for path in sorted(new_contexts.keys()))
    log(f"    file_contexts: added {context_added} new entries")


def repack_single_partition(project_dir: Path, super_dir: Path, part_name: str) -> Path | None:
    part_dir = project_dir / part_name
    if not part_dir.is_dir():
        return None

    fs_config = project_dir / "config" / f"{part_name}_fs_config"
    file_contexts = project_dir / "config" / f"{part_name}_file_contexts"
    if not fs_config.exists() or not file_contexts.exists():
        log(f"Skipping {part_name}: missing config files.")
        return None

    sync_partition_configs(part_dir, fs_config, file_contexts)

    output_img = super_dir / f"{part_name}_a.img"
    if output_img.exists():
        output_img.unlink()

    log(f"Repacking {part_name} to EROFS raw -> {output_img.name}")
    repack_erofs(part_name, project_dir, output_img)
    if remove_path_force(part_dir):
        log(f"Removed partition directory after repack: {part_dir}")
    else:
        log(f"Warning: could not remove partition directory after repack: {part_dir}")
    return output_img


def _load_super_info_from_payload_manifest(project_dir: Path) -> dict | None:
    """
    Recover dynamic partition metadata from payload.bin when no super.img
    was produced (MTK / payload-only builds).

    Reads DeltaArchiveManifest.dynamic_partition_metadata from the payload.
    Uses DynamicPartitionGroup.size as the super block device size — this is
    the verified per-slot maximum from the ROM itself, not an invented value.

    Returns a super_info dict compatible with derive_super_layout(), or None
    if the manifest cannot be found / parsed / is incomplete.
    """
    try:
        from src.core.payload_extract import init_payload_info
    except Exception as exc:
        log(f"[SUPER] Could not import payload_extract: {exc}")
        return None

    # Search for payload.bin in the ROM extraction directory
    search_roots = [project_dir / "rom", project_dir]
    payload_candidates: list[Path] = []
    for root in search_roots:
        if root.is_dir():
            try:
                payload_candidates.extend(p for p in root.rglob("payload.bin") if p.is_file())
            except Exception:
                pass

    seen: set[str] = set()
    unique_payloads = [p for p in payload_candidates if not seen.__contains__(str(p)) and not seen.add(str(p))]  # type: ignore[func-returns-value]

    if not unique_payloads:
        log("[SUPER] No payload.bin found for dynamic partition metadata recovery.")
        return None

    for payload_path in unique_payloads:
        try:
            log(f"[SUPER] Reading dynamic partition metadata from: {payload_path}")
            with payload_path.open("rb") as f:
                manifest = init_payload_info(f)

            dpm = getattr(manifest, "dynamic_partition_metadata", None)
            if dpm is None or not dpm.groups:
                log("[SUPER] Payload manifest has no dynamic_partition_metadata; cannot recover super layout.")
                continue

            # Find the primary (largest) non-default group
            main_group = None
            for g in dpm.groups:
                if not g.name or g.name == "default":
                    continue
                if main_group is None or g.size > main_group.size:
                    main_group = g

            if main_group is None or main_group.size <= 0:
                log("[SUPER] Payload manifest: no valid group with size found.")
                continue

            group_name = main_group.name
            group_size = int(main_group.size)
            part_names = list(main_group.partition_names) if main_group.partition_names else []

            log(f"[SUPER] Payload manifest: group='{group_name}' size={group_size} partitions={part_names}")

            if not part_names:
                log("[SUPER] Payload manifest group has no partition names; cannot recover partition table.")
                continue

            # Build a super_info dict compatible with derive_super_layout().
            # metadata_slot_count=3 forces super_type=2 (VAB).
            # Partition names get _a suffix so derive_super_layout identifies the slot type.
            # group_size is the verified per-slot ROM value — not invented.
            super_info: dict = {
                "metadata_slot_count": 3,
                "block_devices": [
                    {"name": "super", "size": group_size}
                ],
                "group_table": [
                    {"name": f"{group_name}_a"},
                    {"name": f"{group_name}_b"},
                ],
                "partition_table": [
                    {"name": f"{p}_a"} for p in part_names
                ],
            }
            log(f"[SUPER] Recovered super_info from payload manifest for group '{group_name}'.")
            return super_info

        except Exception as exc:
            log(f"[SUPER] Could not parse payload manifest ({payload_path.name}): {exc}")
            continue

    return None


def _save_super_config(project_dir: Path, super_info: dict) -> None:
    """Persist super_info to config/super and inject into config/parts_info."""
    config_dir = project_dir / "config"
    config_dir.mkdir(parents=True, exist_ok=True)
    super_config_path = config_dir / "super"
    try:
        with open(super_config_path, "w", encoding="utf-8", newline="\n") as f:
            json.dump(super_info, f, indent=4, ensure_ascii=False)
        log(f"[SUPER] Wrote super metadata to config/super")
    except Exception as exc:
        log(f"[SUPER] Warning: could not write config/super: {exc}")

    parts_info_path = config_dir / "parts_info"
    try:
        existing = JsonEdit(str(parts_info_path)).read()
        if not isinstance(existing, dict):
            existing = {}
        if "super_info" not in existing:
            existing["super_info"] = super_info
            JsonEdit(str(parts_info_path)).write(existing)
            log(f"[SUPER] Injected super_info into config/parts_info")
    except Exception as exc:
        log(f"[SUPER] Warning: could not update parts_info with super_info: {exc}")


def load_super_info(project_dir: Path) -> dict:
    # Step 1: parts_info["super_info"]
    parts_info = JsonEdit(str(project_dir / "config" / "parts_info")).read()
    super_info = parts_info.get("super_info")
    if isinstance(super_info, dict):
        return super_info

    # Step 2: config/super JSON file
    super_config = project_dir / "config" / "super"
    if super_config.exists():
        try:
            with open(super_config, "r", encoding="utf-8") as file:
                data = json.load(file)
            if isinstance(data, dict):
                return data
        except Exception:
            pass

    # Step 3: super_raw.img or super.img directly in project_dir
    for candidate in [project_dir / "super_raw.img", project_dir / "super.img"]:
        if candidate.exists():
            log(f"[SUPER] Loading super metadata from: {candidate.name}")
            info = lpunpack_get_info(str(candidate))
            _save_super_config(project_dir, info)
            return info

    # Step 4: super.img in the ROM extraction directory (project_dir/rom) or nearby
    for search_dir in [
        project_dir / "rom",
        project_dir / "rom" / "payload_extracted",
    ]:
        if not search_dir.is_dir():
            continue
        found = find_super_img(search_dir)
        if found and found.is_file() and found.stat().st_size > 0:
            log(f"[SUPER] Found super.img in extraction dir: {found}")
            info = lpunpack_get_info(str(found))
            _save_super_config(project_dir, info)
            return info

    # Step 5: recover dynamic partition layout from payload.bin manifest (MTK / payload builds)
    payload_info = _load_super_info_from_payload_manifest(project_dir)
    if payload_info is not None:
        _save_super_config(project_dir, payload_info)
        return payload_info

    # Step 6: check registry device profile for verified super metadata (Part C)
    factory_codename = os.environ.get("DEADZONE_DEVICE_CODENAME", "").strip()
    factory_soc = os.environ.get("DEADZONE_SOC", "").strip()
    registry_super_profile_found = False
    if factory_codename and factory_soc:
        reg_path = ROOT_DIR.parents[1] / "registry" / "devices" / factory_soc / f"{factory_codename}.yml"
        if reg_path.is_file():
            try:
                import yaml  # type: ignore[import]
                with reg_path.open("r", encoding="utf-8") as _f:
                    reg_data = yaml.safe_load(_f)
                reg_super = reg_data.get("super", {}) if isinstance(reg_data, dict) else {}
                verified_size = reg_super.get("super_size") or reg_super.get("verified_size")
                if verified_size and int(verified_size) > 0:
                    registry_super_profile_found = True
                    _reg_slot_mode = reg_super.get("slot_mode", "unknown")
                    _reg_active_slot = reg_super.get("active_slot", "unknown")
                    _reg_inactive_zero = reg_super.get("inactive_slot_zero", False)
                    log(f"[SUPER] Registry super profile found for {factory_codename}")
                    log(f"[SUPER] super_size={verified_size}")
                    log(f"[SUPER] slot_mode={_reg_slot_mode} active_slot={_reg_active_slot} inactive_slot_zero={_reg_inactive_zero}")
                    log(f"[SUPER] _a partitions will use real images")
                    log(f"[SUPER] _b partitions will be zero-size metadata entries")
                    info = {
                        "metadata_slot_count": 3,
                        "block_devices": [{"name": "super", "size": int(verified_size)}],
                        "group_table": [
                            {"name": f"{reg_super.get('dynamic_group', 'qti_dynamic_partitions')}_a"},
                            {"name": f"{reg_super.get('dynamic_group', 'qti_dynamic_partitions')}_b"},
                        ],
                        "partition_table": [],
                    }
                    _save_super_config(project_dir, info)
                    return info
            except ImportError:
                log("[SUPER] yaml not available; skipping registry super profile check.")
            except Exception as exc:
                log(f"[SUPER] Registry super profile check failed: {exc}")

    # Step 7: diagnostic failure — all recovery paths exhausted
    config_dir = project_dir / "config"
    config_files = sorted(f.name for f in config_dir.iterdir()) if config_dir.is_dir() else []
    super_files_in_project = sorted(
        str(p.relative_to(project_dir)) for p in project_dir.glob("*super*") if p.is_file()
    )
    _rom_dir_diag = project_dir / "rom"
    _payload_cands: list[Path] = []
    if _rom_dir_diag.is_dir():
        _payload_cands = list(_rom_dir_diag.rglob("payload.bin"))
    payload_meta_found = bool(_payload_cands)

    super_config_dir = ROOT_DIR / "SuperConfig" / (factory_codename or "(device)")
    registry_hint = (
        f"registry/devices/{factory_soc}/{factory_codename}.yml has no verified super_size"
        if factory_codename and factory_soc and not registry_super_profile_found
        else "(not checked — DEADZONE_DEVICE_CODENAME or DEADZONE_SOC not set)"
    )

    build_prop_device = _q_fix_read_ro_product_odm_device(project_dir) or "(not found)"

    raise RuntimeError(
        "\n[SUPER INFO ERROR] Cannot rebuild super.img — dynamic partition metadata is missing.\n"
        f"  Device                 : {factory_codename or '(not set)'}\n"
        f"  Factory override       : {factory_codename or '(not set)'}\n"
        f"  build.prop device      : {build_prop_device}\n"
        f"  config/super           : exists={super_config.exists()}\n"
        f"  parts_info super_info  : False\n"
        f"  super_raw.img          : {(project_dir / 'super_raw.img').exists()}\n"
        f"  super.img              : {(project_dir / 'super.img').exists()}\n"
        f"  payload metadata found : {payload_meta_found}\n"
        f"  Registry super profile : {registry_super_profile_found} ({registry_hint})\n"
        f"  SuperConfig path       : {super_config_dir / 'super'} (exists={( super_config_dir / 'super').exists()})\n"
        f"  config/ contains       : {config_files}\n"
        f"  *super* in project_dir : {super_files_in_project or ['(none)']}\n"
        f"\n  To fix: provide the stock super.img from fastboot, or add a verified\n"
        f"  super_size to registry/devices/{factory_soc or '<soc>'}/{factory_codename or '<device>'}.yml"
    )


def collect_part_names(project_dir: Path) -> list[str]:
    parts_info = JsonEdit(str(project_dir / "config" / "parts_info")).read()
    return sorted(
        name for name, fs_type in parts_info.items()
        if isinstance(fs_type, str)
        and name not in ["super_info", "dat_ver"]
        and (project_dir / name).is_dir()
    )


def derive_super_layout(super_info: dict, part_names: list[str]) -> tuple[str, int, int, str, str, list[str]]:
    block_devices = super_info.get("block_devices", [])
    group_table = super_info.get("group_table", [])
    partition_table = super_info.get("partition_table", [])

    block_device_name = "super"
    super_size = 0
    if block_devices:
        block_device_name = str(block_devices[0].get("name", "super"))
        super_size = int(block_devices[0].get("size", 0))

    metadata_slot_count = int(super_info.get("metadata_slot_count", 3))
    partition_names = [str(item.get("name", "")) for item in partition_table]
    group_names = [str(item.get("name", "")) for item in group_table if item.get("name") != "default"]

    super_type = 2 if any(name.endswith("_a") or name.endswith("_b") for name in partition_names) else 1
    if metadata_slot_count == 3:
        super_type = 2

    group_name = "qti_dynamic_partitions"
    group_a_name = ""
    group_b_name = ""

    for name in group_names:
        if name.endswith("_a"):
            group_a_name = name
            group_name = name[:-2]
        elif name.endswith("_b"):
            group_b_name = name

    if super_type == 1 and group_names:
        group_name = group_names[0]
        group_a_name = group_name
        group_b_name = group_name
    else:
        if not group_a_name:
            group_a_name = f"{group_name}_a"
        if not group_b_name:
            group_b_name = f"{group_name}_b"

    selected_parts = []
    for name in partition_names:
        if name.endswith("_a") or name.endswith("_b"):
            base_name = name[:-2]
        else:
            base_name = name
        if base_name in part_names and base_name not in selected_parts:
            selected_parts.append(base_name)

    if not selected_parts:
        selected_parts = part_names

    return block_device_name, super_size, super_type, group_a_name, group_b_name, selected_parts


def can_use_slot_image(img_path: Path) -> bool:
    if not img_path.exists() or not img_path.is_file():
        return False
    if img_path.stat().st_size <= 0:
        return False

    img_type = gettype(str(img_path))
    return img_type in {"erofs", "ext", "f2fs", "sparse"}


def build_super_image(project_dir: Path, output_dir: Path, super_dir: Path, super_info: dict, part_names: list[str]) -> Path:
    block_device_name, super_size, super_type, group_a_name, group_b_name, selected_parts = derive_super_layout(
        super_info,
        part_names,
    )
    if super_size <= 0:
        raise RuntimeError("super_info has no valid block device size")

    command = [
        'lpmake',
        '--metadata-size', '65536',
        '-super-name', block_device_name,
        '-metadata-slots', '3' if super_type == 2 else '2',
    ]

    if super_type == 1:
        command += ['-device', f'{block_device_name}:{super_size}', '--group', f'{group_a_name}:{super_size}']
        for part_name in selected_parts:
            img_path = super_dir / f"{part_name}_a.img"
            if not img_path.exists():
                raise RuntimeError(f"Required _a image not found for super pack: {img_path}")
            command += [
                '--partition', f'{part_name}:readonly:{img_path.stat().st_size}:{group_a_name}',
                '--image', f'{part_name}={img_path}',
            ]
    else:
        command += ['-device', f'{block_device_name}:{super_size}', '--group', f'{group_a_name}:{super_size}']
        for part_name in selected_parts:
            img_path = super_dir / f"{part_name}_a.img"
            if not img_path.exists():
                raise RuntimeError(f"Required _a image not found for super pack: {img_path}")
            command += [
                '--partition', f'{part_name}_a:readonly:{img_path.stat().st_size}:{group_a_name}',
                '--image', f'{part_name}_a={img_path}',
            ]

        command += ['--group', f'{group_b_name}:{super_size}']
        for part_name in selected_parts:
            img_path = super_dir / f"{part_name}_b.img"
            if can_use_slot_image(img_path):
                command += [
                    '--partition', f'{part_name}_b:readonly:{img_path.stat().st_size}:{group_b_name}',
                    '--image', f'{part_name}_b={img_path}',
                ]
            else:
                if img_path.exists():
                    log(f"Skipping {img_path.name}: _b image is invalid; adding empty partition.")
                command += ['--partition', f'{part_name}_b:readonly:0:{group_b_name}']
        command += ['--virtual-ab']

    super_img_out = output_dir / "super.img"
    if super_img_out.exists():
        super_img_out.unlink()
    command += ['--out', str(super_img_out)]

    if super_type == 2:
        log("[SUPER] Rebuilding sparse VAB super.img")
    ret = call(command, out=True)
    if ret != 0 or not super_img_out.exists():
        raise RuntimeError("lpmake failed building super.img")
    return super_img_out


def cleanup_after_repack(project_dir: Path) -> None:
    for img_path in sorted(project_dir.glob("*.img")):
        if remove_path_force(img_path):
            log(f"Removed original image: {img_path.name}")
        else:
            log(f"Warning: could not remove original image: {img_path.name}")

    for folder_name in ["super", "config"]:
        folder_path = project_dir / folder_name
        if folder_path.exists():
            if remove_path_force(folder_path):
                log(f"Removed directory: {folder_path}")
            else:
                log(f"Warning: could not remove directory: {folder_path}")


def repack_project(project_dir: Path, rom_path: Path | None = None, output_dir: Path | None = None) -> Path:
    if output_dir is None:
        output_dir = build_repack_output_dir(project_dir)
    ensure_clean_dir(output_dir)
    super_dir = project_dir / "super"
    ensure_clean_dir(super_dir)

    part_names = collect_part_names(project_dir)
    if not part_names:
        raise RuntimeError("No partitions found in config/parts_info to repack.")

    super_info = load_super_info(project_dir)
    log(f"Repacking project: {project_dir}")
    for part_name in part_names:
        repack_single_partition(project_dir, super_dir, part_name)

    super_img_out = build_super_image(project_dir, output_dir, super_dir, super_info, part_names)
    cleanup_after_repack(project_dir)

    if rom_path is not None and rom_path.is_file():
        rom_name = rom_path.name.lower()
        if rom_name.endswith(SUPPORTED_ARCHIVES):
            if remove_path_force(rom_path):
                log(f"Removed original ROM file: {rom_path.name}")
            else:
                log(f"Warning: could not remove original ROM file: {rom_path.name}")

    log(f"[SUPER] super.img repacked: {super_img_out}")
    return super_img_out


# Generic MTK SoC fallback identifiers that must never be used as the SuperConfig folder.
# When one of these is read from build.prop but DEADZONE_DEVICE_CODENAME is not set,
# the sync is skipped to avoid creating a pointless directory under SuperConfig/.
_GENERIC_DEVICE_NAMES = frozenset({
    "mgvi_64_armv82",
    "armv82",
    "generic",
    "unknown",
})


def sync_super_config_for_device(project_dir: Path) -> None:
    """
    Sync project_dir/config/super and project_dir/config/parts_info
    with ROOT_DIR/SuperConfig/<device>/.

    Device name priority:
      1. DEADZONE_DEVICE_CODENAME env var (set by the Factory for the selected device)
      2. ro.product.odm.device from build.prop, unless it is a known generic SoC fallback name
    """
    factory_codename = os.environ.get("DEADZONE_DEVICE_CODENAME", "").strip()
    build_prop_name = _q_fix_read_ro_product_odm_device(project_dir)

    if factory_codename:
        device_name = factory_codename
        if build_prop_name and build_prop_name != factory_codename:
            log(f"[DEVICE] Factory device override: {device_name}  (build.prop had: '{build_prop_name}')")
        else:
            log(f"[DEVICE] Factory device override: {device_name}")
    elif build_prop_name and build_prop_name.lower() not in _GENERIC_DEVICE_NAMES:
        device_name = build_prop_name
        log(f"[DEVICE] Device codename from build.prop: {device_name}")
    else:
        if build_prop_name:
            log(
                f"Warning: build.prop device '{build_prop_name}' is a generic SoC identifier; "
                f"set DEADZONE_DEVICE_CODENAME to override. Skipping SuperConfig sync."
            )
        else:
            log("Warning: could not read ro.product.odm.device from build.prop; skipping SuperConfig sync.")
        return

    config_dir = project_dir / "config"
    config_super_path = config_dir / "super"
    config_parts_info_path = config_dir / "parts_info"

    super_config_root = ROOT_DIR / "SuperConfig"
    device_dir = super_config_root / device_name
    device_super_path = device_dir / "super"
    device_parts_info_path = device_dir / "parts_info"

    try:
        device_dir.mkdir(parents=True, exist_ok=True)

        # sync super
        if config_super_path.is_file():
            shutil.copy2(config_super_path, device_super_path)
            log(f"[SuperConfig] Saved config/super -> {device_super_path}")
        elif device_super_path.is_file():
            config_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(device_super_path, config_super_path)
            log(f"[SuperConfig] Restored config/super from {device_super_path}")
        else:
            log(
                f"Warning: no super file found in:\n"
                f"  - project config/super\n"
                f"  - {device_super_path}"
            )

        # sync parts_info
        if config_parts_info_path.is_file():
            # Guard: do not save parts_info that is missing super_info — it is
            # incomplete and would give the false impression that a working
            # SuperConfig exists for this device.
            try:
                _pi = JsonEdit(str(config_parts_info_path)).read()
                if isinstance(_pi, dict) and "super_info" not in _pi:
                    log(
                        f"[SuperConfig] parts_info exists but super_info is missing; "
                        f"not enough to rebuild super.img. Skipping SuperConfig save."
                    )
                    _pi = None
            except Exception:
                _pi = None
            if _pi is not None:
                shutil.copy2(config_parts_info_path, device_parts_info_path)
                log(f"[SuperConfig] Saved config/parts_info -> {device_parts_info_path}")
        elif device_parts_info_path.is_file():
            config_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(device_parts_info_path, config_parts_info_path)
            log(f"[SuperConfig] Restored config/parts_info from {device_parts_info_path}")
        else:
            log("Warning: no parts_info found in project/config or SuperConfig for this device.")
    except Exception as exc:
        log(f"Warning: error syncing SuperConfig for device '{device_name}': {exc}")


def main() -> int:
    extracted_dir: Path | None = None
    super_img_path: Path | None = None
    super_out_dir: Path | None = None
    payload_partitions_extracted = False
    try:
        if len(sys.argv) > 1:
            input_path = Path(sys.argv[1].strip('"')).expanduser().resolve()
        else:
            selected = choose_path()
            if selected is None:
                log("Khong co duong dan nao duoc chon.")
                return 1
            input_path = selected.resolve()

        if not input_path.exists():
            log(f"Khong tim thay file: {input_path}")
            return 1

        log(f"File dau vao: {input_path}")

        if is_repack_project(input_path):
            sync_super_config_for_device(input_path)
            final_super_img = repack_project(input_path)
            log(f"Repack complete. super.img at: {final_super_img}")
            return 0

        output_dir = build_output_dir(input_path)
        ensure_clean_dir(output_dir)
        log(f"Thu muc output: {output_dir}")

        if input_path.name.lower() == "super.img":
            super_img_path = input_path
        else:
            extracted_dir = extract_rom(input_path, output_dir)
            log(f"[2/4] Searching for super.img in: {extracted_dir}")
            super_img_path = find_super_img(extracted_dir)

        if super_img_path is None:
            log(
                "super.img not found after ROM extraction. Trying to extract payload.bin (if available)..."
            )
            if extracted_dir is not None:
                payload_partitions_extracted = try_extract_super_from_payload(
                    extracted_dir=extracted_dir,
                    project_dir=output_dir,
                    search_roots=[extracted_dir, ROOT_DIR],
                )
                # if payload produced super.img, search again
                if payload_partitions_extracted:
                    super_img_path = find_super_img(extracted_dir)

            if super_img_path is None and not payload_partitions_extracted:
                log("super.img not found (could not be produced from payload.bin either).")
                return 1

        if super_img_path is not None:
            log(f"Found super.img: {super_img_path}")
            super_out_dir = unpack_super(super_img_path, output_dir)
            extract_partitions_from_super(super_out_dir, output_dir, super_img_path)
        else:
            log(
                "No original super.img. Continuing with partitions extracted from payload.bin."
            )

        mi_incremental, _android_release = find_and_read_build_props(output_dir)
        major = mezo_android_major(_android_release)
        debloat_project(output_dir, ROOT_DIR / "debloat.txt")
        clean_system_framework_arch_dirs(output_dir)
        move_product_data_app_to_app(output_dir)
        fix_nfc(output_dir)
        copy_mezo_app_product(output_dir)
        copy_mezo_app_mod(output_dir)
        copy_mezo_app_system(output_dir)

        if mi_incremental:
            apply_language_overlay(output_dir, mi_incremental)
            apply_version_specific_apks(output_dir, mi_incremental, major)
        append_custom_build_prop(output_dir)
        q_fix(output_dir)
        move_framework_jars_to_cwd(output_dir, output_dir)
        unpack_framework_jars_and_classes(output_dir)

        if major == 16:
            prepare_auxiliary_work_files(output_dir)
            dex_redivision(output_dir)
        if major == 15:
            fix_bootloop_a15(output_dir)
        if major in (14, 15):
            disable_signature_verification_a14_15(output_dir)
            disable_flag_secure_a14_15(output_dir)
            tricky_wukong_a15(output_dir)
        elif major == 16:
            disable_signature_verification_a16(output_dir)
            disable_flag_secure_a16(output_dir)
            tricky_wukong_a16(output_dir)

        enhanced_keyboard(output_dir)
        enable_floating_window_all_app(output_dir)
        increase_number_of_floating_windows(output_dir)
        kaori_toolbox(output_dir)
        fix_notification(output_dir)
        fix_theme_reset(output_dir)
        repack_all_classes(output_dir)
        repack_all_jar_files(output_dir)
        restore_repacked_jars_to_project(output_dir, output_dir)
        export_and_decompile_miui_systemui(output_dir, output_dir)
        fix_recompile(output_dir)
        if major == 15:
            apply_miui_systemui_mods_android15(output_dir)
        if major == 16:
            apply_miui_systemui_mods_android16(output_dir)
        recompile_apk(output_dir)
        restore_recompiled_miui_systemui_to_project(output_dir, output_dir)
        process_provision_apk(output_dir, output_dir)

        log("Finished extracting super.img and partitions.")
        log("Continuing to repack _a partitions and super.img...")
        sync_super_config_for_device(output_dir)
        images_output_dir = build_repack_output_dir(output_dir)
        final_super_img = repack_project(output_dir, input_path, images_output_dir)
        if super_out_dir is not None:
            log(f"Done. super.img files at: {super_out_dir}")
        else:
            log("Done. Partitions repacked (no original super.img).")
        log(f"super.img repacked at: {final_super_img}")

        # Copy flash folder into the output parent (provides flash scripts alongside super.img)
        # Legacy HyperUR scripts are excluded — only DeadZone-branded scripts are copied.
        _EXCLUDED_FLASH = {"HyperUR Flash_2.bat", "HyperUR Flash MTK.bat"}
        flash_src = ROOT_DIR / "flash"
        flash_dest_parent = images_output_dir.parent
        if flash_src.is_dir():
            try:
                copy_count = 0
                for flash_item in flash_src.rglob("*"):
                    if flash_item.is_file():
                        if flash_item.name in _EXCLUDED_FLASH:
                            log(f"[FLASH] Excluded legacy script: {flash_item.name}")
                            continue
                        rel = flash_item.relative_to(flash_src)
                        dest = flash_dest_parent / rel
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        if not dest.exists() or dest.stat().st_size != flash_item.stat().st_size:
                            shutil.copy2(flash_item, dest)
                            copy_count += 1
                if copy_count > 0:
                    log(f"[FLASH] Copied {copy_count} file(s) from flash/ to {flash_dest_parent}")
            except Exception as exc:
                log(f"[FLASH] Error copying flash directory: {exc}")

        # Nen thu muc DeadZone_* thanh file zip
        zip_output_folder(images_output_dir)

        return 0
    except Exception as exc:
        log(f"Error: {exc}")
        return 1
    finally:
        pause_if_needed()


if __name__ == "__main__":
    raise SystemExit(main())
