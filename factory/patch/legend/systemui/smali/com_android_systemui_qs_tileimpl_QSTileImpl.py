"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/qs/tileimpl/QSTileImpl.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/qs/tileimpl/QSTileImpl.smali'
CLASS_FALLBACK_NAMES = ['QSTileImpl.smali']
CLASS_ANCHORS        = ['iget-object v0, p0, Lcom/android/systemui/qs/tileimpl/QSTileImpl;->mUiHandler:Landroid/os/Handler;', 'iget-object v2, p0, Lcom/android/systemui/qs/tileimpl/QSTileImpl;->TAG:Ljava/lang/String;', 'iget-boolean v3, p0, Lcom/android/systemui/qs/tileimpl/QSTileImpl;->DEBUG:Z', 'iget-object v5, p0, Lcom/android/systemui/qs/tileimpl/QSTileImpl;->mListeners:Landroid/util/ArraySet;', 'invoke-virtual {v5, p1}, Landroid/util/ArraySet;->add(Ljava/lang/Object;)Z']

PATCHES = [
    {
        'id':             'p0000_isAvailable',
        'type':           'method_replace',
        'method':         '.method public isAvailable()Z',
        'method_name':    'isAvailable',
        'method_anchors': [],
        'search':         '.method public isAvailable()Z\n    .registers 1\n\n    instance-of p0, p0, Lcom/android/systemui/qs/tiles/ModesDndTile;\n\n    xor-int/lit8 p0, p0, 0x1\n\n    return p0\n.end method\n',
        'replacement':    '.method public isAvailable()Z\n    .registers 1\n\n    const/4 p0, 0x1\n\n    return p0\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
]
