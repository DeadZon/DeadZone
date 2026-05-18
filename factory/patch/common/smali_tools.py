"""
smali / baksmali tool resolution and subprocess wrappers.

Legacy source: MEZOBuildRom.py
  resolve_tool_jar()       → lines 5621-5625
  prepare_smali_tools()    → lines 5628-5651
  repack_all_classes()     → lines 5943-5995  (decompile direction)
  unpack_framework_jars_and_classes() → lines 5813-5884 (smali dir naming)

The logic here is copied/extracted inline — these functions only use
subprocess and stdlib, so no legacy module import is needed.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

# Path to mezo_core where baksmali.jar and smali.jar live.
_MEZO_CORE = Path(__file__).resolve().parents[3] / "third_party" / "mezo_core"

# API level passed to smali assembler.  Keep in sync with legacy (was 33).
_SMALI_API_LEVEL = "33"


def resolve_baksmali() -> Path | None:
    """Return path to baksmali.jar if present in mezo_core."""
    p = _MEZO_CORE / "baksmali.jar"
    return p if p.is_file() else None


def resolve_smali() -> Path | None:
    """Return path to smali.jar if present in mezo_core."""
    p = _MEZO_CORE / "smali.jar"
    return p if p.is_file() else None


# ── legacy-extracted from MEZOBuildRom.py:unpack_framework_jars_and_classes
#    (lines 5858-5884) — baksmali invocation ──────────────────────────────────
def decompile_dex(
    baksmali_jar: Path,
    dex_path: Path,
    output_dir: Path,
) -> tuple[bool, str]:
    """
    Run baksmali on *dex_path*, writing smali source into *output_dir*.
    Returns (success, error_message).
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "java", "-jar", str(baksmali_jar),
        "d", str(dex_path),
        "-o", str(output_dir),
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return True, ""
        err = (result.stderr or result.stdout or "").strip()
        return False, err
    except FileNotFoundError:
        return False, "java not found in PATH"
    except Exception as exc:
        return False, str(exc)


# ── legacy-extracted from MEZOBuildRom.py:repack_all_classes (lines 5969-5993)
def compile_smali(
    smali_jar: Path,
    smali_dir: Path,
    output_dex: Path,
) -> tuple[bool, str]:
    """
    Run smali on *smali_dir*, writing the assembled .dex to *output_dex*.
    Returns (success, error_message).
    """
    cmd = [
        "java", "-jar", str(smali_jar),
        "a", str(smali_dir),
        "-o", str(output_dex),
        "--api", _SMALI_API_LEVEL,
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            return True, ""
        err = (result.stderr or result.stdout or "").strip()
        return False, err
    except FileNotFoundError:
        return False, "java not found in PATH"
    except Exception as exc:
        return False, str(exc)


def smali_dirs_in(unpack_dir: Path) -> list[Path]:
    """
    Return all smali_classes* directories inside *unpack_dir*, sorted.
    Naming convention matches legacy: smali_classes, smali_classes2, …
    """
    dirs: list[Path] = []
    try:
        for item in sorted(unpack_dir.iterdir()):
            if item.is_dir() and item.name.startswith("smali_classes"):
                dirs.append(item)
    except Exception:
        pass
    return dirs
