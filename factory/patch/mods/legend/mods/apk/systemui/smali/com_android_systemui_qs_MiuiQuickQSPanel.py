"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/qs/MiuiQuickQSPanel.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/qs/MiuiQuickQSPanel.smali'
CLASS_FALLBACK_NAMES = ['MiuiQuickQSPanel.smali']
CLASS_ANCHORS        = ['invoke-direct {p0, p1, p2}, Lcom/android/systemui/qs/MiuiQSPanel;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V', 'invoke-direct {p1}, Ljava/lang/Object;-><init>()V', 'iput-object p1, p0, Lcom/android/systemui/qs/MiuiQuickQSPanel;->mNumTiles:Lcom/android/systemui/qs/MiuiQuickQSPanel$1;', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getResources()Landroid/content/res/Resources;', 'invoke-virtual {p0, p1}, Landroid/content/res/Resources;->getInteger(I)I']

PATCHES = [
    {
        'id':             'p0000_updateResources_1',
        'type':           'method_replace',
        'method':         '.method public final updateResources$1()V',
        'method_name':    'updateResources$1',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/LinearLayout;->getResources()Landroid/content/res/Resources;', 'invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getInteger(I)I', 'invoke-static {v1, v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I'],
        'search':         '.method public final updateResources$1()V\n    .registers 3\n\n    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getResources()Landroid/content/res/Resources;\n\n    move-result-object v0\n\n    const v1, 0x7f0c0128\n\n    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getInteger(I)I\n\n    move-result v0\n\n    invoke-virtual {p0, v0}, Lcom/android/systemui/qs/MiuiQuickQSPanel;->setMaxTiles(I)V\n\n    return-void\n.end method\n',
        'replacement':    '.method public final updateResources$1()V\n    .registers 3\n\n    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getResources()Landroid/content/res/Resources;\n\n    move-result-object v0\n\n    const v1, 0x7f0c0128\n\n    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getInteger(I)I\n\n    move-result v0\n\n    const/4 v0, 0x6\n\n    const-string v1, "toggles_mezo_count_single"\n\n    invoke-static {v1, v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I\n\n    move-result v1\n\n    if-eqz v1, :cond_0\n\n    move v0, v1\n\n    :cond_0\n    invoke-virtual {p0, v0}, Lcom/android/systemui/qs/MiuiQuickQSPanel;->setMaxTiles(I)V\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI generated generated dex rule modified class',
    },
]
