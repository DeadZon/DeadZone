"""Inspect a final DeadZone ROM ZIP and write a manifest report."""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path


SCRIPT_EXTENSIONS: frozenset[str] = frozenset({".bat", ".cmd"})
IMAGE_EXTENSIONS: frozenset[str] = frozenset({".img"})

REPORT_DIR = Path("output/reports")


def inspect_zip(zip_path: Path) -> dict:
    """Return a dict describing the ZIP contents."""
    if not zip_path.exists():
        return {"error": f"ZIP not found: {zip_path}"}

    entries: list[zipfile.ZipInfo] = []
    with zipfile.ZipFile(zip_path, "r") as zf:
        entries = zf.infolist()

    images = [
        e for e in entries
        if Path(e.filename).suffix.lower() in IMAGE_EXTENSIONS
    ]
    scripts = [
        e for e in entries
        if Path(e.filename).suffix.lower() in SCRIPT_EXTENSIONS
    ]

    total_uncompressed = sum(e.file_size for e in entries)
    compressed_size = zip_path.stat().st_size

    return {
        "zip_path": str(zip_path),
        "zip_name": zip_path.name,
        "total_files": len(entries),
        "image_count": len(images),
        "script_count": len(scripts),
        "total_uncompressed_bytes": total_uncompressed,
        "compressed_bytes": compressed_size,
        "entries": [e.filename for e in entries],
        "images": [e.filename for e in images],
        "scripts": [e.filename for e in scripts],
    }


def write_manifest(info: dict) -> Path:
    """Write the manifest to output/reports/final_zip_manifest.txt and return the path."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / "final_zip_manifest.txt"

    def fmt_size(n: int) -> str:
        for unit in ("B", "KB", "MB", "GB"):
            if n < 1024:
                return f"{n:.1f} {unit}"
            n /= 1024
        return f"{n:.1f} TB"

    lines: list[str] = []
    lines.append("=" * 60)
    lines.append("DeadZone Final ZIP Manifest")
    lines.append("=" * 60)
    lines.append(f"ZIP      : {info.get('zip_name', '?')}")
    lines.append(f"Path     : {info.get('zip_path', '?')}")
    lines.append(f"Files    : {info.get('total_files', 0)}")
    lines.append(f"Images   : {info.get('image_count', 0)}")
    lines.append(f"Scripts  : {info.get('script_count', 0)}")
    lines.append(
        f"Uncompressed size : {fmt_size(info.get('total_uncompressed_bytes', 0))}"
    )
    lines.append(
        f"Compressed size   : {fmt_size(info.get('compressed_bytes', 0))}"
    )
    lines.append("")

    lines.append("--- Image files ---")
    for img in info.get("images", []):
        lines.append(f"  {img}")

    lines.append("")
    lines.append("--- Flash scripts ---")
    for s in info.get("scripts", []):
        lines.append(f"  {s}")

    lines.append("")
    lines.append("--- All entries ---")
    for e in info.get("entries", []):
        lines.append(f"  {e}")

    lines.append("")
    lines.append("=" * 60)

    text = "\n".join(lines) + "\n"
    report_path.write_text(text, encoding="utf-8")
    return report_path


def print_summary(info: dict) -> None:
    from .validate_final_zip_branding import validate_final_zip_branding

    def fmt_size(n: int) -> str:
        for unit in ("B", "KB", "MB", "GB"):
            if n < 1024:
                return f"{n:.1f} {unit}"
            n /= 1024
        return f"{n:.1f} TB"

    print(f"[ZIP MANIFEST] {info.get('zip_name', '?')}")
    print(f"  Total files        : {info['total_files']}")
    print(f"  Image files (.img) : {info['image_count']}")
    print(f"  Flash scripts      : {info['script_count']}")
    print(f"  Uncompressed size  : {fmt_size(info['total_uncompressed_bytes'])}")
    print(f"  Compressed size    : {fmt_size(info['compressed_bytes'])}")

    # Inline branding check
    zip_path = Path(info["zip_path"])
    passed, violations = validate_final_zip_branding(zip_path)
    if passed:
        print("  Branding status    : [OK] No forbidden terms found")
    else:
        print(f"  Branding status    : [FAIL] {len(violations)} violation(s)")
        for v in violations:
            print(f"    {v}")


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Inspect final ROM ZIP and write manifest")
    parser.add_argument("--zip", required=True, help="Path to the final ZIP")
    args = parser.parse_args(argv)

    zip_path = Path(args.zip)
    info = inspect_zip(zip_path)

    if "error" in info:
        print(f"[ZIP MANIFEST ERROR] {info['error']}", file=sys.stderr)
        return 1

    report_path = write_manifest(info)
    print_summary(info)
    print(f"\n[ZIP MANIFEST] Report written to: {report_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
