"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService$1.smali'
CLASS_FALLBACK_NAMES = ['EdgeScreenService$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_phone_MyModifiedUI_EdgeScreen',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService$1;\n.super Landroid/database/ContentObserver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;Landroid/os/Handler;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService$1;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;\n\n    invoke-direct {p0, p2}, Landroid/database/ContentObserver;-><init>(Landroid/os/Handler;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onChange(Z)V\n    .registers 3\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService$1;->this$0:Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;\n\n    invoke-static {v0}, Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;->access$000(Lcom/android/systemui/statusbar/phone/MyModifiedUI/EdgeScreenService;)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
