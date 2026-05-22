TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/statemachine/DisplayFrameSetting.smali'
CLASS_FALLBACK_NAMES = ['DisplayFrameSetting.smali']
CLASS_ANCHORS = ['.super Landroid/os/Handler;', '.field private static final CLOUD_AUTOMODE_VRR_GROUP:Ljava/lang/String; = "automode_vrr_group"', '.field private static final CLOUD_CAMERA_IDLE_GROUP:Ljava/lang/String; = "camera_idle_group"', '.field private static final CLOUD_DISPLAY_FPS_GROUP:Ljava/lang/String; = "display_fps_group"', '.field private static final CLOUD_EBOOK_IDLE_GROUP:Ljava/lang/String; = "ebook_idle_pkg"', '.field private static final CLOUD_EYE_MODE_GROUP:Ljava/lang/String; = "eye_protection_mode"']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_statemachine_DisplayFrameSetting__setScreenEffect',
        'method': '.method private setScreenEffect(Ljava/lang/String;II)V',
        'method_name': 'setScreenEffect',
        'method_anchors': ['iget v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mIsUltimate:I', 'const-string v5, "miui_refresh_rate"', 'if-ne v4, v8, :cond_1', 'if-eq v3, v6, :cond_1', 'if-eq v3, v7, :cond_1', 'const-string v4, "com.android.camera"', 'invoke-virtual {v1, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z', 'if-nez v4, :cond_1'],
        'type': 'insert_after_registers',
        'search': None,
        'replacement': """
    const-string v0, "lock_max_fps_mezo"

    const/4 v1, 0x1

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-eqz v0, :cond_mezo_fps_guard

    return-void

    :cond_mezo_fps_guard""",
        'required': True,
        'flag_rewrite_count': 0,
        'reason': 'FPS guard inserted after .registers — does not replace the method, avoids missing .end method.',
    },
    {
        'id': 'com_miui_powerkeeper_statemachine_DisplayFrameSetting__isSupportDevice',
        'method': '.method public isSupportDevice()Z',
        'method_name': 'isSupportDevice',
        'method_anchors': ['iget-object p0, p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCustomFpsDeviceArray:[Ljava/lang/String;', 'if-ge v2, v0, :cond_2', 'invoke-static {v3}, Lcom/miui/powerkeeper/utils/Utils;->isBelongToDeviceSeries(Ljava/lang/String;)Z', 'if-eqz v4, :cond_0', 'return p0', 'const-string v4, "_intl"', 'invoke-virtual {v3, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z', 'if-eqz v4, :cond_1'],
        'type': 'method_replace',
        'search': """.method public isSupportDevice()Z
    .registers 6

    iget-object p0, p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCustomFpsDeviceArray:[Ljava/lang/String;

    array-length v0, p0

    const/4 v1, 0x0

    move v2, v1

    :goto_0
    if-ge v2, v0, :cond_2

    aget-object v3, p0, v2

    invoke-static {v3}, Lcom/miui/powerkeeper/utils/Utils;->isBelongToDeviceSeries(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const-string v4, "_intl"

    invoke-virtual {v3, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_1

    sget-boolean v4, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v4, :cond_1

    invoke-virtual {v3}, Ljava/lang/String;->length()I

    move-result p0

    add-int/lit8 p0, p0, -0x5

    invoke-virtual {v3, v1, p0}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Lcom/miui/powerkeeper/utils/Utils;->isBelongToDeviceSeries(Ljava/lang/String;)Z

    move-result p0

    return p0

    :cond_1
    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_2
    return v1
.end method""",
        'replacement': """.method public isSupportDevice()Z
    .registers 6

    iget-object p0, p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCustomFpsDeviceArray:[Ljava/lang/String;

    array-length v0, p0

    const/4 v1, 0x0

    move v2, v1

    :goto_0
    if-ge v2, v0, :cond_2

    aget-object v3, p0, v2

    invoke-static {v3}, Lcom/miui/powerkeeper/utils/Utils;->isBelongToDeviceSeries(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const-string v4, "_intl"

    invoke-virtual {v3, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_1

    sget-boolean v4, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v4, :cond_1

    invoke-virtual {v3}, Ljava/lang/String;->length()I

    move-result p0

    add-int/lit8 p0, p0, -0x5

    invoke-virtual {v3, v1, p0}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Lcom/miui/powerkeeper/utils/Utils;->isBelongToDeviceSeries(Ljava/lang/String;)Z

    move-result p0

    return p0

    :cond_1
    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_2
    return v1
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
    {
        'id': 'com_miui_powerkeeper_statemachine_DisplayFrameSetting__getValidLocalConfigPath',
        'method': '.method public static getValidLocalConfigPath(Landroid/content/Context;)Ljava/lang/String;',
        'method_name': 'getValidLocalConfigPath',
        'method_anchors': ['sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;', 'const-string v1, "fps_local.config"', 'invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z', 'if-eqz v2, :cond_0', 'sget-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;', 'const-string v4, "_intl"', 'invoke-virtual {v2, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z', 'if-eqz v2, :cond_3'],
        'type': 'method_replace',
        'search': """.method public static getValidLocalConfigPath(Landroid/content/Context;)Ljava/lang/String;
    .registers 9

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v1, "fps_local.config"

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v2

    const/4 v3, 0x0

    if-eqz v2, :cond_0

    goto :goto_0

    :cond_0
    move-object v0, v3

    :goto_0
    sget-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v4, "_intl"

    invoke-virtual {v2, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_3

    const-string v2, "IN"

    const-string v5, "ro.miui.build.region"

    invoke-static {v5}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v2, v6}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_1

    const-string v2, "ID"

    invoke-static {v5}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v2, v5}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_3

    :cond_1
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "smartfps/"

    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-object v6, Landroid/os/Build;->DEVICE:Ljava/lang/String;

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v7, "_id"

    invoke-virtual {v2, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    sput-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v2, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v2

    const-string v7, "DisplayFrameSetting"

    if-eqz v2, :cond_2

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "switch intl local config to id local config "

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-object v4, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v7, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    :cond_2
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    sput-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v2, "without id local config, no need to switch intl local config"

    invoke-static {v7, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_3
    :goto_1
    if-nez v0, :cond_5

    sget-boolean v2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v2, :cond_7

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_4

    sget-object p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    return-object p0

    :cond_4
    return-object v3

    :cond_5
    sget-boolean v2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v2, :cond_7

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_6

    sget-object p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    return-object p0

    :cond_6
    const-string p0, "smartfps/opt_dafault_config"

    return-object p0

    :cond_7
    return-object v0
.end method""",
        'replacement': """.method public static getValidLocalConfigPath(Landroid/content/Context;)Ljava/lang/String;
    .registers 9

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v1, "fps_local.config"

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v2

    const/4 v3, 0x0

    if-eqz v2, :cond_0

    goto :goto_0

    :cond_0
    move-object v0, v3

    :goto_0
    sget-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v4, "_intl"

    invoke-virtual {v2, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_3

    const-string v2, "IN"

    const-string v5, "ro.miui.build.region"

    invoke-static {v5}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v2, v6}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_1

    const-string v2, "ID"

    invoke-static {v5}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v2, v5}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_3

    :cond_1
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "smartfps/"

    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-object v6, Landroid/os/Build;->DEVICE:Ljava/lang/String;

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v7, "_id"

    invoke-virtual {v2, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    sput-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v2, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v2

    const-string v7, "DisplayFrameSetting"

    if-eqz v2, :cond_2

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "switch intl local config to id local config "

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-object v4, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v7, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    :cond_2
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    sput-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v2, "without id local config, no need to switch intl local config"

    invoke-static {v7, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_3
    :goto_1
    if-nez v0, :cond_5

    sget-boolean v2, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v2, :cond_7

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_4

    sget-object p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    return-object p0

    :cond_4
    return-object v3

    :cond_5
    sget-boolean v2, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v2, :cond_7

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_6

    sget-object p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    return-object p0

    :cond_6
    const-string p0, "smartfps/opt_dafault_config"

    return-object p0

    :cond_7
    return-object v0
.end method""",
        'required': True,
        'flag_rewrite_count': 2,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
