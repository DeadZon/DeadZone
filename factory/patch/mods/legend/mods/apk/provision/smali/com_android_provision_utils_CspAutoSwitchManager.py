TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/utils/CspAutoSwitchManager.smali'
CLASS_FALLBACK_NAMES = ['CspAutoSwitchManager.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final GOOGLE_PACKAGES:[Ljava/lang/String;', '.field private static final GOOGLE_PACKAGE_CONTACTS:Ljava/lang/String; = "com.google.android.contacts"', '.field private static final GOOGLE_PACKAGE_DIALER:Ljava/lang/String; = "com.google.android.dialer"', '.field private static final GOOGLE_PACKAGE_EUICC:Ljava/lang/String; = "com.google.android.euicc"', '.field private static final MIUI_PACKAGES:[Ljava/lang/String;']

PATCHES = [
    {
        'id': 'com_android_provision_utils_CspAutoSwitchManager__checkTailLandRing',
        'method': '.method public static checkTailLandRing(Landroid/content/Context;)V',
        'method_name': 'checkTailLandRing',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'const-string v1, "CspAutoSwitchManager"', 'if-eqz v0, :cond_6', 'invoke-static {}, Lmiui/telephony/TelephonyManagerEx;->getDefault()Lmiui/telephony/TelephonyManagerEx;', 'invoke-virtual {v0}, Lmiui/telephony/TelephonyManagerEx;->isSupportGlobalCrbt()Z', 'if-nez v0, :cond_0', 'invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isRegionSupportRingtoneLocale()Z', 'new-instance v2, Ljava/lang/StringBuilder;'],
        'type': 'policy_skip',
        'search': """.method public static checkTailLandRing(Landroid/content/Context;)V
    .registers 7

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const-string v1, "CspAutoSwitchManager"

    if-eqz v0, :cond_6

    invoke-static {}, Lmiui/telephony/TelephonyManagerEx;->getDefault()Lmiui/telephony/TelephonyManagerEx;

    move-result-object v0

    invoke-virtual {v0}, Lmiui/telephony/TelephonyManagerEx;->isSupportGlobalCrbt()Z

    move-result v0

    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    :try_start_0
    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isRegionSupportRingtoneLocale()Z

    move-result v0

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "checkSupportRingLocal:"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-eqz v0, :cond_1

    sget-object v2, Lcom/android/provision/utils/CspAutoSwitchManager;->GOOGLE_PACKAGES:[Ljava/lang/String;

    goto :goto_0

    :catch_0
    move-exception p0

    goto :goto_3

    :cond_1
    sget-object v2, Lcom/android/provision/utils/CspAutoSwitchManager;->MIUI_PACKAGES:[Ljava/lang/String;

    :goto_0
    if-eqz v0, :cond_2

    const-string v0, "com.google.android.dialer"

    goto :goto_1

    :cond_2
    const-string v0, "com.android.contacts"

    :goto_1
    sget-object v3, Lcom/android/provision/utils/CspAutoSwitchManager;->GOOGLE_PACKAGES:[Ljava/lang/String;

    invoke-static {p0, v3}, Lcom/android/provision/utils/CspAutoSwitchManager;->isAppsAllInstalled(Landroid/content/Context;[Ljava/lang/String;)Z

    move-result v3

    if-eqz v3, :cond_5

    sget-object v3, Lcom/android/provision/utils/CspAutoSwitchManager;->MIUI_PACKAGES:[Ljava/lang/String;

    invoke-static {p0, v3}, Lcom/android/provision/utils/CspAutoSwitchManager;->isAppsAllInstalled(Landroid/content/Context;[Ljava/lang/String;)Z

    move-result v3

    if-nez v3, :cond_3

    goto :goto_4

    :cond_3
    array-length v3, v2

    const/4 v4, 0x0

    :goto_2
    if-ge v4, v3, :cond_4

    aget-object v5, v2, v4

    invoke-static {p0, v5}, Lcom/android/provision/utils/CspAutoSwitchManager;->deleteSystemApp(Landroid/content/Context;Ljava/lang/String;)V

    add-int/lit8 v4, v4, 0x1

    goto :goto_2

    :cond_4
    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p0

    const-string v2, "delete_system_dialer_package"

    invoke-static {p0, v2, v0}, Landroid/provider/MiuiSettings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :goto_3
    const-string v0, "checkTailLandRing error"

    invoke-static {v1, v0, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_5
    :goto_4
    return-void

    :cond_6
    :goto_5
    const-string p0, "conditions not met"

    invoke-static {v1, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method""",
        'replacement': """.method public static checkTailLandRing(Landroid/content/Context;)V
    .registers 7

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const-string v1, "CspAutoSwitchManager"

    if-eqz v0, :cond_6

    invoke-static {}, Lmiui/telephony/TelephonyManagerEx;->getDefault()Lmiui/telephony/TelephonyManagerEx;

    move-result-object v0

    invoke-virtual {v0}, Lmiui/telephony/TelephonyManagerEx;->isSupportGlobalCrbt()Z

    move-result v0

    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    :try_start_0
    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isRegionSupportRingtoneLocale()Z

    move-result v0

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "checkSupportRingLocal:"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v1, v2}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-eqz v0, :cond_1

    sget-object v2, Lcom/android/provision/utils/CspAutoSwitchManager;->GOOGLE_PACKAGES:[Ljava/lang/String;

    goto :goto_0

    :catch_0
    move-exception p0

    goto :goto_3

    :cond_1
    sget-object v2, Lcom/android/provision/utils/CspAutoSwitchManager;->MIUI_PACKAGES:[Ljava/lang/String;

    :goto_0
    if-eqz v0, :cond_2

    const-string v0, "com.google.android.dialer"

    goto :goto_1

    :cond_2
    const-string v0, "com.android.contacts"

    :goto_1
    sget-object v3, Lcom/android/provision/utils/CspAutoSwitchManager;->GOOGLE_PACKAGES:[Ljava/lang/String;

    invoke-static {p0, v3}, Lcom/android/provision/utils/CspAutoSwitchManager;->isAppsAllInstalled(Landroid/content/Context;[Ljava/lang/String;)Z

    move-result v3

    if-eqz v3, :cond_5

    sget-object v3, Lcom/android/provision/utils/CspAutoSwitchManager;->MIUI_PACKAGES:[Ljava/lang/String;

    invoke-static {p0, v3}, Lcom/android/provision/utils/CspAutoSwitchManager;->isAppsAllInstalled(Landroid/content/Context;[Ljava/lang/String;)Z

    move-result v3

    if-nez v3, :cond_3

    goto :goto_4

    :cond_3
    array-length v3, v2

    const/4 v4, 0x0

    :goto_2
    if-ge v4, v3, :cond_4

    aget-object v5, v2, v4

    invoke-static {p0, v5}, Lcom/android/provision/utils/CspAutoSwitchManager;->deleteSystemApp(Landroid/content/Context;Ljava/lang/String;)V

    add-int/lit8 v4, v4, 0x1

    goto :goto_2

    :cond_4
    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p0

    const-string v2, "delete_system_dialer_package"

    invoke-static {p0, v2, v0}, Landroid/provider/MiuiSettings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :goto_3
    const-string v0, "checkTailLandRing error"

    invoke-static {v1, v0, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_5
    :goto_4
    return-void

    :cond_6
    :goto_5
    const-string p0, "conditions not met"

    invoke-static {v1, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
