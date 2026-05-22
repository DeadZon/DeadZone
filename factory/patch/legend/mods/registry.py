"""
Legend mod registry — single source of truth for all Legend mods.

JAR mod groups (factory/patch/legend/mods/jars/<group>/<mod_name>/mod.py):
  framework      → framework.jar
  services       → services.jar
  miui_framework → miui-framework.jar
  miui_services  → miui-services.jar

APK mod groups (factory/patch/legend/mods/apk/<group>/runner.py):
  provision  → Provision.apk
  systemui   → MiuiSystemUI.apk
  powerkeeper → PowerKeeper.apk

Profiles:
  LEGEND_MINIMAL_REAL_PROFILE — sensible defaults, no opt-in-only mods
  LEGEND_FULL_PROFILE         — same, but opt-in mods explicitly enabled
"""
from __future__ import annotations

# ── Mod registry ──────────────────────────────────────────────────────────────

LEGEND_JAR_MODS: dict[str, list[str]] = {
    "framework": [
        "mezo_core",
        "kaorios_toolbox_v203",
        "signature_verification_bypass",
        "invoke_custom_handling",
    ],
    "services": [
        "volume_button_music_control",
        "signature_verification_bypass",
        "kaorios_toolbox_v203",
        "invoke_custom_handling",
    ],
    "miui_framework": [
        "mezo_core",
        "gboard_replace_baidu",
        "invoke_custom_handling",
    ],
    "miui_services": [
        "gboard_replace_baidu",
        "multi_floating_window",
        "process_control",
        "greeze_policy",
        "shortcut_settings_observer",
        "invoke_custom_handling",
    ],
}

# ── APK mod registry ─────────────────────────────────────────────────────────

LEGEND_APK_MODS: dict[str, list[str]] = {
    "provision": [
        "minimal_real",
        "gms_cn_fix",
        "branding",
    ],
    "systemui": [
        "miui_systemui_legend",
        "branding",
    ],
    "powerkeeper": [
        "exact_method_patches",
        "fps_lock",
        "gms_control",
    ],
}

# Flat set of all mod names — used for profile key validation.
ALL_MOD_NAMES: frozenset[str] = frozenset(
    mod for mods in LEGEND_JAR_MODS.values() for mod in mods
)

# ── Profiles ──────────────────────────────────────────────────────────────────

LEGEND_MINIMAL_REAL_PROFILE: dict[str, object] = {
    # On by default — safe, no user data risk
    "mezo_core":                        True,
    "volume_button_music_control":      True,
    "gboard_replace_baidu":             True,
    "multi_floating_window":            True,
    "freeform_max_count":               50,
    "invoke_custom_handling":           True,

    # Off by default — explicit opt-in required
    "kaorios_toolbox_v203":             False,
    "signature_verification_bypass":    False,

    # Off by default — stubs / future mods
    "process_control":                  False,
    "greeze_policy":                    False,
    "shortcut_settings_observer":       False,

    # Off by default — security sensitive
    "secure_screenshot_capture_bypass": False,
    "mock_location_unlock":             False,
    "crypto_biometric_patch":           False,
    "window_flags_mod":                 False,
}

LEGEND_FULL_PROFILE: dict[str, object] = {
    **LEGEND_MINIMAL_REAL_PROFILE,
    # Explicitly enabled in full profile
    "kaorios_toolbox_v203":          True,
    "signature_verification_bypass": True,
}

# Default profile used when caller passes None.
DEFAULT_PROFILE = LEGEND_MINIMAL_REAL_PROFILE


def merge_profile(user_overrides: dict | None) -> dict:
    """Merge user overrides onto the default profile."""
    merged = dict(DEFAULT_PROFILE)
    if user_overrides:
        merged.update(user_overrides)
    return merged
