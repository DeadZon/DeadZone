"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener.smali'
CLASS_FALLBACK_NAMES = ['ControllerExt$SettingsObserver$onChangeListener.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_plugins_controllers_ControllerExt$Setti',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public interface abstract Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x609\n    name = "onChangeListener"\n.end annotation\n\n\n# virtual methods\n.method public onChange()V\n    .registers 1\n\n    return-void\n.end method\n\n.method public onChange(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;Landroid/net/Uri;)V\n    .registers 3\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "(",\n            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver",\n            "<+",\n            "Lcom/android/systemui/plugins/controllers/ControllerExt",\n            "<+",\n            "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",\n            ">;>;",\n            "Landroid/net/Uri;",\n            ")V"\n        }\n    .end annotation\n\n    invoke-interface {p0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;->onChange()V\n\n    return-void\n.end method\n\n.method public onChange(Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;Ljava/lang/String;)V\n    .registers 3\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "(",\n            "Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver",\n            "<+",\n            "Lcom/android/systemui/plugins/controllers/ControllerExt",\n            "<+",\n            "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",\n            ">;>;",\n            "Ljava/lang/String;",\n            ")V"\n        }\n    .end annotation\n\n    invoke-interface {p0, p2}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;->onChange(Ljava/lang/String;)V\n\n    return-void\n.end method\n\n.method public onChange(Ljava/lang/String;)V\n    .registers 2\n\n    invoke-interface {p0}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;->onChange()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
