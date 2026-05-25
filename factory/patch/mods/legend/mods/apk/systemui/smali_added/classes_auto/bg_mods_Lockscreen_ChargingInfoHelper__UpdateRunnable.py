"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'bg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable.smali'
CLASS_FALLBACK_NAMES = ['ChargingInfoHelper$UpdateRunnable.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# instance fields
.field final synthetic this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;


# direct methods
.method constructor <init>(Lbg/mods/Lockscreen/ChargingInfoHelper;)V
    .registers 2

    iput-object p1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 5

    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;

    invoke-static {v0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$000(Lbg/mods/Lockscreen/ChargingInfoHelper;)V

    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;

    invoke-static {v0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$100(Lbg/mods/Lockscreen/ChargingInfoHelper;)Landroid/os/Handler;

    move-result-object v1

    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;->this$0:Lbg/mods/Lockscreen/ChargingInfoHelper;

    invoke-static {v0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->access$200(Lbg/mods/Lockscreen/ChargingInfoHelper;)I

    move-result v0

    int-to-long v2, v0

    invoke-virtual {v1, p0, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_bg_mods_Lockscreen_ChargingInfoHelper_UpdateRunnable',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
