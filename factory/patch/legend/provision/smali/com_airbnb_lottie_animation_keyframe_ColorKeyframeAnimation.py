TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/keyframe/ColorKeyframeAnimation.smali'
CLASS_FALLBACK_NAMES = ['ColorKeyframeAnimation.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/animation/keyframe/KeyframeAnimation;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_keyframe_ColorKeyframeAnimation__getValue',
        'method': '.method bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;',
        'method_name': 'getValue',
        'method_anchors': ['invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/ColorKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method bridge synthetic getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;
    .registers 3

    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/ColorKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;

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
    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/ColorKeyframeAnimation;->getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_keyframe_ColorKeyframeAnimation__getValue',
        'method': '.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;',
        'method_name': 'getValue',
        'method_anchors': ['invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/ColorKeyframeAnimation;->getIntValue(Lcom/airbnb/lottie/value/Keyframe;F)I', 'invoke-static {p0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;
    .registers 3

    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/ColorKeyframeAnimation;->getIntValue(Lcom/airbnb/lottie/value/Keyframe;F)I

    move-result p0

    invoke-static {p0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Integer;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    invoke-static {p0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p0

    goto :goto_2

    nop

    :goto_1
    invoke-virtual {p0, p1, p2}, Lcom/airbnb/lottie/animation/keyframe/ColorKeyframeAnimation;->getIntValue(Lcom/airbnb/lottie/value/Keyframe;F)I

    move-result p0

    goto :goto_0

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
