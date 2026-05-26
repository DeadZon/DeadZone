# EU Import — Skeleton Modules

Skeleton stubs for mods ported from DeadZon/eu (NothingsVN Xiaomi AutoBuild).
No mod logic is implemented here yet. Each subdirectory is a placeholder
for a future DeadZone patch.yml module.

Reference material: `third_party/eu_reference/`
Audit guide: `docs/eu_reference_audit.md`
Migration plan: `output/reports/eu_migration_plan.json`

## Status

| Module | EU source | Status |
|--------|-----------|--------|
| `universal_gms/` | Universal/gmsservices + privapp_whitelist_hyperos.xml | skeleton |
| `notification_fix/` | package/NOTIFICATION_FIX | skeleton |
| `refresh_rate/` | package/RefreshRate | skeleton |
| `debloat_profiles/` | package/DEBLOAT | skeleton |

## Rules

- Do NOT call any script from `third_party/eu_reference/` directly.
- All mod logic must be implemented as DeadZone patch.yml modules.
- Run `python scripts/validate_eu_reference.py` before committing any module here.
