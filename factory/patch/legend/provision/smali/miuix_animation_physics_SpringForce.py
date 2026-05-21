TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/SpringForce.smali'
CLASS_FALLBACK_NAMES = ['SpringForce.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/animation/physics/Force;', '.field public static final DAMPING_RATIO_HIGH_BOUNCY:F = 0.2f', '.field public static final DAMPING_RATIO_LOW_BOUNCY:F = 0.75f', '.field public static final DAMPING_RATIO_MEDIUM_BOUNCY:F = 0.5f', '.field public static final DAMPING_RATIO_NO_BOUNCY:F = 1.0f']

PATCHES = [
    {
        'id': 'miuix_animation_physics_SpringForce__init',
        'method': '.method protected init()V',
        'method_name': 'init',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/animation/physics/SpringForce;->mInitialized:Z', 'if-eqz v0, :cond_0', 'return-void', 'iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D', 'if-eqz v0, :cond_3', 'iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D', 'if-lez v4, :cond_1', 'iget-wide v6, p0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D'],
        'type': 'method_replace',
        'search': """.method protected init()V
    .registers 9

    iget-boolean v0, p0, Lmiuix/animation/physics/SpringForce;->mInitialized:Z

    if-eqz v0, :cond_0

    return-void

    :cond_0
    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D

    const-wide v2, 0x7fefffffffffffffL

    cmpl-double v0, v0, v2

    if-eqz v0, :cond_3

    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D

    const-wide/high16 v2, 0x3ff0000000000000L

    cmpl-double v4, v0, v2

    if-lez v4, :cond_1

    neg-double v4, v0

    iget-wide v6, p0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    mul-double/2addr v4, v6

    mul-double/2addr v0, v0

    sub-double/2addr v0, v2

    invoke-static {v0, v1}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide v0

    mul-double/2addr v6, v0

    add-double/2addr v4, v6

    iput-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mGammaPlus:D

    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D

    neg-double v4, v0

    iget-wide v6, p0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    mul-double/2addr v4, v6

    mul-double/2addr v0, v0

    sub-double/2addr v0, v2

    invoke-static {v0, v1}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide v0

    mul-double/2addr v6, v0

    sub-double/2addr v4, v6

    iput-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mGammaMinus:D

    goto :goto_0

    :cond_1
    const-wide/16 v4, 0x0

    cmpl-double v4, v0, v4

    if-ltz v4, :cond_2

    cmpg-double v4, v0, v2

    if-gez v4, :cond_2

    iget-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    mul-double/2addr v0, v0

    sub-double/2addr v2, v0

    invoke-static {v2, v3}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide v0

    mul-double/2addr v4, v0

    iput-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    :cond_2
    :goto_0
    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/animation/physics/SpringForce;->mInitialized:Z

    return-void

    :cond_3
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string v0, "Error: Final position of the spring must be set before the miuix.animation starts"

    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method protected init()V
    .registers 9

    goto :goto_25

    nop

    :goto_0
    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D

    goto :goto_21

    nop

    :goto_1
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_2f

    nop

    :goto_2
    iget-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    goto :goto_1b

    nop

    :goto_3
    mul-double/2addr v0, v0

    goto :goto_1a

    nop

    :goto_4
    neg-double v4, v0

    goto :goto_22

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_1

    nop

    :goto_7
    goto :goto_32

    :goto_8
    goto :goto_19

    nop

    :goto_9
    if-gtz v4, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_4

    nop

    :goto_a
    invoke-static {v0, v1}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide v0

    goto :goto_16

    nop

    :goto_b
    if-ltz v4, :cond_1

    goto :goto_32

    :cond_1
    goto :goto_2

    nop

    :goto_c
    iput-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mGammaPlus:D

    goto :goto_2d

    nop

    :goto_d
    invoke-static {v0, v1}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide v0

    goto :goto_14

    nop

    :goto_e
    const-wide/high16 v2, 0x3ff0000000000000L

    goto :goto_24

    nop

    :goto_f
    cmpl-double v4, v0, v4

    goto :goto_12

    nop

    :goto_10
    cmpl-double v0, v0, v2

    goto :goto_1f

    nop

    :goto_11
    if-nez v0, :cond_2

    goto :goto_2b

    :cond_2
    goto :goto_2a

    nop

    :goto_12
    if-gez v4, :cond_3

    goto :goto_32

    :cond_3
    goto :goto_34

    nop

    :goto_13
    const/4 v0, 0x1

    goto :goto_17

    nop

    :goto_14
    mul-double/2addr v6, v0

    goto :goto_27

    nop

    :goto_15
    sub-double/2addr v0, v2

    goto :goto_d

    nop

    :goto_16
    mul-double/2addr v6, v0

    goto :goto_28

    nop

    :goto_17
    iput-boolean v0, p0, Lmiuix/animation/physics/SpringForce;->mInitialized:Z

    goto :goto_5

    nop

    :goto_18
    mul-double/2addr v0, v0

    goto :goto_15

    nop

    :goto_19
    const-wide/16 v4, 0x0

    goto :goto_f

    nop

    :goto_1a
    sub-double/2addr v0, v2

    goto :goto_a

    nop

    :goto_1b
    mul-double/2addr v0, v0

    goto :goto_2c

    nop

    :goto_1c
    invoke-static {v2, v3}, Ljava/lang/Math;->sqrt(D)D

    move-result-wide v0

    goto :goto_30

    nop

    :goto_1d
    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_20

    nop

    :goto_1e
    mul-double/2addr v4, v6

    goto :goto_3

    nop

    :goto_1f
    if-nez v0, :cond_4

    goto :goto_6

    :cond_4
    goto :goto_2e

    nop

    :goto_20
    throw p0

    :goto_21
    const-wide v2, 0x7fefffffffffffffL

    goto :goto_10

    nop

    :goto_22
    iget-wide v6, p0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    goto :goto_33

    nop

    :goto_23
    neg-double v4, v0

    goto :goto_29

    nop

    :goto_24
    cmpl-double v4, v0, v2

    goto :goto_9

    nop

    :goto_25
    iget-boolean v0, p0, Lmiuix/animation/physics/SpringForce;->mInitialized:Z

    goto :goto_11

    nop

    :goto_26
    iput-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mGammaMinus:D

    goto :goto_7

    nop

    :goto_27
    add-double/2addr v4, v6

    goto :goto_c

    nop

    :goto_28
    sub-double/2addr v4, v6

    goto :goto_26

    nop

    :goto_29
    iget-wide v6, p0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    goto :goto_1e

    nop

    :goto_2a
    return-void

    :goto_2b
    goto :goto_0

    nop

    :goto_2c
    sub-double/2addr v2, v0

    goto :goto_1c

    nop

    :goto_2d
    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D

    goto :goto_23

    nop

    :goto_2e
    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D

    goto :goto_e

    nop

    :goto_2f
    const-string v0, "Error: Final position of the spring must be set before the miuix.animation starts"

    goto :goto_1d

    nop

    :goto_30
    mul-double/2addr v4, v0

    goto :goto_31

    nop

    :goto_31
    iput-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    :goto_32
    goto :goto_13

    nop

    :goto_33
    mul-double/2addr v4, v6

    goto :goto_18

    nop

    :goto_34
    cmpg-double v4, v0, v2

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_SpringForce__setValueThreshold',
        'method': '.method setValueThreshold(D)V',
        'method_name': 'setValueThreshold',
        'method_anchors': ['invoke-static {p1, p2}, Ljava/lang/Math;->abs(D)D', 'iput-wide p1, p0, Lmiuix/animation/physics/SpringForce;->mValueThreshold:D', 'iput-wide p1, p0, Lmiuix/animation/physics/SpringForce;->mVelocityThreshold:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method setValueThreshold(D)V
    .registers 5

    invoke-static {p1, p2}, Ljava/lang/Math;->abs(D)D

    move-result-wide p1

    iput-wide p1, p0, Lmiuix/animation/physics/SpringForce;->mValueThreshold:D

    const-wide v0, 0x404f400000000000L

    mul-double/2addr p1, v0

    iput-wide p1, p0, Lmiuix/animation/physics/SpringForce;->mVelocityThreshold:D

    return-void
.end method""",
        'replacement': """.method setValueThreshold(D)V
    .registers 5

    goto :goto_4

    nop

    :goto_0
    const-wide v0, 0x404f400000000000L

    goto :goto_3

    nop

    :goto_1
    return-void

    :goto_2
    iput-wide p1, p0, Lmiuix/animation/physics/SpringForce;->mVelocityThreshold:D

    goto :goto_1

    nop

    :goto_3
    mul-double/2addr p1, v0

    goto :goto_2

    nop

    :goto_4
    invoke-static {p1, p2}, Ljava/lang/Math;->abs(D)D

    move-result-wide p1

    goto :goto_5

    nop

    :goto_5
    iput-wide p1, p0, Lmiuix/animation/physics/SpringForce;->mValueThreshold:D

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_SpringForce__updateValues',
        'method': '.method updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;',
        'method_name': 'updateValues',
        'method_anchors': ['invoke-virtual {v0}, Lmiuix/animation/physics/SpringForce;->init()V', 'iget-wide v3, v0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D', 'iget-wide v5, v0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D', 'if-lez v9, :cond_0', 'iget-wide v5, v0, Lmiuix/animation/physics/SpringForce;->mGammaMinus:D', 'iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mGammaPlus:D', 'invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D', 'iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mGammaPlus:D'],
        'type': 'method_replace',
        'search': """.method updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;
    .registers 23

    move-object/from16 v0, p0

    invoke-virtual {v0}, Lmiuix/animation/physics/SpringForce;->init()V

    move-wide/from16 v1, p5

    long-to-double v1, v1

    const-wide v3, 0x41cdcd6500000000L

    div-double/2addr v1, v3

    iget-wide v3, v0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D

    sub-double v3, p1, v3

    iget-wide v5, v0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D

    const-wide/high16 v7, 0x3ff0000000000000L

    cmpl-double v9, v5, v7

    const-wide v10, 0x4005bf0a8b145769L

    if-lez v9, :cond_0

    iget-wide v5, v0, Lmiuix/animation/physics/SpringForce;->mGammaMinus:D

    mul-double v7, v5, v3

    sub-double v7, v7, p3

    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mGammaPlus:D

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

    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mGammaPlus:D

    mul-double/2addr v12, v1

    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    mul-double/2addr v12, v3

    add-double/2addr v5, v12

    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mGammaMinus:D

    mul-double/2addr v7, v12

    mul-double/2addr v12, v1

    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    mul-double/2addr v7, v12

    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mGammaPlus:D

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

    iget-wide v5, v0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    mul-double v7, v5, v3

    add-double v7, p3, v7

    mul-double v12, v7, v1

    add-double/2addr v3, v12

    neg-double v5, v5

    mul-double/2addr v5, v1

    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    mul-double/2addr v5, v3

    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    neg-double v12, v12

    mul-double/2addr v12, v1

    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    mul-double/2addr v3, v12

    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

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
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    div-double/2addr v7, v12

    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    mul-double v14, v5, v12

    mul-double/2addr v14, v3

    add-double v14, v14, p3

    mul-double/2addr v7, v14

    neg-double v5, v5

    mul-double/2addr v5, v12

    mul-double/2addr v5, v1

    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    mul-double/2addr v12, v1

    invoke-static {v12, v13}, Ljava/lang/Math;->cos(D)D

    move-result-wide v12

    mul-double/2addr v12, v3

    iget-wide v14, v0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    mul-double/2addr v14, v1

    invoke-static {v14, v15}, Ljava/lang/Math;->sin(D)D

    move-result-wide v14

    mul-double/2addr v14, v7

    add-double/2addr v12, v14

    mul-double/2addr v5, v12

    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    neg-double v14, v12

    mul-double/2addr v14, v5

    iget-wide v10, v0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D

    mul-double/2addr v14, v10

    neg-double v9, v10

    mul-double/2addr v9, v12

    mul-double/2addr v9, v1

    const-wide v11, 0x4005bf0a8b145769L

    invoke-static {v11, v12, v9, v10}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v9

    iget-wide v11, v0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    move-wide/from16 p5, v1

    neg-double v1, v11

    mul-double/2addr v1, v3

    mul-double v11, v11, p5

    invoke-static {v11, v12}, Ljava/lang/Math;->sin(D)D

    move-result-wide v3

    mul-double/2addr v1, v3

    iget-wide v3, v0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    mul-double/2addr v7, v3

    mul-double v3, v3, p5

    invoke-static {v3, v4}, Ljava/lang/Math;->cos(D)D

    move-result-wide v3

    mul-double/2addr v7, v3

    add-double/2addr v1, v7

    mul-double/2addr v9, v1

    add-double v7, v14, v9

    :goto_0
    iget-object v1, v0, Lmiuix/animation/physics/SpringForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    iget-wide v2, v0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D

    add-double/2addr v5, v2

    double-to-float v0, v5

    iput v0, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    double-to-float v0, v7

    iput v0, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    return-object v1
.end method""",
        'replacement': """.method updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;
    .registers 23

    goto :goto_6e

    nop

    :goto_0
    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    goto :goto_3

    nop

    :goto_1
    add-double v14, v14, p3

    goto :goto_2d

    nop

    :goto_2
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    goto :goto_54

    nop

    :goto_3
    mul-double/2addr v5, v7

    goto :goto_74

    nop

    :goto_4
    neg-double v1, v11

    goto :goto_6f

    nop

    :goto_5
    mul-double/2addr v7, v1

    goto :goto_42

    nop

    :goto_6
    mul-double/2addr v12, v1

    goto :goto_50

    nop

    :goto_7
    mul-double/2addr v5, v1

    goto :goto_0

    nop

    :goto_8
    neg-double v14, v12

    goto :goto_68

    nop

    :goto_9
    mul-double/2addr v14, v7

    goto :goto_34

    nop

    :goto_a
    mul-double v11, v11, p5

    goto :goto_52

    nop

    :goto_b
    iget-wide v5, v0, Lmiuix/animation/physics/SpringForce;->mGammaMinus:D

    goto :goto_4d

    nop

    :goto_c
    neg-double v5, v5

    goto :goto_2a

    nop

    :goto_d
    mul-double/2addr v3, v1

    goto :goto_5c

    nop

    :goto_e
    invoke-static {v3, v4}, Ljava/lang/Math;->cos(D)D

    move-result-wide v3

    goto :goto_51

    nop

    :goto_f
    mul-double/2addr v3, v12

    goto :goto_6b

    nop

    :goto_10
    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v1

    goto :goto_d

    nop

    :goto_11
    move-wide/from16 p5, v1

    goto :goto_4

    nop

    :goto_12
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    goto :goto_4c

    nop

    :goto_13
    mul-double/2addr v14, v3

    goto :goto_1

    nop

    :goto_14
    neg-double v9, v10

    goto :goto_44

    nop

    :goto_15
    const-wide v3, 0x41cdcd6500000000L

    goto :goto_6d

    nop

    :goto_16
    mul-double/2addr v1, v3

    goto :goto_5e

    nop

    :goto_17
    mul-double/2addr v7, v12

    goto :goto_30

    nop

    :goto_18
    if-gtz v9, :cond_0

    goto :goto_24

    :cond_0
    goto :goto_b

    nop

    :goto_19
    sub-double v3, p1, v3

    goto :goto_59

    nop

    :goto_1a
    add-double/2addr v1, v7

    goto :goto_22

    nop

    :goto_1b
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mGammaPlus:D

    goto :goto_37

    nop

    :goto_1c
    iget-wide v5, v0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    goto :goto_72

    nop

    :goto_1d
    mul-double/2addr v7, v3

    goto :goto_5d

    nop

    :goto_1e
    double-to-float v0, v5

    goto :goto_7a

    nop

    :goto_1f
    iget-wide v14, v0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    goto :goto_28

    nop

    :goto_20
    goto :goto_6a

    :goto_21
    goto :goto_12

    nop

    :goto_22
    mul-double/2addr v9, v1

    goto :goto_69

    nop

    :goto_23
    goto :goto_6a

    :goto_24
    goto :goto_3d

    nop

    :goto_25
    invoke-static {v14, v15}, Ljava/lang/Math;->sin(D)D

    move-result-wide v14

    goto :goto_9

    nop

    :goto_26
    mul-double/2addr v5, v3

    goto :goto_2

    nop

    :goto_27
    mul-double/2addr v5, v12

    goto :goto_39

    nop

    :goto_28
    mul-double/2addr v14, v1

    goto :goto_25

    nop

    :goto_29
    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    goto :goto_58

    nop

    :goto_2a
    mul-double/2addr v5, v1

    goto :goto_35

    nop

    :goto_2b
    sub-double v3, v3, p3

    goto :goto_3e

    nop

    :goto_2c
    invoke-virtual {v0}, Lmiuix/animation/physics/SpringForce;->init()V

    goto :goto_7c

    nop

    :goto_2d
    mul-double/2addr v7, v14

    goto :goto_63

    nop

    :goto_2e
    add-double v7, p3, v7

    goto :goto_47

    nop

    :goto_2f
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mGammaPlus:D

    goto :goto_f

    nop

    :goto_30
    mul-double/2addr v12, v1

    goto :goto_31

    nop

    :goto_31
    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    goto :goto_56

    nop

    :goto_32
    mul-double/2addr v5, v12

    goto :goto_4e

    nop

    :goto_33
    iget-wide v10, v0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D

    goto :goto_67

    nop

    :goto_34
    add-double/2addr v12, v14

    goto :goto_32

    nop

    :goto_35
    invoke-static {v10, v11, v5, v6}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v5

    goto :goto_26

    nop

    :goto_36
    iget-wide v2, v0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D

    goto :goto_77

    nop

    :goto_37
    sub-double v14, v5, v12

    goto :goto_48

    nop

    :goto_38
    sub-double v7, v7, p3

    goto :goto_1b

    nop

    :goto_39
    mul-double/2addr v5, v1

    goto :goto_29

    nop

    :goto_3a
    iget-wide v11, v0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    goto :goto_11

    nop

    :goto_3b
    const-wide/high16 v7, 0x3ff0000000000000L

    goto :goto_53

    nop

    :goto_3c
    mul-double v14, v5, v12

    goto :goto_13

    nop

    :goto_3d
    cmpl-double v9, v5, v7

    goto :goto_5a

    nop

    :goto_3e
    sub-double v12, v5, v12

    goto :goto_6c

    nop

    :goto_3f
    long-to-double v1, v1

    goto :goto_15

    nop

    :goto_40
    mul-double/2addr v12, v1

    goto :goto_78

    nop

    :goto_41
    mul-double/2addr v12, v1

    goto :goto_4f

    nop

    :goto_42
    add-double/2addr v7, v3

    goto :goto_20

    nop

    :goto_43
    mul-double/2addr v3, v5

    goto :goto_2b

    nop

    :goto_44
    mul-double/2addr v9, v12

    goto :goto_66

    nop

    :goto_45
    add-double/2addr v5, v12

    goto :goto_7d

    nop

    :goto_46
    const-wide v11, 0x4005bf0a8b145769L

    goto :goto_49

    nop

    :goto_47
    mul-double v12, v7, v1

    goto :goto_55

    nop

    :goto_48
    div-double/2addr v7, v14

    goto :goto_64

    nop

    :goto_49
    invoke-static {v11, v12, v9, v10}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v9

    goto :goto_3a

    nop

    :goto_4a
    iget-wide v3, v0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D

    goto :goto_19

    nop

    :goto_4b
    iput v0, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_70

    nop

    :goto_4c
    div-double/2addr v7, v12

    goto :goto_76

    nop

    :goto_4d
    mul-double v7, v5, v3

    goto :goto_38

    nop

    :goto_4e
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    goto :goto_8

    nop

    :goto_4f
    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    goto :goto_73

    nop

    :goto_50
    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v1

    goto :goto_5

    nop

    :goto_51
    mul-double/2addr v7, v3

    goto :goto_1a

    nop

    :goto_52
    invoke-static {v11, v12}, Ljava/lang/Math;->sin(D)D

    move-result-wide v3

    goto :goto_16

    nop

    :goto_53
    cmpl-double v9, v5, v7

    goto :goto_65

    nop

    :goto_54
    neg-double v12, v12

    goto :goto_71

    nop

    :goto_55
    add-double/2addr v3, v12

    goto :goto_c

    nop

    :goto_56
    mul-double/2addr v7, v12

    goto :goto_2f

    nop

    :goto_57
    neg-double v14, v12

    goto :goto_7b

    nop

    :goto_58
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    goto :goto_40

    nop

    :goto_59
    iget-wide v5, v0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D

    goto :goto_3b

    nop

    :goto_5a
    if-eqz v9, :cond_1

    goto :goto_21

    :cond_1
    goto :goto_1c

    nop

    :goto_5b
    double-to-float v0, v7

    goto :goto_4b

    nop

    :goto_5c
    add-double/2addr v7, v3

    goto :goto_23

    nop

    :goto_5d
    mul-double v3, v3, p5

    goto :goto_e

    nop

    :goto_5e
    iget-wide v3, v0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    goto :goto_1d

    nop

    :goto_5f
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    goto :goto_57

    nop

    :goto_60
    iget-object v1, v0, Lmiuix/animation/physics/SpringForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    goto :goto_36

    nop

    :goto_61
    invoke-static {v10, v11, v12, v13}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v12

    goto :goto_79

    nop

    :goto_62
    mul-double/2addr v12, v3

    goto :goto_1f

    nop

    :goto_63
    neg-double v5, v5

    goto :goto_27

    nop

    :goto_64
    sub-double v7, v3, v7

    goto :goto_43

    nop

    :goto_65
    const-wide v10, 0x4005bf0a8b145769L

    goto :goto_18

    nop

    :goto_66
    mul-double/2addr v9, v1

    goto :goto_46

    nop

    :goto_67
    mul-double/2addr v14, v10

    goto :goto_14

    nop

    :goto_68
    mul-double/2addr v14, v5

    goto :goto_33

    nop

    :goto_69
    add-double v7, v14, v9

    :goto_6a
    goto :goto_60

    nop

    :goto_6b
    mul-double/2addr v12, v1

    goto :goto_10

    nop

    :goto_6c
    div-double/2addr v3, v12

    goto :goto_7

    nop

    :goto_6d
    div-double/2addr v1, v3

    goto :goto_4a

    nop

    :goto_6e
    move-object/from16 v0, p0

    goto :goto_2c

    nop

    :goto_6f
    mul-double/2addr v1, v3

    goto :goto_a

    nop

    :goto_70
    return-object v1

    :goto_71
    mul-double/2addr v12, v1

    goto :goto_61

    nop

    :goto_72
    mul-double v7, v5, v3

    goto :goto_2e

    nop

    :goto_73
    mul-double/2addr v12, v3

    goto :goto_45

    nop

    :goto_74
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mGammaPlus:D

    goto :goto_41

    nop

    :goto_75
    neg-double v12, v12

    goto :goto_6

    nop

    :goto_76
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    goto :goto_3c

    nop

    :goto_77
    add-double/2addr v5, v2

    goto :goto_1e

    nop

    :goto_78
    invoke-static {v12, v13}, Ljava/lang/Math;->cos(D)D

    move-result-wide v12

    goto :goto_62

    nop

    :goto_79
    mul-double/2addr v3, v12

    goto :goto_5f

    nop

    :goto_7a
    iput v0, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    goto :goto_5b

    nop

    :goto_7b
    mul-double/2addr v3, v14

    goto :goto_75

    nop

    :goto_7c
    move-wide/from16 v1, p5

    goto :goto_3f

    nop

    :goto_7d
    iget-wide v12, v0, Lmiuix/animation/physics/SpringForce;->mGammaMinus:D

    goto :goto_17

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
