"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/policy/Shake$ShakeDetector.smali'
CLASS_FALLBACK_NAMES = ['Shake$ShakeDetector.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/hardware/SensorEventListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/policy/Shake;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x9
    name = "ShakeDetector"
.end annotation

.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;
    }
.end annotation


# instance fields
.field private mListener:Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;

.field private mShakeCount:I

.field private mShakeTimestamp:J


# direct methods
.method constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onAccuracyChanged(Landroid/hardware/Sensor;I)V
    .registers 3

    return-void
.end method

.method public onSensorChanged(Landroid/hardware/SensorEvent;)V
    .registers 20

    move-object/from16 v0, p0

    move-object/from16 v1, p1

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->mListener:Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;

    if-eqz v2, :cond_7d

    iget-object v2, v1, Landroid/hardware/SensorEvent;->values:[F

    const/4 v3, 0x0

    aget v2, v2, v3

    iget-object v4, v1, Landroid/hardware/SensorEvent;->values:[F

    const/4 v5, 0x1

    aget v4, v4, v5

    iget-object v6, v1, Landroid/hardware/SensorEvent;->values:[F

    const/4 v7, 0x2

    aget v6, v6, v7

    const v7, 0x411ce80a

    div-float v8, v2, v7

    div-float v9, v4, v7

    div-float v7, v6, v7

    mul-float v10, v8, v8

    mul-float v11, v9, v9

    add-float/2addr v10, v11

    mul-float v11, v7, v7

    add-float/2addr v10, v11

    float-to-double v10, v10

    invoke-static {v10, v11}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide v10

    const-wide v12, 0x40059999a0000000L  # 2.700000047683716

    cmpl-double v12, v10, v12

    if-lez v12, :cond_7d

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v12

    iget-wide v14, v0, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->mShakeTimestamp:J

    const-wide/16 v16, 0x1f4

    add-long v16, v14, v16

    cmp-long v16, v16, v12

    if-lez v16, :cond_45

    return-void

    :cond_45
    const-wide/16 v16, 0xbb8

    add-long v14, v14, v16

    cmp-long v14, v14, v12

    if-gez v14, :cond_4f

    iput v3, v0, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->mShakeCount:I

    :cond_4f
    iput-wide v12, v0, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->mShakeTimestamp:J

    iget v3, v0, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->mShakeCount:I

    add-int/2addr v3, v5

    iput v3, v0, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->mShakeCount:I

    iget-object v3, v0, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->mListener:Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;

    iget v5, v0, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->mShakeCount:I

    invoke-static {}, Lcom/android/systemui/newstatusbar/policy/Shake;->access$000()Ljava/lang/String;

    move-result-object v14

    new-instance v15, Ljava/lang/StringBuilder;

    invoke-direct {v15}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "mShakeCount ="

    invoke-virtual {v15, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    iget v15, v0, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->mShakeCount:I

    invoke-static {v15}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v15

    invoke-virtual {v1, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v14, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    invoke-interface {v3, v5}, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;->onShake(I)V

    :cond_7d
    return-void
.end method

.method public setOnShakeListener(Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector;->mListener:Lcom/android/systemui/newstatusbar/policy/Shake$ShakeDetector$OnShakeListener;

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_policy_Shake_ShakeDetector',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
