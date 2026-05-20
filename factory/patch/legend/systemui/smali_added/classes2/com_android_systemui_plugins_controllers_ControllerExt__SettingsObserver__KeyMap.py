"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap.smali'
CLASS_FALLBACK_NAMES = ['ControllerExt$SettingsObserver$KeyMap.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_plugins_controllers_ControllerExt$Setti',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0xa\n    name = "KeyMap"\n.end annotation\n\n\n# instance fields\n.field isRegister:Z\n\n.field final key:Ljava/lang/String;\n\n\n# direct methods\n.method public constructor <init>(Ljava/lang/String;)V\n    .registers 3\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    const/4 v0, 0x0\n\n    iput-boolean v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->isRegister:Z\n\n    iput-object p1, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->key:Ljava/lang/String;\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public register()V\n    .registers 2\n\n    const/4 v0, 0x1\n\n    iput-boolean v0, p0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$KeyMap;->isRegister:Z\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
