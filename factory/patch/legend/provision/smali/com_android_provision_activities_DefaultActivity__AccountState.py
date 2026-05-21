TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$AccountState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$AccountState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__AccountState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['new-instance v0, Landroid/content/Intent;', 'const-string v1, "com.xiaomi.account.action.XIAOMI_ACCOUNT_WELCOME"', 'invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V', 'const-string v1, "com.xiaomi.account"', 'invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;', 'invoke-virtual {v0, v1}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;', 'new-instance v1, Landroid/os/Bundle;', 'invoke-direct {v1}, Landroid/os/Bundle;-><init>()V'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 6

    new-instance v0, Landroid/content/Intent;

    const-string v1, "com.xiaomi.account.action.XIAOMI_ACCOUNT_WELCOME"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v1, "com.xiaomi.account"

    invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    const/high16 v1, 0x4000000

    invoke-virtual {v0, v1}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    new-instance v1, Landroid/os/Bundle;

    invoke-direct {v1}, Landroid/os/Bundle;-><init>()V

    const-string v2, "extra_show_find_device"

    const/4 v3, 0x1

    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    const-string v2, "extra_show_skip_login"

    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    const-string v2, "show_sync_settings"

    const/4 v4, 0x0

    invoke-virtual {v1, v2, v4}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    const-string v2, "extra_disable_back_key"

    invoke-virtual {v1, v2, v4}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    const-string v2, "extra_find_pwd_on_pc"

    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    const-string v2, "extra_add_account_from_provision"

    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    const-string v2, "fromButton"

    invoke-static {}, Lcom/android/provision/activities/DefaultActivity;->-$$Nest$sfgetMiMoverDirect()I

    move-result v3

    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object p0

    const-string v2, "androidPackageName"

    invoke-virtual {v1, v2, p0}, Landroid/os/Bundle;->putString(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0, v1}, Landroid/content/Intent;->putExtras(Landroid/os/Bundle;)Landroid/content/Intent;

    return-object v0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 6

    goto :goto_1b

    nop

    :goto_0
    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    goto :goto_a

    nop

    :goto_1
    invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_1f

    nop

    :goto_2
    const/4 v4, 0x0

    goto :goto_6

    nop

    :goto_3
    invoke-static {}, Lcom/android/provision/activities/DefaultActivity;->-$$Nest$sfgetMiMoverDirect()I

    move-result v3

    goto :goto_1a

    nop

    :goto_4
    invoke-direct {v1}, Landroid/os/Bundle;-><init>()V

    goto :goto_1e

    nop

    :goto_5
    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object p0

    goto :goto_13

    nop

    :goto_6
    invoke-virtual {v1, v2, v4}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    goto :goto_11

    nop

    :goto_7
    const-string v2, "extra_add_account_from_provision"

    goto :goto_14

    nop

    :goto_8
    const-string v1, "com.xiaomi.account.action.XIAOMI_ACCOUNT_WELCOME"

    goto :goto_c

    nop

    :goto_9
    invoke-virtual {v1, v2, p0}, Landroid/os/Bundle;->putString(Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_16

    nop

    :goto_a
    const-string v2, "extra_show_skip_login"

    goto :goto_b

    nop

    :goto_b
    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    goto :goto_19

    nop

    :goto_c
    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    goto :goto_15

    nop

    :goto_d
    invoke-virtual {v0, v1}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    goto :goto_f

    nop

    :goto_e
    invoke-virtual {v1, v2, v4}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    goto :goto_1d

    nop

    :goto_f
    new-instance v1, Landroid/os/Bundle;

    goto :goto_4

    nop

    :goto_10
    const-string v2, "fromButton"

    goto :goto_3

    nop

    :goto_11
    const-string v2, "extra_disable_back_key"

    goto :goto_e

    nop

    :goto_12
    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    goto :goto_7

    nop

    :goto_13
    const-string v2, "androidPackageName"

    goto :goto_9

    nop

    :goto_14
    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    goto :goto_10

    nop

    :goto_15
    const-string v1, "com.xiaomi.account"

    goto :goto_1

    nop

    :goto_16
    invoke-virtual {v0, v1}, Landroid/content/Intent;->putExtras(Landroid/os/Bundle;)Landroid/content/Intent;

    goto :goto_1c

    nop

    :goto_17
    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    goto :goto_5

    nop

    :goto_18
    const/4 v3, 0x1

    goto :goto_0

    nop

    :goto_19
    const-string v2, "show_sync_settings"

    goto :goto_2

    nop

    :goto_1a
    invoke-virtual {v1, v2, v3}, Landroid/os/Bundle;->putInt(Ljava/lang/String;I)V

    goto :goto_17

    nop

    :goto_1b
    new-instance v0, Landroid/content/Intent;

    goto :goto_8

    nop

    :goto_1c
    return-object v0

    :goto_1d
    const-string v2, "extra_find_pwd_on_pc"

    goto :goto_12

    nop

    :goto_1e
    const-string v2, "extra_show_find_device"

    goto :goto_18

    nop

    :goto_1f
    const/high16 v1, 0x4000000

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__AccountState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z', 'if-nez p1, :cond_0', 'return v0', 'invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;', 'const-string v1, "disallow_mi_account"', 'invoke-interface {p1, v1}, Lmiui/enterprise/IRestrictionsHelper;->isRestriction(Ljava/lang/String;)Z', 'if-eqz p1, :cond_1', 'return v0'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 4

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    const/4 v0, 0x0

    if-nez p1, :cond_0

    return v0

    :cond_0
    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object p1

    const-string v1, "disallow_mi_account"

    invoke-interface {p1, v1}, Lmiui/enterprise/IRestrictionsHelper;->isRestriction(Ljava/lang/String;)Z

    move-result p1

    if-eqz p1, :cond_1

    return v0

    :cond_1
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez p1, :cond_3

    sget-boolean p1, Lmiui/os/Build;->IS_PRIVATE_BUILD:Z

    if-nez p1, :cond_2

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/utils/NetworkUtils;->isCaptivePortalValidated(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_3

    :cond_2
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lmiui/accounts/ExtraAccountManager;->getXiaomiAccount(Landroid/content/Context;)Landroid/accounts/Account;

    move-result-object p1

    if-nez p1, :cond_3

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    const-string p1, "com.xiaomi.account"

    invoke-static {p0, p1}, Lcom/android/provision/Utils;->queryCTAStatus(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_3

    const/4 p0, 0x1

    return p0

    :cond_3
    return v0
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 4

    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    const/4 v0, 0x0

    if-nez p1, :cond_0

    return v0

    :cond_0
    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object p1

    const-string v1, "disallow_mi_account"

    invoke-interface {p1, v1}, Lmiui/enterprise/IRestrictionsHelper;->isRestriction(Ljava/lang/String;)Z

    move-result p1

    if-eqz p1, :cond_1

    return v0

    :cond_1
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez p1, :cond_3

    sget-boolean p1, Lmiui/os/Build;->IS_PRIVATE_BUILD:Z

    if-nez p1, :cond_2

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/utils/NetworkUtils;->isCaptivePortalValidated(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_3

    :cond_2
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lmiui/accounts/ExtraAccountManager;->getXiaomiAccount(Landroid/content/Context;)Landroid/accounts/Account;

    move-result-object p1

    if-nez p1, :cond_3

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    const-string p1, "com.xiaomi.account"

    invoke-static {p0, p1}, Lcom/android/provision/Utils;->queryCTAStatus(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_3

    const/4 p0, 0x1

    return p0

    :cond_3
    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
