TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce.smali'
CLASS_FALLBACK_NAMES = ['FlingAnimation$DragForce.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_FlingAnimation__DragForce__setFrictionScalar',
        'method': '.method setFrictionScalar(F)V',
        'method_name': 'setFrictionScalar',
        'method_anchors': ['iput p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mFriction:F', 'invoke-static {v0, v1, v2, v3}, Ljava/lang/Math;->pow(DD)D', 'iput-wide v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mDragRate:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method setFrictionScalar(F)V
    .registers 6

    const v0, -0x3f79999a

    mul-float/2addr p1, v0

    iput p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mFriction:F

    const-wide v0, 0x4005bf0a8b145769L

    float-to-double v2, p1

    invoke-static {v0, v1, v2, v3}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v0

    const-wide/high16 v2, 0x3ff0000000000000L

    sub-double/2addr v2, v0

    iput-wide v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mDragRate:D

    return-void
.end method""",
        'replacement': """.method setFrictionScalar(F)V
    .registers 6

    goto :goto_1

    nop

    :goto_0
    iput p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mFriction:F

    goto :goto_3

    nop

    :goto_1
    const v0, -0x3f79999a

    goto :goto_8

    nop

    :goto_2
    iput-wide v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mDragRate:D

    goto :goto_5

    nop

    :goto_3
    const-wide v0, 0x4005bf0a8b145769L

    goto :goto_9

    nop

    :goto_4
    invoke-static {v0, v1, v2, v3}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v0

    goto :goto_7

    nop

    :goto_5
    return-void

    :goto_6
    sub-double/2addr v2, v0

    goto :goto_2

    nop

    :goto_7
    const-wide/high16 v2, 0x3ff0000000000000L

    goto :goto_6

    nop

    :goto_8
    mul-float/2addr p1, v0

    goto :goto_0

    nop

    :goto_9
    float-to-double v2, p1

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_FlingAnimation__DragForce__setValueThreshold',
        'method': '.method setValueThreshold(F)V',
        'method_name': 'setValueThreshold',
        'method_anchors': ['iput p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mVelocityThreshold:F', 'return-void'],
        'type': 'method_replace',
        'search': """.method setValueThreshold(F)V
    .registers 3

    const/high16 v0, 0x427a0000

    mul-float/2addr p1, v0

    iput p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mVelocityThreshold:F

    return-void
.end method""",
        'replacement': """.method setValueThreshold(F)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    mul-float/2addr p1, v0

    goto :goto_2

    nop

    :goto_2
    iput p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mVelocityThreshold:F

    goto :goto_0

    nop

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
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_FlingAnimation__DragForce__updateValueAndVelocity',
        'method': '.method updateValueAndVelocity(FFJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;',
        'method_name': 'updateValueAndVelocity',
        'method_anchors': ['iget-wide v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mDragRate:D', 'invoke-static {v0, v1, p3, p4}, Ljava/lang/Math;->pow(DD)D', 'iget-object v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mMassState:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;', 'iput p2, v2, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F', 'iput p1, v2, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F', 'invoke-virtual {p0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z', 'if-eqz p1, :cond_0', 'iget-object p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mMassState:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;'],
        'type': 'method_replace',
        'search': """.method updateValueAndVelocity(FFJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;
    .registers 10

    const-wide/high16 v0, 0x3ff0000000000000L

    iget-wide v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mDragRate:D

    sub-double/2addr v0, v2

    long-to-double p3, p3

    const-wide v2, 0x41cdcd6500000000L

    div-double/2addr p3, v2

    invoke-static {v0, v1, p3, p4}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v0

    iget-object v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mMassState:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    float-to-double v3, p2

    mul-double/2addr v3, v0

    double-to-float p2, v3

    iput p2, v2, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    float-to-double v0, p1

    float-to-double v3, p2

    mul-double/2addr v3, p3

    add-double/2addr v0, v3

    double-to-float p1, v0

    iput p1, v2, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    invoke-virtual {p0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mMassState:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    const/4 p2, 0x0

    iput p2, p1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    :cond_0
    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mMassState:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    return-object p0
.end method""",
        'replacement': """.method updateValueAndVelocity(FFJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;
    .registers 10

    goto :goto_7

    nop

    :goto_0
    iput p2, p1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    :goto_1
    goto :goto_2

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mMassState:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    goto :goto_12

    nop

    :goto_3
    div-double/2addr p3, v2

    goto :goto_f

    nop

    :goto_4
    float-to-double v3, p2

    goto :goto_19

    nop

    :goto_5
    mul-double/2addr v3, v0

    goto :goto_6

    nop

    :goto_6
    double-to-float p2, v3

    goto :goto_8

    nop

    :goto_7
    const-wide/high16 v0, 0x3ff0000000000000L

    goto :goto_11

    nop

    :goto_8
    iput p2, v2, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_13

    nop

    :goto_9
    long-to-double p3, p3

    goto :goto_e

    nop

    :goto_a
    iget-object p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mMassState:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    goto :goto_10

    nop

    :goto_b
    sub-double/2addr v0, v2

    goto :goto_9

    nop

    :goto_c
    iput p1, v2, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    goto :goto_16

    nop

    :goto_d
    float-to-double v3, p2

    goto :goto_5

    nop

    :goto_e
    const-wide v2, 0x41cdcd6500000000L

    goto :goto_3

    nop

    :goto_f
    invoke-static {v0, v1, p3, p4}, Ljava/lang/Math;->pow(DD)D

    move-result-wide v0

    goto :goto_17

    nop

    :goto_10
    const/4 p2, 0x0

    goto :goto_0

    nop

    :goto_11
    iget-wide v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mDragRate:D

    goto :goto_b

    nop

    :goto_12
    return-object p0

    :goto_13
    float-to-double v0, p1

    goto :goto_4

    nop

    :goto_14
    if-nez p1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_a

    nop

    :goto_15
    add-double/2addr v0, v3

    goto :goto_18

    nop

    :goto_16
    invoke-virtual {p0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z

    move-result p1

    goto :goto_14

    nop

    :goto_17
    iget-object v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->mMassState:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    goto :goto_d

    nop

    :goto_18
    double-to-float p1, v0

    goto :goto_c

    nop

    :goto_19
    mul-double/2addr v3, p3

    goto :goto_15

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
