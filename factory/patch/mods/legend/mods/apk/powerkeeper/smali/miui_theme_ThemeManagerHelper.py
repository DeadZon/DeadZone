TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'miui/theme/ThemeManagerHelper.smali'
CLASS_FALLBACK_NAMES = ['ThemeManagerHelper.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final TAG:Ljava/lang/String; = "ThemeManagerHelper"']

PATCHES = [
    {
        'id': 'miui_theme_ThemeManagerHelper__needDisableTheme',
        'method': '.method public static needDisableTheme(Landroid/content/Context;)Z',
        'method_name': 'needDisableTheme',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z', 'if-nez v0, :cond_4', 'invoke-static {}, Lmiui/theme/ThemeManagerHelper;->isHideTheme()Z', 'if-eqz v0, :cond_0', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_3', 'invoke-static {p0}, Lmiui/theme/GlobalUtils;->isEU(Landroid/content/Context;)Z', 'if-eqz v0, :cond_2'],
        'type': 'method_replace',
        'search': """.method public static needDisableTheme(Landroid/content/Context;)Z
    .registers 4

    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    const/4 v1, 0x1

    if-nez v0, :cond_4

    invoke-static {}, Lmiui/theme/ThemeManagerHelper;->isHideTheme()Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v2, 0x0

    if-eqz v0, :cond_3

    invoke-static {p0}, Lmiui/theme/GlobalUtils;->isEU(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-static {}, Lmiui/os/Build;->getMiUiVersionCode()Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_1

    invoke-static {p0}, Ljava/lang/Integer;->valueOf(Ljava/lang/String;)Ljava/lang/Integer;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    const/16 v0, 0x8

    if-lt p0, v0, :cond_1

    return v2

    :cond_1
    return v1

    :cond_2
    invoke-static {p0}, Lmiui/theme/GlobalUtils;->isReligiousArea(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_3

    return v1

    :cond_3
    return v2

    :cond_4
    :goto_0
    return v1
.end method""",
        'replacement': """.method public static needDisableTheme(Landroid/content/Context;)Z
    .registers 4

    sget-boolean v0, Lmiui/os/Build;->IS_TABLET:Z

    const/4 v1, 0x1

    if-nez v0, :cond_4

    invoke-static {}, Lmiui/theme/ThemeManagerHelper;->isHideTheme()Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v2, 0x0

    if-eqz v0, :cond_3

    invoke-static {p0}, Lmiui/theme/GlobalUtils;->isEU(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-static {}, Lmiui/os/Build;->getMiUiVersionCode()Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_1

    invoke-static {p0}, Ljava/lang/Integer;->valueOf(Ljava/lang/String;)Ljava/lang/Integer;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    const/16 v0, 0x8

    if-lt p0, v0, :cond_1

    return v2

    :cond_1
    return v1

    :cond_2
    invoke-static {p0}, Lmiui/theme/GlobalUtils;->isReligiousArea(Landroid/content/Context;)Z

    move-result p0

    if-eqz p0, :cond_3

    return v1

    :cond_3
    return v2

    :cond_4
    :goto_0
    return v1
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
