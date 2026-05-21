TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/AnimationHandler$FrameCallbackProvider33.smali'
CLASS_FALLBACK_NAMES = ['AnimationHandler$FrameCallbackProvider33.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;']

PATCHES = [
    {
        'id': 'miuix_animation_physics_AnimationHandler__FrameCallbackProvider33__getFrameDeltaNanos',
        'method': '.method getFrameDeltaNanos()J',
        'method_name': 'getFrameDeltaNanos',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mFrameDeltaNanos:J', 'return-wide v0'],
        'type': 'method_replace',
        'search': """.method getFrameDeltaNanos()J
    .registers 3

    iget-wide v0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mFrameDeltaNanos:J

    return-wide v0
.end method""",
        'replacement': """.method getFrameDeltaNanos()J
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-wide v0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mFrameDeltaNanos:J

    goto :goto_1

    nop

    :goto_1
    return-wide v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_AnimationHandler__FrameCallbackProvider33__getLooper',
        'method': '.method getLooper()Landroid/os/Looper;',
        'method_name': 'getLooper',
        'method_anchors': ['iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mLooper:Landroid/os/Looper;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getLooper()Landroid/os/Looper;
    .registers 1

    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mLooper:Landroid/os/Looper;

    return-object p0
.end method""",
        'replacement': """.method getLooper()Landroid/os/Looper;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mLooper:Landroid/os/Looper;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_AnimationHandler__FrameCallbackProvider33__isCurrentThread',
        'method': '.method isCurrentThread()Z',
        'method_name': 'isCurrentThread',
        'method_anchors': ['invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mLooper:Landroid/os/Looper;', 'invoke-virtual {p0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;', 'if-ne v0, p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method isCurrentThread()Z
    .registers 2

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mLooper:Landroid/os/Looper;

    invoke-virtual {p0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object p0

    if-ne v0, p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method isCurrentThread()Z
    .registers 2

    goto :goto_8

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    if-eq v0, p0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_4

    nop

    :goto_2
    return p0

    :goto_3
    const/4 p0, 0x0

    goto :goto_2

    nop

    :goto_4
    const/4 p0, 0x1

    goto :goto_6

    nop

    :goto_5
    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mLooper:Landroid/os/Looper;

    goto :goto_0

    nop

    :goto_6
    return p0

    :goto_7
    goto :goto_3

    nop

    :goto_8
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_AnimationHandler__FrameCallbackProvider33__postFrameCallback',
        'method': '.method postFrameCallback()V',
        'method_name': 'postFrameCallback',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mChoreographer:Landroid/view/Choreographer;', 'iget-object v1, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mVsyncCallback:Landroid/view/Choreographer$VsyncCallback;', 'invoke-virtual {v0, v1}, Landroid/view/Choreographer;->postVsyncCallback(Landroid/view/Choreographer$VsyncCallback;)V', 'iget-object v0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mChoreographer:Landroid/view/Choreographer;', 'iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mChoreographerCallback:Landroid/view/Choreographer$FrameCallback;', 'invoke-virtual {v0, p0}, Landroid/view/Choreographer;->postFrameCallback(Landroid/view/Choreographer$FrameCallback;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method postFrameCallback()V
    .registers 3

    iget-object v0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mChoreographer:Landroid/view/Choreographer;

    iget-object v1, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mVsyncCallback:Landroid/view/Choreographer$VsyncCallback;

    invoke-virtual {v0, v1}, Landroid/view/Choreographer;->postVsyncCallback(Landroid/view/Choreographer$VsyncCallback;)V

    iget-object v0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mChoreographer:Landroid/view/Choreographer;

    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mChoreographerCallback:Landroid/view/Choreographer$FrameCallback;

    invoke-virtual {v0, p0}, Landroid/view/Choreographer;->postFrameCallback(Landroid/view/Choreographer$FrameCallback;)V

    return-void
.end method""",
        'replacement': """.method postFrameCallback()V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mChoreographer:Landroid/view/Choreographer;

    goto :goto_4

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mChoreographerCallback:Landroid/view/Choreographer$FrameCallback;

    goto :goto_5

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mChoreographer:Landroid/view/Choreographer;

    goto :goto_1

    nop

    :goto_3
    return-void

    :goto_4
    iget-object v1, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider33;->mVsyncCallback:Landroid/view/Choreographer$VsyncCallback;

    goto :goto_6

    nop

    :goto_5
    invoke-virtual {v0, p0}, Landroid/view/Choreographer;->postFrameCallback(Landroid/view/Choreographer$FrameCallback;)V

    goto :goto_3

    nop

    :goto_6
    invoke-virtual {v0, v1}, Landroid/view/Choreographer;->postVsyncCallback(Landroid/view/Choreographer$VsyncCallback;)V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
