"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/StatusIconsVisibilityController.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/StatusIconsVisibilityController.smali'
CLASS_FALLBACK_NAMES = ['StatusIconsVisibilityController.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_StatusIconsVis',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public Lcom/android/systemui/newstatusbar/controllers/StatusIconsVisibilityController;\n.super Lcom/android/systemui/plugins/controllers/ControllerExt;\n\n\n# annotations\n.annotation system Ldalvik/annotation/MemberClasses;\n    value = {\n        Lcom/android/systemui/newstatusbar/controllers/StatusIconsVisibilityController$IgnoredSlots;\n    }\n.end annotation\n\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "Lcom/android/systemui/plugins/controllers/ControllerExt<",\n        "Lcom/android/systemui/newstatusbar/controllers/StatusIconsVisibilityController$IgnoredSlots;",\n        ">;"\n    }\n.end annotation\n\n\n# direct methods\n.method public constructor <init>(Landroid/content/Context;)V\n    .registers 2\n\n    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
