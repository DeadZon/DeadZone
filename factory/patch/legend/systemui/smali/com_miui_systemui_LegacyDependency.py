"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/LegacyDependency.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/LegacyDependency.smali'
CLASS_FALLBACK_NAMES = ['LegacyDependency.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        'id':             'p0000_field__field_public_mWeath',
        'type':           'field_add',
        'method':         '.field public mWeatherController:Ldagger/Lazy;',
        'method_name':    '',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.field public mWeatherController:Ldagger/Lazy;',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added field',
    },
]
