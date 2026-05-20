"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/policy/AlgorithmCenterCamera.smali'
CLASS_FALLBACK_NAMES = ['AlgorithmCenterCamera.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;
.super Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;


# direct methods
.method public constructor <init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V
    .registers 2

    invoke-direct {p0, p1}, Lcom/android/systemui/newstatusbar/policy/ElementPositionAlgorithm;-><init>(Lcom/android/systemui/newstatusbar/layouts/MainLayout;)V

    return-void
.end method


# virtual methods
.method public checkMeasuredWidth(Ljava/util/ArrayList;Z)V
    .registers 23
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

    invoke-virtual {v0, v3, v1, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->getSummWidth(ILjava/util/ArrayList;Z)[I

    move-result-object v4

    iget-object v5, v0, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    const/4 v6, 0x0

    aget v7, v4, v6

    const/4 v8, 0x1

    if-nez v7, :cond_1a

    iget-boolean v7, v0, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->isIslandShown:Z

    if-nez v7, :cond_1a

    move v7, v8

    goto :goto_1b

    :cond_1a
    move v7, v6

    :goto_1b
    const/4 v9, 0x2

    if-eqz v7, :cond_2b

    new-array v10, v8, [I

    invoke-static {v4}, Ljava/util/Arrays;->stream([I)Ljava/util/stream/IntStream;

    move-result-object v11

    invoke-interface {v11}, Ljava/util/stream/IntStream;->sum()I

    move-result v11

    aput v11, v10, v6

    goto :goto_35

    :cond_2b
    new-array v10, v9, [I

    aget v11, v4, v8

    aput v11, v10, v6

    aget v11, v4, v9

    aput v11, v10, v8

    :goto_35
    if-eqz v7, :cond_39

    move v11, v6

    goto :goto_3a

    :cond_39
    move v11, v8

    :goto_3a
    invoke-virtual {v5}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getWidth()I

    move-result v12

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->getWidthCorrection(Z)I

    move-result v13

    mul-int/2addr v13, v9

    sub-int/2addr v12, v13

    array-length v13, v10

    move v14, v6

    :goto_46
    if-ge v14, v13, :cond_ac

    aget v15, v10, v14

    div-int/lit8 v16, v12, 0x2

    aget v17, v4, v6

    div-int/lit8 v17, v17, 0x2

    sub-int v6, v16, v17

    iget-boolean v9, v0, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->isIslandShown:Z

    if-eqz v9, :cond_6b

    if-ne v11, v8, :cond_5d

    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->getLeftWidth()I

    move-result v9

    goto :goto_61

    :cond_5d
    invoke-virtual/range {p0 .. p0}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->getRightWidth()I

    move-result v9

    :goto_61
    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->getWidthCorrection(Z)I

    move-result v17

    sub-int v9, v9, v17

    invoke-static {v6, v9}, Ljava/lang/Math;->min(II)I

    move-result v6

    :cond_6b
    if-eqz v7, :cond_6f

    move v9, v12

    goto :goto_70

    :cond_6f
    move v9, v6

    :goto_70
    const/16 v17, 0xb

    move/from16 v8, v17

    :goto_74
    if-ge v9, v15, :cond_8c

    add-int/lit8 v8, v8, -0x1

    invoke-virtual {v0, v8, v1, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->getSummWidth(ILjava/util/ArrayList;Z)[I

    move-result-object v18

    if-eqz v7, :cond_87

    invoke-static/range {v18 .. v18}, Ljava/util/Arrays;->stream([I)Ljava/util/stream/IntStream;

    move-result-object v18

    invoke-interface/range {v18 .. v18}, Ljava/util/stream/IntStream;->sum()I

    move-result v18

    goto :goto_89

    :cond_87
    aget v18, v18, v11

    :goto_89
    move/from16 v15, v18

    goto :goto_74

    :cond_8c
    if-ge v8, v3, :cond_95

    sub-int v18, v9, v15

    const/16 v16, 0x2

    add-int/lit8 v18, v18, -0x2

    goto :goto_99

    :cond_95
    const/16 v16, 0x2

    const/16 v18, 0x7d0

    :goto_99
    move/from16 v19, v18

    move/from16 v3, v19

    invoke-virtual {v0, v3, v8, v11, v1}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->sendMaxWidth(IIILjava/util/ArrayList;)V

    nop

    add-int/lit8 v11, v11, 0x1

    add-int/lit8 v14, v14, 0x1

    move/from16 v9, v16

    const/16 v3, 0xb

    const/4 v6, 0x0

    const/4 v8, 0x1

    goto :goto_46

    :cond_ac
    return-void
.end method

.method getSummWidth(ILjava/util/ArrayList;Z)[I
    .registers 14
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(I",
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/layouts/SingleLayout;",
            ">;Z)[I"
        }
    .end annotation

    goto/32 :goto_c6

    nop

    :goto_4
    invoke-virtual {v4}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getRealMeasuredWidth()I

    move-result v8

    goto/32 :goto_3b

    nop

    :goto_c
    if-ne v3, v4, :cond_11

    goto/32 :goto_99

    :cond_11
    :goto_11
    goto/32 :goto_11d

    nop

    :goto_15
    aput v3, v0, v5

    :goto_17
    goto/32 :goto_4c

    nop

    :goto_1b
    if-nez v3, :cond_20

    goto/32 :goto_17

    :cond_20
    goto/32 :goto_114

    nop

    :goto_24
    if-nez v4, :cond_29

    goto/32 :goto_77

    :cond_29
    goto/32 :goto_e1

    nop

    :goto_2d
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_105

    nop

    :goto_33
    invoke-virtual {v4}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getRealMeasuredWidth()I

    move-result v9

    goto/32 :goto_156

    nop

    :goto_3b
    aput v8, v0, v5

    goto/32 :goto_a5

    nop

    :goto_41
    const/4 v5, 0x2

    goto/32 :goto_d3

    nop

    :goto_46
    iget-object v1, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    goto/32 :goto_148

    nop

    :goto_4c
    return-object v0

    nop

    :array_4e
    .array-data 4
        0x0
        0x0
        0x0
    .end array-data

    :goto_58
    iget-object v3, v3, Lcom/android/systemui/newstatusbar/controllers/ElementController;->centerElementPosition:Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;

    goto/32 :goto_ee

    nop

    :goto_5e
    new-array v0, v0, [I

    fill-array-data v0, :array_4e

    goto/32 :goto_46

    nop

    :goto_67
    const/16 v5, 0x14

    goto/32 :goto_f4

    nop

    :goto_6d
    if-nez v2, :cond_72

    goto/32 :goto_17

    :cond_72
    goto/32 :goto_d9

    nop

    :goto_76
    goto :goto_a1

    :goto_77
    goto/32 :goto_6d

    nop

    :goto_7b
    const/4 v5, 0x0

    goto/32 :goto_24

    nop

    :goto_80
    check-cast v4, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    goto/32 :goto_fd

    nop

    :goto_86
    invoke-virtual {v4}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPrior()I

    move-result v7

    goto/32 :goto_10b

    nop

    :goto_8e
    aput v8, v0, v5

    goto/32 :goto_176

    nop

    :goto_94
    if-eq v3, v4, :cond_99

    goto/32 :goto_17

    :cond_99
    :goto_99
    goto/32 :goto_2d

    nop

    :goto_9d
    invoke-virtual {p2}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v3

    :goto_a1
    goto/32 :goto_cb

    nop

    :goto_a5
    goto/16 :goto_16c

    :goto_a7
    goto/32 :goto_b7

    nop

    :goto_ab
    iget-object v3, v3, Lcom/android/systemui/newstatusbar/controllers/ElementController;->centerElementPosition:Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;

    goto/32 :goto_164

    nop

    :goto_b1
    aget v8, v0, v5

    goto/32 :goto_12f

    nop

    :goto_b7
    if-lt v7, p1, :cond_bc

    goto/32 :goto_16c

    :cond_bc
    goto/32 :goto_150

    nop

    :goto_c0
    goto/16 :goto_177

    :goto_c2
    goto/32 :goto_41

    nop

    :goto_c6
    const/4 v0, 0x3

    goto/32 :goto_5e

    nop

    :goto_cb
    invoke-interface {v3}, Ljava/util/Iterator;->hasNext()Z

    move-result v4

    goto/32 :goto_7b

    nop

    :goto_d3
    aget v8, v0, v5

    goto/32 :goto_33

    nop

    :goto_d9
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->isDrip()Z

    move-result v3

    goto/32 :goto_1b

    nop

    :goto_e1
    invoke-interface {v3}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v4

    goto/32 :goto_80

    nop

    :goto_e9
    const/4 v5, 0x1

    goto/32 :goto_b1

    nop

    :goto_ee
    sget-object v4, Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;->upperLine:Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;

    goto/32 :goto_94

    nop

    :goto_f4
    if-gt v6, v5, :cond_f9

    goto/32 :goto_c2

    :cond_f9
    goto/32 :goto_13d

    nop

    :goto_fd
    invoke-virtual {v4}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v6

    goto/32 :goto_86

    nop

    :goto_105
    iget v3, v3, Lcom/android/systemui/newstatusbar/controllers/ElementController;->mCameraWidth:I

    goto/32 :goto_15

    nop

    :goto_10b
    if-eqz v6, :cond_110

    goto/32 :goto_a7

    :cond_110
    goto/32 :goto_4

    nop

    :goto_114
    if-nez p3, :cond_119

    goto/32 :goto_11

    :cond_119
    goto/32 :goto_137

    nop

    :goto_11d
    if-eqz p3, :cond_122

    goto/32 :goto_17

    :cond_122
    goto/32 :goto_170

    nop

    :goto_126
    if-lt v6, v5, :cond_12b

    goto/32 :goto_c2

    :cond_12b
    goto/32 :goto_c0

    nop

    :goto_12f
    invoke-virtual {v4}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getRealMeasuredWidth()I

    move-result v9

    goto/32 :goto_143

    nop

    :goto_137
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_ab

    nop

    :goto_13d
    const/16 v5, 0x1e

    goto/32 :goto_126

    nop

    :goto_143
    add-int/2addr v8, v9

    goto/32 :goto_16a

    nop

    :goto_148
    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->isDoubleStatusBar()Z

    move-result v2

    goto/32 :goto_9d

    nop

    :goto_150
    const/16 v5, 0xa

    goto/32 :goto_15b

    nop

    :goto_156
    add-int/2addr v8, v9

    goto/32 :goto_8e

    nop

    :goto_15b
    if-ge v6, v5, :cond_160

    goto/32 :goto_177

    :cond_160
    goto/32 :goto_67

    nop

    :goto_164
    sget-object v4, Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;->bottomLine:Lcom/android/systemui/newstatusbar/controllers/ElementController$CenterElementPosition;

    goto/32 :goto_c

    nop

    :goto_16a
    aput v8, v0, v5

    :goto_16c
    goto/32 :goto_76

    nop

    :goto_170
    iget-object v3, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_58

    nop

    :goto_176
    goto :goto_16c

    :goto_177
    goto/32 :goto_e9

    nop
.end method

.method isDrip()Z
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->isPortrite()Z

    move-result v0

    goto/32 :goto_27

    nop

    :goto_c
    if-nez v0, :cond_11

    goto/32 :goto_31

    :cond_11
    goto/32 :goto_35

    nop

    :goto_15
    return v0

    :goto_16
    const/4 v0, 0x0

    :goto_17
    goto/32 :goto_15

    nop

    :goto_1b
    iget-boolean v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->isDrip:Z

    goto/32 :goto_c

    nop

    :goto_21
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->controller:Lcom/android/systemui/newstatusbar/controllers/ElementController;

    goto/32 :goto_1b

    nop

    :goto_27
    if-nez v0, :cond_2c

    goto/32 :goto_31

    :cond_2c
    goto/32 :goto_21

    nop

    :goto_30
    goto :goto_17

    :goto_31
    goto/32 :goto_16

    nop

    :goto_35
    const/4 v0, 0x1

    goto/32 :goto_30

    nop
.end method

.method protected isHole(Z)Z
    .registers 3

    goto/32 :goto_5

    nop

    :goto_4
    return v0

    :goto_5
    const/4 v0, 0x0

    goto/32 :goto_4

    nop
.end method

.method protected isNeedAnalyseFirstElement(I)Z
    .registers 3

    goto/32 :goto_4

    nop

    :goto_4
    const/4 v0, 0x1

    goto/32 :goto_9

    nop

    :goto_9
    return v0
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

    goto/32 :goto_ad

    nop

    :goto_4
    check-cast v1, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;

    goto/32 :goto_ba

    nop

    :goto_a
    goto :goto_35

    :goto_b
    goto/32 :goto_34

    nop

    :goto_f
    if-eq p3, v7, :cond_14

    goto/32 :goto_b

    :cond_14
    goto/32 :goto_47

    nop

    :goto_18
    invoke-virtual {v1, v5}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->setMaxMeasureWidth(I)V

    :goto_1b
    goto/32 :goto_9f

    nop

    :goto_1f
    move v4, v5

    :goto_20
    goto/32 :goto_61

    nop

    :goto_24
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto/32 :goto_4

    nop

    :goto_2c
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto/32 :goto_a4

    nop

    :goto_34
    move v7, v4

    :goto_35
    goto/32 :goto_6a

    nop

    :goto_39
    goto :goto_74

    :goto_3a
    goto/32 :goto_78

    nop

    :goto_3e
    if-eq v3, p2, :cond_43

    goto/32 :goto_3a

    :cond_43
    goto/32 :goto_b5

    nop

    :goto_47
    move v7, v5

    goto/32 :goto_a

    nop

    :goto_4c
    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPrior()I

    move-result v3

    goto/32 :goto_94

    nop

    :goto_54
    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/policy/AlgorithmCenterCamera;->isRightPosition(I)Z

    move-result v6

    goto/32 :goto_5c

    nop

    :goto_5c
    const/4 v7, 0x2

    goto/32 :goto_f

    nop

    :goto_61
    if-nez v4, :cond_66

    goto/32 :goto_1b

    :cond_66
    goto/32 :goto_3e

    nop

    :goto_6a
    if-eq v6, v7, :cond_6f

    goto/32 :goto_20

    :cond_6f
    :goto_6f
    goto/32 :goto_1f

    nop

    :goto_73
    const/4 v5, 0x1

    :goto_74
    goto/32 :goto_18

    nop

    :goto_78
    if-lt v3, p2, :cond_7d

    goto/32 :goto_8b

    :cond_7d
    goto/32 :goto_99

    nop

    :goto_81
    if-nez p3, :cond_86

    goto/32 :goto_6f

    :cond_86
    goto/32 :goto_54

    nop

    :goto_8a
    goto :goto_74

    :goto_8b
    goto/32 :goto_73

    nop

    :goto_8f
    const/4 v5, 0x1

    goto/32 :goto_81

    nop

    :goto_94
    const/4 v4, 0x0

    goto/32 :goto_8f

    nop

    :goto_99
    const/16 v5, 0x7d0

    goto/32 :goto_8a

    nop

    :goto_9f
    goto :goto_b1

    :goto_a0
    goto/32 :goto_c2

    nop

    :goto_a4
    if-nez v1, :cond_a9

    goto/32 :goto_a0

    :cond_a9
    goto/32 :goto_24

    nop

    :goto_ad
    invoke-virtual {p4}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_b1
    goto/32 :goto_2c

    nop

    :goto_b5
    move v5, p1

    goto/32 :goto_39

    nop

    :goto_ba
    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/layouts/SingleLayout;->getPosition()I

    move-result v2

    goto/32 :goto_4c

    nop

    :goto_c2
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_policy_AlgorithmCenterCamera',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
