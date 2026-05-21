TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/LocationInformationActivity.smali'
CLASS_FALLBACK_NAMES = ['LocationInformationActivity.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/BaseActivity;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_LocationInformationActivity__getFragment',
        'method': '.method protected getFragment()Landroidx/fragment/app/Fragment;',
        'method_name': 'getFragment',
        'method_anchors': ['new-instance p0, Lcom/android/provision/fragment/LocationInformationBlankFragment;', 'invoke-direct {p0}, Lcom/android/provision/fragment/LocationInformationBlankFragment;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    new-instance p0, Lcom/android/provision/fragment/LocationInformationBlankFragment;

    invoke-direct {p0}, Lcom/android/provision/fragment/LocationInformationBlankFragment;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    new-instance p0, Lcom/android/provision/fragment/LocationInformationBlankFragment;

    goto :goto_2

    nop

    :goto_1
    return-object p0

    :goto_2
    invoke-direct {p0}, Lcom/android/provision/fragment/LocationInformationBlankFragment;-><init>()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_LocationInformationActivity__getFragmentTag',
        'method': '.method protected getFragmentTag()Ljava/lang/String;',
        'method_name': 'getFragmentTag',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    const-class p0, Lcom/android/provision/fragment/LocationInformationBlankFragment;

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const-class p0, Lcom/android/provision/fragment/LocationInformationBlankFragment;

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
        'id': 'com_android_provision_activities_LocationInformationActivity__getListDescCharSequence',
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

    goto :goto_1

    nop

    :goto_0
    return-object p0

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
        'id': 'com_android_provision_activities_LocationInformationActivity__getLogoDrawableId',
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
        'id': 'com_android_provision_activities_LocationInformationActivity__getTitleStringId',
        'method': '.method protected getTitleStringId()I',
        'method_name': 'getTitleStringId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$string;->position_header:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringId()I
    .registers 1

    sget p0, Lcom/android/provision/R$string;->position_header:I

    return p0
.end method""",
        'replacement': """.method protected getTitleStringId()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    sget p0, Lcom/android/provision/R$string;->position_header:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_LocationInformationActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V', 'sget p1, Lcom/android/provision/R$string;->location_U:I', 'invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setSubTitle(I)V', 'invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showEmergencyLocationPageText()Z', 'if-eqz p1, :cond_0', 'sget p1, Lcom/android/provision/R$string;->ktposition_header:I', 'invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(I)V', 'sget p1, Lcom/android/provision/R$string;->ktlocation_U:I'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    sget p1, Lcom/android/provision/R$string;->location_U:I

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setSubTitle(I)V

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showEmergencyLocationPageText()Z

    move-result p1

    if-eqz p1, :cond_0

    sget p1, Lcom/android/provision/R$string;->ktposition_header:I

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(I)V

    sget p1, Lcom/android/provision/R$string;->ktlocation_U:I

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setSubTitle(I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    if-nez p1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_8

    nop

    :goto_1
    sget p1, Lcom/android/provision/R$string;->ktlocation_U:I

    goto :goto_5

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(I)V

    goto :goto_1

    nop

    :goto_3
    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_9

    nop

    :goto_4
    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showEmergencyLocationPageText()Z

    move-result p1

    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setSubTitle(I)V

    :goto_6
    goto :goto_a

    nop

    :goto_7
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setSubTitle(I)V

    goto :goto_4

    nop

    :goto_8
    sget p1, Lcom/android/provision/R$string;->ktposition_header:I

    goto :goto_2

    nop

    :goto_9
    sget p1, Lcom/android/provision/R$string;->location_U:I

    goto :goto_7

    nop

    :goto_a
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
