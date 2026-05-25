TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/TargetVelocityTracker$ResetRunnable.smali'
CLASS_FALLBACK_NAMES = ['TargetVelocityTracker$ResetRunnable.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/lang/Runnable;']

PATCHES = [
    {
        'id': 'miuix_animation_internal_TargetVelocityTracker__ResetRunnable__post',
        'method': '.method post(Lmiuix/animation/IAnimTarget;Lmiuix/animation/property/FloatProperty;)V',
        'method_name': 'post',
        'method_anchors': ['invoke-virtual {p1, p0}, Lmiuix/animation/IAnimTarget;->removeTask(Ljava/lang/Runnable;)V', 'iget-object v0, p0, Lmiuix/animation/internal/TargetVelocityTracker$ResetRunnable;->mTargetRef:Ljava/lang/ref/WeakReference;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'if-eq v0, p1, :cond_1', 'new-instance v0, Ljava/lang/ref/WeakReference;', 'invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V', 'iput-object v0, p0, Lmiuix/animation/internal/TargetVelocityTracker$ResetRunnable;->mTargetRef:Ljava/lang/ref/WeakReference;'],
        'type': 'method_replace',
        'search': """.method post(Lmiuix/animation/IAnimTarget;Lmiuix/animation/property/FloatProperty;)V
    .registers 5

    invoke-virtual {p1, p0}, Lmiuix/animation/IAnimTarget;->removeTask(Ljava/lang/Runnable;)V

    iget-object v0, p0, Lmiuix/animation/internal/TargetVelocityTracker$ResetRunnable;->mTargetRef:Ljava/lang/ref/WeakReference;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    if-eq v0, p1, :cond_1

    :cond_0
    new-instance v0, Ljava/lang/ref/WeakReference;

    invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    iput-object v0, p0, Lmiuix/animation/internal/TargetVelocityTracker$ResetRunnable;->mTargetRef:Ljava/lang/ref/WeakReference;

    :cond_1
    iput-object p2, p0, Lmiuix/animation/internal/TargetVelocityTracker$ResetRunnable;->mProperty:Lmiuix/animation/property/FloatProperty;

    const-wide/16 v0, 0x258

    invoke-virtual {p1, p0, v0, v1}, Lmiuix/animation/IAnimTarget;->postDelayed(Ljava/lang/Runnable;J)V

    return-void
.end method""",
        'replacement': """.method post(Lmiuix/animation/IAnimTarget;Lmiuix/animation/property/FloatProperty;)V
    .registers 5

    goto :goto_7

    nop

    :goto_0
    invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    goto :goto_5

    nop

    :goto_1
    new-instance v0, Ljava/lang/ref/WeakReference;

    goto :goto_0

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_8

    nop

    :goto_3
    if-ne v0, p1, :cond_1

    goto :goto_6

    :cond_1
    :goto_4
    goto :goto_1

    nop

    :goto_5
    iput-object v0, p0, Lmiuix/animation/internal/TargetVelocityTracker$ResetRunnable;->mTargetRef:Ljava/lang/ref/WeakReference;

    :goto_6
    goto :goto_c

    nop

    :goto_7
    invoke-virtual {p1, p0}, Lmiuix/animation/IAnimTarget;->removeTask(Ljava/lang/Runnable;)V

    goto :goto_d

    nop

    :goto_8
    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    goto :goto_3

    nop

    :goto_9
    return-void

    :goto_a
    invoke-virtual {p1, p0, v0, v1}, Lmiuix/animation/IAnimTarget;->postDelayed(Ljava/lang/Runnable;J)V

    goto :goto_9

    nop

    :goto_b
    const-wide/16 v0, 0x258

    goto :goto_a

    nop

    :goto_c
    iput-object p2, p0, Lmiuix/animation/internal/TargetVelocityTracker$ResetRunnable;->mProperty:Lmiuix/animation/property/FloatProperty;

    goto :goto_b

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/animation/internal/TargetVelocityTracker$ResetRunnable;->mTargetRef:Ljava/lang/ref/WeakReference;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
