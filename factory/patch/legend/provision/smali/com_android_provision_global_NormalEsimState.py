TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/NormalEsimState.smali'
CLASS_FALLBACK_NAMES = ['NormalEsimState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/State;', '.field private static final ESIM_ACTION:Ljava/lang/String; = "android.service.euicc.action.PROVISION_EMBEDDED_SUBSCRIPTION"', '.field private static final ESIM_ACTION_LUI:Ljava/lang/String; = "android.service.euicc.action.MANAGE_EMBEDDED_SUBSCRIPTIONS"', '.field private static final TAG:Ljava/lang/String; = "NormalEsimState"']

PATCHES = [
    {
        'id': 'com_android_provision_global_NormalEsimState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/global/State;->context:Landroid/content/Context;', 'const-string v0, "mi_lpa_tech_version"', 'const-string v1, "lui"', 'const-string v2, "com.miui.euicc"', 'invoke-static {p0, v2, v0, v1}, Lcom/android/provision/Utils;->isPackagesSupportMetaDataFeature(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Z', 'new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "getIntent: isSupportLUI "'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 4

    iget-object p0, p0, Lcom/android/provision/global/State;->context:Landroid/content/Context;

    const-string v0, "mi_lpa_tech_version"

    const-string v1, "lui"

    const-string v2, "com.miui.euicc"

    invoke-static {p0, v2, v0, v1}, Lcom/android/provision/Utils;->isPackagesSupportMetaDataFeature(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Z

    move-result p0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "getIntent: isSupportLUI "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "NormalEsimState"

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    new-instance v0, Landroid/content/Intent;

    if-eqz p0, :cond_0

    const-string p0, "android.service.euicc.action.MANAGE_EMBEDDED_SUBSCRIPTIONS"

    goto :goto_0

    :cond_0
    const-string p0, "android.service.euicc.action.PROVISION_EMBEDDED_SUBSCRIPTION"

    :goto_0
    invoke-direct {v0, p0}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string p0, "inProvision"

    const/4 v1, 0x1

    invoke-virtual {v0, p0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    const-string p0, "fromProvision"

    invoke-virtual {v0, p0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    return-object v0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 4

    goto :goto_14

    nop

    :goto_0
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_15

    nop

    :goto_1
    invoke-virtual {v0, p0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    goto :goto_19

    nop

    :goto_2
    invoke-direct {v0, p0}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    goto :goto_c

    nop

    :goto_3
    const-string p0, "android.service.euicc.action.MANAGE_EMBEDDED_SUBSCRIPTIONS"

    goto :goto_17

    nop

    :goto_4
    return-object v0

    :goto_5
    new-instance v0, Landroid/content/Intent;

    goto :goto_e

    nop

    :goto_6
    const-string v1, "lui"

    goto :goto_9

    nop

    :goto_7
    const-string p0, "android.service.euicc.action.PROVISION_EMBEDDED_SUBSCRIPTION"

    :goto_8
    goto :goto_2

    nop

    :goto_9
    const-string v2, "com.miui.euicc"

    goto :goto_11

    nop

    :goto_a
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_12

    nop

    :goto_b
    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_5

    nop

    :goto_c
    const-string p0, "inProvision"

    goto :goto_10

    nop

    :goto_d
    const-string v1, "NormalEsimState"

    goto :goto_b

    nop

    :goto_e
    if-nez p0, :cond_0

    goto :goto_18

    :cond_0
    goto :goto_3

    nop

    :goto_f
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_d

    nop

    :goto_10
    const/4 v1, 0x1

    goto :goto_1

    nop

    :goto_11
    invoke-static {p0, v2, v0, v1}, Lcom/android/provision/Utils;->isPackagesSupportMetaDataFeature(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Z

    move-result p0

    goto :goto_13

    nop

    :goto_12
    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_f

    nop

    :goto_13
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_14
    iget-object p0, p0, Lcom/android/provision/global/State;->context:Landroid/content/Context;

    goto :goto_16

    nop

    :goto_15
    const-string v1, "getIntent: isSupportLUI "

    goto :goto_a

    nop

    :goto_16
    const-string v0, "mi_lpa_tech_version"

    goto :goto_6

    nop

    :goto_17
    goto :goto_8

    :goto_18
    goto :goto_7

    nop

    :goto_19
    const-string p0, "fromProvision"

    goto :goto_1a

    nop

    :goto_1a
    invoke-virtual {v0, p0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
