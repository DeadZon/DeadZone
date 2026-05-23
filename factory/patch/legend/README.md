# DeadZone Legend — Self-Contained Mod

`factory/patch/legend/` is the **only active home** for all DeadZone Legend
patch logic, assets, actions, patchers, reports, and validators.

## Layout

```
factory/patch/legend/
├── runner.py                 ← ONLY entrypoint: run_legend(root, ...)
├── manifest.yml              ← mod metadata
├── __init__.py
├── actions/
│   ├── run_legend.py         ← thin CI/workflow action launcher
│   ├── validate_legend_home.py ← single-home enforcement scanner
│   └── report_legend.py      ← report viewer
├── patchers/
│   ├── fstab_patcher.py      ← fstab: AVB removal, overlays, miui_dlkm removal
│   ├── props_patcher.py      ← build.prop patches (extend as needed)
│   ├── apk_patcher.py        ← Provision, SystemUI, PowerKeeper APK patches
│   ├── jar_patcher.py        ← delegates to mtcr/runner.py
│   ├── systemui_resources.py ← assets root resolver for SystemUI
│   └── permissions_patcher.py ← permissions XML patches (extend as needed)
├── mtcr/
│   ├── runner.py             ← MTCR class/method-level JAR runner
│   └── smart_smali_patcher.py
├── mods/
│   ├── registry.py           ← mod config registry
│   ├── jars/                 ← per-JAR class/method patch modules
│   └── apk/                  ← per-APK patch runners (systemui, powerkeeper, provision)
├── assets/
│   ├── systemui/             ← SystemUI drawables, DEX payloads, resources
│   ├── jar/                  ← DEX payloads for JAR injection
│   ├── apk/
│   ├── product/
│   ├── system/
│   ├── system_ext/
│   └── mi_ext/
├── reports/
│   └── writer.py             ← unified report writer → output/reports/deadzone_patch_report.txt
└── archived_legacy/
    └── README.md             ← dead archive, nothing executes from here
```

## Single entrypoint

```python
from factory.patch.legend.runner import run_legend

report = run_legend(
    root=Path("/path/to/unpacked_rom"),
    context={"flavor": "legend", "execute": True},
)
```

Pipeline steps (in order):
1. Validate single Legend home
2. Patch fstab (AVB removal, overlay injection, miui_dlkm removal)
3. Patch props
4. Apply APK mods (Provision, SystemUI, PowerKeeper)
5. Apply JAR mods via MTCR runner
6. Validate SystemUI assets
7. Patch permissions

All steps report to: `output/reports/deadzone_patch_report.txt`

## GitHub Actions workflows

Workflow YAML files live in `.github/workflows/` because GitHub requires it.
They are **thin launchers only** — they call the factory orchestrator or this
module's action entrypoint. They contain no Legend patch logic.

To call Legend from a workflow step:
```yaml
- run: python -m factory.patch.legend.actions.run_legend \
         --project "${{ env.PROJECT_DIR }}" \
         --flavor legend \
         --execute
```

## Registry

`registry/flavors/deadzone_legend.yml` is **metadata only**.
It declares the runner module path but contains no patch logic or asset paths.

## Assets

All Legend assets live in `factory/patch/legend/assets/`.
Previously at `factory/assets/legend/` — that path is now retired.

## fstab patcher

`patchers/fstab_patcher.py` patches `vendor/etc/fstab.emmc` and
`vendor/etc/fstab.mt6886`:

- Removes AVB flags (`avb`, `avb=vbmeta`, `avb=vbmeta_system`, `avb_keys=...`)
  from dynamic partition mount lines only.
- Adds mi_ext / pangu overlay lines after the mi_ext bind mount if absent.
- **Removes all `miui_dlkm` lines** — DeadZone Legend does not use miui_dlkm.
  Leaving those lines causes boot failure when miui_dlkm is absent from super.img.
- Creates `.dzlegend.bak` backups (skipped if backup already exists).

## archived_legacy

`archived_legacy/` is a dead archive. Nothing imports or executes from it.
It exists only for historical reference.

## Future mods

The factory is designed for sibling mod packages:
- `factory/patch/gaming/`
- `factory/patch/epic/`
- `factory/patch/base/`

Each mod owns its own `runner.py`, `assets/`, `patchers/`, etc.
Legend logic does not bleed into those namespaces.
