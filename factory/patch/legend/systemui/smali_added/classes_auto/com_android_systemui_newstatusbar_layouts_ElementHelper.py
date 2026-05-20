"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/ElementHelper.smali'
CLASS_FALLBACK_NAMES = ['ElementHelper.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/ElementHelper;
.super Ljava/lang/Object;


# static fields
.field private static final ALL:I = 0x0

.field private static final LEFT:I = 0x1

.field private static final RIGHT:I = 0x2


# instance fields
.field TAG:Ljava/lang/String;

.field private algorithm:Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;

.field private final controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

.field private final mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 3

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    sget-object v0, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->TAG:Ljava/lang/String;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->TAG:Ljava/lang/String;

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    return-void
.end method

.method private getLeftHidePromptZone()I
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getWidth()I

    move-result v0

    mul-int/lit8 v0, v0, 0x8

    div-int/lit8 v0, v0, 0x9

    return v0
.end method

.method private isCenterSectorDisable(ILjava/util/ArrayList;)Z
    .registers 8
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(I",
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;)Z"
        }
    .end annotation

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->isDoubleStatusBar()Z

    move-result v0

    if-eqz v0, :cond_a

    const/4 v0, 0x1

    return v0

    :cond_a
    add-int/lit8 v0, p1, 0x1

    mul-int/lit8 v0, v0, 0xa

    const/4 p1, 0x0

    invoke-virtual {p2}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_13
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    if-eqz v2, :cond_2c

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v3

    if-le v3, v0, :cond_2b

    add-int/lit8 v4, v0, 0xa

    if-ge v3, v4, :cond_2b

    const/4 p1, 0x1

    goto :goto_2c

    :cond_2b
    goto :goto_13

    :cond_2c
    :goto_2c
    xor-int/lit8 v1, p1, 0x1

    return v1
.end method

.method private isDrip()Z
    .registers 2

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->isPortrite()Z

    move-result v0

    if-eqz v0, :cond_e

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->isDrip:Z

    if-eqz v0, :cond_e

    const/4 v0, 0x1

    goto :goto_f

    :cond_e
    const/4 v0, 0x0

    :goto_f
    return v0
.end method

.method private isHole(Z)Z
    .registers 4

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->isPortrite()Z

    move-result v0

    if-eqz v0, :cond_24

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->isHole:Z

    if-eqz v0, :cond_24

    if-eqz p1, :cond_18

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->notCalculateHoleInLine:Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;->ordinal()I

    move-result v0

    if-gtz v0, :cond_22

    :cond_18
    if-nez p1, :cond_24

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->notCalculateHoleInLine:Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;

    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;->bottomLine:Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;

    if-eq v0, v1, :cond_24

    :cond_22
    const/4 v0, 0x1

    goto :goto_25

    :cond_24
    const/4 v0, 0x0

    :goto_25
    return v0
.end method

.method private isNeedAnalyseFirstElement(I)Z
    .registers 8

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v1, v1, Lcom/android/systemui/newstatusbar/controllers/ElementController;->leftElementPosition:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->isDoubleStatusBar()Z

    move-result v2

    const/16 v3, 0x15

    const/4 v4, 0x1

    if-eqz v2, :cond_14

    if-eq p1, v4, :cond_16

    if-ne p1, v3, :cond_3d

    goto :goto_16

    :cond_14
    if-ne p1, v4, :cond_3d

    :cond_16
    :goto_16
    const/4 v2, 0x0

    if-ne p1, v4, :cond_1b

    move v5, v4

    goto :goto_1c

    :cond_1b
    move v5, v2

    :goto_1c
    invoke-direct {p0, v5}, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->isHole(Z)Z

    move-result v5

    if-eqz v5, :cond_3d

    sget-object v5, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->twoElemOnRight:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    if-eq v1, v5, :cond_3d

    if-ne p1, v4, :cond_30

    sget-object v5, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->upperElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    if-eq v1, v5, :cond_3b

    sget-object v5, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->twoElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    if-eq v1, v5, :cond_3b

    :cond_30
    if-ne p1, v3, :cond_3c

    sget-object v3, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->bottomElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    if-eq v1, v3, :cond_3b

    sget-object v3, Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;->twoElemOnLeft:Lcom/android/systemui/newstatusbar/controllers/ElementController$LeftElementPosition;

    if-eq v1, v3, :cond_3b

    goto :goto_3c

    :cond_3b
    move v4, v2

    :cond_3c
    :goto_3c
    return v4

    :cond_3d
    return v4
.end method

.method private isPortrite()Z
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v0

    iget v0, v0, Landroid/content/res/Configuration;->orientation:I

    const/4 v1, 0x1

    if-ne v0, v1, :cond_10

    goto :goto_11

    :cond_10
    const/4 v1, 0x0

    :goto_11
    return v1
.end method

.method private isRightPosition(I)Z
    .registers 3

    const/16 v0, 0xa

    if-le p1, v0, :cond_8

    const/16 v0, 0x14

    if-lt p1, v0, :cond_c

    :cond_8
    const/16 v0, 0x1e

    if-le p1, v0, :cond_e

    :cond_c
    const/4 v0, 0x1

    goto :goto_f

    :cond_e
    const/4 v0, 0x0

    :goto_f
    return v0
.end method


# virtual methods
.method getWidthCorrection(Z)I
    .registers 3

    goto/32 :goto_9

    nop

    :goto_4
    const/4 v0, 0x0

    :goto_5
    goto/32 :goto_23

    nop

    :goto_9
    if-nez p1, :cond_e

    goto/32 :goto_19

    :cond_e
    goto/32 :goto_1d

    nop

    :goto_12
    iget v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->horizontalPaddingForCorners:I

    goto/32 :goto_18

    nop

    :goto_18
    goto :goto_5

    :goto_19
    goto/32 :goto_4

    nop

    :goto_1d
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_12

    nop

    :goto_23
    return v0
.end method

.method public updateAlgoritm()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->isHole:Z

    if-eqz v0, :cond_e

    new-instance v0, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-direct {v0, v1}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    goto :goto_15

    :cond_e
    new-instance v0, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-direct {v0, v1}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    :goto_15
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ElementHelper;->algorithm:Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_ElementHelper',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
