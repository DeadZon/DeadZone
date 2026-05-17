# DeadZone ROM Factory — Architecture

## Design Principle

This is **not a rewrite**. The existing MEZO engine (`third_party/mezo_core/MEZOBuildRom.py`) remains the build engine. The `factory/` layer orchestrates it without touching it.

```
MEZOBuildRom.py  →  actual ROM build engine (unchanged)
factory/         →  build controller / orchestration
registry/        →  device, SoC, platform, flavor definitions
patchpacks/      →  scalable ROM modifications
templates/       →  generated fastboot scripts
validators/      →  safety gates
queues/          →  mass-build input definitions
```

---

## Directory Map

### `third_party/mezo_core/`
Current working MEZO build engine. **Never modified by the factory layer.**
- `MEZOBuildRom.py` — entry point called by `mezo_legacy_engine.py`
- `SuperConfig/` — super partition configuration
- `bin/` — build tools
- `flash/` — legacy flash scripts (referenced by SoC registry)
- `assets_manifest/` — MEZO app asset list

### `factory/`
Python orchestration layer. Does not contain build logic.

| Module | Responsibility |
|---|---|
| `cli.py` | CLI entry point (`python -m factory.cli`) |
| `core/paths.py` | Resolves REPO_ROOT, REGISTRY_ROOT, MEZO_CORE paths |
| `core/build_plan.py` | Loads registry configs and prints a build plan |
| `engines/mezo_legacy_engine.py` | Calls MEZOBuildRom.py via subprocess |
| `adapters/mezo_output_adapter.py` | Collects MEZO output into normalized output/ structure |
| `validators/validate_registry.py` | Validates all registry YAML files |
| `validators/validate_public_zip.py` | Validates a public ROM ZIP before release |

### `registry/`
YAML config files. Defines what exists — not how to build.

```
registry/
├── soc/           # SoC track definitions (snapdragon, mtk)
├── platforms/     # Android version / ROM family (miui_a13 … os3_a16)
├── flavors/       # ROM flavor variants (deadzone, gaming, epic, legend)
└── devices/       # Per-device config, grouped by SoC track
    ├── snapdragon/
    └── mtk/
```

### `patchpacks/`
Scalable ROM modification packs. Applied by the factory pipeline after base build.
Organized by scope: `common/`, `soc/`, `platforms/`, `flavors/`.

### `templates/`
Jinja2 templates for generating fastboot flash scripts and release notes.

### `queues/`
JSON files defining mass-build inputs. Each entry specifies device + soc + platform + flavor + rom_url.

### `assets/`
Asset manifests and download scripts. `assets/cache/` is git-ignored.

### `output/`
Git-ignored. Contains build artifacts, images, logs. Never committed.

---

## SoC Tracks

| ID | Name | Default Engine | Legacy Flash |
|---|---|---|---|
| `snapdragon` | Qualcomm Snapdragon | `snapdragon_engine` (→ mezo_legacy) | `HyperUR Flash_2.bat` |
| `mtk` | MediaTek | `mtk_engine` (→ mezo_legacy) | `HyperUR Flash MTK.bat` |

---

## Platform Targets

| ID | Name | Android | Super FS |
|---|---|---|---|
| `miui_a13` | MIUI Android 13 | 13 | ext4 |
| `os1_a13` | HyperOS 1 Android 13 | 13 | ext4 |
| `os1_a14` | HyperOS 1 Android 14 | 14 | erofs |
| `os2_a14` | HyperOS 2 Android 14 | 14 | erofs |
| `os2_a15` | HyperOS 2 Android 15 | 15 | erofs |
| `os3_a15` | HyperOS 3 Android 15 | 15 | erofs |
| `os3_a16` | HyperOS 3 Android 16 | 16 | erofs |

---

## ROM Flavors

| ID | Name | Inherits |
|---|---|---|
| `deadzone` | DeadZone | — |
| `deadzone_gaming` | DeadZone Gaming | deadzone |
| `deadzone_epic` | DeadZone EPiC | deadzone |
| `deadzone_legend` | DeadZone Legend | deadzone |

---

## Golden Devices (Phase 1)

| Codename | Brand/Model | SoC | Default Platform |
|---|---|---|---|
| `garnet` | Redmi Note 13 Pro 5G | Snapdragon | os3_a16 |
| `zircon` | Redmi Note 13 Pro+ 5G | MTK | os3_a16 |

---

## Phase Expansion Order

```
Phase 1:  garnet + zircon, deadzone flavor, os3_a16
Phase 2:  deadzone_gaming, deadzone_epic, deadzone_legend
Phase 3:  os2_a15, os3_a15, os2_a14, os1_a14, os1_a13, miui_a13
Phase 4+: additional devices
```
