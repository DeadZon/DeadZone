"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/IClock.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/IClock.smali'
CLASS_FALLBACK_NAMES = ['IClock.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_IClock',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public interface abstract Lcom/android/systemui/newstatusbar/clock/IClock;\n.super Ljava/lang/Object;\n\n\n# virtual methods\n.method public abstract fullInvalidate()V\n.end method\n\n.method public abstract getContext()Landroid/content/Context;\n.end method\n\n.method public abstract getTextHeight()F\n.end method\n\n.method public abstract getTextSize()F\n.end method\n\n.method public abstract onTextChanged(Ljava/lang/CharSequence;)V\n.end method\n\n.method public setText(Ljava/lang/String;Z)V\n    .registers 3\n\n    return-void\n.end method\n\n.method public abstract setTextSize(F)V\n.end method\n\n.method public abstract setTextSizeWidthAnimation(F)V\n.end method\n\n.method public abstract setVisibility(I)V\n.end method\n\n.method public updateSettings()V\n    .registers 1\n\n    return-void\n.end method\n\n.method public abstract updateTypeface(Landroid/graphics/Typeface;I)V\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
