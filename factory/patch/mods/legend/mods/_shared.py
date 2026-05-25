"""
Shared utilities used by multiple Legend JAR mods.

Contents:
  find_first(root, filename)            — rglob search, first result
  find_all(root, filename)             — rglob, all results
  invoke_custom_patch_file(smali_file, dry_run) -> dict
  invoke_custom_scan_dir(unpack_dir, dry_run) -> list[dict]
  gboard_replace_in_file(file_path, dry_run) -> dict
  gboard_replace_in_dir(root, target_files, dry_run) -> list[dict]
  smali_const(reg, value) -> str       — pick correct smali const opcode

These helpers are implementation details; callers are the per-mod mod.py files.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

_GBOARD_OLD = "com.baidu.input_mi"
_GBOARD_NEW = "com.google.android.inputmethod.latin"

_INVOKE_CUSTOM_SAFE_STUBS: dict[str, list[str]] = {
    "equals":   ["    .registers 2\n", "    const/4 v0, 0x0\n", "    return v0\n"],
    "hashCode": ["    .registers 1\n", "    const/4 v0, 0x0\n", "    return v0\n"],
    "toString": ["    .registers 1\n", "    const/4 v0, 0x0\n", "    return-object v0\n"],
}


# ── File search ───────────────────────────────────────────────────────────────

def find_first(root: Path, filename: str) -> Path | None:
    if not root.is_dir():
        return None
    for p in root.rglob(filename):
        if p.is_file():
            return p
    return None


def find_all(root: Path, filename: str) -> list[Path]:
    if not root.is_dir():
        return []
    return [p for p in root.rglob(filename) if p.is_file()]


# ── Smali const opcode ────────────────────────────────────────────────────────

def smali_const(reg: str, value: int) -> str:
    if -8 <= value <= 7:
        return f"    const/4 {reg}, {hex(value)}"
    if -32768 <= value <= 32767:
        return f"    const/16 {reg}, {hex(value)}"
    return f"    const {reg}, {hex(value)}"


# ── invoke-custom handling ────────────────────────────────────────────────────

def _extract_method_name(method_line: str) -> str | None:
    parts = method_line.strip().split()
    if not parts:
        return None
    last = parts[-1]
    paren = last.find("(")
    return last[:paren] if paren >= 0 else last


def _safe_stub(method_name: str) -> list[str] | None:
    for key, stub in _INVOKE_CUSTOM_SAFE_STUBS.items():
        if key in method_name:
            return stub
    return None


def invoke_custom_patch_file(smali_file: Path, dry_run: bool) -> dict[str, Any]:
    """
    Inspect one smali file for invoke-custom. Apply safe stubs where possible.
    Returns a per-file detail dict.
    """
    detail: dict[str, Any] = {
        "file": smali_file.name,
        "path": str(smali_file),
        "has_invoke_custom": False,
        "methods_patched": [],
        "methods_skipped_unsafe": [],
        "status": "CLEAN",
        "error": None,
    }
    try:
        lines = smali_file.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
    except Exception as exc:
        detail["status"] = "ERROR"
        detail["error"] = str(exc)
        return detail

    if not any("invoke-custom" in line for line in lines):
        return detail

    detail["has_invoke_custom"] = True

    new_lines: list[str] = []
    in_method = False
    method_lines: list[str] = []
    method_name: str | None = None
    has_ic = False
    file_modified = False

    def _flush(end_line: str) -> None:
        nonlocal file_modified
        if not has_ic:
            new_lines.extend(method_lines)
            new_lines.append(end_line)
            return
        stub = _safe_stub(method_name or "")
        if stub is None:
            detail["methods_skipped_unsafe"].append(method_name or "?")
            new_lines.extend(method_lines)
            new_lines.append(end_line)
            return
        detail["methods_patched"].append(method_name or "?")
        if dry_run:
            new_lines.extend(method_lines)
            new_lines.append(end_line)
            return
        new_lines.append(method_lines[0])
        new_lines.extend(stub)
        new_lines.append(end_line)
        file_modified = True

    for line in lines:
        s = line.strip()
        if s.startswith(".method"):
            in_method = True
            method_lines = [line]
            has_ic = False
            method_name = _extract_method_name(s)
        elif in_method and s.startswith(".end method"):
            _flush(line)
            in_method = False
            method_lines = []
            method_name = None
            has_ic = False
        elif in_method:
            if "invoke-custom" in s:
                has_ic = True
            method_lines.append(line)
        else:
            new_lines.append(line)

    if in_method and method_lines:
        new_lines.extend(method_lines)

    if detail["methods_patched"]:
        if dry_run:
            detail["status"] = "WOULD_PATCH"
        elif file_modified:
            try:
                smali_file.write_text("".join(new_lines), encoding="utf-8")
                detail["status"] = "PATCHED"
            except Exception as exc:
                detail["status"] = "ERROR"
                detail["error"] = str(exc)
        else:
            detail["status"] = "SKIPPED_UNSAFE"
    elif detail["methods_skipped_unsafe"]:
        detail["status"] = "SKIPPED_UNSAFE"
    else:
        detail["status"] = "SKIPPED_UNHANDLED"

    return detail


def invoke_custom_scan_dir(unpack_dir: Path, dry_run: bool) -> list[dict[str, Any]]:
    """
    Scan all *.smali files under unpack_dir for invoke-custom; apply safe stubs.
    Returns list of per-file detail dicts (only files that had invoke-custom).
    """
    results: list[dict[str, Any]] = []
    for sf in unpack_dir.rglob("*.smali") if unpack_dir.is_dir() else []:
        d = invoke_custom_patch_file(sf, dry_run)
        if d["has_invoke_custom"]:
            results.append(d)
    return results


# ── Gboard / Baidu replacement ────────────────────────────────────────────────

def gboard_replace_in_file(file_path: Path, dry_run: bool) -> dict[str, Any]:
    detail: dict[str, Any] = {
        "file": file_path.name,
        "path": str(file_path),
        "occurrences": 0,
        "status": "NOT_FOUND",
    }
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
        count = content.count(_GBOARD_OLD)
        detail["occurrences"] = count
        if count == 0:
            return detail
        if dry_run:
            detail["status"] = "WOULD_REPLACE"
            return detail
        file_path.write_text(content.replace(_GBOARD_OLD, _GBOARD_NEW), encoding="utf-8")
        detail["status"] = "REPLACED"
    except Exception as exc:
        detail["status"] = f"ERROR: {exc}"
    return detail


def gboard_replace_in_dir(
    root: Path,
    target_files: list[str],
    dry_run: bool,
) -> list[dict[str, Any]]:
    """Replace Baidu keyboard string in named smali files within root."""
    results: list[dict[str, Any]] = []
    for fname in target_files:
        fp = find_first(root, fname)
        if fp is None:
            results.append({"file": fname, "path": "(not found)", "occurrences": 0, "status": "MISSING"})
            continue
        results.append(gboard_replace_in_file(fp, dry_run))
    return results
