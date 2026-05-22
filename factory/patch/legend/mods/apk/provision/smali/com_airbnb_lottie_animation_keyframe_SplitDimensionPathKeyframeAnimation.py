TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation.smali'
CLASS_FALLBACK_NAMES = ['SplitDimensionPathKeyframeAnimation.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_keyframe_SplitDimensionPathKeyframeAnimation__getValue',
        'method': '.method bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;',
        'method_name': 'getValue',
        'method_anchors': ['invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Landroid/graphics/PointF;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;
    .registers 3

    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Landroid/graphics/PointF;

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
    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Landroid/graphics/PointF;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_keyframe_SplitDimensionPathKeyframeAnimation__getValue',
        'method': '.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Landroid/graphics/PointF;',
        'method_name': 'getValue',
        'method_anchors': ['iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xValueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;', 'if-eqz p1, :cond_1', 'iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;', 'invoke-virtual {p1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;', 'if-eqz p1, :cond_1', 'iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;', 'invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getInterpolatedCurrentKeyframeProgress()F', 'iget-object v1, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;'],
        'type': 'method_replace',
        'search': """.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Landroid/graphics/PointF;
    .registers 13

    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xValueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    const/4 v0, 0x0

    if-eqz p1, :cond_1

    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    invoke-virtual {p1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;

    move-result-object p1

    if-eqz p1, :cond_1

    iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getInterpolatedCurrentKeyframeProgress()F

    move-result v9

    iget-object v1, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;

    iget-object v2, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xValueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    iget v3, p1, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F

    if-nez v1, :cond_0

    move v4, v3

    goto :goto_0

    :cond_0
    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    move v4, v1

    :goto_0
    iget-object v1, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    move-object v5, v1

    check-cast v5, Ljava/lang/Float;

    iget-object p1, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    move-object v6, p1

    check-cast v6, Ljava/lang/Float;

    move v8, p2

    move v7, p2

    invoke-virtual/range {v2 .. v9}, Lcom/airbnb/lottie/value/LottieValueCallback;->getValueInternal(FFLjava/lang/Object;Ljava/lang/Object;FFF)Ljava/lang/Object;

    move-result-object p1

    move v6, v7

    check-cast p1, Ljava/lang/Float;

    goto :goto_1

    :cond_1
    move v6, p2

    move-object p1, v0

    :goto_1
    iget-object p2, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->yValueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    if-eqz p2, :cond_3

    iget-object p2, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->yAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    invoke-virtual {p2}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;

    move-result-object p2

    if-eqz p2, :cond_3

    iget-object v0, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->yAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    invoke-virtual {v0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getInterpolatedCurrentKeyframeProgress()F

    move-result v8

    iget-object v0, p2, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;

    iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->yValueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    iget v2, p2, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F

    if-nez v0, :cond_2

    move v3, v2

    goto :goto_2

    :cond_2
    invoke-virtual {v0}, Ljava/lang/Float;->floatValue()F

    move-result v0

    move v3, v0

    :goto_2
    iget-object v0, p2, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    move-object v4, v0

    check-cast v4, Ljava/lang/Float;

    iget-object p2, p2, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    move-object v5, p2

    check-cast v5, Ljava/lang/Float;

    move v7, v6

    invoke-virtual/range {v1 .. v8}, Lcom/airbnb/lottie/value/LottieValueCallback;->getValueInternal(FFLjava/lang/Object;Ljava/lang/Object;FFF)Ljava/lang/Object;

    move-result-object p2

    move-object v0, p2

    check-cast v0, Ljava/lang/Float;

    :cond_3
    const/4 p2, 0x0

    if-nez p1, :cond_4

    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->pointWithCallbackValues:Landroid/graphics/PointF;

    iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->point:Landroid/graphics/PointF;

    iget v1, v1, Landroid/graphics/PointF;->x:F

    invoke-virtual {p1, v1, p2}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_3

    :cond_4
    iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->pointWithCallbackValues:Landroid/graphics/PointF;

    invoke-virtual {p1}, Ljava/lang/Float;->floatValue()F

    move-result p1

    invoke-virtual {v1, p1, p2}, Landroid/graphics/PointF;->set(FF)V

    :goto_3
    if-nez v0, :cond_5

    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->pointWithCallbackValues:Landroid/graphics/PointF;

    iget p2, p1, Landroid/graphics/PointF;->x:F

    iget-object v0, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->point:Landroid/graphics/PointF;

    iget v0, v0, Landroid/graphics/PointF;->y:F

    invoke-virtual {p1, p2, v0}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_4

    :cond_5
    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->pointWithCallbackValues:Landroid/graphics/PointF;

    iget p2, p1, Landroid/graphics/PointF;->x:F

    invoke-virtual {v0}, Ljava/lang/Float;->floatValue()F

    move-result v0

    invoke-virtual {p1, p2, v0}, Landroid/graphics/PointF;->set(FF)V

    :goto_4
    iget-object p0, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->pointWithCallbackValues:Landroid/graphics/PointF;

    return-object p0
.end method""",
        'replacement': """.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Landroid/graphics/PointF;
    .registers 13

    goto :goto_29

    nop

    :goto_0
    iget-object v1, p1, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    goto :goto_2

    nop

    :goto_1
    iget-object v0, p2, Lcom/airbnb/lottie/value/Keyframe;->startValue:Ljava/lang/Object;

    goto :goto_1b

    nop

    :goto_2
    move-object v5, v1

    goto :goto_a

    nop

    :goto_3
    invoke-virtual {p1, p2, v0}, Landroid/graphics/PointF;->set(FF)V

    :goto_4
    goto :goto_53

    nop

    :goto_5
    const/4 p2, 0x0

    goto :goto_39

    nop

    :goto_6
    invoke-virtual {v0}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getInterpolatedCurrentKeyframeProgress()F

    move-result v8

    goto :goto_2f

    nop

    :goto_7
    move-object p1, v0

    :goto_8
    goto :goto_35

    nop

    :goto_9
    iget v3, p1, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F

    goto :goto_3d

    nop

    :goto_a
    check-cast v5, Ljava/lang/Float;

    goto :goto_25

    nop

    :goto_b
    move v6, v7

    goto :goto_13

    nop

    :goto_c
    iget p2, p1, Landroid/graphics/PointF;->x:F

    goto :goto_16

    nop

    :goto_d
    goto :goto_4

    :goto_e
    goto :goto_3f

    nop

    :goto_f
    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->pointWithCallbackValues:Landroid/graphics/PointF;

    goto :goto_28

    nop

    :goto_10
    move v8, p2

    goto :goto_22

    nop

    :goto_11
    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_34

    nop

    :goto_12
    iget-object v0, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->point:Landroid/graphics/PointF;

    goto :goto_30

    nop

    :goto_13
    check-cast p1, Ljava/lang/Float;

    goto :goto_51

    nop

    :goto_14
    invoke-virtual {v1, p1, p2}, Landroid/graphics/PointF;->set(FF)V

    :goto_15
    goto :goto_2c

    nop

    :goto_16
    invoke-virtual {v0}, Ljava/lang/Float;->floatValue()F

    move-result v0

    goto :goto_3

    nop

    :goto_17
    iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_26

    nop

    :goto_18
    iget-object v2, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xValueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    goto :goto_9

    nop

    :goto_19
    if-nez p2, :cond_0

    goto :goto_33

    :cond_0
    goto :goto_4a

    nop

    :goto_1a
    move-object v0, p2

    goto :goto_32

    nop

    :goto_1b
    move-object v4, v0

    goto :goto_55

    nop

    :goto_1c
    if-nez p2, :cond_1

    goto :goto_33

    :cond_1
    goto :goto_56

    nop

    :goto_1d
    if-nez p1, :cond_2

    goto :goto_52

    :cond_2
    goto :goto_11

    nop

    :goto_1e
    move v7, v6

    goto :goto_50

    nop

    :goto_1f
    invoke-virtual {p2}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;

    move-result-object p2

    goto :goto_1c

    nop

    :goto_20
    invoke-virtual {p1, p2, v0}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_d

    nop

    :goto_21
    iget p2, p1, Landroid/graphics/PointF;->x:F

    goto :goto_12

    nop

    :goto_22
    move v7, p2

    goto :goto_43

    nop

    :goto_23
    move v4, v1

    :goto_24
    goto :goto_0

    nop

    :goto_25
    iget-object p1, p1, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    goto :goto_38

    nop

    :goto_26
    invoke-virtual {v1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getInterpolatedCurrentKeyframeProgress()F

    move-result v9

    goto :goto_57

    nop

    :goto_27
    check-cast v5, Ljava/lang/Float;

    goto :goto_1e

    nop

    :goto_28
    iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->point:Landroid/graphics/PointF;

    goto :goto_2d

    nop

    :goto_29
    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->xValueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    goto :goto_31

    nop

    :goto_2a
    iget v2, p2, Lcom/airbnb/lottie/value/Keyframe;->startFrame:F

    goto :goto_46

    nop

    :goto_2b
    invoke-virtual {v1}, Ljava/lang/Float;->floatValue()F

    move-result v1

    goto :goto_23

    nop

    :goto_2c
    if-eqz v0, :cond_3

    goto :goto_e

    :cond_3
    goto :goto_3e

    nop

    :goto_2d
    iget v1, v1, Landroid/graphics/PointF;->x:F

    goto :goto_40

    nop

    :goto_2e
    return-object p0

    :goto_2f
    iget-object v0, p2, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;

    goto :goto_4f

    nop

    :goto_30
    iget v0, v0, Landroid/graphics/PointF;->y:F

    goto :goto_20

    nop

    :goto_31
    const/4 v0, 0x0

    goto :goto_1d

    nop

    :goto_32
    check-cast v0, Ljava/lang/Float;

    :goto_33
    goto :goto_5

    nop

    :goto_34
    invoke-virtual {p1}, Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;->getCurrentKeyframe()Lcom/airbnb/lottie/value/Keyframe;

    move-result-object p1

    goto :goto_54

    nop

    :goto_35
    iget-object p2, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->yValueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    goto :goto_19

    nop

    :goto_36
    goto :goto_45

    :goto_37
    goto :goto_42

    nop

    :goto_38
    move-object v6, p1

    goto :goto_4b

    nop

    :goto_39
    if-eqz p1, :cond_4

    goto :goto_3c

    :cond_4
    goto :goto_f

    nop

    :goto_3a
    iget-object p2, p2, Lcom/airbnb/lottie/value/Keyframe;->endValue:Ljava/lang/Object;

    goto :goto_41

    nop

    :goto_3b
    goto :goto_15

    :goto_3c
    goto :goto_47

    nop

    :goto_3d
    if-eqz v1, :cond_5

    goto :goto_4d

    :cond_5
    goto :goto_49

    nop

    :goto_3e
    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->pointWithCallbackValues:Landroid/graphics/PointF;

    goto :goto_21

    nop

    :goto_3f
    iget-object p1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->pointWithCallbackValues:Landroid/graphics/PointF;

    goto :goto_c

    nop

    :goto_40
    invoke-virtual {p1, v1, p2}, Landroid/graphics/PointF;->set(FF)V

    goto :goto_3b

    nop

    :goto_41
    move-object v5, p2

    goto :goto_27

    nop

    :goto_42
    invoke-virtual {v0}, Ljava/lang/Float;->floatValue()F

    move-result v0

    goto :goto_44

    nop

    :goto_43
    invoke-virtual/range {v2 .. v9}, Lcom/airbnb/lottie/value/LottieValueCallback;->getValueInternal(FFLjava/lang/Object;Ljava/lang/Object;FFF)Ljava/lang/Object;

    move-result-object p1

    goto :goto_b

    nop

    :goto_44
    move v3, v0

    :goto_45
    goto :goto_1

    nop

    :goto_46
    if-eqz v0, :cond_6

    goto :goto_37

    :cond_6
    goto :goto_48

    nop

    :goto_47
    iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->pointWithCallbackValues:Landroid/graphics/PointF;

    goto :goto_4e

    nop

    :goto_48
    move v3, v2

    goto :goto_36

    nop

    :goto_49
    move v4, v3

    goto :goto_4c

    nop

    :goto_4a
    iget-object p2, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->yAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_1f

    nop

    :goto_4b
    check-cast v6, Ljava/lang/Float;

    goto :goto_10

    nop

    :goto_4c
    goto :goto_24

    :goto_4d
    goto :goto_2b

    nop

    :goto_4e
    invoke-virtual {p1}, Ljava/lang/Float;->floatValue()F

    move-result p1

    goto :goto_14

    nop

    :goto_4f
    iget-object v1, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->yValueCallback:Lcom/airbnb/lottie/value/LottieValueCallback;

    goto :goto_2a

    nop

    :goto_50
    invoke-virtual/range {v1 .. v8}, Lcom/airbnb/lottie/value/LottieValueCallback;->getValueInternal(FFLjava/lang/Object;Ljava/lang/Object;FFF)Ljava/lang/Object;

    move-result-object p2

    goto :goto_1a

    nop

    :goto_51
    goto :goto_8

    :goto_52
    goto :goto_58

    nop

    :goto_53
    iget-object p0, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->pointWithCallbackValues:Landroid/graphics/PointF;

    goto :goto_2e

    nop

    :goto_54
    if-nez p1, :cond_7

    goto :goto_52

    :cond_7
    goto :goto_17

    nop

    :goto_55
    check-cast v4, Ljava/lang/Float;

    goto :goto_3a

    nop

    :goto_56
    iget-object v0, p0, Lcom/airbnb/lottie/animation/keyframe/SplitDimensionPathKeyframeAnimation;->yAnimation:Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;

    goto :goto_6

    nop

    :goto_57
    iget-object v1, p1, Lcom/airbnb/lottie/value/Keyframe;->endFrame:Ljava/lang/Float;

    goto :goto_18

    nop

    :goto_58
    move v6, p2

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
