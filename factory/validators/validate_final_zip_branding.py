"""Validate that a final DeadZone ROM ZIP contains no forbidden branding."""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

FORBIDDEN_TERMS: list[str] = [
    "HyperUR",
    "hyperur",
    "HYPERUR",
    "Elite",
    "elite",
    "ELITE",
    "lcnguyn06",
    "HassanMirz01",
    "RIO",
    "hyperur.io.vn",
    "HyperUR_firmware.txt",
]

# Extensions whose text content is scanned
TEXT_EXTENSIONS: frozenset[str] = frozenset(
    {".bat", ".cmd", ".txt", ".md", ".xml", ".prop", ".ini", ".json"}
)

# Extensions that are binary and too large to text-scan
SKIP_EXTENSIONS: frozenset[str] = frozenset(
    {".img", ".so", ".elf", ".bin", ".apk", ".jar", ".dll", ".exe"}
)


def validate_final_zip_branding(zip_path: Path) -> tuple[bool, list[str]]:
    """Return (passed, violations).

    violations is a list of human-readable strings describing each problem found.
    """
    if not zip_path.exists():
        return False, [f"[BRANDING] ZIP not found: {zip_path}"]

    violations: list[str] = []

    with zipfile.ZipFile(zip_path, "r") as zf:
        for entry in zf.infolist():
            name = entry.filename

            # 1 — Check the filename / path itself
            for term in FORBIDDEN_TERMS:
                if term in name:
                    violations.append(
                        f"[BRANDING] Filename contains forbidden term {term!r}: {name!r}"
                    )

            # 2 — Check text content for scannable extensions
            ext = Path(name).suffix.lower()
            if ext in SKIP_EXTENSIONS:
                continue
            if ext not in TEXT_EXTENSIONS:
                continue
            try:
                raw = zf.read(name)
                # Skip large files (> 2 MB) even for text
                if len(raw) > 2 * 1024 * 1024:
                    continue
                content = raw.decode("utf-8", errors="replace")
                for term in FORBIDDEN_TERMS:
                    if term in content:
                        violations.append(
                            f"[BRANDING] File content contains forbidden term {term!r}: {name!r}"
                        )
            except Exception as exc:
                violations.append(f"[BRANDING] Could not read {name!r}: {exc}")

    passed = len(violations) == 0
    return passed, violations


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Validate final ROM ZIP branding")
    parser.add_argument("--zip", required=True, help="Path to the final ZIP to validate")
    args = parser.parse_args(argv)

    zip_path = Path(args.zip)
    passed, violations = validate_final_zip_branding(zip_path)

    if passed:
        print(f"[BRANDING OK] No forbidden branding found in: {zip_path.name}")
    else:
        print(f"[BRANDING FAIL] {len(violations)} violation(s) found in: {zip_path.name}")
        for v in violations:
            print(f"  {v}")

    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
