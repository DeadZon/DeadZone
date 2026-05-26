"""Validate that EU reference material has not leaked into DeadZone's active pipeline.

Checks:
  1. No eu script is marked direct_execution_allowed in the scan report
  2. packROM.sh lpmake sizing (du -sb) not present in factory/repack
  3. du -sb not used as lpmake partition size anywhere in factory/
  4. No image file size fallback in DeadZone super code
  5. No eu workflow YAML files in .github/workflows/
  6. scan_eu_reference.py does not call subprocess / os.system on eu scripts
"""
from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = REPO_ROOT / "output" / "reports"
SCAN_FILE = REPORTS_DIR / "eu_reference_scan.json"
EU_ROOT = REPO_ROOT / "third_party" / "eu_reference"
FACTORY_DIR = REPO_ROOT / "factory"
WORKFLOWS_DIR = REPO_ROOT / ".github" / "workflows"
SCRIPTS_DIR = REPO_ROOT / "scripts"

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


# ── Check 1: scan report — no direct_execution_allowed=True entries ───────────
print("\n=== Check 1: eu_reference_scan.json — no direct_execution_allowed entries ===")
if not SCAN_FILE.exists():
    warn(f"Scan report not found ({SCAN_FILE.name}); run scan_eu_reference.py to generate it")
else:
    scan = json.loads(SCAN_FILE.read_text(encoding="utf-8"))
    bad = [e["path"] for e in scan.get("entries", []) if e.get("direct_execution_allowed")]
    if bad:
        for b in bad:
            fail(f"direct_execution_allowed=true found in scan entry: {b}")
    else:
        ok(f"All {scan['summary']['total']} scan entries have direct_execution_allowed=false")


# ── Check 2: factory/repack must not contain du -sb lpmake sizing ─────────────
print("\n=== Check 2: factory/repack — no `du -sb` lpmake partition sizing ===")
DU_SB_PATTERN = re.compile(r"du\s+-sb")
repack_dir = FACTORY_DIR / "repack"
found_du_sb = False
if repack_dir.exists():
    for py_file in repack_dir.rglob("*.py"):
        text = py_file.read_text(encoding="utf-8", errors="replace")
        if DU_SB_PATTERN.search(text):
            fail(f"du -sb found in repack file: {py_file.relative_to(REPO_ROOT)}")
            found_du_sb = True
    if not found_du_sb:
        ok("factory/repack: no `du -sb` lpmake sizing found")
else:
    warn("factory/repack/ directory not found")


# ── Check 3: factory/ wide — du -sb must not appear as lpmake size source ─────
print("\n=== Check 3: factory/ — `du -sb` must not be used as lpmake partition size ===")
# We search for the combined pattern of du -sb AND lpmake in the same file
LPMAKE_PATTERN = re.compile(r"lpmake", re.IGNORECASE)
found_any = False
for py_file in FACTORY_DIR.rglob("*.py"):
    text = py_file.read_text(encoding="utf-8", errors="replace")
    if DU_SB_PATTERN.search(text) and LPMAKE_PATTERN.search(text):
        fail(
            f"Both `du -sb` and `lpmake` found in same file — "
            f"verify lpmake sizing is NOT from du: {py_file.relative_to(REPO_ROOT)}"
        )
        found_any = True
if not found_any:
    ok("factory/: no file uses du -sb together with lpmake")


# ── Check 4: super code must not use image file size as lpmake fallback ────────
print("\n=== Check 4: factory/ — no image file size fallback for lpmake ===")
# Detect lines where a variable whose name implies a partition/group size is assigned from
# os.path.getsize() or .stat().st_size, AND lpmake also appears on that same line or the
# variable is then passed directly to a lpmake call on the same line.
# Single-line pattern avoids false positives from files that merely mention both concepts
# in unrelated contexts.
FILE_SIZE_LPMAKE = re.compile(
    r"(partition_size|group_size|part_size|lpmake_size|block_size)"
    r"\s*=\s*.*?(getsize\(|\.stat\(\)\.st_size)",
    re.IGNORECASE,
)
LPMAKE_DIRECT = re.compile(
    r"lpmake.*?(getsize\(|\.stat\(\)\.st_size)",
    re.IGNORECASE,
)
found_fallback = False
for py_file in FACTORY_DIR.rglob("*.py"):
    for lineno, line in enumerate(
        py_file.read_text(encoding="utf-8", errors="replace").splitlines(), start=1
    ):
        if FILE_SIZE_LPMAKE.search(line) or LPMAKE_DIRECT.search(line):
            fail(
                f"Image file size used as lpmake partition size on line {lineno}: "
                f"{py_file.relative_to(REPO_ROOT)} — use payload_manifest sizes only"
            )
            found_fallback = True
if not found_fallback:
    ok("factory/: no image file-size fallback for lpmake partition sizing")


# ── Check 5: no eu workflow YAMLs in .github/workflows/ ───────────────────────
print("\n=== Check 5: .github/workflows/ — no eu workflow files ===")
EU_WORKFLOW_INDICATORS = [
    "NothingsVN",
    "eu_reference",
    "packROM.sh",
    "uploadROM.sh",
    "eu_upload",
    "OneDrive",
    "super.img.zst",
]
found_eu_workflow = False
if WORKFLOWS_DIR.exists():
    for wf_file in WORKFLOWS_DIR.glob("*.yml"):
        text = wf_file.read_text(encoding="utf-8", errors="replace")
        for indicator in EU_WORKFLOW_INDICATORS:
            if indicator in text:
                fail(
                    f"EU workflow indicator '{indicator}' found in "
                    f".github/workflows/{wf_file.name}"
                )
                found_eu_workflow = True
    if not found_eu_workflow:
        ok(".github/workflows/: no eu workflow content detected")
else:
    warn(".github/workflows/ not found")


# ── Check 6: scan_eu_reference.py must not execute eu scripts ─────────────────
print("\n=== Check 6: scan_eu_reference.py — no subprocess / os.system calls on eu paths ===")
scanner_file = SCRIPTS_DIR / "scan_eu_reference.py"
EXEC_PATTERNS = re.compile(
    r"subprocess\.(run|call|Popen|check_output)|"
    r"os\.system\s*\(|"
    r"os\.execv|"
    r"shlex\.split.*eu_reference"
)
if scanner_file.exists():
    scanner_text = scanner_file.read_text(encoding="utf-8")
    if EXEC_PATTERNS.search(scanner_text):
        fail("scan_eu_reference.py contains subprocess/os.system calls — scanner must NOT execute eu scripts")
    else:
        ok("scan_eu_reference.py: no subprocess/os.system execution found")
else:
    warn("scan_eu_reference.py not found")


# ── Check 7: eu_reference tree has no symlinks pointing outside third_party ───
print("\n=== Check 7: third_party/eu_reference/ — no symlinks escaping the tree ===")
if EU_ROOT.exists():
    bad_links: list[str] = []
    for p in EU_ROOT.rglob("*"):
        if p.is_symlink():
            target = p.resolve()
            try:
                target.relative_to(EU_ROOT)
            except ValueError:
                bad_links.append(str(p.relative_to(REPO_ROOT)))
    if bad_links:
        for bl in bad_links:
            fail(f"Symlink in eu_reference escapes the tree: {bl}")
    else:
        ok("third_party/eu_reference/: no escaping symlinks")
else:
    warn("third_party/eu_reference/ not found")


# ── Summary ────────────────────────────────────────────────────────────────────
print("\n=== Summary ===")
print(f"  Errors  : {len(errors)}")
print(f"  Warnings: {len(warnings)}")

if errors:
    print("\nFAILED — EU reference safety checks failed.\n")
    sys.exit(1)
else:
    print("\nAll EU reference checks passed.\n")
    sys.exit(0)
