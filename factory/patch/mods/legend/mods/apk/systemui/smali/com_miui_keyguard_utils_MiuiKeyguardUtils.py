"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/keyguard/utils/MiuiKeyguardUtils.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/keyguard/utils/MiuiKeyguardUtils.smali'
CLASS_FALLBACK_NAMES = ['MiuiKeyguardUtils.smali']
CLASS_ANCHORS        = ['invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V', 'sput-object v0, Lcom/miui/keyguard/utils/MiuiKeyguardUtils;->sRegionSupportMiHomeList:Ljava/util/List;', 'invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V', 'sput-object v0, Lcom/miui/keyguard/utils/MiuiKeyguardUtils;->sKeepScreenOnWhenLargeAreaTouchList:Ljava/util/List;', 'invoke-direct {v1, v0, v2}, Lkotlin/Pair;-><init>(Ljava/lang/Object;Ljava/lang/Object;)V']

PATCHES = [
    {
        'id':             'p0000_isRegionSupportMiHome',
        'type':           'method_replace',
        'method':         '.method public static isRegionSupportMiHome(Landroid/content/Context;)Z',
        'method_name':    'isRegionSupportMiHome',
        'method_anchors': [],
        'search':         '.method public static isRegionSupportMiHome(Landroid/content/Context;)Z\n    .registers 3\n\n    sget-object v0, Lcom/miui/keyguard/utils/MiuiKeyguardUtils;->sRegionSupportMiHomeList:Ljava/util/List;\n\n    invoke-interface {v0}, Ljava/util/List;->isEmpty()Z\n\n    move-result v0\n\n    if-eqz v0, :cond_0\n\n    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;\n\n    move-result-object p0\n\n    const v0, 0x7f0300d8\n\n    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getStringArray(I)[Ljava/lang/String;\n\n    move-result-object p0\n\n    array-length v0, p0\n\n    invoke-static {p0, v0}, Ljava/util/Arrays;->copyOf([Ljava/lang/Object;I)[Ljava/lang/Object;\n\n    move-result-object p0\n\n    invoke-static {p0}, Lkotlin/collections/CollectionsKt__CollectionsKt;->listOf([Ljava/lang/Object;)Ljava/util/List;\n\n    move-result-object p0\n\n    sput-object p0, Lcom/miui/keyguard/utils/MiuiKeyguardUtils;->sRegionSupportMiHomeList:Ljava/util/List;\n\n    :cond_0\n    sget-object p0, Lcom/miui/keyguard/utils/MiuiKeyguardUtils;->sRegionSupportMiHomeList:Ljava/util/List;\n\n    sget-object v0, Lcom/miui/utils/configs/MiuiConfigs;->CUSTOMIZED_REGION:Ljava/lang/String;\n\n    const-string v0, "ro.miui.region"\n\n    const-string v1, "CN"\n\n    invoke-static {v0, v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;\n\n    move-result-object v0\n\n    invoke-interface {p0, v0}, Ljava/util/List;->contains(Ljava/lang/Object;)Z\n\n    move-result p0\n\n    return p0\n.end method\n',
        'replacement':    '.method public static isRegionSupportMiHome(Landroid/content/Context;)Z\n    .registers 2\n\n    const/4 v0, 0x1\n\n    return v0\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI generated generated dex rule modified class',
    },
]
