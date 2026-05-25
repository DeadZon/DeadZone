"""Validate a DeadZone build report JSON for consistency and correctness.

Fails (exit 1) when any of these invariants are violated:
  1. payload_found=true  AND  partitions_extracted=[]
  2. Any stage final_status=APPLIED but errors list is not empty
  3. apk_mods sub-report contains import errors
  4. erofs_repack partitions_found=[] in execute mode after a successful unpack
  5. super_build ran lpmake without original partition sizes

Usage:
    python scripts/validate_build_report.py <pipeline_report.json>
    python scripts/validate_build_report.py <01_unpack_report.json> [<13_erofs_report.json> ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def _load(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"[validate_report] ERROR reading {path}: {exc}", file=sys.stderr)
        sys.exit(1)


errors: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)
    print(f"  [FAIL] {msg}")


def warn(msg: str) -> None:
    warnings.append(msg)
    print(f"  [WARN] {msg}")


def ok(msg: str) -> None:
    print(f"  [ OK ] {msg}")


# ── Check 1: payload_found=true but partitions_extracted=[] ──────────────────

def check_unpack_report(report: dict, label: str = "unpack") -> None:
    print(f"\n=== {label}: payload extraction consistency ===")
    payload_found = report.get("payload_found", False)
    partitions = report.get("partitions_extracted") or []
    super_found = report.get("super_found", False)

    if payload_found and not super_found and not partitions:
        fail(
            f"{label}: payload_found=true but partitions_extracted=[] — "
            "payload extraction produced nothing; pipeline must not have continued."
        )
    elif payload_found and partitions:
        ok(f"{label}: payload_found=true, partitions_extracted={partitions}")
    elif not payload_found:
        ok(f"{label}: payload_found=false (super path or no ROM)")
    else:
        ok(f"{label}: super_found=true — super path used")


# ── Check 2: APPLIED status with non-empty errors ────────────────────────────

def check_no_applied_with_errors(report: dict, stage_label: str) -> None:
    status = str(
        report.get("final_status") or report.get("status") or ""
    ).upper()
    errs = report.get("errors") or []
    if isinstance(errs, str):
        errs = [errs]

    if status == "APPLIED" and errs:
        fail(
            f"{stage_label}: final_status=APPLIED but errors list is non-empty: "
            f"{errs[:3]}"
        )
    else:
        ok(f"{stage_label}: status={status or '(none)'}, errors={len(errs)}")


# ── Check 3: apk_mods import errors ─────────────────────────────────────────

def check_apk_mods(apk_mods: dict, label: str = "apk_mods") -> None:
    print(f"\n=== {label}: import error check ===")
    errs = apk_mods.get("errors") or []
    import_errors = [e for e in errs if "No module named" in str(e) or "ImportError" in str(e)]
    if import_errors:
        for ie in import_errors:
            fail(f"{label}: import error — {ie}")
    else:
        ok(f"{label}: no import errors")


# ── Check 4: erofs partitions_found=[] in execute mode after successful unpack ─

def check_erofs_report(erofs: dict, unpack_ok: bool, label: str = "erofs_repack") -> None:
    print(f"\n=== {label}: partition detection ===")
    execute = erofs.get("execute", True)
    partitions_found = erofs.get("partitions_found") or []
    partitions_requested = erofs.get("partitions_requested") or []

    if execute and unpack_ok and not partitions_found:
        fail(
            f"{label}: execute mode, unpack succeeded, but partitions_found=[] — "
            "EROFS repack has nothing to pack."
        )
    elif not execute:
        ok(f"{label}: dry-run, skipping partition check")
    else:
        ok(f"{label}: partitions_found={partitions_found}")

    if execute and partitions_requested and not partitions_found:
        fail(
            f"{label}: partitions_requested={partitions_requested} but none found on disk"
        )


# ── Check 5: super_build reached lpmake without original partition sizes ──────

def check_super_report(super_report: dict, label: str = "super_build") -> None:
    print(f"\n=== {label}: lpmake preflight ===")
    lpmake_executed = super_report.get("lpmake_executed", False)
    errs = super_report.get("errors") or []

    missing_meta = any(
        "original super metadata missing" in str(e)
        or "original_partition_sizes is empty" in str(e)
        for e in errs
    )
    if lpmake_executed and missing_meta:
        fail(
            f"{label}: lpmake_executed=true but original metadata/partition-sizes are "
            "missing — super build must have been refused."
        )
    elif lpmake_executed:
        ok(f"{label}: lpmake ran with metadata present")
    else:
        ok(f"{label}: lpmake not executed (expected when metadata is missing or dry-run)")

    if missing_meta:
        ok(f"{label}: correct — super refused lpmake due to missing metadata")


# ── Main dispatcher ───────────────────────────────────────────────────────────

def _validate_pipeline_report(report: dict) -> None:
    """Validate a full pipeline_report JSON (from legacy_build_orchestrator)."""

    # 1. Unpack
    stage_reports = report.get("stage_reports") or {}
    unpack_rep = stage_reports.get("unpack") or {}
    check_unpack_report(unpack_rep, "pipeline/unpack")

    unpack_status = str(unpack_rep.get("status") or unpack_rep.get("final_status") or "").upper()
    unpack_ok = unpack_status not in {"FAILED", "PARTIAL_FAILED", ""}

    # 2. Stage APPLIED-with-errors check
    print("\n=== Stage status consistency ===")
    for stage in report.get("stages") or []:
        sid = stage.get("id", "?")
        check_no_applied_with_errors(stage, f"stage/{sid}")

    for sid, srep in stage_reports.items():
        if isinstance(srep, dict):
            check_no_applied_with_errors(srep, f"stage_reports/{sid}")

    # 3. APK mods import errors
    legend_rep = stage_reports.get("legend_jar") or stage_reports.get("legend_runner") or {}
    apk_mods = legend_rep.get("steps", {}).get("apk_mods") or {}
    if apk_mods:
        check_apk_mods(apk_mods, "legend/apk_mods")
    else:
        print("\n=== apk_mods: not present in report (OK if legend skipped) ===")

    # 4. EROFS
    erofs_rep = stage_reports.get("erofs_repack") or {}
    if erofs_rep:
        check_erofs_report(erofs_rep, unpack_ok, "stage_reports/erofs_repack")

    # 5. Super
    super_rep = stage_reports.get("super_build") or {}
    if super_rep:
        check_super_report(super_rep, "stage_reports/super_build")


def _validate_standalone_report(path: Path, report: dict) -> None:
    """Validate a standalone stage report by name."""
    name = path.name.lower()

    if "unpack" in name:
        check_unpack_report(report, path.name)
    elif "erofs" in name:
        check_erofs_report(report, unpack_ok=True, label=path.name)
    elif "super" in name:
        check_super_report(report, path.name)
    elif "patch" in name or "legend" in name or "deadzone" in name:
        check_no_applied_with_errors(report, path.name)
        apk_mods = report.get("steps", {}).get("apk_mods") or {}
        if apk_mods:
            check_apk_mods(apk_mods, f"{path.name}/apk_mods")
    else:
        check_no_applied_with_errors(report, path.name)


def main(argv: list[str] | None = None) -> int:
    paths = [Path(a) for a in (argv if argv is not None else sys.argv[1:])]
    if not paths:
        print("Usage: validate_build_report.py <report.json> [<report2.json> ...]", file=sys.stderr)
        return 2

    for path in paths:
        if not path.exists():
            print(f"[validate_report] ERROR: not found: {path}", file=sys.stderr)
            errors.append(f"file not found: {path}")
            continue

        report = _load(path)
        stage_key = report.get("stage") or ""
        if stage_key == "legacy_build_pipeline" or "stages" in report:
            print(f"\n{'=' * 60}")
            print(f"Validating full pipeline report: {path}")
            _validate_pipeline_report(report)
        else:
            print(f"\n{'=' * 60}")
            print(f"Validating standalone report: {path}")
            _validate_standalone_report(path, report)

    print(f"\n{'=' * 60}")
    print(f"=== Summary ===")
    print(f"  Errors  : {len(errors)}")
    print(f"  Warnings: {len(warnings)}")

    if errors:
        print("\nFAILED — build report has consistency violations.\n")
        return 1

    print("\nAll checks passed.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
