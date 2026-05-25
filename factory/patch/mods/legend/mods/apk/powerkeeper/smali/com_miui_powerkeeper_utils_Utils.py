TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/utils/Utils.smali'
CLASS_FALLBACK_NAMES = ['Utils.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final APP_CONTEXT:Landroid/content/Context;', '.field static final EU:Ljava/util/Set;', '.field private static final PROCESS_STATS_FORMAT:[I', '.field public static final SERVICE_NAME_POWER:Ljava/lang/String; = "miui.whetstone.power"', '.field private static final SYSTEM_CPU_FORMAT:[I']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_utils_Utils__isCloudControlAllowed',
        'method': '.method public static isCloudControlAllowed(Landroid/content/Context;)Z',
        'method_name': 'isCloudControlAllowed',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'const-string v1, "upload_log"', 'invoke-static {p0, v1, v0}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method public static isCloudControlAllowed(Landroid/content/Context;)Z
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 v0, v0, 0x1

    const-string v1, "upload_log"

    invoke-static {p0, v1, v0}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method public static isCloudControlAllowed(Landroid/content/Context;)Z
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    xor-int/lit8 v0, v0, 0x1

    const-string v1, "upload_log"

    invoke-static {p0, v1, v0}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z

    move-result p0

    return p0
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
    {
        'id': 'com_miui_powerkeeper_utils_Utils__isUserExperienceAndPrivacyAllowed',
        'method': '.method public static isUserExperienceAndPrivacyAllowed(Landroid/content/Context;)Z',
        'method_name': 'isUserExperienceAndPrivacyAllowed',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'const-string v2, "upload_log"', 'invoke-static {p0, v2, v0}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;', 'const-string v3, "upload_log_pref"', 'invoke-static {v0, v3, v2}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I', 'if-lez v0, :cond_0'],
        'type': 'method_replace',
        'search': """.method public static isUserExperienceAndPrivacyAllowed(Landroid/content/Context;)Z
    .registers 5

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x1

    xor-int/2addr v0, v1

    const-string v2, "upload_log"

    invoke-static {p0, v2, v0}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z

    move-result v0

    const/4 v2, 0x0

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v3, "upload_log_pref"

    invoke-static {v0, v3, v2}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    if-lez v0, :cond_0

    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v0

    invoke-static {p0, v0}, Landroid/provider/MiuiSettings$Privacy;->isEnabled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    return v1

    :cond_0
    return v2
.end method""",
        'replacement': """.method public static isUserExperienceAndPrivacyAllowed(Landroid/content/Context;)Z
    .registers 5

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v1, 0x1

    xor-int/2addr v0, v1

    const-string v2, "upload_log"

    invoke-static {p0, v2, v0}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z

    move-result v0

    const/4 v2, 0x0

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v3, "upload_log_pref"

    invoke-static {v0, v3, v2}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    if-lez v0, :cond_0

    invoke-virtual {p0}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v0

    invoke-static {p0, v0}, Landroid/provider/MiuiSettings$Privacy;->isEnabled(Landroid/content/Context;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_0

    return v1

    :cond_0
    return v2
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
