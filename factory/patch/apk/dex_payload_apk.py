"""
DEX payload merging for MiuiSystemUI APK patch stage.

Decompiles add/classes2.dex, add/classes3.dex, add/classes4.dex using
baksmali.jar and merges the resulting smali directories into new smali_classesN
roots inside the decompiled APK directory.

Safety rules:
  - Never inject dex files directly into the APK.
  - Requires baksmali.jar to decompile dex to smali first.
  - Creates a new smali_classesN root per dex file (avoids mixing with existing roots).
  - If a class file already exists in any existing smali root:
      identical content  -> EXISTS_IDENTICAL (skip)
      different content  -> CONFLICT (skip, do not overwrite)
  - If baksmali.jar is not found: status SKIPPED_MISSING_TOOL, all dex skipped.
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[3]

_BAKSMALI_SEARCH_LOCATIONS: list[Path] = [
    _REPO_ROOT / "third_party" / "mezo_core",
    _REPO_ROOT / "tools",
    _REPO_ROOT,
]

_DEX_NAMES = ("classes2.dex", "classes3.dex", "classes4.dex")


# ---------------------------------------------------------------------------
# Tool resolution
# ---------------------------------------------------------------------------

def find_baksmali() -> Path | None:
    """
    Search for baksmali.jar in known local locations, then system PATH.

    Search order:
      third_party/mezo_core/baksmali.jar
      third_party/mezo_core/baksmali-*.jar
      tools/baksmali.jar
      <repo_root>/baksmali.jar
      PATH (baksmali or baksmali.jar executables)

    Returns Path to the jar/executable, or None if not found.
    """
    for search_dir in _BAKSMALI_SEARCH_LOCATIONS:
        if not search_dir.is_dir():
            continue
        # Exact name first
        exact = search_dir / "baksmali.jar"
        if exact.is_file():
            return exact
        # Glob for versioned names
        matches = sorted(search_dir.glob("baksmali-*.jar"))
        if matches:
            return matches[0]

    # Fall back to system PATH
    exe = shutil.which("baksmali")
    if exe:
        return Path(exe)

    return None


# ---------------------------------------------------------------------------
# Dex decompilation
# ---------------------------------------------------------------------------

def _decompile_dex_to_smali(baksmali_jar: Path, dex_path: Path, out_dir: Path) -> bool:
    """
    Run baksmali to decompile dex_path into smali files in out_dir.

    Command: java -jar baksmali.jar d -o <out_dir> <dex_path>
    Clears out_dir before running.
    Returns True on success.
    """
    if out_dir.exists():
        shutil.rmtree(out_dir, ignore_errors=True)
    out_dir.mkdir(parents=True, exist_ok=True)

    cmd = ["java", "-jar", str(baksmali_jar), "d", "-o", str(out_dir), str(dex_path)]
    print(f"[dex_payload_apk] Decompiling {dex_path.name} -> {out_dir.name} ...")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        smali_count = sum(1 for _ in out_dir.rglob("*.smali"))
        print(f"[dex_payload_apk] Decompile OK: {dex_path.name} ({smali_count} smali files)")
        return True
    except subprocess.CalledProcessError as exc:
        err = (exc.stderr or exc.stdout or "").strip()
        print(
            f"[dex_payload_apk] Decompile FAILED {dex_path.name}: "
            f"{err or ('exit ' + str(exc.returncode))}"
        )
        return False
    except FileNotFoundError:
        print("[dex_payload_apk] ERROR: java not found in PATH")
        return False
    except Exception as exc:
        print(f"[dex_payload_apk] ERROR decompiling {dex_path.name}: {exc}")
        return False


# ---------------------------------------------------------------------------
# Smali root helpers
# ---------------------------------------------------------------------------

def _find_all_smali_roots(decompiled_dir: Path) -> list[Path]:
    """Return all existing smali* subdirectories in the decompiled APK directory."""
    return sorted(
        d for d in decompiled_dir.iterdir()
        if d.is_dir() and d.name.startswith("smali")
    )


def _find_next_smali_root_name(decompiled_dir: Path) -> Path:
    """
    Return the next unused smali_classesN directory path.

    Existing names (smali, smali_classes2, smali_classes3, ...) are skipped.
    """
    existing = {d.name for d in _find_all_smali_roots(decompiled_dir)}
    n = 2
    while True:
        candidate = f"smali_classes{n}"
        if candidate not in existing:
            return decompiled_dir / candidate
        n += 1


def _class_already_exists_in_apk(
    decompiled_dir: Path, relative_smali: Path
) -> tuple[bool, str]:
    """
    Check whether a smali class with the given relative path exists in any
    existing smali root of the decompiled APK.

    relative_smali -- path relative to the smali source root,
                      e.g. Path("com/example/Foo.smali")

    Returns (found: bool, status: str) where status is one of:
      EXISTS_IDENTICAL, EXISTS_DIFFERENT, NOT_FOUND.
    """
    for root in _find_all_smali_roots(decompiled_dir):
        # Direct layout
        candidate = root / relative_smali
        # APKEditor classes/ layout
        alt = root / "classes" / relative_smali
        for target in (candidate, alt):
            if target.is_file():
                return True, target.read_bytes()
    return False, b""


def _merge_smali_dir_into_new_root(
    src_smali_dir: Path,
    target_root: Path,
    decompiled_dir: Path,
) -> dict:
    """
    Copy all .smali files from src_smali_dir into target_root, checking for
    conflicts against all existing smali roots in the decompiled APK.

    Returns a summary dict.
    """
    summary: dict = {
        "target_smali_root": str(target_root),
        "classes_found": 0,
        "classes_added": 0,
        "exists_identical": 0,
        "conflicts": [],
        "errors": [],
    }

    all_existing_roots = _find_all_smali_roots(decompiled_dir)

    for smali_file in sorted(src_smali_dir.rglob("*.smali")):
        relative = smali_file.relative_to(src_smali_dir)
        summary["classes_found"] += 1

        # Check all existing roots for this class
        conflict = False
        identical_found = False
        src_content = None

        for root in all_existing_roots:
            for check_path in (root / relative, root / "classes" / relative):
                if check_path.is_file():
                    if src_content is None:
                        src_content = smali_file.read_bytes()
                    dst_content = check_path.read_bytes()
                    if src_content == dst_content:
                        identical_found = True
                    else:
                        conflict = True
                        summary["conflicts"].append(str(relative))
                    break
            if conflict or identical_found:
                break

        if identical_found:
            summary["exists_identical"] += 1
            continue
        if conflict:
            continue

        # Class not found in any existing root: add it
        dest = target_root / relative
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            if src_content is None:
                src_content = smali_file.read_bytes()
            dest.write_bytes(src_content)
            summary["classes_added"] += 1
        except Exception as exc:
            summary["errors"].append(f"Copy error {relative}: {exc}")

    return summary


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def apply_add_dex(ref_dir: Path, decompiled_dir: Path, work_dir: Path) -> dict:
    """
    Decompile add/classes*.dex with baksmali and merge smali into the decompiled APK.

    For each dex file:
      1. Run baksmali to decompile into a temporary smali directory.
      2. Choose the next unused smali_classesN root in the decompiled APK.
      3. Merge smali files into that root, checking for conflicts.

    Returns a detailed status dict.
    """
    result: dict = {
        "baksmali_jar": None,
        "baksmali_found": False,
        "dex_files": [],
        "status": "NOT_RUN",
        "errors": [],
    }

    baksmali = find_baksmali()
    result["baksmali_jar"] = str(baksmali) if baksmali else None
    result["baksmali_found"] = baksmali is not None

    if baksmali is None:
        result["status"] = "SKIPPED_MISSING_TOOL"
        msg = "baksmali.jar not found; add/classes*.dex payload step skipped"
        result["errors"].append(msg)
        print(f"[dex_payload_apk] WARNING: {msg}")
        return result

    add_dir = ref_dir / "add"
    all_ok = True

    for dex_name in _DEX_NAMES:
        dex_path = add_dir / dex_name
        if not dex_path.is_file():
            result["dex_files"].append({
                "name": dex_name,
                "exists": False,
                "status": "SKIPPED_NOT_FOUND",
            })
            continue

        # Temporary smali output directory in work_dir
        smali_out = work_dir / f"smali_from_{dex_name.replace('.', '_')}"
        decompile_ok = _decompile_dex_to_smali(baksmali, dex_path, smali_out)

        if not decompile_ok:
            result["dex_files"].append({
                "name": dex_name,
                "exists": True,
                "status": "DECOMPILE_FAILED",
                "classes_found": 0,
                "classes_added": 0,
                "exists_identical": 0,
                "conflicts": [],
                "errors": [f"baksmali failed for {dex_name}"],
            })
            all_ok = False
            continue

        target_root = _find_next_smali_root_name(decompiled_dir)
        target_root.mkdir(parents=True, exist_ok=True)

        merge = _merge_smali_dir_into_new_root(smali_out, target_root, decompiled_dir)
        file_status = "PARTIAL" if merge["errors"] else "OK"
        if merge["errors"]:
            all_ok = False

        result["dex_files"].append({
            "name": dex_name,
            "exists": True,
            "smali_temp_dir": str(smali_out),
            "target_smali_root": target_root.name,
            "status": file_status,
            **merge,
        })

    result["status"] = "OK" if all_ok else "PARTIAL"
    return result
