TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/BaseActivity.smali'
CLASS_FALLBACK_NAMES = ['BaseActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/provision/ProvisionBaseActivity;', '.field public static final EMPTY_STRING:Ljava/lang/String; = " "', '.field public static final EXTRA_DISABLE_BACK:Ljava/lang/String; = "extra_disable_back"', '.field public static final EXTRA_TO_NEXT:Ljava/lang/String; = "extra_to_next"', '.field private static final TAG:Ljava/lang/String; = "BaseActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_BaseActivity__additionalProcess',
        'method': '.method protected additionalProcess()V',
        'method_name': 'additionalProcess',
        'method_anchors': ['invoke-virtual {p0, v0}, Landroid/app/Activity;->setResult(I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected additionalProcess()V
    .registers 2

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Landroid/app/Activity;->setResult(I)V

    return-void
.end method""",
        'replacement': """.method protected additionalProcess()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, v0}, Landroid/app/Activity;->setResult(I)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_BaseActivity__getDescriptionContent',
        'method': '.method protected getDescriptionContent()Ljava/lang/CharSequence;',
        'method_name': 'getDescriptionContent',
        'method_anchors': ['return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getDescriptionContent()Ljava/lang/CharSequence;
    .registers 1

    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected getDescriptionContent()Ljava/lang/CharSequence;
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
        'id': 'com_android_provision_activities_BaseActivity__getTitleStringText',
        'method': '.method protected getTitleStringText()Ljava/lang/String;',
        'method_name': 'getTitleStringText',
        'method_anchors': ['const-string p0, ""', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringText()Ljava/lang/String;
    .registers 1

    const-string p0, ""

    return-object p0
.end method""",
        'replacement': """.method protected getTitleStringText()Ljava/lang/String;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    const-string p0, ""

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_BaseActivity__isNeedDefaultPadding',
        'method': '.method protected isNeedDefaultPadding()Z',
        'method_name': 'isNeedDefaultPadding',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected isNeedDefaultPadding()Z
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected isNeedDefaultPadding()Z
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
        'id': 'com_android_provision_activities_BaseActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->onCreate(Landroid/os/Bundle;)V', 'invoke-static {}, Lcom/android/provision/Utils;->isFoldDevice()Z', 'if-nez p1, :cond_0', 'invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z', 'if-nez p1, :cond_0', 'invoke-static {p0}, Lcom/android/provision/utils/NotchAdapterUtils;->fitNotchForFullScreen(Landroid/app/Activity;)V', 'invoke-static {p0}, Lcom/android/provision/Utils;->isProvisioned(Landroid/content/Context;)Z', 'if-eqz p1, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 5

    invoke-super {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->onCreate(Landroid/os/Bundle;)V

    invoke-static {}, Lcom/android/provision/Utils;->isFoldDevice()Z

    move-result p1

    if-nez p1, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result p1

    if-nez p1, :cond_0

    invoke-static {p0}, Lcom/android/provision/utils/NotchAdapterUtils;->fitNotchForFullScreen(Landroid/app/Activity;)V

    :cond_0
    invoke-static {p0}, Lcom/android/provision/Utils;->isProvisioned(Landroid/content/Context;)Z

    move-result p1

    const/4 v0, -0x1

    if-eqz p1, :cond_1

    invoke-virtual {p0, v0}, Landroid/app/Activity;->setResult(I)V

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->finish()V

    return-void

    :cond_1
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    const-string v1, "extra_disable_back"

    const/4 v2, 0x0

    invoke-virtual {p1, v1, v2}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result p1

    iput-boolean p1, p0, Lcom/android/provision/activities/BaseActivity;->mIsDisableBack:Z

    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object p1

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->isDestroyed()Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-virtual {p0, v0}, Landroid/app/Activity;->setResult(I)V

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->finish()V

    return-void

    :cond_2
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Landroidx/fragment/app/FragmentManager;->findFragmentByTag(Ljava/lang/String;)Landroidx/fragment/app/Fragment;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/activities/BaseActivity;->mFragment:Landroidx/fragment/app/Fragment;

    if-nez v0, :cond_3

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getFragment()Landroidx/fragment/app/Fragment;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/activities/BaseActivity;->mFragment:Landroidx/fragment/app/Fragment;

    sget v1, Lcom/android/provision/R$id;->provision_container:I

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {p1, v1, v0, v2}, Landroidx/fragment/app/FragmentTransaction;->replace(ILandroidx/fragment/app/Fragment;Ljava/lang/String;)Landroidx/fragment/app/FragmentTransaction;

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commit()I

    :cond_3
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringId()I

    move-result p1

    if-lez p1, :cond_5

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringId()I

    move-result p1

    sget v0, Lcom/android/provision/R$string;->multisim_settings_title:I

    if-ne p1, v0, :cond_4

    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p1

    const/4 v0, 0x2

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    filled-new-array {v0}, [Ljava/lang/Object;

    move-result-object v0

    invoke-static {p1, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(Ljava/lang/CharSequence;)V

    goto :goto_0

    :cond_4
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringId()I

    move-result p1

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(I)V

    goto :goto_0

    :cond_5
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result p1

    if-eqz p1, :cond_6

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    if-eqz p1, :cond_7

    :cond_6
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result p1

    if-eqz p1, :cond_8

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    if-nez p1, :cond_8

    :cond_7
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(Ljava/lang/CharSequence;)V

    :cond_8
    :goto_0
    invoke-direct {p0}, Lcom/android/provision/activities/BaseActivity;->disableWindowInsetsListener()V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 5

    goto :goto_28

    nop

    :goto_0
    if-nez p1, :cond_0

    goto :goto_37

    :cond_0
    goto :goto_15

    nop

    :goto_1
    sget v1, Lcom/android/provision/R$id;->provision_container:I

    goto :goto_17

    nop

    :goto_2
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->finish()V

    goto :goto_e

    nop

    :goto_3
    filled-new-array {v0}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_c

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    goto :goto_18

    nop

    :goto_5
    goto :goto_46

    :goto_6
    goto :goto_b

    nop

    :goto_7
    iput-object v0, p0, Lcom/android/provision/activities/BaseActivity;->mFragment:Landroidx/fragment/app/Fragment;

    goto :goto_1

    nop

    :goto_8
    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object p1

    goto :goto_12

    nop

    :goto_9
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringId()I

    move-result p1

    goto :goto_20

    nop

    :goto_a
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p1

    goto :goto_1e

    nop

    :goto_b
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result p1

    goto :goto_31

    nop

    :goto_c
    invoke-static {p1, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p1

    goto :goto_2d

    nop

    :goto_d
    invoke-direct {p0}, Lcom/android/provision/activities/BaseActivity;->disableWindowInsetsListener()V

    goto :goto_3a

    nop

    :goto_e
    return-void

    :goto_f
    goto :goto_47

    nop

    :goto_10
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringId()I

    move-result p1

    goto :goto_22

    nop

    :goto_11
    if-eqz p1, :cond_1

    goto :goto_24

    :cond_1
    goto :goto_23

    nop

    :goto_12
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->isDestroyed()Z

    move-result v1

    goto :goto_1c

    nop

    :goto_13
    invoke-virtual {p0, v0}, Landroid/app/Activity;->setResult(I)V

    goto :goto_2

    nop

    :goto_14
    invoke-virtual {p1, v0}, Landroidx/fragment/app/FragmentManager;->findFragmentByTag(Ljava/lang/String;)Landroidx/fragment/app/Fragment;

    move-result-object v0

    goto :goto_2b

    nop

    :goto_15
    invoke-virtual {p0, v0}, Landroid/app/Activity;->setResult(I)V

    goto :goto_3c

    nop

    :goto_16
    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    goto :goto_40

    nop

    :goto_17
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object v2

    goto :goto_32

    nop

    :goto_18
    const-string v1, "extra_disable_back"

    goto :goto_25

    nop

    :goto_19
    if-eqz p1, :cond_2

    goto :goto_24

    :cond_2
    goto :goto_27

    nop

    :goto_1a
    if-eq p1, v0, :cond_3

    goto :goto_43

    :cond_3
    goto :goto_1f

    nop

    :goto_1b
    if-eqz v0, :cond_4

    goto :goto_30

    :cond_4
    goto :goto_44

    nop

    :goto_1c
    if-nez v1, :cond_5

    goto :goto_f

    :cond_5
    goto :goto_13

    nop

    :goto_1d
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_3

    nop

    :goto_1e
    const/4 v0, 0x2

    goto :goto_1d

    nop

    :goto_1f
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    goto :goto_a

    nop

    :goto_20
    sget v0, Lcom/android/provision/R$string;->multisim_settings_title:I

    goto :goto_1a

    nop

    :goto_21
    invoke-virtual {p1, v1, v2}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result p1

    goto :goto_39

    nop

    :goto_22
    if-gtz p1, :cond_6

    goto :goto_6

    :cond_6
    goto :goto_9

    nop

    :goto_23
    invoke-static {p0}, Lcom/android/provision/utils/NotchAdapterUtils;->fitNotchForFullScreen(Landroid/app/Activity;)V

    :goto_24
    goto :goto_38

    nop

    :goto_25
    const/4 v2, 0x0

    goto :goto_21

    nop

    :goto_26
    if-nez p1, :cond_7

    goto :goto_46

    :cond_7
    goto :goto_3b

    nop

    :goto_27
    invoke-static {}, Lcom/android/provision/Utils;->isTabletDevice()Z

    move-result p1

    goto :goto_11

    nop

    :goto_28
    invoke-super {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_33

    nop

    :goto_29
    if-nez p1, :cond_8

    goto :goto_41

    :cond_8
    :goto_2a
    goto :goto_3e

    nop

    :goto_2b
    iput-object v0, p0, Lcom/android/provision/activities/BaseActivity;->mFragment:Landroidx/fragment/app/Fragment;

    goto :goto_1b

    nop

    :goto_2c
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getFragment()Landroidx/fragment/app/Fragment;

    move-result-object v0

    goto :goto_7

    nop

    :goto_2d
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(Ljava/lang/CharSequence;)V

    goto :goto_42

    nop

    :goto_2e
    const/4 v0, -0x1

    goto :goto_0

    nop

    :goto_2f
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commit()I

    :goto_30
    goto :goto_10

    nop

    :goto_31
    if-nez p1, :cond_9

    goto :goto_2a

    :cond_9
    goto :goto_34

    nop

    :goto_32
    invoke-virtual {p1, v1, v0, v2}, Landroidx/fragment/app/FragmentTransaction;->replace(ILandroidx/fragment/app/Fragment;Ljava/lang/String;)Landroidx/fragment/app/FragmentTransaction;

    goto :goto_2f

    nop

    :goto_33
    invoke-static {}, Lcom/android/provision/Utils;->isFoldDevice()Z

    move-result p1

    goto :goto_19

    nop

    :goto_34
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object p1

    goto :goto_35

    nop

    :goto_35
    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    goto :goto_29

    nop

    :goto_36
    return-void

    :goto_37
    goto :goto_4

    nop

    :goto_38
    invoke-static {p0}, Lcom/android/provision/Utils;->isProvisioned(Landroid/content/Context;)Z

    move-result p1

    goto :goto_2e

    nop

    :goto_39
    iput-boolean p1, p0, Lcom/android/provision/activities/BaseActivity;->mIsDisableBack:Z

    goto :goto_8

    nop

    :goto_3a
    return-void

    :goto_3b
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object p1

    goto :goto_16

    nop

    :goto_3c
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->finish()V

    goto :goto_36

    nop

    :goto_3d
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringId()I

    move-result p1

    goto :goto_3f

    nop

    :goto_3e
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result p1

    goto :goto_26

    nop

    :goto_3f
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(I)V

    goto :goto_5

    nop

    :goto_40
    if-eqz p1, :cond_a

    goto :goto_46

    :cond_a
    :goto_41
    goto :goto_48

    nop

    :goto_42
    goto :goto_46

    :goto_43
    goto :goto_3d

    nop

    :goto_44
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    goto :goto_2c

    nop

    :goto_45
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setTitle(Ljava/lang/CharSequence;)V

    :goto_46
    goto :goto_d

    nop

    :goto_47
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object v0

    goto :goto_14

    nop

    :goto_48
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object p1

    goto :goto_45

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_BaseActivity__onPause',
        'method': '.method protected onPause()V',
        'method_name': 'onPause',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onPause()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onPause()V
    .registers 1

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onPause()V

    return-void
.end method""",
        'replacement': """.method protected onPause()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onPause()V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_BaseActivity__onResume',
        'method': '.method protected onResume()V',
        'method_name': 'onResume',
        'method_anchors': ['invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onResume()V', 'iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitle:Lmiuix/appcompat/widget/TextView;', 'if-eqz v0, :cond_5', 'invoke-static {}, Lcom/android/provision/Utils;->isRTL()Z', 'if-eqz v3, :cond_0', 'invoke-virtual {v0, v3}, Landroid/view/View;->setTextDirection(I)V', 'invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringId()I', 'if-lez v3, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected onResume()V
    .registers 8

    invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onResume()V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitle:Lmiuix/appcompat/widget/TextView;

    const/4 v1, 0x3

    const/4 v2, 0x4

    if-eqz v0, :cond_5

    invoke-static {}, Lcom/android/provision/Utils;->isRTL()Z

    move-result v3

    if-eqz v3, :cond_0

    move v3, v2

    goto :goto_0

    :cond_0
    move v3, v1

    :goto_0
    invoke-virtual {v0, v3}, Landroid/view/View;->setTextDirection(I)V

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringId()I

    move-result v3

    if-lez v3, :cond_2

    sget v4, Lcom/android/provision/R$string;->multisim_settings_title:I

    if-ne v3, v4, :cond_1

    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    invoke-virtual {v3, v4}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v3

    const/4 v4, 0x2

    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    filled-new-array {v4}, [Ljava/lang/Object;

    move-result-object v4

    invoke-static {v3, v4}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v0, v3}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    goto :goto_1

    :cond_1
    invoke-virtual {v0, v3}, Landroid/widget/TextView;->setText(I)V

    goto :goto_1

    :cond_2
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result v3

    if-eqz v3, :cond_3

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object v3

    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    if-eqz v3, :cond_4

    :cond_3
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result v3

    if-eqz v3, :cond_5

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object v3

    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    if-nez v3, :cond_5

    :cond_4
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v0, v3}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    :cond_5
    :goto_1
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    if-eqz v0, :cond_6

    iget-boolean v0, p0, Lcom/android/provision/activities/BaseActivity;->mIsDisableBack:Z

    if-nez v0, :cond_6

    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->hasPreview()Z

    move-result v0

    if-nez v0, :cond_6

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    iget-object v3, p0, Lcom/android/provision/activities/BaseActivity;->mBackListener:Landroid/view/View$OnClickListener;

    invoke-virtual {v0, v3}, Landroid/widget/ImageView;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    :cond_6
    iget-object v0, p0, Lcom/android/provision/activities/BaseActivity;->mFragment:Landroidx/fragment/app/Fragment;

    if-eqz v0, :cond_c

    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getView()Landroid/view/View;

    move-result-object v0

    sget v3, Lcom/android/provision/R$id;->list_description:I

    invoke-virtual {v0, v3}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    const/16 v3, 0x8

    const/4 v4, 0x0

    if-eqz v0, :cond_9

    instance-of v5, v0, Landroid/widget/TextView;

    if-eqz v5, :cond_9

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getListDescCharSequence()Ljava/lang/CharSequence;

    move-result-object v5

    if-eqz v5, :cond_8

    invoke-static {}, Lcom/android/provision/Utils;->isRTL()Z

    move-result v6

    if-eqz v6, :cond_7

    move v6, v2

    goto :goto_2

    :cond_7
    move v6, v1

    :goto_2
    invoke-virtual {v0, v6}, Landroid/view/View;->setTextDirection(I)V

    move-object v6, v0

    check-cast v6, Landroid/widget/TextView;

    invoke-virtual {v6, v5}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    invoke-virtual {v0, v4}, Landroid/view/View;->setVisibility(I)V

    instance-of v0, p0, Lcom/android/provision/activities/InputMethodActivity;

    if-eqz v0, :cond_9

    invoke-static {}, Landroid/text/method/LinkMovementMethod;->getInstance()Landroid/text/method/MovementMethod;

    move-result-object v0

    invoke-virtual {v6, v0}, Landroid/widget/TextView;->setMovementMethod(Landroid/text/method/MovementMethod;)V

    goto :goto_3

    :cond_8
    invoke-virtual {v0, v3}, Landroid/view/View;->setVisibility(I)V

    :cond_9
    :goto_3
    iget-object v0, p0, Lcom/android/provision/activities/BaseActivity;->mFragment:Landroidx/fragment/app/Fragment;

    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getView()Landroid/view/View;

    move-result-object v0

    sget v5, Lcom/android/provision/R$id;->description:I

    invoke-virtual {v0, v5}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_c

    instance-of v5, v0, Landroid/widget/TextView;

    if-eqz v5, :cond_c

    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getDescriptionContent()Ljava/lang/CharSequence;

    move-result-object p0

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v5

    if-nez v5, :cond_b

    invoke-static {}, Lcom/android/provision/Utils;->isRTL()Z

    move-result v3

    if-eqz v3, :cond_a

    move v1, v2

    :cond_a
    invoke-virtual {v0, v1}, Landroid/view/View;->setTextDirection(I)V

    move-object v1, v0

    check-cast v1, Landroid/widget/TextView;

    invoke-virtual {v1, p0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    invoke-virtual {v0, v4}, Landroid/view/View;->setVisibility(I)V

    return-void

    :cond_b
    invoke-virtual {v0, v3}, Landroid/view/View;->setVisibility(I)V

    :cond_c
    return-void
.end method""",
        'replacement': """.method protected onResume()V
    .registers 8

    goto :goto_b

    nop

    :goto_0
    sget v3, Lcom/android/provision/R$id;->list_description:I

    goto :goto_17

    nop

    :goto_1
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result v3

    goto :goto_15

    nop

    :goto_2
    invoke-virtual {v0, v6}, Landroid/view/View;->setTextDirection(I)V

    goto :goto_6d

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_16

    nop

    :goto_4
    invoke-virtual {v0, v3}, Landroid/view/View;->setVisibility(I)V

    :goto_5
    goto :goto_34

    nop

    :goto_6
    sget v5, Lcom/android/provision/R$id;->description:I

    goto :goto_63

    nop

    :goto_7
    return-void

    :goto_8
    goto :goto_4

    nop

    :goto_9
    if-eqz v3, :cond_1

    goto :goto_2d

    :cond_1
    :goto_a
    goto :goto_14

    nop

    :goto_b
    invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onResume()V

    goto :goto_44

    nop

    :goto_c
    invoke-virtual {v0, v3}, Landroid/view/View;->setVisibility(I)V

    :goto_d
    goto :goto_26

    nop

    :goto_e
    move v3, v1

    :goto_f
    goto :goto_30

    nop

    :goto_10
    goto :goto_d

    :goto_11
    goto :goto_c

    nop

    :goto_12
    if-eqz v0, :cond_2

    goto :goto_49

    :cond_2
    goto :goto_1a

    nop

    :goto_13
    const/4 v4, 0x2

    goto :goto_65

    nop

    :goto_14
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object v3

    goto :goto_2c

    nop

    :goto_15
    if-nez v3, :cond_3

    goto :goto_1e

    :cond_3
    goto :goto_36

    nop

    :goto_16
    instance-of v5, v0, Landroid/widget/TextView;

    goto :goto_23

    nop

    :goto_17
    invoke-virtual {v0, v3}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_61

    nop

    :goto_18
    goto :goto_2d

    :goto_19
    goto :goto_1

    nop

    :goto_1a
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_6c

    nop

    :goto_1b
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getDescriptionContent()Ljava/lang/CharSequence;

    move-result-object p0

    goto :goto_32

    nop

    :goto_1c
    invoke-virtual {v6, v5}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    goto :goto_20

    nop

    :goto_1d
    if-nez v3, :cond_4

    goto :goto_a

    :cond_4
    :goto_1e
    goto :goto_58

    nop

    :goto_1f
    if-nez v0, :cond_5

    goto :goto_d

    :cond_5
    goto :goto_5b

    nop

    :goto_20
    invoke-virtual {v0, v4}, Landroid/view/View;->setVisibility(I)V

    goto :goto_43

    nop

    :goto_21
    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    goto :goto_1d

    nop

    :goto_22
    const/4 v2, 0x4

    goto :goto_25

    nop

    :goto_23
    if-nez v5, :cond_6

    goto :goto_d

    :cond_6
    goto :goto_50

    nop

    :goto_24
    invoke-virtual {v0, v4}, Landroid/view/View;->setVisibility(I)V

    goto :goto_7

    nop

    :goto_25
    if-nez v0, :cond_7

    goto :goto_2d

    :cond_7
    goto :goto_5e

    nop

    :goto_26
    iget-object v0, p0, Lcom/android/provision/activities/BaseActivity;->mFragment:Landroidx/fragment/app/Fragment;

    goto :goto_2e

    nop

    :goto_27
    if-nez v5, :cond_8

    goto :goto_11

    :cond_8
    goto :goto_2f

    nop

    :goto_28
    invoke-static {v3, v4}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v3

    goto :goto_47

    nop

    :goto_29
    if-nez v3, :cond_9

    goto :goto_4c

    :cond_9
    goto :goto_66

    nop

    :goto_2a
    move v6, v1

    :goto_2b
    goto :goto_2

    nop

    :goto_2c
    invoke-virtual {v0, v3}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    :goto_2d
    goto :goto_69

    nop

    :goto_2e
    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getView()Landroid/view/View;

    move-result-object v0

    goto :goto_6

    nop

    :goto_2f
    invoke-static {}, Lcom/android/provision/Utils;->isRTL()Z

    move-result v6

    goto :goto_4e

    nop

    :goto_30
    invoke-virtual {v0, v3}, Landroid/view/View;->setTextDirection(I)V

    goto :goto_6b

    nop

    :goto_31
    const/4 v1, 0x3

    goto :goto_22

    nop

    :goto_32
    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v5

    goto :goto_68

    nop

    :goto_33
    if-eq v3, v4, :cond_a

    goto :goto_5a

    :cond_a
    goto :goto_37

    nop

    :goto_34
    return-void

    :goto_35
    iget-boolean v0, p0, Lcom/android/provision/activities/BaseActivity;->mIsDisableBack:Z

    goto :goto_41

    nop

    :goto_36
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object v3

    goto :goto_21

    nop

    :goto_37
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object v3

    goto :goto_54

    nop

    :goto_38
    move-object v1, v0

    goto :goto_56

    nop

    :goto_39
    invoke-virtual {p0}, Lmiuix/provision/ProvisionBaseActivity;->hasPreview()Z

    move-result v0

    goto :goto_12

    nop

    :goto_3a
    const/4 v4, 0x0

    goto :goto_3

    nop

    :goto_3b
    goto :goto_2b

    :goto_3c
    goto :goto_2a

    nop

    :goto_3d
    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    goto :goto_9

    nop

    :goto_3e
    instance-of v5, v0, Landroid/widget/TextView;

    goto :goto_52

    nop

    :goto_3f
    if-gtz v3, :cond_b

    goto :goto_19

    :cond_b
    goto :goto_57

    nop

    :goto_40
    invoke-virtual {v6, v0}, Landroid/widget/TextView;->setMovementMethod(Landroid/text/method/MovementMethod;)V

    goto :goto_10

    nop

    :goto_41
    if-eqz v0, :cond_c

    goto :goto_49

    :cond_c
    goto :goto_39

    nop

    :goto_42
    check-cast v6, Landroid/widget/TextView;

    goto :goto_1c

    nop

    :goto_43
    instance-of v0, p0, Lcom/android/provision/activities/InputMethodActivity;

    goto :goto_1f

    nop

    :goto_44
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mTitle:Lmiuix/appcompat/widget/TextView;

    goto :goto_31

    nop

    :goto_45
    invoke-virtual {v1, p0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    goto :goto_24

    nop

    :goto_46
    if-nez v0, :cond_d

    goto :goto_5

    :cond_d
    goto :goto_3e

    nop

    :goto_47
    invoke-virtual {v0, v3}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    goto :goto_59

    nop

    :goto_48
    invoke-virtual {v0, v3}, Landroid/widget/ImageView;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    :goto_49
    goto :goto_5f

    nop

    :goto_4a
    invoke-virtual {v0, v1}, Landroid/view/View;->setTextDirection(I)V

    goto :goto_38

    nop

    :goto_4b
    goto :goto_f

    :goto_4c
    goto :goto_e

    nop

    :goto_4d
    invoke-virtual {v0, v3}, Landroid/widget/TextView;->setText(I)V

    goto :goto_18

    nop

    :goto_4e
    if-nez v6, :cond_e

    goto :goto_3c

    :cond_e
    goto :goto_53

    nop

    :goto_4f
    invoke-virtual {v0}, Landroidx/fragment/app/Fragment;->getView()Landroid/view/View;

    move-result-object v0

    goto :goto_0

    nop

    :goto_50
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getListDescCharSequence()Ljava/lang/CharSequence;

    move-result-object v5

    goto :goto_27

    nop

    :goto_51
    if-nez v3, :cond_f

    goto :goto_5d

    :cond_f
    goto :goto_5c

    nop

    :goto_52
    if-nez v5, :cond_10

    goto :goto_5

    :cond_10
    goto :goto_1b

    nop

    :goto_53
    move v6, v2

    goto :goto_3b

    nop

    :goto_54
    invoke-virtual {v3, v4}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object v3

    goto :goto_13

    nop

    :goto_55
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringText()Ljava/lang/String;

    move-result-object v3

    goto :goto_3d

    nop

    :goto_56
    check-cast v1, Landroid/widget/TextView;

    goto :goto_45

    nop

    :goto_57
    sget v4, Lcom/android/provision/R$string;->multisim_settings_title:I

    goto :goto_33

    nop

    :goto_58
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result v3

    goto :goto_62

    nop

    :goto_59
    goto :goto_2d

    :goto_5a
    goto :goto_4d

    nop

    :goto_5b
    invoke-static {}, Landroid/text/method/LinkMovementMethod;->getInstance()Landroid/text/method/MovementMethod;

    move-result-object v0

    goto :goto_40

    nop

    :goto_5c
    move v1, v2

    :goto_5d
    goto :goto_4a

    nop

    :goto_5e
    invoke-static {}, Lcom/android/provision/Utils;->isRTL()Z

    move-result v3

    goto :goto_29

    nop

    :goto_5f
    iget-object v0, p0, Lcom/android/provision/activities/BaseActivity;->mFragment:Landroidx/fragment/app/Fragment;

    goto :goto_64

    nop

    :goto_60
    if-nez v0, :cond_11

    goto :goto_49

    :cond_11
    goto :goto_35

    nop

    :goto_61
    const/16 v3, 0x8

    goto :goto_3a

    nop

    :goto_62
    if-nez v3, :cond_12

    goto :goto_2d

    :cond_12
    goto :goto_55

    nop

    :goto_63
    invoke-virtual {v0, v5}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_46

    nop

    :goto_64
    if-nez v0, :cond_13

    goto :goto_5

    :cond_13
    goto :goto_4f

    nop

    :goto_65
    invoke-static {v4}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    goto :goto_67

    nop

    :goto_66
    move v3, v2

    goto :goto_4b

    nop

    :goto_67
    filled-new-array {v4}, [Ljava/lang/Object;

    move-result-object v4

    goto :goto_28

    nop

    :goto_68
    if-eqz v5, :cond_14

    goto :goto_8

    :cond_14
    goto :goto_6a

    nop

    :goto_69
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_60

    nop

    :goto_6a
    invoke-static {}, Lcom/android/provision/Utils;->isRTL()Z

    move-result v3

    goto :goto_51

    nop

    :goto_6b
    invoke-virtual {p0}, Lcom/android/provision/activities/BaseActivity;->getTitleStringId()I

    move-result v3

    goto :goto_3f

    nop

    :goto_6c
    iget-object v3, p0, Lcom/android/provision/activities/BaseActivity;->mBackListener:Landroid/view/View$OnClickListener;

    goto :goto_48

    nop

    :goto_6d
    move-object v6, v0

    goto :goto_42

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_BaseActivity__removeProvisionContainerMargin',
        'method': '.method protected removeProvisionContainerMargin()V',
        'method_name': 'removeProvisionContainerMargin',
        'method_anchors': ['const-string v0, "BaseActivity"', 'iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;', 'if-eqz v1, :cond_0', 'invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;', 'invoke-virtual {v1, v2}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginStart(I)V', 'invoke-virtual {v1, v2}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginEnd(I)V', 'iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;'],
        'type': 'method_replace',
        'search': """.method protected removeProvisionContainerMargin()V
    .registers 4

    const-string v0, "BaseActivity"

    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    if-eqz v1, :cond_0

    :try_start_0
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginStart(I)V

    invoke-virtual {v1, v2}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginEnd(I)V

    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    invoke-virtual {p0, v1}, Landroid/view/View;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    const-string p0, "removeProvisionMargin success"

    invoke-static {v0, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_0
    .catch Ljava/lang/ClassCastException; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :catch_0
    move-exception p0

    const-string v1, "removeProvisionMargin fail"

    invoke-static {v0, v1, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected removeProvisionContainerMargin()V
    .registers 4

    goto :goto_5

    nop

    :goto_0
    return-void

    :goto_1
    invoke-static {v0, v1, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_2
    goto :goto_0

    nop

    :goto_3
    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    goto :goto_4

    nop

    :goto_4
    if-nez v1, :cond_0

    goto :goto_2

    :cond_0
    :try_start_0
    invoke-virtual {v1}, Landroid/view/View;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    check-cast v1, Landroid/view/ViewGroup$MarginLayoutParams;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginStart(I)V

    invoke-virtual {v1, v2}, Landroid/view/ViewGroup$MarginLayoutParams;->setMarginEnd(I)V

    iget-object p0, p0, Lmiuix/provision/ProvisionBaseActivity;->mProvisionContainer:Landroid/view/View;

    invoke-virtual {p0, v1}, Landroid/view/View;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    const-string p0, "removeProvisionMargin success"

    invoke-static {v0, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_0
    .catch Ljava/lang/ClassCastException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_7

    nop

    :goto_5
    const-string v0, "BaseActivity"

    goto :goto_3

    nop

    :goto_6
    const-string v1, "removeProvisionMargin fail"

    goto :goto_1

    nop

    :goto_7
    return-void

    :catch_0
    move-exception p0

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_BaseActivity__updateConfirmButtonEnableState',
        'method': '.method protected updateConfirmButtonEnableState()V',
        'method_name': 'updateConfirmButtonEnableState',
        'method_anchors': ['iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;', 'if-nez v0, :cond_0', 'return-void', 'invoke-virtual {v0}, Landroid/widget/Button;->isEnabled()Z', 'iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;', 'invoke-virtual {v1, v2}, Landroid/widget/Button;->setEnabled(Z)V', 'iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;', 'new-instance v2, Lcom/android/provision/activities/BaseActivity$$ExternalSyntheticLambda0;'],
        'type': 'method_replace',
        'search': """.method protected updateConfirmButtonEnableState()V
    .registers 6

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    if-nez v0, :cond_0

    return-void

    :cond_0
    invoke-virtual {v0}, Landroid/widget/Button;->isEnabled()Z

    move-result v0

    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Landroid/widget/Button;->setEnabled(Z)V

    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    new-instance v2, Lcom/android/provision/activities/BaseActivity$$ExternalSyntheticLambda0;

    invoke-direct {v2, p0, v0}, Lcom/android/provision/activities/BaseActivity$$ExternalSyntheticLambda0;-><init>(Lcom/android/provision/activities/BaseActivity;Z)V

    const-wide/16 v3, 0x36b

    invoke-virtual {v1, v2, v3, v4}, Landroid/widget/Button;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void
.end method""",
        'replacement': """.method protected updateConfirmButtonEnableState()V
    .registers 6

    goto :goto_8

    nop

    :goto_0
    return-void

    :goto_1
    invoke-direct {v2, p0, v0}, Lcom/android/provision/activities/BaseActivity$$ExternalSyntheticLambda0;-><init>(Lcom/android/provision/activities/BaseActivity;Z)V

    goto :goto_d

    nop

    :goto_2
    const/4 v2, 0x0

    goto :goto_b

    nop

    :goto_3
    invoke-virtual {v0}, Landroid/widget/Button;->isEnabled()Z

    move-result v0

    goto :goto_4

    nop

    :goto_4
    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    goto :goto_2

    nop

    :goto_5
    new-instance v2, Lcom/android/provision/activities/BaseActivity$$ExternalSyntheticLambda0;

    goto :goto_1

    nop

    :goto_6
    return-void

    :goto_7
    goto :goto_3

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    goto :goto_9

    nop

    :goto_9
    if-eqz v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_6

    nop

    :goto_a
    invoke-virtual {v1, v2, v3, v4}, Landroid/widget/Button;->postDelayed(Ljava/lang/Runnable;J)Z

    goto :goto_0

    nop

    :goto_b
    invoke-virtual {v1, v2}, Landroid/widget/Button;->setEnabled(Z)V

    goto :goto_c

    nop

    :goto_c
    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    goto :goto_5

    nop

    :goto_d
    const-wide/16 v3, 0x36b

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
