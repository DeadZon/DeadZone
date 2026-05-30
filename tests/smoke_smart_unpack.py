"""
DeadZone Phase 6 – Smart Unpack Smoke Test
==========================================

Validates deadzone_smart_unpack against four synthetic input types:
  1. Recovery OTA ZIP with payload.bin
  2. Fastboot TGZ with images/ directory
  3. Raw super.img (with Android LP magic)
  4. Folder with existing partition .img files

Usage:
    python tests/smoke_smart_unpack.py

    # Verbose output
    python tests/smoke_smart_unpack.py --verbose

    # Run against a real ROM input file or folder
    python tests/smoke_smart_unpack.py --rom-path /path/to/rom.zip

    # Keep the temporary workspace for inspection
    python tests/smoke_smart_unpack.py --keep-workspace

Exit code: 0 if all enabled scenarios pass, 1 otherwise.

Notes:
  - Synthetic inputs are minimal and do not exercise payload-dumper-go.
    For full payload extraction validation, supply a real OTA ZIP via
    --rom-path and ensure payload-dumper-go is on PATH.
  - If mkfs.erofs is not available on Windows, stable_partition_rebuild
    tests in the full suite will fail.  That is unrelated to smart_unpack
    and is documented as a pre-existing platform limitation.
"""
from __future__ import annotations

import argparse
import json
import shutil
import struct
import sys
import tarfile
import tempfile
import time
import traceback
import zipfile
from io import BytesIO
from pathlib import Path
from typing import Any

# Ensure the repo root is on sys.path when run directly
_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from factory.core.smart_unpack import (
    ROUTE_FASTBOOT,
    ROUTE_IMAGE_FOLDER,
    ROUTE_PAYLOAD,
    ROUTE_SUPER,
    deadzone_smart_unpack,
)
from factory.core.workspace import create_workspace


# ── Minimal payload.bin bytes (CrAU header) ───────────────────────────────────

def _minimal_payload_bytes() -> bytes:
    """Construct a minimal payload.bin that satisfies the header check."""
    manifest = b"\x00" * 4
    sig_len = 4
    header = struct.pack(">4sQQI", b"CrAU", 2, len(manifest), sig_len)
    return header + manifest + b"\x00" * sig_len


# ── Android LP magic (super.img detection) ────────────────────────────────────

def _minimal_super_img_bytes() -> bytes:
    """Return bytes that look like a super.img by LP magic at offset 4096."""
    buf = bytearray(4096 + 8)
    # Android LP metadata magic: little-endian 0x534C4F57 at offset 4096
    struct.pack_into("<I", buf, 4096, 0x534C4F57)
    return bytes(buf)


# ── Fixture builders ──────────────────────────────────────────────────────────

def _make_ota_zip_with_payload(dest: Path) -> Path:
    """ZIP containing payload.bin and payload_properties.txt."""
    zip_path = dest / "ota_rom.zip"
    payload_bytes = _minimal_payload_bytes()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_STORED) as zf:
        zf.writestr("payload.bin", payload_bytes)
        zf.writestr("payload_properties.txt", "FILE_HASH=deadbeef\nFILE_SIZE=1\n")
    return zip_path


def _make_fastboot_tgz(dest: Path) -> Path:
    """TGZ containing images/system.img, images/product.img, images/vendor.img."""
    tgz_path = dest / "fastboot_images.tgz"
    buf = BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tf:
        for part in ("system", "product", "vendor"):
            data = b"\x00" * 512
            info = tarfile.TarInfo(name=f"images/{part}.img")
            info.size = len(data)
            tf.addfile(info, BytesIO(data))
    tgz_path.write_bytes(buf.getvalue())
    return tgz_path


def _make_raw_super_img(dest: Path) -> Path:
    """A raw super.img file with Android LP magic at offset 4096."""
    img_path = dest / "super.img"
    img_path.write_bytes(_minimal_super_img_bytes())
    return img_path


def _make_image_folder(dest: Path) -> Path:
    """Folder containing system.img, product.img, vendor.img."""
    folder = dest / "partition_images"
    folder.mkdir(parents=True, exist_ok=True)
    for part in ("system", "product", "vendor"):
        (folder / f"{part}.img").write_bytes(b"\x00" * 512)
    return folder


# ── Result validation ─────────────────────────────────────────────────────────

_REQUIRED_RESULT_KEYS = {
    "input_path", "input_type", "route", "route_reason",
    "status", "images", "missing_required", "missing_optional",
    "reports", "error", "elapsed_seconds",
}


def _validate_result(result: dict[str, Any], expected_route: str, label: str) -> list[str]:
    """Return a list of failure messages (empty = pass)."""
    failures: list[str] = []

    missing_keys = _REQUIRED_RESULT_KEYS - result.keys()
    if missing_keys:
        failures.append(f"[{label}] Missing result keys: {sorted(missing_keys)}")

    if result.get("route") != expected_route:
        failures.append(
            f"[{label}] Expected route={expected_route!r}, got {result.get('route')!r}"
        )

    if result.get("status") not in ("OK", "FAILED", "UNSUPPORTED"):
        failures.append(f"[{label}] Unknown status: {result.get('status')!r}")

    return failures


def _validate_outputs(ws_root: Path, label: str) -> list[str]:
    """Check that smart_unpack.json and the txt report exist."""
    failures: list[str] = []
    json_path = ws_root / "meta" / "smart_unpack.json"
    report_path = ws_root / "reports" / "deadzone_smart_unpack_report.txt"

    if not json_path.is_file():
        failures.append(f"[{label}] smart_unpack.json not found at {json_path}")
    else:
        try:
            data = json.loads(json_path.read_text())
            missing = _REQUIRED_RESULT_KEYS - data.keys()
            if missing:
                failures.append(f"[{label}] smart_unpack.json missing keys: {sorted(missing)}")
        except Exception as exc:
            failures.append(f"[{label}] smart_unpack.json parse error: {exc}")

    if not report_path.is_file():
        failures.append(f"[{label}] deadzone_smart_unpack_report.txt not found")
    else:
        content = report_path.read_text()
        for section in ("input_path", "route", "status"):
            if section not in content:
                failures.append(f"[{label}] '{section}' missing from txt report")

    return failures


# ── Scenario runner ───────────────────────────────────────────────────────────

def _run_scenario(
    label: str,
    input_path: Path,
    expected_route: str,
    work_root: Path,
    verbose: bool = False,
) -> tuple[bool, list[str]]:
    """Run one smoke scenario. Returns (passed, messages)."""
    messages: list[str] = []
    ws = create_workspace(work_root / label / "workspace")
    t0 = time.monotonic()

    try:
        result = deadzone_smart_unpack(input_path, ws)
    except FileNotFoundError as exc:
        return False, [f"[{label}] FileNotFoundError: {exc}"]
    except Exception as exc:
        return False, [f"[{label}] Unexpected exception: {exc}\n{traceback.format_exc()}"]

    elapsed = time.monotonic() - t0

    failures = _validate_result(result, expected_route, label)
    failures += _validate_outputs(ws.root, label)

    if verbose:
        print(f"  route          : {result.get('route')}")
        print(f"  route_reason   : {result.get('route_reason')}")
        print(f"  status         : {result.get('status')}")
        images = result.get("images") or {}
        found = [k for k, v in images.items() if v]
        print(f"  images found   : {found or '(none)'}")
        missing_req = result.get("missing_required") or []
        if missing_req:
            print(f"  missing req    : {missing_req}")
        print(f"  elapsed        : {elapsed:.3f}s")

    passed = len(failures) == 0
    return passed, failures


# ── Real-ROM scenario (optional) ─────────────────────────────────────────────

def _run_real_rom_scenario(
    rom_path: Path,
    work_root: Path,
    verbose: bool = False,
) -> tuple[bool, list[str]]:
    label = "real_rom"
    messages: list[str] = []
    ws = create_workspace(work_root / label / "workspace")

    try:
        result = deadzone_smart_unpack(rom_path, ws)
    except FileNotFoundError as exc:
        return False, [f"[{label}] FileNotFoundError: {exc}"]
    except Exception as exc:
        return False, [f"[{label}] Unexpected exception: {exc}\n{traceback.format_exc()}"]

    if verbose:
        print(f"  route          : {result.get('route')}")
        print(f"  route_reason   : {result.get('route_reason')}")
        print(f"  status         : {result.get('status')}")
        images = result.get("images") or {}
        found = [k for k, v in images.items() if v]
        print(f"  images found   : {found or '(none)'}")
        missing_req = result.get("missing_required") or []
        if missing_req:
            print(f"  missing req    : {missing_req}")
        missing_opt = result.get("missing_optional") or []
        if missing_opt:
            print(f"  missing opt    : {missing_opt}")
        print(f"  error          : {result.get('error') or '(none)'}")

    failures = _validate_result(result, result.get("route", ""), label)
    # Accept any known route for real ROM — no expected_route assertion
    failures = [f for f in failures if "Expected route=" not in f]
    failures += _validate_outputs(ws.root, label)

    passed = len(failures) == 0
    return passed, failures


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description="DeadZone smart_unpack smoke test")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show detailed output per scenario")
    parser.add_argument("--rom-path", type=Path, default=None,
                        help="Optional path to a real ROM file or folder for an extra real-ROM scenario")
    parser.add_argument("--keep-workspace", action="store_true",
                        help="Keep temporary workspace directories after the run")
    args = parser.parse_args()

    print("=" * 60)
    print("  DeadZone Smart Unpack – Smoke Test")
    print("=" * 60)

    work_root = Path(tempfile.mkdtemp(prefix="dz_smoke_"))
    fixture_root = work_root / "fixtures"
    fixture_root.mkdir(parents=True)

    all_passed = True
    total = 0
    passed_count = 0

    scenarios = [
        ("ota_zip_payload",    _make_ota_zip_with_payload(fixture_root), ROUTE_PAYLOAD),
        ("fastboot_tgz",       _make_fastboot_tgz(fixture_root),         ROUTE_FASTBOOT),
        ("raw_super_img",      _make_raw_super_img(fixture_root),        ROUTE_SUPER),
        ("image_folder",       _make_image_folder(fixture_root),         ROUTE_IMAGE_FOLDER),
    ]

    for label, input_path, expected_route in scenarios:
        total += 1
        print(f"\n[{label}]")
        print(f"  input          : {input_path}")
        print(f"  expected route : {expected_route}")

        passed, failures = _run_scenario(
            label, input_path, expected_route, work_root, verbose=args.verbose
        )

        if passed:
            passed_count += 1
            print(f"  result         : PASS")
        else:
            all_passed = False
            print(f"  result         : FAIL")
            for msg in failures:
                print(f"    {msg}")

    if args.rom_path:
        total += 1
        print(f"\n[real_rom]")
        print(f"  input          : {args.rom_path}")

        if not args.rom_path.exists():
            print(f"  result         : SKIP (path does not exist)")
        else:
            passed, failures = _run_real_rom_scenario(
                args.rom_path, work_root, verbose=args.verbose
            )
            if passed:
                passed_count += 1
                print(f"  result         : PASS")
            else:
                all_passed = False
                print(f"  result         : FAIL")
                for msg in failures:
                    print(f"    {msg}")

    if not args.keep_workspace:
        try:
            shutil.rmtree(work_root, ignore_errors=True)
        except Exception:
            pass
    else:
        print(f"\n[workspace] kept at: {work_root}")

    print("\n" + "=" * 60)
    print(f"  Results: {passed_count}/{total} scenarios passed")
    if all_passed:
        print("  Status : ALL PASSED")
    else:
        print("  Status : FAILURES — see above")
    print("=" * 60)

    print("\nNote: mkfs.erofs is not available on Windows.")
    print("If the full test suite fails only on stable_partition_rebuild tests,")
    print("that is a pre-existing platform limitation unrelated to smart_unpack.")

    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
