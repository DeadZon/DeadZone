"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/plugins/qs/QS.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/plugins/qs/QS.smali'
CLASS_FALLBACK_NAMES = ['QS.smali']
CLASS_ANCHORS        = ['invoke-interface {p0}, Lcom/android/systemui/plugins/qs/QS;->isShowingDetail()Z', 'invoke-interface {p0}, Lcom/android/systemui/plugins/qs/QS;->getHeaderBottom()I', 'invoke-interface {p0}, Lcom/android/systemui/plugins/qs/QS;->getHeaderTop()I']

PATCHES = [
    {
        'id':             'p0000_updateBackgroundColors',
        'type':           'method_add',
        'method':         '.method public abstract updateBackgroundColors()V',
        'method_name':    'updateBackgroundColors',
        'method_anchors': [],
        'search':         None,
        'replacement':    '.method public abstract updateBackgroundColors()V\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
]
