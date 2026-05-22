TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$LanguageState.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$LanguageState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/DefaultActivity$State;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__LanguageState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;', 'const-string v0, "lang_show_anim"', 'invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;

    move-result-object p0

    const-string v0, "lang_show_anim"

    const/4 v1, 0x1

    invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    return-object p0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    goto :goto_4

    nop

    :goto_1
    const-string v0, "lang_show_anim"

    goto :goto_3

    nop

    :goto_2
    invoke-super {p0}, Lcom/android/provision/activities/DefaultActivity$State;->getIntent()Landroid/content/Intent;

    move-result-object p0

    goto :goto_1

    nop

    :goto_3
    const/4 v1, 0x1

    goto :goto_0

    nop

    :goto_4
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
