"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/policy/ElementPositionAlgorithm.smali'
CLASS_FALLBACK_NAMES = ['ElementPositionAlgorithm.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public abstract Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;


# static fields
.field public static final ALL:I = 0x0

.field public static final LEFT:I = 0x1

.field public static final RIGHT:I = 0x2


# instance fields
.field private final centerElemEnableInIsland:Z

.field protected controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

.field protected isIslandShown:Z

.field protected islandController:Lcom/android/systemui/newstatusbar/controllers/IslandController;

.field private leftWidth:I

.field protected mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

.field private rightWidth:I

.field private final sKeyCenterElemEnableInIsland:Ljava/lang/String;


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 4

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/IslandController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->islandController:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    const-string v0, "status_bar_elem_center_in_island"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->sKeyCenterElemEnableInIsland:Ljava/lang/String;

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->islandController:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-virtual {v1, p0}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;)V

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->islandController:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->getLeftWidth()I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->leftWidth:I

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->islandController:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->getRightWidth()I

    move-result v1

    iput v1, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->rightWidth:I

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->islandController:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->isShown()Z

    move-result v1

    iput-boolean v1, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->isIslandShown:Z

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings1(Ljava/lang/String;)Z

    move-result v0

    iput-boolean v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->centerElemEnableInIsland:Z

    return-void
.end method

.method private getLeftHidePromptZone()I
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getWidth()I

    move-result v0

    mul-int/lit8 v0, v0, 0x8

    div-int/lit8 v0, v0, 0x9

    return v0
.end method

.method private updateClock(Lcom/android/systemui/newstatusbar/layouts/SingleLayout;)V
    .registers 4

    instance-of v0, p1, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;

    if-eqz v0, :cond_1b

    move-object v0, p1

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->getClockView()Lcom/android/systemui/newstatusbar/clock/ClockView;

    move-result-object v0

    invoke-virtual {p1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v1

    if-eqz v1, :cond_1b

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/clock/ClockView;->getVisibility()I

    move-result v1

    if-eqz v1, :cond_1b

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->setVisibility(I)V

    :cond_1b
    return-void
.end method


# virtual methods
.method public abstract checkMeasuredWidth(Ljava/util/ArrayList;Z)V
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;Z)V"
        }
    .end annotation
.end method

.method public clearCallBackIslandController()V
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->islandController:Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    return-void
.end method

.method protected getLeftWidth()I
    .registers 2

    goto/32 :goto_10

    nop

    :goto_4
    const/16 v0, 0xbb8

    :goto_6
    goto/32 :goto_a

    nop

    :goto_a
    return v0

    :goto_b
    goto :goto_6

    :goto_c
    goto/32 :goto_4

    nop

    :goto_10
    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->isIslandShown:Z

    goto/32 :goto_1c

    nop

    :goto_16
    iget v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->leftWidth:I

    goto/32 :goto_b

    nop

    :goto_1c
    if-nez v0, :cond_21

    goto/32 :goto_c

    :cond_21
    goto/32 :goto_16

    nop
.end method

.method public getRightWidth()I
    .registers 2

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->isIslandShown:Z

    if-eqz v0, :cond_7

    iget v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->rightWidth:I

    goto :goto_9

    :cond_7
    const/16 v0, 0xbb8

    :goto_9
    return v0
.end method

.method abstract getSummWidth(ILjava/util/ArrayList;Z)[I
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(I",
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;Z)[I"
        }
    .end annotation
.end method

.method getWidthCorrection(Z)I
    .registers 3

    goto/32 :goto_1b

    nop

    :goto_4
    iget v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->horizontalPaddingForCorners:I

    goto/32 :goto_16

    nop

    :goto_a
    return v0

    :goto_b
    const/4 v0, 0x0

    :goto_c
    goto/32 :goto_a

    nop

    :goto_10
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_4

    nop

    :goto_16
    goto :goto_c

    :goto_17
    goto/32 :goto_b

    nop

    :goto_1b
    if-nez p1, :cond_20

    goto/32 :goto_17

    :cond_20
    goto/32 :goto_10

    nop
.end method

.method abstract isDrip()Z
.end method

.method abstract isHole(Z)Z
.end method

.method abstract isNeedAnalyseFirstElement(I)Z
.end method

.method isPortrite()Z
    .registers 3

    goto/32 :goto_16

    nop

    :goto_4
    const/4 v1, 0x0

    :goto_5
    goto/32 :goto_2f

    nop

    :goto_9
    invoke-virtual {v0}, Landroid/content/res/Resources;->getConfiguration()Landroid/content/res/Configuration;

    move-result-object v0

    goto/32 :goto_21

    nop

    :goto_11
    goto :goto_5

    :goto_12
    goto/32 :goto_4

    nop

    :goto_16
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    goto/32 :goto_27

    nop

    :goto_1c
    const/4 v1, 0x1

    goto/32 :goto_30

    nop

    :goto_21
    iget v0, v0, Landroid/content/res/Configuration;->orientation:I

    goto/32 :goto_1c

    nop

    :goto_27
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    goto/32 :goto_9

    nop

    :goto_2f
    return v1

    :goto_30
    if-eq v0, v1, :cond_35

    goto/32 :goto_12

    :cond_35
    goto/32 :goto_11

    nop
.end method

.method isRightPosition(I)Z
    .registers 3

    goto/32 :goto_1d

    nop

    :goto_4
    const/16 v0, 0x14

    goto/32 :goto_14

    nop

    :goto_a
    if-gt p1, v0, :cond_f

    goto/32 :goto_19

    :cond_f
    goto/32 :goto_4

    nop

    :goto_13
    return v0

    :goto_14
    if-ge p1, v0, :cond_19

    goto/32 :goto_3d

    :cond_19
    :goto_19
    goto/32 :goto_2d

    nop

    :goto_1d
    const/16 v0, 0xa

    goto/32 :goto_a

    nop

    :goto_23
    const/4 v0, 0x0

    :goto_24
    goto/32 :goto_13

    nop

    :goto_28
    const/4 v0, 0x1

    goto/32 :goto_33

    nop

    :goto_2d
    const/16 v0, 0x1e

    goto/32 :goto_38

    nop

    :goto_33
    goto :goto_24

    :goto_34
    goto/32 :goto_23

    nop

    :goto_38
    if-gt p1, v0, :cond_3d

    goto/32 :goto_34

    :cond_3d
    :goto_3d
    goto/32 :goto_28

    nop
.end method

.method public onIslandShowChange(Z)V
    .registers 3

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->isIslandShown:Z

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateMainLayouts()V

    return-void
.end method

.method public onIslandSizeChange(II)V
    .registers 4

    iput p2, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->rightWidth:I

    iput p1, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->leftWidth:I

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateMainLayouts()V

    return-void
.end method

.method public placeCalculation(Ljava/util/ArrayList;Z)V
    .registers 27
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;Z)V"
        }
    .end annotation

    move-object/from16 v0, p0

    move/from16 v1, p2

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    iget-object v3, v0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->isHole(Z)Z

    move-result v4

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getWidth()I

    move-result v5

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->isPortrite()Z

    move-result v6

    const/16 v7, 0x14

    if-eqz v6, :cond_22

    if-eqz v4, :cond_1d

    iget v6, v3, Lcom/android/systemui/newstatusbar/controllers/ElementController;->mCameraWidth:I

    goto :goto_2a

    :cond_1d
    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->getWidthCorrection(Z)I

    move-result v6

    goto :goto_2a

    :cond_22
    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getContext()Landroid/content/Context;

    move-result-object v6

    invoke-static {v6, v7}, Landroid/Utils/ImageUtils;->convertDpToPx(Landroid/content/Context;I)I

    move-result v6

    :goto_2a
    nop

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->isPortrite()Z

    move-result v8

    if-eqz v8, :cond_36

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->getWidthCorrection(Z)I

    move-result v8

    goto :goto_3e

    :cond_36
    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getContext()Landroid/content/Context;

    move-result-object v8

    invoke-static {v8, v7}, Landroid/Utils/ImageUtils;->convertDpToPx(Landroid/content/Context;I)I

    move-result v8

    :goto_3e
    sub-int v8, v5, v8

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->isCenterEnable()Z

    move-result v9

    const/4 v10, 0x0

    if-eqz v9, :cond_52

    if-nez v1, :cond_52

    invoke-virtual {v2, v10}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getElementForPosition(I)Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    move-result-object v9

    invoke-virtual {v9}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getLayoutWidth()I

    move-result v9

    goto :goto_5c

    :cond_52
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->isDrip()Z

    move-result v9

    if-eqz v9, :cond_5b

    iget v9, v3, Lcom/android/systemui/newstatusbar/controllers/ElementController;->mCameraWidth:I

    goto :goto_5c

    :cond_5b
    move v9, v10

    :goto_5c
    nop

    div-int/lit8 v11, v5, 0x2

    div-int/lit8 v12, v9, 0x2

    sub-int/2addr v11, v12

    div-int/lit8 v12, v5, 0x2

    div-int/lit8 v13, v9, 0x2

    add-int/2addr v12, v13

    const/4 v13, 0x0

    iget v14, v3, Lcom/android/systemui/newstatusbar/controllers/ElementController;->statusBarHeight:I

    invoke-direct/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->getLeftHidePromptZone()I

    move-result v15

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->isDoubleStatusBar()Z

    move-result v16

    invoke-virtual/range {p1 .. p1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v17

    :goto_76
    invoke-interface/range {v17 .. v17}, Ljava/util/Iterator;->hasNext()Z

    move-result v18

    if-eqz v18, :cond_12b

    invoke-interface/range {v17 .. v17}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v18

    move-object/from16 v10, v18

    check-cast v10, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    invoke-direct {v0, v10}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->updateClock(Lcom/android/systemui/newstatusbar/layouts/SingleLayout;)V

    invoke-virtual {v10}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v7

    invoke-virtual {v10}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getLayoutWidth()I

    move-result v19

    move-object/from16 v20, v2

    const/16 v2, 0x14

    if-le v7, v2, :cond_9a

    if-eqz v16, :cond_9a

    add-int/lit8 v7, v7, -0x14

    move v13, v14

    :cond_9a
    if-nez v7, :cond_c6

    iget-boolean v2, v0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->isIslandShown:Z

    if-eqz v2, :cond_a6

    iget-boolean v2, v0, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->centerElemEnableInIsland:Z

    if-nez v2, :cond_a6

    const/16 v19, 0x0

    :cond_a6
    div-int/lit8 v2, v5, 0x2

    div-int/lit8 v21, v19, 0x2

    sub-int v2, v2, v21

    add-int v21, v2, v19

    if-eqz v16, :cond_c1

    move/from16 v22, v2

    iget-object v2, v3, Lcom/android/systemui/newstatusbar/controllers/ElementController;->centerElementPosition:Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;->ordinal()I

    move-result v2

    div-int/lit8 v23, v14, 0x2

    mul-int v13, v2, v23

    move/from16 v0, v21

    move/from16 v2, v22

    goto :goto_110

    :cond_c1
    move/from16 v22, v2

    move/from16 v0, v21

    goto :goto_110

    :cond_c6
    const/16 v2, 0xa

    if-ge v7, v2, :cond_ea

    if-eqz v16, :cond_d1

    if-nez v1, :cond_d1

    const/16 v2, 0x14

    goto :goto_d2

    :cond_d1
    const/4 v2, 0x0

    :goto_d2
    add-int/2addr v2, v7

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->isNeedAnalyseFirstElement(I)Z

    move-result v2

    if-nez v2, :cond_e2

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;->getWidthCorrection(Z)I

    move-result v2

    add-int v21, v2, v19

    move/from16 v0, v21

    goto :goto_110

    :cond_e2
    move v2, v6

    add-int v21, v2, v19

    move/from16 v6, v21

    move/from16 v0, v21

    goto :goto_110

    :cond_ea
    if-le v7, v2, :cond_fb

    const/16 v2, 0x14

    if-ge v7, v2, :cond_fd

    move/from16 v21, v8

    sub-int v18, v21, v19

    move/from16 v8, v18

    move/from16 v2, v18

    move/from16 v0, v21

    goto :goto_110

    :cond_fb
    const/16 v2, 0x14

    :cond_fd
    const/16 v2, 0x1e

    if-ge v7, v2, :cond_109

    move/from16 v21, v11

    sub-int v2, v21, v19

    move v11, v2

    move/from16 v0, v21

    goto :goto_110

    :cond_109
    move v2, v12

    add-int v21, v2, v19

    move/from16 v12, v21

    move/from16 v0, v21

    :goto_110
    add-int v1, v13, v14

    invoke-virtual {v10, v2, v13, v0, v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->preLayout(IIII)V

    if-le v0, v15, :cond_119

    const/4 v1, 0x1

    goto :goto_11a

    :cond_119
    const/4 v1, 0x0

    :goto_11a
    iput-boolean v1, v10, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->isHideInPromptVisible:Z

    if-nez v7, :cond_120

    const/4 v1, 0x0

    move v13, v1

    :cond_120
    move-object/from16 v0, p0

    move/from16 v1, p2

    move-object/from16 v2, v20

    const/16 v7, 0x14

    const/4 v10, 0x0

    goto/16 :goto_76

    :cond_12b
    return-void
.end method

.method abstract sendMaxWidth(IIILjava/util/ArrayList;)V
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(III",
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;)V"
        }
    .end annotation
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_policy_ElementPositionAlgorithm',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
