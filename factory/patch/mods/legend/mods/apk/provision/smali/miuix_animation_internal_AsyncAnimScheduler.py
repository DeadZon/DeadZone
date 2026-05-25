TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/AsyncAnimScheduler.smali'
CLASS_FALLBACK_NAMES = ['AsyncAnimScheduler.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/internal/AnimScheduler;']

PATCHES = [
    {
        'id': 'miuix_animation_internal_AsyncAnimScheduler__executeDoAnimOnFrame',
        'method': '.method executeDoAnimOnFrame(JJ)V',
        'method_name': 'executeDoAnimOnFrame',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mScheduleHandler:Landroid/os/Handler;', 'invoke-virtual {v0}, Landroid/os/Handler;->obtainMessage()Landroid/os/Message;', 'iput v1, v0, Landroid/os/Message;->what:I', 'new-instance v1, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;', 'invoke-direct {v1, p0}, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;-><init>(Lmiuix/animation/internal/AsyncAnimScheduler;)V', 'iput-wide p1, v1, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;->frameTime:J', 'iput-wide p3, v1, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;->deltaT:J', 'iput-object v1, v0, Landroid/os/Message;->obj:Ljava/lang/Object;'],
        'type': 'method_replace',
        'search': """.method executeDoAnimOnFrame(JJ)V
    .registers 7

    iget-object v0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mScheduleHandler:Landroid/os/Handler;

    invoke-virtual {v0}, Landroid/os/Handler;->obtainMessage()Landroid/os/Message;

    move-result-object v0

    const/4 v1, 0x3

    iput v1, v0, Landroid/os/Message;->what:I

    new-instance v1, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;

    invoke-direct {v1, p0}, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;-><init>(Lmiuix/animation/internal/AsyncAnimScheduler;)V

    iput-wide p1, v1, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;->frameTime:J

    iput-wide p3, v1, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;->deltaT:J

    iput-object v1, v0, Landroid/os/Message;->obj:Ljava/lang/Object;

    iget-object p0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mScheduleHandler:Landroid/os/Handler;

    invoke-virtual {p0, v0}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    return-void
.end method""",
        'replacement': """.method executeDoAnimOnFrame(JJ)V
    .registers 7

    goto :goto_4

    nop

    :goto_0
    invoke-direct {v1, p0}, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;-><init>(Lmiuix/animation/internal/AsyncAnimScheduler;)V

    goto :goto_a

    nop

    :goto_1
    iput-object v1, v0, Landroid/os/Message;->obj:Ljava/lang/Object;

    goto :goto_b

    nop

    :goto_2
    new-instance v1, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;

    goto :goto_0

    nop

    :goto_3
    return-void

    :goto_4
    iget-object v0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mScheduleHandler:Landroid/os/Handler;

    goto :goto_8

    nop

    :goto_5
    invoke-virtual {p0, v0}, Landroid/os/Handler;->sendMessage(Landroid/os/Message;)Z

    goto :goto_3

    nop

    :goto_6
    iput-wide p3, v1, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;->deltaT:J

    goto :goto_1

    nop

    :goto_7
    iput v1, v0, Landroid/os/Message;->what:I

    goto :goto_2

    nop

    :goto_8
    invoke-virtual {v0}, Landroid/os/Handler;->obtainMessage()Landroid/os/Message;

    move-result-object v0

    goto :goto_9

    nop

    :goto_9
    const/4 v1, 0x3

    goto :goto_7

    nop

    :goto_a
    iput-wide p1, v1, Lmiuix/animation/internal/AsyncAnimScheduler$TimeInfo;->frameTime:J

    goto :goto_6

    nop

    :goto_b
    iget-object p0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mScheduleHandler:Landroid/os/Handler;

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AsyncAnimScheduler__executePendingSetTo',
        'method': '.method executePendingSetTo(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;)V',
        'method_name': 'executePendingSetTo',
        'method_anchors': ['new-instance v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;', 'invoke-direct {v0}, Lmiuix/animation/internal/AnimScheduler$SetToInfo;-><init>()V', 'iput-object p1, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->target:Lmiuix/animation/IAnimTarget;', 'iget-boolean p1, p2, Lmiuix/animation/controller/AnimState;->needDuplicate:Z', 'if-eqz p1, :cond_0', 'new-instance p1, Lmiuix/animation/controller/AnimState;', 'invoke-direct {p1}, Lmiuix/animation/controller/AnimState;-><init>()V', 'iput-object p1, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->state:Lmiuix/animation/controller/AnimState;'],
        'type': 'method_replace',
        'search': """.method executePendingSetTo(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;)V
    .registers 4

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
    iget-object p0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mScheduleHandler:Landroid/os/Handler;

    const/4 p1, 0x4

    invoke-virtual {p0, p1, v0}, Landroid/os/Handler;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    return-void
.end method""",
        'replacement': """.method executePendingSetTo(Lmiuix/animation/IAnimTarget;Lmiuix/animation/controller/AnimState;)V
    .registers 4

    goto :goto_3

    nop

    :goto_0
    iput-object p1, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->state:Lmiuix/animation/controller/AnimState;

    goto :goto_b

    nop

    :goto_1
    iput-object p1, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->target:Lmiuix/animation/IAnimTarget;

    goto :goto_a

    nop

    :goto_2
    invoke-virtual {p0, p1, v0}, Landroid/os/Handler;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    goto :goto_6

    nop

    :goto_3
    new-instance v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;

    goto :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    invoke-direct {v0}, Lmiuix/animation/internal/AnimScheduler$SetToInfo;-><init>()V

    goto :goto_1

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_4

    nop

    :goto_7
    invoke-direct {p1}, Lmiuix/animation/controller/AnimState;-><init>()V

    goto :goto_0

    nop

    :goto_8
    iput-object p2, v0, Lmiuix/animation/internal/AnimScheduler$SetToInfo;->state:Lmiuix/animation/controller/AnimState;

    :goto_9
    goto :goto_10

    nop

    :goto_a
    iget-boolean p1, p2, Lmiuix/animation/controller/AnimState;->needDuplicate:Z

    goto :goto_f

    nop

    :goto_b
    invoke-virtual {p1, p2}, Lmiuix/animation/controller/AnimState;->set(Lmiuix/animation/controller/AnimState;)V

    goto :goto_d

    nop

    :goto_c
    new-instance p1, Lmiuix/animation/controller/AnimState;

    goto :goto_7

    nop

    :goto_d
    goto :goto_9

    :goto_e
    goto :goto_8

    nop

    :goto_f
    if-nez p1, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_c

    nop

    :goto_10
    iget-object p0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mScheduleHandler:Landroid/os/Handler;

    goto :goto_11

    nop

    :goto_11
    const/4 p1, 0x4

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AsyncAnimScheduler__executeTo',
        'method': '.method executeTo(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'executeTo',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mTempInfoMap:Ljava/util/Map;', 'iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I', 'invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-interface {v0, v1, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;', 'iget-object p0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mScheduleHandler:Landroid/os/Handler;', 'iget p1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I', 'invoke-virtual {p0, v1, p1, v0}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;', 'invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V'],
        'type': 'method_replace',
        'search': """.method executeTo(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 4

    iget-object v0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mTempInfoMap:Ljava/util/Map;

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-interface {v0, v1, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget-object p0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mScheduleHandler:Landroid/os/Handler;

    iget p1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    const/4 v0, 0x0

    const/4 v1, 0x1

    invoke-virtual {p0, v1, p1, v0}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;

    move-result-object p0

    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    return-void
.end method""",
        'replacement': """.method executeTo(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 4

    goto :goto_8

    nop

    :goto_0
    const/4 v0, 0x0

    goto :goto_1

    nop

    :goto_1
    const/4 v1, 0x1

    goto :goto_6

    nop

    :goto_2
    invoke-interface {v0, v1, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_9

    nop

    :goto_3
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_5

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_a

    nop

    :goto_5
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_2

    nop

    :goto_6
    invoke-virtual {p0, v1, p1, v0}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;

    move-result-object p0

    goto :goto_4

    nop

    :goto_7
    iget p1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_0

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mTempInfoMap:Ljava/util/Map;

    goto :goto_3

    nop

    :goto_9
    iget-object p0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mScheduleHandler:Landroid/os/Handler;

    goto :goto_7

    nop

    :goto_a
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AsyncAnimScheduler__runAnimTaskOnFrame',
        'method': '.method protected runAnimTaskOnFrame(JJJ)V',
        'method_name': 'runAnimTaskOnFrame',
        'method_anchors': ['sget-object v0, Lmiuix/animation/utils/BoostHelper;->hasBindBigCpu:Ljava/util/concurrent/atomic/AtomicBoolean;', 'invoke-virtual {v0}, Ljava/util/concurrent/atomic/AtomicBoolean;->get()Z', 'if-nez v0, :cond_0', 'invoke-static {}, Lmiuix/animation/utils/BoostHelper;->getInstance()Lmiuix/animation/utils/BoostHelper;', 'iget-boolean v0, v0, Lmiuix/animation/utils/BoostHelper;->isTurboSchedDisabled:Z', 'if-nez v0, :cond_0', 'sget-object v0, Lmiuix/animation/Folme;->appContext:Landroid/content/Context;', 'if-eqz v0, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected runAnimTaskOnFrame(JJJ)V
    .registers 12

    sget-object v0, Lmiuix/animation/utils/BoostHelper;->hasBindBigCpu:Ljava/util/concurrent/atomic/AtomicBoolean;

    invoke-virtual {v0}, Ljava/util/concurrent/atomic/AtomicBoolean;->get()Z

    move-result v0

    if-nez v0, :cond_0

    invoke-static {}, Lmiuix/animation/utils/BoostHelper;->getInstance()Lmiuix/animation/utils/BoostHelper;

    move-result-object v0

    iget-boolean v0, v0, Lmiuix/animation/utils/BoostHelper;->isTurboSchedDisabled:Z

    if-nez v0, :cond_0

    sget-object v0, Lmiuix/animation/Folme;->appContext:Landroid/content/Context;

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mThread:Landroid/os/HandlerThread;

    invoke-virtual {v0}, Landroid/os/HandlerThread;->getThreadId()I

    move-result v0

    :try_start_0
    invoke-static {}, Lmiuix/animation/utils/BoostHelper;->getInstance()Lmiuix/animation/utils/BoostHelper;

    move-result-object v1

    filled-new-array {v0}, [I

    move-result-object v0

    sget-object v2, Lmiuix/animation/Folme;->appContext:Landroid/content/Context;

    const-wide/16 v3, 0xbb8

    invoke-virtual {v1, v0, v3, v4, v2}, Lmiuix/animation/utils/BoostHelper;->setTurboSchedActionWithoutBlock([IJLandroid/content/Context;)V

    sget-object v0, Lmiuix/animation/utils/BoostHelper;->hasBindBigCpu:Ljava/util/concurrent/atomic/AtomicBoolean;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Ljava/util/concurrent/atomic/AtomicBoolean;->set(Z)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    :catch_0
    :cond_0
    invoke-super/range {p0 .. p6}, Lmiuix/animation/internal/AnimScheduler;->runAnimTaskOnFrame(JJJ)V

    return-void
.end method""",
        'replacement': """.method protected runAnimTaskOnFrame(JJJ)V
    .registers 12

    goto :goto_9

    nop

    :goto_0
    if-eqz v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_4

    nop

    :goto_1
    if-eqz v0, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_b

    nop

    :goto_2
    invoke-virtual {v0}, Ljava/util/concurrent/atomic/AtomicBoolean;->get()Z

    move-result v0

    goto :goto_0

    nop

    :goto_3
    iget-boolean v0, v0, Lmiuix/animation/utils/BoostHelper;->isTurboSchedDisabled:Z

    goto :goto_1

    nop

    :goto_4
    invoke-static {}, Lmiuix/animation/utils/BoostHelper;->getInstance()Lmiuix/animation/utils/BoostHelper;

    move-result-object v0

    goto :goto_3

    nop

    :goto_5
    invoke-virtual {v0}, Landroid/os/HandlerThread;->getThreadId()I

    move-result v0

    :try_start_0
    invoke-static {}, Lmiuix/animation/utils/BoostHelper;->getInstance()Lmiuix/animation/utils/BoostHelper;

    move-result-object v1

    filled-new-array {v0}, [I

    move-result-object v0

    sget-object v2, Lmiuix/animation/Folme;->appContext:Landroid/content/Context;

    const-wide/16 v3, 0xbb8

    invoke-virtual {v1, v0, v3, v4, v2}, Lmiuix/animation/utils/BoostHelper;->setTurboSchedActionWithoutBlock([IJLandroid/content/Context;)V

    sget-object v0, Lmiuix/animation/utils/BoostHelper;->hasBindBigCpu:Ljava/util/concurrent/atomic/AtomicBoolean;

    const/4 v1, 0x1

    invoke-virtual {v0, v1}, Ljava/util/concurrent/atomic/AtomicBoolean;->set(Z)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    :catch_0
    :goto_6
    goto :goto_7

    nop

    :goto_7
    invoke-super/range {p0 .. p6}, Lmiuix/animation/internal/AnimScheduler;->runAnimTaskOnFrame(JJJ)V

    goto :goto_8

    nop

    :goto_8
    return-void

    :goto_9
    sget-object v0, Lmiuix/animation/utils/BoostHelper;->hasBindBigCpu:Ljava/util/concurrent/atomic/AtomicBoolean;

    goto :goto_2

    nop

    :goto_a
    if-nez v0, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_c

    nop

    :goto_b
    sget-object v0, Lmiuix/animation/Folme;->appContext:Landroid/content/Context;

    goto :goto_a

    nop

    :goto_c
    iget-object v0, p0, Lmiuix/animation/internal/AsyncAnimScheduler;->mThread:Landroid/os/HandlerThread;

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
