"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/charge/ChargeUtils.smali
Patches      : 5
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/charge/ChargeUtils.smali'
CLASS_FALLBACK_NAMES = ['ChargeUtils.smali']
CLASS_ANCHORS        = ['invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z', 'sput-boolean v0, Lcom/miui/charge/ChargeUtils;->SUPPORT_DOUBLE_CHARGE:Z', 'invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z', 'sput-boolean v0, Lcom/miui/charge/ChargeUtils;->SUPPORT_CHARGE_SHADER:Z', 'sput-boolean v0, Lcom/miui/charge/ChargeUtils;->sDevelopAnimationEnable:Z']

PATCHES = [
    {
        'id':             'p0000_getChargeAnimationType',
        'type':           'method_add',
        'method':         '.method public static getChargeAnimationType()I',
        'method_name':    'getChargeAnimationType',
        'method_anchors': ['invoke-static {v0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;', 'iget v0, v0, Lcom/miui/systemui/SettingsManager;->chargeAnimType:I'],
        'search':         None,
        'replacement':    '.method public static getChargeAnimationType()I\n    .registers 1\n\n    const-class v0, Lcom/miui/systemui/SettingsManager;\n\n    invoke-static {v0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/miui/systemui/SettingsManager;\n\n    iget v0, v0, Lcom/miui/systemui/SettingsManager;->chargeAnimType:I\n\n    return v0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0001_isChargeAnimationDisabled',
        'type':           'method_add',
        'method':         '.method public static isChargeAnimationDisabled()Z',
        'method_name':    'isChargeAnimationDisabled',
        'method_anchors': ['sget-boolean v0, Lcom/miui/charge/ChargeUtils;->sChargeAnimationDisabled:Z', 'invoke-static {}, Lcom/miui/charge/ChargeUtils;->getChargeAnimationType()I'],
        'search':         None,
        'replacement':    '.method public static isChargeAnimationDisabled()Z\n    .registers 1\n\n    sget-boolean v0, Lcom/miui/charge/ChargeUtils;->sChargeAnimationDisabled:Z\n\n    if-nez v0, :cond_0\n\n    invoke-static {}, Lcom/miui/charge/ChargeUtils;->getChargeAnimationType()I\n\n    move-result v0\n\n    if-lez v0, :cond_0\n\n    const/4 v0, 0x0\n\n    goto :goto_0\n\n    :cond_0\n    const/4 v0, 0x1\n\n    :goto_0\n    return v0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0002_supportShaderChargeAnimation',
        'type':           'method_add',
        'method':         '.method public static supportShaderChargeAnimation()Z',
        'method_name':    'supportShaderChargeAnimation',
        'method_anchors': ['sget-boolean v0, Lcom/miui/charge/ChargeUtils;->SUPPORT_CHARGE_SHADER:Z', 'invoke-static {}, Lcom/miui/charge/ChargeUtils;->getChargeAnimationType()I'],
        'search':         None,
        'replacement':    '.method public static supportShaderChargeAnimation()Z\n    .registers 2\n\n    sget-boolean v0, Lcom/miui/charge/ChargeUtils;->SUPPORT_CHARGE_SHADER:Z\n\n    if-eqz v0, :cond_0\n\n    invoke-static {}, Lcom/miui/charge/ChargeUtils;->getChargeAnimationType()I\n\n    move-result v0\n\n    const/4 v1, 0x1\n\n    if-ne v0, v1, :cond_0\n\n    goto :goto_0\n\n    :cond_0\n    const/4 v1, 0x0\n\n    :goto_0\n    return v1\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0003_supportVideoChargeAnimation',
        'type':           'method_add',
        'method':         '.method public static supportVideoChargeAnimation()Z',
        'method_name':    'supportVideoChargeAnimation',
        'method_anchors': ['invoke-static {}, Lcom/miui/charge/ChargeUtils;->getChargeAnimationType()I'],
        'search':         None,
        'replacement':    '.method public static supportVideoChargeAnimation()Z\n    .registers 2\n\n    invoke-static {}, Lcom/miui/charge/ChargeUtils;->getChargeAnimationType()I\n\n    move-result v0\n\n    const/4 v1, 0x1\n\n    if-ne v0, v1, :cond_0\n\n    goto :goto_0\n\n    :cond_0\n    const/4 v1, 0x0\n\n    :goto_0\n    return v1\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
    {
        'id':             'p0004_supportWaveChargeAnimation',
        'type':           'method_replace',
        'method':         '.method public static supportWaveChargeAnimation()Z',
        'method_name':    'supportWaveChargeAnimation',
        'method_anchors': ['invoke-static {}, Lcom/miui/charge/ChargeUtils;->getChargeAnimationType()I'],
        'search':         '.method public static supportWaveChargeAnimation()Z\n    .registers 2\n\n    const-class v0, Lcom/android/systemui/plugins/miui/settings/IUserTracker;\n\n    invoke-static {v0}, Lcom/miui/systemui/interfacesmanager/InterfacesImplManager;->getImpl(Ljava/lang/Class;)Ljava/lang/Object;\n\n    move-result-object v0\n\n    check-cast v0, Lcom/android/systemui/plugins/miui/settings/IUserTracker;\n\n    invoke-interface {v0}, Lcom/android/systemui/plugins/miui/settings/IUserTracker;->getUserContext()Landroid/content/Context;\n\n    move-result-object v0\n\n    invoke-virtual {v0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;\n\n    move-result-object v0\n\n    const v1, 0x7f0c008a\n\n    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getInteger(I)I\n\n    move-result v0\n\n    const/4 v1, 0x2\n\n    if-ne v0, v1, :cond_0\n\n    const/4 v0, 0x1\n\n    return v0\n\n    :cond_0\n    const/4 v0, 0x0\n\n    return v0\n.end method\n',
        'replacement':    '.method public static supportWaveChargeAnimation()Z\n    .registers 2\n\n    invoke-static {}, Lcom/miui/charge/ChargeUtils;->getChargeAnimationType()I\n\n    move-result v0\n\n    const/4 v1, 0x2\n\n    if-ne v0, v1, :cond_0\n\n    const/4 v0, 0x1\n\n    return v0\n\n    :cond_0\n    const/4 v0, 0x0\n\n    return v0\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
]
