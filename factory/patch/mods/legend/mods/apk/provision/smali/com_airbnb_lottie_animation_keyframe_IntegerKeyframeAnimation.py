TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/keyframe/IntegerKeyframeAnimation.smali'
CLASS_FALLBACK_NAMES = ['IntegerKeyframeAnimation.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/animation/keyframe/KeyframeAnimation;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_keyframe_IntegerKeyframeAnimation__getValue',
        'method': '.method bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;',
        'method_name': 'getValue',
        'method_anchors': ['invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/IntegerKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;
    .registers 3

    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/IntegerKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/IntegerKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_keyframe_IntegerKeyframeAnimation__getIntValue',
        'method': '.method getIntValue(Lcom/airbnb/lottie/value/Keyframe;F)I',
        'method_name': 'getIntValue',
        'method_anchors': ['iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;', 'if-eqz v0, :cond_2', 'iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;', 'if-eqz v0, :cond_2', 'iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->valueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;', 'if-eqz v1, :cond_0', 'iget v2, p1, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F', 'iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;'],
        'type': 'method_replace',
        'search': """.method getIntValue(Lcom/airbnb/lottie/value/Keyframe;F)I
    .registers 12

    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    if-eqz v0, :cond_2

    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    if-eqz v0, :cond_2

    iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->valueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    if-eqz v1, :cond_0

    iget v2, p1, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F

    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;

    invoke-virtual {v0}, Ljava/lang/Float;->floatValue()F

    move-result v3

    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    move-object v4, v0

    check-cast v4, Ljava/lang/Integer;

    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    move-object v5, v0

    check-cast v5, Ljava/lang/Integer;

    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getLinearCurrentKeyframeProgress()F

    move-result v7

    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getProgress()F

    move-result v8

    move v6, p2

    invoke-virtual/range {v1 .. v8}, Lcom/airbnb/lottie/value/LottieValueCallback;->getValueInternal(FFLjava/lang/Object;Ljava/lang/Object;FFF)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Ljava/lang/Integer;

    if-eqz p0, :cond_1

    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    return p0

    :cond_0
    move v6, p2

    :cond_1
    invoke-virtual {p1}, Lcom/airbnb/lottie/value/Keyframe;->getStartValueInt()I

    move-result p0

    invoke-virtual {p1}, Lcom/airbnb/lottie/value/Keyframe;->getEndValueInt()I

    move-result p1

    invoke-static {p0, p1, v6}, Lcom/airbnb/lottie/utils/MiscUtils;->lerp(IIF)I

    move-result p0

    return p0

    :cond_2
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string p1, "Missing values for keyframe."

    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method getIntValue(Lcom/airbnb/lottie/value/Keyframe;F)I
    .registers 12

    goto :goto_4

    nop

    :goto_0
    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    goto :goto_21

    nop

    :goto_1
    invoke-static {p0, p1, v6}, Lcom/airbnb/lottie/utils/MiscUtils;->lerp(IIF)I

    move-result p0

    goto :goto_17

    nop

    :goto_2
    check-cast p0, Ljava/lang/Integer;

    goto :goto_b

    nop

    :goto_3
    move-object v5, v0

    goto :goto_9

    nop

    :goto_4
    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    goto :goto_19

    nop

    :goto_5
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getLinearCurrentKeyframeProgress()F

    move-result v7

    goto :goto_a

    nop

    :goto_6
    return p0

    :goto_7
    goto :goto_e

    nop

    :goto_8
    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;

    goto :goto_12

    nop

    :goto_9
    check-cast v5, Ljava/lang/Integer;

    goto :goto_5

    nop

    :goto_a
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getProgress()F

    move-result v8

    goto :goto_1d

    nop

    :goto_b
    if-nez p0, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_1f

    nop

    :goto_c
    check-cast v4, Ljava/lang/Integer;

    goto :goto_10

    nop

    :goto_d
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_13

    nop

    :goto_e
    move v6, p2

    :goto_f
    goto :goto_15

    nop

    :goto_10
    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    goto :goto_3

    nop

    :goto_11
    throw p0

    :goto_12
    invoke-virtual {v0}, Ljava/lang/Float;->floatValue()F

    move-result v3

    goto :goto_0

    nop

    :goto_13
    const-string p1, "Missing values for keyframe."

    goto :goto_1b

    nop

    :goto_14
    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    goto :goto_20

    nop

    :goto_15
    invoke-virtual {p1}, Lcom/airbnb/lottie/value/Keyframe;->getStartValueInt()I

    move-result p0

    goto :goto_22

    nop

    :goto_16
    if-nez v1, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_1a

    nop

    :goto_17
    return p0

    :goto_18
    goto :goto_d

    nop

    :goto_19
    if-nez v0, :cond_2

    goto :goto_18

    :cond_2
    goto :goto_14

    nop

    :goto_1a
    iget v2, p1, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F

    goto :goto_8

    nop

    :goto_1b
    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_11

    nop

    :goto_1c
    iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->valueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    goto :goto_16

    nop

    :goto_1d
    move v6, p2

    goto :goto_1e

    nop

    :goto_1e
    invoke-virtual/range {v1 .. v8}, Lcom/airbnb/lottie/value/LottieValueCallback;->getValueInternal(FFLjava/lang/Object;Ljava/lang/Object;FFF)Ljava/lang/Object;

    move-result-object p0

    goto :goto_2

    nop

    :goto_1f
    invoke-virtual {p0}, Ljava/lang/Integer;->intValue()I

    move-result p0

    goto :goto_6

    nop

    :goto_20
    if-nez v0, :cond_3

    goto :goto_18

    :cond_3
    goto :goto_1c

    nop

    :goto_21
    move-object v4, v0

    goto :goto_c

    nop

    :goto_22
    invoke-virtual {p1}, Lcom/airbnb/lottie/value/Keyframe;->getEndValueInt()I

    move-result p1

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_keyframe_IntegerKeyframeAnimation__getValue',
        'method': '.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;',
        'method_name': 'getValue',
        'method_anchors': ['invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/IntegerKeyframeAnimation;->getIntValue(Lcom/airbnb/lottie/value/Keyframe;F)I', 'invoke-static {p0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;
    .registers 3

    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/IntegerKeyframeAnimation;->getIntValue(Lcom/airbnb/lottie/value/Keyframe;F)I

    move-result p0

    invoke-static {p0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;
    .registers 3

    goto :goto_2

    nop

    :goto_0
    invoke-static {p0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    return-object p0

    :goto_2
    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/IntegerKeyframeAnimation;->getIntValue(Lcom/airbnb/lottie/value/Keyframe;F)I

    move-result p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
