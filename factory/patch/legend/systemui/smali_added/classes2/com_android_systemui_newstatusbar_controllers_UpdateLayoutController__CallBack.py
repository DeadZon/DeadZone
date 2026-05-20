"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/UpdateLayoutController$CallBack.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/UpdateLayoutController$CallBack.smali'
CLASS_FALLBACK_NAMES = ['UpdateLayoutController$CallBack.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_UpdateLayoutCo',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public interface abstract Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$CallBack;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x609\n    name = "CallBack"\n.end annotation\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
