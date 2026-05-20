"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/plugins/controllers/ControllerExt$CallBack.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/plugins/controllers/ControllerExt$CallBack.smali'
CLASS_FALLBACK_NAMES = ['ControllerExt$CallBack.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_plugins_controllers_ControllerExt$CallB',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public interface abstract Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/plugins/controllers/ControllerExt;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x609\n    name = "CallBack"\n.end annotation\n\n\n# virtual methods\n.method public post(Ljava/lang/Runnable;)Z\n    .registers 3\n\n    const/4 v0, 0x0\n\n    return v0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
