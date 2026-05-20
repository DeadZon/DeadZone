"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/policy/TextUtil.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/policy/TextUtil.smali'
CLASS_FALLBACK_NAMES = ['TextUtil.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_policy_TextUtil',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/policy/TextUtil;\n.super Ljava/lang/Object;\n\n\n# direct methods\n.method public constructor <init>()V\n    .registers 1\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n.method public static measureText(Landroid/text/TextPaint;Ljava/lang/String;Z)I\n    .registers 8\n\n    const/4 v2, 0x0\n\n    if-eqz p0, :cond_0\n\n    if-eqz p1, :cond_0\n\n    invoke-virtual {p1}, Ljava/lang/String;->isEmpty()Z\n\n    move-result v3\n\n    if-eqz v3, :cond_2\n\n    :cond_0\n    move v1, v2\n\n    :cond_1\n    :goto_0\n    return v1\n\n    :cond_2\n    new-instance v0, Landroid/graphics/Rect;\n\n    invoke-direct {v0}, Landroid/graphics/Rect;-><init>()V\n\n    invoke-virtual {p1}, Ljava/lang/String;->length()I\n\n    move-result v3\n\n    invoke-virtual {p0, p1, v2, v3, v0}, Landroid/text/TextPaint;->getTextBounds(Ljava/lang/String;IILandroid/graphics/Rect;)V\n\n    invoke-virtual {v0}, Landroid/graphics/Rect;->width()I\n\n    move-result v1\n\n    if-eqz p2, :cond_1\n\n    invoke-virtual {p1}, Ljava/lang/String;->length()I\n\n    move-result v3\n\n    add-int/lit8 v3, v3, -0x1\n\n    invoke-virtual {p1, v3}, Ljava/lang/String;->substring(I)Ljava/lang/String;\n\n    move-result-object v3\n\n    const/4 v4, 0x1\n\n    invoke-virtual {p0, v3, v2, v4, v0}, Landroid/text/TextPaint;->getTextBounds(Ljava/lang/String;IILandroid/graphics/Rect;)V\n\n    invoke-virtual {v0}, Landroid/graphics/Rect;->width()I\n\n    move-result v2\n\n    div-int/lit8 v2, v2, 0x3\n\n    add-int/2addr v1, v2\n\n    goto :goto_0\n.end method\n\n.method public static measureText(Landroid/widget/TextView;)I\n    .registers 4\n\n    invoke-virtual {p0}, Landroid/widget/TextView;->getPaint()Landroid/text/TextPaint;\n\n    move-result-object v0\n\n    invoke-virtual {p0}, Landroid/widget/TextView;->getText()Ljava/lang/CharSequence;\n\n    move-result-object v1\n\n    invoke-interface {v1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;\n\n    move-result-object v1\n\n    const/4 v2, 0x0\n\n    invoke-static {v0, v1, v2}, Lcom/android/systemui/newstatusbar/policy/TextUtil;->measureText(Landroid/text/TextPaint;Ljava/lang/String;Z)I\n\n    move-result v0\n\n    return v0\n.end method\n\n.method public static measureText(Landroid/widget/TextView;Z)I\n    .registers 4\n\n    invoke-virtual {p0}, Landroid/widget/TextView;->getPaint()Landroid/text/TextPaint;\n\n    move-result-object v0\n\n    invoke-virtual {p0}, Landroid/widget/TextView;->getText()Ljava/lang/CharSequence;\n\n    move-result-object v1\n\n    invoke-interface {v1}, Ljava/lang/CharSequence;->toString()Ljava/lang/String;\n\n    move-result-object v1\n\n    invoke-static {v0, v1, p1}, Lcom/android/systemui/newstatusbar/policy/TextUtil;->measureText(Landroid/text/TextPaint;Ljava/lang/String;Z)I\n\n    move-result v0\n\n    return v0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
