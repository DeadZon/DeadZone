TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/LanguagePickerActivity.smali'
CLASS_FALLBACK_NAMES = ['LanguagePickerActivity.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/BaseActivity;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_LanguagePickerActivity__getFragment',
        'method': '.method protected getFragment()Landroidx/fragment/app/Fragment;',
        'method_name': 'getFragment',
        'method_anchors': ['new-instance p0, Lcom/android/provision/fragment/LanguagePickerFragment;', 'invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    new-instance p0, Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    new-instance p0, Lcom/android/provision/fragment/LanguagePickerFragment;

    goto :goto_2

    nop

    :goto_2
    invoke-direct {p0}, Lcom/android/provision/fragment/LanguagePickerFragment;-><init>()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_LanguagePickerActivity__getFragmentTag',
        'method': '.method protected getFragmentTag()Ljava/lang/String;',
        'method_name': 'getFragmentTag',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    const-class p0, Lcom/android/provision/fragment/LanguagePickerFragment;

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const-class p0, Lcom/android/provision/fragment/LanguagePickerFragment;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    goto :goto_2

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_LanguagePickerActivity__getListDescCharSequence',
        'method': '.method protected getListDescCharSequence()Ljava/lang/CharSequence;',
        'method_name': 'getListDescCharSequence',
        'method_anchors': ['const-string p0, ""', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getListDescCharSequence()Ljava/lang/CharSequence;
    .registers 1

    const-string p0, ""

    return-object p0
.end method""",
        'replacement': """.method protected getListDescCharSequence()Ljava/lang/CharSequence;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const-string p0, ""

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
        'id': 'com_android_provision_activities_LanguagePickerActivity__getLogoDrawableId',
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
        'id': 'com_android_provision_activities_LanguagePickerActivity__getTitleStringId',
        'method': '.method protected getTitleStringId()I',
        'method_name': 'getTitleStringId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$string;->language_settings:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringId()I
    .registers 1

    sget p0, Lcom/android/provision/R$string;->language_settings:I

    return p0
.end method""",
        'replacement': """.method protected getTitleStringId()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    sget p0, Lcom/android/provision/R$string;->language_settings:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_LanguagePickerActivity__isOtherAnimEnd',
        'method': '.method protected isOtherAnimEnd()Z',
        'method_name': 'isOtherAnimEnd',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;', 'if-nez p0, :cond_0', 'return p0', 'invoke-virtual {p0}, Lcom/android/provision/animtool/LanguageAnimTool;->isAnimEnd()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected isOtherAnimEnd()Z
    .registers 1

    iget-object p0, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;

    if-nez p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    invoke-virtual {p0}, Lcom/android/provision/animtool/LanguageAnimTool;->isAnimEnd()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected isOtherAnimEnd()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    if-eqz p0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_6

    nop

    :goto_1
    iget-object p0, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;

    goto :goto_0

    nop

    :goto_2
    return p0

    :goto_3
    invoke-virtual {p0}, Lcom/android/provision/animtool/LanguageAnimTool;->isAnimEnd()Z

    move-result p0

    goto :goto_2

    nop

    :goto_4
    return p0

    :goto_5
    goto :goto_3

    nop

    :goto_6
    const/4 p0, 0x1

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_LanguagePickerActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V', 'const-string p1, "language.json"', 'invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V', 'invoke-direct {p0}, Lcom/android/provision/activities/LanguagePickerActivity;->initAccessibility()V', 'new-instance p1, Lcom/android/provision/animtool/LanguageAnimTool;', 'invoke-direct {p1}, Lcom/android/provision/animtool/LanguageAnimTool;-><init>()V', 'iput-object p1, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;', 'invoke-virtual {p1, p0}, Lcom/android/provision/animtool/LanguageAnimTool;->playAnim(Landroid/app/Activity;)V'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    const-string p1, "language.json"

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    invoke-direct {p0}, Lcom/android/provision/activities/LanguagePickerActivity;->initAccessibility()V

    new-instance p1, Lcom/android/provision/animtool/LanguageAnimTool;

    invoke-direct {p1}, Lcom/android/provision/animtool/LanguageAnimTool;-><init>()V

    iput-object p1, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;

    invoke-virtual {p1, p0}, Lcom/android/provision/animtool/LanguageAnimTool;->playAnim(Landroid/app/Activity;)V

    invoke-direct {p0}, Lcom/android/provision/activities/LanguagePickerActivity;->addWhiteOverlay()V

    invoke-direct {p0}, Lcom/android/provision/activities/LanguagePickerActivity;->adjustTitleLayout()V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 2

    goto :goto_9

    nop

    :goto_0
    return-void

    :goto_1
    iput-object p1, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;

    goto :goto_3

    nop

    :goto_2
    invoke-direct {p0}, Lcom/android/provision/activities/LanguagePickerActivity;->initAccessibility()V

    goto :goto_8

    nop

    :goto_3
    invoke-virtual {p1, p0}, Lcom/android/provision/animtool/LanguageAnimTool;->playAnim(Landroid/app/Activity;)V

    goto :goto_4

    nop

    :goto_4
    invoke-direct {p0}, Lcom/android/provision/activities/LanguagePickerActivity;->addWhiteOverlay()V

    goto :goto_7

    nop

    :goto_5
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    goto :goto_2

    nop

    :goto_6
    const-string p1, "language.json"

    goto :goto_5

    nop

    :goto_7
    invoke-direct {p0}, Lcom/android/provision/activities/LanguagePickerActivity;->adjustTitleLayout()V

    goto :goto_0

    nop

    :goto_8
    new-instance p1, Lcom/android/provision/animtool/LanguageAnimTool;

    goto :goto_a

    nop

    :goto_9
    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_6

    nop

    :goto_a
    invoke-direct {p1}, Lcom/android/provision/animtool/LanguageAnimTool;-><init>()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_LanguagePickerActivity__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onDestroy()V', 'iget-object v0, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lcom/android/provision/animtool/LanguageAnimTool;->destory()V', 'iput-object v0, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 2

    invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onDestroy()V

    iget-object v0, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Lcom/android/provision/animtool/LanguageAnimTool;->destory()V

    const/4 v0, 0x0

    iput-object v0, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;

    goto :goto_6

    nop

    :goto_1
    iput-object v0, p0, Lcom/android/provision/activities/LanguagePickerActivity;->languageAnimTool:Lcom/android/provision/animtool/LanguageAnimTool;

    :goto_2
    goto :goto_7

    nop

    :goto_3
    invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onDestroy()V

    goto :goto_0

    nop

    :goto_4
    invoke-virtual {v0}, Lcom/android/provision/animtool/LanguageAnimTool;->destory()V

    goto :goto_5

    nop

    :goto_5
    const/4 v0, 0x0

    goto :goto_1

    nop

    :goto_6
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_4

    nop

    :goto_7
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
