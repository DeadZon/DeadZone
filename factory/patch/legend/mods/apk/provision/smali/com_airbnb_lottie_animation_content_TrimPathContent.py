TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/content/TrimPathContent.smali'
CLASS_FALLBACK_NAMES = ['TrimPathContent.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lcom/airbnb/lottie/animation/content/Content;', '.implements Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$AnimationListener;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_content_TrimPathContent__addListener',
        'method': '.method addListener(Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$AnimationListener;)V',
        'method_name': 'addListener',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/animation/content/TrimPathContent;->listeners:Ljava/util/List;', 'invoke-interface {p0, p1}, Ljava/util/List;->add(Ljava/lang/Object;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method addListener(Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$AnimationListener;)V
    .registers 2

    iget-object p0, p0, Lcom/airbnb/lottie/animation/content/TrimPathContent;->listeners:Ljava/util/List;

    invoke-interface {p0, p1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    return-void
.end method""",
        'replacement': """.method addListener(Lcom/airbnb/lottie/animation/keyframe/BaseKeyframeAnimation$AnimationListener;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iget-object p0, p0, Lcom/airbnb/lottie/animation/content/TrimPathContent;->listeners:Ljava/util/List;

    goto :goto_2

    nop

    :goto_2
    invoke-interface {p0, p1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_animation_content_TrimPathContent__getType',
        'method': '.method getType()Lcom/airbnb/lottie/model/content/ShapeTrimPath$Type;',
        'method_name': 'getType',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/animation/content/TrimPathContent;->type:Lcom/airbnb/lottie/model/content/ShapeTrimPath$Type;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getType()Lcom/airbnb/lottie/model/content/ShapeTrimPath$Type;
    .registers 1

    iget-object p0, p0, Lcom/airbnb/lottie/animation/content/TrimPathContent;->type:Lcom/airbnb/lottie/model/content/ShapeTrimPath$Type;

    return-object p0
.end method""",
        'replacement': """.method getType()Lcom/airbnb/lottie/model/content/ShapeTrimPath$Type;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    iget-object p0, p0, Lcom/airbnb/lottie/animation/content/TrimPathContent;->type:Lcom/airbnb/lottie/model/content/ShapeTrimPath$Type;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
