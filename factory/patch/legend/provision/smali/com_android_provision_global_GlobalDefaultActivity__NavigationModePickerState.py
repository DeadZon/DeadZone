TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/GlobalDefaultActivity$NavigationModePickerState.smali'
CLASS_FALLBACK_NAMES = ['GlobalDefaultActivity$NavigationModePickerState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/GlobalDefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__NavigationModePickerState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isNeedRemoveSystemNavigationMode()Z', 'if-eqz p1, :cond_0', 'return v0', 'iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;', 'invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z', 'if-nez p0, :cond_1', 'invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z', 'if-nez p0, :cond_1'],
        'type': 'method_replace',
        'search': """.method public isAvailable(Z)Z
    .registers 3

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isNeedRemoveSystemNavigationMode()Z

    move-result p1

    const/4 v0, 0x0

    if-eqz p1, :cond_0

    return v0

    :cond_0
    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result p0

    if-nez p0, :cond_1

    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result p0

    if-nez p0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    return v0
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 4

    invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    const/4 v0, 0x0

    if-nez p1, :cond_0

    return v0

    :cond_0
    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result p1

    if-eqz p1, :cond_1

    return v0

    :cond_1
    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/Utils;->getHuanjiSettingsStatus(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_2

    return v0

    :cond_2
    invoke-static {}, Lcom/android/provision/utils/NotchAdapterUtils;->checkDeviceHasNavigationBar()Z

    move-result p1

    if-eqz p1, :cond_3

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object p1

    iget-object v1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {v1}, Lcom/android/provision/Utils;->getGestureIntent(Landroid/content/Context;)Landroid/content/Intent;

    move-result-object v1

    invoke-virtual {p1, v1, v0}, Landroid/content/pm/PackageManager;->resolveActivity(Landroid/content/Intent;I)Landroid/content/pm/ResolveInfo;

    move-result-object p1

    if-eqz p1, :cond_3

    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {}, Lcom/android/provision/Utils;->navigationPickerDisplayable()Z

    move-result p0

    if-eqz p0, :cond_3

    const/4 p0, 0x1

    return p0

    :cond_3
    return v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
