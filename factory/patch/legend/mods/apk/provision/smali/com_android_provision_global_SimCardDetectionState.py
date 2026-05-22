TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/SimCardDetectionState.smali'
CLASS_FALLBACK_NAMES = ['SimCardDetectionState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/State;', '.field private static final TAG:Ljava/lang/String; = "SimCardDetectionState"']

PATCHES = [
    {
        'id': 'com_android_provision_global_SimCardDetectionState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['invoke-super {p0}, Lcom/android/provision/global/State;->getIntent()Landroid/content/Intent;', 'if-eqz p0, :cond_0', 'sget-boolean v0, Lmiui/enterprise/EnterpriseManagerStub;->ENTERPRISE_ACTIVATED:Z', 'if-eqz v0, :cond_0', 'const-string v0, "from_provision"', 'invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    invoke-super {p0}, Lcom/android/provision/global/State;->getIntent()Landroid/content/Intent;

    move-result-object p0

    if-eqz p0, :cond_0

    sget-boolean v0, Lmiui/enterprise/EnterpriseManagerStub;->ENTERPRISE_ACTIVATED:Z

    if-eqz v0, :cond_0

    const-string v0, "from_provision"

    const/4 v1, 0x1

    invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    :cond_0
    return-object p0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    goto :goto_6

    nop

    :goto_0
    const-string v0, "from_provision"

    goto :goto_5

    nop

    :goto_1
    sget-boolean v0, Lmiui/enterprise/EnterpriseManagerStub;->ENTERPRISE_ACTIVATED:Z

    goto :goto_8

    nop

    :goto_2
    if-nez p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_1

    nop

    :goto_3
    invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    :goto_4
    goto :goto_7

    nop

    :goto_5
    const/4 v1, 0x1

    goto :goto_3

    nop

    :goto_6
    invoke-super {p0}, Lcom/android/provision/global/State;->getIntent()Landroid/content/Intent;

    move-result-object p0

    goto :goto_2

    nop

    :goto_7
    return-object p0

    :goto_8
    if-nez v0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
