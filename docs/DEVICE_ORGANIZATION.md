# DeadZone Device Organization

## Design Principle

`third_party/mezo_core/SuperConfig/` is the build engine's data store — it is **never modified** by the factory layer.

`registry/` is the factory selection layer. It describes which devices are ready to build, what their SoC is, and which workflow panel they belong to.

---

## Layer Separation

```
third_party/mezo_core/SuperConfig/<codename>/   ← engine data (read-only)
registry/devices/<soc>/<codename>.yml           ← factory device config
registry/device_groups/<soc>.yml                ← panel device list
.github/workflows/deadzone_snapdragon.yml       ← Snapdragon UI panel
.github/workflows/deadzone_mtk.yml              ← MTK UI panel
```

---

## Panel Structure

Each SoC has its own GitHub Actions workflow so device choices stay clean and SoC is never user-selectable — it is hardcoded per panel.

| Panel | Workflow | SoC passed |
|---|---|---|
| DeadZone Snapdragon Factory | `deadzone_snapdragon.yml` | `--soc snapdragon` (always) |
| DeadZone MTK Factory | `deadzone_mtk.yml` | `--soc mtk` (always) |

---

## Device Choice Format

Devices appear in workflow dropdowns as:

```
codename | Device Marketing Name
```

Example:
```
garnet | Redmi Note 13 Pro 5G
zircon | Redmi Note 13 Pro+ 5G
```

### How the codename is parsed

The workflow strips everything after ` | ` before passing to the factory CLI:

```bash
RAW_DEVICE="${{ inputs.device }}"
DEVICE="${RAW_DEVICE%% | *}"
# DEVICE = "garnet"

python -m factory.cli plan --device "$DEVICE" --soc snapdragon ...
```

The factory CLI receives only the codename. It never sees the marketing name.

---

## Device Status Values

| Status | Meaning | Appears in panel? |
|---|---|---|
| `golden` | Primary golden device — fully tested | Yes |
| `ready` | Registry confirmed, SoC confirmed | Yes |
| `todo` | Needs work before adding to panel | No |
| `unknown` | SoC or name not confirmed | No |

Only `golden` and `ready` devices are added to workflow options.

---

## Unknown Devices

Devices found in SuperConfig but not yet classified go to:

```
docs/DEVICE_CLASSIFICATION_TODO.md
```

Unknown devices are **not a failure** — they are documented and left for later confirmation. Do not guess SoC classifications.

---

## How to Add a New Device

Follow this order strictly:

1. **Confirm SoC** — Snapdragon or MTK. Do not guess.
2. **Confirm marketing name** — use official Xiaomi/Redmi branding.
3. **Create registry device file**
   ```
   registry/devices/<soc>/<codename>.yml
   ```
4. **Add to device group**
   ```
   registry/device_groups/<soc>.yml
   ```
   with `status: ready`.
5. **Add to panel workflow options**
   ```
   "codename | Marketing Name"
   ```
6. **Test plan command** (no real build needed):
   ```bash
   python -m factory.cli plan --device <codename> --soc <soc> --platform os3_a16 --flavor deadzone
   ```
7. **Run validate-registry** to confirm everything passes:
   ```bash
   python -m factory.cli validate-registry
   ```

---

## Current Live Devices

### Snapdragon Panel

| Codename | Device | SuperConfig | Status |
|---|---|---|---|
| garnet | Redmi Note 13 Pro 5G | yes | ready |

### MTK Panel

| Codename | Device | SuperConfig | Status |
|---|---|---|---|
| zircon | Redmi Note 13 Pro+ 5G | no (manual) | golden |

---

## Classification Report

Run to update `docs/DEVICE_CLASSIFICATION_TODO.md`:

```bash
python -m factory.tools.scan_superconfig_devices --write-doc
```

This scans all 71 SuperConfig device folders and cross-checks them against registry and device_group files. It does not modify SuperConfig.
