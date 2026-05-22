TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/PrivacyProvisionActivity.smali'
CLASS_FALLBACK_NAMES = ['PrivacyProvisionActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/provision/ProvisionBaseActivity;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_PrivacyProvisionActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->onCreate(Landroid/os/Bundle;)V', 'invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;', 'invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;', 'sget v0, Lcom/android/provision/R$id;->provision_container:I', 'invoke-static {}, Lcom/android/provision/activities/PrivacyProvisionActivity$PrivacyProvisionFragment;->newInstance()Lcom/android/provision/activities/PrivacyProvisionActivity$PrivacyProvisionFragment;', 'invoke-virtual {p1, v0, v1}, Landroidx/fragment/app/FragmentTransaction;->replace(ILandroidx/fragment/app/Fragment;)Landroidx/fragment/app/FragmentTransaction;', 'invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commit()I', 'invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    invoke-super {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->onCreate(Landroid/os/Bundle;)V

    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object p1

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    sget v0, Lcom/android/provision/R$id;->provision_container:I

    invoke-static {}, Lcom/android/provision/activities/PrivacyProvisionActivity$PrivacyProvisionFragment;->newInstance()Lcom/android/provision/activities/PrivacyProvisionActivity$PrivacyProvisionFragment;

    move-result-object v1

    invoke-virtual {p1, v0, v1}, Landroidx/fragment/app/FragmentTransaction;->replace(ILandroidx/fragment/app/Fragment;)Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commit()I

    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object p1

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->executePendingTransactions()Z

    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    sget v0, Lcom/android/provision/R$string;->privacy_provision_title:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(Ljava/lang/CharSequence;)V

    iget-object p1, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    if-eqz p1, :cond_0

    sget v0, Lcom/android/provision/R$string;->back:I

    invoke-virtual {p0, v0}, Landroid/app/Activity;->getString(I)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p1, p0}, Landroid/widget/ImageView;->setContentDescription(Ljava/lang/CharSequence;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_6

    nop

    :goto_0
    sget v0, Lcom/android/provision/R$string;->back:I

    goto :goto_11

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p1, v0, v1}, Landroidx/fragment/app/FragmentTransaction;->replace(ILandroidx/fragment/app/Fragment;)Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    goto :goto_f

    nop

    :goto_4
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commit()I

    goto :goto_d

    nop

    :goto_5
    invoke-static {}, Lcom/android/provision/activities/PrivacyProvisionActivity$PrivacyProvisionFragment;->newInstance()Lcom/android/provision/activities/PrivacyProvisionActivity$PrivacyProvisionFragment;

    move-result-object v1

    goto :goto_2

    nop

    :goto_6
    invoke-super {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_c

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    goto :goto_13

    nop

    :goto_8
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->executePendingTransactions()Z

    goto :goto_7

    nop

    :goto_9
    invoke-virtual {p1, p0}, Landroid/widget/ImageView;->setContentDescription(Ljava/lang/CharSequence;)V

    :goto_a
    goto :goto_1

    nop

    :goto_b
    if-nez p1, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_0

    nop

    :goto_c
    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object p1

    goto :goto_3

    nop

    :goto_d
    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object p1

    goto :goto_8

    nop

    :goto_e
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p1

    goto :goto_12

    nop

    :goto_f
    sget v0, Lcom/android/provision/R$id;->provision_container:I

    goto :goto_5

    nop

    :goto_10
    iget-object p1, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_b

    nop

    :goto_11
    invoke-virtual {p0, v0}, Landroid/app/Activity;->getString(I)Ljava/lang/String;

    move-result-object p0

    goto :goto_9

    nop

    :goto_12
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(Ljava/lang/CharSequence;)V

    goto :goto_10

    nop

    :goto_13
    sget v0, Lcom/android/provision/R$string;->privacy_provision_title:I

    goto :goto_e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
