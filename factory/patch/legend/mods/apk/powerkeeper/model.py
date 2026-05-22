"""Data model for Legend PowerKeeper APK patch rules."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class PatchStatus(Enum):
    PATCHED = "PATCHED"
    WOULD_PATCH = "WOULD_PATCH"
    EXISTS = "EXISTS"
    SKIPPED_OPTIONAL = "SKIPPED_OPTIONAL"
    FAILED_NOT_FOUND = "FAILED_NOT_FOUND"
    FAILED_AMBIGUOUS = "FAILED_AMBIGUOUS"
    FAILED_REBUILD = "FAILED_REBUILD"


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
    flag_rewrite_count: int = 0


@dataclass
class ClassPatch:
    target_class: str
    patches: list[SmaliPatch] = field(default_factory=list)
    class_fallback_names: list[str] = field(default_factory=list)
    class_anchors: list[str] = field(default_factory=list)


def load_class_patch(module) -> ClassPatch:
    patches: list[SmaliPatch] = []
    for patch in getattr(module, "PATCHES", []):
        patches.append(SmaliPatch(
            id=patch.get("id", ""),
            type=patch.get("type", "method_replace"),
            method=patch.get("method", ""),
            method_name=patch.get("method_name", ""),
            method_anchors=patch.get("method_anchors", []),
            search=patch.get("search"),
            replacement=patch.get("replacement", ""),
            required=patch.get("required", True),
            reason=patch.get("reason", ""),
            flag_rewrite_count=int(patch.get("flag_rewrite_count", 0) or 0),
        ))
    return ClassPatch(
        target_class=getattr(module, "TARGET_CLASS", ""),
        patches=patches,
        class_fallback_names=getattr(module, "CLASS_FALLBACK_NAMES", []),
        class_anchors=getattr(module, "CLASS_ANCHORS", []),
    )
