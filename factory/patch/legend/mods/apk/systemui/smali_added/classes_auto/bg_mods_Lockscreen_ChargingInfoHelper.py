"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'bg/mods/Lockscreen/ChargingInfoHelper.smali'
CLASS_FALLBACK_NAMES = ['ChargingInfoHelper.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final Lbg/mods/Lockscreen/ChargingInfoHelper;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;,
        Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;,
        Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;
    }
.end annotation


# static fields
.field private static sInstance:Lbg/mods/Lockscreen/ChargingInfoHelper;


# instance fields
.field private final mContext:Landroid/content/Context;

.field private final mHandler:Landroid/os/Handler;

.field private final mKeyguardIndicationController:Lcom/android/systemui/statusbar/KeyguardIndicationController;

.field private final mRefreshInterval:I

.field private final mScreenOnOffReceiver:Landroid/content/BroadcastReceiver;

.field private final mUpdateRunnable:Ljava/lang/Runnable;


# direct methods
.method private constructor <init>(Landroid/content/Context;Lcom/android/systemui/statusbar/KeyguardIndicationController;)V
    .registers 6

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mContext:Landroid/content/Context;

    iput-object p2, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mKeyguardIndicationController:Lcom/android/systemui/statusbar/KeyguardIndicationController;

    new-instance v0, Landroid/os/Handler;

    invoke-direct {v0}, Landroid/os/Handler;-><init>()V

    iput-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mHandler:Landroid/os/Handler;

    new-instance v0, Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;

    invoke-direct {v0, p0}, Lbg/mods/Lockscreen/ChargingInfoHelper$UpdateRunnable;-><init>(Lbg/mods/Lockscreen/ChargingInfoHelper;)V

    iput-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mUpdateRunnable:Ljava/lang/Runnable;

    new-instance v0, Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;

    invoke-direct {v0, p0}, Lbg/mods/Lockscreen/ChargingInfoHelper$ScreenReceiver;-><init>(Lbg/mods/Lockscreen/ChargingInfoHelper;)V

    iput-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mScreenOnOffReceiver:Landroid/content/BroadcastReceiver;

    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    const-string v1, "android.intent.action.SCREEN_ON"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v1, "android.intent.action.SCREEN_OFF"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    iget-object v1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mScreenOnOffReceiver:Landroid/content/BroadcastReceiver;

    invoke-virtual {p1, v1, v0}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "bg_refresh_interval"

    const/16 v2, 0x7d0

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    iput v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mRefreshInterval:I

    return-void
.end method

.method static synthetic access$000(Lbg/mods/Lockscreen/ChargingInfoHelper;)V
    .registers 1

    invoke-direct {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->bg_updateChargingInfo()V

    return-void
.end method

.method static synthetic access$100(Lbg/mods/Lockscreen/ChargingInfoHelper;)Landroid/os/Handler;
    .registers 1

    iget-object p0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mHandler:Landroid/os/Handler;

    return-object p0
.end method

.method static synthetic access$200(Lbg/mods/Lockscreen/ChargingInfoHelper;)I
    .registers 1

    iget p0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mRefreshInterval:I

    return p0
.end method

.method static synthetic access$300(Lbg/mods/Lockscreen/ChargingInfoHelper;)V
    .registers 1

    invoke-direct {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->startPeriodicUpdates()V

    return-void
.end method

.method static synthetic access$400(Lbg/mods/Lockscreen/ChargingInfoHelper;)V
    .registers 1

    invoke-direct {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->stopPeriodicUpdates()V

    return-void
.end method

.method private bg_formatChargingInfo(Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;Ljava/lang/CharSequence;)Ljava/lang/String;
    .registers 16

    const/4 v6, 0x1

    const/4 v5, 0x0

    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v11

    const-string v0, "bg_show_temp"

    invoke-static {v11, v0, v6}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    const-string v1, "bg_show_ampere"

    invoke-static {v11, v1, v6}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    const-string v2, "bg_show_voltage"

    invoke-static {v11, v2, v5}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v2

    const-string v3, "bg_show_power"

    invoke-static {v11, v3, v6}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v3

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const/4 v12, 0x0

    if-eqz v0, :cond_3c

    const-string v0, "%.1f ℃"

    new-array v7, v6, [Ljava/lang/Object;

    iget-wide v8, p1, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->temp:D

    invoke-static {v8, v9}, Ljava/lang/Double;->valueOf(D)Ljava/lang/Double;

    move-result-object v8

    aput-object v8, v7, v5

    invoke-static {v0, v7}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/4 v12, 0x1

    :cond_3c
    invoke-direct {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->shouldShowOriginalChargingText()Z

    move-result v0

    if-eqz v0, :cond_4c

    if-eqz v12, :cond_49

    const-string v0, " · "

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_49
    invoke-virtual {v4, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/CharSequence;)Ljava/lang/StringBuilder;

    :cond_4c
    const-string p2, "\n"

    invoke-virtual {v4, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/4 p2, 0x0

    if-eqz v1, :cond_69

    const-string v0, "%.2f A"

    new-array v7, v6, [Ljava/lang/Object;

    iget-wide v8, p1, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->current:D

    invoke-static {v8, v9}, Ljava/lang/Double;->valueOf(D)Ljava/lang/Double;

    move-result-object v8

    aput-object v8, v7, v5

    invoke-static {v0, v7}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    add-int/lit8 p2, p2, 0x1

    :cond_69
    if-eqz v2, :cond_87

    if-lez p2, :cond_72

    const-string v0, " · "

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_72
    const-string v0, "%.1f V"

    new-array v1, v6, [Ljava/lang/Object;

    iget-wide v7, p1, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->voltage:D

    invoke-static {v7, v8}, Ljava/lang/Double;->valueOf(D)Ljava/lang/Double;

    move-result-object v7

    aput-object v7, v1, v5

    invoke-static {v0, v1}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    add-int/lit8 p2, p2, 0x1

    :cond_87
    if-eqz v3, :cond_a3

    if-lez p2, :cond_90

    const-string p2, " · "

    invoke-virtual {v4, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_90
    const-string p2, "%.2f W"

    new-array v0, v6, [Ljava/lang/Object;

    iget-wide v1, p1, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->power:D

    invoke-static {v1, v2}, Ljava/lang/Double;->valueOf(D)Ljava/lang/Double;

    move-result-object p0

    aput-object p0, v0, v5

    invoke-static {p2, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v4, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_a3
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method

.method private bg_readChargingInfo()Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;
    .registers 7

    new-instance v0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;

    const/4 v1, 0x0

    invoke-direct {v0, v1}, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;-><init>(Lcom/android/keyguard/injector/KeyguardIndicationHelper$1;)V

    :try_start_6
    const-string v1, "/sys/class/power_supply/battery/temp"

    invoke-direct {p0, v1}, Lbg/mods/Lockscreen/ChargingInfoHelper;->readSysfsFile(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    if-eqz v1, :cond_17

    invoke-static {v1}, Ljava/lang/Double;->parseDouble(Ljava/lang/String;)D

    move-result-wide v1

    const-wide/high16 v3, 0x4024000000000000L  # 10.0

    div-double/2addr v1, v3

    iput-wide v1, v0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->temp:D

    :cond_17
    const-string v1, "/sys/class/power_supply/battery/current_now"

    invoke-direct {p0, v1}, Lbg/mods/Lockscreen/ChargingInfoHelper;->readSysfsFile(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    const-wide v2, 0x412e848000000000L  # 1000000.0

    if-eqz v1, :cond_2f

    invoke-static {v1}, Ljava/lang/Double;->parseDouble(Ljava/lang/String;)D

    move-result-wide v4

    invoke-static {v4, v5}, Ljava/lang/Math;->abs(D)D

    move-result-wide v4

    div-double/2addr v4, v2

    iput-wide v4, v0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->current:D

    :cond_2f
    const-string v1, "/sys/class/power_supply/battery/voltage_now"

    invoke-direct {p0, v1}, Lbg/mods/Lockscreen/ChargingInfoHelper;->readSysfsFile(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    if-eqz p0, :cond_3e

    invoke-static {p0}, Ljava/lang/Double;->parseDouble(Ljava/lang/String;)D

    move-result-wide v4

    div-double/2addr v4, v2

    iput-wide v4, v0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->voltage:D

    :cond_3e
    iget-wide v1, v0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->current:D

    iget-wide v3, v0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->voltage:D

    mul-double/2addr v1, v3

    iput-wide v1, v0, Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;->power:D
    :try_end_45
    .catch Ljava/lang/Exception; {:try_start_6 .. :try_end_45} :catch_45

    :catch_45
    return-object v0
.end method

.method private bg_updateChargingInfo()V
    .registers 6

    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mKeyguardIndicationController:Lcom/android/systemui/statusbar/KeyguardIndicationController;

    iget-boolean v1, v0, Lcom/android/systemui/statusbar/KeyguardIndicationController;->mPowerPluggedIn:Z

    if-nez v1, :cond_7

    return-void

    :cond_7
    iget-object v1, v0, Lcom/android/systemui/statusbar/KeyguardIndicationController;->mLockScreenIndicationView:Lcom/android/systemui/statusbar/phone/KeyguardIndicationTextView;

    if-nez v1, :cond_c

    return-void

    :cond_c
    iget-object v2, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    const-string v3, "bg_extra_charging_info"

    const/4 v4, 0x0

    invoke-static {v2, v3, v4}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v2

    if-nez v2, :cond_1c

    return-void

    :cond_1c
    iget-object v2, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    const-string v3, "bg_charging_info_text_size"

    const/high16 v4, 0x41200000  # 10.0f

    invoke-static {v2, v3, v4}, Landroid/provider/Settings$System;->getFloat(Landroid/content/ContentResolver;Ljava/lang/String;F)F

    move-result v2

    invoke-virtual {v1, v2}, Landroid/widget/TextView;->setTextSize(F)V

    iget-object v2, v0, Lcom/android/systemui/statusbar/KeyguardIndicationController;->mContext:Landroid/content/Context;

    iget v3, v0, Lcom/android/systemui/statusbar/KeyguardIndicationController;->mChargingSpeed:I

    iget v0, v0, Lcom/android/systemui/statusbar/KeyguardIndicationController;->mBatteryLevel:I

    invoke-direct {p0, v2, v3, v0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->getBaseChargingString(Landroid/content/Context;II)Ljava/lang/String;

    move-result-object v0

    invoke-direct {p0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->bg_readChargingInfo()Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;

    move-result-object v2

    invoke-direct {p0, v2, v0}, Lbg/mods/Lockscreen/ChargingInfoHelper;->bg_formatChargingInfo(Lbg/mods/Lockscreen/ChargingInfoHelper$ChargingInfo;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object p0

    invoke-virtual {v1, p0}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    return-void
.end method

.method private getBaseChargingString(Landroid/content/Context;II)Ljava/lang/String;
    .registers 6

    const/16 v0, 0x64

    if-ne p3, v0, :cond_b

    const-string v0, "keyguard_charged"

    invoke-static {p1, v0}, Landroid/Utils/Utils;->getString(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    return-object p0

    :cond_b
    const/4 v0, 0x1

    new-array v0, v0, [Ljava/lang/Object;

    const/4 v1, 0x0

    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p3

    aput-object p3, v0, v1

    const/4 p3, 0x2

    if-ne p2, p3, :cond_1f

    const-string p2, "keyguard_charging_quick_and_level_tip"

    invoke-static {p1, p2}, Landroid/Utils/Utils;->getString(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    goto :goto_2e

    :cond_1f
    if-nez p2, :cond_28

    const-string p2, "keyguard_charging_normal_and_level_tip"

    invoke-static {p1, p2}, Landroid/Utils/Utils;->getString(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    goto :goto_2e

    :cond_28
    const-string p2, "keyguard_charging_super_quick_and_level_tip"

    invoke-static {p1, p2}, Landroid/Utils/Utils;->getString(Landroid/content/Context;Ljava/lang/String;)Ljava/lang/String;

    move-result-object p0

    :goto_2e
    return-object p0
.end method

.method public static getInstance()Lbg/mods/Lockscreen/ChargingInfoHelper;
    .registers 1

    sget-object v0, Lbg/mods/Lockscreen/ChargingInfoHelper;->sInstance:Lbg/mods/Lockscreen/ChargingInfoHelper;

    return-object v0
.end method

.method public static init(Landroid/content/Context;Lcom/android/systemui/statusbar/KeyguardIndicationController;)V
    .registers 4

    sget-object v0, Lbg/mods/Lockscreen/ChargingInfoHelper;->sInstance:Lbg/mods/Lockscreen/ChargingInfoHelper;

    if-nez v0, :cond_b

    new-instance v0, Lbg/mods/Lockscreen/ChargingInfoHelper;

    invoke-direct {v0, p0, p1}, Lbg/mods/Lockscreen/ChargingInfoHelper;-><init>(Landroid/content/Context;Lcom/android/systemui/statusbar/KeyguardIndicationController;)V

    sput-object v0, Lbg/mods/Lockscreen/ChargingInfoHelper;->sInstance:Lbg/mods/Lockscreen/ChargingInfoHelper;

    :cond_b
    return-void
.end method

.method private readSysfsFile(Ljava/lang/String;)Ljava/lang/String;
    .registers 4

    const/4 v0, 0x0

    :try_start_1
    new-instance v1, Ljava/io/BufferedReader;

    new-instance p0, Ljava/io/FileReader;

    invoke-direct {p0, p1}, Ljava/io/FileReader;-><init>(Ljava/lang/String;)V

    invoke-direct {v1, p0}, Ljava/io/BufferedReader;-><init>(Ljava/io/Reader;)V

    invoke-virtual {v1}, Ljava/io/BufferedReader;->readLine()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v1}, Ljava/io/BufferedReader;->close()V
    :try_end_12
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_12} :catch_12

    :catch_12
    return-object v0
.end method

.method private shouldShowOriginalChargingText()Z
    .registers 4

    const/4 v2, 0x0

    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "bg_hide_original_charging_text"

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    if-eqz v0, :cond_11

    const/4 v0, 0x1

    :goto_10
    return v0

    :cond_11
    const/4 v0, 0x0

    goto :goto_10
.end method

.method private startPeriodicUpdates()V
    .registers 5

    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mUpdateRunnable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mUpdateRunnable:Ljava/lang/Runnable;

    iget v2, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mRefreshInterval:I

    int-to-long v2, v2

    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void
.end method

.method private stopPeriodicUpdates()V
    .registers 3

    iget-object v0, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mHandler:Landroid/os/Handler;

    iget-object v1, p0, Lbg/mods/Lockscreen/ChargingInfoHelper;->mUpdateRunnable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_bg_mods_Lockscreen_ChargingInfoHelper',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
