"""
APKEditor.jar resolution and execution helpers.

Resolves APKEditor.jar from:
  third_party/mezo_core/APKEditor.jar

Exposes:
  resolve_apkeditor_jar(root_dir=None) -> Path | None
  run_apkeditor(args, cwd=None) -> int
"""
from __future__ import annotations

import subprocess
from pathlib import Path

_REPO_ROOT   = Path(__file__).resolve().parents[3]
_LEGACY_ROOT = _REPO_ROOT / "third_party" / "mezo_core"

APK_EDITOR_JAR_NAME        = "APKEditor.jar"
APK_EDITOR_FRAMEWORK_VERSION = 35


def resolve_apkeditor_jar(root_dir: Path | None = None) -> Path | None:
    """Return the path to APKEditor.jar if it exists, else None."""
    search = root_dir if root_dir is not None else _LEGACY_ROOT
    jar = search / APK_EDITOR_JAR_NAME
    if jar.is_file():
        return jar
    return None


def run_apkeditor(args: list[str], cwd: Path | None = None) -> int:
    """
    Run APKEditor.jar with the given argument list.

    Resolves APKEditor.jar automatically.
    Returns the process exit code (0 = success).
    Returns 1 if APKEditor.jar is not found.
    Returns 127 if java is not in PATH.
    """
    jar = resolve_apkeditor_jar()
    if jar is None:
        print(f"[apkeditor_tools] ERROR: {APK_EDITOR_JAR_NAME} not found at {_LEGACY_ROOT}")
        return 1

    cmd = ["java", "-jar", str(jar)] + args
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(cwd) if cwd is not None else None,
        )
        if result.returncode != 0:
            err = (result.stderr or result.stdout or "").strip()
            if err:
                print(f"[apkeditor_tools] ERROR (exit {result.returncode}): {err}")
            else:
                print(f"[apkeditor_tools] ERROR: exit code {result.returncode}")
        return result.returncode
    except FileNotFoundError:
        print("[apkeditor_tools] ERROR: java not found in PATH")
        return 127
    except Exception as exc:
        print(f"[apkeditor_tools] ERROR: {exc}")
        return 1
