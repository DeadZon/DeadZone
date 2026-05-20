"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/policy/NetworkSpeedController$WorkHandler.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/policy/NetworkSpeedController$WorkHandler.smali'
CLASS_FALLBACK_NAMES = ['NetworkSpeedController$WorkHandler.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_policy_NetworkSpeedController',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/statusbar/policy/NetworkSpeedController$WorkHandler;\n.super Landroid/os/Handler;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x2\n    name = "WorkHandler"\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n\n# direct methods\n.method public constructor <init>(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;Landroid/os/Looper;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$WorkHandler;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-direct {p0, p2}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public handleMessage(Landroid/os/Message;)V\n    .registers 4\n\n    iget v0, p1, Landroid/os/Message;->what:I\n\n    const v1, 0x30d41\n\n    if-ne v0, v1, :cond_0\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/NetworkSpeedController$WorkHandler;->this$0:Lcom/android/systemui/statusbar/policy/NetworkSpeedController;\n\n    invoke-static {v0}, Lcom/android/systemui/statusbar/policy/NetworkSpeedController;->access$900(Lcom/android/systemui/statusbar/policy/NetworkSpeedController;)V\n\n    :cond_0\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
