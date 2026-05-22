TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'miui/yellowpage/YellowPageUtils.smali'
CLASS_FALLBACK_NAMES = ['YellowPageUtils.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final ANTISPAM_COLUMN_CID:I = 0x1', '.field private static final ANTISPAM_COLUMN_MARKED_COUNT:I = 0x3', '.field private static final ANTISPAM_COLUMN_NORMALIZED_NUMBER:I = 0x4', '.field private static final ANTISPAM_COLUMN_NUMBER_TYPE:I = 0x5', '.field private static final ANTISPAM_COLUMN_PID:I = 0x0']

PATCHES = [
    {
        'id': 'miui_yellowpage_YellowPageUtils__isYellowPageAvailable',
        'method': '.method public static isYellowPageAvailable(Landroid/content/Context;)Z',
        'method_name': 'isYellowPageAvailable',
        'method_anchors': ['invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_1', 'sget-object v0, Ljava/util/Locale;->SIMPLIFIED_CHINESE:Ljava/util/Locale;', 'invoke-virtual {v0, p0}, Ljava/util/Locale;->equals(Ljava/lang/Object;)Z', 'if-nez v0, :cond_0', 'sget-object v0, Ljava/util/Locale;->TRADITIONAL_CHINESE:Ljava/util/Locale;', 'invoke-virtual {v0, p0}, Ljava/util/Locale;->equals(Ljava/lang/Object;)Z'],
        'type': 'method_replace',
        'search': """.method public static isYellowPageAvailable(Landroid/content/Context;)Z
    .registers 5

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object p0

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    const/4 v2, 0x1

    if-nez v0, :cond_1

    sget-object v0, Ljava/util/Locale;->SIMPLIFIED_CHINESE:Ljava/util/Locale;

    invoke-virtual {v0, p0}, Ljava/util/Locale;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    sget-object v0, Ljava/util/Locale;->TRADITIONAL_CHINESE:Ljava/util/Locale;

    invoke-virtual {v0, p0}, Ljava/util/Locale;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    sget-object v0, Ljava/util/Locale;->US:Ljava/util/Locale;

    invoke-virtual {v0, p0}, Ljava/util/Locale;->equals(Ljava/lang/Object;)Z

    move-result p0

    if-eqz p0, :cond_1

    :cond_0
    move p0, v2

    goto :goto_0

    :cond_1
    move p0, v1

    :goto_0
    const-string v0, "IN"

    invoke-static {}, Lmiui/os/Build;->getRegion()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez p0, :cond_3

    if-eqz v0, :cond_2

    goto :goto_1

    :cond_2
    return v1

    :cond_3
    :goto_1
    return v2
.end method""",
        'replacement': """.method public static isYellowPageAvailable(Landroid/content/Context;)Z
    .registers 5

    invoke-static {}, Ljava/util/Locale;->getDefault()Ljava/util/Locale;

    move-result-object p0

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v1, 0x0

    const/4 v2, 0x1

    if-nez v0, :cond_1

    sget-object v0, Ljava/util/Locale;->SIMPLIFIED_CHINESE:Ljava/util/Locale;

    invoke-virtual {v0, p0}, Ljava/util/Locale;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    sget-object v0, Ljava/util/Locale;->TRADITIONAL_CHINESE:Ljava/util/Locale;

    invoke-virtual {v0, p0}, Ljava/util/Locale;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    sget-object v0, Ljava/util/Locale;->US:Ljava/util/Locale;

    invoke-virtual {v0, p0}, Ljava/util/Locale;->equals(Ljava/lang/Object;)Z

    move-result p0

    if-eqz p0, :cond_1

    :cond_0
    move p0, v2

    goto :goto_0

    :cond_1
    move p0, v1

    :goto_0
    const-string v0, "IN"

    invoke-static {}, Lmiui/os/Build;->getRegion()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez p0, :cond_3

    if-eqz v0, :cond_2

    goto :goto_1

    :cond_2
    return v1

    :cond_3
    :goto_1
    return v2
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
