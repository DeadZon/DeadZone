"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/plugins/ControllerStorage$ControllerStorageKey.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/plugins/ControllerStorage$ControllerStorageKey.smali'
CLASS_FALLBACK_NAMES = ['ControllerStorage$ControllerStorageKey.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_plugins_ControllerStorage$ControllerSto',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/android/systemui/plugins/ControllerStorage$ControllerStorageKey;\n.super Ljava/lang/Object;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/plugins/ControllerStorage;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x19\n    name = "ControllerStorageKey"\n.end annotation\n\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "<V:",\n        "Ljava/lang/Object;",\n        ">",\n        "Ljava/lang/Object;"\n    }\n.end annotation\n\n\n# instance fields\n.field public final mDisplayName:Ljava/lang/String;\n\n\n# direct methods\n.method public constructor <init>(Ljava/lang/String;)V\n    .registers 2\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    iput-object p1, p0, Lcom/android/systemui/plugins/ControllerStorage$ControllerStorageKey;->mDisplayName:Ljava/lang/String;\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public toString()Ljava/lang/String;\n    .registers 2\n    .annotation build Lorg/jetbrains/annotations/NotNull;\n    .end annotation\n\n    iget-object v0, p0, Lcom/android/systemui/plugins/ControllerStorage$ControllerStorageKey;->mDisplayName:Ljava/lang/String;\n\n    return-object v0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
