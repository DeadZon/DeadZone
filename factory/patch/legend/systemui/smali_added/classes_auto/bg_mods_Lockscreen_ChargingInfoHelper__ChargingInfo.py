"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'bg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo.smali'
CLASS_FALLBACK_NAMES = ['ChargingInfoHelper$ChargingInfo.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class final Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;
.super Ljava/lang/Object;


# instance fields
.field current:D

.field power:D

.field temp:D

.field voltage:D


# direct methods
.method private constructor <init>()V
    .registers 3

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    const-wide/16 v0, 0x0

    iput-wide v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->temp:D

    iput-wide v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->current:D

    iput-wide v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->voltage:D

    iput-wide v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->power:D

    return-void
.end method

.method synthetic constructor <init>(Lcom/android/keyguard/injector/KeyguardIndicationHelper$1;)V
    .registers 2

    invoke-direct {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;-><init>()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_bg_mods_Lockscreen_ChargingInfoHelper_ChargingInfo',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
