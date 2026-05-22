"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/UpdateLayoutController.smali'
CLASS_FALLBACK_NAMES = ['UpdateLayoutController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$CallBack;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$CallBack;",
        ">;"
    }
.end annotation


# instance fields
.field private changed:Z

.field private elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

.field private final handler:Landroid/os/Handler;

.field private final layoutListener:Landroid/view/View$OnLayoutChangeListener;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 4

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    new-instance v0, Landroid/os/Handler;

    invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;

    move-result-object v1

    invoke-direct {v0, v1}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->handler:Landroid/os/Handler;

    new-instance v0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$1;

    invoke-direct {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->layoutListener:Landroid/view/View$OnLayoutChangeListener;

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->changed:Z

    return-void
.end method

.method static synthetic access$000(Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;)Lcom/android/systemui/newstatusbar/controllers/ElementController;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    return-object v0
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

    const-wide/high16 v6, 0x4014000000000000L  # 5.0

    cmpl-double v2, v4, v6

    if-ltz v2, :cond_20

    goto :goto_21

    :cond_20
    const/4 v3, 0x0

    :goto_21
    return v3
.end method


# virtual methods
.method public getLayoutListener()Landroid/view/View$OnLayoutChangeListener;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->layoutListener:Landroid/view/View$OnLayoutChangeListener;

    return-object v0
.end method

.method isChange(IIIIIIII)Z
    .registers 15

    goto/32 :goto_4

    nop

    :goto_4
    sub-int v0, p3, p1

    goto/32 :goto_60

    nop

    :goto_a
    int-to-float v4, v0

    goto/32 :goto_29

    nop

    :goto_f
    int-to-float v5, v3

    goto/32 :goto_14

    nop

    :goto_14
    invoke-direct {p0, v4, v5}, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->compare(FF)Z

    move-result v4

    goto/32 :goto_57

    nop

    :goto_1c
    const/4 v4, 0x1

    :goto_1d
    goto/32 :goto_66

    nop

    :goto_21
    invoke-direct {p0, v4, v5}, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->compare(FF)Z

    move-result v4

    goto/32 :goto_38

    nop

    :goto_29
    int-to-float v5, v1

    goto/32 :goto_21

    nop

    :goto_2e
    const/4 v4, 0x0

    goto/32 :goto_33

    nop

    :goto_33
    goto :goto_1d

    :goto_34
    goto/32 :goto_1c

    nop

    :goto_38
    if-eqz v4, :cond_3d

    goto/32 :goto_34

    :cond_3d
    goto/32 :goto_4c

    nop

    :goto_41
    goto :goto_34

    :goto_42
    goto/32 :goto_2e

    nop

    :goto_46
    sub-int v2, p4, p2

    goto/32 :goto_51

    nop

    :goto_4c
    int-to-float v4, v2

    goto/32 :goto_f

    nop

    :goto_51
    sub-int v3, p8, p6

    goto/32 :goto_a

    nop

    :goto_57
    if-nez v4, :cond_5c

    goto/32 :goto_42

    :cond_5c
    goto/32 :goto_41

    nop

    :goto_60
    sub-int v1, p7, p5

    goto/32 :goto_46

    nop

    :goto_66
    return v4
.end method

.method public setElementController(Lcom/android/systemui/newstatusbar/controllers/ElementController;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->elementController:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_UpdateLayoutController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
