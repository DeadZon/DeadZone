TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/TermsFragment.smali'
CLASS_FALLBACK_NAMES = ['TermsFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseListFragment;', '.implements Landroid/widget/CompoundButton$OnCheckedChangeListener;', '.field private static final ACTION_KIKA_PRIVACY:Ljava/lang/String; = "com.qisi.launch.privacy"', '.field private static final DEVICE_FIRST_USING_DATA:Ljava/lang/String; = "device_first_using_data"', '.field private static final DEVICE_PROVISIONING_MOBILE_DATA_ENABLED:Ljava/lang/String; = "device_provisioning_mobile_data"', '.field private static final PRIVACY_TERMS_ADDITIONAL_AGREED:Ljava/lang/String; = "privacy_terms_additional_agreed"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_TermsFragment__needShowTrafficConfirmedDialog',
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
        'id': 'com_android_provision_fragment_TermsFragment__requestRemoteConfigIfNeeded',
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
        'id': 'com_android_provision_fragment_TermsFragment__setClick',
        'method': '.method private setClick()V',
        'method_name': 'setClick',
        'method_anchors': ['new-instance v0, Landroid/text/SpannableStringBuilder;', 'invoke-direct {v0}, Landroid/text/SpannableStringBuilder;-><init>()V', 'sget v1, Lcom/android/provision/R$string;->agree_terms:I', 'invoke-virtual {p0, v1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;', 'invoke-virtual {v0, v1}, Landroid/text/SpannableStringBuilder;->append(Ljava/lang/CharSequence;)Landroid/text/SpannableStringBuilder;', 'invoke-virtual {v0}, Landroid/text/SpannableStringBuilder;->length()I', 'sget v2, Lcom/android/provision/R$string;->poco_agree_terms_other:I', 'invoke-virtual {p0, v2}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;'],
        'type': 'policy_skip',
        'search': """.method private setClick()V
    .registers 6

    new-instance v0, Landroid/text/SpannableStringBuilder;

    invoke-direct {v0}, Landroid/text/SpannableStringBuilder;-><init>()V

    sget v1, Lcom/android/provision/R$string;->agree_terms:I

    invoke-virtual {p0, v1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/text/SpannableStringBuilder;->append(Ljava/lang/CharSequence;)Landroid/text/SpannableStringBuilder;

    invoke-virtual {v0}, Landroid/text/SpannableStringBuilder;->length()I

    move-result v1

    sget v2, Lcom/android/provision/R$string;->poco_agree_terms_other:I

    invoke-virtual {p0, v2}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/text/SpannableStringBuilder;->append(Ljava/lang/CharSequence;)Landroid/text/SpannableStringBuilder;

    const/4 v3, -0x1

    if-eq v1, v3, :cond_0

    new-instance v3, Lcom/android/provision/fragment/TermsFragment$TermsLinkSpan;

    const/16 v4, 0x9

    invoke-direct {v3, p0, v4}, Lcom/android/provision/fragment/TermsFragment$TermsLinkSpan;-><init>(Lcom/android/provision/fragment/TermsFragment;I)V

    invoke-virtual {v2}, Ljava/lang/String;->length()I

    move-result v2

    add-int/2addr v2, v1

    const/16 v4, 0x21

    invoke-virtual {v0, v3, v1, v2, v4}, Landroid/text/SpannableStringBuilder;->setSpan(Ljava/lang/Object;III)V

    :cond_0
    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v2, 0x0

    const v3, 0x106000d

    if-eqz v1, :cond_1

    iget-object v1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v1, v0}, Landroid/widget/CheckBox;->setText(Ljava/lang/CharSequence;)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->getColor(I)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/widget/CheckBox;->setHighlightColor(I)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-static {}, Landroid/text/method/LinkMovementMethod;->getInstance()Landroid/text/method/MovementMethod;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/widget/CheckBox;->setMovementMethod(Landroid/text/method/MovementMethod;)V

    iget-object p0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {p0, v2}, Landroid/widget/CheckBox;->setFocusable(Z)V

    return-void

    :cond_1
    iget-object v1, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-virtual {v1, v0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->getColor(I)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setHighlightColor(I)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-static {}, Landroid/text/method/LinkMovementMethod;->getInstance()Landroid/text/method/MovementMethod;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setMovementMethod(Landroid/text/method/MovementMethod;)V

    iget-object p0, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-virtual {p0, v2}, Landroid/widget/TextView;->setFocusable(Z)V

    return-void
.end method""",
        'replacement': """.method private setClick()V
    .registers 6

    new-instance v0, Landroid/text/SpannableStringBuilder;

    invoke-direct {v0}, Landroid/text/SpannableStringBuilder;-><init>()V

    sget v1, Lcom/android/provision/R$string;->agree_terms:I

    invoke-virtual {p0, v1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/text/SpannableStringBuilder;->append(Ljava/lang/CharSequence;)Landroid/text/SpannableStringBuilder;

    invoke-virtual {v0}, Landroid/text/SpannableStringBuilder;->length()I

    move-result v1

    sget v2, Lcom/android/provision/R$string;->poco_agree_terms_other:I

    invoke-virtual {p0, v2}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/text/SpannableStringBuilder;->append(Ljava/lang/CharSequence;)Landroid/text/SpannableStringBuilder;

    const/4 v3, -0x1

    if-eq v1, v3, :cond_0

    new-instance v3, Lcom/android/provision/fragment/TermsFragment$TermsLinkSpan;

    const/16 v4, 0x9

    invoke-direct {v3, p0, v4}, Lcom/android/provision/fragment/TermsFragment$TermsLinkSpan;-><init>(Lcom/android/provision/fragment/TermsFragment;I)V

    invoke-virtual {v2}, Ljava/lang/String;->length()I

    move-result v2

    add-int/2addr v2, v1

    const/16 v4, 0x21

    invoke-virtual {v0, v3, v1, v2, v4}, Landroid/text/SpannableStringBuilder;->setSpan(Ljava/lang/Object;III)V

    :cond_0
    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v2, 0x0

    const v3, 0x106000d

    if-eqz v1, :cond_1

    iget-object v1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v1, v0}, Landroid/widget/CheckBox;->setText(Ljava/lang/CharSequence;)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->getColor(I)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/widget/CheckBox;->setHighlightColor(I)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-static {}, Landroid/text/method/LinkMovementMethod;->getInstance()Landroid/text/method/MovementMethod;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/widget/CheckBox;->setMovementMethod(Landroid/text/method/MovementMethod;)V

    iget-object p0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {p0, v2}, Landroid/widget/CheckBox;->setFocusable(Z)V

    return-void

    :cond_1
    iget-object v1, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-virtual {v1, v0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1, v3}, Landroid/content/res/Resources;->getColor(I)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setHighlightColor(I)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-static {}, Landroid/text/method/LinkMovementMethod;->getInstance()Landroid/text/method/MovementMethod;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setMovementMethod(Landroid/text/method/MovementMethod;)V

    iget-object p0, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-virtual {p0, v2}, Landroid/widget/TextView;->setFocusable(Z)V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_TermsFragment__getName',
        'method': '.method protected getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['const-string p0, "TermsFragment"', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getName()Ljava/lang/String;
    .registers 1

    const-string p0, "TermsFragment"

    return-object p0
.end method""",
        'replacement': """.method protected getName()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const-string p0, "TermsFragment"

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
        'id': 'com_android_provision_fragment_TermsFragment__goNext',
        'method': '.method public goNext()V',
        'method_name': 'goNext',
        'method_anchors': ['invoke-virtual {p0}, Lcom/android/provision/fragment/BaseListFragment;->recordPageStayTime()V', 'const-string v0, "next"', 'invoke-virtual {p0, v0}, Lcom/android/provision/fragment/BaseListFragment;->recordBottomButtonClick(Ljava/lang/String;)V', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'if-nez v0, :cond_0', 'return-void', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'invoke-static {v0, v1}, Lcom/android/provision/Utils;->setClauseAgreed(Landroid/content/Context;Z)V'],
        'type': 'policy_skip',
        'search': """.method public goNext()V
    .registers 5

    invoke-virtual {p0}, Lcom/android/provision/fragment/BaseListFragment;->recordPageStayTime()V

    const-string v0, "next"

    invoke-virtual {p0, v0}, Lcom/android/provision/fragment/BaseListFragment;->recordBottomButtonClick(Ljava/lang/String;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    if-nez v0, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    const/4 v1, 0x1

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->setClauseAgreed(Landroid/content/Context;Z)V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v2

    invoke-virtual {v2}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    const-string v3, "privacy_terms_additional_agreed"

    invoke-static {v2, v3, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_1
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v1

    invoke-static {v1}, Lcom/android/provision/Utils;->setTermsAgreedTime(Landroid/content/Context;)V

    if-nez v0, :cond_2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    new-instance v1, Landroid/content/Intent;

    const-string v2, "com.miui.clause_agreed"

    invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->sendBroadcastAsUser(Landroid/content/Context;Landroid/content/Intent;)V

    :cond_2
    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showDataTrafficDialog()Z

    move-result v0

    if-eqz v0, :cond_4

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->mobileDataConfirmDisplayable()Z

    move-result v1

    if-eqz v1, :cond_4

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showDataConnectionReminderDialog()Z

    move-result v0

    if-eqz v0, :cond_3

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/TermsFragment;->showDataConnectionReminderDialog(Landroid/content/Context;)V

    return-void

    :cond_3
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/fragment/TermsFragment;->showNetworkAccessConfirmedDialog(Landroid/content/Context;)V

    return-void

    :cond_4
    if-nez v0, :cond_5

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isNeedDisableDataAfterPrivacy()Z

    move-result v0

    if-nez v0, :cond_5

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/fragment/TermsFragment;->setDataEnabled(Landroid/content/Context;)V

    :cond_5
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result v0

    const/4 v1, -0x1

    if-eqz v0, :cond_6

    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    const-string v2, "eSim"

    const/4 v3, 0x0

    invoke-virtual {v0, v2, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v2

    invoke-virtual {v2, v1, v0}, Landroid/app/Activity;->setResult(ILandroid/content/Intent;)V

    goto :goto_0

    :cond_6
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0, v1}, Landroid/app/Activity;->setResult(I)V

    :goto_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-virtual {p0}, Landroid/app/Activity;->finish()V

    return-void
.end method""",
        'replacement': """.method public goNext()V
    .registers 5

    invoke-virtual {p0}, Lcom/android/provision/fragment/BaseListFragment;->recordPageStayTime()V

    const-string v0, "next"

    invoke-virtual {p0, v0}, Lcom/android/provision/fragment/BaseListFragment;->recordBottomButtonClick(Ljava/lang/String;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    if-nez v0, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    const/4 v1, 0x1

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->setClauseAgreed(Landroid/content/Context;Z)V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v2

    invoke-virtual {v2}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    const-string v3, "privacy_terms_additional_agreed"

    invoke-static {v2, v3, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_1
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v1

    invoke-static {v1}, Lcom/android/provision/Utils;->setTermsAgreedTime(Landroid/content/Context;)V

    if-nez v0, :cond_2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    new-instance v1, Landroid/content/Intent;

    const-string v2, "com.miui.clause_agreed"

    invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->sendBroadcastAsUser(Landroid/content/Context;Landroid/content/Intent;)V

    :cond_2
    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showDataTrafficDialog()Z

    move-result v0

    if-eqz v0, :cond_4

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->mobileDataConfirmDisplayable()Z

    move-result v1

    if-eqz v1, :cond_4

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->showDataConnectionReminderDialog()Z

    move-result v0

    if-eqz v0, :cond_3

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/provision/fragment/TermsFragment;->showDataConnectionReminderDialog(Landroid/content/Context;)V

    return-void

    :cond_3
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-static {p0}, Lcom/android/provision/fragment/TermsFragment;->showNetworkAccessConfirmedDialog(Landroid/content/Context;)V

    return-void

    :cond_4
    if-nez v0, :cond_5

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isNeedDisableDataAfterPrivacy()Z

    move-result v0

    if-nez v0, :cond_5

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/fragment/TermsFragment;->setDataEnabled(Landroid/content/Context;)V

    :cond_5
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result v0

    const/4 v1, -0x1

    if-eqz v0, :cond_6

    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    const-string v2, "eSim"

    const/4 v3, 0x0

    invoke-virtual {v0, v2, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;I)Landroid/content/Intent;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v2

    invoke-virtual {v2, v1, v0}, Landroid/app/Activity;->setResult(ILandroid/content/Intent;)V

    goto :goto_0

    :cond_6
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0, v1}, Landroid/app/Activity;->setResult(I)V

    :goto_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-virtual {p0}, Landroid/app/Activity;->finish()V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_TermsFragment__onDestroy',
        'method': '.method public onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/Fragment;->onDestroy()V', 'invoke-direct {p0}, Lcom/android/provision/fragment/TermsFragment;->requestRemoteConfigIfNeeded()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method public onDestroy()V
    .registers 1

    invoke-super {p0}, Landroidx/fragment/app/Fragment;->onDestroy()V

    invoke-direct {p0}, Lcom/android/provision/fragment/TermsFragment;->requestRemoteConfigIfNeeded()V

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
    {
        'id': 'com_android_provision_fragment_TermsFragment__onViewCreated',
        'method': '.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V',
        'method_name': 'onViewCreated',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroidx/fragment/app/ListFragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'if-nez p2, :cond_0', 'return-void', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'invoke-static {p2}, Lcom/android/provision/Utils;->getNextView(Landroid/app/Activity;)Landroid/widget/Button;', 'iput-object p2, p0, Lcom/android/provision/fragment/TermsFragment;->mNext:Landroid/view/View;', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z'],
        'type': 'policy_skip',
        'search': """.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V
    .registers 8

    invoke-super {p0, p1, p2}, Landroidx/fragment/app/ListFragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p2

    if-nez p2, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p2

    invoke-static {p2}, Lcom/android/provision/Utils;->getNextView(Landroid/app/Activity;)Landroid/widget/Button;

    move-result-object p2

    iput-object p2, p0, Lcom/android/provision/fragment/TermsFragment;->mNext:Landroid/view/View;

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_1

    instance-of v1, p2, Landroid/widget/TextView;

    if-eqz v1, :cond_1

    check-cast p2, Landroid/widget/TextView;

    sget v1, Lcom/android/provision/R$string;->agree_and_next:I

    invoke-virtual {p2, v1}, Landroid/widget/TextView;->setText(I)V

    :cond_1
    new-instance p2, Ljava/util/ArrayList;

    invoke-direct {p2}, Ljava/util/ArrayList;-><init>()V

    iput-object p2, p0, Lcom/android/provision/fragment/TermsFragment;->mLicenseType:Ljava/util/ArrayList;

    sget v1, Lcom/android/provision/R$string;->user_agreement:I

    invoke-virtual {p0, v1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    iget-object p2, p0, Lcom/android/provision/fragment/TermsFragment;->mLicenseType:Ljava/util/ArrayList;

    sget v1, Lcom/android/provision/R$string;->privacy_policy:I

    invoke-virtual {p0, v1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getImmId()Ljava/lang/String;

    move-result-object p2

    invoke-static {p2}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    const-string v2, "com.mint.keyboard/.services.MintKeyboard"

    const-string v3, ""

    if-nez v1, :cond_4

    invoke-static {p2, v2}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v1

    sget v3, Lcom/android/provision/R$string;->mint_keyboard_oobe_terms:I

    invoke-virtual {v1, v3}, Landroid/app/Activity;->getString(I)Ljava/lang/String;

    move-result-object v3

    goto :goto_0

    :cond_2
    const-string v1, "com.kikaoem.xiaomi.qisiemoji.inputmethod/com.android.inputmethod.latin.LatinIME"

    invoke-static {p2, v1}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v1

    sget v3, Lcom/android/provision/R$string;->terms_privacy_policy_input_method_kika:I

    invoke-virtual {v1, v3}, Landroid/app/Activity;->getString(I)Ljava/lang/String;

    move-result-object v3

    :cond_3
    :goto_0
    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_4

    iget-object v1, p0, Lcom/android/provision/fragment/TermsFragment;->mLicenseType:Ljava/util/ArrayList;

    invoke-virtual {v1, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :cond_4
    invoke-virtual {p0}, Landroidx/fragment/app/ListFragment;->getListView()Landroid/widget/ListView;

    move-result-object v1

    iget-object v4, p0, Lcom/android/provision/fragment/TermsFragment;->mLicenseAdapter:Lcom/android/provision/fragment/TermsFragment$LicenseAdapter;

    invoke-virtual {v1, v4}, Landroid/widget/ListView;->setAdapter(Landroid/widget/ListAdapter;)V

    invoke-virtual {p0}, Landroidx/fragment/app/ListFragment;->getListView()Landroid/widget/ListView;

    move-result-object v1

    new-instance v4, Lcom/android/provision/fragment/TermsFragment$1;

    invoke-direct {v4, p0, v3, p2}, Lcom/android/provision/fragment/TermsFragment$1;-><init>(Lcom/android/provision/fragment/TermsFragment;Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v1, v4}, Landroid/widget/ListView;->setOnItemClickListener(Landroid/widget/AdapterView$OnItemClickListener;)V

    sget v1, Lcom/android/provision/R$id;->checkbox_agree:I

    invoke-virtual {p1, v1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/CheckBox;

    iput-object v1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    sget v1, Lcom/android/provision/R$id;->text_agree:I

    invoke-virtual {p1, v1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/TextView;

    iput-object v1, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    const/16 v1, 0x8

    const/4 v3, 0x0

    if-eqz v0, :cond_6

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v0, v3}, Landroid/widget/CheckBox;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mNext:Landroid/view/View;

    iget-object v4, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v4}, Landroid/widget/CheckBox;->isChecked()Z

    move-result v4

    invoke-virtual {v0, v4}, Landroid/view/View;->setEnabled(Z)V

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isTermPageCheck()Z

    move-result v0

    if-eqz v0, :cond_5

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    const/4 v4, 0x1

    invoke-virtual {v0, v4}, Landroid/widget/CheckBox;->setChecked(Z)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mNext:Landroid/view/View;

    invoke-virtual {v0, v4}, Landroid/view/View;->setEnabled(Z)V

    goto :goto_1

    :cond_5
    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v0, v3}, Landroid/widget/CheckBox;->setChecked(Z)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mNext:Landroid/view/View;

    invoke-virtual {v0, v3}, Landroid/view/View;->setEnabled(Z)V

    :goto_1
    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setVisibility(I)V

    goto :goto_2

    :cond_6
    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v0, v1}, Landroid/widget/CheckBox;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-virtual {v0, v3}, Landroid/widget/TextView;->setVisibility(I)V

    :goto_2
    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v0, p0}, Landroid/widget/CheckBox;->setOnCheckedChangeListener(Landroid/widget/CompoundButton$OnCheckedChangeListener;)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    sget v1, Lcom/android/provision/R$string;->agree_terms:I

    invoke-virtual {v0, v1}, Landroid/widget/CheckBox;->setText(I)V

    invoke-static {p2}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_7

    const-string v0, "com.preff.kb.xm/com.preff.kb.LatinIME"

    invoke-static {p2, v0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_7

    const-string v0, "com.google.android.inputmethod.latin/com.android.inputmethod.latin.LatinIME"

    invoke-static {p2, v0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_7

    const-string v0, "ru.yandex.androidkeyboard/com.android.inputmethod.latin.LatinIME"

    invoke-static {p2, v0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_7

    sget v0, Lcom/android/provision/R$id;->checkbox_agree_imm:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/CheckBox;

    iput-object p1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxImm:Landroid/widget/CheckBox;

    invoke-virtual {p1, v3}, Landroid/widget/CheckBox;->setVisibility(I)V

    iget-object p1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxImm:Landroid/widget/CheckBox;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-direct {p0, p2, v0}, Lcom/android/provision/fragment/TermsFragment;->getDefaultImmAgreeTerms(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Landroid/widget/CheckBox;->setText(Ljava/lang/CharSequence;)V

    iget-object p1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxImm:Landroid/widget/CheckBox;

    invoke-virtual {p1, p0}, Landroid/widget/CheckBox;->setOnCheckedChangeListener(Landroid/widget/CompoundButton$OnCheckedChangeListener;)V

    invoke-static {p2, v2}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p1

    if-eqz p1, :cond_7

    iget-object p1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxImm:Landroid/widget/CheckBox;

    invoke-virtual {p1, v3}, Landroid/widget/CheckBox;->setChecked(Z)V

    :cond_7
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-direct {p0, p1}, Lcom/android/provision/fragment/TermsFragment;->showDataTrafficConfirmedDialog(Landroid/content/Context;)V

    return-void
.end method""",
        'replacement': """.method public onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V
    .registers 8

    invoke-super {p0, p1, p2}, Landroidx/fragment/app/ListFragment;->onViewCreated(Landroid/view/View;Landroid/os/Bundle;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p2

    if-nez p2, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p2

    invoke-static {p2}, Lcom/android/provision/Utils;->getNextView(Landroid/app/Activity;)Landroid/widget/Button;

    move-result-object p2

    iput-object p2, p0, Lcom/android/provision/fragment/TermsFragment;->mNext:Landroid/view/View;

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_1

    instance-of v1, p2, Landroid/widget/TextView;

    if-eqz v1, :cond_1

    check-cast p2, Landroid/widget/TextView;

    sget v1, Lcom/android/provision/R$string;->agree_and_next:I

    invoke-virtual {p2, v1}, Landroid/widget/TextView;->setText(I)V

    :cond_1
    new-instance p2, Ljava/util/ArrayList;

    invoke-direct {p2}, Ljava/util/ArrayList;-><init>()V

    iput-object p2, p0, Lcom/android/provision/fragment/TermsFragment;->mLicenseType:Ljava/util/ArrayList;

    sget v1, Lcom/android/provision/R$string;->user_agreement:I

    invoke-virtual {p0, v1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    iget-object p2, p0, Lcom/android/provision/fragment/TermsFragment;->mLicenseType:Ljava/util/ArrayList;

    sget v1, Lcom/android/provision/R$string;->privacy_policy:I

    invoke-virtual {p0, v1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->getImmId()Ljava/lang/String;

    move-result-object p2

    invoke-static {p2}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    const-string v2, "com.mint.keyboard/.services.MintKeyboard"

    const-string v3, ""

    if-nez v1, :cond_4

    invoke-static {p2, v2}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v1

    sget v3, Lcom/android/provision/R$string;->mint_keyboard_oobe_terms:I

    invoke-virtual {v1, v3}, Landroid/app/Activity;->getString(I)Ljava/lang/String;

    move-result-object v3

    goto :goto_0

    :cond_2
    const-string v1, "com.kikaoem.xiaomi.qisiemoji.inputmethod/com.android.inputmethod.latin.LatinIME"

    invoke-static {p2, v1}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v1

    sget v3, Lcom/android/provision/R$string;->terms_privacy_policy_input_method_kika:I

    invoke-virtual {v1, v3}, Landroid/app/Activity;->getString(I)Ljava/lang/String;

    move-result-object v3

    :cond_3
    :goto_0
    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-nez v1, :cond_4

    iget-object v1, p0, Lcom/android/provision/fragment/TermsFragment;->mLicenseType:Ljava/util/ArrayList;

    invoke-virtual {v1, v3}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :cond_4
    invoke-virtual {p0}, Landroidx/fragment/app/ListFragment;->getListView()Landroid/widget/ListView;

    move-result-object v1

    iget-object v4, p0, Lcom/android/provision/fragment/TermsFragment;->mLicenseAdapter:Lcom/android/provision/fragment/TermsFragment$LicenseAdapter;

    invoke-virtual {v1, v4}, Landroid/widget/ListView;->setAdapter(Landroid/widget/ListAdapter;)V

    invoke-virtual {p0}, Landroidx/fragment/app/ListFragment;->getListView()Landroid/widget/ListView;

    move-result-object v1

    new-instance v4, Lcom/android/provision/fragment/TermsFragment$1;

    invoke-direct {v4, p0, v3, p2}, Lcom/android/provision/fragment/TermsFragment$1;-><init>(Lcom/android/provision/fragment/TermsFragment;Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v1, v4}, Landroid/widget/ListView;->setOnItemClickListener(Landroid/widget/AdapterView$OnItemClickListener;)V

    sget v1, Lcom/android/provision/R$id;->checkbox_agree:I

    invoke-virtual {p1, v1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/CheckBox;

    iput-object v1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    sget v1, Lcom/android/provision/R$id;->text_agree:I

    invoke-virtual {p1, v1}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/widget/TextView;

    iput-object v1, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    const/16 v1, 0x8

    const/4 v3, 0x0

    if-eqz v0, :cond_6

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v0, v3}, Landroid/widget/CheckBox;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mNext:Landroid/view/View;

    iget-object v4, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v4}, Landroid/widget/CheckBox;->isChecked()Z

    move-result v4

    invoke-virtual {v0, v4}, Landroid/view/View;->setEnabled(Z)V

    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isTermPageCheck()Z

    move-result v0

    if-eqz v0, :cond_5

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    const/4 v4, 0x1

    invoke-virtual {v0, v4}, Landroid/widget/CheckBox;->setChecked(Z)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mNext:Landroid/view/View;

    invoke-virtual {v0, v4}, Landroid/view/View;->setEnabled(Z)V

    goto :goto_1

    :cond_5
    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v0, v3}, Landroid/widget/CheckBox;->setChecked(Z)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mNext:Landroid/view/View;

    invoke-virtual {v0, v3}, Landroid/view/View;->setEnabled(Z)V

    :goto_1
    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setVisibility(I)V

    goto :goto_2

    :cond_6
    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v0, v1}, Landroid/widget/CheckBox;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mTextAgree:Landroid/widget/TextView;

    invoke-virtual {v0, v3}, Landroid/widget/TextView;->setVisibility(I)V

    :goto_2
    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    invoke-virtual {v0, p0}, Landroid/widget/CheckBox;->setOnCheckedChangeListener(Landroid/widget/CompoundButton$OnCheckedChangeListener;)V

    iget-object v0, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxAgree:Landroid/widget/CheckBox;

    sget v1, Lcom/android/provision/R$string;->agree_terms:I

    invoke-virtual {v0, v1}, Landroid/widget/CheckBox;->setText(I)V

    invoke-static {p2}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_7

    const-string v0, "com.preff.kb.xm/com.preff.kb.LatinIME"

    invoke-static {p2, v0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_7

    const-string v0, "com.google.android.inputmethod.latin/com.android.inputmethod.latin.LatinIME"

    invoke-static {p2, v0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_7

    const-string v0, "ru.yandex.androidkeyboard/com.android.inputmethod.latin.LatinIME"

    invoke-static {p2, v0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_7

    sget v0, Lcom/android/provision/R$id;->checkbox_agree_imm:I

    invoke-virtual {p1, v0}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/CheckBox;

    iput-object p1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxImm:Landroid/widget/CheckBox;

    invoke-virtual {p1, v3}, Landroid/widget/CheckBox;->setVisibility(I)V

    iget-object p1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxImm:Landroid/widget/CheckBox;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-direct {p0, p2, v0}, Lcom/android/provision/fragment/TermsFragment;->getDefaultImmAgreeTerms(Ljava/lang/String;Landroid/content/Context;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Landroid/widget/CheckBox;->setText(Ljava/lang/CharSequence;)V

    iget-object p1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxImm:Landroid/widget/CheckBox;

    invoke-virtual {p1, p0}, Landroid/widget/CheckBox;->setOnCheckedChangeListener(Landroid/widget/CompoundButton$OnCheckedChangeListener;)V

    invoke-static {p2, v2}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p1

    if-eqz p1, :cond_7

    iget-object p1, p0, Lcom/android/provision/fragment/TermsFragment;->mCheckBoxImm:Landroid/widget/CheckBox;

    invoke-virtual {p1, v3}, Landroid/widget/CheckBox;->setChecked(Z)V

    :cond_7
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-direct {p0, p1}, Lcom/android/provision/fragment/TermsFragment;->showDataTrafficConfirmedDialog(Landroid/content/Context;)V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
