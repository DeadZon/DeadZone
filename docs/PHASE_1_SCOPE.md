# Phase 1 Scope

Phase 1 establishes the factory skeleton and validates it with two golden devices.
No real ROM build is required to complete Phase 1.

## Acceptance Criteria

- [x] `registry/soc/` — snapdragon.yml, mtk.yml
- [x] `registry/platforms/` — 7 platform files (miui_a13 … os3_a16)
- [x] `registry/flavors/` — 4 flavor files (deadzone, gaming, epic, legend)
- [x] `registry/devices/snapdragon/garnet.yml`
- [x] `registry/devices/mtk/zircon.yml`
- [x] `queues/test_dual_soc.json` — garnet + zircon entries
- [x] `factory/cli.py` — plan, validate-registry, validate-zip, run-mezo commands
- [x] `factory/engines/mezo_legacy_engine.py` — subprocess wrapper (dry-run safe)
- [x] `factory/validators/validate_registry.py` — registry checks
- [x] `factory/validators/validate_public_zip.py` — ZIP safety checks
- [x] `.github/workflows/mezo_build.yml` preserved (not removed)
- [x] `.gitignore` blocks output/, cache/, ROM binaries
- [x] `docs/FACTORY_ARCHITECTURE.md` explains the design

## CLI Commands (Phase 1)

```bash
# Validate all registry files
python -m factory.cli validate-registry

# Show build plan (no build)
python -m factory.cli plan --device garnet --soc snapdragon --platform os3_a16 --flavor deadzone
python -m factory.cli plan --device zircon  --soc mtk        --platform os3_a16 --flavor deadzone

# Dry-run MEZO engine call (shows what would run)
python -m factory.cli run-mezo --rom path/to/rom.zip --device zircon --soc mtk --platform os3_a16 --flavor deadzone

# Actually run MEZO (only when ROM is ready)
python -m factory.cli run-mezo --rom path/to/rom.zip --device zircon --soc mtk --platform os3_a16 --flavor deadzone --execute

# Validate a finished public ZIP before release
python -m factory.cli validate-zip --zip DeadZone_zircon_os3_a16_fastboot.zip
```

## What Phase 1 Does NOT Include

- No actual ROM build is triggered
- No patchpack application logic
- No template rendering
- No GitHub Actions mass-build matrix
- No additional devices beyond garnet and zircon
- No release uploader
