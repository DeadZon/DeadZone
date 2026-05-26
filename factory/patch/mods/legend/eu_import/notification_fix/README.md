# EU Import — notification_fix (skeleton)

Source: `third_party/eu_reference/bin/package/NOTIFICATION_FIX/`

Target partition: system
Action type: prop_patch or smali_patch
Risk: safe
Priority: 1

## Implementation plan (not yet implemented)

1. Audit NOTIFICATION_FIX for prop vs smali changes
2. For prop changes: extract key=value pairs -> DeadZone build_prop patcher
3. For smali changes: identify target class + method -> smali_tools patch
4. Register in patch.yml
5. Validate on a real ROM before enabling by default
