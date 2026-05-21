TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/OtherSettingsFragment.smali'
CLASS_FALLBACK_NAMES = ['OtherSettingsFragment.smali']
CLASS_ANCHORS = ['.super Lmiuix/preference/PreferenceFragment;', '.field private static final ACTION_SET_USE_LOCATION_FOR_SERVICES:Ljava/lang/String; = "com.google.android.gsf.action.SET_USE_LOCATION_FOR_SERVICES"', '.field private static final BUTTON_ALARM_ASSISTANCE_KEY:Ljava/lang/String; = "button_alarm_assistance_key"', '.field private static final BUTTON_AUTO_UPDATE_KEY:Ljava/lang/String; = "button_auto_update_key"', '.field private static final BUTTON_ENHANCED_LOCKSCREEN_KEY:Ljava/lang/String; = "button_enhanced_lockscreen_key"', '.field private static final BUTTON_GET_APPS_KEY:Ljava/lang/String; = "button_get_apps_key"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_OtherSettingsFragment__addGlobalUpdatePreference',
        'method': '.method private addGlobalUpdatePreference()V',
        'method_name': 'addGlobalUpdatePreference',
        'method_anchors': ['iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;', 'const-string v1, "OtherSettingsFragment"', 'if-nez v0, :cond_0', 'const-string p0, "addGlobalUpdatePreference: mCategory is null"', 'invoke-static {v1, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I', 'return-void', 'iget-boolean v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsINBuild:Z', 'if-eqz v2, :cond_2'],
        'type': 'method_replace',
        'search': """.method private addGlobalUpdatePreference()V
    .registers 5

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    const-string v1, "OtherSettingsFragment"

    if-nez v0, :cond_0

    const-string p0, "addGlobalUpdatePreference: mCategory is null"

    invoke-static {v1, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_0
    iget-boolean v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsINBuild:Z

    if-eqz v2, :cond_2

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAutoUpdatePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v0, v2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    invoke-static {}, Lcom/android/provision/SimInfoUtils;->getSimSlotCount()I

    move-result v0

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "simSlotCount: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    const/4 v1, 0x0

    if-nez v0, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v0, v2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v2, Lcom/android/provision/R$array;->other_settings_auto_update_at_no_simslot_entries:I

    invoke-virtual {v0, v2}, Landroid/content/res/Resources;->getStringArray(I)[Ljava/lang/String;

    move-result-object v0

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    aget-object v0, v0, v1

    invoke-virtual {v2, v0}, Lcom/android/provision/widget/ValueListPreference;->setRightValue(Ljava/lang/String;)V

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$4;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$4;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-virtual {v0, v1}, Landroidx/preference/Preference;->setOnPreferenceChangeListener(Landroidx/preference/Preference$OnPreferenceChangeListener;)V

    return-void

    :cond_1
    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v0, v2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    sget v2, Lcom/android/provision/R$array;->other_settings_auto_update_entries:I

    invoke-virtual {v0, v2}, Landroid/content/res/Resources;->getStringArray(I)[Ljava/lang/String;

    move-result-object v0

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    aget-object v0, v0, v1

    invoke-virtual {v2, v0}, Lcom/android/provision/widget/ValueListPreference;->setRightValue(Ljava/lang/String;)V

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$5;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$5;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-virtual {v0, v1}, Landroidx/preference/Preference;->setOnPreferenceChangeListener(Landroidx/preference/Preference$OnPreferenceChangeListener;)V

    return-void

    :cond_2
    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v0, v1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v0, p0}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    return-void
.end method""",
        'replacement': """.method private addGlobalUpdatePreference()V
    .registers 3

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    if-eqz v0, :cond_0

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAutoUpdatePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v0, v1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v0, v1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v0, p0}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :cond_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_OtherSettingsFragment__handleNext',
        'method': '.method private handleNext()V',
        'method_name': 'handleNext',
        'method_anchors': ['invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'invoke-static {}, Ljava/lang/System;->currentTimeMillis()J', 'iget-wide v3, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUserStayStartTime:J', 'invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdPageStayTimeEvent(Ljava/lang/String;J)V', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-virtual {v1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;'],
        'type': 'policy_skip',
        'search': """.method private handleNext()V
    .registers 16

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v0

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v1

    iget-wide v3, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUserStayStartTime:J

    sub-long/2addr v1, v3

    invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdPageStayTimeEvent(Ljava/lang/String;J)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v1

    const-string v2, "next"

    invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    new-instance v1, Ljava/util/HashMap;

    invoke-direct {v1}, Ljava/util/HashMap;-><init>()V

    invoke-static {}, Lcom/android/provision/Utils;->isCmTest()Z

    move-result v2

    iget-object v3, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationPreference:Landroidx/preference/CheckBoxPreference;

    const/4 v4, 0x1

    const/4 v5, 0x0

    if-eqz v3, :cond_2

    if-nez v2, :cond_1

    invoke-virtual {v3}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v2

    if-eqz v2, :cond_0

    goto :goto_0

    :cond_0
    move v2, v5

    goto :goto_1

    :cond_1
    :goto_0
    move v2, v4

    :cond_2
    :goto_1
    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->isRestricted()Z

    move-result v3

    if-nez v3, :cond_3

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v3

    invoke-static {}, Landroid/os/UserHandle;->myUserId()I

    move-result v6

    invoke-static {v3, v2, v6, v4}, Lcom/android/provision/Utils;->updateLocationEnabled(Landroid/content/Context;ZII)V

    :cond_3
    iget-object v3, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUserExperiencePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v3}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v3

    const-string v6, "upload_log_pref"

    invoke-static {v0, v6, v3}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-static {v6}, Lcom/android/provision/utils/MinorControlUtils;->isSupportMinorsControl(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_4

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v6

    iget-object v7, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mMinorModePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v7}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v7

    invoke-static {v6, v7}, Lcom/android/provision/Utils;->setMinorsModeFlag(Landroid/content/Context;Z)V

    :cond_4
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-static {v6}, Lcom/android/provision/Utils;->isShowMiShareItem(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_5

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v6

    iget-object v7, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mXiaomiSharePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v7}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v7

    invoke-static {v6, v7}, Lcom/android/provision/Utils;->setXiaomiShareFlag(Landroid/content/Context;Z)V

    :cond_5
    if-eqz v3, :cond_6

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v6

    invoke-static {v6}, Lcom/android/provision/utils/OTHelper;->setNetworkAccessEnabled(Landroid/content/Context;)V

    :cond_6
    iget-object v6, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationUsePreference:Landroidx/preference/CheckBoxPreference;

    if-eqz v6, :cond_7

    invoke-virtual {v6}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v6

    invoke-virtual {p0, v6}, Lcom/android/provision/fragment/OtherSettingsFragment;->setUseLocationForServices(Z)V

    :cond_7
    iget-object v6, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mQualityServicePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v6}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v6

    iget-object v7, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v7}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v7

    iget-object v8, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUploadDebugLogPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v8}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v8

    invoke-static {v0, v8}, Landroid/provider/MiuiSettings$Secure;->enableUploadDebugLog(Landroid/content/ContentResolver;Z)V

    iget-boolean v9, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsINBuild:Z

    const-string v10, "auto_download"

    const-string v11, "auto_update"

    if-nez v9, :cond_8

    iget-object v9, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAutoUpdatePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v9}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v9

    invoke-static {v0, v11, v9}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-static {v0, v10, v9}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_5

    :cond_8
    invoke-static {}, Lmiui/telephony/TelephonyManager;->getDefault()Lmiui/telephony/TelephonyManager;

    move-result-object v9

    invoke-virtual {v9}, Lmiui/telephony/TelephonyManager;->getPhoneCount()I

    move-result v9

    const/4 v12, 0x2

    if-nez v9, :cond_a

    iget-object v9, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v9}, Landroidx/preference/ListPreference;->getValue()Ljava/lang/String;

    move-result-object v9

    iget-object v13, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v13, v9}, Landroidx/preference/ListPreference;->findIndexOfValue(Ljava/lang/String;)I

    move-result v9

    if-ne v9, v4, :cond_9

    move v13, v5

    goto :goto_2

    :cond_9
    move v13, v4

    :goto_2
    move v14, v13

    move v13, v9

    move v9, v14

    move v14, v5

    goto :goto_4

    :cond_a
    iget-object v9, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v9}, Landroidx/preference/ListPreference;->getValue()Ljava/lang/String;

    move-result-object v9

    iget-object v13, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v13, v9}, Landroidx/preference/ListPreference;->findIndexOfValue(Ljava/lang/String;)I

    move-result v9

    if-eqz v9, :cond_b

    move v13, v5

    goto :goto_3

    :cond_b
    move v13, v4

    :goto_3
    move v14, v13

    move v13, v9

    if-ne v9, v12, :cond_c

    move v9, v5

    goto :goto_4

    :cond_c
    move v9, v4

    :goto_4
    invoke-static {v0, v11, v9}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-static {v0, v10, v9}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    const-string v10, "mobile_download"

    invoke-static {v0, v10, v14}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    sub-int/2addr v12, v13

    const-string v10, "com.xiaomi.discover.auto_update_enabled"

    invoke-static {v0, v10, v12}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    const-string v10, "global_auto_update_network_type"

    invoke-static {v12}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v1, v10, v11}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :goto_5
    sget-boolean v10, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v10, :cond_e

    iget-object v11, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v11}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v11

    invoke-direct {p0, v0, v11}, Lcom/android/provision/fragment/OtherSettingsFragment;->setPersonalizedAdEnable(Landroid/content/ContentResolver;Z)V

    invoke-direct {p0, v0, v4}, Lcom/android/provision/fragment/OtherSettingsFragment;->setPersonalizedAdDialogPromoted(Landroid/content/ContentResolver;Z)V

    if-eqz v11, :cond_d

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v11

    invoke-static {v0, v11, v12}, Lcom/android/provision/fragment/OtherSettingsFragment;->setPersonalizedAdEnableTime(Landroid/content/ContentResolver;J)V

    goto :goto_6

    :cond_d
    const-wide/16 v11, 0x0

    invoke-static {v0, v11, v12}, Lcom/android/provision/fragment/OtherSettingsFragment;->setPersonalizedAdEnableTime(Landroid/content/ContentResolver;J)V

    :cond_e
    :goto_6
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v4

    invoke-static {v4}, Lcom/android/provision/utils/CarouselUtils;->shouldShowOldCarousel(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_11

    iget-object v4, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mEnhancedLockscreenPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v4}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v4

    const/4 v11, 0x0

    if-eqz v4, :cond_f

    const-string v12, "com.miui.android.fashiongallery.lockscreen_magazine_provider"

    goto :goto_7

    :cond_f
    move-object v12, v11

    :goto_7
    const-string v13, "lock_wallpaper_provider_authority"

    invoke-static {v0, v13, v12}, Lmiuix/provider/ExtraSettings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    const-string v12, "mifg_online_content"

    invoke-static {v0, v12, v4}, Lmiuix/provider/ExtraSettings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    if-eqz v4, :cond_10

    const-string v11, "oobe"

    :cond_10
    const-string v12, "wc_enable_source"

    invoke-static {v0, v12, v11}, Lmiuix/provider/ExtraSettings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    invoke-static {}, Lmiui/os/Build;->getRegion()Ljava/lang/String;

    move-result-object v0

    iget-object v11, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCarouselProvisionMessageBean:Lcom/android/provision/beans/CarouselProvisionMessageBean;

    invoke-virtual {v0}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;

    move-result-object v12

    invoke-static {v0}, Lcom/android/provision/utils/CarouselUtils;->getCurrentSource(Ljava/lang/String;)I

    move-result v0

    invoke-virtual {v11, v12, v0, v4}, Lcom/android/provision/beans/CarouselProvisionMessageBean;->build(Ljava/lang/String;IZ)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    iget-object v4, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCarouselProvisionMessageBean:Lcom/android/provision/beans/CarouselProvisionMessageBean;

    invoke-static {v0, v4}, Lcom/android/provision/utils/CarouselUtils;->setCarouselInfoData(Landroid/content/Context;Lcom/android/provision/beans/CarouselProvisionMessageBean;)V

    :cond_11
    const-string v0, "location_state"

    invoke-static {v2}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "user_experience_state"

    invoke-static {v3}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "auto_update_state"

    invoke-static {v9}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "quality_service_state"

    invoke-static {v6}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "button_upload_debug_log_key"

    invoke-static {v8}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "interconnection_service"

    if-nez v10, :cond_12

    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v2

    if-eqz v2, :cond_12

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v2}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v2

    invoke-static {v2}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :cond_12
    invoke-static {}, Lcom/android/provision/Utils;->isSupportGlobalInterconnectionEntrance()Z

    move-result v2

    if-eqz v2, :cond_13

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v2}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v2

    invoke-static {v2}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :cond_13
    const-string v0, "alarm_assistance_state"

    invoke-static {v7}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "key_click_other_setting_continue"

    invoke-static {v0, v1}, Lcom/android/provision/utils/OTHelper;->rdCountEvent(Ljava/lang/String;Ljava/util/Map;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->enableSOTIDeviceOwner(Landroid/content/Context;)V

    invoke-static {}, Lcom/android/provision/Utils;->isMiuiSupportSystemappUninstallV2()Z

    move-result v0

    if-nez v0, :cond_14

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->handleNextShortcut()V

    goto :goto_8

    :cond_14
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    const-string v1, "com.miui.voiceassist"

    invoke-static {v0, v1, v5}, Lcom/android/provision/utils/ShortcutProviderUtils;->setPackageShortcutEnable(Landroid/content/Context;Ljava/lang/String;Z)V

    :goto_8
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    const/4 v1, -0x1

    invoke-virtual {v0, v1}, Landroid/app/Activity;->setResult(I)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p0

    invoke-virtual {p0}, Landroid/app/Activity;->finish()V

    return-void
.end method""",
        'replacement': """.method private handleNext()V
    .registers 16

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v0

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v1

    iget-wide v3, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUserStayStartTime:J

    sub-long/2addr v1, v3

    invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdPageStayTimeEvent(Ljava/lang/String;J)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v1

    const-string v2, "next"

    invoke-static {v0, v1, v2}, Lcom/android/provision/utils/OTHelper;->rdBottomButtonEvent(Landroid/app/Activity;Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    new-instance v1, Ljava/util/HashMap;

    invoke-direct {v1}, Ljava/util/HashMap;-><init>()V

    invoke-static {}, Lcom/android/provision/Utils;->isCmTest()Z

    move-result v2

    iget-object v3, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationPreference:Landroidx/preference/CheckBoxPreference;

    const/4 v4, 0x1

    const/4 v5, 0x0

    if-eqz v3, :cond_2

    if-nez v2, :cond_1

    invoke-virtual {v3}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v2

    if-eqz v2, :cond_0

    goto :goto_0

    :cond_0
    move v2, v5

    goto :goto_1

    :cond_1
    :goto_0
    move v2, v4

    :cond_2
    :goto_1
    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->isRestricted()Z

    move-result v3

    if-nez v3, :cond_3

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v3

    invoke-static {}, Landroid/os/UserHandle;->myUserId()I

    move-result v6

    invoke-static {v3, v2, v6, v4}, Lcom/android/provision/Utils;->updateLocationEnabled(Landroid/content/Context;ZII)V

    :cond_3
    iget-object v3, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUserExperiencePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v3}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v3

    const-string v6, "upload_log_pref"

    invoke-static {v0, v6, v3}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-static {v6}, Lcom/android/provision/utils/MinorControlUtils;->isSupportMinorsControl(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_4

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v6

    iget-object v7, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mMinorModePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v7}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v7

    invoke-static {v6, v7}, Lcom/android/provision/Utils;->setMinorsModeFlag(Landroid/content/Context;Z)V

    :cond_4
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-static {v6}, Lcom/android/provision/Utils;->isShowMiShareItem(Landroid/content/Context;)Z

    move-result v6

    if-eqz v6, :cond_5

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v6

    iget-object v7, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mXiaomiSharePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v7}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v7

    invoke-static {v6, v7}, Lcom/android/provision/Utils;->setXiaomiShareFlag(Landroid/content/Context;Z)V

    :cond_5
    if-eqz v3, :cond_6

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v6

    invoke-static {v6}, Lcom/android/provision/utils/OTHelper;->setNetworkAccessEnabled(Landroid/content/Context;)V

    :cond_6
    iget-object v6, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationUsePreference:Landroidx/preference/CheckBoxPreference;

    if-eqz v6, :cond_7

    invoke-virtual {v6}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v6

    invoke-virtual {p0, v6}, Lcom/android/provision/fragment/OtherSettingsFragment;->setUseLocationForServices(Z)V

    :cond_7
    iget-object v6, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mQualityServicePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v6}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v6

    iget-object v7, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v7}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v7

    iget-object v8, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUploadDebugLogPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v8}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v8

    invoke-static {v0, v8}, Landroid/provider/MiuiSettings$Secure;->enableUploadDebugLog(Landroid/content/ContentResolver;Z)V

    iget-boolean v9, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsINBuild:Z

    const-string v10, "auto_download"

    const-string v11, "auto_update"

    if-nez v9, :cond_8

    iget-object v9, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAutoUpdatePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v9}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v9

    invoke-static {v0, v11, v9}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-static {v0, v10, v9}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_5

    :cond_8
    invoke-static {}, Lmiui/telephony/TelephonyManager;->getDefault()Lmiui/telephony/TelephonyManager;

    move-result-object v9

    invoke-virtual {v9}, Lmiui/telephony/TelephonyManager;->getPhoneCount()I

    move-result v9

    const/4 v12, 0x2

    if-nez v9, :cond_a

    iget-object v9, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v9}, Landroidx/preference/ListPreference;->getValue()Ljava/lang/String;

    move-result-object v9

    iget-object v13, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v13, v9}, Landroidx/preference/ListPreference;->findIndexOfValue(Ljava/lang/String;)I

    move-result v9

    if-ne v9, v4, :cond_9

    move v13, v5

    goto :goto_2

    :cond_9
    move v13, v4

    :goto_2
    move v14, v13

    move v13, v9

    move v9, v14

    move v14, v5

    goto :goto_4

    :cond_a
    iget-object v9, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v9}, Landroidx/preference/ListPreference;->getValue()Ljava/lang/String;

    move-result-object v9

    iget-object v13, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    invoke-virtual {v13, v9}, Landroidx/preference/ListPreference;->findIndexOfValue(Ljava/lang/String;)I

    move-result v9

    if-eqz v9, :cond_b

    move v13, v5

    goto :goto_3

    :cond_b
    move v13, v4

    :goto_3
    move v14, v13

    move v13, v9

    if-ne v9, v12, :cond_c

    move v9, v5

    goto :goto_4

    :cond_c
    move v9, v4

    :goto_4
    invoke-static {v0, v11, v9}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-static {v0, v10, v9}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    const-string v10, "mobile_download"

    invoke-static {v0, v10, v14}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    sub-int/2addr v12, v13

    const-string v10, "com.xiaomi.discover.auto_update_enabled"

    invoke-static {v0, v10, v12}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    const-string v10, "global_auto_update_network_type"

    invoke-static {v12}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v11

    invoke-virtual {v1, v10, v11}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :goto_5
    sget-boolean v10, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v10, :cond_e

    iget-object v11, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v11}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v11

    invoke-direct {p0, v0, v11}, Lcom/android/provision/fragment/OtherSettingsFragment;->setPersonalizedAdEnable(Landroid/content/ContentResolver;Z)V

    invoke-direct {p0, v0, v4}, Lcom/android/provision/fragment/OtherSettingsFragment;->setPersonalizedAdDialogPromoted(Landroid/content/ContentResolver;Z)V

    if-eqz v11, :cond_d

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v11

    invoke-static {v0, v11, v12}, Lcom/android/provision/fragment/OtherSettingsFragment;->setPersonalizedAdEnableTime(Landroid/content/ContentResolver;J)V

    goto :goto_6

    :cond_d
    const-wide/16 v11, 0x0

    invoke-static {v0, v11, v12}, Lcom/android/provision/fragment/OtherSettingsFragment;->setPersonalizedAdEnableTime(Landroid/content/ContentResolver;J)V

    :cond_e
    :goto_6
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v4

    invoke-static {v4}, Lcom/android/provision/utils/CarouselUtils;->shouldShowOldCarousel(Landroid/content/Context;)Z

    move-result v4

    if-eqz v4, :cond_11

    iget-object v4, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mEnhancedLockscreenPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v4}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v4

    const/4 v11, 0x0

    if-eqz v4, :cond_f

    const-string v12, "com.miui.android.fashiongallery.lockscreen_magazine_provider"

    goto :goto_7

    :cond_f
    move-object v12, v11

    :goto_7
    const-string v13, "lock_wallpaper_provider_authority"

    invoke-static {v0, v13, v12}, Lmiuix/provider/ExtraSettings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    const-string v12, "mifg_online_content"

    invoke-static {v0, v12, v4}, Lmiuix/provider/ExtraSettings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    if-eqz v4, :cond_10

    const-string v11, "oobe"

    :cond_10
    const-string v12, "wc_enable_source"

    invoke-static {v0, v12, v11}, Lmiuix/provider/ExtraSettings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    invoke-static {}, Lmiui/os/Build;->getRegion()Ljava/lang/String;

    move-result-object v0

    iget-object v11, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCarouselProvisionMessageBean:Lcom/android/provision/beans/CarouselProvisionMessageBean;

    invoke-virtual {v0}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;

    move-result-object v12

    invoke-static {v0}, Lcom/android/provision/utils/CarouselUtils;->getCurrentSource(Ljava/lang/String;)I

    move-result v0

    invoke-virtual {v11, v12, v0, v4}, Lcom/android/provision/beans/CarouselProvisionMessageBean;->build(Ljava/lang/String;IZ)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    iget-object v4, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCarouselProvisionMessageBean:Lcom/android/provision/beans/CarouselProvisionMessageBean;

    invoke-static {v0, v4}, Lcom/android/provision/utils/CarouselUtils;->setCarouselInfoData(Landroid/content/Context;Lcom/android/provision/beans/CarouselProvisionMessageBean;)V

    :cond_11
    const-string v0, "location_state"

    invoke-static {v2}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "user_experience_state"

    invoke-static {v3}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "auto_update_state"

    invoke-static {v9}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "quality_service_state"

    invoke-static {v6}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "button_upload_debug_log_key"

    invoke-static {v8}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "interconnection_service"

    if-nez v10, :cond_12

    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v2

    if-eqz v2, :cond_12

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v2}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v2

    invoke-static {v2}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :cond_12
    invoke-static {}, Lcom/android/provision/Utils;->isSupportGlobalInterconnectionEntrance()Z

    move-result v2

    if-eqz v2, :cond_13

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v2}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v2

    invoke-static {v2}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :cond_13
    const-string v0, "alarm_assistance_state"

    invoke-static {v7}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v0, v2}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    const-string v0, "key_click_other_setting_continue"

    invoke-static {v0, v1}, Lcom/android/provision/utils/OTHelper;->rdCountEvent(Ljava/lang/String;Ljava/util/Map;)V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->enableSOTIDeviceOwner(Landroid/content/Context;)V

    invoke-static {}, Lcom/android/provision/Utils;->isMiuiSupportSystemappUninstallV2()Z

    move-result v0

    if-nez v0, :cond_14

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->handleNextShortcut()V

    goto :goto_8

    :cond_14
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    const-string v1, "com.miui.voiceassist"

    invoke-static {v0, v1, v5}, Lcom/android/provision/utils/ShortcutProviderUtils;->setPackageShortcutEnable(Landroid/content/Context;Ljava/lang/String;Z)V

    :goto_8
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    const/4 v1, -0x1

    invoke-virtual {v0, v1}, Landroid/app/Activity;->setResult(I)V

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
        'id': 'com_android_provision_fragment_OtherSettingsFragment__handleNextShortcut',
        'method': '.method private handleNextShortcut()V',
        'method_name': 'handleNextShortcut',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'invoke-static {}, Lcom/android/provision/utils/ShortcutProviderUtils;->isDeviceNotSupportShortCut()Z', 'if-eqz v0, :cond_1', 'return-void', 'new-instance v0, Ljava/lang/Thread;', 'new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda7;', 'invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda7;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V'],
        'type': 'policy_skip',
        'search': """.method private handleNextShortcut()V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {}, Lcom/android/provision/utils/ShortcutProviderUtils;->isDeviceNotSupportShortCut()Z

    move-result v0

    if-eqz v0, :cond_1

    :goto_0
    return-void

    :cond_1
    new-instance v0, Ljava/lang/Thread;

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda7;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda7;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-direct {v0, v1}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V

    invoke-virtual {v0}, Ljava/lang/Thread;->start()V

    return-void
.end method""",
        'replacement': """.method private handleNextShortcut()V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {}, Lcom/android/provision/utils/ShortcutProviderUtils;->isDeviceNotSupportShortCut()Z

    move-result v0

    if-eqz v0, :cond_1

    :goto_0
    return-void

    :cond_1
    new-instance v0, Ljava/lang/Thread;

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda7;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda7;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-direct {v0, v1}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V

    invoke-virtual {v0}, Ljava/lang/Thread;->start()V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_OtherSettingsFragment__initInterconnectionPreference',
        'method': '.method private initInterconnectionPreference()V',
        'method_name': 'initInterconnectionPreference',
        'method_anchors': ['iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;', 'if-eqz v0, :cond_6', 'iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;', 'if-nez v0, :cond_0', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_2', 'invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;', 'invoke-virtual {v1}, Ljava/lang/Boolean;->booleanValue()Z'],
        'type': 'policy_skip',
        'search': """.method private initInterconnectionPreference()V
    .registers 4

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    if-eqz v0, :cond_6

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_2

    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v1

    if-nez v1, :cond_1

    goto :goto_0

    :cond_1
    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->addAppendStr()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Lcom/android/provision/widget/CTACheckboxPreference;->setAdditionalDescription(Ljava/lang/CharSequence;)V

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->InterconnectionLinkageLogic(Landroidx/preference/CheckBoxPreference;)V

    goto :goto_1

    :cond_2
    :goto_0
    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v1, v2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :goto_1
    invoke-static {}, Lcom/android/provision/Utils;->isSupportGlobalInterconnectionEntrance()Z

    move-result v1

    if-eqz v1, :cond_3

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    sget v2, Lcom/android/provision/R$string;->interconnection_service_summary_global:I

    invoke-virtual {p0, v2}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Lcom/android/provision/widget/CTACheckboxPreference;->setAdditionalDescription(Ljava/lang/CharSequence;)V

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->InterconnectionLinkageLogic(Landroidx/preference/CheckBoxPreference;)V

    goto :goto_2

    :cond_3
    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v1, v2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :goto_2
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isInterconnectionPortalState()Z

    move-result v1

    if-nez v1, :cond_5

    const/4 v1, 0x1

    invoke-static {v1}, Lcom/android/provision/DefaultPreferenceHelper;->setInterconnectionPortalState(Z)V

    if-eqz v0, :cond_4

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    goto :goto_3

    :cond_4
    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    :goto_3
    invoke-direct {p0, v0}, Lcom/android/provision/fragment/OtherSettingsFragment;->interconnectionPreferencePartSwitch(Landroidx/preference/CheckBoxPreference;)V

    :cond_5
    return-void

    :cond_6
    :goto_4
    const-string p0, "OtherSettingsFragment"

    const-string v0, "initInterconnectionPreference: preference is null"

    invoke-static {p0, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method""",
        'replacement': """.method private initInterconnectionPreference()V
    .registers 4

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    if-eqz v0, :cond_6

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_2

    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v1

    if-nez v1, :cond_1

    goto :goto_0

    :cond_1
    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->addAppendStr()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Lcom/android/provision/widget/CTACheckboxPreference;->setAdditionalDescription(Ljava/lang/CharSequence;)V

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->InterconnectionLinkageLogic(Landroidx/preference/CheckBoxPreference;)V

    goto :goto_1

    :cond_2
    :goto_0
    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v1, v2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :goto_1
    invoke-static {}, Lcom/android/provision/Utils;->isSupportGlobalInterconnectionEntrance()Z

    move-result v1

    if-eqz v1, :cond_3

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    sget v2, Lcom/android/provision/R$string;->interconnection_service_summary_global:I

    invoke-virtual {p0, v2}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Lcom/android/provision/widget/CTACheckboxPreference;->setAdditionalDescription(Ljava/lang/CharSequence;)V

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->InterconnectionLinkageLogic(Landroidx/preference/CheckBoxPreference;)V

    goto :goto_2

    :cond_3
    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v1, v2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :goto_2
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isInterconnectionPortalState()Z

    move-result v1

    if-nez v1, :cond_5

    const/4 v1, 0x1

    invoke-static {v1}, Lcom/android/provision/DefaultPreferenceHelper;->setInterconnectionPortalState(Z)V

    if-eqz v0, :cond_4

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    goto :goto_3

    :cond_4
    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    :goto_3
    invoke-direct {p0, v0}, Lcom/android/provision/fragment/OtherSettingsFragment;->interconnectionPreferencePartSwitch(Landroidx/preference/CheckBoxPreference;)V

    :cond_5
    return-void

    :cond_6
    :goto_4
    const-string p0, "OtherSettingsFragment"

    const-string v0, "initInterconnectionPreference: preference is null"

    invoke-static {p0, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_OtherSettingsFragment__initPersonalRecommandAdPreference',
        'method': '.method private initPersonalRecommandAdPreference()V',
        'method_name': 'initPersonalRecommandAdPreference',
        'method_anchors': ['iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;', 'if-nez v0, :cond_0', 'return-void', 'sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v1, :cond_1', 'iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;', 'invoke-virtual {p0, v0}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z', 'return-void'],
        'type': 'policy_skip',
        'search': """.method private initPersonalRecommandAdPreference()V
    .registers 3

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    if-nez v0, :cond_0

    return-void

    :cond_0
    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v1, :cond_1

    iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    invoke-virtual {p0, v0}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    return-void

    :cond_1
    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$6;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$6;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-virtual {v0, v1}, Landroidx/preference/Preference;->setOnPreferenceChangeListener(Landroidx/preference/Preference$OnPreferenceChangeListener;)V

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v0}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    sget v0, Lcom/android/provision/R$string;->other_settings_ad_enable_summary:I

    invoke-virtual {p0, v0}, Landroidx/preference/Preference;->setSummary(I)V

    return-void

    :cond_2
    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->getPersonalRecommandAdContent()Landroid/text/SpannableStringBuilder;

    move-result-object p0

    invoke-virtual {v0, p0}, Landroidx/preference/Preference;->setSummary(Ljava/lang/CharSequence;)V

    return-void
.end method""",
        'replacement': """.method private initPersonalRecommandAdPreference()V
    .registers 3

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    if-nez v0, :cond_0

    return-void

    :cond_0
    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v1, :cond_1

    iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    invoke-virtual {p0, v0}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    return-void

    :cond_1
    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$6;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$6;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-virtual {v0, v1}, Landroidx/preference/Preference;->setOnPreferenceChangeListener(Landroidx/preference/Preference$OnPreferenceChangeListener;)V

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v0}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    sget v0, Lcom/android/provision/R$string;->other_settings_ad_enable_summary:I

    invoke-virtual {p0, v0}, Landroidx/preference/Preference;->setSummary(I)V

    return-void

    :cond_2
    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->getPersonalRecommandAdContent()Landroid/text/SpannableStringBuilder;

    move-result-object p0

    invoke-virtual {v0, p0}, Landroidx/preference/Preference;->setSummary(Ljava/lang/CharSequence;)V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_OtherSettingsFragment__initShortcutPreference',
        'method': '.method private initShortcutPreference()V',
        'method_name': 'initShortcutPreference',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'invoke-static {}, Lcom/android/provision/utils/ShortcutProviderUtils;->isDeviceNotSupportShortCut()Z', 'if-eqz v0, :cond_1', 'return-void', 'new-instance v0, Ljava/lang/Thread;', 'new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda2;', 'invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda2;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V'],
        'type': 'policy_skip',
        'search': """.method private initShortcutPreference()V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {}, Lcom/android/provision/utils/ShortcutProviderUtils;->isDeviceNotSupportShortCut()Z

    move-result v0

    if-eqz v0, :cond_1

    :goto_0
    return-void

    :cond_1
    new-instance v0, Ljava/lang/Thread;

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda2;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda2;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-direct {v0, v1}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V

    invoke-virtual {v0}, Ljava/lang/Thread;->start()V

    return-void
.end method""",
        'replacement': """.method private initShortcutPreference()V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-static {}, Lcom/android/provision/utils/ShortcutProviderUtils;->isDeviceNotSupportShortCut()Z

    move-result v0

    if-eqz v0, :cond_1

    :goto_0
    return-void

    :cond_1
    new-instance v0, Ljava/lang/Thread;

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda2;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda2;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-direct {v0, v1}, Ljava/lang/Thread;-><init>(Ljava/lang/Runnable;)V

    invoke-virtual {v0}, Ljava/lang/Thread;->start()V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_OtherSettingsFragment__showPrivacyDialog',
        'method': '.method private showPrivacyDialog(Landroid/content/Context;Z)V',
        'method_name': 'showPrivacyDialog',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'invoke-static {}, Lmiui/os/Build;->getRegion()Ljava/lang/String;', 'invoke-virtual {v0}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;', 'invoke-static {v0}, Lcom/android/provision/utils/CarouselUtils;->getCurrentCarousel(Ljava/lang/String;)Lcom/android/provision/beans/CarouselBean;', 'if-eqz v4, :cond_1', 'invoke-virtual {v4}, Lcom/android/provision/beans/CarouselBean;->isRecord()Z', 'if-eqz v2, :cond_1'],
        'type': 'policy_skip',
        'search': """.method private showPrivacyDialog(Landroid/content/Context;Z)V
    .registers 20

    move-object/from16 v1, p0

    move/from16 v3, p2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    goto :goto_7

    :cond_0
    invoke-static {}, Lmiui/os/Build;->getRegion()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/utils/CarouselUtils;->getCurrentCarousel(Ljava/lang/String;)Lcom/android/provision/beans/CarouselBean;

    move-result-object v4

    const/4 v0, 0x0

    const/4 v8, 0x1

    if-eqz v4, :cond_1

    invoke-virtual {v4}, Lcom/android/provision/beans/CarouselBean;->isRecord()Z

    move-result v2

    if-eqz v2, :cond_1

    move v2, v8

    goto :goto_0

    :cond_1
    move v2, v0

    :goto_0
    if-eqz v4, :cond_a

    if-eqz v2, :cond_2

    if-eqz v3, :cond_2

    goto :goto_7

    :cond_2
    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v2

    const v5, 0x102000a

    invoke-virtual {v2, v5}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v2

    move-object v7, v2

    check-cast v7, Landroid/widget/ListView;

    if-eqz v3, :cond_3

    if-eqz v7, :cond_3

    invoke-virtual {v7, v0}, Landroid/widget/ListView;->setStackFromBottom(Z)V

    :cond_3
    invoke-static/range {p1 .. p1}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v2

    sget v5, Lcom/android/provision/R$layout;->layout_dialog_wc_protocol:I

    const/4 v6, 0x0

    invoke-virtual {v2, v5, v6}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v2

    sget v5, Lcom/android/provision/R$id;->switch_dialog_summary:I

    invoke-virtual {v2, v5}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v5

    check-cast v5, Landroid/widget/TextView;

    sget v6, Lcom/android/provision/R$id;->switch_dialog_privacy_content:I

    invoke-virtual {v2, v6}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v6

    check-cast v6, Landroid/widget/TextView;

    sget v9, Lcom/android/provision/R$id;->wc_pre_img_id:I

    invoke-virtual {v2, v9}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v9

    check-cast v9, Landroid/widget/ImageView;

    sget v10, Lcom/android/provision/R$id;->btn_sure:I

    invoke-virtual {v2, v10}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v10

    check-cast v10, Landroid/widget/Button;

    sget v11, Lcom/android/provision/R$id;->vs_reject:I

    invoke-virtual {v2, v11}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v11

    check-cast v11, Landroid/view/ViewStub;

    invoke-virtual {v11}, Landroid/view/ViewStub;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v12

    if-eqz v3, :cond_4

    sget v13, Lcom/android/provision/R$string;->wc_dialog_reject:I

    :goto_1
    move-object/from16 v14, p1

    goto :goto_2

    :cond_4
    sget v13, Lcom/android/provision/R$string;->wc_double_check_reject:I

    goto :goto_1

    :goto_2
    invoke-virtual {v14, v13}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v4}, Lcom/android/provision/beans/CarouselBean;->isGdpr()Z

    move-result v15

    if-eqz v15, :cond_5

    sget v15, Lcom/android/provision/R$layout;->layout_dialog_wc_protocol_reject_btn:I

    invoke-virtual {v11, v15}, Landroid/view/ViewStub;->setLayoutResource(I)V

    const/4 v15, -0x1

    iput v15, v12, Landroid/view/ViewGroup$LayoutParams;->width:I

    invoke-virtual {v11, v12}, Landroid/view/ViewStub;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    invoke-virtual {v11}, Landroid/view/ViewStub;->inflate()Landroid/view/View;

    move-result-object v11

    sget v12, Lcom/android/provision/R$id;->btn_wc_dialog_privacy_reject:I

    invoke-virtual {v11, v12}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v12

    check-cast v12, Landroid/widget/Button;

    invoke-virtual {v12, v13}, Landroid/widget/Button;->setText(Ljava/lang/CharSequence;)V

    invoke-virtual {v12, v0}, Landroid/widget/Button;->setClickable(Z)V

    goto :goto_3

    :cond_5
    sget v15, Lcom/android/provision/R$layout;->layout_dialog_wc_protocol_reject_tv:I

    invoke-virtual {v11, v15}, Landroid/view/ViewStub;->setLayoutResource(I)V

    const/4 v15, -0x2

    iput v15, v12, Landroid/view/ViewGroup$LayoutParams;->width:I

    invoke-virtual {v11, v12}, Landroid/view/ViewStub;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    invoke-virtual {v11}, Landroid/view/ViewStub;->inflate()Landroid/view/View;

    move-result-object v11

    sget v12, Lcom/android/provision/R$id;->tv_wc_dialog_privacy_reject:I

    invoke-virtual {v11, v12}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v12

    check-cast v12, Landroid/widget/TextView;

    invoke-virtual {v12}, Landroid/widget/TextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v15

    const/16 v0, 0x8

    invoke-virtual {v15, v0}, Landroid/text/TextPaint;->setFlags(I)V

    invoke-virtual {v12}, Landroid/widget/TextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    invoke-virtual {v0, v8}, Landroid/text/TextPaint;->setAntiAlias(Z)V

    invoke-virtual {v12, v13}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    :goto_3
    invoke-virtual {v4}, Lcom/android/provision/beans/CarouselBean;->getSource()I

    move-result v0

    const/4 v12, 0x5

    if-ne v0, v12, :cond_6

    sget v0, Lcom/android/provision/R$string;->privacy_content_one:I

    goto :goto_4

    :cond_6
    sget v0, Lcom/android/provision/R$string;->wc_notice_link_announcement_summary:I

    :goto_4
    invoke-static {v8}, Lcom/android/provision/utils/CarouselUtils;->getProtocolByType(I)Ljava/lang/String;

    move-result-object v13

    const/4 v15, 0x2

    invoke-static {v15}, Lcom/android/provision/utils/CarouselUtils;->getProtocolByType(I)Ljava/lang/String;

    move-result-object v15

    move/from16 v16, v8

    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v8

    filled-new-array {v13, v15}, [Ljava/lang/Object;

    move-result-object v13

    invoke-virtual {v8, v0, v13}, Landroid/app/Activity;->getString(I[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    if-eqz v3, :cond_7

    sget v8, Lcom/android/provision/R$drawable;->wc_dialog_pic_protocol:I

    invoke-virtual {v9, v8}, Landroid/widget/ImageView;->setImageResource(I)V

    sget v8, Lcom/android/provision/R$string;->wc_dialog_summary:I

    invoke-virtual {v5, v8}, Landroid/widget/TextView;->setText(I)V

    sget v5, Lcom/android/provision/R$string;->wc_dialog_agree:I

    invoke-virtual {v10, v5}, Landroid/widget/Button;->setText(I)V

    sput v16, Lcom/android/provision/beans/CarouselProvisionMessageBean$Store;->privacy:I

    goto :goto_5

    :cond_7
    sget v8, Lcom/android/provision/R$drawable;->wc_dialog_pic_protocol:I

    invoke-virtual {v9, v8}, Landroid/widget/ImageView;->setImageResource(I)V

    sget v8, Lcom/android/provision/R$string;->wc_double_check_summary:I

    invoke-virtual {v5, v8}, Landroid/widget/TextView;->setText(I)V

    sget v5, Lcom/android/provision/R$string;->wc_double_check_agree:I

    invoke-virtual {v10, v5}, Landroid/widget/Button;->setText(I)V

    invoke-virtual {v4}, Lcom/android/provision/beans/CarouselBean;->getSource()I

    move-result v5

    if-ne v5, v12, :cond_8

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    sget v8, Lcom/android/provision/R$string;->privacy_title:I

    invoke-virtual {v1, v8}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v5, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v8, ": "

    invoke-virtual {v5, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    :cond_8
    sput v16, Lcom/android/provision/beans/CarouselProvisionMessageBean$Store;->retrieve:I

    :goto_5
    invoke-static {v0}, Landroid/text/Html;->fromHtml(Ljava/lang/String;)Landroid/text/Spanned;

    move-result-object v0

    new-instance v5, Landroid/text/SpannableStringBuilder;

    invoke-direct {v5, v0}, Landroid/text/SpannableStringBuilder;-><init>(Ljava/lang/CharSequence;)V

    invoke-virtual {v6}, Landroid/widget/TextView;->getCurrentTextColor()I

    move-result v0

    const-string v8, "#3482FF"

    invoke-static {v8}, Landroid/graphics/Color;->parseColor(Ljava/lang/String;)I

    move-result v8

    invoke-direct {v1, v5, v0, v8}, Lcom/android/provision/fragment/OtherSettingsFragment;->getUniformColoredContent(Landroid/text/SpannableStringBuilder;II)Landroid/text/SpannableStringBuilder;

    move-result-object v0

    invoke-virtual {v6, v0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const v5, 0x106000d

    invoke-virtual {v0, v5}, Landroid/content/res/Resources;->getColor(I)I

    move-result v0

    invoke-virtual {v6, v0}, Landroid/widget/TextView;->setHighlightColor(I)V

    invoke-static {}, Landroid/text/method/LinkMovementMethod;->getInstance()Landroid/text/method/MovementMethod;

    move-result-object v0

    invoke-virtual {v6, v0}, Landroid/widget/TextView;->setMovementMethod(Landroid/text/method/MovementMethod;)V

    const/4 v0, 0x0

    invoke-virtual {v6, v0}, Landroid/widget/TextView;->setFocusable(Z)V

    new-instance v5, Lmiuix/appcompat/app/AlertDialog$Builder;

    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-direct {v5, v6}, Lmiuix/appcompat/app/AlertDialog$Builder;-><init>(Landroid/content/Context;)V

    invoke-virtual {v5, v0}, Lmiuix/appcompat/app/AlertDialog$Builder;->setCancelable(Z)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object v0

    if-eqz v3, :cond_9

    sget v5, Lcom/android/provision/R$string;->wc_dialog_title:I

    goto :goto_6

    :cond_9
    sget v5, Lcom/android/provision/R$string;->wc_double_check_title:I

    :goto_6
    invoke-virtual {v0, v5}, Lmiuix/appcompat/app/AlertDialog$Builder;->setTitle(I)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object v0

    invoke-virtual {v0, v2}, Lmiuix/appcompat/app/AlertDialog$Builder;->setView(Landroid/view/View;)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object v0

    new-instance v2, Lcom/android/provision/fragment/OtherSettingsFragment$2;

    invoke-direct {v2, v1, v3, v7}, Lcom/android/provision/fragment/OtherSettingsFragment$2;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;ZLandroid/widget/ListView;)V

    invoke-virtual {v0, v2}, Lmiuix/appcompat/app/AlertDialog$Builder;->setOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)Lmiuix/appcompat/app/AlertDialog$Builder;

    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$Builder;->create()Lmiuix/appcompat/app/AlertDialog;

    move-result-object v5

    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    new-instance v0, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda4;

    move-object v6, v5

    move-object v5, v14

    invoke-direct/range {v0 .. v7}, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda4;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;Landroid/content/ContentResolver;ZLcom/android/provision/beans/CarouselBean;Landroid/content/Context;Lmiuix/appcompat/app/AlertDialog;Landroid/widget/ListView;)V

    move-object v5, v6

    move-object v4, v7

    invoke-virtual {v10, v0}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    new-instance v0, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda5;

    move-object/from16 v1, p0

    move/from16 v3, p2

    invoke-direct/range {v0 .. v5}, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda5;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;Landroid/content/ContentResolver;ZLandroid/widget/ListView;Lmiuix/appcompat/app/AlertDialog;)V

    invoke-virtual {v11, v0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    invoke-virtual {v5}, Lmiuix/appcompat/app/AlertDialog;->show()V

    invoke-static/range {v16 .. v16}, Lcom/android/provision/utils/CarouselUtils;->setCurrentRegionRecord(Z)V

    :cond_a
    :goto_7
    return-void
.end method""",
        'replacement': """.method private showPrivacyDialog(Landroid/content/Context;Z)V
    .registers 20

    move-object/from16 v1, p0

    move/from16 v3, p2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    goto :goto_7

    :cond_0
    invoke-static {}, Lmiui/os/Build;->getRegion()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/String;->toUpperCase()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/utils/CarouselUtils;->getCurrentCarousel(Ljava/lang/String;)Lcom/android/provision/beans/CarouselBean;

    move-result-object v4

    const/4 v0, 0x0

    const/4 v8, 0x1

    if-eqz v4, :cond_1

    invoke-virtual {v4}, Lcom/android/provision/beans/CarouselBean;->isRecord()Z

    move-result v2

    if-eqz v2, :cond_1

    move v2, v8

    goto :goto_0

    :cond_1
    move v2, v0

    :goto_0
    if-eqz v4, :cond_a

    if-eqz v2, :cond_2

    if-eqz v3, :cond_2

    goto :goto_7

    :cond_2
    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v2

    const v5, 0x102000a

    invoke-virtual {v2, v5}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object v2

    move-object v7, v2

    check-cast v7, Landroid/widget/ListView;

    if-eqz v3, :cond_3

    if-eqz v7, :cond_3

    invoke-virtual {v7, v0}, Landroid/widget/ListView;->setStackFromBottom(Z)V

    :cond_3
    invoke-static/range {p1 .. p1}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v2

    sget v5, Lcom/android/provision/R$layout;->layout_dialog_wc_protocol:I

    const/4 v6, 0x0

    invoke-virtual {v2, v5, v6}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v2

    sget v5, Lcom/android/provision/R$id;->switch_dialog_summary:I

    invoke-virtual {v2, v5}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v5

    check-cast v5, Landroid/widget/TextView;

    sget v6, Lcom/android/provision/R$id;->switch_dialog_privacy_content:I

    invoke-virtual {v2, v6}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v6

    check-cast v6, Landroid/widget/TextView;

    sget v9, Lcom/android/provision/R$id;->wc_pre_img_id:I

    invoke-virtual {v2, v9}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v9

    check-cast v9, Landroid/widget/ImageView;

    sget v10, Lcom/android/provision/R$id;->btn_sure:I

    invoke-virtual {v2, v10}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v10

    check-cast v10, Landroid/widget/Button;

    sget v11, Lcom/android/provision/R$id;->vs_reject:I

    invoke-virtual {v2, v11}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v11

    check-cast v11, Landroid/view/ViewStub;

    invoke-virtual {v11}, Landroid/view/ViewStub;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v12

    if-eqz v3, :cond_4

    sget v13, Lcom/android/provision/R$string;->wc_dialog_reject:I

    :goto_1
    move-object/from16 v14, p1

    goto :goto_2

    :cond_4
    sget v13, Lcom/android/provision/R$string;->wc_double_check_reject:I

    goto :goto_1

    :goto_2
    invoke-virtual {v14, v13}, Landroid/content/Context;->getString(I)Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v4}, Lcom/android/provision/beans/CarouselBean;->isGdpr()Z

    move-result v15

    if-eqz v15, :cond_5

    sget v15, Lcom/android/provision/R$layout;->layout_dialog_wc_protocol_reject_btn:I

    invoke-virtual {v11, v15}, Landroid/view/ViewStub;->setLayoutResource(I)V

    const/4 v15, -0x1

    iput v15, v12, Landroid/view/ViewGroup$LayoutParams;->width:I

    invoke-virtual {v11, v12}, Landroid/view/ViewStub;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    invoke-virtual {v11}, Landroid/view/ViewStub;->inflate()Landroid/view/View;

    move-result-object v11

    sget v12, Lcom/android/provision/R$id;->btn_wc_dialog_privacy_reject:I

    invoke-virtual {v11, v12}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v12

    check-cast v12, Landroid/widget/Button;

    invoke-virtual {v12, v13}, Landroid/widget/Button;->setText(Ljava/lang/CharSequence;)V

    invoke-virtual {v12, v0}, Landroid/widget/Button;->setClickable(Z)V

    goto :goto_3

    :cond_5
    sget v15, Lcom/android/provision/R$layout;->layout_dialog_wc_protocol_reject_tv:I

    invoke-virtual {v11, v15}, Landroid/view/ViewStub;->setLayoutResource(I)V

    const/4 v15, -0x2

    iput v15, v12, Landroid/view/ViewGroup$LayoutParams;->width:I

    invoke-virtual {v11, v12}, Landroid/view/ViewStub;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    invoke-virtual {v11}, Landroid/view/ViewStub;->inflate()Landroid/view/View;

    move-result-object v11

    sget v12, Lcom/android/provision/R$id;->tv_wc_dialog_privacy_reject:I

    invoke-virtual {v11, v12}, Landroid/view/View;->findViewById(I)Landroid/view/View;

    move-result-object v12

    check-cast v12, Landroid/widget/TextView;

    invoke-virtual {v12}, Landroid/widget/TextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v15

    const/16 v0, 0x8

    invoke-virtual {v15, v0}, Landroid/text/TextPaint;->setFlags(I)V

    invoke-virtual {v12}, Landroid/widget/TextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    invoke-virtual {v0, v8}, Landroid/text/TextPaint;->setAntiAlias(Z)V

    invoke-virtual {v12, v13}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    :goto_3
    invoke-virtual {v4}, Lcom/android/provision/beans/CarouselBean;->getSource()I

    move-result v0

    const/4 v12, 0x5

    if-ne v0, v12, :cond_6

    sget v0, Lcom/android/provision/R$string;->privacy_content_one:I

    goto :goto_4

    :cond_6
    sget v0, Lcom/android/provision/R$string;->wc_notice_link_announcement_summary:I

    :goto_4
    invoke-static {v8}, Lcom/android/provision/utils/CarouselUtils;->getProtocolByType(I)Ljava/lang/String;

    move-result-object v13

    const/4 v15, 0x2

    invoke-static {v15}, Lcom/android/provision/utils/CarouselUtils;->getProtocolByType(I)Ljava/lang/String;

    move-result-object v15

    move/from16 v16, v8

    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v8

    filled-new-array {v13, v15}, [Ljava/lang/Object;

    move-result-object v13

    invoke-virtual {v8, v0, v13}, Landroid/app/Activity;->getString(I[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    if-eqz v3, :cond_7

    sget v8, Lcom/android/provision/R$drawable;->wc_dialog_pic_protocol:I

    invoke-virtual {v9, v8}, Landroid/widget/ImageView;->setImageResource(I)V

    sget v8, Lcom/android/provision/R$string;->wc_dialog_summary:I

    invoke-virtual {v5, v8}, Landroid/widget/TextView;->setText(I)V

    sget v5, Lcom/android/provision/R$string;->wc_dialog_agree:I

    invoke-virtual {v10, v5}, Landroid/widget/Button;->setText(I)V

    sput v16, Lcom/android/provision/beans/CarouselProvisionMessageBean$Store;->privacy:I

    goto :goto_5

    :cond_7
    sget v8, Lcom/android/provision/R$drawable;->wc_dialog_pic_protocol:I

    invoke-virtual {v9, v8}, Landroid/widget/ImageView;->setImageResource(I)V

    sget v8, Lcom/android/provision/R$string;->wc_double_check_summary:I

    invoke-virtual {v5, v8}, Landroid/widget/TextView;->setText(I)V

    sget v5, Lcom/android/provision/R$string;->wc_double_check_agree:I

    invoke-virtual {v10, v5}, Landroid/widget/Button;->setText(I)V

    invoke-virtual {v4}, Lcom/android/provision/beans/CarouselBean;->getSource()I

    move-result v5

    if-ne v5, v12, :cond_8

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    sget v8, Lcom/android/provision/R$string;->privacy_title:I

    invoke-virtual {v1, v8}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v5, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v8, ": "

    invoke-virtual {v5, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    :cond_8
    sput v16, Lcom/android/provision/beans/CarouselProvisionMessageBean$Store;->retrieve:I

    :goto_5
    invoke-static {v0}, Landroid/text/Html;->fromHtml(Ljava/lang/String;)Landroid/text/Spanned;

    move-result-object v0

    new-instance v5, Landroid/text/SpannableStringBuilder;

    invoke-direct {v5, v0}, Landroid/text/SpannableStringBuilder;-><init>(Ljava/lang/CharSequence;)V

    invoke-virtual {v6}, Landroid/widget/TextView;->getCurrentTextColor()I

    move-result v0

    const-string v8, "#3482FF"

    invoke-static {v8}, Landroid/graphics/Color;->parseColor(Ljava/lang/String;)I

    move-result v8

    invoke-direct {v1, v5, v0, v8}, Lcom/android/provision/fragment/OtherSettingsFragment;->getUniformColoredContent(Landroid/text/SpannableStringBuilder;II)Landroid/text/SpannableStringBuilder;

    move-result-object v0

    invoke-virtual {v6, v0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const v5, 0x106000d

    invoke-virtual {v0, v5}, Landroid/content/res/Resources;->getColor(I)I

    move-result v0

    invoke-virtual {v6, v0}, Landroid/widget/TextView;->setHighlightColor(I)V

    invoke-static {}, Landroid/text/method/LinkMovementMethod;->getInstance()Landroid/text/method/MovementMethod;

    move-result-object v0

    invoke-virtual {v6, v0}, Landroid/widget/TextView;->setMovementMethod(Landroid/text/method/MovementMethod;)V

    const/4 v0, 0x0

    invoke-virtual {v6, v0}, Landroid/widget/TextView;->setFocusable(Z)V

    new-instance v5, Lmiuix/appcompat/app/AlertDialog$Builder;

    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-direct {v5, v6}, Lmiuix/appcompat/app/AlertDialog$Builder;-><init>(Landroid/content/Context;)V

    invoke-virtual {v5, v0}, Lmiuix/appcompat/app/AlertDialog$Builder;->setCancelable(Z)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object v0

    if-eqz v3, :cond_9

    sget v5, Lcom/android/provision/R$string;->wc_dialog_title:I

    goto :goto_6

    :cond_9
    sget v5, Lcom/android/provision/R$string;->wc_double_check_title:I

    :goto_6
    invoke-virtual {v0, v5}, Lmiuix/appcompat/app/AlertDialog$Builder;->setTitle(I)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object v0

    invoke-virtual {v0, v2}, Lmiuix/appcompat/app/AlertDialog$Builder;->setView(Landroid/view/View;)Lmiuix/appcompat/app/AlertDialog$Builder;

    move-result-object v0

    new-instance v2, Lcom/android/provision/fragment/OtherSettingsFragment$2;

    invoke-direct {v2, v1, v3, v7}, Lcom/android/provision/fragment/OtherSettingsFragment$2;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;ZLandroid/widget/ListView;)V

    invoke-virtual {v0, v2}, Lmiuix/appcompat/app/AlertDialog$Builder;->setOnCancelListener(Landroid/content/DialogInterface$OnCancelListener;)Lmiuix/appcompat/app/AlertDialog$Builder;

    invoke-virtual {v0}, Lmiuix/appcompat/app/AlertDialog$Builder;->create()Lmiuix/appcompat/app/AlertDialog;

    move-result-object v5

    invoke-virtual {v1}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    new-instance v0, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda4;

    move-object v6, v5

    move-object v5, v14

    invoke-direct/range {v0 .. v7}, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda4;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;Landroid/content/ContentResolver;ZLcom/android/provision/beans/CarouselBean;Landroid/content/Context;Lmiuix/appcompat/app/AlertDialog;Landroid/widget/ListView;)V

    move-object v5, v6

    move-object v4, v7

    invoke-virtual {v10, v0}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    new-instance v0, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda5;

    move-object/from16 v1, p0

    move/from16 v3, p2

    invoke-direct/range {v0 .. v5}, Lcom/android/provision/fragment/OtherSettingsFragment$$ExternalSyntheticLambda5;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;Landroid/content/ContentResolver;ZLandroid/widget/ListView;Lmiuix/appcompat/app/AlertDialog;)V

    invoke-virtual {v11, v0}, Landroid/view/View;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    invoke-virtual {v5}, Lmiuix/appcompat/app/AlertDialog;->show()V

    invoke-static/range {v16 .. v16}, Lcom/android/provision/utils/CarouselUtils;->setCurrentRegionRecord(Z)V

    :cond_a
    :goto_7
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_OtherSettingsFragment__init',
        'method': '.method public constructor <init>()V',
        'method_name': '<init>',
        'method_anchors': ['invoke-direct {p0}, Lmiuix/preference/PreferenceFragment;-><init>()V', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'const-string v0, "IN"', 'invoke-static {v0}, Lmiui/os/Build;->checkRegion(Ljava/lang/String;)Z', 'if-eqz v0, :cond_0', 'iput-boolean v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsINBuild:Z', 'iput-boolean v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsScrolledBottom:Z'],
        'type': 'policy_skip',
        'search': """.method public constructor <init>()V
    .registers 3

    invoke-direct {p0}, Lmiuix/preference/PreferenceFragment;-><init>()V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    const-string v0, "IN"

    invoke-static {v0}, Lmiui/os/Build;->checkRegion(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    move v0, v1

    :goto_0
    iput-boolean v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsINBuild:Z

    iput-boolean v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsScrolledBottom:Z

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mShortcutWrapperList:Ljava/util/List;

    new-instance v0, Landroid/os/Handler;

    invoke-direct {v0}, Landroid/os/Handler;-><init>()V

    iput-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mNextViewStyleHander:Landroid/os/Handler;

    const-string v0, "com.xiaomi.continuity.ENABLE_STATIC_MICONNECT_CHANGED"

    iput-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->INTERCONNECTION_SWITCH_BROADCAST:Ljava/lang/String;

    const-string v0, "connectivityState"

    iput-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->INTERCONNECTION_SWITCH_STATE:Ljava/lang/String;

    new-instance v0, Lcom/android/provision/fragment/OtherSettingsFragment$3;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$3;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    iput-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mNextClickListener:Landroid/view/View$OnClickListener;

    return-void
.end method""",
        'replacement': """.method public constructor <init>()V
    .registers 3

    invoke-direct {p0}, Lmiuix/preference/PreferenceFragment;-><init>()V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    const-string v0, "IN"

    invoke-static {v0}, Lmiui/os/Build;->checkRegion(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    move v0, v1

    :goto_0
    iput-boolean v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsINBuild:Z

    iput-boolean v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsScrolledBottom:Z

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mShortcutWrapperList:Ljava/util/List;

    new-instance v0, Landroid/os/Handler;

    invoke-direct {v0}, Landroid/os/Handler;-><init>()V

    iput-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mNextViewStyleHander:Landroid/os/Handler;

    const-string v0, "com.xiaomi.continuity.ENABLE_STATIC_MICONNECT_CHANGED"

    iput-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->INTERCONNECTION_SWITCH_BROADCAST:Ljava/lang/String;

    const-string v0, "connectivityState"

    iput-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->INTERCONNECTION_SWITCH_STATE:Ljava/lang/String;

    new-instance v0, Lcom/android/provision/fragment/OtherSettingsFragment$3;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$3;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    iput-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mNextClickListener:Landroid/view/View$OnClickListener;

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_OtherSettingsFragment__onCreatePreferences',
        'method': '.method public onCreatePreferences(Landroid/os/Bundle;Ljava/lang/String;)V',
        'method_name': 'onCreatePreferences',
        'method_anchors': ['sget p1, Lcom/android/provision/R$xml;->other_settings:I', 'invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->addPreferencesFromResource(I)V', 'const-string p1, "other_settings_category"', 'invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;', 'check-cast p1, Landroidx/preference/PreferenceCategory;', 'iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;', 'const-string p1, "button_location_service_key"', 'invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;'],
        'type': 'policy_skip',
        'search': """.method public onCreatePreferences(Landroid/os/Bundle;Ljava/lang/String;)V
    .registers 8

    sget p1, Lcom/android/provision/R$xml;->other_settings:I

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->addPreferencesFromResource(I)V

    const-string p1, "other_settings_category"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/PreferenceCategory;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    const-string p1, "button_location_service_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationPreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_location_user_for_service_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationUsePreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_user_experience_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUserExperiencePreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_minor_mode_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mMinorModePreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_xiaomi_share_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mXiaomiSharePreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "mi_interconnection_service"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Lcom/android/provision/widget/CTACheckboxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    const-string p1, "mi_interconnection_service_global"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Lcom/android/provision/widget/CTACheckboxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object p1

    invoke-static {p1}, Lcom/android/provision/utils/MinorControlUtils;->isSupportMinorsControl(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object p2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mMinorModePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, p2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    goto :goto_0

    :cond_0
    sget p1, Lcom/android/provision/R$string;->other_settings_minor_mode_summary:I

    invoke-virtual {p0, p1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/Html;->fromHtml(Ljava/lang/String;)Landroid/text/Spanned;

    move-result-object p1

    iget-object p2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mMinorModePreference:Landroidx/preference/CheckBoxPreference;

    new-instance v0, Lcom/android/provision/fragment/OtherSettingsFragment$MinorModeSpan;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$MinorModeSpan;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-direct {p0, p2, p1, v0}, Lcom/android/provision/fragment/OtherSettingsFragment;->setNewClick(Landroidx/preference/Preference;Ljava/lang/CharSequence;Landroid/text/style/ClickableSpan;)V

    :goto_0
    const-string p1, "button_quality_service_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mQualityServicePreference:Landroidx/preference/CheckBoxPreference;

    sget-boolean p2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez p2, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    invoke-virtual {v0, p1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    goto :goto_1

    :cond_1
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mQualityServicePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v0}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v0

    const-string v1, "quality_service"

    invoke-static {p1, v1, v0}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :goto_1
    const-string p1, "button_alarm_assistance_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-static {}, Lcom/android/provision/Utils;->alarmAssistanceLimitedRange()Z

    move-result p1

    const/4 v0, 0x1

    if-eqz p1, :cond_2

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, v1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    goto :goto_3

    :cond_2
    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->initAlarmAssistance()V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    const/4 v2, -0x1

    if-eqz v1, :cond_3

    move v1, v0

    goto :goto_2

    :cond_3
    move v1, v2

    :goto_2
    const-string v3, "com_miui_warningcenter_pa_status"

    invoke-static {p1, v3, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    if-eqz v1, :cond_4

    move v2, v0

    :cond_4
    const-string v1, "com_miui_warningcenter_eps_status"

    invoke-static {p1, v1, v2}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :goto_3
    const-string p1, "button_get_apps_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-static {p1}, Lcom/android/provision/utils/MiAppsHelper;->shouldShowIndusApps(Landroid/content/Context;)Z

    move-result p1

    const-string v1, "auto_update_app_via_wifi"

    const-string v2, "OtherSettingsFragment"

    const/4 v3, 0x0

    if-eqz p1, :cond_5

    const-string p1, "support indus apps"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, v2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    invoke-static {p1, v1, v3}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_4

    :cond_5
    invoke-static {}, Lcom/android/provision/Utils;->unSupportGetAppsModels()Z

    move-result p1

    if-eqz p1, :cond_6

    const-string p1, "not support get apps"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    invoke-static {p1, v1, v3}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, v1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    goto :goto_4

    :cond_6
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p1

    const-string v4, "com.xiaomi.mipicks"

    invoke-static {p1, v4}, Lcom/android/provision/Utils;->judgeGetAppsEnable(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p1

    if-eqz p1, :cond_7

    const-string p1, "support get apps"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v2}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v2

    invoke-static {p1, v1, v2}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_4

    :cond_7
    const-string p1, "disable get apps"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    invoke-static {p1, v1, v3}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, v1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :goto_4
    const-string p1, "button_upload_debug_log_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUploadDebugLogPreference:Landroidx/preference/CheckBoxPreference;

    if-nez p2, :cond_8

    sget p2, Lcom/android/provision/R$string;->diagnose_report:I

    invoke-virtual {p1, p2}, Landroidx/preference/Preference;->setSummary(I)V

    :cond_8
    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object p1

    invoke-interface {p1}, Lmiui/enterprise/IRestrictionsHelper;->isGPSCloseRestriction()Z

    move-result p1

    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object p2

    invoke-interface {p2}, Lmiui/enterprise/IRestrictionsHelper;->isGPSRestriction()Z

    move-result p2

    if-nez p2, :cond_9

    if-eqz p1, :cond_b

    :cond_9
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v1, "location_mode"

    const/4 v2, 0x3

    invoke-static {p1, v1, v2}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p1

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationPreference:Landroidx/preference/CheckBoxPreference;

    if-ne p1, v2, :cond_a

    goto :goto_5

    :cond_a
    move v0, v3

    :goto_5
    invoke-virtual {v1, v0}, Landroidx/preference/TwoStatePreference;->setChecked(Z)V

    if-eqz p2, :cond_b

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, v3}, Landroidx/preference/Preference;->setEnabled(Z)V

    :cond_b
    const-string p1, "button_auto_update_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAutoUpdatePreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_personalized_ad_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_global_auto_update_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Lcom/android/provision/widget/ValueListPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    const-string p1, "button_global_auto_update_at_no_simslot_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Lcom/android/provision/widget/ValueListPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    const-string p1, "button_enhanced_lockscreen_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mEnhancedLockscreenPreference:Landroidx/preference/CheckBoxPreference;

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->addGlobalUpdatePreference()V

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUserExperiencePreference:Landroidx/preference/CheckBoxPreference;

    new-instance p2, Ljava/lang/StringBuilder;

    invoke-direct {p2}, Ljava/lang/StringBuilder;-><init>()V

    sget v0, Lcom/android/provision/R$string;->other_settings_user_experience_summary:I

    invoke-virtual {p0, v0}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v0, Lcom/android/provision/R$string;->other_settings_user_experience_summary_index:I

    invoke-virtual {p0, v0}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p2

    invoke-virtual {p0, v0}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    new-instance v2, Lcom/android/provision/fragment/OtherSettingsFragment$UserExpSpan;

    invoke-direct {v2, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$UserExpSpan;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-direct {p0, p1, p2, v1, v2}, Lcom/android/provision/fragment/OtherSettingsFragment;->setClick(Landroidx/preference/CheckBoxPreference;Ljava/lang/String;Ljava/lang/String;Landroid/text/style/ClickableSpan;)V

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUploadDebugLogPreference:Landroidx/preference/CheckBoxPreference;

    new-instance p2, Ljava/lang/StringBuilder;

    invoke-direct {p2}, Ljava/lang/StringBuilder;-><init>()V

    sget v1, Lcom/android/provision/R$string;->other_settings_upload_debug_log_summary:I

    invoke-virtual {p0, v1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, v0}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p2

    invoke-virtual {p0, v0}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v0

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$DetailExpSpan;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$DetailExpSpan;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-direct {p0, p1, p2, v0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->setClick(Landroidx/preference/CheckBoxPreference;Ljava/lang/String;Ljava/lang/String;Landroid/text/style/ClickableSpan;)V

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->initPersonalRecommandAdPreference()V

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->initLockscreenPreference()V

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->initInterconnectionPreference()V

    invoke-static {}, Lcom/android/provision/Utils;->isCmTest()Z

    move-result p1

    if-eqz p1, :cond_c

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object p2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, p2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :cond_c
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-static {p1}, Lcom/android/provision/Utils;->isShowMiShareItem(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_d

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object p2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mXiaomiSharePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, p2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :cond_d
    invoke-static {}, Lcom/android/provision/Utils;->isMiuiSupportSystemappUninstallV2()Z

    move-result p1

    if-nez p1, :cond_e

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->initShortcutPreference()V

    :cond_e
    return-void
.end method""",
        'replacement': """.method public onCreatePreferences(Landroid/os/Bundle;Ljava/lang/String;)V
    .registers 8

    sget p1, Lcom/android/provision/R$xml;->other_settings:I

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->addPreferencesFromResource(I)V

    const-string p1, "other_settings_category"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/PreferenceCategory;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    const-string p1, "button_location_service_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationPreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_location_user_for_service_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationUsePreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_user_experience_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUserExperiencePreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_minor_mode_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mMinorModePreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_xiaomi_share_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mXiaomiSharePreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "mi_interconnection_service"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Lcom/android/provision/widget/CTACheckboxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    const-string p1, "mi_interconnection_service_global"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Lcom/android/provision/widget/CTACheckboxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object p1

    invoke-static {p1}, Lcom/android/provision/utils/MinorControlUtils;->isSupportMinorsControl(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_0

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object p2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mMinorModePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, p2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    goto :goto_0

    :cond_0
    sget p1, Lcom/android/provision/R$string;->other_settings_minor_mode_summary:I

    invoke-virtual {p0, p1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/Html;->fromHtml(Ljava/lang/String;)Landroid/text/Spanned;

    move-result-object p1

    iget-object p2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mMinorModePreference:Landroidx/preference/CheckBoxPreference;

    new-instance v0, Lcom/android/provision/fragment/OtherSettingsFragment$MinorModeSpan;

    invoke-direct {v0, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$MinorModeSpan;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-direct {p0, p2, p1, v0}, Lcom/android/provision/fragment/OtherSettingsFragment;->setNewClick(Landroidx/preference/Preference;Ljava/lang/CharSequence;Landroid/text/style/ClickableSpan;)V

    :goto_0
    const-string p1, "button_quality_service_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mQualityServicePreference:Landroidx/preference/CheckBoxPreference;

    sget-boolean p2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez p2, :cond_1

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    invoke-virtual {v0, p1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    goto :goto_1

    :cond_1
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    iget-object v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mQualityServicePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v0}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v0

    const-string v1, "quality_service"

    invoke-static {p1, v1, v0}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :goto_1
    const-string p1, "button_alarm_assistance_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-static {}, Lcom/android/provision/Utils;->alarmAssistanceLimitedRange()Z

    move-result p1

    const/4 v0, 0x1

    if-eqz p1, :cond_2

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, v1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    goto :goto_3

    :cond_2
    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->initAlarmAssistance()V

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    const/4 v2, -0x1

    if-eqz v1, :cond_3

    move v1, v0

    goto :goto_2

    :cond_3
    move v1, v2

    :goto_2
    const-string v3, "com_miui_warningcenter_pa_status"

    invoke-static {p1, v3, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    if-eqz v1, :cond_4

    move v2, v0

    :cond_4
    const-string v1, "com_miui_warningcenter_eps_status"

    invoke-static {p1, v1, v2}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :goto_3
    const-string p1, "button_get_apps_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-static {p1}, Lcom/android/provision/utils/MiAppsHelper;->shouldShowIndusApps(Landroid/content/Context;)Z

    move-result p1

    const-string v1, "auto_update_app_via_wifi"

    const-string v2, "OtherSettingsFragment"

    const/4 v3, 0x0

    if-eqz p1, :cond_5

    const-string p1, "support indus apps"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, v2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    invoke-static {p1, v1, v3}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_4

    :cond_5
    invoke-static {}, Lcom/android/provision/Utils;->unSupportGetAppsModels()Z

    move-result p1

    if-eqz p1, :cond_6

    const-string p1, "not support get apps"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    invoke-static {p1, v1, v3}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, v1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    goto :goto_4

    :cond_6
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p1

    const-string v4, "com.xiaomi.mipicks"

    invoke-static {p1, v4}, Lcom/android/provision/Utils;->judgeGetAppsEnable(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p1

    if-eqz p1, :cond_7

    const-string p1, "support get apps"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v2}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v2

    invoke-static {p1, v1, v2}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_4

    :cond_7
    const-string p1, "disable get apps"

    invoke-static {v2, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    invoke-static {p1, v1, v3}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, v1}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :goto_4
    const-string p1, "button_upload_debug_log_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUploadDebugLogPreference:Landroidx/preference/CheckBoxPreference;

    if-nez p2, :cond_8

    sget p2, Lcom/android/provision/R$string;->diagnose_report:I

    invoke-virtual {p1, p2}, Landroidx/preference/Preference;->setSummary(I)V

    :cond_8
    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object p1

    invoke-interface {p1}, Lmiui/enterprise/IRestrictionsHelper;->isGPSCloseRestriction()Z

    move-result p1

    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object p2

    invoke-interface {p2}, Lmiui/enterprise/IRestrictionsHelper;->isGPSRestriction()Z

    move-result p2

    if-nez p2, :cond_9

    if-eqz p1, :cond_b

    :cond_9
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-virtual {p1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    const-string v1, "location_mode"

    const/4 v2, 0x3

    invoke-static {p1, v1, v2}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p1

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationPreference:Landroidx/preference/CheckBoxPreference;

    if-ne p1, v2, :cond_a

    goto :goto_5

    :cond_a
    move v0, v3

    :goto_5
    invoke-virtual {v1, v0}, Landroidx/preference/TwoStatePreference;->setChecked(Z)V

    if-eqz p2, :cond_b

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, v3}, Landroidx/preference/Preference;->setEnabled(Z)V

    :cond_b
    const-string p1, "button_auto_update_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAutoUpdatePreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_personalized_ad_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mPersonalizedAdPreference:Landroidx/preference/CheckBoxPreference;

    const-string p1, "button_global_auto_update_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Lcom/android/provision/widget/ValueListPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdatePreference:Lcom/android/provision/widget/ValueListPreference;

    const-string p1, "button_global_auto_update_at_no_simslot_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Lcom/android/provision/widget/ValueListPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGlobalAutoUpdateAtNoSimSlotPreference:Lcom/android/provision/widget/ValueListPreference;

    const-string p1, "button_enhanced_lockscreen_key"

    invoke-virtual {p0, p1}, Landroidx/preference/PreferenceFragmentCompat;->findPreference(Ljava/lang/CharSequence;)Landroidx/preference/Preference;

    move-result-object p1

    check-cast p1, Landroidx/preference/CheckBoxPreference;

    iput-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mEnhancedLockscreenPreference:Landroidx/preference/CheckBoxPreference;

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->addGlobalUpdatePreference()V

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUserExperiencePreference:Landroidx/preference/CheckBoxPreference;

    new-instance p2, Ljava/lang/StringBuilder;

    invoke-direct {p2}, Ljava/lang/StringBuilder;-><init>()V

    sget v0, Lcom/android/provision/R$string;->other_settings_user_experience_summary:I

    invoke-virtual {p0, v0}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v0, Lcom/android/provision/R$string;->other_settings_user_experience_summary_index:I

    invoke-virtual {p0, v0}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p2

    invoke-virtual {p0, v0}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    new-instance v2, Lcom/android/provision/fragment/OtherSettingsFragment$UserExpSpan;

    invoke-direct {v2, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$UserExpSpan;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-direct {p0, p1, p2, v1, v2}, Lcom/android/provision/fragment/OtherSettingsFragment;->setClick(Landroidx/preference/CheckBoxPreference;Ljava/lang/String;Ljava/lang/String;Landroid/text/style/ClickableSpan;)V

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mUploadDebugLogPreference:Landroidx/preference/CheckBoxPreference;

    new-instance p2, Ljava/lang/StringBuilder;

    invoke-direct {p2}, Ljava/lang/StringBuilder;-><init>()V

    sget v1, Lcom/android/provision/R$string;->other_settings_upload_debug_log_summary:I

    invoke-virtual {p0, v1}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, v0}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p2

    invoke-virtual {p0, v0}, Landroidx/fragment/app/Fragment;->getString(I)Ljava/lang/String;

    move-result-object v0

    new-instance v1, Lcom/android/provision/fragment/OtherSettingsFragment$DetailExpSpan;

    invoke-direct {v1, p0}, Lcom/android/provision/fragment/OtherSettingsFragment$DetailExpSpan;-><init>(Lcom/android/provision/fragment/OtherSettingsFragment;)V

    invoke-direct {p0, p1, p2, v0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->setClick(Landroidx/preference/CheckBoxPreference;Ljava/lang/String;Ljava/lang/String;Landroid/text/style/ClickableSpan;)V

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->initPersonalRecommandAdPreference()V

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->initLockscreenPreference()V

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->initInterconnectionPreference()V

    invoke-static {}, Lcom/android/provision/Utils;->isCmTest()Z

    move-result p1

    if-eqz p1, :cond_c

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object p2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mLocationPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, p2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :cond_c
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object p1

    invoke-static {p1}, Lcom/android/provision/Utils;->isShowMiShareItem(Landroid/content/Context;)Z

    move-result p1

    if-nez p1, :cond_d

    iget-object p1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mCategory:Landroidx/preference/PreferenceCategory;

    iget-object p2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mXiaomiSharePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p1, p2}, Landroidx/preference/PreferenceGroup;->removePreference(Landroidx/preference/Preference;)Z

    :cond_d
    invoke-static {}, Lcom/android/provision/Utils;->isMiuiSupportSystemappUninstallV2()Z

    move-result p1

    if-nez p1, :cond_e

    invoke-direct {p0}, Lcom/android/provision/fragment/OtherSettingsFragment;->initShortcutPreference()V

    :cond_e
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_fragment_OtherSettingsFragment__onStop',
        'method': '.method public onStop()V',
        'method_name': 'onStop',
        'method_anchors': ['invoke-super {p0}, Lmiuix/preference/PreferenceFragment;->onStop()V', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;', 'invoke-virtual {v1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;', 'iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mQualityServicePreference:Landroidx/preference/CheckBoxPreference;', 'invoke-virtual {v2}, Landroidx/preference/TwoStatePreference;->isChecked()Z', 'const-string v3, "quality_service"'],
        'type': 'policy_skip',
        'search': """.method public onStop()V
    .registers 6

    invoke-super {p0}, Lmiuix/preference/PreferenceFragment;->onStop()V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v1

    invoke-virtual {v1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mQualityServicePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v2}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v2

    const-string v3, "quality_service"

    invoke-static {v1, v3, v2}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_0
    if-nez v0, :cond_1

    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v1

    if-eqz v1, :cond_1

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->InterconnectionLinkageLogic(Landroidx/preference/CheckBoxPreference;)V

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    invoke-static {v1}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v1

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->sendBroadcastSwitchStatus(Ljava/lang/Object;)Z

    :cond_1
    invoke-static {}, Lcom/android/provision/Utils;->isSupportGlobalInterconnectionEntrance()Z

    move-result v1

    if-eqz v1, :cond_2

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->InterconnectionLinkageLogic(Landroidx/preference/CheckBoxPreference;)V

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    invoke-static {v1}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v1

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->sendBroadcastSwitchStatus(Ljava/lang/Object;)Z

    :cond_2
    if-nez v0, :cond_5

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    const/4 v2, -0x1

    const/4 v3, 0x1

    if-eqz v1, :cond_3

    move v1, v3

    goto :goto_0

    :cond_3
    move v1, v2

    :goto_0
    const-string v4, "com_miui_warningcenter_pa_status"

    invoke-static {v0, v4, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    if-eqz v1, :cond_4

    move v2, v3

    :cond_4
    const-string v1, "com_miui_warningcenter_eps_status"

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_5
    invoke-static {}, Lcom/android/provision/Utils;->unSupportGetAppsModels()Z

    move-result v0

    if-nez v0, :cond_6

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "com.xiaomi.mipicks"

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->judgeGetAppsEnable(Landroid/content/Context;Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_6

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    const-string v2, "auto_update_app_via_wifi"

    invoke-static {v0, v2, v1}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_6
    iget-boolean v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsINBuild:Z

    if-nez v0, :cond_7

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAutoUpdatePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    const-string v2, "auto_update"

    invoke-static {v0, v2, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAutoUpdatePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p0}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result p0

    const-string v1, "auto_download"

    invoke-static {v0, v1, p0}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_7
    return-void
.end method""",
        'replacement': """.method public onStop()V
    .registers 6

    invoke-super {p0}, Lmiuix/preference/PreferenceFragment;->onStop()V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v1

    invoke-virtual {v1}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget-object v2, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mQualityServicePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v2}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v2

    const-string v3, "quality_service"

    invoke-static {v1, v3, v2}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_0
    if-nez v0, :cond_1

    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v1

    if-eqz v1, :cond_1

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->InterconnectionLinkageLogic(Landroidx/preference/CheckBoxPreference;)V

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionPreference:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    invoke-static {v1}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v1

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->sendBroadcastSwitchStatus(Ljava/lang/Object;)Z

    :cond_1
    invoke-static {}, Lcom/android/provision/Utils;->isSupportGlobalInterconnectionEntrance()Z

    move-result v1

    if-eqz v1, :cond_2

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->InterconnectionLinkageLogic(Landroidx/preference/CheckBoxPreference;)V

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mInterconnectionGlobalItem:Lcom/android/provision/widget/CTACheckboxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    invoke-static {v1}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v1

    invoke-direct {p0, v1}, Lcom/android/provision/fragment/OtherSettingsFragment;->sendBroadcastSwitchStatus(Ljava/lang/Object;)Z

    :cond_2
    if-nez v0, :cond_5

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    const/4 v2, -0x1

    const/4 v3, 0x1

    if-eqz v1, :cond_3

    move v1, v3

    goto :goto_0

    :cond_3
    move v1, v2

    :goto_0
    const-string v4, "com_miui_warningcenter_pa_status"

    invoke-static {v0, v4, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAlarmPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    if-eqz v1, :cond_4

    move v2, v3

    :cond_4
    const-string v1, "com_miui_warningcenter_eps_status"

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_5
    invoke-static {}, Lcom/android/provision/Utils;->unSupportGetAppsModels()Z

    move-result v0

    if-nez v0, :cond_6

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "com.xiaomi.mipicks"

    invoke-static {v0, v1}, Lcom/android/provision/Utils;->judgeGetAppsEnable(Landroid/content/Context;Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_6

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mGetAppsPreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    const-string v2, "auto_update_app_via_wifi"

    invoke-static {v0, v2, v1}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_6
    iget-boolean v0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mIsINBuild:Z

    if-nez v0, :cond_7

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object v1, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAutoUpdatePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {v1}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result v1

    const-string v2, "auto_update"

    invoke-static {v0, v2, v1}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getActivity()Landroidx/fragment/app/FragmentActivity;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    iget-object p0, p0, Lcom/android/provision/fragment/OtherSettingsFragment;->mAutoUpdatePreference:Landroidx/preference/CheckBoxPreference;

    invoke-virtual {p0}, Landroidx/preference/TwoStatePreference;->isChecked()Z

    move-result p0

    const-string v1, "auto_download"

    invoke-static {v0, v1, p0}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_7
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
