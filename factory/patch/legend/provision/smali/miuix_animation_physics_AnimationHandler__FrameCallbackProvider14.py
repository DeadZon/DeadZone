TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/physics/AnimationHandler$FrameCallbackProvider14.smali'
CLASS_FALLBACK_NAMES = ['AnimationHandler$FrameCallbackProvider14.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/physics/AnimationHandler$AnimationFrameCallbackProvider;']

PATCHES = [
    {
        'id': 'miuix_animation_physics_AnimationHandler__FrameCallbackProvider14__getLooper',
        'method': '.method getLooper()Landroid/os/Looper;',
        'method_name': 'getLooper',
        'method_anchors': ['iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mHandler:Landroid/os/Handler;', 'invoke-virtual {p0}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getLooper()Landroid/os/Looper;
    .registers 1

    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mHandler:Landroid/os/Handler;

    invoke-virtual {p0}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method getLooper()Landroid/os/Looper;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;

    move-result-object p0

    goto :goto_2

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mHandler:Landroid/os/Handler;

    goto :goto_0

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_AnimationHandler__FrameCallbackProvider14__isCurrentThread',
        'method': '.method isCurrentThread()Z',
        'method_name': 'isCurrentThread',
        'method_anchors': ['invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mHandler:Landroid/os/Handler;', 'invoke-virtual {p0}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;', 'invoke-virtual {p0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;', 'if-ne v0, p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method isCurrentThread()Z
    .registers 2

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mHandler:Landroid/os/Handler;

    invoke-virtual {p0}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;

    move-result-object p0

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

    goto :goto_6

    nop

    :goto_0
    if-eq v0, p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_5

    nop

    :goto_1
    invoke-virtual {p0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object p0

    goto :goto_0

    nop

    :goto_2
    return p0

    :goto_3
    goto :goto_8

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/os/Handler;->getLooper()Landroid/os/Looper;

    move-result-object p0

    goto :goto_1

    nop

    :goto_5
    const/4 p0, 0x1

    goto :goto_2

    nop

    :goto_6
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_7

    nop

    :goto_7
    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mHandler:Landroid/os/Handler;

    goto :goto_4

    nop

    :goto_8
    const/4 p0, 0x0

    goto :goto_9

    nop

    :goto_9
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_physics_AnimationHandler__FrameCallbackProvider14__postFrameCallback',
        'method': '.method postFrameCallback()V',
        'method_name': 'postFrameCallback',
        'method_anchors': ['invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J', 'iget-wide v2, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mLastFrameTime:J', 'invoke-static {v2, v3, v0, v1}, Ljava/lang/Math;->max(JJ)J', 'iget-object v2, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mHandler:Landroid/os/Handler;', 'iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mRunnable:Ljava/lang/Runnable;', 'invoke-virtual {v2, p0, v0, v1}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method postFrameCallback()V
    .registers 5

    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v0

    iget-wide v2, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mLastFrameTime:J

    sub-long/2addr v0, v2

    const-wide/16 v2, 0xa

    sub-long/2addr v2, v0

    const-wide/16 v0, 0x0

    invoke-static {v2, v3, v0, v1}, Ljava/lang/Math;->max(JJ)J

    move-result-wide v0

    iget-object v2, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mHandler:Landroid/os/Handler;

    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mRunnable:Ljava/lang/Runnable;

    invoke-virtual {v2, p0, v0, v1}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    return-void
.end method""",
        'replacement': """.method postFrameCallback()V
    .registers 5

    goto :goto_4

    nop

    :goto_0
    invoke-static {v2, v3, v0, v1}, Ljava/lang/Math;->max(JJ)J

    move-result-wide v0

    goto :goto_7

    nop

    :goto_1
    sub-long/2addr v0, v2

    goto :goto_a

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mRunnable:Ljava/lang/Runnable;

    goto :goto_9

    nop

    :goto_3
    iget-wide v2, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mLastFrameTime:J

    goto :goto_1

    nop

    :goto_4
    invoke-static {}, Landroid/os/SystemClock;->uptimeMillis()J

    move-result-wide v0

    goto :goto_3

    nop

    :goto_5
    sub-long/2addr v2, v0

    goto :goto_8

    nop

    :goto_6
    return-void

    :goto_7
    iget-object v2, p0, Lmiuix/animation/physics/AnimationHandler$FrameCallbackProvider14;->mHandler:Landroid/os/Handler;

    goto :goto_2

    nop

    :goto_8
    const-wide/16 v0, 0x0

    goto :goto_0

    nop

    :goto_9
    invoke-virtual {v2, p0, v0, v1}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    goto :goto_6

    nop

    :goto_a
    const-wide/16 v2, 0xa

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
