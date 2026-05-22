"""
Legend JAR mod — framework/kaorios_toolbox_v203

Injects the Kaorios Toolbox v2.0.3 DEX into framework.jar.

Asset location (user must place it manually):
  Legend/kousi/v2.0.3/classes_kaorios.dex

Optional checksum file:
  Legend/kousi/v2.0.3/sha256.txt

Behavior:
  1. Locate the DEX at Legend/kousi/v2.0.3/classes_kaorios.dex.
  2. Verify SHA-256 if sha256.txt present.
  3. If DEX missing and mod enabled → FAIL clearly (no silent skip).
  4. If found → inject into framework.jar via add_dex_merger.
  5. DO NOT download the DEX during build.

Config gate: kaorios_toolbox_v203 (default: False)
Security sensitive: True (adds third-party code to system framework)
"""
from __future__ import annotations

import hashlib
from pathlib import Path

MOD_ID = "kaorios_toolbox_v203"
TARGET_JAR = "framework.jar"
METADATA = {
    "mod_id":             MOD_ID,
    "target_jar":         TARGET_JAR,
    "target_classes":     ["com/android/internal/util/kaorios/*"],
    "target_methods":     ["(injected via DEX merge)"],
    "enabled_by_default": False,
    "security_sensitive": True,
    "report_keys":        ["status", "enabled", "dex_path", "dex_found", "sha256_verified"],
}

_REPO_ROOT = Path(__file__).resolve().parents[6]  # MEZO repo root
_DEX_PATH  = _REPO_ROOT / "Legend" / "kousi" / "v2.0.3" / "classes_kaorios.dex"
_SHA_PATH  = _REPO_ROOT / "Legend" / "kousi" / "v2.0.3" / "sha256.txt"
_OUTPUT_DEX_NAME = "classes_kaorios.dex"


def _verify_sha256(dex_path: Path, sha_path: Path) -> tuple[bool, str]:
    """Return (ok, message)."""
    try:
        expected = sha_path.read_text(encoding="utf-8").strip().split()[0].lower()
        digest = hashlib.sha256(dex_path.read_bytes()).hexdigest().lower()
        if digest == expected:
            return True, f"SHA-256 OK: {digest}"
        return False, f"SHA-256 mismatch: expected {expected}, got {digest}"
    except Exception as exc:
        return False, f"SHA-256 check error: {exc}"


def apply(unpack_dir: Path, config: dict, dry_run: bool = True) -> dict:
    enabled = config.get(MOD_ID, False)

    report: dict = {
        "mod_id":          MOD_ID,
        "target_jar":      TARGET_JAR,
        "status":          "UNKNOWN",
        "enabled":         enabled,
        "dex_path":        str(_DEX_PATH),
        "dex_found":       _DEX_PATH.is_file(),
        "sha256_verified": None,
        "patched_classes": [],
        "patched_methods": [],
        "warnings":        [],
        "errors":          [],
    }

    if not enabled:
        report["status"] = "SKIPPED_CONFIG_DISABLED"
        report["warnings"].append(
            f"{MOD_ID} is disabled (default). "
            "Set kaorios_toolbox_v203=True in legend_jar_mods to enable."
        )
        return report

    if not _DEX_PATH.is_file():
        report["status"] = "FAILED"
        report["errors"].append(
            f"Kaorios v2.0.3 DEX missing. "
            f"Put classes_kaorios.dex in: {_DEX_PATH.parent}"
        )
        return report

    # Optional SHA-256 verification
    if _SHA_PATH.is_file():
        ok, msg = _verify_sha256(_DEX_PATH, _SHA_PATH)
        report["sha256_verified"] = ok
        if not ok:
            report["status"] = "FAILED"
            report["errors"].append(msg)
            return report
        report["warnings"].append(msg)

    if dry_run:
        report["status"] = "DRY_RUN"
        report["warnings"].append(
            f"Would inject {_DEX_PATH.name} into {TARGET_JAR} as {_OUTPUT_DEX_NAME}."
        )
        return report

    # Inject DEX
    try:
        from factory.patch.common.add_dex_merger import merge_add_dex
        result = merge_add_dex(
            _DEX_PATH,
            unpack_dir,
            TARGET_JAR,
            dry_run=False,
        )
        if result.errors:
            report["status"] = "PARTIAL"
            report["errors"].extend(result.errors)
        else:
            report["status"] = "APPLIED"
            report["patched_classes"] = ["classes_kaorios (via DEX inject)"]
    except Exception as exc:
        report["status"] = "FAILED"
        report["errors"].append(str(exc))

    return report
