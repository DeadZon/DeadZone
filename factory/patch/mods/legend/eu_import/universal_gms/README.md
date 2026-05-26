# EU Import — universal_gms (skeleton)

Sources from eu reference:
- `third_party/eu_reference/bin/modfile/Universal/gmsservices/`
- `third_party/eu_reference/bin/modfile/Universal/privapp_whitelist_hyperos.xml`

Target partitions: system (permissions), product (GMS APKs)
Action type: file_copy
Risk: safe
Priority: 1

## Implementation plan (not yet implemented)

1. Copy `privapp_whitelist_hyperos.xml` -> `/system/etc/permissions/`
2. Enumerate GMS service APKs from `Universal/gmsservices/`
3. Copy APKs to `/product/priv-app/` matching ROM's product manifest entries
4. Register in patch.yml as `file_copy` actions
5. Add to `factory/patch/mods/legend/actions/run_legend.py` as optional module
