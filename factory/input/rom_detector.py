"""ROM format detection for DeadZone Factory.

Inspects archive contents without relying on filename alone.
Returns a RomDetectionResult with format classification, metadata,
and a confidence score.

Supported formats
-----------------
    payload_ota      — ZIP/TAR containing payload.bin (OTA update)
    fastboot_tgz     — .tgz / .tar.gz with images/ directory
    fastboot_tar     — .tar with images/ directory
    images_zip       — ZIP with images/*.img or firmware-update/*.img
    xiaomi_eu_zip    — Xiaomi.eu ZIP (EU markers + super.img)
    split_super_zip  — ZIP/TAR with super.img.0 / super.img.1 / …
    new_dat_br_zip   — ZIP/TAR containing *.new.dat.br files
    raw_super_zip    — ZIP/TAR containing super.img directly
    unknown          — nothing recognised

Safety rules
------------
- Never guess dangerous build parameters from filename only.
- If the archive is not readable, return FORMAT_UNKNOWN with errors.
- check_codename_match() fails unless force=True when codenames conflict.
"""
from __future__ import annotations

import re
import tarfile
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ── Format constants ──────────────────────────────────────────────────────────
FORMAT_PAYLOAD_OTA = "payload_ota"
FORMAT_FASTBOOT_TGZ = "fastboot_tgz"
FORMAT_FASTBOOT_TAR = "fastboot_tar"
FORMAT_IMAGES_ZIP = "images_zip"
FORMAT_XIAOMI_EU_ZIP = "xiaomi_eu_zip"
FORMAT_SPLIT_SUPER_ZIP = "split_super_zip"
FORMAT_NEW_DAT_BR_ZIP = "new_dat_br_zip"
FORMAT_RAW_SUPER_ZIP = "raw_super_zip"
FORMAT_UNKNOWN = "unknown"

ARCHIVE_TYPE_ZIP = "zip"
ARCHIVE_TYPE_TGZ = "tgz"
ARCHIVE_TYPE_TAR = "tar"
ARCHIVE_TYPE_UNKNOWN = "unknown"

_EU_MARKERS: frozenset[str] = frozenset({
    "xiaomi.eu_multilang",
    "meta-inf/com/miui",
    "eu_multilang",
})

_EU_FILENAME_RE = re.compile(r"xiaomi\.eu|eu_multilang", re.IGNORECASE)


@dataclass
class RomDetectionResult:
    """Result returned by detect_rom_format()."""

    rom_path: Path
    rom_format: str = FORMAT_UNKNOWN
    archive_type: str = ARCHIVE_TYPE_UNKNOWN
    has_payload_bin: bool = False
    has_images_dir: bool = False
    has_super_img: bool = False
    has_split_super: bool = False
    has_new_dat_br: bool = False
    detected_device_codename: Optional[str] = None
    detected_android_version: Optional[str] = None
    detected_hyperos_or_miui_version: Optional[str] = None
    detected_region: Optional[str] = None
    confidence: float = 0.0
    reason: str = ""
    errors: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    member_names: list = field(default_factory=list)


# ── Archive helpers ───────────────────────────────────────────────────────────

def _is_zip(path: Path) -> bool:
    try:
        return zipfile.is_zipfile(str(path))
    except Exception:
        return False


def _is_tar(path: Path) -> bool:
    try:
        return tarfile.is_tarfile(str(path))
    except Exception:
        return False


def _list_zip_members(path: Path) -> list[str]:
    try:
        with zipfile.ZipFile(str(path), "r") as zf:
            return zf.namelist()
    except Exception:
        return []


def _list_tar_members(path: Path) -> list[str]:
    try:
        with tarfile.open(str(path), "r:*") as tf:
            return tf.getnames()
    except Exception:
        return []


def _read_zip_member(path: Path, name: str) -> Optional[bytes]:
    try:
        with zipfile.ZipFile(str(path), "r") as zf:
            return zf.read(name)
    except Exception:
        return None


def _read_tar_member(path: Path, name: str) -> Optional[bytes]:
    try:
        with tarfile.open(str(path), "r:*") as tf:
            fh = tf.extractfile(tf.getmember(name))
            return fh.read() if fh else None
    except Exception:
        return None


# ── Content analysis ──────────────────────────────────────────────────────────

def _analyse_members(members: list[str]) -> dict:
    """Classify content signals from archive member names."""
    lower = [m.lower() for m in members]

    has_payload_bin = any(m.endswith("payload.bin") for m in lower)
    has_new_dat_br = any(m.endswith(".new.dat.br") for m in lower)

    has_images_dir = any(
        (m.startswith("images/") or m.startswith("firmware-update/")) and m.endswith(".img")
        for m in lower
    )

    has_super_img = any(
        m == "super.img" or m.endswith("/super.img")
        for m in lower
    )

    split_parts = [m for m in lower if re.search(r"super\.img\.\d+$", m)]
    has_split_super = len(split_parts) >= 2

    is_eu = any(
        marker in m for m in lower for marker in _EU_MARKERS
    ) or any(_EU_FILENAME_RE.search(m) for m in members)

    img_count = sum(1 for m in lower if m.endswith(".img") and "super" not in m.rsplit("/", 1)[-1])

    return {
        "has_payload_bin": has_payload_bin,
        "has_new_dat_br": has_new_dat_br,
        "has_images_dir": has_images_dir,
        "has_super_img": has_super_img,
        "has_split_super": has_split_super,
        "split_super_count": len(split_parts),
        "is_eu": is_eu,
        "img_count": img_count,
    }


def _parse_build_prop(content: bytes) -> dict[str, str]:
    props: dict[str, str] = {}
    try:
        for line in content.decode("utf-8", errors="replace").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            k, _, v = line.partition("=")
            props[k.strip()] = v.strip()
    except Exception:
        pass
    return props


def _extract_metadata(
    members: list[str],
    read_fn,
) -> tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
    """Read build.prop from archive → (codename, android_ver, hyper_miui, region)."""
    codename = android_ver = hyper_miui = region = None
    candidates = [
        m for m in members
        if m.lower().endswith("build.prop") and (
            "system" in m.lower() or "/" not in m
        )
    ]
    for candidate in candidates[:3]:
        content = read_fn(candidate)
        if not content:
            continue
        props = _parse_build_prop(content)
        if not codename:
            codename = (
                props.get("ro.product.device")
                or props.get("ro.build.product")
                or props.get("ro.product.name")
            )
        if not android_ver:
            android_ver = props.get("ro.build.version.release")
        if not hyper_miui:
            hyper_miui = (
                props.get("ro.mi.os.version.name")
                or props.get("ro.miui.ui.version.name")
                or props.get("ro.build.version.incremental")
            )
        if not region:
            region = props.get("ro.miui.region") or props.get("ro.product.locale.region")
        if codename and android_ver:
            break
    return codename, android_ver, hyper_miui, region


# ── Public API ─────────────────────────────────────────────────────────────────

def detect_rom_format(rom_path: Path) -> RomDetectionResult:
    """Detect the format of a ROM archive by inspecting its contents.

    Detection priority:
    1. payload_ota      — payload.bin present
    2. split_super_zip  — super.img.N parts (>=2) present
    3. xiaomi_eu_zip    — EU markers + super.img
    4. raw_super_zip    — super.img present
    5. new_dat_br_zip   — *.new.dat.br files present
    6. fastboot_tgz     — TGZ/TAR.GZ with image files
    7. fastboot_tar     — TAR with image files
    8. images_zip       — ZIP with images/ directory
    9. unknown          — nothing recognised

    Never guesses from filename alone; always reads archive contents.
    """
    rom_path = Path(rom_path)
    result = RomDetectionResult(rom_path=rom_path)

    if not rom_path.exists():
        result.errors.append(f"ROM file not found: {rom_path}")
        result.reason = "file not found"
        return result

    if not rom_path.is_file():
        result.errors.append(f"ROM path is not a file: {rom_path}")
        result.reason = "not a file"
        return result

    # ── Determine archive type ────────────────────────────────────────────────
    is_zip = _is_zip(rom_path)
    is_tar = False if is_zip else _is_tar(rom_path)

    if is_zip:
        result.archive_type = ARCHIVE_TYPE_ZIP
        members = _list_zip_members(rom_path)
        read_fn = lambda name: _read_zip_member(rom_path, name)
    elif is_tar:
        name_lower = rom_path.name.lower()
        result.archive_type = (
            ARCHIVE_TYPE_TGZ
            if (name_lower.endswith(".tgz") or name_lower.endswith(".tar.gz"))
            else ARCHIVE_TYPE_TAR
        )
        members = _list_tar_members(rom_path)
        read_fn = lambda name: _read_tar_member(rom_path, name)
    else:
        result.rom_format = FORMAT_UNKNOWN
        result.reason = "file is not a recognisable archive (not ZIP or TAR)"
        result.errors.append(result.reason)
        return result

    if not members:
        result.rom_format = FORMAT_UNKNOWN
        result.reason = "archive is empty or member list could not be read"
        result.errors.append(result.reason)
        return result

    result.member_names = members
    signals = _analyse_members(members)
    result.has_payload_bin = signals["has_payload_bin"]
    result.has_images_dir = signals["has_images_dir"]
    result.has_super_img = signals["has_super_img"]
    result.has_split_super = signals["has_split_super"]
    result.has_new_dat_br = signals["has_new_dat_br"]

    # Best-effort metadata extraction
    try:
        codename, android_ver, hyper_miui, region = _extract_metadata(members, read_fn)
        result.detected_device_codename = codename
        result.detected_android_version = android_ver
        result.detected_hyperos_or_miui_version = hyper_miui
        result.detected_region = region
    except Exception as exc:
        result.warnings.append(f"metadata extraction failed: {exc}")

    # ── Classification (priority order) ───────────────────────────────────────
    #
    # IMPORTANT: For TAR/TGZ archives, fastboot_tgz/tar is checked BEFORE
    # raw_super_zip.  Real fastboot packages (e.g. zorn) contain images/super.img
    # alongside all other partition images — they must never be classified as
    # raw_super_zip just because super.img is present.
    # raw_super_zip is reserved for ZIP-like archives where super.img is the
    # primary content and there is no proper images/ fastboot directory.

    if signals["has_payload_bin"]:
        result.rom_format = FORMAT_PAYLOAD_OTA
        result.confidence = 1.0
        result.reason = "payload.bin found inside archive"
        return result

    if signals["has_split_super"]:
        result.rom_format = FORMAT_SPLIT_SUPER_ZIP
        result.confidence = 0.95
        result.reason = f"split super.img detected ({signals['split_super_count']} parts)"
        return result

    # For TAR/TGZ: fastboot classification takes priority over raw_super_zip.
    # A fastboot package naturally includes super.img — don't misclassify it.
    if result.archive_type in (ARCHIVE_TYPE_TGZ, ARCHIVE_TYPE_TAR):
        if signals["has_images_dir"] or signals["img_count"] >= 3:
            if result.archive_type == ARCHIVE_TYPE_TGZ:
                result.rom_format = FORMAT_FASTBOOT_TGZ
                result.confidence = 0.90
                result.reason = "TGZ archive with image files"
            else:
                result.rom_format = FORMAT_FASTBOOT_TAR
                result.confidence = 0.90
                result.reason = "TAR archive with image files"
            return result

    if signals["is_eu"] and signals["has_super_img"]:
        result.rom_format = FORMAT_XIAOMI_EU_ZIP
        result.confidence = 0.90
        result.reason = "Xiaomi EU markers and super.img detected"
        return result

    if signals["has_super_img"]:
        result.rom_format = FORMAT_RAW_SUPER_ZIP
        result.confidence = 0.85
        result.reason = "super.img found directly in archive"
        return result

    if signals["has_new_dat_br"]:
        result.rom_format = FORMAT_NEW_DAT_BR_ZIP
        result.confidence = 0.90
        result.reason = "*.new.dat.br files detected"
        return result

    if signals["has_images_dir"] or signals["img_count"] >= 3:
        result.rom_format = FORMAT_IMAGES_ZIP
        result.confidence = 0.80
        result.reason = "ZIP archive with images directory"
        return result

    result.rom_format = FORMAT_UNKNOWN
    result.confidence = 0.0
    result.reason = "no recognisable ROM layout signals detected in archive"
    return result


def check_codename_match(
    detected: Optional[str],
    selected: str,
    force: bool = False,
) -> tuple[bool, str]:
    """Verify detected codename matches selected codename.

    Returns (ok, message).
    Fails (ok=False) when codenames conflict unless force=True.
    """
    if not detected:
        return True, "detected codename unknown — skipping match check"

    detected_norm = detected.strip().lower()
    selected_norm = selected.strip().lower()

    if detected_norm == selected_norm:
        return True, f"codename match: {selected}"

    msg = (
        f"codename mismatch: detected={detected!r} vs selected={selected!r}. "
        f"Pass force=True to override this safety check."
    )
    if force:
        return True, f"FORCED: {msg}"
    return False, msg
