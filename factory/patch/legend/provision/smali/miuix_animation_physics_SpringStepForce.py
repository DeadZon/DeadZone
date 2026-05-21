TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/SpringStepForce.smali'
CLASS_FALLBACK_NAMES = ['SpringStepForce.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/physics/SpringForce;']

PATCHES = [
    {
        'id': 'miuix_animation_physics_SpringStepForce__init',
        'method': '.method protected init()V',
        'method_name': 'init',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/animation/physics/SpringForce;->mInitialized:Z', 'if-eqz v0, :cond_0', 'return-void', 'iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D', 'if-eqz v0, :cond_1', 'iget-wide v2, p0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D', 'iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D', 'invoke-static {v2, v3, v0, v1}, Ljava/lang/Math;->min(DD)D'],
        'type': 'method_replace',
        'search': """.method protected init()V
    .registers 5

    iget-boolean v0, p0, Lmiuix/animation/physics/SpringForce;->mInitialized:Z

    if-eqz v0, :cond_0

    return-void

    :cond_0
    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D

    const-wide v2, 0x7fefffffffffffffL

    cmpl-double v0, v0, v2

    if-eqz v0, :cond_1

    const-wide/high16 v0, 0x4000000000000000L

    iget-wide v2, p0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    mul-double/2addr v2, v0

    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D

    mul-double/2addr v2, v0

    const-wide/high16 v0, 0x404e000000000000L

    invoke-static {v2, v3, v0, v1}, Ljava/lang/Math;->min(DD)D

    move-result-wide v0

    iput-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/animation/physics/SpringForce;->mInitialized:Z

    return-void

    :cond_1
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string v0, "Error: Final position of the spring must be set before the miuix.animation starts"

    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method protected init()V
    .registers 5

    goto :goto_0

    nop

    :goto_0
    iget-boolean v0, p0, Lmiuix/animation/physics/SpringForce;->mInitialized:Z

    goto :goto_b

    nop

    :goto_1
    const-wide/high16 v0, 0x4000000000000000L

    goto :goto_e

    nop

    :goto_2
    const/4 v0, 0x1

    goto :goto_7

    nop

    :goto_3
    iput-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    goto :goto_2

    nop

    :goto_4
    const-string v0, "Error: Final position of the spring must be set before the miuix.animation starts"

    goto :goto_5

    nop

    :goto_5
    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_15

    nop

    :goto_6
    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampingRatio:D

    goto :goto_12

    nop

    :goto_7
    iput-boolean v0, p0, Lmiuix/animation/physics/SpringForce;->mInitialized:Z

    goto :goto_13

    nop

    :goto_8
    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D

    goto :goto_11

    nop

    :goto_9
    const-wide/high16 v0, 0x404e000000000000L

    goto :goto_16

    nop

    :goto_a
    if-nez v0, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_1

    nop

    :goto_b
    if-nez v0, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_c

    nop

    :goto_c
    return-void

    :goto_d
    goto :goto_8

    nop

    :goto_e
    iget-wide v2, p0, Lmiuix/animation/physics/SpringForce;->mNaturalFreq:D

    goto :goto_f

    nop

    :goto_f
    mul-double/2addr v2, v0

    goto :goto_6

    nop

    :goto_10
    cmpl-double v0, v0, v2

    goto :goto_a

    nop

    :goto_11
    const-wide v2, 0x7fefffffffffffffL

    goto :goto_10

    nop

    :goto_12
    mul-double/2addr v2, v0

    goto :goto_9

    nop

    :goto_13
    return-void

    :goto_14
    goto :goto_17

    nop

    :goto_15
    throw p0

    :goto_16
    invoke-static {v2, v3, v0, v1}, Ljava/lang/Math;->min(DD)D

    move-result-wide v0

    goto :goto_3

    nop

    :goto_17
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_SpringStepForce__updateValues',
        'method': '.method updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;',
        'method_name': 'updateValues',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/animation/physics/SpringStepForce;->init()V', 'iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D', 'invoke-virtual {p0}, Lmiuix/animation/physics/SpringForce;->getStiffness()F', 'iget-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D', 'iget-object p0, p0, Lmiuix/animation/physics/SpringForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;', 'iput p1, p0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F', 'iput p1, p0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;
    .registers 13

    invoke-virtual {p0}, Lmiuix/animation/physics/SpringStepForce;->init()V

    long-to-double p5, p5

    const-wide v0, 0x41cdcd6500000000L

    div-double/2addr p5, v0

    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    mul-double/2addr v0, p5

    const-wide/high16 v2, 0x3ff0000000000000L

    sub-double/2addr v2, v0

    mul-double/2addr v2, p3

    invoke-virtual {p0}, Lmiuix/animation/physics/SpringForce;->getStiffness()F

    move-result v0

    float-to-double v0, v0

    iget-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D

    sub-double/2addr v4, p1

    mul-double/2addr v0, v4

    mul-double/2addr v0, p5

    add-double/2addr v2, v0

    add-double/2addr p3, v2

    const-wide/high16 v0, 0x3fe0000000000000L

    mul-double/2addr p3, v0

    mul-double/2addr p3, p5

    add-double/2addr p1, p3

    iget-object p0, p0, Lmiuix/animation/physics/SpringForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    double-to-float p1, p1

    iput p1, p0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    double-to-float p1, v2

    iput p1, p0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    return-object p0
.end method""",
        'replacement': """.method updateValues(DDJ)Lmiuix/animation/physics/DynamicAnimation$MassState;
    .registers 13

    goto :goto_f

    nop

    :goto_0
    mul-double/2addr v2, p3

    goto :goto_8

    nop

    :goto_1
    add-double/2addr v2, v0

    goto :goto_4

    nop

    :goto_2
    float-to-double v0, v0

    goto :goto_15

    nop

    :goto_3
    div-double/2addr p5, v0

    goto :goto_12

    nop

    :goto_4
    add-double/2addr p3, v2

    goto :goto_18

    nop

    :goto_5
    long-to-double p5, p5

    goto :goto_c

    nop

    :goto_6
    iput p1, p0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    goto :goto_7

    nop

    :goto_7
    double-to-float p1, v2

    goto :goto_b

    nop

    :goto_8
    invoke-virtual {p0}, Lmiuix/animation/physics/SpringForce;->getStiffness()F

    move-result v0

    goto :goto_2

    nop

    :goto_9
    iget-object p0, p0, Lmiuix/animation/physics/SpringForce;->mMassState:Lmiuix/animation/physics/DynamicAnimation$MassState;

    goto :goto_16

    nop

    :goto_a
    mul-double/2addr p3, p5

    goto :goto_19

    nop

    :goto_b
    iput p1, p0, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_14

    nop

    :goto_c
    const-wide v0, 0x41cdcd6500000000L

    goto :goto_3

    nop

    :goto_d
    sub-double/2addr v2, v0

    goto :goto_0

    nop

    :goto_e
    mul-double/2addr v0, p5

    goto :goto_11

    nop

    :goto_f
    invoke-virtual {p0}, Lmiuix/animation/physics/SpringStepForce;->init()V

    goto :goto_5

    nop

    :goto_10
    mul-double/2addr p3, v0

    goto :goto_a

    nop

    :goto_11
    const-wide/high16 v2, 0x3ff0000000000000L

    goto :goto_d

    nop

    :goto_12
    iget-wide v0, p0, Lmiuix/animation/physics/SpringForce;->mDampedFreq:D

    goto :goto_e

    nop

    :goto_13
    mul-double/2addr v0, v4

    goto :goto_17

    nop

    :goto_14
    return-object p0

    :goto_15
    iget-wide v4, p0, Lmiuix/animation/physics/SpringForce;->mFinalPosition:D

    goto :goto_1a

    nop

    :goto_16
    double-to-float p1, p1

    goto :goto_6

    nop

    :goto_17
    mul-double/2addr v0, p5

    goto :goto_1

    nop

    :goto_18
    const-wide/high16 v0, 0x3fe0000000000000L

    goto :goto_10

    nop

    :goto_19
    add-double/2addr p1, p3

    goto :goto_9

    nop

    :goto_1a
    sub-double/2addr v4, p1

    goto :goto_13

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
