TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/AnimationHandler.smali'
CLASS_FALLBACK_NAMES = ['AnimationHandler.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final FRAME_DELAY_MS:J = 0xaL', '.field public static final sAnimatorHandler:Ljava/lang/ThreadLocal;']

PATCHES = [
    {
        'id': 'miuix_animation_physics_AnimationHandler__isCurrentThread',
        'method': '.method isCurrentThread()Z',
        'method_name': 'isCurrentThread',
        'method_anchors': ['invoke-direct {p0}, Lmiuix/animation/physics/AnimationHandler;->getProvider()Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;', 'invoke-virtual {p0}, Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;->isCurrentThread()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method isCurrentThread()Z
    .registers 1

    invoke-direct {p0}, Lmiuix/animation/physics/AnimationHandler;->getProvider()Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;->isCurrentThread()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method isCurrentThread()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-direct {p0}, Lmiuix/animation/physics/AnimationHandler;->getProvider()Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;

    move-result-object p0

    goto :goto_2

    nop

    :goto_1
    return p0

    :goto_2
    invoke-virtual {p0}, Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;->isCurrentThread()Z

    move-result p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
