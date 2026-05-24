"""
Legend build package patcher.

Applies a pre-built Legend OS package into the unpacked ROM root by
copying partition-relative files from:

    factory/patch/legend/build/

into the ROM root, preserving directory structure.

Supported top-level partitions
-------------------------------
    system, product, system_ext, vendor, odm, mi_ext

Status values
-------------
    SKIPPED_TEMPORARY   — build folder missing and LEGEND_BUILD_URL not set
    DRY_RUN             — dry-run mode, no filesystem writes
    APPLIED             — files copied successfully (execute=True)
    FAILED              — unknown top-level folder, zip error, or copy error

External download (optional, env-driven)
-----------------------------------------
Set LEGEND_BUILD_URL to a zip URL.  If the local build folder is absent the
patcher downloads the zip to output/work/legend_build/, extracts it safely,
and applies from the detected build root.

Zip layouts supported
---------------------
    A) system/ product/ system_ext/ ...           (root-level partitions)
    B) build/system build/product ...             (build/ prefix)
    C) Legend_OS3/system Legend_OS3/product ...   (arbitrary single prefix)

Zip safety
----------
    - Rejects paths containing ../
    - Rejects absolute paths (starting with / or Windows drive like C:)
    - Rejects Windows drive paths
"""
from __future__ import annotations

import os
import shutil
import zipfile
from pathlib import Path
from typing import Optional

_REPO_ROOT = Path(__file__).resolve().parents[4]
_LOCAL_BUILD_DIR = _REPO_ROOT / "factory" / "patch" / "legend" / "build"
_WORK_DIR = _REPO_ROOT / "output" / "work" / "legend_build"

ALLOWED_PARTITIONS: frozenset[str] = frozenset({
    "system", "product", "system_ext", "vendor", "odm", "mi_ext",
})


def _log(report_lines: Optional[list[str]], msg: str) -> None:
    print(msg)
    if report_lines is not None:
        report_lines.append(msg)


# ── Zip safety ────────────────────────────────────────────────────────────────

def _is_safe_zip_member(name: str) -> bool:
    parts = name.replace("\\", "/").split("/")
    if ".." in parts:
        return False
    if name.startswith("/"):
        return False
    if len(name) >= 2 and name[1] == ":" and name[0].isalpha():
        return False
    return True


def _detect_zip_build_root(members: list[str]) -> Optional[str]:
    """
    Detect the prefix inside a zip that contains partition top-level dirs.

    Returns the prefix string ("" for layout A, "build" for B, "Legend_OS3"
    for C) or None if no recognisable layout is found.
    """
    hits: dict[str, int] = {}
    for m in members:
        parts = [p for p in m.replace("\\", "/").split("/") if p]
        if not parts:
            continue
        if parts[0] in ALLOWED_PARTITIONS:
            hits[""] = hits.get("", 0) + 1
        elif len(parts) >= 2 and parts[1] in ALLOWED_PARTITIONS:
            hits[parts[0]] = hits.get(parts[0], 0) + 1
    if not hits:
        return None
    return max(hits, key=lambda k: hits[k])


def _extract_zip(
    zip_path: Path,
    dest: Path,
    report_lines: Optional[list[str]],
) -> Optional[Path]:
    """Extract zip safely. Returns dest on success, None on error."""
    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            members = zf.namelist()
            prefix = _detect_zip_build_root(members)
            if prefix is None:
                _log(report_lines,
                     "[build_patcher] ERROR: zip has no recognisable partition structure")
                return None

            dest.mkdir(parents=True, exist_ok=True)
            for m in members:
                if not _is_safe_zip_member(m):
                    _log(report_lines, f"[build_patcher] REJECTED unsafe zip path: {m}")
                    continue
                norm = m.replace("\\", "/")
                if prefix:
                    if not norm.startswith(prefix + "/"):
                        continue
                    rel = norm[len(prefix) + 1:]
                else:
                    rel = norm
                if not rel:
                    continue
                target = dest / rel
                if norm.endswith("/"):
                    target.mkdir(parents=True, exist_ok=True)
                else:
                    target.parent.mkdir(parents=True, exist_ok=True)
                    with zf.open(m) as src, open(target, "wb") as dst:
                        shutil.copyfileobj(src, dst)

            _log(report_lines,
                 f"[build_patcher] zip extracted to {dest} (prefix={prefix!r})")
            return dest
    except Exception as exc:
        _log(report_lines, f"[build_patcher] ERROR extracting zip: {exc}")
        return None


# ── Core copy logic ───────────────────────────────────────────────────────────

def _apply_build_root(
    build_root: Path,
    rom_root: Path,
    execute: bool,
    report_lines: Optional[list[str]],
) -> dict:
    """Copy all files from build_root into rom_root, partition-relative."""
    result: dict = {
        "source_root": str(build_root),
        "copied": [],
        "replaced": [],
        "created_dirs": [],
        "created_empty_dirs": [],
        "vendor_copied": [],
        "vendor_replaced": [],
        "vendor_dirs_created": [],
        "unknown_partitions": [],
        "errors": [],
    }

    try:
        top_dirs = [d for d in build_root.iterdir() if d.is_dir()]
    except Exception as exc:
        result["errors"].append(f"cannot list build root: {exc}")
        return result

    for d in top_dirs:
        if d.name not in ALLOWED_PARTITIONS:
            result["unknown_partitions"].append(d.name)
            _log(report_lines, f"[build_patcher] UNKNOWN partition folder: {d.name}")

    if result["unknown_partitions"]:
        return result

    for src_path in sorted(build_root.rglob("*")):
        rel = src_path.relative_to(build_root)
        dst_path = rom_root / rel
        is_vendor = bool(rel.parts) and rel.parts[0] == "vendor"
        rel_posix = rel.as_posix()

        if src_path.is_dir():
            children = list(src_path.iterdir())
            if execute:
                dst_path.mkdir(parents=True, exist_ok=True)
            if not children:
                result["created_empty_dirs"].append(rel_posix)
                if is_vendor:
                    result["vendor_dirs_created"].append(rel_posix)
                _log(report_lines, f"[build_patcher]   created_empty_dir: {rel_posix}")
            else:
                result["created_dirs"].append(rel_posix)
                if is_vendor:
                    result["vendor_dirs_created"].append(rel_posix)

        elif src_path.is_file():
            already_exists = dst_path.exists()
            try:
                if execute:
                    dst_path.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src_path, dst_path)
            except Exception as exc:
                result["errors"].append(f"copy failed {rel_posix}: {exc}")
                _log(report_lines, f"[build_patcher] ERROR copying {rel_posix}: {exc}")
                continue

            if already_exists:
                result["replaced"].append(rel_posix)
                if is_vendor:
                    result["vendor_replaced"].append(rel_posix)
                _log(report_lines, f"[build_patcher]   replaced: {rel_posix}")
            else:
                result["copied"].append(rel_posix)
                if is_vendor:
                    result["vendor_copied"].append(rel_posix)
                _log(report_lines, f"[build_patcher]   copied: {rel_posix}")

    return result


# ── Public API ────────────────────────────────────────────────────────────────

def patch_legend_build(
    root: Path,
    *,
    execute: bool = False,
    report_lines: Optional[list[str]] = None,
    work_dir: Optional[Path] = None,
) -> dict:
    """
    Apply Legend build package files into the unpacked ROM root.

    Parameters
    ----------
    root         : Path  Root of the unpacked ROM project.
    execute      : bool  True → write changes; False → dry-run only.
    report_lines : list  Optional list to append human-readable report lines to.
    work_dir     : Path  Override extraction work directory (default: output/work/legend_build/).

    Returns
    -------
    dict with keys:
        status, source_used, source_root, copied, replaced, created_dirs,
        created_empty_dirs, vendor_copied, vendor_replaced, vendor_dirs_created,
        unknown_partitions, errors, dry_run
    """
    _wd = Path(work_dir) if work_dir else _WORK_DIR
    legend_build_url = os.environ.get("LEGEND_BUILD_URL", "").strip()

    result: dict = {
        "status": "PENDING",
        "source_used": None,
        "source_root": None,
        "copied": [],
        "replaced": [],
        "created_dirs": [],
        "created_empty_dirs": [],
        "vendor_copied": [],
        "vendor_replaced": [],
        "vendor_dirs_created": [],
        "unknown_partitions": [],
        "errors": [],
        "dry_run": not execute,
    }

    build_root: Optional[Path] = None

    # ── Locate build root ────────────────────────────────────────────────────
    if _LOCAL_BUILD_DIR.is_dir():
        _log(report_lines, f"[build_patcher] Using local build folder: {_LOCAL_BUILD_DIR}")
        result["source_used"] = "local_build_folder"
        build_root = _LOCAL_BUILD_DIR

    elif legend_build_url:
        _log(report_lines,
             "[build_patcher] Local build folder absent — downloading from LEGEND_BUILD_URL")
        try:
            import urllib.request
            _wd.mkdir(parents=True, exist_ok=True)
            zip_name = legend_build_url.rstrip("/").split("/")[-1] or "legend_build.zip"
            if not zip_name.lower().endswith(".zip"):
                zip_name += ".zip"
            zip_dest = _wd / zip_name
            _log(report_lines, f"[build_patcher] Downloading -> {zip_dest}")
            urllib.request.urlretrieve(legend_build_url, zip_dest)
            extract_dest = _wd / "extracted"
            extracted = _extract_zip(zip_dest, extract_dest, report_lines)
            if extracted is None:
                result["status"] = "FAILED"
                result["errors"].append(
                    "zip extraction failed — no recognisable partition structure")
                return result
            result["source_used"] = "downloaded_zip"
            build_root = extracted
        except Exception as exc:
            result["status"] = "FAILED"
            result["errors"].append(f"download failed: {exc}")
            _log(report_lines, f"[build_patcher] ERROR: download failed: {exc}")
            return result

    else:
        _log(report_lines,
             "[build_patcher] SKIPPED_TEMPORARY: "
             "factory/patch/legend/build/ not found and LEGEND_BUILD_URL not set")
        result["status"] = "SKIPPED_TEMPORARY"
        result["source_used"] = "missing_temporary"
        return result

    result["source_root"] = str(build_root)

    # ── Apply files ──────────────────────────────────────────────────────────
    copy_result = _apply_build_root(
        build_root, root, execute=execute, report_lines=report_lines)

    for key in ("copied", "replaced", "created_dirs", "created_empty_dirs",
                "vendor_copied", "vendor_replaced", "vendor_dirs_created",
                "unknown_partitions", "errors"):
        result[key] = copy_result.get(key, [])

    if result["unknown_partitions"]:
        result["status"] = "FAILED"
        return result

    if result["errors"]:
        result["status"] = "FAILED"
        return result

    result["status"] = "APPLIED" if execute else "DRY_RUN"

    _log(report_lines, f"[build_patcher] status          : {result['status']}")
    _log(report_lines, f"[build_patcher] source          : {result['source_used']}")
    _log(report_lines, f"[build_patcher] copied          : {len(result['copied'])}")
    _log(report_lines, f"[build_patcher] replaced        : {len(result['replaced'])}")
    _log(report_lines, f"[build_patcher] created_dirs    : {len(result['created_dirs'])}")
    _log(report_lines, f"[build_patcher] created_empty   : {len(result['created_empty_dirs'])}")
    _log(report_lines, f"[build_patcher] vendor_copied   : {len(result['vendor_copied'])}")
    _log(report_lines, f"[build_patcher] vendor_replaced : {len(result['vendor_replaced'])}")
    _log(report_lines, f"[build_patcher] vendor_dirs     : {len(result['vendor_dirs_created'])}")

    return result
