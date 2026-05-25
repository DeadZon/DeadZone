TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/keyframe/ValueCallbackKeyframeAnimation.smali'
CLASS_FALLBACK_NAMES = ['ValueCallbackKeyframeAnimation.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_keyframe_ValueCallbackKeyframeAnimation__getEndProgress',
        'method': '.method getEndProgress()F',
        'method_name': 'getEndProgress',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method getEndProgress()F
    .registers 1

    const/high16 p0, 0x3f800000

    return p0
.end method""",
        'replacement': """.method getEndProgress()F
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/high16 p0, 0x3f800000

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_keyframe_ValueCallbackKeyframeAnimation__getValue',
        'method': '.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;',
        'method_name': 'getValue',
        'method_anchors': ['invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/ValueCallbackKeyframeAnimation;->getValue()Ljava/lang/Object;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;
    .registers 3

    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/ValueCallbackKeyframeAnimation;->getValue()Ljava/lang/Object;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method getValue(Lcom/airbnb/lottie/value/Keyframe;F)Ljava/lang/Object;
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/airbnb/lottie/animation/keyframe/ValueCallbackKeyframeAnimation;->getValue()Ljava/lang/Object;

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
]
