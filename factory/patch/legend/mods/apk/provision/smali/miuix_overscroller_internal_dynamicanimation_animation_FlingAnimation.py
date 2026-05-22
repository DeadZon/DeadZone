TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/overscroller/internal/dynamicanimation/animation/FlingAnimation.smali'
CLASS_FALLBACK_NAMES = ['FlingAnimation.smali']
CLASS_ANCHORS = ['.super Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;']

PATCHES = [
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_FlingAnimation__isAtEquilibrium',
        'method': '.method isAtEquilibrium(FF)Z',
        'method_name': 'isAtEquilibrium',
        'method_anchors': ['iget v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMaxValue:F', 'if-gez v0, :cond_1', 'iget v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMinValue:F', 'if-lez v0, :cond_1', 'iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFlingForce:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;', 'invoke-virtual {p0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z', 'if-eqz p0, :cond_0', 'return p0'],
        'type': 'method_replace',
        'search': """.method isAtEquilibrium(FF)Z
    .registers 4

    iget v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMaxValue:F

    cmpl-float v0, p1, v0

    if-gez v0, :cond_1

    iget v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMinValue:F

    cmpg-float v0, p1, v0

    if-lez v0, :cond_1

    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFlingForce:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;

    invoke-virtual {p0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z

    move-result p0

    if-eqz p0, :cond_0

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method isAtEquilibrium(FF)Z
    .registers 4

    goto :goto_d

    nop

    :goto_0
    if-ltz v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_9

    nop

    :goto_1
    cmpg-float v0, p1, v0

    goto :goto_3

    nop

    :goto_2
    cmpl-float v0, p1, v0

    goto :goto_0

    nop

    :goto_3
    if-gtz v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_b

    nop

    :goto_4
    return p0

    :goto_5
    goto :goto_f

    nop

    :goto_6
    goto :goto_5

    :goto_7
    goto :goto_c

    nop

    :goto_8
    invoke-virtual {p0, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z

    move-result p0

    goto :goto_a

    nop

    :goto_9
    iget v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMinValue:F

    goto :goto_1

    nop

    :goto_a
    if-nez p0, :cond_2

    goto :goto_7

    :cond_2
    goto :goto_6

    nop

    :goto_b
    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFlingForce:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;

    goto :goto_8

    nop

    :goto_c
    const/4 p0, 0x0

    goto :goto_4

    nop

    :goto_d
    iget v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMaxValue:F

    goto :goto_2

    nop

    :goto_e
    return p0

    :goto_f
    const/4 p0, 0x1

    goto :goto_e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_FlingAnimation__setValueThreshold',
        'method': '.method setValueThreshold(F)V',
        'method_name': 'setValueThreshold',
        'method_anchors': ['iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFlingForce:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;', 'invoke-virtual {p0, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->setValueThreshold(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method setValueThreshold(F)V
    .registers 2

    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFlingForce:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;

    invoke-virtual {p0, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->setValueThreshold(F)V

    return-void
.end method""",
        'replacement': """.method setValueThreshold(F)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFlingForce:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->setValueThreshold(F)V

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_FlingAnimation__updateValueAndVelocity',
        'method': '.method updateValueAndVelocity(J)Z',
        'method_name': 'updateValueAndVelocity',
        'method_anchors': ['iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFlingForce:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;', 'iget v1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F', 'iget v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F', 'invoke-virtual {v0, v1, v2, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->updateValueAndVelocity(FFJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;', 'iget p2, p1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F', 'iput p2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F', 'iget p1, p1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F', 'iput p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F'],
        'type': 'method_replace',
        'search': """.method updateValueAndVelocity(J)Z
    .registers 6

    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFlingForce:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;

    iget v1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    iget v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    invoke-virtual {v0, v1, v2, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->updateValueAndVelocity(FFJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    move-result-object p1

    iget p2, p1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    iput p2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    iget p1, p1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    iput p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    iget v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMinValue:F

    cmpg-float v1, p2, v0

    const/4 v2, 0x1

    if-gez v1, :cond_0

    iput v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    return v2

    :cond_0
    iget v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMaxValue:F

    cmpl-float v1, p2, v0

    if-lez v1, :cond_1

    iput v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    return v2

    :cond_1
    invoke-virtual {p0, p2, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->isAtEquilibrium(FF)Z

    move-result p1

    if-eqz p1, :cond_2

    iget-object p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFinalValueListener:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$FinalValueListener;

    iget p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    float-to-int p0, p0

    invoke-interface {p1, p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$FinalValueListener;->onFinalValueArrived(I)V

    return v2

    :cond_2
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method updateValueAndVelocity(J)Z
    .registers 6

    goto :goto_5

    nop

    :goto_0
    iget v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMinValue:F

    goto :goto_16

    nop

    :goto_1
    return v2

    :goto_2
    goto :goto_13

    nop

    :goto_3
    if-gtz v1, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_4

    nop

    :goto_4
    iput v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_c

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFlingForce:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;

    goto :goto_f

    nop

    :goto_6
    iget p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_8

    nop

    :goto_7
    return p0

    :goto_8
    float-to-int p0, p0

    goto :goto_b

    nop

    :goto_9
    return v2

    :goto_a
    goto :goto_14

    nop

    :goto_b
    invoke-interface {p1, p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$FinalValueListener;->onFinalValueArrived(I)V

    goto :goto_9

    nop

    :goto_c
    return v2

    :goto_d
    goto :goto_12

    nop

    :goto_e
    iput p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    goto :goto_0

    nop

    :goto_f
    iget v1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_1e

    nop

    :goto_10
    iget p1, p1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_e

    nop

    :goto_11
    const/4 v2, 0x1

    goto :goto_1d

    nop

    :goto_12
    invoke-virtual {p0, p2, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->isAtEquilibrium(FF)Z

    move-result p1

    goto :goto_1a

    nop

    :goto_13
    iget v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMaxValue:F

    goto :goto_19

    nop

    :goto_14
    const/4 p0, 0x0

    goto :goto_7

    nop

    :goto_15
    iput p2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_10

    nop

    :goto_16
    cmpg-float v1, p2, v0

    goto :goto_11

    nop

    :goto_17
    iget p2, p1, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;->mValue:F

    goto :goto_15

    nop

    :goto_18
    iput v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_1

    nop

    :goto_19
    cmpl-float v1, p2, v0

    goto :goto_3

    nop

    :goto_1a
    if-nez p1, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_1b

    nop

    :goto_1b
    iget-object p1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation;->mFinalValueListener:Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$FinalValueListener;

    goto :goto_6

    nop

    :goto_1c
    invoke-virtual {v0, v1, v2, p1, p2}, Lmiuix/overscroller/internal/dynamicanimation/animation/FlingAnimation$DragForce;->updateValueAndVelocity(FFJ)Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$MassState;

    move-result-object p1

    goto :goto_17

    nop

    :goto_1d
    if-ltz v1, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_18

    nop

    :goto_1e
    iget v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    goto :goto_1c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
