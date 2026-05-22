"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/policy/AlgorithmLeftCamera.smali'
CLASS_FALLBACK_NAMES = ['AlgorithmLeftCamera.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;
.super Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 2

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    return-void
.end method


# virtual methods
.method public checkMeasuredWidth(Ljava/util/ArrayList;Z)V
    .registers 25
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;Z)V"
        }
    .end annotation

    move-object/from16 v0, p0

    move-object/from16 v1, p1

    move/from16 v2, p2

    const/16 v3, 0xb

    invoke-virtual {v0, v3, v1, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->getSummWidth(ILjava/util/ArrayList;Z)[I

    move-result-object v4

    iget-object v5, v0, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    const/4 v6, 0x0

    aget v7, v4, v6

    const/4 v8, 0x1

    if-nez v7, :cond_16

    move v7, v8

    goto :goto_17

    :cond_16
    move v7, v6

    :goto_17
    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->isHole(Z)Z

    move-result v9

    const/4 v10, 0x2

    if-eqz v7, :cond_2b

    new-array v11, v8, [I

    invoke-static {v4}, Ljava/util/Arrays;->stream([I)Ljava/util/stream/IntStream;

    move-result-object v12

    invoke-interface {v12}, Ljava/util/stream/IntStream;->sum()I

    move-result v12

    aput v12, v11, v6

    goto :goto_35

    :cond_2b
    new-array v11, v10, [I

    aget v12, v4, v8

    aput v12, v11, v6

    aget v12, v4, v10

    aput v12, v11, v8

    :goto_35
    if-eqz v7, :cond_39

    move v12, v6

    goto :goto_3a

    :cond_39
    move v12, v8

    :goto_3a
    invoke-virtual {v5}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getWidth()I

    move-result v13

    if-eqz v9, :cond_42

    move v14, v8

    goto :goto_43

    :cond_42
    move v14, v10

    :goto_43
    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->getWidthCorrection(Z)I

    move-result v15

    mul-int/2addr v14, v15

    sub-int/2addr v13, v14

    iget-object v14, v0, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget v14, v14, Lcom/android/systemui/newstatusbar/controllers/ElementController;->mCameraWidth:I

    if-eqz v9, :cond_51

    move v15, v14

    goto :goto_52

    :cond_51
    move v15, v6

    :goto_52
    sub-int v15, v13, v15

    array-length v3, v11

    move v10, v6

    :goto_56
    if-ge v10, v3, :cond_c6

    aget v18, v11, v10

    if-ne v12, v8, :cond_6b

    if-eqz v9, :cond_6b

    div-int/lit8 v19, v13, 0x2

    aget v20, v4, v6

    const/16 v17, 0x2

    div-int/lit8 v20, v20, 0x2

    sub-int v19, v19, v20

    sub-int v19, v19, v14

    goto :goto_75

    :cond_6b
    div-int/lit8 v19, v13, 0x2

    aget v20, v4, v6

    const/16 v17, 0x2

    div-int/lit8 v20, v20, 0x2

    sub-int v19, v19, v20

    :goto_75
    if-eqz v7, :cond_7a

    move/from16 v20, v15

    goto :goto_7c

    :cond_7a
    move/from16 v20, v19

    :goto_7c
    move/from16 v21, v20

    const/16 v20, 0xb

    move/from16 v6, v18

    move/from16 v8, v20

    :goto_84
    move/from16 v20, v3

    move/from16 v3, v21

    if-ge v3, v6, :cond_a4

    add-int/lit8 v8, v8, -0x1

    invoke-virtual {v0, v8, v1, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->getSummWidth(ILjava/util/ArrayList;Z)[I

    move-result-object v21

    if-eqz v7, :cond_9b

    invoke-static/range {v21 .. v21}, Ljava/util/Arrays;->stream([I)Ljava/util/stream/IntStream;

    move-result-object v21

    invoke-interface/range {v21 .. v21}, Ljava/util/stream/IntStream;->sum()I

    move-result v21

    goto :goto_9d

    :cond_9b
    aget v21, v21, v12

    :goto_9d
    move/from16 v6, v21

    move/from16 v21, v3

    move/from16 v3, v20

    goto :goto_84

    :cond_a4
    const/16 v2, 0xb

    if-ge v8, v2, :cond_af

    sub-int v21, v3, v6

    const/16 v16, 0x2

    add-int/lit8 v21, v21, -0x2

    goto :goto_b3

    :cond_af
    const/16 v16, 0x2

    const/16 v21, 0x7d0

    :goto_b3
    move/from16 v17, v21

    move/from16 v2, v17

    invoke-virtual {v0, v2, v8, v12, v1}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->sendMaxWidth(IIILjava/util/ArrayList;)V

    nop

    add-int/lit8 v12, v12, 0x1

    add-int/lit8 v10, v10, 0x1

    move/from16 v2, p2

    move/from16 v3, v20

    const/4 v6, 0x0

    const/4 v8, 0x1

    goto :goto_56

    :cond_c6
    return-void
.end method

.method getSummWidth(ILjava/util/ArrayList;Z)[I
    .registers 13
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(I",
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;Z)[I"
        }
    .end annotation

    goto/32 :goto_ec

    nop

    :goto_4
    goto/16 :goto_d4

    :goto_6
    goto/32 :goto_80

    nop

    :goto_a
    goto/16 :goto_108

    :goto_c
    goto/32 :goto_35

    nop

    :goto_10
    aget v6, v0, v5

    goto/32 :goto_16

    nop

    :goto_16
    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getRealMeasuredWidth()I

    move-result v7

    goto/32 :goto_de

    nop

    :goto_1e
    const/16 v6, 0xa

    goto/32 :goto_8c

    nop

    :goto_24
    invoke-virtual {p0, v3}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->isNeedAnalyseFirstElement(I)Z

    move-result v8

    goto/32 :goto_e3

    nop

    :goto_2c
    if-gt v3, v6, :cond_31

    goto/32 :goto_a6

    :cond_31
    goto/32 :goto_aa

    nop

    :goto_35
    const/4 v6, 0x1

    goto/32 :goto_ca

    nop

    :goto_3a
    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getRealMeasuredWidth()I

    move-result v6

    goto/32 :goto_9e

    nop

    :goto_42
    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPrior()I

    move-result v4

    goto/32 :goto_75

    nop

    :goto_4a
    add-int/2addr v7, v5

    goto/32 :goto_106

    nop

    :goto_4f
    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getRealMeasuredWidth()I

    move-result v5

    :goto_53
    goto/32 :goto_4a

    nop

    :goto_57
    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v3

    goto/32 :goto_42

    nop

    :goto_5f
    const/4 v5, 0x2

    goto/32 :goto_10

    nop

    :goto_64
    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v2

    goto/32 :goto_f1

    nop

    :goto_6c
    if-nez v2, :cond_71

    goto/32 :goto_6

    :cond_71
    goto/32 :goto_64

    nop

    :goto_75
    const/4 v5, 0x0

    goto/32 :goto_f7

    nop

    :goto_7a
    goto/16 :goto_108

    :goto_7c
    goto/32 :goto_c1

    nop

    :goto_80
    return-object v0

    nop

    :array_82
    .array-data 4
        0x0
        0x0
        0x0
    .end array-data

    :goto_8c
    if-ge v3, v6, :cond_91

    goto/32 :goto_c

    :cond_91
    goto/32 :goto_d8

    nop

    :goto_95
    if-lt v3, v6, :cond_9a

    goto/32 :goto_a6

    :cond_9a
    goto/32 :goto_a4

    nop

    :goto_9e
    aput v6, v0, v5

    goto/32 :goto_7a

    nop

    :goto_a4
    goto/16 :goto_c

    :goto_a6
    goto/32 :goto_5f

    nop

    :goto_aa
    const/16 v6, 0x1e

    goto/32 :goto_95

    nop

    :goto_b0
    new-array v0, v0, [I

    fill-array-data v0, :array_82

    goto/32 :goto_d0

    nop

    :goto_b9
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v2

    goto/32 :goto_6c

    nop

    :goto_c1
    if-lt v4, p1, :cond_c6

    goto/32 :goto_108

    :cond_c6
    goto/32 :goto_1e

    nop

    :goto_ca
    aget v7, v0, v6

    goto/32 :goto_24

    nop

    :goto_d0
    invoke-virtual {p2}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_d4
    goto/32 :goto_b9

    nop

    :goto_d8
    const/16 v6, 0x14

    goto/32 :goto_2c

    nop

    :goto_de
    add-int/2addr v6, v7

    goto/32 :goto_100

    nop

    :goto_e3
    if-nez v8, :cond_e8

    goto/32 :goto_53

    :cond_e8
    goto/32 :goto_4f

    nop

    :goto_ec
    const/4 v0, 0x3

    goto/32 :goto_b0

    nop

    :goto_f1
    check-cast v2, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    goto/32 :goto_57

    nop

    :goto_f7
    if-eqz v3, :cond_fc

    goto/32 :goto_7c

    :cond_fc
    goto/32 :goto_3a

    nop

    :goto_100
    aput v6, v0, v5

    goto/32 :goto_a

    nop

    :goto_106
    aput v7, v0, v6

    :goto_108
    goto/32 :goto_4

    nop
.end method

.method isDrip()Z
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    const/4 v0, 0x0

    goto/32 :goto_9

    nop

    :goto_9
    return v0
.end method

.method protected isHole(Z)Z
    .registers 4

    goto/32 :goto_65

    nop

    :goto_4
    if-eqz p1, :cond_9

    goto/32 :goto_61

    :cond_9
    goto/32 :goto_3d

    nop

    :goto_d
    if-nez v0, :cond_12

    goto/32 :goto_61

    :cond_12
    goto/32 :goto_4f

    nop

    :goto_16
    if-nez v0, :cond_1b

    goto/32 :goto_61

    :cond_1b
    goto/32 :goto_73

    nop

    :goto_1f
    if-lez v0, :cond_24

    goto/32 :goto_39

    :cond_24
    :goto_24
    goto/32 :goto_4

    nop

    :goto_28
    const/4 v0, 0x0

    :goto_29
    goto/32 :goto_2d

    nop

    :goto_2d
    return v0

    :goto_2e
    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->notCalculateHoleInLine:Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;

    goto/32 :goto_7c

    nop

    :goto_34
    if-ne v0, v1, :cond_39

    goto/32 :goto_61

    :cond_39
    :goto_39
    goto/32 :goto_5b

    nop

    :goto_3d
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_43

    nop

    :goto_43
    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->notCalculateHoleInLine:Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;

    goto/32 :goto_55

    nop

    :goto_49
    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->isHole:Z

    goto/32 :goto_16

    nop

    :goto_4f
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_49

    nop

    :goto_55
    sget-object v1, Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;->bottomLine:Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;

    goto/32 :goto_34

    nop

    :goto_5b
    const/4 v0, 0x1

    goto/32 :goto_60

    nop

    :goto_60
    goto :goto_29

    :goto_61
    goto/32 :goto_28

    nop

    :goto_65
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->isPortrite()Z

    move-result v0

    goto/32 :goto_d

    nop

    :goto_6d
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_2e

    nop

    :goto_73
    if-nez p1, :cond_78

    goto/32 :goto_24

    :cond_78
    goto/32 :goto_6d

    nop

    :goto_7c
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/ElementController$NotCalculateHoleInLine;->ordinal()I

    move-result v0

    goto/32 :goto_1f

    nop
.end method

.method public isNeedAnalyseFirstElement(I)Z
    .registers 8

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

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
    invoke-virtual {p0, v5}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->isHole(Z)Z

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

.method sendMaxWidth(IIILjava/util/ArrayList;)V
    .registers 13
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(III",
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;)V"
        }
    .end annotation

    goto/32 :goto_8f

    nop

    :goto_4
    move v4, v5

    :goto_5
    goto/32 :goto_2b

    nop

    :goto_9
    const/16 v4, 0x7d0

    :goto_b
    goto/32 :goto_c9

    nop

    :goto_f
    if-nez p3, :cond_14

    goto/32 :goto_8b

    :cond_14
    goto/32 :goto_67

    nop

    :goto_18
    goto/16 :goto_f1

    :goto_1a
    goto/32 :goto_f0

    nop

    :goto_1e
    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v2

    goto/32 :goto_f5

    nop

    :goto_26
    const/4 v5, 0x1

    goto/32 :goto_f

    nop

    :goto_2b
    if-nez v4, :cond_30

    goto/32 :goto_ec

    :cond_30
    goto/32 :goto_78

    nop

    :goto_34
    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPrior()I

    move-result v3

    goto/32 :goto_fd

    nop

    :goto_3c
    if-lt v3, p2, :cond_41

    goto/32 :goto_1a

    :cond_41
    goto/32 :goto_a2

    nop

    :goto_45
    if-eq p3, v7, :cond_4a

    goto/32 :goto_d7

    :cond_4a
    goto/32 :goto_53

    nop

    :goto_4e
    move v5, p1

    goto/32 :goto_c4

    nop

    :goto_53
    move v7, v5

    goto/32 :goto_d6

    nop

    :goto_58
    if-gt v4, v3, :cond_5d

    goto/32 :goto_d2

    :cond_5d
    goto/32 :goto_81

    nop

    :goto_61
    goto/16 :goto_ec

    :goto_63
    goto/32 :goto_34

    nop

    :goto_67
    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->isRightPosition(I)Z

    move-result v6

    goto/32 :goto_9d

    nop

    :goto_6f
    if-eqz v3, :cond_74

    goto/32 :goto_63

    :cond_74
    goto/32 :goto_10a

    nop

    :goto_78
    if-eq v3, p2, :cond_7d

    goto/32 :goto_c5

    :cond_7d
    goto/32 :goto_4e

    nop

    :goto_81
    move v4, v3

    goto/32 :goto_d0

    nop

    :goto_86
    if-eq v6, v7, :cond_8b

    goto/32 :goto_5

    :cond_8b
    :goto_8b
    goto/32 :goto_4

    nop

    :goto_8f
    invoke-virtual {p4}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_93
    goto/32 :goto_db

    nop

    :goto_97
    check-cast v1, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    goto/32 :goto_1e

    nop

    :goto_9d
    const/4 v7, 0x2

    goto/32 :goto_45

    nop

    :goto_a2
    const/16 v5, 0x7d0

    goto/32 :goto_18

    nop

    :goto_a8
    move v7, v4

    :goto_a9
    goto/32 :goto_86

    nop

    :goto_ad
    return-void

    :goto_ae
    if-nez v1, :cond_b3

    goto/32 :goto_b8

    :cond_b3
    goto/32 :goto_bc

    nop

    :goto_b7
    goto :goto_93

    :goto_b8
    goto/32 :goto_ad

    nop

    :goto_bc
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto/32 :goto_97

    nop

    :goto_c4
    goto :goto_f1

    :goto_c5
    goto/32 :goto_3c

    nop

    :goto_c9
    invoke-virtual {v1, v4}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->setMaxMeasureWidth(I)V

    goto/32 :goto_61

    nop

    :goto_d0
    goto/16 :goto_b

    :goto_d2
    goto/32 :goto_9

    nop

    :goto_d6
    goto :goto_a9

    :goto_d7
    goto/32 :goto_a8

    nop

    :goto_db
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto/32 :goto_ae

    nop

    :goto_e3
    iget v3, v3, Lcom/android/systemui/newstatusbar/controllers/ElementController;->leftWidthToCamera:I

    goto/32 :goto_102

    nop

    :goto_e9
    invoke-virtual {v1, v5}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->setMaxMeasureWidth(I)V

    :goto_ec
    goto/32 :goto_b7

    nop

    :goto_f0
    const/4 v5, 0x1

    :goto_f1
    goto/32 :goto_e9

    nop

    :goto_f5
    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->isNeedAnalyseFirstElement(I)Z

    move-result v3

    goto/32 :goto_6f

    nop

    :goto_fd
    const/4 v4, 0x0

    goto/32 :goto_26

    nop

    :goto_102
    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getRealMeasuredWidth()I

    move-result v4

    goto/32 :goto_58

    nop

    :goto_10a
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmLeftCamera;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_e3

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_policy_AlgorithmLeftCamera',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
