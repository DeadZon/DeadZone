"""Provision patch policy gates."""
from __future__ import annotations

BUILD_FLAG_POLICY = "keep_stock"
SKIP_BUILD_FLAG_REWRITES = True
PROTECTED_BUILD_FLAGS = [
    "Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z",
    "Lmiui/os/Build;->IS_GLOBAL_BUILD:Z",
]
DISALLOWED_TARGET_FLAGS = [
    "Lmiui/os/Build;->IS_ELITE_DEVELOPMENT_BUILD:Z",
    "Lmiui/os/Build;->IS_MEZO_DEVELOPMENT_BUILD:Z",
]

_FLAG_MAP = {
    DISALLOWED_TARGET_FLAGS[0]: PROTECTED_BUILD_FLAGS[0],
    DISALLOWED_TARGET_FLAGS[1]: PROTECTED_BUILD_FLAGS[1],
}


def contains_protected_or_disallowed_build_flag(text: str) -> bool:
    return any(flag in text for flag in PROTECTED_BUILD_FLAGS + DISALLOWED_TARGET_FLAGS)


def normalize_build_flags_to_stock(text: str) -> tuple[str, bool]:
    changed = False
    for bad, stock in _FLAG_MAP.items():
        if bad in text:
            text = text.replace(bad, stock)
            changed = True
    return text, changed


def strip_build_flag_refs(text: str) -> str:
    for flag in PROTECTED_BUILD_FLAGS + DISALLOWED_TARGET_FLAGS:
        text = text.replace(flag, "")
    return "".join(text.split())

