"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener.smali'
CLASS_FALLBACK_NAMES = ['Shake$ShakeDetector$OnShakeListener.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_policy_Shake$ShakeDetector',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public interface abstract Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x609\n    name = "OnShakeListener"\n.end annotation\n\n\n# virtual methods\n.method public abstract onShake(I)V\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
