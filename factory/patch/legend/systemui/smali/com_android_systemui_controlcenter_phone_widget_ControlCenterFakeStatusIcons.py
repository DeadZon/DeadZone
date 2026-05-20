"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/controlcenter/phone/widget/ControlCenterFakeStatusIcons.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/controlcenter/phone/widget/ControlCenterFakeStatusIcons.smali'
CLASS_FALLBACK_NAMES = ['ControlCenterFakeStatusIcons.smali']
CLASS_ANCHORS        = ['invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V', 'invoke-direct {p1, p0}, Lcom/android/systemui/controlcenter/header/CcFakeStatusBarIcons;-><init>(Lcom/android/systemui/controlcenter/phone/widget/ControlCenterFakeStatusIcons;)V', 'iput-object p1, p0, Lcom/android/systemui/controlcenter/phone/widget/ControlCenterFakeStatusIcons;->delegate:Lcom/android/systemui/controlcenter/header/CcFakeStatusBarIcons;', 'invoke-direct {p0}, Landroid/graphics/Rect;-><init>()V', 'invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V']

PATCHES = [
    {
        'id':             'p0000_setAlpha',
        'type':           'method_add',
        'method':         '.method public setAlpha(F)V',
        'method_name':    'setAlpha',
        'method_anchors': ['invoke-super {p0, v0}, Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;->setAlpha(F)V'],
        'search':         None,
        'replacement':    '.method public setAlpha(F)V\n    .registers 3\n\n    const/4 v0, 0x0\n\n    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/AlphaOptimizedFrameLayout;->setAlpha(F)V\n\n    return-void\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
]
