TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/keyframe/PointKeyframeAnimation.smali'
CLASS_FALLBACK_NAMES = ['PointKeyframeAnimation.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/animation/keyframe/KeyframeAnimation;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_keyframe_PointKeyframeAnimation__getValue',
        'method': '.method protected bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Ljava/lang/Object;',
        'method_name': 'getValue',
        'method_anchors': ['invoke-virtual {p0, p1, p2, p3, p4}, Lcom/airbnb/lottie/animation/keyframe/PointKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Landroid/graphics/PointF;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Ljava/lang/Object;
    .registers 5

    invoke-virtual {p0, p1, p2, p3, p4}, Lcom/airbnb/lottie/animation/keyframe/PointKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Landroid/graphics/PointF;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Ljava/lang/Object;
    .registers 5

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0, p1, p2, p3, p4}, Lcom/airbnb/lottie/animation/keyframe/PointKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Landroid/graphics/PointF;

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
        'id': 'com_airbnb_lottie_animation_keyframe_PointKeyframeAnimation__getValue',
        'method': '.method protected getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Landroid/graphics/PointF;',
        'method_name': 'getValue',
        'method_anchors': ['iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;', 'if-eqz v0, :cond_1', 'iget-object v1, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;', 'if-eqz v1, :cond_1', 'check-cast v5, Landroid/graphics/PointF;', 'check-cast v6, Landroid/graphics/PointF;', 'iget-object v2, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->valueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;', 'if-eqz v2, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Landroid/graphics/PointF;
    .registers 15

    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    if-eqz v0, :cond_1

    iget-object v1, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    if-eqz v1, :cond_1

    move-object v5, v0

    check-cast v5, Landroid/graphics/PointF;

    move-object v6, v1

    check-cast v6, Landroid/graphics/PointF;

    iget-object v2, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->valueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    if-eqz v2, :cond_0

    iget v3, p1, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F

    iget-object p1, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;

    invoke-virtual {p1}, Ljava/lang/Float;->floatValue()F

    move-result v4

    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getLinearCurrentKeyframeProgress()F

    move-result v8

    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getProgress()F

    move-result v9

    move v7, p2

    invoke-virtual/range {v2 .. v9}, Lcom/airbnb/lottie/value/LottieValueCallback;->getValueInternal(FFLjava/lang/Object;Ljava/lang/Object;FFF)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Landroid/graphics/PointF;

    if-eqz p1, :cond_0

    return-object p1

    :cond_0
    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/PointKeyframeAnimation;->point:Landroid/graphics/PointF;

    iget p2, v5, Landroid/graphics/PointF;->x:F

    iget v0, v6, Landroid/graphics/PointF;->x:F

    sub-float/2addr v0, p2

    mul-float/2addr p3, v0

    add-float/2addr p2, p3

    iget p3, v5, Landroid/graphics/PointF;->y:F

    iget v0, v6, Landroid/graphics/PointF;->y:F

    sub-float/2addr v0, p3

    mul-float/2addr p4, v0

    add-float/2addr p3, p4

    invoke-virtual {p1, p2, p3}, Landroid/graphics/PointF;->set(FF)V

    iget-object p0, p0, Lcom/airbnb/lottie/animation/keyframe/PointKeyframeAnimation;->point:Landroid/graphics/PointF;

    return-object p0

    :cond_1
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string p1, "Missing values for keyframe."

    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method protected getValue(Lcom/airbnb/lottie/value/Keyframe;FFF)Landroid/graphics/PointF;
    .registers 15

    goto :goto_1c

    nop

    :goto_0
    if-nez v1, :cond_0

    goto :goto_12

    :cond_0
    goto :goto_1d

    nop

    :goto_1
    if-nez p1, :cond_1

    goto :goto_27

    :cond_1
    goto :goto_26

    nop

    :goto_2
    iget v0, v6, Landroid/graphics/PointF;->x:F

    goto :goto_e

    nop

    :goto_3
    const-string p1, "Missing values for keyframe."

    goto :goto_1b

    nop

    :goto_4
    mul-float/2addr p3, v0

    goto :goto_1a

    nop

    :goto_5
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getLinearCurrentKeyframeProgress()F

    move-result v8

    goto :goto_9

    nop

    :goto_6
    check-cast v6, Landroid/graphics/PointF;

    goto :goto_1e

    nop

    :goto_7
    iget v3, p1, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F

    goto :goto_8

    nop

    :goto_8
    iget-object p1, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;

    goto :goto_20

    nop

    :goto_9
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getProgress()F

    move-result v9

    goto :goto_13

    nop

    :goto_a
    move-object v6, v1

    goto :goto_6

    nop

    :goto_b
    invoke-virtual/range {v2 .. v9}, Lcom/airbnb/lottie/value/LottieValueCallback;->getValueInternal(FFLjava/lang/Object;Ljava/lang/Object;FFF)Ljava/lang/Object;

    move-result-object p1

    goto :goto_17

    nop

    :goto_c
    sub-float/2addr v0, p3

    goto :goto_25

    nop

    :goto_d
    if-nez v2, :cond_2

    goto :goto_27

    :cond_2
    goto :goto_7

    nop

    :goto_e
    sub-float/2addr v0, p2

    goto :goto_4

    nop

    :goto_f
    iget-object p0, p0, Lcom/airbnb/lottie/animation/keyframe/PointKeyframeAnimation;->point:Landroid/graphics/PointF;

    goto :goto_11

    nop

    :goto_10
    throw p0

    :goto_11
    return-object p0

    :goto_12
    goto :goto_22

    nop

    :goto_13
    move v7, p2

    goto :goto_b

    nop

    :goto_14
    if-nez v0, :cond_3

    goto :goto_12

    :cond_3
    goto :goto_21

    nop

    :goto_15
    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/PointKeyframeAnimation;->point:Landroid/graphics/PointF;

    goto :goto_18

    nop

    :goto_16
    add-float/2addr p3, p4

    goto :goto_24

    nop

    :goto_17
    check-cast p1, Landroid/graphics/PointF;

    goto :goto_1

    nop

    :goto_18
    iget p2, v5, Landroid/graphics/PointF;->x:F

    goto :goto_2

    nop

    :goto_19
    iget p3, v5, Landroid/graphics/PointF;->y:F

    goto :goto_23

    nop

    :goto_1a
    add-float/2addr p2, p3

    goto :goto_19

    nop

    :goto_1b
    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_10

    nop

    :goto_1c
    iget-object v0, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    goto :goto_14

    nop

    :goto_1d
    move-object v5, v0

    goto :goto_1f

    nop

    :goto_1e
    iget-object v2, p0, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->valueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    goto :goto_d

    nop

    :goto_1f
    check-cast v5, Landroid/graphics/PointF;

    goto :goto_a

    nop

    :goto_20
    invoke-virtual {p1}, Ljava/lang/Float;->floatValue()F

    move-result v4

    goto :goto_5

    nop

    :goto_21
    iget-object v1, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    goto :goto_0

    nop

    :goto_22
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_3

    nop

    :goto_23
    iget v0, v6, Landroid/graphics/PointF;->y:F

    goto :goto_c

    nop

    :goto_24
    invoke-virtual {p1, p2, p3}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_f

    nop

    :goto_25
    mul-float/2addr p4, v0

    goto :goto_16

    nop

    :goto_26
    return-object p1

    :goto_27
    goto :goto_15

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
