TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/keyframe/PathKeyframe.smali'
CLASS_FALLBACK_NAMES = ['PathKeyframe.smali']
CLASS_ANCHORS = ['.super Lcom/airbnb/lottie/value/Keyframe;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_keyframe_PathKeyframe__getPath',
        'method': '.method getPath()Landroid/graphics/Path;',
        'method_name': 'getPath',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/animation/keyframe/PathKeyframe;->path:Landroid/graphics/Path;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getPath()Landroid/graphics/Path;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/animation/keyframe/PathKeyframe;->path:Landroid/graphics/Path;

    return-object p0
.end method""",
        'replacement': """.method getPath()Landroid/graphics/Path;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Lcom/airbnb/lottie/animation/keyframe/PathKeyframe;->path:Landroid/graphics/Path;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
