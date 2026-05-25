"""
Post-extraction partition and boot-image scanning, plus dynamic-partition
extraction from a payload_extracted directory.

DeadZone-native extraction flow (in priority order):
  1. Detect image type from header magic (sparse / erofs / ext4 / unknown)
  2. If sparse → convert to raw via simg2img (bundled bin/)
  3. Extract EROFS images via extract.erofs (bundled bin/)
  4. Extract ext4 images via debugfs (system tool, if available)
  5. MEZOBuildRom.extract_single_partition as final fallback only

Safe flow per partition:
  - Source image stays in payload_extracted (never moved or deleted here)
  - Sparse → raw written to project_dir/.tmp_raw/
  - Extract target: project_dir/.extract_tmp/<partition>/
  - On success: rename .extract_tmp/<partition>/ → project_dir/<partition>/
  - Temp files deleted only after successful rename
  - payload_extracted images kept until entire unpack stage completes

Detailed log: output/logs/partition_extract.log
"""
from __future__ import annotations

import json
import os
import shutil
import struct
import subprocess
import sys
from pathlib import Path
from typing import Optional

_BIN_DIR = Path(__file__).resolve().parents[2] / "third_party" / "mezo_core" / "bin"

# Dynamic partitions that live inside super.img (slot _a suffix stripped).
_DYNAMIC_PARTITION_NAMES = frozenset({
    "system",
    "system_ext",
    "system_dlkm",
    "vendor",
    "vendor_dlkm",
    "product",
    "odm",
    "odm_dlkm",
    "mi_ext",
})

# Ordered list of dynamic partition images expected from payload extraction.
_DYNAMIC_PARTITION_IMGS = [
    "mi_ext.img",
    "odm.img",
    "odm_dlkm.img",
    "product.img",
    "system.img",
    "system_dlkm.img",
    "system_ext.img",
    "vendor.img",
    "vendor_dlkm.img",
]

# Standalone flash images that sit alongside the ROM ZIP (never inside super).
_BOOT_IMAGE_NAMES = frozenset({
    "boot.img",
    "init_boot.img",
    "vendor_boot.img",
    "recovery.img",
    "dtbo.img",
    "vbmeta.img",
    "vbmeta_system.img",
    "vbmeta_vendor.img",
    "super_empty.img",
    "cust.img",
    "preloader.img",
    "lk.img",
    "logo.img",
    "persist.img",
    "tee.img",
})

# Image format magic constants
_SPARSE_MAGIC        = 0x3AFF26ED
_EROFS_MAGIC         = 0xE2E1F5E0
_EXT4_MAGIC          = 0xEF53
_EROFS_MAGIC_OFFSET  = 1024   # EROFS superblock starts at byte 1024
_EXT4_MAGIC_OFFSET   = 1080   # ext4 superblock magic at 1024+56


# ── Logging ───────────────────────────────────────────────────────────────────

def _log(log_path: Path, text: str) -> None:
    if not text:
        return
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8", errors="replace") as fh:
        if not text.endswith("\n"):
            text += "\n"
        fh.write(text)


def _logprint(log_path: Path, text: str) -> None:
    print(text)
    _log(log_path, text)


# ── Tool helpers ──────────────────────────────────────────────────────────────

def _bundled_tool(name: str) -> Optional[str]:
    """Return absolute path to a bundled tool; chmod +x on Linux/macOS."""
    p = _BIN_DIR / name
    if p.is_file():
        if sys.platform != "win32":
            try:
                p.chmod(p.stat().st_mode | 0o111)
            except Exception:
                pass
        return str(p)
    return None


def _find_tool(name: str) -> Optional[str]:
    """Find tool: bundled bin/ first, then system PATH."""
    bundled = _bundled_tool(name)
    if bundled:
        return bundled
    return shutil.which(name)


def ensure_tool_executable(path: str, log_path: Path) -> bool:
    """chmod +x a bundled tool; no-op on Windows. Logs result."""
    if sys.platform == "win32":
        return True
    try:
        p = Path(path)
        if p.is_file():
            p.chmod(p.stat().st_mode | 0o111)
            _logprint(log_path, f"[tools] chmod +x OK: {path}")
            return True
        _logprint(log_path, f"[tools] chmod skipped (not a file): {path}")
        return False
    except Exception as exc:
        _logprint(log_path, f"[tools] chmod failed: {path}: {exc}")
        return False


def _ensure_all_bin_tools_executable(log_path: Path) -> None:
    """Pre-chmod all bundled tools in bin/ so fallbacks never hit Permission denied."""
    if sys.platform == "win32":
        return
    for name in ("extract.erofs", "simg2img", "lpunpack", "lpmake"):
        p = _BIN_DIR / name
        if p.is_file():
            ensure_tool_executable(str(p), log_path)


# ── Image type detection ──────────────────────────────────────────────────────

def detect_image_type(img_path: Path) -> str:
    """
    Returns 'sparse', 'erofs', 'ext4', or 'unknown'.

    Checks in order:
      offset 0    — Android sparse magic (0x3AFF26ED LE)
      offset 1024 — EROFS superblock magic (0xE2E1F5E0 LE or BE)
      offset 1080 — ext4 superblock magic (0xEF53 LE, at 1024+56)

    First 16 bytes being zero does NOT mean the image is invalid;
    EROFS and ext4 embed their magic far into the header.
    """
    read_size = max(_EXT4_MAGIC_OFFSET + 2, _EROFS_MAGIC_OFFSET + 4)
    try:
        with img_path.open("rb") as fh:
            header = fh.read(read_size)
    except Exception:
        return "unknown"

    # Android sparse — magic is at offset 0
    if len(header) >= 4:
        magic4 = struct.unpack_from("<I", header, 0)[0]
        if magic4 == _SPARSE_MAGIC:
            return "sparse"

    # EROFS — superblock starts at byte 1024, magic is first 4 bytes
    if len(header) >= _EROFS_MAGIC_OFFSET + 4:
        magic_le = struct.unpack_from("<I", header, _EROFS_MAGIC_OFFSET)[0]
        magic_be = struct.unpack_from(">I", header, _EROFS_MAGIC_OFFSET)[0]
        if magic_le == _EROFS_MAGIC or magic_be == _EROFS_MAGIC:
            return "erofs"

    # ext4 — superblock at byte 1024, magic field at superblock+56 = byte 1080
    if len(header) >= _EXT4_MAGIC_OFFSET + 2:
        magic2 = struct.unpack_from("<H", header, _EXT4_MAGIC_OFFSET)[0]
        if magic2 == _EXT4_MAGIC:
            return "ext4"

    return "unknown"


def _header_hex(img_path: Path, n: int = 16) -> str:
    try:
        with img_path.open("rb") as fh:
            raw = fh.read(n)
        return raw.hex(" ")
    except Exception:
        return "(unreadable)"


def _offset_hex(img_path: Path, offset: int, n: int = 8) -> str:
    """Read n bytes at offset and return as hex string."""
    try:
        with img_path.open("rb") as fh:
            fh.seek(offset)
            raw = fh.read(n)
        return raw.hex(" ") if raw else "(empty)"
    except Exception:
        return "(unreadable)"


def _img_size(img_path: Path) -> int:
    try:
        return img_path.stat().st_size
    except Exception:
        return 0


# ── Sparse → raw conversion ───────────────────────────────────────────────────

def convert_sparse_to_raw(
    img_path: Path,
    temp_dir: Path,
    log_path: Path,
) -> Optional[Path]:
    """
    Convert a sparse Android image to raw using simg2img.
    Writes raw image to temp_dir/<stem>_raw.img.
    Returns the raw Path on success, None on failure.
    """
    tool = _find_tool("simg2img")
    if not tool:
        _logprint(log_path, "[sparse→raw] simg2img not found in bin/ or PATH — cannot convert")
        return None

    temp_dir.mkdir(parents=True, exist_ok=True)
    raw_path = temp_dir / (img_path.stem + "_raw.img")

    cmd = [tool, str(img_path), str(raw_path)]
    _logprint(log_path, f"[sparse→raw] cmd: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.stdout.strip():
            _log(log_path, result.stdout)
        if result.stderr.strip():
            _log(log_path, result.stderr)

        if result.returncode == 0 and raw_path.is_file() and raw_path.stat().st_size > 0:
            _logprint(log_path, f"[sparse→raw] success → {raw_path} ({raw_path.stat().st_size} bytes)")
            return raw_path

        _logprint(log_path, f"[sparse→raw] simg2img exited {result.returncode} or output is empty")
        return None
    except Exception as exc:
        _logprint(log_path, f"[sparse→raw] execution error: {exc}")
        return None


# ── EROFS extraction ──────────────────────────────────────────────────────────

def extract_erofs_image(
    img_path: Path,
    out_dir: Path,
    log_path: Path,
) -> bool:
    """
    Extract an EROFS image using extract.erofs from bundled bin/.
    Returns True when files are produced in out_dir.
    """
    tool = _find_tool("extract.erofs")
    if not tool:
        _logprint(log_path, "[erofs] extract.erofs not found in bin/ or PATH")
        return False

    out_dir.mkdir(parents=True, exist_ok=True)
    cmd = [tool, "-i", str(img_path), "-x", "-o", str(out_dir)]
    _logprint(log_path, f"[erofs] cmd: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.stdout.strip():
            _log(log_path, result.stdout)
        if result.stderr.strip():
            _log(log_path, result.stderr)

        if result.returncode != 0:
            _logprint(log_path, f"[erofs] extract.erofs exited {result.returncode}")
            return False

        any_files = any(p.is_file() for p in out_dir.rglob("*"))
        if not any_files:
            _logprint(log_path, "[erofs] extract.erofs returned 0 but output dir is empty")
            return False

        _logprint(log_path, f"[erofs] extraction succeeded → {out_dir}")
        return True
    except Exception as exc:
        _logprint(log_path, f"[erofs] execution error: {exc}")
        return False


# ── ext4 extraction (native, debugfs) ────────────────────────────────────────

def extract_ext_image(
    img_path: Path,
    out_dir: Path,
    log_path: Path,
) -> bool:
    """
    Extract an ext4 image using debugfs (rdump).
    Returns True when files are produced in out_dir.
    Falls back gracefully if debugfs is not available.
    """
    debugfs = shutil.which("debugfs")
    if not debugfs:
        _logprint(log_path, "[ext4] debugfs not found in PATH — cannot extract natively")
        return False

    out_dir.mkdir(parents=True, exist_ok=True)
    # debugfs rdump: dump all files from / into out_dir
    cmd = [debugfs, "-R", f"rdump / {out_dir!s}", str(img_path)]
    _logprint(log_path, f"[ext4] cmd: {' '.join(cmd)}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.stdout.strip():
            _log(log_path, result.stdout)
        if result.stderr.strip():
            _log(log_path, result.stderr)

        any_files = any(p.is_file() for p in out_dir.rglob("*"))
        if any_files:
            _logprint(log_path, f"[ext4] debugfs extraction succeeded → {out_dir}")
            return True

        _logprint(log_path, "[ext4] debugfs ran but output dir is empty")
        return False
    except Exception as exc:
        _logprint(log_path, f"[ext4] debugfs execution error: {exc}")
        return False


# ── MEZOBuildRom fallback ─────────────────────────────────────────────────────

def _extract_with_legacy_fallback(
    img_path: Path,
    partition_name: str,
    project_dir: Path,
    log_path: Path,
    parts_info: dict[str, str],
) -> bool:
    """
    Last-resort fallback: copy img to project_dir, call MEZOBuildRom.extract_single_partition,
    then clean up the .img copy. The original img_path in payload_extracted is never touched.
    Returns True if a non-empty partition folder was created.
    """
    _logprint(
        log_path,
        f"[fallback] MEZOBuildRom.extract_single_partition used for {partition_name}",
    )

    from factory.unpack.payload import _legacy  # lazy-import, safe CWD guard

    legacy = _legacy()
    dst_img = project_dir / img_path.name

    try:
        if dst_img.exists():
            _remove_force(dst_img)
        shutil.copy2(str(img_path), str(dst_img))
        legacy.extract_single_partition(dst_img, project_dir, parts_info)

        out_folder = project_dir / partition_name
        if out_folder.is_dir() and any(p.is_file() for p in out_folder.rglob("*")):
            _logprint(log_path, f"[fallback] success → {out_folder}")
            return True

        _logprint(log_path, f"[fallback] ran but folder not created or empty: {project_dir / partition_name}")
        return False
    except Exception as exc:
        _logprint(log_path, f"[fallback] exception: {exc}")
        return False
    finally:
        if dst_img.exists():
            _remove_force(dst_img)


# ── Safe temp helpers ─────────────────────────────────────────────────────────

def _remove_force(path: Path) -> None:
    try:
        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)
        else:
            path.unlink(missing_ok=True)
    except Exception:
        pass


def _cleanup_dir(tmp_dir: Path, log_path: Path) -> None:
    if tmp_dir.exists():
        try:
            shutil.rmtree(tmp_dir, ignore_errors=True)
        except Exception as exc:
            _log(log_path, f"[cleanup] error removing {tmp_dir}: {exc}")


# ── Per-partition extraction ──────────────────────────────────────────────────

def extract_partition_image(
    img_path: Path,
    partition_name: str,
    project_dir: Path,
    log_path: Path,
    parts_info: dict[str, str],
) -> dict:
    """
    Extract one dynamic partition image into project_dir/<partition_name>/.

    Safe temp flow:
      1. Source image stays in payload_extracted (never moved/deleted)
      2. If sparse → convert to raw in project_dir/.tmp_raw/
      3. Extract into project_dir/.extract_tmp/<partition>/
      4. On success: rename .extract_tmp/<partition>/ → project_dir/<partition>/
      5. Clean temp files only after success
      6. If native extraction fails → MEZOBuildRom fallback

    Returns a result dict with image_found, image_size, detected_type, status, error.
    Also mutates parts_info on success to record {partition_name: fs_type}.
    """
    result: dict = {
        "image_found": False,
        "image_size": 0,
        "detected_type": "unknown",
        "status": "SKIPPED",
        "error": None,
        "native": False,
        "fallback": False,
        "output_folder_exists": False,
        "build_prop_exists": False,
    }

    tmp_raw_dir  = project_dir / ".tmp_raw"
    tmp_extract_dir = project_dir / ".extract_tmp"
    tmp_out      = tmp_extract_dir / partition_name

    _logprint(log_path, f"\n[partition] ─── {partition_name} ───────────────────────────────────")
    _logprint(log_path, f"[partition] source      : {img_path}")
    _logprint(log_path, f"[partition] exists      : {img_path.is_file()}")

    if not img_path.is_file():
        _logprint(log_path, f"[partition] SKIP — image not found")
        return result

    size = _img_size(img_path)
    magic_hex  = _header_hex(img_path)
    offset1024 = _offset_hex(img_path, _EROFS_MAGIC_OFFSET, 8)
    erofs_hex  = _offset_hex(img_path, _EROFS_MAGIC_OFFSET, 4)
    ext4_hex   = _offset_hex(img_path, _EXT4_MAGIC_OFFSET, 2)
    raw_type   = detect_image_type(img_path)

    result["image_found"]  = True
    result["image_size"]   = size
    result["detected_type"] = raw_type

    _logprint(log_path, f"[partition] size            : {size} bytes ({size // 1024 // 1024} MiB)")
    _logprint(log_path, f"[partition] header hex (0)  : {magic_hex}")
    _logprint(log_path, f"[partition] bytes @1024     : {offset1024}")
    _logprint(log_path, f"[partition] erofs magic @1024: {erofs_hex}  (expect e0 f5 e1 e2 LE)")
    _logprint(log_path, f"[partition] ext4 magic @1080 : {ext4_hex}   (expect 53 ef LE)")
    _logprint(log_path, f"[partition] detected_type   : {raw_type}")

    work_img    = img_path
    work_type   = raw_type
    raw_created = None

    # Step 1: sparse → raw conversion
    if raw_type == "sparse":
        _logprint(log_path, f"[partition] converting sparse → raw …")
        raw_created = convert_sparse_to_raw(img_path, tmp_raw_dir, log_path)
        if raw_created is not None:
            work_img  = raw_created
            work_type = detect_image_type(raw_created)
            _logprint(log_path, f"[partition] raw type after conversion: {work_type}")
        else:
            _logprint(log_path, f"[partition] sparse conversion failed; using original for fallback")

    # Prepare temp extraction directory
    if tmp_out.exists():
        _remove_force(tmp_out)
    tmp_out.mkdir(parents=True, exist_ok=True)

    extraction_ok = False
    method_used   = "none"

    # Step 2: chmod bundled tools before any extraction attempt
    _ensure_all_bin_tools_executable(log_path)

    # Step 3: attempt native extraction
    if work_type == "erofs":
        _logprint(log_path, f"[partition] extracting EROFS …")
        extraction_ok = extract_erofs_image(work_img, tmp_out, log_path)
        method_used = "erofs"
    elif work_type == "ext4":
        _logprint(log_path, f"[partition] extracting ext4 (debugfs) …")
        extraction_ok = extract_ext_image(work_img, tmp_out, log_path)
        method_used = "ext4/debugfs"
    else:
        _logprint(log_path, f"[partition] type '{work_type}' — no native extractor available")

    # Verify output is non-empty even if extractor claimed success
    if extraction_ok:
        any_files = any(p.is_file() for p in tmp_out.rglob("*"))
        if not any_files:
            _logprint(log_path, f"[partition] extractor reported success but output dir is empty")
            extraction_ok = False

    if extraction_ok:
        # Move temp dir to final location atomically
        final_out = project_dir / partition_name
        if final_out.exists():
            _remove_force(final_out)
        shutil.move(str(tmp_out), str(final_out))

        build_prop_paths = [
            final_out / "build.prop",
            final_out / "system" / "build.prop",
        ]
        bp_exists = any(p.exists() for p in build_prop_paths)
        _logprint(log_path, f"[partition] output folder : {final_out}")
        _logprint(log_path, f"[partition] build.prop    : {bp_exists}")
        _logprint(log_path, f"[partition] method        : {method_used}")
        _logprint(log_path, f"[partition] STATUS        : SUCCESS (native)")

        parts_info[partition_name] = work_type
        result.update({
            "status": "SUCCESS",
            "native": True,
            "fallback": False,
            "output_folder_exists": final_out.is_dir(),
            "build_prop_exists": bp_exists,
        })

        # Clean temp files only after success
        _cleanup_dir(tmp_raw_dir, log_path)
        if tmp_out.exists():
            _remove_force(tmp_out)

        return result

    # Fallback: chmod again explicitly before delegating to MEZOBuildRom
    if tmp_out.exists():
        _remove_force(tmp_out)
    _logprint(log_path, f"[partition] native extraction failed — trying MEZOBuildRom fallback")
    _ensure_all_bin_tools_executable(log_path)

    fallback_ok = _extract_with_legacy_fallback(
        img_path, partition_name, project_dir, log_path, parts_info
    )
    _cleanup_dir(tmp_raw_dir, log_path)

    if fallback_ok:
        final_out = project_dir / partition_name
        build_prop_paths = [
            final_out / "build.prop",
            final_out / "system" / "build.prop",
        ]
        bp_exists = any(p.exists() for p in build_prop_paths)
        _logprint(log_path, f"[partition] STATUS        : SUCCESS (fallback)")
        result.update({
            "status": "SUCCESS",
            "native": False,
            "fallback": True,
            "output_folder_exists": final_out.is_dir(),
            "build_prop_exists": bp_exists,
        })
    else:
        _logprint(log_path, f"[partition] STATUS        : FAILED")
        result.update({
            "status": "FAILED",
            "native": False,
            "fallback": True,
            "error": (
                f"Both native ({work_type}) and MEZOBuildRom fallback failed. "
                f"See output/logs/partition_extract.log"
            ),
        })

    return result


# ── Main orchestrator ─────────────────────────────────────────────────────────

def list_payload_dynamic_images(payload_out_dir: Path) -> list[str]:
    """Return names of dynamic partition .img files found in payload_out_dir."""
    found = []
    for name in _DYNAMIC_PARTITION_IMGS:
        if (payload_out_dir / name).is_file():
            found.append(name)
    return found


def extract_dynamic_partitions_from_payload_dir(
    payload_out_dir: Path,
    project_dir: Path,
    log_path: Optional[Path] = None,
) -> tuple[dict[str, str], dict[str, dict]]:
    """
    For each expected dynamic partition image found in payload_out_dir,
    extract it into project_dir/<partition_name>/ using DeadZone-native tools.
    MEZOBuildRom.extract_single_partition is used only as a last-resort fallback.

    Safe flow:
      - Source images in payload_out_dir are never moved or deleted here.
      - Extraction uses temp dirs (.tmp_raw/, .extract_tmp/) under project_dir.
      - Only after success does the final project_dir/<partition>/ appear.

    Args:
        payload_out_dir: directory where payload.bin extraction placed .img files
        project_dir:     directory where partition folders should be created
        log_path:        where to write the detailed partition extraction log
                         (defaults to project_dir/../../logs/partition_extract.log)

    Returns:
        (parts_info, partition_extract_results)
        parts_info: {partition_name: fs_type} for successfully extracted partitions
        partition_extract_results: {partition_name: {image_found, image_size,
                                    detected_type, status, error, native}}
    """
    if log_path is None:
        # Compute a sensible default: two levels up from project_dir is usually output/
        log_path = project_dir.parent.parent / "logs" / "partition_extract.log"

    log_path.parent.mkdir(parents=True, exist_ok=True)

    config_dir = project_dir / "config"
    config_dir.mkdir(parents=True, exist_ok=True)

    parts_info: dict[str, str] = {}
    partition_extract_results: dict[str, dict] = {}

    _logprint(log_path, f"\n[partitions] ══════════════════════════════════════════")
    _logprint(log_path, f"[partitions] DeadZone Partition Extraction")
    _logprint(log_path, f"[partitions] payload_out_dir : {payload_out_dir}")
    _logprint(log_path, f"[partitions] project_dir     : {project_dir}")
    _logprint(log_path, f"[partitions] ══════════════════════════════════════════")

    # Pre-chmod all bundled tools so Permission denied never blocks extraction or fallback
    _ensure_all_bin_tools_executable(log_path)

    imgs_found = list_payload_dynamic_images(payload_out_dir)
    _logprint(log_path, f"[partitions] Dynamic images found: {imgs_found or '(none)'}")

    if not imgs_found:
        _logprint(log_path, "[partitions] No dynamic partition images found — nothing to extract")
        return parts_info, partition_extract_results

    for img_name in _DYNAMIC_PARTITION_IMGS:
        src_img = payload_out_dir / img_name
        if not src_img.is_file():
            continue

        partition_name = img_name.replace(".img", "")
        result = extract_partition_image(
            img_path=src_img,
            partition_name=partition_name,
            project_dir=project_dir,
            log_path=log_path,
            parts_info=parts_info,
        )
        partition_extract_results[partition_name] = result

    # Persist parts_info for downstream stages
    if parts_info:
        _write_parts_info(config_dir, parts_info)

    _logprint(log_path, f"\n[partitions] ══════════════════════════════════════════")
    _logprint(log_path, f"[partitions] Summary: {len(parts_info)}/{len(imgs_found)} partitions extracted")
    for name, fs in sorted(parts_info.items()):
        _logprint(log_path, f"[partitions]   ✓ {name} ({fs})")
    for name, res in sorted(partition_extract_results.items()):
        if res.get("status") != "SUCCESS":
            _logprint(log_path, f"[partitions]   ✗ {name}: {res.get('status')} — {res.get('error', '')}")
    _logprint(log_path, f"[partitions] ══════════════════════════════════════════\n")

    return parts_info, partition_extract_results


# ── Existing public helpers (unchanged interface) ─────────────────────────────

def collect_extracted_partitions(project_dir: Path) -> list[str]:
    """Return names of dynamic partitions extracted into project_dir (as dirs)."""
    found: list[str] = []
    for name in sorted(_DYNAMIC_PARTITION_NAMES):
        if (project_dir / name).is_dir():
            found.append(name)
    return found


def collect_boot_images(rom_extract_dir: Path) -> list[str]:
    """Return filenames of standalone boot-class images under rom_extract_dir."""
    found: set[str] = set()
    _scan_dir_for_boot_images(rom_extract_dir, found)
    try:
        for child in rom_extract_dir.iterdir():
            if child.is_dir():
                _scan_dir_for_boot_images(child, found)
    except Exception:
        pass
    return sorted(found)


def _scan_dir_for_boot_images(directory: Path, result: set[str]) -> None:
    try:
        for entry in directory.iterdir():
            if entry.is_file() and entry.name.lower() in _BOOT_IMAGE_NAMES:
                result.add(entry.name)
    except Exception:
        pass


def _write_parts_info(config_dir: Path, parts_info: dict[str, str]) -> None:
    """Merge parts_info into config_dir/parts_info (JSON)."""
    parts_info_path = config_dir / "parts_info"
    existing: dict = {}
    try:
        if parts_info_path.exists():
            existing = json.loads(parts_info_path.read_text(encoding="utf-8"))
    except Exception:
        existing = {}
    if isinstance(existing, dict):
        existing.update(parts_info)
    else:
        existing = dict(parts_info)
    parts_info_path.write_text(
        json.dumps(existing, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
