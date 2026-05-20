"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/controlcenter/phone/ControlPanelWindowManager$OnWindowChangeListener.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/controlcenter/phone/ControlPanelWindowManager$OnWindowChangeListener.smali'
CLASS_FALLBACK_NAMES = ['ControlPanelWindowManager$OnWindowChangeListener.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_controlcenter_phone_ControlPanelWindowM',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public interface abstract Lcom/android/systemui/controlcenter/phone/ControlPanelWindowManager$OnWindowChangeListener;\n.super Ljava/lang/Object;\n\n\n# virtual methods\n.method public abstract onExpandChange(Z)V\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
