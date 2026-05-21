TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/FlingAnimation$DragForce.smali'
CLASS_FALLBACK_NAMES = ['FlingAnimation$DragForce.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/animation/physics/Force;', '.field private static final DEFAULT_FRICTION:F = -4.2f', '.field private static final VELOCITY_THRESHOLD_MULTIPLIER:F = 62.5f']

PATCHES = [
    {
        'id': 'miuix_animation_physics_FlingAnimation__DragForce__getFrictionScalar',
        'method': '.method getFrictionScalar()F',
        'method_name': 'getFrictionScalar',
        'method_anchors': ['iget p0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F', 'return p0'],
        'type': 'method_replace',
        'search': """.method getFrictionScalar()F
    .registers 2

    iget p0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F

    const v0, -0x3f79999a

    div-float/2addr p0, v0

    return p0
.end method""",
        'replacement': """.method getFrictionScalar()F
    .registers 2

    goto :goto_3

    nop

    :goto_0
    div-float/2addr p0, v0

    goto :goto_1

    nop

    :goto_1
    return p0

    :goto_2
    const v0, -0x3f79999a

    goto :goto_0

    nop

    :goto_3
    iget p0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_FlingAnimation__DragForce__setFrictionScalar',
        'method': '.method setFrictionScalar(F)V',
        'method_name': 'setFrictionScalar',
        'method_anchors': ['iput p1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F', 'return-void'],
        'type': 'method_replace',
        'search': """.method setFrictionScalar(F)V
    .registers 3

    const v0, -0x3f79999a

    mul-float/2addr p1, v0

    iput p1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F

    return-void
.end method""",
        'replacement': """.method setFrictionScalar(F)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    iput p1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F

    goto :goto_0

    nop

    :goto_2
    const v0, -0x3f79999a

    goto :goto_3

    nop

    :goto_3
    mul-float/2addr p1, v0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_FlingAnimation__DragForce__setValueThreshold',
        'method': '.method setValueThreshold(F)V',
        'method_name': 'setValueThreshold',
        'method_anchors': ['iput p1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mVelocityThreshold:F', 'return-void'],
        'type': 'method_replace',
        'search': """.method setValueThreshold(F)V
    .registers 3

    const/high16 v0, 0x427a0000

    mul-float/2addr p1, v0

    iput p1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mVelocityThreshold:F

    return-void
.end method""",
        'replacement': """.method setValueThreshold(F)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    iput p1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mVelocityThreshold:F

    goto :goto_2

    nop

    :goto_1
    mul-float/2addr p1, v0

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    const/high16 v0, 0x427a0000

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_FlingAnimation__DragForce__updateValueAndVelocity',
        'method': '.method updateValueAndVelocity(FFJ)Lmiuix/animation/physics/DynamicAnimation$MassState;',
        'method_name': 'updateValueAndVelocity',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;', 'iget v3, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F', 'invoke-static {v3, v4}, Ljava/lang/Math;->exp(D)D', 'iput v1, v0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F', 'iget-object v0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;', 'iget v1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F', 'invoke-static {v4, v5}, Ljava/lang/Math;->exp(D)D', 'iput p1, v0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F'],
        'type': 'method_replace',
        'search': """.method updateValueAndVelocity(FFJ)Lmiuix/animation/physics/DynamicAnimation$MassState;
    .registers 11

    long-to-double p3, p3

    const-wide v0, 0x41cdcd6500000000L

    div-double/2addr p3, v0

    iget-object v0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    float-to-double v1, p2

    iget v3, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F

    float-to-double v3, v3

    mul-double/2addr v3, p3

    invoke-static {v3, v4}, Ljava/lang/Math;->exp(D)D

    move-result-wide v3

    mul-double/2addr v1, v3

    double-to-float v1, v1

    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    iget-object v0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    iget v1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F

    div-float v2, p2, v1

    sub-float/2addr p1, v2

    float-to-double v2, p1

    div-float/2addr p2, v1

    float-to-double p1, p2

    float-to-double v4, v1

    mul-double/2addr v4, p3

    invoke-static {v4, v5}, Ljava/lang/Math;->exp(D)D

    move-result-wide p3

    mul-double/2addr p1, p3

    add-double/2addr v2, p1

    double-to-float p1, v2

    iput p1, v0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    iget-object p1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    iget p2, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    iget p1, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    invoke-virtual {p0, p2, p1}, Lmiuix/animation/physics/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    const/4 p2, 0x0

    iput p2, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    :cond_0
    iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    return-object p0
.end method""",
        'replacement': """.method updateValueAndVelocity(FFJ)Lmiuix/animation/physics/DynamicAnimation$MassState;
    .registers 11

    goto :goto_1f

    nop

    :goto_0
    mul-double/2addr v4, p3

    goto :goto_2

    nop

    :goto_1
    mul-double/2addr p1, p3

    goto :goto_1a

    nop

    :goto_2
    invoke-static {v4, v5}, Ljava/lang/Math;->exp(D)D

    move-result-wide p3

    goto :goto_1

    nop

    :goto_3
    float-to-double p1, p2

    goto :goto_f

    nop

    :goto_4
    mul-double/2addr v1, v3

    goto :goto_a

    nop

    :goto_5
    iget-object p1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    goto :goto_17

    nop

    :goto_6
    div-float v2, p2, v1

    goto :goto_19

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    goto :goto_1c

    nop

    :goto_8
    return-object p0

    :goto_9
    iget p1, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_18

    nop

    :goto_a
    double-to-float v1, v1

    goto :goto_20

    nop

    :goto_b
    iget v3, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F

    goto :goto_1b

    nop

    :goto_c
    mul-double/2addr v3, p3

    goto :goto_21

    nop

    :goto_d
    iput p1, v0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    goto :goto_e

    nop

    :goto_e
    iget-object p1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    goto :goto_1e

    nop

    :goto_f
    float-to-double v4, v1

    goto :goto_0

    nop

    :goto_10
    double-to-float p1, v2

    goto :goto_d

    nop

    :goto_11
    iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    goto :goto_8

    nop

    :goto_12
    div-float/2addr p2, v1

    goto :goto_3

    nop

    :goto_13
    iput p2, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    :goto_14
    goto :goto_11

    nop

    :goto_15
    float-to-double v2, p1

    goto :goto_12

    nop

    :goto_16
    if-nez p1, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_5

    nop

    :goto_17
    const/4 p2, 0x0

    goto :goto_13

    nop

    :goto_18
    invoke-virtual {p0, p2, p1}, Lmiuix/animation/physics/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z

    move-result p1

    goto :goto_16

    nop

    :goto_19
    sub-float/2addr p1, v2

    goto :goto_15

    nop

    :goto_1a
    add-double/2addr v2, p1

    goto :goto_10

    nop

    :goto_1b
    float-to-double v3, v3

    goto :goto_c

    nop

    :goto_1c
    float-to-double v1, p2

    goto :goto_b

    nop

    :goto_1d
    iget v1, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mFriction:F

    goto :goto_6

    nop

    :goto_1e
    iget p2, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    goto :goto_9

    nop

    :goto_1f
    long-to-double p3, p3

    goto :goto_23

    nop

    :goto_20
    iput v1, v0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_22

    nop

    :goto_21
    invoke-static {v3, v4}, Ljava/lang/Math;->exp(D)D

    move-result-wide v3

    goto :goto_4

    nop

    :goto_22
    iget-object v0, p0, Lmiuix/animation/physics/FlingAnimation$DragForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    goto :goto_1d

    nop

    :goto_23
    const-wide v0, 0x41cdcd6500000000L

    goto :goto_24

    nop

    :goto_24
    div-double/2addr p3, v0

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
