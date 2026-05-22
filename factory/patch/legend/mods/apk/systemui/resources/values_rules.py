"""
Legend MiuiSystemUI add/ resource values rules.

Points to managed factory assets at:
  factory/assets/legend/systemui/resources/com.android.systemui/

Runner merges all XML files from this asset path into the decompiled APK
using the same logic as the original apply_add_resources().

Total XML files : 224
  array       : 50
  bool        : 2
  dimen       : 1
  integer     : 1
  plurals     : 50
  string      : 120
"""
from __future__ import annotations
from pathlib import Path

TARGET_APK = 'MiuiSystemUI.apk'

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parents[4]

# Managed asset root — do NOT read from Legend/ at runtime
ASSETS_ROOT = _REPO_ROOT / 'factory' / 'assets' / 'legend' / 'systemui' / 'resources'
ADD_RESOURCES_SRC = ASSETS_ROOT / 'com.android.systemui'

RESOURCE_TYPES = ['array', 'bool', 'dimen', 'integer', 'plurals', 'string']

RESOURCE_FILE_COUNTS = {'array': 50, 'bool': 2, 'dimen': 1, 'integer': 1, 'plurals': 50, 'string': 120}

REQUIRED = True
REASON   = 'Legend MiuiSystemUI managed resource additions'
