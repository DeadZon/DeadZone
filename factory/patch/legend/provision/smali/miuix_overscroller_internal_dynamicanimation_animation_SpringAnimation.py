TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/overscroller/internal/dynamicanimation/animation/SpringAnimation.smali'
CLASS_FALLBACK_NAMES = ['SpringAnimation.smali']
CLASS_ANCHORS = ['.super Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;']

PATCHES = [
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_SpringAnimation__isAtEquilibrium',
        'method': '.method isAtEquilibrium(FF)Z',
        'method_name': 'isAtEquilibrium',
        'method_anchors': ['iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;', 'invoke-virtual {p0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->isAtEquilibrium(FF)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method isAtEquilibrium(FF)Z
    .registers 3

    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    invoke-virtual {p0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->isAtEquilibrium(FF)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method isAtEquilibrium(FF)Z
    .registers 3

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->isAtEquilibrium(FF)Z

    move-result p0

    goto :goto_2

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_0

    nop

    :goto_2
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_SpringAnimation__setValueThreshold',
        'method': '.method setValueThreshold(F)V',
        'method_name': 'setValueThreshold',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method setValueThreshold(F)V
    .registers 2

    return-void
.end method""",
        'replacement': """.method setValueThreshold(F)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_SpringAnimation__updateValueAndVelocity',
        'method': '.method updateValueAndVelocity(J)Z',
        'method_name': 'updateValueAndVelocity',
        'method_anchors': ['iget-boolean v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mEndRequested:Z', 'if-eqz v1, :cond_1', 'iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F', 'if-eqz v6, :cond_0', 'iget-object v6, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;', 'invoke-virtual {v6, v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->setFinalPosition(F)Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;', 'iput v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F', 'iget-object v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;'],
        'type': 'method_replace',
        'search': """.method updateValueAndVelocity(J)Z
    .registers 23

    move-object/from16 v0, p0

    iget-boolean v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mEndRequested:Z

    const/4 v2, 0x1

    const/4 v3, 0x0

    const/4 v4, 0x0

    const v5, 0x7f7fffff

    if-eqz v1, :cond_1

    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F

    cmpl-float v6, v1, v5

    if-eqz v6, :cond_0

    iget-object v6, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    invoke-virtual {v6, v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->setFinalPosition(F)Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    iput v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F

    :cond_0
    iget-object v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    invoke-virtual {v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->getFinalPosition()F

    move-result v1

    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    iput v4, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    iput-boolean v3, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mEndRequested:Z

    return v2

    :cond_1
    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F

    cmpl-float v1, v1, v5

    if-eqz v1, :cond_2

    iget-object v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    invoke-virtual {v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->getFinalPosition()F

    iget-object v6, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    float-to-double v7, v1

    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    float-to-double v9, v1

    const-wide/16 v11, 0x2

    div-long v18, p1, v11

    move-wide/from16 v11, v18

    invoke-virtual/range {v6 .. v12}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->updateValues(DDJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    move-result-object v1

    iget-object v6, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    iget v7, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F

    invoke-virtual {v6, v7}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->setFinalPosition(F)Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    iput v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F

    iget-object v13, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    iget v5, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    float-to-double v14, v5

    iget v1, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    float-to-double v5, v1

    move-wide/from16 v16, v5

    invoke-virtual/range {v13 .. v19}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->updateValues(DDJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    move-result-object v1

    iget v5, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    iput v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    iget v1, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    goto :goto_0

    :cond_2
    iget-object v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    float-to-double v6, v1

    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    float-to-double v8, v1

    move-wide/from16 v10, p1

    invoke-virtual/range {v5 .. v11}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->updateValues(DDJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    move-result-object v1

    iget v5, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    iput v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    iget v1, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    :goto_0
    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    iget v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMinValue:F

    invoke-static {v1, v5}, Ljava/lang/Math;->max(FF)F

    move-result v1

    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    iget v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMaxValue:F

    invoke-static {v1, v5}, Ljava/lang/Math;->min(FF)F

    move-result v1

    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    iget v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    invoke-virtual {v0, v1, v5}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->isAtEquilibrium(FF)Z

    move-result v1

    if-eqz v1, :cond_3

    iget-object v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    invoke-virtual {v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->getFinalPosition()F

    move-result v1

    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    iput v4, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    return v2

    :cond_3
    return v3
.end method""",
        'replacement': """.method updateValueAndVelocity(J)Z
    .registers 23

    goto :goto_2d

    nop

    :goto_0
    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_43

    nop

    :goto_1
    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_4c

    nop

    :goto_2
    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    :goto_3
    goto :goto_3e

    nop

    :goto_4
    iget v1, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_33

    nop

    :goto_5
    invoke-static {v1, v5}, Ljava/lang/Math;->min(FF)F

    move-result v1

    goto :goto_29

    nop

    :goto_6
    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_10

    nop

    :goto_7
    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    goto :goto_3a

    nop

    :goto_8
    invoke-virtual {v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->getFinalPosition()F

    goto :goto_4b

    nop

    :goto_9
    iget-boolean v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mEndRequested:Z

    goto :goto_11

    nop

    :goto_a
    if-nez v1, :cond_0

    goto :goto_36

    :cond_0
    goto :goto_47

    nop

    :goto_b
    cmpl-float v6, v1, v5

    goto :goto_31

    nop

    :goto_c
    iput v4, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    goto :goto_18

    nop

    :goto_d
    invoke-virtual {v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->getFinalPosition()F

    move-result v1

    goto :goto_0

    nop

    :goto_e
    if-nez v1, :cond_1

    goto :goto_20

    :cond_1
    goto :goto_f

    nop

    :goto_f
    iget-object v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_8

    nop

    :goto_10
    iget v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMaxValue:F

    goto :goto_5

    nop

    :goto_11
    const/4 v2, 0x1

    goto :goto_45

    nop

    :goto_12
    iget v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMinValue:F

    goto :goto_13

    nop

    :goto_13
    invoke-static {v1, v5}, Ljava/lang/Math;->max(FF)F

    move-result v1

    goto :goto_6

    nop

    :goto_14
    iget-object v13, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_4a

    nop

    :goto_15
    move-wide/from16 v10, p1

    goto :goto_23

    nop

    :goto_16
    iget v1, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_2

    nop

    :goto_17
    iget v5, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    goto :goto_44

    nop

    :goto_18
    iput-boolean v3, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mEndRequested:Z

    goto :goto_35

    nop

    :goto_19
    iget v1, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_49

    nop

    :goto_1a
    invoke-virtual/range {v13 .. v19}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->updateValues(DDJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    move-result-object v1

    goto :goto_17

    nop

    :goto_1b
    iget v7, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F

    goto :goto_4f

    nop

    :goto_1c
    iput v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F

    :goto_1d
    goto :goto_32

    nop

    :goto_1e
    iput v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_16

    nop

    :goto_1f
    goto :goto_3

    :goto_20
    goto :goto_25

    nop

    :goto_21
    iget v5, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    goto :goto_1e

    nop

    :goto_22
    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    goto :goto_3d

    nop

    :goto_23
    invoke-virtual/range {v5 .. v11}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->updateValues(DDJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    move-result-object v1

    goto :goto_21

    nop

    :goto_24
    float-to-double v14, v5

    goto :goto_4

    nop

    :goto_25
    iget-object v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_2a

    nop

    :goto_26
    invoke-virtual {v6, v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->setFinalPosition(F)Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_1c

    nop

    :goto_27
    move-wide/from16 v16, v5

    goto :goto_1a

    nop

    :goto_28
    const/4 v4, 0x0

    goto :goto_3c

    nop

    :goto_29
    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_3b

    nop

    :goto_2a
    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_30

    nop

    :goto_2b
    const-wide/16 v11, 0x2

    goto :goto_37

    nop

    :goto_2c
    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F

    goto :goto_41

    nop

    :goto_2d
    move-object/from16 v0, p0

    goto :goto_9

    nop

    :goto_2e
    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_c

    nop

    :goto_2f
    invoke-virtual {v0, v1, v5}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->isAtEquilibrium(FF)Z

    move-result v1

    goto :goto_34

    nop

    :goto_30
    float-to-double v6, v1

    goto :goto_7

    nop

    :goto_31
    if-nez v6, :cond_2

    goto :goto_1d

    :cond_2
    goto :goto_42

    nop

    :goto_32
    iget-object v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_48

    nop

    :goto_33
    float-to-double v5, v1

    goto :goto_27

    nop

    :goto_34
    if-nez v1, :cond_3

    goto :goto_4e

    :cond_3
    goto :goto_46

    nop

    :goto_35
    return v2

    :goto_36
    goto :goto_2c

    nop

    :goto_37
    div-long v18, p1, v11

    goto :goto_39

    nop

    :goto_38
    iget-object v6, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_1b

    nop

    :goto_39
    move-wide/from16 v11, v18

    goto :goto_3f

    nop

    :goto_3a
    float-to-double v8, v1

    goto :goto_15

    nop

    :goto_3b
    iget v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    goto :goto_2f

    nop

    :goto_3c
    const v5, 0x7f7fffff

    goto :goto_a

    nop

    :goto_3d
    float-to-double v9, v1

    goto :goto_2b

    nop

    :goto_3e
    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_12

    nop

    :goto_3f
    invoke-virtual/range {v6 .. v12}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->updateValues(DDJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    move-result-object v1

    goto :goto_38

    nop

    :goto_40
    iput v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F

    goto :goto_14

    nop

    :goto_41
    cmpl-float v1, v1, v5

    goto :goto_e

    nop

    :goto_42
    iget-object v6, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_26

    nop

    :goto_43
    iput v4, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    goto :goto_4d

    nop

    :goto_44
    iput v5, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_19

    nop

    :goto_45
    const/4 v3, 0x0

    goto :goto_28

    nop

    :goto_46
    iget-object v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_d

    nop

    :goto_47
    iget v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mPendingPosition:F

    goto :goto_b

    nop

    :goto_48
    invoke-virtual {v1}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->getFinalPosition()F

    move-result v1

    goto :goto_2e

    nop

    :goto_49
    iput v1, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    goto :goto_1f

    nop

    :goto_4a
    iget v5, v1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    goto :goto_24

    nop

    :goto_4b
    iget-object v6, v0, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringAnimation;->mSpring:Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_1

    nop

    :goto_4c
    float-to-double v7, v1

    goto :goto_22

    nop

    :goto_4d
    return v2

    :goto_4e
    goto :goto_50

    nop

    :goto_4f
    invoke-virtual {v6, v7}, Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;->setFinalPosition(F)Lmiuix/overscroller/internal/dynamicanimation/animation/SpringForce;

    goto :goto_40

    nop

    :goto_50
    return v3
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
