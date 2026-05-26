# EU Reference — NothingsVN Xiaomi AutoBuild

Reference copy of DeadZon/eu (NothingsVN Xiaomi AutoBuild) for mod analysis.

**DO NOT execute any scripts in this tree directly.**
All scripts are for reference/audit only. DeadZone factory runs its own pipeline.

## What is here

- `bin/modfile/` — OS-version mod trees (MIUI13, MIUI14, OS1, OS2, OS3, Universal)
- `bin/package/` — standalone patch packages (DEBLOAT, COREPATCH, etc.)
- `bin/ddevice/` — device identity / ROM metadata parsers
- `bin/script2flash/` — flash helpers (reference only, not used by DeadZone)

## What must never be imported

- `packROM.sh` lpmake sizing via `du -sb` — DeadZone uses payload_manifest sizes only
- `uploadROM.sh` super.img.zst + OneDrive logic
- Any eu workflow YAML into `.github/workflows/`

See `docs/eu_reference_audit.md` for the full porting guide.
