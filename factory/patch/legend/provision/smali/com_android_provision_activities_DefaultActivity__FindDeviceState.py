TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$FindDeviceState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$FindDeviceState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__FindDeviceState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['iget-object v0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;', 'invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;', 'const-string v1, "provision_findDevice_enabled"', 'invoke-static {v0, v1, v2}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I', 'if-nez v0, :cond_0', 'iget-object v3, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;', 'invoke-static {v3}, Lmiui/accounts/ExtraAccountManager;->getXiaomiAccount(Landroid/content/Context;)Landroid/accounts/Account;', 'if-eqz v3, :cond_1'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 9

    iget-object v0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "provision_findDevice_enabled"

    const/4 v2, 0x0

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    const/4 v1, 0x1

    if-nez v0, :cond_0

    move v0, v1

    goto :goto_0

    :cond_0
    move v0, v2

    :goto_0
    iget-object v3, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {v3}, Lmiui/accounts/ExtraAccountManager;->getXiaomiAccount(Landroid/content/Context;)Landroid/accounts/Account;

    move-result-object v3

    if-eqz v3, :cond_1

    move v3, v1

    goto :goto_1

    :cond_1
    move v3, v2

    :goto_1
    iget-object v4, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-direct {p0, v4}, Lcom/android/provision/activities/DefaultActivity$FindDeviceState;->getLastSessionUserId(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v4

    invoke-static {v4}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v4

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "FindDeviceState: findDevice:"

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v6, ",isHasXiaomiCount:"

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v6, ",isSessionUserIdEmpty:"

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    const-string v6, "Provision_DefaultActivity"

    invoke-static {v6, v5}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    sget-boolean v5, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v5, :cond_2

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    if-eqz p1, :cond_2

    if-eqz v3, :cond_2

    if-eqz v4, :cond_2

    iget-boolean p1, p0, Lcom/android/provision/activities/DefaultActivity$FindDeviceState;->mPasswordLogin:Z

    if-eqz p1, :cond_2

    if-eqz v0, :cond_2

    invoke-static {}, Lcom/android/provision/Utils;->isRedmiDigitOrNoteSeries()Z

    move-result p1

    if-eqz p1, :cond_2

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    const-string p1, "com.xiaomi.account"

    invoke-static {p0, p1}, Lcom/android/provision/Utils;->queryCTAStatus(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_2

    return v1

    :cond_2
    return v2
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 9

    iget-object v0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "provision_findDevice_enabled"

    const/4 v2, 0x0

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    const/4 v1, 0x1

    if-nez v0, :cond_0

    move v0, v1

    goto :goto_0

    :cond_0
    move v0, v2

    :goto_0
    iget-object v3, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {v3}, Lmiui/accounts/ExtraAccountManager;->getXiaomiAccount(Landroid/content/Context;)Landroid/accounts/Account;

    move-result-object v3

    if-eqz v3, :cond_1

    move v3, v1

    goto :goto_1

    :cond_1
    move v3, v2

    :goto_1
    iget-object v4, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-direct {p0, v4}, Lcom/android/provision/activities/DefaultActivity$FindDeviceState;->getLastSessionUserId(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v4

    invoke-static {v4}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v4

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "FindDeviceState: findDevice:"

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v6, ",isHasXiaomiCount:"

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v6, ",isSessionUserIdEmpty:"

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    const-string v6, "Provision_DefaultActivity"

    invoke-static {v6, v5}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    sget-boolean v5, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v5, :cond_2

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    if-eqz p1, :cond_2

    if-eqz v3, :cond_2

    if-eqz v4, :cond_2

    iget-boolean p1, p0, Lcom/android/provision/activities/DefaultActivity$FindDeviceState;->mPasswordLogin:Z

    if-eqz p1, :cond_2

    if-eqz v0, :cond_2

    invoke-static {}, Lcom/android/provision/Utils;->isRedmiDigitOrNoteSeries()Z

    move-result p1

    if-eqz p1, :cond_2

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    const-string p1, "com.xiaomi.account"

    invoke-static {p0, p1}, Lcom/android/provision/Utils;->queryCTAStatus(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_2

    return v1

    :cond_2
    return v2
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
