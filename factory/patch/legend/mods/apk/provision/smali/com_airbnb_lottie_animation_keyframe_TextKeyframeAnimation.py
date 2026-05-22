TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/keyframe/TextKeyframeAnimation.smali'
CLASS_FALLBACK_NAMES = ['TextKeyframeAnimation.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/animation/keyframe/KeyframeAnimation;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_keyframe_TextKeyframeAnimation__getValue',
        'method': '.method bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;',
        'method_name': 'getValue',
        'method_anchors': ['invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/TextKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Lcom/airbnb/lottie/model/DocumentData;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;
    .registers 3

    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/TextKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Lcom/airbnb/lottie/model/DocumentData;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/TextKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Lcom/airbnb/lottie/model/DocumentData;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_keyframe_TextKeyframeAnimation__getValue',
        'method': '.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Lcom/airbnb/lottie/model/DocumentData;',
        'method_name': 'getValue',
        'method_anchors': ['iget-object v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->valueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;', 'if-eqz v0, :cond_2', 'iget v1, p1, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F', 'iget-object v2, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;', 'if-nez v2, :cond_0', 'invoke-virtual {v2}, Ljava/lang/Float;->floatValue()F', 'iget-object v3, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;', 'check-cast v3, Lcom/airbnb/lottie/model/DocumentData;'],
        'type': 'method_replace',
        'search': """.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Lcom/airbnb/lottie/model/DocumentData;
    .registers 11

    iget-object v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->valueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    if-eqz v0, :cond_2

    iget v1, p1, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F

    iget-object v2, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;

    if-nez v2, :cond_0

    const v2, 0x7f7fffff

    goto :goto_0

    :cond_0
    invoke-virtual {v2}, Ljava/lang/Float;->floatValue()F

    move-result v2

    :goto_0
    iget-object v3, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    move-object v4, v3

    move-object v3, v4

    check-cast v3, Lcom/airbnb/lottie/model/DocumentData;

    iget-object p1, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    if-nez p1, :cond_1

    move-object p1, v4

    check-cast p1, Lcom/airbnb/lottie/model/DocumentData;

    :goto_1
    move-object v4, p1

    goto :goto_2

    :cond_1
    check-cast p1, Lcom/airbnb/lottie/model/DocumentData;

    goto :goto_1

    :goto_2
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getInterpolatedCurrentKeyframeProgress()F

    move-result v6

    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getProgress()F

    move-result v7

    move v5, p2

    invoke-virtual/range {v0 .. v7}, Lcom/airbnb/lottie/value/LottieValueCallback;->getValueInternal(FFLjava/lang/Object;Ljava/lang/Object;FFF)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Lcom/airbnb/lottie/model/DocumentData;

    return-object p0

    :cond_2
    move v5, p2

    const/high16 p0, 0x3f800000

    cmpl-float p0, v5, p0

    if-nez p0, :cond_4

    iget-object p0, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    if-nez p0, :cond_3

    goto :goto_3

    :cond_3
    check-cast p0, Lcom/airbnb/lottie/model/DocumentData;

    return-object p0

    :cond_4
    :goto_3
    iget-object p0, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    check-cast p0, Lcom/airbnb/lottie/model/DocumentData;

    return-object p0
.end method""",
        'replacement': """.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Lcom/airbnb/lottie/model/DocumentData;
    .registers 11

    goto :goto_d

    nop

    :goto_0
    iget-object p0, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    goto :goto_21

    nop

    :goto_1
    goto :goto_12

    :goto_2
    goto :goto_15

    nop

    :goto_3
    move v5, p2

    goto :goto_28

    nop

    :goto_4
    if-eqz p1, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_b

    nop

    :goto_5
    check-cast p0, Lcom/airbnb/lottie/model/DocumentData;

    goto :goto_e

    nop

    :goto_6
    goto :goto_20

    :goto_7
    goto :goto_1c

    nop

    :goto_8
    move-object v3, v4

    goto :goto_9

    nop

    :goto_9
    check-cast v3, Lcom/airbnb/lottie/model/DocumentData;

    goto :goto_27

    nop

    :goto_a
    cmpl-float p0, v5, p0

    goto :goto_1a

    nop

    :goto_b
    move-object p1, v4

    goto :goto_29

    nop

    :goto_c
    move-object v4, v3

    goto :goto_8

    nop

    :goto_d
    iget-object v0, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->valueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    goto :goto_14

    nop

    :goto_e
    return-object p0

    :goto_f
    goto :goto_3

    nop

    :goto_10
    iget v1, p1, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F

    goto :goto_17

    nop

    :goto_11
    return-object p0

    :goto_12
    goto :goto_0

    nop

    :goto_13
    iget-object v3, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    goto :goto_c

    nop

    :goto_14
    if-nez v0, :cond_1

    goto :goto_f

    :cond_1
    goto :goto_10

    nop

    :goto_15
    check-cast p0, Lcom/airbnb/lottie/model/DocumentData;

    goto :goto_11

    nop

    :goto_16
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getProgress()F

    move-result v7

    goto :goto_23

    nop

    :goto_17
    iget-object v2, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;

    goto :goto_19

    nop

    :goto_18
    return-object p0

    :goto_19
    if-eqz v2, :cond_2

    goto :goto_25

    :cond_2
    goto :goto_1e

    nop

    :goto_1a
    if-eqz p0, :cond_3

    goto :goto_12

    :cond_3
    goto :goto_26

    nop

    :goto_1b
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getInterpolatedCurrentKeyframeProgress()F

    move-result v6

    goto :goto_16

    nop

    :goto_1c
    check-cast p1, Lcom/airbnb/lottie/model/DocumentData;

    goto :goto_1f

    nop

    :goto_1d
    if-eqz p0, :cond_4

    goto :goto_2

    :cond_4
    goto :goto_1

    nop

    :goto_1e
    const v2, 0x7f7fffff

    goto :goto_24

    nop

    :goto_1f
    goto :goto_2a

    :goto_20
    goto :goto_1b

    nop

    :goto_21
    check-cast p0, Lcom/airbnb/lottie/model/DocumentData;

    goto :goto_18

    nop

    :goto_22
    invoke-virtual/range {v0 .. v7}, Lcom/airbnb/lottie/value/LottieValueCallback;->getValueInternal(FFLjava/lang/Object;Ljava/lang/Object;FFF)Ljava/lang/Object;

    move-result-object p0

    goto :goto_5

    nop

    :goto_23
    move v5, p2

    goto :goto_22

    nop

    :goto_24
    goto :goto_2d

    :goto_25
    goto :goto_2c

    nop

    :goto_26
    iget-object p0, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    goto :goto_1d

    nop

    :goto_27
    iget-object p1, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    goto :goto_4

    nop

    :goto_28
    const/high16 p0, 0x3f800000

    goto :goto_a

    nop

    :goto_29
    check-cast p1, Lcom/airbnb/lottie/model/DocumentData;

    :goto_2a
    goto :goto_2b

    nop

    :goto_2b
    move-object v4, p1

    goto :goto_6

    nop

    :goto_2c
    invoke-virtual {v2}, Ljava/lang/Float;->floatValue()F

    move-result v2

    :goto_2d
    goto :goto_13

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
