TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/cloudcontrol/LocalUpdateUtils.smali'
CLASS_FALLBACK_NAMES = ['LocalUpdateUtils.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final APP_BG_DATA_DELAY_COUNT:Ljava/lang/String; = "set_delay_count"', '.field private static final APP_BG_DATA_DELAY_TIME:Ljava/lang/String; = "app_delay"', '.field private static final APP_BG_DATA_DISABLE_LONG_TIME:Ljava/lang/String; = "set_data_disable_long"', '.field private static final APP_BG_DATA_DISABLE_SHORT_TIME:Ljava/lang/String; = "set_data_disable_short"', '.field private static final APP_BG_DATA_MAX_INACTIVE_COUNT:Ljava/lang/String; = "set_inactive_count"']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_cloudcontrol_LocalUpdateUtils__getCloudServer',
        'method': '.method private static getCloudServer(Landroid/content/Context;)Ljava/lang/String;',
        'method_name': 'getCloudServer',
        'method_anchors': ['new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0, v1}, Ljava/lang/StringBuilder;-><init>(I)V', 'invoke-static {}, Lcom/miui/powerkeeper/cloudcontrol/LocalUpdateUtils;->useNewCloudControl()Z', 'if-eqz v1, :cond_0', 'const-string v1, "new"', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'const-string v1, "cloud_current_enviroment"', 'const-string v2, ""'],
        'type': 'method_replace',
        'search': """.method private static getCloudServer(Landroid/content/Context;)Ljava/lang/String;
    .registers 4

    new-instance v0, Ljava/lang/StringBuilder;

    const/16 v1, 0x20

    invoke-direct {v0, v1}, Ljava/lang/StringBuilder;-><init>(I)V

    invoke-static {}, Lcom/miui/powerkeeper/cloudcontrol/LocalUpdateUtils;->useNewCloudControl()Z

    move-result v1

    if-eqz v1, :cond_0

    const-string v1, "new"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_0
    const-string v1, "cloud_current_enviroment"

    const-string v2, ""

    invoke-static {p0, v1, v2}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/String;->isEmpty()Z

    move-result v1

    if-eqz v1, :cond_2

    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p0, :cond_1

    const-string p0, "International"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_1
    const-string p0, "China"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_2
    const-string v1, "https://jupiter.sys.miui.com/api/profile/getProfile.do?"

    invoke-virtual {v1, p0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_3

    const-string p0, " force China"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_3
    const-string v1, "https://preview-jupiter.sys.miui.com/api/profile/getProfile.do?"

    invoke-virtual {v1, p0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_4

    const-string p0, " force Staging"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_4
    const-string v1, "https://jupiter.intl.sys.miui.com/api/profile/getProfile.do?"

    invoke-virtual {v1, p0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p0

    if-eqz p0, :cond_5

    const-string p0, " force International"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_5
    :goto_0
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method private static getCloudServer(Landroid/content/Context;)Ljava/lang/String;
    .registers 4

    new-instance v0, Ljava/lang/StringBuilder;

    const/16 v1, 0x20

    invoke-direct {v0, v1}, Ljava/lang/StringBuilder;-><init>(I)V

    invoke-static {}, Lcom/miui/powerkeeper/cloudcontrol/LocalUpdateUtils;->useNewCloudControl()Z

    move-result v1

    if-eqz v1, :cond_0

    const-string v1, "new"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_0
    const-string v1, "cloud_current_enviroment"

    const-string v2, ""

    invoke-static {p0, v1, v2}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/String;->isEmpty()Z

    move-result v1

    if-eqz v1, :cond_2

    sget-boolean p0, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz p0, :cond_1

    const-string p0, "International"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_1
    const-string p0, "China"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_2
    const-string v1, "https://jupiter.sys.miui.com/api/profile/getProfile.do?"

    invoke-virtual {v1, p0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_3

    const-string p0, " force China"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_3
    const-string v1, "https://preview-jupiter.sys.miui.com/api/profile/getProfile.do?"

    invoke-virtual {v1, p0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_4

    const-string p0, " force Staging"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_4
    const-string v1, "https://jupiter.intl.sys.miui.com/api/profile/getProfile.do?"

    invoke-virtual {v1, p0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p0

    if-eqz p0, :cond_5

    const-string p0, " force International"

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_5
    :goto_0
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
    {
        'id': 'com_miui_powerkeeper_cloudcontrol_LocalUpdateUtils__setServerConfigurations',
        'method': '.method private static setServerConfigurations(Landroid/content/Context;)V',
        'method_name': 'setServerConfigurations',
        'method_anchors': ['const-string v0, "cloud_current_enviroment"', 'const-string v1, ""', 'invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;', 'invoke-virtual {p0}, Ljava/lang/String;->isEmpty()Z', 'const-string v1, "https://jupiter.rus.sys.miui.com/api/profile/getProfile.do?"', 'const-string v2, "https://jupiter.intl.sys.miui.com/api/profile/getProfile.do?"', 'const-string v3, "https://preview-jupiter.sys.miui.com/api/profile/getProfile.do?"', 'const-string v4, "https://jupiter.sys.miui.com/api/profile/getProfile.do?"'],
        'type': 'method_replace',
        'search': """.method private static setServerConfigurations(Landroid/content/Context;)V
    .registers 11

    const-string v0, "cloud_current_enviroment"

    const-string v1, ""

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/String;->isEmpty()Z

    move-result v0

    const-string v1, "https://jupiter.rus.sys.miui.com/api/profile/getProfile.do?"

    const-string v2, "https://jupiter.intl.sys.miui.com/api/profile/getProfile.do?"

    const-string v3, "https://preview-jupiter.sys.miui.com/api/profile/getProfile.do?"

    const-string v4, "https://jupiter.sys.miui.com/api/profile/getProfile.do?"

    const/4 v5, 0x1

    const/4 v6, 0x0

    if-nez v0, :cond_5

    invoke-virtual {p0, v4}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_1

    :cond_0
    move p0, v5

    move v0, v6

    :goto_0
    move v5, v0

    goto :goto_3

    :cond_1
    invoke-virtual {p0, v3}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_2

    move v0, v5

    move p0, v6

    move v5, p0

    goto :goto_3

    :cond_2
    invoke-virtual {p0, v2}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_3

    :goto_1
    move p0, v6

    move v0, p0

    move v6, v5

    goto :goto_0

    :cond_3
    invoke-virtual {p0, v1}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_4

    :goto_2
    move p0, v6

    move v0, p0

    goto :goto_3

    :cond_4
    move p0, v6

    move v0, p0

    goto :goto_0

    :cond_5
    const-string p0, "ro.miui.region"

    const-string v0, "unknown"

    invoke-static {p0, v0}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    const-string v0, "RU"

    invoke-virtual {p0, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p0

    if-eqz p0, :cond_6

    goto :goto_2

    :cond_6
    sget-boolean p0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p0, :cond_0

    goto :goto_1

    :goto_3
    const-string v7, "J6G4oVvvp"

    const-string v8, "kxIu9S9Wi"

    const-string v9, "wdFSzmfNh"

    if-eqz v5, :cond_7

    sput-object v1, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_NEW_SERVER:Ljava/lang/String;

    sput-object v9, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_POWER_NEW_SID:Ljava/lang/String;

    sput-object v8, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_ENGINE_SID:Ljava/lang/String;

    sput-object v7, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_THERMAL_NEW_SID:Ljava/lang/String;

    const-string p0, "78U2YSIGr"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_SHIELDER_SID:Ljava/lang/String;

    return-void

    :cond_7
    if-eqz v6, :cond_8

    sput-object v2, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_NEW_SERVER:Ljava/lang/String;

    sput-object v9, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_POWER_NEW_SID:Ljava/lang/String;

    sput-object v8, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_ENGINE_SID:Ljava/lang/String;

    sput-object v7, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_THERMAL_NEW_SID:Ljava/lang/String;

    const-string p0, "MGdeXyMDu"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_SHIELDER_SID:Ljava/lang/String;

    return-void

    :cond_8
    if-eqz p0, :cond_9

    sput-object v4, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_NEW_SERVER:Ljava/lang/String;

    const-string p0, "Ag1c4rX26"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_POWER_NEW_SID:Ljava/lang/String;

    const-string p0, "rMT8fp00I"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_ENGINE_SID:Ljava/lang/String;

    const-string p0, "6obOqcftx"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_THERMAL_NEW_SID:Ljava/lang/String;

    const-string p0, "epZVJIYU2"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_SHIELDER_SID:Ljava/lang/String;

    return-void

    :cond_9
    if-eqz v0, :cond_a

    sput-object v3, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_NEW_SERVER:Ljava/lang/String;

    const-string p0, "y4tW6V9BZ"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_POWER_NEW_SID:Ljava/lang/String;

    const-string p0, "t5fs40sND"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_ENGINE_SID:Ljava/lang/String;

    const-string p0, "mWYgmiZPb"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_THERMAL_NEW_SID:Ljava/lang/String;

    const-string p0, "ILQAXSz73"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_SHIELDER_SID:Ljava/lang/String;

    :cond_a
    return-void
.end method""",
        'replacement': """.method private static setServerConfigurations(Landroid/content/Context;)V
    .registers 11

    const-string v0, "cloud_current_enviroment"

    const-string v1, ""

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/String;->isEmpty()Z

    move-result v0

    const-string v1, "https://jupiter.rus.sys.miui.com/api/profile/getProfile.do?"

    const-string v2, "https://jupiter.intl.sys.miui.com/api/profile/getProfile.do?"

    const-string v3, "https://preview-jupiter.sys.miui.com/api/profile/getProfile.do?"

    const-string v4, "https://jupiter.sys.miui.com/api/profile/getProfile.do?"

    const/4 v5, 0x1

    const/4 v6, 0x0

    if-nez v0, :cond_5

    invoke-virtual {p0, v4}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_1

    :cond_0
    move p0, v5

    move v0, v6

    :goto_0
    move v5, v0

    goto :goto_3

    :cond_1
    invoke-virtual {p0, v3}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_2

    move v0, v5

    move p0, v6

    move v5, p0

    goto :goto_3

    :cond_2
    invoke-virtual {p0, v2}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_3

    :goto_1
    move p0, v6

    move v0, p0

    move v6, v5

    goto :goto_0

    :cond_3
    invoke-virtual {p0, v1}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_4

    :goto_2
    move p0, v6

    move v0, p0

    goto :goto_3

    :cond_4
    move p0, v6

    move v0, p0

    goto :goto_0

    :cond_5
    const-string p0, "ro.miui.region"

    const-string v0, "unknown"

    invoke-static {p0, v0}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    const-string v0, "RU"

    invoke-virtual {p0, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p0

    if-eqz p0, :cond_6

    goto :goto_2

    :cond_6
    sget-boolean p0, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz p0, :cond_0

    goto :goto_1

    :goto_3
    const-string v7, "J6G4oVvvp"

    const-string v8, "kxIu9S9Wi"

    const-string v9, "wdFSzmfNh"

    if-eqz v5, :cond_7

    sput-object v1, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_NEW_SERVER:Ljava/lang/String;

    sput-object v9, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_POWER_NEW_SID:Ljava/lang/String;

    sput-object v8, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_ENGINE_SID:Ljava/lang/String;

    sput-object v7, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_THERMAL_NEW_SID:Ljava/lang/String;

    const-string p0, "78U2YSIGr"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_SHIELDER_SID:Ljava/lang/String;

    return-void

    :cond_7
    if-eqz v6, :cond_8

    sput-object v2, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_NEW_SERVER:Ljava/lang/String;

    sput-object v9, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_POWER_NEW_SID:Ljava/lang/String;

    sput-object v8, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_ENGINE_SID:Ljava/lang/String;

    sput-object v7, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_THERMAL_NEW_SID:Ljava/lang/String;

    const-string p0, "MGdeXyMDu"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_SHIELDER_SID:Ljava/lang/String;

    return-void

    :cond_8
    if-eqz p0, :cond_9

    sput-object v4, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_NEW_SERVER:Ljava/lang/String;

    const-string p0, "Ag1c4rX26"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_POWER_NEW_SID:Ljava/lang/String;

    const-string p0, "rMT8fp00I"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_ENGINE_SID:Ljava/lang/String;

    const-string p0, "6obOqcftx"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_THERMAL_NEW_SID:Ljava/lang/String;

    const-string p0, "epZVJIYU2"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_SHIELDER_SID:Ljava/lang/String;

    return-void

    :cond_9
    if-eqz v0, :cond_a

    sput-object v3, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_NEW_SERVER:Ljava/lang/String;

    const-string p0, "y4tW6V9BZ"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_POWER_NEW_SID:Ljava/lang/String;

    const-string p0, "t5fs40sND"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_ENGINE_SID:Ljava/lang/String;

    const-string p0, "mWYgmiZPb"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_THERMAL_NEW_SID:Ljava/lang/String;

    const-string p0, "ILQAXSz73"

    sput-object p0, Lcom/miui/powerkeeper/cloudcontrol/Constants;->CLOUD_PERF_SHIELDER_SID:Ljava/lang/String;

    :cond_a
    return-void
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
