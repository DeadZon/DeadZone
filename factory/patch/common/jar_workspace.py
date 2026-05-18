"""
JAR workspace — copy, unpack, repack, and restore framework JARs.

Legacy sources extracted from MEZOBuildRom.py:
  resolve_partition_root()          → lines 683-691
  resolve_partition_file()          → lines 694-698
  move_framework_jars_to_cwd()      → lines 5784-5810
  unpack_framework_jars_and_classes() → lines 5813-5884
  repack_all_classes()              → lines 5943-5995
  repack_all_jar_files()            → lines 5998-6031
  restore_repacked_jars_to_project() → lines 5887-5940

All functions here use only stdlib (zipfile, shutil, subprocess, pathlib).
"""
from __future__ import annotations

import shutil
import subprocess
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

from factory.patch.common.smali_tools import (
    compile_smali,
    decompile_dex,
    resolve_baksmali,
    resolve_smali,
    smali_dirs_in,
)

# ── JAR targets ───────────────────────────────────────────────────────────────
# (jar_filename, partition_name, path_within_partition)
JAR_TARGETS: list[tuple[str, str, str]] = [
    ("framework.jar",       "system",     "framework/framework.jar"),
    ("services.jar",        "system",     "framework/services.jar"),
    ("miui-framework.jar",  "system_ext", "framework/miui-framework.jar"),
    ("miui-services.jar",   "system_ext", "framework/miui-services.jar"),
]

# JAR name → unpack directory suffix
_UNPACK_DIR_NAME: dict[str, str] = {
    "framework.jar":      "framework_unpacked",
    "services.jar":       "services_unpacked",
    "miui-framework.jar": "miui_framework_unpacked",
    "miui-services.jar":  "miui_services_unpacked",
}


@dataclass
class JarCopyResult:
    jar_name: str
    source_path: Path | None
    dest_path: Path
    found: bool
    error: str = ""


@dataclass
class JarUnpackResult:
    jar_name: str
    unpack_dir: Path
    dex_count: int
    smali_roots: list[Path] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


@dataclass
class JarRepackResult:
    jar_name: str
    success: bool
    rebuilt_jar: Path | None = None
    error: str = ""


@dataclass
class JarRestoreResult:
    jar_name: str
    success: bool
    backup_path: Path | None = None
    error: str = ""


# ── legacy-extracted from MEZOBuildRom.py:resolve_partition_root (683-691) ───
def _resolve_partition_root(project_dir: Path, partition_name: str) -> Path | None:
    direct = project_dir / partition_name
    nested = direct / partition_name
    if nested.is_dir():
        return nested
    if direct.is_dir():
        return direct
    return None


# ── legacy-extracted from MEZOBuildRom.py:resolve_partition_file (694-698) ───
def resolve_partition_file(project_dir: Path, partition_name: str, *parts: str) -> Path | None:
    root = _resolve_partition_root(project_dir, partition_name)
    if root is None:
        return None
    return root.joinpath(*parts)


# ── legacy-extracted from MEZOBuildRom.py:move_framework_jars_to_cwd (5784-5810)
def copy_jars_to_workspace(project_dir: Path, work_dir: Path) -> list[JarCopyResult]:
    """
    Copy the four target JARs from the unpacked project into *work_dir*.
    A copy (not move) is made to preserve the live partition files.
    Returns one JarCopyResult per JAR regardless of whether it was found.
    """
    results: list[JarCopyResult] = []
    work_dir.mkdir(parents=True, exist_ok=True)

    for jar_name, partition, rel_path in JAR_TARGETS:
        parts = rel_path.split("/")
        src = resolve_partition_file(project_dir, partition, *parts)
        dst = work_dir / jar_name
        if src is None or not src.is_file():
            results.append(JarCopyResult(
                jar_name=jar_name, source_path=src, dest_path=dst, found=False,
                error=f"not found in partition {partition}/{rel_path}",
            ))
            print(f"[jar_workspace] Not found: {jar_name}")
            continue
        try:
            if dst.exists():
                dst.unlink()
            shutil.copy2(src, dst)
            results.append(JarCopyResult(
                jar_name=jar_name, source_path=src, dest_path=dst, found=True,
            ))
            print(f"[jar_workspace] Copied: {jar_name} -> {dst}")
        except Exception as exc:
            results.append(JarCopyResult(
                jar_name=jar_name, source_path=src, dest_path=dst, found=True,
                error=str(exc),
            ))
    return results


# ── legacy-extracted from MEZOBuildRom.py:unpack_framework_jars_and_classes
#    (lines 5813-5884) ─────────────────────────────────────────────────────────
def unpack_jar(jar_path: Path, unpack_dir: Path) -> JarUnpackResult:
    """
    1. Extract the JAR (it is a ZIP) into *unpack_dir*.
    2. Find all .dex files.
    3. Run baksmali on each .dex → smali_classes / smali_classes2 / …

    Naming convention (from legacy):
      classes.dex  → smali_classes/
      classes2.dex → smali_classes2/
      classes3.dex → smali_classes3/
    """
    jar_name = jar_path.name
    result = JarUnpackResult(jar_name=jar_name, unpack_dir=unpack_dir, dex_count=0)

    if unpack_dir.exists():
        shutil.rmtree(unpack_dir, ignore_errors=True)
    unpack_dir.mkdir(parents=True, exist_ok=True)

    # Step 1: extract JAR contents
    try:
        with zipfile.ZipFile(jar_path, "r") as zf:
            zf.extractall(unpack_dir)
        print(f"[jar_workspace] Extracted {jar_name} -> {unpack_dir.name}")
    except Exception as exc:
        result.errors.append(f"JAR extraction failed: {exc}")
        return result

    # Step 2: find dex files
    dex_files = sorted(unpack_dir.rglob("*.dex"))
    result.dex_count = len(dex_files)
    if not dex_files:
        result.errors.append("No .dex files found inside JAR")
        return result
    print(f"[jar_workspace] Found {len(dex_files)} DEX file(s) in {jar_name}")

    # Step 3: baksmali each dex
    baksmali_jar = resolve_baksmali()
    if baksmali_jar is None:
        result.errors.append("baksmali.jar not found; smali decompile skipped")
        return result

    for dex_path in dex_files:
        smali_root_name = f"smali_{dex_path.stem}"   # classes → smali_classes
        smali_out = unpack_dir / smali_root_name
        ok, err = decompile_dex(baksmali_jar, dex_path, smali_out)
        if ok:
            result.smali_roots.append(smali_out)
            print(f"[jar_workspace]   Decompiled {dex_path.name} -> {smali_root_name}/")
        else:
            result.errors.append(f"baksmali failed for {dex_path.name}: {err}")
            print(f"[jar_workspace]   baksmali ERROR {dex_path.name}: {err}")

    return result


# ── legacy-extracted from MEZOBuildRom.py:repack_all_classes (lines 5943-5995)
def repack_smali_to_dex(unpack_dir: Path) -> list[tuple[str, bool, str]]:
    """
    Rebuild every smali_classes* directory in *unpack_dir* back into a .dex.
    Returns list of (smali_dir_name, success, error).

    smali_classes  → classes.dex
    smali_classes2 → classes2.dex
    """
    smali_jar = resolve_smali()
    if smali_jar is None:
        return [("*", False, "smali.jar not found")]

    results: list[tuple[str, bool, str]] = []
    dirs = smali_dirs_in(unpack_dir)
    if not dirs:
        return [("*", False, "no smali_classes* directories found")]

    for smali_dir in dirs:
        dex_name = smali_dir.name.replace("smali_", "") + ".dex"
        output_dex = unpack_dir / dex_name
        print(f"[jar_workspace] Repacking {smali_dir.name} -> {dex_name}")
        ok, err = compile_smali(smali_jar, smali_dir, output_dex)
        if ok:
            shutil.rmtree(smali_dir, ignore_errors=True)
            results.append((smali_dir.name, True, ""))
            print(f"[jar_workspace]   Done: {dex_name}")
        else:
            results.append((smali_dir.name, False, err))
            print(f"[jar_workspace]   FAILED {smali_dir.name}: {err}")

    return results


# ── legacy-extracted from MEZOBuildRom.py:repack_all_jar_files (5998-6031) ──
def repack_dir_to_jar(unpack_dir: Path, output_jar: Path) -> JarRepackResult:
    """
    Repack *unpack_dir* back into a JAR using the system ``jar`` command.
    Equivalent to: jar cfM output.jar -C unpack_dir .
    """
    jar_name = output_jar.name
    cmd = ["jar", "cfM", str(output_jar), "-C", str(unpack_dir), "."]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[jar_workspace] Repacked -> {jar_name}")
            return JarRepackResult(jar_name=jar_name, success=True, rebuilt_jar=output_jar)
        err = (result.stderr or result.stdout or "").strip()
        print(f"[jar_workspace] Repack FAILED {jar_name}: {err}")
        return JarRepackResult(jar_name=jar_name, success=False, error=err)
    except FileNotFoundError:
        return JarRepackResult(jar_name=jar_name, success=False, error="'jar' command not found (JDK not in PATH)")
    except Exception as exc:
        return JarRepackResult(jar_name=jar_name, success=False, error=str(exc))


# ── legacy-extracted from MEZOBuildRom.py:restore_repacked_jars_to_project
#    (lines 5887-5940) — per-jar backup + restore ─────────────────────────────
def backup_and_restore_jar(
    rebuilt_jar: Path,
    project_jar: Path,
    backup_dir: Path,
) -> JarRestoreResult:
    """
    1. Back up the original *project_jar* into *backup_dir*.
    2. Copy *rebuilt_jar* over *project_jar*.

    If step 2 fails, restores from backup automatically.
    """
    jar_name = project_jar.name
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / jar_name

    if not rebuilt_jar.is_file():
        return JarRestoreResult(jar_name=jar_name, success=False, error="rebuilt jar missing")

    if not project_jar.exists():
        return JarRestoreResult(jar_name=jar_name, success=False, error="project jar missing")

    # Step 1: backup
    try:
        shutil.copy2(project_jar, backup_path)
        print(f"[jar_workspace] Backed up: {jar_name} -> {backup_path}")
    except Exception as exc:
        return JarRestoreResult(
            jar_name=jar_name, success=False,
            error=f"backup failed: {exc}",
        )

    # Step 2: restore
    try:
        shutil.copy2(rebuilt_jar, project_jar)
        print(f"[jar_workspace] Restored: {jar_name} -> {project_jar}")
        return JarRestoreResult(jar_name=jar_name, success=True, backup_path=backup_path)
    except Exception as exc:
        # Roll back from backup
        try:
            shutil.copy2(backup_path, project_jar)
            print(f"[jar_workspace] Rolled back {jar_name} from backup after restore failure.")
        except Exception:
            pass
        return JarRestoreResult(
            jar_name=jar_name, success=False, backup_path=backup_path,
            error=f"restore failed (original rolled back): {exc}",
        )


def unpack_dir_for(work_dir: Path, jar_name: str) -> Path:
    """Return the unpack directory path for a given jar_name."""
    return work_dir / _UNPACK_DIR_NAME.get(jar_name, jar_name.replace(".", "_") + "_unpacked")
