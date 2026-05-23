"""
Legend fstab patcher.

Patches vendor/etc/fstab.emmc and vendor/etc/fstab.mt6886 inside an
unpacked ROM root:

  1. Remove AVB flags from dynamic partition mount lines.
  2. Add mi_ext / pangu overlay lines after the mi_ext bind mount if absent.
  3. Remove miui_dlkm lines completely (avoids boot failure when absent from super).
  4. Create .dzlegend.bak backups (skip if backup already exists).
  5. Report all changes to the unified patch report.
"""
from __future__ import annotations

import re
import shutil
from pathlib import Path
from typing import Optional


# ── Fstab filenames ───────────────────────────────────────────────────────────

FSTAB_NAMES = ("fstab.emmc", "fstab.mt6886")

# ── AVB flags to strip ────────────────────────────────────────────────────────

_AVB_FLAG_PATTERNS: tuple[re.Pattern, ...] = (
    re.compile(r"(?<![=\w])avb_keys=/avb/q-gsi\.avbpubkey:/avb/r-gsi\.avbpubkey:/avb/s-gsi\.avbpubkey"),
    re.compile(r"(?<![=\w])avb=vbmeta_system(?!\w)"),
    re.compile(r"(?<![=\w])avb=vbmeta(?!\w)"),
    re.compile(r"(?<![=\w])avb(?![_=\w])"),
)

# Mount points of dynamic partitions — AVB flags are removed only on these.
_DYNAMIC_MOUNT_POINTS = frozenset({
    "/system", "/vendor", "/product",
    "/mnt/vendor/mi_ext",
    "/odm", "/vendor_dlkm", "/odm_dlkm", "/system_dlkm", "/system_ext",
    "/vbmeta_system",
})

# Mount points that must never be touched.
_PROTECTED_MOUNT_POINTS = frozenset({
    "/data", "/metadata",
    "/mnt/vendor/persist", "/mnt/vendor/nvdata", "/mnt/vendor/nvcfg",
    "/mnt/vendor/protect_f", "/mnt/vendor/protect_s",
})

# ── miui_dlkm markers — lines containing any of these are removed ─────────────

_MIUI_DLKM_MARKERS = (
    "miui_dlkm",
    "/mnt/vendor/miui_dlkm",
    "/miui_dlkm",
)

# ── Overlay lines to inject after the mi_ext bind mount ──────────────────────

_MI_EXT_BIND_RE = re.compile(
    r"^\S+\s+/mi_ext\s+\S+\s+.*\bbind\b", re.IGNORECASE
)

_OVERLAY_LINES: tuple[str, ...] = (
    "overlay /product/overlay overlay ro,lowerdir=/mnt/vendor/mi_ext/product/overlay/:/product/overlay check,nofail",
    "overlay /product/app overlay ro,lowerdir=/mnt/vendor/mi_ext/product/app/:/product/app check,nofail",
    "overlay /product/priv-app overlay ro,lowerdir=/mnt/vendor/mi_ext/product/priv-app/:/product/priv-app check,nofail",
    "overlay /product/lib overlay ro,lowerdir=/mnt/vendor/mi_ext/product/lib/:/product/lib check,nofail",
    "overlay /product/lib64 overlay ro,lowerdir=/mnt/vendor/mi_ext/product/lib64/:/product/lib64 check,nofail",
    "overlay /product/bin overlay ro,lowerdir=/mnt/vendor/mi_ext/product/bin/:/product/bin check,nofail",
    "overlay /product/framework overlay ro,lowerdir=/mnt/vendor/mi_ext/product/framework/:/product/framework check,nofail",
    "overlay /product/media overlay ro,lowerdir=/mnt/vendor/mi_ext/product/media/:/product/media check,nofail",
    "overlay /product/opcust overlay ro,lowerdir=/mnt/vendor/mi_ext/product/opcust/:/product/opcust check,nofail",
    "overlay /product/data-app overlay ro,lowerdir=/mnt/vendor/mi_ext/product/data-app/:/product/data-app check,nofail",
    "overlay /product/etc/sysconfig overlay ro,lowerdir=/mnt/vendor/mi_ext/product/etc/sysconfig/:/product/etc/sysconfig check,nofail",
    "overlay /product/etc/permissions overlay ro,lowerdir=/mnt/vendor/mi_ext/product/etc/permissions/:/product/etc/permissions check,nofail",
    "overlay /system/app overlay ro,lowerdir=/mnt/vendor/mi_ext/system/app/:/product/pangu/system/app/:/system/app check,nofail",
    "overlay /system/priv-app overlay ro,lowerdir=/mnt/vendor/mi_ext/system/priv-app/:/product/pangu/system/priv-app/:/system/priv-app check,nofail",
    "overlay /system/framework overlay ro,lowerdir=/product/pangu/system/framework/:/system/framework check,nofail",
    "overlay /system/etc/sysconfig overlay ro,lowerdir=/mnt/vendor/mi_ext/system/etc/sysconfig/:/system/etc/sysconfig check,nofail",
    "overlay /system/etc/permissions overlay ro,lowerdir=/mnt/vendor/mi_ext/system/etc/permissions/:/product/pangu/system/etc/permissions/:/system/etc/permissions check,nofail",
    "overlay /product/usr overlay ro,lowerdir=/mnt/vendor/mi_ext/product/usr:/product/usr check,nofail",
    "overlay /product/etc/precust_theme overlay ro,lowerdir=/mnt/vendor/mi_ext/product/etc/precust_theme:/product/etc/precust_theme check,nofail",
    "overlay /product/etc/preferred-apps overlay ro,lowerdir=/mnt/vendor/mi_ext/product/etc/preferred-apps:/product/etc/preferred-apps check,nofail",
    "overlay /product/etc/security overlay ro,lowerdir=/mnt/vendor/mi_ext/product/etc/security:/product/etc/security check,nofail",
    "overlay /system_ext/etc/permissions overlay ro,lowerdir=/mnt/vendor/mi_ext/system_ext/etc/permissions:/system_ext/etc/permissions check,nofail",
)


# ── Internal helpers ──────────────────────────────────────────────────────────

def _mount_point_of(line: str) -> Optional[str]:
    """Return the 2nd whitespace-delimited token (mount point) or None."""
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    parts = stripped.split()
    return parts[1] if len(parts) >= 2 else None


def _is_miui_dlkm_line(line: str) -> bool:
    lo = line.lower()
    return any(m in lo for m in _MIUI_DLKM_MARKERS)


def _strip_avb_from_flags(flags_field: str) -> tuple[str, int]:
    """
    Remove AVB-related tokens from a comma-separated fs_mgr_flags field.
    Returns (new_flags, removed_count).
    """
    tokens = [t.strip() for t in flags_field.split(",")]
    removed = 0
    kept: list[str] = []
    for tok in tokens:
        original = tok
        for pat in _AVB_FLAG_PATTERNS:
            tok = pat.sub("", tok).strip()
        if tok != original or not tok:
            if original:
                removed += 1
        if tok:
            kept.append(tok)
    return ",".join(kept), removed


def _process_line_avb(line: str) -> tuple[str, int]:
    """
    Strip AVB flags from a single fstab line if its mount point is a
    dynamic partition.  Returns (new_line, avb_removed_count).
    """
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return line, 0

    mp = _mount_point_of(line)
    if mp is None:
        return line, 0
    if mp in _PROTECTED_MOUNT_POINTS:
        return line, 0
    if mp not in _DYNAMIC_MOUNT_POINTS:
        return line, 0

    # The fs_mgr_flags are the last whitespace-separated token (5th column).
    parts = stripped.split()
    if len(parts) < 5:
        return line, 0

    flags_field = parts[4]
    new_flags, removed = _strip_avb_from_flags(flags_field)
    if removed == 0:
        return line, 0

    parts[4] = new_flags
    # Reconstruct preserving trailing newline.
    suffix = "\n" if line.endswith("\n") else ""
    return " ".join(parts) + suffix, removed


def _overlay_already_present(lines: list[str]) -> bool:
    """True if at least the first overlay line is already in the file."""
    first_overlay = _OVERLAY_LINES[0].split()[1]  # e.g. /product/overlay
    return any(
        "overlay" in ln and first_overlay in ln
        for ln in lines
    )


def _insert_overlay_lines(lines: list[str]) -> tuple[list[str], int]:
    """
    Find the mi_ext bind-mount line and insert the overlay block after it.
    Returns (new_lines, count_added).
    """
    insert_idx = None
    for i, ln in enumerate(lines):
        if _MI_EXT_BIND_RE.match(ln.strip()):
            insert_idx = i
            # Keep searching in case there are multiple; use the last match.

    if insert_idx is None:
        return lines, 0

    overlay_block = [ol + "\n" for ol in _OVERLAY_LINES]
    new_lines = lines[: insert_idx + 1] + overlay_block + lines[insert_idx + 1 :]
    return new_lines, len(_OVERLAY_LINES)


def _remove_miui_dlkm_lines(lines: list[str]) -> tuple[list[str], int]:
    kept: list[str] = []
    removed = 0
    for ln in lines:
        if _is_miui_dlkm_line(ln):
            removed += 1
        else:
            kept.append(ln)
    return kept, removed


# ── Public API ────────────────────────────────────────────────────────────────

def patch_fstab(
    root: Path,
    *,
    execute: bool = False,
    report_lines: Optional[list[str]] = None,
) -> dict:
    """
    Patch all known fstab files found under root/vendor/etc/.

    Parameters
    ----------
    root        : Path  Root of the unpacked ROM project.
    execute     : bool  True → write changes; False → dry-run only.
    report_lines: list  Optional list to append human-readable report lines to.

    Returns
    -------
    dict with keys:
        found_files, patched_files, avb_flags_removed,
        overlay_lines_added, miui_dlkm_lines_removed, backups_created,
        errors, dry_run
    """
    result: dict = {
        "found_files": [],
        "patched_files": [],
        "avb_flags_removed": 0,
        "overlay_lines_added": 0,
        "miui_dlkm_lines_removed": 0,
        "backups_created": [],
        "errors": [],
        "dry_run": not execute,
    }

    vendor_etc = root / "vendor" / "etc"
    if not vendor_etc.is_dir():
        msg = f"vendor/etc not found under {root}"
        result["errors"].append(msg)
        _log(report_lines, f"[fstab_patcher] ERROR: {msg}")
        return result

    for name in FSTAB_NAMES:
        fstab_path = vendor_etc / name
        if not fstab_path.is_file():
            _log(report_lines, f"[fstab_patcher] NOT FOUND: {fstab_path}")
            continue

        result["found_files"].append(str(fstab_path))
        _log(report_lines, f"[fstab_patcher] Processing: {fstab_path}")

        try:
            original_text = fstab_path.read_text(encoding="utf-8", errors="replace")
        except Exception as exc:
            result["errors"].append(f"read error {name}: {exc}")
            continue

        lines = original_text.splitlines(keepends=True)

        # Step 1: remove miui_dlkm lines
        lines, dlkm_removed = _remove_miui_dlkm_lines(lines)
        result["miui_dlkm_lines_removed"] += dlkm_removed
        _log(report_lines, f"[fstab_patcher]   miui_dlkm lines removed: {dlkm_removed}")

        # Step 2: strip AVB flags
        total_avb = 0
        new_lines: list[str] = []
        for ln in lines:
            patched_ln, removed = _process_line_avb(ln)
            new_lines.append(patched_ln)
            total_avb += removed
        lines = new_lines
        result["avb_flags_removed"] += total_avb
        _log(report_lines, f"[fstab_patcher]   AVB flags removed: {total_avb}")

        # Step 3: inject overlay lines if missing
        overlay_added = 0
        if not _overlay_already_present(lines):
            lines, overlay_added = _insert_overlay_lines(lines)
            _log(report_lines, f"[fstab_patcher]   overlay lines added: {overlay_added}")
        else:
            _log(report_lines, f"[fstab_patcher]   overlay lines already present, skipping")
        result["overlay_lines_added"] += overlay_added

        new_text = "".join(lines)
        changed = new_text != original_text

        if not changed:
            _log(report_lines, f"[fstab_patcher]   no changes needed for {name}")
            continue

        if not execute:
            _log(report_lines, f"[fstab_patcher]   DRY-RUN: would patch {name}")
            result["patched_files"].append(str(fstab_path) + " [dry-run]")
            continue

        # Create backup if not yet present
        bak_path = fstab_path.with_suffix(fstab_path.suffix + ".dzlegend.bak")
        if not bak_path.exists():
            try:
                shutil.copy2(fstab_path, bak_path)
                result["backups_created"].append(str(bak_path))
                _log(report_lines, f"[fstab_patcher]   backup: {bak_path}")
            except Exception as exc:
                result["errors"].append(f"backup failed {name}: {exc}")
                continue

        # Write patched file
        try:
            fstab_path.write_text(new_text, encoding="utf-8")
            result["patched_files"].append(str(fstab_path))
            _log(report_lines, f"[fstab_patcher]   PATCHED: {fstab_path}")
        except Exception as exc:
            result["errors"].append(f"write error {name}: {exc}")

    return result


def _log(report_lines: Optional[list[str]], msg: str) -> None:
    print(msg)
    if report_lines is not None:
        report_lines.append(msg)
