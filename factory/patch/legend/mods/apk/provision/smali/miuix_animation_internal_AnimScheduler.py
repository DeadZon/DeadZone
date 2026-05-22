TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/AnimScheduler.smali'
CLASS_FALLBACK_NAMES = ['AnimScheduler.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field static final MSG_CLEAN:I = 0x5', '.field static final MSG_RUN:I = 0x3', '.field static final MSG_SET_TO:I = 0x4', '.field static final MSG_TO:I = 0x1', '.field static final MSG_UPDATE:I = 0x2']

PATCHES = [
    {
        'id': 'miuix_animation_internal_AnimScheduler__executeDoAnimOnFrame',
        'method': '.method executeDoAnimOnFrame(JJ)V',
        'method_name': 'executeDoAnimOnFrame',
        'method_anchors': ['invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-virtual {v0}, Ljava/lang/Thread;->getId()J', 'invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0, p1, p2, p3, p4}, Lmiuix/animation/internal/AnimScheduler;->doAnimationFrame(JJ)V', 'return-void', 'iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;', 'if-eqz v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method executeDoAnimOnFrame(JJ)V
    .registers 12

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p0, p1, p2, p3, p4}, Lmiuix/animation/internal/AnimScheduler;->doAnimationFrame(JJ)V

    return-void

    :cond_0
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    if-eqz v0, :cond_1

    new-instance v1, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda1;

    move-object v2, p0

    move-wide v3, p1

    move-wide v5, p3

    invoke-direct/range {v1 .. v6}, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda1;-><init>(Lmiuix/animation/internal/AnimScheduler;JJ)V

    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    return-void

    :cond_1
    move-object v2, p0

    move-wide v3, p1

    move-wide v5, p3

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string p1, "executeOnFrame warning!! this scheduler has no handler"

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/16 p1, 0x8

    invoke-static {p1}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string p1, "miuix_anim"

    invoke-static {p1, p0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {v2, v3, v4, v5, v6}, Lmiuix/animation/internal/AnimScheduler;->doAnimationFrame(JJ)V

    return-void
.end method""",
        'replacement': """.method executeDoAnimOnFrame(JJ)V
    .registers 12

    goto :goto_1e

    nop

    :goto_0
    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    goto :goto_1f

    nop

    :goto_1
    const-string p1, "miuix_anim"

    goto :goto_10

    nop

    :goto_2
    return-void

    :goto_3
    goto :goto_15

    nop

    :goto_4
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_f

    nop

    :goto_5
    move-wide v3, p1

    goto :goto_12

    nop

    :goto_6
    move-object v2, p0

    goto :goto_c

    nop

    :goto_7
    return-void

    :goto_8
    goto :goto_18

    nop

    :goto_9
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_1

    nop

    :goto_a
    new-instance v1, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda1;

    goto :goto_6

    nop

    :goto_b
    return-void

    :goto_c
    move-wide v3, p1

    goto :goto_1c

    nop

    :goto_d
    if-nez v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_a

    nop

    :goto_e
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_11

    nop

    :goto_f
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_1a

    nop

    :goto_10
    invoke-static {p1, p0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1d

    nop

    :goto_11
    const/16 p1, 0x8

    goto :goto_14

    nop

    :goto_12
    move-wide v5, p3

    goto :goto_4

    nop

    :goto_13
    invoke-virtual {p0, p1, p2, p3, p4}, Lmiuix/animation/internal/AnimScheduler;->doAnimationFrame(JJ)V

    goto :goto_2

    nop

    :goto_14
    invoke-static {p1}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object p1

    goto :goto_1b

    nop

    :goto_15
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    goto :goto_d

    nop

    :goto_16
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_13

    nop

    :goto_17
    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    goto :goto_7

    nop

    :goto_18
    move-object v2, p0

    goto :goto_5

    nop

    :goto_19
    invoke-direct/range {v1 .. v6}, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda1;-><init>(Lmiuix/animation/internal/AnimScheduler;JJ)V

    goto :goto_17

    nop

    :goto_1a
    const-string p1, "executeOnFrame warning!! this scheduler has no handler"

    goto :goto_e

    nop

    :goto_1b
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_1c
    move-wide v5, p3

    goto :goto_19

    nop

    :goto_1d
    invoke-virtual {v2, v3, v4, v5, v6}, Lmiuix/animation/internal/AnimScheduler;->doAnimationFrame(JJ)V

    goto :goto_b

    nop

    :goto_1e
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_0

    nop

    :goto_1f
    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result v0

    goto :goto_16

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__executeNotifyTransitionBegin',
        'method': '.method executeNotifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'executeNotifyTransitionBegin',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'if-eqz v0, :cond_0', 'const-string v1, "----- TaskStackRunner before update : notifyTransitionBegin "', 'invoke-static {v1, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V', 'invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-virtual {v0}, Ljava/lang/Thread;->getId()J', 'invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z', 'if-eqz v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method executeNotifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 4

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/Object;

    const-string v1, "----- TaskStackRunner before update : notifyTransitionBegin "

    invoke-static {v1, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimScheduler;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;)V

    return-void

    :cond_1
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    if-eqz v0, :cond_2

    new-instance v1, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda0;

    invoke-direct {v1, p0, p1}, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda0;-><init>(Lmiuix/animation/internal/AnimScheduler;Lmiuix/animation/internal/TransitionInfo;)V

    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    return-void

    :cond_2
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "executeNotifyTransitionBegin warning!! this scheduler has no handler"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/16 v1, 0x8

    invoke-static {v1}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "miuix_anim"

    invoke-static {v1, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimScheduler;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;)V

    return-void
.end method""",
        'replacement': """.method executeNotifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 4

    goto :goto_12

    nop

    :goto_0
    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result v0

    goto :goto_10

    nop

    :goto_1
    const-string v1, "executeNotifyTransitionBegin warning!! this scheduler has no handler"

    goto :goto_d

    nop

    :goto_2
    invoke-static {v1}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v1

    goto :goto_17

    nop

    :goto_3
    const-string v1, "miuix_anim"

    goto :goto_1a

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_7

    nop

    :goto_6
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_3

    nop

    :goto_7
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_20

    nop

    :goto_8
    return-void

    :goto_9
    new-instance v1, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda0;

    goto :goto_18

    nop

    :goto_a
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_15

    nop

    :goto_b
    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    goto :goto_4

    nop

    :goto_c
    const-string v1, "----- TaskStackRunner before update : notifyTransitionBegin "

    goto :goto_1c

    nop

    :goto_d
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_11

    nop

    :goto_e
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    goto :goto_19

    nop

    :goto_f
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimScheduler;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_13

    nop

    :goto_10
    if-nez v0, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_f

    nop

    :goto_11
    const/16 v1, 0x8

    goto :goto_2

    nop

    :goto_12
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_1b

    nop

    :goto_13
    return-void

    :goto_14
    goto :goto_e

    nop

    :goto_15
    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    goto :goto_0

    nop

    :goto_16
    new-array v0, v0, [Ljava/lang/Object;

    goto :goto_c

    nop

    :goto_17
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_18
    invoke-direct {v1, p0, p1}, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda0;-><init>(Lmiuix/animation/internal/AnimScheduler;Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_b

    nop

    :goto_19
    if-nez v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_9

    nop

    :goto_1a
    invoke-static {v1, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1e

    nop

    :goto_1b
    if-nez v0, :cond_2

    goto :goto_1d

    :cond_2
    goto :goto_1f

    nop

    :goto_1c
    invoke-static {v1, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_1d
    goto :goto_a

    nop

    :goto_1e
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimScheduler;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_8

    nop

    :goto_1f
    const/4 v0, 0x0

    goto :goto_16

    nop

    :goto_20
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__executePendingSetTo',
        'method': '.method executePendingSetTo(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;)V',
        'method_name': 'executePendingSetTo',
        'method_anchors': ['new-instance v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;', 'invoke-direct {v0}, Lmiuix/animation/internal/AnimScheduler$SetToInfo;-><init>()V', 'iput-object p1, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->target:Lmiuix/animation/IAnimTarget;', 'iget-boolean p1, p2, Lmiuix/animation/controller/AnimState;->needDuplicate:Z', 'if-eqz p1, :cond_0', 'new-instance p1, Lmiuix/animation/controller/AnimState;', 'invoke-direct {p1}, Lmiuix/animation/controller/AnimState;-><init>()V', 'iput-object p1, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->state:Lmiuix/animation/controller/AnimState;'],
        'type': 'method_replace',
        'search': """.method executePendingSetTo(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;)V
    .registers 6
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    new-instance v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;

    invoke-direct {v0}, Lmiuix/animation/internal/AnimScheduler$SetToInfo;-><init>()V

    iput-object p1, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->target:Lmiuix/animation/IAnimTarget;

    iget-boolean p1, p2, Lmiuix/animation/controller/AnimState;->needDuplicate:Z

    if-eqz p1, :cond_0

    new-instance p1, Lmiuix/animation/controller/AnimState;

    invoke-direct {p1}, Lmiuix/animation/controller/AnimState;-><init>()V

    iput-object p1, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->state:Lmiuix/animation/controller/AnimState;

    invoke-virtual {p1, p2}, Lmiuix/animation/controller/AnimState;->set(Lmiuix/animation/controller/AnimState;)V

    goto :goto_0

    :cond_0
    iput-object p2, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->state:Lmiuix/animation/controller/AnimState;

    :goto_0
    iget-object p1, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    if-nez p1, :cond_1

    new-instance p2, Ljava/lang/StringBuilder;

    invoke-direct {p2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "executeSetTo warning!! this scheduler has no handler, so direct run executePendingSetTo(info)"

    invoke-virtual {p2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/16 v1, 0x8

    invoke-static {v1}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {p2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p2

    const-string v1, "miuix_anim"

    invoke-static {v1, p2}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    :cond_1
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p2

    invoke-virtual {p2}, Ljava/lang/Thread;->getId()J

    move-result-wide v1

    invoke-virtual {p0, v1, v2}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result p2

    if-nez p2, :cond_3

    if-nez p1, :cond_2

    goto :goto_1

    :cond_2
    new-instance p2, Lmiuix/animation/internal/AnimScheduler$1;

    invoke-direct {p2, p0, v0}, Lmiuix/animation/internal/AnimScheduler$1;-><init>(Lmiuix/animation/internal/AnimScheduler;Lmiuix/animation/internal/AnimScheduler$SetToInfo;)V

    invoke-virtual {p1, p2}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    return-void

    :cond_3
    :goto_1
    invoke-virtual {p0, v0}, Lmiuix/animation/internal/AnimScheduler;->pendingSetTo(Lmiuix/animation/internal/AnimScheduler$SetToInfo;)V

    return-void
.end method""",
        'replacement': """.method executePendingSetTo(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;)V
    .registers 6
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    goto :goto_1f

    nop

    :goto_0
    invoke-virtual {p2}, Ljava/lang/Thread;->getId()J

    move-result-wide v1

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, v1, v2}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result p2

    goto :goto_1e

    nop

    :goto_2
    if-eqz p1, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_4

    nop

    :goto_3
    if-eqz p1, :cond_1

    goto :goto_10

    :cond_1
    goto :goto_21

    nop

    :goto_4
    goto :goto_1a

    :goto_5
    goto :goto_d

    nop

    :goto_6
    invoke-virtual {p0, v0}, Lmiuix/animation/internal/AnimScheduler;->pendingSetTo(Lmiuix/animation/internal/AnimScheduler$SetToInfo;)V

    goto :goto_e

    nop

    :goto_7
    invoke-static {v1}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v1

    goto :goto_20

    nop

    :goto_8
    invoke-direct {p1}, Lmiuix/animation/controller/AnimState;-><init>()V

    goto :goto_11

    nop

    :goto_9
    invoke-direct {p2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_27

    nop

    :goto_a
    invoke-virtual {p2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1b

    nop

    :goto_b
    goto :goto_26

    :goto_c
    goto :goto_25

    nop

    :goto_d
    new-instance p2, Lmiuix/animation/internal/AnimScheduler$1;

    goto :goto_18

    nop

    :goto_e
    return-void

    :goto_f
    invoke-static {v1, p2}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    :goto_10
    goto :goto_23

    nop

    :goto_11
    iput-object p1, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->state:Lmiuix/animation/controller/AnimState;

    goto :goto_14

    nop

    :goto_12
    const-string v1, "miuix_anim"

    goto :goto_f

    nop

    :goto_13
    iget-boolean p1, p2, Lmiuix/animation/controller/AnimState;->needDuplicate:Z

    goto :goto_22

    nop

    :goto_14
    invoke-virtual {p1, p2}, Lmiuix/animation/controller/AnimState;->set(Lmiuix/animation/controller/AnimState;)V

    goto :goto_b

    nop

    :goto_15
    iget-object p1, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    goto :goto_3

    nop

    :goto_16
    iput-object p1, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->target:Lmiuix/animation/IAnimTarget;

    goto :goto_13

    nop

    :goto_17
    invoke-virtual {p1, p2}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    goto :goto_19

    nop

    :goto_18
    invoke-direct {p2, p0, v0}, Lmiuix/animation/internal/AnimScheduler$1;-><init>(Lmiuix/animation/internal/AnimScheduler;Lmiuix/animation/internal/AnimScheduler$SetToInfo;)V

    goto :goto_17

    nop

    :goto_19
    return-void

    :goto_1a
    goto :goto_6

    nop

    :goto_1b
    const/16 v1, 0x8

    goto :goto_7

    nop

    :goto_1c
    invoke-virtual {p2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p2

    goto :goto_12

    nop

    :goto_1d
    invoke-direct {v0}, Lmiuix/animation/internal/AnimScheduler$SetToInfo;-><init>()V

    goto :goto_16

    nop

    :goto_1e
    if-eqz p2, :cond_2

    goto :goto_1a

    :cond_2
    goto :goto_2

    nop

    :goto_1f
    new-instance v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;

    goto :goto_1d

    nop

    :goto_20
    invoke-virtual {p2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1c

    nop

    :goto_21
    new-instance p2, Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_22
    if-nez p1, :cond_3

    goto :goto_c

    :cond_3
    goto :goto_24

    nop

    :goto_23
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object p2

    goto :goto_0

    nop

    :goto_24
    new-instance p1, Lmiuix/animation/controller/AnimState;

    goto :goto_8

    nop

    :goto_25
    iput-object p2, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->state:Lmiuix/animation/controller/AnimState;

    :goto_26
    goto :goto_15

    nop

    :goto_27
    const-string v1, "executeSetTo warning!! this scheduler has no handler, so direct run executePendingSetTo(info)"

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__executeTo',
        'method': '.method executeTo(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'executeTo',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z', 'if-eqz v0, :cond_0', 'const-string v0, "++ executeTo"', 'invoke-static {v0, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V', 'iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;', 'iget-wide v2, v0, Lmiuix/animation/base/AnimConfig;->delay:J', 'if-lez v0, :cond_3', 'iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;'],
        'type': 'method_replace',
        'search': """.method executeTo(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 8

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    const-string v0, "++ executeTo"

    new-array v2, v1, [Ljava/lang/Object;

    invoke-static {v0, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    iget-wide v2, v0, Lmiuix/animation/base/AnimConfig;->delay:J

    const-wide/16 v4, 0x0

    cmp-long v0, v2, v4

    if-lez v0, :cond_3

    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    if-eqz v0, :cond_2

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    if-eqz v0, :cond_1

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "-- to with delay Scheduler@"

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result v2

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v2, " "

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    new-array v1, v1, [Ljava/lang/Object;

    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    new-instance v1, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda3;

    invoke-direct {v1, p0, p1}, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda3;-><init>(Lmiuix/animation/internal/AnimScheduler;Lmiuix/animation/internal/TransitionInfo;)V

    iget-object p0, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    iget-wide p0, p0, Lmiuix/animation/base/AnimConfig;->delay:J

    invoke-virtual {v0, v1, p0, p1}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    :cond_2
    return-void

    :cond_3
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result v0

    if-eqz v0, :cond_4

    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimScheduler;->to(Lmiuix/animation/internal/TransitionInfo;)V

    return-void

    :cond_4
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    if-eqz v0, :cond_5

    new-instance v1, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda4;

    invoke-direct {v1, p0, p1}, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda4;-><init>(Lmiuix/animation/internal/AnimScheduler;Lmiuix/animation/internal/TransitionInfo;)V

    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    return-void

    :cond_5
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "executeTo warning!! this scheduler has no handler, so direct run to(info)"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/16 v1, 0x8

    invoke-static {v1}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "miuix_anim"

    invoke-static {v1, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimScheduler;->to(Lmiuix/animation/internal/TransitionInfo;)V

    return-void
.end method""",
        'replacement': """.method executeTo(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 8

    goto :goto_7

    nop

    :goto_0
    const/4 v1, 0x0

    goto :goto_26

    nop

    :goto_1
    const-string v1, "miuix_anim"

    goto :goto_27

    nop

    :goto_2
    const-string v2, "-- to with delay Scheduler@"

    goto :goto_5

    nop

    :goto_3
    invoke-virtual {v0, v1, p0, p1}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    :goto_4
    goto :goto_1f

    nop

    :goto_5
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_18

    nop

    :goto_6
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_9

    nop

    :goto_7
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result v0

    goto :goto_0

    nop

    :goto_8
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_34

    nop

    :goto_9
    if-nez v0, :cond_0

    goto :goto_30

    :cond_0
    goto :goto_11

    nop

    :goto_a
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimScheduler;->to(Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_3e

    nop

    :goto_b
    const-string v0, "++ executeTo"

    goto :goto_35

    nop

    :goto_c
    invoke-direct {v1, p0, p1}, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda3;-><init>(Lmiuix/animation/internal/AnimScheduler;Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_3c

    nop

    :goto_d
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_1a

    nop

    :goto_e
    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    goto :goto_3f

    nop

    :goto_f
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    goto :goto_31

    nop

    :goto_10
    new-instance v1, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda3;

    goto :goto_c

    nop

    :goto_11
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_37

    nop

    :goto_12
    const-wide/16 v4, 0x0

    goto :goto_14

    nop

    :goto_13
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_d

    nop

    :goto_14
    cmp-long v0, v2, v4

    goto :goto_23

    nop

    :goto_15
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_8

    nop

    :goto_16
    if-nez v0, :cond_1

    goto :goto_1d

    :cond_1
    goto :goto_38

    nop

    :goto_17
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_13

    nop

    :goto_18
    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result v2

    goto :goto_1e

    nop

    :goto_19
    if-nez v0, :cond_2

    goto :goto_22

    :cond_2
    goto :goto_1b

    nop

    :goto_1a
    new-array v1, v1, [Ljava/lang/Object;

    goto :goto_2f

    nop

    :goto_1b
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimScheduler;->to(Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_21

    nop

    :goto_1c
    return-void

    :goto_1d
    goto :goto_15

    nop

    :goto_1e
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_24

    nop

    :goto_1f
    return-void

    :goto_20
    goto :goto_28

    nop

    :goto_21
    return-void

    :goto_22
    goto :goto_2d

    nop

    :goto_23
    if-gtz v0, :cond_3

    goto :goto_20

    :cond_3
    goto :goto_f

    nop

    :goto_24
    const-string v2, " "

    goto :goto_17

    nop

    :goto_25
    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    goto :goto_1c

    nop

    :goto_26
    if-nez v0, :cond_4

    goto :goto_2b

    :cond_4
    goto :goto_b

    nop

    :goto_27
    invoke-static {v1, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_a

    nop

    :goto_28
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_e

    nop

    :goto_29
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_36

    nop

    :goto_2a
    invoke-static {v0, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_2b
    goto :goto_32

    nop

    :goto_2c
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    goto :goto_10

    nop

    :goto_2d
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    goto :goto_16

    nop

    :goto_2e
    iget-wide p0, p0, Lmiuix/animation/base/AnimConfig;->delay:J

    goto :goto_3

    nop

    :goto_2f
    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_30
    goto :goto_2c

    nop

    :goto_31
    if-nez v0, :cond_5

    goto :goto_4

    :cond_5
    goto :goto_6

    nop

    :goto_32
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_33

    nop

    :goto_33
    iget-wide v2, v0, Lmiuix/animation/base/AnimConfig;->delay:J

    goto :goto_12

    nop

    :goto_34
    const-string v1, "executeTo warning!! this scheduler has no handler, so direct run to(info)"

    goto :goto_3a

    nop

    :goto_35
    new-array v2, v1, [Ljava/lang/Object;

    goto :goto_2a

    nop

    :goto_36
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_1

    nop

    :goto_37
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_2

    nop

    :goto_38
    new-instance v1, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda4;

    goto :goto_3b

    nop

    :goto_39
    const/16 v1, 0x8

    goto :goto_3d

    nop

    :goto_3a
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_39

    nop

    :goto_3b
    invoke-direct {v1, p0, p1}, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda4;-><init>(Lmiuix/animation/internal/AnimScheduler;Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_25

    nop

    :goto_3c
    iget-object p0, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_2e

    nop

    :goto_3d
    invoke-static {v1}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v1

    goto :goto_29

    nop

    :goto_3e
    return-void

    :goto_3f
    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result v0

    goto :goto_19

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__executeUpdate',
        'method': '.method executeUpdate()V',
        'method_name': 'executeUpdate',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z', 'if-eqz v0, :cond_0', 'const-string v1, "-- executeUpdate"', 'invoke-static {v1, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V', 'invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-virtual {v0}, Ljava/lang/Thread;->getId()J', 'invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z', 'if-eqz v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method executeUpdate()V
    .registers 3

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/Object;

    const-string v1, "-- executeUpdate"

    invoke-static {v1, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-virtual {p0}, Lmiuix/animation/internal/AnimScheduler;->update()V

    return-void

    :cond_1
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    if-eqz v0, :cond_2

    new-instance v1, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda2;

    invoke-direct {v1, p0}, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda2;-><init>(Lmiuix/animation/internal/AnimScheduler;)V

    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    return-void

    :cond_2
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "executeUpdate warning!! this scheduler has no handler"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/16 v1, 0x8

    invoke-static {v1}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "miuix_anim"

    invoke-static {v1, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Lmiuix/animation/internal/AnimScheduler;->update()V

    return-void
.end method""",
        'replacement': """.method executeUpdate()V
    .registers 3

    goto :goto_13

    nop

    :goto_0
    return-void

    :goto_1
    goto :goto_10

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_18

    :cond_0
    goto :goto_e

    nop

    :goto_3
    invoke-direct {v1, p0}, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda2;-><init>(Lmiuix/animation/internal/AnimScheduler;)V

    goto :goto_1b

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    goto :goto_1f

    nop

    :goto_5
    const-string v1, "executeUpdate warning!! this scheduler has no handler"

    goto :goto_12

    nop

    :goto_6
    const-string v1, "-- executeUpdate"

    goto :goto_a

    nop

    :goto_7
    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    goto :goto_9

    nop

    :goto_8
    if-nez v0, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_15

    nop

    :goto_9
    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result v0

    goto :goto_2

    nop

    :goto_a
    invoke-static {v1, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_b
    goto :goto_1d

    nop

    :goto_c
    invoke-virtual {p0}, Lmiuix/animation/internal/AnimScheduler;->update()V

    goto :goto_19

    nop

    :goto_d
    new-array v0, v0, [Ljava/lang/Object;

    goto :goto_6

    nop

    :goto_e
    invoke-virtual {p0}, Lmiuix/animation/internal/AnimScheduler;->update()V

    goto :goto_17

    nop

    :goto_f
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1c

    nop

    :goto_10
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_1e

    nop

    :goto_11
    const/16 v1, 0x8

    goto :goto_16

    nop

    :goto_12
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_11

    nop

    :goto_13
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result v0

    goto :goto_8

    nop

    :goto_14
    const-string v1, "miuix_anim"

    goto :goto_20

    nop

    :goto_15
    const/4 v0, 0x0

    goto :goto_d

    nop

    :goto_16
    invoke-static {v1}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v1

    goto :goto_f

    nop

    :goto_17
    return-void

    :goto_18
    goto :goto_4

    nop

    :goto_19
    return-void

    :goto_1a
    new-instance v1, Lmiuix/animation/internal/AnimScheduler$$ExternalSyntheticLambda2;

    goto :goto_3

    nop

    :goto_1b
    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    goto :goto_0

    nop

    :goto_1c
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_14

    nop

    :goto_1d
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_7

    nop

    :goto_1e
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_5

    nop

    :goto_1f
    if-nez v0, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_1a

    nop

    :goto_20
    invoke-static {v1, v0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__execute',
        'method': '.method final execute(Ljava/lang/Runnable;)V',
        'method_name': 'execute',
        'method_anchors': ['invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;', 'invoke-virtual {v0}, Ljava/lang/Thread;->getId()J', 'invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z', 'if-eqz v0, :cond_0', 'invoke-interface {p1}, Ljava/lang/Runnable;->run()V', 'return-void', 'iget-object p0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;', 'if-eqz p0, :cond_1'],
        'type': 'method_replace',
        'search': """.method final execute(Ljava/lang/Runnable;)V
    .registers 4

    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-interface {p1}, Ljava/lang/Runnable;->run()V

    return-void

    :cond_0
    iget-object p0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    if-eqz p0, :cond_1

    invoke-virtual {p0, p1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    return-void

    :cond_1
    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "execute warning!! this scheduler has no handler"

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/16 v0, 0x8

    invoke-static {v0}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string v0, "miuix_anim"

    invoke-static {v0, p0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    invoke-interface {p1}, Ljava/lang/Runnable;->run()V

    return-void
.end method""",
        'replacement': """.method final execute(Ljava/lang/Runnable;)V
    .registers 4

    goto :goto_16

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_d

    nop

    :goto_1
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_a

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_12

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/animation/internal/AnimScheduler;->handler:Landroid/os/Handler;

    goto :goto_f

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_e

    nop

    :goto_7
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_17

    nop

    :goto_8
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1

    nop

    :goto_9
    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/AnimScheduler;->isInMainThread(J)Z

    move-result v0

    goto :goto_0

    nop

    :goto_a
    const-string v0, "miuix_anim"

    goto :goto_14

    nop

    :goto_b
    invoke-virtual {p0, p1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    goto :goto_5

    nop

    :goto_c
    invoke-static {v0}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v0

    goto :goto_8

    nop

    :goto_d
    invoke-interface {p1}, Ljava/lang/Runnable;->run()V

    goto :goto_10

    nop

    :goto_e
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_f
    if-nez p0, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_b

    nop

    :goto_10
    return-void

    :goto_11
    goto :goto_4

    nop

    :goto_12
    const/16 v0, 0x8

    goto :goto_c

    nop

    :goto_13
    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    goto :goto_9

    nop

    :goto_14
    invoke-static {v0, p0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_15

    nop

    :goto_15
    invoke-interface {p1}, Ljava/lang/Runnable;->run()V

    goto :goto_2

    nop

    :goto_16
    invoke-static {}, Ljava/lang/Thread;->currentThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_13

    nop

    :goto_17
    const-string v0, "execute warning!! this scheduler has no handler"

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__getTotalRunningTransitionCount',
        'method': '.method getTotalRunningTransitionCount()I',
        'method_name': 'getTotalRunningTransitionCount',
        'method_anchors': ['new-instance v0, Ljava/util/HashSet;', 'iget-object p0, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;', 'invoke-direct {v0, p0}, Ljava/util/HashSet;-><init>(Ljava/util/Collection;)V', 'invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;', 'invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_0', 'invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v1, Lmiuix/animation/IAnimTarget;'],
        'type': 'method_replace',
        'search': """.method getTotalRunningTransitionCount()I
    .registers 3

    new-instance v0, Ljava/util/HashSet;

    iget-object p0, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    invoke-direct {v0, p0}, Ljava/util/HashSet;-><init>(Ljava/util/Collection;)V

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p0

    const/4 v0, 0x0

    :goto_0
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/animation/IAnimTarget;

    iget-object v1, v1, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    invoke-virtual {v1}, Lmiuix/animation/internal/AnimManager;->getRunningTransitionCount()I

    move-result v1

    add-int/2addr v0, v1

    goto :goto_0

    :cond_0
    return v0
.end method""",
        'replacement': """.method getTotalRunningTransitionCount()I
    .registers 3

    goto :goto_b

    nop

    :goto_0
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_6

    nop

    :goto_1
    invoke-direct {v0, p0}, Ljava/util/HashSet;-><init>(Ljava/util/Collection;)V

    goto :goto_7

    nop

    :goto_2
    const/4 v0, 0x0

    :goto_3
    goto :goto_0

    nop

    :goto_4
    goto :goto_3

    :goto_5
    goto :goto_f

    nop

    :goto_6
    if-nez v1, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_d

    nop

    :goto_7
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p0

    goto :goto_2

    nop

    :goto_8
    add-int/2addr v0, v1

    goto :goto_4

    nop

    :goto_9
    iget-object v1, v1, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    goto :goto_e

    nop

    :goto_a
    check-cast v1, Lmiuix/animation/IAnimTarget;

    goto :goto_9

    nop

    :goto_b
    new-instance v0, Ljava/util/HashSet;

    goto :goto_c

    nop

    :goto_c
    iget-object p0, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    goto :goto_1

    nop

    :goto_d
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_a

    nop

    :goto_e
    invoke-virtual {v1}, Lmiuix/animation/internal/AnimManager;->getRunningTransitionCount()I

    move-result v1

    goto :goto_8

    nop

    :goto_f
    return v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__doAnimationFrame',
        'method': '.method protected final doAnimationFrame(JJ)V',
        'method_name': 'doAnimationFrame',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z', 'invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'if-eqz v1, :cond_0', 'invoke-static {p3, p4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;', 'invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I', 'invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'const-string v3, "++ doAnimationFrame: deltaTNanos=%d Scheduler@%s"', 'invoke-static {v3, v1}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected final doAnimationFrame(JJ)V
    .registers 15

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v1

    const/4 v2, 0x0

    if-eqz v1, :cond_0

    invoke-static {p3, p4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v1

    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result v3

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    filled-new-array {v1, v3}, [Ljava/lang/Object;

    move-result-object v1

    const-string v3, "++ doAnimationFrame: deltaTNanos=%d Scheduler@%s"

    invoke-static {v3, v1}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    new-array v3, v2, [Ljava/lang/Object;

    invoke-static {v1, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    invoke-direct {p0}, Lmiuix/animation/internal/AnimScheduler;->setup()V

    if-eqz v0, :cond_1

    iget-object v1, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    invoke-interface {v1}, Ljava/util/Set;->size()I

    move-result v1

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v1

    const-string v3, "++ doAnimationFrame: |-> after setup: mRunningTarget.size=%s"

    invoke-static {v3, v1}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    new-array v3, v2, [Ljava/lang/Object;

    invoke-static {v1, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    iget-object v1, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    invoke-interface {v1}, Ljava/util/Set;->isEmpty()Z

    move-result v1

    if-nez v1, :cond_4

    invoke-static {}, Lmiuix/animation/internal/AndroidEngine;->getInst()Lmiuix/animation/internal/AndroidEngine;

    move-result-object v1

    invoke-virtual {v1}, Lmiuix/animation/internal/FolmeEngine;->getAverageDeltaNanos()J

    move-result-wide v8

    if-eqz v0, :cond_2

    iget-boolean v0, p0, Lmiuix/animation/internal/AnimScheduler;->mStart:Z

    invoke-static {v0}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v0

    iget-boolean v1, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    invoke-static {v1}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v1

    filled-new-array {v0, v1}, [Ljava/lang/Object;

    move-result-object v0

    const-string v1, "++ doAnimationFrame: |--> hasRunningTarget mStart=%s mHasTaskStackRunning=%s "

    invoke-static {v1, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    new-array v1, v2, [Ljava/lang/Object;

    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_2
    iget-boolean v0, p0, Lmiuix/animation/internal/AnimScheduler;->mStart:Z

    if-nez v0, :cond_3

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/animation/internal/AnimScheduler;->mStart:Z

    const-wide/16 v0, 0x0

    iput-wide v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J

    iput v2, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I

    :cond_3
    move-object v3, p0

    move-wide v4, p1

    move-wide v6, p3

    invoke-virtual/range {v3 .. v9}, Lmiuix/animation/internal/AnimScheduler;->runAnimTaskOnFrame(JJJ)V

    goto :goto_0

    :cond_4
    move-object v3, p0

    :goto_0
    invoke-direct {v3}, Lmiuix/animation/internal/AnimScheduler;->releaseIdleOneShotTargetAfterRun()V

    return-void
.end method""",
        'replacement': """.method protected final doAnimationFrame(JJ)V
    .registers 15

    goto :goto_38

    nop

    :goto_0
    invoke-direct {p0}, Lmiuix/animation/internal/AnimScheduler;->setup()V

    goto :goto_1c

    nop

    :goto_1
    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    goto :goto_18

    nop

    :goto_2
    goto :goto_f

    :goto_3
    goto :goto_e

    nop

    :goto_4
    iget-object v1, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    goto :goto_29

    nop

    :goto_5
    invoke-static {v3, v1}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    goto :goto_2c

    nop

    :goto_6
    const-string v1, "++ doAnimationFrame: |--> hasRunningTarget mStart=%s mHasTaskStackRunning=%s "

    goto :goto_25

    nop

    :goto_7
    iget-boolean v0, p0, Lmiuix/animation/internal/AnimScheduler;->mStart:Z

    goto :goto_21

    nop

    :goto_8
    if-eqz v1, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_16

    nop

    :goto_9
    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_31

    nop

    :goto_a
    iput v2, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I

    :goto_b
    goto :goto_1a

    nop

    :goto_c
    invoke-static {v1, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_d
    goto :goto_0

    nop

    :goto_e
    move-object v3, p0

    :goto_f
    goto :goto_37

    nop

    :goto_10
    const-wide/16 v0, 0x0

    goto :goto_2d

    nop

    :goto_11
    invoke-static {v1, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_12
    goto :goto_15

    nop

    :goto_13
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v1

    goto :goto_28

    nop

    :goto_14
    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result v3

    goto :goto_1

    nop

    :goto_15
    iget-object v1, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    goto :goto_27

    nop

    :goto_16
    invoke-static {}, Lmiuix/animation/internal/AndroidEngine;->getInst()Lmiuix/animation/internal/AndroidEngine;

    move-result-object v1

    goto :goto_1f

    nop

    :goto_17
    iput-boolean v0, p0, Lmiuix/animation/internal/AnimScheduler;->mStart:Z

    goto :goto_10

    nop

    :goto_18
    filled-new-array {v1, v3}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_2a

    nop

    :goto_19
    invoke-static {v3, v1}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    goto :goto_23

    nop

    :goto_1a
    move-object v3, p0

    goto :goto_2f

    nop

    :goto_1b
    invoke-static {v1}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v1

    goto :goto_20

    nop

    :goto_1c
    if-nez v0, :cond_1

    goto :goto_12

    :cond_1
    goto :goto_4

    nop

    :goto_1d
    if-nez v0, :cond_2

    goto :goto_34

    :cond_2
    goto :goto_30

    nop

    :goto_1e
    const/4 v0, 0x1

    goto :goto_17

    nop

    :goto_1f
    invoke-virtual {v1}, Lmiuix/animation/internal/FolmeEngine;->getAverageDeltaNanos()J

    move-result-wide v8

    goto :goto_1d

    nop

    :goto_20
    filled-new-array {v0, v1}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_6

    nop

    :goto_21
    if-eqz v0, :cond_3

    goto :goto_b

    :cond_3
    goto :goto_1e

    nop

    :goto_22
    move-wide v6, p3

    goto :goto_36

    nop

    :goto_23
    new-array v3, v2, [Ljava/lang/Object;

    goto :goto_c

    nop

    :goto_24
    if-nez v1, :cond_4

    goto :goto_d

    :cond_4
    goto :goto_26

    nop

    :goto_25
    invoke-static {v1, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    goto :goto_39

    nop

    :goto_26
    invoke-static {p3, p4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v1

    goto :goto_14

    nop

    :goto_27
    invoke-interface {v1}, Ljava/util/Set;->isEmpty()Z

    move-result v1

    goto :goto_8

    nop

    :goto_28
    const/4 v2, 0x0

    goto :goto_24

    nop

    :goto_29
    invoke-interface {v1}, Ljava/util/Set;->size()I

    move-result v1

    goto :goto_2e

    nop

    :goto_2a
    const-string v3, "++ doAnimationFrame: deltaTNanos=%d Scheduler@%s"

    goto :goto_19

    nop

    :goto_2b
    return-void

    :goto_2c
    new-array v3, v2, [Ljava/lang/Object;

    goto :goto_11

    nop

    :goto_2d
    iput-wide v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J

    goto :goto_a

    nop

    :goto_2e
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_9

    nop

    :goto_2f
    move-wide v4, p1

    goto :goto_22

    nop

    :goto_30
    iget-boolean v0, p0, Lmiuix/animation/internal/AnimScheduler;->mStart:Z

    goto :goto_35

    nop

    :goto_31
    const-string v3, "++ doAnimationFrame: |-> after setup: mRunningTarget.size=%s"

    goto :goto_5

    nop

    :goto_32
    iget-boolean v1, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    goto :goto_1b

    nop

    :goto_33
    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_34
    goto :goto_7

    nop

    :goto_35
    invoke-static {v0}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v0

    goto :goto_32

    nop

    :goto_36
    invoke-virtual/range {v3 .. v9}, Lmiuix/animation/internal/AnimScheduler;->runAnimTaskOnFrame(JJJ)V

    goto :goto_2

    nop

    :goto_37
    invoke-direct {v3}, Lmiuix/animation/internal/AnimScheduler;->releaseIdleOneShotTargetAfterRun()V

    goto :goto_2b

    nop

    :goto_38
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    goto :goto_13

    nop

    :goto_39
    new-array v1, v2, [Ljava/lang/Object;

    goto :goto_33

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__isInMainThread',
        'method': '.method protected final isInMainThread(J)Z',
        'method_name': 'isInMainThread',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/animation/internal/AnimScheduler;->runnerThreadId:J', 'if-nez p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected final isInMainThread(J)Z
    .registers 5

    iget-wide v0, p0, Lmiuix/animation/internal/AnimScheduler;->runnerThreadId:J

    cmp-long p0, v0, p1

    if-nez p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected final isInMainThread(J)Z
    .registers 5

    goto :goto_0

    nop

    :goto_0
    iget-wide v0, p0, Lmiuix/animation/internal/AnimScheduler;->runnerThreadId:J

    goto :goto_6

    nop

    :goto_1
    return p0

    :goto_2
    goto :goto_4

    nop

    :goto_3
    const/4 p0, 0x1

    goto :goto_1

    nop

    :goto_4
    const/4 p0, 0x0

    goto :goto_7

    nop

    :goto_5
    if-eqz p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_3

    nop

    :goto_6
    cmp-long p0, v0, p1

    goto :goto_5

    nop

    :goto_7
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__notifyTransitionBegin',
        'method': '.method protected final notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'notifyTransitionBegin',
        'method_anchors': ['iget-object p0, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;', 'iget-object p0, p0, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;', 'iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;', 'invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected final notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 4

    iget-object p0, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    iget-object p0, p0, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    const/4 v1, 0x0

    invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V

    return-void
.end method""",
        'replacement': """.method protected final notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 4

    goto :goto_4

    nop

    :goto_0
    return-void

    :goto_1
    const/4 v1, 0x0

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V

    goto :goto_0

    nop

    :goto_3
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    goto :goto_1

    nop

    :goto_4
    iget-object p0, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    goto :goto_5

    nop

    :goto_5
    iget-object p0, p0, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__pendingSetTo',
        'method': '.method protected final pendingSetTo(Lmiuix/animation/internal/AnimScheduler$SetToInfo;)V',
        'method_name': 'pendingSetTo',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'iget-object v1, p1, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->target:Lmiuix/animation/IAnimTarget;', 'const-string v2, " "', 'if-eqz v0, :cond_0', 'new-instance v4, Ljava/lang/StringBuilder;', 'invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v5, "-- setTo Scheduler@"', 'invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method protected final pendingSetTo(Lmiuix/animation/internal/AnimScheduler$SetToInfo;)V
    .registers 12
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    iget-object v1, p1, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->target:Lmiuix/animation/IAnimTarget;

    const-string v2, " "

    const/4 v3, 0x0

    if-eqz v0, :cond_0

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "-- setTo Scheduler@"

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result p0

    invoke-virtual {v4, p0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    new-array v4, v3, [Ljava/lang/Object;

    invoke-static {p0, v4}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    iget-object p0, p1, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->state:Lmiuix/animation/controller/AnimState;

    iget-object p1, p1, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->target:Lmiuix/animation/IAnimTarget;

    iget-object p1, p1, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    const/4 v4, 0x0

    invoke-virtual {p1, p0, v4}, Lmiuix/animation/internal/AnimManager;->setTo(Lmiuix/animation/controller/AnimState;Lmiuix/animation/base/AnimConfigLink;)Z

    invoke-virtual {p0}, Lmiuix/animation/controller/AnimState;->keySet()Ljava/util/Set;

    move-result-object p1

    invoke-interface {p1}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p1

    :goto_0
    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    move-result v4

    if-eqz v4, :cond_5

    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v4

    invoke-virtual {p0, v1, v4}, Lmiuix/animation/controller/AnimState;->getProperty(Lmiuix/animation/IAnimTarget;Ljava/lang/Object;)Lmiuix/animation/property/FloatProperty;

    move-result-object v4

    iget-object v5, v1, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    iget-object v5, v5, Lmiuix/animation/internal/AnimManager;->mUpdateMap:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {v5, v4}, Ljava/util/concurrent/ConcurrentHashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Lmiuix/animation/listener/UpdateInfo;

    if-nez v5, :cond_1

    goto :goto_0

    :cond_1
    invoke-virtual {p0, v1, v4}, Lmiuix/animation/controller/AnimState;->get(Lmiuix/animation/IAnimTarget;Lmiuix/animation/property/FloatProperty;)D

    move-result-wide v6

    if-eqz v0, :cond_2

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v9, "-- setTo setToValue="

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v6, v7}, Ljava/lang/StringBuilder;->append(D)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    const-string v9, " toState "

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    new-array v9, v3, [Ljava/lang/Object;

    invoke-static {v8, v9}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_2
    iget-object v8, v5, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    iput-wide v6, v8, Lmiuix/animation/internal/AnimInfo;->startValue:D

    iput-wide v6, v8, Lmiuix/animation/internal/AnimInfo;->setToValue:D

    iget-boolean v6, v5, Lmiuix/animation/listener/UpdateInfo;->useInt:Z

    if-eqz v6, :cond_3

    instance-of v7, v4, Lmiuix/animation/property/IIntValueProperty;

    if-eqz v7, :cond_3

    check-cast v4, Lmiuix/animation/property/IIntValueProperty;

    invoke-virtual {v5}, Lmiuix/animation/listener/UpdateInfo;->getIntValue()I

    move-result v5

    invoke-virtual {v1, v4, v5}, Lmiuix/animation/IAnimTarget;->doSetIntValue(Lmiuix/animation/property/IIntValueProperty;I)V

    goto :goto_0

    :cond_3
    if-eqz v6, :cond_4

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "-- setTo Warning!! the property is "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    new-array v7, v3, [Ljava/lang/Object;

    invoke-static {v6, v7}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_4
    invoke-virtual {v5}, Lmiuix/animation/listener/UpdateInfo;->getFloatValue()F

    move-result v5

    invoke-virtual {v1, v4, v5}, Lmiuix/animation/IAnimTarget;->doSetValue(Lmiuix/animation/property/FloatProperty;F)V

    goto :goto_0

    :cond_5
    if-eqz v0, :cond_6

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string p1, "-- setTo done "

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    new-array p1, v3, [Ljava/lang/Object;

    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_6
    return-void
.end method""",
        'replacement': """.method protected final pendingSetTo(Lmiuix/animation/internal/AnimScheduler$SetToInfo;)V
    .registers 12
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    goto :goto_30

    nop

    :goto_0
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_47

    nop

    :goto_1
    invoke-virtual {p0, v1, v4}, Lmiuix/animation/controller/AnimState;->getProperty(Lmiuix/animation/IAnimTarget;Ljava/lang/Object;)Lmiuix/animation/property/FloatProperty;

    move-result-object v4

    goto :goto_4a

    nop

    :goto_2
    invoke-virtual {v8, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_a

    nop

    :goto_3
    if-nez v4, :cond_0

    goto :goto_24

    :cond_0
    goto :goto_34

    nop

    :goto_4
    invoke-virtual {p0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_3f

    nop

    :goto_5
    iget-object p1, p1, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    goto :goto_2b

    nop

    :goto_6
    iget-object v1, p1, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->target:Lmiuix/animation/IAnimTarget;

    goto :goto_1f

    nop

    :goto_7
    const-string v9, " toState "

    goto :goto_15

    nop

    :goto_8
    check-cast v4, Lmiuix/animation/property/IIntValueProperty;

    goto :goto_3c

    nop

    :goto_9
    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result p0

    goto :goto_39

    nop

    :goto_a
    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    goto :goto_14

    nop

    :goto_b
    iget-object p1, p1, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->target:Lmiuix/animation/IAnimTarget;

    goto :goto_5

    nop

    :goto_c
    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_41

    nop

    :goto_d
    iput-wide v6, v8, Lmiuix/animation/internal/AnimInfo;->startValue:D

    goto :goto_55

    nop

    :goto_e
    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_35

    nop

    :goto_f
    new-array v4, v3, [Ljava/lang/Object;

    goto :goto_45

    nop

    :goto_10
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_5a

    nop

    :goto_11
    instance-of v7, v4, Lmiuix/animation/property/IIntValueProperty;

    goto :goto_28

    nop

    :goto_12
    iget-object v8, v5, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    goto :goto_d

    nop

    :goto_13
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_f

    nop

    :goto_14
    new-array v9, v3, [Ljava/lang/Object;

    goto :goto_4c

    nop

    :goto_15
    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2

    nop

    :goto_16
    invoke-virtual {v1, v4, v5}, Lmiuix/animation/IAnimTarget;->doSetIntValue(Lmiuix/animation/property/IIntValueProperty;I)V

    goto :goto_2d

    nop

    :goto_17
    invoke-virtual {p0, v1, v4}, Lmiuix/animation/controller/AnimState;->get(Lmiuix/animation/IAnimTarget;Lmiuix/animation/property/FloatProperty;)D

    move-result-wide v6

    goto :goto_18

    nop

    :goto_18
    if-nez v0, :cond_1

    goto :goto_4d

    :cond_1
    goto :goto_3b

    nop

    :goto_19
    invoke-interface {p1}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object p1

    :goto_1a
    goto :goto_59

    nop

    :goto_1b
    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_13

    nop

    :goto_1c
    const/4 v3, 0x0

    goto :goto_51

    nop

    :goto_1d
    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_3d

    nop

    :goto_1e
    new-instance v4, Ljava/lang/StringBuilder;

    goto :goto_10

    nop

    :goto_1f
    const-string v2, " "

    goto :goto_1c

    nop

    :goto_20
    check-cast v5, Lmiuix/animation/listener/UpdateInfo;

    goto :goto_53

    nop

    :goto_21
    invoke-virtual {v5}, Lmiuix/animation/listener/UpdateInfo;->getFloatValue()F

    move-result v5

    goto :goto_3e

    nop

    :goto_22
    if-nez v6, :cond_2

    goto :goto_2e

    :cond_2
    goto :goto_11

    nop

    :goto_23
    goto :goto_1a

    :goto_24
    goto :goto_25

    nop

    :goto_25
    if-nez v0, :cond_3

    goto :goto_32

    :cond_3
    goto :goto_0

    nop

    :goto_26
    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_2c

    nop

    :goto_27
    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    goto :goto_52

    nop

    :goto_28
    if-nez v7, :cond_4

    goto :goto_2e

    :cond_4
    goto :goto_8

    nop

    :goto_29
    goto :goto_1a

    :goto_2a
    goto :goto_17

    nop

    :goto_2b
    const/4 v4, 0x0

    goto :goto_3a

    nop

    :goto_2c
    const-string v9, "-- setTo setToValue="

    goto :goto_e

    nop

    :goto_2d
    goto :goto_1a

    :goto_2e
    goto :goto_50

    nop

    :goto_2f
    iget-boolean v6, v5, Lmiuix/animation/listener/UpdateInfo;->useInt:Z

    goto :goto_22

    nop

    :goto_30
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_6

    nop

    :goto_31
    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_32
    goto :goto_42

    nop

    :goto_33
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_34
    invoke-interface {p1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v4

    goto :goto_1

    nop

    :goto_35
    invoke-virtual {v8, v6, v7}, Ljava/lang/StringBuilder;->append(D)Ljava/lang/StringBuilder;

    goto :goto_48

    nop

    :goto_36
    invoke-static {v6, v7}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_37
    goto :goto_21

    nop

    :goto_38
    invoke-virtual {p0}, Lmiuix/animation/controller/AnimState;->keySet()Ljava/util/Set;

    move-result-object p1

    goto :goto_19

    nop

    :goto_39
    invoke-virtual {v4, p0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_c

    nop

    :goto_3a
    invoke-virtual {p1, p0, v4}, Lmiuix/animation/internal/AnimManager;->setTo(Lmiuix/animation/controller/AnimState;Lmiuix/animation/base/AnimConfigLink;)Z

    goto :goto_38

    nop

    :goto_3b
    new-instance v8, Ljava/lang/StringBuilder;

    goto :goto_26

    nop

    :goto_3c
    invoke-virtual {v5}, Lmiuix/animation/listener/UpdateInfo;->getIntValue()I

    move-result v5

    goto :goto_16

    nop

    :goto_3d
    const-string v7, "-- setTo Warning!! the property is "

    goto :goto_4e

    nop

    :goto_3e
    invoke-virtual {v1, v4, v5}, Lmiuix/animation/IAnimTarget;->doSetValue(Lmiuix/animation/property/FloatProperty;F)V

    goto :goto_23

    nop

    :goto_3f
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_4b

    nop

    :goto_40
    invoke-virtual {v5, v4}, Ljava/util/concurrent/ConcurrentHashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v5

    goto :goto_20

    nop

    :goto_41
    invoke-virtual {v4, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_44

    nop

    :goto_42
    return-void

    :goto_43
    iget-object p0, p1, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->state:Lmiuix/animation/controller/AnimState;

    goto :goto_b

    nop

    :goto_44
    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1b

    nop

    :goto_45
    invoke-static {p0, v4}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_46
    goto :goto_43

    nop

    :goto_47
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_58

    nop

    :goto_48
    invoke-virtual {v8, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_54

    nop

    :goto_49
    iget-object v5, v5, Lmiuix/animation/internal/AnimManager;->mUpdateMap:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_40

    nop

    :goto_4a
    iget-object v5, v1, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    goto :goto_49

    nop

    :goto_4b
    new-array p1, v3, [Ljava/lang/Object;

    goto :goto_31

    nop

    :goto_4c
    invoke-static {v8, v9}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_4d
    goto :goto_12

    nop

    :goto_4e
    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_57

    nop

    :goto_4f
    new-instance v6, Ljava/lang/StringBuilder;

    goto :goto_1d

    nop

    :goto_50
    if-nez v6, :cond_5

    goto :goto_37

    :cond_5
    goto :goto_4f

    nop

    :goto_51
    if-nez v0, :cond_6

    goto :goto_46

    :cond_6
    goto :goto_1e

    nop

    :goto_52
    new-array v7, v3, [Ljava/lang/Object;

    goto :goto_36

    nop

    :goto_53
    if-eqz v5, :cond_7

    goto :goto_2a

    :cond_7
    goto :goto_29

    nop

    :goto_54
    invoke-virtual {v8, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_55
    iput-wide v6, v8, Lmiuix/animation/internal/AnimInfo;->setToValue:D

    goto :goto_2f

    nop

    :goto_56
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_57
    invoke-virtual {v6, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_27

    nop

    :goto_58
    const-string p1, "-- setTo done "

    goto :goto_33

    nop

    :goto_59
    invoke-interface {p1}, Ljava/util/Iterator;->hasNext()Z

    move-result v4

    goto :goto_3

    nop

    :goto_5a
    const-string v5, "-- setTo Scheduler@"

    goto :goto_56

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__to',
        'method': '.method protected final to(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'to',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'if-eqz v0, :cond_0', 'new-instance v2, Ljava/lang/StringBuilder;', 'invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v3, "-- to Scheduler@"', 'invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I', 'invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method protected final to(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 6

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "-- to Scheduler@"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v3, " "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    new-array v3, v1, [Ljava/lang/Object;

    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    if-eqz p1, :cond_2

    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mPrepareTransMap:Ljava/util/Map;

    invoke-direct {p0, v2, p1, v3}, Lmiuix/animation/internal/AnimScheduler;->addToMap(Lmiuix/animation/IAnimTarget;Lmiuix/animation/utils/LinkNode;Ljava/util/Map;)V

    iget-boolean p1, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    if-nez p1, :cond_2

    if-eqz v0, :cond_1

    const-string p1, "-- to->startEngine"

    new-array v0, v1, [Ljava/lang/Object;

    invoke-static {p1, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    invoke-direct {p0}, Lmiuix/animation/internal/AnimScheduler;->startEngine()V

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected final to(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 6

    goto :goto_b

    nop

    :goto_0
    const-string v3, " "

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_19

    nop

    :goto_2
    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_3
    goto :goto_13

    nop

    :goto_4
    const-string v3, "-- to Scheduler@"

    goto :goto_10

    nop

    :goto_5
    new-array v3, v1, [Ljava/lang/Object;

    goto :goto_2

    nop

    :goto_6
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_7
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_1c

    nop

    :goto_8
    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result v3

    goto :goto_6

    nop

    :goto_9
    invoke-direct {p0}, Lmiuix/animation/internal/AnimScheduler;->startEngine()V

    :goto_a
    goto :goto_c

    nop

    :goto_b
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_14

    nop

    :goto_c
    return-void

    :goto_d
    invoke-static {p1, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_e
    goto :goto_9

    nop

    :goto_f
    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mPrepareTransMap:Ljava/util/Map;

    goto :goto_12

    nop

    :goto_10
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_8

    nop

    :goto_11
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_5

    nop

    :goto_12
    invoke-direct {p0, v2, p1, v3}, Lmiuix/animation/internal/AnimScheduler;->addToMap(Lmiuix/animation/IAnimTarget;Lmiuix/animation/utils/LinkNode;Ljava/util/Map;)V

    goto :goto_1d

    nop

    :goto_13
    if-nez p1, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_1b

    nop

    :goto_14
    const/4 v1, 0x0

    goto :goto_16

    nop

    :goto_15
    new-array v0, v1, [Ljava/lang/Object;

    goto :goto_d

    nop

    :goto_16
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_7

    nop

    :goto_17
    const-string p1, "-- to->startEngine"

    goto :goto_15

    nop

    :goto_18
    if-eqz p1, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_1a

    nop

    :goto_19
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_11

    nop

    :goto_1a
    if-nez v0, :cond_3

    goto :goto_e

    :cond_3
    goto :goto_17

    nop

    :goto_1b
    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    goto :goto_f

    nop

    :goto_1c
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_4

    nop

    :goto_1d
    iget-boolean p1, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    goto :goto_18

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__update',
        'method': '.method protected final update()V',
        'method_name': 'update',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z', 'if-eqz v0, :cond_0', 'new-instance v2, Ljava/lang/StringBuilder;', 'invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v3, "-- update from runningStackCount == 0 frameCount="', 'invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'iget v3, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I', 'invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method protected final update()V
    .registers 9

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "-- update from runningStackCount == 0 frameCount="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v3, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v3, " Scheduler@"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    new-array v3, v1, [Ljava/lang/Object;

    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    iput v1, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    new-instance v2, Ljava/util/HashSet;

    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    invoke-direct {v2, v3}, Ljava/util/HashSet;-><init>(Ljava/util/Collection;)V

    invoke-interface {v2}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    move v3, v1

    :cond_1
    :goto_0
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v4

    const/4 v5, 0x1

    if-eqz v4, :cond_4

    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v4

    check-cast v4, Lmiuix/animation/IAnimTarget;

    iget-object v6, p0, Lmiuix/animation/internal/AnimScheduler;->mTempTargetRunningInfo:Ljava/util/List;

    invoke-direct {p0, v4, v6}, Lmiuix/animation/internal/AnimScheduler;->updateTarget(Lmiuix/animation/IAnimTarget;Ljava/util/List;)Z

    move-result v6

    if-nez v6, :cond_3

    invoke-direct {p0, v4}, Lmiuix/animation/internal/AnimScheduler;->prepareWaitTransAfterUpdated(Lmiuix/animation/IAnimTarget;)Z

    move-result v6

    if-eqz v6, :cond_2

    goto :goto_1

    :cond_2
    iget-object v5, p0, Lmiuix/animation/internal/AnimScheduler;->mPreDelTargetList:Ljava/util/List;

    invoke-interface {v5, v4}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_2

    :cond_3
    :goto_1
    move v3, v5

    :goto_2
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v5

    if-eqz v5, :cond_1

    iget v5, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    iget-object v4, v4, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    invoke-virtual {v4}, Lmiuix/animation/internal/AnimManager;->getTotalAnimCount()I

    move-result v4

    add-int/2addr v5, v4

    iput v5, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    goto :goto_0

    :cond_4
    iput-boolean v1, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mPreDelTargetList:Ljava/util/List;

    invoke-interface {v2}, Ljava/util/List;->isEmpty()Z

    move-result v2

    if-nez v2, :cond_5

    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    iget-object v4, p0, Lmiuix/animation/internal/AnimScheduler;->mPreDelTargetList:Ljava/util/List;

    invoke-interface {v2, v4}, Ljava/util/Set;->removeAll(Ljava/util/Collection;)Z

    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mPreDelTargetList:Ljava/util/List;

    invoke-interface {v2}, Ljava/util/List;->clear()V

    :cond_5
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v2

    if-eqz v2, :cond_6

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "mRunningAnimCount="

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v4, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "mPrepareTransMap.size="

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v6, p0, Lmiuix/animation/internal/AnimScheduler;->mPrepareTransMap:Ljava/util/Map;

    invoke-interface {v6}, Ljava/util/Map;->size()I

    move-result v6

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "mRunningTarget.size="

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v7, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    invoke-interface {v7}, Ljava/util/Set;->size()I

    move-result v7

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    filled-new-array {v2, v4, v6}, [Ljava/lang/Object;

    move-result-object v2

    const-string v4, "-- update after traversal all target"

    invoke-static {v4, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_6
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mPrepareTransMap:Ljava/util/Map;

    invoke-interface {v2}, Ljava/util/Map;->isEmpty()Z

    move-result v2

    xor-int/lit8 v4, v2, 0x1

    iget-object v6, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    invoke-interface {v6}, Ljava/util/Set;->isEmpty()Z

    move-result v6

    xor-int/lit8 v7, v6, 0x1

    if-eqz v2, :cond_7

    if-nez v6, :cond_9

    :cond_7
    if-eqz v0, :cond_8

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "-- update finish->startEngine hasPrepareTrans:"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v3, " hasRunningTarget:"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v7}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    new-array v3, v1, [Ljava/lang/Object;

    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_8
    invoke-direct {p0}, Lmiuix/animation/internal/AnimScheduler;->startEngine()V

    move v3, v5

    :cond_9
    if-nez v3, :cond_b

    if-eqz v0, :cond_a

    const-string v0, "-- update->endEngine when isRunning is false"

    new-array v1, v1, [Ljava/lang/Object;

    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_a
    invoke-direct {p0}, Lmiuix/animation/internal/AnimScheduler;->endEngine()V

    :cond_b
    return-void
.end method""",
        'replacement': """.method protected final update()V
    .registers 9

    goto :goto_2a

    nop

    :goto_0
    const-string v3, "-- update from runningStackCount == 0 frameCount="

    goto :goto_c

    nop

    :goto_1
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mPreDelTargetList:Ljava/util/List;

    goto :goto_b

    nop

    :goto_2
    add-int/2addr v5, v4

    goto :goto_43

    nop

    :goto_3
    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_26

    nop

    :goto_4
    goto :goto_37

    :goto_5
    goto :goto_36

    nop

    :goto_6
    iget-object v5, p0, Lmiuix/animation/internal/AnimScheduler;->mPreDelTargetList:Ljava/util/List;

    goto :goto_29

    nop

    :goto_7
    if-eqz v2, :cond_0

    goto :goto_4d

    :cond_0
    goto :goto_6e

    nop

    :goto_8
    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_9
    goto :goto_27

    nop

    :goto_a
    if-nez v5, :cond_1

    goto :goto_4b

    :cond_1
    goto :goto_57

    nop

    :goto_b
    invoke-interface {v2}, Ljava/util/List;->isEmpty()Z

    move-result v2

    goto :goto_7

    nop

    :goto_c
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_56

    nop

    :goto_d
    invoke-direct {p0, v4}, Lmiuix/animation/internal/AnimScheduler;->prepareWaitTransAfterUpdated(Lmiuix/animation/IAnimTarget;)Z

    move-result v6

    goto :goto_34

    nop

    :goto_e
    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_17

    nop

    :goto_f
    invoke-interface {v2}, Ljava/util/Map;->isEmpty()Z

    move-result v2

    goto :goto_11

    nop

    :goto_10
    invoke-interface {v6}, Ljava/util/Map;->size()I

    move-result v6

    goto :goto_44

    nop

    :goto_11
    xor-int/lit8 v4, v2, 0x1

    goto :goto_28

    nop

    :goto_12
    if-eqz v6, :cond_2

    goto :goto_5

    :cond_2
    goto :goto_d

    nop

    :goto_13
    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result v3

    goto :goto_31

    nop

    :goto_14
    xor-int/lit8 v7, v6, 0x1

    goto :goto_4f

    nop

    :goto_15
    invoke-direct {p0, v4, v6}, Lmiuix/animation/internal/AnimScheduler;->updateTarget(Lmiuix/animation/IAnimTarget;Ljava/util/List;)Z

    move-result v6

    goto :goto_12

    nop

    :goto_16
    const-string v4, "mRunningAnimCount="

    goto :goto_71

    nop

    :goto_17
    const-string v3, " hasRunningTarget:"

    goto :goto_7b

    nop

    :goto_18
    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    goto :goto_3e

    nop

    :goto_19
    const-string v7, "mRunningTarget.size="

    goto :goto_78

    nop

    :goto_1a
    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_1e

    nop

    :goto_1b
    goto :goto_4b

    :goto_1c
    goto :goto_2c

    nop

    :goto_1d
    if-nez v0, :cond_3

    goto :goto_49

    :cond_3
    goto :goto_55

    nop

    :goto_1e
    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    goto :goto_62

    nop

    :goto_1f
    const-string v3, "-- update finish->startEngine hasPrepareTrans:"

    goto :goto_5e

    nop

    :goto_20
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_3d

    nop

    :goto_21
    invoke-interface {v6}, Ljava/util/Set;->isEmpty()Z

    move-result v6

    goto :goto_14

    nop

    :goto_22
    invoke-static {v4, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_23
    goto :goto_32

    nop

    :goto_24
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mPreDelTargetList:Ljava/util/List;

    goto :goto_4c

    nop

    :goto_25
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_74

    nop

    :goto_26
    iget-object v6, p0, Lmiuix/animation/internal/AnimScheduler;->mPrepareTransMap:Ljava/util/Map;

    goto :goto_10

    nop

    :goto_27
    invoke-direct {p0}, Lmiuix/animation/internal/AnimScheduler;->startEngine()V

    goto :goto_65

    nop

    :goto_28
    iget-object v6, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    goto :goto_21

    nop

    :goto_29
    invoke-interface {v5, v4}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_4

    nop

    :goto_2a
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    goto :goto_5c

    nop

    :goto_2b
    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v4

    goto :goto_73

    nop

    :goto_2c
    iput-boolean v1, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    goto :goto_1

    nop

    :goto_2d
    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_2e
    goto :goto_45

    nop

    :goto_2f
    iget v4, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    goto :goto_3f

    nop

    :goto_30
    iget-object v4, v4, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    goto :goto_53

    nop

    :goto_31
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_25

    nop

    :goto_32
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mPrepareTransMap:Ljava/util/Map;

    goto :goto_f

    nop

    :goto_33
    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_19

    nop

    :goto_34
    if-nez v6, :cond_4

    goto :goto_6d

    :cond_4
    goto :goto_6c

    nop

    :goto_35
    invoke-virtual {v2, v7}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_67

    nop

    :goto_36
    move v3, v5

    :goto_37
    goto :goto_69

    nop

    :goto_38
    iput v1, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    goto :goto_59

    nop

    :goto_39
    if-nez v4, :cond_5

    goto :goto_1c

    :cond_5
    goto :goto_2b

    nop

    :goto_3a
    if-nez v0, :cond_6

    goto :goto_2e

    :cond_6
    goto :goto_6b

    nop

    :goto_3b
    const-string v3, " Scheduler@"

    goto :goto_54

    nop

    :goto_3c
    return-void

    :goto_3d
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_16

    nop

    :goto_3e
    invoke-direct {v2, v3}, Ljava/util/HashSet;-><init>(Ljava/util/Collection;)V

    goto :goto_64

    nop

    :goto_3f
    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_42

    nop

    :goto_40
    if-eqz v3, :cond_7

    goto :goto_46

    :cond_7
    goto :goto_3a

    nop

    :goto_41
    iget-object v4, p0, Lmiuix/animation/internal/AnimScheduler;->mPreDelTargetList:Ljava/util/List;

    goto :goto_70

    nop

    :goto_42
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_72

    nop

    :goto_43
    iput v5, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    goto :goto_1b

    nop

    :goto_44
    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_50

    nop

    :goto_45
    invoke-direct {p0}, Lmiuix/animation/internal/AnimScheduler;->endEngine()V

    :goto_46
    goto :goto_3c

    nop

    :goto_47
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_79

    nop

    :goto_48
    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_49
    goto :goto_38

    nop

    :goto_4a
    move v3, v1

    :goto_4b
    goto :goto_61

    nop

    :goto_4c
    invoke-interface {v2}, Ljava/util/List;->clear()V

    :goto_4d
    goto :goto_60

    nop

    :goto_4e
    new-array v3, v1, [Ljava/lang/Object;

    goto :goto_8

    nop

    :goto_4f
    if-nez v2, :cond_8

    goto :goto_76

    :cond_8
    goto :goto_75

    nop

    :goto_50
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    goto :goto_63

    nop

    :goto_51
    const/4 v5, 0x1

    goto :goto_39

    nop

    :goto_52
    invoke-interface {v7}, Ljava/util/Set;->size()I

    move-result v7

    goto :goto_1a

    nop

    :goto_53
    invoke-virtual {v4}, Lmiuix/animation/internal/AnimManager;->getTotalAnimCount()I

    move-result v4

    goto :goto_2

    nop

    :goto_54
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_13

    nop

    :goto_55
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_77

    nop

    :goto_56
    iget v3, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I

    goto :goto_5b

    nop

    :goto_57
    iget v5, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    goto :goto_30

    nop

    :goto_58
    iget-object v6, p0, Lmiuix/animation/internal/AnimScheduler;->mTempTargetRunningInfo:Ljava/util/List;

    goto :goto_15

    nop

    :goto_59
    new-instance v2, Ljava/util/HashSet;

    goto :goto_18

    nop

    :goto_5a
    const-string v4, "-- update after traversal all target"

    goto :goto_22

    nop

    :goto_5b
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_3b

    nop

    :goto_5c
    const/4 v1, 0x0

    goto :goto_1d

    nop

    :goto_5d
    if-nez v2, :cond_9

    goto :goto_23

    :cond_9
    goto :goto_20

    nop

    :goto_5e
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_5f
    if-nez v0, :cond_a

    goto :goto_9

    :cond_a
    goto :goto_6a

    nop

    :goto_60
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v2

    goto :goto_5d

    nop

    :goto_61
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v4

    goto :goto_51

    nop

    :goto_62
    filled-new-array {v2, v4, v6}, [Ljava/lang/Object;

    move-result-object v2

    goto :goto_5a

    nop

    :goto_63
    new-instance v6, Ljava/lang/StringBuilder;

    goto :goto_33

    nop

    :goto_64
    invoke-interface {v2}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    goto :goto_4a

    nop

    :goto_65
    move v3, v5

    :goto_66
    goto :goto_40

    nop

    :goto_67
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_4e

    nop

    :goto_68
    iget-object v7, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    goto :goto_52

    nop

    :goto_69
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v5

    goto :goto_a

    nop

    :goto_6a
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_7a

    nop

    :goto_6b
    const-string v0, "-- update->endEngine when isRunning is false"

    goto :goto_6f

    nop

    :goto_6c
    goto :goto_5

    :goto_6d
    goto :goto_6

    nop

    :goto_6e
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    goto :goto_41

    nop

    :goto_6f
    new-array v1, v1, [Ljava/lang/Object;

    goto :goto_2d

    nop

    :goto_70
    invoke-interface {v2, v4}, Ljava/util/Set;->removeAll(Ljava/util/Collection;)Z

    goto :goto_24

    nop

    :goto_71
    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2f

    nop

    :goto_72
    new-instance v4, Ljava/lang/StringBuilder;

    goto :goto_47

    nop

    :goto_73
    check-cast v4, Lmiuix/animation/IAnimTarget;

    goto :goto_58

    nop

    :goto_74
    new-array v3, v1, [Ljava/lang/Object;

    goto :goto_48

    nop

    :goto_75
    if-eqz v6, :cond_b

    goto :goto_66

    :cond_b
    :goto_76
    goto :goto_5f

    nop

    :goto_77
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_0

    nop

    :goto_78
    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_68

    nop

    :goto_79
    const-string v6, "mPrepareTransMap.size="

    goto :goto_3

    nop

    :goto_7a
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_1f

    nop

    :goto_7b
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_35

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimScheduler__runAnimTaskOnFrame',
        'method': '.method protected runAnimTaskOnFrame(JJJ)V',
        'method_name': 'runAnimTaskOnFrame',
        'method_anchors': ['new-instance v2, Ljava/util/HashSet;', 'iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;', 'invoke-direct {v2, v3}, Ljava/util/HashSet;-><init>(Ljava/util/Collection;)V', 'iget-wide v6, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J', 'iput-wide v6, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J', 'if-lez v3, :cond_0', 'iget v3, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I', 'iput v3, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I'],
        'type': 'method_replace',
        'search': """.method protected runAnimTaskOnFrame(JJJ)V
    .registers 21

    move-wide/from16 v4, p3

    move-wide/from16 v0, p5

    new-instance v2, Ljava/util/HashSet;

    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    invoke-direct {v2, v3}, Ljava/util/HashSet;-><init>(Ljava/util/Collection;)V

    iget-wide v6, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J

    add-long/2addr v6, v4

    iput-wide v6, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J

    const-wide/16 v6, 0x0

    cmp-long v3, v4, v6

    const/4 v6, 0x1

    if-lez v3, :cond_0

    iget v3, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I

    add-int/2addr v3, v6

    iput v3, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I

    :cond_0
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v9

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v3

    const/4 v10, 0x0

    if-eqz v3, :cond_1

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "+++ runAnimTaskOnFrame start frameCount="

    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v7, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I

    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v7, " nowNanos="

    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-wide v7, p1

    invoke-virtual {v3, v7, v8}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    const-string v7, " deltaTNanos="

    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v4, v5}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    const-string v7, " averageDelta="

    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v0, v1}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    const-string v7, " Scheduler@"

    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result v7

    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    new-array v7, v10, [Ljava/lang/Object;

    invoke-static {v3, v7}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    iput v10, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    invoke-interface {v2}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_0
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_2

    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lmiuix/animation/IAnimTarget;

    iget-object v3, v3, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    iget-object v7, p0, Lmiuix/animation/internal/AnimScheduler;->mTransListForRun:Ljava/util/List;

    invoke-virtual {v3, v7}, Lmiuix/animation/internal/AnimManager;->addToTransitionInfoList(Ljava/util/List;)V

    goto :goto_0

    :cond_2
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTransListForRun:Ljava/util/List;

    invoke-interface {v2}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_1
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_3

    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lmiuix/animation/internal/TransitionInfo;

    iget v7, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    invoke-virtual {v3}, Lmiuix/animation/internal/TransitionInfo;->getAnimCount()I

    move-result v8

    add-int/2addr v7, v8

    iput v7, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    invoke-static {v3, v0, v1}, Lmiuix/animation/internal/TransitionInfo;->tickOnFrame(Lmiuix/animation/internal/TransitionInfo;J)V

    iget-object v7, p0, Lmiuix/animation/internal/AnimScheduler;->mAnimTaskForRun:Ljava/util/List;

    iget-object v3, v3, Lmiuix/animation/internal/TransitionInfo;->animTasks:Ljava/util/List;

    invoke-interface {v7, v3}, Ljava/util/List;->addAll(Ljava/util/Collection;)Z

    goto :goto_1

    :cond_3
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTransListForRun:Ljava/util/List;

    invoke-interface {v2}, Ljava/util/List;->isEmpty()Z

    move-result v11

    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTransListForRun:Ljava/util/List;

    invoke-interface {v2}, Ljava/util/List;->clear()V

    iget v2, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    add-int/lit16 v2, v2, -0xfa0

    invoke-static {v10, v2}, Ljava/lang/Math;->max(II)I

    move-result v2

    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackSplitInfo:[I

    invoke-static {v2, v3}, Lmiuix/animation/internal/ThreadPoolUtil;->getSplitCount(I[I)V

    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackSplitInfo:[I

    aget v3, v2, v10

    aget v2, v2, v6

    iget-object v7, p0, Lmiuix/animation/internal/AnimScheduler;->mAnimTaskForRun:Ljava/util/List;

    invoke-direct {p0, v7, v2, v3}, Lmiuix/animation/internal/AnimScheduler;->assignAnimTaskToStack(Ljava/util/List;II)V

    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mAnimTaskForRun:Ljava/util/List;

    invoke-interface {v2}, Ljava/util/List;->clear()V

    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    invoke-interface {v2}, Ljava/util/List;->isEmpty()Z

    move-result v2

    xor-int/2addr v2, v6

    iput-boolean v2, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->runningStackCount:Ljava/util/concurrent/atomic/AtomicInteger;

    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    invoke-interface {v3}, Ljava/util/List;->size()I

    move-result v3

    invoke-virtual {v2, v3}, Ljava/util/concurrent/atomic/AtomicInteger;->getAndAdd(I)I

    if-eqz v9, :cond_4

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "+++ runAnimTaskOnFrame mTaskStackList.size "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    invoke-interface {v3}, Ljava/util/List;->size()I

    move-result v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    new-array v3, v10, [Ljava/lang/Object;

    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_4
    long-to-double v0, v0

    const-wide v2, 0x41cdcd6500000000L

    div-double v7, v0, v2

    iget-boolean v0, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    if-eqz v0, :cond_6

    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    invoke-interface {v0, v10}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    move-object v12, v0

    check-cast v12, Lmiuix/animation/internal/AnimTask;

    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v0

    const/4 v1, 0x1

    if-le v0, v6, :cond_5

    move v13, v6

    :goto_2
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v0

    if-ge v13, v0, :cond_5

    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    invoke-interface {v0, v13}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiuix/animation/internal/AnimTask;

    iget-wide v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J

    move v6, v1

    move-object v1, p0

    invoke-static/range {v0 .. v8}, Lmiuix/animation/internal/AnimTask;->asyncStart(Lmiuix/animation/internal/AnimTask;Lmiuix/animation/internal/AnimScheduler;JJID)V

    add-int/lit8 v13, v13, 0x1

    move-wide/from16 v4, p3

    move v1, v6

    goto :goto_2

    :cond_5
    move v6, v1

    iget-wide v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J

    move-object v1, p0

    move-wide/from16 v4, p3

    move-object v0, v12

    invoke-static/range {v0 .. v8}, Lmiuix/animation/internal/AnimTask;->start(Lmiuix/animation/internal/AnimTask;Lmiuix/animation/internal/AnimScheduler;JJID)V

    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->clear()V

    :cond_6
    if-eqz v9, :cond_7

    invoke-static {v11}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v0

    iget-boolean v2, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    invoke-static {v2}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v2

    filled-new-array {v0, v2}, [Ljava/lang/Object;

    move-result-object v0

    const-string v2, "--- runAnimTaskOnFrame finish isAllTransFinish:%s mHasTaskStackRunning:%s"

    invoke-static {v2, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    new-array v2, v10, [Ljava/lang/Object;

    invoke-static {v0, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_7
    iget-boolean v0, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    if-eqz v0, :cond_8

    iput-boolean v10, p0, Lmiuix/animation/internal/AnimScheduler;->mEngineStart:Z

    iget-object p0, p0, Lmiuix/animation/internal/AnimScheduler;->mEngine:Lmiuix/animation/internal/FolmeEngine;

    invoke-virtual {p0}, Lmiuix/animation/internal/FolmeEngine;->waitForAllTaskFinish()V

    return-void

    :cond_8
    if-eqz v11, :cond_a

    if-eqz v9, :cond_9

    const-string v0, "--- runAnimTaskOnFrame->endEngine: no transList then endEngine"

    new-array v2, v10, [Ljava/lang/Object;

    invoke-static {v0, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_9
    invoke-direct {p0}, Lmiuix/animation/internal/AnimScheduler;->endEngine()V

    :cond_a
    return-void
.end method""",
        'replacement': """.method protected runAnimTaskOnFrame(JJJ)V
    .registers 21

    goto :goto_17

    nop

    :goto_0
    goto :goto_7d

    :goto_1
    goto :goto_56

    nop

    :goto_2
    if-nez v3, :cond_0

    goto :goto_63

    :cond_0
    goto :goto_32

    nop

    :goto_3
    invoke-direct {p0}, Lmiuix/animation/internal/AnimScheduler;->endEngine()V

    :goto_4
    goto :goto_85

    nop

    :goto_5
    div-double v7, v0, v2

    goto :goto_3d

    nop

    :goto_6
    add-long/2addr v6, v4

    goto :goto_25

    nop

    :goto_7
    const/4 v10, 0x0

    goto :goto_2

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    goto :goto_89

    nop

    :goto_9
    move-object v0, v12

    goto :goto_75

    nop

    :goto_a
    new-array v2, v10, [Ljava/lang/Object;

    goto :goto_18

    nop

    :goto_b
    invoke-static {v2, v3}, Lmiuix/animation/internal/ThreadPoolUtil;->getSplitCount(I[I)V

    goto :goto_53

    nop

    :goto_c
    if-lt v13, v0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_21

    nop

    :goto_d
    if-gtz v3, :cond_2

    goto :goto_9a

    :cond_2
    goto :goto_9b

    nop

    :goto_e
    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackSplitInfo:[I

    goto :goto_b

    nop

    :goto_f
    move-object v1, p0

    goto :goto_44

    nop

    :goto_10
    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_11
    goto :goto_1b

    nop

    :goto_12
    new-array v7, v10, [Ljava/lang/Object;

    goto :goto_62

    nop

    :goto_13
    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9e

    nop

    :goto_14
    cmp-long v3, v4, v6

    goto :goto_a2

    nop

    :goto_15
    iput-boolean v10, p0, Lmiuix/animation/internal/AnimScheduler;->mEngineStart:Z

    goto :goto_ad

    nop

    :goto_16
    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_34

    nop

    :goto_17
    move-wide/from16 v4, p3

    goto :goto_90

    nop

    :goto_18
    invoke-static {v0, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_19
    goto :goto_3

    nop

    :goto_1a
    const-string v0, "--- runAnimTaskOnFrame->endEngine: no transList then endEngine"

    goto :goto_a

    nop

    :goto_1b
    long-to-double v0, v0

    goto :goto_45

    nop

    :goto_1c
    aget v2, v2, v6

    goto :goto_24

    nop

    :goto_1d
    invoke-static {v10, v2}, Ljava/lang/Math;->max(II)I

    move-result v2

    goto :goto_e

    nop

    :goto_1e
    iget-wide v6, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J

    goto :goto_6

    nop

    :goto_1f
    iget-wide v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J

    goto :goto_5f

    nop

    :goto_20
    invoke-direct {p0, v7, v2, v3}, Lmiuix/animation/internal/AnimScheduler;->assignAnimTaskToStack(Ljava/util/List;II)V

    goto :goto_70

    nop

    :goto_21
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    goto :goto_60

    nop

    :goto_22
    filled-new-array {v0, v2}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_92

    nop

    :goto_23
    invoke-virtual {v3}, Lmiuix/animation/internal/TransitionInfo;->getAnimCount()I

    move-result v8

    goto :goto_43

    nop

    :goto_24
    iget-object v7, p0, Lmiuix/animation/internal/AnimScheduler;->mAnimTaskForRun:Ljava/util/List;

    goto :goto_20

    nop

    :goto_25
    iput-wide v6, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J

    goto :goto_2a

    nop

    :goto_26
    invoke-static {v2, v0}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    goto :goto_42

    nop

    :goto_27
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v3

    goto :goto_7

    nop

    :goto_28
    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_64

    nop

    :goto_29
    iget-boolean v2, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    goto :goto_a5

    nop

    :goto_2a
    const-wide/16 v6, 0x0

    goto :goto_14

    nop

    :goto_2b
    if-nez v0, :cond_3

    goto :goto_38

    :cond_3
    goto :goto_15

    nop

    :goto_2c
    if-gt v0, v6, :cond_4

    goto :goto_1

    :cond_4
    goto :goto_7c

    nop

    :goto_2d
    invoke-interface {v2}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_2e
    goto :goto_73

    nop

    :goto_2f
    invoke-virtual {v3, v0, v1}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    goto :goto_a9

    nop

    :goto_30
    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    goto :goto_a3

    nop

    :goto_31
    if-nez v3, :cond_5

    goto :goto_79

    :cond_5
    goto :goto_96

    nop

    :goto_32
    new-instance v3, Ljava/lang/StringBuilder;

    goto :goto_8c

    nop

    :goto_33
    if-nez v11, :cond_6

    goto :goto_4

    :cond_6
    goto :goto_74

    nop

    :goto_34
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    goto :goto_12

    nop

    :goto_35
    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result v7

    goto :goto_16

    nop

    :goto_36
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    goto :goto_8a

    nop

    :goto_37
    return-void

    :goto_38
    goto :goto_33

    nop

    :goto_39
    invoke-interface {v2}, Ljava/util/List;->clear()V

    goto :goto_8f

    nop

    :goto_3a
    invoke-direct {v2, v3}, Ljava/util/HashSet;-><init>(Ljava/util/Collection;)V

    goto :goto_1e

    nop

    :goto_3b
    check-cast v3, Lmiuix/animation/internal/TransitionInfo;

    goto :goto_4a

    nop

    :goto_3c
    invoke-virtual {v3, v7, v8}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    goto :goto_a4

    nop

    :goto_3d
    iget-boolean v0, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    goto :goto_7b

    nop

    :goto_3e
    const-string v7, " nowNanos="

    goto :goto_13

    nop

    :goto_3f
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_aa

    nop

    :goto_40
    add-int/lit8 v13, v13, 0x1

    goto :goto_9c

    nop

    :goto_41
    invoke-interface {v0, v10}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_49

    nop

    :goto_42
    new-array v2, v10, [Ljava/lang/Object;

    goto :goto_6d

    nop

    :goto_43
    add-int/2addr v7, v8

    goto :goto_98

    nop

    :goto_44
    move-wide/from16 v4, p3

    goto :goto_9

    nop

    :goto_45
    const-wide v2, 0x41cdcd6500000000L

    goto :goto_5

    nop

    :goto_46
    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningTarget:Ljava/util/Set;

    goto :goto_3a

    nop

    :goto_47
    invoke-static {v11}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v0

    goto :goto_29

    nop

    :goto_48
    invoke-interface {v3}, Ljava/util/List;->size()I

    move-result v3

    goto :goto_4d

    nop

    :goto_49
    move-object v12, v0

    goto :goto_8d

    nop

    :goto_4a
    iget v7, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    goto :goto_23

    nop

    :goto_4b
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    goto :goto_ac

    nop

    :goto_4c
    invoke-interface {v7, v3}, Ljava/util/List;->addAll(Ljava/util/Collection;)Z

    goto :goto_78

    nop

    :goto_4d
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_7f

    nop

    :goto_4e
    if-nez v9, :cond_7

    goto :goto_11

    :cond_7
    goto :goto_6c

    nop

    :goto_4f
    new-array v3, v10, [Ljava/lang/Object;

    goto :goto_10

    nop

    :goto_50
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    goto :goto_68

    nop

    :goto_51
    move v1, v6

    goto :goto_0

    nop

    :goto_52
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    goto :goto_31

    nop

    :goto_53
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackSplitInfo:[I

    goto :goto_58

    nop

    :goto_54
    const/4 v1, 0x1

    goto :goto_2c

    nop

    :goto_55
    add-int/2addr v3, v6

    goto :goto_99

    nop

    :goto_56
    move v6, v1

    goto :goto_59

    nop

    :goto_57
    const-string v7, "+++ runAnimTaskOnFrame start frameCount="

    goto :goto_28

    nop

    :goto_58
    aget v3, v2, v10

    goto :goto_1c

    nop

    :goto_59
    iget-wide v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTotalTNanos:J

    goto :goto_f

    nop

    :goto_5a
    invoke-static {v3, v0, v1}, Lmiuix/animation/internal/TransitionInfo;->tickOnFrame(Lmiuix/animation/internal/TransitionInfo;J)V

    goto :goto_67

    nop

    :goto_5b
    invoke-interface {v2}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_5c
    goto :goto_52

    nop

    :goto_5d
    invoke-virtual {v3, v4, v5}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    goto :goto_8e

    nop

    :goto_5e
    iput-boolean v2, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    goto :goto_88

    nop

    :goto_5f
    move v6, v1

    goto :goto_7a

    nop

    :goto_60
    invoke-interface {v0, v13}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_9d

    nop

    :goto_61
    if-nez v3, :cond_8

    goto :goto_87

    :cond_8
    goto :goto_76

    nop

    :goto_62
    invoke-static {v3, v7}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_63
    goto :goto_95

    nop

    :goto_64
    iget v7, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I

    goto :goto_83

    nop

    :goto_65
    invoke-virtual {v3, v7}, Lmiuix/animation/internal/AnimManager;->addToTransitionInfoList(Ljava/util/List;)V

    goto :goto_86

    nop

    :goto_66
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTransListForRun:Ljava/util/List;

    goto :goto_39

    nop

    :goto_67
    iget-object v7, p0, Lmiuix/animation/internal/AnimScheduler;->mAnimTaskForRun:Ljava/util/List;

    goto :goto_9f

    nop

    :goto_68
    invoke-interface {v0}, Ljava/util/List;->clear()V

    :goto_69
    goto :goto_94

    nop

    :goto_6a
    check-cast v3, Lmiuix/animation/IAnimTarget;

    goto :goto_80

    nop

    :goto_6b
    const-string v3, "+++ runAnimTaskOnFrame mTaskStackList.size "

    goto :goto_3f

    nop

    :goto_6c
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_82

    nop

    :goto_6d
    invoke-static {v0, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_6e
    goto :goto_a1

    nop

    :goto_6f
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v9

    goto :goto_27

    nop

    :goto_70
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mAnimTaskForRun:Ljava/util/List;

    goto :goto_a8

    nop

    :goto_71
    invoke-virtual {p0}, Lmiuix/animation/internal/FolmeEngine;->waitForAllTaskFinish()V

    goto :goto_37

    nop

    :goto_72
    iget-object v7, p0, Lmiuix/animation/internal/AnimScheduler;->mTransListForRun:Ljava/util/List;

    goto :goto_65

    nop

    :goto_73
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    goto :goto_61

    nop

    :goto_74
    if-nez v9, :cond_9

    goto :goto_19

    :cond_9
    goto :goto_1a

    nop

    :goto_75
    invoke-static/range {v0 .. v8}, Lmiuix/animation/internal/AnimTask;->start(Lmiuix/animation/internal/AnimTask;Lmiuix/animation/internal/AnimScheduler;JJID)V

    goto :goto_50

    nop

    :goto_76
    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    goto :goto_6a

    nop

    :goto_77
    iget-object v0, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    goto :goto_41

    nop

    :goto_78
    goto :goto_5c

    :goto_79
    goto :goto_a7

    nop

    :goto_7a
    move-object v1, p0

    goto :goto_a0

    nop

    :goto_7b
    if-nez v0, :cond_a

    goto :goto_69

    :cond_a
    goto :goto_77

    nop

    :goto_7c
    move v13, v6

    :goto_7d
    goto :goto_8

    nop

    :goto_7e
    xor-int/2addr v2, v6

    goto :goto_5e

    nop

    :goto_7f
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_4f

    nop

    :goto_80
    iget-object v3, v3, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    goto :goto_72

    nop

    :goto_81
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTransListForRun:Ljava/util/List;

    goto :goto_5b

    nop

    :goto_82
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_6b

    nop

    :goto_83
    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_3e

    nop

    :goto_84
    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_5d

    nop

    :goto_85
    return-void

    :goto_86
    goto :goto_2e

    :goto_87
    goto :goto_81

    nop

    :goto_88
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->runningStackCount:Ljava/util/concurrent/atomic/AtomicInteger;

    goto :goto_30

    nop

    :goto_89
    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v0

    goto :goto_c

    nop

    :goto_8a
    invoke-interface {v2}, Ljava/util/List;->isEmpty()Z

    move-result v2

    goto :goto_7e

    nop

    :goto_8b
    invoke-interface {v2}, Ljava/util/List;->isEmpty()Z

    move-result v11

    goto :goto_66

    nop

    :goto_8c
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_57

    nop

    :goto_8d
    check-cast v12, Lmiuix/animation/internal/AnimTask;

    goto :goto_4b

    nop

    :goto_8e
    const-string v7, " averageDelta="

    goto :goto_a6

    nop

    :goto_8f
    iget v2, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    goto :goto_91

    nop

    :goto_90
    move-wide/from16 v0, p5

    goto :goto_ab

    nop

    :goto_91
    add-int/lit16 v2, v2, -0xfa0

    goto :goto_1d

    nop

    :goto_92
    const-string v2, "--- runAnimTaskOnFrame finish isAllTransFinish:%s mHasTaskStackRunning:%s"

    goto :goto_26

    nop

    :goto_93
    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_35

    nop

    :goto_94
    if-nez v9, :cond_b

    goto :goto_6e

    :cond_b
    goto :goto_47

    nop

    :goto_95
    iput v10, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    goto :goto_2d

    nop

    :goto_96
    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    goto :goto_3b

    nop

    :goto_97
    invoke-virtual {v2, v3}, Ljava/util/concurrent/atomic/AtomicInteger;->getAndAdd(I)I

    goto :goto_4e

    nop

    :goto_98
    iput v7, p0, Lmiuix/animation/internal/AnimScheduler;->mRunningAnimCount:I

    goto :goto_5a

    nop

    :goto_99
    iput v3, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I

    :goto_9a
    goto :goto_6f

    nop

    :goto_9b
    iget v3, p0, Lmiuix/animation/internal/AnimScheduler;->mFrameCount:I

    goto :goto_55

    nop

    :goto_9c
    move-wide/from16 v4, p3

    goto :goto_51

    nop

    :goto_9d
    check-cast v0, Lmiuix/animation/internal/AnimTask;

    goto :goto_1f

    nop

    :goto_9e
    move-wide v7, p1

    goto :goto_3c

    nop

    :goto_9f
    iget-object v3, v3, Lmiuix/animation/internal/TransitionInfo;->animTasks:Ljava/util/List;

    goto :goto_4c

    nop

    :goto_a0
    invoke-static/range {v0 .. v8}, Lmiuix/animation/internal/AnimTask;->asyncStart(Lmiuix/animation/internal/AnimTask;Lmiuix/animation/internal/AnimScheduler;JJID)V

    goto :goto_40

    nop

    :goto_a1
    iget-boolean v0, p0, Lmiuix/animation/internal/AnimScheduler;->mHasTaskStackRunning:Z

    goto :goto_2b

    nop

    :goto_a2
    const/4 v6, 0x1

    goto :goto_d

    nop

    :goto_a3
    invoke-interface {v3}, Ljava/util/List;->size()I

    move-result v3

    goto :goto_97

    nop

    :goto_a4
    const-string v7, " deltaTNanos="

    goto :goto_84

    nop

    :goto_a5
    invoke-static {v2}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v2

    goto :goto_22

    nop

    :goto_a6
    invoke-virtual {v3, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2f

    nop

    :goto_a7
    iget-object v2, p0, Lmiuix/animation/internal/AnimScheduler;->mTransListForRun:Ljava/util/List;

    goto :goto_8b

    nop

    :goto_a8
    invoke-interface {v2}, Ljava/util/List;->clear()V

    goto :goto_36

    nop

    :goto_a9
    const-string v7, " Scheduler@"

    goto :goto_93

    nop

    :goto_aa
    iget-object v3, p0, Lmiuix/animation/internal/AnimScheduler;->mTaskStackList:Ljava/util/List;

    goto :goto_48

    nop

    :goto_ab
    new-instance v2, Ljava/util/HashSet;

    goto :goto_46

    nop

    :goto_ac
    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v0

    goto :goto_54

    nop

    :goto_ad
    iget-object p0, p0, Lmiuix/animation/internal/AnimScheduler;->mEngine:Lmiuix/animation/internal/FolmeEngine;

    goto :goto_71

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
