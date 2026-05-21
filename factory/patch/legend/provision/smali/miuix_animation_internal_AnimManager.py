TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/AnimManager.smali'
CLASS_FALLBACK_NAMES = ['AnimManager.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/animation/internal/TransitionInfo$IUpdateInfoCreator;']

PATCHES = [
    {
        'id': 'miuix_animation_internal_AnimManager__addToTransitionInfoList',
        'method': '.method addToTransitionInfoList(Ljava/util/List;)V',
        'method_name': 'addToTransitionInfoList',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z', 'const-string v1, "target="', 'const-string v2, "list.size="', 'if-eqz v0, :cond_0', 'new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-interface {p1}, Ljava/util/List;->size()I'],
        'type': 'method_replace',
        'search': """.method addToTransitionInfoList(Ljava/util/List;)V
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/List<",
            "Lmiuix/animation/internal/TransitionInfo;",
            ">;)V"
        }
    .end annotation

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    const-string v1, "target="

    const-string v2, "list.size="

    if-eqz v0, :cond_0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result v3

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v4, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    filled-new-array {v0, v3}, [Ljava/lang/Object;

    move-result-object v0

    const-string v3, "++++ addToTransitionInfoList before add"

    invoke-static {v3, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object v0

    invoke-interface {v0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :cond_1
    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_2

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lmiuix/animation/internal/TransitionInfo;

    invoke-virtual {v3}, Lmiuix/animation/internal/TransitionInfo;->hasUpdateInfo()Z

    move-result v4

    if-eqz v4, :cond_1

    invoke-interface {p1, v3}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_0

    :cond_2
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    if-eqz v0, :cond_3

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result p1

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    filled-new-array {p1, p0}, [Ljava/lang/Object;

    move-result-object p0

    const-string p1, "++++ addToTransitionInfoList after add"

    invoke-static {p1, p0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_3
    return-void
.end method""",
        'replacement': """.method addToTransitionInfoList(Ljava/util/List;)V
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/List<",
            "Lmiuix/animation/internal/TransitionInfo;",
            ">;)V"
        }
    .end annotation

    goto :goto_24

    nop

    :goto_0
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1e

    nop

    :goto_1
    if-nez v4, :cond_0

    goto :goto_1d

    :cond_0
    goto :goto_2c

    nop

    :goto_2
    const-string v2, "list.size="

    goto :goto_d

    nop

    :goto_3
    invoke-virtual {v0, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_4
    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_2e

    nop

    :goto_5
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_6
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_e

    nop

    :goto_7
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    goto :goto_1a

    nop

    :goto_8
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2a

    nop

    :goto_9
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_3

    nop

    :goto_a
    if-nez v0, :cond_1

    goto :goto_29

    :cond_1
    goto :goto_21

    nop

    :goto_b
    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_31

    nop

    :goto_c
    const-string v1, "target="

    goto :goto_2

    nop

    :goto_d
    if-nez v0, :cond_2

    goto :goto_19

    :cond_2
    goto :goto_27

    nop

    :goto_e
    filled-new-array {p1, p0}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_22

    nop

    :goto_f
    return-void

    :goto_10
    check-cast v3, Lmiuix/animation/internal/TransitionInfo;

    goto :goto_12

    nop

    :goto_11
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_12
    invoke-virtual {v3}, Lmiuix/animation/internal/TransitionInfo;->hasUpdateInfo()Z

    move-result v4

    goto :goto_1

    nop

    :goto_13
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    goto :goto_26

    nop

    :goto_14
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_b

    nop

    :goto_15
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_16

    nop

    :goto_16
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_11

    nop

    :goto_17
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_1b

    nop

    :goto_18
    invoke-static {v3, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_19
    goto :goto_17

    nop

    :goto_1a
    filled-new-array {v0, v3}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_33

    nop

    :goto_1b
    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object v0

    goto :goto_1c

    nop

    :goto_1c
    invoke-interface {v0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_1d
    goto :goto_13

    nop

    :goto_1e
    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result v3

    goto :goto_4

    nop

    :goto_1f
    goto :goto_1d

    :goto_20
    goto :goto_2b

    nop

    :goto_21
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_32

    nop

    :goto_22
    const-string p1, "++++ addToTransitionInfoList after add"

    goto :goto_28

    nop

    :goto_23
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    goto :goto_10

    nop

    :goto_24
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    goto :goto_c

    nop

    :goto_25
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_15

    nop

    :goto_26
    if-nez v3, :cond_3

    goto :goto_20

    :cond_3
    goto :goto_23

    nop

    :goto_27
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_30

    nop

    :goto_28
    invoke-static {p1, p0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_29
    goto :goto_f

    nop

    :goto_2a
    invoke-interface {p1}, Ljava/util/List;->size()I

    move-result p1

    goto :goto_2d

    nop

    :goto_2b
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    goto :goto_a

    nop

    :goto_2c
    invoke-interface {p1, v3}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_1f

    nop

    :goto_2d
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_25

    nop

    :goto_2e
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_2f

    nop

    :goto_2f
    new-instance v3, Ljava/lang/StringBuilder;

    goto :goto_14

    nop

    :goto_30
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_0

    nop

    :goto_31
    iget-object v4, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_5

    nop

    :goto_32
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_8

    nop

    :goto_33
    const-string v3, "++++ addToTransitionInfoList before add"

    goto :goto_18

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__cancelPrepareTransition',
        'method': '.method cancelPrepareTransition(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'cancelPrepareTransition',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;', 'iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I', 'invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-virtual {v0, v1}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;', 'iget-boolean v0, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z', 'if-nez v0, :cond_0', 'iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;', 'invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V'],
        'type': 'method_replace',
        'search': """.method cancelPrepareTransition(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 7

    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    iget-boolean v0, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    const/4 v1, 0x0

    if-nez v0, :cond_0

    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V

    :cond_0
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    invoke-virtual {v0}, Lmiuix/animation/controller/AnimState;->keySet()Ljava/util/Set;

    move-result-object v2

    invoke-interface {v2}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_0
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_1

    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    iget-object v4, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0, v4, v3}, Lmiuix/animation/controller/AnimState;->getProperty(Lmiuix/animation/IAnimTarget;Ljava/lang/Object;)Lmiuix/animation/property/FloatProperty;

    move-result-object v3

    invoke-virtual {p0, v3}, Lmiuix/animation/internal/AnimManager;->getUpdateInfo(Lmiuix/animation/property/FloatProperty;)Lmiuix/animation/listener/UpdateInfo;

    move-result-object v3

    const/4 v4, 0x0

    iput-object v4, v3, Lmiuix/animation/listener/UpdateInfo;->preparedTransitionId:Ljava/lang/Integer;

    const/4 v3, 0x3

    iput-byte v3, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    goto :goto_0

    :cond_1
    const/4 v0, 0x2

    const/4 v1, 0x4

    invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionEndOrCancel(Lmiuix/animation/internal/TransitionInfo;II)V

    return-void
.end method""",
        'replacement': """.method cancelPrepareTransition(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 7

    goto :goto_17

    nop

    :goto_0
    const/4 v4, 0x0

    goto :goto_1e

    nop

    :goto_1
    invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionEndOrCancel(Lmiuix/animation/internal/TransitionInfo;II)V

    goto :goto_1d

    nop

    :goto_2
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_b

    nop

    :goto_3
    invoke-virtual {p0, v3}, Lmiuix/animation/internal/AnimManager;->getUpdateInfo(Lmiuix/animation/property/FloatProperty;)Lmiuix/animation/listener/UpdateInfo;

    move-result-object v3

    goto :goto_0

    nop

    :goto_4
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    goto :goto_d

    nop

    :goto_5
    if-nez v3, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_19

    nop

    :goto_6
    iget-boolean v0, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    goto :goto_1b

    nop

    :goto_7
    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    goto :goto_8

    nop

    :goto_8
    goto :goto_11

    :goto_9
    goto :goto_1c

    nop

    :goto_a
    iget-object v4, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_1a

    nop

    :goto_b
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_f

    nop

    :goto_c
    const/4 v3, 0x3

    goto :goto_12

    nop

    :goto_d
    invoke-virtual {v0}, Lmiuix/animation/controller/AnimState;->keySet()Ljava/util/Set;

    move-result-object v2

    goto :goto_10

    nop

    :goto_e
    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    goto :goto_7

    nop

    :goto_f
    invoke-virtual {v0, v1}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_6

    nop

    :goto_10
    invoke-interface {v2}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_11
    goto :goto_16

    nop

    :goto_12
    iput-byte v3, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    goto :goto_e

    nop

    :goto_13
    invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V

    :goto_14
    goto :goto_4

    nop

    :goto_15
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    goto :goto_13

    nop

    :goto_16
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    goto :goto_5

    nop

    :goto_17
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_2

    nop

    :goto_18
    const/4 v1, 0x4

    goto :goto_1

    nop

    :goto_19
    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    goto :goto_a

    nop

    :goto_1a
    invoke-virtual {v0, v4, v3}, Lmiuix/animation/controller/AnimState;->getProperty(Lmiuix/animation/IAnimTarget;Ljava/lang/Object;)Lmiuix/animation/property/FloatProperty;

    move-result-object v3

    goto :goto_3

    nop

    :goto_1b
    const/4 v1, 0x0

    goto :goto_1f

    nop

    :goto_1c
    const/4 v0, 0x2

    goto :goto_18

    nop

    :goto_1d
    return-void

    :goto_1e
    iput-object v4, v3, Lmiuix/animation/listener/UpdateInfo;->preparedTransitionId:Ljava/lang/Integer;

    goto :goto_c

    nop

    :goto_1f
    if-eqz v0, :cond_1

    goto :goto_14

    :cond_1
    goto :goto_15

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__endPrepareTransition',
        'method': '.method endPrepareTransition(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'endPrepareTransition',
        'method_anchors': ['invoke-virtual {p1, p0}, Lmiuix/animation/internal/TransitionInfo;->initUpdateList(Lmiuix/animation/internal/TransitionInfo$IUpdateInfoCreator;)Z', 'iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;', 'iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I', 'invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-virtual {v0, v1}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;', 'iget-boolean v0, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z', 'if-nez v0, :cond_0', 'iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;'],
        'type': 'method_replace',
        'search': """.method endPrepareTransition(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 10

    invoke-virtual {p1, p0}, Lmiuix/animation/internal/TransitionInfo;->initUpdateList(Lmiuix/animation/internal/TransitionInfo$IUpdateInfoCreator;)Z

    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    iget-boolean v0, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    const/4 v1, 0x0

    if-nez v0, :cond_0

    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V

    :cond_0
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->updateListForNotify:Ljava/util/List;

    invoke-interface {v2}, Ljava/util/List;->clear()V

    invoke-virtual {v0}, Lmiuix/animation/controller/AnimState;->keySet()Ljava/util/Set;

    move-result-object v2

    invoke-interface {v2}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_0
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_2

    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    iget-object v4, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0, v4, v3}, Lmiuix/animation/controller/AnimState;->getProperty(Lmiuix/animation/IAnimTarget;Ljava/lang/Object;)Lmiuix/animation/property/FloatProperty;

    move-result-object v3

    invoke-virtual {p0, v3}, Lmiuix/animation/internal/AnimManager;->getUpdateInfo(Lmiuix/animation/property/FloatProperty;)Lmiuix/animation/listener/UpdateInfo;

    move-result-object v4

    iget-object v5, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0, v5, v3}, Lmiuix/animation/controller/AnimState;->get(Lmiuix/animation/IAnimTarget;Lmiuix/animation/property/FloatProperty;)D

    move-result-wide v5

    instance-of v7, v3, Lmiuix/animation/property/IIntValueProperty;

    if-eqz v7, :cond_1

    iget-object v7, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    check-cast v3, Lmiuix/animation/property/IIntValueProperty;

    double-to-int v5, v5

    invoke-virtual {v7, v3, v5}, Lmiuix/animation/IAnimTarget;->setIntValue(Lmiuix/animation/property/IIntValueProperty;I)V

    goto :goto_1

    :cond_1
    iget-object v7, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    double-to-float v5, v5

    invoke-virtual {v7, v3, v5}, Lmiuix/animation/IAnimTarget;->setValue(Lmiuix/animation/property/FloatProperty;F)V

    :goto_1
    iget-object v3, p1, Lmiuix/animation/internal/TransitionInfo;->updateListForNotify:Ljava/util/List;

    invoke-interface {v3, v4}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    const/4 v3, 0x0

    iput-object v3, v4, Lmiuix/animation/listener/UpdateInfo;->preparedTransitionId:Ljava/lang/Integer;

    const/4 v3, 0x4

    iput-byte v3, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    goto :goto_0

    :cond_2
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateListForNotify:Ljava/util/List;

    invoke-virtual {p0, p1, v0}, Lmiuix/animation/internal/AnimManager;->notifyTransitionUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V

    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateListForNotify:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->clear()V

    const/4 v0, 0x2

    const/4 v1, 0x3

    invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionEndOrCancel(Lmiuix/animation/internal/TransitionInfo;II)V

    return-void
.end method""",
        'replacement': """.method endPrepareTransition(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 10

    goto :goto_25

    nop

    :goto_0
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_30

    nop

    :goto_1
    invoke-interface {v0}, Ljava/util/List;->clear()V

    goto :goto_19

    nop

    :goto_2
    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->updateListForNotify:Ljava/util/List;

    goto :goto_17

    nop

    :goto_3
    if-nez v7, :cond_0

    goto :goto_2c

    :cond_0
    goto :goto_20

    nop

    :goto_4
    iget-object v5, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_2a

    nop

    :goto_5
    double-to-float v5, v5

    goto :goto_31

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_33

    nop

    :goto_7
    invoke-virtual {p0, v3}, Lmiuix/animation/internal/AnimManager;->getUpdateInfo(Lmiuix/animation/property/FloatProperty;)Lmiuix/animation/listener/UpdateInfo;

    move-result-object v4

    goto :goto_4

    nop

    :goto_8
    return-void

    :goto_9
    const/4 v1, 0x3

    goto :goto_1d

    nop

    :goto_a
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    goto :goto_b

    nop

    :goto_b
    if-nez v3, :cond_1

    goto :goto_f

    :cond_1
    goto :goto_18

    nop

    :goto_c
    invoke-virtual {v7, v3, v5}, Lmiuix/animation/IAnimTarget;->setIntValue(Lmiuix/animation/property/IIntValueProperty;I)V

    goto :goto_2b

    nop

    :goto_d
    invoke-virtual {v0, v4, v3}, Lmiuix/animation/controller/AnimState;->getProperty(Lmiuix/animation/IAnimTarget;Ljava/lang/Object;)Lmiuix/animation/property/FloatProperty;

    move-result-object v3

    goto :goto_7

    nop

    :goto_e
    goto :goto_15

    :goto_f
    goto :goto_10

    nop

    :goto_10
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateListForNotify:Ljava/util/List;

    goto :goto_35

    nop

    :goto_11
    invoke-virtual {v0}, Lmiuix/animation/controller/AnimState;->keySet()Ljava/util/Set;

    move-result-object v2

    goto :goto_14

    nop

    :goto_12
    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    goto :goto_1e

    nop

    :goto_13
    double-to-int v5, v5

    goto :goto_c

    nop

    :goto_14
    invoke-interface {v2}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_15
    goto :goto_a

    nop

    :goto_16
    const/4 v3, 0x4

    goto :goto_1a

    nop

    :goto_17
    invoke-interface {v2}, Ljava/util/List;->clear()V

    goto :goto_11

    nop

    :goto_18
    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    goto :goto_22

    nop

    :goto_19
    const/4 v0, 0x2

    goto :goto_9

    nop

    :goto_1a
    iput-byte v3, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    goto :goto_12

    nop

    :goto_1b
    invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V

    :goto_1c
    goto :goto_2d

    nop

    :goto_1d
    invoke-virtual {p0, p1, v0, v1}, Lmiuix/animation/internal/AnimManager;->notifyTransitionEndOrCancel(Lmiuix/animation/internal/TransitionInfo;II)V

    goto :goto_8

    nop

    :goto_1e
    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    goto :goto_e

    nop

    :goto_1f
    const/4 v1, 0x0

    goto :goto_2f

    nop

    :goto_20
    iget-object v7, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_2e

    nop

    :goto_21
    invoke-interface {v3, v4}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_24

    nop

    :goto_22
    iget-object v4, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_d

    nop

    :goto_23
    iget-boolean v0, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    goto :goto_1f

    nop

    :goto_24
    const/4 v3, 0x0

    goto :goto_29

    nop

    :goto_25
    invoke-virtual {p1, p0}, Lmiuix/animation/internal/TransitionInfo;->initUpdateList(Lmiuix/animation/internal/TransitionInfo$IUpdateInfoCreator;)Z

    goto :goto_6

    nop

    :goto_26
    iget-object v3, p1, Lmiuix/animation/internal/TransitionInfo;->updateListForNotify:Ljava/util/List;

    goto :goto_21

    nop

    :goto_27
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    goto :goto_1b

    nop

    :goto_28
    iget-object v7, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_5

    nop

    :goto_29
    iput-object v3, v4, Lmiuix/animation/listener/UpdateInfo;->preparedTransitionId:Ljava/lang/Integer;

    goto :goto_16

    nop

    :goto_2a
    invoke-virtual {v0, v5, v3}, Lmiuix/animation/controller/AnimState;->get(Lmiuix/animation/IAnimTarget;Lmiuix/animation/property/FloatProperty;)D

    move-result-wide v5

    goto :goto_34

    nop

    :goto_2b
    goto :goto_32

    :goto_2c
    goto :goto_28

    nop

    :goto_2d
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    goto :goto_2

    nop

    :goto_2e
    check-cast v3, Lmiuix/animation/property/IIntValueProperty;

    goto :goto_13

    nop

    :goto_2f
    if-eqz v0, :cond_2

    goto :goto_1c

    :cond_2
    goto :goto_27

    nop

    :goto_30
    invoke-virtual {v0, v1}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_23

    nop

    :goto_31
    invoke-virtual {v7, v3, v5}, Lmiuix/animation/IAnimTarget;->setValue(Lmiuix/animation/property/FloatProperty;F)V

    :goto_32
    goto :goto_26

    nop

    :goto_33
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_0

    nop

    :goto_34
    instance-of v7, v3, Lmiuix/animation/property/IIntValueProperty;

    goto :goto_3

    nop

    :goto_35
    invoke-virtual {p0, p1, v0}, Lmiuix/animation/internal/AnimManager;->notifyTransitionUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V

    goto :goto_36

    nop

    :goto_36
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateListForNotify:Ljava/util/List;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__getPrepareTransInfoByToState',
        'method': '.method getPrepareTransInfoByToState(Lmiuix/animation/controller/AnimState;)Lmiuix/animation/internal/TransitionInfo;',
        'method_name': 'getPrepareTransInfoByToState',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z', 'iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;', 'invoke-virtual {p0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;', 'invoke-interface {p0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;', 'invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_3', 'invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v1, Lmiuix/animation/internal/TransitionInfo;'],
        'type': 'method_replace',
        'search': """.method getPrepareTransInfoByToState(Lmiuix/animation/controller/AnimState;)Lmiuix/animation/internal/TransitionInfo;
    .registers 7

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {p0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object p0

    invoke-interface {p0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :cond_0
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/animation/internal/TransitionInfo;

    iget-object v2, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    const/4 v3, 0x0

    if-ne v2, p1, :cond_1

    if-eqz v0, :cond_2

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "getPrepareTransInfoByToState info.to == toState: "

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    new-array p1, v3, [Ljava/lang/Object;

    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    return-object v1

    :cond_1
    iget-boolean v2, p1, Lmiuix/animation/controller/AnimState;->needDuplicate:Z

    if-eqz v2, :cond_0

    iget-object v2, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    invoke-virtual {v2}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;

    move-result-object v2

    invoke-virtual {p1}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;

    move-result-object v4

    invoke-virtual {v2, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_0

    if-eqz v0, :cond_2

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string p1, "getPrepareTransInfoByToState info.to != toState: "

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p1, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    new-array p1, v3, [Ljava/lang/Object;

    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_2
    return-object v1

    :cond_3
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method getPrepareTransInfoByToState(Lmiuix/animation/controller/AnimState;)Lmiuix/animation/internal/TransitionInfo;
    .registers 7

    goto :goto_29

    nop

    :goto_0
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_14

    nop

    :goto_2
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_15

    nop

    :goto_3
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_4
    iget-object p1, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    goto :goto_5

    nop

    :goto_5
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_6
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_20

    nop

    :goto_7
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_8
    invoke-virtual {v2}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;

    move-result-object v2

    goto :goto_1c

    nop

    :goto_9
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_2a

    nop

    :goto_a
    const-string p1, "getPrepareTransInfoByToState info.to != toState: "

    goto :goto_3

    nop

    :goto_b
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_a

    nop

    :goto_c
    return-object v1

    :goto_d
    goto :goto_12

    nop

    :goto_e
    if-nez v0, :cond_0

    goto :goto_17

    :cond_0
    goto :goto_13

    nop

    :goto_f
    iget-object v2, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    goto :goto_8

    nop

    :goto_10
    invoke-virtual {v2, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v2

    goto :goto_19

    nop

    :goto_11
    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_c

    nop

    :goto_12
    iget-boolean v2, p1, Lmiuix/animation/controller/AnimState;->needDuplicate:Z

    goto :goto_2c

    nop

    :goto_13
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_b

    nop

    :goto_14
    new-array p1, v3, [Ljava/lang/Object;

    goto :goto_11

    nop

    :goto_15
    check-cast v1, Lmiuix/animation/internal/TransitionInfo;

    goto :goto_2b

    nop

    :goto_16
    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_17
    goto :goto_21

    nop

    :goto_18
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_1a

    nop

    :goto_19
    if-nez v2, :cond_1

    goto :goto_24

    :cond_1
    goto :goto_e

    nop

    :goto_1a
    invoke-virtual {p0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object p0

    goto :goto_23

    nop

    :goto_1b
    const/4 p0, 0x0

    goto :goto_27

    nop

    :goto_1c
    invoke-virtual {p1}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;

    move-result-object v4

    goto :goto_10

    nop

    :goto_1d
    if-nez v1, :cond_2

    goto :goto_22

    :cond_2
    goto :goto_2

    nop

    :goto_1e
    if-nez v0, :cond_3

    goto :goto_17

    :cond_3
    goto :goto_9

    nop

    :goto_1f
    const/4 v3, 0x0

    goto :goto_25

    nop

    :goto_20
    new-array p1, v3, [Ljava/lang/Object;

    goto :goto_16

    nop

    :goto_21
    return-object v1

    :goto_22
    goto :goto_1b

    nop

    :goto_23
    invoke-interface {p0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :goto_24
    goto :goto_26

    nop

    :goto_25
    if-eq v2, p1, :cond_4

    goto :goto_d

    :cond_4
    goto :goto_1e

    nop

    :goto_26
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_1d

    nop

    :goto_27
    return-object p0

    :goto_28
    const-string v0, "getPrepareTransInfoByToState info.to == toState: "

    goto :goto_7

    nop

    :goto_29
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    goto :goto_18

    nop

    :goto_2a
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_28

    nop

    :goto_2b
    iget-object v2, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    goto :goto_1f

    nop

    :goto_2c
    if-nez v2, :cond_5

    goto :goto_24

    :cond_5
    goto :goto_f

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__getRunningTransInfoByToState',
        'method': '.method getRunningTransInfoByToState(Lmiuix/animation/controller/AnimState;)Lmiuix/animation/internal/TransitionInfo;',
        'method_name': 'getRunningTransInfoByToState',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z', 'iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;', 'invoke-virtual {p0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;', 'invoke-interface {p0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;', 'invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_3', 'invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v1, Lmiuix/animation/internal/TransitionInfo;'],
        'type': 'method_replace',
        'search': """.method getRunningTransInfoByToState(Lmiuix/animation/controller/AnimState;)Lmiuix/animation/internal/TransitionInfo;
    .registers 7

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {p0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object p0

    invoke-interface {p0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :cond_0
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/animation/internal/TransitionInfo;

    iget-object v2, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    const/4 v3, 0x0

    if-ne v2, p1, :cond_1

    if-eqz v0, :cond_2

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "getRunningTransInfoByToState info.to == toState: "

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    new-array p1, v3, [Ljava/lang/Object;

    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    return-object v1

    :cond_1
    iget-boolean v2, p1, Lmiuix/animation/controller/AnimState;->needDuplicate:Z

    if-eqz v2, :cond_0

    iget-object v2, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    invoke-virtual {v2}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;

    move-result-object v2

    invoke-virtual {p1}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;

    move-result-object v4

    invoke-virtual {v2, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_0

    if-eqz v0, :cond_2

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string p1, "getRunningTransInfoByToState info.to != toState: "

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p1, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    new-array p1, v3, [Ljava/lang/Object;

    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_2
    return-object v1

    :cond_3
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method getRunningTransInfoByToState(Lmiuix/animation/controller/AnimState;)Lmiuix/animation/internal/TransitionInfo;
    .registers 7

    goto :goto_24

    nop

    :goto_0
    if-nez v2, :cond_0

    goto :goto_26

    :cond_0
    goto :goto_23

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_1d

    nop

    :goto_2
    invoke-virtual {v2}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;

    move-result-object v2

    goto :goto_1e

    nop

    :goto_3
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_14

    nop

    :goto_4
    if-nez v1, :cond_1

    goto :goto_29

    :cond_1
    goto :goto_12

    nop

    :goto_5
    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_6
    goto :goto_28

    nop

    :goto_7
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_10

    nop

    :goto_8
    return-object v1

    :goto_9
    goto :goto_15

    nop

    :goto_a
    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_8

    nop

    :goto_b
    iget-object v2, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    goto :goto_2

    nop

    :goto_c
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_4

    nop

    :goto_d
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_27

    nop

    :goto_e
    const/4 v3, 0x0

    goto :goto_2c

    nop

    :goto_f
    invoke-virtual {v2, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v2

    goto :goto_0

    nop

    :goto_10
    new-array p1, v3, [Ljava/lang/Object;

    goto :goto_a

    nop

    :goto_11
    iget-object v2, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    goto :goto_e

    nop

    :goto_12
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_1f

    nop

    :goto_13
    const/4 p0, 0x0

    goto :goto_22

    nop

    :goto_14
    const-string v0, "getRunningTransInfoByToState info.to == toState: "

    goto :goto_1a

    nop

    :goto_15
    iget-boolean v2, p1, Lmiuix/animation/controller/AnimState;->needDuplicate:Z

    goto :goto_2a

    nop

    :goto_16
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_d

    nop

    :goto_17
    new-array p1, v3, [Ljava/lang/Object;

    goto :goto_5

    nop

    :goto_18
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_17

    nop

    :goto_19
    if-nez v0, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_21

    nop

    :goto_1a
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1b

    nop

    :goto_1b
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_1c
    iget-object p1, v1, Lmiuix/animation/internal/TransitionInfo;->to:Lmiuix/animation/controller/AnimState;

    goto :goto_2b

    nop

    :goto_1d
    invoke-virtual {p0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object p0

    goto :goto_25

    nop

    :goto_1e
    invoke-virtual {p1}, Lmiuix/animation/controller/AnimState;->getTag()Ljava/lang/Object;

    move-result-object v4

    goto :goto_f

    nop

    :goto_1f
    check-cast v1, Lmiuix/animation/internal/TransitionInfo;

    goto :goto_11

    nop

    :goto_20
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1c

    nop

    :goto_21
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_3

    nop

    :goto_22
    return-object p0

    :goto_23
    if-nez v0, :cond_3

    goto :goto_6

    :cond_3
    goto :goto_16

    nop

    :goto_24
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    goto :goto_1

    nop

    :goto_25
    invoke-interface {p0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :goto_26
    goto :goto_c

    nop

    :goto_27
    const-string p1, "getRunningTransInfoByToState info.to != toState: "

    goto :goto_20

    nop

    :goto_28
    return-object v1

    :goto_29
    goto :goto_13

    nop

    :goto_2a
    if-nez v2, :cond_4

    goto :goto_26

    :cond_4
    goto :goto_b

    nop

    :goto_2b
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_18

    nop

    :goto_2c
    if-eq v2, p1, :cond_5

    goto :goto_9

    :cond_5
    goto :goto_19

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__notifyReplaceTargetListeners',
        'method': '.method notifyReplaceTargetListeners(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'notifyReplaceTargetListeners',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;', 'invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0}, Lmiuix/animation/internal/TargetHandler;->isInTargetThread()Z', 'if-eqz v1, :cond_0', 'iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;', 'iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I', 'invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;'],
        'type': 'method_replace',
        'search': """.method notifyReplaceTargetListeners(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 4

    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;

    move-result-object v0

    if-eqz v0, :cond_1

    invoke-virtual {v0}, Lmiuix/animation/internal/TargetHandler;->isInTargetThread()Z

    move-result v1

    if-eqz v1, :cond_0

    goto :goto_0

    :cond_0
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-interface {p0, v1, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    const/4 p1, 0x0

    const/4 v1, 0x4

    invoke-virtual {v0, v1, p0, p1}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;

    move-result-object p0

    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    return-void

    :cond_1
    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimManager;->onReplaceListeners(Lmiuix/animation/internal/TransitionInfo;)V

    return-void
.end method""",
        'replacement': """.method notifyReplaceTargetListeners(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 4

    goto :goto_6

    nop

    :goto_0
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_3

    nop

    :goto_1
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {v0, v1, p0, p1}, Landroid/os/Handler;->obtainMessage(III)Landroid/os/Message;

    move-result-object p0

    goto :goto_c

    nop

    :goto_3
    invoke-interface {p0, v1, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_10

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_f

    nop

    :goto_5
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimManager;->onReplaceListeners(Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_8

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_11

    nop

    :goto_7
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;

    goto :goto_1

    nop

    :goto_8
    return-void

    :goto_9
    const/4 p1, 0x0

    goto :goto_b

    nop

    :goto_a
    if-nez v1, :cond_1

    goto :goto_13

    :cond_1
    goto :goto_12

    nop

    :goto_b
    const/4 v1, 0x4

    goto :goto_2

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_d

    nop

    :goto_d
    return-void

    :goto_e
    goto :goto_5

    nop

    :goto_f
    invoke-virtual {v0}, Lmiuix/animation/internal/TargetHandler;->isInTargetThread()Z

    move-result v1

    goto :goto_a

    nop

    :goto_10
    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_9

    nop

    :goto_11
    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;

    move-result-object v0

    goto :goto_4

    nop

    :goto_12
    goto :goto_e

    :goto_13
    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__notifyTransitionBegin',
        'method': '.method notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V',
        'method_name': 'notifyTransitionBegin',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;', 'invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;', 'iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z', 'iput-byte v1, p1, Lmiuix/animation/internal/TransitionInfo;->state:B', 'iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;', 'invoke-virtual {v1}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;', 'if-eqz v1, :cond_1', 'if-nez p2, :cond_0'],
        'type': 'method_replace',
        'search': """.method notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V
    .registers 11
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lmiuix/animation/internal/TransitionInfo;",
            "Ljava/util/List<",
            "Lmiuix/animation/listener/UpdateInfo;",
            ">;Z)V"
        }
    .end annotation

    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;

    move-result-object v0

    const/4 v1, 0x1

    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    const/4 v1, 0x2

    iput-byte v1, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v1}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v1

    const/4 v2, 0x0

    const/4 v3, 0x0

    if-eqz v1, :cond_1

    if-nez p2, :cond_0

    move-object v1, v3

    goto :goto_0

    :cond_0
    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1, p2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_0
    iget-object v4, p0, Lmiuix/animation/internal/AnimManager;->mObserverHandlerMap:Ljava/util/concurrent/ConcurrentHashMap;

    iget-object v5, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v5}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v5

    invoke-virtual {v5}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/Thread;->getId()J

    move-result-wide v5

    invoke-static {v5, v6}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v5

    invoke-virtual {v4, v5}, Ljava/util/concurrent/ConcurrentHashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v4

    check-cast v4, Lmiuix/animation/internal/TargetHandler;

    if-eqz v4, :cond_1

    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;

    iget p2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    invoke-interface {p0, p2, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v4, v2, p0, p3, v1}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    return-void

    :cond_1
    if-eqz v0, :cond_4

    invoke-virtual {v0}, Lmiuix/animation/internal/TargetHandler;->isInTargetThread()Z

    move-result v1

    if-eqz v1, :cond_2

    goto :goto_2

    :cond_2
    if-nez p2, :cond_3

    goto :goto_1

    :cond_3
    new-instance v3, Ljava/util/ArrayList;

    invoke-direct {v3, p2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_1
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;

    iget p2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    invoke-interface {p0, p2, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v0, v2, p0, p3, v3}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    return-void

    :cond_4
    :goto_2
    invoke-virtual {p0, p1, p2, p3}, Lmiuix/animation/internal/AnimManager;->onStart(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V

    return-void
.end method""",
        'replacement': """.method notifyTransitionBegin(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V
    .registers 11
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lmiuix/animation/internal/TransitionInfo;",
            "Ljava/util/List<",
            "Lmiuix/animation/listener/UpdateInfo;",
            ">;Z)V"
        }
    .end annotation

    goto :goto_10

    nop

    :goto_0
    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_1f

    nop

    :goto_1
    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_2b

    nop

    :goto_2
    const/4 v3, 0x0

    goto :goto_33

    nop

    :goto_3
    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    goto :goto_b

    nop

    :goto_4
    invoke-direct {v1, p2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_5
    goto :goto_14

    nop

    :goto_6
    goto :goto_37

    :goto_7
    goto :goto_32

    nop

    :goto_8
    goto :goto_21

    :goto_9
    goto :goto_13

    nop

    :goto_a
    const/4 v2, 0x0

    goto :goto_2

    nop

    :goto_b
    const/4 v1, 0x2

    goto :goto_22

    nop

    :goto_c
    invoke-interface {p0, p2, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_e

    nop

    :goto_d
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;

    goto :goto_34

    nop

    :goto_e
    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_19

    nop

    :goto_f
    iget-object v5, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_1c

    nop

    :goto_10
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_35

    nop

    :goto_11
    goto :goto_5

    :goto_12
    goto :goto_16

    nop

    :goto_13
    if-eqz p2, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_6

    nop

    :goto_14
    iget-object v4, p0, Lmiuix/animation/internal/AnimManager;->mObserverHandlerMap:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_f

    nop

    :goto_15
    return-void

    :goto_16
    new-instance v1, Ljava/util/ArrayList;

    goto :goto_4

    nop

    :goto_17
    iget p2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_30

    nop

    :goto_18
    check-cast v4, Lmiuix/animation/internal/TargetHandler;

    goto :goto_28

    nop

    :goto_19
    invoke-virtual {v4, v2, p0, p3, v1}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    goto :goto_2a

    nop

    :goto_1a
    invoke-virtual {v4, v5}, Ljava/util/concurrent/ConcurrentHashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v4

    goto :goto_18

    nop

    :goto_1b
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;

    goto :goto_17

    nop

    :goto_1c
    invoke-virtual {v5}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v5

    goto :goto_29

    nop

    :goto_1d
    invoke-virtual {v5}, Ljava/lang/Thread;->getId()J

    move-result-wide v5

    goto :goto_2c

    nop

    :goto_1e
    if-nez v1, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_8

    nop

    :goto_1f
    invoke-virtual {v0, v2, p0, p3, v3}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    goto :goto_38

    nop

    :goto_20
    return-void

    :goto_21
    goto :goto_31

    nop

    :goto_22
    iput-byte v1, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    goto :goto_1

    nop

    :goto_23
    invoke-virtual {v0}, Lmiuix/animation/internal/TargetHandler;->isInTargetThread()Z

    move-result v1

    goto :goto_1e

    nop

    :goto_24
    if-eqz p2, :cond_2

    goto :goto_12

    :cond_2
    goto :goto_27

    nop

    :goto_25
    const/4 v1, 0x1

    goto :goto_3

    nop

    :goto_26
    invoke-interface {p0, p2, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_0

    nop

    :goto_27
    move-object v1, v3

    goto :goto_11

    nop

    :goto_28
    if-nez v4, :cond_3

    goto :goto_2e

    :cond_3
    goto :goto_d

    nop

    :goto_29
    invoke-virtual {v5}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v5

    goto :goto_1d

    nop

    :goto_2a
    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_2d

    nop

    :goto_2b
    invoke-virtual {v1}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v1

    goto :goto_a

    nop

    :goto_2c
    invoke-static {v5, v6}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v5

    goto :goto_1a

    nop

    :goto_2d
    return-void

    :goto_2e
    goto :goto_2f

    nop

    :goto_2f
    if-nez v0, :cond_4

    goto :goto_21

    :cond_4
    goto :goto_23

    nop

    :goto_30
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    goto :goto_26

    nop

    :goto_31
    invoke-virtual {p0, p1, p2, p3}, Lmiuix/animation/internal/AnimManager;->onStart(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V

    goto :goto_15

    nop

    :goto_32
    new-instance v3, Ljava/util/ArrayList;

    goto :goto_36

    nop

    :goto_33
    if-nez v1, :cond_5

    goto :goto_2e

    :cond_5
    goto :goto_24

    nop

    :goto_34
    iget p2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_39

    nop

    :goto_35
    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;

    move-result-object v0

    goto :goto_25

    nop

    :goto_36
    invoke-direct {v3, p2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_37
    goto :goto_1b

    nop

    :goto_38
    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_20

    nop

    :goto_39
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__notifyTransitionEndOrCancel',
        'method': '.method notifyTransitionEndOrCancel(Lmiuix/animation/internal/TransitionInfo;II)V',
        'method_name': 'notifyTransitionEndOrCancel',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;', 'invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;', 'iget-byte v1, p1, Lmiuix/animation/internal/TransitionInfo;->state:B', 'if-lt v1, v2, :cond_5', 'invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'if-eqz v1, :cond_0', 'invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;'],
        'type': 'method_replace',
        'search': """.method notifyTransitionEndOrCancel(Lmiuix/animation/internal/TransitionInfo;II)V
    .registers 8

    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;

    move-result-object v0

    iget-byte v1, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    const/4 v2, 0x2

    const/4 v3, 0x0

    if-lt v1, v2, :cond_5

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    filled-new-array {v1, v2, p1}, [Ljava/lang/Object;

    move-result-object v1

    const-string v2, "------ do notifyTransEndOrCancel after start, msg=%d, op=%d, info=%s"

    invoke-static {v2, v1}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    new-array v2, v3, [Ljava/lang/Object;

    invoke-static {v1, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimManager;->removeRunningInfo(Lmiuix/animation/internal/TransitionInfo;)V

    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v1}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v1

    if-eqz v1, :cond_1

    iget-object v1, p0, Lmiuix/animation/internal/AnimManager;->mObserverHandlerMap:Ljava/util/concurrent/ConcurrentHashMap;

    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v2}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v2

    invoke-virtual {v2}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Thread;->getId()J

    move-result-wide v2

    invoke-static {v2, v3}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/util/concurrent/ConcurrentHashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/animation/internal/TargetHandler;

    if-eqz v1, :cond_1

    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;

    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    invoke-interface {p0, v0, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v1, p2, p0, p3, p1}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    return-void

    :cond_1
    if-eqz v0, :cond_3

    invoke-virtual {v0}, Lmiuix/animation/internal/TargetHandler;->isInTargetThread()Z

    move-result v1

    if-eqz v1, :cond_2

    goto :goto_0

    :cond_2
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-interface {p0, v1, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v0, p2, p0, p3, p1}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    return-void

    :cond_3
    :goto_0
    const/4 v0, 0x5

    if-ne p2, v0, :cond_4

    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimManager;->onReplaced(Lmiuix/animation/internal/TransitionInfo;)V

    return-void

    :cond_4
    invoke-virtual {p0, p1, p3}, Lmiuix/animation/internal/AnimManager;->onEnd(Lmiuix/animation/internal/TransitionInfo;I)V

    return-void

    :cond_5
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    if-eqz v0, :cond_6

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p3

    filled-new-array {p2, p3, p1}, [Ljava/lang/Object;

    move-result-object p2

    const-string p3, "------ do notifyTransEndOrCancel before start, msg=%d, op=%d, info=%s"

    invoke-static {p3, p2}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p2

    new-array p3, v3, [Ljava/lang/Object;

    invoke-static {p2, p3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_6
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimManager;->removeRunningInfo(Lmiuix/animation/internal/TransitionInfo;)V

    iget-object p2, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    new-instance p3, Lmiuix/animation/internal/AnimManager$1;

    invoke-direct {p3, p0, p1}, Lmiuix/animation/internal/AnimManager$1;-><init>(Lmiuix/animation/internal/AnimManager;Lmiuix/animation/internal/TransitionInfo;)V

    invoke-virtual {p2, p3}, Lmiuix/animation/IAnimTarget;->post(Ljava/lang/Runnable;)V

    return-void
.end method""",
        'replacement': """.method notifyTransitionEndOrCancel(Lmiuix/animation/internal/TransitionInfo;II)V
    .registers 8

    goto :goto_48

    nop

    :goto_0
    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_34

    nop

    :goto_1
    invoke-static {v1, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_2
    goto :goto_3d

    nop

    :goto_3
    filled-new-array {p2, p3, p1}, [Ljava/lang/Object;

    move-result-object p2

    goto :goto_a

    nop

    :goto_4
    invoke-interface {p0, v0, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_37

    nop

    :goto_5
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_46

    nop

    :goto_6
    if-ge v1, v2, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_25

    nop

    :goto_7
    invoke-virtual {v1, v2}, Ljava/util/concurrent/ConcurrentHashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_49

    nop

    :goto_8
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_4

    nop

    :goto_9
    invoke-virtual {v1}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v1

    goto :goto_47

    nop

    :goto_a
    const-string p3, "------ do notifyTransEndOrCancel before start, msg=%d, op=%d, info=%s"

    goto :goto_1b

    nop

    :goto_b
    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_40

    nop

    :goto_c
    const-string v2, "------ do notifyTransEndOrCancel after start, msg=%d, op=%d, info=%s"

    goto :goto_2c

    nop

    :goto_d
    return-void

    :goto_e
    goto :goto_24

    nop

    :goto_f
    if-nez v0, :cond_1

    goto :goto_14

    :cond_1
    goto :goto_31

    nop

    :goto_10
    goto :goto_2b

    :goto_11
    goto :goto_12

    nop

    :goto_12
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;

    goto :goto_38

    nop

    :goto_13
    invoke-static {p2, p3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_14
    goto :goto_18

    nop

    :goto_15
    const/4 v0, 0x5

    goto :goto_3e

    nop

    :goto_16
    iget-byte v1, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    goto :goto_29

    nop

    :goto_17
    new-instance p3, Lmiuix/animation/internal/AnimManager$1;

    goto :goto_33

    nop

    :goto_18
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimManager;->removeRunningInfo(Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_32

    nop

    :goto_19
    if-nez v0, :cond_2

    goto :goto_2b

    :cond_2
    goto :goto_2e

    nop

    :goto_1a
    filled-new-array {v1, v2, p1}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_c

    nop

    :goto_1b
    invoke-static {p3, p2}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object p2

    goto :goto_43

    nop

    :goto_1c
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_4a

    nop

    :goto_1d
    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_2a

    nop

    :goto_1e
    invoke-virtual {v1, p2, p0, p3, p1}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    goto :goto_b

    nop

    :goto_1f
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimManager;->onReplaced(Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_21

    nop

    :goto_20
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransMap:Ljava/util/Map;

    goto :goto_39

    nop

    :goto_21
    return-void

    :goto_22
    goto :goto_26

    nop

    :goto_23
    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_2d

    nop

    :goto_24
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_f

    nop

    :goto_25
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v1

    goto :goto_30

    nop

    :goto_26
    invoke-virtual {p0, p1, p3}, Lmiuix/animation/internal/AnimManager;->onEnd(Lmiuix/animation/internal/TransitionInfo;I)V

    goto :goto_d

    nop

    :goto_27
    const/4 v3, 0x0

    goto :goto_6

    nop

    :goto_28
    if-nez v1, :cond_3

    goto :goto_11

    :cond_3
    goto :goto_10

    nop

    :goto_29
    const/4 v2, 0x2

    goto :goto_27

    nop

    :goto_2a
    return-void

    :goto_2b
    goto :goto_15

    nop

    :goto_2c
    invoke-static {v2, v1}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    goto :goto_3b

    nop

    :goto_2d
    invoke-virtual {v0, p2, p0, p3, p1}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    goto :goto_1d

    nop

    :goto_2e
    invoke-virtual {v0}, Lmiuix/animation/internal/TargetHandler;->isInTargetThread()Z

    move-result v1

    goto :goto_28

    nop

    :goto_2f
    invoke-virtual {v2}, Ljava/lang/Thread;->getId()J

    move-result-wide v2

    goto :goto_44

    nop

    :goto_30
    if-nez v1, :cond_4

    goto :goto_2

    :cond_4
    goto :goto_5

    nop

    :goto_31
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    goto :goto_42

    nop

    :goto_32
    iget-object p2, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_17

    nop

    :goto_33
    invoke-direct {p3, p0, p1}, Lmiuix/animation/internal/AnimManager$1;-><init>(Lmiuix/animation/internal/AnimManager;Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_3f

    nop

    :goto_34
    invoke-virtual {v2}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v2

    goto :goto_35

    nop

    :goto_35
    invoke-virtual {v2}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v2

    goto :goto_2f

    nop

    :goto_36
    if-nez v1, :cond_5

    goto :goto_41

    :cond_5
    goto :goto_20

    nop

    :goto_37
    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_1e

    nop

    :goto_38
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_1c

    nop

    :goto_39
    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_8

    nop

    :goto_3a
    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_9

    nop

    :goto_3b
    new-array v2, v3, [Ljava/lang/Object;

    goto :goto_1

    nop

    :goto_3c
    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;

    move-result-object v0

    goto :goto_16

    nop

    :goto_3d
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimManager;->removeRunningInfo(Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_3a

    nop

    :goto_3e
    if-eq p2, v0, :cond_6

    goto :goto_22

    :cond_6
    goto :goto_1f

    nop

    :goto_3f
    invoke-virtual {p2, p3}, Lmiuix/animation/IAnimTarget;->post(Ljava/lang/Runnable;)V

    goto :goto_45

    nop

    :goto_40
    return-void

    :goto_41
    goto :goto_19

    nop

    :goto_42
    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p3

    goto :goto_3

    nop

    :goto_43
    new-array p3, v3, [Ljava/lang/Object;

    goto :goto_13

    nop

    :goto_44
    invoke-static {v2, v3}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v2

    goto :goto_7

    nop

    :goto_45
    return-void

    :goto_46
    invoke-static {p3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_1a

    nop

    :goto_47
    if-nez v1, :cond_7

    goto :goto_41

    :cond_7
    goto :goto_4b

    nop

    :goto_48
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_3c

    nop

    :goto_49
    check-cast v1, Lmiuix/animation/internal/TargetHandler;

    goto :goto_36

    nop

    :goto_4a
    invoke-interface {p0, v1, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_23

    nop

    :goto_4b
    iget-object v1, p0, Lmiuix/animation/internal/AnimManager;->mObserverHandlerMap:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__notifyTransitionUpdate',
        'method': '.method notifyTransitionUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V',
        'method_name': 'notifyTransitionUpdate',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;', 'invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;', 'iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;', 'invoke-virtual {v1}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;', 'if-eqz v1, :cond_1', 'if-nez p2, :cond_0', 'new-instance v1, Ljava/util/ArrayList;', 'invoke-direct {v1, p2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V'],
        'type': 'method_replace',
        'search': """.method notifyTransitionUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V
    .registers 11
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lmiuix/animation/internal/TransitionInfo;",
            "Ljava/util/List<",
            "Lmiuix/animation/listener/UpdateInfo;",
            ">;)V"
        }
    .end annotation

    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;

    move-result-object v0

    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v1}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v1

    const/4 v2, 0x0

    const/4 v3, 0x1

    const/4 v4, 0x0

    if-eqz v1, :cond_1

    if-nez p2, :cond_0

    move-object v1, v4

    goto :goto_0

    :cond_0
    new-instance v1, Ljava/util/ArrayList;

    invoke-direct {v1, p2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_0
    iget-object v5, p0, Lmiuix/animation/internal/AnimManager;->mObserverHandlerMap:Ljava/util/concurrent/ConcurrentHashMap;

    iget-object v6, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v6}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v6

    invoke-virtual {v6}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/Thread;->getId()J

    move-result-wide v6

    invoke-static {v6, v7}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v6

    invoke-virtual {v5, v6}, Ljava/util/concurrent/ConcurrentHashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Lmiuix/animation/internal/TargetHandler;

    if-eqz v5, :cond_1

    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransForUpdateMap:Ljava/util/Map;

    iget p2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    invoke-interface {p0, p2, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v5, v3, p0, v2, v1}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    return-void

    :cond_1
    if-eqz v0, :cond_4

    invoke-virtual {v0}, Lmiuix/animation/internal/TargetHandler;->isInTargetThread()Z

    move-result v1

    if-eqz v1, :cond_2

    goto :goto_2

    :cond_2
    if-nez p2, :cond_3

    goto :goto_1

    :cond_3
    new-instance v4, Ljava/util/ArrayList;

    invoke-direct {v4, p2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_1
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransForUpdateMap:Ljava/util/Map;

    iget p2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    invoke-interface {p0, p2, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v0, v3, p0, v2, v4}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    return-void

    :cond_4
    :goto_2
    invoke-virtual {p0, p1, p2}, Lmiuix/animation/internal/AnimManager;->onUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V

    return-void
.end method""",
        'replacement': """.method notifyTransitionUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V
    .registers 11
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lmiuix/animation/internal/TransitionInfo;",
            "Ljava/util/List<",
            "Lmiuix/animation/listener/UpdateInfo;",
            ">;)V"
        }
    .end annotation

    goto :goto_26

    nop

    :goto_0
    iget-object v5, p0, Lmiuix/animation/internal/AnimManager;->mObserverHandlerMap:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_10

    nop

    :goto_1
    return-void

    :goto_2
    check-cast v5, Lmiuix/animation/internal/TargetHandler;

    goto :goto_9

    nop

    :goto_3
    invoke-static {v6, v7}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v6

    goto :goto_18

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_33

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_4

    nop

    :goto_7
    invoke-virtual {v5, v3, p0, v2, v1}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    goto :goto_1c

    nop

    :goto_8
    if-eqz p2, :cond_0

    goto :goto_12

    :cond_0
    goto :goto_21

    nop

    :goto_9
    if-nez v5, :cond_1

    goto :goto_2c

    :cond_1
    goto :goto_22

    nop

    :goto_a
    invoke-virtual {v1}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v1

    goto :goto_23

    nop

    :goto_b
    iget p2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_15

    nop

    :goto_c
    invoke-virtual {v6}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v6

    goto :goto_1f

    nop

    :goto_d
    goto :goto_5

    :goto_e
    goto :goto_2f

    nop

    :goto_f
    invoke-interface {p0, p2, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_17

    nop

    :goto_10
    iget-object v6, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_24

    nop

    :goto_11
    goto :goto_2e

    :goto_12
    goto :goto_1a

    nop

    :goto_13
    goto :goto_28

    :goto_14
    goto :goto_25

    nop

    :goto_15
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    goto :goto_1e

    nop

    :goto_16
    if-nez v0, :cond_2

    goto :goto_5

    :cond_2
    goto :goto_1b

    nop

    :goto_17
    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_19

    nop

    :goto_18
    invoke-virtual {v5, v6}, Ljava/util/concurrent/ConcurrentHashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v5

    goto :goto_2

    nop

    :goto_19
    invoke-virtual {v0, v3, p0, v2, v4}, Landroid/os/Handler;->obtainMessage(IIILjava/lang/Object;)Landroid/os/Message;

    move-result-object p0

    goto :goto_6

    nop

    :goto_1a
    new-instance v1, Ljava/util/ArrayList;

    goto :goto_2d

    nop

    :goto_1b
    invoke-virtual {v0}, Lmiuix/animation/internal/TargetHandler;->isInTargetThread()Z

    move-result v1

    goto :goto_2a

    nop

    :goto_1c
    invoke-virtual {p0}, Landroid/os/Message;->sendToTarget()V

    goto :goto_2b

    nop

    :goto_1d
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransForUpdateMap:Ljava/util/Map;

    goto :goto_20

    nop

    :goto_1e
    invoke-interface {p0, p2, p1}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_30

    nop

    :goto_1f
    invoke-virtual {v6}, Ljava/lang/Thread;->getId()J

    move-result-wide v6

    goto :goto_3

    nop

    :goto_20
    iget p2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_34

    nop

    :goto_21
    move-object v1, v4

    goto :goto_11

    nop

    :goto_22
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTempTransForUpdateMap:Ljava/util/Map;

    goto :goto_b

    nop

    :goto_23
    const/4 v2, 0x0

    goto :goto_36

    nop

    :goto_24
    invoke-virtual {v6}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v6

    goto :goto_c

    nop

    :goto_25
    new-instance v4, Ljava/util/ArrayList;

    goto :goto_27

    nop

    :goto_26
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_32

    nop

    :goto_27
    invoke-direct {v4, p2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_28
    goto :goto_1d

    nop

    :goto_29
    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_a

    nop

    :goto_2a
    if-nez v1, :cond_3

    goto :goto_e

    :cond_3
    goto :goto_d

    nop

    :goto_2b
    return-void

    :goto_2c
    goto :goto_16

    nop

    :goto_2d
    invoke-direct {v1, p2}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_2e
    goto :goto_0

    nop

    :goto_2f
    if-eqz p2, :cond_4

    goto :goto_14

    :cond_4
    goto :goto_13

    nop

    :goto_30
    iget p0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_7

    nop

    :goto_31
    const/4 v4, 0x0

    goto :goto_35

    nop

    :goto_32
    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getHandler()Lmiuix/animation/internal/TargetHandler;

    move-result-object v0

    goto :goto_29

    nop

    :goto_33
    invoke-virtual {p0, p1, p2}, Lmiuix/animation/internal/AnimManager;->onUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V

    goto :goto_1

    nop

    :goto_34
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p2

    goto :goto_f

    nop

    :goto_35
    if-nez v1, :cond_5

    goto :goto_2c

    :cond_5
    goto :goto_8

    nop

    :goto_36
    const/4 v3, 0x1

    goto :goto_31

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__onEnd',
        'method': '.method onEnd(Lmiuix/animation/internal/TransitionInfo;I)V',
        'method_name': 'onEnd',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'const-string v1, "@"', 'const-string v2, "info.key="', 'const-string v3, ">>> "', 'const-string v4, "onEnd"', 'const-string v5, "onCancel"', 'if-eqz v0, :cond_1', 'if-ne p2, v6, :cond_0'],
        'type': 'method_replace',
        'search': """.method onEnd(Lmiuix/animation/internal/TransitionInfo;I)V
    .registers 15

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    const-string v1, "@"

    const-string v2, "info.key="

    const-string v3, ">>> "

    const-string v4, "onEnd"

    const-string v5, "onCancel"

    const/4 v6, 0x4

    if-eqz v0, :cond_1

    if-ne p2, v6, :cond_0

    move-object v7, v5

    goto :goto_0

    :cond_0
    move-object v7, v4

    :goto_0
    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v8, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v7, " info.id="

    invoke-virtual {v8, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v7, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v8, v7}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v8, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v9, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v9, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {v9}, Ljava/lang/Object;->hashCode()I

    move-result v9

    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    new-instance v9, Ljava/lang/StringBuilder;

    invoke-direct {v9}, Ljava/lang/StringBuilder;-><init>()V

    const-string v10, "info.startTime="

    invoke-virtual {v9, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-wide v10, p1, Lmiuix/animation/internal/TransitionInfo;->startTime:J

    invoke-virtual {v9, v10, v11}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    filled-new-array {v8, v9}, [Ljava/lang/Object;

    move-result-object v8

    invoke-static {v7, v8}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    if-eqz v0, :cond_3

    if-ne p2, v6, :cond_2

    move-object v4, v5

    :cond_2
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v3, " finish notify info.id="

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v3, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {v1}, Ljava/lang/Object;->hashCode()I

    move-result v1

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v1

    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_3
    if-ne p2, v6, :cond_4

    iget-object p2, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    invoke-virtual {p2}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object p2

    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->tag:Ljava/lang/Object;

    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->listenerSetForNotify:Ljava/util/Set;

    invoke-virtual {p2, v0, v1, v2}, Lmiuix/animation/listener/ListenerNotifier;->notifyCancelAll(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Set;)V

    goto :goto_1

    :cond_4
    iget-object p2, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    invoke-virtual {p2}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object p2

    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->tag:Ljava/lang/Object;

    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->listenerSetForNotify:Ljava/util/Set;

    invoke-virtual {p2, v0, v1, v2}, Lmiuix/animation/listener/ListenerNotifier;->notifyEndAll(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Set;)V

    :goto_1
    iget-object p2, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    new-instance v0, Lmiuix/animation/internal/AnimManager$2;

    invoke-direct {v0, p0, p1}, Lmiuix/animation/internal/AnimManager$2;-><init>(Lmiuix/animation/internal/AnimManager;Lmiuix/animation/internal/TransitionInfo;)V

    invoke-virtual {p2, v0}, Lmiuix/animation/IAnimTarget;->post(Ljava/lang/Runnable;)V

    iput-byte v6, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    const/4 p0, 0x0

    iput-boolean p0, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    iput-boolean p0, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    return-void
.end method""",
        'replacement': """.method onEnd(Lmiuix/animation/internal/TransitionInfo;I)V
    .registers 15

    goto :goto_c

    nop

    :goto_0
    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->listenerSetForNotify:Ljava/util/Set;

    goto :goto_49

    nop

    :goto_1
    new-instance v8, Ljava/lang/StringBuilder;

    goto :goto_42

    nop

    :goto_2
    const-string v1, "@"

    goto :goto_51

    nop

    :goto_3
    const-string v4, "onEnd"

    goto :goto_14

    nop

    :goto_4
    move-object v7, v4

    :goto_5
    goto :goto_7

    nop

    :goto_6
    iget v7, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_1b

    nop

    :goto_7
    new-instance v8, Ljava/lang/StringBuilder;

    goto :goto_55

    nop

    :goto_8
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    goto :goto_4e

    nop

    :goto_9
    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_5d

    nop

    :goto_a
    invoke-direct {v0, p0, p1}, Lmiuix/animation/internal/AnimManager$2;-><init>(Lmiuix/animation/internal/AnimManager;Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_13

    nop

    :goto_b
    move-object v7, v5

    goto :goto_4b

    nop

    :goto_c
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_2

    nop

    :goto_d
    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_32

    nop

    :goto_e
    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    goto :goto_26

    nop

    :goto_f
    invoke-virtual {p2}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object p2

    goto :goto_25

    nop

    :goto_10
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_1d

    nop

    :goto_11
    invoke-direct {v9}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_20

    nop

    :goto_12
    const/4 p0, 0x0

    goto :goto_28

    nop

    :goto_13
    invoke-virtual {p2, v0}, Lmiuix/animation/IAnimTarget;->post(Ljava/lang/Runnable;)V

    goto :goto_24

    nop

    :goto_14
    const-string v5, "onCancel"

    goto :goto_48

    nop

    :goto_15
    invoke-virtual {v8, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_40

    nop

    :goto_16
    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    goto :goto_3e

    nop

    :goto_17
    iput-boolean p0, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    goto :goto_35

    nop

    :goto_18
    new-instance v0, Lmiuix/animation/internal/AnimManager$2;

    goto :goto_a

    nop

    :goto_19
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_41

    nop

    :goto_1a
    invoke-virtual {v9, v10, v11}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    goto :goto_16

    nop

    :goto_1b
    invoke-virtual {v8, v7}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_2e

    nop

    :goto_1c
    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_2d

    nop

    :goto_1d
    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->tag:Ljava/lang/Object;

    goto :goto_0

    nop

    :goto_1e
    new-instance v3, Ljava/lang/StringBuilder;

    goto :goto_5a

    nop

    :goto_1f
    iget-wide v10, p1, Lmiuix/animation/internal/TransitionInfo;->startTime:J

    goto :goto_1a

    nop

    :goto_20
    const-string v10, "info.startTime="

    goto :goto_2b

    nop

    :goto_21
    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->tag:Ljava/lang/Object;

    goto :goto_2c

    nop

    :goto_22
    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_23
    invoke-virtual {v8, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_4f

    nop

    :goto_24
    iput-byte v6, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    goto :goto_12

    nop

    :goto_25
    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_10

    nop

    :goto_26
    new-instance v9, Ljava/lang/StringBuilder;

    goto :goto_11

    nop

    :goto_27
    iget-object v9, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_3d

    nop

    :goto_28
    iput-boolean p0, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    goto :goto_17

    nop

    :goto_29
    const-string v3, ">>> "

    goto :goto_3

    nop

    :goto_2a
    if-eq p2, v6, :cond_0

    goto :goto_31

    :cond_0
    goto :goto_30

    nop

    :goto_2b
    invoke-virtual {v9, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1f

    nop

    :goto_2c
    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->listenerSetForNotify:Ljava/util/Set;

    goto :goto_53

    nop

    :goto_2d
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_1e

    nop

    :goto_2e
    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    goto :goto_1

    nop

    :goto_2f
    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_5c

    nop

    :goto_30
    move-object v4, v5

    :goto_31
    goto :goto_19

    nop

    :goto_32
    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_33
    invoke-static {v7, v8}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_34
    goto :goto_37

    nop

    :goto_35
    return-void

    :goto_36
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_21

    nop

    :goto_37
    if-nez v0, :cond_1

    goto :goto_3c

    :cond_1
    goto :goto_2a

    nop

    :goto_38
    goto :goto_54

    :goto_39
    goto :goto_43

    nop

    :goto_3a
    iget-object p2, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    goto :goto_f

    nop

    :goto_3b
    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_3c
    goto :goto_57

    nop

    :goto_3d
    invoke-virtual {v9}, Ljava/lang/Object;->hashCode()I

    move-result v9

    goto :goto_22

    nop

    :goto_3e
    filled-new-array {v8, v9}, [Ljava/lang/Object;

    move-result-object v8

    goto :goto_33

    nop

    :goto_3f
    invoke-virtual {v0, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_59

    nop

    :goto_40
    invoke-virtual {v8, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_5b

    nop

    :goto_41
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_46

    nop

    :goto_42
    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_45

    nop

    :goto_43
    iget-object p2, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    goto :goto_44

    nop

    :goto_44
    invoke-virtual {p2}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object p2

    goto :goto_47

    nop

    :goto_45
    invoke-virtual {v8, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_5e

    nop

    :goto_46
    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_3f

    nop

    :goto_47
    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_36

    nop

    :goto_48
    const/4 v6, 0x4

    goto :goto_58

    nop

    :goto_49
    invoke-virtual {p2, v0, v1, v2}, Lmiuix/animation/listener/ListenerNotifier;->notifyCancelAll(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Set;)V

    goto :goto_38

    nop

    :goto_4a
    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_8

    nop

    :goto_4b
    goto :goto_5

    :goto_4c
    goto :goto_4

    nop

    :goto_4d
    iget-object p2, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_18

    nop

    :goto_4e
    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_3b

    nop

    :goto_4f
    invoke-virtual {v8, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_27

    nop

    :goto_50
    invoke-virtual {v8, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_51
    const-string v2, "info.key="

    goto :goto_29

    nop

    :goto_52
    if-eq p2, v6, :cond_2

    goto :goto_4c

    :cond_2
    goto :goto_b

    nop

    :goto_53
    invoke-virtual {p2, v0, v1, v2}, Lmiuix/animation/listener/ListenerNotifier;->notifyEndAll(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Set;)V

    :goto_54
    goto :goto_4d

    nop

    :goto_55
    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_15

    nop

    :goto_56
    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_5f

    nop

    :goto_57
    if-eq p2, v6, :cond_3

    goto :goto_39

    :cond_3
    goto :goto_3a

    nop

    :goto_58
    if-nez v0, :cond_4

    goto :goto_34

    :cond_4
    goto :goto_52

    nop

    :goto_59
    const-string v3, " finish notify info.id="

    goto :goto_2f

    nop

    :goto_5a
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_56

    nop

    :goto_5b
    const-string v7, " info.id="

    goto :goto_50

    nop

    :goto_5c
    iget v3, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_1c

    nop

    :goto_5d
    invoke-virtual {v1}, Ljava/lang/Object;->hashCode()I

    move-result v1

    goto :goto_4a

    nop

    :goto_5e
    iget-object v9, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_23

    nop

    :goto_5f
    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__onReplaceListeners',
        'method': '.method onReplaceListeners(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'onReplaceListeners',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z', 'if-eqz v0, :cond_0', 'new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, ">>> onReplaceListeners info.id="', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method onReplaceListeners(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 4

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    if-eqz v0, :cond_0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, ">>> onReplaceListeners info.id="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v1, ", info.key="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const/4 v1, 0x0

    new-array v1, v1, [Ljava/lang/Object;

    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object v0

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-virtual {v0, v1}, Lmiuix/animation/listener/ListenerNotifier;->removeListeners(Ljava/lang/Object;)V

    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {p0}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object p0

    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    iget-object p1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {p0, v0, p1}, Lmiuix/animation/listener/ListenerNotifier;->addListeners(Ljava/lang/Object;Lmiuix/animation/base/AnimConfig;)Z

    return-void
.end method""",
        'replacement': """.method onReplaceListeners(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 4

    goto :goto_11

    nop

    :goto_0
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_18

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_19

    nop

    :goto_2
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_5

    nop

    :goto_3
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_6

    nop

    :goto_4
    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_14

    nop

    :goto_5
    const-string v1, ", info.key="

    goto :goto_b

    nop

    :goto_6
    const/4 v1, 0x0

    goto :goto_1a

    nop

    :goto_7
    const-string v1, ">>> onReplaceListeners info.id="

    goto :goto_f

    nop

    :goto_8
    invoke-virtual {p0, v0, p1}, Lmiuix/animation/listener/ListenerNotifier;->addListeners(Ljava/lang/Object;Lmiuix/animation/base/AnimConfig;)Z

    goto :goto_9

    nop

    :goto_9
    return-void

    :goto_a
    invoke-virtual {v0, v1}, Lmiuix/animation/listener/ListenerNotifier;->removeListeners(Ljava/lang/Object;)V

    goto :goto_15

    nop

    :goto_b
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_c
    invoke-virtual {p0}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object p0

    goto :goto_16

    nop

    :goto_d
    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_e
    goto :goto_1

    nop

    :goto_f
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_13

    nop

    :goto_10
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_1b

    nop

    :goto_11
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v0

    goto :goto_1c

    nop

    :goto_12
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_17

    nop

    :goto_13
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_2

    nop

    :goto_14
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_3

    nop

    :goto_15
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_c

    nop

    :goto_16
    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_10

    nop

    :goto_17
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_a

    nop

    :goto_18
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_7

    nop

    :goto_19
    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object v0

    goto :goto_12

    nop

    :goto_1a
    new-array v1, v1, [Ljava/lang/Object;

    goto :goto_d

    nop

    :goto_1b
    iget-object p1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_8

    nop

    :goto_1c
    if-nez v0, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__onReplaced',
        'method': '.method onReplaced(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'onReplaced',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'if-eqz v0, :cond_0', 'new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v2, ">>> onReplaced info.id="', 'invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'iget v2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I', 'invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method onReplaced(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 7

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, ">>> onReplaced info.id="

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v2, ", info.key="

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    const-string v2, "@"

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {v2}, Ljava/lang/Object;->hashCode()I

    move-result v2

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v2, ", info.startTime="

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-wide v2, p1, Lmiuix/animation/internal/TransitionInfo;->startTime:J

    invoke-virtual {v0, v2, v3}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    new-array v2, v1, [Ljava/lang/Object;

    invoke-static {v0, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object v0

    iget v2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    iget-object v3, p1, Lmiuix/animation/internal/TransitionInfo;->tag:Ljava/lang/Object;

    iget-object v4, p1, Lmiuix/animation/internal/TransitionInfo;->listenerSetForNotify:Ljava/util/Set;

    invoke-virtual {v0, v2, v3, v4}, Lmiuix/animation/listener/ListenerNotifier;->notifyCancelAll(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Set;)V

    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    new-instance v2, Lmiuix/animation/internal/AnimManager$3;

    invoke-direct {v2, p0, p1}, Lmiuix/animation/internal/AnimManager$3;-><init>(Lmiuix/animation/internal/AnimManager;Lmiuix/animation/internal/TransitionInfo;)V

    invoke-virtual {v0, v2}, Lmiuix/animation/IAnimTarget;->post(Ljava/lang/Runnable;)V

    const/4 p0, 0x3

    iput-byte p0, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    return-void
.end method""",
        'replacement': """.method onReplaced(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 7

    goto :goto_b

    nop

    :goto_0
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_26

    nop

    :goto_1
    const/4 v1, 0x0

    goto :goto_15

    nop

    :goto_2
    iput-byte p0, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    goto :goto_a

    nop

    :goto_3
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_16

    nop

    :goto_4
    iget-object v3, p1, Lmiuix/animation/internal/TransitionInfo;->tag:Ljava/lang/Object;

    goto :goto_25

    nop

    :goto_5
    const-string v2, "@"

    goto :goto_8

    nop

    :goto_6
    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_17

    nop

    :goto_7
    new-array v2, v1, [Ljava/lang/Object;

    goto :goto_1f

    nop

    :goto_8
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_9
    return-void

    :goto_a
    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasSendNotifyStart:Z

    goto :goto_1d

    nop

    :goto_b
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_1

    nop

    :goto_c
    iget-wide v2, p1, Lmiuix/animation/internal/TransitionInfo;->startTime:J

    goto :goto_d

    nop

    :goto_d
    invoke-virtual {v0, v2, v3}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    goto :goto_1c

    nop

    :goto_e
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_24

    nop

    :goto_f
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_28

    nop

    :goto_10
    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v2

    goto :goto_4

    nop

    :goto_11
    invoke-direct {v2, p0, p1}, Lmiuix/animation/internal/AnimManager$3;-><init>(Lmiuix/animation/internal/AnimManager;Lmiuix/animation/internal/TransitionInfo;)V

    goto :goto_14

    nop

    :goto_12
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_1a

    nop

    :goto_13
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_5

    nop

    :goto_14
    invoke-virtual {v0, v2}, Lmiuix/animation/IAnimTarget;->post(Ljava/lang/Runnable;)V

    goto :goto_21

    nop

    :goto_15
    if-nez v0, :cond_0

    goto :goto_20

    :cond_0
    goto :goto_27

    nop

    :goto_16
    const-string v2, ">>> onReplaced info.id="

    goto :goto_1e

    nop

    :goto_17
    invoke-virtual {v2}, Ljava/lang/Object;->hashCode()I

    move-result v2

    goto :goto_f

    nop

    :goto_18
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_c

    nop

    :goto_19
    iget v2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_0

    nop

    :goto_1a
    new-instance v2, Lmiuix/animation/internal/AnimManager$3;

    goto :goto_11

    nop

    :goto_1b
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_23

    nop

    :goto_1c
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_7

    nop

    :goto_1d
    iput-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    goto :goto_9

    nop

    :goto_1e
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_19

    nop

    :goto_1f
    invoke-static {v0, v2}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_20
    goto :goto_e

    nop

    :goto_21
    const/4 p0, 0x3

    goto :goto_2

    nop

    :goto_22
    invoke-virtual {v0, v2, v3, v4}, Lmiuix/animation/listener/ListenerNotifier;->notifyCancelAll(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Set;)V

    goto :goto_12

    nop

    :goto_23
    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_13

    nop

    :goto_24
    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object v0

    goto :goto_29

    nop

    :goto_25
    iget-object v4, p1, Lmiuix/animation/internal/TransitionInfo;->listenerSetForNotify:Ljava/util/Set;

    goto :goto_22

    nop

    :goto_26
    const-string v2, ", info.key="

    goto :goto_1b

    nop

    :goto_27
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_3

    nop

    :goto_28
    const-string v2, ", info.startTime="

    goto :goto_18

    nop

    :goto_29
    iget v2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__onStart',
        'method': '.method onStart(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V',
        'method_name': 'onStart',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'iget-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z', 'const-string v3, ", info.key="', 'if-eqz v1, :cond_0', 'if-eqz v0, :cond_3', 'new-instance p0, Ljava/lang/StringBuilder;', 'invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string p2, ">>> onStart warning!! this transition has notified start: info.id="'],
        'type': 'method_replace',
        'search': """.method onStart(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V
    .registers 9
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lmiuix/animation/internal/TransitionInfo;",
            "Ljava/util/List<",
            "Lmiuix/animation/listener/UpdateInfo;",
            ">;Z)V"
        }
    .end annotation

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    iget-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    const/4 v2, 0x0

    const-string v3, ", info.key="

    if-eqz v1, :cond_0

    if-eqz v0, :cond_3

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string p2, ">>> onStart warning!! this transition has notified start: info.id="

    invoke-virtual {p0, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget p2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {p0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {p0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p1, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    new-array p1, v2, [Ljava/lang/Object;

    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    return-void

    :cond_0
    if-eqz v0, :cond_1

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, ">>> onStart info.id="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    const-string v1, ", info.startTime="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-wide v3, p1, Lmiuix/animation/internal/TransitionInfo;->startTime:J

    invoke-virtual {v0, v3, v4}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    const-string v1, ", mRunningInfo.contains="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    iget-object v1, v1, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    iget-object v1, v1, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {v1, p1}, Ljava/util/concurrent/ConcurrentHashMap;->contains(Ljava/lang/Object;)Z

    move-result v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v1, ", target="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v1, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    new-array v1, v2, [Ljava/lang/Object;

    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    const/4 v0, 0x1

    iput-boolean v0, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateListForNotify:Ljava/util/List;

    invoke-interface {v0}, Ljava/util/List;->clear()V

    if-nez p2, :cond_2

    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    if-eqz v0, :cond_2

    new-instance p2, Ljava/util/ArrayList;

    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    invoke-direct {p2, v0}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :cond_2
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object v0

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->tag:Ljava/lang/Object;

    iget-object v3, p1, Lmiuix/animation/internal/TransitionInfo;->listenerSetForNotify:Ljava/util/Set;

    invoke-virtual {v0, v1, v2, p2, v3}, Lmiuix/animation/listener/ListenerNotifier;->notifyBegin(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Collection;Ljava/util/Set;)V

    if-eqz p3, :cond_3

    invoke-virtual {p0, p1, p2}, Lmiuix/animation/internal/AnimManager;->onUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V

    :cond_3
    return-void
.end method""",
        'replacement': """.method onStart(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;Z)V
    .registers 9
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lmiuix/animation/internal/TransitionInfo;",
            "Ljava/util/List<",
            "Lmiuix/animation/listener/UpdateInfo;",
            ">;Z)V"
        }
    .end annotation

    goto :goto_3f

    nop

    :goto_0
    iget p2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_26

    nop

    :goto_1
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateListForNotify:Ljava/util/List;

    goto :goto_16

    nop

    :goto_2
    invoke-virtual {p0, p1, p2}, Lmiuix/animation/internal/AnimManager;->onUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V

    :goto_3
    goto :goto_14

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_11

    nop

    :goto_5
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_2f

    nop

    :goto_6
    new-array p1, v2, [Ljava/lang/Object;

    goto :goto_15

    nop

    :goto_7
    invoke-direct {p2, v0}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    :goto_8
    goto :goto_2c

    nop

    :goto_9
    iget-object v3, p1, Lmiuix/animation/internal/TransitionInfo;->listenerSetForNotify:Ljava/util/Set;

    goto :goto_39

    nop

    :goto_a
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_33

    nop

    :goto_b
    new-instance p2, Ljava/util/ArrayList;

    goto :goto_1f

    nop

    :goto_c
    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->tag:Ljava/lang/Object;

    goto :goto_9

    nop

    :goto_d
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_a

    nop

    :goto_e
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_38

    nop

    :goto_f
    invoke-virtual {v0}, Lmiuix/animation/IAnimTarget;->getNotifier()Lmiuix/animation/listener/ListenerNotifier;

    move-result-object v0

    goto :goto_24

    nop

    :goto_10
    if-nez p3, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_2

    nop

    :goto_11
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_41

    nop

    :goto_12
    if-eqz p2, :cond_2

    goto :goto_8

    :cond_2
    goto :goto_3d

    nop

    :goto_13
    invoke-virtual {p0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1d

    nop

    :goto_14
    return-void

    :goto_15
    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_42

    nop

    :goto_16
    invoke-interface {v0}, Ljava/util/List;->clear()V

    goto :goto_12

    nop

    :goto_17
    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_18
    goto :goto_28

    nop

    :goto_19
    iget-wide v3, p1, Lmiuix/animation/internal/TransitionInfo;->startTime:J

    goto :goto_20

    nop

    :goto_1a
    const-string v1, ", mRunningInfo.contains="

    goto :goto_44

    nop

    :goto_1b
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_c

    nop

    :goto_1c
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_2a

    nop

    :goto_1d
    iget-object p1, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_46

    nop

    :goto_1e
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_d

    nop

    :goto_1f
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    goto :goto_7

    nop

    :goto_20
    invoke-virtual {v0, v3, v4}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    goto :goto_1a

    nop

    :goto_21
    iget-boolean v1, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    goto :goto_3b

    nop

    :goto_22
    iget-object v1, v1, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_29

    nop

    :goto_23
    invoke-virtual {p0, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_24
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_1b

    nop

    :goto_25
    new-array v1, v2, [Ljava/lang/Object;

    goto :goto_17

    nop

    :goto_26
    invoke-virtual {p0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_13

    nop

    :goto_27
    const-string p2, ">>> onStart warning!! this transition has notified start: info.id="

    goto :goto_23

    nop

    :goto_28
    const/4 v0, 0x1

    goto :goto_3a

    nop

    :goto_29
    invoke-virtual {v1, p1}, Ljava/util/concurrent/ConcurrentHashMap;->contains(Ljava/lang/Object;)Z

    move-result v1

    goto :goto_1c

    nop

    :goto_2a
    const-string v1, ", target="

    goto :goto_32

    nop

    :goto_2b
    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    goto :goto_34

    nop

    :goto_2c
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_f

    nop

    :goto_2d
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_6

    nop

    :goto_2e
    const-string v3, ", info.key="

    goto :goto_3e

    nop

    :goto_2f
    const-string v1, ", info.startTime="

    goto :goto_35

    nop

    :goto_30
    const-string v1, ">>> onStart info.id="

    goto :goto_1e

    nop

    :goto_31
    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_5

    nop

    :goto_32
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_40

    nop

    :goto_33
    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_31

    nop

    :goto_34
    iget-object v1, v1, Lmiuix/animation/IAnimTarget;->animManager:Lmiuix/animation/internal/AnimManager;

    goto :goto_22

    nop

    :goto_35
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_19

    nop

    :goto_36
    if-nez v0, :cond_3

    goto :goto_8

    :cond_3
    goto :goto_b

    nop

    :goto_37
    if-nez v0, :cond_4

    goto :goto_18

    :cond_4
    goto :goto_3c

    nop

    :goto_38
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_25

    nop

    :goto_39
    invoke-virtual {v0, v1, v2, p2, v3}, Lmiuix/animation/listener/ListenerNotifier;->notifyBegin(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/Collection;Ljava/util/Set;)V

    goto :goto_10

    nop

    :goto_3a
    iput-boolean v0, p1, Lmiuix/animation/internal/TransitionInfo;->hasOnStart:Z

    goto :goto_1

    nop

    :goto_3b
    const/4 v2, 0x0

    goto :goto_2e

    nop

    :goto_3c
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_45

    nop

    :goto_3d
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    goto :goto_36

    nop

    :goto_3e
    if-nez v1, :cond_5

    goto :goto_43

    :cond_5
    goto :goto_4

    nop

    :goto_3f
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_21

    nop

    :goto_40
    iget-object v1, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_e

    nop

    :goto_41
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_27

    nop

    :goto_42
    return-void

    :goto_43
    goto :goto_37

    nop

    :goto_44
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2b

    nop

    :goto_45
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_30

    nop

    :goto_46
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_2d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__onUpdate',
        'method': '.method onUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V',
        'method_name': 'onUpdate',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'if-eqz v0, :cond_0', 'new-instance v1, Ljava/lang/StringBuilder;', 'invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v2, ">>> onUpdate info.id="', 'invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'iget v2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I', 'invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method onUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V
    .registers 9
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lmiuix/animation/internal/TransitionInfo;",
            "Ljava/util/List<",
            "Lmiuix/animation/listener/UpdateInfo;",
            ">;)V"
        }
    .end annotation

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    if-eqz v0, :cond_0

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, ">>> onUpdate info.id="

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "info.key="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v3, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "update.size="

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v4, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    invoke-interface {v4}, Ljava/util/List;->size()I

    move-result v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "target="

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v4, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    filled-new-array {v2, v3, p0}, [Ljava/lang/Object;

    move-result-object p0

    invoke-static {v1, p0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    if-nez p2, :cond_1

    new-instance p2, Ljava/util/ArrayList;

    iget-object p0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    invoke-direct {p2, p0}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    if-eqz v0, :cond_1

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, ">>> onUpdate warning!! infoUpdateList is null!!info.id="

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const/4 v0, 0x0

    new-array v0, v0, [Ljava/lang/Object;

    invoke-static {p0, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    iget-object p0, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->tag:Ljava/lang/Object;

    iget-object p1, p1, Lmiuix/animation/internal/TransitionInfo;->listenerSetForNotify:Ljava/util/Set;

    invoke-static {p0, v0, v1, p2, p1}, Lmiuix/animation/internal/AnimManager;->doNotifyUpdate(Lmiuix/animation/IAnimTarget;Ljava/lang/Object;Ljava/lang/Object;Ljava/util/List;Ljava/util/Set;)V

    return-void
.end method""",
        'replacement': """.method onUpdate(Lmiuix/animation/internal/TransitionInfo;Ljava/util/List;)V
    .registers 9
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lmiuix/animation/internal/TransitionInfo;",
            "Ljava/util/List<",
            "Lmiuix/animation/listener/UpdateInfo;",
            ">;)V"
        }
    .end annotation

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_26

    nop

    :goto_1
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_b

    nop

    :goto_2
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1d

    nop

    :goto_3
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_30

    nop

    :goto_4
    iget v2, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_0

    nop

    :goto_5
    invoke-static {p0, v0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_6
    goto :goto_23

    nop

    :goto_7
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_1a

    nop

    :goto_8
    const-string v0, ">>> onUpdate warning!! infoUpdateList is null!!info.id="

    goto :goto_2

    nop

    :goto_9
    invoke-interface {v4}, Ljava/util/List;->size()I

    move-result v4

    goto :goto_29

    nop

    :goto_a
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_13

    nop

    :goto_b
    if-nez v0, :cond_0

    goto :goto_21

    :cond_0
    goto :goto_f

    nop

    :goto_c
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_22

    nop

    :goto_d
    iget-object v1, p1, Lmiuix/animation/internal/TransitionInfo;->tag:Ljava/lang/Object;

    goto :goto_34

    nop

    :goto_e
    const-string v5, "target="

    goto :goto_28

    nop

    :goto_f
    new-instance v1, Ljava/lang/StringBuilder;

    goto :goto_35

    nop

    :goto_10
    invoke-static {p0, v0, v1, p2, p1}, Lmiuix/animation/internal/AnimManager;->doNotifyUpdate(Lmiuix/animation/IAnimTarget;Ljava/lang/Object;Ljava/lang/Object;Ljava/util/List;Ljava/util/Set;)V

    goto :goto_38

    nop

    :goto_11
    invoke-direct {p2, p0}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    goto :goto_2c

    nop

    :goto_12
    const/4 v0, 0x0

    goto :goto_15

    nop

    :goto_13
    invoke-virtual {v4, p0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_24

    nop

    :goto_14
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_2e

    nop

    :goto_15
    new-array v0, v0, [Ljava/lang/Object;

    goto :goto_5

    nop

    :goto_16
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_8

    nop

    :goto_17
    const-string v2, ">>> onUpdate info.id="

    goto :goto_37

    nop

    :goto_18
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_e

    nop

    :goto_19
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    goto :goto_32

    nop

    :goto_1a
    const-string v3, "info.key="

    goto :goto_c

    nop

    :goto_1b
    iget-object p0, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    goto :goto_11

    nop

    :goto_1c
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_2f

    nop

    :goto_1d
    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_3

    nop

    :goto_1e
    new-instance p2, Ljava/util/ArrayList;

    goto :goto_1b

    nop

    :goto_1f
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_d

    nop

    :goto_20
    invoke-static {v1, p0}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_21
    goto :goto_2b

    nop

    :goto_22
    iget-object v3, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_1c

    nop

    :goto_23
    iget-object p0, p1, Lmiuix/animation/internal/TransitionInfo;->target:Lmiuix/animation/IAnimTarget;

    goto :goto_31

    nop

    :goto_24
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_2a

    nop

    :goto_25
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_33

    nop

    :goto_26
    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    goto :goto_2d

    nop

    :goto_27
    new-instance v3, Ljava/lang/StringBuilder;

    goto :goto_14

    nop

    :goto_28
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_a

    nop

    :goto_29
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_19

    nop

    :goto_2a
    filled-new-array {v2, v3, p0}, [Ljava/lang/Object;

    move-result-object p0

    goto :goto_20

    nop

    :goto_2b
    if-eqz p2, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_1e

    nop

    :goto_2c
    if-nez v0, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_36

    nop

    :goto_2d
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_2e
    const-string v4, "update.size="

    goto :goto_25

    nop

    :goto_2f
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_27

    nop

    :goto_30
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_12

    nop

    :goto_31
    iget v0, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_1f

    nop

    :goto_32
    new-instance v4, Ljava/lang/StringBuilder;

    goto :goto_18

    nop

    :goto_33
    iget-object v4, p1, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    goto :goto_9

    nop

    :goto_34
    iget-object p1, p1, Lmiuix/animation/internal/TransitionInfo;->listenerSetForNotify:Ljava/util/Set;

    goto :goto_10

    nop

    :goto_35
    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_17

    nop

    :goto_36
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_16

    nop

    :goto_37
    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_38
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__removeRunningInfo',
        'method': '.method removeRunningInfo(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'removeRunningInfo',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;', 'iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I', 'invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-virtual {v0, v1}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;', 'iget v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I', 'invoke-virtual {p1}, Lmiuix/animation/internal/TransitionInfo;->getAnimCount()I', 'iput v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I', 'invoke-virtual {p0, v1}, Lmiuix/animation/internal/AnimManager;->isAnimRunning([Lmiuix/animation/property/FloatProperty;)Z'],
        'type': 'method_replace',
        'search': """.method removeRunningInfo(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 6

    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    iget v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I

    invoke-virtual {p1}, Lmiuix/animation/internal/TransitionInfo;->getAnimCount()I

    move-result v1

    sub-int/2addr v0, v1

    iput v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I

    const/4 v0, 0x0

    new-array v1, v0, [Lmiuix/animation/property/FloatProperty;

    invoke-virtual {p0, v1}, Lmiuix/animation/internal/AnimManager;->isAnimRunning([Lmiuix/animation/property/FloatProperty;)Z

    move-result v1

    if-nez v1, :cond_0

    invoke-virtual {p0}, Lmiuix/animation/internal/AnimManager;->hasAnimSetup()Z

    move-result v2

    if-nez v2, :cond_0

    iget-object v2, p0, Lmiuix/animation/internal/AnimManager;->mUpdateMap:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {v2}, Ljava/util/concurrent/ConcurrentHashMap;->clear()V

    :cond_0
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v2

    if-eqz v2, :cond_2

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "----- removeRunningInfo"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v3, " ,id="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v3, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v3, " ,key="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v3, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    const-string v3, " "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p1, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result p1

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string p1, " ,runningInfo.size="

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p1, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {p1}, Ljava/util/concurrent/ConcurrentHashMap;->size()I

    move-result p1

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string p1, " ,isAnimRunning="

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string p1, " ,target="

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p1, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result p1

    if-eqz p1, :cond_1

    const/16 p1, 0xa

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    iget-object v1, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {v1}, Ljava/util/concurrent/ConcurrentHashMap;->size()I

    move-result v1

    if-lez v1, :cond_1

    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    invoke-virtual {p0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object p0

    invoke-interface {p0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :goto_0
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lmiuix/animation/internal/TransitionInfo;

    const-string v3, " |-- after remove resetRunInfo = "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    goto :goto_0

    :cond_1
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    new-array p1, v0, [Ljava/lang/Object;

    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_2
    return-void
.end method""",
        'replacement': """.method removeRunningInfo(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 6

    goto :goto_49

    nop

    :goto_0
    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_12

    nop

    :goto_1
    invoke-virtual {v0, v1}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_d

    nop

    :goto_2
    invoke-virtual {p0}, Ljava/util/concurrent/ConcurrentHashMap;->values()Ljava/util/Collection;

    move-result-object p0

    goto :goto_6

    nop

    :goto_3
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_41

    nop

    :goto_4
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_35

    nop

    :goto_5
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_3c

    nop

    :goto_6
    invoke-interface {p0}, Ljava/util/Collection;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :goto_7
    goto :goto_38

    nop

    :goto_8
    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_46

    nop

    :goto_9
    goto :goto_7

    :goto_a
    goto :goto_27

    nop

    :goto_b
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_37

    nop

    :goto_c
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_45

    nop

    :goto_d
    iget v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I

    goto :goto_19

    nop

    :goto_e
    invoke-virtual {p1}, Ljava/lang/Object;->hashCode()I

    move-result p1

    goto :goto_39

    nop

    :goto_f
    sub-int/2addr v0, v1

    goto :goto_2c

    nop

    :goto_10
    invoke-virtual {p1}, Ljava/util/concurrent/ConcurrentHashMap;->size()I

    move-result p1

    goto :goto_48

    nop

    :goto_11
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_2a

    nop

    :goto_12
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_13
    const-string v3, " |-- after remove resetRunInfo = "

    goto :goto_1f

    nop

    :goto_14
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_3a

    nop

    :goto_15
    iget-object p1, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_e

    nop

    :goto_16
    invoke-virtual {p0}, Lmiuix/animation/internal/AnimManager;->hasAnimSetup()Z

    move-result v2

    goto :goto_1b

    nop

    :goto_17
    const-string p1, " ,runningInfo.size="

    goto :goto_14

    nop

    :goto_18
    const-string p1, " ,isAnimRunning="

    goto :goto_23

    nop

    :goto_19
    invoke-virtual {p1}, Lmiuix/animation/internal/TransitionInfo;->getAnimCount()I

    move-result v1

    goto :goto_f

    nop

    :goto_1a
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result p1

    goto :goto_2d

    nop

    :goto_1b
    if-eqz v2, :cond_0

    goto :goto_2f

    :cond_0
    goto :goto_44

    nop

    :goto_1c
    iget-object v1, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_30

    nop

    :goto_1d
    if-gtz v1, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_40

    nop

    :goto_1e
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_3e

    nop

    :goto_1f
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_20
    return-void

    :goto_21
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(C)Ljava/lang/StringBuilder;

    goto :goto_1c

    nop

    :goto_22
    new-array v1, v0, [Lmiuix/animation/property/FloatProperty;

    goto :goto_34

    nop

    :goto_23
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_8

    nop

    :goto_24
    if-nez v2, :cond_2

    goto :goto_33

    :cond_2
    goto :goto_43

    nop

    :goto_25
    new-array p1, v0, [Ljava/lang/Object;

    goto :goto_32

    nop

    :goto_26
    iget-object p1, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_3b

    nop

    :goto_27
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_25

    nop

    :goto_28
    if-nez v1, :cond_3

    goto :goto_a

    :cond_3
    goto :goto_b

    nop

    :goto_29
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_36

    nop

    :goto_2a
    const-string v3, " ,key="

    goto :goto_3

    nop

    :goto_2b
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_15

    nop

    :goto_2c
    iput v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I

    goto :goto_3f

    nop

    :goto_2d
    if-nez p1, :cond_4

    goto :goto_a

    :cond_4
    goto :goto_47

    nop

    :goto_2e
    invoke-virtual {v2}, Ljava/util/concurrent/ConcurrentHashMap;->clear()V

    :goto_2f
    goto :goto_31

    nop

    :goto_30
    invoke-virtual {v1}, Ljava/util/concurrent/ConcurrentHashMap;->size()I

    move-result v1

    goto :goto_1d

    nop

    :goto_31
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMoreEnable()Z

    move-result v2

    goto :goto_24

    nop

    :goto_32
    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_33
    goto :goto_20

    nop

    :goto_34
    invoke-virtual {p0, v1}, Lmiuix/animation/internal/AnimManager;->isAnimRunning([Lmiuix/animation/property/FloatProperty;)Z

    move-result v1

    goto :goto_3d

    nop

    :goto_35
    const-string v3, " ,id="

    goto :goto_29

    nop

    :goto_36
    iget v3, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_11

    nop

    :goto_37
    check-cast v1, Lmiuix/animation/internal/TransitionInfo;

    goto :goto_13

    nop

    :goto_38
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_28

    nop

    :goto_39
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_17

    nop

    :goto_3a
    iget-object p1, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_10

    nop

    :goto_3b
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_1a

    nop

    :goto_3c
    const-string v3, "----- removeRunningInfo"

    goto :goto_4

    nop

    :goto_3d
    if-eqz v1, :cond_5

    goto :goto_2f

    :cond_5
    goto :goto_16

    nop

    :goto_3e
    const-string v3, " "

    goto :goto_2b

    nop

    :goto_3f
    const/4 v0, 0x0

    goto :goto_22

    nop

    :goto_40
    iget-object p0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_2

    nop

    :goto_41
    iget-object v3, p1, Lmiuix/animation/internal/TransitionInfo;->key:Ljava/lang/Object;

    goto :goto_1e

    nop

    :goto_42
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_26

    nop

    :goto_43
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_5

    nop

    :goto_44
    iget-object v2, p0, Lmiuix/animation/internal/AnimManager;->mUpdateMap:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_2e

    nop

    :goto_45
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_1

    nop

    :goto_46
    const-string p1, " ,target="

    goto :goto_42

    nop

    :goto_47
    const/16 p1, 0xa

    goto :goto_21

    nop

    :goto_48
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_18

    nop

    :goto_49
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimManager__setupTransition',
        'method': '.method setupTransition(Lmiuix/animation/internal/TransitionInfo;)V',
        'method_name': 'setupTransition',
        'method_anchors': ['invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z', 'if-eqz v0, :cond_1', 'new-instance v2, Ljava/lang/StringBuilder;', 'invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v3, "----- setupTransition "', 'invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;', 'invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z'],
        'type': 'method_replace',
        'search': """.method setupTransition(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 12

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_1

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "----- setupTransition "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result v3

    if-eqz v3, :cond_0

    const/4 v3, 0x7

    invoke-static {v3}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :cond_0
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    new-array v3, v1, [Ljava/lang/Object;

    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    iget-byte v2, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    const/4 v3, 0x3

    if-lt v2, v3, :cond_2

    if-eqz v0, :cond_7

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "----- setupTransition return because this transition has cancel or end before start: "

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-byte v2, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {p1}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object p1

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    new-array p1, v1, [Ljava/lang/Object;

    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    return-void

    :cond_2
    const/4 v3, 0x2

    const/4 v4, 0x1

    if-ne v2, v3, :cond_3

    move v5, v4

    goto :goto_0

    :cond_3
    move v5, v1

    :goto_0
    if-ge v2, v4, :cond_4

    iget-object v2, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;

    iget v6, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v6}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v6

    invoke-virtual {v2, v6}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v2}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v2

    if-eqz v2, :cond_4

    iget-object v2, p0, Lmiuix/animation/internal/AnimManager;->mObserverHandlerMap:Ljava/util/concurrent/ConcurrentHashMap;

    iget-object v6, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v6}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v6

    invoke-virtual {v6}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/Thread;->getId()J

    move-result-wide v6

    invoke-static {v6, v7}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v6

    invoke-virtual {v2, v6}, Ljava/util/concurrent/ConcurrentHashMap;->containsKey(Ljava/lang/Object;)Z

    move-result v2

    if-nez v2, :cond_4

    iget-object v2, p0, Lmiuix/animation/internal/AnimManager;->mObserverHandlerMap:Ljava/util/concurrent/ConcurrentHashMap;

    iget-object v6, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v6}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v6

    invoke-virtual {v6}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/Thread;->getId()J

    move-result-wide v6

    invoke-static {v6, v7}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v6

    new-instance v7, Lmiuix/animation/internal/TargetHandler;

    iget-object v8, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v8}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v8

    iget-object v9, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    invoke-direct {v7, v8, v9}, Lmiuix/animation/internal/TargetHandler;-><init>(Landroid/os/Looper;Lmiuix/animation/IAnimTarget;)V

    invoke-virtual {v2, v6, v7}, Ljava/util/concurrent/ConcurrentHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    if-eqz v0, :cond_4

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "----- setupTransition create TargetHandler for Looper "

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v6, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {v6}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v6

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    new-array v6, v1, [Ljava/lang/Object;

    invoke-static {v2, v6}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_4
    invoke-virtual {p1, p0}, Lmiuix/animation/internal/TransitionInfo;->initUpdateList(Lmiuix/animation/internal/TransitionInfo$IUpdateInfoCreator;)Z

    move-result v2

    if-nez v2, :cond_5

    const/4 v2, 0x4

    invoke-virtual {p0, p1, v3, v2}, Lmiuix/animation/internal/AnimManager;->notifyTransitionEndOrCancel(Lmiuix/animation/internal/TransitionInfo;II)V

    if-eqz v0, :cond_7

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "----- setupTransition info.id="

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget p1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string p1, " has cancel after setup because all properties have handled setTo."

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    new-array p1, v1, [Ljava/lang/Object;

    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    return-void

    :cond_5
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    invoke-virtual {v0, v1, p1}, Ljava/util/concurrent/ConcurrentHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I

    invoke-virtual {p1}, Lmiuix/animation/internal/TransitionInfo;->getAnimCount()I

    move-result v1

    add-int/2addr v0, v1

    iput v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I

    iget-byte v1, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    if-ge v1, v4, :cond_6

    iput-byte v4, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    :cond_6
    invoke-direct {p0, p1}, Lmiuix/animation/internal/AnimManager;->removeSameAnim(Lmiuix/animation/internal/TransitionInfo;)I

    move-result v1

    add-int/2addr v0, v1

    iput v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I

    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    iget-object v0, v0, Lmiuix/animation/base/AnimConfig;->listeners:Ljava/util/HashSet;

    invoke-virtual {v0}, Ljava/util/HashSet;->isEmpty()Z

    move-result v0

    if-nez v0, :cond_7

    if-eqz v5, :cond_7

    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimManager;->notifyReplaceTargetListeners(Lmiuix/animation/internal/TransitionInfo;)V

    :cond_7
    return-void
.end method""",
        'replacement': """.method setupTransition(Lmiuix/animation/internal/TransitionInfo;)V
    .registers 12

    goto :goto_7d

    nop

    :goto_0
    invoke-virtual {v2}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v2

    goto :goto_75

    nop

    :goto_1
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_3b

    nop

    :goto_2
    return-void

    :goto_3
    goto :goto_36

    nop

    :goto_4
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_4b

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_51

    nop

    :goto_6
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_66

    nop

    :goto_7
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_60

    nop

    :goto_8
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_6d

    nop

    :goto_9
    goto :goto_63

    :goto_a
    goto :goto_62

    nop

    :goto_b
    invoke-virtual {v6}, Ljava/lang/Thread;->getId()J

    move-result-wide v6

    goto :goto_53

    nop

    :goto_c
    invoke-direct {p0, p1}, Lmiuix/animation/internal/AnimManager;->removeSameAnim(Lmiuix/animation/internal/TransitionInfo;)I

    move-result v1

    goto :goto_64

    nop

    :goto_d
    iput v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I

    goto :goto_72

    nop

    :goto_e
    invoke-virtual {v6}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v6

    goto :goto_18

    nop

    :goto_f
    if-nez v3, :cond_0

    goto :goto_6b

    :cond_0
    goto :goto_3c

    nop

    :goto_10
    if-nez v0, :cond_1

    goto :goto_21

    :cond_1
    goto :goto_8

    nop

    :goto_11
    const/4 v2, 0x4

    goto :goto_19

    nop

    :goto_12
    if-eqz v0, :cond_2

    goto :goto_4e

    :cond_2
    goto :goto_1e

    nop

    :goto_13
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_30

    nop

    :goto_14
    new-instance v7, Lmiuix/animation/internal/TargetHandler;

    goto :goto_47

    nop

    :goto_15
    if-ge v2, v3, :cond_3

    goto :goto_3

    :cond_3
    goto :goto_78

    nop

    :goto_16
    invoke-static {v6, v7}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v6

    goto :goto_2a

    nop

    :goto_17
    iget-object v2, p0, Lmiuix/animation/internal/AnimManager;->mPrepareInfo:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_2b

    nop

    :goto_18
    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_74

    nop

    :goto_19
    invoke-virtual {p0, p1, v3, v2}, Lmiuix/animation/internal/AnimManager;->notifyTransitionEndOrCancel(Lmiuix/animation/internal/TransitionInfo;II)V

    goto :goto_56

    nop

    :goto_1a
    const-string v2, "----- setupTransition return because this transition has cancel or end before start: "

    goto :goto_1

    nop

    :goto_1b
    iput-byte v4, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    :goto_1c
    goto :goto_c

    nop

    :goto_1d
    iget-object v6, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_5c

    nop

    :goto_1e
    if-nez v5, :cond_4

    goto :goto_4e

    :cond_4
    goto :goto_4d

    nop

    :goto_1f
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_20
    invoke-static {v2, v3}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_21
    goto :goto_2c

    nop

    :goto_22
    invoke-virtual {v0, v1, p1}, Ljava/util/concurrent/ConcurrentHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_57

    nop

    :goto_23
    const-string p1, " has cancel after setup because all properties have handled setTo."

    goto :goto_26

    nop

    :goto_24
    iget-object v0, v0, Lmiuix/animation/base/AnimConfig;->listeners:Ljava/util/HashSet;

    goto :goto_68

    nop

    :goto_25
    invoke-virtual {p1}, Lmiuix/animation/internal/TransitionInfo;->getAnimCount()I

    move-result v1

    goto :goto_34

    nop

    :goto_26
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_32

    nop

    :goto_27
    if-eqz v2, :cond_5

    goto :goto_41

    :cond_5
    goto :goto_11

    nop

    :goto_28
    invoke-static {v3}, Lmiuix/animation/utils/LogUtils;->getStackTrace(I)Ljava/lang/String;

    move-result-object v3

    goto :goto_6a

    nop

    :goto_29
    iget-object v2, p0, Lmiuix/animation/internal/AnimManager;->mObserverHandlerMap:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_5a

    nop

    :goto_2a
    invoke-virtual {v2, v6}, Ljava/util/concurrent/ConcurrentHashMap;->containsKey(Ljava/lang/Object;)Z

    move-result v2

    goto :goto_70

    nop

    :goto_2b
    iget v6, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_3d

    nop

    :goto_2c
    iget-byte v2, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    goto :goto_2f

    nop

    :goto_2d
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_1a

    nop

    :goto_2e
    invoke-virtual {p1}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object p1

    goto :goto_43

    nop

    :goto_2f
    const/4 v3, 0x3

    goto :goto_15

    nop

    :goto_30
    iget-object p1, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_2e

    nop

    :goto_31
    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_40

    nop

    :goto_32
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_49

    nop

    :goto_33
    invoke-virtual {v8}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v8

    goto :goto_48

    nop

    :goto_34
    add-int/2addr v0, v1

    goto :goto_45

    nop

    :goto_35
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_13

    nop

    :goto_36
    const/4 v3, 0x2

    goto :goto_6c

    nop

    :goto_37
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_2d

    nop

    :goto_38
    iget-object v2, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_0

    nop

    :goto_39
    iget-byte v1, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    goto :goto_3e

    nop

    :goto_3a
    invoke-virtual {v6}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v6

    goto :goto_5b

    nop

    :goto_3b
    iget-byte v2, p1, Lmiuix/animation/internal/TransitionInfo;->state:B

    goto :goto_61

    nop

    :goto_3c
    const/4 v3, 0x7

    goto :goto_28

    nop

    :goto_3d
    invoke-static {v6}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v6

    goto :goto_79

    nop

    :goto_3e
    if-lt v1, v4, :cond_6

    goto :goto_1c

    :cond_6
    goto :goto_1b

    nop

    :goto_3f
    const-string v0, "----- setupTransition info.id="

    goto :goto_6

    nop

    :goto_40
    return-void

    :goto_41
    goto :goto_5

    nop

    :goto_42
    const/4 v1, 0x0

    goto :goto_10

    nop

    :goto_43
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_73

    nop

    :goto_44
    if-nez v0, :cond_7

    goto :goto_80

    :cond_7
    goto :goto_4

    nop

    :goto_45
    iput v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I

    goto :goto_39

    nop

    :goto_46
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_50

    nop

    :goto_47
    iget-object v8, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_33

    nop

    :goto_48
    iget-object v9, p0, Lmiuix/animation/internal/AnimManager;->mTarget:Lmiuix/animation/IAnimTarget;

    goto :goto_65

    nop

    :goto_49
    new-array p1, v1, [Ljava/lang/Object;

    goto :goto_31

    nop

    :goto_4a
    invoke-virtual {v6}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v6

    goto :goto_b

    nop

    :goto_4b
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_67

    nop

    :goto_4c
    iget-object v2, p0, Lmiuix/animation/internal/AnimManager;->mObserverHandlerMap:Ljava/util/concurrent/ConcurrentHashMap;

    goto :goto_1d

    nop

    :goto_4d
    invoke-virtual {p0, p1}, Lmiuix/animation/internal/AnimManager;->notifyReplaceTargetListeners(Lmiuix/animation/internal/TransitionInfo;)V

    :goto_4e
    goto :goto_59

    nop

    :goto_4f
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_23

    nop

    :goto_50
    new-array v3, v1, [Ljava/lang/Object;

    goto :goto_20

    nop

    :goto_51
    iget v1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_6e

    nop

    :goto_52
    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_69

    nop

    :goto_53
    invoke-static {v6, v7}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v6

    goto :goto_14

    nop

    :goto_54
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_5f

    nop

    :goto_55
    new-array v6, v1, [Ljava/lang/Object;

    goto :goto_7f

    nop

    :goto_56
    if-nez v0, :cond_8

    goto :goto_4e

    :cond_8
    goto :goto_54

    nop

    :goto_57
    iget v0, p0, Lmiuix/animation/internal/AnimManager;->mRunningAnimCount:I

    goto :goto_25

    nop

    :goto_58
    new-array p1, v1, [Ljava/lang/Object;

    goto :goto_7a

    nop

    :goto_59
    return-void

    :goto_5a
    iget-object v6, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_76

    nop

    :goto_5b
    invoke-virtual {v6}, Ljava/lang/Thread;->getId()J

    move-result-wide v6

    goto :goto_16

    nop

    :goto_5c
    invoke-virtual {v6}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v6

    goto :goto_4a

    nop

    :goto_5d
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_37

    nop

    :goto_5e
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_5d

    nop

    :goto_5f
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_3f

    nop

    :goto_60
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result v3

    goto :goto_f

    nop

    :goto_61
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_35

    nop

    :goto_62
    move v5, v1

    :goto_63
    goto :goto_77

    nop

    :goto_64
    add-int/2addr v0, v1

    goto :goto_d

    nop

    :goto_65
    invoke-direct {v7, v8, v9}, Lmiuix/animation/internal/TargetHandler;-><init>(Landroid/os/Looper;Lmiuix/animation/IAnimTarget;)V

    goto :goto_71

    nop

    :goto_66
    iget p1, p1, Lmiuix/animation/internal/TransitionInfo;->id:I

    goto :goto_4f

    nop

    :goto_67
    const-string v6, "----- setupTransition create TargetHandler for Looper "

    goto :goto_52

    nop

    :goto_68
    invoke-virtual {v0}, Ljava/util/HashSet;->isEmpty()Z

    move-result v0

    goto :goto_12

    nop

    :goto_69
    iget-object v6, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_e

    nop

    :goto_6a
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    :goto_6b
    goto :goto_46

    nop

    :goto_6c
    const/4 v4, 0x1

    goto :goto_7b

    nop

    :goto_6d
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_7c

    nop

    :goto_6e
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_22

    nop

    :goto_6f
    invoke-virtual {p1, p0}, Lmiuix/animation/internal/TransitionInfo;->initUpdateList(Lmiuix/animation/internal/TransitionInfo$IUpdateInfoCreator;)Z

    move-result v2

    goto :goto_27

    nop

    :goto_70
    if-eqz v2, :cond_9

    goto :goto_80

    :cond_9
    goto :goto_4c

    nop

    :goto_71
    invoke-virtual {v2, v6, v7}, Ljava/util/concurrent/ConcurrentHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_44

    nop

    :goto_72
    iget-object v0, p1, Lmiuix/animation/internal/TransitionInfo;->config:Lmiuix/animation/base/AnimConfig;

    goto :goto_24

    nop

    :goto_73
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_58

    nop

    :goto_74
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_55

    nop

    :goto_75
    if-nez v2, :cond_a

    goto :goto_80

    :cond_a
    goto :goto_29

    nop

    :goto_76
    invoke-virtual {v6}, Lmiuix/animation/base/AnimConfig;->getObserverLooper()Landroid/os/Looper;

    move-result-object v6

    goto :goto_3a

    nop

    :goto_77
    if-lt v2, v4, :cond_b

    goto :goto_80

    :cond_b
    goto :goto_17

    nop

    :goto_78
    if-nez v0, :cond_c

    goto :goto_4e

    :cond_c
    goto :goto_5e

    nop

    :goto_79
    invoke-virtual {v2, v6}, Ljava/util/concurrent/ConcurrentHashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_38

    nop

    :goto_7a
    invoke-static {p0, p1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_2

    nop

    :goto_7b
    if-eq v2, v3, :cond_d

    goto :goto_a

    :cond_d
    goto :goto_7e

    nop

    :goto_7c
    const-string v3, "----- setupTransition "

    goto :goto_1f

    nop

    :goto_7d
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogMainEnabled()Z

    move-result v0

    goto :goto_42

    nop

    :goto_7e
    move v5, v4

    goto :goto_9

    nop

    :goto_7f
    invoke-static {v2, v6}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_80
    goto :goto_6f

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
