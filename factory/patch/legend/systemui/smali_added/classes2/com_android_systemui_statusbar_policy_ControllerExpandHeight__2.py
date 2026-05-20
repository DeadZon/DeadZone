"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/policy/ControllerExpandHeight$2.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/policy/ControllerExpandHeight$2.smali'
CLASS_FALLBACK_NAMES = ['ControllerExpandHeight$2.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_policy_ControllerExpandHeight',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$2;\n.super Ljava/lang/Object;\n\n# interfaces\n.implements Lcom/android/systemui/statusbar/policy/ConfigurationController$ConfigurationListener;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;-><init>()V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$2;->this$0:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onConfigChanged(Landroid/content/res/Configuration;)V\n    .registers 5\n\n    const/4 v0, 0x1\n\n    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$2;->this$0:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;\n\n    iget v2, p1, Landroid/content/res/Configuration;->orientation:I\n\n    if-ne v2, v0, :cond_0\n\n    :goto_0\n    invoke-static {v1, v0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->access$102(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;Z)Z\n\n    iget-object v0, p0, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight$2;->this$0:Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;\n\n    invoke-static {v0}, Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;->access$200(Lcom/android/systemui/statusbar/policy/ControllerExpandHeight;)V\n\n    return-void\n\n    :cond_0\n    const/4 v0, 0x0\n\n    goto :goto_0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
