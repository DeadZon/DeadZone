"""
Compatibility wrapper — miui-services.jar MTCR patch.

Real logic has moved to per-class modules under:
  factory/patch/legend/mtcr/miui_services/
"""
from __future__ import annotations

from pathlib import Path

TARGET_JAR_NAME      = "miui-services.jar"
TARGET_JAR_PARTITION = "system_ext"
TARGET_JAR_REL_PATH  = "framework/miui-services.jar"
PATCH_ID             = "legend_mtcr_miui_services"
MTCR_FILENAME        = "miui-services_Legend.mtcr"


def apply_miui_services_mtcr_patch(work_dir: Path, report: dict, execute: bool) -> dict:
    """Compatibility shim — real logic lives in per-class modules."""
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
            "apply_miui_services_mtcr_patch() is a compatibility shim. "
            "Real patches are applied by factory.patch.legend.mtcr.runner."
        ],
    }
