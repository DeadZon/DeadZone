# EU Reference — package/DISABLE_AVB
# Category: package_patch | Action: fstab_patch | Risk: high
# Disables AVB verification in fstab. NEVER import the fstab logic into DeadZone.
# DeadZone handles vbmeta via its own vbmeta_legacy flow, not fstab patching.
# DO NOT execute directly.
