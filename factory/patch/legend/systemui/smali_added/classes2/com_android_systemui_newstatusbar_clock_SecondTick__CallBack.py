"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/clock/SecondTick$CallBack.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/clock/SecondTick$CallBack.smali'
CLASS_FALLBACK_NAMES = ['SecondTick$CallBack.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_clock_SecondTick$CallBack',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public interface abstract Lcom/android/systemui/newstatusbar/clock/SecondTick$CallBack;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/clock/SecondTick;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x609\n    name = "CallBack"\n.end annotation\n\n\n# virtual methods\n.method public isSecondEnable()Z\n    .registers 2\n\n    const/4 v0, 0x0\n\n    return v0\n.end method\n\n.method public abstract post(Ljava/lang/Runnable;)Z\n.end method\n\n.method public secondTick()V\n    .registers 1\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
