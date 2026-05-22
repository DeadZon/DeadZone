TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/AndroidEngine.smali'
CLASS_FALLBACK_NAMES = ['AndroidEngine.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/internal/FolmeEngine;', '.implements Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallback;', '.field private static final MSG_END:I = 0x1', '.field private static final MSG_START:I', '.field static final sThreadInstance:Ljava/lang/ThreadLocal;']

PATCHES = [
    {
        'id': 'miuix_animation_internal_AndroidEngine__scheduleNextFrame',
        'method': '.method protected scheduleNextFrame(J)V',
        'method_name': 'scheduleNextFrame',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/physics/AnimationHandler;->getInstance()Lmiuix/animation/physics/AnimationHandler;', 'invoke-virtual {v0, p0, p1, p2}, Lmiuix/animation/physics/AnimationHandler;->addAnimationFrameCallback(Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallback;J)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected scheduleNextFrame(J)V
    .registers 4

    invoke-static {}, Lmiuix/animation/physics/AnimationHandler;->getInstance()Lmiuix/animation/physics/AnimationHandler;

    move-result-object v0

    invoke-virtual {v0, p0, p1, p2}, Lmiuix/animation/physics/AnimationHandler;->addAnimationFrameCallback(Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallback;J)V

    return-void
.end method""",
        'replacement': """.method protected scheduleNextFrame(J)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v0, p0, p1, p2}, Lmiuix/animation/physics/AnimationHandler;->addAnimationFrameCallback(Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallback;J)V

    goto :goto_2

    nop

    :goto_1
    invoke-static {}, Lmiuix/animation/physics/AnimationHandler;->getInstance()Lmiuix/animation/physics/AnimationHandler;

    move-result-object v0

    goto :goto_0

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AndroidEngine__stopNextFrame',
        'method': '.method protected stopNextFrame()V',
        'method_name': 'stopNextFrame',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/physics/AnimationHandler;->getInstance()Lmiuix/animation/physics/AnimationHandler;', 'invoke-virtual {v0, p0}, Lmiuix/animation/physics/AnimationHandler;->removeCallback(Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallback;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected stopNextFrame()V
    .registers 2

    invoke-static {}, Lmiuix/animation/physics/AnimationHandler;->getInstance()Lmiuix/animation/physics/AnimationHandler;

    move-result-object v0

    invoke-virtual {v0, p0}, Lmiuix/animation/physics/AnimationHandler;->removeCallback(Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallback;)V

    return-void
.end method""",
        'replacement': """.method protected stopNextFrame()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v0, p0}, Lmiuix/animation/physics/AnimationHandler;->removeCallback(Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallback;)V

    goto :goto_2

    nop

    :goto_1
    invoke-static {}, Lmiuix/animation/physics/AnimationHandler;->getInstance()Lmiuix/animation/physics/AnimationHandler;

    move-result-object v0

    goto :goto_0

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
