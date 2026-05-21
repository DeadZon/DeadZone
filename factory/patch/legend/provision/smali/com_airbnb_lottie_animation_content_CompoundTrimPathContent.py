TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/animation/content/CompoundTrimPathContent.smali'
CLASS_FALLBACK_NAMES = ['CompoundTrimPathContent.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_animation_content_CompoundTrimPathContent__addTrimPath',
        'method': '.method addTrimPath(Lcom/airbnb/lottie/animation/content/TrimPathContent;)V',
        'method_name': 'addTrimPath',
        'method_anchors': ['iget-object p0, p0, Lcom/airbnb/lottie/animation/content/CompoundTrimPathContent;->contents:Ljava/util/List;', 'invoke-interface {p0, p1}, Ljava/util/List;->add(Ljava/lang/Object;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method addTrimPath(Lcom/airbnb/lottie/animation/content/TrimPathContent;)V
    .registers 2

    iget-object p0, p0, Lcom/airbnb/lottie/animation/content/CompoundTrimPathContent;->contents:Ljava/util/List;

    invoke-interface {p0, p1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    return-void
.end method""",
        'replacement': """.method addTrimPath(Lcom/airbnb/lottie/animation/content/TrimPathContent;)V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    invoke-interface {p0, p1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_0

    nop

    :goto_2
    iget-object p0, p0, Lcom/airbnb/lottie/animation/content/CompoundTrimPathContent;->contents:Ljava/util/List;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
