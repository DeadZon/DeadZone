TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/FolmeEngine.smali'
CLASS_FALLBACK_NAMES = ['FolmeEngine.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final MAX_DELTA:J = 0xfe502aL', '.field protected static final MAX_RECORD:I = 0x5']

PATCHES = [
    {
        'id': 'miuix_animation_internal_FolmeEngine__endAnim',
        'method': '.method protected endAnim()V',
        'method_name': 'endAnim',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'if-eqz v0, :cond_0', 'const-string v2, "- FolmeEngine.endAnim start"', 'invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V', 'iput-wide v2, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J', 'iget-boolean v2, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z', 'if-nez v2, :cond_4', 'if-eqz v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected endAnim()V
    .registers 5

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    const-string v2, "- FolmeEngine.endAnim start"

    new-array v3, v1, [Ljava/lang/Object;

    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    const-wide/16 v2, 0x0

    iput-wide v2, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J

    iget-boolean v2, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z

    if-nez v2, :cond_4

    if-eqz v0, :cond_1

    const-string v0, "- FolmeEngine.endAnim return when runner is not running"

    new-array v1, v1, [Ljava/lang/Object;

    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    invoke-virtual {p0}, Lmiuix/animation/internal/FolmeEngine;->stopNextFrame()V

    iget-object v0, p0, Lmiuix/animation/internal/FolmeEngine;->mEngineListener:Ljava/util/Set;

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_2

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/animation/listener/EngineListener;

    invoke-virtual {v1}, Lmiuix/animation/listener/EngineListener;->onComplete()V

    goto :goto_0

    :cond_2
    iget-object v0, p0, Lmiuix/animation/internal/FolmeEngine;->mPendingRemoveEngineListener:Ljava/util/Set;

    if-eqz v0, :cond_5

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_1
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/animation/listener/EngineListener;

    iget-object v2, p0, Lmiuix/animation/internal/FolmeEngine;->mEngineListener:Ljava/util/Set;

    invoke-interface {v2, v1}, Ljava/util/Set;->remove(Ljava/lang/Object;)Z

    goto :goto_1

    :cond_3
    iget-object v0, p0, Lmiuix/animation/internal/FolmeEngine;->mPendingRemoveEngineListener:Ljava/util/Set;

    invoke-interface {v0}, Ljava/util/Set;->clear()V

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/animation/internal/FolmeEngine;->mPendingRemoveEngineListener:Ljava/util/Set;

    return-void

    :cond_4
    iput-boolean v1, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z

    invoke-virtual {p0}, Lmiuix/animation/internal/FolmeEngine;->stopNextFrame()V

    if-eqz v0, :cond_5

    const-string p0, "- FolmeEngine.endAnim finish"

    new-array v0, v1, [Ljava/lang/Object;

    invoke-static {p0, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_5
    return-void
.end method""",
        'replacement': """.method protected endAnim()V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    invoke-interface {v0}, Ljava/util/Set;->clear()V

    goto :goto_14

    nop

    :goto_1
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_30

    nop

    :goto_2
    new-array v1, v1, [Ljava/lang/Object;

    goto :goto_9

    nop

    :goto_3
    invoke-virtual {v1}, Lmiuix/animation/listener/EngineListener;->onComplete()V

    goto :goto_5

    nop

    :goto_4
    invoke-interface {v2, v1}, Ljava/util/Set;->remove(Ljava/lang/Object;)Z

    goto :goto_10

    nop

    :goto_5
    goto :goto_1b

    :goto_6
    goto :goto_2a

    nop

    :goto_7
    const-string p0, "- FolmeEngine.endAnim finish"

    goto :goto_31

    nop

    :goto_8
    if-nez v1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_32

    nop

    :goto_9
    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_a
    goto :goto_2c

    nop

    :goto_b
    if-nez v0, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_2b

    nop

    :goto_c
    if-eqz v2, :cond_2

    goto :goto_1f

    :cond_2
    goto :goto_b

    nop

    :goto_d
    if-nez v0, :cond_3

    goto :goto_21

    :cond_3
    goto :goto_7

    nop

    :goto_e
    invoke-virtual {p0}, Lmiuix/animation/internal/FolmeEngine;->stopNextFrame()V

    goto :goto_d

    nop

    :goto_f
    iput-wide v2, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J

    goto :goto_2d

    nop

    :goto_10
    goto :goto_2f

    :goto_11
    goto :goto_13

    nop

    :goto_12
    iput-boolean v1, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z

    goto :goto_e

    nop

    :goto_13
    iget-object v0, p0, Lmiuix/animation/internal/FolmeEngine;->mPendingRemoveEngineListener:Ljava/util/Set;

    goto :goto_0

    nop

    :goto_14
    const/4 v0, 0x0

    goto :goto_19

    nop

    :goto_15
    iget-object v0, p0, Lmiuix/animation/internal/FolmeEngine;->mEngineListener:Ljava/util/Set;

    goto :goto_1a

    nop

    :goto_16
    new-array v3, v1, [Ljava/lang/Object;

    goto :goto_33

    nop

    :goto_17
    const-string v2, "- FolmeEngine.endAnim start"

    goto :goto_16

    nop

    :goto_18
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_28

    nop

    :goto_19
    iput-object v0, p0, Lmiuix/animation/internal/FolmeEngine;->mPendingRemoveEngineListener:Ljava/util/Set;

    goto :goto_1e

    nop

    :goto_1a
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_1b
    goto :goto_25

    nop

    :goto_1c
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_29

    nop

    :goto_1d
    return-void

    :goto_1e
    return-void

    :goto_1f
    goto :goto_12

    nop

    :goto_20
    invoke-static {p0, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_21
    goto :goto_1d

    nop

    :goto_22
    if-nez v0, :cond_4

    goto :goto_34

    :cond_4
    goto :goto_17

    nop

    :goto_23
    check-cast v1, Lmiuix/animation/listener/EngineListener;

    goto :goto_3

    nop

    :goto_24
    iget-object v2, p0, Lmiuix/animation/internal/FolmeEngine;->mEngineListener:Ljava/util/Set;

    goto :goto_4

    nop

    :goto_25
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_8

    nop

    :goto_26
    const-wide/16 v2, 0x0

    goto :goto_f

    nop

    :goto_27
    if-nez v0, :cond_5

    goto :goto_21

    :cond_5
    goto :goto_2e

    nop

    :goto_28
    check-cast v1, Lmiuix/animation/listener/EngineListener;

    goto :goto_24

    nop

    :goto_29
    if-nez v1, :cond_6

    goto :goto_11

    :cond_6
    goto :goto_18

    nop

    :goto_2a
    iget-object v0, p0, Lmiuix/animation/internal/FolmeEngine;->mPendingRemoveEngineListener:Ljava/util/Set;

    goto :goto_27

    nop

    :goto_2b
    const-string v0, "- FolmeEngine.endAnim return when runner is not running"

    goto :goto_2

    nop

    :goto_2c
    invoke-virtual {p0}, Lmiuix/animation/internal/FolmeEngine;->stopNextFrame()V

    goto :goto_15

    nop

    :goto_2d
    iget-boolean v2, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z

    goto :goto_c

    nop

    :goto_2e
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_2f
    goto :goto_1c

    nop

    :goto_30
    const/4 v1, 0x0

    goto :goto_22

    nop

    :goto_31
    new-array v0, v1, [Ljava/lang/Object;

    goto :goto_20

    nop

    :goto_32
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_23

    nop

    :goto_33
    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_34
    goto :goto_26

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_FolmeEngine__startAnim',
        'method': '.method protected startAnim()V',
        'method_name': 'startAnim',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'if-eqz v0, :cond_0', 'const-string v2, "+ FolmeEngine.startAnim"', 'invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V', 'iget-boolean v2, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z', 'if-eqz v2, :cond_2', 'if-eqz v0, :cond_1', 'const-string p0, "+ FolmeEngine.startAnim but isRunning, return"'],
        'type': 'method_replace',
        'search': """.method protected startAnim()V
    .registers 5

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    const-string v2, "+ FolmeEngine.startAnim"

    new-array v3, v1, [Ljava/lang/Object;

    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    iget-boolean v2, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z

    if-eqz v2, :cond_2

    if-eqz v0, :cond_1

    const-string p0, "+ FolmeEngine.startAnim but isRunning, return"

    new-array v0, v1, [Ljava/lang/Object;

    invoke-static {p0, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    return-void

    :cond_2
    invoke-static {}, Lmiuix/animation/Folme;->getTimeRatio()F

    move-result v0

    iput v0, p0, Lmiuix/animation/internal/FolmeEngine;->mRatio:F

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z

    iget-object v0, p0, Lmiuix/animation/internal/FolmeEngine;->mEngineListener:Ljava/util/Set;

    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/animation/listener/EngineListener;

    invoke-virtual {v1}, Lmiuix/animation/listener/EngineListener;->onBegin()V

    goto :goto_0

    :cond_3
    const-wide/16 v0, 0x0

    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/FolmeEngine;->scheduleNextFrame(J)V

    return-void
.end method""",
        'replacement': """.method protected startAnim()V
    .registers 5

    goto :goto_0

    nop

    :goto_0
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_18

    nop

    :goto_1
    invoke-virtual {p0, v0, v1}, Lmiuix/animation/internal/FolmeEngine;->scheduleNextFrame(J)V

    goto :goto_3

    nop

    :goto_2
    new-array v3, v1, [Ljava/lang/Object;

    goto :goto_1f

    nop

    :goto_3
    return-void

    :goto_4
    iget-boolean v2, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z

    goto :goto_1e

    nop

    :goto_5
    const-string p0, "+ FolmeEngine.startAnim but isRunning, return"

    goto :goto_1b

    nop

    :goto_6
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_7

    nop

    :goto_7
    check-cast v1, Lmiuix/animation/listener/EngineListener;

    goto :goto_b

    nop

    :goto_8
    iput-boolean v0, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z

    goto :goto_13

    nop

    :goto_9
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_17

    nop

    :goto_a
    if-nez v0, :cond_0

    goto :goto_20

    :cond_0
    goto :goto_f

    nop

    :goto_b
    invoke-virtual {v1}, Lmiuix/animation/listener/EngineListener;->onBegin()V

    goto :goto_1c

    nop

    :goto_c
    invoke-static {p0, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_d
    goto :goto_15

    nop

    :goto_e
    if-nez v0, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_5

    nop

    :goto_f
    const-string v2, "+ FolmeEngine.startAnim"

    goto :goto_2

    nop

    :goto_10
    invoke-static {}, Lmiuix/animation/Folme;->getTimeRatio()F

    move-result v0

    goto :goto_14

    nop

    :goto_11
    const-wide/16 v0, 0x0

    goto :goto_1

    nop

    :goto_12
    const/4 v0, 0x1

    goto :goto_8

    nop

    :goto_13
    iget-object v0, p0, Lmiuix/animation/internal/FolmeEngine;->mEngineListener:Ljava/util/Set;

    goto :goto_19

    nop

    :goto_14
    iput v0, p0, Lmiuix/animation/internal/FolmeEngine;->mRatio:F

    goto :goto_12

    nop

    :goto_15
    return-void

    :goto_16
    goto :goto_10

    nop

    :goto_17
    if-nez v1, :cond_2

    goto :goto_1d

    :cond_2
    goto :goto_6

    nop

    :goto_18
    const/4 v1, 0x0

    goto :goto_a

    nop

    :goto_19
    invoke-interface {v0}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_1a
    goto :goto_9

    nop

    :goto_1b
    new-array v0, v1, [Ljava/lang/Object;

    goto :goto_c

    nop

    :goto_1c
    goto :goto_1a

    :goto_1d
    goto :goto_11

    nop

    :goto_1e
    if-nez v2, :cond_3

    goto :goto_16

    :cond_3
    goto :goto_e

    nop

    :goto_1f
    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_20
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_FolmeEngine__updateRunningTime',
        'method': '.method protected updateRunningTime(J)J',
        'method_name': 'updateRunningTime',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J', 'if-nez v4, :cond_0', 'iput-wide p1, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J', 'iput-wide p1, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J', 'iget p1, p0, Lmiuix/animation/internal/FolmeEngine;->mRecordCount:I', 'iget-object v4, p0, Lmiuix/animation/internal/FolmeEngine;->mDeltaRecord:[J', 'iput p1, p0, Lmiuix/animation/internal/FolmeEngine;->mRecordCount:I', 'invoke-direct {p0, v0, v1}, Lmiuix/animation/internal/FolmeEngine;->calculateAverageDelta(J)J'],
        'type': 'method_replace',
        'search': """.method protected updateRunningTime(J)J
    .registers 8

    iget-wide v0, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J

    const-wide/16 v2, 0x0

    cmp-long v4, v0, v2

    if-nez v4, :cond_0

    iput-wide p1, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J

    move-wide v0, v2

    goto :goto_0

    :cond_0
    sub-long v0, p1, v0

    iput-wide p1, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J

    :goto_0
    iget p1, p0, Lmiuix/animation/internal/FolmeEngine;->mRecordCount:I

    rem-int/lit8 p2, p1, 0x5

    iget-object v4, p0, Lmiuix/animation/internal/FolmeEngine;->mDeltaRecord:[J

    aput-wide v0, v4, p2

    add-int/lit8 p1, p1, 0x1

    iput p1, p0, Lmiuix/animation/internal/FolmeEngine;->mRecordCount:I

    invoke-direct {p0, v0, v1}, Lmiuix/animation/internal/FolmeEngine;->calculateAverageDelta(J)J

    move-result-wide p1

    iput-wide p1, p0, Lmiuix/animation/internal/FolmeEngine;->mAverageDeltaNanos:J

    invoke-static {}, Lmiuix/animation/physics/AnimationHandler;->getInstance()Lmiuix/animation/physics/AnimationHandler;

    move-result-object p1

    invoke-virtual {p1}, Lmiuix/animation/physics/AnimationHandler;->getFrameDeltaNanos()J

    move-result-wide p1

    cmp-long v2, p1, v2

    if-lez v2, :cond_1

    iput-wide p1, p0, Lmiuix/animation/internal/FolmeEngine;->mAverageDeltaNanos:J

    :cond_1
    return-wide v0
.end method""",
        'replacement': """.method protected updateRunningTime(J)J
    .registers 8

    goto :goto_12

    nop

    :goto_0
    iput p1, p0, Lmiuix/animation/internal/FolmeEngine;->mRecordCount:I

    goto :goto_14

    nop

    :goto_1
    if-eqz v4, :cond_0

    goto :goto_10

    :cond_0
    goto :goto_6

    nop

    :goto_2
    iget p1, p0, Lmiuix/animation/internal/FolmeEngine;->mRecordCount:I

    goto :goto_3

    nop

    :goto_3
    rem-int/lit8 p2, p1, 0x5

    goto :goto_5

    nop

    :goto_4
    cmp-long v2, p1, v2

    goto :goto_17

    nop

    :goto_5
    iget-object v4, p0, Lmiuix/animation/internal/FolmeEngine;->mDeltaRecord:[J

    goto :goto_13

    nop

    :goto_6
    iput-wide p1, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J

    goto :goto_16

    nop

    :goto_7
    cmp-long v4, v0, v2

    goto :goto_1

    nop

    :goto_8
    iput-wide p1, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J

    :goto_9
    goto :goto_2

    nop

    :goto_a
    sub-long v0, p1, v0

    goto :goto_8

    nop

    :goto_b
    add-int/lit8 p1, p1, 0x1

    goto :goto_0

    nop

    :goto_c
    iput-wide p1, p0, Lmiuix/animation/internal/FolmeEngine;->mAverageDeltaNanos:J

    goto :goto_e

    nop

    :goto_d
    return-wide v0

    :goto_e
    invoke-static {}, Lmiuix/animation/physics/AnimationHandler;->getInstance()Lmiuix/animation/physics/AnimationHandler;

    move-result-object p1

    goto :goto_15

    nop

    :goto_f
    goto :goto_9

    :goto_10
    goto :goto_a

    nop

    :goto_11
    const-wide/16 v2, 0x0

    goto :goto_7

    nop

    :goto_12
    iget-wide v0, p0, Lmiuix/animation/internal/FolmeEngine;->mLastFrameTimeNanos:J

    goto :goto_11

    nop

    :goto_13
    aput-wide v0, v4, p2

    goto :goto_b

    nop

    :goto_14
    invoke-direct {p0, v0, v1}, Lmiuix/animation/internal/FolmeEngine;->calculateAverageDelta(J)J

    move-result-wide p1

    goto :goto_c

    nop

    :goto_15
    invoke-virtual {p1}, Lmiuix/animation/physics/AnimationHandler;->getFrameDeltaNanos()J

    move-result-wide p1

    goto :goto_4

    nop

    :goto_16
    move-wide v0, v2

    goto :goto_f

    nop

    :goto_17
    if-gtz v2, :cond_1

    goto :goto_19

    :cond_1
    goto :goto_18

    nop

    :goto_18
    iput-wide p1, p0, Lmiuix/animation/internal/FolmeEngine;->mAverageDeltaNanos:J

    :goto_19
    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_FolmeEngine__waitAnim',
        'method': '.method protected waitAnim()V',
        'method_name': 'waitAnim',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'if-eqz v0, :cond_0', 'const-string v2, "- FolmeEngine.waitAnim start"', 'invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V', 'iput-boolean v1, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z', 'invoke-virtual {p0}, Lmiuix/animation/internal/FolmeEngine;->stopNextFrame()V', 'if-eqz v0, :cond_1', 'const-string p0, "- FolmeEngine.waitAnim finish"'],
        'type': 'method_replace',
        'search': """.method protected waitAnim()V
    .registers 5

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    const-string v2, "- FolmeEngine.waitAnim start"

    new-array v3, v1, [Ljava/lang/Object;

    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    iput-boolean v1, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z

    invoke-virtual {p0}, Lmiuix/animation/internal/FolmeEngine;->stopNextFrame()V

    if-eqz v0, :cond_1

    const-string p0, "- FolmeEngine.waitAnim finish"

    new-array v0, v1, [Ljava/lang/Object;

    invoke-static {p0, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected waitAnim()V
    .registers 5

    goto :goto_e

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/animation/internal/FolmeEngine;->stopNextFrame()V

    goto :goto_5

    nop

    :goto_1
    iput-boolean v1, p0, Lmiuix/animation/internal/FolmeEngine;->mIsRunning:Z

    goto :goto_0

    nop

    :goto_2
    new-array v0, v1, [Ljava/lang/Object;

    goto :goto_3

    nop

    :goto_3
    invoke-static {p0, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_4
    goto :goto_d

    nop

    :goto_5
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_c

    nop

    :goto_6
    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_7
    goto :goto_1

    nop

    :goto_8
    new-array v3, v1, [Ljava/lang/Object;

    goto :goto_6

    nop

    :goto_9
    if-nez v0, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_a

    nop

    :goto_a
    const-string v2, "- FolmeEngine.waitAnim start"

    goto :goto_8

    nop

    :goto_b
    const/4 v1, 0x0

    goto :goto_9

    nop

    :goto_c
    const-string p0, "- FolmeEngine.waitAnim finish"

    goto :goto_2

    nop

    :goto_d
    return-void

    :goto_e
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
