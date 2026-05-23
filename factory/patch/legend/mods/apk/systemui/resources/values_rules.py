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


def _find_repo_root(start: Path) -> Path:
    """Walk upward until a directory containing factory/ and (.git or third_party/) is found."""
    p = start.resolve()
    while p != p.parent:
        if (p / 'factory').is_dir() and ((p / '.git').exists() or (p / 'third_party').is_dir()):
            return p
        p = p.parent
    raise RuntimeError(
        f"Cannot locate repo root from {start!r}: "
        "no directory with factory/ + (.git or third_party/) found"
    )


TARGET_APK = 'MiuiSystemUI.apk'

_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _find_repo_root(_HERE)

# Managed asset root — do NOT read from Legend/ at runtime
ASSETS_ROOT = _REPO_ROOT / 'factory' / 'assets' / 'legend' / 'systemui' / 'resources'
ADD_RESOURCES_SRC = ASSETS_ROOT / 'com.android.systemui'

RESOURCE_TYPES = ['array', 'bool', 'dimen', 'integer', 'plurals', 'string']

RESOURCE_FILE_COUNTS = {'array': 50, 'bool': 2, 'dimen': 1, 'integer': 1, 'plurals': 50, 'string': 120}

REQUIRED = True
REASON   = 'Legend MiuiSystemUI managed resource additions'
