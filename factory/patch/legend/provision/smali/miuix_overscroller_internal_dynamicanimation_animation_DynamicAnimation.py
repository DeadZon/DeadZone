TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation.smali'
CLASS_FALLBACK_NAMES = ['DynamicAnimation.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallback;', '.field public static final ALPHA:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$ViewProperty;', '.field public static final ROTATION:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$ViewProperty;', '.field public static final ROTATION_X:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$ViewProperty;', '.field public static final ROTATION_Y:Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$ViewProperty;']

PATCHES = [
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_DynamicAnimation__getValueThreshold',
        'method': '.method getValueThreshold()F',
        'method_name': 'getValueThreshold',
        'method_anchors': ['iget p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMinVisibleChange:F', 'return p0'],
        'type': 'method_replace',
        'search': """.method getValueThreshold()F
    .registers 2

    iget p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMinVisibleChange:F

    const/high16 v0, 0x3f400000

    mul-float/2addr p0, v0

    return p0
.end method""",
        'replacement': """.method getValueThreshold()F
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mMinVisibleChange:F

    goto :goto_3

    nop

    :goto_2
    mul-float/2addr p0, v0

    goto :goto_0

    nop

    :goto_3
    const/high16 v0, 0x3f400000

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_DynamicAnimation__setPropertyValue',
        'method': '.method setPropertyValue(F)V',
        'method_name': 'setPropertyValue',
        'method_anchors': ['iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mProperty:Lmiuix/overscroller/internal/dynamicanimation/animation/FloatPropertyCompat;', 'iget-object v1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mTarget:Ljava/lang/Object;', 'invoke-virtual {v0, v1, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/FloatPropertyCompat;->setValue(Ljava/lang/Object;F)V', 'iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;', 'invoke-virtual {v0}, Ljava/util/ArrayList;->size()I', 'if-ge p1, v0, :cond_1', 'iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;', 'invoke-virtual {v0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;'],
        'type': 'method_replace',
        'search': """.method setPropertyValue(F)V
    .registers 5

    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mProperty:Lmiuix/overscroller/internal/dynamicanimation/animation/FloatPropertyCompat;

    iget-object v1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mTarget:Ljava/lang/Object;

    invoke-virtual {v0, v1, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/FloatPropertyCompat;->setValue(Ljava/lang/Object;F)V

    const/4 p1, 0x0

    :goto_0
    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-ge p1, v0, :cond_1

    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;

    iget v1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    iget v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    invoke-interface {v0, p0, v1, v2}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;->onAnimationUpdate(Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;FF)V

    :cond_0
    add-int/lit8 p1, p1, 0x1

    goto :goto_0

    :cond_1
    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    invoke-static {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->removeNullEntries(Ljava/util/ArrayList;)V

    return-void
.end method""",
        'replacement': """.method setPropertyValue(F)V
    .registers 5

    goto :goto_f

    nop

    :goto_0
    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_3

    nop

    :goto_1
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    goto :goto_a

    nop

    :goto_2
    iget-object v1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mTarget:Ljava/lang/Object;

    goto :goto_b

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_e

    nop

    :goto_4
    check-cast v0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;

    goto :goto_12

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    goto :goto_1

    nop

    :goto_6
    iget v2, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mVelocity:F

    goto :goto_c

    nop

    :goto_7
    invoke-static {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->removeNullEntries(Ljava/util/ArrayList;)V

    goto :goto_15

    nop

    :goto_8
    const/4 p1, 0x0

    :goto_9
    goto :goto_5

    nop

    :goto_a
    if-lt p1, v0, :cond_1

    goto :goto_17

    :cond_1
    goto :goto_13

    nop

    :goto_b
    invoke-virtual {v0, v1, p1}, Lmiuix/overscroller/internal/dynamicanimation/animation/FloatPropertyCompat;->setValue(Ljava/lang/Object;F)V

    goto :goto_8

    nop

    :goto_c
    invoke-interface {v0, p0, v1, v2}, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation$OnAnimationUpdateListener;->onAnimationUpdate(Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;FF)V

    :goto_d
    goto :goto_11

    nop

    :goto_e
    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    goto :goto_14

    nop

    :goto_f
    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mProperty:Lmiuix/overscroller/internal/dynamicanimation/animation/FloatPropertyCompat;

    goto :goto_2

    nop

    :goto_10
    iget-object p0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    goto :goto_7

    nop

    :goto_11
    add-int/lit8 p1, p1, 0x1

    goto :goto_16

    nop

    :goto_12
    iget v1, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mValue:F

    goto :goto_6

    nop

    :goto_13
    iget-object v0, p0, Lmiuix/overscroller/internal/dynamicanimation/animation/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    goto :goto_0

    nop

    :goto_14
    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_4

    nop

    :goto_15
    return-void

    :goto_16
    goto :goto_9

    :goto_17
    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
