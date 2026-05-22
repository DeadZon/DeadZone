TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/KindTipActivity.smali'
CLASS_FALLBACK_NAMES = ['KindTipActivity.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/BaseActivity;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_KindTipActivity__getFragment',
        'method': '.method protected getFragment()Landroidx/fragment/app/Fragment;',
        'method_name': 'getFragment',
        'method_anchors': ['new-instance p0, Lcom/android/provision/fragment/KindTipFragment;', 'invoke-direct {p0}, Lcom/android/provision/fragment/KindTipFragment;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    new-instance p0, Lcom/android/provision/fragment/KindTipFragment;

    invoke-direct {p0}, Lcom/android/provision/fragment/KindTipFragment;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    new-instance p0, Lcom/android/provision/fragment/KindTipFragment;

    goto :goto_2

    nop

    :goto_2
    invoke-direct {p0}, Lcom/android/provision/fragment/KindTipFragment;-><init>()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_KindTipActivity__getFragmentTag',
        'method': '.method protected getFragmentTag()Ljava/lang/String;',
        'method_name': 'getFragmentTag',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    const-class p0, Lcom/android/provision/fragment/KindTipFragment;

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const-class p0, Lcom/android/provision/fragment/KindTipFragment;

    goto :goto_2

    nop

    :goto_1
    return-object p0

    :goto_2
    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_KindTipActivity__getListDescCharSequence',
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
        'id': 'com_android_provision_activities_KindTipActivity__getLogoDrawableId',
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
        'id': 'com_android_provision_activities_KindTipActivity__getTitleStringId',
        'method': '.method protected getTitleStringId()I',
        'method_name': 'getTitleStringId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$string;->kind_tip_title:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringId()I
    .registers 1

    sget p0, Lcom/android/provision/R$string;->kind_tip_title:I

    return p0
.end method""",
        'replacement': """.method protected getTitleStringId()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    sget p0, Lcom/android/provision/R$string;->kind_tip_title:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_KindTipActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V', 'sget p1, Lcom/android/provision/R$string;->kind_subtitle:I', 'invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setSubTitle(I)V', 'iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitle:Lmiuix/appcompat/widget/TextView;', 'invoke-virtual {p0, p1, v0}, Landroid/widget/TextView;->setLineSpacing(FF)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    sget p1, Lcom/android/provision/R$string;->kind_subtitle:I

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setSubTitle(I)V

    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitle:Lmiuix/appcompat/widget/TextView;

    const/4 p1, 0x0

    const v0, 0x3f8ccccd

    invoke-virtual {p0, p1, v0}, Landroid/widget/TextView;->setLineSpacing(FF)V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setSubTitle(I)V

    goto :goto_3

    nop

    :goto_1
    const v0, 0x3f8ccccd

    goto :goto_6

    nop

    :goto_2
    sget p1, Lcom/android/provision/R$string;->kind_subtitle:I

    goto :goto_0

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mSubTitle:Lmiuix/appcompat/widget/TextView;

    goto :goto_7

    nop

    :goto_4
    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_2

    nop

    :goto_5
    return-void

    :goto_6
    invoke-virtual {p0, p1, v0}, Landroid/widget/TextView;->setLineSpacing(FF)V

    goto :goto_5

    nop

    :goto_7
    const/4 p1, 0x0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
