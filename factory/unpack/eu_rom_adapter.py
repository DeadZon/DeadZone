"""
EU/split-super ROM adapter for DeadZone.

Detects ROM source layout and normalises split-super inputs into a
single super.img that the standard pipeline can consume.

Supported layouts
-----------------
* payload.bin           → source_type="payload"      (pipeline handles extraction)
* *.new.dat.br          → source_type="new_dat_br"   (pipeline handles extraction)
* super.img             → source_type="super_img"    (registered as normalised source)
* images/super.img      → source_type="super_img"    (preferred path variant)
* super.img.0 / .1 …   → source_type="split_super"  (merged → work/eu_adapter/super.img)
* super.img.zst         → source_type="super_img_zst" (decompressed → work/eu_adapter/super.img)

Public API
----------
    from factory.unpack.eu_rom_adapter import inspect_rom_source, EuRomInfo

    info = inspect_rom_source(rom_path, work_dir, reports_dir)
    if info.status == "FAILED":
        raise RuntimeError(info.error)
    if info.source_type in ("split_super", "super_img", "super_img_zst"):
        use_super_img = info.normalized_path
"""
from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


# ── Source type constants ──────────────────────────────────────────────────────
SOURCE_PAYLOAD = "payload"
SOURCE_NEW_DAT_BR = "new_dat_br"
SOURCE_SUPER_IMG = "super_img"
SOURCE_SPLIT_SUPER = "split_super"
SOURCE_SUPER_IMG_ZST = "super_img_zst"
SOURCE_UNKNOWN = "unknown"

STATUS_OK = "OK"
STATUS_FAILED = "FAILED"


@dataclass
class EuRomInfo:
    """Result returned by inspect_rom_source()."""

    source_type: str
    original_path: Path
    normalized_path: Optional[Path] = None
    found_files: list = field(default_factory=list)
    status: str = STATUS_OK
    error: Optional[str] = None


# ── Natural sort helper ────────────────────────────────────────────────────────
def _natural_key(p: Path) -> list:
    """Sort key that orders super.img.0 < super.img.1 < super.img.10."""
    parts = re.split(r"(\d+)", p.name)
    return [int(x) if x.isdigit() else x.lower() for x in parts]


def _extract_numeric_suffix(p: Path) -> Optional[int]:
    """Return the trailing integer suffix of a filename, or None."""
    m = re.search(r"\.(\d+)$", p.name)
    return int(m.group(1)) if m else None


# ── Layout detection ───────────────────────────────────────────────────────────
def _scan_layout(rom_path: Path) -> dict:
    """
    Walk rom_path (directory) or its parent (file) and catalogue found files.

    Returns a dict:
        payload    : Path | None
        new_dat_br : list[Path]
        super_img  : Path | None   — prefers paths under an "images/" directory
        split_parts: list[Path]    — sorted naturally
        super_zst  : Path | None
    """
    result: dict = {
        "payload": None,
        "new_dat_br": [],
        "super_img": None,
        "split_parts": [],
        "super_zst": None,
    }

    search_root = rom_path if rom_path.is_dir() else rom_path.parent

    for p in search_root.rglob("*"):
        if not p.is_file():
            continue
        name = p.name.lower()

        if name == "payload.bin":
            result["payload"] = p

        elif name.endswith(".new.dat.br"):
            result["new_dat_br"].append(p)

        elif name == "super.img":
            # Prefer the path that lives under an "images/" component.
            current = result["super_img"]
            if current is None:
                result["super_img"] = p
            elif "images" in [part.lower() for part in p.parts]:
                result["super_img"] = p

        elif re.fullmatch(r"super\.img\.\d+", name):
            result["split_parts"].append(p)

        elif name in ("super.img.zst", "super.zst"):
            result["super_zst"] = p

    result["split_parts"].sort(key=_natural_key)
    return result


# ── Split-super merge ──────────────────────────────────────────────────────────
def _merge_split_super(
    parts: list,
    out_super: Path,
    diag: list,
) -> bool:
    """
    Concatenate sorted split-super parts into out_super.

    Verifies that part numbers are contiguous starting from 0 before writing.
    Never overwrites original input files.
    Returns True on success, False on failure.
    """
    nums = [_extract_numeric_suffix(p) for p in parts]

    if None in nums:
        diag.append(
            f"ERROR: Could not parse numeric suffix from one or more "
            f"split-super parts: {[p.name for p in parts]}"
        )
        return False

    expected = list(range(len(parts)))
    if nums != expected:
        missing = sorted(set(expected) - set(nums))
        diag.append(
            f"ERROR: Split-super parts are not contiguous. "
            f"Expected indices {expected}, found {nums}. "
            f"Missing: {missing}"
        )
        return False

    out_super.parent.mkdir(parents=True, exist_ok=True)

    diag.append(f"Merging {len(parts)} split-super parts → {out_super}")
    for p in parts:
        diag.append(f"  part {_extract_numeric_suffix(p)}: {p.name}  ({p.stat().st_size:,} bytes)")

    total_written = 0
    _CHUNK = 8 * 1024 * 1024  # 8 MiB
    try:
        with out_super.open("wb") as dst:
            for p in parts:
                with p.open("rb") as src:
                    while True:
                        buf = src.read(_CHUNK)
                        if not buf:
                            break
                        dst.write(buf)
                        total_written += len(buf)
    except OSError as exc:
        diag.append(f"ERROR: I/O error while writing merged super.img: {exc}")
        out_super.unlink(missing_ok=True)
        return False

    diag.append(f"Merge complete — {out_super.name}  ({total_written:,} bytes total)")
    return True


# ── ZST decompression ──────────────────────────────────────────────────────────
def _decompress_zst(src: Path, dst: Path, diag: list) -> bool:
    """
    Decompress a .zst file to dst using the zstandard library.

    Returns True on success, False on failure (including missing library).
    """
    try:
        import zstandard as zstd  # type: ignore[import]
    except ImportError:
        diag.append(
            "ERROR: The 'zstandard' library is not installed. "
            "Cannot decompress super.img.zst. "
            "Install it with:  pip install zstandard"
        )
        return False

    dst.parent.mkdir(parents=True, exist_ok=True)
    diag.append(f"Decompressing {src.name} → {dst}")
    try:
        dctx = zstd.ZstdDecompressor()
        with src.open("rb") as fin, dst.open("wb") as fout:
            dctx.copy_stream(fin, fout)
    except Exception as exc:  # noqa: BLE001
        diag.append(f"ERROR: ZST decompression failed: {exc}")
        dst.unlink(missing_ok=True)
        return False

    diag.append(f"Decompression complete — {dst.name}  ({dst.stat().st_size:,} bytes)")
    return True


# ── Report writer ──────────────────────────────────────────────────────────────
def _write_report(
    reports_dir: Path,
    info: EuRomInfo,
    diag: list,
) -> None:
    """Write output/reports/eu_rom_adapter_report.txt."""
    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path = reports_dir / "eu_rom_adapter_report.txt"

    lines: list[str] = [
        "═══════════════════════════════════════════════════════",
        "  DeadZone EU ROM Adapter — Source Inspection Report",
        "═══════════════════════════════════════════════════════",
        f"  Detected source type : {info.source_type}",
        f"  Original path        : {info.original_path}",
        f"  Normalized path      : {info.normalized_path or '(none)'}",
        "",
        "  Files found:",
    ]
    if info.found_files:
        for f in info.found_files:
            lines.append(f"    {f}")
    else:
        lines.append("    (none)")
    lines.append("")

    if info.error:
        lines.append(f"  Error: {info.error}")
        lines.append("")

    lines.append("  Diagnostics:")
    for entry in diag:
        lines.append(f"    {entry}")
    lines.append("")
    lines.append(f"  Final status: {info.status}")
    lines.append("═══════════════════════════════════════════════════════")

    report_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[eu_adapter] Report written: {report_path}")


# ── Public API ─────────────────────────────────────────────────────────────────
def inspect_rom_source(
    rom_path: Path,
    work_dir: Path,
    reports_dir: Path,
) -> EuRomInfo:
    """
    Inspect *rom_path* (file or directory) and normalise the ROM source layout.

    Detection priority
    ------------------
    1. split_super   — super.img.0 / super.img.1 / … parts present
    2. super_img_zst — super.img.zst present
    3. super_img     — super.img present (registers it as normalised source)
    4. payload       — payload.bin present (pipeline handles extraction)
    5. new_dat_br    — *.new.dat.br files present (pipeline handles extraction)
    6. unknown       — nothing recognised

    Parameters
    ----------
    rom_path:
        ROM archive or pre-extracted directory to inspect.
    work_dir:
        Session work directory.  Merged/decompressed super.img is written to
        work_dir/eu_adapter/super.img — original input files are never modified.
    reports_dir:
        Directory where eu_rom_adapter_report.txt is written.

    Returns
    -------
    EuRomInfo
        .status == "OK"     → normalised_path is set when applicable
        .status == "FAILED" → .error describes what went wrong
    """
    diag: list[str] = []

    diag.append(f"Scanning ROM source: {rom_path}")
    layout = _scan_layout(rom_path)

    # Collect all found files for the report (in discovery order).
    found: list[Path] = []
    if layout["payload"]:
        found.append(layout["payload"])
    found.extend(layout["new_dat_br"])
    if layout["super_img"]:
        found.append(layout["super_img"])
    found.extend(layout["split_parts"])
    if layout["super_zst"]:
        found.append(layout["super_zst"])

    diag.append(f"  payload.bin      : {layout['payload'] or 'not found'}")
    diag.append(f"  *.new.dat.br     : {len(layout['new_dat_br'])} file(s)")
    diag.append(f"  super.img        : {layout['super_img'] or 'not found'}")
    diag.append(f"  split-super parts: {len(layout['split_parts'])} file(s)")
    diag.append(f"  super.img.zst    : {layout['super_zst'] or 'not found'}")

    adapter_dir = work_dir / "eu_adapter"

    # ── Priority 1: split-super ───────────────────────────────────────────────
    if layout["split_parts"]:
        diag.append(
            f"Detected layout: split_super "
            f"({len(layout['split_parts'])} parts)"
        )
        out_super = adapter_dir / "super.img"

        info = EuRomInfo(
            source_type=SOURCE_SPLIT_SUPER,
            original_path=rom_path,
            found_files=found,
        )

        ok = _merge_split_super(layout["split_parts"], out_super, diag)
        if ok:
            info.normalized_path = out_super
            info.status = STATUS_OK
            diag.append("Split-super merge: OK")
        else:
            info.status = STATUS_FAILED
            info.error = "Split-super merge failed — see diagnostics in the report."

        _write_report(reports_dir, info, diag)
        return info

    # ── Priority 2: super.img.zst ─────────────────────────────────────────────
    if layout["super_zst"]:
        diag.append(f"Detected layout: super_img_zst ({layout['super_zst'].name})")
        out_super = adapter_dir / "super.img"

        info = EuRomInfo(
            source_type=SOURCE_SUPER_IMG_ZST,
            original_path=rom_path,
            found_files=found,
        )

        ok = _decompress_zst(layout["super_zst"], out_super, diag)
        if ok:
            info.normalized_path = out_super
            info.status = STATUS_OK
        else:
            info.status = STATUS_FAILED
            info.error = "ZST decompression failed — see diagnostics in the report."

        _write_report(reports_dir, info, diag)
        return info

    # ── Priority 3: normal super.img ──────────────────────────────────────────
    if layout["super_img"]:
        diag.append(f"Detected layout: super_img ({layout['super_img']})")
        info = EuRomInfo(
            source_type=SOURCE_SUPER_IMG,
            original_path=rom_path,
            normalized_path=layout["super_img"],
            found_files=found,
            status=STATUS_OK,
        )
        _write_report(reports_dir, info, diag)
        return info

    # ── Priority 4: payload.bin ───────────────────────────────────────────────
    if layout["payload"]:
        diag.append("Detected layout: payload  (existing pipeline will handle extraction)")
        info = EuRomInfo(
            source_type=SOURCE_PAYLOAD,
            original_path=rom_path,
            found_files=found,
            status=STATUS_OK,
        )
        _write_report(reports_dir, info, diag)
        return info

    # ── Priority 5: new.dat.br ────────────────────────────────────────────────
    if layout["new_dat_br"]:
        diag.append(
            f"Detected layout: new_dat_br "
            f"({len(layout['new_dat_br'])} file(s) — existing pipeline will handle extraction)"
        )
        info = EuRomInfo(
            source_type=SOURCE_NEW_DAT_BR,
            original_path=rom_path,
            found_files=found,
            status=STATUS_OK,
        )
        _write_report(reports_dir, info, diag)
        return info

    # ── Priority 6: unknown ───────────────────────────────────────────────────
    diag.append("WARNING: No recognised ROM layout detected in this directory.")
    info = EuRomInfo(
        source_type=SOURCE_UNKNOWN,
        original_path=rom_path,
        found_files=found,
        status=STATUS_OK,
    )
    _write_report(reports_dir, info, diag)
    return info
