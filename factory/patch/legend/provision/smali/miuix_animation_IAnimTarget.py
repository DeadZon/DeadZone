TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/IAnimTarget.smali'
CLASS_FALLBACK_NAMES = ['IAnimTarget.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final FLAT_ONESHOT:J = 0x1L', '.field static final sTargetIds:Ljava/util/concurrent/atomic/AtomicInteger;']

PATCHES = [
    {
        'id': 'miuix_animation_IAnimTarget__awake',
        'method': '.method awake()V',
        'method_name': 'awake',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/animation/IAnimTarget;->mIsSleep:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method awake()V
    .registers 2

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/animation/IAnimTarget;->mIsSleep:Z

    return-void
.end method""",
        'replacement': """.method awake()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    iput-boolean v0, p0, Lmiuix/animation/IAnimTarget;->mIsSleep:Z

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_IAnimTarget__createHandler',
        'method': '.method protected createHandler(Landroid/os/Looper;)Lmiuix/animation/internal/TargetHandler;',
        'method_name': 'createHandler',
        'method_anchors': ['if-nez p1, :cond_0', 'new-instance p0, Ljava/lang/StringBuilder;', 'invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string p1, "warning!! the AnimTarget has created in a thread without Looper, the animation will do not work!!you should use HandlerThread instead of Thread, trace:"', 'invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'new-instance p1, Ljava/lang/Throwable;', 'invoke-direct {p1}, Ljava/lang/Throwable;-><init>()V', 'invoke-static {p1}, Landroid/util/Log;->getStackTraceString(Ljava/lang/Throwable;)Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected createHandler(Landroid/os/Looper;)Lmiuix/animation/internal/TargetHandler;
    .registers 5

    if-nez p1, :cond_0

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string p1, "warning!! the AnimTarget has created in a thread without Looper, the animation will do not work!!you should use HandlerThread instead of Thread, trace:"

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    new-instance p1, Ljava/lang/Throwable;

    invoke-direct {p1}, Ljava/lang/Throwable;-><init>()V

    invoke-static {p1}, Landroid/util/Log;->getStackTraceString(Ljava/lang/Throwable;)Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string p1, "miuix_anim"

    invoke-static {p1, p0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    const/4 p0, 0x0

    return-object p0

    :cond_0
    invoke-virtual {p1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    invoke-static {v0, v1}, Lmiuix/animation/Folme;->getUiLooperByTid(J)Landroid/os/Looper;

    move-result-object v0

    if-nez v0, :cond_2

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result v0

    if-eqz v0, :cond_1

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "IAnimTarget.createHandler registerUiLooper "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    const-string v1, " tid "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Thread;->getId()J

    move-result-wide v1

    invoke-virtual {v0, v1, v2}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const/4 v1, 0x0

    new-array v1, v1, [Ljava/lang/Object;

    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    invoke-static {p1}, Lmiuix/animation/Folme;->registerUiLooper(Landroid/os/Looper;)V

    :cond_2
    new-instance v0, Lmiuix/animation/internal/TargetHandler;

    invoke-direct {v0, p1, p0}, Lmiuix/animation/internal/TargetHandler;-><init>(Landroid/os/Looper;Lmiuix/animation/IAnimTarget;)V

    return-object v0
.end method""",
        'replacement': """.method protected createHandler(Landroid/os/Looper;)Lmiuix/animation/internal/TargetHandler;
    .registers 5

    goto :goto_27

    nop

    :goto_0
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_1
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_14

    nop

    :goto_2
    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    goto :goto_20

    nop

    :goto_3
    new-array v1, v1, [Ljava/lang/Object;

    goto :goto_21

    nop

    :goto_4
    const-string p1, "warning!! the AnimTarget has created in a thread without Looper, the animation will do not work!!you should use HandlerThread instead of Thread, trace:"

    goto :goto_1

    nop

    :goto_5
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result v0

    goto :goto_d

    nop

    :goto_6
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_25

    nop

    :goto_7
    const-string v1, "IAnimTarget.createHandler registerUiLooper "

    goto :goto_1c

    nop

    :goto_8
    invoke-static {p1, p0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1d

    nop

    :goto_9
    invoke-direct {v0, p1, p0}, Lmiuix/animation/internal/TargetHandler;-><init>(Landroid/os/Looper;Lmiuix/animation/IAnimTarget;)V

    goto :goto_15

    nop

    :goto_a
    invoke-virtual {p1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_2

    nop

    :goto_b
    invoke-direct {p1}, Ljava/lang/Throwable;-><init>()V

    goto :goto_28

    nop

    :goto_c
    new-instance v0, Lmiuix/animation/internal/TargetHandler;

    goto :goto_9

    nop

    :goto_d
    if-nez v0, :cond_0

    goto :goto_22

    :cond_0
    goto :goto_16

    nop

    :goto_e
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_f

    nop

    :goto_f
    const-string p1, "miuix_anim"

    goto :goto_8

    nop

    :goto_10
    if-eqz v0, :cond_1

    goto :goto_12

    :cond_1
    goto :goto_5

    nop

    :goto_11
    invoke-static {p1}, Lmiuix/animation/Folme;->registerUiLooper(Landroid/os/Looper;)V

    :goto_12
    goto :goto_c

    nop

    :goto_13
    invoke-virtual {v0, v1, v2}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    goto :goto_26

    nop

    :goto_14
    new-instance p1, Ljava/lang/Throwable;

    goto :goto_b

    nop

    :goto_15
    return-object v0

    :goto_16
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_1a

    nop

    :goto_17
    invoke-virtual {v1}, Ljava/lang/Thread;->getId()J

    move-result-wide v1

    goto :goto_13

    nop

    :goto_18
    return-object p0

    :goto_19
    goto :goto_a

    nop

    :goto_1a
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_7

    nop

    :goto_1b
    invoke-virtual {p1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v1

    goto :goto_17

    nop

    :goto_1c
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_1d
    const/4 p0, 0x0

    goto :goto_18

    nop

    :goto_1e
    const/4 v1, 0x0

    goto :goto_3

    nop

    :goto_1f
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_23

    nop

    :goto_20
    invoke-static {v0, v1}, Lmiuix/animation/Folme;->getUiLooperByTid(J)Landroid/os/Looper;

    move-result-object v0

    goto :goto_10

    nop

    :goto_21
    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_22
    goto :goto_11

    nop

    :goto_23
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_4

    nop

    :goto_24
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1b

    nop

    :goto_25
    const-string v1, " tid "

    goto :goto_24

    nop

    :goto_26
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_1e

    nop

    :goto_27
    if-eqz p1, :cond_2

    goto :goto_19

    :cond_2
    goto :goto_1f

    nop

    :goto_28
    invoke-static {p1}, Landroid/util/Log;->getStackTraceString(Ljava/lang/Throwable;)Ljava/lang/String;

    move-result-object p1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_IAnimTarget__finalize',
        'method': '.method protected finalize()V',
        'method_name': 'finalize',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z', 'if-eqz v0, :cond_0', 'new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "IAnimTarget was destroyed！"', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;', 'invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected finalize()V
    .registers 3
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/Throwable;
        }
    .end annotation

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    if-eqz v0, :cond_0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "IAnimTarget was destroyed！"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const/4 v1, 0x0

    new-array v1, v1, [Ljava/lang/Object;

    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    invoke-super {p0}, Ljava/lang/Object;->finalize()V

    return-void
.end method""",
        'replacement': """.method protected finalize()V
    .registers 3
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/Throwable;
        }
    .end annotation

    goto :goto_7

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_2

    nop

    :goto_1
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_8

    nop

    :goto_2
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_c

    nop

    :goto_3
    const-string v1, "IAnimTarget was destroyed！"

    goto :goto_b

    nop

    :goto_4
    return-void

    :goto_5
    new-array v1, v1, [Ljava/lang/Object;

    goto :goto_9

    nop

    :goto_6
    invoke-super {p0}, Ljava/lang/Object;->finalize()V

    goto :goto_4

    nop

    :goto_7
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    goto :goto_0

    nop

    :goto_8
    const/4 v1, 0x0

    goto :goto_5

    nop

    :goto_9
    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_a
    goto :goto_6

    nop

    :goto_b
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_d

    nop

    :goto_c
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_3

    nop

    :goto_d
    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_IAnimTarget__sleep',
        'method': '.method sleep()V',
        'method_name': 'sleep',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/animation/IAnimTarget;->mIsSleep:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method sleep()V
    .registers 2

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/animation/IAnimTarget;->mIsSleep:Z

    return-void
.end method""",
        'replacement': """.method sleep()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    const/4 v0, 0x1

    goto :goto_2

    nop

    :goto_2
    iput-boolean v0, p0, Lmiuix/animation/IAnimTarget;->mIsSleep:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
