"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/policy/Shake.smali'
CLASS_FALLBACK_NAMES = ['Shake.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/policy/Shake;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;,
        Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;
    }
.end annotation


# static fields
.field private static final SHAKE_COUNT_RESET_TIME_MS:I = 0xbb8

.field private static final SHAKE_SLOP_TIME_MS:I = 0x1f4

.field private static final SHAKE_THRESHOLD_GRAVITY:F = 2.7f

.field private static final TAG:Ljava/lang/String;


# instance fields
.field private final mAccelerometer:Landroid/hardware/Sensor;

.field public mContext:Landroid/content/Context;

.field public mHandler:Landroid/os/Handler;

.field private mIsScreenOnOffListenerRegistered:Z

.field private mIsSensorListenerRegistered:Z

.field private mListener:Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;

.field private final mScreenOnOffChangeListener:Landroid/content/BroadcastReceiver;

.field private final mSensorManager:Landroid/hardware/SensorManager;

.field private mShakeCount:I

.field private final mShakeDetector:Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;

.field private mShakeTimestamp:J


# direct methods
.method static constructor <clinit>()V
    .registers 2

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-class v1, Lcom/android/systemui/newstatusbar/policy/Shake;

    invoke-virtual {v1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "_log_tag"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/newstatusbar/policy/Shake;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;)V
    .registers 5

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    const-class v0, Landroid/hardware/SensorManager;

    invoke-virtual {p1, v0}, Landroid/content/Context;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/hardware/SensorManager;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mSensorManager:Landroid/hardware/SensorManager;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Landroid/hardware/SensorManager;->getDefaultSensor(I)Landroid/hardware/Sensor;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mAccelerometer:Landroid/hardware/Sensor;

    new-instance v0, Landroid/os/Handler;

    invoke-direct {v0}, Landroid/os/Handler;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mHandler:Landroid/os/Handler;

    new-instance v0, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mHandler:Landroid/os/Handler;

    invoke-direct {v0, p0, v1}, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;-><init>(Lcom/android/systemui/newstatusbar/policy/Shake;Landroid/os/Handler;)V

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/policy/Shake$SettingsObserver;->observe()V

    new-instance v1, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;

    invoke-direct {v1}, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;-><init>()V

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mShakeDetector:Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;

    new-instance v2, Lcom/android/systemui/newstatusbar/policy/Shake$1;

    invoke-direct {v2, p0}, Lcom/android/systemui/newstatusbar/policy/Shake$1;-><init>(Lcom/android/systemui/newstatusbar/policy/Shake;)V

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->setOnShakeListener(Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;)V

    new-instance v1, Lcom/android/systemui/newstatusbar/policy/Shake$2;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/policy/Shake$2;-><init>(Lcom/android/systemui/newstatusbar/policy/Shake;)V

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mScreenOnOffChangeListener:Landroid/content/BroadcastReceiver;

    const/4 v1, 0x0

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mIsScreenOnOffListenerRegistered:Z

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mIsSensorListenerRegistered:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake;->onAttachedToWindow()V

    return-void
.end method

.method static synthetic access$000()Ljava/lang/String;
    .registers 1

    sget-object v0, Lcom/android/systemui/newstatusbar/policy/Shake;->TAG:Ljava/lang/String;

    return-object v0
.end method


# virtual methods
.method protected onAttachedToWindow()V
    .registers 3

    goto/32 :goto_29

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake;->registerOnOffScreenListener()V

    goto/32 :goto_14

    nop

    :goto_b
    return-void

    :goto_c
    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    goto/32 :goto_20

    nop

    :goto_14
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake;->registerSensorListener()V

    :goto_17
    goto/32 :goto_b

    nop

    :goto_1b
    const/4 v1, 0x1

    goto/32 :goto_c

    nop

    :goto_20
    if-gtz v0, :cond_25

    goto/32 :goto_17

    :cond_25
    goto/32 :goto_4

    nop

    :goto_29
    const-string v0, "shake_mobile"

    goto/32 :goto_1b

    nop
.end method

.method protected onDetachedFromWindow()V
    .registers 1

    goto/32 :goto_b

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake;->unregisterSensorListener()V

    goto/32 :goto_12

    nop

    :goto_b
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake;->unregisterOnOffScreenListener()V

    goto/32 :goto_4

    nop

    :goto_12
    return-void
.end method

.method public onScreenOnOffChanged(Z)V
    .registers 2

    if-eqz p1, :cond_6

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake;->registerSensorListener()V

    goto :goto_9

    :cond_6
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/Shake;->unregisterSensorListener()V

    :goto_9
    return-void
.end method

.method public registerOnOffScreenListener()V
    .registers 5

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mIsScreenOnOffListenerRegistered:Z

    if-eqz v0, :cond_5

    return-void

    :cond_5
    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    const-string v1, "android.intent.action.SCREEN_ON"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v1, "android.intent.action.SCREEN_OFF"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mScreenOnOffChangeListener:Landroid/content/BroadcastReceiver;

    const/4 v3, 0x2

    invoke-virtual {v1, v2, v0, v3}, Landroid/content/Context;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;I)Landroid/content/Intent;

    const/4 v1, 0x1

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mIsScreenOnOffListenerRegistered:Z

    return-void
.end method

.method public registerSensorListener()V
    .registers 5

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mIsSensorListenerRegistered:Z

    if-eqz v0, :cond_5

    return-void

    :cond_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mSensorManager:Landroid/hardware/SensorManager;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mShakeDetector:Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mAccelerometer:Landroid/hardware/Sensor;

    const/4 v3, 0x2

    invoke-virtual {v0, v1, v2, v3}, Landroid/hardware/SensorManager;->registerListener(Landroid/hardware/SensorEventListener;Landroid/hardware/Sensor;I)Z

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mIsSensorListenerRegistered:Z

    return-void
.end method

.method public unregisterOnOffScreenListener()V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mIsScreenOnOffListenerRegistered:Z

    if-eqz v0, :cond_e

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mContext:Landroid/content/Context;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mScreenOnOffChangeListener:Landroid/content/BroadcastReceiver;

    invoke-virtual {v0, v1}, Landroid/content/Context;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mIsScreenOnOffListenerRegistered:Z

    :cond_e
    return-void
.end method

.method public unregisterSensorListener()V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mIsSensorListenerRegistered:Z

    if-eqz v0, :cond_e

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mSensorManager:Landroid/hardware/SensorManager;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mShakeDetector:Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;

    invoke-virtual {v0, v1}, Landroid/hardware/SensorManager;->unregisterListener(Landroid/hardware/SensorEventListener;)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/policy/Shake;->mIsSensorListenerRegistered:Z

    :cond_e
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_policy_Shake',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
