TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/TermsAndStatementActivity.smali'
CLASS_FALLBACK_NAMES = ['TermsAndStatementActivity.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/BaseActivity;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_TermsAndStatementActivity__getDescriptionContent',
        'method': '.method protected getDescriptionContent()Ljava/lang/CharSequence;',
        'method_name': 'getDescriptionContent',
        'method_anchors': ['invoke-super {p0}, Lcom/android/provision/activities/BaseActivity;->getDescriptionContent()Ljava/lang/CharSequence;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getDescriptionContent()Ljava/lang/CharSequence;
    .registers 1

    invoke-super {p0}, Lcom/android/provision/activities/BaseActivity;->getDescriptionContent()Ljava/lang/CharSequence;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getDescriptionContent()Ljava/lang/CharSequence;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Lcom/android/provision/activities/BaseActivity;->getDescriptionContent()Ljava/lang/CharSequence;

    move-result-object p0

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
        'id': 'com_android_provision_activities_TermsAndStatementActivity__getFragment',
        'method': '.method protected getFragment()Landroidx/fragment/app/Fragment;',
        'method_name': 'getFragment',
        'method_anchors': ['new-instance p0, Lcom/android/provision/fragment/TermsAndStatementFragment;', 'invoke-direct {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    new-instance p0, Lcom/android/provision/fragment/TermsAndStatementFragment;

    invoke-direct {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    goto :goto_2

    nop

    :goto_0
    invoke-direct {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;-><init>()V

    goto :goto_1

    nop

    :goto_1
    return-object p0

    :goto_2
    new-instance p0, Lcom/android/provision/fragment/TermsAndStatementFragment;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_TermsAndStatementActivity__getFragmentTag',
        'method': '.method protected getFragmentTag()Ljava/lang/String;',
        'method_name': 'getFragmentTag',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    const-class p0, Lcom/android/provision/activities/TermsAndStatementActivity;

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    return-object p0

    :goto_2
    const-class p0, Lcom/android/provision/activities/TermsAndStatementActivity;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_TermsAndStatementActivity__getListDescCharSequence',
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
        'id': 'com_android_provision_activities_TermsAndStatementActivity__getLogoDrawableId',
        'method': '.method protected getLogoDrawableId()I',
        'method_name': 'getLogoDrawableId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$drawable;->logo_terms:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getLogoDrawableId()I
    .registers 1

    sget p0, Lcom/android/provision/R$drawable;->logo_terms:I

    return p0
.end method""",
        'replacement': """.method protected getLogoDrawableId()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lcom/android/provision/R$drawable;->logo_terms:I

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
        'id': 'com_android_provision_activities_TermsAndStatementActivity__getTitleStringId',
        'method': '.method protected getTitleStringId()I',
        'method_name': 'getTitleStringId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$string;->terms_and_statement_title:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringId()I
    .registers 1

    sget p0, Lcom/android/provision/R$string;->terms_and_statement_title:I

    return p0
.end method""",
        'replacement': """.method protected getTitleStringId()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    sget p0, Lcom/android/provision/R$string;->terms_and_statement_title:I

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_TermsAndStatementActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V', 'const-string p1, "terms.json"', 'invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    const-string p1, "terms.json"

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    const-string p1, "terms.json"

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    goto :goto_0

    nop

    :goto_3
    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
