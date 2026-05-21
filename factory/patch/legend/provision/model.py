"""Data model for Legend Provision.apk patch rules."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class PatchStatus(Enum):
    PATCHED = "PATCHED"
    WOULD_PATCH = "WOULD_PATCH"
    EXISTS = "EXISTS"
    SKIPPED_OPTIONAL = "SKIPPED_OPTIONAL"
    SKIPPED_BUILD_FLAG_POLICY = "SKIPPED_BUILD_FLAG_POLICY"
    BUILD_FLAG_PARTIALLY_SKIPPED = "BUILD_FLAG_PARTIALLY_SKIPPED"
    BRANDING_PATCHED = "BRANDING_PATCHED"
    BRANDING_SKIPPED_UNSAFE = "BRANDING_SKIPPED_UNSAFE"
    REVIEW_REQUIRED_BRANDING_STRING = "REVIEW_REQUIRED_BRANDING_STRING"
    FAILED_NOT_FOUND = "FAILED_NOT_FOUND"
    FAILED_AMBIGUOUS = "FAILED_AMBIGUOUS"
    FAILED_REBUILD = "FAILED_REBUILD"
    FAILED_MANIFEST_PATCH = "FAILED_MANIFEST_PATCH"
    FAILED_RESOURCE_PATCH = "FAILED_RESOURCE_PATCH"
    FAILED_BRANDING_PATCH = "FAILED_BRANDING_PATCH"


@dataclass
class SmaliPatch:
    id: str
    type: str
    replacement: str = ""
    required: bool = True
    reason: str = ""
    method: str = ""
    method_name: str = ""
    method_anchors: list[str] = field(default_factory=list)
    search: Optional[str] = None
    policy_status: str = ""


@dataclass
class ClassPatch:
    target_class: str
    patches: list[SmaliPatch] = field(default_factory=list)
    class_fallback_names: list[str] = field(default_factory=list)
    class_anchors: list[str] = field(default_factory=list)


def load_class_patch(module) -> ClassPatch:
    patches: list[SmaliPatch] = []
    for p in getattr(module, "PATCHES", []):
        patches.append(SmaliPatch(
            id=p.get("id", ""),
            type=p.get("type", "method_replace"),
            method=p.get("method", ""),
            method_name=p.get("method_name", ""),
            method_anchors=p.get("method_anchors", []),
            search=p.get("search"),
            replacement=p.get("replacement", ""),
            required=p.get("required", True),
            reason=p.get("reason", ""),
            policy_status=p.get("policy_status", ""),
        ))
    return ClassPatch(
        target_class=getattr(module, "TARGET_CLASS", ""),
        patches=patches,
        class_fallback_names=getattr(module, "CLASS_FALLBACK_NAMES", []),
        class_anchors=getattr(module, "CLASS_ANCHORS", []),
    )

