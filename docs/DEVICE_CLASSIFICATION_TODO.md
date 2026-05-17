# Device Classification TODO

Updated after full SuperConfig device assignment.

## Status

All current SuperConfig devices have been assigned to Snapdragon or MTK panels.

```
Total SuperConfig devices      : 71
Snapdragon SuperConfig devices : 67
MTK SuperConfig devices        : 4
Manual MTK golden devices      : 1  (zircon — not in SuperConfig)
Total MTK panel devices        : 5
```

Verify at any time:

```bash
python factory/tools/sync_device_panels_from_superconfig.py --check
python -m factory.cli validate-registry
```

---

## Snapdragon Panel (67 SuperConfig devices)

| Codename | Device | Registry File |
|---|---|---|
| amethyst | Redmi Note 14 Pro+ 5G | null |
| aurora | Xiaomi 14 Ultra | null |
| babylon | Xiaomi MIX Fold 3 | null |
| breeze | Redmi 13 5G / Redmi Note 13R / POCO M6 Plus 5G | null |
| chenfeng | Xiaomi Civi 4 Pro | null |
| cupid | Xiaomi 12 | null |
| dada | Xiaomi 15 | null |
| dagu | Xiaomi Pad 5 Pro 12.4 | null |
| diting | Xiaomi 12T Pro / Redmi K50 Ultra | null |
| dizi | Redmi Pad Pro | null |
| flame | Redmi 14R 5G / Redmi 14C 5G / POCO M7 5G | null |
| fuxi | Xiaomi 13 | null |
| **garnet** | **Redmi Note 13 Pro 5G / POCO X6 5G** | **registry/devices/snapdragon/garnet.yml** |
| goku | Xiaomi MIX Fold 4 | null |
| haotian | Xiaomi 15 Pro | null |
| haydn | Redmi K40 Pro / K40 Pro+ / Mi 11i | null |
| houji | Xiaomi 14 | null |
| ingres | Redmi K50 Gaming / POCO F4 GT | null |
| ishtar | Xiaomi 13 Ultra | null |
| lisa | Xiaomi 11 Lite 5G NE | null |
| liuqin | Xiaomi Pad 6 Pro | null |
| marble | Redmi Note 12 Turbo / POCO F5 | null |
| mayfly | Xiaomi 12S | null |
| miro | Redmi K80 Pro / POCO F7 Ultra | null |
| mondrian | Redmi K60 / POCO F5 Pro | null |
| moonstone | POCO X5 5G | null |
| munch | Redmi K40S / POCO F4 | null |
| muyu | Xiaomi Pad 7 Pro | null |
| myron | Redmi K90 Pro Max / POCO F8 Ultra | null |
| nezha | Xiaomi 17 Ultra | null |
| nuwa | Xiaomi 13 Pro | null |
| odin | Xiaomi MIX 4 | null |
| onyx | Redmi Turbo 4 Pro / POCO F7 | null |
| pandora | Xiaomi 17 Pro | null |
| peridot | Redmi Turbo 3 / POCO F6 | null |
| piano | Xiaomi Pad 8 Pro | null |
| pipa | Xiaomi Pad 6 | null |
| popsicle | Xiaomi 17 Pro Max | null |
| pudding | Xiaomi 17 | null |
| redwood | Redmi Note 12 Pro Speed / POCO X5 Pro 5G | null |
| ruan | Redmi Pad Pro 5G / POCO Pad 5G | null |
| sapphire | Redmi Note 13 4G | null |
| sapphiren | Redmi Note 13 4G NFC | null |
| sheng | Xiaomi Pad 6S Pro 12.4 | null |
| shennong | Xiaomi 14 Pro | null |
| sky | Redmi 12 5G / Redmi Note 12R / POCO M6 Pro 5G | null |
| socrates | Redmi K60 Pro | null |
| star | Xiaomi Mi 11 Ultra | null |
| sunstone | Redmi Note 12 5G / Redmi Note 12R Pro | null |
| taoyao | Xiaomi 12 Lite 5G | null |
| tapas | Redmi Note 12 4G | null |
| thor | Xiaomi 12S Ultra | null |
| topaz | Redmi Note 12 4G NFC | null |
| uke | Xiaomi Pad 7 | null |
| unicorn | Xiaomi 12S Pro | null |
| venus | Xiaomi Mi 11 | null |
| vermeer | Redmi K70 | null |
| vili | Xiaomi 11T Pro | null |
| xuanyuan | Xiaomi 15 Ultra | null |
| xun | Redmi Pad SE | null |
| yudi | Xiaomi Pad 6 Max 14 | null |
| yupei | Xiaomi Pad 8 | null |
| zeus | Xiaomi 12 Pro | null |
| zijin | Xiaomi Civi 1S | null |
| ziyi | Xiaomi 13 Lite / Xiaomi Civi 2 | null |
| zizhan | Xiaomi MIX Fold 2 | null |
| zorn | Redmi K80 / POCO F7 Pro | null |

---

## MTK Panel (4 SuperConfig + 1 manual golden)

| Codename | Device | Source | Registry File |
|---|---|---|---|
| agate | Xiaomi 11T | SuperConfig | null |
| aristotle | Xiaomi 13T | SuperConfig | null |
| daumier | Xiaomi 12 Pro Dimensity Edition | SuperConfig | null |
| plato | Xiaomi 12T | SuperConfig | null |
| **zircon** | **Redmi Note 13 Pro+ 5G** | **manual/golden** | **registry/devices/mtk/zircon.yml** |

---

## Adding Full Registry Files

A full `registry/devices/<soc>/<codename>.yml` is only needed for advanced per-device
customization (flash profile, vbmeta policy, image list overrides). For all other devices,
the device_groups entry + SuperConfig is sufficient to run a build.

Priority: garnet (done), zircon (done). Create new ones only when actively tested.

---

## How to Add a New SuperConfig Device

1. Add folder appears in `third_party/mezo_core/SuperConfig/<codename>/`.
2. Confirm SoC — do not guess.
3. Add entry to `registry/device_groups/<soc>.yml`.
4. Add option to `deadzone_snapdragon.yml` or `deadzone_mtk.yml`.
5. Run `python factory/tools/sync_device_panels_from_superconfig.py --check`.
6. Run `python -m factory.cli validate-registry`.
