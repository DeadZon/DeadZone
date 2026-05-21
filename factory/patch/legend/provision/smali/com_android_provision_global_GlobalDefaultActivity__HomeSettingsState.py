TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/GlobalDefaultActivity$HomeSettingsState.smali'
CLASS_FALLBACK_NAMES = ['GlobalDefaultActivity$HomeSettingsState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/GlobalDefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__HomeSettingsState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z', 'if-eqz p1, :cond_1', 'sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz p1, :cond_1', 'invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->disabledHomeLayoutOptional()Z', 'if-nez p1, :cond_1', 'invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z', 'if-eqz p1, :cond_0'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 2

    invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    if-eqz p1, :cond_1

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_1

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->disabledHomeLayoutOptional()Z

    move-result p1

    if-nez p1, :cond_1

    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result p1

    if-eqz p1, :cond_0

    goto :goto_0

    :cond_0
    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result p0

    xor-int/lit8 p0, p0, 0x1

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 2

    invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    if-eqz p1, :cond_1

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_1

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->disabledHomeLayoutOptional()Z

    move-result p1

    if-nez p1, :cond_1

    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result p1

    if-eqz p1, :cond_0

    goto :goto_0

    :cond_0
    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result p0

    xor-int/lit8 p0, p0, 0x1

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x0

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
