TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/Utils.smali'
CLASS_FALLBACK_NAMES = ['Utils.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final ACTION_GESTUE:Ljava/lang/String; = "com.android.systemui.fsgesture"', '.field private static final ALL_BUCKETS:I = 0x3e8', '.field public static final AUTHORITY_FOR_LAUNCHER:Ljava/lang/String;', '.field private static final AUTHORITY_THEME_PROVIDER:Ljava/lang/String; = "com.android.thememanager.theme_provider"', '.field private static final BRAND_POCO:Ljava/lang/String; = "poco"']

PATCHES = [
    {
        'id': 'com_android_provision_Utils__alarmAssistanceLimitedRange',
        'method': '.method public static alarmAssistanceLimitedRange()Z',
        'method_name': 'alarmAssistanceLimitedRange',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_1', 'sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z', 'if-eqz v0, :cond_0', 'return v0', 'return v0'],
        'type': 'policy_skip',
        'search': """.method public static alarmAssistanceLimitedRange()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_1

    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    return v0

    :cond_1
    :goto_0
    const/4 v0, 0x1

    return v0
.end method""",
        'replacement': """.method public static alarmAssistanceLimitedRange()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_1

    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    return v0

    :cond_1
    :goto_0
    const/4 v0, 0x1

    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__checkAndActivateEsimAfterFactoryReset',
        'method': '.method public static checkAndActivateEsimAfterFactoryReset(Landroid/content/Context;)V',
        'method_name': 'checkAndActivateEsimAfterFactoryReset',
        'method_anchors': ['if-nez p0, :cond_0', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_1', 'invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimRegardlessRegion()Z', 'if-nez v0, :cond_2', 'invoke-static {}, Lcom/android/provision/Utils;->isSupportGoogleEsimModeRegardlessRegion()Z', 'if-nez v0, :cond_2', 'invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isActivateEsimCardSelect()Z'],
        'type': 'policy_skip',
        'search': """.method public static checkAndActivateEsimAfterFactoryReset(Landroid/content/Context;)V
    .registers 3

    if-nez p0, :cond_0

    goto :goto_0

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_1

    goto :goto_0

    :cond_1
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimRegardlessRegion()Z

    move-result v0

    if-nez v0, :cond_2

    invoke-static {}, Lcom/android/provision/Utils;->isSupportGoogleEsimModeRegardlessRegion()Z

    move-result v0

    if-nez v0, :cond_2

    goto :goto_0

    :cond_2
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isActivateEsimCardSelect()Z

    move-result v0

    if-eqz v0, :cond_3

    goto :goto_0

    :cond_3
    const-string v0, "esim_import_properties"

    invoke-static {}, Lcom/android/provision/Utils;->readEsimPowerRecordFilePersist()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_4

    :goto_0
    return-void

    :cond_4
    const-string v0, "Provision_Utils"

    const-string v1, "checkAndActivateEsimAfterFactoryReset"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    new-instance v0, Lcom/android/provision/utils/ResetSimCountHelper;

    invoke-direct {v0}, Lcom/android/provision/utils/ResetSimCountHelper;-><init>()V

    invoke-virtual {v0, p0}, Lcom/android/provision/utils/ResetSimCountHelper;->isSuccessPhoneInit(Landroid/content/Context;)V

    return-void
.end method""",
        'replacement': """.method public static checkAndActivateEsimAfterFactoryReset(Landroid/content/Context;)V
    .registers 3

    if-nez p0, :cond_0

    goto :goto_0

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_1

    goto :goto_0

    :cond_1
    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimRegardlessRegion()Z

    move-result v0

    if-nez v0, :cond_2

    invoke-static {}, Lcom/android/provision/Utils;->isSupportGoogleEsimModeRegardlessRegion()Z

    move-result v0

    if-nez v0, :cond_2

    goto :goto_0

    :cond_2
    invoke-static {}, Lcom/android/provision/DefaultPreferenceHelper;->isActivateEsimCardSelect()Z

    move-result v0

    if-eqz v0, :cond_3

    goto :goto_0

    :cond_3
    const-string v0, "esim_import_properties"

    invoke-static {}, Lcom/android/provision/Utils;->readEsimPowerRecordFilePersist()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_4

    :goto_0
    return-void

    :cond_4
    const-string v0, "Provision_Utils"

    const-string v1, "checkAndActivateEsimAfterFactoryReset"

    invoke-static {v0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    new-instance v0, Lcom/android/provision/utils/ResetSimCountHelper;

    invoke-direct {v0}, Lcom/android/provision/utils/ResetSimCountHelper;-><init>()V

    invoke-virtual {v0, p0}, Lcom/android/provision/utils/ResetSimCountHelper;->isSuccessPhoneInit(Landroid/content/Context;)V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__checkEsimConsistent',
        'method': '.method public static checkEsimConsistent()Z',
        'method_name': 'checkEsimConsistent',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z', 'if-nez v0, :cond_0', 'invoke-static {}, Lcom/android/provision/Utils;->isSupportGoogleEsimMode()Z', 'if-eqz v0, :cond_1', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_1', 'return v0', 'return v0'],
        'type': 'policy_skip',
        'search': """.method public static checkEsimConsistent()Z
    .registers 1

    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result v0

    if-nez v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isSupportGoogleEsimMode()Z

    move-result v0

    if-eqz v0, :cond_1

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    const/4 v0, 0x1

    return v0

    :cond_1
    const/4 v0, 0x0

    return v0
.end method""",
        'replacement': """.method public static checkEsimConsistent()Z
    .registers 1

    invoke-static {}, Lcom/android/provision/Utils;->isSupportEsimMode()Z

    move-result v0

    if-nez v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isSupportGoogleEsimMode()Z

    move-result v0

    if-eqz v0, :cond_1

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_1

    const/4 v0, 0x1

    return v0

    :cond_1
    const/4 v0, 0x0

    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__enableSOTIDeviceOwner',
        'method': '.method public static enableSOTIDeviceOwner(Landroid/content/Context;)V',
        'method_name': 'enableSOTIDeviceOwner',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'if-eqz p0, :cond_0', 'const-string v0, "net.soti.mobicontrol.androidwork"', 'invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z', 'if-eqz p0, :cond_0', 'new-instance p0, Ljava/lang/StringBuilder;', 'invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V'],
        'type': 'policy_skip',
        'search': """.method public static enableSOTIDeviceOwner(Landroid/content/Context;)V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    if-eqz p0, :cond_0

    const-string v0, "net.soti.mobicontrol.androidwork"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "/system/bin/dpm set-device-owner --user current "

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v0, "net.soti.mobicontrol.androidwork/net.soti.mobicontrol.admin.DeviceAdminAdapter"

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    :try_start_0
    invoke-static {}, Ljava/lang/Runtime;->getRuntime()Ljava/lang/Runtime;

    move-result-object v0

    invoke-virtual {v0, p0}, Ljava/lang/Runtime;->exec(Ljava/lang/String;)Ljava/lang/Process;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :catch_0
    move-exception p0

    const-string v0, "Provision_Utils"

    const-string v1, "run cmd failed"

    invoke-static {v0, v1, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_0
    return-void
.end method""",
        'replacement': """.method public static enableSOTIDeviceOwner(Landroid/content/Context;)V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    if-eqz p0, :cond_0

    const-string v0, "net.soti.mobicontrol.androidwork"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "/system/bin/dpm set-device-owner --user current "

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v0, "net.soti.mobicontrol.androidwork/net.soti.mobicontrol.admin.DeviceAdminAdapter"

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    :try_start_0
    invoke-static {}, Ljava/lang/Runtime;->getRuntime()Ljava/lang/Runtime;

    move-result-object v0

    invoke-virtual {v0, p0}, Ljava/lang/Runtime;->exec(Ljava/lang/String;)Ljava/lang/Process;
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return-void

    :catch_0
    move-exception p0

    const-string v0, "Provision_Utils"

    const-string v1, "run cmd failed"

    invoke-static {v0, v1, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_0
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__getHuanjiSettingsStatus',
        'method': '.method public static getHuanjiSettingsStatus(Landroid/content/Context;)Z',
        'method_name': 'getHuanjiSettingsStatus',
        'method_anchors': ['invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;', 'const-string v0, "huanji_settings"', 'invoke-static {p0, v0, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I', 'if-eqz p0, :cond_0', 'return p0', 'return v1'],
        'type': 'method_replace',
        'search': """.method public static getHuanjiSettingsStatus(Landroid/content/Context;)Z
    .registers 3

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p0

    const-string v0, "huanji_settings"

    const/4 v1, 0x0

    invoke-static {p0, v0, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    return v1
.end method""",
        'replacement': """.method public static getHuanjiSettingsStatus(Landroid/content/Context;)Z
    .registers 3

    const/4 v0, 0x0

    if-nez p0, :cond_0

    return v0

    :cond_0
    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p0

    const-string v0, "huanji_settings"

    const/4 v1, 0x0

    invoke-static {p0, v0, v1}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result p0

    if-eqz p0, :cond_1

    const/4 p0, 0x1

    return p0

    :cond_1
    return v1
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_Utils__isGlobalBuild',
        'method': '.method public static isGlobalBuild()Z',
        'method_name': 'isGlobalBuild',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return v0'],
        'type': 'policy_skip',
        'search': """.method public static isGlobalBuild()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return v0
.end method""",
        'replacement': """.method public static isGlobalBuild()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isNewGlobalOOBE',
        'method': '.method public static isNewGlobalOOBE()Z',
        'method_name': 'isNewGlobalOOBE',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'return v0', 'return v0'],
        'type': 'policy_skip',
        'search': """.method public static isNewGlobalOOBE()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    const/4 v0, 0x0

    return v0
.end method""",
        'replacement': """.method public static isNewGlobalOOBE()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    const/4 v0, 0x0

    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isShowMiShareItem',
        'method': '.method public static isShowMiShareItem(Landroid/content/Context;)Z',
        'method_name': 'isShowMiShareItem',
        'method_anchors': ['if-nez p0, :cond_0', 'const-string p0, "Provision_Utils"', 'const-string v1, "isShowMiShareItem: context is null"', 'invoke-static {p0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I', 'return v0', 'sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v1, :cond_1', 'return v0'],
        'type': 'policy_skip',
        'search': """.method public static isShowMiShareItem(Landroid/content/Context;)Z
    .registers 3

    const/4 v0, 0x0

    if-nez p0, :cond_0

    const-string p0, "Provision_Utils"

    const-string v1, "isShowMiShareItem: context is null"

    invoke-static {p0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return v0

    :cond_0
    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v1, :cond_1

    return v0

    :cond_1
    const-string v0, "com.miui.mishare.connectivity"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method public static isShowMiShareItem(Landroid/content/Context;)Z
    .registers 3

    const/4 v0, 0x0

    if-nez p0, :cond_0

    const-string p0, "Provision_Utils"

    const-string v1, "isShowMiShareItem: context is null"

    invoke-static {p0, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return v0

    :cond_0
    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v1, :cond_1

    return v0

    :cond_1
    const-string v0, "com.miui.mishare.connectivity"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportAIAssistant',
        'method': '.method public static isSupportAIAssistant(Landroid/content/Context;)Z',
        'method_name': 'isSupportAIAssistant',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportAIAssistant(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'replacement': """.method public static isSupportAIAssistant(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportAppVault',
        'method': '.method public static isSupportAppVault(Landroid/content/Context;)Z',
        'method_name': 'isSupportAppVault',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportAppVault(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'replacement': """.method public static isSupportAppVault(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportCloudBackup',
        'method': '.method public static isSupportCloudBackup(Landroid/content/Context;)Z',
        'method_name': 'isSupportCloudBackup',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'const-string v0, "com.miui.cloudbackup"', 'invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportCloudBackup(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.miui.cloudbackup"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method public static isSupportCloudBackup(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.miui.cloudbackup"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportCommService',
        'method': '.method public static isSupportCommService(Landroid/content/Context;)Z',
        'method_name': 'isSupportCommService',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportCommService(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'replacement': """.method public static isSupportCommService(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportEsimMode',
        'method': '.method public static isSupportEsimMode()Z',
        'method_name': 'isSupportEsimMode',
        'method_anchors': ['const-string v0, "ro.vendor.miui.support_esim"', 'invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z', 'if-eqz v0, :cond_0', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'invoke-static {}, Lcom/android/provision/Utils;->getLocaleISO()Ljava/lang/String;', 'invoke-static {v0}, Lcom/android/provision/Utils;->judgeSupportEsimForCountry(Ljava/lang/String;)Z', 'if-eqz v0, :cond_0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportEsimMode()Z
    .registers 2

    const-string v0, "ro.vendor.miui.support_esim"

    const/4 v1, 0x0

    invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->getLocaleISO()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->judgeSupportEsimForCountry(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    return v1
.end method""",
        'replacement': """.method public static isSupportEsimMode()Z
    .registers 2

    const-string v0, "ro.vendor.miui.support_esim"

    const/4 v1, 0x0

    invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->getLocaleISO()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->judgeSupportEsimForCountry(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    return v1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportEsimRegardlessRegion',
        'method': '.method public static isSupportEsimRegardlessRegion()Z',
        'method_name': 'isSupportEsimRegardlessRegion',
        'method_anchors': ['const-string v0, "ro.vendor.miui.support_esim"', 'invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z', 'if-eqz v0, :cond_0', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'return v0', 'return v1'],
        'type': 'policy_skip',
        'search': """.method public static isSupportEsimRegardlessRegion()Z
    .registers 2

    const-string v0, "ro.vendor.miui.support_esim"

    const/4 v1, 0x0

    invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    return v1
.end method""",
        'replacement': """.method public static isSupportEsimRegardlessRegion()Z
    .registers 2

    const-string v0, "ro.vendor.miui.support_esim"

    const/4 v1, 0x0

    invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    return v1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportGameCenterService',
        'method': '.method public static isSupportGameCenterService(Landroid/content/Context;)Z',
        'method_name': 'isSupportGameCenterService',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportGameCenterService(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'replacement': """.method public static isSupportGameCenterService(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportGlobalInterconnectionEntrance',
        'method': '.method public static isSupportGlobalInterconnectionEntrance()Z',
        'method_name': 'isSupportGlobalInterconnectionEntrance',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;', 'invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z', 'if-eqz v0, :cond_0', 'return v0', 'return v0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportGlobalInterconnectionEntrance()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    const/4 v0, 0x0

    return v0
.end method""",
        'replacement': """.method public static isSupportGlobalInterconnectionEntrance()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->supportInterconnectivity()Ljava/lang/Boolean;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    const/4 v0, 0x0

    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportHTMLViewer',
        'method': '.method public static isSupportHTMLViewer(Landroid/content/Context;)Z',
        'method_name': 'isSupportHTMLViewer',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'const-string v0, "com.android.htmlviewer"', 'invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportHTMLViewer(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.android.htmlviewer"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method public static isSupportHTMLViewer(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.android.htmlviewer"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportInfoAssistant',
        'method': '.method public static isSupportInfoAssistant(Landroid/content/Context;)Z',
        'method_name': 'isSupportInfoAssistant',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportInfoAssistant(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'replacement': """.method public static isSupportInfoAssistant(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportIntentFilterVerificationService',
        'method': '.method public static isSupportIntentFilterVerificationService()Z',
        'method_name': 'isSupportIntentFilterVerificationService',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return v0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportIntentFilterVerificationService()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 v0, v0, 0x1

    return v0
.end method""",
        'replacement': """.method public static isSupportIntentFilterVerificationService()Z
    .registers 1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 v0, v0, 0x1

    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportJoyose',
        'method': '.method public static isSupportJoyose(Landroid/content/Context;)Z',
        'method_name': 'isSupportJoyose',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'const-string v0, "com.xiaomi.joyose"', 'invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportJoyose(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.xiaomi.joyose"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method public static isSupportJoyose(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.xiaomi.joyose"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportMAB',
        'method': '.method public static isSupportMAB(Landroid/content/Context;)Z',
        'method_name': 'isSupportMAB',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportMAB(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'replacement': """.method public static isSupportMAB(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportMSA',
        'method': '.method public static isSupportMSA(Landroid/content/Context;)Z',
        'method_name': 'isSupportMSA',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportMSA(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'replacement': """.method public static isSupportMSA(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportMiAccount',
        'method': '.method public static isSupportMiAccount(Landroid/content/Context;)Z',
        'method_name': 'isSupportMiAccount',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportMiAccount(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'replacement': """.method public static isSupportMiAccount(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportOs',
        'method': '.method public static isSupportOs(Landroid/content/Context;)Z',
        'method_name': 'isSupportOs',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportOs(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'replacement': """.method public static isSupportOs(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportPowerKeeper',
        'method': '.method public static isSupportPowerKeeper(Landroid/content/Context;)Z',
        'method_name': 'isSupportPowerKeeper',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'const-string v0, "com.miui.powerkeeper"', 'invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportPowerKeeper(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.miui.powerkeeper"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method public static isSupportPowerKeeper(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.miui.powerkeeper"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportPowerchecker',
        'method': '.method public static isSupportPowerchecker(Landroid/content/Context;)Z',
        'method_name': 'isSupportPowerchecker',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'const-string v0, "com.xiaomi.powerchecker"', 'invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportPowerchecker(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.xiaomi.powerchecker"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method public static isSupportPowerchecker(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.xiaomi.powerchecker"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportQuickApp',
        'method': '.method public static isSupportQuickApp(Landroid/content/Context;)Z',
        'method_name': 'isSupportQuickApp',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportQuickApp(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'replacement': """.method public static isSupportQuickApp(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportRMS',
        'method': '.method public static isSupportRMS(Landroid/content/Context;)Z',
        'method_name': 'isSupportRMS',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportRMS(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'replacement': """.method public static isSupportRMS(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportSecureElementApplication',
        'method': '.method public static isSupportSecureElementApplication(Landroid/content/Context;)Z',
        'method_name': 'isSupportSecureElementApplication',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'const-string v0, "com.android.se"', 'invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportSecureElementApplication(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.android.se"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method public static isSupportSecureElementApplication(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.android.se"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportSmartService',
        'method': '.method public static isSupportSmartService(Landroid/content/Context;)Z',
        'method_name': 'isSupportSmartService',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportSmartService(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'replacement': """.method public static isSupportSmartService(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportStatistics',
        'method': '.method public static isSupportStatistics(Landroid/content/Context;)Z',
        'method_name': 'isSupportStatistics',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportStatistics(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'replacement': """.method public static isSupportStatistics(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportSystemHelper',
        'method': '.method public static isSupportSystemHelper(Landroid/content/Context;)Z',
        'method_name': 'isSupportSystemHelper',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportSystemHelper(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'replacement': """.method public static isSupportSystemHelper(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportWallpaper',
        'method': '.method public static isSupportWallpaper(Landroid/content/Context;)Z',
        'method_name': 'isSupportWallpaper',
        'method_anchors': ['sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportWallpaper(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'replacement': """.method public static isSupportWallpaper(Landroid/content/Context;)Z
    .registers 1

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 p0, p0, 0x1

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__isSupportXmsf',
        'method': '.method public static isSupportXmsf(Landroid/content/Context;)Z',
        'method_name': 'isSupportXmsf',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'const-string v0, "com.xiaomi.xmsf"', 'invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'policy_skip',
        'search': """.method public static isSupportXmsf(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const-string v0, "com.xiaomi.xmsf"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method public static isSupportXmsf(Landroid/content/Context;)Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    const-string v0, "com.xiaomi.xmsf"

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__setGmsAppEnabledStateForCn',
        'method': '.method public static setGmsAppEnabledStateForCn(Landroid/content/Context;I)V',
        'method_name': 'setGmsAppEnabledStateForCn',
        'method_anchors': ['if-eqz p0, :cond_3', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_3', 'invoke-static {p0}, Lcom/android/provision/Utils;->isProvisioned(Landroid/content/Context;)Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;', 'invoke-virtual {v0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;', 'new-instance v1, Ljava/util/ArrayList;'],
        'type': 'method_replace',
        'search': """.method public static setGmsAppEnabledStateForCn(Landroid/content/Context;I)V
    .registers 10

    if-eqz p0, :cond_3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_3

    invoke-static {p0}, Lcom/android/provision/Utils;->isProvisioned(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    invoke-virtual {p0}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v0

    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    sget-object v2, Lcom/android/provision/Utils;->GMS_APPS:Ljava/util/ArrayList;

    invoke-virtual {v2}, Ljava/util/ArrayList;->size()I

    move-result v3

    const/4 v4, 0x0

    move v5, v4

    :cond_1
    :goto_0
    if-ge v5, v3, :cond_2

    invoke-virtual {v2, v5}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v6

    add-int/lit8 v5, v5, 0x1

    check-cast v6, Ljava/lang/String;

    invoke-static {p0, v6}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result v7

    if-eqz v7, :cond_1

    invoke-virtual {v0, v6}, Landroid/content/pm/PackageManager;->getApplicationEnabledSetting(Ljava/lang/String;)I

    move-result v7

    if-ne v7, p1, :cond_1

    invoke-virtual {v1, v6}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_0

    :cond_2
    new-instance p0, Lcom/android/provision/Utils$2;

    invoke-direct {p0, v1, v0, p1}, Lcom/android/provision/Utils$2;-><init>(Ljava/util/ArrayList;Landroid/content/pm/PackageManager;I)V

    new-array p1, v4, [Ljava/lang/Void;

    invoke-virtual {p0, p1}, Landroid/os/AsyncTask;->execute([Ljava/lang/Object;)Landroid/os/AsyncTask;

    :cond_3
    :goto_1
    return-void
.end method""",
        'replacement': """.method public static setGmsAppEnabledStateForCn(Landroid/content/Context;I)V
    .registers 10

    if-eqz p0, :cond_3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_3

    invoke-static {p0}, Lcom/android/provision/Utils;->isProvisioned(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    invoke-virtual {p0}, Landroid/content/Context;->getApplicationContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v0

    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1}, Ljava/util/ArrayList;-><init>()V

    sget-object v2, Lcom/android/provision/Utils;->GMS_APPS:Ljava/util/ArrayList;

    invoke-virtual {v2}, Ljava/util/ArrayList;->size()I

    move-result v3

    const/4 v4, 0x0

    move v5, v4

    :cond_1
    :goto_0
    if-ge v5, v3, :cond_2

    invoke-virtual {v2, v5}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v6

    add-int/lit8 v5, v5, 0x1

    check-cast v6, Ljava/lang/String;

    invoke-static {p0, v6}, Lcom/android/provision/Utils;->applicationInstalled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result v7

    if-eqz v7, :cond_1

    invoke-virtual {v0, v6}, Landroid/content/pm/PackageManager;->getApplicationEnabledSetting(Ljava/lang/String;)I

    move-result v7

    if-eq v7, p1, :cond_1

    invoke-virtual {v1, v6}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_0

    :cond_2
    new-instance p0, Lcom/android/provision/Utils$2;

    invoke-direct {p0, v1, v0, p1}, Lcom/android/provision/Utils$2;-><init>(Ljava/util/ArrayList;Landroid/content/pm/PackageManager;I)V

    new-array p1, v4, [Ljava/lang/Void;

    invoke-virtual {p0, p1}, Landroid/os/AsyncTask;->execute([Ljava/lang/Object;)Landroid/os/AsyncTask;

    :cond_3
    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': 'BUILD_FLAG_PARTIALLY_SKIPPED',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_Utils__shouldForceSetDrawerHome',
        'method': '.method public static shouldForceSetDrawerHome()Z',
        'method_name': 'shouldForceSetDrawerHome',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'invoke-static {}, Lcom/android/provision/Utils;->hasPocoLauncherDefault()Z', 'if-nez v0, :cond_0', 'invoke-static {}, Lcom/android/provision/Utils;->isMiuiVersionLite()Z', 'if-eqz v0, :cond_0', 'const-string v0, "POCO"', 'invoke-static {}, Lcom/android/provision/Utils;->getProductBrand()Ljava/lang/String;'],
        'type': 'policy_skip',
        'search': """.method public static shouldForceSetDrawerHome()Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->hasPocoLauncherDefault()Z

    move-result v0

    if-nez v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isMiuiVersionLite()Z

    move-result v0

    if-eqz v0, :cond_0

    const-string v0, "POCO"

    invoke-static {}, Lcom/android/provision/Utils;->getProductBrand()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    const/4 v0, 0x0

    return v0
.end method""",
        'replacement': """.method public static shouldForceSetDrawerHome()Z
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->hasPocoLauncherDefault()Z

    move-result v0

    if-nez v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->isMiuiVersionLite()Z

    move-result v0

    if-eqz v0, :cond_0

    const-string v0, "POCO"

    invoke-static {}, Lcom/android/provision/Utils;->getProductBrand()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    const/4 v0, 0x0

    return v0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__startBackViewService',
        'method': '.method public static startBackViewService(Landroid/content/Context;)V',
        'method_name': 'startBackViewService',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z', 'if-eqz v0, :cond_1', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'new-instance v0, Landroid/content/Intent;', 'const-string v1, "miui.intent.action.SHOW_BACKSERVICE"', 'invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V', 'const-string v1, "com.android.provision"'],
        'type': 'policy_skip',
        'search': """.method public static startBackViewService(Landroid/content/Context;)V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v0, :cond_1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    new-instance v0, Landroid/content/Intent;

    const-string v1, "miui.intent.action.SHOW_BACKSERVICE"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v1, "com.android.provision"

    invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {p0, v0}, Landroid/content/Context;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;

    :cond_1
    :goto_0
    return-void
.end method""",
        'replacement': """.method public static startBackViewService(Landroid/content/Context;)V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v0, :cond_1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    new-instance v0, Landroid/content/Intent;

    const-string v1, "miui.intent.action.SHOW_BACKSERVICE"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v1, "com.android.provision"

    invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {p0, v0}, Landroid/content/Context;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;

    :cond_1
    :goto_0
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__startCongratulationPage',
        'method': '.method public static startCongratulationPage(Landroid/app/Activity;Z)V',
        'method_name': 'startCongratulationPage',
        'method_anchors': ['const-string v1, "Provision_Utils"', 'sget-boolean v0, Lcom/android/provision/Utils;->isFirstStartCongratulationPage:Z', 'if-nez v0, :cond_0', 'if-nez p1, :cond_1', 'sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz p1, :cond_2', 'new-instance p1, Landroid/content/Intent;', 'const-string v0, "com.android.settings.provision_congratulation"'],
        'type': 'policy_skip',
        'search': """.method public static startCongratulationPage(Landroid/app/Activity;Z)V
    .registers 12

    const-string v1, "Provision_Utils"

    sget-boolean v0, Lcom/android/provision/Utils;->isFirstStartCongratulationPage:Z

    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    if-nez p1, :cond_1

    goto :goto_2

    :cond_1
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_2

    goto :goto_2

    :cond_2
    new-instance p1, Landroid/content/Intent;

    const-string v0, "com.android.settings.provision_congratulation"

    invoke-direct {p1, v0}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v0, "com.android.settings"

    invoke-virtual {p1, v0}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    move-result-object p1

    const/high16 v2, 0x10000000

    invoke-virtual {p1, v2}, Landroid/content/Intent;->setFlags(I)Landroid/content/Intent;

    move-result-object p1

    const/4 v2, 0x0

    :try_start_0
    invoke-static {}, Lcom/android/provision/utils/BoostHelper;->getInstance()Lcom/android/provision/utils/BoostHelper;

    move-result-object v3

    invoke-virtual {v3, p0, v0}, Lcom/android/provision/utils/BoostHelper;->boostOtherProcess(Landroid/content/Context;Ljava/lang/String;)V

    sget v5, Lcom/android/provision/R$anim;->slide_in_right:I

    sget v6, Lcom/android/provision/R$anim;->slide_out_left:I
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_1
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    const/4 v8, 0x0

    const/4 v9, 0x0

    const/4 v7, 0x0

    move-object v4, p0

    :try_start_1
    invoke-static/range {v4 .. v9}, Landroid/app/ActivityOptions;->makeCustomTaskAnimation(Landroid/content/Context;IILandroid/os/Handler;Landroid/app/ActivityOptions$OnAnimationStartedListener;Landroid/app/ActivityOptions$OnAnimationFinishedListener;)Landroid/app/ActivityOptions;

    move-result-object p0

    invoke-virtual {p0}, Landroid/app/ActivityOptions;->toBundle()Landroid/os/Bundle;

    move-result-object p0

    invoke-virtual {v4, p1, p0}, Landroid/app/Activity;->startActivity(Landroid/content/Intent;Landroid/os/Bundle;)V

    const-string p0, "startCongratulationPage success"

    invoke-static {v1, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_0
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    sput-boolean v2, Lcom/android/provision/Utils;->isFirstStartCongratulationPage:Z

    return-void

    :catchall_0
    move-exception v0

    move-object p0, v0

    goto :goto_3

    :catch_0
    move-exception v0

    :goto_0
    move-object p0, v0

    goto :goto_1

    :catch_1
    move-exception v0

    move-object v4, p0

    goto :goto_0

    :goto_1
    :try_start_2
    const-string v0, "startCongratulationPage fail"

    invoke-static {v1, v0, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    invoke-virtual {v4, p1}, Landroid/app/Activity;->startActivity(Landroid/content/Intent;)V
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    sput-boolean v2, Lcom/android/provision/Utils;->isFirstStartCongratulationPage:Z

    :goto_2
    return-void

    :goto_3
    sput-boolean v2, Lcom/android/provision/Utils;->isFirstStartCongratulationPage:Z

    throw p0
.end method""",
        'replacement': """.method public static startCongratulationPage(Landroid/app/Activity;Z)V
    .registers 12

    const-string v1, "Provision_Utils"

    sget-boolean v0, Lcom/android/provision/Utils;->isFirstStartCongratulationPage:Z

    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    if-nez p1, :cond_1

    goto :goto_2

    :cond_1
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_2

    goto :goto_2

    :cond_2
    new-instance p1, Landroid/content/Intent;

    const-string v0, "com.android.settings.provision_congratulation"

    invoke-direct {p1, v0}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v0, "com.android.settings"

    invoke-virtual {p1, v0}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    move-result-object p1

    const/high16 v2, 0x10000000

    invoke-virtual {p1, v2}, Landroid/content/Intent;->setFlags(I)Landroid/content/Intent;

    move-result-object p1

    const/4 v2, 0x0

    :try_start_0
    invoke-static {}, Lcom/android/provision/utils/BoostHelper;->getInstance()Lcom/android/provision/utils/BoostHelper;

    move-result-object v3

    invoke-virtual {v3, p0, v0}, Lcom/android/provision/utils/BoostHelper;->boostOtherProcess(Landroid/content/Context;Ljava/lang/String;)V

    sget v5, Lcom/android/provision/R$anim;->slide_in_right:I

    sget v6, Lcom/android/provision/R$anim;->slide_out_left:I
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_1
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    const/4 v8, 0x0

    const/4 v9, 0x0

    const/4 v7, 0x0

    move-object v4, p0

    :try_start_1
    invoke-static/range {v4 .. v9}, Landroid/app/ActivityOptions;->makeCustomTaskAnimation(Landroid/content/Context;IILandroid/os/Handler;Landroid/app/ActivityOptions$OnAnimationStartedListener;Landroid/app/ActivityOptions$OnAnimationFinishedListener;)Landroid/app/ActivityOptions;

    move-result-object p0

    invoke-virtual {p0}, Landroid/app/ActivityOptions;->toBundle()Landroid/os/Bundle;

    move-result-object p0

    invoke-virtual {v4, p1, p0}, Landroid/app/Activity;->startActivity(Landroid/content/Intent;Landroid/os/Bundle;)V

    const-string p0, "startCongratulationPage success"

    invoke-static {v1, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_0
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    sput-boolean v2, Lcom/android/provision/Utils;->isFirstStartCongratulationPage:Z

    return-void

    :catchall_0
    move-exception v0

    move-object p0, v0

    goto :goto_3

    :catch_0
    move-exception v0

    :goto_0
    move-object p0, v0

    goto :goto_1

    :catch_1
    move-exception v0

    move-object v4, p0

    goto :goto_0

    :goto_1
    :try_start_2
    const-string v0, "startCongratulationPage fail"

    invoke-static {v1, v0, p0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    invoke-virtual {v4, p1}, Landroid/app/Activity;->startActivity(Landroid/content/Intent;)V
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    sput-boolean v2, Lcom/android/provision/Utils;->isFirstStartCongratulationPage:Z

    :goto_2
    return-void

    :goto_3
    sput-boolean v2, Lcom/android/provision/Utils;->isFirstStartCongratulationPage:Z

    throw p0
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__stopBackViewService',
        'method': '.method public static stopBackViewService(Landroid/content/Context;)V',
        'method_name': 'stopBackViewService',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z', 'if-eqz v0, :cond_1', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'new-instance v0, Landroid/content/Intent;', 'const-string v1, "miui.intent.action.STOP_BACKSERVICE"', 'invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V', 'invoke-virtual {p0, v0}, Landroid/content/Context;->sendBroadcast(Landroid/content/Intent;)V'],
        'type': 'policy_skip',
        'search': """.method public static stopBackViewService(Landroid/content/Context;)V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v0, :cond_1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    new-instance v0, Landroid/content/Intent;

    const-string v1, "miui.intent.action.STOP_BACKSERVICE"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-virtual {p0, v0}, Landroid/content/Context;->sendBroadcast(Landroid/content/Intent;)V

    new-instance v0, Landroid/content/Intent;

    const-string v1, "miui.intent.action.SHOW_BACKSERVICE"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v1, "com.android.provision"

    invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {p0, v0}, Landroid/content/Context;->stopService(Landroid/content/Intent;)Z

    :cond_1
    :goto_0
    return-void
.end method""",
        'replacement': """.method public static stopBackViewService(Landroid/content/Context;)V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    if-eqz v0, :cond_1

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    new-instance v0, Landroid/content/Intent;

    const-string v1, "miui.intent.action.STOP_BACKSERVICE"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-virtual {p0, v0}, Landroid/content/Context;->sendBroadcast(Landroid/content/Intent;)V

    new-instance v0, Landroid/content/Intent;

    const-string v1, "miui.intent.action.SHOW_BACKSERVICE"

    invoke-direct {v0, v1}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string v1, "com.android.provision"

    invoke-virtual {v0, v1}, Landroid/content/Intent;->setPackage(Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {p0, v0}, Landroid/content/Context;->stopService(Landroid/content/Intent;)Z

    :cond_1
    :goto_0
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__supportDisplayApplicationPermission',
        'method': '.method public static supportDisplayApplicationPermission()Z',
        'method_name': 'supportDisplayApplicationPermission',
        'method_anchors': ['const-string v0, "support_provision_app_permission"', 'invoke-static {v0, v1}, Lmiui/util/FeatureParser;->getBoolean(Ljava/lang/String;Z)Z', 'if-eqz v0, :cond_0', 'sget-boolean v0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z', 'if-nez v0, :cond_0', 'invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;', 'invoke-virtual {v0}, Ljava/util/Locale;->getCountry()Ljava/lang/String;', 'const-string v2, "CN"'],
        'type': 'policy_skip',
        'search': """.method public static supportDisplayApplicationPermission()Z
    .registers 3

    const-string v0, "support_provision_app_permission"

    const/4 v1, 0x0

    invoke-static {v0, v1}, Lmiui/util/FeatureParser;->getBoolean(Ljava/lang/String;Z)Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    if-nez v0, :cond_0

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object v0

    invoke-virtual {v0}, Ljava/util/Locale;->getCountry()Ljava/lang/String;

    move-result-object v0

    const-string v2, "CN"

    invoke-virtual {v2, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object v0

    invoke-virtual {v0}, Ljava/util/Locale;->getLanguage()Ljava/lang/String;

    move-result-object v0

    const-string v2, "zh"

    invoke-virtual {v2, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_STABLE_VERSION:Z

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    return v1
.end method""",
        'replacement': """.method public static supportDisplayApplicationPermission()Z
    .registers 3

    const-string v0, "support_provision_app_permission"

    const/4 v1, 0x0

    invoke-static {v0, v1}, Lmiui/util/FeatureParser;->getBoolean(Ljava/lang/String;Z)Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_GLOBAL_BUILD:Z

    if-nez v0, :cond_0

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object v0

    invoke-virtual {v0}, Ljava/util/Locale;->getCountry()Ljava/lang/String;

    move-result-object v0

    const-string v2, "CN"

    invoke-virtual {v2, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object v0

    invoke-virtual {v0}, Ljava/util/Locale;->getLanguage()Ljava/lang/String;

    move-result-object v0

    const-string v2, "zh"

    invoke-virtual {v2, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_STABLE_VERSION:Z

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    return v1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_Utils__supportMiMover',
        'method': '.method public static supportMiMover(Landroid/content/Context;)Z',
        'method_name': 'supportMiMover',
        'method_anchors': ['invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;', 'const-string v1, "disallow_mimover"', 'invoke-interface {v0, v1}, Lmiui/enterprise/IRestrictionsHelper;->isRestriction(Ljava/lang/String;)Z', 'if-eqz v0, :cond_0', 'const-string p0, "Provision_Utils"', 'const-string v0, "Device is in enterprise mode, MiMover is restricted by enterprise!"', 'invoke-static {p0, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I', 'return v1'],
        'type': 'policy_skip',
        'search': """.method public static supportMiMover(Landroid/content/Context;)Z
    .registers 6

    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object v0

    const-string v1, "disallow_mimover"

    invoke-interface {v0, v1}, Lmiui/enterprise/IRestrictionsHelper;->isRestriction(Ljava/lang/String;)Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    const-string p0, "Provision_Utils"

    const-string v0, "Device is in enterprise mode, MiMover is restricted by enterprise!"

    invoke-static {p0, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return v1

    :cond_0
    if-nez p0, :cond_1

    return v1

    :cond_1
    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    new-instance v2, Landroid/content/ComponentName;

    const-string v3, "com.miui.huanji"

    const-string v4, "com.miui.huanji.provision.ui.ProvisionCTAActivity"

    invoke-direct {v2, v3, v4}, Landroid/content/ComponentName;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0, v2}, Landroid/content/Intent;->setComponent(Landroid/content/ComponentName;)Landroid/content/Intent;

    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object p0

    const/high16 v2, 0x20000

    invoke-virtual {p0, v0, v2}, Landroid/content/pm/PackageManager;->queryIntentActivities(Landroid/content/Intent;I)Ljava/util/List;

    move-result-object p0

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_2

    invoke-interface {p0}, Ljava/util/List;->isEmpty()Z

    move-result p0

    if-nez p0, :cond_2

    const/4 p0, 0x1

    return p0

    :cond_2
    return v1
.end method""",
        'replacement': """.method public static supportMiMover(Landroid/content/Context;)Z
    .registers 6

    invoke-static {}, Lmiui/enterprise/RestrictionsHelperStub;->getInstance()Lmiui/enterprise/IRestrictionsHelper;

    move-result-object v0

    const-string v1, "disallow_mimover"

    invoke-interface {v0, v1}, Lmiui/enterprise/IRestrictionsHelper;->isRestriction(Ljava/lang/String;)Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    const-string p0, "Provision_Utils"

    const-string v0, "Device is in enterprise mode, MiMover is restricted by enterprise!"

    invoke-static {p0, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    return v1

    :cond_0
    if-nez p0, :cond_1

    return v1

    :cond_1
    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    new-instance v2, Landroid/content/ComponentName;

    const-string v3, "com.miui.huanji"

    const-string v4, "com.miui.huanji.provision.ui.ProvisionCTAActivity"

    invoke-direct {v2, v3, v4}, Landroid/content/ComponentName;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0, v2}, Landroid/content/Intent;->setComponent(Landroid/content/ComponentName;)Landroid/content/Intent;

    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object p0

    const/high16 v2, 0x20000

    invoke-virtual {p0, v0, v2}, Landroid/content/pm/PackageManager;->queryIntentActivities(Landroid/content/Intent;I)Ljava/util/List;

    move-result-object p0

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_2

    invoke-interface {p0}, Ljava/util/List;->isEmpty()Z

    move-result p0

    if-nez p0, :cond_2

    const/4 p0, 0x1

    return p0

    :cond_2
    return v1
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
