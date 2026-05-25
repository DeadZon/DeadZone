TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/SimCardDetectionActivity.smali'
CLASS_FALLBACK_NAMES = ['SimCardDetectionActivity.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/BaseActivity;', '.field public static final IS_FROM_PHONE_ACTIVATION:Ljava/lang/String; = "from_phone_activation"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_SimCardDetectionActivity__additionalProcess',
        'method': '.method protected additionalProcess()V',
        'method_name': 'additionalProcess',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z', 'if-eqz v0, :cond_0', 'new-instance v0, Landroid/content/Intent;', 'invoke-direct {v0}, Landroid/content/Intent;-><init>()V', 'const-string v1, "eSim_GL"', 'invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;', 'invoke-virtual {p0, v1, v0}, Landroid/app/Activity;->setResult(ILandroid/content/Intent;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected additionalProcess()V
    .registers 4

    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result v0

    if-eqz v0, :cond_0

    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    const-string v1, "eSim_GL"

    const/4 v2, 0x2

    invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    const/4 v1, 0x0

    invoke-virtual {p0, v1, v0}, Landroid/app/Activity;->setResult(ILandroid/content/Intent;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected additionalProcess()V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    new-instance v0, Landroid/content/Intent;

    goto :goto_1

    nop

    :goto_1
    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    goto :goto_6

    nop

    :goto_2
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result v0

    goto :goto_a

    nop

    :goto_3
    invoke-virtual {p0, v1, v0}, Landroid/app/Activity;->setResult(ILandroid/content/Intent;)V

    :goto_4
    goto :goto_8

    nop

    :goto_5
    const/4 v1, 0x0

    goto :goto_3

    nop

    :goto_6
    const-string v1, "eSim_GL"

    goto :goto_7

    nop

    :goto_7
    const/4 v2, 0x2

    goto :goto_9

    nop

    :goto_8
    return-void

    :goto_9
    invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    goto :goto_5

    nop

    :goto_a
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_SimCardDetectionActivity__getFragment',
        'method': '.method protected getFragment()Landroidx/fragment/app/Fragment;',
        'method_name': 'getFragment',
        'method_anchors': ['new-instance p0, Lcom/android/provision/fragment/SimCardDetectionFragment;', 'invoke-direct {p0}, Lcom/android/provision/fragment/SimCardDetectionFragment;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    new-instance p0, Lcom/android/provision/fragment/SimCardDetectionFragment;

    invoke-direct {p0}, Lcom/android/provision/fragment/SimCardDetectionFragment;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    goto :goto_2

    nop

    :goto_0
    invoke-direct {p0}, Lcom/android/provision/fragment/SimCardDetectionFragment;-><init>()V

    goto :goto_1

    nop

    :goto_1
    return-object p0

    :goto_2
    new-instance p0, Lcom/android/provision/fragment/SimCardDetectionFragment;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_SimCardDetectionActivity__getFragmentTag',
        'method': '.method protected getFragmentTag()Ljava/lang/String;',
        'method_name': 'getFragmentTag',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    const-class p0, Lcom/android/provision/fragment/SimCardDetectionFragment;

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    goto :goto_2

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    goto :goto_0

    nop

    :goto_2
    const-class p0, Lcom/android/provision/fragment/SimCardDetectionFragment;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_SimCardDetectionActivity__getListDescCharSequence',
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
        'id': 'com_android_provision_activities_SimCardDetectionActivity__getLogoDrawableId',
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
        'id': 'com_android_provision_activities_SimCardDetectionActivity__getTitleStringId',
        'method': '.method protected getTitleStringId()I',
        'method_name': 'getTitleStringId',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringId()I
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected getTitleStringId()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_SimCardDetectionActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V', 'const-string p1, "SimCardDetectionFragment "', 'const-string v0, " here is SimCardDetectionFragment\\\'s onCreate "', 'invoke-static {p1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I', 'const-string p1, "no_sim_card.json"', 'invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V', 'invoke-direct {p0}, Lcom/android/provision/activities/SimCardDetectionActivity;->initGroupButtons()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    const-string p1, "SimCardDetectionFragment "

    const-string v0, " here is SimCardDetectionFragment\'s onCreate "

    invoke-static {p1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    const-string p1, "no_sim_card.json"

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    invoke-direct {p0}, Lcom/android/provision/activities/SimCardDetectionActivity;->initGroupButtons()V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    const-string p1, "no_sim_card.json"

    goto :goto_6

    nop

    :goto_1
    invoke-static {p1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    nop

    :goto_2
    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_3

    nop

    :goto_3
    const-string p1, "SimCardDetectionFragment "

    goto :goto_4

    nop

    :goto_4
    const-string v0, " here is SimCardDetectionFragment\'s onCreate "

    goto :goto_1

    nop

    :goto_5
    return-void

    :goto_6
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    goto :goto_7

    nop

    :goto_7
    invoke-direct {p0}, Lcom/android/provision/activities/SimCardDetectionActivity;->initGroupButtons()V

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
