# EU Import — debloat_profiles (skeleton)

Source: `third_party/eu_reference/bin/package/DEBLOAT/`

Target partition: system, product
Action type: debloat
Risk: safe
Priority: 1

## Implementation plan (not yet implemented)

1. Parse DEBLOAT shell rm list into structured YAML:
   ```yaml
   debloat:
     - system/app/MiuiSuperMarket
     - product/app/MiShop
     # ...
   ```
2. Place YAML under this directory as `debloat_list.yml`
3. Register in patch.yml as debloat action
4. Cross-reference against target ROM app list to avoid removing required deps
5. Mark each entry with OS version applicability (OS3 / Universal)
