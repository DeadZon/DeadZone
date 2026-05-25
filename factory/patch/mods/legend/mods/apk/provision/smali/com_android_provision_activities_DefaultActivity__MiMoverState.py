TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$MiMoverState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$MiMoverState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__MiMoverState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;', 'sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z', 'if-nez v0, :cond_0', 'invoke-static {}, Lcom/android/provision/miconnect/MiConnectServer;->getInstance()Lcom/android/provision/miconnect/MiConnectServer;', 'invoke-virtual {v0}, Lcom/android/provision/miconnect/MiConnectServer;->getConnectedStatus()Z', 'if-eqz v0, :cond_0', 'const-string v1, "idm_mode"', 'invoke-virtual {p0, v1, v0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;

    move-result-object p0

    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    if-nez v0, :cond_0

    invoke-static {}, Lcom/android/provision/miconnect/MiConnectServer;->getInstance()Lcom/android/provision/miconnect/MiConnectServer;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/provision/miconnect/MiConnectServer;->getConnectedStatus()Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    const-string v1, "idm_mode"

    invoke-virtual {p0, v1, v0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    return-object p0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    goto :goto_6

    nop

    :goto_0
    const/4 v0, 0x0

    :goto_1
    goto :goto_5

    nop

    :goto_2
    const/4 v0, 0x1

    goto :goto_3

    nop

    :goto_3
    goto :goto_1

    :goto_4
    goto :goto_0

    nop

    :goto_5
    const-string v1, "idm_mode"

    goto :goto_8

    nop

    :goto_6
    invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;

    move-result-object p0

    goto :goto_9

    nop

    :goto_7
    invoke-virtual {v0}, Lcom/android/provision/miconnect/MiConnectServer;->getConnectedStatus()Z

    move-result v0

    goto :goto_a

    nop

    :goto_8
    invoke-virtual {p0, v1, v0}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    goto :goto_d

    nop

    :goto_9
    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    goto :goto_b

    nop

    :goto_a
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_2

    nop

    :goto_b
    if-eqz v0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_c

    nop

    :goto_c
    invoke-static {}, Lcom/android/provision/miconnect/MiConnectServer;->getInstance()Lcom/android/provision/miconnect/MiConnectServer;

    move-result-object v0

    goto :goto_7

    nop

    :goto_d
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
