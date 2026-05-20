"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'bg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver.smali'
CLASS_FALLBACK_NAMES = ['ChargingInfoHelper$ScreenReceiver.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;
.super Landroid/content/BroadcastReceiver;


# instance fields
.field final synthetic this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;


# direct methods
.method constructor <init>(Lbg/mods/Lockscreen/ChargingInfoHelper;)V
    .registers 2

    iput-object p1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;

    invoke-direct {p0}, Landroid/content/BroadcastReceiver;-><init>()V

    return-void
.end method


# virtual methods
.method public onReceive(Landroid/content/Context;Landroid/content/Intent;)V
    .registers 3

    invoke-virtual {p2}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object p1

    const-string p2, "android.intent.action.SCREEN_ON"

    invoke-virtual {p2, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p2

    if-eqz p2, :cond_17

    iget-object p1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;

    invoke-static {p1}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$000(Lbg/mods/Lockscreen/ChargingInfoHelper;)V

    iget-object p0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;

    invoke-static {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$300(Lbg/mods/Lockscreen/ChargingInfoHelper;)V

    goto :goto_24

    :cond_17
    const-string p2, "android.intent.action.SCREEN_OFF"

    invoke-virtual {p2, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_24

    iget-object p0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;

    invoke-static {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$400(Lbg/mods/Lockscreen/ChargingInfoHelper;)V

    :cond_24
    :goto_24
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_bg_mods_Lockscreen_ChargingInfoHelper_ScreenReceiver',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
