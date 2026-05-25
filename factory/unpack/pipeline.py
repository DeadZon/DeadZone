"""
Phase 1 unpack pipeline — orchestrates the full unpack stage.

This module is the single entry point for the unpack stage.  It:
  1. Resolves the factory device from --device / DEADZONE_DEVICE_CODENAME
  2. Creates a BuildContext with all absolute paths
  3. Detects and extracts the ROM archive
  4. Searches for super.img
  5. Falls back to payload.bin extraction when super.img is absent
  6. Unpacks super.img (or uses payload-extracted partitions directly)
  7. Reads build.prop (pure read — NO patching)
  8. Resolves effective device codename
  9. Writes reports: output/reports/01_unpack_report.json + .txt

Nothing here patches APKs, JARs, smali, vbmeta, or any filesystem image.

CLI usage
---------
    python -m factory.unpack.pipeline \\
        --rom  "path/to/rom.zip" \\
        --device zircon \\
        --soc mtk \\
        --platform os3_a16

    python -m factory.unpack.pipeline --rom "path/to/super.img"
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

# ── Repo root — used to resolve output/ and work/ directories ────────────────
_REPO_ROOT = Path(__file__).resolve().parents[2]


def _resolve_output_root() -> Path:
    """Return the repo-level output/ directory (created if absent)."""
    return _REPO_ROOT / "output"


def _build_work_dir(rom_path: Path, output_root: Path) -> Path:
    """Derive a session work directory from the ROM stem + a short timestamp."""
    stem = rom_path.name
    for suffix in (".tar.gz", ".tgz", ".zip", ".tar", ".img"):
        if stem.lower().endswith(suffix):
            stem = stem[: -len(suffix)]
            break
    ts = time.strftime("%Y%m%d_%H%M%S")
    return output_root / "work" / f"{stem}_{ts}"


# ─────────────────────────────────────────────────────────────────────────────
class UnpackPipeline:
    """
    Execute the full Phase 1 unpack stage and return the populated BuildContext.

    Parameters
    ----------
    rom_path:
        Absolute path to the source ROM (zip/tgz/tar/img).
    factory_device:
        Device codename supplied by the operator (--device flag or
        DEADZONE_DEVICE_CODENAME environment variable).  May be None.
    soc:
        SoC family string ("mtk" / "snapdragon") — stored for downstream use.
    platform:
        Platform identifier ("os3_a16", …) — stored for downstream use.
    output_root:
        Where output/ lives.  Defaults to repo_root/output/.
    """

    def __init__(
        self,
        rom_path: Path,
        *,
        factory_device: str | None = None,
        soc: str | None = None,
        platform: str | None = None,
        output_root: Path | None = None,
    ) -> None:
        self.rom_path = rom_path.resolve()
        self.factory_device = factory_device
        self.soc = soc
        self.platform = platform
        self.output_root = (output_root or _resolve_output_root()).resolve()

    # ── Public entry ──────────────────────────────────────────────────────────
    def run(self):
        """
        Execute all unpack steps and return the populated BuildContext.
        Raises RuntimeError when unpack cannot proceed (no super.img and no
        payload.bin extraction succeeded).
        """
        from factory.core.context import BuildContext
        from factory.unpack.archive import detect_archive_type, extract_rom
        from factory.unpack.build_prop import read_build_props, resolve_effective_device
        from factory.unpack.partitions import collect_boot_images, collect_extracted_partitions
        from factory.unpack.payload import extract_from_payload, find_payload_bin
        from factory.unpack.report import write_reports
        from factory.unpack.super_image import extract_partitions, find_super_img, unpack_super_img

        # ── 1. Build context with absolute paths ──────────────────────────────
        work_dir = _build_work_dir(self.rom_path, self.output_root)
        project_dir = work_dir / "project"
        output_dir = work_dir / "output"
        reports_dir = self.output_root / "reports"

        for d in (work_dir, project_dir, output_dir, reports_dir):
            d.mkdir(parents=True, exist_ok=True)

        ctx = BuildContext(
            root_dir=_REPO_ROOT,
            work_dir=work_dir,
            input_rom=self.rom_path,
            project_dir=project_dir,
            output_dir=output_dir,
            reports_dir=reports_dir,
            factory_device=self.factory_device,
        )

        print(f"\n[unpack] ═══ DeadZone Unpack Stage ═══")
        print(f"[unpack] ROM      : {ctx.input_rom}")
        print(f"[unpack] Device   : {ctx.factory_device or '(not set)'}")
        print(f"[unpack] Work dir : {ctx.work_dir}")

        # ── 2. Archive detection and extraction ───────────────────────────────
        ctx.archive_type = detect_archive_type(self.rom_path)
        print(f"[unpack] Archive type: {ctx.archive_type}")

        super_img_path: Path | None = None
        extracted_dir: Path | None = None

        if ctx.archive_type == "img" and self.rom_path.name.lower() == "super.img":
            # Direct super.img input — skip ROM extraction.
            super_img_path = self.rom_path
            ctx.super_found = True
            print(f"[unpack] Direct super.img input detected.")
        elif ctx.archive_type == "dir":
            # Existing project directory — treat as already-extracted.
            extracted_dir = self.rom_path
            print(f"[unpack] Input is a directory; treating as pre-extracted ROM.")
        else:
            extracted_dir = extract_rom(self.rom_path, work_dir)

        # ── 3. Locate super.img ───────────────────────────────────────────────
        if super_img_path is None and extracted_dir is not None:
            print(f"[unpack] Searching for super.img in: {extracted_dir}")
            super_img_path = find_super_img(extracted_dir)
            if super_img_path:
                ctx.super_found = True
                print(f"[unpack] Found super.img: {super_img_path}")
            else:
                print(f"[unpack] super.img not found.")

        # ── 4. Payload.bin fallback ───────────────────────────────────────────
        if super_img_path is None:
            search_roots: list[Path] = []
            if extracted_dir:
                search_roots.append(extracted_dir)
            search_roots.append(_REPO_ROOT)

            payload_paths = find_payload_bin(search_roots)
            ctx.payload_found = bool(payload_paths)

            if payload_paths:
                print(f"[unpack] payload.bin found: {payload_paths[0]}")
                print(f"[unpack] Attempting partition extraction from payload.bin …")
                success = extract_from_payload(
                    extracted_dir=extracted_dir or work_dir,
                    project_dir=project_dir,
                    search_roots=search_roots,
                )
                if success:
                    # payload extraction may have produced super.img — check again
                    re_found = find_super_img(extracted_dir or work_dir) if extracted_dir else None
                    if re_found:
                        super_img_path = re_found
                        ctx.super_found = True
                        print(f"[unpack] super.img materialised from payload: {super_img_path}")
                    else:
                        print(f"[unpack] Payload extracted direct partition images (no super.img).")
                else:
                    ctx.warn("payload.bin extraction failed or produced no usable output.")
            else:
                ctx.payload_found = False
                print(f"[unpack] payload.bin not found.")

        # ── 5. Unpack super.img and extract partitions ────────────────────────
        if super_img_path is not None:
            print(f"[unpack] Unpacking super.img …")
            super_out_dir = unpack_super_img(super_img_path, project_dir)
            print(f"[unpack] Extracting partitions from super …")
            extract_partitions(super_out_dir, project_dir, super_img_path)
        elif not ctx.payload_found:
            # Neither super.img nor payload.bin — cannot continue.
            ctx.error("No super.img found and no payload.bin available. Unpack cannot continue.")
            write_reports(ctx)
            raise RuntimeError(ctx.errors[-1])

        # ── 6. Boot images (standalone, from ROM extract dir) ─────────────────
        if extracted_dir and extracted_dir.is_dir():
            ctx.images = collect_boot_images(extracted_dir)
            if ctx.images:
                print(f"[unpack] Boot images found: {', '.join(ctx.images)}")

        # ── 7. Collected partitions ───────────────────────────────────────────
        ctx.partitions = collect_extracted_partitions(project_dir)
        print(f"[unpack] Extracted partitions: {ctx.partitions or '(none yet)'}")

        # ── 7a. Fail-fast: payload found but no dynamic partitions extracted ──
        if ctx.payload_found and not ctx.super_found and not ctx.partitions:
            _fail_msg = (
                "Payload extraction produced no dynamic partitions; refusing to continue "
                "patch/repack/super stages."
            )
            ctx.error(_fail_msg)
            write_reports(ctx)
            raise RuntimeError(_fail_msg)

        # ── 8. Read build.prop — pure, no patching ────────────────────────────
        print(f"[unpack] Reading build.prop …")
        props = read_build_props(project_dir)

        ctx.detected_device = props.get("ro.product.odm.device")
        ctx.android_version = props.get("ro.system.build.version.release")
        ctx.mi_version = props.get("ro.mi.os.version.incremental")

        brand = props.get("ro.product.odm.brand")
        marketname = props.get("ro.product.odm.marketname")
        if brand:
            print(f"[unpack] Brand         : {brand}")
        if ctx.detected_device:
            print(f"[unpack] Device (prop) : {ctx.detected_device}")
        if marketname:
            print(f"[unpack] Market name   : {marketname}")
        if ctx.mi_version:
            print(f"[unpack] MI version    : {ctx.mi_version}")
        if ctx.android_version:
            print(f"[unpack] Android       : {ctx.android_version}")

        # ── 9. Effective device resolution ────────────────────────────────────
        ctx.effective_device, reason = resolve_effective_device(
            ctx.detected_device, ctx.factory_device
        )
        print(f"[unpack] Effective device: {ctx.effective_device or '(undetermined)'} — {reason}")

        if ctx.effective_device is None:
            ctx.warn(
                "Effective device codename could not be determined. "
                "Set --device or DEADZONE_DEVICE_CODENAME."
            )

        # ── 10. Write reports ─────────────────────────────────────────────────
        write_reports(ctx)

        print(f"[unpack] ═══ Unpack stage complete ═══\n")
        return ctx


# ─────────────────────────────────────────────────────────────────────────────
def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m factory.unpack.pipeline",
        description="DeadZone Phase 1 — ROM unpack stage",
    )
    parser.add_argument(
        "--rom",
        required=True,
        metavar="PATH",
        help="Path to ROM archive (.zip .tgz .tar.gz .tar .img) or pre-extracted directory",
    )
    parser.add_argument(
        "--device",
        metavar="CODENAME",
        default=None,
        help="Device codename (overrides DEADZONE_DEVICE_CODENAME env var)",
    )
    parser.add_argument(
        "--soc",
        choices=["snapdragon", "mtk"],
        default=None,
        help="SoC family",
    )
    parser.add_argument(
        "--platform",
        metavar="ID",
        default=None,
        help="Platform identifier (e.g. os3_a16)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    rom_path = Path(args.rom).expanduser().resolve()
    if not rom_path.exists():
        print(f"[pipeline] ERROR: ROM path does not exist: {rom_path}", file=sys.stderr)
        return 1

    # Factory device: --device flag takes priority over environment variable.
    factory_device = args.device or os.environ.get("DEADZONE_DEVICE_CODENAME") or None

    try:
        pipeline = UnpackPipeline(
            rom_path,
            factory_device=factory_device,
            soc=args.soc,
            platform=args.platform,
        )
        ctx = pipeline.run()
        status = "OK" if not ctx.errors else "FAILED"
        print(f"[pipeline] Status: {status}")
        return 0 if not ctx.errors else 1
    except RuntimeError as exc:
        print(f"[pipeline] FATAL: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"[pipeline] Unexpected error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
