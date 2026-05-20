"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/BatteryColorSizeController.smali'
CLASS_FALLBACK_NAMES = ['BatteryColorSizeController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;
.super Lcom/android/systemui/newstatusbar/controllers/IconController;

# interfaces
.implements Lcom/android/systemui/statusbar/policy/BatteryController$BatteryStateChangeCallback;
.implements Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;


# static fields
.field public static TAG:Ljava/lang/String;


# instance fields
.field private final batteryData:Lcom/android/systemui/newstatusbar/data/IconData;

.field private final batteryIcon:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final chargeData:Lcom/android/systemui/newstatusbar/data/IconData;

.field private final chargeIcon:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private currLevel:Ljava/lang/String;

.field private currLevelMark:Ljava/lang/String;

.field private isAddOnBatteryLevelChanged:Z

.field private final markData:Lcom/android/systemui/newstatusbar/data/TextData;

.field private final otherIcon:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final percentData:Lcom/android/systemui/newstatusbar/data/TextData;

.field private percentDigitColor:I

.field private percentDigitZoom:I

.field private final percentLayout:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final percentMark:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final percentOut:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;"
        }
    .end annotation
.end field

.field private final sKeysBatteryIcon:[Ljava/lang/String;

.field private final sKeysMark:[Ljava/lang/String;

.field private final sKeysOther:[Ljava/lang/String;

.field private final sKeysPercent:[Ljava/lang/String;


# direct methods
.method static constructor <clinit>()V
    .registers 1

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;

    invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;)V
    .registers 13

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IconController;-><init>(Landroid/content/Context;)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentOut:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentMark:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->chargeIcon:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->otherIcon:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentLayout:Ljava/util/ArrayList;

    const-string v1, "battery_percent_zoom"

    const-string v2, "text_bat_color_4"

    const-string v3, "text_bat_color_3"

    const-string v4, "text_bat_color_2"

    const-string v5, "text_bat_color_1"

    const-string v6, "text_bat_color_0"

    const-string v7, "battery_percent_division"

    const-string v8, "battery_percent_typefasestyle"

    const-string v9, "battery_percent_typefase"

    filled-new-array/range {v1 .. v9}, [Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->sKeysPercent:[Ljava/lang/String;

    const-string v1, "battery_percent_mark_zoom"

    const-string v2, "text_bat_color_mark_4"

    const-string v3, "text_bat_color_mark_3"

    const-string v4, "text_bat_color_mark_2"

    const-string v5, "text_bat_color_mark_1"

    const-string v6, "text_bat_color_mark_0"

    const-string v7, "battery_percent_mark_division"

    const-string v8, "battery_percent_mark_settings_enable"

    const-string v9, "battery_percent_mark_typefasestyle"

    const-string v10, "battery_percent_mark_typefase"

    filled-new-array/range {v1 .. v10}, [Ljava/lang/String;

    move-result-object v1

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->sKeysMark:[Ljava/lang/String;

    const-string v2, "batteryview_zoom"

    const-string v3, "batteryview_scale"

    const-string v4, "batteryview_division"

    const-string v5, "batteryview_color"

    const-string v6, "battery_percent_digit_color"

    const-string v7, "battery_percent_digit_zoom"

    filled-new-array/range {v2 .. v7}, [Ljava/lang/String;

    move-result-object v2

    iput-object v2, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->sKeysBatteryIcon:[Ljava/lang/String;

    const-string v3, "use_legacy_drawable"

    const-string v4, "battery_percent_mark_enable"

    filled-new-array {v3, v4}, [Ljava/lang/String;

    move-result-object v3

    iput-object v3, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->sKeysOther:[Ljava/lang/String;

    const-string v4, ""

    iput-object v4, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    iput-object v4, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->currLevelMark:Ljava/lang/String;

    const/4 v4, 0x0

    iput-boolean v4, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->isAddOnBatteryLevelChanged:Z

    new-instance v5, Lcom/android/systemui/newstatusbar/data/TextData;

    const-string v6, "battery_percent"

    invoke-direct {v5, p1, v6}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    invoke-virtual {v5, v0}, Lcom/android/systemui/newstatusbar/data/TextData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v5, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$1;

    invoke-direct {v5, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)V

    invoke-virtual {v0, v5}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/TextData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentData:Lcom/android/systemui/newstatusbar/data/TextData;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;

    const-string v5, "battery_percent_mark"

    invoke-direct {v0, p1, v5}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/TextData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$2;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$2;-><init>(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/TextData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->markData:Lcom/android/systemui/newstatusbar/data/TextData;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    const-string v1, "batteryview"

    invoke-direct {v0, p1, v1}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$3;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$3;-><init>(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/IconData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->batteryData:Lcom/android/systemui/newstatusbar/data/IconData;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    const-string v1, "battery_charge"

    invoke-direct {v0, p1, v1}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    new-array v1, v4, [Ljava/lang/String;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/IconData;->addKeys([Ljava/lang/String;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$4;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$4;-><init>(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/data/Data;->addListener(Lcom/android/systemui/newstatusbar/data/Data$OnDataChangeListener;)Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/Data;->update()Lcom/android/systemui/newstatusbar/data/Data;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/data/IconData;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->chargeData:Lcom/android/systemui/newstatusbar/data/IconData;

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$5;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$5;-><init>(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)V

    invoke-direct {v0, p0, v3, v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver$onChangeListener;)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updatePercentData()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateBatteryData()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateMarkData()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->postUpdateAfterStart()V

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updatePercentData()V

    return-void
.end method

.method static synthetic access$100(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentOut:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$200(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentLayout:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$300(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->otherIcon:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$400(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateMarkData()V

    return-void
.end method

.method static synthetic access$500(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentMark:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$600(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateBatteryData()V

    return-void
.end method

.method static synthetic access$700(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$800(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Ljava/util/ArrayList;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->chargeIcon:Ljava/util/ArrayList;

    return-object v0
.end method

.method static synthetic access$900(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;)Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->markData:Lcom/android/systemui/newstatusbar/data/TextData;

    return-object v0
.end method

.method private addOnBatteryLevelChanged(Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->isAddOnBatteryLevelChanged:Z

    if-nez v0, :cond_10

    iget-object v0, p1, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryController:Lcom/android/systemui/statusbar/policy/BatteryController;

    if-eqz v0, :cond_10

    iget-object v0, p1, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;->mBatteryController:Lcom/android/systemui/statusbar/policy/BatteryController;

    invoke-interface {v0, p0}, Lcom/android/systemui/statusbar/policy/BatteryController;->addCallback(Ljava/lang/Object;)V

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->isAddOnBatteryLevelChanged:Z

    :cond_10
    return-void
.end method

.method private getKeyMarkToLevel(I)Ljava/lang/String;
    .registers 4

    const/16 v0, 0x64

    if-ne p1, v0, :cond_7

    const-string v0, "text_bat_color_mark_4"

    goto :goto_1c

    :cond_7
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "text_bat_color_mark_"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    div-int/lit8 v1, p1, 0x14

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    :goto_1c
    return-object v0
.end method

.method private getKeyToLevel(I)Ljava/lang/String;
    .registers 4

    const/16 v0, 0x64

    if-ne p1, v0, :cond_7

    const-string v0, "text_bat_color_4"

    goto :goto_1c

    :cond_7
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "text_bat_color_"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    div-int/lit8 v1, p1, 0x14

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    :goto_1c
    return-object v0
.end method

.method private postUpdateAfterStart()V
    .registers 5

    new-instance v0, Landroid/os/Handler;

    invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;

    move-result-object v1

    invoke-direct {v0, v1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;

    invoke-direct {v1, p0, v0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController$6;-><init>(Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;Landroid/os/Handler;)V

    const-wide/16 v2, 0x3e8

    invoke-virtual {v0, v1, v2, v3}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void
.end method

.method private updateBatteryData()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->batteryData:Lcom/android/systemui/newstatusbar/data/IconData;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    const-string v0, "battery_percent_digit_color"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentDigitColor:I

    const-string v0, "battery_percent_digit_zoom"

    const v1, 0x18

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentDigitZoom:I

    return-void
.end method

.method private updateMarkData()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->markData:Lcom/android/systemui/newstatusbar/data/TextData;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->currLevelMark:Ljava/lang/String;

    const/4 v2, 0x0

    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I

    return-void
.end method

.method private updatePercentData()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentData:Lcom/android/systemui/newstatusbar/data/TextData;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    const/4 v2, 0x0

    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I

    return-void
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
    .registers 3

    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;

    if-eqz v0, :cond_10

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->otherIcon:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    move-object v0, p1

    check-cast v0, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->addOnBatteryLevelChanged(Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;)V

    goto :goto_3d

    :cond_10
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;

    if-eqz v0, :cond_1a

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentMark:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_3d

    :cond_1a
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/PercentOutView;

    if-eqz v0, :cond_24

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentOut:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_3d

    :cond_24
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/BatteryChargeView;

    if-eqz v0, :cond_2e

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->chargeIcon:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_3d

    :cond_2e
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;

    if-eqz v0, :cond_38

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentLayout:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_3d

    :cond_38
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :goto_3d
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;

    if-eqz v0, :cond_44

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->postUpdateAfterStart()V

    :cond_44
    return-void
.end method

.method public bridge synthetic addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public getIconData(Z)Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 3

    if-eqz p1, :cond_5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->batteryData:Lcom/android/systemui/newstatusbar/data/IconData;

    goto :goto_7

    :cond_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->chargeData:Lcom/android/systemui/newstatusbar/data/IconData;

    :goto_7
    return-object v0
.end method

.method public getPercentDigitColor()I
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentDigitColor:I

    return v0
.end method

.method public getPercentDigitZoom()I
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentDigitZoom:I

    return v0
.end method

.method public getTextData(Z)Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 3

    if-eqz p1, :cond_5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentData:Lcom/android/systemui/newstatusbar/data/TextData;

    goto :goto_7

    :cond_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->markData:Lcom/android/systemui/newstatusbar/data/TextData;

    :goto_7
    return-object v0
.end method

.method public onBatteryLevelChanged(IZZ)V
    .registers 6

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getKeyToLevel(I)Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_23

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getKeyToLevel(I)Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updatePercentData()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateBatteryData()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentOut:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    goto :goto_3d

    :cond_23
    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getKeyMarkToLevel(I)Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->currLevelMark:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_3d

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->getKeyMarkToLevel(I)Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->currLevelMark:Ljava/lang/String;

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateMarkData()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentMark:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    :cond_3d
    :goto_3d
    return-void
.end method

.method public onDataChanged(Ljava/lang/String;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    invoke-virtual {p1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_10

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateBatteryData()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    :cond_10
    return-void
.end method

.method public removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
    .registers 3

    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/MiuiBatteryMeterView;

    if-eqz v0, :cond_a

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->otherIcon:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_37

    :cond_a
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/PercentMarkView;

    if-eqz v0, :cond_14

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentMark:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_37

    :cond_14
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/PercentOutView;

    if-eqz v0, :cond_1e

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentOut:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_37

    :cond_1e
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/BatteryChargeView;

    if-eqz v0, :cond_28

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->chargeIcon:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_37

    :cond_28
    instance-of v0, p1, Lcom/android/systemui/newstatusbar/battery/BatteryPercentContainer;

    if-eqz v0, :cond_32

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->percentLayout:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_37

    :cond_32
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    :goto_37
    return-void
.end method

.method public bridge synthetic removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/BatteryColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_BatteryColorSizeController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
