"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/SingleLayout.smali'
CLASS_FALLBACK_NAMES = ['SingleLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/SingleLayout;
.super Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;


# static fields
.field private static final TAG:Ljava/lang/String;

.field private static final priorArray:[Ljava/lang/String;


# instance fields
.field private final iconSize:I

.field private isCenterEnableByIsland:Z

.field public isHideInPromptVisible:Z

.field private final longClick:Ljava/lang/Runnable;

.field private mChild:Landroid/view/View;

.field private mClockView:Landroid/view/View;

.field private mName:Ljava/lang/String;

.field private mPosition:I

.field private mPrior:I

.field private mVisible:Z

.field private mWidth:I


# direct methods
.method static constructor <clinit>()V
    .registers 12

    const-class v0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    invoke-virtual {v0}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->TAG:Ljava/lang/String;

    const-string v1, "elem_clock"

    const-string v2, "elem_net1"

    const-string v3, "elem_net2"

    const-string v4, "elem_bat"

    const-string v5, "elem_wifi"

    const-string v6, "elem_speed"

    const-string v7, "elem_date"

    const-string v8, "elem_status"

    const-string v9, "elem_weather"

    const-string v10, "fullscreen_notification_icon_area"

    const-string v11, "elem_prompt"

    filled-new-array/range {v1 .. v11}, [Ljava/lang/String;

    move-result-object v0

    sput-object v0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->priorArray:[Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, -0x5

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mWidth:I

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->isCenterEnableByIsland:Z

    new-instance v0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout$1;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout$1;-><init>(Lcom/android/systemui/newstatusbar/layouts/SingleLayout;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->longClick:Ljava/lang/Runnable;

    invoke-virtual {p1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    const-string v1, "status_bar_icon_height"

    invoke-static {p1, v1}, Landroid/Utils/Utils;->DimenToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getDimensionPixelSize(I)I

    move-result v0

    div-int/lit8 v1, v0, 0x3

    add-int/2addr v1, v0

    iput v1, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->iconSize:I

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/layouts/SingleLayout;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->startActivityOnClkick()V

    return-void
.end method

.method private compare(FF)Z
    .registers 11

    add-float v0, p1, p2

    const/high16 v1, 0x40000000  # 2.0f

    div-float/2addr v0, v1

    float-to-double v0, v0

    const-wide/16 v2, 0x0

    cmpl-double v2, v0, v2

    const/4 v3, 0x1

    if-nez v2, :cond_e

    return v3

    :cond_e
    sub-float v2, p1, p2

    float-to-double v4, v2

    div-double/2addr v4, v0

    invoke-static {v4, v5}, Ljava/lang/Math;->abs(D)D

    move-result-wide v4

    const-wide/high16 v6, 0x4059000000000000L  # 100.0

    mul-double/2addr v4, v6

    const-wide/high16 v6, 0x4000000000000000L  # 2.0

    cmpl-double v2, v4, v6

    if-ltz v2, :cond_20

    goto :goto_21

    :cond_20
    const/4 v3, 0x0

    :goto_21
    return v3
.end method

.method private findChild()V
    .registers 2

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getChildCount()I

    move-result v0

    if-lez v0, :cond_d

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mChild:Landroid/view/View;

    :cond_d
    return-void
.end method

.method private getIntentForName()Landroid/content/Intent;
    .registers 8

    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    const-string v1, "miui.intent.action.Elem_"

    const-string v2, ""

    const-string v3, ""

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    sget-object v5, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->priorArray:[Ljava/lang/String;

    const/4 v6, 0x0

    aget-object v6, v5, v6

    invoke-virtual {v4, v6}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_31

    const-string v2, "com.android.settings.statusbarelement.StatusBarElementClock"

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, "0"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v3, "Часы"

    goto/16 :goto_142

    :cond_31
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const/4 v6, 0x1

    aget-object v6, v5, v6

    invoke-virtual {v4, v6}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_12b

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const/4 v6, 0x2

    aget-object v6, v5, v6

    invoke-virtual {v4, v6}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_12b

    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const/4 v6, 0x3

    aget-object v6, v5, v6

    invoke-virtual {v4, v6}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_54

    goto/16 :goto_12b

    :cond_54
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const/4 v6, 0x4

    aget-object v6, v5, v6

    invoke-virtual {v4, v6}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_78

    const-string v2, "com.android.settings.statusbarelement.StatusBarElementSpeed"

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, "3"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v3, "Скорость подключения"

    goto/16 :goto_142

    :cond_78
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const/4 v6, 0x5

    aget-object v6, v5, v6

    invoke-virtual {v4, v6}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_9c

    const-string v2, "com.android.settings.statusbarelement.StatusBarElementDate"

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, "6"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v3, "Настройки даты"

    goto/16 :goto_142

    :cond_9c
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const/4 v6, 0x6

    aget-object v6, v5, v6

    invoke-virtual {v4, v6}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_c0

    const-string v2, "com.android.settings.statusbarelement.StatusBarElementBat"

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, "1"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v3, "Батарея"

    goto/16 :goto_142

    :cond_c0
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const/4 v6, 0x7

    aget-object v6, v5, v6

    invoke-virtual {v4, v6}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_e3

    const-string v2, "com.android.settings.statusbarelement.StatusBarElementStatus"

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, "5"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v3, "Иконки статусов"

    goto :goto_142

    :cond_e3
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const/16 v6, 0x8

    aget-object v6, v5, v6

    invoke-virtual {v4, v6}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_107

    const-string v2, "com.android.settings.statusbarelement.StatusBarElementWeather"

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, "4"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v3, "Погода в строке состояния"

    goto :goto_142

    :cond_107
    iget-object v4, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const/16 v6, 0x9

    aget-object v5, v5, v6

    invoke-virtual {v4, v5}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_142

    const-string v2, "com.android.settings.statusbarelement.StatusBarElementNotif"

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, "7"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v3, "Настройки уведомлений"

    goto :goto_142

    :cond_12b
    :goto_12b
    const-string v2, "com.android.settings.statusbarelement.StatusBarElementNet"

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v5, "2"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v3, "Иконки сети"

    :cond_142
    :goto_142
    const-string v4, ":settings:show_fragment"

    invoke-virtual {v0, v4, v2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    const-string v4, ":settings:show_fragment_title"

    invoke-virtual {v0, v4, v3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {v0, v1}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;

    return-object v0
.end method

.method private getPriorforName(Ljava/lang/String;)I
    .registers 5

    sget-object v0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->priorArray:[Ljava/lang/String;

    const/4 v1, 0x0

    :goto_3
    array-length v2, v0

    if-ge v1, v2, :cond_12

    aget-object v2, v0, v1

    invoke-virtual {v2, p1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_f

    return v1

    :cond_f
    add-int/lit8 v1, v1, 0x1

    goto :goto_3

    :cond_12
    const/16 v1, 0xa

    return v1
.end method

.method private initial()V
    .registers 3

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getId()I

    move-result v1

    invoke-virtual {v0, v1}, Landroid/content/res/Resources;->getResourceName(I)Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const-string v1, "/"

    invoke-virtual {v0, v1}, Ljava/lang/String;->indexOf(Ljava/lang/String;)I

    move-result v1

    add-int/lit8 v1, v1, 0x1

    invoke-virtual {v0, v1}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPriorforName(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mPrior:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->updateVisibility()V

    return-void
.end method

.method private isEnableAnim()Z
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const-string v1, "elem_status"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_17

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const-string v1, "fullscreen_notification_icon_area"

    invoke-virtual {v1, v0}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_15

    goto :goto_17

    :cond_15
    const/4 v0, 0x0

    goto :goto_18

    :cond_17
    :goto_17
    const/4 v0, 0x1

    :goto_18
    return v0
.end method

.method private isNotif()Z
    .registers 4

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getId()I

    move-result v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "fullscreen_notification_icon_area"

    invoke-static {v1, v2}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    if-ne v0, v1, :cond_12

    const/4 v0, 0x1

    goto :goto_13

    :cond_12
    const/4 v0, 0x0

    :goto_13
    return v0
.end method

.method private startActivityOnClkick()V
    .registers 4

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->performHapticFeedback(I)Z

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getIntentForName()Landroid/content/Intent;

    move-result-object v0

    const-string v1, "com.android.settings"

    const-string v2, "com.android.settings.wifi.WifiPickerActivity"

    invoke-virtual {v0, v1, v2}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    const-class v1, Lcom/android/systemui/plugins/ActivityStarter;

    invoke-static {v1}, Lcom/android/systemui/SysDependency;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/plugins/ActivityStarter;

    const/4 v2, 0x1

    invoke-interface {v1, v0, v2}, Lcom/android/systemui/plugins/ActivityStarter;->startActivity(Landroid/content/Intent;Z)V

    return-void
.end method


# virtual methods
.method public addView(Landroid/view/View;)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->addView(Landroid/view/View;)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->findChild()V

    return-void
.end method

.method public asView()Lcom/android/systemui/newstatusbar/layouts/SingleLayout;
    .registers 1
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">()TT;"
        }
    .end annotation

    return-object p0
.end method

.method public getAddedChild()Landroid/view/View;
    .registers 4

    instance-of v0, p0, Lcom/android/systemui/newstatusbar/layouts/TransferMobileLayout;

    if-eqz v0, :cond_5

    return-object p0

    :cond_5
    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    instance-of v2, v1, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;

    if-eqz v2, :cond_15

    move-object v2, v1

    check-cast v2, Landroid/view/ViewGroup;

    invoke-virtual {v2, v0}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    :cond_15
    return-object v1
.end method

.method public getElementName()Ljava/lang/String;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    return-object v0
.end method

.method public getLayoutWidth()I
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mVisible:Z

    if-eqz v0, :cond_d

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->isVisibleByPlaceCalculation()Z

    move-result v0

    if-eqz v0, :cond_d

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mWidth:I

    goto :goto_e

    :cond_d
    const/4 v0, 0x0

    :goto_e
    return v0
.end method

.method public getPosition()I
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mPosition:I

    return v0
.end method

.method public getPrior()I
    .registers 2

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mPrior:I

    return v0
.end method

.method public getRealMeasuredWidth()I
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mVisible:Z

    if-eqz v0, :cond_24

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mChild:Landroid/view/View;

    if-eqz v0, :cond_24

    instance-of v1, v0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;

    if-eqz v1, :cond_19

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->getRealMeasuredWidth()I

    move-result v0

    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->leftMargin:I

    add-int/2addr v0, v1

    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->rightMargin:I

    add-int/2addr v0, v1

    goto :goto_23

    :cond_19
    invoke-virtual {v0}, Landroid/view/View;->getMeasuredWidth()I

    move-result v0

    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->leftMargin:I

    add-int/2addr v0, v1

    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->rightMargin:I

    add-int/2addr v0, v1

    :goto_23
    return v0

    :cond_24
    const/4 v0, 0x0

    return v0
.end method

.method isChange(IIII)Z
    .registers 7

    goto/32 :goto_25

    nop

    :goto_4
    int-to-float v0, p4

    goto/32 :goto_18

    nop

    :goto_9
    int-to-float v1, v1

    goto/32 :goto_33

    nop

    :goto_e
    const/4 v0, 0x1

    :goto_f
    goto/32 :goto_8f

    nop

    :goto_13
    goto :goto_f

    :goto_14
    goto/32 :goto_e

    nop

    :goto_18
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getBottom()I

    move-result v1

    goto/32 :goto_6b

    nop

    :goto_20
    int-to-float v0, p3

    goto/32 :goto_48

    nop

    :goto_25
    int-to-float v0, p1

    goto/32 :goto_9e

    nop

    :goto_2a
    if-eqz v0, :cond_2f

    goto/32 :goto_14

    :cond_2f
    goto/32 :goto_20

    nop

    :goto_33
    invoke-direct {p0, v0, v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->compare(FF)Z

    move-result v0

    goto/32 :goto_62

    nop

    :goto_3b
    invoke-direct {p0, v0, v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->compare(FF)Z

    move-result v0

    goto/32 :goto_7e

    nop

    :goto_43
    const/4 v0, 0x0

    goto/32 :goto_13

    nop

    :goto_48
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getRight()I

    move-result v1

    goto/32 :goto_9

    nop

    :goto_50
    int-to-float v1, v1

    goto/32 :goto_3b

    nop

    :goto_55
    int-to-float v0, p2

    goto/32 :goto_90

    nop

    :goto_5a
    invoke-direct {p0, v0, v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->compare(FF)Z

    move-result v0

    goto/32 :goto_70

    nop

    :goto_62
    if-eqz v0, :cond_67

    goto/32 :goto_14

    :cond_67
    goto/32 :goto_4

    nop

    :goto_6b
    int-to-float v1, v1

    goto/32 :goto_5a

    nop

    :goto_70
    if-nez v0, :cond_75

    goto/32 :goto_9a

    :cond_75
    goto/32 :goto_98

    nop

    :goto_79
    int-to-float v1, v1

    goto/32 :goto_87

    nop

    :goto_7e
    if-eqz v0, :cond_83

    goto/32 :goto_14

    :cond_83
    goto/32 :goto_55

    nop

    :goto_87
    invoke-direct {p0, v0, v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->compare(FF)Z

    move-result v0

    goto/32 :goto_2a

    nop

    :goto_8f
    return v0

    :goto_90
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getTop()I

    move-result v1

    goto/32 :goto_79

    nop

    :goto_98
    goto/16 :goto_14

    :goto_9a
    goto/32 :goto_43

    nop

    :goto_9e
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getLeft()I

    move-result v1

    goto/32 :goto_50

    nop
.end method

.method public isVisibleByPlaceCalculation()Z
    .registers 3

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mWidth:I

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getRealMeasuredWidth()I

    move-result v1

    if-ge v0, v1, :cond_17

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->isEnableAnim()Z

    move-result v0

    if-eqz v0, :cond_15

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mWidth:I

    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->iconSize:I

    if-le v0, v1, :cond_15

    goto :goto_17

    :cond_15
    const/4 v0, 0x0

    goto :goto_18

    :cond_17
    :goto_17
    const/4 v0, 0x1

    :goto_18
    return v0
.end method

.method protected onFinishInflate()V
    .registers 1

    goto/32 :goto_13

    nop

    :goto_4
    return-void

    :goto_5
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->initial()V

    goto/32 :goto_4

    nop

    :goto_c
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->findChild()V

    goto/32 :goto_5

    nop

    :goto_13
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->onFinishInflate()V

    goto/32 :goto_c

    nop
.end method

.method public onViewAdded(Landroid/view/View;)V
    .registers 2

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->onViewAdded(Landroid/view/View;)V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->findChild()V

    return-void
.end method

.method public preLayout(IIII)V
    .registers 6

    invoke-virtual {p0, p1, p2, p3, p4}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->isChange(IIII)Z

    move-result v0

    if-nez v0, :cond_c

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->isLayoutRequested()Z

    move-result v0

    if-eqz v0, :cond_f

    :cond_c
    invoke-virtual {p0, p1, p2, p3, p4}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->layout(IIII)V

    :cond_f
    return-void
.end method

.method public resetLongClick()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->longClick:Ljava/lang/Runnable;

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->removeCallbacks(Ljava/lang/Runnable;)Z

    return-void
.end method

.method public setCenterEnableByIsland(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->isCenterEnableByIsland:Z

    return-void
.end method

.method public setMaxMeasureWidth(I)V
    .registers 5

    iget v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mWidth:I

    if-eq v0, p1, :cond_10

    const/16 v0, 0x7d0

    if-ne p1, v0, :cond_d

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getRealMeasuredWidth()I

    move-result v0

    goto :goto_e

    :cond_d
    move v0, p1

    :goto_e
    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mWidth:I

    :cond_10
    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->isEnableAnim()Z

    move-result v0

    if-eqz v0, :cond_28

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mChild:Landroid/view/View;

    instance-of v1, v0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;

    if-eqz v1, :cond_28

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;

    iget v1, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->leftMargin:I

    sub-int v1, p1, v1

    iget v2, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->rightMargin:I

    sub-int/2addr v1, v2

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->setWidth(I)V

    :cond_28
    return-void
.end method

.method public setPosition(I)V
    .registers 3

    iput p1, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mPosition:I

    if-nez p1, :cond_b

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->bringToFront()V

    const/4 v0, 0x0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mPrior:I

    goto :goto_13

    :cond_b
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    invoke-direct {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPriorforName(Ljava/lang/String;)I

    move-result v0

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mPrior:I

    :goto_13
    return-void
.end method

.method public setVisibility(I)V
    .registers 3

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mVisible:Z

    if-nez v0, :cond_6

    const/16 p1, 0x8

    :cond_6
    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/layouts/ElementBgLayout;->setVisibility(I)V

    return-void
.end method

.method public updateVisibility()V
    .registers 4

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mName:Ljava/lang/String;

    const-string v1, "elem_net1"

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-nez v1, :cond_12

    const-string v1, "elem_net2"

    invoke-virtual {v0, v1}, Ljava/lang/String;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_14

    :cond_12
    const-string v0, "elem_net"

    :cond_14
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "_element_visible"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x1

    invoke-static {v1, v2}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings(Ljava/lang/String;I)Z

    move-result v1

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->mVisible:Z

    if-eqz v1, :cond_32

    const/4 v1, 0x0

    goto :goto_34

    :cond_32
    const/16 v1, 0x8

    :goto_34
    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->setVisibility(I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_SingleLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
