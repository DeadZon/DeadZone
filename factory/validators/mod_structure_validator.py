"""Mod structure validator.

Verifies that every mod under factory/patch/mods/ is self-contained and
that no forbidden old paths exist in the repository.

Usage:
    python -m factory.validators.mod_structure_validator
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
_MODS_DIR = _REPO_ROOT / "factory" / "patch" / "mods"

_FORBIDDEN_PATHS = [
    "factory/patch/legend",
    "factory/patch/editions",
    "factory/assets/legend",
    "factory/patches",
]

_FORBIDDEN_CONTENT_PATTERNS = [
    "factory.patch.legend.",
    "factory/patch/legend/",
    "factory.patch.editions.",
    "factory/patch/editions/",
]

_CORE_FORBIDDEN_IN_MOD = [
    "unpack",
    "super_build",
    "final_zip",
    "flash_script",
    "pixeldrain",
    "telegram",
]

_ALLOWED_PARTITIONS = frozenset({
    "system", "product", "system_ext", "vendor", "odm", "mi_ext",
})

_REQUIRED_MOD_ITEMS = [
    "manifest.yml",
    "runner.py",
    "profiles",
    "patchers",
    "assets",
    "reports",
    "validators",
]


def _check_forbidden_paths(errors: list[str]) -> None:
    for rel in _FORBIDDEN_PATHS:
        p = _REPO_ROOT / rel.replace("/", "\\")
        if p.exists():
            errors.append(f"FORBIDDEN path still exists: {rel}")


def _check_no_stray_imports(errors: list[str]) -> None:
    """Ensure no .py file outside the old locations still imports old paths."""
    for py in _REPO_ROOT.rglob("*.py"):
        rel = py.relative_to(_REPO_ROOT).as_posix()
        # Skip archived / pycache / old paths (they'll be deleted)
        if any(s in rel for s in ["archived_legacy", "__pycache__", ".git"]):
            continue
        try:
            text = py.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for pattern in _FORBIDDEN_CONTENT_PATTERNS:
            if pattern in text:
                errors.append(f"stray import {pattern!r} in: {rel}")
                break


def _check_mod_structure(mod_dir: Path, errors: list[str], warnings: list[str]) -> None:
    mod_id = mod_dir.name
    if mod_id.startswith("_"):
        return  # skip _common

    for item in _REQUIRED_MOD_ITEMS:
        if not (mod_dir / item).exists():
            errors.append(f"mod {mod_id}: missing {item}")

    # Validate runner.py exposes run_mod
    runner = mod_dir / "runner.py"
    if runner.is_file():
        text = runner.read_text(encoding="utf-8", errors="replace")
        if "def run_mod" not in text:
            errors.append(f"mod {mod_id}: runner.py missing def run_mod()")

    # Validate manifest.yml has required keys
    manifest = mod_dir / "manifest.yml"
    if manifest.is_file():
        text = manifest.read_text(encoding="utf-8", errors="replace")
        for key in ("id:", "display_name:", "enabled:", "stages:"):
            if key not in text:
                warnings.append(f"mod {mod_id}: manifest.yml missing key {key!r}")

    # Validate build/ uses only allowed top-level partitions
    build_dir = mod_dir / "build"
    if build_dir.is_dir():
        for entry in build_dir.iterdir():
            if entry.is_dir() and entry.name not in _ALLOWED_PARTITIONS:
                errors.append(
                    f"mod {mod_id}: build/ contains unknown partition: {entry.name} "
                    f"(allowed: {sorted(_ALLOWED_PARTITIONS)})"
                )

    # Validate no core pipeline logic in mod
    for py in mod_dir.rglob("*.py"):
        if "__pycache__" in py.parts:
            continue
        try:
            text = py.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for forbidden in _CORE_FORBIDDEN_IN_MOD:
            # Check for direct function definitions (not imports of core modules)
            if f"def {forbidden}" in text or f"def apply_{forbidden}" in text:
                warnings.append(
                    f"mod {mod_id}: {py.relative_to(mod_dir)} may contain core logic: {forbidden}"
                )


def validate(quiet: bool = False) -> dict:
    errors: list[str] = []
    warnings: list[str] = []

    if not _MODS_DIR.is_dir():
        errors.append(f"mods directory missing: {_MODS_DIR}")
        return {"passed": False, "errors": errors, "warnings": warnings}

    # Check each mod
    mods_found = []
    for mod_dir in sorted(_MODS_DIR.iterdir()):
        if not mod_dir.is_dir() or mod_dir.name.startswith("_"):
            continue
        mods_found.append(mod_dir.name)
        _check_mod_structure(mod_dir, errors, warnings)

    if not mods_found:
        warnings.append("No mods found under factory/patch/mods/")

    # Check forbidden old paths exist
    _check_forbidden_paths(errors)

    if not quiet:
        print(f"[mod_validator] Mods found: {mods_found}")
        for e in errors:
            print(f"[mod_validator] ERROR: {e}")
        for w in warnings:
            print(f"[mod_validator] WARN:  {w}")
        passed = not bool(errors)
        print(f"[mod_validator] Result: {'PASSED' if passed else 'FAILED'}")

    return {
        "passed": not bool(errors),
        "mods_found": mods_found,
        "errors": errors,
        "warnings": warnings,
    }


if __name__ == "__main__":
    result = validate()
    sys.exit(0 if result["passed"] else 1)
