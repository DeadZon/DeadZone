TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/FingerprintActivity.smali'
CLASS_FALLBACK_NAMES = ['FingerprintActivity.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/BaseActivity;', '.field private static final TAG:Ljava/lang/String; = "FingerprintActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_FingerprintActivity__isSkipPasswordSettingPage',
        'method': '.method private isSkipPasswordSettingPage()Z',
        'method_name': 'isSkipPasswordSettingPage',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'return v1', 'invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isTransferPassword()Z', 'if-nez v0, :cond_1', 'invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z', 'if-eqz v3, :cond_1', 'if-eqz v0, :cond_3'],
        'type': 'policy_skip',
        'search': """.method private isSkipPasswordSettingPage()Z
    .registers 9

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-nez v0, :cond_0

    return v1

    :cond_0
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isTransferPassword()Z

    move-result v0

    const/4 v2, 0x1

    if-nez v0, :cond_1

    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1

    move v3, v2

    goto :goto_0

    :cond_1
    move v3, v1

    :goto_0
    if-eqz v0, :cond_3

    invoke-static {p0}, Lcom/android/provision/Utils;->hasEnrolledFace(Landroid/content/Context;)Z

    move-result v4

    if-nez v4, :cond_2

    invoke-static {p0}, Lcom/android/provision/Utils;->hasEnrolledFinger(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_3

    :cond_2
    move v4, v2

    goto :goto_1

    :cond_3
    move v4, v1

    :goto_1
    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionWorkOnlyState(Landroid/content/Context;)Z

    move-result v5

    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_6

    invoke-static {p0}, Lcom/android/provision/Utils;->hasFingerPrint(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_4

    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result v6

    if-nez v6, :cond_4

    move v6, v2

    goto :goto_2

    :cond_4
    move v6, v1

    :goto_2
    invoke-static {p0}, Lcom/android/provision/Utils;->hasFaceRecognition(Landroid/content/Context;)Z

    move-result v7

    if-eqz v7, :cond_5

    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result v7

    if-nez v7, :cond_5

    invoke-static {p0}, Lcom/android/provision/Utils;->isFaceDisabledByAdmin(Landroid/content/Context;)Z

    move-result p0

    if-nez p0, :cond_5

    move p0, v2

    goto :goto_3

    :cond_5
    move p0, v1

    :goto_3
    if-nez v6, :cond_6

    if-nez p0, :cond_6

    move p0, v2

    goto :goto_4

    :cond_6
    move p0, v1

    :goto_4
    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "isSkipPasswordSettingPage isTransferPassword: "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v0, " hasPasswordWithoutTransfer: "

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v0, " hasBiometricsWithTransfer: "

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v4}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v0, " isWorkOnlyState: "

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v5}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v0, " hasPasswordButNoBiometrics: "

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, p0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v6, "FingerprintActivity"

    invoke-static {v6, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    if-nez v3, :cond_8

    if-nez v5, :cond_8

    if-nez v4, :cond_8

    if-eqz p0, :cond_7

    goto :goto_5

    :cond_7
    return v1

    :cond_8
    :goto_5
    return v2
.end method""",
        'replacement': """.method private isSkipPasswordSettingPage()Z
    .registers 9

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-nez v0, :cond_0

    return v1

    :cond_0
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isTransferPassword()Z

    move-result v0

    const/4 v2, 0x1

    if-nez v0, :cond_1

    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1

    move v3, v2

    goto :goto_0

    :cond_1
    move v3, v1

    :goto_0
    if-eqz v0, :cond_3

    invoke-static {p0}, Lcom/android/provision/Utils;->hasEnrolledFace(Landroid/content/Context;)Z

    move-result v4

    if-nez v4, :cond_2

    invoke-static {p0}, Lcom/android/provision/Utils;->hasEnrolledFinger(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_3

    :cond_2
    move v4, v2

    goto :goto_1

    :cond_3
    move v4, v1

    :goto_1
    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionWorkOnlyState(Landroid/content/Context;)Z

    move-result v5

    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_6

    invoke-static {p0}, Lcom/android/provision/Utils;->hasFingerPrint(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_4

    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result v6

    if-nez v6, :cond_4

    move v6, v2

    goto :goto_2

    :cond_4
    move v6, v1

    :goto_2
    invoke-static {p0}, Lcom/android/provision/Utils;->hasFaceRecognition(Landroid/content/Context;)Z

    move-result v7

    if-eqz v7, :cond_5

    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result v7

    if-nez v7, :cond_5

    invoke-static {p0}, Lcom/android/provision/Utils;->isFaceDisabledByAdmin(Landroid/content/Context;)Z

    move-result p0

    if-nez p0, :cond_5

    move p0, v2

    goto :goto_3

    :cond_5
    move p0, v1

    :goto_3
    if-nez v6, :cond_6

    if-nez p0, :cond_6

    move p0, v2

    goto :goto_4

    :cond_6
    move p0, v1

    :goto_4
    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "isSkipPasswordSettingPage isTransferPassword: "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v0, " hasPasswordWithoutTransfer: "

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v0, " hasBiometricsWithTransfer: "

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v4}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v0, " isWorkOnlyState: "

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v5}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v0, " hasPasswordButNoBiometrics: "

    invoke-virtual {v6, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, p0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v6, "FingerprintActivity"

    invoke-static {v6, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    if-nez v3, :cond_8

    if-nez v5, :cond_8

    if-nez v4, :cond_8

    if-eqz p0, :cond_7

    goto :goto_5

    :cond_7
    return v1

    :cond_8
    :goto_5
    return v2
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_activities_FingerprintActivity__getFragment',
        'method': '.method protected getFragment()Landroidx/fragment/app/Fragment;',
        'method_name': 'getFragment',
        'method_anchors': ['new-instance p0, Lcom/android/provision/fragment/FingerprintFragment;', 'invoke-direct {p0}, Lcom/android/provision/fragment/FingerprintFragment;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    new-instance p0, Lcom/android/provision/fragment/FingerprintFragment;

    invoke-direct {p0}, Lcom/android/provision/fragment/FingerprintFragment;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    invoke-direct {p0}, Lcom/android/provision/fragment/FingerprintFragment;-><init>()V

    goto :goto_2

    nop

    :goto_1
    new-instance p0, Lcom/android/provision/fragment/FingerprintFragment;

    goto :goto_0

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_FingerprintActivity__getFragmentTag',
        'method': '.method protected getFragmentTag()Ljava/lang/String;',
        'method_name': 'getFragmentTag',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    const-class p0, Lcom/android/provision/fragment/FingerprintFragment;

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    const-class p0, Lcom/android/provision/fragment/FingerprintFragment;

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_FingerprintActivity__getListDescCharSequence',
        'method': '.method protected getListDescCharSequence()Ljava/lang/CharSequence;',
        'method_name': 'getListDescCharSequence',
        'method_anchors': ['return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getListDescCharSequence()Ljava/lang/CharSequence;
    .registers 1

    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected getListDescCharSequence()Ljava/lang/CharSequence;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_FingerprintActivity__getLogoDrawableId',
        'method': '.method protected getLogoDrawableId()I',
        'method_name': 'getLogoDrawableId',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getLogoDrawableId()I
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected getLogoDrawableId()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/4 p0, 0x0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_FingerprintActivity__getTitleStringId',
        'method': '.method protected getTitleStringId()I',
        'method_name': 'getTitleStringId',
        'method_anchors': ['invoke-static {p0}, Lcom/android/provision/Utils;->isFaceDisabledByAdmin(Landroid/content/Context;)Z', 'if-eqz v0, :cond_0', 'invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z', 'if-eqz v0, :cond_0', 'sget p0, Lcom/android/provision/R$string;->title_only_fingerprint:I', 'return p0', 'invoke-static {p0}, Lcom/android/provision/Utils;->isFaceDisabledByAdmin(Landroid/content/Context;)Z', 'if-eqz v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringId()I
    .registers 2

    invoke-static {p0}, Lcom/android/provision/Utils;->isFaceDisabledByAdmin(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_0

    sget p0, Lcom/android/provision/R$string;->title_only_fingerprint:I

    return p0

    :cond_0
    invoke-static {p0}, Lcom/android/provision/Utils;->isFaceDisabledByAdmin(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_1

    sget p0, Lcom/android/provision/R$string;->title_fingerprint:I

    return p0

    :cond_1
    invoke-static {p0}, Lcom/android/provision/Utils;->isFaceDisabledByAdmin(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_3

    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_3

    invoke-virtual {p0}, Landroid/app/Activity;->getApplicationContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/Utils;->hasFingerPrint(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_2

    sget p0, Lcom/android/provision/R$string;->title_fingers_and_faces:I

    return p0

    :cond_2
    sget p0, Lcom/android/provision/R$string;->title_setting_up_face:I

    return p0

    :cond_3
    sget p0, Lcom/android/provision/R$string;->title_fingerprint:I

    return p0
.end method""",
        'replacement': """.method protected getTitleStringId()I
    .registers 2

    goto :goto_b

    nop

    :goto_0
    return p0

    :goto_1
    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result v0

    goto :goto_13

    nop

    :goto_2
    return p0

    :goto_3
    goto :goto_10

    nop

    :goto_4
    if-nez p0, :cond_0

    goto :goto_1c

    :cond_0
    goto :goto_15

    nop

    :goto_5
    if-nez v0, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_17

    nop

    :goto_6
    sget p0, Lcom/android/provision/R$string;->title_fingerprint:I

    goto :goto_9

    nop

    :goto_7
    invoke-static {p0}, Lcom/android/provision/Utils;->hasFingerPrint(Landroid/content/Context;)Z

    move-result p0

    goto :goto_4

    nop

    :goto_8
    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result v0

    goto :goto_d

    nop

    :goto_9
    return p0

    :goto_a
    goto :goto_14

    nop

    :goto_b
    invoke-static {p0}, Lcom/android/provision/Utils;->isFaceDisabledByAdmin(Landroid/content/Context;)Z

    move-result v0

    goto :goto_16

    nop

    :goto_c
    if-eqz v0, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_6

    nop

    :goto_d
    if-nez v0, :cond_3

    goto :goto_3

    :cond_3
    goto :goto_12

    nop

    :goto_e
    return p0

    :goto_f
    goto :goto_11

    nop

    :goto_10
    invoke-static {p0}, Lcom/android/provision/Utils;->isFaceDisabledByAdmin(Landroid/content/Context;)Z

    move-result v0

    goto :goto_5

    nop

    :goto_11
    sget p0, Lcom/android/provision/R$string;->title_fingerprint:I

    goto :goto_0

    nop

    :goto_12
    sget p0, Lcom/android/provision/R$string;->title_only_fingerprint:I

    goto :goto_2

    nop

    :goto_13
    if-nez v0, :cond_4

    goto :goto_f

    :cond_4
    goto :goto_1a

    nop

    :goto_14
    invoke-static {p0}, Lcom/android/provision/Utils;->isFaceDisabledByAdmin(Landroid/content/Context;)Z

    move-result v0

    goto :goto_19

    nop

    :goto_15
    sget p0, Lcom/android/provision/R$string;->title_fingers_and_faces:I

    goto :goto_1b

    nop

    :goto_16
    if-nez v0, :cond_5

    goto :goto_3

    :cond_5
    goto :goto_8

    nop

    :goto_17
    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result v0

    goto :goto_c

    nop

    :goto_18
    sget p0, Lcom/android/provision/R$string;->title_setting_up_face:I

    goto :goto_e

    nop

    :goto_19
    if-eqz v0, :cond_6

    goto :goto_f

    :cond_6
    goto :goto_1

    nop

    :goto_1a
    invoke-virtual {p0}, Landroid/app/Activity;->getApplicationContext()Landroid/content/Context;

    move-result-object p0

    goto :goto_7

    nop

    :goto_1b
    return p0

    :goto_1c
    goto :goto_18

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_FingerprintActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V', 'invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isExecuteOncePasswordPage()Z', 'if-nez p1, :cond_1', 'invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z', 'if-eqz p1, :cond_0', 'invoke-static {v0}, Lcom/android/provision/DefaultPreferenceHelper;->setFirstEntryPasswordPage(Z)V', 'invoke-static {v0}, Lcom/android/provision/DefaultPreferenceHelper;->setExecuteOncePasswordPage(Z)V', 'invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isTransferPassword()Z'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isExecuteOncePasswordPage()Z

    move-result p1

    const/4 v0, 0x1

    if-nez p1, :cond_1

    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_0

    invoke-static {v0}, Lcom/android/provision/DefaultPreferenceHelper;->setFirstEntryPasswordPage(Z)V

    :cond_0
    invoke-static {v0}, Lcom/android/provision/DefaultPreferenceHelper;->setExecuteOncePasswordPage(Z)V

    :cond_1
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isTransferPassword()Z

    move-result p1

    if-nez p1, :cond_2

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_2

    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_2

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isFirstEntryPasswordPage()Z

    move-result p1

    if-eqz p1, :cond_2

    invoke-static {v0}, Lcom/android/provision/DefaultPreferenceHelper;->setTransferPassword(Z)V

    :cond_2
    invoke-direct {p0}, Lcom/android/provision/activities/FingerprintActivity;->isSkipPasswordSettingPage()Z

    move-result p1

    if-eqz p1, :cond_3

    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    const/4 v0, -0x1

    invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->finish()V

    return-void

    :cond_3
    const-string p1, "password.json"

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_4

    sput-object p0, Lcom/android/provision/Utils;->FINGER_PRINT_POINT:Landroid/app/Activity;

    :cond_4
    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_19

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    goto :goto_16

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    goto :goto_5

    nop

    :goto_2
    if-nez p1, :cond_0

    goto :goto_15

    :cond_0
    goto :goto_b

    nop

    :goto_3
    if-eqz p1, :cond_1

    goto :goto_15

    :cond_1
    goto :goto_a

    nop

    :goto_4
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isExecuteOncePasswordPage()Z

    move-result p1

    goto :goto_22

    nop

    :goto_5
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    goto :goto_12

    nop

    :goto_6
    invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    goto :goto_20

    nop

    :goto_7
    return-void

    :goto_8
    goto :goto_1a

    nop

    :goto_9
    if-nez p1, :cond_2

    goto :goto_15

    :cond_2
    goto :goto_11

    nop

    :goto_a
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    goto :goto_9

    nop

    :goto_b
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isFirstEntryPasswordPage()Z

    move-result p1

    goto :goto_c

    nop

    :goto_c
    if-nez p1, :cond_3

    goto :goto_15

    :cond_3
    goto :goto_14

    nop

    :goto_d
    sput-object p0, Lcom/android/provision/Utils;->FINGER_PRINT_POINT:Landroid/app/Activity;

    :goto_e
    goto :goto_18

    nop

    :goto_f
    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result p1

    goto :goto_10

    nop

    :goto_10
    if-nez p1, :cond_4

    goto :goto_1f

    :cond_4
    goto :goto_1e

    nop

    :goto_11
    invoke-static {p0}, Landroid/provider/MiuiSettings$Secure;->hasCommonPassword(Landroid/content/Context;)Z

    move-result p1

    goto :goto_2

    nop

    :goto_12
    if-nez p1, :cond_5

    goto :goto_e

    :cond_5
    goto :goto_d

    nop

    :goto_13
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isTransferPassword()Z

    move-result p1

    goto :goto_3

    nop

    :goto_14
    invoke-static {v0}, Lcom/android/provision/DefaultPreferenceHelper;->setTransferPassword(Z)V

    :goto_15
    goto :goto_21

    nop

    :goto_16
    const/4 v0, -0x1

    goto :goto_6

    nop

    :goto_17
    if-eqz p1, :cond_6

    goto :goto_1c

    :cond_6
    goto :goto_f

    nop

    :goto_18
    return-void

    :goto_19
    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_4

    nop

    :goto_1a
    const-string p1, "password.json"

    goto :goto_1

    nop

    :goto_1b
    invoke-static {v0}, Lcom/android/provision/DefaultPreferenceHelper;->setExecuteOncePasswordPage(Z)V

    :goto_1c
    goto :goto_13

    nop

    :goto_1d
    if-nez p1, :cond_7

    goto :goto_8

    :cond_7
    goto :goto_0

    nop

    :goto_1e
    invoke-static {v0}, Lcom/android/provision/DefaultPreferenceHelper;->setFirstEntryPasswordPage(Z)V

    :goto_1f
    goto :goto_1b

    nop

    :goto_20
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->finish()V

    goto :goto_7

    nop

    :goto_21
    invoke-direct {p0}, Lcom/android/provision/activities/FingerprintActivity;->isSkipPasswordSettingPage()Z

    move-result p1

    goto :goto_1d

    nop

    :goto_22
    const/4 v0, 0x1

    goto :goto_17

    nop
.end method""",
        'required': True,
        'policy_status': 'BUILD_FLAG_PARTIALLY_SKIPPED',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_FingerprintActivity__onResume',
        'method': '.method protected onResume()V',
        'method_name': 'onResume',
        'method_anchors': ['invoke-super {p0}, Lcom/android/provision/activities/BaseActivity;->onResume()V', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0, v0}, Lmiuix/provision/ProvisionBaseActivity;->updateButtonState(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onResume()V
    .registers 2

    invoke-super {p0}, Lcom/android/provision/activities/BaseActivity;->onResume()V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    invoke-virtual {p0, v0}, Lmiuix/provision/ProvisionBaseActivity;->updateButtonState(Z)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onResume()V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_4

    nop

    :goto_1
    return-void

    :goto_2
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    goto :goto_0

    nop

    :goto_3
    invoke-super {p0}, Lcom/android/provision/activities/BaseActivity;->onResume()V

    goto :goto_2

    nop

    :goto_4
    const/4 v0, 0x1

    goto :goto_5

    nop

    :goto_5
    invoke-virtual {p0, v0}, Lmiuix/provision/ProvisionBaseActivity;->updateButtonState(Z)V

    :goto_6
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': 'BUILD_FLAG_PARTIALLY_SKIPPED',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
