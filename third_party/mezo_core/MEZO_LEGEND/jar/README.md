# MEZO_LEGEND — JAR Patch Packs

This is the **canonical** location for Legend-flavor MTCR patch files.

## File naming

| MTCR filename                  | Target JAR                              |
|--------------------------------|-----------------------------------------|
| `Framework_Legend.mtcr`        | `system/framework/framework.jar`        |
| `Service_Legend.mtcr`          | `system/framework/services.jar`         |
| `miui-framework_Legend.mtcr`   | `system_ext/framework/miui-framework.jar` |
| `miui-services_Legend.mtcr`    | `system_ext/framework/miui-services.jar`|

## Fallback location

The engine also accepts MTCR files from `Legend/jar/` at the repo root.
Place files here (canonical) to take priority; the fallback is kept for
backwards compatibility during migration.

## Adding a new Legend JAR patch

1. Place `<Name>_Legend.mtcr` in this directory.
2. Add a `LegendJarRule` entry in `factory/patch/legend/jar_rules.py`.
3. Run: `python -m factory.patch.legend.jar_patch --project <dir> --flavor legend`
   (dry-run by default) to verify classes are found.
4. Add `--execute` to apply.

## MTCR format

An MTCR file is a ZIP archive containing:
- `a/<class_path>` — original smali (no .smali extension)
- `b/<class_path>` — modified / new smali
- `info.json`       — metadata (paths, tool settings)

Classes in `b/` but not `a/` are treated as **added** (injected into the jar).
Classes in both `a/` and `b/` are treated as **modified** (replaced in the jar).
