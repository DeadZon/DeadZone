TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$CloudServiceState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$CloudServiceState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;', '.field private static final INTENT_KEY_CAN_INSTALL:Ljava/lang/String; = "extra_can_install"', '.field private static final INTENT_KEY_PASSWORD_LOGIN:Ljava/lang/String; = "extra_password_login"', '.field private static final INTENT_KEY_VERSION:Ljava/lang/String; = "extra_master_key_version"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__CloudServiceState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;', 'const-string v1, "extra_master_key_version"', 'iget-wide v2, p0, Lcom/android/provision/activities/DefaultActivity$CloudServiceState;->mMasterKeyVersion:J', 'invoke-virtual {v0, v1, v2, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;J)Landroid/content/Intent;', 'const-string v1, "extra_can_install"', 'iget-boolean p0, p0, Lcom/android/provision/activities/DefaultActivity$CloudServiceState;->mCanInstall:Z', 'invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;', 'const-string p0, "extra_password_login"'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 5

    invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;

    move-result-object v0

    const-string v1, "extra_master_key_version"

    iget-wide v2, p0, Lcom/android/provision/activities/DefaultActivity$CloudServiceState;->mMasterKeyVersion:J

    invoke-virtual {v0, v1, v2, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;J)Landroid/content/Intent;

    const-string v1, "extra_can_install"

    iget-boolean p0, p0, Lcom/android/provision/activities/DefaultActivity$CloudServiceState;->mCanInstall:Z

    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    const-string p0, "extra_password_login"

    sget-boolean v1, Lcom/android/provision/activities/DefaultActivity$CloudServiceState;->mPasswordLogin:Z

    invoke-virtual {v0, p0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    return-object v0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 5

    goto :goto_6

    nop

    :goto_0
    const-string p0, "extra_password_login"

    goto :goto_2

    nop

    :goto_1
    const-string v1, "extra_master_key_version"

    goto :goto_7

    nop

    :goto_2
    sget-boolean v1, Lcom/android/provision/activities/DefaultActivity$CloudServiceState;->mPasswordLogin:Z

    goto :goto_4

    nop

    :goto_3
    const-string v1, "extra_can_install"

    goto :goto_8

    nop

    :goto_4
    invoke-virtual {v0, p0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    goto :goto_5

    nop

    :goto_5
    return-object v0

    :goto_6
    invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;

    move-result-object v0

    goto :goto_1

    nop

    :goto_7
    iget-wide v2, p0, Lcom/android/provision/activities/DefaultActivity$CloudServiceState;->mMasterKeyVersion:J

    goto :goto_9

    nop

    :goto_8
    iget-boolean p0, p0, Lcom/android/provision/activities/DefaultActivity$CloudServiceState;->mCanInstall:Z

    goto :goto_a

    nop

    :goto_9
    invoke-virtual {v0, v1, v2, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;J)Landroid/content/Intent;

    goto :goto_3

    nop

    :goto_a
    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__CloudServiceState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z', 'if-eqz p1, :cond_0', 'iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;', 'invoke-static {p1}, Lmiui/accounts/ExtraAccountManager;->getXiaomiAccount(Landroid/content/Context;)Landroid/accounts/Account;', 'if-eqz p1, :cond_0', 'iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 4

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-nez v0, :cond_0

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lmiui/accounts/ExtraAccountManager;->getXiaomiAccount(Landroid/content/Context;)Landroid/accounts/Account;

    move-result-object p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v0, "provision_cloudService_enabled"

    invoke-static {p1, v0, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p1

    if-nez p1, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isRedmiDigitOrNoteSeries()Z

    move-result p1

    if-nez p1, :cond_0

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    const-string p1, "com.xiaomi.account"

    invoke-static {p0, p1}, Lcom/android/provision/Utils;->queryCTAStatus(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    return v1
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 4

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-nez v0, :cond_0

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lmiui/accounts/ExtraAccountManager;->getXiaomiAccount(Landroid/content/Context;)Landroid/accounts/Account;

    move-result-object p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v0, "provision_cloudService_enabled"

    invoke-static {p1, v0, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p1

    if-nez p1, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isRedmiDigitOrNoteSeries()Z

    move-result p1

    if-nez p1, :cond_0

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    const-string p1, "com.xiaomi.account"

    invoke-static {p0, p1}, Lcom/android/provision/Utils;->queryCTAStatus(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    return v1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
