"""
payload.bin extraction — thin wrapper around the legacy implementation.

The real logic lives in MEZOBuildRom.py:try_extract_super_from_payload
(lines 286-414).  That function depends on:
  src.core.payload_extract.extract_partitions_from_payload
  src.core.utils.JsonEdit
  extract_single_partition() (also in MEZOBuildRom.py)

Rather than duplicating those ~130 lines and their deep src.core dependencies
we import the function from the legacy module at call time.

Side-effect note: importing MEZOBuildRom changes the CWD to
  third_party/mezo_core/
because of the module-level ``os.chdir(ROOT_DIR)`` call.  The pipeline saves
and restores CWD around the import so that callers with relative paths are
not affected.  All paths in BuildContext are absolute, so this is safe.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# Absolute path to mezo_core so we can sys.path-inject without relying on CWD.
_MEZO_CORE_DIR = Path(__file__).resolve().parents[2] / "third_party" / "mezo_core"


def _legacy():
    """
    Lazy-import MEZOBuildRom, saving/restoring CWD around the first import.
    Returns the module object (cached by sys.modules on subsequent calls).
    """
    if "MEZOBuildRom" in sys.modules:
        return sys.modules["MEZOBuildRom"]

    saved_cwd = os.getcwd()
    try:
        if str(_MEZO_CORE_DIR) not in sys.path:
            sys.path.insert(0, str(_MEZO_CORE_DIR))
        import MEZOBuildRom as _m  # noqa: PLC0415
        return _m
    finally:
        # Restore CWD that MEZOBuildRom changed at module level.
        os.chdir(saved_cwd)


def find_payload_bin(search_roots: list[Path]) -> list[Path]:
    """
    Return all payload.bin files found under the given search roots (unique, sorted).

    Used by the pipeline to report whether payload.bin was present even when
    extraction is delegated to the legacy function.
    """
    seen: set[str] = set()
    found: list[Path] = []
    for root in search_roots:
        if not root.exists():
            continue
        try:
            for p in root.rglob("payload.bin"):
                if p.is_file() and str(p) not in seen:
                    seen.add(str(p))
                    found.append(p)
        except Exception:
            pass
    return found


def extract_from_payload(
    extracted_dir: Path,
    project_dir: Path,
    search_roots: list[Path],
) -> bool:
    """
    Delegate to MEZOBuildRom.try_extract_super_from_payload (lines 286-414).

    Returns True when at least one partition image was produced (or super.img
    was created from payload).  Returns False when payload.bin is absent or
    extraction fails entirely.

    This call may extract partition directories into project_dir and write
    config/parts_info — the same behaviour as the legacy main() function.
    No APK/JAR/smali patching is triggered.
    """
    m = _legacy()
    return m.try_extract_super_from_payload(
        extracted_dir=extracted_dir,
        project_dir=project_dir,
        search_roots=search_roots,
    )
