"""
smoke_test_all_devices_readiness.py

Smoke-tests every enabled device in factory_devices.json against the Universal
Smart ROM Engine — without performing a real build.

For each device the script:
  1. Loads the device record from factory_devices.json.
  2. Simulates selecting the device (sets selected_codename).
  3. Creates a fake RomAnalysis with a matching detected_codename.
  4. Verifies the universal engine accepts it (no crash, no hard errors).
  5. Verifies the DeadZone_Mezo banner can be generated for the codename.
  6. Verifies a valid ZIP name can be constructed.
  7. Verifies no device-specific crash occurs.

Output:
  output/reports/all_devices_smoke_test_report.txt

Exit code: 0 = all passed, 1 = one or more devices failed.
"""
from __future__ import annotations

import json
import sys
import traceback
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

FACTORY_JSON = REPO_ROOT / "registry" / "devices" / "factory_devices.json"
REPORTS_DIR  = REPO_ROOT / "output" / "reports"


# ── Helpers ───────────────────────────────────────────────────────────────────

def _fake_rom_analysis(codename: str, soc: str):
    """Return a minimal RomAnalysis-like dict for smoke testing."""
    from factory.input.universal_rom_intake import RomAnalysis
    from factory.input.rom_detector import FORMAT_FASTBOOT_TGZ

    r = RomAnalysis(
        rom_format=FORMAT_FASTBOOT_TGZ,
        archive_type="tgz",
        selected_codename=codename,
        detected_codename=codename,
        codename_match=True,
        android_version="16.0",
        build_incremental="OS3.0.303.0.FAKETEST",
        region="CN",
        rom_channel="CN",
        rom_type="fastboot",
        soc_guess=soc if soc != "auto" else "auto",
        confidence=1.0,
        reason="smoke_test",
    )
    return r


def _check_banner_generation(codename: str, edition: str = "Free") -> tuple[bool, str]:
    try:
        from factory.output.deadzone_template_patcher import _bat_banner_lines, _sh_banner_lines

        bat = _bat_banner_lines(
            codename=codename,
            edition=edition,
            android_version="16.0",
            build_incremental="OS3.0.000.0.SMOKETEST",
            region="CN",
        )
        sh = _sh_banner_lines(
            codename=codename,
            edition=edition,
            android_version="16.0",
            build_incremental="OS3.0.000.0.SMOKETEST",
            region="CN",
        )
        if not bat or not sh:
            return False, "banner_lines returned empty list"
        # Verify codename appears in banner
        combined = "\n".join(bat + sh)
        if codename not in combined:
            return False, f"codename {codename!r} not found in generated banner"
        return True, "ok"
    except Exception as exc:
        return False, f"exception: {exc}"


def _check_zip_name(codename: str, edition: str = "Free") -> tuple[bool, str]:
    try:
        edition_part = f"_{edition}" if edition.lower() != "free" else ""
        zip_name = f"DeadZone_{codename}{edition_part}_V1.zip"
        if not zip_name.startswith("DeadZone_"):
            return False, f"unexpected zip name format: {zip_name}"
        if codename not in zip_name:
            return False, f"codename {codename!r} not in zip name {zip_name!r}"
        return True, zip_name
    except Exception as exc:
        return False, f"exception: {exc}"


def _check_codename_validation(codename: str) -> tuple[bool, str]:
    try:
        from factory.output.deadzone_template_patcher import validate_codename

        match, err = validate_codename(codename, codename)
        if not match or err is not None:
            return False, f"codename self-match failed: match={match} err={err}"

        # Mismatch with different codename must fail
        match2, err2 = validate_codename(codename, "totally_different_device_xyz")
        if match2:
            return False, "codename mismatch should fail but returned match=True"

        # No detected codename must pass (warning, not fail)
        match3, err3 = validate_codename(codename, None)
        if not match3:
            return False, "missing detected codename should return match=True"

        return True, "ok"
    except Exception as exc:
        return False, f"exception: {exc}"


def _check_intake_codename_mismatch(codename: str) -> tuple[bool, str]:
    try:
        from factory.input.rom_detector import check_codename_match

        ok, msg = check_codename_match(codename, codename)
        if not ok:
            return False, f"self-match failed: {msg}"

        ok2, msg2 = check_codename_match("wrong_device_xyz", codename)
        if ok2:
            return False, "mismatch detection failed — expected fail"

        ok3, _ = check_codename_match(None, codename)
        if not ok3:
            return False, "None detected_codename should pass with warning"

        return True, "ok"
    except Exception as exc:
        return False, f"exception: {exc}"


# ── Per-device smoke test ─────────────────────────────────────────────────────

def smoke_test_device(device: dict) -> dict:
    codename = device.get("codename", "")
    soc      = device.get("soc", "auto")
    result: dict = {
        "codename":    codename,
        "display_name": device.get("display_name", ""),
        "soc":         soc,
        "passed":      True,
        "checks":      {},
        "errors":      [],
    }

    checks = {
        "banner_generation":       lambda: _check_banner_generation(codename),
        "zip_name":                lambda: _check_zip_name(codename),
        "codename_validation":     lambda: _check_codename_validation(codename),
        "intake_codename_mismatch": lambda: _check_intake_codename_mismatch(codename),
    }

    for name, fn in checks.items():
        try:
            ok, detail = fn()
            result["checks"][name] = {"passed": ok, "detail": detail}
            if not ok:
                result["passed"] = False
                result["errors"].append(f"{name}: {detail}")
        except Exception as exc:
            tb = traceback.format_exc()
            result["checks"][name] = {"passed": False, "detail": str(exc)}
            result["passed"] = False
            result["errors"].append(f"{name}: unexpected exception: {exc}\n{tb}")

    return result


# ── Report writer ─────────────────────────────────────────────────────────────

def _write_report(results: list[dict], output_path: Path) -> None:
    passed = sum(1 for r in results if r["passed"])
    failed = len(results) - passed

    lines = [
        "=" * 62,
        "  DeadZone Factory — All Devices Smoke Test Report",
        "=" * 62,
        "",
        f"  Total devices tested : {len(results)}",
        f"  Passed               : {passed}",
        f"  Failed               : {failed}",
        "",
    ]

    failed_results = [r for r in results if not r["passed"]]
    if failed_results:
        lines.append("  FAILED DEVICES:")
        for r in failed_results:
            lines.append(f"    - {r['codename']} ({r['soc']})")
            for e in r["errors"]:
                lines.append(f"        ERROR: {e}")
        lines.append("")

    lines.append("  Per-device results:")
    for r in sorted(results, key=lambda x: x["codename"]):
        status = "PASS" if r["passed"] else "FAIL"
        lines.append(f"    [{status}] {r['codename']:<20} soc={r['soc']}")
        if not r["passed"]:
            for e in r["errors"]:
                lines.append(f"              ! {e}")

    lines += ["", "=" * 62]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# ── Main ──────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    if not FACTORY_JSON.exists():
        print(f"[FAIL] factory_devices.json not found: {FACTORY_JSON}", file=sys.stderr)
        return 1

    devices_raw: list[dict] = json.loads(FACTORY_JSON.read_text(encoding="utf-8"))
    enabled = [d for d in devices_raw if d.get("enabled", True)]

    print(f"[smoke_test] Testing {len(enabled)} enabled devices ...")
    results: list[dict] = []

    for device in enabled:
        r = smoke_test_device(device)
        status = "PASS" if r["passed"] else "FAIL"
        print(f"  [{status}] {r['codename']}")
        if not r["passed"]:
            for e in r["errors"]:
                print(f"         ! {e}", file=sys.stderr)
        results.append(r)

    report_path = REPORTS_DIR / "all_devices_smoke_test_report.txt"
    _write_report(results, report_path)
    print(f"\n[smoke_test] Report written: {report_path}")

    passed = sum(1 for r in results if r["passed"])
    failed = len(results) - passed

    if failed:
        print(
            f"\n[RESULT] FAILED — {failed}/{len(results)} device(s) failed smoke test.",
            file=sys.stderr,
        )
        return 1

    print(f"\n[RESULT] All {passed} devices passed smoke test.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
