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


# ── Minimal-real mode ──────────────────────────────────────────────────────────
# When True, only PROVISION_MINIMAL_REAL_ALLOWLIST patch IDs are applied.
# All other smali patches are classified, counted, and skipped.
MINIMAL_REAL_MODE: bool = True

_LOTTIE_PKG   = "com/airbnb/lottie"
_ONETRACK_PKG = "com/xiaomi/onetrack"
_MIUIX_PKG    = "miuix/"
_ELITE_KW     = (
    "IS_ELITE_DEVELOPMENT_BUILD",
    "IS_ELITE_DEVELOPMENT_BUILDD",
    "elite",
)

# Manually approved patch IDs for minimal_real mode.
# Each entry must be hand-reviewed and must contain no Elite/flag rewrites.
PROVISION_MINIMAL_REAL_ALLOWLIST: frozenset[str] = frozenset({
    # GMS-CN state fix: corrects if-ne → if-eq in the GMS app-enabled loop.
    # Uses IS_INTERNATIONAL_BUILD only as a guard (stock value unchanged),
    # no Elite/IS_ELITE_DEVELOPMENT_BUILD references.
    "com_android_provision_Utils__setGmsAppEnabledStateForCn",
})


def classify_provision_patch_skip(
    target_class: str,
    patch_id: str,
    search: str = "",
    reason: str = "",
) -> str:
    """
    Return the skip-reason category for a patch excluded in minimal_real mode.

    Returns one of:
      'skipped_library_rules'        – Lottie or miuix library patch
      'skipped_onetrack_delete_rules' – OneTrack class/method deletion
      'skipped_elite_flag_rules'     – references IS_ELITE_DEVELOPMENT_BUILD or 'elite'
      'dex_mtcr_broad_rules_skipped' – all other broad dex.mtcr-sourced rules
    """
    tc  = target_class.replace("\\", "/").lower()
    hay = (patch_id + search + reason).lower()

    if _LOTTIE_PKG in tc or _MIUIX_PKG in tc:
        return "skipped_library_rules"
    if _ONETRACK_PKG in tc:
        return "skipped_onetrack_delete_rules"
    for kw in _ELITE_KW:
        if kw.lower() in hay:
            return "skipped_elite_flag_rules"
    return "dex_mtcr_broad_rules_skipped"

