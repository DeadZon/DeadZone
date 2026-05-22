TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/TermsActivity.smali'
CLASS_FALLBACK_NAMES = ['TermsActivity.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/activities/BaseActivity;', '.field private static final TAG:Ljava/lang/String; = "TermsActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_TermsActivity__getFragment',
        'method': '.method protected getFragment()Landroidx/fragment/app/Fragment;',
        'method_name': 'getFragment',
        'method_anchors': ['new-instance p0, Lcom/android/provision/fragment/TermsFragment;', 'invoke-direct {p0}, Lcom/android/provision/fragment/TermsFragment;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    new-instance p0, Lcom/android/provision/fragment/TermsFragment;

    invoke-direct {p0}, Lcom/android/provision/fragment/TermsFragment;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected getFragment()Landroidx/fragment/app/Fragment;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    new-instance p0, Lcom/android/provision/fragment/TermsFragment;

    goto :goto_2

    nop

    :goto_2
    invoke-direct {p0}, Lcom/android/provision/fragment/TermsFragment;-><init>()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_TermsActivity__getFragmentTag',
        'method': '.method protected getFragmentTag()Ljava/lang/String;',
        'method_name': 'getFragmentTag',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    const-class p0, Lcom/android/provision/fragment/TermsFragment;

    invoke-virtual {p0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected getFragmentTag()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const-class p0, Lcom/android/provision/fragment/TermsFragment;

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
        'id': 'com_android_provision_activities_TermsActivity__getListDescCharSequence',
        'method': '.method protected getListDescCharSequence()Ljava/lang/CharSequence;',
        'method_name': 'getListDescCharSequence',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-static {p0, v0}, Lcom/android/provision/manager/PreLoadManager;->getLogic(Ljava/lang/Class;Ljava/lang/Class;)Lcom/android/provision/manager/logic/ILogic;', 'check-cast p0, Lcom/android/provision/manager/logic/TermsListDescLogic;', 'if-nez p0, :cond_0', 'invoke-static {}, Lcom/android/provision/activities/TermsActivity;->getListDescription()Ljava/lang/String;', 'return-object p0', 'invoke-virtual {p0}, Lcom/android/provision/manager/logic/BaseLogic;->getResult()Ljava/lang/Object;', 'check-cast p0, Ljava/lang/CharSequence;'],
        'type': 'method_replace',
        'search': """.method protected getListDescCharSequence()Ljava/lang/CharSequence;
    .registers 2

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    const-class v0, Lcom/android/provision/manager/logic/TermsListDescLogic;

    invoke-static {p0, v0}, Lcom/android/provision/manager/PreLoadManager;->getLogic(Ljava/lang/Class;Ljava/lang/Class;)Lcom/android/provision/manager/logic/ILogic;

    move-result-object p0

    check-cast p0, Lcom/android/provision/manager/logic/TermsListDescLogic;

    if-nez p0, :cond_0

    invoke-static {}, Lcom/android/provision/activities/TermsActivity;->getListDescription()Ljava/lang/String;

    move-result-object p0

    return-object p0

    :cond_0
    invoke-virtual {p0}, Lcom/android/provision/manager/logic/BaseLogic;->getResult()Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/lang/CharSequence;

    return-object p0
.end method""",
        'replacement': """.method protected getListDescCharSequence()Ljava/lang/CharSequence;
    .registers 2

    goto :goto_8

    nop

    :goto_0
    check-cast p0, Ljava/lang/CharSequence;

    goto :goto_7

    nop

    :goto_1
    if-eqz p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_9

    nop

    :goto_2
    const-class v0, Lcom/android/provision/manager/logic/TermsListDescLogic;

    goto :goto_5

    nop

    :goto_3
    return-object p0

    :goto_4
    goto :goto_a

    nop

    :goto_5
    invoke-static {p0, v0}, Lcom/android/provision/manager/PreLoadManager;->getLogic(Ljava/lang/Class;Ljava/lang/Class;)Lcom/android/provision/manager/logic/ILogic;

    move-result-object p0

    goto :goto_6

    nop

    :goto_6
    check-cast p0, Lcom/android/provision/manager/logic/TermsListDescLogic;

    goto :goto_1

    nop

    :goto_7
    return-object p0

    :goto_8
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p0

    goto :goto_2

    nop

    :goto_9
    invoke-static {}, Lcom/android/provision/activities/TermsActivity;->getListDescription()Ljava/lang/String;

    move-result-object p0

    goto :goto_3

    nop

    :goto_a
    invoke-virtual {p0}, Lcom/android/provision/manager/logic/BaseLogic;->getResult()Ljava/lang/Object;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_TermsActivity__getLogoDrawableId',
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
        'id': 'com_android_provision_activities_TermsActivity__getTitleStringId',
        'method': '.method protected getTitleStringId()I',
        'method_name': 'getTitleStringId',
        'method_anchors': ['sget p0, Lcom/android/provision/R$string;->terms_of_use:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getTitleStringId()I
    .registers 1

    sget p0, Lcom/android/provision/R$string;->terms_of_use:I

    return p0
.end method""",
        'replacement': """.method protected getTitleStringId()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lcom/android/provision/R$string;->terms_of_use:I

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
        'id': 'com_android_provision_activities_TermsActivity__onCreate',
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

    goto :goto_1

    nop

    :goto_0
    const-string p1, "terms.json"

    goto :goto_3

    nop

    :goto_1
    invoke-super {p0, p1}, Lcom/android/provision/activities/BaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->setAnimationView(Ljava/lang/String;)V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_TermsActivity__getListDescription',
        'method': '.method public static getListDescription()Ljava/lang/String;',
        'method_name': 'getListDescription',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;', 'sget v1, Lcom/android/provision/R$string;->terms_of_label_separator:I', 'invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;', 'new-instance v2, Ljava/lang/StringBuilder;', 'invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V', 'sget-boolean v3, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v3, :cond_0', 'sget v4, Lcom/android/provision/R$string;->terms_of_use_label_use_location_and_network_global:I'],
        'type': 'policy_skip',
        'search': """.method public static getListDescription()Ljava/lang/String;
    .registers 6

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    sget v1, Lcom/android/provision/R$string;->terms_of_label_separator:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    sget-boolean v3, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v3, :cond_0

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_use_location_and_network_global:I

    invoke-virtual {v0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_0
    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_use_network_china:I

    invoke-virtual {v0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_0
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportCloudService(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_1

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_cloud:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1
    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_remote_provisioner:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportCloudBackup(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_2

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_back:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_2
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportFindDevice(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_3

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_finddevice:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_3
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportSecureElementApplication(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_4

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_secure:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_4
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportHome(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_5

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_home:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_5
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportGameCenterService(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_6

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_game:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_6
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportTranslationService(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_7

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_translation:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_7
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportXmsf(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_8

    sget v5, Lcom/android/provision/R$string;->terms_of_use_lable_xmsf:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_8
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportMiuiDaemon(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_9

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_miuiDaemon:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_9
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportMSA(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_a

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_MSA:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_a
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportSimActivateService(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_b

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_simcard:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_b
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportAIAssistant(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_c

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_ai_assistant:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_c
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportPowerKeeper(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_d

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_power_performance:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_d
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportPowerchecker(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_e

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_power_detection:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_e
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportOs(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_f

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_os:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_f
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportJoyose(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_10

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_joyose:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_10
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportWallpaper(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_11

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_wallpaper:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_11
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportHTMLViewer(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_12

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_htmlViewer:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_12
    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_landscape:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-nez v3, :cond_1a

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_system_quality_monitoring:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_webview:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Lcom/android/provision/Utils;->isSupportIntentFilterVerificationService()Z

    move-result v3

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportUpdater(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_13

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_updater:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-eqz v3, :cond_13

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_13
    if-eqz v3, :cond_14

    sget v3, Lcom/android/provision/R$string;->intent_filter_verification_service:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_14
    sget v3, Lcom/android/provision/R$string;->fidio_declare_permissions:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v3, Lcom/android/provision/R$string;->terms_of_label_period:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v5, Lcom/android/provision/R$string;->image_brain_configuration_service:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v3, Lcom/android/provision/R$string;->agreement_declare_use_network_and_location_china:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/4 v3, 0x0

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->length()I

    move-result v5

    invoke-virtual {v4, v3, v5}, Ljava/lang/StringBuilder;->delete(II)Ljava/lang/StringBuilder;

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportSmartCard(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_15

    sget v3, Lcom/android/provision/R$string;->terms_of_use_lable_smart_cards:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_15
    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_unionplay_security:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportRMS(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_16

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_RMS:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_16
    invoke-static {}, Lcom/android/provision/Utils;->hasGmscore()Z

    move-result v3

    if-eqz v3, :cond_17

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_config_updater:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_17
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportSmartService(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_18

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_smart_service:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_18
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportCommService(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_19

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_communication_service:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_19
    sget v1, Lcom/android/provision/R$string;->terms_of_use_label_miuisdk:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;

    goto :goto_1

    :cond_1a
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportQuickApp(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1b

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_quickapp:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1b
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportAppVault(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1c

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_app_vault:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1c
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportInfoAssistant(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1d

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_info_assistant:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1d
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportStatistics(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1e

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_statistics:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1e
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportMAB(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1f

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_mab:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1f
    sget v3, Lcom/android/provision/R$string;->terms_of_use_lable_gms:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportSmartCard(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_20

    sget v3, Lcom/android/provision/R$string;->terms_of_use_lable_smart_cards:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_20
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportUpdater(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_21

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_updater:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_21
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportMiAccount(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_22

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_mi_account:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_22
    sget v3, Lcom/android/provision/R$string;->fidio_declare_permissions:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v3, Lcom/android/provision/R$string;->image_brain_configuration_service:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v3

    if-eqz v3, :cond_23

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_label_communication_service:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_23
    sget v1, Lcom/android/provision/R$string;->terms_of_label_space:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_1
    sget v1, Lcom/android/provision/R$string;->terms_of_label_period:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getImmId()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    if-nez v3, :cond_26

    const-string v3, "com.facemoji.lite.xiaomi/com.baidu.simeji.SimejiIME"

    invoke-static {v2, v3}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v3

    const-string v4, "\n"

    const-string v5, "\\n"

    if-eqz v3, :cond_24

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_facemoji:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0, v5, v4}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    return-object v0

    :cond_24
    const-string v3, "com.mint.keyboard/.services.MintKeyboard"

    invoke-static {v2, v3}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v3

    if-eqz v3, :cond_25

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_mint:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0, v5, v4}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    return-object v0

    :cond_25
    const-string v3, "com.kikaoem.xiaomi.qisiemoji.inputmethod/com.android.inputmethod.latin.LatinIME"

    invoke-static {v2, v3}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v2

    if-eqz v2, :cond_26

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_kika:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0, v5, v4}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    return-object v0

    :cond_26
    return-object v1
.end method""",
        'replacement': """.method public static getListDescription()Ljava/lang/String;
    .registers 6

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    sget v1, Lcom/android/provision/R$string;->terms_of_label_separator:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    sget-boolean v3, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v3, :cond_0

    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_use_location_and_network_global:I

    invoke-virtual {v0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_0
    sget v4, Lcom/android/provision/R$string;->terms_of_use_label_use_network_china:I

    invoke-virtual {v0, v4}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_0
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportCloudService(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_1

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_cloud:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1
    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_remote_provisioner:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportCloudBackup(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_2

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_back:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_2
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportFindDevice(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_3

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_finddevice:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_3
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportSecureElementApplication(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_4

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_secure:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_4
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportHome(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_5

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_home:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_5
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportGameCenterService(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_6

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_game:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_6
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportTranslationService(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_7

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_translation:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_7
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportXmsf(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_8

    sget v5, Lcom/android/provision/R$string;->terms_of_use_lable_xmsf:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_8
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportMiuiDaemon(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_9

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_miuiDaemon:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_9
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportMSA(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_a

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_MSA:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_a
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportSimActivateService(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_b

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_simcard:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_b
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportAIAssistant(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_c

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_ai_assistant:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_c
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportPowerKeeper(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_d

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_power_performance:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_d
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportPowerchecker(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_e

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_power_detection:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_e
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportOs(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_f

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_os:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_f
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportJoyose(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_10

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_joyose:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_10
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportWallpaper(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_11

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_wallpaper:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_11
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportHTMLViewer(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_12

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_htmlViewer:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_12
    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_landscape:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-nez v3, :cond_1a

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_system_quality_monitoring:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_webview:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Lcom/android/provision/Utils;->isSupportIntentFilterVerificationService()Z

    move-result v3

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportUpdater(Landroid/content/Context;)Z

    move-result v5

    if-eqz v5, :cond_13

    sget v5, Lcom/android/provision/R$string;->terms_of_use_label_updater:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    if-eqz v3, :cond_13

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_13
    if-eqz v3, :cond_14

    sget v3, Lcom/android/provision/R$string;->intent_filter_verification_service:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_14
    sget v3, Lcom/android/provision/R$string;->fidio_declare_permissions:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v3, Lcom/android/provision/R$string;->terms_of_label_period:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v5, Lcom/android/provision/R$string;->image_brain_configuration_service:I

    invoke-virtual {v0, v5}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v3, Lcom/android/provision/R$string;->agreement_declare_use_network_and_location_china:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/4 v3, 0x0

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->length()I

    move-result v5

    invoke-virtual {v4, v3, v5}, Ljava/lang/StringBuilder;->delete(II)Ljava/lang/StringBuilder;

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportSmartCard(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_15

    sget v3, Lcom/android/provision/R$string;->terms_of_use_lable_smart_cards:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_15
    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_unionplay_security:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportRMS(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_16

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_RMS:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_16
    invoke-static {}, Lcom/android/provision/Utils;->hasGmscore()Z

    move-result v3

    if-eqz v3, :cond_17

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_config_updater:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_17
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportSmartService(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_18

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_smart_service:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_18
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportCommService(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_19

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_communication_service:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_19
    sget v1, Lcom/android/provision/R$string;->terms_of_use_label_miuisdk:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;

    goto :goto_1

    :cond_1a
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportQuickApp(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1b

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_quickapp:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1b
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportAppVault(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1c

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_app_vault:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1c
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportInfoAssistant(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1d

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_info_assistant:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1d
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportStatistics(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1e

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_statistics:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1e
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportMAB(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_1f

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_mab:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_1f
    sget v3, Lcom/android/provision/R$string;->terms_of_use_lable_gms:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportSmartCard(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_20

    sget v3, Lcom/android/provision/R$string;->terms_of_use_lable_smart_cards:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_20
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportUpdater(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_21

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_updater:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_21
    invoke-static {v0}, Lcom/android/provision/Utils;->isSupportMiAccount(Landroid/content/Context;)Z

    move-result v3

    if-eqz v3, :cond_22

    sget v3, Lcom/android/provision/R$string;->terms_of_use_label_mi_account:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_22
    sget v3, Lcom/android/provision/R$string;->fidio_declare_permissions:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v3, Lcom/android/provision/R$string;->image_brain_configuration_service:I

    invoke-virtual {v0, v3}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v3

    if-eqz v3, :cond_23

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_label_communication_service:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_23
    sget v1, Lcom/android/provision/R$string;->terms_of_label_space:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_1
    sget v1, Lcom/android/provision/R$string;->terms_of_label_period:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getImmId()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    if-nez v3, :cond_26

    const-string v3, "com.facemoji.lite.xiaomi/com.baidu.simeji.SimejiIME"

    invoke-static {v2, v3}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v3

    const-string v4, "\n"

    const-string v5, "\\n"

    if-eqz v3, :cond_24

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_facemoji:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0, v5, v4}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    return-object v0

    :cond_24
    const-string v3, "com.mint.keyboard/.services.MintKeyboard"

    invoke-static {v2, v3}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v3

    if-eqz v3, :cond_25

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_mint:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0, v5, v4}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    return-object v0

    :cond_25
    const-string v3, "com.kikaoem.xiaomi.qisiemoji.inputmethod/com.android.inputmethod.latin.LatinIME"

    invoke-static {v2, v3}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v2

    if-eqz v2, :cond_26

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v1, Lcom/android/provision/R$string;->terms_of_use_lable_default_input_method_kika:I

    invoke-virtual {v0, v1}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0, v5, v4}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    return-object v0

    :cond_26
    return-object v1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
