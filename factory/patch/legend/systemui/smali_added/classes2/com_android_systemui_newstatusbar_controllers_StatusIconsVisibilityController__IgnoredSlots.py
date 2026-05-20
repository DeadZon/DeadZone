"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/controllers/StatusIconsVisibilityController$IgnoredSlots.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/controllers/StatusIconsVisibilityController$IgnoredSlots.smali'
CLASS_FALLBACK_NAMES = ['StatusIconsVisibilityController$IgnoredSlots.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_controllers_StatusIconsVis',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public interface abstract Lcom/android/systemui/newstatusbar/controllers/StatusIconsVisibilityController$IgnoredSlots;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/newstatusbar/controllers/StatusIconsVisibilityController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x609\n    name = "IgnoredSlots"\n.end annotation\n\n\n# virtual methods\n.method public abstract setIgnoredSlots(Ljava/util/ArrayList;)V\n    .annotation system Ldalvik/annotation/Signature;\n        value = {\n            "(",\n            "Ljava/util/ArrayList<",\n            "Ljava/lang/String;",\n            ">;)V"\n        }\n    .end annotation\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
