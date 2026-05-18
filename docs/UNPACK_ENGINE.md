# DeadZone Unpack Engine — Phase 1

**Stage**: Unpack only.  No patching, no repack, no final ZIP creation.

---

## Overview

Phase 1 extracts a source ROM archive, locates and unpacks dynamic partition
images, reads device metadata from `build.prop`, and writes a structured
report.  It is the foundation that downstream patch/repack stages will build on.

The unpack stage lives in **`factory/unpack/`** and delegates heavy extraction
work to the existing legacy engine in
`third_party/mezo_core/MEZOBuildRom.py` — it does **not** rewrite that logic.

---

## Module Map

```
factory/
├── core/
│   ├── context.py      BuildContext dataclass — paths + metadata for one session
│   └── reports.py      write_json_report / write_text_report helpers
└── unpack/
    ├── __init__.py
    ├── archive.py      ROM archive detection + extraction (stdlib only)
    ├── payload.py      payload.bin extraction (delegates to legacy)
    ├── super_image.py  find / unpack / extract super.img (delegates to legacy)
    ├── partitions.py   post-extraction partition + boot-image scanning
    ├── build_prop.py   pure build.prop reader — NO side effects, NO patching
    ├── report.py       01_unpack_report.json + 01_unpack_report.txt generation
    └── pipeline.py     orchestration + CLI entry point
```

---

## How to Run

```bash
python -m factory.unpack.pipeline \
    --rom  "path/to/rom.zip" \
    --device zircon \
    --soc mtk \
    --platform os3_a16
```

Or with an environment variable for device:

```bash
set DEADZONE_DEVICE_CODENAME=zircon
python -m factory.unpack.pipeline --rom "path/to/rom.zip"
```

Supported ROM input types:

| Extension          | Behaviour                              |
|--------------------|----------------------------------------|
| `.zip`             | ZipFile extraction                     |
| `.tar.gz` / `.tgz` | gzip-tar extraction (path-traversal safe) |
| `.tar`             | plain-tar extraction (path-traversal safe) |
| `.img` (super.img) | Used directly as super image           |
| directory          | Treated as pre-extracted project       |

---

## Extraction Flow

```
Input ROM
    │
    ▼
[archive.py] extract_rom()
    │
    ▼
[super_image.py] find_super_img()
    │
    ├── Found ──▶ [super_image.py] unpack_super_img()
    │                               │
    │                               ▼
    │             [super_image.py] extract_partitions()
    │
    └── Not found ──▶ [payload.py] find_payload_bin() / extract_from_payload()
                          │
                          ├── payload produced super.img ──▶ unpack as above
                          │
                          └── direct partition images ──▶ already in project_dir
    │
    ▼
[partitions.py] collect_extracted_partitions()
                collect_boot_images()
    │
    ▼
[build_prop.py] read_build_props()   ← PURE READ, no writes, no patches
    │
    ▼
[build_prop.py] resolve_effective_device()
    │
    ▼
[report.py] write_reports()
    ├── output/reports/01_unpack_report.json
    └── output/reports/01_unpack_report.txt
```

---

## Device Codename Resolution

Build.prop can return generic placeholder codenames such as:

- `mgvi_64_armv82`
- `generic`
- `qssi`
- `system`
- `unknown`

**Rule**: when the detected codename is in the `GENERIC_CODENAMES` set and
`DEADZONE_DEVICE_CODENAME` is set (or `--device` was passed), the factory
device takes precedence as the **effective device**.

When `--device` is supplied for a real codename from build.prop, the flag
still wins (the operator knows the target device better than the ROM).

The decision and reason string are recorded in the report under
`effective_device`.

---

## Report Format

### JSON (`01_unpack_report.json`)

```json
{
  "input_rom": "/abs/path/to/rom.zip",
  "archive_type": "zip",
  "payload_found": false,
  "super_found": true,
  "partitions_extracted": ["odm", "product", "system", "system_ext", "vendor"],
  "boot_images_found": ["boot.img", "dtbo.img", "vbmeta.img"],
  "build_prop_device": "zircon",
  "factory_device": "zircon",
  "effective_device": "zircon",
  "android_version": "16",
  "mi_version": "OS3.0.1.0.VNACNXM",
  "warnings": [],
  "errors": [],
  "paths": {
    "root_dir": "...",
    "work_dir": "...",
    "project_dir": "...",
    "output_dir": "...",
    "reports_dir": "..."
  }
}
```

### Text (`01_unpack_report.txt`)

```
DeadZone Unpack Report
======================
Input ROM:           /abs/path/to/rom.zip
Archive type:        zip
Payload found:       no
Super found:         yes

Partitions extracted:
  - odm
  - product
  - system
  - system_ext
  - vendor

Boot images found:
  - boot.img
  - dtbo.img
  - vbmeta.img

Build.prop device:   zircon
Factory device:      zircon
Effective device:    zircon
Android:             16
MI version:          OS3.0.1.0.VNACNXM

Warnings:
  (none)

Errors:
  (none)
```

---

## Legacy Code Provenance

| New module                  | Legacy source                                        |
|-----------------------------|------------------------------------------------------|
| `archive.extract_tar_safe`  | MEZOBuildRom.py lines 133–139                        |
| `archive.extract_rom`       | MEZOBuildRom.py lines 142–166                        |
| `super_image.find_super_img`| MEZOBuildRom.py lines 266–283                        |
| `super_image.unpack_super_img` | delegates → MEZOBuildRom.unpack_super (6457–6468) |
| `super_image.extract_partitions` | delegates → MEZOBuildRom.extract_partitions_from_super (6661–6677) |
| `payload.extract_from_payload` | delegates → MEZOBuildRom.try_extract_super_from_payload (286–414) |
| `build_prop.parse_build_prop` | MEZOBuildRom.py lines 417–436                      |
| `build_prop.BUILD_PROP_KEYS`  | MEZOBuildRom.py lines 44–51                        |

Functions marked "delegates" import and call the legacy implementation at
runtime via a lazy import helper in `payload._legacy()`.  This avoids code
duplication while preserving identical behaviour.

---

## What Phase 1 Does NOT Touch

- APK decompile / recompile
- JAR / DEX patching
- Smali patching
- Signature verification bypass
- FLAG_SECURE disable
- vbmeta patching
- EROFS repack
- lpmake / super.img rebuild
- Final ZIP creation
- Telegram / PixelDrain upload

All of the above remain solely in `MEZOBuildRom.py` and are invoked by the
existing `factory run-mezo` command.

---

## Safety Notes

- `MEZOBuildRom.py` is **not modified** by Phase 1.
- All paths in `BuildContext` are absolute — safe across `os.chdir()` calls.
- Tar extraction uses `extract_tar_safe()` which validates every member path
  against the destination root (prevents path-traversal attacks).
- No patch function is called during the unpack stage.
