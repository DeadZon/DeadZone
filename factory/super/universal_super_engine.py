"""Universal super engine for DeadZone Factory.

Selects the correct super.img handling strategy from the ROM state and
edition flags, then executes it by delegating to super_rebuilder.

Strategy rules
--------------
Free edition (apply_mods=False):
  preserve_original_super  — original standalone super.img exists
  preserve_merged_super    — split chunks were merged into one super.img
  preserve_payload_super   — payload OTA supplied super.img via dump
  rebuild_with_lpmake      — no original super but dynamic partitions available
  no_super_available       — no super and no dynamic partitions (non-fatal)

Modified editions (apply_mods=True):
  rebuild_modified_super   — always rebuild; mods change partition content

Reports written:
  output/reports/super_metadata_report.txt
  output/reports/super_rebuild_report.txt   (written by super_rebuilder)
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import Optional


# ── Strategy constants ────────────────────────────────────────────────────────

STRATEGY_PRESERVE_ORIGINAL  = "preserve_original_super"
STRATEGY_PRESERVE_MERGED    = "preserve_merged_super"
STRATEGY_PRESERVE_PAYLOAD   = "preserve_payload_super"
STRATEGY_REBUILD_LPMAKE     = "rebuild_with_lpmake"
STRATEGY_REBUILD_MODIFIED   = "rebuild_modified_super"
STRATEGY_NO_SUPER           = "no_super_available"

_PRESERVE_STRATEGIES = frozenset({
    STRATEGY_PRESERVE_ORIGINAL,
    STRATEGY_PRESERVE_MERGED,
    STRATEGY_PRESERVE_PAYLOAD,
})


# ── Public API ─────────────────────────────────────────────────────────────────

def select_super_strategy(
    original_super_img: Optional[Path],
    split_super_merged: bool,
    has_dynamic_partitions: bool,
    apply_mods: bool,
    is_payload_ota: bool = False,
) -> str:
    """Return the strategy constant that matches the current ROM state.

    Parameters
    ----------
    original_super_img:
        Path to a standalone super.img found in the source ROM (None if absent).
    split_super_merged:
        True when split super chunks were merged into a single file.
    has_dynamic_partitions:
        True when at least one dynamic partition image is present (system …).
    apply_mods:
        True for Legend/Gaming/EPIC; False for Free.
    is_payload_ota:
        True when the ROM was a payload OTA that produced super.img via dump.
    """
    if apply_mods:
        return STRATEGY_REBUILD_MODIFIED

    if original_super_img is not None:
        if split_super_merged:
            return STRATEGY_PRESERVE_MERGED
        if is_payload_ota:
            return STRATEGY_PRESERVE_PAYLOAD
        return STRATEGY_PRESERVE_ORIGINAL

    if has_dynamic_partitions:
        return STRATEGY_REBUILD_LPMAKE

    return STRATEGY_NO_SUPER


def execute_super_strategy(
    strategy: str,
    original_super_img: Optional[Path],
    super_parts_dir: Path,
    output_super: Path,
    reports_dir: Path,
    original_partition_sizes: Optional[dict] = None,
    execute: bool = False,
) -> dict:
    """Execute the selected super strategy.

    Delegates to factory.super.super_rebuilder.rebuild_super with the
    correct flags for the chosen strategy, then writes the metadata report.

    Parameters
    ----------
    strategy:
        One of the STRATEGY_* constants.
    original_super_img:
        Path to original super.img (required for preserve strategies).
    super_parts_dir:
        Directory containing base-named partition .img files for lpmake.
    output_super:
        Destination path for the final super.img.
    reports_dir:
        Where to write super_metadata_report.txt.
    original_partition_sizes:
        {base_name: lp_allocation_bytes} from original super metadata.
        Required for lpmake rebuild; derived automatically if original super
        is present.
    execute:
        False → dry-run.
    """
    from factory.super.super_rebuilder import rebuild_super

    if strategy == STRATEGY_NO_SUPER:
        result: dict = {
            "status": "SKIPPED",
            "strategy": strategy,
            "warnings": ["No super.img available — final ZIP may lack super.img"],
            "errors": [],
            "lpmake_executed": False,
            "super_img_created": False,
        }
        _write_super_metadata_report(
            reports_dir=reports_dir,
            strategy=strategy,
            original_super_img=original_super_img,
            output_super=output_super,
            rebuild_result=result,
        )
        return result

    preserve = strategy in _PRESERVE_STRATEGIES

    result = rebuild_super(
        super_parts_dir=super_parts_dir,
        output_super=output_super,
        reports_dir=reports_dir,
        original_super_img=original_super_img,
        original_partition_sizes=original_partition_sizes,
        execute=execute,
        preserve_original_super=preserve,
    )
    result["strategy"] = strategy

    _write_super_metadata_report(
        reports_dir=reports_dir,
        strategy=strategy,
        original_super_img=original_super_img,
        output_super=output_super,
        rebuild_result=result,
    )
    return result


# ── Report writer ─────────────────────────────────────────────────────────────

def _write_super_metadata_report(
    reports_dir: Path,
    strategy: str,
    original_super_img: Optional[Path],
    output_super: Path,
    rebuild_result: dict,
) -> None:
    """Write output/reports/super_metadata_report.txt."""
    reports_dir = Path(reports_dir)
    reports_dir.mkdir(parents=True, exist_ok=True)
    out_path = reports_dir / "super_metadata_report.txt"
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    sr = rebuild_result
    # VAB: valid when _b slots all have zero size
    is_vab = bool(
        sr.get("vab_b_slots_valid")
        or sr.get("vab_b_slots_are_zero_size")
    )
    partitions: list[str] = sr.get("partitions_in_final") or []
    a_parts = sorted(p for p in partitions if p.endswith("_a"))
    b_parts = sorted(p for p in partitions if p.endswith("_b"))

    orig_size: Optional[int] = None
    if original_super_img and Path(original_super_img).is_file():
        try:
            orig_size = Path(original_super_img).stat().st_size
        except OSError:
            orig_size = None

    lines = [
        "=" * 60,
        "  DeadZone Factory — Super Metadata Report",
        "=" * 60,
        f"  Generated           : {ts}",
        f"  Strategy            : {strategy}",
        f"  Original super path : {original_super_img or '(none)'}",
        f"  Original super size : {orig_size if orig_size is not None else '(unknown)'}",
        f"  Final super path    : {output_super}",
        f"  Final super size    : {sr.get('super_img_size') or '(unknown)'}",
        f"  Metadata source     : {sr.get('super_metadata_source') or '(unknown)'}",
        f"  VAB layout          : {is_vab}",
        f"  lpmake executed     : {sr.get('lpmake_executed', False)}",
        f"  lpmake return code  : {sr.get('lpmake_return_code')}",
        f"  Validation status   : {sr.get('validation_status', 'NOT_RUN')}",
        "",
        f"  _a partitions ({len(a_parts)}):",
    ]
    for p in a_parts:
        lines.append(f"    {p}")
    if not a_parts:
        lines.append("    (none — preserve strategy or no VAB layout)")

    lines += ["", f"  _b placeholder partitions ({len(b_parts)}):"]
    for p in b_parts:
        lines.append(f"    {p}")
    if not b_parts:
        lines.append("    (none — preserve strategy or no VAB layout)")

    lpmake_cmd = sr.get("lpmake_command") or []
    lines += ["", "  lpmake command:"]
    lines.append("    " + " ".join(str(t) for t in lpmake_cmd) if lpmake_cmd else "    (not used)")

    if sr.get("errors"):
        lines += ["", f"  Errors ({len(sr['errors'])}):"]
        for e in sr["errors"]:
            lines.append(f"    ! {e}")
    if sr.get("warnings"):
        lines += ["", f"  Warnings ({len(sr['warnings'])}):"]
        for w in sr["warnings"]:
            lines.append(f"    - {w}")
    lines.append("=" * 60)

    try:
        out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    except Exception as exc:
        print(
            f"[universal_super_engine] Warning: could not write "
            f"super_metadata_report.txt: {exc}"
        )
