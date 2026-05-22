TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/InputMethodActivity.smali'
CLASS_FALLBACK_NAMES = ['InputMethodActivity.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/BaseActivity;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_InputMethodActivity__getFragment',
        'method': '.method protected getFragment()Landroidx/fragment/app/Fragment;',
        'method_name': 'getFragment',
        'method_anchors': ['invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;', 'invoke-virtual {p0}, Lcom/android/provision/activities/InputMethodActivity;->getFragmentTag()Ljava/lang/String;', 'invoke-virtual {v0, v1}, Landroidx/fragment/app/FragmentManager;->findFragmentByTag(Ljava/lang/String;)Landroidx/fragment/app/Fragment;', 'check-cast v0, Lcom/android/provision/fragment/InputMethodFragment;', 'iput-object v0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;', 'if-nez v0, :cond_0', 'new-instance v0, Lcom/android/provision/fragment/InputMethodFragment;', 'invoke-direct {v0}, Lcom/android/provision/fragment/InputMethodFragment;-><init>()V'],
        'type': 'method_replace',
        'search': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 3

    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/provision/activities/InputMethodActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroidx/fragment/app/FragmentManager;->findFragmentByTag(Ljava/lang/String;)Landroidx/fragment/app/Fragment;

    move-result-object v0

    check-cast v0, Lcom/android/provision/fragment/InputMethodFragment;

    iput-object v0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    if-nez v0, :cond_0

    new-instance v0, Lcom/android/provision/fragment/InputMethodFragment;

    invoke-direct {v0}, Lcom/android/provision/fragment/InputMethodFragment;-><init>()V

    iput-object v0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    :cond_0
    iget-object p0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    return-object p0
.end method""",
        'replacement': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 3

    goto :goto_6

    nop

    :goto_0
    invoke-direct {v0}, Lcom/android/provision/fragment/InputMethodFragment;-><init>()V

    goto :goto_7

    nop

    :goto_1
    check-cast v0, Lcom/android/provision/fragment/InputMethodFragment;

    goto :goto_a

    nop

    :goto_2
    if-eqz v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_3

    nop

    :goto_3
    new-instance v0, Lcom/android/provision/fragment/InputMethodFragment;

    goto :goto_0

    nop

    :goto_4
    iget-object p0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    goto :goto_9

    nop

    :goto_5
    invoke-virtual {p0}, Lcom/android/provision/activities/InputMethodActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object v1

    goto :goto_b

    nop

    :goto_6
    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object v0

    goto :goto_5

    nop

    :goto_7
    iput-object v0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    :goto_8
    goto :goto_4

    nop

    :goto_9
    return-object p0

    :goto_a
    iput-object v0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    goto :goto_2

    nop

    :goto_b
    invoke-virtual {v0, v1}, Landroidx/fragment/app/FragmentManager;->findFragmentByTag(Ljava/lang/String;)Landroidx/fragment/app/Fragment;

    move-result-object v0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_InputMethodActivity__getFragmentTag',
        'method': '.method protected getFragmentTag()Ljava/lang/String;',
        'method_name': 'getFragmentTag',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    const-class p0, Lcom/android/provision/fragment/InputMethodFragment;

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
    const-class p0, Lcom/android/provision/fragment/InputMethodFragment;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_InputMethodActivity__getListDescCharSequence',
        'method': '.method protected getListDescCharSequence()Ljava/lang/CharSequence;',
        'method_name': 'getListDescCharSequence',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;', 'invoke-virtual {p0}, Lcom/android/provision/fragment/InputMethodFragment;->getPolicyDescription()Ljava/lang/CharSequence;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getListDescCharSequence()Ljava/lang/CharSequence;
    .registers 1

    iget-object p0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    invoke-virtual {p0}, Lcom/android/provision/fragment/InputMethodFragment;->getPolicyDescription()Ljava/lang/CharSequence;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getListDescCharSequence()Ljava/lang/CharSequence;
    .registers 1

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/android/provision/fragment/InputMethodFragment;->getPolicyDescription()Ljava/lang/CharSequence;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    return-object p0

    :goto_2
    iget-object p0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_InputMethodActivity__getLogoDrawableId',
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
        'id': 'com_android_provision_activities_InputMethodActivity__getTitleStringId',
        'method': '.method protected getTitleStringId()I',
        'method_name': 'getTitleStringId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$string;->input_method_setting:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringId()I
    .registers 1

    sget p0, Lcom/android/provision/R$string;->input_method_setting:I

    return p0
.end method""",
        'replacement': """.method protected getTitleStringId()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lcom/android/provision/R$string;->input_method_setting:I

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
        'id': 'com_android_provision_activities_InputMethodActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V', 'iget-object p1, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;', 'if-nez p1, :cond_0', 'invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;', 'invoke-virtual {p0}, Lcom/android/provision/activities/InputMethodActivity;->getFragmentTag()Ljava/lang/String;', 'invoke-virtual {p1, v0}, Landroidx/fragment/app/FragmentManager;->findFragmentByTag(Ljava/lang/String;)Landroidx/fragment/app/Fragment;', 'check-cast p1, Lcom/android/provision/fragment/InputMethodFragment;', 'iput-object p1, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    iget-object p1, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    if-nez p1, :cond_0

    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object p1

    invoke-virtual {p0}, Lcom/android/provision/activities/InputMethodActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Landroidx/fragment/app/FragmentManager;->findFragmentByTag(Ljava/lang/String;)Landroidx/fragment/app/Fragment;

    move-result-object p1

    check-cast p1, Lcom/android/provision/fragment/InputMethodFragment;

    iput-object p1, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    :cond_0
    const-string p1, "input_method.json"

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_a

    nop

    :goto_0
    iput-object p1, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    :goto_1
    goto :goto_b

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p1, v0}, Landroidx/fragment/app/FragmentManager;->findFragmentByTag(Ljava/lang/String;)Landroidx/fragment/app/Fragment;

    move-result-object p1

    goto :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    check-cast p1, Lcom/android/provision/fragment/InputMethodFragment;

    goto :goto_0

    nop

    :goto_6
    invoke-virtual {p0}, Lcom/android/provision/activities/InputMethodActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object v0

    goto :goto_3

    nop

    :goto_7
    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object p1

    goto :goto_6

    nop

    :goto_8
    if-eqz p1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_7

    nop

    :goto_9
    iget-object p1, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    goto :goto_8

    nop

    :goto_a
    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_9

    nop

    :goto_b
    const-string p1, "input_method.json"

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_InputMethodActivity__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onDestroy()V', 'iput-object v0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 2

    invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onDestroy()V

    const/4 v0, 0x0

    iput-object v0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    const/4 v0, 0x0

    goto :goto_3

    nop

    :goto_2
    invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onDestroy()V

    goto :goto_1

    nop

    :goto_3
    iput-object v0, p0, Lcom/android/provision/activities/InputMethodActivity;->mInputMethodFragment:Lcom/android/provision/fragment/InputMethodFragment;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
