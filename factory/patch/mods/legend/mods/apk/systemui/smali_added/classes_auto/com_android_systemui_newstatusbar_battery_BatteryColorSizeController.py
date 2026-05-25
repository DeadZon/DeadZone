"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/battery/BatteryColorSizeController.smali'
CLASS_FALLBACK_NAMES = ['BatteryColorSizeController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;
.super Lcom/android/systemui/newstatusbar/controllers/IconController;

# interfaces
.implements Lcom/android/systemui/statusbar/policy/BatteryController$BatteryStateChangeCallback;


# static fields
.field public static TAG:Ljava/lang/String;

.field private static final sKeys:[Ljava/lang/String;


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

.field private final iDs:[I

.field private final inData:Lcom/android/systemui/newstatusbar/data/TextData;

.field private final outData:Lcom/android/systemui/newstatusbar/data/TextData;

.field private final percentIn:Ljava/util/ArrayList;
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


# direct methods
.method static constructor <clinit>()V
    .registers 5

    const-class v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;

    invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->TAG:Ljava/lang/String;

    const-string v0, "batteryview_zoom"

    const-string v1, "battery_percent_zoom"

    const-string v2, "battery_charge_color"

    const-string v3, "battery_percent_digit_color"

    const-string v4, "text_bat_color"

    filled-new-array {v0, v1, v2, v3, v4}, [Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->sKeys:[Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IconController;-><init>(Landroid/content/Context;)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->percentOut:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->percentIn:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->chargeIcon:Ljava/util/ArrayList;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;

    const-string v1, "battery_percent"

    invoke-direct {v0, v1}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Ljava/lang/String;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->outData:Lcom/android/systemui/newstatusbar/data/TextData;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/TextData;

    const-string v1, "battery_percent_digit"

    invoke-direct {v0, v1}, Lcom/android/systemui/newstatusbar/data/TextData;-><init>(Ljava/lang/String;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->inData:Lcom/android/systemui/newstatusbar/data/TextData;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    const-string v1, "batteryview"

    invoke-direct {v0, v1}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Ljava/lang/String;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->batteryData:Lcom/android/systemui/newstatusbar/data/IconData;

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    const-string v1, "battery_charge"

    invoke-direct {v0, v1}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Ljava/lang/String;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->chargeData:Lcom/android/systemui/newstatusbar/data/IconData;

    const/4 v0, 0x6

    new-array v0, v0, [I

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->iDs:[I

    const-string v0, ""

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    const-class v0, Lcom/android/systemui/statusbar/policy/BatteryController;

    invoke-static {v0}, Lcom/android/systemui/SysDependency;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/statusbar/policy/BatteryController;

    invoke-interface {v0, p0}, Lcom/android/systemui/statusbar/policy/BatteryController;->addCallback(Ljava/lang/Object;)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateOutData()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateBatteryData()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateChargeData()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateInData()V

    return-void
.end method

.method private getId(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)I
    .registers 3

    move-object v0, p1

    check-cast v0, Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getId()I

    move-result v0

    return v0
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

.method private updateBatteryData()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->batteryData:Lcom/android/systemui/newstatusbar/data/IconData;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/IconData;->update()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    return-void
.end method

.method private updateChargeData()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->chargeData:Lcom/android/systemui/newstatusbar/data/IconData;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/IconData;->update()V

    return-void
.end method

.method private updateIdsArray(Landroid/content/Context;)V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->iDs:[I

    const-string v1, "battery_percentage_view"

    invoke-static {p1, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    const/4 v2, 0x0

    aput v1, v0, v2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->iDs:[I

    const-string v1, "battery_left_percentage_view"

    invoke-static {p1, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    const/4 v2, 0x1

    aput v1, v0, v2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->iDs:[I

    const-string v1, "battery_charge_out_image"

    invoke-static {p1, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    const/4 v2, 0x2

    aput v1, v0, v2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->iDs:[I

    const-string v1, "battery_charge_image"

    invoke-static {p1, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    const/4 v2, 0x3

    aput v1, v0, v2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->iDs:[I

    const-string v1, "battery_image"

    invoke-static {p1, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    const/4 v2, 0x4

    aput v1, v0, v2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->iDs:[I

    const-string v1, "battery_digit"

    invoke-static {p1, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    const/4 v2, 0x5

    aput v1, v0, v2

    return-void
.end method

.method private updateInData()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->inData:Lcom/android/systemui/newstatusbar/data/TextData;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->update()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->inData:Lcom/android/systemui/newstatusbar/data/TextData;

    const/4 v1, 0x0

    iput-boolean v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->shadow_enable:Z

    return-void
.end method

.method private updateOutData()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->outData:Lcom/android/systemui/newstatusbar/data/TextData;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/TextData;->update()V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    const/4 v2, 0x0

    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/TextData;->color:I

    return-void
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->iDs:[I

    const/4 v1, 0x0

    aget v0, v0, v1

    if-nez v0, :cond_11

    move-object v0, p1

    check-cast v0, Landroid/view/View;

    invoke-virtual {v0}, Landroid/view/View;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateIdsArray(Landroid/content/Context;)V

    :cond_11
    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->getId(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)I

    move-result v0

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->iDs:[I

    aget v1, v2, v1

    if-eq v0, v1, :cond_43

    const/4 v1, 0x1

    aget v1, v2, v1

    if-ne v0, v1, :cond_21

    goto :goto_43

    :cond_21
    const/4 v1, 0x2

    aget v1, v2, v1

    if-eq v0, v1, :cond_3d

    const/4 v1, 0x3

    aget v1, v2, v1

    if-ne v0, v1, :cond_2c

    goto :goto_3d

    :cond_2c
    const/4 v1, 0x4

    aget v1, v2, v1

    if-ne v0, v1, :cond_37

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_48

    :cond_37
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->percentIn:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_48

    :cond_3d
    :goto_3d
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->chargeIcon:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_48

    :cond_43
    :goto_43
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->percentOut:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :goto_48
    return-void
.end method

.method public bridge synthetic addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public getIconData(Z)Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 3

    if-eqz p1, :cond_5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->batteryData:Lcom/android/systemui/newstatusbar/data/IconData;

    goto :goto_7

    :cond_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->chargeData:Lcom/android/systemui/newstatusbar/data/IconData;

    :goto_7
    return-object v0
.end method

.method public getTextData(Z)Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 3

    if-eqz p1, :cond_5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->outData:Lcom/android/systemui/newstatusbar/data/TextData;

    goto :goto_7

    :cond_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->inData:Lcom/android/systemui/newstatusbar/data/TextData;

    :goto_7
    return-object v0
.end method

.method public onBatteryLevelChanged(IZZ)V
    .registers 6

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->getKeyToLevel(I)Ljava/lang/String;

    move-result-object v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_1a

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->getKeyToLevel(I)Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->currLevel:Ljava/lang/String;

    sget-object v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->sKeys:[Ljava/lang/String;

    const/4 v1, 0x4

    aget-object v0, v0, v1

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->onCustomChanged(Ljava/lang/String;)V

    :cond_1a
    return-void
.end method

.method public onCustomChanged(Ljava/lang/String;)V
    .registers 4

    sget-object v0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->sKeys:[Ljava/lang/String;

    invoke-static {v0}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v1

    invoke-interface {v1, p1}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_64

    const/4 v1, 0x0

    aget-object v1, v0, v1

    invoke-virtual {v1, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_1e

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateBatteryData()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    goto :goto_64

    :cond_1e
    const/4 v1, 0x1

    aget-object v1, v0, v1

    invoke-virtual {v1, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_30

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateOutData()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->percentOut:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    goto :goto_64

    :cond_30
    const/4 v1, 0x2

    aget-object v1, v0, v1

    invoke-virtual {v1, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_42

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateChargeData()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->chargeIcon:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    goto :goto_64

    :cond_42
    const/4 v1, 0x3

    aget-object v0, v0, v1

    invoke-virtual {v0, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_54

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateInData()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->percentIn:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    goto :goto_64

    :cond_54
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateOutData()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateBatteryData()V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->percentOut:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->updateCallBacks(Ljava/util/ArrayList;)V

    :cond_64
    :goto_64
    return-void
.end method

.method public removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
    .registers 5

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->getId(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)I

    move-result v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->iDs:[I

    const/4 v2, 0x0

    aget v2, v1, v2

    if-eq v0, v2, :cond_33

    const/4 v2, 0x1

    aget v2, v1, v2

    if-ne v0, v2, :cond_11

    goto :goto_33

    :cond_11
    const/4 v2, 0x2

    aget v2, v1, v2

    if-eq v0, v2, :cond_2d

    const/4 v2, 0x3

    aget v2, v1, v2

    if-ne v0, v2, :cond_1c

    goto :goto_2d

    :cond_1c
    const/4 v2, 0x4

    aget v1, v1, v2

    if-ne v0, v1, :cond_27

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->batteryIcon:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_38

    :cond_27
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->percentIn:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_38

    :cond_2d
    :goto_2d
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->chargeIcon:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    goto :goto_38

    :cond_33
    :goto_33
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->percentOut:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    :goto_38
    return-void
.end method

.method public bridge synthetic removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/battery/BatteryColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_battery_BatteryColorSizeController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
