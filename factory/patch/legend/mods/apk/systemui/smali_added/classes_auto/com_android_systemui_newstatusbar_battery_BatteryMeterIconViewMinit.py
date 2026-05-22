"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit.smali'
CLASS_FALLBACK_NAMES = ['BatteryMeterIconViewMinit.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;
.super Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;,
        Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;
    }
.end annotation


# static fields
.field static final sMinitUpdate:Ljava/lang/ThreadLocal;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/lang/ThreadLocal<",
            "Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;",
            ">;"
        }
    .end annotation
.end field


# instance fields
.field private isCharging:Z

.field private isMinit:Z

.field private level:I

.field private mBatteryIconsLoaction:Ljava/lang/String;

.field private mBatteryType:I

.field private mChargeAnim:I

.field private mDownloadBatteryIconsLoaction:Ljava/lang/String;

.field private mRM:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;

.field private mWorkingType:I


# direct methods
.method static constructor <clinit>()V
    .registers 1

    new-instance v0, Ljava/lang/ThreadLocal;

    invoke-direct {v0}, Ljava/lang/ThreadLocal;-><init>()V

    sput-object v0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->sMinitUpdate:Ljava/lang/ThreadLocal;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;-><init>(Landroid/content/Context;)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->isCharging:Z

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mWorkingType:I

    const/16 v1, 0x8

    iput v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mBatteryType:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mChargeAnim:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->init(Landroid/content/Context;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->isCharging:Z

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mWorkingType:I

    const/16 v1, 0x8

    iput v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mBatteryType:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mChargeAnim:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->init(Landroid/content/Context;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 6

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->isCharging:Z

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mWorkingType:I

    const/16 v1, 0x8

    iput v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mBatteryType:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mChargeAnim:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->init(Landroid/content/Context;)V

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)Landroid/graphics/drawable/Drawable;
    .registers 2

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getMinitDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    return-object v0
.end method

.method private addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V
    .registers 4

    if-eqz p2, :cond_5

    invoke-virtual {p1, p2, p3}, Landroid/graphics/drawable/AnimationDrawable;->addFrame(Landroid/graphics/drawable/Drawable;I)V

    :cond_5
    return-void
.end method

.method private getChargingAnimation(I)Landroid/graphics/drawable/AnimationDrawable;
    .registers 10

    new-instance v0, Landroid/graphics/drawable/AnimationDrawable;

    invoke-direct {v0}, Landroid/graphics/drawable/AnimationDrawable;-><init>()V

    :try_start_5
    iget v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mChargeAnim:I

    const/16 v2, 0x1f4

    if-eqz v1, :cond_a2

    const/16 v3, 0x9c4

    const/16 v4, 0x14

    const/16 v5, 0x64

    const/4 v6, 0x1

    if-eq v1, v6, :cond_86

    const/4 v2, 0x2

    const/16 v6, 0x65

    const/16 v7, 0x7d0

    if-eq v1, v2, :cond_6f

    const/4 v2, 0x3

    if-eq v1, v2, :cond_56

    const/4 v2, 0x4

    if-eq v1, v2, :cond_23

    goto/16 :goto_b3

    :cond_23
    const/4 v1, 0x0

    :goto_24
    if-ge v1, v6, :cond_30

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getChargingDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v2

    invoke-direct {p0, v0, v2, v4}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    add-int/lit8 v1, v1, 0x1

    goto :goto_24

    :cond_30
    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getNormalDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    const/16 v2, 0xfa

    invoke-direct {p0, v0, v1, v2}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getChargingDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    invoke-direct {p0, v0, v1, v5}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getNormalDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    invoke-direct {p0, v0, v1, v2}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getChargingDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    invoke-direct {p0, v0, v1, v5}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getNormalDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    invoke-direct {p0, v0, v1, v7}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    goto :goto_b3

    :cond_56
    move v1, p1

    if-nez v1, :cond_5a

    const/4 v1, 0x1

    :cond_5a
    const/4 v2, 0x0

    :goto_5b
    if-ge v2, v1, :cond_67

    invoke-direct {p0, v2}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getChargingDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v5

    invoke-direct {p0, v0, v5, v4}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    add-int/lit8 v2, v2, 0x1

    goto :goto_5b

    :cond_67
    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getNormalDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v2

    invoke-direct {p0, v0, v2, v3}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    goto :goto_b3

    :cond_6f
    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getNormalDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    invoke-direct {p0, v0, v1, v7}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    move v1, p1

    :goto_77
    if-ge v1, v6, :cond_85

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getChargingDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v2

    const/16 v3, 0x50

    invoke-direct {p0, v0, v2, v3}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    add-int/lit8 v1, v1, 0x1

    goto :goto_77

    :cond_85
    goto :goto_b3

    :cond_86
    const/4 v1, 0x1

    :goto_87
    if-ge v1, v5, :cond_93

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getChargingDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v6

    invoke-direct {p0, v0, v6, v4}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    add-int/lit8 v1, v1, 0x1

    goto :goto_87

    :cond_93
    invoke-direct {p0, v5}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getChargingDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    invoke-direct {p0, v0, v1, v2}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getNormalDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    invoke-direct {p0, v0, v1, v3}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    goto :goto_b3

    :cond_a2
    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getChargingDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    const/16 v3, 0x5dc

    invoke-direct {p0, v0, v1, v3}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getNormalDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    invoke-direct {p0, v0, v1, v2}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->addFrame(Landroid/graphics/drawable/AnimationDrawable;Landroid/graphics/drawable/Drawable;I)V
    :try_end_b2
    .catch Ljava/lang/Exception; {:try_start_5 .. :try_end_b2} :catch_b4

    nop

    :goto_b3
    goto :goto_d3

    :catch_b4
    move-exception v1

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v2

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "getChargingAnimation: "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v2, v3}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_d3
    return-object v0
.end method

.method private getChargingDrawable(I)Landroid/graphics/drawable/Drawable;
    .registers 8

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mWorkingType:I

    const/4 v1, 0x1

    if-eqz v0, :cond_7e

    const-string v2, ".png"

    if-eq v0, v1, :cond_44

    const/4 v3, 0x2

    if-eq v0, v3, :cond_e

    const/4 v0, 0x0

    return-object v0

    :cond_e
    new-instance v0, Ljava/io/File;

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mBatteryIconsLoaction:Ljava/lang/String;

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "stat_sys_battery_charge_anim"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-static {p1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-direct {v0, v3, v2}, Ljava/io/File;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/io/File;->exists()Z

    move-result v2

    if-nez v2, :cond_3b

    invoke-direct {p0, p1, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getDefaultBattery(IZ)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    return-object v1

    :cond_3b
    invoke-virtual {v0}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/graphics/drawable/Drawable;->createFromPath(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    return-object v1

    :cond_44
    new-instance v0, Ljava/io/File;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mDownloadBatteryIconsLoaction:Ljava/lang/String;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, "stat_sys_battery_charge_"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-static {p1}, Ljava/lang/String;->valueOf(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-direct {v0, v2}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/io/File;->exists()Z

    move-result v2

    if-nez v2, :cond_75

    invoke-direct {p0, p1, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getDefaultBattery(IZ)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    return-object v1

    :cond_75
    invoke-virtual {v0}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/graphics/drawable/Drawable;->createFromPath(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    return-object v1

    :cond_7e
    invoke-direct {p0, p1, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getDefaultBattery(IZ)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    return-object v0
.end method

.method private getDefaultBattery(IZ)Landroid/graphics/drawable/Drawable;
    .registers 6

    const-string v0, "battery_"

    if-eqz p2, :cond_28

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mRM:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    iget v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mBatteryType:I

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v2, "_charge_anim"

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v1, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->getDrawable(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_4b

    :cond_28
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mRM:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    iget v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mBatteryType:I

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v2, "_"

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v1, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;->getDrawable(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    :goto_4b
    return-object v0
.end method

.method private getMinitDrawable()Landroid/graphics/drawable/Drawable;
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->isCharging:Z

    if-eqz v0, :cond_f

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->level:I

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getChargingAnimation(I)Landroid/graphics/drawable/AnimationDrawable;

    move-result-object v0

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/AnimationDrawable;->setOneShot(Z)V

    return-object v0

    :cond_f
    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->level:I

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getNormalDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    return-object v0
.end method

.method private getNormalDrawable(I)Landroid/graphics/drawable/Drawable;
    .registers 8

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mWorkingType:I

    const/4 v1, 0x0

    if-eqz v0, :cond_75

    const/4 v2, 0x1

    const-string v3, ".png"

    const-string v4, "stat_sys_battery_"

    if-eq v0, v2, :cond_41

    const/4 v2, 0x2

    if-eq v0, v2, :cond_11

    const/4 v0, 0x0

    return-object v0

    :cond_11
    new-instance v0, Ljava/io/File;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mBatteryIconsLoaction:Ljava/lang/String;

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v5, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v0, v2, v3}, Ljava/io/File;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/io/File;->exists()Z

    move-result v2

    if-nez v2, :cond_38

    invoke-direct {p0, p1, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getDefaultBattery(IZ)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    return-object v1

    :cond_38
    invoke-virtual {v0}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/graphics/drawable/Drawable;->createFromPath(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    return-object v1

    :cond_41
    new-instance v0, Ljava/io/File;

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v5, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mDownloadBatteryIconsLoaction:Ljava/lang/String;

    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-direct {v0, v2}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/io/File;->exists()Z

    move-result v2

    if-nez v2, :cond_6c

    invoke-direct {p0, p1, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getDefaultBattery(IZ)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    return-object v1

    :cond_6c
    invoke-virtual {v0}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Landroid/graphics/drawable/Drawable;->createFromPath(Ljava/lang/String;)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    return-object v1

    :cond_75
    invoke-direct {p0, p1, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getDefaultBattery(IZ)Landroid/graphics/drawable/Drawable;

    move-result-object v0

    return-object v0
.end method

.method private getSaveLocation(Landroid/content/Context;)Ljava/lang/String;
    .registers 6

    invoke-virtual {p1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "save_loc"

    invoke-static {v0, v1}, Landroid/provider/Settings$System;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    const-string v1, "/3Minit Downloads/BatteryIcons/"

    if-eqz v0, :cond_20

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    return-object v1

    :cond_20
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-static {}, Landroid/os/Environment;->getExternalStorageDirectory()Ljava/io/File;

    move-result-object v3

    invoke-virtual {v3}, Ljava/io/File;->getPath()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    return-object v1
.end method

.method private init(Landroid/content/Context;)V
    .registers 4

    :try_start_0
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-static {}, Landroid/os/Environment;->getExternalStorageDirectory()Ljava/io/File;

    move-result-object v1

    invoke-virtual {v1}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    sget-object v1, Ljava/io/File;->separator:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "3MinitBatteryIcons"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mBatteryIconsLoaction:Ljava/lang/String;

    new-instance v0, Ljava/io/File;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mBatteryIconsLoaction:Ljava/lang/String;

    invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/io/File;->mkdirs()Z

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getSaveLocation(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v1

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mDownloadBatteryIconsLoaction:Ljava/lang/String;

    new-instance v1, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;

    invoke-direct {v1, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;-><init>(Landroid/content/Context;)V

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mRM:Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$ResourceManager;
    :try_end_3a
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_3a} :catch_3b

    goto :goto_3f

    :catch_3b
    move-exception v0

    invoke-virtual {v0}, Ljava/lang/Exception;->printStackTrace()V

    :goto_3f
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->updateSettings()V

    return-void
.end method

.method private setImage()V
    .registers 3

    invoke-static {}, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;->getInstance()Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;

    move-result-object v0

    new-instance v1, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$1;-><init>(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/thread/FixedThreadPool;->execute(Ljava/lang/Runnable;)V

    return-void
.end method

.method private updateSettings()V
    .registers 5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getSaveLocation(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v1

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mDownloadBatteryIconsLoaction:Ljava/lang/String;

    const-string v1, "minit_anim_type"

    const/4 v2, 0x0

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mChargeAnim:I

    const-string v1, "minit_battery_type"

    const/16 v3, 0x8

    invoke-static {v0, v1, v3}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mBatteryType:I

    const-string v1, "minit_working_type"

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->mWorkingType:I

    return-void
.end method


# virtual methods
.method public onAttachedToWindow()V
    .registers 5

    invoke-super {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->onAttachedToWindow()V

    sget-object v0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->sMinitUpdate:Ljava/lang/ThreadLocal;

    invoke-virtual {v0}, Ljava/lang/ThreadLocal;->get()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;

    move-object v2, v1

    if-nez v1, :cond_1b

    new-instance v1, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->getContext()Landroid/content/Context;

    move-result-object v3

    invoke-direct {v1, v3}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;-><init>(Landroid/content/Context;)V

    move-object v2, v1

    invoke-virtual {v0, v2}, Ljava/lang/ThreadLocal;->set(Ljava/lang/Object;)V

    :cond_1b
    invoke-virtual {v2, p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->addCallBack(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)V

    return-void
.end method

.method public onBatteryLevelChanged(IZZ)V
    .registers 4

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->updateSettings()V

    iput p1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->level:I

    invoke-super {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->onBatteryLevelChanged(IZZ)V

    return-void
.end method

.method public onChargeStateChanged(ZZ)V
    .registers 4

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->updateSettings()V

    if-nez p1, :cond_a

    if-eqz p2, :cond_8

    goto :goto_a

    :cond_8
    const/4 v0, 0x0

    goto :goto_b

    :cond_a
    :goto_a
    const/4 v0, 0x1

    :goto_b
    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->isCharging:Z

    invoke-super {p0, p1, p2}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->onChargeStateChanged(ZZ)V

    return-void
.end method

.method public onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->onDetachedFromWindow()V

    sget-object v0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->sMinitUpdate:Ljava/lang/ThreadLocal;

    invoke-virtual {v0}, Ljava/lang/ThreadLocal;->get()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;

    if-eqz v0, :cond_10

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit$MinitUpdate;->removeCallBack(Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;)V

    :cond_10
    return-void
.end method

.method public setImageDrawable(Landroid/graphics/drawable/Drawable;)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->isMinit:Z

    if-eqz v0, :cond_8

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->setImage()V

    return-void

    :cond_8
    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    return-void
.end method

.method public setImageLevel(I)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->isMinit:Z

    if-nez v0, :cond_7

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->setImageLevel(I)V

    :cond_7
    return-void
.end method

.method public setUseLegacyDrawable(Z)V
    .registers 5

    const-string v0, "use_legacy_drawable"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    const/4 v1, 0x1

    const/4 v2, 0x0

    if-le v0, v1, :cond_b

    goto :goto_c

    :cond_b
    move v1, v2

    :goto_c
    move v0, v1

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->isMinit:Z

    if-eq v0, v1, :cond_16

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->isMinit:Z

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->onDensityOrFontScaleChanged()V

    :cond_16
    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->setUseLegacyDrawable(Z)V

    if-eqz v0, :cond_1e

    const/16 v1, 0x14

    goto :goto_1f

    :cond_1e
    move v1, v2

    :goto_1f
    invoke-virtual {p0, v1, v2, v1, v2}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->setPadding(IIII)V

    return-void
.end method

.method superSetImageDrawable(Landroid/graphics/drawable/Drawable;)V
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    goto/32 :goto_b

    nop

    :goto_b
    return-void
.end method

.method updateImage()V
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->isMinit:Z

    goto/32 :goto_1e

    nop

    :goto_a
    return-void

    :goto_b
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    :goto_e
    goto/32 :goto_a

    nop

    :goto_12
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryMeterIconViewMinit;->updateSettings()V

    goto/32 :goto_19

    nop

    :goto_19
    const/4 v0, 0x0

    goto/32 :goto_b

    nop

    :goto_1e
    if-nez v0, :cond_23

    goto/32 :goto_e

    :cond_23
    goto/32 :goto_12

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_BatteryMeterIconViewMinit',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
