"""ROM archive unpacker for DeadZone Factory.

Accepts rom_path, detected rom_format, and work_dir.
Unpacks into standardised subdirectories.

Output layout
-------------
    work_dir/unpacked_rom/     — full archive extraction
    work_dir/source_images/    — collected .img files
    work_dir/super_parts/      — dynamic partition images
    work_dir/super_workspace/  — lpmake scratch area (created, kept empty here)

Supported formats mirror factory.input.rom_detector FORMAT_* constants.
Unknown format causes an immediate UNSUPPORTED failure — never guesses.
"""
from __future__ import annotations

import re
import shutil
import tarfile
import zipfile
from pathlib import Path

from factory.input.rom_detector import (
    ARCHIVE_TYPE_TGZ,
    ARCHIVE_TYPE_TAR,
    FORMAT_FASTBOOT_TAR,
    FORMAT_FASTBOOT_TGZ,
    FORMAT_IMAGES_ZIP,
    FORMAT_NEW_DAT_BR_ZIP,
    FORMAT_PAYLOAD_OTA,
    FORMAT_RAW_SUPER_ZIP,
    FORMAT_SPLIT_SUPER_ZIP,
    FORMAT_UNKNOWN,
    FORMAT_XIAOMI_EU_ZIP,
)


# ── Archive extraction ────────────────────────────────────────────────────────

def _extract_zip(rom_path: Path, dest: Path) -> list[str]:
    dest.mkdir(parents=True, exist_ok=True)
    try:
        with zipfile.ZipFile(str(rom_path), "r") as zf:
            zf.extractall(str(dest))
            return zf.namelist()
    except Exception as exc:
        raise RuntimeError(f"ZIP extraction failed: {exc}") from exc


def _extract_tar(rom_path: Path, dest: Path) -> list[str]:
    dest.mkdir(parents=True, exist_ok=True)
    try:
        with tarfile.open(str(rom_path), "r:*") as tf:
            tf.extractall(str(dest))
            return tf.getnames()
    except Exception as exc:
        raise RuntimeError(f"TAR extraction failed: {exc}") from exc


def _extract_archive(rom_path: Path, dest: Path) -> list[str]:
    """Extract ZIP or TAR archive; detect type by content."""
    if zipfile.is_zipfile(str(rom_path)):
        return _extract_zip(rom_path, dest)
    return _extract_tar(rom_path, dest)


# ── Image collection ──────────────────────────────────────────────────────────

def _collect_imgs(src_dir: Path, dest: Path) -> list[str]:
    """Recursively copy *.img files from src_dir into dest. Returns copied names."""
    dest.mkdir(parents=True, exist_ok=True)
    copied: list[str] = []
    for img in sorted(src_dir.rglob("*.img")):
        if not img.is_file():
            continue
        target = dest / img.name
        if not target.exists():
            shutil.copy2(img, target)
            copied.append(img.name)
    return copied


# ── Split-super merge ─────────────────────────────────────────────────────────

def _natural_key(p: Path) -> list:
    return [int(x) if x.isdigit() else x.lower() for x in re.split(r"(\d+)", p.name)]


def _suffix_num(p: Path) -> int | None:
    m = re.search(r"\.(\d+)$", p.name)
    return int(m.group(1)) if m else None


def _merge_split_super(parts: list[Path], out: Path, diag: list[str]) -> bool:
    """Concatenate naturally-sorted split super.img.* parts into out."""
    parts = sorted(parts, key=_natural_key)
    nums = [_suffix_num(p) for p in parts]

    if None in nums:
        diag.append(f"ERROR: cannot parse numeric suffix from: {[p.name for p in parts]}")
        return False

    expected = list(range(len(parts)))
    if nums != expected:
        missing = sorted(set(expected) - set(nums))
        diag.append(f"ERROR: split super parts not contiguous — missing indices: {missing}")
        return False

    out.parent.mkdir(parents=True, exist_ok=True)
    total = 0
    _CHUNK = 8 * 1024 * 1024
    try:
        with out.open("wb") as dst:
            for p in parts:
                with p.open("rb") as src:
                    while True:
                        buf = src.read(_CHUNK)
                        if not buf:
                            break
                        dst.write(buf)
                        total += len(buf)
    except OSError as exc:
        diag.append(f"ERROR: I/O error merging split super: {exc}")
        out.unlink(missing_ok=True)
        return False

    diag.append(f"Merged {len(parts)} parts → {out.name} ({total:,} bytes)")
    return True


# ── Public API ─────────────────────────────────────────────────────────────────

def unpack_rom(
    rom_path: Path,
    rom_format: str,
    work_dir: Path,
) -> dict:
    """Unpack a ROM archive into standardised work subdirectories.

    Parameters
    ----------
    rom_path:
        Path to the ROM archive file.
    rom_format:
        One of the FORMAT_* constants from factory.input.rom_detector.
    work_dir:
        Base working directory for all intermediate files.

    Returns
    -------
    dict with keys:
        status              — "OK" | "FAILED" | "UNSUPPORTED"
        unpacked_rom        — str path where archive was extracted
        source_images       — str path where .img files were gathered
        super_parts         — str path for dynamic partition images
        super_workspace     — str path for lpmake scratch area
        split_super_merged  — bool
        split_super_path    — str | None
        messages            — list[str]
        errors              — list[str]
    """
    rom_path = Path(rom_path)
    work_dir = Path(work_dir)

    unpacked_dir = work_dir / "unpacked_rom"
    source_images_dir = work_dir / "source_images"
    super_parts_dir = work_dir / "super_parts"
    super_workspace_dir = work_dir / "super_workspace"

    result: dict = {
        "status": "FAILED",
        "rom_path": str(rom_path),
        "rom_format": rom_format,
        "unpacked_rom": str(unpacked_dir),
        "source_images": str(source_images_dir),
        "super_parts": str(super_parts_dir),
        "super_workspace": str(super_workspace_dir),
        "split_super_merged": False,
        "split_super_path": None,
        "messages": [],
        "errors": [],
    }

    def _msg(s: str) -> None:
        result["messages"].append(s)
        print(f"[rom_unpacker] {s}")

    def _err(s: str) -> None:
        result["errors"].append(s)
        print(f"[rom_unpacker] ERROR: {s}")

    if rom_format == FORMAT_UNKNOWN:
        _err("ROM format is unknown — cannot unpack. Detect format with rom_detector first.")
        result["status"] = "UNSUPPORTED"
        return result

    # Create all workspace dirs up-front
    for d in [unpacked_dir, source_images_dir, super_parts_dir, super_workspace_dir]:
        d.mkdir(parents=True, exist_ok=True)

    # ── payload_ota ───────────────────────────────────────────────────────────
    if rom_format == FORMAT_PAYLOAD_OTA:
        _msg("Format: payload_ota — extracting archive")
        try:
            _extract_archive(rom_path, unpacked_dir)
        except RuntimeError as exc:
            _err(str(exc))
            return result
        payload_list = list(unpacked_dir.rglob("payload.bin"))
        if not payload_list:
            _err("payload.bin not found after extraction")
            return result
        _msg(f"payload.bin found: {payload_list[0]}")
        result["status"] = "OK"
        return result

    # ── fastboot_tgz / fastboot_tar ───────────────────────────────────────────
    if rom_format in (FORMAT_FASTBOOT_TGZ, FORMAT_FASTBOOT_TAR):
        _msg(f"Format: {rom_format} — extracting TAR archive")
        try:
            _extract_tar(rom_path, unpacked_dir)
        except RuntimeError as exc:
            _err(str(exc))
            return result
        copied = _collect_imgs(unpacked_dir, source_images_dir)
        _msg(f"Collected {len(copied)} images → source_images/")
        result["status"] = "OK"
        return result

    # ── images_zip ────────────────────────────────────────────────────────────
    if rom_format == FORMAT_IMAGES_ZIP:
        _msg("Format: images_zip — extracting ZIP archive")
        try:
            _extract_zip(rom_path, unpacked_dir)
        except RuntimeError as exc:
            _err(str(exc))
            return result
        copied = _collect_imgs(unpacked_dir, source_images_dir)
        _msg(f"Collected {len(copied)} images → source_images/")
        result["status"] = "OK"
        return result

    # ── xiaomi_eu_zip / split_super_zip ───────────────────────────────────────
    if rom_format in (FORMAT_XIAOMI_EU_ZIP, FORMAT_SPLIT_SUPER_ZIP):
        _msg(f"Format: {rom_format} — extracting and merging split super")
        try:
            _extract_archive(rom_path, unpacked_dir)
        except RuntimeError as exc:
            _err(str(exc))
            return result

        split_parts = sorted(
            [
                p for p in unpacked_dir.rglob("*")
                if p.is_file() and re.search(r"super\.img\.\d+$", p.name.lower())
            ],
            key=_natural_key,
        )

        if split_parts:
            merged_super = work_dir / "eu_adapter" / "super.img"
            diag: list[str] = []
            ok = _merge_split_super(split_parts, merged_super, diag)
            for line in diag:
                _msg(line)
            if not ok:
                _err("Failed to merge split super.img parts")
                return result
            result["split_super_merged"] = True
            result["split_super_path"] = str(merged_super)
            target = source_images_dir / "super.img"
            if not target.exists():
                shutil.copy2(merged_super, target)
            _msg("Merged super.img placed in source_images/")
        else:
            super_candidates = sorted(unpacked_dir.rglob("super.img"))
            if not super_candidates:
                _err("No super.img or split super parts found after extraction")
                return result
            target = source_images_dir / "super.img"
            if not target.exists():
                shutil.copy2(super_candidates[0], target)
            _msg(f"super.img found and copied to source_images/")

        copied = _collect_imgs(unpacked_dir, source_images_dir)
        _msg(f"Collected {len(copied)} additional images → source_images/")
        result["status"] = "OK"
        return result

    # ── raw_super_zip ─────────────────────────────────────────────────────────
    if rom_format == FORMAT_RAW_SUPER_ZIP:
        _msg("Format: raw_super_zip — extracting archive")
        try:
            _extract_archive(rom_path, unpacked_dir)
        except RuntimeError as exc:
            _err(str(exc))
            return result
        super_candidates = sorted(unpacked_dir.rglob("super.img"))
        if not super_candidates:
            _err("super.img not found in archive after extraction")
            return result
        target = source_images_dir / "super.img"
        if not target.exists():
            shutil.copy2(super_candidates[0], target)
        copied = _collect_imgs(unpacked_dir, source_images_dir)
        _msg(f"super.img extracted, collected {len(copied)} images → source_images/")
        result["status"] = "OK"
        return result

    # ── new_dat_br_zip ────────────────────────────────────────────────────────
    if rom_format == FORMAT_NEW_DAT_BR_ZIP:
        _msg("Format: new_dat_br_zip — extracting archive")
        try:
            _extract_archive(rom_path, unpacked_dir)
        except RuntimeError as exc:
            _err(str(exc))
            return result
        dat_br = list(unpacked_dir.rglob("*.new.dat.br"))
        part_names = [re.sub(r"\.new\.dat\.br$", "", f.name, flags=re.IGNORECASE) for f in dat_br]
        _msg(
            f"Found {len(dat_br)} .new.dat.br files. "
            f"Partitions: {', '.join(part_names) or '(none)'}. "
            f"Conversion is handled by the datbr_adapter pipeline."
        )
        result["new_dat_br_partitions"] = part_names
        result["status"] = "OK"
        return result

    _err(f"Unhandled rom_format: {rom_format!r}")
    result["status"] = "UNSUPPORTED"
    return result
