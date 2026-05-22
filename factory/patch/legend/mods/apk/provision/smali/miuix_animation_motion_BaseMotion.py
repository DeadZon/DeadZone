TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/motion/BaseMotion.smali'
CLASS_FALLBACK_NAMES = ['BaseMotion.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/animation/motion/Motion;']

PATCHES = [
    {
        'id': 'miuix_animation_motion_BaseMotion__onInitialVChanged',
        'method': '.method protected onInitialVChanged()V',
        'method_name': 'onInitialVChanged',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onInitialVChanged()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected onInitialVChanged()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_motion_BaseMotion__onInitialXChanged',
        'method': '.method protected onInitialXChanged()V',
        'method_name': 'onInitialXChanged',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onInitialXChanged()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected onInitialXChanged()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
