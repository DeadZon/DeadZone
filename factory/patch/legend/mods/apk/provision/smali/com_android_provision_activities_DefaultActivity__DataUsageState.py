TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$DataUsageState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$DataUsageState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__DataUsageState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z', 'if-nez p0, :cond_0', 'return p1', 'invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z', 'if-nez p0, :cond_1', 'sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez p0, :cond_1', 'invoke-static {}, Landroid/telephony/TelephonyManager;->getDefault()Landroid/telephony/TelephonyManager;'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 3

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p0

    const/4 p1, 0x0

    if-nez p0, :cond_0

    return p1

    :cond_0
    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result p0

    if-nez p0, :cond_1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez p0, :cond_1

    invoke-static {}, Landroid/telephony/TelephonyManager;->getDefault()Landroid/telephony/TelephonyManager;

    move-result-object p0

    invoke-virtual {p0}, Landroid/telephony/TelephonyManager;->getSimState()I

    move-result p0

    const/4 v0, 0x5

    if-ne p0, v0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    return p1
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 3

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p0

    const/4 p1, 0x0

    if-nez p0, :cond_0

    return p1

    :cond_0
    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result p0

    if-nez p0, :cond_1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez p0, :cond_1

    invoke-static {}, Landroid/telephony/TelephonyManager;->getDefault()Landroid/telephony/TelephonyManager;

    move-result-object p0

    invoke-virtual {p0}, Landroid/telephony/TelephonyManager;->getSimState()I

    move-result p0

    const/4 v0, 0x5

    if-ne p0, v0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    return p1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
