TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/overscroller/internal/dynamicanimation/animation/AnimationHandler.smali'
CLASS_FALLBACK_NAMES = ['AnimationHandler.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final SUPPORT_MI_MOTION:Z', '.field public static final sAnimatorHandler:Ljava/lang/ThreadLocal;']

PATCHES = [
    {
        'id': 'miuix_overscroller_internal_dynamicanimation_animation_AnimationHandler__isCurrentThread',
        'method': '.method isCurrentThread()Z',
        'method_name': 'isCurrentThread',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->getProvider()Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;', 'invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;->isCurrentThread()Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method isCurrentThread()Z
    .registers 1

    invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->getProvider()Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;

    move-result-object p0

    invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;->isCurrentThread()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method isCurrentThread()Z
    .registers 1

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;->isCurrentThread()Z

    move-result p0

    goto :goto_1

    nop

    :goto_1
    return p0

    :goto_2
    invoke-virtual {p0}, Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler;->getProvider()Lmiuix/overscroller/internal/dynamicanimation/animation/AnimationHandler$AnimationFrameCallbackProvider;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
