"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/statusbar/policy/BatteryBar$1.smali'
CLASS_FALLBACK_NAMES = ['BatteryBar$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/statusbar/policy/BatteryBar$1;
.super Landroid/content/BroadcastReceiver;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/statusbar/policy/BatteryBar;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;


# direct methods
.method constructor <init>(Lcom/android/systemui/statusbar/policy/BatteryBar;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V

    return-void
.end method


# virtual methods
.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .registers 9

    const/16 v5, 0x64

    const/4 v1, 0x0

    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object v0

    const-string/jumbo v2, "android.intent.action.BATTERY_CHANGED"

    invoke-virtual {v2, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_53

    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    const-string/jumbo v3, "level"

    invoke-virtual {p2, v3, v1}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I

    move-result v3

    invoke-static {v2, v3}, Lcom/android/systemui/statusbar/policy/BatteryBar;->-set1(Lcom/android/systemui/statusbar/policy/BatteryBar;I)I

    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    const-string/jumbo v3, "status"

    invoke-virtual {p2, v3, v1}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I

    move-result v3

    const/4 v4, 0x2

    if-ne v3, v4, :cond_29

    const/4 v1, 0x1

    :cond_29
    invoke-static {v2, v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->-set0(Lcom/android/systemui/statusbar/policy/BatteryBar;Z)Z

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-static {v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->-get0(Lcom/android/systemui/statusbar/policy/BatteryBar;)Z

    move-result v1

    if-eqz v1, :cond_4d

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-static {v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->-get1(Lcom/android/systemui/statusbar/policy/BatteryBar;)I

    move-result v1

    if-ge v1, v5, :cond_4d

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-virtual {v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->start()V

    :goto_41
    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    iget-object v2, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-static {v2}, Lcom/android/systemui/statusbar/policy/BatteryBar;->-get1(Lcom/android/systemui/statusbar/policy/BatteryBar;)I

    move-result v2

    invoke-static {v1, v2}, Lcom/android/systemui/statusbar/policy/BatteryBar;->-wrap0(Lcom/android/systemui/statusbar/policy/BatteryBar;I)V

    :cond_4c
    :goto_4c
    return-void

    :cond_4d
    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-virtual {v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->stop()V

    goto :goto_41

    :cond_53
    const-string/jumbo v1, "android.intent.action.SCREEN_OFF"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_62

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-virtual {v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->stop()V

    goto :goto_4c

    :cond_62
    const-string/jumbo v1, "android.intent.action.SCREEN_ON"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_4c

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-static {v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->-get0(Lcom/android/systemui/statusbar/policy/BatteryBar;)Z

    move-result v1

    if-eqz v1, :cond_4c

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-static {v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->-get1(Lcom/android/systemui/statusbar/policy/BatteryBar;)I

    move-result v1

    if-ge v1, v5, :cond_4c

    iget-object v1, p0, Lcom/android/systemui/statusbar/policy/BatteryBar$1;->this$0:Lcom/android/systemui/statusbar/policy/BatteryBar;

    invoke-virtual {v1}, Lcom/android/systemui/statusbar/policy/BatteryBar;->start()V

    goto :goto_4c
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_statusbar_policy_BatteryBar_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
