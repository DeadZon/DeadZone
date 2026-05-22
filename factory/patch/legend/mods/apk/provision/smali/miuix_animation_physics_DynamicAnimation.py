TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/DynamicAnimation.smali'
CLASS_FALLBACK_NAMES = ['DynamicAnimation.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallback;', '.field public static final MIN_VISIBLE_CHANGE_ALPHA:F = 0.00390625f', '.field public static final MIN_VISIBLE_CHANGE_PIXELS:F = 1.0f', '.field public static final MIN_VISIBLE_CHANGE_ROTATION_DEGREES:F = 0.1f', '.field public static final MIN_VISIBLE_CHANGE_SCALE:F = 0.002f']

PATCHES = [
    {
        'id': 'miuix_animation_physics_DynamicAnimation__getValueThreshold',
        'method': '.method getValueThreshold()F',
        'method_name': 'getValueThreshold',
        'method_anchors': ['iget p0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMinVisibleChange:F', 'return p0'],
        'type': 'method_replace',
        'search': """.method getValueThreshold()F
    .registers 2

    iget p0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMinVisibleChange:F

    const/high16 v0, 0x3f400000

    mul-float/2addr p0, v0

    return p0
.end method""",
        'replacement': """.method getValueThreshold()F
    .registers 2

    goto :goto_1

    nop

    :goto_0
    const/high16 v0, 0x3f400000

    goto :goto_2

    nop

    :goto_1
    iget p0, p0, Lmiuix/animation/physics/DynamicAnimation;->mMinVisibleChange:F

    goto :goto_0

    nop

    :goto_2
    mul-float/2addr p0, v0

    goto :goto_3

    nop

    :goto_3
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_DynamicAnimation__setPropertyValue',
        'method': '.method setPropertyValue(F)V',
        'method_name': 'setPropertyValue',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mProperty:Lmiuix/animation/property/FloatProperty;', 'iget-object v1, p0, Lmiuix/animation/physics/DynamicAnimation;->mTarget:Ljava/lang/Object;', 'invoke-virtual {v0, v1, p1}, Lmiuix/animation/property/FloatProperty;->setValue(Ljava/lang/Object;F)V', 'iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;', 'invoke-virtual {v0}, Ljava/util/ArrayList;->size()I', 'if-ge p1, v0, :cond_1', 'iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;', 'invoke-virtual {v0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;'],
        'type': 'method_replace',
        'search': """.method setPropertyValue(F)V
    .registers 5

    iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mProperty:Lmiuix/animation/property/FloatProperty;

    iget-object v1, p0, Lmiuix/animation/physics/DynamicAnimation;->mTarget:Ljava/lang/Object;

    invoke-virtual {v0, v1, p1}, Lmiuix/animation/property/FloatProperty;->setValue(Ljava/lang/Object;F)V

    const/4 p1, 0x0

    :goto_0
    iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-ge p1, v0, :cond_1

    iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiuix/animation/physics/DynamicAnimation$OnAnimationUpdateListener;

    iget v1, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    iget v2, p0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    invoke-interface {v0, p0, v1, v2}, Lmiuix/animation/physics/DynamicAnimation$OnAnimationUpdateListener;->onAnimationUpdate(Lmiuix/animation/physics/DynamicAnimation;FF)V

    :cond_0
    add-int/lit8 p1, p1, 0x1

    goto :goto_0

    :cond_1
    iget-object p0, p0, Lmiuix/animation/physics/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    invoke-static {p0}, Lmiuix/animation/physics/DynamicAnimation;->removeNullEntries(Ljava/util/ArrayList;)V

    return-void
.end method""",
        'replacement': """.method setPropertyValue(F)V
    .registers 5

    goto :goto_12

    nop

    :goto_0
    invoke-virtual {v0, v1, p1}, Lmiuix/animation/property/FloatProperty;->setValue(Ljava/lang/Object;F)V

    goto :goto_c

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    goto :goto_f

    nop

    :goto_2
    iget v1, p0, Lmiuix/animation/physics/DynamicAnimation;->mValue:F

    goto :goto_e

    nop

    :goto_3
    return-void

    :goto_4
    goto :goto_d

    :goto_5
    goto :goto_9

    nop

    :goto_6
    if-lt p1, v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_14

    nop

    :goto_7
    invoke-interface {v0, p0, v1, v2}, Lmiuix/animation/physics/DynamicAnimation$OnAnimationUpdateListener;->onAnimationUpdate(Lmiuix/animation/physics/DynamicAnimation;FF)V

    :goto_8
    goto :goto_13

    nop

    :goto_9
    iget-object p0, p0, Lmiuix/animation/physics/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    goto :goto_16

    nop

    :goto_a
    iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    goto :goto_17

    nop

    :goto_b
    check-cast v0, Lmiuix/animation/physics/DynamicAnimation$OnAnimationUpdateListener;

    goto :goto_2

    nop

    :goto_c
    const/4 p1, 0x0

    :goto_d
    goto :goto_a

    nop

    :goto_e
    iget v2, p0, Lmiuix/animation/physics/DynamicAnimation;->mVelocity:F

    goto :goto_7

    nop

    :goto_f
    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_b

    nop

    :goto_10
    iget-object v1, p0, Lmiuix/animation/physics/DynamicAnimation;->mTarget:Ljava/lang/Object;

    goto :goto_0

    nop

    :goto_11
    if-nez v0, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_1

    nop

    :goto_12
    iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mProperty:Lmiuix/animation/property/FloatProperty;

    goto :goto_10

    nop

    :goto_13
    add-int/lit8 p1, p1, 0x1

    goto :goto_4

    nop

    :goto_14
    iget-object v0, p0, Lmiuix/animation/physics/DynamicAnimation;->mUpdateListeners:Ljava/util/ArrayList;

    goto :goto_15

    nop

    :goto_15
    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_11

    nop

    :goto_16
    invoke-static {p0}, Lmiuix/animation/physics/DynamicAnimation;->removeNullEntries(Ljava/util/ArrayList;)V

    goto :goto_3

    nop

    :goto_17
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
