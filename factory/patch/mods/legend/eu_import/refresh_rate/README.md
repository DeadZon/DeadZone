# EU Import — refresh_rate (skeleton)

Source: `third_party/eu_reference/bin/package/RefreshRate/`

Target partition: system (build.prop / display config overlay)
Action type: prop_patch
Risk: safe
Priority: 1

## Implementation plan (not yet implemented)

1. Extract property keys from RefreshRate (e.g. ro.surface_flinger.max_frame_buffer_acquired_buffers,
   persist.sys.miui_optimization, display.max_refresh_rate, etc.)
2. Add entries to DeadZone build_prop patcher config
3. Register in patch.yml as prop_patch
4. Verify refresh rate unlocks correctly on target device; check for SafetyNet impact
