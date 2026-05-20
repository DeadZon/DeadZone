"""
Compatibility wrapper — framework.jar MTCR patch.

Real logic has moved to per-class modules under:
  factory/patch/legend/mtcr/framework/

This file is kept only so that any callers that imported
apply_framework_mtcr_patch() directly continue to work.
It now delegates to runner._patch_one_jar() logic via the runner API.
"""
from __future__ import annotations

from pathlib import Path

TARGET_JAR_NAME      = "framework.jar"
TARGET_JAR_PARTITION = "system"
TARGET_JAR_REL_PATH  = "framework/framework.jar"
PATCH_ID             = "legend_mtcr_framework"
MTCR_FILENAME        = "Framework_Legend.mtcr"


def apply_framework_mtcr_patch(work_dir: Path, report: dict, execute: bool) -> dict:
    """
    Compatibility shim — delegates to the per-class runner logic.

    The real patching is done by runner.apply_legend_mtcr_patches().
    This wrapper is invoked from the old per-JAR call site in runner.py;
    the new runner no longer calls it — it works directly with per-class modules.
    """
    return {
        "patch_id":       PATCH_ID,
        "mtcr_filename":  MTCR_FILENAME,
        "target_jar":     TARGET_JAR_NAME,
        "status":         "DELEGATED_TO_PER_CLASS_RUNNER",
        "modified_count": 0,
        "added_count":    0,
        "mtcr_path":      None,
        "class_results":  [],
        "errors":         [],
        "warnings":       [
            "apply_framework_mtcr_patch() is a compatibility shim. "
            "Real patches are applied by factory.patch.legend.mtcr.runner."
        ],
    }
