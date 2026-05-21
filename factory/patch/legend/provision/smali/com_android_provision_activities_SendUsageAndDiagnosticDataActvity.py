TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/SendUsageAndDiagnosticDataActvity.smali'
CLASS_FALLBACK_NAMES = ['SendUsageAndDiagnosticDataActvity.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/BaseActivity;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_SendUsageAndDiagnosticDataActvity__getFragment',
        'method': '.method protected getFragment()Landroidx/fragment/app/Fragment;',
        'method_name': 'getFragment',
        'method_anchors': ['new-instance p0, Lcom/android/provision/fragment/SendUsageAndDiagnosticDataFragment;', 'invoke-direct {p0}, Lcom/android/provision/fragment/SendUsageAndDiagnosticDataFragment;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    new-instance p0, Lcom/android/provision/fragment/SendUsageAndDiagnosticDataFragment;

    invoke-direct {p0}, Lcom/android/provision/fragment/SendUsageAndDiagnosticDataFragment;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    new-instance p0, Lcom/android/provision/fragment/SendUsageAndDiagnosticDataFragment;

    goto :goto_1

    nop

    :goto_1
    invoke-direct {p0}, Lcom/android/provision/fragment/SendUsageAndDiagnosticDataFragment;-><init>()V

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
        'id': 'com_android_provision_activities_SendUsageAndDiagnosticDataActvity__getFragmentTag',
        'method': '.method protected getFragmentTag()Ljava/lang/String;',
        'method_name': 'getFragmentTag',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    const-class p0, Lcom/android/provision/fragment/SendUsageAndDiagnosticDataFragment;

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
    const-class p0, Lcom/android/provision/fragment/SendUsageAndDiagnosticDataFragment;

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
        'id': 'com_android_provision_activities_SendUsageAndDiagnosticDataActvity__getListDescCharSequence',
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
        'id': 'com_android_provision_activities_SendUsageAndDiagnosticDataActvity__getLogoDrawableId',
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
        'id': 'com_android_provision_activities_SendUsageAndDiagnosticDataActvity__getTitleStringId',
        'method': '.method protected getTitleStringId()I',
        'method_name': 'getTitleStringId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$string;->other_settings_user_experience_summary_index:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringId()I
    .registers 1

    sget p0, Lcom/android/provision/R$string;->other_settings_user_experience_summary_index:I

    return p0
.end method""",
        'replacement': """.method protected getTitleStringId()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lcom/android/provision/R$string;->other_settings_user_experience_summary_index:I

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
        'id': 'com_android_provision_activities_SendUsageAndDiagnosticDataActvity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V', 'iget-object p1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;', 'invoke-virtual {p1, v0}, Landroid/widget/Button;->setVisibility(I)V', 'iget-object p1, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;', 'invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setVisibility(I)V', 'sget p1, Lcom/android/provision/R$id;->provision_lyt_actionbar:I', 'invoke-virtual {p0, p1}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;', 'if-eqz p1, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    iget-object p1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    const/16 v0, 0x8

    invoke-virtual {p1, v0}, Landroid/widget/Button;->setVisibility(I)V

    iget-object p1, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setVisibility(I)V

    sget p1, Lcom/android/provision/R$id;->provision_lyt_actionbar:I

    invoke-virtual {p0, p1}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    if-eqz p1, :cond_0

    invoke-virtual {p1, v0}, Landroid/view/View;->setVisibility(I)V

    :cond_0
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->getAppCompatActionBar()Lmiuix/appcompat/app/ActionBar;

    move-result-object p0

    if-eqz p0, :cond_1

    const-string p1, ""

    invoke-virtual {p0, p1}, Landroidx/appcompat/app/ActionBar;->setTitle(Ljava/lang/CharSequence;)V

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/ActionBar;->setExpandState(I)V

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/ActionBar;->setResizable(Z)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_a

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    goto :goto_b

    nop

    :goto_1
    sget p1, Lcom/android/provision/R$id;->provision_lyt_actionbar:I

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0, p1}, Landroidx/appcompat/app/ActionBar;->setTitle(Ljava/lang/CharSequence;)V

    goto :goto_9

    nop

    :goto_3
    invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setVisibility(I)V

    goto :goto_1

    nop

    :goto_4
    const-string p1, ""

    goto :goto_2

    nop

    :goto_5
    invoke-virtual {p1, v0}, Landroid/view/View;->setVisibility(I)V

    :goto_6
    goto :goto_8

    nop

    :goto_7
    invoke-virtual {p1, v0}, Landroid/widget/Button;->setVisibility(I)V

    goto :goto_10

    nop

    :goto_8
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->getAppCompatActionBar()Lmiuix/appcompat/app/ActionBar;

    move-result-object p0

    goto :goto_f

    nop

    :goto_9
    const/4 p1, 0x0

    goto :goto_13

    nop

    :goto_a
    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_12

    nop

    :goto_b
    if-nez p1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_5

    nop

    :goto_c
    return-void

    :goto_d
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/ActionBar;->setResizable(Z)V

    :goto_e
    goto :goto_c

    nop

    :goto_f
    if-nez p0, :cond_1

    goto :goto_e

    :cond_1
    goto :goto_4

    nop

    :goto_10
    iget-object p1, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_3

    nop

    :goto_11
    const/16 v0, 0x8

    goto :goto_7

    nop

    :goto_12
    iget-object p1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    goto :goto_11

    nop

    :goto_13
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/ActionBar;->setExpandState(I)V

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
