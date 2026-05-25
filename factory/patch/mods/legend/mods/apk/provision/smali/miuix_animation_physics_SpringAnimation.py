TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/SpringAnimation.smali'
CLASS_FALLBACK_NAMES = ['SpringAnimation.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/physics/DynamicAnimation;', '.field private static final UNSET:F = 3.4028235E38f']

PATCHES = [
    {
        'id': 'miuix_animation_physics_SpringAnimation__getAcceleration',
        'method': '.method getAcceleration(FF)F',
        'method_name': 'getAcceleration',
        'method_anchors': ['iget-object p0, p0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;', 'invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/SpringForce;->getAcceleration(FF)F', 'return p0'],
        'type': 'method_replace',
        'search': """.method getAcceleration(FF)F
    .registers 3

    iget-object p0, p0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/SpringForce;->getAcceleration(FF)F

    move-result p0

    return p0
.end method""",
        'replacement': """.method getAcceleration(FF)F
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return p0

    :goto_1
    invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/SpringForce;->getAcceleration(FF)F

    move-result p0

    goto :goto_0

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_SpringAnimation__isAtEquilibrium',
        'method': '.method isAtEquilibrium(FF)Z',
        'method_name': 'isAtEquilibrium',
        'method_anchors': ['iget-object p0, p0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;', 'invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/SpringForce;->isAtEquilibrium(FF)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method isAtEquilibrium(FF)Z
    .registers 3

    iget-object p0, p0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/SpringForce;->isAtEquilibrium(FF)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method isAtEquilibrium(FF)Z
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    goto :goto_2

    nop

    :goto_1
    return p0

    :goto_2
    invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/SpringForce;->isAtEquilibrium(FF)Z

    move-result p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_SpringAnimation__setValueThreshold',
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
        'id': 'miuix_animation_physics_SpringAnimation__updateValueAndVelocity',
        'method': '.method updateValueAndVelocity(J)Z',
        'method_name': 'updateValueAndVelocity',
        'method_anchors': ['iget-boolean v1, v0, Lmiuix/animation/physics/SpringAnimation;->mEndRequested:Z', 'if-eqz v1, :cond_1', 'iget v1, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F', 'if-eqz v6, :cond_0', 'iget-object v6, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;', 'invoke-virtual {v6, v1}, Lmiuix/animation/physics/SpringForce;->setFinalPosition(F)Lmiuix/animation/physics/SpringForce;', 'iput v5, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F', 'iget-object v1, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;'],
        'type': 'method_replace',
        'search': """.method updateValueAndVelocity(J)Z
    .registers 23

    move-object/from16 v0, p0

    iget-boolean v1, v0, Lmiuix/animation/physics/SpringAnimation;->mEndRequested:Z

    const/4 v2, 0x1

    const/4 v3, 0x0

    const/4 v4, 0x0

    const v5, 0x7f7fffff

    if-eqz v1, :cond_1

    iget v1, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F

    cmpl-float v6, v1, v5

    if-eqz v6, :cond_0

    iget-object v6, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    invoke-virtual {v6, v1}, Lmiuix/animation/physics/SpringForce;->setFinalPosition(F)Lmiuix/animation/physics/SpringForce;

    iput v5, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F

    :cond_0
    iget-object v1, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    invoke-virtual {v1}, Lmiuix/animation/physics/SpringForce;->getFinalPosition()F

    move-result v1

    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    iput v4, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    iput-boolean v3, v0, Lmiuix/animation/physics/SpringAnimation;->mEndRequested:Z

    return v2

    :cond_1
    iget v1, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F

    cmpl-float v1, v1, v5

    if-eqz v1, :cond_2

    iget-object v1, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    invoke-virtual {v1}, Lmiuix/animation/physics/SpringForce;->getFinalPosition()F

    iget-object v6, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    iget v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    float-to-double v7, v1

    iget v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    float-to-double v9, v1

    const-wide/16 v11, 0x2

    div-long v18, p1, v11

    move-wide/from16 v11, v18

    invoke-virtual/range {v6 .. v12}, Lmiuix/animation/physics/SpringForce;->updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;

    move-result-object v1

    iget-object v6, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    iget v7, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F

    invoke-virtual {v6, v7}, Lmiuix/animation/physics/SpringForce;->setFinalPosition(F)Lmiuix/animation/physics/SpringForce;

    iput v5, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F

    iget-object v13, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    iget v5, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    float-to-double v14, v5

    iget v1, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    float-to-double v5, v1

    move-wide/from16 v16, v5

    invoke-virtual/range {v13 .. v19}, Lmiuix/animation/physics/SpringForce;->updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;

    move-result-object v1

    iget v5, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    iput v5, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    iget v1, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    goto :goto_0

    :cond_2
    iget-object v5, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    iget v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    float-to-double v6, v1

    iget v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    float-to-double v8, v1

    move-wide/from16 v10, p1

    invoke-virtual/range {v5 .. v11}, Lmiuix/animation/physics/SpringForce;->updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;

    move-result-object v1

    iget v5, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    iput v5, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    iget v1, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    :goto_0
    iget v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    iget v5, v0, Lmiuix/animation/physics/DynamicAnimation;->mMinValue:F

    invoke-static {v1, v5}, Ljava/lang/Math;->max(FF)F

    move-result v1

    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    iget v5, v0, Lmiuix/animation/physics/DynamicAnimation;->mMaxValue:F

    invoke-static {v1, v5}, Ljava/lang/Math;->min(FF)F

    move-result v1

    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    iget v5, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    invoke-virtual {v0, v1, v5}, Lmiuix/animation/physics/SpringAnimation;->isAtEquilibrium(FF)Z

    move-result v1

    if-eqz v1, :cond_3

    iget-object v1, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    invoke-virtual {v1}, Lmiuix/animation/physics/SpringForce;->getFinalPosition()F

    move-result v1

    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    iput v4, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    return v2

    :cond_3
    return v3
.end method""",
        'replacement': """.method updateValueAndVelocity(J)Z
    .registers 23

    goto :goto_4c

    nop

    :goto_0
    const/4 v2, 0x1

    goto :goto_2c

    nop

    :goto_1
    div-long v18, p1, v11

    goto :goto_1e

    nop

    :goto_2
    iput v5, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_40

    nop

    :goto_3
    iput v5, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_33

    nop

    :goto_4
    iget v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    goto :goto_e

    nop

    :goto_5
    iget v5, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    goto :goto_3f

    nop

    :goto_6
    move-wide/from16 v10, p1

    goto :goto_4b

    nop

    :goto_7
    iget v7, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F

    goto :goto_26

    nop

    :goto_8
    iput-boolean v3, v0, Lmiuix/animation/physics/SpringAnimation;->mEndRequested:Z

    goto :goto_3d

    nop

    :goto_9
    return v3

    :goto_a
    const/4 v4, 0x0

    goto :goto_f

    nop

    :goto_b
    iget v5, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    goto :goto_39

    nop

    :goto_c
    iget-object v6, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    goto :goto_7

    nop

    :goto_d
    iget-object v6, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    goto :goto_34

    nop

    :goto_e
    float-to-double v9, v1

    goto :goto_43

    nop

    :goto_f
    const v5, 0x7f7fffff

    goto :goto_3c

    nop

    :goto_10
    invoke-virtual {v1}, Lmiuix/animation/physics/SpringForce;->getFinalPosition()F

    move-result v1

    goto :goto_2e

    nop

    :goto_11
    float-to-double v8, v1

    goto :goto_6

    nop

    :goto_12
    invoke-static {v1, v5}, Ljava/lang/Math;->min(FF)F

    move-result v1

    goto :goto_46

    nop

    :goto_13
    invoke-virtual/range {v13 .. v19}, Lmiuix/animation/physics/SpringForce;->updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;

    move-result-object v1

    goto :goto_22

    nop

    :goto_14
    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    goto :goto_1c

    nop

    :goto_15
    iget-object v1, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    goto :goto_49

    nop

    :goto_16
    iget v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    goto :goto_11

    nop

    :goto_17
    iget v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_1f

    nop

    :goto_18
    cmpl-float v6, v1, v5

    goto :goto_31

    nop

    :goto_19
    move-wide/from16 v16, v5

    goto :goto_13

    nop

    :goto_1a
    iget v5, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    goto :goto_2

    nop

    :goto_1b
    invoke-virtual {v1}, Lmiuix/animation/physics/SpringForce;->getFinalPosition()F

    goto :goto_20

    nop

    :goto_1c
    goto :goto_45

    :goto_1d
    goto :goto_41

    nop

    :goto_1e
    move-wide/from16 v11, v18

    goto :goto_4d

    nop

    :goto_1f
    iget v5, v0, Lmiuix/animation/physics/DynamicAnimation;->mMinValue:F

    goto :goto_25

    nop

    :goto_20
    iget-object v6, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    goto :goto_3b

    nop

    :goto_21
    iget v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_28

    nop

    :goto_22
    iget v5, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    goto :goto_3

    nop

    :goto_23
    iget v1, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_2a

    nop

    :goto_24
    if-nez v1, :cond_0

    goto :goto_1d

    :cond_0
    goto :goto_2f

    nop

    :goto_25
    invoke-static {v1, v5}, Ljava/lang/Math;->max(FF)F

    move-result v1

    goto :goto_42

    nop

    :goto_26
    invoke-virtual {v6, v7}, Lmiuix/animation/physics/SpringForce;->setFinalPosition(F)Lmiuix/animation/physics/SpringForce;

    goto :goto_29

    nop

    :goto_27
    iget-object v13, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    goto :goto_b

    nop

    :goto_28
    float-to-double v6, v1

    goto :goto_16

    nop

    :goto_29
    iput v5, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F

    goto :goto_27

    nop

    :goto_2a
    float-to-double v5, v1

    goto :goto_19

    nop

    :goto_2b
    float-to-double v7, v1

    goto :goto_4

    nop

    :goto_2c
    const/4 v3, 0x0

    goto :goto_a

    nop

    :goto_2d
    iput v4, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    goto :goto_4e

    nop

    :goto_2e
    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_38

    nop

    :goto_2f
    iget-object v1, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    goto :goto_1b

    nop

    :goto_30
    iget v5, v0, Lmiuix/animation/physics/DynamicAnimation;->mMaxValue:F

    goto :goto_12

    nop

    :goto_31
    if-nez v6, :cond_1

    goto :goto_36

    :cond_1
    goto :goto_d

    nop

    :goto_32
    iget v1, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F

    goto :goto_18

    nop

    :goto_33
    iget v1, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_14

    nop

    :goto_34
    invoke-virtual {v6, v1}, Lmiuix/animation/physics/SpringForce;->setFinalPosition(F)Lmiuix/animation/physics/SpringForce;

    goto :goto_35

    nop

    :goto_35
    iput v5, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F

    :goto_36
    goto :goto_48

    nop

    :goto_37
    cmpl-float v1, v1, v5

    goto :goto_24

    nop

    :goto_38
    iput v4, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    goto :goto_8

    nop

    :goto_39
    float-to-double v14, v5

    goto :goto_23

    nop

    :goto_3a
    if-nez v1, :cond_2

    goto :goto_4f

    :cond_2
    goto :goto_15

    nop

    :goto_3b
    iget v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_2b

    nop

    :goto_3c
    if-nez v1, :cond_3

    goto :goto_3e

    :cond_3
    goto :goto_32

    nop

    :goto_3d
    return v2

    :goto_3e
    goto :goto_47

    nop

    :goto_3f
    invoke-virtual {v0, v1, v5}, Lmiuix/animation/physics/SpringAnimation;->isAtEquilibrium(FF)Z

    move-result v1

    goto :goto_3a

    nop

    :goto_40
    iget v1, v1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_44

    nop

    :goto_41
    iget-object v5, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    goto :goto_21

    nop

    :goto_42
    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_30

    nop

    :goto_43
    const-wide/16 v11, 0x2

    goto :goto_1

    nop

    :goto_44
    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    :goto_45
    goto :goto_17

    nop

    :goto_46
    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_5

    nop

    :goto_47
    iget v1, v0, Lmiuix/animation/physics/SpringAnimation;->mPendingPosition:F

    goto :goto_37

    nop

    :goto_48
    iget-object v1, v0, Lmiuix/animation/physics/SpringAnimation;->mSpring:Lmiuix/animation/physics/SpringForce;

    goto :goto_10

    nop

    :goto_49
    invoke-virtual {v1}, Lmiuix/animation/physics/SpringForce;->getFinalPosition()F

    move-result v1

    goto :goto_50

    nop

    :goto_4a
    iget-boolean v1, v0, Lmiuix/animation/physics/SpringAnimation;->mEndRequested:Z

    goto :goto_0

    nop

    :goto_4b
    invoke-virtual/range {v5 .. v11}, Lmiuix/animation/physics/SpringForce;->updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;

    move-result-object v1

    goto :goto_1a

    nop

    :goto_4c
    move-object/from16 v0, p0

    goto :goto_4a

    nop

    :goto_4d
    invoke-virtual/range {v6 .. v12}, Lmiuix/animation/physics/SpringForce;->updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;

    move-result-object v1

    goto :goto_c

    nop

    :goto_4e
    return v2

    :goto_4f
    goto :goto_9

    nop

    :goto_50
    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_2d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
