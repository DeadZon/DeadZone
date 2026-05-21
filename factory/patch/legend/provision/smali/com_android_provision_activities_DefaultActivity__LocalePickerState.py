TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$LocalePickerState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$LocalePickerState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__LocalePickerState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z', 'if-nez p0, :cond_0', 'return p1', 'invoke-static {}, Lmiui/os/MiuiInit;->getCustVariants()[Ljava/lang/String;', 'if-eqz p0, :cond_1', 'invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;', 'invoke-virtual {p0}, Lcom/android/provision/utils/MccHelper;->isTaiwanLocale()Z', 'if-nez p0, :cond_1'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 3

    sget-boolean p0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    const/4 p1, 0x0

    if-nez p0, :cond_0

    return p1

    :cond_0
    :try_start_0
    invoke-static {}, Lmiui/os/MiuiInit;->getCustVariants()[Ljava/lang/String;

    move-result-object v0
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    const/4 v0, 0x0

    :goto_0
    if-eqz p0, :cond_1

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object p0

    invoke-virtual {p0}, Lcom/android/provision/utils/MccHelper;->isTaiwanLocale()Z

    move-result p0

    if-nez p0, :cond_1

    if-eqz v0, :cond_1

    array-length p0, v0

    if-lez p0, :cond_1

    const/4 p1, 0x1

    :cond_1
    return p1
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 3

    sget-boolean p0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    const/4 p1, 0x0

    if-nez p0, :cond_0

    return p1

    :cond_0
    :try_start_0
    invoke-static {}, Lmiui/os/MiuiInit;->getCustVariants()[Ljava/lang/String;

    move-result-object v0
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    const/4 v0, 0x0

    :goto_0
    if-eqz p0, :cond_1

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object p0

    invoke-virtual {p0}, Lcom/android/provision/utils/MccHelper;->isTaiwanLocale()Z

    move-result p0

    if-nez p0, :cond_1

    if-eqz v0, :cond_1

    array-length p0, v0

    if-lez p0, :cond_1

    const/4 p1, 0x1

    :cond_1
    return p1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
