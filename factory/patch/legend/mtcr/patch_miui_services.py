"""
Legend MTCR patch: miui-services.jar  <-  miui-services_Legend.mtcr

Target:  system_ext/framework/miui-services.jar
MTCR:    miui-services_Legend.mtcr

Exposes:
  apply_miui_services_mtcr_patch(work_dir, report, execute) -> dict
"""
from __future__ import annotations

from pathlib import Path

PATCH_ID              = "legend_mtcr_miui_services"
MTCR_FILENAME         = "miui-services_Legend.mtcr"
TARGET_JAR_NAME       = "miui-services.jar"
TARGET_JAR_PARTITION  = "system_ext"
TARGET_JAR_REL_PATH   = "framework/miui-services.jar"

_REPO_ROOT          = Path(__file__).resolve().parents[4]
_CANONICAL_MTCR_DIR = _REPO_ROOT / "third_party" / "mezo_core" / "MEZO_LEGEND" / "jar"
_FALLBACK_MTCR_DIR  = _REPO_ROOT / "Legend" / "jar"

SMALI_REPLACEMENTS: list[dict] = []
XML_REPLACEMENTS:   list[dict] = []
FILES_TO_COPY:      list[dict] = []
FILES_TO_REMOVE:    list[dict] = []
METHOD_PATCHES:     list[dict] = []


def _find_mtcr() -> Path | None:
    for base in (_CANONICAL_MTCR_DIR, _FALLBACK_MTCR_DIR):
        p = base / MTCR_FILENAME
        if p.is_file():
            return p
    return None


def apply_miui_services_mtcr_patch(work_dir: Path, report: dict, execute: bool) -> dict:
    """
    Apply miui-services_Legend.mtcr to the already-unpacked miui-services.jar workspace.

    Parameters
    ----------
    work_dir : Path
        Directory containing smali_classes* dirs for miui-services.jar.
    report : dict
        Parent report dict (not mutated by this function).
    execute : bool
        True to apply patches; False for dry-run (WOULD_PATCH statuses only).

    Returns
    -------
    dict  with keys: patch_id, target_jar, status, modified_count, added_count,
                     mtcr_path, class_results, errors, warnings.
    """
    from factory.patch.common.mtcr_patch import parse_mtcr
    from factory.patch.common.mtcr_exact_patcher import apply_exact_mtcr

    result: dict = {
        "patch_id":       PATCH_ID,
        "mtcr_filename":  MTCR_FILENAME,
        "target_jar":     TARGET_JAR_NAME,
        "status":         "FAILED",
        "modified_count": 0,
        "added_count":    0,
        "mtcr_path":      None,
        "class_results":  [],
        "errors":         [],
        "warnings":       [],
    }

    mtcr_path = _find_mtcr()
    if mtcr_path is None:
        result["status"] = "SKIPPED_MISSING_MTCR"
        result["errors"].append(
            f"{MTCR_FILENAME} not found in canonical or fallback location"
        )
        return result

    result["mtcr_path"] = str(mtcr_path)

    try:
        pack = parse_mtcr(mtcr_path)
    except Exception as exc:
        result["errors"].append(f"Failed to parse {MTCR_FILENAME}: {exc}")
        return result

    result["modified_count"] = len(pack.modified_classes)
    result["added_count"]    = len(pack.added_classes)

    if not execute:
        result["status"] = "WOULD_PATCH"
        result["planned"] = [
            f"WOULD_REPLACE: {len(pack.modified_classes)} modified classes",
            f"WOULD_ADD: {len(pack.added_classes)} added classes",
        ]
        return result

    try:
        raw_results = apply_exact_mtcr(pack, work_dir, dry_run=False)
        result["class_results"] = [
            {
                "class":   r.class_name,
                "status":  str(r.status),
                "message": getattr(r, "message", ""),
            }
            for r in raw_results
        ]
        failed = [r for r in raw_results if str(r.status) == "FAILED"]
        result["status"] = "FAILED" if failed else "PATCHED"
        for r in failed:
            result["errors"].append(
                f"{r.class_name}: {getattr(r, 'message', 'unknown error')}"
            )
    except Exception as exc:
        result["errors"].append(f"apply_exact_mtcr raised: {exc}")

    return result
