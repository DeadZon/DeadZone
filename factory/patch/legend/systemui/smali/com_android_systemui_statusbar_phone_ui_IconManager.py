"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/phone/ui/IconManager.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/phone/ui/IconManager.smali'
CLASS_FALLBACK_NAMES = ['IconManager.smali']
CLASS_ANCHORS        = ['invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'invoke-direct {v0, v1}, Landroidx/collection/MutableIntObjectMap;-><init>(Ljava/lang/Object;)V', 'invoke-direct {v0}, Ljava/util/HashMap;-><init>()V', 'iput-object v0, p0, Lcom/android/systemui/statusbar/phone/ui/IconManager;->mBindableIcons:Ljava/util/Map;', 'iput-boolean v0, p0, Lcom/android/systemui/statusbar/phone/ui/IconManager;->mShouldLog:Z']

PATCHES = [
    {
        'id':             'p0000_onCreateLayoutParams',
        'type':           'method_replace',
        'method':         '.method public onCreateLayoutParams(Lcom/android/internal/statusbar/StatusBarIcon$Shape;)Landroid/widget/LinearLayout$LayoutParams;',
        'method_name':    'onCreateLayoutParams',
        'method_anchors': ['sget-object v0, Lcom/android/internal/statusbar/StatusBarIcon$Shape;->FIXED_SPACE:Lcom/android/internal/statusbar/StatusBarIcon$Shape;', 'iget p1, p0, Lcom/android/systemui/statusbar/phone/ui/IconManager;->mIconSize:I', 'iget p0, p0, Lcom/android/systemui/statusbar/phone/ui/IconManager;->mIconSize:I'],
        'search':         '.method public onCreateLayoutParams(Lcom/android/internal/statusbar/StatusBarIcon$Shape;)Landroid/widget/LinearLayout$LayoutParams;\n    .registers 3\n\n    sget-object v0, Lcom/android/internal/statusbar/StatusBarIcon$Shape;->FIXED_SPACE:Lcom/android/internal/statusbar/StatusBarIcon$Shape;\n\n    if-ne p1, v0, :cond_0\n\n    iget p1, p0, Lcom/android/systemui/statusbar/phone/ui/IconManager;->mIconSize:I\n\n    goto :goto_0\n\n    :cond_0\n    const/4 p1, -0x2\n\n    :goto_0\n    new-instance v0, Landroid/widget/LinearLayout$LayoutParams;\n\n    iget p0, p0, Lcom/android/systemui/statusbar/phone/ui/IconManager;->mIconSize:I\n\n    invoke-direct {v0, p1, p0}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V\n\n    return-object v0\n.end method\n',
        'replacement':    '.method public onCreateLayoutParams(Lcom/android/internal/statusbar/StatusBarIcon$Shape;)Landroid/widget/LinearLayout$LayoutParams;\n    .registers 3\n\n    sget-object v0, Lcom/android/internal/statusbar/StatusBarIcon$Shape;->FIXED_SPACE:Lcom/android/internal/statusbar/StatusBarIcon$Shape;\n\n    if-ne p1, v0, :cond_0\n\n    iget p1, p0, Lcom/android/systemui/statusbar/phone/ui/IconManager;->mIconSize:I\n\n    goto :goto_0\n\n    :cond_0\n    const/4 p1, -0x2\n\n    :goto_0\n    new-instance v0, Landroid/widget/LinearLayout$LayoutParams;\n\n    iget p0, p0, Lcom/android/systemui/statusbar/phone/ui/IconManager;->mIconSize:I\n\n    invoke-direct {v0, p1, p1}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V\n\n    return-object v0\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
]
