from __future__ import annotations
from pathlib import Path

ALLOWED_PARTITIONS = {
    "system",
    "system_ext",
    "product",
    "vendor",
    "odm",
    "vendor_dlkm",
    "system_dlkm",
    "odm_dlkm",
    "mi_ext",
    "cust",
    "vendor_boot",
    "boot",
    "init_boot",
    "dtbo",
    "vbmeta",
    "vbmeta_system",
    "vbmeta_vendor",
    "metadata",
}


def apply_build_package(
    root: Path,
    build_dir: Path | None,
    build_url: str | None,
    edition: str,
    execute: bool = False,
) -> dict:
    if build_dir is None:
        return {"status": "SKIPPED_TEMPORARY", "reason": "no build_dir provided"}

    unknown = [
        d.name for d in sorted(build_dir.iterdir())
        if d.is_dir() and d.name not in ALLOWED_PARTITIONS
    ]
    if unknown:
        return {
            "status": "FAILED",
            "reason": f"unknown partitions: {unknown}",
            "unknown_partitions": unknown,
        }

    return {
        "status": "OK",
        "edition": edition,
        "execute": execute,
        "build_dir": str(build_dir),
    }
