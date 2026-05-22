TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/TermsAndStatementFragment.smali'
CLASS_FALLBACK_NAMES = ['TermsAndStatementFragment.smali']
CLASS_ANCHORS = ['.super Landroidx/fragment/app/Fragment;', '.field private static final DEVICE_FIRST_USING_DATA:Ljava/lang/String; = "device_first_using_data"', '.field private static final DEVICE_PROVISIONING_MOBILE_DATA_ENABLED:Ljava/lang/String; = "device_provisioning_mobile_data"', '.field private static final DEVICE_PROVISIONING_SERVICE_STATEMENT_AGREED:Ljava/lang/String; = "device_provisioning_service_agreed"', '.field private static final PROVISION_CLAUSE_AGREED_BROADCAST:Ljava/lang/String; = "com.miui.clause_agreed"', '.field private static final SERVICE_STATEMENT_COMPLETE_BROADCAST:Ljava/lang/String; = "android.provision.action.SERVICE_STATEMENT_COMPLETE"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_TermsAndStatementFragment__needShowTrafficConfirmedDialog',
        'method': '.method private needShowTrafficConfirmedDialog(Landroid/content/Context;)Z',
        'method_name': 'needShowTrafficConfirmedDialog',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->mobileDataConfirmDisplayable()Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;', 'const-string v0, "device_first_using_data"', 'invoke-static {p1, v0, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I', 'if-eq p1, v0, :cond_0'],
        'type': 'policy_skip',
        'search': """.method private needShowTrafficConfirmedDialog(Landroid/content/Context;)Z
    .registers 4

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->mobileDataConfirmDisplayable()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v0, "device_first_using_data"

    invoke-static {p1, v0, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p1

    const/4 v0, 0x1

    if-eq p1, v0, :cond_0

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showDataTrafficDialog()Z

    move-result p1

    if-nez p1, :cond_0

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object p1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-virtual {p1, p0}, Lcom/android/provision/utils/MccHelper;->initDataTraffic(Landroid/content/Context;)V

    invoke-virtual {p1}, Lcom/android/provision/utils/MccHelper;->showDataTrafficConfirmDialog()Z

    move-result p0

    return p0

    :cond_0
    return v1
.end method""",
        'replacement': """.method private needShowTrafficConfirmedDialog(Landroid/content/Context;)Z
    .registers 4

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->mobileDataConfirmDisplayable()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v0, "device_first_using_data"

    invoke-static {p1, v0, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p1

    const/4 v0, 0x1

    if-eq p1, v0, :cond_0

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showDataTrafficDialog()Z

    move-result p1

    if-nez p1, :cond_0

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object p1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-virtual {p1, p0}, Lcom/android/provision/utils/MccHelper;->initDataTraffic(Landroid/content/Context;)V

    invoke-virtual {p1}, Lcom/android/provision/utils/MccHelper;->showDataTrafficConfirmDialog()Z

    move-result p0

    return p0

    :cond_0
    return v1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_TermsAndStatementFragment__requestRemoteConfigIfNeeded',
        'method': '.method private requestRemoteConfigIfNeeded()V',
        'method_name': 'requestRemoteConfigIfNeeded',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz p0, :cond_1', 'invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;', 'invoke-static {p0}, Lcom/android/provision/Utils;->isClauseAgreed(Landroid/content/Context;)Z', 'if-eqz p0, :cond_1', 'invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getLastLocale()Ljava/lang/String;', 'invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;', 'invoke-static {v0}, Lcom/android/provision/Utils;->networkAvailable(Landroid/content/Context;)Z'],
        'type': 'policy_skip',
        'search': """.method private requestRemoteConfigIfNeeded()V
    .registers 5

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p0, :cond_1

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/Utils;->isClauseAgreed(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_1

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getLastLocale()Ljava/lang/String;

    move-result-object p0

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->networkAvailable(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    const/4 v1, -0x1

    if-nez v0, :cond_0

    invoke-static {v1}, Lcom/android/provision/DefaultPreferenceHelper;->setCarouselEnable(I)V

    new-instance v0, Lcom/android/provision/utils/CloudConfigRequest;

    invoke-direct {v0}, Lcom/android/provision/utils/CloudConfigRequest;-><init>()V

    const-string v2, "carousel_switch"

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v3

    invoke-virtual {v0, p0, v2, v3}, Lcom/android/provision/utils/CloudConfigRequest;->cloudConfigRequest(Ljava/lang/String;Ljava/lang/String;Landroid/content/Context;)V

    new-instance v0, Lcom/android/provision/utils/CloudConfigRequest;

    invoke-direct {v0}, Lcom/android/provision/utils/CloudConfigRequest;-><init>()V

    invoke-static {v1}, Lcom/android/provision/DefaultPreferenceHelper;->setDrawerEnable(I)V

    const-string v2, "drawer_switch"

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v3

    invoke-virtual {v0, p0, v2, v3}, Lcom/android/provision/utils/CloudConfigRequest;->cloudConfigRequest(Ljava/lang/String;Ljava/lang/String;Landroid/content/Context;)V

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getRecommendedOperation()I

    move-result v0

    if-ne v0, v1, :cond_0

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {p0, v0}, Lcom/android/provision/utils/RequestUtils;->prepareAndStartRecommendedRequest(Ljava/lang/String;Landroid/content/Context;)V

    :cond_0
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getPreinstallStatusCode()I

    move-result p0

    if-ne p0, v1, :cond_1

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/utils/RequestUtils;->prepareAndStartPreinstallRequest(Landroid/content/Context;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method private requestRemoteConfigIfNeeded()V
    .registers 5

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p0, :cond_1

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/Utils;->isClauseAgreed(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_1

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getLastLocale()Ljava/lang/String;

    move-result-object p0

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->networkAvailable(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    const/4 v1, -0x1

    if-nez v0, :cond_0

    invoke-static {v1}, Lcom/android/provision/DefaultPreferenceHelper;->setCarouselEnable(I)V

    new-instance v0, Lcom/android/provision/utils/CloudConfigRequest;

    invoke-direct {v0}, Lcom/android/provision/utils/CloudConfigRequest;-><init>()V

    const-string v2, "carousel_switch"

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v3

    invoke-virtual {v0, p0, v2, v3}, Lcom/android/provision/utils/CloudConfigRequest;->cloudConfigRequest(Ljava/lang/String;Ljava/lang/String;Landroid/content/Context;)V

    new-instance v0, Lcom/android/provision/utils/CloudConfigRequest;

    invoke-direct {v0}, Lcom/android/provision/utils/CloudConfigRequest;-><init>()V

    invoke-static {v1}, Lcom/android/provision/DefaultPreferenceHelper;->setDrawerEnable(I)V

    const-string v2, "drawer_switch"

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v3

    invoke-virtual {v0, p0, v2, v3}, Lcom/android/provision/utils/CloudConfigRequest;->cloudConfigRequest(Ljava/lang/String;Ljava/lang/String;Landroid/content/Context;)V

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getRecommendedOperation()I

    move-result v0

    if-ne v0, v1, :cond_0

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {p0, v0}, Lcom/android/provision/utils/RequestUtils;->prepareAndStartRecommendedRequest(Ljava/lang/String;Landroid/content/Context;)V

    :cond_0
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getPreinstallStatusCode()I

    move-result p0

    if-ne p0, v1, :cond_1

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/utils/RequestUtils;->prepareAndStartPreinstallRequest(Landroid/content/Context;)V

    :cond_1
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_TermsAndStatementFragment__getName',
        'method': '.method protected getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['const-string p0, "ServiceStatementFragment"', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getName()Ljava/lang/String;
    .registers 1

    const-string p0, "ServiceStatementFragment"

    return-object p0
.end method""",
        'replacement': """.method protected getName()Ljava/lang/String;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    const-string p0, "ServiceStatementFragment"

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_TermsAndStatementFragment__recordBottomButtonClick',
        'method': '.method protected recordBottomButtonClick(Ljava/lang/String;)V',
        'method_name': 'recordBottomButtonClick',
        'method_anchors': ['invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'invoke-virtual {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->getName()Ljava/lang/String;', 'invoke-static {v0, p0, p1}, Lcom/android/provision/utils/OTHelper;->rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected recordBottomButtonClick(Ljava/lang/String;)V
    .registers 3

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->getName()Ljava/lang/String;

    move-result-object p0

    invoke-static {v0, p0, p1}, Lcom/android/provision/utils/OTHelper;->rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    return-void
.end method""",
        'replacement': """.method protected recordBottomButtonClick(Ljava/lang/String;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    goto :goto_3

    nop

    :goto_1
    invoke-static {v0, p0, p1}, Lcom/android/provision/utils/OTHelper;->rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_2

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->getName()Ljava/lang/String;

    move-result-object p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_TermsAndStatementFragment__recordPageStayTime',
        'method': '.method protected recordPageStayTime()V',
        'method_name': 'recordPageStayTime',
        'method_anchors': ['invoke-virtual {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->getName()Ljava/lang/String;', 'invoke-static {}, Ljava/lang/System;->currentTimeMillis()J', 'iget-wide v3, p0, Lcom/android/provision/fragment/TermsAndStatementFragment;->mUserStayStartTime:J', 'invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdPageStayTimeEvent(Ljava/lang/String;J)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected recordPageStayTime()V
    .registers 6

    invoke-virtual {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->getName()Ljava/lang/String;

    move-result-object v0

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v1

    iget-wide v3, p0, Lcom/android/provision/fragment/TermsAndStatementFragment;->mUserStayStartTime:J

    sub-long/2addr v1, v3

    invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdPageStayTimeEvent(Ljava/lang/String;J)V

    return-void
.end method""",
        'replacement': """.method protected recordPageStayTime()V
    .registers 6

    goto :goto_5

    nop

    :goto_0
    sub-long/2addr v1, v3

    goto :goto_2

    nop

    :goto_1
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v1

    goto :goto_3

    nop

    :goto_2
    invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdPageStayTimeEvent(Ljava/lang/String;J)V

    goto :goto_4

    nop

    :goto_3
    iget-wide v3, p0, Lcom/android/provision/fragment/TermsAndStatementFragment;->mUserStayStartTime:J

    goto :goto_0

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->getName()Ljava/lang/String;

    move-result-object v0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_TermsAndStatementFragment__goNext',
        'method': '.method public goNext()V',
        'method_name': 'goNext',
        'method_anchors': ['invoke-virtual {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->recordPageStayTime()V', 'const-string v0, "next"', 'invoke-virtual {p0, v0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->recordBottomButtonClick(Ljava/lang/String;)V', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'if-nez v0, :cond_0', 'return-void', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'invoke-static {v0, v1}, Lcom/android/provision/Utils;->setClauseAgreed(Landroid/content/Context;Z)V'],
        'type': 'policy_skip',
        'search': """.method public goNext()V
    .registers 5

    invoke-virtual {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->recordPageStayTime()V

    const-string v0, "next"

    invoke-virtual {p0, v0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->recordBottomButtonClick(Ljava/lang/String;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    if-nez v0, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    const/4 v1, 0x1

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->setClauseAgreed(Landroid/content/Context;Z)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->setTermsAgreedTime(Landroid/content/Context;)V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    new-instance v2, Landroid/content/Intent;

    const-string v3, "com.miui.clause_agreed"

    invoke-direct {v2, v3}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-static {v0, v2}, Lcom/android/provision/Utils;->sendBroadcastAsUser(Landroid/content/Context;Landroid/content/Intent;)V

    :cond_1
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v2, "device_provisioning_service_agreed"

    invoke-static {v0, v2, v1}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-direct {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->serviceStatementCompleteBroadcast()V

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showDataTrafficDialog()Z

    move-result v0

    if-eqz v0, :cond_3

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->mobileDataConfirmDisplayable()Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showDataConnectionReminderDialog()Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->showDataConnectionReminderDialog(Landroid/content/Context;)V

    return-void

    :cond_2
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->showNetworkAccessConfirmedDialog(Landroid/content/Context;)V

    return-void

    :cond_3
    if-nez v0, :cond_4

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isNeedDisableDataAfterPrivacy()Z

    move-result v0

    if-nez v0, :cond_4

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->setDataEnabled(Landroid/content/Context;)V

    :cond_4
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result v0

    const/4 v1, -0x1

    if-eqz v0, :cond_5

    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    const-string v2, "eSim"

    const/4 v3, 0x0

    invoke-virtual {v0, v2, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v2

    invoke-virtual {v2, v1, v0}, Landroid/app/Activity;->setResult(ILandroid/content/Intent;)V

    goto :goto_0

    :cond_5
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0, v1}, Landroid/app/Activity;->setResult(I)V

    :goto_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->finish()V

    invoke-direct {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->sendMiMoverBleBroadCast()V

    return-void
.end method""",
        'replacement': """.method public goNext()V
    .registers 5

    invoke-virtual {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->recordPageStayTime()V

    const-string v0, "next"

    invoke-virtual {p0, v0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->recordBottomButtonClick(Ljava/lang/String;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    if-nez v0, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    const/4 v1, 0x1

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->setClauseAgreed(Landroid/content/Context;Z)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->setTermsAgreedTime(Landroid/content/Context;)V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    new-instance v2, Landroid/content/Intent;

    const-string v3, "com.miui.clause_agreed"

    invoke-direct {v2, v3}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-static {v0, v2}, Lcom/android/provision/Utils;->sendBroadcastAsUser(Landroid/content/Context;Landroid/content/Intent;)V

    :cond_1
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v2, "device_provisioning_service_agreed"

    invoke-static {v0, v2, v1}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-direct {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->serviceStatementCompleteBroadcast()V

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showDataTrafficDialog()Z

    move-result v0

    if-eqz v0, :cond_3

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->mobileDataConfirmDisplayable()Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showDataConnectionReminderDialog()Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->showDataConnectionReminderDialog(Landroid/content/Context;)V

    return-void

    :cond_2
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->showNetworkAccessConfirmedDialog(Landroid/content/Context;)V

    return-void

    :cond_3
    if-nez v0, :cond_4

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isNeedDisableDataAfterPrivacy()Z

    move-result v0

    if-nez v0, :cond_4

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->setDataEnabled(Landroid/content/Context;)V

    :cond_4
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result v0

    const/4 v1, -0x1

    if-eqz v0, :cond_5

    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    const-string v2, "eSim"

    const/4 v3, 0x0

    invoke-virtual {v0, v2, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v2

    invoke-virtual {v2, v1, v0}, Landroid/app/Activity;->setResult(ILandroid/content/Intent;)V

    goto :goto_0

    :cond_5
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0, v1}, Landroid/app/Activity;->setResult(I)V

    :goto_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->finish()V

    invoke-direct {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->sendMiMoverBleBroadCast()V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_TermsAndStatementFragment__onDestroy',
        'method': '.method public onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/Fragment;->onDestroy()V', 'invoke-direct {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->requestRemoteConfigIfNeeded()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method public onDestroy()V
    .registers 1

    invoke-super {p0}, Landroidx/fragment/app/Fragment;->onDestroy()V

    invoke-direct {p0}, Lcom/android/provision/fragment/TermsAndStatementFragment;->requestRemoteConfigIfNeeded()V

    return-void
.end method""",
        'replacement': """.method public onDestroy()V
    .registers 1

    invoke-super {p0}, Landroidx/fragment/app/Fragment;->onDestroy()V

    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
