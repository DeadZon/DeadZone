# DeadZone Device Organization

## Design Principle

`third_party/mezo_core/SuperConfig/` is the **source of truth** for working build configs.
It is never modified by the factory layer.

`registry/device_groups/` is only a selection/organization layer. All SuperConfig devices
are treated as working and ready for builds. Full `registry/devices/<soc>/<codename>.yml`
files are only required for golden or manually managed devices.

---

## Layer Separation

```
third_party/mezo_core/SuperConfig/<codename>/   <- engine data (read-only, source of truth)
registry/devices/<soc>/<codename>.yml           <- full device config (golden devices only)
registry/device_groups/<soc>.yml                <- panel device list (all devices)
.github/workflows/deadzone_snapdragon.yml       <- Snapdragon UI panel
.github/workflows/deadzone_mtk.yml              <- MTK UI panel
```

---

## Panel Structure

Each SoC has its own GitHub Actions workflow. SoC is never a user input — it is hardcoded
per panel so device choices stay clean and unambiguous.

| Panel | Workflow | SoC | Devices |
|---|---|---|---|
| DeadZone Snapdragon Factory | `deadzone_snapdragon.yml` | `--soc snapdragon` (always) | 67 |
| DeadZone MTK Factory | `deadzone_mtk.yml` | `--soc mtk` (always) | 5 |

---

## Device Choice Format

Devices appear in workflow dropdowns as:

```
codename | Device Marketing Name
```

Examples:
```
garnet | Redmi Note 13 Pro 5G / POCO X6 5G
zircon | Redmi Note 13 Pro+ 5G
agate  | Xiaomi 11T
```

### How the codename is parsed

The workflow strips the marketing name before passing to the factory CLI:

```bash
RAW_DEVICE="${{ inputs.device }}"
DEVICE="${RAW_DEVICE%% | *}"
# DEVICE = "garnet"

python -m factory.cli plan --device "$DEVICE" --soc snapdragon ...
```

The factory CLI only receives the codename — never the marketing name string.

---

## Device Status Values

| Status | Meaning | Appears in panel? |
|---|---|---|
| `golden` | Primary golden device — fully tested, has full registry YAML | Yes |
| `ready` | SuperConfig source confirmed, added to panel | Yes |
| `todo` | Not ready yet | No |
| `unknown` | Unclassified | No |

---

## SuperConfig Devices vs Full Registry Files

SuperConfig devices (`source: superconfig`) use:
- `registry/device_groups/<soc>.yml` entry for name and panel display
- `third_party/mezo_core/SuperConfig/<codename>/` for build data (unchanged)
- SoC defaults for flash profile, vbmeta policy, required images

Full registry device files (`registry/devices/<soc>/<codename>.yml`) exist only for:
- `garnet` (Snapdragon golden)
- `zircon` (MTK manual golden)

Adding a full registry file is optional and only needed for per-device customization.

---

## Current Device Counts

| Group | SuperConfig devices | Manual | Total |
|---|---|---|---|
| Snapdragon | 67 | 0 | 67 |
| MTK | 4 | 1 (zircon) | 5 |
| **Total** | **71** | **1** | **72** |

---

## Validation and Sync Tools

```bash
# Validate full registry (SOC + platforms + flavors + golden devices + device_groups + SuperConfig coverage)
python -m factory.cli validate-registry

# Check that every SuperConfig folder is assigned to exactly one panel
python factory/tools/sync_device_panels_from_superconfig.py --check

# Show build plan for any device (works with or without a full registry YAML)
python -m factory.cli plan --device <codename> --soc <soc> --platform os3_a16 --flavor deadzone
```

---

## How to Add a New Device

1. **Confirm SoC** (Snapdragon or MTK) — do not guess.
2. **Confirm marketing name** — use official branding.
3. **Add to device_groups YAML** (`registry/device_groups/<soc>.yml`), `status: ready`.
4. **Add option to workflow** (`deadzone_snapdragon.yml` or `deadzone_mtk.yml`).
5. **Verify**: `python factory/tools/sync_device_panels_from_superconfig.py --check`
6. **Validate**: `python -m factory.cli validate-registry`
7. **Test plan**: `python -m factory.cli plan --device <codename> --soc <soc> --platform os3_a16 --flavor deadzone`

Full `registry/devices/<soc>/<codename>.yml` is optional — create it only when doing
advanced per-device config or when the device becomes a priority build target.
