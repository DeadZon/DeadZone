"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/tuner/TunerService.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/tuner/TunerService.smali'
CLASS_FALLBACK_NAMES = ['TunerService.smali']
CLASS_ANCHORS        = ['invoke-static {p0}, Ljava/lang/Integer;->parseInt(Ljava/lang/String;)I']

PATCHES = [
    {
        'id':             'p0000_getValue',
        'type':           'method_add',
        'method':         '.method public abstract getValue(ILjava/lang/String;)I',
        'method_name':    'getValue',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.method public abstract getValue(ILjava/lang/String;)I\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
]
