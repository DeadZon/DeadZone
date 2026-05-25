"""Generic mod build package patcher.

Applies a mod's build/ folder partition-relative into an unpacked ROM tree.
Shared by all mods — no mod-specific logic here.

Allowed top-level partitions:
    system, product, system_ext, vendor, odm, mi_ext

Status values:
    SKIPPED_TEMPORARY   build/ absent and env URL not set
    DRY_RUN             dry-run mode, no writes
    APPLIED             files copied successfully (execute=True)
    FAILED              unknown partition, zip error, or copy error
"""
from __future__ import annotations

import os
import shutil
import zipfile
from pathlib import Path
from typing import Optional

ALLOWED_PARTITIONS: frozenset[str] = frozenset({
    "system", "product", "system_ext", "vendor", "odm", "mi_ext",
})

_REPO_ROOT = Path(__file__).resolve().parents[4]


def _log(lines: Optional[list[str]], msg: str) -> None:
    print(msg)
    if lines is not None:
        lines.append(msg)


# ── Zip safety ────────────────────────────────────────────────────────────────

def _safe_zip_member(name: str) -> bool:
    parts = name.replace("\\", "/").split("/")
    if ".." in parts:
        return False
    if name.startswith("/"):
        return False
    if len(name) >= 2 and name[1] == ":" and name[0].isalpha():
        return False
    return True


def _detect_zip_root(members: list[str]) -> Optional[str]:
    hits: dict[str, int] = {}
    for m in members:
        parts = [p for p in m.replace("\\", "/").split("/") if p]
        if not parts:
            continue
        if parts[0] in ALLOWED_PARTITIONS:
            hits[""] = hits.get("", 0) + 1
        elif len(parts) >= 2 and parts[1] in ALLOWED_PARTITIONS:
            hits[parts[0]] = hits.get(parts[0], 0) + 1
    return max(hits, key=lambda k: hits[k]) if hits else None


def _extract_zip(zip_path: Path, dest: Path, lines: Optional[list[str]]) -> Optional[Path]:
    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            members = zf.namelist()
            prefix = _detect_zip_root(members)
            if prefix is None:
                _log(lines, "[build_patcher] ERROR: zip has no recognisable partition structure")
                return None
            dest.mkdir(parents=True, exist_ok=True)
            for m in members:
                if not _safe_zip_member(m):
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
            _log(lines, f"[build_patcher] extracted to {dest} (prefix={prefix!r})")
            return dest
    except Exception as exc:
        _log(lines, f"[build_patcher] ERROR extracting zip: {exc}")
        return None


# ── Copy logic ────────────────────────────────────────────────────────────────

def _apply_build_root(
    build_root: Path,
    rom_root: Path,
    execute: bool,
    lines: Optional[list[str]],
) -> dict:
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
            _log(lines, f"[build_patcher] UNKNOWN partition: {d.name}")

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
                _log(lines, f"[build_patcher] ERROR copying {rel_posix}: {exc}")
                continue

            if already_exists:
                result["replaced"].append(rel_posix)
                if is_vendor:
                    result["vendor_replaced"].append(rel_posix)
                _log(lines, f"[build_patcher]   replaced: {rel_posix}")
            else:
                result["copied"].append(rel_posix)
                if is_vendor:
                    result["vendor_copied"].append(rel_posix)
                _log(lines, f"[build_patcher]   copied: {rel_posix}")

    return result


# ── Public API ────────────────────────────────────────────────────────────────

def apply_mod_build_package(
    rom_root: Path,
    mod_id: str,
    build_dir: Optional[Path] = None,
    build_url_env: Optional[str] = None,
    work_dir: Optional[Path] = None,
    execute: bool = False,
    report_lines: Optional[list[str]] = None,
) -> dict:
    """Apply a mod's build package into the unpacked ROM root.

    Parameters
    ----------
    rom_root      ROM project root directory.
    mod_id        Mod identifier string (for logging and work dir naming).
    build_dir     Path to the mod's build/ folder. Takes priority over URL.
    build_url_env Name of the env var holding an optional download URL.
    work_dir      Override extraction work dir (default: output/work/<mod_id>_build/).
    execute       True → write changes; False → dry-run only.
    report_lines  Optional list to append human-readable log lines to.
    """
    _wd = Path(work_dir) if work_dir else _REPO_ROOT / "output" / "work" / f"{mod_id}_build"
    build_url = os.environ.get(build_url_env or "", "").strip() if build_url_env else ""

    result: dict = {
        "status": "PENDING",
        "mod": mod_id,
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

    if build_dir and build_dir.is_dir():
        _log(report_lines, f"[build_patcher:{mod_id}] Using local build folder: {build_dir}")
        result["source_used"] = "local_build_folder"
        build_root = build_dir

    elif build_url:
        _log(report_lines, f"[build_patcher:{mod_id}] Downloading from env URL")
        try:
            import urllib.request
            _wd.mkdir(parents=True, exist_ok=True)
            zip_name = build_url.rstrip("/").split("/")[-1] or f"{mod_id}_build.zip"
            if not zip_name.lower().endswith(".zip"):
                zip_name += ".zip"
            zip_dest = _wd / zip_name
            _log(report_lines, f"[build_patcher:{mod_id}] Downloading -> {zip_dest}")
            urllib.request.urlretrieve(build_url, zip_dest)
            extracted = _extract_zip(zip_dest, _wd / "extracted", report_lines)
            if extracted is None:
                result["status"] = "FAILED"
                result["errors"].append("zip extraction failed — no recognisable partition structure")
                return result
            result["source_used"] = "downloaded_zip"
            build_root = extracted
        except Exception as exc:
            result["status"] = "FAILED"
            result["errors"].append(f"download failed: {exc}")
            _log(report_lines, f"[build_patcher:{mod_id}] ERROR: download failed: {exc}")
            return result

    else:
        _log(report_lines,
             f"[build_patcher:{mod_id}] SKIPPED_TEMPORARY: build/ missing and env URL not set")
        result["status"] = "SKIPPED_TEMPORARY"
        result["source_used"] = "missing_temporary"
        return result

    result["source_root"] = str(build_root)

    copy_result = _apply_build_root(build_root, rom_root, execute=execute, lines=report_lines)

    for key in ("copied", "replaced", "created_dirs", "created_empty_dirs",
                "vendor_copied", "vendor_replaced", "vendor_dirs_created",
                "unknown_partitions", "errors"):
        result[key] = copy_result.get(key, [])

    if result["unknown_partitions"]:
        result["status"] = "FAILED"
        result["errors"].append(
            f"Unknown top-level partition(s) in {mod_id} build package: "
            f"{result['unknown_partitions']}. Allowed: {sorted(ALLOWED_PARTITIONS)}"
        )
        return result

    if result["errors"]:
        result["status"] = "FAILED"
        return result

    result["status"] = "APPLIED" if execute else "DRY_RUN"
    _log(report_lines, f"[build_patcher:{mod_id}] status: {result['status']}")
    _log(report_lines, f"[build_patcher:{mod_id}] copied={len(result['copied'])} replaced={len(result['replaced'])}")
    return result
