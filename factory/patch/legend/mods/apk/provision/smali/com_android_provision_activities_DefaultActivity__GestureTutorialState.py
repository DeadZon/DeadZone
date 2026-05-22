TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$GestureTutorialState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$GestureTutorialState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__GestureTutorialState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z', 'if-eqz p0, :cond_1', 'sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz p0, :cond_0', 'invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z', 'return p0', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 2

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p0

    if-eqz p0, :cond_1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result p0

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 2

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p0

    if-eqz p0, :cond_1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result p0

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
