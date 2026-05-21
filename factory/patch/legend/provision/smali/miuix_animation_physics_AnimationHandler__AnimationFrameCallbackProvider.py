TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider.smali'
CLASS_FALLBACK_NAMES = ['AnimationHandler$AnimationFrameCallbackProvider.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_animation_physics_AnimationHandler__AnimationFrameCallbackProvider__getFrameDeltaNanos',
        'method': '.method getFrameDeltaNanos()J',
        'method_name': 'getFrameDeltaNanos',
        'method_anchors': ['return-wide v0'],
        'type': 'method_replace',
        'search': """.method getFrameDeltaNanos()J
    .registers 3

    const-wide/16 v0, 0x0

    return-wide v0
.end method""",
        'replacement': """.method getFrameDeltaNanos()J
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-wide v0

    :goto_1
    const-wide/16 v0, 0x0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_AnimationHandler__AnimationFrameCallbackProvider__postVsyncCallback',
        'method': '.method postVsyncCallback()V',
        'method_name': 'postVsyncCallback',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method postVsyncCallback()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method postVsyncCallback()V
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
