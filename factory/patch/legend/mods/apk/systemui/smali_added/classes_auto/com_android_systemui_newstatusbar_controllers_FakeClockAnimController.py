"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/FakeClockAnimController.smali'
CLASS_FALLBACK_NAMES = ['FakeClockAnimController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;,
        Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;",
        ">;"
    }
.end annotation


# static fields
.field static final REFRESH_EXPAND:I = 0x1f6

.field static final REFRESH_STATUS:I = 0x1f5

.field static TAG:Ljava/lang/String;


# instance fields
.field private expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

.field private final expandCoor:[I

.field private expandSize:F

.field private final handler:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;

.field private isValid:Z

.field private statusClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

.field private final statusCoor:[I

.field private statusSize:F

.field private final tmpExpandCoor:[I


# direct methods
.method static constructor <clinit>()V
    .registers 1

    const-string v0, "Nastya_super_porn"

    sput-object v0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->TAG:Ljava/lang/String;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->isValid:Z

    const/4 v0, 0x2

    new-array v1, v0, [I

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->statusCoor:[I

    new-array v1, v0, [I

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandCoor:[I

    new-array v0, v0, [I

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->tmpExpandCoor:[I

    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;-><init>(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->handler:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)Lcom/android/systemui/newstatusbar/clock/ClockLayout;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->statusClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    return-object v0
.end method

.method static synthetic access$100(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->getLocStatus()V

    return-void
.end method

.method static synthetic access$200(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->getLocExpand()V

    return-void
.end method

.method static synthetic access$302(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;F)F
    .registers 2

    iput p1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->statusSize:F

    return p1
.end method

.method static synthetic access$400(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)Landroid/content/Context;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->context:Landroid/content/Context;

    return-object v0
.end method

.method static synthetic access$500(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)Lcom/android/systemui/newstatusbar/clock/ClockLayout;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    return-object v0
.end method

.method static synthetic access$602(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;F)F
    .registers 2

    iput p1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandSize:F

    return p1
.end method

.method static synthetic access$700(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)Landroid/content/Context;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->context:Landroid/content/Context;

    return-object v0
.end method

.method static synthetic access$800(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->handler:Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$WorkHandler;

    return-object v0
.end method

.method private calculated(FFF)F
    .registers 7

    sub-float v0, p1, p2

    const/high16 v1, 0x43480000  # 200.0f

    div-float v1, p3, v1

    const/high16 v2, 0x3f800000  # 1.0f

    sub-float/2addr v2, v1

    mul-float/2addr v0, v2

    return v0
.end method

.method private getLocExpand()V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_29

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandCoor:[I

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getLocationInWindow([I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandCoor:[I

    const/4 v1, 0x0

    aget v2, v0, v1

    int-to-float v2, v2

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getTranslationX()F

    move-result v3

    sub-float/2addr v2, v3

    float-to-int v2, v2

    aput v2, v0, v1

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandCoor:[I

    const/4 v1, 0x1

    aget v2, v0, v1

    int-to-float v2, v2

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getTranslationY()F

    move-result v3

    sub-float/2addr v2, v3

    float-to-int v2, v2

    aput v2, v0, v1

    :cond_29
    return-void
.end method

.method private getLocStatus()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->statusClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_9

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->statusCoor:[I

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getLocationInWindow([I)V

    :cond_9
    return-void
.end method

.method public static startExpandAnimation(FZ)V
    .registers 3

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->onExpandAnimChange(F)V

    return-void
.end method


# virtual methods
.method public addCallBack(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;)V
    .registers 4

    invoke-interface {p1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;->isStatus()Z

    move-result v0

    if-eqz v0, :cond_15

    invoke-interface {p1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;->asView()Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->statusClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$1;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->post(Ljava/lang/Runnable;)Z

    goto :goto_23

    :cond_15
    invoke-interface {p1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;->asView()Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    new-instance v1, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$2;

    invoke-direct {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$2;-><init>(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;)V

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->post(Ljava/lang/Runnable;)Z

    :goto_23
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->statusClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_2d

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    if-eqz v0, :cond_2d

    const/4 v0, 0x1

    goto :goto_2e

    :cond_2d
    const/4 v0, 0x0

    :goto_2e
    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->isValid:Z

    return-void
.end method

.method public bridge synthetic addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;)V

    return-void
.end method

.method public onExpandAnimChange(F)V
    .registers 6

    const/4 v0, 0x0

    cmpg-float v0, p1, v0

    if-gez v0, :cond_6

    const/4 p1, 0x0

    :cond_6
    const/high16 v0, 0x43480000  # 200.0f

    cmpl-float v0, p1, v0

    if-lez v0, :cond_e

    const/high16 p1, 0x43480000  # 200.0f

    :cond_e
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->isValid:Z

    if-eqz v0, :cond_59

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    const/high16 v1, 0x42c80000  # 100.0f

    cmpg-float v1, p1, v1

    const/4 v2, 0x0

    if-gez v1, :cond_1d

    const/4 v1, 0x1

    goto :goto_1e

    :cond_1d
    move v1, v2

    :goto_1e
    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->refreshClockSettings(Z)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->tmpExpandCoor:[I

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getLocationOnScreen([I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->statusCoor:[I

    aget v0, v0, v2

    int-to-float v0, v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandCoor:[I

    aget v1, v1, v2

    int-to-float v1, v1

    invoke-direct {p0, v0, v1, p1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->calculated(FFF)F

    move-result v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->tmpExpandCoor:[I

    aget v1, v1, v2

    int-to-float v1, v1

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandCoor:[I

    aget v2, v3, v2

    int-to-float v2, v2

    iget-object v3, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    invoke-virtual {v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->getTranslationX()F

    move-result v3

    add-float/2addr v2, v3

    sub-float/2addr v1, v2

    add-float/2addr v0, v1

    iget v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->statusSize:F

    iget v2, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandSize:F

    invoke-direct {p0, v1, v2, p1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->calculated(FFF)F

    move-result v1

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    iget v3, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandSize:F

    add-float/2addr v3, v1

    invoke-virtual {v2, v3}, Lcom/android/systemui/newstatusbar/clock/ClockLayout;->setTextSizeWidthAnimation(F)V

    :cond_59
    return-void
.end method

.method public removeCallBack(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;)V
    .registers 4

    invoke-interface {p1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;->isStatus()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_a

    iput-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->statusClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    goto :goto_c

    :cond_a
    iput-object v1, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->expandClock:Lcom/android/systemui/newstatusbar/clock/ClockLayout;

    :goto_c
    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->isValid:Z

    return-void
.end method

.method public bridge synthetic removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController$CallBack;)V

    return-void
.end method

.method public updateLoc()V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->getLocExpand()V

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/controllers/FakeClockAnimController;->getLocStatus()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_FakeClockAnimController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
