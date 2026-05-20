"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : bg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo.smali
DEX group    : classes4
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'bg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo.smali'
CLASS_FALLBACK_NAMES = ['ChargingInfoHelper$ChargingInfo.smali']
DEX_GROUP            = 'classes4'

PATCHES = [
    {
        'id':          'class_add_bg_mods_Lockscreen_ChargingInfoHelper$ChargingInfo',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class final Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;\n.super Ljava/lang/Object;\n\n\n# instance fields\n.field current:D\n\n.field power:D\n\n.field temp:D\n\n.field voltage:D\n\n\n# direct methods\n.method private constructor <init>()V\n    .registers 3\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    const-wide/16 v0, 0x0\n\n    iput-wide v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->temp:D\n\n    iput-wide v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->current:D\n\n    iput-wide v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->voltage:D\n\n    iput-wide v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->power:D\n\n    return-void\n.end method\n\n.method synthetic constructor <init>(Lcom/android/keyguard/injector/KeyguardIndicationHelper$1;)V\n    .registers 2\n\n    invoke-direct {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;-><init>()V\n\n    return-void\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
