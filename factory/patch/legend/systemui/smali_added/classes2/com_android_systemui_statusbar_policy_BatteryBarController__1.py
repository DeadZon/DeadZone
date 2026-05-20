"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/policy/BatteryBarController$1.smali
DEX group    : classes2
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/policy/BatteryBarController$1.smali'
CLASS_FALLBACK_NAMES = ['BatteryBarController$1.smali']
DEX_GROUP            = 'classes2'

PATCHES = [
    {
        'id':          'class_add_com_android_systemui_statusbar_policy_BatteryBarController$1',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class Lcom/android/systemui/statusbar/policy/BatteryBarController$1;\n.super Landroid/content/BroadcastReceiver;\n\n\n# annotations\n.annotation system Ldalvik/annotation/EnclosingClass;\n    value = Lcom/android/systemui/statusbar/policy/BatteryBarController;\n.end annotation\n\n.annotation system Ldalvik/annotation/InnerClass;\n    accessFlags = 0x0\n    name = null\n.end annotation\n\n\n# instance fields\n.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;\n\n\n# direct methods\n.method constructor <init>(Lcom/android/systemui/statusbar/policy/BatteryBarController;)V\n    .registers 2\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;\n\n    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V\n    .registers 8\n\n    const/4 v1, 0x0\n\n    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;\n\n    move-result-object v0\n\n    const-string v2, "android.intent.action.BATTERY_CHANGED"\n\n    invoke-virtual {v2, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z\n\n    move-result v2\n\n    if-eqz v2, :cond_1\n\n    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;\n\n    const-string v3, "level"\n\n    invoke-virtual {p2, v3, v1}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I\n\n    move-result v3\n\n    invoke-static {v2, v3}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->access$102(Lcom/android/systemui/statusbar/policy/BatteryBarController;I)I\n\n    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;\n\n    const-string v3, "status"\n\n    invoke-virtual {p2, v3, v1}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I\n\n    move-result v3\n\n    const/4 v4, 0x2\n\n    if-ne v3, v4, :cond_0\n\n    const/4 v1, 0x1\n\n    :cond_0\n    invoke-static {v2, v1}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->access$202(Lcom/android/systemui/statusbar/policy/BatteryBarController;Z)Z\n\n    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBarController$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBarController;\n\n    invoke-static {v1}, Lcom/android/systemui/statusbar/policy/BatteryBarController;->access$100(Lcom/android/systemui/statusbar/policy/BatteryBarController;)I\n\n    move-result v1\n\n    invoke-static {p1, v1}, Lcom/android/systemui/statusbar/policy/Prefs;->setLastBatteryLevel(Landroid/content/Context;I)V\n\n    :cond_1\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
