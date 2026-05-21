TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/GlobalDefaultActivity$ActivateDeviceState.smali'
CLASS_FALLBACK_NAMES = ['GlobalDefaultActivity$ActivateDeviceState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/GlobalDefaultActivity$State;', '.field private static final ASSOCIATED_ACCOUNT:Ljava/lang/String; = "associated_account"']

PATCHES = [
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__ActivateDeviceState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['invoke-super {p0}, Lcom/android/provision/global/GlobalDefaultActivity$State;->getIntent()Landroid/content/Intent;', 'const-string v1, "associated_account"', 'iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$ActivateDeviceState;->mAssociatedAccount:Ljava/lang/String;', 'invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    invoke-super {p0}, Lcom/android/provision/global/GlobalDefaultActivity$State;->getIntent()Landroid/content/Intent;

    move-result-object v0

    const-string v1, "associated_account"

    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$ActivateDeviceState;->mAssociatedAccount:Ljava/lang/String;

    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    return-object v0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    goto :goto_2

    nop

    :goto_0
    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$ActivateDeviceState;->mAssociatedAccount:Ljava/lang/String;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_4

    nop

    :goto_2
    invoke-super {p0}, Lcom/android/provision/global/GlobalDefaultActivity$State;->getIntent()Landroid/content/Intent;

    move-result-object v0

    goto :goto_3

    nop

    :goto_3
    const-string v1, "associated_account"

    goto :goto_0

    nop

    :goto_4
    return-object v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__ActivateDeviceState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z', 'if-nez p1, :cond_0', 'return v0', 'sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez p1, :cond_1', 'invoke-direct {p0}, Lcom/android/provision/global/GlobalDefaultActivity$ActivateDeviceState;->isNetworkAvailable()Z', 'if-nez p1, :cond_1', 'iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 3

    invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    const/4 v0, 0x0

    if-nez p1, :cond_0

    return v0

    :cond_0
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez p1, :cond_1

    invoke-direct {p0}, Lcom/android/provision/global/GlobalDefaultActivity$ActivateDeviceState;->isNetworkAvailable()Z

    move-result p1

    if-nez p1, :cond_1

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_1

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-direct {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$ActivateDeviceState;->getLastSessionUserId(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p0

    if-nez p0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    return v0
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 3

    invoke-super {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$State;->isAvailable(Z)Z

    move-result p1

    const/4 v0, 0x0

    if-nez p1, :cond_0

    return v0

    :cond_0
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez p1, :cond_1

    invoke-direct {p0}, Lcom/android/provision/global/GlobalDefaultActivity$ActivateDeviceState;->isNetworkAvailable()Z

    move-result p1

    if-nez p1, :cond_1

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-static {p1}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_1

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity$State;->context:Landroid/content/Context;

    invoke-direct {p0, p1}, Lcom/android/provision/global/GlobalDefaultActivity$ActivateDeviceState;->getLastSessionUserId(Landroid/content/Context;)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p0

    if-nez p0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
