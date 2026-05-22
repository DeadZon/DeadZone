TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$ActivateDeviceState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$ActivateDeviceState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;', '.field private static final ASSOCIATED_ACCOUNT:Ljava/lang/String; = "associated_account"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__ActivateDeviceState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;', 'const-string v1, "associated_account"', 'iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$ActivateDeviceState;->mAssociatedAccount:Ljava/lang/String;', 'invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;

    move-result-object v0

    const-string v1, "associated_account"

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$ActivateDeviceState;->mAssociatedAccount:Ljava/lang/String;

    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    return-object v0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    goto :goto_4

    nop

    :goto_0
    const-string v1, "associated_account"

    goto :goto_3

    nop

    :goto_1
    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_2

    nop

    :goto_2
    return-object v0

    :goto_3
    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$ActivateDeviceState;->mAssociatedAccount:Ljava/lang/String;

    goto :goto_1

    nop

    :goto_4
    invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;

    move-result-object v0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__ActivateDeviceState__isAvailable',
        'method': '.method public isAvailable(Z)Z',
        'method_name': 'isAvailable',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'return v1', 'invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z', 'return v1'],
        'type': 'policy_skip',
        'search': """.method public isAvailable(Z)Z
    .registers 4

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    return v1

    :cond_0
    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    return v1
.end method""",
        'replacement': """.method public isAvailable(Z)Z
    .registers 4

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    return v1

    :cond_0
    invoke-super {p0, p1}, Lcom/android/provision/activities/DefaultActivity$State;->isAvailable(Z)Z

    return v1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
