"""
APK workspace helpers: find, copy, decompile, rebuild, and no-backup restore.

All functions use only stdlib (shutil, subprocess, pathlib).
No patch logic lives here.
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

from factory.patch.apk.apkeditor_tools import APK_EDITOR_FRAMEWORK_VERSION

# Partition / sub-directory search order for find_apk.
_APK_SEARCH_LOCATIONS: list[tuple[str, str]] = [
    ("system",     "priv-app"),
    ("system",     "app"),
    ("system_ext", "priv-app"),
    ("system_ext", "app"),
    ("product",    "priv-app"),
    ("product",    "app"),
    ("mi_ext",     "priv-app"),
    ("mi_ext",     "app"),
    ("odm",        "priv-app"),
    ("odm",        "app"),
]


# Equivalent to MEZOBuildRom.py:resolve_partition_root (lines 683-691).
def _resolve_partition_root(project_dir: Path, partition: str) -> Path | None:
    direct = project_dir / partition
    nested = direct / partition
    if nested.is_dir():
        return nested
    if direct.is_dir():
        return direct
    return None


def find_apk(project_dir: Path, apk_name: str) -> Path | None:
    """
    Search standard partition locations for apk_name.

    Search order:
      system/priv-app, system/app,
      system_ext/priv-app, system_ext/app,
      product/priv-app, product/app,
      mi_ext/priv-app, mi_ext/app,
      odm/priv-app, odm/app

    Returns the first match found, or None.
    """
    for partition, subdir in _APK_SEARCH_LOCATIONS:
        root = _resolve_partition_root(project_dir, partition)
        if root is None:
            continue
        loc = root / subdir
        if not loc.is_dir():
            continue
        for candidate in sorted(loc.rglob(apk_name)):
            if candidate.is_file():
                return candidate
    return None


def prepare_apk_work_dir(work_dir: Path, apk_name: str) -> Path:
    """Ensure work_dir exists and return the expected APK path inside it."""
    work_dir.mkdir(parents=True, exist_ok=True)
    return work_dir / apk_name


def copy_apk_to_work(apk_path: Path, work_dir: Path) -> Path:
    """
    Copy apk_path into work_dir.

    Removes any existing copy before copying.
    Returns the path of the copied file.
    """
    work_dir.mkdir(parents=True, exist_ok=True)
    dest = work_dir / apk_path.name
    if dest.exists():
        try:
            dest.unlink()
        except Exception:
            pass
    shutil.copy2(apk_path, dest)
    print(f"[apk_workspace] Copied {apk_path.name} -> {dest}")
    return dest


def decompile_apk(apkeditor_jar: Path, apk_path: Path, out_dir: Path) -> bool:
    """
    Decompile apk_path into out_dir using APKEditor.

    Command: java -jar APKEditor.jar d -framework-version 35 -i <apk> -o <out_dir>

    Clears out_dir before running.
    Returns True on success.
    """
    if out_dir.exists():
        shutil.rmtree(out_dir, ignore_errors=True)

    cmd = [
        "java", "-jar", str(apkeditor_jar),
        "d",
        "-framework-version", str(APK_EDITOR_FRAMEWORK_VERSION),
        "-i", str(apk_path),
        "-o", str(out_dir),
    ]
    print(f"[apk_workspace] Decompiling {apk_path.name} -> {out_dir.name} ...")
    try:
        subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            cwd=str(apk_path.parent),
        )
        if out_dir.is_dir():
            print(f"[apk_workspace] Decompile complete: {apk_path.name}")
            return True
        print(f"[apk_workspace] Warning: decompile ran but {out_dir.name} was not created")
        return False
    except subprocess.CalledProcessError as exc:
        err = (exc.stderr or exc.stdout or "").strip()
        if err:
            print(f"[apk_workspace] Decompile ERROR {apk_path.name}: {err}")
        else:
            print(f"[apk_workspace] Decompile ERROR {apk_path.name}: exit code {exc.returncode}")
        return False
    except FileNotFoundError:
        print("[apk_workspace] ERROR: java not found in PATH")
        return False
    except Exception as exc:
        print(f"[apk_workspace] Decompile ERROR {apk_path.name}: {exc}")
        return False


def rebuild_apk(apkeditor_jar: Path, decompiled_dir: Path) -> bool:
    """
    Rebuild decompiled_dir back into an APK using APKEditor.

    Command: java -jar APKEditor.jar b -framework-version 35 -i <decompiled_dir> -o <apk>

    Output APK name is derived from decompiled_dir.name by stripping the
    '_apk_src' suffix and appending '.apk':
      Provision_apk_src  ->  Provision.apk
      MiuiSystemUI_apk_src  ->  MiuiSystemUI.apk

    Output APK is placed in decompiled_dir.parent.
    Returns True on success.
    """
    raw = decompiled_dir.name
    apk_base = raw[: -len("_apk_src")] if raw.endswith("_apk_src") else raw
    output_apk = decompiled_dir.parent / (apk_base + ".apk")

    if output_apk.exists():
        try:
            output_apk.unlink()
        except Exception:
            pass

    cmd = [
        "java", "-jar", str(apkeditor_jar),
        "b",
        "-framework-version", str(APK_EDITOR_FRAMEWORK_VERSION),
        "-i", str(decompiled_dir),
        "-o", str(output_apk),
    ]
    print(f"[apk_workspace] Rebuilding {apk_base}.apk from {decompiled_dir.name} ...")
    try:
        subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True,
            cwd=str(decompiled_dir.parent),
        )
        if output_apk.is_file():
            print(f"[apk_workspace] Rebuild OK -> {output_apk.name}")
            return True
        print(f"[apk_workspace] Rebuild FAILED: output file not created")
        return False
    except subprocess.CalledProcessError as exc:
        err = (exc.stderr or exc.stdout or "").strip()
        if err:
            print(f"[apk_workspace] Rebuild ERROR {apk_base}.apk: {err}")
        else:
            print(f"[apk_workspace] Rebuild ERROR {apk_base}.apk: exit code {exc.returncode}")
        return False
    except FileNotFoundError:
        print("[apk_workspace] ERROR: java not found in PATH")
        return False
    except Exception as exc:
        print(f"[apk_workspace] Rebuild ERROR {apk_base}.apk: {exc}")
        return False


def rebuild_apk_with_diagnostics(apkeditor_jar: Path, decompiled_dir: Path) -> dict:
    """
    Like rebuild_apk but captures and returns full diagnostics.

    Returns a dict with keys:
      command, returncode, stdout, stderr, success, output_apk
    Never raises — all errors are captured into the returned dict.
    """
    raw = decompiled_dir.name
    apk_base = raw[: -len("_apk_src")] if raw.endswith("_apk_src") else raw
    output_apk = decompiled_dir.parent / (apk_base + ".apk")

    if output_apk.exists():
        try:
            output_apk.unlink()
        except Exception:
            pass

    cmd = [
        "java", "-jar", str(apkeditor_jar),
        "b",
        "-framework-version", str(APK_EDITOR_FRAMEWORK_VERSION),
        "-i", str(decompiled_dir),
        "-o", str(output_apk),
    ]

    result: dict = {
        "command": " ".join(cmd),
        "returncode": None,
        "stdout": "",
        "stderr": "",
        "success": False,
        "output_apk": str(output_apk),
    }

    print(f"[apk_workspace] Rebuilding {apk_base}.apk from {decompiled_dir.name} ...")
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(decompiled_dir.parent),
        )
        result["returncode"] = proc.returncode
        result["stdout"] = proc.stdout or ""
        result["stderr"] = proc.stderr or ""
        if proc.returncode == 0 and output_apk.is_file():
            result["success"] = True
            print(f"[apk_workspace] Rebuild OK -> {output_apk.name}")
        else:
            err = (proc.stderr or proc.stdout or "").strip()
            tail = err[-600:] if len(err) > 600 else err
            if tail:
                print(f"[apk_workspace] Rebuild ERROR {apk_base}.apk: {tail}")
            else:
                print(f"[apk_workspace] Rebuild ERROR {apk_base}.apk: exit code {proc.returncode}")
    except FileNotFoundError:
        result["returncode"] = -1
        result["stderr"] = "java not found in PATH"
        print("[apk_workspace] ERROR: java not found in PATH")
    except Exception as exc:
        result["returncode"] = -1
        result["stderr"] = str(exc)
        print(f"[apk_workspace] Rebuild ERROR {apk_base}.apk: {exc}")

    return result


def restore_rebuilt_apk_no_backup(rebuilt_apk: Path, target_apk: Path) -> dict:
    """
    Replace target_apk with rebuilt_apk. No backup is created.

    Rules:
    - rebuilt_apk must exist
    - rebuilt_apk size must be > 0
    - target_apk parent directory must exist
    - Replace via temp file + atomic rename
    - If replacement fails, target_apk is NOT touched

    Returns:
      {"success": bool, "error": str, "backup_policy": "disabled"}
    """
    result: dict = {"success": False, "error": "", "backup_policy": "disabled"}

    if not rebuilt_apk.is_file():
        result["error"] = f"rebuilt APK not found: {rebuilt_apk}"
        print(f"[apk_workspace] Replace FAILED: {result['error']}")
        return result

    if rebuilt_apk.stat().st_size == 0:
        result["error"] = "rebuilt APK is zero bytes"
        print(f"[apk_workspace] Replace FAILED: {result['error']}")
        return result

    if not target_apk.parent.is_dir():
        result["error"] = f"target parent directory does not exist: {target_apk.parent}"
        print(f"[apk_workspace] Replace FAILED: {result['error']}")
        return result

    tmp = target_apk.with_suffix(".tmp_replace")
    try:
        shutil.copy2(rebuilt_apk, tmp)
        tmp.replace(target_apk)
        print(f"[apk_workspace] Replaced (no backup): {rebuilt_apk.name} -> {target_apk}")
        result["success"] = True
        return result
    except Exception as exc:
        try:
            tmp.unlink(missing_ok=True)
        except Exception:
            pass
        result["error"] = str(exc)
        print(f"[apk_workspace] Replace FAILED: {exc}")
        return result
