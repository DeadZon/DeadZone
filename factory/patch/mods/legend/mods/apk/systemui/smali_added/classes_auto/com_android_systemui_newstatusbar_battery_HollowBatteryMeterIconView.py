"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView.smali'
CLASS_FALLBACK_NAMES = ['HollowBatteryMeterIconView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;
.super Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# instance fields
.field protected batteryHeight:I

.field private final controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

.field protected curHeight:I

.field protected curWidth:I

.field private isIconAdded:Z

.field protected naturalHeight:I

.field protected naturalWidth:I


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 6

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->isIconAdded:Z

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const-string v1, "status_bar_icon_height"

    invoke-static {p1, v1}, Landroid/Utils/Utils;->DimenToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryHeight:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "battery_meter_width"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->getDimen(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryWidth:I

    return-void
.end method

.method private clearTint()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstBackground:Landroid/graphics/drawable/Drawable;

    const/4 v1, 0x0

    if-eqz v0, :cond_a

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstBackground:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    :cond_a
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_13

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBackground:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    :cond_13
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->thirdBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_1c

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->thirdBackground:Landroid/graphics/drawable/Drawable;

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    :cond_1c
    return-void
.end method

.method private evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 9

    const/4 v0, 0x0

    const/4 v1, 0x0

    :try_start_2
    const-class v2, Landroid/animation/ArgbEvaluator;

    const-string v3, "getInstance"

    new-array v4, v1, [Ljava/lang/Class;

    invoke-virtual {v2, v3, v4}, Ljava/lang/Class;->getMethod(Ljava/lang/String;[Ljava/lang/Class;)Ljava/lang/reflect/Method;

    move-result-object v2

    const/4 v3, 0x0

    new-array v4, v1, [Ljava/lang/Object;

    invoke-virtual {v2, v3, v4}, Ljava/lang/reflect/Method;->invoke(Ljava/lang/Object;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Landroid/animation/ArgbEvaluator;
    :try_end_15
    .catch Ljava/lang/Exception; {:try_start_2 .. :try_end_15} :catch_17

    move-object v0, v2

    goto :goto_18

    :catch_17
    move-exception v2

    :goto_18
    nop

    if-eqz v0, :cond_20

    invoke-virtual {v0, p1, p2, p3}, Landroid/animation/ArgbEvaluator;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    return-object v1

    :cond_20
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    return-object v1
.end method

.method private firstDrawableToBitmap(Landroid/graphics/drawable/Drawable;)V
    .registers 5

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getIntrinsicWidth()I

    move-result v0

    if-eqz v0, :cond_41

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getIntrinsicHeight()I

    move-result v0

    if-nez v0, :cond_d

    goto :goto_41

    :cond_d
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getWidth()I

    move-result v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getHeight()I

    move-result v1

    sget-object v2, Landroid/graphics/Bitmap$Config;->ARGB_8888:Landroid/graphics/Bitmap$Config;

    invoke-static {v0, v1, v2}, Landroid/graphics/Bitmap;->createBitmap(IILandroid/graphics/Bitmap$Config;)Landroid/graphics/Bitmap;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstDrawableBitmap:Landroid/graphics/Bitmap;

    new-instance v0, Landroid/graphics/Canvas;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstDrawableBitmap:Landroid/graphics/Bitmap;

    invoke-direct {v0, v1}, Landroid/graphics/Canvas;-><init>(Landroid/graphics/Bitmap;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstDrawableCanvas:Landroid/graphics/Canvas;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstDrawableBitmap:Landroid/graphics/Bitmap;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/graphics/Bitmap;->eraseColor(I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getWidth()I

    move-result v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getHeight()I

    move-result v2

    invoke-virtual {p1, v1, v1, v0, v2}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstDrawableCanvas:Landroid/graphics/Canvas;

    if-eqz v0, :cond_40

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstDrawableCanvas:Landroid/graphics/Canvas;

    invoke-virtual {p1, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :cond_40
    return-void

    :cond_41
    :goto_41
    return-void
.end method

.method private getBatteryLevelColor()I
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->low:Z

    if-nez v0, :cond_20

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->powerSave:Z

    if-nez v0, :cond_20

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->performanceMode:Z

    if-nez v0, :cond_20

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->charging:Z

    if-nez v0, :cond_20

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->quickCharging:Z

    if-eqz v0, :cond_15

    goto :goto_20

    :cond_15
    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->dark:I

    const/4 v1, 0x2

    if-ne v0, v1, :cond_1d

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryLevelTransWhite:I

    goto :goto_22

    :cond_1d
    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryLevelTransDark:I

    goto :goto_22

    :cond_20
    :goto_20
    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryLevelWhite:I

    :goto_22
    return v0
.end method

.method private getBatterySecondTintColor()I
    .registers 4

    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/Object;

    const-string v1, "getBatterySecondTintColor"

    const/4 v2, 0x1

    invoke-static {p0, v1, v2, v0}, Landroid/Utils/ReflectionUtil;->invokeInSuperClass(Ljava/lang/Object;Ljava/lang/String;I[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Integer;

    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v0

    return v0
.end method

.method private getChargeDrawable()Landroid/graphics/drawable/LevelListDrawable;
    .registers 8

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->dark:I

    const/16 v1, 0xa

    const/4 v2, 0x1

    const/4 v3, -0x1

    const/4 v4, 0x2

    if-ne v0, v4, :cond_2d

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryIcon:Lcom/miui/systemui/statusbar/BatteryIcon;

    iget v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    iget v5, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mChargeDigitDarkLevel:I

    if-eq v5, v3, :cond_1b

    iget v3, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    iget v6, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mChargeDigitDarkLevel:I

    sub-int/2addr v3, v6

    move v6, v3

    if-gt v3, v1, :cond_1b

    if-gez v6, :cond_2a

    :cond_1b
    nop

    const-string v1, "stat_sys_battery_charge_digit_darkmode"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->rawToId(Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1, v4, v2}, Lcom/miui/systemui/statusbar/BatteryIcon;->generateIcon(IIZ)Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v1

    iput-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicChargeDigitIconDarkMode:Landroid/graphics/drawable/LevelListDrawable;

    iput v4, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mChargeDigitDarkLevel:I

    :cond_2a
    iget-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicChargeDigitIconDarkMode:Landroid/graphics/drawable/LevelListDrawable;

    return-object v1

    :cond_2d
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryIcon:Lcom/miui/systemui/statusbar/BatteryIcon;

    iget v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    iget v5, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mChargeDigitLevel:I

    if-eq v5, v3, :cond_3c

    sub-int v3, v4, v5

    move v6, v3

    if-gt v3, v1, :cond_3c

    if-gez v6, :cond_4b

    :cond_3c
    nop

    const-string v1, "stat_sys_battery_charge_digit"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->rawToId(Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1, v4, v2}, Lcom/miui/systemui/statusbar/BatteryIcon;->generateIcon(IIZ)Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v1

    iput-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicChargeDigitIcon:Landroid/graphics/drawable/LevelListDrawable;

    iput v4, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mChargeDigitLevel:I

    :cond_4b
    iget-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicChargeDigitIcon:Landroid/graphics/drawable/LevelListDrawable;

    return-object v1
.end method

.method private getData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getIconData(Z)Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    return-object v0
.end method

.method private getDigitalDrawable()Landroid/graphics/drawable/LevelListDrawable;
    .registers 8

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->dark:I

    const/16 v1, 0xa

    const/4 v2, 0x0

    const/4 v3, -0x1

    const/4 v4, 0x2

    if-ne v0, v4, :cond_2a

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryIcon:Lcom/miui/systemui/statusbar/BatteryIcon;

    iget v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    iget v5, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mDigitalDarkLevel:I

    if-eq v5, v3, :cond_18

    sub-int v3, v5, v4

    move v6, v3

    if-gt v3, v1, :cond_18

    if-gez v6, :cond_27

    :cond_18
    nop

    const-string v1, "stat_sys_battery_digital_darkmode"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->rawToId(Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1, v4, v2}, Lcom/miui/systemui/statusbar/BatteryIcon;->generateIcon(IIZ)Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v1

    iput-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicDigitalIconDarkMode:Landroid/graphics/drawable/LevelListDrawable;

    iput v4, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mDigitalDarkLevel:I

    :cond_27
    iget-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicDigitalIconDarkMode:Landroid/graphics/drawable/LevelListDrawable;

    return-object v1

    :cond_2a
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryIcon:Lcom/miui/systemui/statusbar/BatteryIcon;

    iget v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    iget v5, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mDigitalLevel:I

    if-eq v5, v3, :cond_39

    sub-int v3, v5, v4

    move v6, v3

    if-gt v3, v1, :cond_39

    if-gez v6, :cond_48

    :cond_39
    nop

    const-string v1, "stat_sys_battery_digital"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->rawToId(Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1, v4, v2}, Lcom/miui/systemui/statusbar/BatteryIcon;->generateIcon(IIZ)Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v1

    iput-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicDigitalIcon:Landroid/graphics/drawable/LevelListDrawable;

    iput v4, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mDigitalLevel:I

    :cond_48
    iget-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicDigitalIcon:Landroid/graphics/drawable/LevelListDrawable;

    return-object v1
.end method

.method private getFirstBgStatus()Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->performanceMode:Z

    const/4 v1, 0x2

    if-eqz v0, :cond_f

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->dark:I

    if-ne v0, v1, :cond_c

    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->PERFORMANCE_MODE_DARK:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    goto :goto_18

    :cond_c
    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->PERFORMANCE_MODE:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    goto :goto_18

    :cond_f
    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->dark:I

    if-ne v0, v1, :cond_16

    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->NORMAL_DARK:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    goto :goto_18

    :cond_16
    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->NORMAL:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    :goto_18
    return-object v0
.end method

.method private getPerfomanceModeDrawable()Landroid/graphics/drawable/LevelListDrawable;
    .registers 8

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->dark:I

    const/16 v1, 0xa

    const/4 v2, 0x1

    const/4 v3, -0x1

    const/4 v4, 0x2

    if-ne v0, v4, :cond_2a

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryIcon:Lcom/miui/systemui/statusbar/BatteryIcon;

    iget v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    iget v5, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mPerformanceModeDigitDarkLevel:I

    if-eq v5, v3, :cond_18

    sub-int v3, v4, v5

    move v6, v3

    if-gt v3, v1, :cond_18

    if-gez v6, :cond_27

    :cond_18
    nop

    const-string v1, "stat_sys_battery_performance_mode_digit_darkmode"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->rawToId(Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1, v4, v2}, Lcom/miui/systemui/statusbar/BatteryIcon;->generateIcon(IIZ)Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v1

    iput-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicPerformanceModeDigitIconDarkMode:Landroid/graphics/drawable/LevelListDrawable;

    iput v4, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mPerformanceModeDigitDarkLevel:I

    :cond_27
    iget-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicPerformanceModeDigitIconDarkMode:Landroid/graphics/drawable/LevelListDrawable;

    return-object v1

    :cond_2a
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryIcon:Lcom/miui/systemui/statusbar/BatteryIcon;

    iget v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    iget v5, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mPerformanceModeDigitLevel:I

    if-eq v5, v3, :cond_39

    sub-int v3, v4, v5

    move v6, v3

    if-gt v3, v1, :cond_39

    if-gez v6, :cond_48

    :cond_39
    nop

    const-string v1, "stat_sys_battery_performance_mode_digit"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->rawToId(Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1, v4, v2}, Lcom/miui/systemui/statusbar/BatteryIcon;->generateIcon(IIZ)Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v1

    iput-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicPerformanceModeDigitIcon:Landroid/graphics/drawable/LevelListDrawable;

    iput v4, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mPerformanceModeDigitLevel:I

    :cond_48
    iget-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicPerformanceModeDigitIcon:Landroid/graphics/drawable/LevelListDrawable;

    return-object v1
.end method

.method private getPowerSaveDrawable()Landroid/graphics/drawable/LevelListDrawable;
    .registers 8

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->dark:I

    const/16 v1, 0xa

    const/4 v2, 0x1

    const/4 v3, -0x1

    const/4 v4, 0x2

    if-ne v0, v4, :cond_2a

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryIcon:Lcom/miui/systemui/statusbar/BatteryIcon;

    iget v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    iget v5, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mPowerSaveDigitDarkLevel:I

    if-eq v5, v3, :cond_18

    sub-int v3, v4, v5

    move v6, v3

    if-gt v3, v1, :cond_18

    if-gez v6, :cond_27

    :cond_18
    nop

    const-string v1, "stat_sys_battery_power_save_digit_darkmode"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->rawToId(Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1, v4, v2}, Lcom/miui/systemui/statusbar/BatteryIcon;->generateIcon(IIZ)Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v1

    iput-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicPowerSaveDigitIconDarkMode:Landroid/graphics/drawable/LevelListDrawable;

    iput v4, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mPowerSaveDigitDarkLevel:I

    :cond_27
    iget-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicPowerSaveDigitIconDarkMode:Landroid/graphics/drawable/LevelListDrawable;

    return-object v1

    :cond_2a
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryIcon:Lcom/miui/systemui/statusbar/BatteryIcon;

    iget v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    iget v5, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mPowerSaveDigitLevel:I

    if-eq v5, v3, :cond_39

    sub-int v3, v4, v5

    move v6, v3

    if-gt v3, v1, :cond_39

    if-gez v6, :cond_48

    :cond_39
    nop

    const-string v1, "stat_sys_battery_power_save_digit"

    invoke-direct {p0, v1}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->rawToId(Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1, v4, v2}, Lcom/miui/systemui/statusbar/BatteryIcon;->generateIcon(IIZ)Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v1

    iput-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicPowerSaveDigitIcon:Landroid/graphics/drawable/LevelListDrawable;

    iput v4, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mPowerSaveDigitLevel:I

    :cond_48
    iget-object v1, v0, Lcom/miui/systemui/statusbar/BatteryIcon;->mGraphicPowerSaveDigitIcon:Landroid/graphics/drawable/LevelListDrawable;

    return-object v1
.end method

.method private getRealCornerRadiusTranX()I
    .registers 4

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getWidth()I

    move-result v0

    int-to-float v0, v0

    iget v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryWidth:I

    int-to-float v1, v1

    div-float/2addr v0, v1

    iget v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->cornerRadiusTranX:F

    mul-float/2addr v0, v1

    iget v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    div-int/lit8 v1, v1, 0x64

    rsub-int/lit8 v1, v1, 0x1

    int-to-float v1, v1

    mul-float/2addr v1, v0

    float-to-int v1, v1

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->progressOrientationPortrait:Z

    if-eqz v2, :cond_1b

    const/4 v1, 0x0

    goto :goto_20

    :cond_1b
    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->progressGravityStart:Z

    if-nez v2, :cond_20

    neg-int v1, v1

    :cond_20
    :goto_20
    iget v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    if-nez v2, :cond_27

    mul-int/lit8 v2, v1, 0x2

    goto :goto_28

    :cond_27
    move v2, v1

    :goto_28
    return v2
.end method

.method private getRealCornerRadiusTranY()I
    .registers 4

    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/Object;

    const-string v1, "getRealCornerRadiusTranY"

    const/4 v2, 0x1

    invoke-static {p0, v1, v2, v0}, Landroid/Utils/ReflectionUtil;->invokeInSuperClass(Ljava/lang/Object;Ljava/lang/String;I[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Integer;

    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v0

    return v0
.end method

.method private getSecondBgStatus()Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->quickCharging:Z

    if-nez v0, :cond_29

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->charging:Z

    if-eqz v0, :cond_9

    goto :goto_29

    :cond_9
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->powerSave:Z

    if-eqz v0, :cond_10

    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->POWER_SAVE:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    goto :goto_32

    :cond_10
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->performanceMode:Z

    if-eqz v0, :cond_17

    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->PERFORMANCE_MODE:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    goto :goto_32

    :cond_17
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->low:Z

    if-eqz v0, :cond_1e

    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->LOW:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    goto :goto_32

    :cond_1e
    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->dark:I

    const/4 v1, 0x2

    if-ne v0, v1, :cond_26

    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->NORMAL_DARK:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    goto :goto_32

    :cond_26
    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->NORMAL:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    goto :goto_32

    :cond_29
    :goto_29
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->performanceMode:Z

    if-eqz v0, :cond_30

    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->PERF_CHARGE_MODE:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    goto :goto_32

    :cond_30
    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->CHARGING:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    :goto_32
    return-object v0
.end method

.method private getThirdBgStatus()Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;
    .registers 3

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->dark:I

    const/4 v1, 0x2

    if-ne v0, v1, :cond_8

    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->PERFORMANCE_MODE_DARK:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    goto :goto_a

    :cond_8
    sget-object v0, Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;->PERFORMANCE_MODE:Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    :goto_a
    return-object v0
.end method

.method private isZero()Z
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->naturalHeight:I

    if-eqz v0, :cond_b

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->naturalWidth:I

    if-nez v0, :cond_9

    goto :goto_b

    :cond_9
    const/4 v0, 0x0

    goto :goto_c

    :cond_b
    :goto_b
    const/4 v0, 0x1

    :goto_c
    return v0
.end method

.method private rawToId(Ljava/lang/String;)I
    .registers 5

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/Context;->getPackageName()Ljava/lang/String;

    move-result-object v1

    const-string v2, "raw"

    invoke-virtual {v0, p1, v2, v1}, Landroid/content/res/Resources;->getIdentifier(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)I

    move-result v0

    return v0
.end method

.method private setNoUseTintColor(II)V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstBackgroundDrawables:Landroid/util/ArrayMap;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getFirstBgStatus()Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/graphics/drawable/Drawable;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstBackground:Landroid/graphics/drawable/Drawable;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBackgroundDrawables:Landroid/util/ArrayMap;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getSecondBgStatus()Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/graphics/drawable/Drawable;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBackground:Landroid/graphics/drawable/Drawable;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->thirdBackgroundDrawables:Landroid/util/ArrayMap;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getThirdBgStatus()Lcom/android/systemui/statusbar/util/MiuiBatteryUtils$BatteryStatus;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/graphics/drawable/Drawable;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->thirdBackground:Landroid/graphics/drawable/Drawable;

    if-eqz p1, :cond_47

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstBackground:Landroid/graphics/drawable/Drawable;

    invoke-static {p1}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBackground:Landroid/graphics/drawable/Drawable;

    invoke-static {p1}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->thirdBackground:Landroid/graphics/drawable/Drawable;

    invoke-static {p1}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    :cond_47
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->textPaint:Landroid/graphics/Paint;

    if-eqz v0, :cond_58

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->textPaint:Landroid/graphics/Paint;

    if-eqz p2, :cond_51

    move v1, p2

    goto :goto_55

    :cond_51
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getBatteryLevelColor()I

    move-result v1

    :goto_55
    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->setColor(I)V

    :cond_58
    return-void
.end method

.method private setUseTintColor(II)V
    .registers 7

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_19

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstBackground:Landroid/graphics/drawable/Drawable;

    if-eqz p1, :cond_a

    move v1, p1

    goto :goto_12

    :cond_a
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->tintAreas:Ljava/util/ArrayList;

    iget v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->tintColor:I

    invoke-static {v1, p0, v2}, Lcom/android/systemui/plugins/DarkIconDispatcher;->getTint(Ljava/util/Collection;Landroid/view/View;I)I

    move-result v1

    :goto_12
    invoke-static {v1}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    :cond_19
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_2e

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBackground:Landroid/graphics/drawable/Drawable;

    if-eqz p1, :cond_23

    move v1, p1

    goto :goto_27

    :cond_23
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getBatterySecondTintColor()I

    move-result v1

    :goto_27
    invoke-static {v1}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    :cond_2e
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->thirdBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_47

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->thirdBackground:Landroid/graphics/drawable/Drawable;

    if-eqz p1, :cond_38

    move v1, p1

    goto :goto_40

    :cond_38
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->tintAreas:Ljava/util/ArrayList;

    iget v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->tintColor:I

    invoke-static {v1, p0, v2}, Lcom/android/systemui/plugins/DarkIconDispatcher;->getTint(Ljava/util/Collection;Landroid/view/View;I)I

    move-result v1

    :goto_40
    invoke-static {v1}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setTintList(Landroid/content/res/ColorStateList;)V

    :cond_47
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->textPaint:Landroid/graphics/Paint;

    if-eqz v0, :cond_99

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->textPaint:Landroid/graphics/Paint;

    if-eqz p2, :cond_51

    move v1, p2

    goto :goto_96

    :cond_51
    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->low:Z

    if-nez v1, :cond_88

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->powerSave:Z

    if-nez v1, :cond_88

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->performanceMode:Z

    if-nez v1, :cond_88

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->charging:Z

    if-nez v1, :cond_88

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->quickCharging:Z

    if-eqz v1, :cond_66

    goto :goto_88

    :cond_66
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->tintAreas:Ljava/util/ArrayList;

    invoke-static {v1, p0}, Lcom/android/systemui/plugins/DarkIconDispatcher;->isInAreas(Ljava/util/Collection;Landroid/view/View;)Z

    move-result v1

    if-eqz v1, :cond_81

    iget v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->darkIntensity:F

    iget v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryLevelTransDark:I

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    iget v3, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryLevelTransWhite:I

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    invoke-direct {p0, v1, v2, v3}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->evaluate(FLjava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_8e

    :cond_81
    iget v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryLevelTransDark:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_8e

    :cond_88
    :goto_88
    iget v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryLevelWhite:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    :goto_8e
    check-cast v1, Ljava/lang/Integer;

    check-cast v1, Ljava/lang/Integer;

    invoke-virtual {v1}, Ljava/lang/Integer;->intValue()I

    move-result v1

    :goto_96
    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->setColor(I)V

    :cond_99
    return-void
.end method

.method private update()V
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->isIconAdded:Z

    if-eqz v0, :cond_d

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->updateZoom()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->updateResources()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->invalidate()V

    :cond_d
    return-void
.end method

.method private updateScale(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V
    .registers 9

    iget v0, p2, Lcom/android/systemui/newstatusbar/data/IconData;->zoom:I

    int-to-float v0, v0

    const/high16 v1, 0x42c80000  # 100.0f

    div-float v0, v1, v0

    const/high16 v2, 0x3f800000  # 1.0f

    sub-float/2addr v0, v2

    const/high16 v2, 0x40800000  # 4.0f

    mul-float/2addr v0, v2

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->division:I

    int-to-float v2, v2

    add-float/2addr v2, v0

    const/4 v3, 0x0

    invoke-virtual {p1, v3, v2}, Landroid/graphics/Canvas;->translate(FF)V

    iget v2, p2, Lcom/android/systemui/newstatusbar/data/IconData;->scale:I

    int-to-float v2, v2

    div-float/2addr v2, v1

    iget v3, p2, Lcom/android/systemui/newstatusbar/data/IconData;->scale:I

    int-to-float v3, v3

    div-float/2addr v3, v1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getWidth()I

    move-result v1

    int-to-float v1, v1

    const/high16 v4, 0x40000000  # 2.0f

    div-float/2addr v1, v4

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getHeight()I

    move-result v5

    int-to-float v5, v5

    div-float/2addr v5, v4

    invoke-virtual {p1, v2, v3, v1, v5}, Landroid/graphics/Canvas;->scale(FFFF)V

    return-void
.end method

.method private updateZoom()V
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    if-eqz v0, :cond_9

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    :cond_9
    return-void
.end method


# virtual methods
.method public onAttachedToWindow()V
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;->onAttachedToWindow()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;->onDetachedFromWindow()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public onDraw(Landroid/graphics/Canvas;)V
    .registers 4

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->isIconAdded:Z

    if-eqz v1, :cond_d

    if-eqz v0, :cond_d

    invoke-direct {p0, p1, v0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->updateScale(Landroid/graphics/Canvas;Lcom/android/systemui/newstatusbar/data/IconData;)V

    :cond_d
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;->onDraw(Landroid/graphics/Canvas;)V

    return-void
.end method

.method public onIconChange()V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->update()V

    return-void
.end method

.method public final radiusDrawableToBitmap(Landroid/graphics/drawable/Drawable;II)V
    .registers 7

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getIntrinsicWidth()I

    move-result v0

    if-eqz v0, :cond_43

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getIntrinsicHeight()I

    move-result v0

    if-nez v0, :cond_d

    goto :goto_43

    :cond_d
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getWidth()I

    move-result v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getHeight()I

    move-result v1

    sget-object v2, Landroid/graphics/Bitmap$Config;->ARGB_8888:Landroid/graphics/Bitmap$Config;

    invoke-static {v0, v1, v2}, Landroid/graphics/Bitmap;->createBitmap(IILandroid/graphics/Bitmap$Config;)Landroid/graphics/Bitmap;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawableBitmap:Landroid/graphics/Bitmap;

    new-instance v0, Landroid/graphics/Canvas;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawableBitmap:Landroid/graphics/Bitmap;

    invoke-direct {v0, v1}, Landroid/graphics/Canvas;-><init>(Landroid/graphics/Bitmap;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawableCanvas:Landroid/graphics/Canvas;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawableBitmap:Landroid/graphics/Bitmap;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/graphics/Bitmap;->eraseColor(I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getWidth()I

    move-result v0

    add-int/2addr v0, p2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getHeight()I

    move-result v1

    add-int/2addr v1, p3

    invoke-virtual {p1, p2, p3, v0, v1}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawableCanvas:Landroid/graphics/Canvas;

    if-eqz v0, :cond_42

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawableCanvas:Landroid/graphics/Canvas;

    invoke-virtual {p1, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :cond_42
    return-void

    :cond_43
    :goto_43
    return-void
.end method

.method public final secondDrawableToBitmap(Landroid/graphics/drawable/Drawable;)V
    .registers 5

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getIntrinsicWidth()I

    move-result v0

    if-eqz v0, :cond_41

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getIntrinsicHeight()I

    move-result v0

    if-nez v0, :cond_d

    goto :goto_41

    :cond_d
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getWidth()I

    move-result v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getHeight()I

    move-result v1

    sget-object v2, Landroid/graphics/Bitmap$Config;->ARGB_8888:Landroid/graphics/Bitmap$Config;

    invoke-static {v0, v1, v2}, Landroid/graphics/Bitmap;->createBitmap(IILandroid/graphics/Bitmap$Config;)Landroid/graphics/Bitmap;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondDrawableBitmap:Landroid/graphics/Bitmap;

    new-instance v0, Landroid/graphics/Canvas;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondDrawableBitmap:Landroid/graphics/Bitmap;

    invoke-direct {v0, v1}, Landroid/graphics/Canvas;-><init>(Landroid/graphics/Bitmap;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondDrawableCanvas:Landroid/graphics/Canvas;

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondDrawableBitmap:Landroid/graphics/Bitmap;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/graphics/Bitmap;->eraseColor(I)V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getWidth()I

    move-result v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getHeight()I

    move-result v2

    invoke-virtual {p1, v1, v1, v0, v2}, Landroid/graphics/drawable/Drawable;->setBounds(IIII)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondDrawableCanvas:Landroid/graphics/Canvas;

    if-eqz v0, :cond_40

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondDrawableCanvas:Landroid/graphics/Canvas;

    invoke-virtual {p1, v0}, Landroid/graphics/drawable/Drawable;->draw(Landroid/graphics/Canvas;)V

    :cond_40
    return-void

    :cond_41
    :goto_41
    return-void
.end method

.method public setImageDrawable(Landroid/graphics/drawable/Drawable;)V
    .registers 3

    if-eqz p1, :cond_1a

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->isZero()Z

    move-result v0

    if-eqz v0, :cond_1a

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getIntrinsicHeight()I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->naturalHeight:I

    invoke-virtual {p1}, Landroid/graphics/drawable/Drawable;->getIntrinsicWidth()I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->naturalWidth:I

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->isIconAdded:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->update()V

    :cond_1a
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    return-void
.end method

.method public setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V
    .registers 8

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getData()Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v0

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->isIconAdded:Z

    if-eqz v1, :cond_2d

    if-eqz v0, :cond_2d

    if-eqz p1, :cond_2d

    iget v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->zoom:I

    iget v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->naturalWidth:I

    if-lez v2, :cond_2d

    iget v3, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->naturalHeight:I

    if-lez v3, :cond_2d

    int-to-float v4, v1

    iget v5, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryHeight:I

    int-to-float v5, v5

    mul-float/2addr v4, v5

    const/high16 v5, 0x42c80000  # 100.0f

    div-float/2addr v4, v5

    float-to-int v4, v4

    int-to-float v5, v4

    int-to-float v2, v2

    mul-float/2addr v5, v2

    int-to-float v2, v3

    div-float/2addr v5, v2

    float-to-int v2, v5

    iput v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->curHeight:I

    iput v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->curWidth:I

    iput v2, p1, Landroid/view/ViewGroup$LayoutParams;->width:I

    iput v4, p1, Landroid/view/ViewGroup$LayoutParams;->height:I

    :cond_2d
    invoke-super {p0, p1}, Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    return-void
.end method

.method public setScaleType(Landroid/widget/ImageView$ScaleType;)V
    .registers 2

    return-void
.end method

.method public final updateBatteryDrawable()V
    .registers 6

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getPercentDigitColor()I

    move-result v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    const/4 v2, 0x1

    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getIconData(Z)Lcom/android/systemui/newstatusbar/data/IconData;

    move-result-object v1

    iget v1, v1, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->clearTint()V

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->useTint:Z

    if-eqz v2, :cond_1a

    invoke-direct {p0, v1, v0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->setUseTintColor(II)V

    goto :goto_1d

    :cond_1a
    invoke-direct {p0, v1, v0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->setNoUseTintColor(II)V

    :goto_1d
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->updateFirstBitmap()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->updateSecondBitmap()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->invalidate()V

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->useLegacyDrawable:Z

    if-nez v2, :cond_2f

    const/4 v2, 0x0

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    return-void

    :cond_2f
    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->textPaint:Landroid/graphics/Paint;

    if-eqz v2, :cond_44

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->textPaint:Landroid/graphics/Paint;

    if-eqz v0, :cond_39

    move v3, v0

    goto :goto_41

    :cond_39
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->tintAreas:Ljava/util/ArrayList;

    iget v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->tintColor:I

    invoke-static {v3, p0, v4}, Lcom/android/systemui/plugins/DarkIconDispatcher;->getTint(Ljava/util/Collection;Landroid/view/View;I)I

    move-result v3

    :goto_41
    invoke-virtual {v2, v3}, Landroid/graphics/Paint;->setColor(I)V

    :cond_44
    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->charging:Z

    if-eqz v2, :cond_4d

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getChargeDrawable()Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v2

    goto :goto_63

    :cond_4d
    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->performanceMode:Z

    if-eqz v2, :cond_56

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getPerfomanceModeDrawable()Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v2

    goto :goto_63

    :cond_56
    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->powerSave:Z

    if-eqz v2, :cond_5f

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getPowerSaveDrawable()Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v2

    goto :goto_63

    :cond_5f
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getDigitalDrawable()Landroid/graphics/drawable/LevelListDrawable;

    move-result-object v2

    :goto_63
    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    iget v3, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->level:I

    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->setImageLevel(I)V

    if-eqz v1, :cond_74

    invoke-static {v1}, Landroid/content/res/ColorStateList;->valueOf(I)Landroid/content/res/ColorStateList;

    move-result-object v3

    invoke-virtual {v2, v3}, Landroid/graphics/drawable/LevelListDrawable;->setTintList(Landroid/content/res/ColorStateList;)V

    :cond_74
    return-void
.end method

.method public updateResources()V
    .registers 3

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MiuiHollowBatteryMeterIconView;->updateResources()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->isZero()Z

    move-result v0

    if-eqz v0, :cond_17

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryWidth:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->naturalWidth:I

    iget v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->batteryHeight:I

    iput v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->naturalHeight:I

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->isIconAdded:Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->update()V

    :cond_17
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->hollowTextPaint:Landroid/graphics/Paint;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getPercentDigitZoom()I

    move-result v1

    int-to-float v1, v1

    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->setTextSize(F)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->textPaint:Landroid/graphics/Paint;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->controller:Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getPercentDigitZoom()I

    move-result v1

    int-to-float v1, v1

    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->setTextSize(F)V

    return-void
.end method

.method public final updateSecondBitmap()V
    .registers 8

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getWidth()I

    move-result v0

    if-eqz v0, :cond_a9

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getHeight()I

    move-result v0

    if-nez v0, :cond_e

    goto/16 :goto_a9

    :cond_e
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getWidth()I

    move-result v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getHeight()I

    move-result v1

    sget-object v2, Landroid/graphics/Bitmap$Config;->ARGB_8888:Landroid/graphics/Bitmap$Config;

    invoke-static {v0, v1, v2}, Landroid/graphics/Bitmap;->createBitmap(IILandroid/graphics/Bitmap$Config;)Landroid/graphics/Bitmap;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBitmap:Landroid/graphics/Bitmap;

    new-instance v0, Landroid/graphics/Canvas;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBitmap:Landroid/graphics/Bitmap;

    invoke-direct {v0, v1}, Landroid/graphics/Canvas;-><init>(Landroid/graphics/Bitmap;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondCanvas:Landroid/graphics/Canvas;

    new-instance v0, Landroid/graphics/Paint;

    invoke-direct {v0}, Landroid/graphics/Paint;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondPaint:Landroid/graphics/Paint;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->setAntiAlias(Z)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBitmap:Landroid/graphics/Bitmap;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Landroid/graphics/Bitmap;->eraseColor(I)V

    new-instance v1, Landroid/graphics/PorterDuffXfermode;

    sget-object v2, Landroid/graphics/PorterDuff$Mode;->SRC_OVER:Landroid/graphics/PorterDuff$Mode;

    invoke-direct {v1, v2}, Landroid/graphics/PorterDuffXfermode;-><init>(Landroid/graphics/PorterDuff$Mode;)V

    invoke-virtual {v0, v1}, Landroid/graphics/Paint;->setXfermode(Landroid/graphics/Xfermode;)Landroid/graphics/Xfermode;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v1, :cond_5a

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondDrawableToBitmap(Landroid/graphics/drawable/Drawable;)V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondDrawableBitmap:Landroid/graphics/Bitmap;

    if-eqz v2, :cond_5a

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondCanvas:Landroid/graphics/Canvas;

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondDrawableBitmap:Landroid/graphics/Bitmap;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getMatrix()Landroid/graphics/Matrix;

    move-result-object v4

    iget-object v5, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondPaint:Landroid/graphics/Paint;

    invoke-virtual {v2, v3, v4, v5}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;Landroid/graphics/Matrix;Landroid/graphics/Paint;)V

    :cond_5a
    new-instance v2, Landroid/graphics/PorterDuffXfermode;

    sget-object v3, Landroid/graphics/PorterDuff$Mode;->DST_IN:Landroid/graphics/PorterDuff$Mode;

    invoke-direct {v2, v3}, Landroid/graphics/PorterDuffXfermode;-><init>(Landroid/graphics/PorterDuff$Mode;)V

    invoke-virtual {v0, v2}, Landroid/graphics/Paint;->setXfermode(Landroid/graphics/Xfermode;)Landroid/graphics/Xfermode;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawable:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_86

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawable:Landroid/graphics/drawable/Drawable;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getRealCornerRadiusTranX()I

    move-result v3

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getRealCornerRadiusTranY()I

    move-result v4

    invoke-virtual {p0, v2, v3, v4}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawableToBitmap(Landroid/graphics/drawable/Drawable;II)V

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawableBitmap:Landroid/graphics/Bitmap;

    if-eqz v2, :cond_86

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondCanvas:Landroid/graphics/Canvas;

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->radiusDrawableBitmap:Landroid/graphics/Bitmap;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getMatrix()Landroid/graphics/Matrix;

    move-result-object v4

    iget-object v5, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondPaint:Landroid/graphics/Paint;

    invoke-virtual {v2, v3, v4, v5}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;Landroid/graphics/Matrix;Landroid/graphics/Paint;)V

    :cond_86
    new-instance v2, Landroid/graphics/PorterDuffXfermode;

    sget-object v3, Landroid/graphics/PorterDuff$Mode;->SRC_OUT:Landroid/graphics/PorterDuff$Mode;

    invoke-direct {v2, v3}, Landroid/graphics/PorterDuffXfermode;-><init>(Landroid/graphics/PorterDuff$Mode;)V

    invoke-virtual {v0, v2}, Landroid/graphics/Paint;->setXfermode(Landroid/graphics/Xfermode;)Landroid/graphics/Xfermode;

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v2, :cond_a8

    invoke-direct {p0, v2}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstDrawableToBitmap(Landroid/graphics/drawable/Drawable;)V

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstDrawableBitmap:Landroid/graphics/Bitmap;

    if-eqz v3, :cond_a8

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondCanvas:Landroid/graphics/Canvas;

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->firstDrawableBitmap:Landroid/graphics/Bitmap;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->getMatrix()Landroid/graphics/Matrix;

    move-result-object v5

    iget-object v6, p0, Lcom/android/systemui/newstatusbar/battery/HollowBatteryMeterIconView;->secondPaint:Landroid/graphics/Paint;

    invoke-virtual {v3, v4, v5, v6}, Landroid/graphics/Canvas;->drawBitmap(Landroid/graphics/Bitmap;Landroid/graphics/Matrix;Landroid/graphics/Paint;)V

    :cond_a8
    return-void

    :cond_a9
    :goto_a9
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_HollowBatteryMeterIconView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
