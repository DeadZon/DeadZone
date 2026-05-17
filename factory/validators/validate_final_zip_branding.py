"""Validate that a final DeadZone ROM ZIP contains no forbidden branding."""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

# ── Strictly forbidden in filenames AND text content ──────────────────────────
# Plain substring match: any occurrence in a scannable file is a violation.
# NOTE: "RIO" is intentionally absent here — see _RIO_BRANDING_RE below.
FORBIDDEN_TERMS: list[str] = [
    "HyperUR",
    "hyperur",
    "HYPERUR",
    "Elite",
    "elite",
    "ELITE",
    "lcnguyn06",
    "HassanMirz01",
    "hyperur.io.vn",
    "HyperUR_firmware.txt",
]

# ── RIO: context-sensitive branding check ─────────────────────────────────────
# "RIO" is the handle of a contributor to a competing ROM project.  It MUST NOT
# be a plain global substring match because it appears legitimately inside
# bundled platform-tools NOTICE / licence text (e.g. as a substring of
# third-party library or project names in Android SDK NOTICE.txt).
#
# It is only a violation when it appears in a clear DeadZone branding /
# attribution context:
#   - lcnguyn06(RIO)         ← attribution line pairing both handles
#   - by RIO                 ← direct authorship claim
#   - Mod by RIO
#   - Developer: RIO / Developer RIO
#   - RIO Team
#   - title ... RIO          ← Windows batch title command
#   - echo  ... RIO          ← Windows batch echo command
#
# BAT / CMD scripts are still fully covered: if a flash script were to echo
# or title "RIO" it would match the last two patterns.
_RIO_BRANDING_RE = re.compile(
    r"lcnguyn06[^\n]*RIO"        # lcnguyn06(RIO) or any attribution pairing
    r"|by\s+RIO\b"               # by RIO
    r"|Mod\s+by\s+RIO\b"        # Mod by RIO
    r"|Developer[:\s]+RIO\b"    # Developer: RIO  /  Developer RIO
    r"|RIO\s+Team\b"             # RIO Team
    r"|title\b[^\n]*\bRIO\b"    # BAT title command mentioning RIO
    r"|echo\b[^\n]*\bRIO\b"     # BAT echo command mentioning RIO
)

# ── Third-party notice / licence files: content scan skipped ──────────────────
# These files are part of the bundled platform-tools (fastboot.exe, adb.exe,
# DLLs) distributed by Google under Apache 2.0.  Their content legitimately
# contains third-party project names and author handles.  They are NOT DeadZone
# flash scripts and MUST NOT be edited or removed.
#
# Filenames are still scanned for strong forbidden terms (FORBIDDEN_TERMS).
# Only content scanning is skipped.
_THIRD_PARTY_NOTICE_BASENAMES: frozenset[str] = frozenset(
    {"notice.txt", "license.txt", "source.properties"}
)


def _is_third_party_notice(archive_name: str) -> bool:
    """Return True if the ZIP entry is a known third-party licence / notice file."""
    basename = archive_name.lower().rsplit("/", 1)[-1]
    return basename in _THIRD_PARTY_NOTICE_BASENAMES


# Extensions whose text content is scanned for branding terms
TEXT_EXTENSIONS: frozenset[str] = frozenset(
    {".bat", ".cmd", ".txt", ".md", ".xml", ".prop", ".ini", ".json"}
)

# Binary extensions — never text-scanned
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

            # ── 1. Filename / path check ──────────────────────────────────────
            # Strong terms only.  RIO is not checked in filenames because no
            # legitimate file in the ZIP should ever be named after that handle,
            # but a generic substring match would be too broad for short paths.
            for term in FORBIDDEN_TERMS:
                if term in name:
                    violations.append(
                        f"[BRANDING] Filename contains forbidden term {term!r}: {name!r}"
                    )

            # ── 2. Text content check ─────────────────────────────────────────
            ext = Path(name).suffix.lower()
            if ext in SKIP_EXTENSIONS:
                continue
            if ext not in TEXT_EXTENSIONS:
                continue

            # Third-party tool notice/licence files: skip content scan.
            # META-INF/windows/NOTICE.txt (and any other NOTICE.txt /
            # LICENSE.txt / source.properties) belong to bundled platform-tools
            # distributed by Google.  Their text is not under our control.
            if _is_third_party_notice(name):
                continue

            try:
                raw = zf.read(name)
                # Skip unexpectedly large text files
                if len(raw) > 2 * 1024 * 1024:
                    continue
                content = raw.decode("utf-8", errors="replace")

                # Strong terms — plain substring match
                for term in FORBIDDEN_TERMS:
                    if term in content:
                        violations.append(
                            f"[BRANDING] File content contains forbidden term {term!r}: {name!r}"
                        )

                # RIO — context-sensitive pattern match
                m = _RIO_BRANDING_RE.search(content)
                if m:
                    violations.append(
                        f"[BRANDING] File content contains RIO branding pattern "
                        f"({m.group()!r}): {name!r}"
                    )

            except Exception as exc:
                violations.append(f"[BRANDING] Could not read {name!r}: {exc}")

    passed = len(violations) == 0
    return passed, violations


# ── Self-test: documents expected behaviour without requiring pytest ───────────
def _selftest() -> None:
    """Smoke-test the RIO and notice-skip logic in isolation."""
    # Context patterns that MUST be flagged
    assert _RIO_BRANDING_RE.search("Developer: RIO"), "Developer: RIO must match"
    assert _RIO_BRANDING_RE.search("Mod by RIO"), "Mod by RIO must match"
    assert _RIO_BRANDING_RE.search("lcnguyn06(RIO)"), "lcnguyn06(RIO) must match"
    assert _RIO_BRANDING_RE.search("title DeadZone RIO"), "BAT title RIO must match"
    assert _RIO_BRANDING_RE.search("echo Flash by RIO"), "BAT echo by RIO must match"

    # Plain RIO in licence text MUST NOT be flagged
    plain = "This software includes RIO networking library under Apache 2.0."
    assert not _RIO_BRANDING_RE.search(plain), "Plain RIO in licence text must not match"

    # Notice file skip check
    assert _is_third_party_notice("META-INF/windows/NOTICE.txt")
    assert _is_third_party_notice("tools/LICENSE.txt")
    assert _is_third_party_notice("source.properties")
    assert not _is_third_party_notice("META-INF/windows/windows_install_upgrade.bat")

    print("[SELFTEST] validate_final_zip_branding: all assertions passed.")


def main(argv: list[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Validate final ROM ZIP branding")
    parser.add_argument("--zip", required=True, help="Path to the final ZIP to validate")
    parser.add_argument("--selftest", action="store_true", help="Run internal logic assertions")
    args = parser.parse_args(argv)

    if args.selftest:
        _selftest()
        return 0

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
