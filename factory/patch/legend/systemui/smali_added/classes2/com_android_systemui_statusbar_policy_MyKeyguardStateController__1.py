"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/policy/MyKeyguardStateController$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/policy/MyKeyguardStateController$1.smali'
CLASS_FALLBACK_NAMES = ['MyKeyguardStateController$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_policy_MyKeyguardStateControl',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$1;\n.super Landroid/os/Handler;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$1;->this$0:Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;\n\n    invoke-direct {p0}, Landroid/os/Handler;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public handleMessage(Landroid/os/Message;)V\n    .registers 5\n    .param p1  # Landroid/os/Message;\n        .annotation build Landroidx/annotation/NonNull;\n        .end annotation\n    .end param\n\n    const/4 v0, 0x1\n\n    iget v1, p1, Landroid/os/Message;->what:I\n\n    const/16 v2, 0x65\n\n    if-ne v1, v2, :cond_0\n\n    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController$1;->this$0:Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;\n\n    iget v2, p1, Landroid/os/Message;->arg1:I\n\n    if-ne v2, v0, :cond_1\n\n    :goto_0\n    invoke-static {v1, v0}, Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;->access$000(Lcom/android/systemui/statusbar/policy/MyKeyguardStateController;Z)V\n\n    :cond_0\n    return-void\n\n    :cond_1\n    const/4 v0, 0x0\n\n    goto :goto_0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
