# DeadZone Final ZIP Policy

## ROM Branding

- ROM name: **DeadZone**
- Developer: **MEZO Developer**
- No HyperUR, Elite, RIO, lcnguyn06, or any other developer/team name
  may appear in final ZIP filenames, flash script content, or any text file inside the ZIP.

## Flash Scripts

Three Windows flash scripts are included in every final ROM ZIP:

| Script | Purpose |
|---|---|
| `windows_install_upgrade.bat` | Flash ROM images, keep user data |
| `windows_install_and_format_data.bat` | Flash ROM images + erase metadata/userdata (clean install) |
| `windows_format_data_only.bat` | Erase metadata/userdata only, no image flashing |

### Script features

- ANSI colored output (Windows 10+)
- Reads ROM info from `images\DeadZone_firmware.txt`
- Checks required images before flashing
- Compares connected device codename against expected codename
- Skips optional images with `[SKIP]` log rather than failing
- **Never** erases FRP unless explicitly intended
- **Never** flashes MTK preloader by default (prints a warning)
- Stops on any required image flash failure

### Required images (checked before flash)

- `images\super.img`
- `images\boot.img`
- `images\init_boot.img`
- `images\vendor_boot.img`
- `images\vbmeta.img`

## ZIP Compression

Final public ROM ZIP uses `ZIP_DEFLATED` at `compresslevel=9`.

## Final ZIP Structure

```
DeadZone_<device>_<version>_<android>.zip
├── images/
│   ├── DeadZone_firmware.txt   (codename, device name, MI version, Android release)
│   ├── super.img
│   ├── boot.img
│   ├── init_boot.img
│   ├── vendor_boot.img
│   ├── vbmeta.img
│   └── <optional firmware images>
├── META-INF/
│   └── windows/
│       ├── fastboot.exe
│       └── <DLLs>
├── windows_install_upgrade.bat
├── windows_install_and_format_data.bat
└── windows_format_data_only.bat
```

Files that must **never** appear in the final ZIP:
- `HyperUR*.bat`
- `Elite*.bat`
- Log files or diagnostic ZIPs
- `_input_roms/` content
- GitHub workspace paths
- Telegram tokens or PixelDrain API keys

## Branding Validation

Before every PixelDrain upload, the workflow runs:

```bash
python -m factory.cli validate-final-zip --zip <final.zip>
python -m factory.cli inspect-zip --zip <final.zip>
```

Validation scans filenames and text files (`.bat`, `.cmd`, `.txt`, `.md`, `.xml`,
`.prop`, `.ini`, `.json`) for forbidden terms:
`HyperUR`, `hyperur`, `HYPERUR`, `Elite`, `elite`, `ELITE`,
`lcnguyn06`, `HassanMirz01`, `RIO`, `hyperur.io.vn`, `HyperUR_firmware.txt`.

If any violation is found, the build is marked as failed and PixelDrain upload is skipped.
The Telegram bot receives a failure notification.

## Upload Policy

- **PixelDrain** is the only public release channel (default: `upload_target=pixeldrain`).
- GitHub Actions artifacts are **disabled by default** (`upload_debug_artifacts=false`).
- Enable `upload_debug_artifacts=true` only when debugging a build failure.

See also: `docs/UPLOAD_POLICY.md`
