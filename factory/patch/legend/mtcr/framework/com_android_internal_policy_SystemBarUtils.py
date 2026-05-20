"""
Legend MTCR patch - class-level rule.

Target JAR   : framework.jar
Target class : com/android/internal/policy/SystemBarUtils
Source MTCR  : Framework_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "framework.jar"
TARGET_CLASS = "com/android/internal/policy/SystemBarUtils.smali"
CLASS_FALLBACK_NAMES = ['SystemBarUtils.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "add_method__init___V",
        "method":      ".method public constructor whitelist <init>()V",
        "method_name": '<init>',
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method public constructor whitelist <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Framework_Legend.mtcr",
    },
    {
        "id":          "add_method_getDesktopViewAppHeaderHeightId__I",
        "method":      ".method public static whitelist getDesktopViewAppHeaderHeightId()I",
        "method_name": 'getDesktopViewAppHeaderHeightId',
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method public static whitelist getDesktopViewAppHeaderHeightId()I
    .registers 1

    const v0, 0x1050174

    return v0
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Framework_Legend.mtcr",
    },
    {
        "id":          "add_method_getDesktopViewAppHeaderHeightPx_Landroid_content_Context__I",
        "method":      ".method public static whitelist getDesktopViewAppHeaderHeightPx(Landroid/content/Context;)I",
        "method_name": 'getDesktopViewAppHeaderHeightPx',
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method public static whitelist getDesktopViewAppHeaderHeightPx(Landroid/content/Context;)I
    .registers 3

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-static {}, Lcom/android/internal/policy/SystemBarUtils;->getDesktopViewAppHeaderHeightId()I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    return v0
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Framework_Legend.mtcr",
    },
    {
        "id":          "add_method_getQuickQsOffsetHeight_Landroid_content_Context__I",
        "method":      ".method public static whitelist getQuickQsOffsetHeight(Landroid/content/Context;)I",
        "method_name": 'getQuickQsOffsetHeight',
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method public static whitelist getQuickQsOffsetHeight(Landroid/content/Context;)I
    .registers 4

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const v1, 0x105034a

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    invoke-static {p0}, Lcom/android/internal/policy/SystemBarUtils;->getStatusBarHeight(Landroid/content/Context;)I

    move-result v1

    invoke-static {v0, v1}, Ljava/lang/Math;->max(II)I

    move-result v2

    return v2
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Framework_Legend.mtcr",
    },
    {
        "id":          "add_method_getStatusBarHeight_Landroid_content_Context__I",
        "method":      ".method public static whitelist getStatusBarHeight(Landroid/content/Context;)I",
        "method_name": 'getStatusBarHeight',
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method public static whitelist getStatusBarHeight(Landroid/content/Context;)I
    .registers 3

    invoke-static {p0}, Lcom/android/internal/policy/SystemBarUtils;->getSystemSettingsHeight(Landroid/content/Context;)I

    move-result v0

    if-lez v0, :cond_0

    return v0

    :cond_0
    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {p0}, Landroid/content/Context;->getDisplay()Landroid/view/Display;

    move-result-object v1

    invoke-virtual {v1}, Landroid/view/Display;->getCutout()Landroid/view/DisplayCutout;

    move-result-object v1

    invoke-static {v0, v1}, Lcom/android/internal/policy/SystemBarUtils;->getStatusBarHeight(Landroid/content/res/Resources;Landroid/view/DisplayCutout;)I

    move-result v0

    return v0
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Framework_Legend.mtcr",
    },
    {
        "id":          "add_method_getStatusBarHeight_Landroid_content_res_Resources_Landroid_v",
        "method":      ".method public static whitelist getStatusBarHeight(Landroid/content/res/Resources;Landroid/view/DisplayCutout;)I",
        "method_name": 'getStatusBarHeight',
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method public static whitelist getStatusBarHeight(Landroid/content/res/Resources;Landroid/view/DisplayCutout;)I
    .registers 6

    const v0, 0x105038d

    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    const/4 v1, 0x0

    if-nez p1, :cond_0

    move v2, v1

    goto :goto_0

    :cond_0
    invoke-virtual {p1}, Landroid/view/DisplayCutout;->getSafeInsetTop()I

    move-result v2

    :goto_0
    if-nez p1, :cond_1

    goto :goto_1

    :cond_1
    invoke-virtual {p1}, Landroid/view/DisplayCutout;->getWaterfallInsets()Landroid/graphics/Insets;

    move-result-object v1

    iget v1, v1, Landroid/graphics/Insets;->top:I

    :goto_1
    add-int v3, v0, v1

    invoke-static {v2, v3}, Ljava/lang/Math;->max(II)I

    move-result v3

    return v3
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Framework_Legend.mtcr",
    },
    {
        "id":          "add_method_getStatusBarHeightForRotation_Landroid_content_Context_I_I",
        "method":      ".method public static whitelist getStatusBarHeightForRotation(Landroid/content/Context;I)I",
        "method_name": 'getStatusBarHeightForRotation',
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method public static whitelist getStatusBarHeightForRotation(Landroid/content/Context;I)I
    .registers 13

    invoke-static {p0}, Lcom/android/internal/policy/SystemBarUtils;->getSystemSettingsHeight(Landroid/content/Context;)I

    move-result v0

    if-lez v0, :cond_0

    return v0

    :cond_0
    invoke-virtual {p0}, Landroid/content/Context;->getDisplay()Landroid/view/Display;

    move-result-object v0

    invoke-virtual {v0}, Landroid/view/Display;->getRotation()I

    move-result v1

    invoke-virtual {v0}, Landroid/view/Display;->getCutout()Landroid/view/DisplayCutout;

    move-result-object v2

    new-instance v3, Landroid/view/DisplayInfo;

    invoke-direct {v3}, Landroid/view/DisplayInfo;-><init>()V

    invoke-virtual {v0, v3}, Landroid/view/Display;->getDisplayInfo(Landroid/view/DisplayInfo;)Z

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v4

    invoke-virtual {v4}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v4

    iget v4, v4, Landroid/util/DisplayMetrics;->widthPixels:I

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v5

    invoke-virtual {v5}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v5

    iget v5, v5, Landroid/util/DisplayMetrics;->heightPixels:I

    if-nez v2, :cond_1

    sget-object v6, Landroid/graphics/Insets;->NONE:Landroid/graphics/Insets;

    sget-object v7, Landroid/graphics/Insets;->NONE:Landroid/graphics/Insets;

    goto :goto_0

    :cond_1
    nop

    invoke-virtual {v2, v4, v5, v1, p1}, Landroid/view/DisplayCutout;->getRotated(IIII)Landroid/view/DisplayCutout;

    move-result-object v6

    invoke-virtual {v6}, Landroid/view/DisplayCutout;->getSafeInsets()Landroid/graphics/Rect;

    move-result-object v7

    invoke-static {v7}, Landroid/graphics/Insets;->of(Landroid/graphics/Rect;)Landroid/graphics/Insets;

    move-result-object v7

    invoke-virtual {v6}, Landroid/view/DisplayCutout;->getWaterfallInsets()Landroid/graphics/Insets;

    move-result-object v8

    move-object v6, v7

    move-object v7, v8

    :goto_0
    nop

    invoke-virtual {p0}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v8

    const v9, 0x105038d

    invoke-virtual {v8, v9}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v8

    iget v9, v6, Landroid/graphics/Insets;->top:I

    iget v10, v7, Landroid/graphics/Insets;->top:I

    add-int/2addr v10, v8

    invoke-static {v9, v10}, Ljava/lang/Math;->max(II)I

    move-result v9

    return v9
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Framework_Legend.mtcr",
    },
    {
        "id":          "add_method_getSystemSettingsHeight_Landroid_content_Context__I",
        "method":      ".method public static blacklist getSystemSettingsHeight(Landroid/content/Context;)I",
        "method_name": 'getSystemSettingsHeight',
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method public static blacklist getSystemSettingsHeight(Landroid/content/Context;)I
    .registers 5

    const/4 v3, 0x0

    const/4 v0, 0x0

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    if-eqz v1, :cond_0

    const-string v2, "custom_status_bar_height"

    invoke-static {v1, v2, v3}, Landroid/provider/Settings$Global;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    const-string v2, "custom_statusbar_dialog_open"

    invoke-static {v1, v2, v3}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v2

    const/4 v3, 0x1

    if-ne v2, v3, :cond_0

    const/16 v0, 0xfa

    :cond_0
    return v0
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Framework_Legend.mtcr",
    },
    {
        "id":          "add_method_getTaskbarHeight_Landroid_content_res_Resources__I",
        "method":      ".method public static whitelist getTaskbarHeight(Landroid/content/res/Resources;)I",
        "method_name": 'getTaskbarHeight',
        "type":        "method_add",
        "search":      None,
        "replacement": """\
.method public static whitelist getTaskbarHeight(Landroid/content/res/Resources;)I
    .registers 2

    const v0, 0x105039c

    invoke-virtual {p0, v0}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    return v0
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR new method from Framework_Legend.mtcr",
    },
]
