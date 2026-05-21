TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation.smali'
CLASS_FALLBACK_NAMES = ['BaseKeyframeAnimation.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_keyframe_BaseKeyframeAnimation__getEndProgress',
        'method': '.method getEndProgress()F',
        'method_name': 'getEndProgress',
        'method_anchors': ['iget v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->cachedEndProgress:F', 'if-nez v0, :cond_0', 'iget-object v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->keyframesWrapper:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;', 'invoke-interface {v0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;->getEndProgress()F', 'iput v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->cachedEndProgress:F', 'iget p0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->cachedEndProgress:F', 'return p0'],
        'type': 'method_replace',
        'search': """.method getEndProgress()F
    .registers 3

    iget v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->cachedEndProgress:F

    const/high16 v1, -0x40800000

    cmpl-float v0, v0, v1

    if-nez v0, :cond_0

    iget-object v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->keyframesWrapper:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;

    invoke-interface {v0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;->getEndProgress()F

    move-result v0

    iput v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->cachedEndProgress:F

    :cond_0
    iget p0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->cachedEndProgress:F

    return p0
.end method""",
        'replacement': """.method getEndProgress()F
    .registers 3

    goto :goto_8

    nop

    :goto_0
    iget-object v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->keyframesWrapper:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;

    goto :goto_2

    nop

    :goto_1
    iget p0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->cachedEndProgress:F

    goto :goto_6

    nop

    :goto_2
    invoke-interface {v0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;->getEndProgress()F

    move-result v0

    goto :goto_4

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_0

    nop

    :goto_4
    iput v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->cachedEndProgress:F

    :goto_5
    goto :goto_1

    nop

    :goto_6
    return p0

    :goto_7
    const/high16 v1, -0x40800000

    goto :goto_9

    nop

    :goto_8
    iget v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->cachedEndProgress:F

    goto :goto_7

    nop

    :goto_9
    cmpl-float v0, v0, v1

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_keyframe_BaseKeyframeAnimation__getLinearCurrentKeyframeProgress',
        'method': '.method getLinearCurrentKeyframeProgress()F',
        'method_name': 'getLinearCurrentKeyframeProgress',
        'method_anchors': ['iget-boolean v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->isDiscrete:Z', 'if-eqz v0, :cond_0', 'return v1', 'invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;', 'invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->isStatic()Z', 'if-eqz v2, :cond_1', 'return v1', 'iget p0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->progress:F'],
        'type': 'method_replace',
        'search': """.method getLinearCurrentKeyframeProgress()F
    .registers 4

    iget-boolean v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->isDiscrete:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    return v1

    :cond_0
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;

    move-result-object v0

    invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->isStatic()Z

    move-result v2

    if-eqz v2, :cond_1

    return v1

    :cond_1
    iget p0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->progress:F

    invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->getStartProgress()F

    move-result v1

    sub-float/2addr p0, v1

    invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->getEndProgress()F

    move-result v1

    invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->getStartProgress()F

    move-result v0

    sub-float/2addr v1, v0

    div-float/2addr p0, v1

    return p0
.end method""",
        'replacement': """.method getLinearCurrentKeyframeProgress()F
    .registers 4

    goto :goto_1

    nop

    :goto_0
    if-nez v2, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_2

    nop

    :goto_1
    iget-boolean v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->isDiscrete:Z

    goto :goto_8

    nop

    :goto_2
    return v1

    :goto_3
    goto :goto_a

    nop

    :goto_4
    return v1

    :goto_5
    goto :goto_9

    nop

    :goto_6
    sub-float/2addr p0, v1

    goto :goto_b

    nop

    :goto_7
    invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->isStatic()Z

    move-result v2

    goto :goto_0

    nop

    :goto_8
    const/4 v1, 0x0

    goto :goto_f

    nop

    :goto_9
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;

    move-result-object v0

    goto :goto_7

    nop

    :goto_a
    iget p0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->progress:F

    goto :goto_10

    nop

    :goto_b
    invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->getEndProgress()F

    move-result v1

    goto :goto_e

    nop

    :goto_c
    return p0

    :goto_d
    div-float/2addr p0, v1

    goto :goto_c

    nop

    :goto_e
    invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->getStartProgress()F

    move-result v0

    goto :goto_11

    nop

    :goto_f
    if-nez v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_4

    nop

    :goto_10
    invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->getStartProgress()F

    move-result v1

    goto :goto_6

    nop

    :goto_11
    sub-float/2addr v1, v0

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_keyframe_BaseKeyframeAnimation__getCurrentKeyframe',
        'method': '.method protected getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;',
        'method_name': 'getCurrentKeyframe',
        'method_anchors': ['const-string v0, "BaseKeyframeAnimation#getCurrentKeyframe"', 'invoke-static {v0}, Lcom/airbnb/lottie/L;->beginSection(Ljava/lang/String;)V', 'iget-object p0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->keyframesWrapper:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;', 'invoke-interface {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;', 'invoke-static {v0}, Lcom/airbnb/lottie/L;->endSection(Ljava/lang/String;)F', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;
    .registers 2

    const-string v0, "BaseKeyframeAnimation#getCurrentKeyframe"

    invoke-static {v0}, Lcom/airbnb/lottie/L;->beginSection(Ljava/lang/String;)V

    iget-object p0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->keyframesWrapper:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;

    invoke-interface {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;

    move-result-object p0

    invoke-static {v0}, Lcom/airbnb/lottie/L;->endSection(Ljava/lang/String;)F

    return-object p0
.end method""",
        'replacement': """.method protected getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;
    .registers 2

    goto :goto_5

    nop

    :goto_0
    invoke-interface {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;

    move-result-object p0

    goto :goto_3

    nop

    :goto_1
    iget-object p0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->keyframesWrapper:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$KeyframesWrapper;

    goto :goto_0

    nop

    :goto_2
    return-object p0

    :goto_3
    invoke-static {v0}, Lcom/airbnb/lottie/L;->endSection(Ljava/lang/String;)F

    goto :goto_2

    nop

    :goto_4
    invoke-static {v0}, Lcom/airbnb/lottie/L;->beginSection(Ljava/lang/String;)V

    goto :goto_1

    nop

    :goto_5
    const-string v0, "BaseKeyframeAnimation#getCurrentKeyframe"

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_keyframe_BaseKeyframeAnimation__getInterpolatedCurrentKeyframeProgress',
        'method': '.method protected getInterpolatedCurrentKeyframeProgress()F',
        'method_name': 'getInterpolatedCurrentKeyframeProgress',
        'method_anchors': ['invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->isStatic()Z', 'if-eqz v1, :cond_0', 'iget-object v0, v0, Lcom/airbnb/lottie/value/Keyframe;->interpolator:Landroid/view/animation/Interpolator;', 'invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getLinearCurrentKeyframeProgress()F', 'invoke-interface {v0, p0}, Landroid/view/animation/Interpolator;->getInterpolation(F)F', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getInterpolatedCurrentKeyframeProgress()F
    .registers 3

    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;

    move-result-object v0

    if-eqz v0, :cond_1

    invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->isStatic()Z

    move-result v1

    if-eqz v1, :cond_0

    goto :goto_0

    :cond_0
    iget-object v0, v0, Lcom/airbnb/lottie/value/Keyframe;->interpolator:Landroid/view/animation/Interpolator;

    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getLinearCurrentKeyframeProgress()F

    move-result p0

    invoke-interface {v0, p0}, Landroid/view/animation/Interpolator;->getInterpolation(F)F

    move-result p0

    return p0

    :cond_1
    :goto_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected getInterpolatedCurrentKeyframeProgress()F
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return p0

    :goto_1
    goto :goto_6

    nop

    :goto_2
    invoke-virtual {v0}, Lcom/airbnb/lottie/value/Keyframe;->isStatic()Z

    move-result v1

    goto :goto_8

    nop

    :goto_3
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;

    move-result-object v0

    goto :goto_9

    nop

    :goto_4
    iget-object v0, v0, Lcom/airbnb/lottie/value/Keyframe;->interpolator:Landroid/view/animation/Interpolator;

    goto :goto_5

    nop

    :goto_5
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getLinearCurrentKeyframeProgress()F

    move-result p0

    goto :goto_7

    nop

    :goto_6
    const/4 p0, 0x0

    goto :goto_c

    nop

    :goto_7
    invoke-interface {v0, p0}, Landroid/view/animation/Interpolator;->getInterpolation(F)F

    move-result p0

    goto :goto_0

    nop

    :goto_8
    if-nez v1, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_a

    nop

    :goto_9
    if-nez v0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_2

    nop

    :goto_a
    goto :goto_1

    :goto_b
    goto :goto_4

    nop

    :goto_c
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_keyframe_BaseKeyframeAnimation__getValue',
        'method': '.method protected getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Ljava/lang/Object;',
        'method_name': 'getValue',
        'method_anchors': ['new-instance p0, Ljava/lang/UnsupportedOperationException;', 'const-string p1, "This animation does not support split dimensions!"', 'invoke-direct {p0, p1}, Ljava/lang/UnsupportedOperationException;-><init>(Ljava/lang/String;)V'],
        'type': 'method_replace',
        'search': """.method protected getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Ljava/lang/Object;
    .registers 5

    new-instance p0, Ljava/lang/UnsupportedOperationException;

    const-string p1, "This animation does not support split dimensions!"

    invoke-direct {p0, p1}, Ljava/lang/UnsupportedOperationException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method protected getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Ljava/lang/Object;
    .registers 5

    goto :goto_0

    nop

    :goto_0
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_3

    nop

    :goto_1
    invoke-direct {p0, p1}, Ljava/lang/UnsupportedOperationException;-><init>(Ljava/lang/String;)V

    goto :goto_2

    nop

    :goto_2
    throw p0

    :goto_3
    const-string p1, "This animation does not support split dimensions!"

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
