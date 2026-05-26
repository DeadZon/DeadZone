"""
new.dat.br → raw img adapter for DeadZone.

Detects *.new.dat.br + *.transfer.list pairs, reads dynamic_partitions_op_list,
brotli-decompresses .br files, converts to raw img via Sdat2img from
third_party/mezo_core, and returns a structured result compatible with
the UnpackPipeline.

Public API
----------
    from factory.unpack.datbr_adapter import process_datbr_rom, DatBrResult

    result = process_datbr_rom(rom_dir, work_dir, reports_dir)
    if result.status == "FAILED":
        raise RuntimeError(result.error)
    for part_name, img_path in result.images.items():
        use_partition_image(part_name, img_path)
"""
from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

STATUS_OK = "OK"
STATUS_FAILED = "FAILED"
STATUS_PARTIAL = "PARTIAL"

_REPO_ROOT = Path(__file__).resolve().parents[2]
_THIRD_PARTY = _REPO_ROOT / "third_party" / "mezo_core"


# ── Data structures ────────────────────────────────────────────────────────────

@dataclass
class DatBrPair:
    """One *.new.dat.br + *.transfer.list pair for a single partition."""

    partition: str
    br_file: Path
    transfer_list: Optional[Path] = None
    new_dat: Optional[Path] = None   # set after brotli decompression
    img_path: Optional[Path] = None  # set after sdat2img conversion


@dataclass
class DatBrResult:
    """Result returned by process_datbr_rom()."""

    status: str
    rom_dir: Path
    pairs: list[DatBrPair] = field(default_factory=list)
    images: dict[str, Path] = field(default_factory=dict)
    op_list_path: Optional[Path] = None
    op_list_groups: dict[str, int] = field(default_factory=dict)
    op_list_partitions: list[str] = field(default_factory=list)
    # Group max-sizes from op_list keyed by base name — use for super rebuild.
    # Empty when op_list is absent or unparseable.
    original_partition_sizes: dict[str, int] = field(default_factory=dict)
    warnings: list[str] = field(default_factory=list)
    error: Optional[str] = None


# ── Detection helpers ──────────────────────────────────────────────────────────

def _partition_name_from_br(p: Path) -> str:
    """Extract partition name from 'system.new.dat.br' → 'system'."""
    name = p.name.lower()
    if name.endswith(".new.dat.br"):
        return name[: -len(".new.dat.br")]
    return p.stem


def detect_datbr_pairs(rom_dir: Path) -> list[DatBrPair]:
    """Scan rom_dir recursively for *.new.dat.br files and match transfer.list files."""
    pairs: list[DatBrPair] = []
    for br in sorted(rom_dir.rglob("*.new.dat.br")):
        part = _partition_name_from_br(br)
        tl_candidate = br.parent / f"{part}.transfer.list"
        transfer_list: Optional[Path] = tl_candidate if tl_candidate.is_file() else None
        pairs.append(DatBrPair(partition=part, br_file=br, transfer_list=transfer_list))
    return pairs


def find_dynamic_partitions_op_list(rom_dir: Path) -> Optional[Path]:
    """Search rom_dir recursively for a dynamic_partitions_op_list file."""
    for p in rom_dir.rglob("dynamic_partitions_op_list"):
        if p.is_file():
            return p
    return None


def parse_op_list(path: Path) -> tuple[dict[str, int], list[str]]:
    """Parse dynamic_partitions_op_list → (groups: {base_name: max_size}, partitions: [names]).

    Lines of interest:
      add_group      <name>  <max_size>
      add_partition  <name>  <group>

    Group names with _a/_b suffixes are stripped to base names.
    """
    groups: dict[str, int] = {}
    partitions: list[str] = []
    try:
        for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            tokens = line.split()
            cmd = tokens[0]
            if cmd == "add_group" and len(tokens) >= 3:
                try:
                    name = tokens[1]
                    if name.endswith("_a") or name.endswith("_b"):
                        name = name[:-2]
                    val = int(tokens[2])
                    if val > 0:
                        groups[name] = val
                except ValueError:
                    pass
            elif cmd == "add_partition" and len(tokens) >= 3:
                partitions.append(tokens[1])
    except Exception:
        pass
    return groups, partitions


# ── Brotli decompression ───────────────────────────────────────────────────────

def _decompress_brotli(br_file: Path, out_file: Path, diag: list) -> bool:
    """Decompress a .br file to out_file.

    Tries (in order):
      1. brotli Python library  (pip install brotli)
      2. subprocess 'brotli -d' command

    Returns True on success.
    """
    out_file.parent.mkdir(parents=True, exist_ok=True)
    diag.append(f"Decompressing {br_file.name} → {out_file.name}")

    # Strategy 1: brotli Python library
    try:
        import brotli  # type: ignore[import]
        data = brotli.decompress(br_file.read_bytes())
        out_file.write_bytes(data)
        diag.append(f"  brotli (library) OK — {out_file.stat().st_size:,} bytes")
        return True
    except ImportError:
        diag.append("  brotli library not available; trying subprocess …")
    except Exception as exc:
        diag.append(f"  brotli library failed: {exc}; trying subprocess …")
        out_file.unlink(missing_ok=True)

    # Strategy 2: subprocess brotli command
    try:
        result = subprocess.run(
            ["brotli", "--decompress", "--output", str(out_file), str(br_file)],
            capture_output=True,
            timeout=300,
        )
        if result.returncode == 0 and out_file.is_file() and out_file.stat().st_size > 0:
            diag.append(f"  brotli (subprocess) OK — {out_file.stat().st_size:,} bytes")
            return True
        diag.append(
            f"ERROR: brotli subprocess exited {result.returncode}: "
            f"{result.stderr.decode(errors='replace').strip()}"
        )
    except FileNotFoundError:
        diag.append(
            "ERROR: 'brotli' command not found and 'brotli' Python library is not installed. "
            "Install with:  pip install brotli  OR  apt-get install brotli"
        )
    except Exception as exc:
        diag.append(f"ERROR: brotli subprocess failed: {exc}")

    out_file.unlink(missing_ok=True)
    return False


# ── sdat → img conversion ──────────────────────────────────────────────────────

def _sdat2img(
    transfer_list: Path,
    new_dat: Path,
    out_img: Path,
    diag: list,
) -> bool:
    """Convert new.dat + transfer.list → raw ext4 img using third_party Sdat2img.

    Returns True on success.
    """
    tp = str(_THIRD_PARTY)
    if tp not in sys.path:
        sys.path.insert(0, tp)

    try:
        from src.core.utils import Sdat2img  # type: ignore[import]
    except ImportError as exc:
        diag.append(f"ERROR: Cannot import Sdat2img from third_party ({_THIRD_PARTY}): {exc}")
        return False

    out_img.parent.mkdir(parents=True, exist_ok=True)
    try:
        Sdat2img(str(transfer_list), str(new_dat), str(out_img))
    except Exception as exc:
        diag.append(f"ERROR: Sdat2img raised an exception: {exc}")
        out_img.unlink(missing_ok=True)
        return False

    if not out_img.is_file() or out_img.stat().st_size == 0:
        diag.append(f"ERROR: sdat2img produced no output for {new_dat.name}")
        out_img.unlink(missing_ok=True)
        return False

    diag.append(f"  sdat2img OK — {out_img.name}  ({out_img.stat().st_size:,} bytes)")
    return True


# ── Report writer ──────────────────────────────────────────────────────────────

def _write_report(reports_dir: Path, result: DatBrResult, diag: list) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = reports_dir / "datbr_adapter_report.txt"

    lines: list[str] = [
        "═══════════════════════════════════════════════════════",
        "  DeadZone new.dat.br Adapter — Conversion Report",
        "═══════════════════════════════════════════════════════",
        f"  ROM dir     : {result.rom_dir}",
        f"  Pairs found : {len(result.pairs)}",
        "",
        "  Pairs:",
    ]
    for p in result.pairs:
        tl_tag = "present" if p.transfer_list else "MISSING"
        img_tag = p.img_path.name if p.img_path else "—"
        lines.append(
            f"    {p.partition:20s}  br={p.br_file.name}  "
            f"transfer.list={tl_tag}  img={img_tag}"
        )

    if result.op_list_path:
        lines += [
            "",
            f"  dynamic_partitions_op_list : {result.op_list_path}",
        ]
        if result.op_list_groups:
            lines.append("  Groups:")
            for grp, sz in sorted(result.op_list_groups.items()):
                lines.append(f"    {grp:25s}: {sz:,} bytes")
        if result.op_list_partitions:
            lines.append(f"  Partitions in op_list : {result.op_list_partitions}")
    else:
        lines += ["", "  dynamic_partitions_op_list : not found"]

    if result.original_partition_sizes:
        lines += ["", "  Original partition sizes (from op_list):"]
        for k, v in sorted(result.original_partition_sizes.items()):
            lines.append(f"    {k:20s}: {v:,} bytes")

    if result.images:
        lines += ["", "  Converted images:"]
        for part, img in sorted(result.images.items()):
            lines.append(f"    {part:20s}: {img}")

    if result.warnings:
        lines += ["", "  Warnings:"]
        for w in result.warnings:
            lines.append(f"    {w}")

    if result.error:
        lines += ["", f"  Error: {result.error}"]

    lines += ["", "  Diagnostics:"]
    for entry in diag:
        lines.append(f"    {entry}")
    lines += ["", f"  Final status: {result.status}"]
    lines.append("═══════════════════════════════════════════════════════")

    path.write_text("\n".join(lines), encoding="utf-8")
    print(f"[datbr_adapter] Report written: {path}")


# ── Public API ─────────────────────────────────────────────────────────────────

def process_datbr_rom(
    rom_dir: Path,
    work_dir: Path,
    reports_dir: Path,
) -> DatBrResult:
    """
    Process all *.new.dat.br files found in rom_dir.

    Steps
    -----
    1. Detect all *.new.dat.br + *.transfer.list pairs.
    2. Locate and parse dynamic_partitions_op_list (for original partition sizes).
    3. For each pair: brotli-decompress → sdat2img → <partition>.img.
    4. Missing transfer.list emits a warning and skips that partition (continues).
    5. Write datbr_adapter_report.txt.

    Returns
    -------
    DatBrResult
        .status == "OK"      → all pairs converted successfully
        .status == "PARTIAL" → at least one pair converted, at least one failed
        .status == "FAILED"  → no pair could be converted at all
    """
    diag: list[str] = []
    diag.append(f"Scanning {rom_dir} for *.new.dat.br files")

    pairs = detect_datbr_pairs(rom_dir)
    result = DatBrResult(status=STATUS_OK, rom_dir=rom_dir, pairs=pairs)

    if not pairs:
        result.status = STATUS_FAILED
        result.error = f"No *.new.dat.br files found in {rom_dir}"
        diag.append(f"ERROR: {result.error}")
        _write_report(reports_dir, result, diag)
        return result

    diag.append(f"Found {len(pairs)} *.new.dat.br pair(s)")

    # ── Parse dynamic_partitions_op_list ──────────────────────────────────────
    op_list_path = find_dynamic_partitions_op_list(rom_dir)
    if op_list_path:
        diag.append(f"dynamic_partitions_op_list: {op_list_path}")
        groups, part_names = parse_op_list(op_list_path)
        result.op_list_path = op_list_path
        result.op_list_groups = groups
        result.op_list_partitions = part_names
        result.original_partition_sizes = {k: v for k, v in groups.items() if v > 0}
        if result.original_partition_sizes:
            diag.append(f"op_list sizes: {result.original_partition_sizes}")
    else:
        msg = "dynamic_partitions_op_list not found — original partition sizes unavailable"
        diag.append(f"WARNING: {msg}")
        result.warnings.append(msg)

    adapter_dir = work_dir / "datbr_adapter"
    success_count = 0
    fail_count = 0

    for pair in pairs:
        part = pair.partition
        diag.append(f"\nProcessing partition: {part}")

        # ── Check for missing transfer.list ───────────────────────────────────
        if pair.transfer_list is None:
            expected = pair.br_file.parent / f"{part}.transfer.list"
            msg = f"Missing {expected.name} for partition '{part}'"
            diag.append(f"  WARNING: {msg} — skipping this partition")
            result.warnings.append(msg)
            fail_count += 1
            continue

        # ── Brotli decompress ─────────────────────────────────────────────────
        new_dat_path = adapter_dir / f"{part}.new.dat"
        if not _decompress_brotli(pair.br_file, new_dat_path, diag):
            msg = f"Brotli decompression failed for partition '{part}'"
            result.warnings.append(msg)
            fail_count += 1
            continue
        pair.new_dat = new_dat_path

        # ── sdat → img ────────────────────────────────────────────────────────
        img_path = adapter_dir / f"{part}.img"
        if not _sdat2img(pair.transfer_list, new_dat_path, img_path, diag):
            msg = f"sdat2img failed for partition '{part}'"
            result.warnings.append(msg)
            fail_count += 1
            continue

        pair.img_path = img_path
        result.images[part] = img_path
        success_count += 1
        diag.append(f"  {part}: OK → {img_path.name}")

    # ── Final status ──────────────────────────────────────────────────────────
    if success_count == 0:
        result.status = STATUS_FAILED
        result.error = f"All {len(pairs)} partition(s) failed to convert"
    elif fail_count > 0:
        result.status = STATUS_PARTIAL
    else:
        result.status = STATUS_OK

    diag.append(f"\nSummary: {success_count} converted, {fail_count} failed")
    _write_report(reports_dir, result, diag)
    return result
