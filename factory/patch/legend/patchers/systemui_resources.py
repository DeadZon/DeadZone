"""
Legend SystemUI resource injector.

Assets live exclusively in:
    factory/patch/legend/assets/systemui/

This module is a thin layer that confirms the assets root is correct
and delegates injection to the SystemUI APK runner (which handles copy +
arsc/layout/values rules internally).  Do not duplicate injection logic here.
"""
from __future__ import annotations

from pathlib import Path
from typing import Optional

_HERE = Path(__file__).resolve()
_LEGEND_HOME = _HERE.parents[1]
ASSETS_ROOT = _LEGEND_HOME / "assets" / "systemui"


def assets_root() -> Path:
    """Return the canonical SystemUI assets path inside the Legend home."""
    return ASSETS_ROOT


def validate_assets_present(report_lines: Optional[list[str]] = None) -> bool:
    """Return True if the systemui assets directory exists and is non-empty."""
    if ASSETS_ROOT.is_dir() and any(ASSETS_ROOT.iterdir()):
        _log(report_lines, f"[systemui_resources] assets found: {ASSETS_ROOT}")
        return True
    _log(report_lines, f"[systemui_resources] WARNING: assets missing or empty: {ASSETS_ROOT}")
    return False


def _log(report_lines: Optional[list[str]], msg: str) -> None:
    print(msg)
    if report_lines is not None:
        report_lines.append(msg)
