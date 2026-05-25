"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/clock/IClock.smali'
CLASS_FALLBACK_NAMES = ['IClock.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public interface abstract Lcom/android/systemui/newstatusbar/clock/IClock;
.super Ljava/lang/Object;


# virtual methods
.method public abstract fullInvalidate()V
.end method

.method public abstract getContext()Landroid/content/Context;
.end method

.method public abstract getTextHeight()F
.end method

.method public abstract getTextSize()F
.end method

.method public abstract onTextChanged(Ljava/lang/CharSequence;)V
.end method

.method public setText(Ljava/lang/String;Z)V
    .registers 3

    return-void
.end method

.method public abstract setTextSize(F)V
.end method

.method public abstract setTextSizeWidthAnimation(F)V
.end method

.method public abstract setVisibility(I)V
.end method

.method public updateSettings()V
    .registers 1

    return-void
.end method

.method public abstract updateTypeface(Landroid/graphics/Typeface;I)V
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_clock_IClock',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
