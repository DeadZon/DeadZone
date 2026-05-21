TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/FlingAnimation.smali'
CLASS_FALLBACK_NAMES = ['FlingAnimation.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/physics/DynamicAnimation;']

PATCHES = [
    {
        'id': 'miuix_animation_physics_FlingAnimation__getAcceleration',
        'method': '.method getAcceleration(FF)F',
        'method_name': 'getAcceleration',
        'method_anchors': ['iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;', 'invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/FlingAnimation$DragForce;->getAcceleration(FF)F', 'return p0'],
        'type': 'method_replace',
        'search': """.method getAcceleration(FF)F
    .registers 3

    iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;

    invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/FlingAnimation$DragForce;->getAcceleration(FF)F

    move-result p0

    return p0
.end method""",
        'replacement': """.method getAcceleration(FF)F
    .registers 3

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/FlingAnimation$DragForce;->getAcceleration(FF)F

    move-result p0

    goto :goto_2

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;

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
        'id': 'miuix_animation_physics_FlingAnimation__isAtEquilibrium',
        'method': '.method isAtEquilibrium(FF)Z',
        'method_name': 'isAtEquilibrium',
        'method_anchors': ['iget v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMaxValue:F', 'if-gez v0, :cond_1', 'iget v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMinValue:F', 'if-lez v0, :cond_1', 'iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;', 'invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z', 'if-eqz p0, :cond_0', 'return p0'],
        'type': 'method_replace',
        'search': """.method isAtEquilibrium(FF)Z
    .registers 4

    iget v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMaxValue:F

    cmpl-float v0, p1, v0

    if-gez v0, :cond_1

    iget v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMinValue:F

    cmpg-float v0, p1, v0

    if-lez v0, :cond_1

    iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;

    invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z

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

    goto :goto_c

    nop

    :goto_0
    invoke-virtual {p0, p1, p2}, Lmiuix/animation/physics/FlingAnimation$DragForce;->isAtEquilibrium(FF)Z

    move-result p0

    goto :goto_1

    nop

    :goto_1
    if-nez p0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_d

    nop

    :goto_2
    cmpg-float v0, p1, v0

    goto :goto_5

    nop

    :goto_3
    return p0

    :goto_4
    cmpl-float v0, p1, v0

    goto :goto_8

    nop

    :goto_5
    if-gtz v0, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_6

    nop

    :goto_6
    iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;

    goto :goto_0

    nop

    :goto_7
    iget v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMinValue:F

    goto :goto_2

    nop

    :goto_8
    if-ltz v0, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_7

    nop

    :goto_9
    return p0

    :goto_a
    goto :goto_b

    nop

    :goto_b
    const/4 p0, 0x1

    goto :goto_3

    nop

    :goto_c
    iget v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMaxValue:F

    goto :goto_4

    nop

    :goto_d
    goto :goto_a

    :goto_e
    goto :goto_f

    nop

    :goto_f
    const/4 p0, 0x0

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_FlingAnimation__setValueThreshold',
        'method': '.method setValueThreshold(F)V',
        'method_name': 'setValueThreshold',
        'method_anchors': ['iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;', 'invoke-virtual {p0, p1}, Lmiuix/animation/physics/FlingAnimation$DragForce;->setValueThreshold(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method setValueThreshold(F)V
    .registers 2

    iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;

    invoke-virtual {p0, p1}, Lmiuix/animation/physics/FlingAnimation$DragForce;->setValueThreshold(F)V

    return-void
.end method""",
        'replacement': """.method setValueThreshold(F)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/animation/physics/FlingAnimation$DragForce;->setValueThreshold(F)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_FlingAnimation__updateValueAndVelocity',
        'method': '.method updateValueAndVelocity(J)Z',
        'method_name': 'updateValueAndVelocity',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;', 'iget v1, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F', 'iget v2, p0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F', 'invoke-virtual {v0, v1, v2, p1, p2}, Lmiuix/animation/physics/FlingAnimation$DragForce;->updateValueAndVelocity(FFJ)Lmiuix/animation/physics/DynamicAnimation$MassState;', 'iget p2, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F', 'iput p2, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F', 'iget p1, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F', 'iput p1, p0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F'],
        'type': 'method_replace',
        'search': """.method updateValueAndVelocity(J)Z
    .registers 6

    iget-object v0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;

    iget v1, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    iget v2, p0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    invoke-virtual {v0, v1, v2, p1, p2}, Lmiuix/animation/physics/FlingAnimation$DragForce;->updateValueAndVelocity(FFJ)Lmiuix/animation/physics/DynamicAnimation$MassState;

    move-result-object p1

    iget p2, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    iput p2, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    iget p1, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    iput p1, p0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    iget v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMinValue:F

    cmpg-float v1, p2, v0

    const/4 v2, 0x1

    if-gez v1, :cond_0

    iput v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    return v2

    :cond_0
    iget v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMaxValue:F

    cmpl-float v1, p2, v0

    if-lez v1, :cond_1

    iput v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    return v2

    :cond_1
    invoke-virtual {p0, p2, p1}, Lmiuix/animation/physics/FlingAnimation;->isAtEquilibrium(FF)Z

    move-result p0

    if-eqz p0, :cond_2

    return v2

    :cond_2
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method updateValueAndVelocity(J)Z
    .registers 6

    goto :goto_7

    nop

    :goto_0
    return v2

    :goto_1
    goto :goto_5

    nop

    :goto_2
    cmpl-float v1, p2, v0

    goto :goto_11

    nop

    :goto_3
    iget p2, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mValue:F

    goto :goto_14

    nop

    :goto_4
    iget v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMinValue:F

    goto :goto_9

    nop

    :goto_5
    iget v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMaxValue:F

    goto :goto_2

    nop

    :goto_6
    iput v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_0

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/animation/physics/FlingAnimation;->mFlingForce:Lmiuix/animation/physics/FlingAnimation$DragForce;

    goto :goto_18

    nop

    :goto_8
    return p0

    :goto_9
    cmpg-float v1, p2, v0

    goto :goto_a

    nop

    :goto_a
    const/4 v2, 0x1

    goto :goto_19

    nop

    :goto_b
    iput v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_16

    nop

    :goto_c
    return v2

    :goto_d
    goto :goto_13

    nop

    :goto_e
    iget v2, p0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    goto :goto_10

    nop

    :goto_f
    if-nez p0, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_c

    nop

    :goto_10
    invoke-virtual {v0, v1, v2, p1, p2}, Lmiuix/animation/physics/FlingAnimation$DragForce;->updateValueAndVelocity(FFJ)Lmiuix/animation/physics/DynamicAnimation$MassState;

    move-result-object p1

    goto :goto_3

    nop

    :goto_11
    if-gtz v1, :cond_1

    goto :goto_17

    :cond_1
    goto :goto_b

    nop

    :goto_12
    iget p1, p1, Lmiuix/animation/physics/DynamicAnimation$MassState;->mVelocity:F

    goto :goto_1a

    nop

    :goto_13
    const/4 p0, 0x0

    goto :goto_8

    nop

    :goto_14
    iput p2, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_12

    nop

    :goto_15
    invoke-virtual {p0, p2, p1}, Lmiuix/animation/physics/FlingAnimation;->isAtEquilibrium(FF)Z

    move-result p0

    goto :goto_f

    nop

    :goto_16
    return v2

    :goto_17
    goto :goto_15

    nop

    :goto_18
    iget v1, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_e

    nop

    :goto_19
    if-ltz v1, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_6

    nop

    :goto_1a
    iput p1, p0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
