from __future__ import annotations

from typing import Any


STAGE_DEFINITIONS: list[dict[str, Any]] = [
    {
        "id": "preflight",
        "title": "Preflight Check",
        "description": "Workspace setup and policy configuration",
        "weight": 2,
        "success_text": "Workspace ready",
        "fail_text": "Workspace setup failed",
    },
    {
        "id": "rom_detect",
        "title": "ROM Detection",
        "description": "Download ROM and detect version, device, and metadata",
        "weight": 6,
        "success_text": "ROM detected",
        "fail_text": "ROM detection failed",
    },
    {
        "id": "payload_unpack",
        "title": "Payload Unpack",
        "description": "Extract ROM payload and inspect partition layout",
        "weight": 10,
        "success_text": "Payload extracted",
        "fail_text": "Payload extraction failed",
    },
    {
        "id": "image_mount",
        "title": "Image Mount",
        "description": "Extract and mount partition images for modification",
        "weight": 12,
        "success_text": "Images mounted",
        "fail_text": "Image mount failed",
    },
    {
        "id": "app_inventory_scan",
        "title": "App Inventory Scan",
        "description": "Scan all partition app directories and classify apps",
        "weight": 8,
        "success_text": "App inventory complete",
        "fail_text": "App inventory scan failed",
    },
    {
        "id": "app_policy_compare",
        "title": "App Policy Compare",
        "description": "Compare scanned apps against DeadZone app policy list",
        "weight": 6,
        "success_text": "App policy applied",
        "fail_text": "App policy comparison failed",
    },
    {
        "id": "stable_app_policy",
        "title": "Stable App Policy",
        "description": "Enforce apps.list as source of truth: rename misnamed, delete extras",
        "weight": 7,
        "success_text": "Stable app policy enforced",
        "fail_text": "Stable app policy failed",
    },
    {
        "id": "stable_partition_rebuild",
        "title": "Stable Partition Rebuild",
        "description": "Rebuild partition images changed by Stable App Policy",
        "weight": 8,
        "success_text": "Stable partitions rebuilt",
        "fail_text": "Stable partition rebuild failed",
    },
    {
        "id": "pre_super_image_validation",
        "title": "Validating Rebuilt Images",
        "description": "Validate rebuilt dynamic partition images before lpmake",
        "weight": 3,
        "success_text": "Rebuilt images validated",
        "fail_text": "Rebuilt image validation failed",
    },
    {
        "id": "legend_patches",
        "title": "Legend Patches",
        "description": "Apply style patches (Stable, Legend, Gaming, EPiC)",
        "weight": 5,
        "success_text": "Style patches applied",
        "fail_text": "Style patch failed",
    },
    {
        "id": "image_repack",
        "title": "Image Repack",
        "description": "Repack modified partitions into images",
        "weight": 12,
        "success_text": "Images repacked",
        "fail_text": "Image repack failed",
    },
    {
        "id": "super_build",
        "title": "Super Build",
        "description": "Build super partition with lpmake",
        "weight": 14,
        "success_text": "Super image built",
        "fail_text": "Super build failed",
    },
    {
        "id": "fastboot_validation",
        "title": "Fastboot Validation",
        "description": "Validate final ZIP size and fastboot compatibility",
        "weight": 3,
        "success_text": "Validation passed",
        "fail_text": "Fastboot validation failed",
    },
    {
        "id": "zip_package",
        "title": "ZIP Package",
        "description": "Assemble final ROM ZIP",
        "weight": 8,
        "success_text": "ZIP assembled",
        "fail_text": "ZIP packaging failed",
    },
    {
        "id": "upload",
        "title": "Upload",
        "description": "Upload final ZIP to PixelDrain",
        "weight": 6,
        "success_text": "Upload complete",
        "fail_text": "Upload failed",
    },
    {
        "id": "final_report",
        "title": "Final Report",
        "description": "Generate reports, send Telegram notification, and clean up",
        "weight": 4,
        "success_text": "Build complete",
        "fail_text": "Report generation failed",
    },
]

# Maps actual build stage names (used in deadzone.py) to registry stage IDs
BUILD_STAGE_MAP: dict[str, str] = {
    "prepare": "preflight",
    "download": "rom_detect",
    "detect": "rom_detect",
    "device": "rom_detect",
    "unpack": "payload_unpack",
    "inspect": "payload_unpack",
    "image_extraction": "image_mount",
    "app_inventory": "app_inventory_scan",
    "app_policy_compare": "app_policy_compare",
    "stable_app_normalize": "app_policy_compare",
    "inventory_package": "app_policy_compare",
    "stable_app_policy": "stable_app_policy",
    "stable_partition_rebuild": "stable_partition_rebuild",
    "pre_super_image_validation": "pre_super_image_validation",
    "size_reduction": "image_mount",
    "super_profile": "super_build",
    "style": "legend_patches",
    "repack": "image_repack",
    "super": "super_build",
    "final_zip": "zip_package",
    "size_policy": "fastboot_validation",
    "upload": "upload",
    "telegram": "final_report",
    "cleanup": "final_report",
}

_STAGE_ORDER: list[str] = [s["id"] for s in STAGE_DEFINITIONS]
_TOTAL_WEIGHT: int = sum(s["weight"] for s in STAGE_DEFINITIONS)
_BY_ID: dict[str, dict[str, Any]] = {s["id"]: s for s in STAGE_DEFINITIONS}


def stage_by_id(stage_id: str) -> dict[str, Any] | None:
    return _BY_ID.get(stage_id)


def registry_stage_for(build_stage: str) -> str:
    return BUILD_STAGE_MAP.get(build_stage, build_stage)


def progress_for_completed_stages(completed_registry_ids: set[str]) -> float:
    done = sum(
        s["weight"]
        for s in STAGE_DEFINITIONS
        if s["id"] in completed_registry_ids
    )
    if _TOTAL_WEIGHT == 0:
        return 0.0
    return min(100.0, done / _TOTAL_WEIGHT * 100.0)


def progress_at_stage_start(build_stage: str) -> float:
    registry_id = registry_stage_for(build_stage)
    cumulative = 0
    for s in STAGE_DEFINITIONS:
        if s["id"] == registry_id:
            break
        cumulative += s["weight"]
    return min(99.0, cumulative / _TOTAL_WEIGHT * 100.0)


def ordered_stage_ids() -> list[str]:
    return list(_STAGE_ORDER)


def total_weight() -> int:
    return _TOTAL_WEIGHT
