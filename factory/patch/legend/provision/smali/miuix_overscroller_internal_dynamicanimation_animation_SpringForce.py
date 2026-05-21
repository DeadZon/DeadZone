TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/overscroller/internal/dynamicanimation/animation/SpringForce.smali'
CLASS_FALLBACK_NAMES = ['SpringForce.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_SpringForce__updateValues',
        'method': '.method updateValues(DDJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;',
        'method_name': 'updateValues',
        'method_anchors': ['invoke-direct {v0}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->init()V', 'iget-wide v3, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mFinalPosition:D', 'iget-wide v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampingRatio:D', 'if-lez v9, :cond_0', 'iget-wide v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaMinus:D', 'iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaPlus:D', 'invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D', 'iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaPlus:D'],
        'type': 'method_replace',
        'search': """.method updateValues(DDJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;
    .registers 23

    move-object/from16 v0, p0

    invoke-direct {v0}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->init()V

    move-wide/from16 v1, p5

    long-to-double v1, v1

    const-wide v3, 0x41cdcd6500000000L

    div-double/2addr v1, v3

    iget-wide v3, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mFinalPosition:D

    sub-double v3, p1, v3

    iget-wide v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampingRatio:D

    const-wide/high16 v7, 0x3ff0000000000000L

    cmpl-double v9, v5, v7

    const-wide v10, 0x4005bf0a8b145769L

    if-lez v9, :cond_0

    iget-wide v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaMinus:D

    mul-double v7, v5, v3

    sub-double v7, v7, p3

    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaPlus:D

    sub-double v14, v5, v12

    div-double/2addr v7, v14

    sub-double v7, v3, v7

    mul-double/2addr v3, v5

    sub-double v3, v3, p3

    sub-double v12, v5, v12

    div-double/2addr v3, v12

    mul-double/2addr v5, v1

    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    mul-double/2addr v5, v7

    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaPlus:D

    mul-double/2addr v12, v1

    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    mul-double/2addr v12, v3

    add-double/2addr v5, v12

    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaMinus:D

    mul-double/2addr v7, v12

    mul-double/2addr v12, v1

    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    mul-double/2addr v7, v12

    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaPlus:D

    mul-double/2addr v3, v12

    mul-double/2addr v12, v1

    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v1

    mul-double/2addr v3, v1

    add-double/2addr v7, v3

    goto :goto_0

    :cond_0
    cmpl-double v9, v5, v7

    if-nez v9, :cond_1

    iget-wide v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mNaturalFreq:D

    mul-double v7, v5, v3

    add-double v7, p3, v7

    mul-double v12, v7, v1

    add-double/2addr v3, v12

    neg-double v5, v5

    mul-double/2addr v5, v1

    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    mul-double/2addr v5, v3

    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mNaturalFreq:D

    neg-double v12, v12

    mul-double/2addr v12, v1

    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    mul-double/2addr v3, v12

    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mNaturalFreq:D

    neg-double v14, v12

    mul-double/2addr v3, v14

    neg-double v12, v12

    mul-double/2addr v12, v1

    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v1

    mul-double/2addr v7, v1

    add-double/2addr v7, v3

    goto :goto_0

    :cond_1
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampedFreq:D

    div-double/2addr v7, v12

    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mNaturalFreq:D

    mul-double v14, v5, v12

    mul-double/2addr v14, v3

    add-double v14, v14, p3

    mul-double/2addr v7, v14

    neg-double v5, v5

    mul-double/2addr v5, v12

    mul-double/2addr v5, v1

    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampedFreq:D

    mul-double/2addr v12, v1

    invoke-static {v12, v13}, Ljava/lang/Math;->cos(D)D

    move-result-wide v12

    mul-double/2addr v12, v3

    iget-wide v14, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampedFreq:D

    mul-double/2addr v14, v1

    invoke-static {v14, v15}, Ljava/lang/Math;->sin(D)D

    move-result-wide v14

    mul-double/2addr v14, v7

    add-double/2addr v12, v14

    mul-double/2addr v5, v12

    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mNaturalFreq:D

    neg-double v14, v12

    mul-double/2addr v14, v5

    iget-wide v10, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampingRatio:D

    mul-double/2addr v14, v10

    neg-double v9, v10

    mul-double/2addr v9, v12

    mul-double/2addr v9, v1

    const-wide v11, 0x4005bf0a8b145769L

    invoke-static {v11, v12, v9, v10}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v9

    iget-wide v11, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampedFreq:D

    move-wide/from16 p5, v1

    neg-double v1, v11

    mul-double/2addr v1, v3

    mul-double v11, v11, p5

    invoke-static {v11, v12}, Ljava/lang/Math;->sin(D)D

    move-result-wide v3

    mul-double/2addr v1, v3

    iget-wide v3, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampedFreq:D

    mul-double/2addr v7, v3

    mul-double v3, v3, p5

    invoke-static {v3, v4}, Ljava/lang/Math;->cos(D)D

    move-result-wide v3

    mul-double/2addr v7, v3

    add-double/2addr v1, v7

    mul-double/2addr v9, v1

    add-double v7, v14, v9

    :goto_0
    invoke-static {v5, v6}, Ljava/lang/Math;->abs(D)D

    move-result-wide v1

    const-wide v3, 0x3fe3333340000000L

    cmpg-double v1, v1, v3

    if-gez v1, :cond_2

    const-wide/16 v5, 0x0

    move-wide v7, v5

    :cond_2
    iget-object v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mMassState:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    iget-wide v2, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mFinalPosition:D

    add-double/2addr v5, v2

    double-to-float v0, v5

    iput v0, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    double-to-float v0, v7

    iput v0, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    return-object v1
.end method""",
        'replacement': """.method updateValues(DDJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;
    .registers 23

    goto :goto_81

    nop

    :goto_0
    sub-double v12, v5, v12

    goto :goto_8

    nop

    :goto_1
    iget-wide v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampingRatio:D

    goto :goto_72

    nop

    :goto_2
    div-double/2addr v7, v12

    goto :goto_7f

    nop

    :goto_3
    neg-double v12, v12

    goto :goto_1a

    nop

    :goto_4
    if-gtz v9, :cond_0

    goto :goto_62

    :cond_0
    goto :goto_73

    nop

    :goto_5
    mul-double/2addr v5, v12

    goto :goto_26

    nop

    :goto_6
    mul-double/2addr v12, v1

    goto :goto_7

    nop

    :goto_7
    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v1

    goto :goto_63

    nop

    :goto_8
    div-double/2addr v3, v12

    goto :goto_13

    nop

    :goto_9
    iget-wide v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mNaturalFreq:D

    goto :goto_5f

    nop

    :goto_a
    mul-double/2addr v7, v12

    goto :goto_37

    nop

    :goto_b
    mul-double/2addr v9, v1

    goto :goto_69

    nop

    :goto_c
    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    goto :goto_54

    nop

    :goto_d
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mNaturalFreq:D

    goto :goto_3

    nop

    :goto_e
    return-object v1

    :goto_f
    mul-double/2addr v14, v3

    goto :goto_51

    nop

    :goto_10
    mul-double v3, v3, p5

    goto :goto_36

    nop

    :goto_11
    mul-double/2addr v12, v3

    goto :goto_31

    nop

    :goto_12
    div-double/2addr v7, v14

    goto :goto_5a

    nop

    :goto_13
    mul-double/2addr v5, v1

    goto :goto_2e

    nop

    :goto_14
    mul-double/2addr v7, v3

    goto :goto_79

    nop

    :goto_15
    invoke-static {v11, v12, v9, v10}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v9

    goto :goto_19

    nop

    :goto_16
    mul-double/2addr v12, v1

    goto :goto_35

    nop

    :goto_17
    add-double/2addr v5, v2

    goto :goto_3d

    nop

    :goto_18
    invoke-static {v5, v6}, Ljava/lang/Math;->abs(D)D

    move-result-wide v1

    goto :goto_3a

    nop

    :goto_19
    iget-wide v11, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampedFreq:D

    goto :goto_27

    nop

    :goto_1a
    mul-double/2addr v12, v1

    goto :goto_24

    nop

    :goto_1b
    sub-double v3, p1, v3

    goto :goto_1

    nop

    :goto_1c
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaMinus:D

    goto :goto_7a

    nop

    :goto_1d
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mNaturalFreq:D

    goto :goto_71

    nop

    :goto_1e
    mul-double/2addr v3, v12

    goto :goto_78

    nop

    :goto_1f
    mul-double/2addr v3, v12

    goto :goto_6

    nop

    :goto_20
    mul-double/2addr v14, v5

    goto :goto_48

    nop

    :goto_21
    const-wide v10, 0x4005bf0a8b145769L

    goto :goto_4

    nop

    :goto_22
    add-double v7, p3, v7

    goto :goto_7e

    nop

    :goto_23
    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    goto :goto_a

    nop

    :goto_24
    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    goto :goto_1e

    nop

    :goto_25
    add-double/2addr v7, v3

    goto :goto_61

    nop

    :goto_26
    mul-double/2addr v5, v1

    goto :goto_6b

    nop

    :goto_27
    move-wide/from16 p5, v1

    goto :goto_4a

    nop

    :goto_28
    mul-double/2addr v5, v12

    goto :goto_1d

    nop

    :goto_29
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampedFreq:D

    goto :goto_34

    nop

    :goto_2a
    mul-double/2addr v12, v1

    goto :goto_23

    nop

    :goto_2b
    mul-double v11, v11, p5

    goto :goto_4d

    nop

    :goto_2c
    mul-double/2addr v1, v3

    goto :goto_2b

    nop

    :goto_2d
    mul-double/2addr v9, v1

    goto :goto_3c

    nop

    :goto_2e
    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    goto :goto_3e

    nop

    :goto_2f
    goto :goto_6a

    :goto_30
    goto :goto_40

    nop

    :goto_31
    add-double/2addr v5, v12

    goto :goto_1c

    nop

    :goto_32
    add-double/2addr v7, v3

    goto :goto_2f

    nop

    :goto_33
    mul-double/2addr v14, v1

    goto :goto_5e

    nop

    :goto_34
    mul-double/2addr v12, v1

    goto :goto_84

    nop

    :goto_35
    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v1

    goto :goto_47

    nop

    :goto_36
    invoke-static {v3, v4}, Ljava/lang/Math;->cos(D)D

    move-result-wide v3

    goto :goto_14

    nop

    :goto_37
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaPlus:D

    goto :goto_1f

    nop

    :goto_38
    if-ltz v1, :cond_1

    goto :goto_76

    :cond_1
    goto :goto_58

    nop

    :goto_39
    iget-wide v3, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampedFreq:D

    goto :goto_5b

    nop

    :goto_3a
    const-wide v3, 0x3fe3333340000000L

    goto :goto_77

    nop

    :goto_3b
    mul-double/2addr v1, v3

    goto :goto_39

    nop

    :goto_3c
    const-wide v11, 0x4005bf0a8b145769L

    goto :goto_15

    nop

    :goto_3d
    double-to-float v0, v5

    goto :goto_70

    nop

    :goto_3e
    mul-double/2addr v5, v7

    goto :goto_68

    nop

    :goto_3f
    mul-double/2addr v12, v1

    goto :goto_50

    nop

    :goto_40
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampedFreq:D

    goto :goto_2

    nop

    :goto_41
    cmpl-double v9, v5, v7

    goto :goto_60

    nop

    :goto_42
    invoke-direct {v0}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->init()V

    goto :goto_67

    nop

    :goto_43
    iget-object v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mMassState:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    goto :goto_83

    nop

    :goto_44
    long-to-double v1, v1

    goto :goto_57

    nop

    :goto_45
    double-to-float v0, v7

    goto :goto_7d

    nop

    :goto_46
    mul-double/2addr v7, v14

    goto :goto_6f

    nop

    :goto_47
    mul-double/2addr v7, v1

    goto :goto_32

    nop

    :goto_48
    iget-wide v10, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampingRatio:D

    goto :goto_4e

    nop

    :goto_49
    mul-double v14, v5, v12

    goto :goto_f

    nop

    :goto_4a
    neg-double v1, v11

    goto :goto_2c

    nop

    :goto_4b
    neg-double v5, v5

    goto :goto_56

    nop

    :goto_4c
    neg-double v14, v12

    goto :goto_7b

    nop

    :goto_4d
    invoke-static {v11, v12}, Ljava/lang/Math;->sin(D)D

    move-result-wide v3

    goto :goto_3b

    nop

    :goto_4e
    mul-double/2addr v14, v10

    goto :goto_5c

    nop

    :goto_4f
    mul-double v7, v5, v3

    goto :goto_74

    nop

    :goto_50
    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    goto :goto_11

    nop

    :goto_51
    add-double v14, v14, p3

    goto :goto_46

    nop

    :goto_52
    mul-double/2addr v9, v12

    goto :goto_2d

    nop

    :goto_53
    add-double/2addr v3, v12

    goto :goto_4b

    nop

    :goto_54
    mul-double/2addr v5, v3

    goto :goto_d

    nop

    :goto_55
    neg-double v12, v12

    goto :goto_16

    nop

    :goto_56
    mul-double/2addr v5, v1

    goto :goto_c

    nop

    :goto_57
    const-wide v3, 0x41cdcd6500000000L

    goto :goto_6d

    nop

    :goto_58
    const-wide/16 v5, 0x0

    goto :goto_75

    nop

    :goto_59
    mul-double/2addr v14, v7

    goto :goto_64

    nop

    :goto_5a
    sub-double v7, v3, v7

    goto :goto_80

    nop

    :goto_5b
    mul-double/2addr v7, v3

    goto :goto_10

    nop

    :goto_5c
    neg-double v9, v10

    goto :goto_52

    nop

    :goto_5d
    sub-double v3, v3, p3

    goto :goto_0

    nop

    :goto_5e
    invoke-static {v14, v15}, Ljava/lang/Math;->sin(D)D

    move-result-wide v14

    goto :goto_59

    nop

    :goto_5f
    mul-double v7, v5, v3

    goto :goto_22

    nop

    :goto_60
    if-eqz v9, :cond_2

    goto :goto_30

    :cond_2
    goto :goto_9

    nop

    :goto_61
    goto :goto_6a

    :goto_62
    goto :goto_41

    nop

    :goto_63
    mul-double/2addr v3, v1

    goto :goto_25

    nop

    :goto_64
    add-double/2addr v12, v14

    goto :goto_28

    nop

    :goto_65
    iget-wide v3, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mFinalPosition:D

    goto :goto_1b

    nop

    :goto_66
    sub-double v14, v5, v12

    goto :goto_12

    nop

    :goto_67
    move-wide/from16 v1, p5

    goto :goto_44

    nop

    :goto_68
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaPlus:D

    goto :goto_3f

    nop

    :goto_69
    add-double v7, v14, v9

    :goto_6a
    goto :goto_18

    nop

    :goto_6b
    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    goto :goto_29

    nop

    :goto_6c
    cmpl-double v9, v5, v7

    goto :goto_21

    nop

    :goto_6d
    div-double/2addr v1, v3

    goto :goto_65

    nop

    :goto_6e
    mul-double/2addr v12, v3

    goto :goto_82

    nop

    :goto_6f
    neg-double v5, v5

    goto :goto_5

    nop

    :goto_70
    iput v0, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    goto :goto_45

    nop

    :goto_71
    neg-double v14, v12

    goto :goto_20

    nop

    :goto_72
    const-wide/high16 v7, 0x3ff0000000000000L

    goto :goto_6c

    nop

    :goto_73
    iget-wide v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaMinus:D

    goto :goto_4f

    nop

    :goto_74
    sub-double v7, v7, p3

    goto :goto_7c

    nop

    :goto_75
    move-wide v7, v5

    :goto_76
    goto :goto_43

    nop

    :goto_77
    cmpg-double v1, v1, v3

    goto :goto_38

    nop

    :goto_78
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mNaturalFreq:D

    goto :goto_4c

    nop

    :goto_79
    add-double/2addr v1, v7

    goto :goto_b

    nop

    :goto_7a
    mul-double/2addr v7, v12

    goto :goto_2a

    nop

    :goto_7b
    mul-double/2addr v3, v14

    goto :goto_55

    nop

    :goto_7c
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mGammaPlus:D

    goto :goto_66

    nop

    :goto_7d
    iput v0, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_e

    nop

    :goto_7e
    mul-double v12, v7, v1

    goto :goto_53

    nop

    :goto_7f
    iget-wide v12, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mNaturalFreq:D

    goto :goto_49

    nop

    :goto_80
    mul-double/2addr v3, v5

    goto :goto_5d

    nop

    :goto_81
    move-object/from16 v0, p0

    goto :goto_42

    nop

    :goto_82
    iget-wide v14, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mDampedFreq:D

    goto :goto_33

    nop

    :goto_83
    iget-wide v2, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->mFinalPosition:D

    goto :goto_17

    nop

    :goto_84
    invoke-static {v12, v13}, Ljava/lang/Math;->cos(D)D

    move-result-wide v12

    goto :goto_6e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
