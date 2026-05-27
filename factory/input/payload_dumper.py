"""Payload dump helper for the ROM intake pipeline.

Wraps factory.unpack.payload.extract_from_payload into the dict interface
consumed by rom_unpacker and the test suite.
"""
from __future__ import annotations

from pathlib import Path

# Partitions targeted for Free builds.  All available partitions are dumped
# when the extractor is called with an empty partition list; this constant is
# kept for documentation and selective-dump fallback if needed.
FREE_PARTITIONS: list[str] = [
    "boot", "init_boot", "vendor_boot", "dtbo",
    "vbmeta", "vbmeta_system", "vbmeta_vendor",
    "system", "system_ext", "product", "vendor", "odm",
    "mi_ext", "vendor_dlkm", "odm_dlkm", "system_dlkm",
    # common firmware partitions
    "tz", "aboot", "xbl", "xbl_config", "devcfg",
    "modem", "bluetooth", "dsp", "keymaster",
]


def dump_payload(
    payload_bin: Path,
    output_dir: Path,
    partitions: list[str] | None = None,
) -> dict:
    """Extract partition images from *payload_bin* into *output_dir*.

    Parameters
    ----------
    payload_bin:
        Path to a payload.bin file.
    output_dir:
        Directory where extracted .img files will be written.
    partitions:
        Optional list of partition names to extract.  Pass None (default) to
        dump all available partitions.

    Returns
    -------
    dict with keys:
        status        — "OK" | "FAILED"
        payload_bin   — str path
        output_dir    — str path
        dumped_images — list[str] of extracted .img filenames
        dumped_count  — int
        tool_used     — str description of the extractor used
        errors        — list[str]
        warnings      — list[str]
    """
    payload_bin = Path(payload_bin)
    output_dir = Path(output_dir)
    log_path = output_dir.parent / "logs" / "payload_extract.log"

    result: dict = {
        "status": "FAILED",
        "payload_bin": str(payload_bin),
        "output_dir": str(output_dir),
        "dumped_images": [],
        "dumped_count": 0,
        "tool_used": "unknown",
        "errors": [],
        "warnings": [],
    }

    if not payload_bin.is_file():
        result["errors"].append(f"payload.bin not found: {payload_bin}")
        return result

    output_dir.mkdir(parents=True, exist_ok=True)

    from factory.unpack.payload import extract_from_payload  # noqa: PLC0415

    success, _manifest_sizes = extract_from_payload(payload_bin, output_dir, log_path)

    # Infer which backend succeeded from the log file.
    tool_used = "unknown"
    if log_path.is_file():
        try:
            log_text = log_path.read_text(encoding="utf-8", errors="replace")
            if "Internal extractor: success" in log_text:
                tool_used = "payload_extract (internal)"
            elif "payload-dumper-go: success" in log_text:
                tool_used = "payload-dumper-go"
        except Exception:
            pass

    result["tool_used"] = tool_used

    if success:
        imgs = sorted(output_dir.glob("*.img"))
        result["dumped_images"] = [p.name for p in imgs]
        result["dumped_count"] = len(imgs)
        result["status"] = "OK"
    else:
        result["errors"].append(
            "payload.bin was extracted but could not be dumped into images."
        )

    return result
