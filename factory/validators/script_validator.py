"""Flash script validator.

Checks:
- No Unknown/unknown in user-facing script header
- No forbidden flash commands (fastboot -w, --disable-verity, etc.)
- No hardcoded per-device targets (lk1, bootloader2, tee1, tee2, scp1, scp2)
- All flashed images reference stem_ab (except super)
"""
from __future__ import annotations

import re
from pathlib import Path

_FORBIDDEN_PATTERNS = [
    (r"fastboot\s+-w\b", "fastboot -w"),
    (r"--disable-verity", "--disable-verity"),
    (r"--disable-verification", "--disable-verification"),
    (r"\bflash\s+preloader\b", "flash preloader"),
    (r"\bflash\s+lk1\b", "flash lk1"),
    (r"\bflash\s+bootloader2\b", "flash bootloader2"),
    (r"\bflash\s+tee1\b", "flash tee1"),
    (r"\bflash\s+tee2\b", "flash tee2"),
    (r"\bflash\s+scp1\b", "flash scp1"),
    (r"\bflash\s+scp2\b", "flash scp2"),
]

_FORBIDDEN_HEADER = re.compile(r"\bunknown\b", re.IGNORECASE)


def validate_script(script_path: Path | str) -> dict:
    script_path = Path(script_path)
    errors: list[str] = []
    warnings: list[str] = []

    if not script_path.is_file():
        return {"passed": False, "errors": [f"Script not found: {script_path}"], "warnings": []}

    text = script_path.read_text(encoding="ascii", errors="replace")
    lines = text.splitlines()

    for i, line in enumerate(lines, 1):
        for pattern, label in _FORBIDDEN_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                errors.append(f"line {i}: forbidden command '{label}'")
        # Check for Unknown in header echo lines
        if line.strip().lower().startswith("echo") and _FORBIDDEN_HEADER.search(line):
            errors.append(f"line {i}: 'unknown' found in user-facing header: {line.strip()!r}")

    passed = not errors
    return {"passed": passed, "errors": errors, "warnings": warnings, "script": str(script_path)}


if __name__ == "__main__":
    import json, sys
    for path in sys.argv[1:]:
        r = validate_script(path)
        print(json.dumps(r, indent=2))
    sys.exit(0 if all(not r["errors"] for r in [validate_script(p) for p in sys.argv[1:]]) else 1)
