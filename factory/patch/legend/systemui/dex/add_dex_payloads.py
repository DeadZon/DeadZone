"""
Legend MiuiSystemUI DEX payload rules.

Declares managed factory assets for classes2.dex, classes3.dex, classes4.dex.
These dex files contain added classes that are merged into the APK as new
smali_classesN roots during build.

Runtime behavior:
  1. Detect existing smali roots in the decompiled APK workspace.
  2. For each payload, decode dex → smali using baksmali.
  3. Place decoded smali into the next available smali_classesN root.
  4. APKEditor rebuild auto-generates classesN.dex from each smali root.

Do NOT copy raw .dex files into the APK manually.
"""
from __future__ import annotations
from pathlib import Path

TARGET_APK = 'MiuiSystemUI.apk'

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parents[5]

ASSETS_DEX_DIR = _REPO_ROOT / 'factory' / 'assets' / 'legend' / 'systemui' / 'dex'

DEX_PAYLOADS = [
    {
        'name':        'classes2.dex',
        'asset_path':  ASSETS_DEX_DIR / 'classes2.dex',
        'smali_group': 'classes2',
        'size_bytes':  240740,
        'required':    True,
        'reason':      'Legend MiuiSystemUI managed dex payload',
    },
    {
        'name':        'classes3.dex',
        'asset_path':  ASSETS_DEX_DIR / 'classes3.dex',
        'smali_group': 'classes3',
        'size_bytes':  25824,
        'required':    True,
        'reason':      'Legend MiuiSystemUI managed dex payload',
    },
    {
        'name':        'classes4.dex',
        'asset_path':  ASSETS_DEX_DIR / 'classes4.dex',
        'smali_group': 'classes4',
        'size_bytes':  72932,
        'required':    True,
        'reason':      'Legend MiuiSystemUI managed dex payload',
    },
]

# These packages are introduced by the dex payloads.
# Used for reporting and validation.
PAYLOAD_PACKAGE_GROUPS = {
    'classes2': ['com/android/systemui'],
    'classes3': ['com/justas', 'com/miui/charge', 'com/miui/systemui'],
    'classes4': ['bg/mods'],
}
