"""Universal unpacker for DeadZone Factory.

Accepts a RomAnalysis result and unpacks the ROM using the correct strategy.

Output directories (under work_dir):
  unpacked_rom/    — full archive extraction
  source_images/   — discovered standalone .img files
  super_workspace/ — lpmake scratch area (kept empty here)
  super_parts/     — dynamic partition images (populated later)

Delegates actual unpacking to factory.input.rom_unpacker.unpack_rom, which
owns all format-specific logic.  This wrapper adds:
  - RomAnalysis integration (no need to re-detect format)
  - Consistent DRY_RUN path
  - payload_dump_report.txt location awareness
"""
from __future__ import annotations

from pathlib import Path

from factory.input.rom_detector import FORMAT_UNKNOWN
from factory.input.rom_unpacker import unpack_rom
from factory.input.universal_rom_intake import RomAnalysis


def unpack_with_analysis(
    analysis: RomAnalysis,
    work_dir: Path,
    execute: bool = False,
) -> dict:
    """Unpack ROM described by *analysis* into *work_dir*.

    Parameters
    ----------
    analysis:
        RomAnalysis from analyze_rom() — carries format + local_path.
    work_dir:
        Root workspace directory (output/work).
    execute:
        False → dry-run (no files written).

    Returns
    -------
    dict  matching the rom_unpacker.unpack_rom result schema, with extras:
        status, errors, warnings, rom_format, …
    """
    work_dir = Path(work_dir)

    if not execute:
        return {
            "status": "DRY_RUN",
            "rom_format": analysis.rom_format,
            "work_dir": str(work_dir),
            "errors": [],
            "warnings": [],
        }

    if analysis.rom_format == FORMAT_UNKNOWN:
        return {
            "status": "UNSUPPORTED",
            "rom_format": FORMAT_UNKNOWN,
            "work_dir": str(work_dir),
            "errors": [f"Cannot unpack unknown ROM format: {analysis.reason}"],
            "warnings": [],
        }

    if analysis.local_path is None or not Path(analysis.local_path).is_file():
        return {
            "status": "FAILED",
            "rom_format": analysis.rom_format,
            "work_dir": str(work_dir),
            "errors": [f"ROM file not found: {analysis.local_path}"],
            "warnings": [],
        }

    return unpack_rom(
        rom_path=analysis.local_path,
        rom_format=analysis.rom_format,
        work_dir=work_dir,
    )
