TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/WifiState.smali'
CLASS_FALLBACK_NAMES = ['WifiState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/State;', '.field private static final TAG:Ljava/lang/String; = "WifiState"']

PATCHES = [
    {
        'id': 'com_android_provision_global_WifiState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['invoke-super {p0}, Lcom/android/provision/global/State;->getIntent()Landroid/content/Intent;', 'const-string v0, "wifi_setup_wizard"', 'invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;', 'const-string v0, "eSim"', 'sget v1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimeCode:I', 'invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;', 'new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    invoke-super {p0}, Lcom/android/provision/global/State;->getIntent()Landroid/content/Intent;

    move-result-object p0

    const-string v0, "wifi_setup_wizard"

    const/4 v1, 0x1

    invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    const-string v0, "eSim"

    sget v1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimeCode:I

    invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "WifiState esim sb ->eSim  eSimeCode -> "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimeCode:I

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "WifiState"

    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    const-string v0, "eSim_GL"

    sget v1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimCode:I

    invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    return-object p0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    goto :goto_c

    nop

    :goto_0
    const-string v1, "WifiState esim sb ->eSim  eSimeCode -> "

    goto :goto_4

    nop

    :goto_1
    const-string v1, "WifiState"

    goto :goto_5

    nop

    :goto_2
    return-object p0

    :goto_3
    invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_5
    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_f

    nop

    :goto_6
    const-string v0, "eSim"

    goto :goto_13

    nop

    :goto_7
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_a

    nop

    :goto_8
    const-string v0, "wifi_setup_wizard"

    goto :goto_9

    nop

    :goto_9
    const/4 v1, 0x1

    goto :goto_11

    nop

    :goto_a
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_1

    nop

    :goto_b
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_12

    nop

    :goto_c
    invoke-super {p0}, Lcom/android/provision/global/State;->getIntent()Landroid/content/Intent;

    move-result-object p0

    goto :goto_8

    nop

    :goto_d
    invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    goto :goto_b

    nop

    :goto_e
    sget v1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimeCode:I

    goto :goto_7

    nop

    :goto_f
    const-string v0, "eSim_GL"

    goto :goto_10

    nop

    :goto_10
    sget v1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimCode:I

    goto :goto_3

    nop

    :goto_11
    invoke-virtual {p0, v0, v1}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Z)Landroid/content/Intent;

    goto :goto_6

    nop

    :goto_12
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_0

    nop

    :goto_13
    sget v1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimeCode:I

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
