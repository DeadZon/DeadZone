TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/MultiSimSettingsActivity.smali'
CLASS_FALLBACK_NAMES = ['MultiSimSettingsActivity.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/BaseActivity;']

PATCHES = [
    {
        'id': 'com_android_provision_activities_MultiSimSettingsActivity__getFragment',
        'method': '.method protected getFragment()Landroidx/fragment/app/Fragment;',
        'method_name': 'getFragment',
        'method_anchors': ['new-instance p0, Lcom/android/provision/fragment/MultiSimSettingsFragment;', 'invoke-direct {p0}, Lcom/android/provision/fragment/MultiSimSettingsFragment;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    new-instance p0, Lcom/android/provision/fragment/MultiSimSettingsFragment;

    invoke-direct {p0}, Lcom/android/provision/fragment/MultiSimSettingsFragment;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    invoke-direct {p0}, Lcom/android/provision/fragment/MultiSimSettingsFragment;-><init>()V

    goto :goto_2

    nop

    :goto_1
    new-instance p0, Lcom/android/provision/fragment/MultiSimSettingsFragment;

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
        'id': 'com_android_provision_activities_MultiSimSettingsActivity__getFragmentTag',
        'method': '.method protected getFragmentTag()Ljava/lang/String;',
        'method_name': 'getFragmentTag',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    const-class p0, Lcom/android/provision/fragment/MultiSimSettingsFragment;

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const-class p0, Lcom/android/provision/fragment/MultiSimSettingsFragment;

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
        'id': 'com_android_provision_activities_MultiSimSettingsActivity__getListDescCharSequence',
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
        'id': 'com_android_provision_activities_MultiSimSettingsActivity__getLogoDrawableId',
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
        'id': 'com_android_provision_activities_MultiSimSettingsActivity__getTitleStringId',
        'method': '.method protected getTitleStringId()I',
        'method_name': 'getTitleStringId',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z', 'if-nez p0, :cond_1', 'invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z', 'if-eqz p0, :cond_0', 'sget p0, Lcom/android/provision/R$string;->multisim_settings_title:I', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringId()I
    .registers 1

    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result p0

    if-nez p0, :cond_1

    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result p0

    if-eqz p0, :cond_0

    goto :goto_0

    :cond_0
    sget p0, Lcom/android/provision/R$string;->multisim_settings_title:I

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected getTitleStringId()I
    .registers 1

    goto :goto_8

    nop

    :goto_0
    return p0

    :goto_1
    if-eqz p0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_7

    nop

    :goto_2
    goto :goto_5

    :goto_3
    goto :goto_a

    nop

    :goto_4
    return p0

    :goto_5
    goto :goto_6

    nop

    :goto_6
    const/4 p0, 0x0

    goto :goto_0

    nop

    :goto_7
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result p0

    goto :goto_9

    nop

    :goto_8
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result p0

    goto :goto_1

    nop

    :goto_9
    if-nez p0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_2

    nop

    :goto_a
    sget p0, Lcom/android/provision/R$string;->multisim_settings_title:I

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_MultiSimSettingsActivity__getTitleStringText',
        'method': '.method protected getTitleStringText()Ljava/lang/String;',
        'method_name': 'getTitleStringText',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z', 'if-eqz v0, :cond_0', 'invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getActiveSimCount(Landroid/content/Context;Z)I', 'if-ne v0, v1, :cond_0', 'invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I', 'invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;', 'invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-nez v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringText()Ljava/lang/String;
    .registers 4

    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result v0

    const/4 v1, 0x2

    const/4 v2, 0x1

    if-eqz v0, :cond_0

    invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getActiveSimCount(Landroid/content/Context;Z)I

    move-result v0

    if-ne v0, v1, :cond_0

    invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result v0

    invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_1

    :cond_0
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result v0

    invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_2

    :cond_1
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget v0, Lcom/android/provision/R$string;->multisim_settings_sb_title:I

    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p0

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    filled-new-array {v0}, [Ljava/lang/Object;

    move-result-object v0

    invoke-static {p0, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :cond_2
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    sget v0, Lcom/android/provision/R$string;->multisim_settings_title:I

    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p0

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    filled-new-array {v0}, [Ljava/lang/Object;

    move-result-object v0

    invoke-static {p0, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getTitleStringText()Ljava/lang/String;
    .registers 4

    goto :goto_1d

    nop

    :goto_0
    invoke-static {p0, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    goto :goto_5

    nop

    :goto_1
    invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getActiveSimCount(Landroid/content/Context;Z)I

    move-result v0

    goto :goto_1c

    nop

    :goto_2
    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_20

    nop

    :goto_3
    filled-new-array {v0}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_0

    nop

    :goto_4
    invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result v0

    goto :goto_1a

    nop

    :goto_5
    return-object p0

    :goto_6
    const/4 v2, 0x1

    goto :goto_17

    nop

    :goto_7
    invoke-static {p0, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    goto :goto_a

    nop

    :goto_8
    invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object v0

    goto :goto_19

    nop

    :goto_9
    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p0

    goto :goto_15

    nop

    :goto_a
    return-object p0

    :goto_b
    goto :goto_10

    nop

    :goto_c
    if-eqz v0, :cond_0

    goto :goto_f

    :cond_0
    :goto_d
    goto :goto_13

    nop

    :goto_e
    if-nez v0, :cond_1

    goto :goto_b

    :cond_1
    :goto_f
    goto :goto_1f

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    goto :goto_11

    nop

    :goto_11
    sget v0, Lcom/android/provision/R$string;->multisim_settings_title:I

    goto :goto_9

    nop

    :goto_12
    sget v0, Lcom/android/provision/R$string;->multisim_settings_sb_title:I

    goto :goto_1e

    nop

    :goto_13
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result v0

    goto :goto_18

    nop

    :goto_14
    const/4 v1, 0x2

    goto :goto_6

    nop

    :goto_15
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_3

    nop

    :goto_16
    invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result v0

    goto :goto_8

    nop

    :goto_17
    if-nez v0, :cond_2

    goto :goto_d

    :cond_2
    goto :goto_1

    nop

    :goto_18
    if-nez v0, :cond_3

    goto :goto_b

    :cond_3
    goto :goto_4

    nop

    :goto_19
    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    goto :goto_c

    nop

    :goto_1a
    invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object v0

    goto :goto_1b

    nop

    :goto_1b
    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    goto :goto_e

    nop

    :goto_1c
    if-eq v0, v1, :cond_4

    goto :goto_d

    :cond_4
    goto :goto_16

    nop

    :goto_1d
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result v0

    goto :goto_14

    nop

    :goto_1e
    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getString(I)Ljava/lang/String;

    move-result-object p0

    goto :goto_2

    nop

    :goto_1f
    invoke-virtual {p0}, Landroid/app/Activity;->getResources()Landroid/content/res/Resources;

    move-result-object p0

    goto :goto_12

    nop

    :goto_20
    filled-new-array {v0}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_MultiSimSettingsActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V', 'invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z', 'if-eqz p1, :cond_0', 'invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getActiveSimCount(Landroid/content/Context;Z)I', 'if-ne p1, v1, :cond_0', 'invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I', 'invoke-static {p0, p1}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;', 'invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result p1

    const/4 v0, 0x1

    if-eqz p1, :cond_0

    invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getActiveSimCount(Landroid/content/Context;Z)I

    move-result p1

    const/4 v1, 0x2

    if-ne p1, v1, :cond_0

    invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result p1

    invoke-static {p0, p1}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    if-nez p1, :cond_1

    :cond_0
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result p1

    if-eqz p1, :cond_2

    invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result p1

    invoke-static {p0, p1}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    if-eqz p1, :cond_2

    :cond_1
    const-string p1, "single_sim_card.json"

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    return-void

    :cond_2
    const-string p1, "double_sim_card.json"

    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_16

    nop

    :goto_0
    if-eqz p1, :cond_0

    goto :goto_13

    :cond_0
    :goto_1
    goto :goto_5

    nop

    :goto_2
    invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getActiveSimCount(Landroid/content/Context;Z)I

    move-result p1

    goto :goto_19

    nop

    :goto_3
    if-nez p1, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_2

    nop

    :goto_4
    const-string p1, "double_sim_card.json"

    goto :goto_f

    nop

    :goto_5
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result p1

    goto :goto_15

    nop

    :goto_6
    if-eq p1, v1, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_b

    nop

    :goto_7
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result p1

    goto :goto_a

    nop

    :goto_8
    invoke-static {p0, p1}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object p1

    goto :goto_18

    nop

    :goto_9
    invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result p1

    goto :goto_8

    nop

    :goto_a
    const/4 v0, 0x1

    goto :goto_3

    nop

    :goto_b
    invoke-static {p0, v0}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result p1

    goto :goto_10

    nop

    :goto_c
    return-void

    :goto_d
    goto :goto_4

    nop

    :goto_e
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    goto :goto_c

    nop

    :goto_f
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    goto :goto_14

    nop

    :goto_10
    invoke-static {p0, p1}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object p1

    goto :goto_17

    nop

    :goto_11
    const-string p1, "single_sim_card.json"

    goto :goto_e

    nop

    :goto_12
    if-nez p1, :cond_3

    goto :goto_d

    :cond_3
    :goto_13
    goto :goto_11

    nop

    :goto_14
    return-void

    :goto_15
    if-nez p1, :cond_4

    goto :goto_d

    :cond_4
    goto :goto_9

    nop

    :goto_16
    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_7

    nop

    :goto_17
    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    goto :goto_0

    nop

    :goto_18
    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    goto :goto_12

    nop

    :goto_19
    const/4 v1, 0x2

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
