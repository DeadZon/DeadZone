"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/newstatusbar/policy/Shake$2.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/newstatusbar/policy/Shake$2.smali'
CLASS_FALLBACK_NAMES = ['Shake$2.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_newstatusbar_policy_Shake$2',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/newstatusbar/policy/Shake$2;\n.super Landroid/content/BroadcastReceiver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingMethod;\n    value = Lcom/android/systemui/newstatusbar/policy/Shake;-><init>(Landroid/content/Context;)V\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/newstatusbar/policy/Shake;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/newstatusbar/policy/Shake;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/newstatusbar/policy/Shake$2;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;\n\n    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V\n    .registers 6\n\n    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;\n\n    move-result-object v0\n\n    const-string v1, "android.intent.action.SCREEN_ON"\n\n    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    if-eqz v1, :cond_0\n\n    const/4 v1, 0x1\n\n    goto :goto_0\n\n    :cond_0\n    const-string v1, "android.intent.action.SCREEN_OFF"\n\n    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v1\n\n    if-nez v1, :cond_1\n\n    return-void\n\n    :cond_1\n    const/4 v1, 0x0\n\n    :goto_0\n    iget-object v2, p0, Lcom/android/systemui/newstatusbar/policy/Shake$2;->this$0:Lcom/android/systemui/newstatusbar/policy/Shake;\n\n    invoke-virtual {v2, v1}, Lcom/android/systemui/newstatusbar/policy/Shake;->onScreenOnOffChanged(Z)V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
