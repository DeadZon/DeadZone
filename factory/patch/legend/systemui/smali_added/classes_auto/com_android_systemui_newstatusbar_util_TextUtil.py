"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/util/TextUtil.smali'
CLASS_FALLBACK_NAMES = ['TextUtil.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/util/TextUtil;
.super Ljava/lang/Object;


# static fields
.field private static final tmpRect:Landroid/graphics/Rect;


# direct methods
.method static constructor <clinit>()V
    .registers 1

    new-instance v0, Landroid/graphics/Rect;

    invoke-direct {v0}, Landroid/graphics/Rect;-><init>()V

    sput-object v0, Lcom/android/systemui/newstatusbar/util/TextUtil;->tmpRect:Landroid/graphics/Rect;

    return-void
.end method

.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static getTextHeight(Landroid/widget/TextView;)I
    .registers 3

    if-nez p0, :cond_4

    const/4 v0, 0x0

    return v0

    :cond_4
    invoke-virtual {p0}, Landroid/widget/TextView;->getText()Ljava/lang/CharSequence;

    move-result-object v0

    invoke-interface {v0}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p0}, Landroid/widget/TextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v1

    invoke-static {v0, v1}, Lcom/android/systemui/newstatusbar/util/TextUtil;->getTextHeight(Ljava/lang/String;Landroid/text/TextPaint;)I

    move-result v0

    return v0
.end method

.method public static getTextHeight(Ljava/lang/String;Landroid/text/TextPaint;)I
    .registers 5

    const/4 v0, 0x0

    if-eqz p0, :cond_1a

    invoke-virtual {p0}, Ljava/lang/String;->isEmpty()Z

    move-result v1

    if-nez v1, :cond_1a

    if-nez p1, :cond_c

    goto :goto_1a

    :cond_c
    invoke-virtual {p0}, Ljava/lang/String;->length()I

    move-result v1

    sget-object v2, Lcom/android/systemui/newstatusbar/util/TextUtil;->tmpRect:Landroid/graphics/Rect;

    invoke-virtual {p1, p0, v0, v1, v2}, Landroid/text/TextPaint;->getTextBounds(Ljava/lang/String;IILandroid/graphics/Rect;)V

    invoke-virtual {v2}, Landroid/graphics/Rect;->height()I

    move-result v0

    return v0

    :cond_1a
    :goto_1a
    return v0
.end method

.method public static measureText(Landroid/text/TextPaint;Ljava/lang/String;Z)I
    .registers 8

    const/4 v0, 0x0

    if-eqz p0, :cond_3a

    if-eqz p1, :cond_3a

    invoke-virtual {p1}, Ljava/lang/String;->isEmpty()Z

    move-result v1

    if-eqz v1, :cond_c

    goto :goto_3a

    :cond_c
    if-eqz p2, :cond_32

    sget-object v1, Lcom/android/systemui/newstatusbar/util/TextUtil;->tmpRect:Landroid/graphics/Rect;

    invoke-virtual {p1}, Ljava/lang/String;->length()I

    move-result v2

    invoke-virtual {p0, p1, v0, v2, v1}, Landroid/text/TextPaint;->getTextBounds(Ljava/lang/String;IILandroid/graphics/Rect;)V

    invoke-virtual {v1}, Landroid/graphics/Rect;->width()I

    move-result v2

    if-eqz p2, :cond_31

    invoke-virtual {p1}, Ljava/lang/String;->length()I

    move-result v3

    const/4 v4, 0x1

    sub-int/2addr v3, v4

    invoke-virtual {p1, v3}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {p0, v3, v0, v4, v1}, Landroid/text/TextPaint;->getTextBounds(Ljava/lang/String;IILandroid/graphics/Rect;)V

    invoke-virtual {v1}, Landroid/graphics/Rect;->width()I

    move-result v0

    div-int/lit8 v0, v0, 0x3

    add-int/2addr v2, v0

    :cond_31
    return v2

    :cond_32
    invoke-virtual {p0, p1}, Landroid/text/TextPaint;->measureText(Ljava/lang/String;)F

    move-result v0

    float-to-int v0, v0

    add-int/lit8 v0, v0, 0x5

    return v0

    :cond_3a
    :goto_3a
    return v0
.end method

.method public static measureText(Landroid/widget/TextView;)I
    .registers 4

    invoke-virtual {p0}, Landroid/widget/TextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    invoke-virtual {p0}, Landroid/widget/TextView;->getText()Ljava/lang/CharSequence;

    move-result-object v1

    invoke-interface {v1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x0

    invoke-static {v0, v1, v2}, Lcom/android/systemui/newstatusbar/util/TextUtil;->measureText(Landroid/text/TextPaint;Ljava/lang/String;Z)I

    move-result v0

    return v0
.end method

.method public static measureText(Landroid/widget/TextView;Z)I
    .registers 4

    invoke-virtual {p0}, Landroid/widget/TextView;->getPaint()Landroid/text/TextPaint;

    move-result-object v0

    invoke-virtual {p0}, Landroid/widget/TextView;->getText()Ljava/lang/CharSequence;

    move-result-object v1

    invoke-interface {v1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v1, p1}, Lcom/android/systemui/newstatusbar/util/TextUtil;->measureText(Landroid/text/TextPaint;Ljava/lang/String;Z)I

    move-result v0

    return v0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_util_TextUtil',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
