TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/core/util/Pools$BasePool.smali'
CLASS_FALLBACK_NAMES = ['Pools$BasePool.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/core/util/Pools$Pool;']

PATCHES = [
    {
        'id': 'miuix_core_util_Pools__BasePool__doAcquire',
        'method': '.method protected final doAcquire()Ljava/lang/Object;',
        'method_name': 'doAcquire',
        'method_anchors': ['iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mInstanceHolder:Lmiuix/core/util/Pools$IInstanceHolder;', 'if-eqz v0, :cond_2', 'invoke-interface {v0}, Lmiuix/core/util/Pools$IInstanceHolder;->get()Ljava/lang/Object;', 'if-nez v0, :cond_1', 'iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mManager:Lmiuix/core/util/Pools$Manager;', 'invoke-virtual {v0}, Lmiuix/core/util/Pools$Manager;->createInstance()Ljava/lang/Object;', 'if-eqz v0, :cond_0', 'new-instance p0, Ljava/lang/IllegalStateException;'],
        'type': 'method_replace',
        'search': """.method protected final doAcquire()Ljava/lang/Object;
    .registers 2

    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mInstanceHolder:Lmiuix/core/util/Pools$IInstanceHolder;

    if-eqz v0, :cond_2

    invoke-interface {v0}, Lmiuix/core/util/Pools$IInstanceHolder;->get()Ljava/lang/Object;

    move-result-object v0

    if-nez v0, :cond_1

    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mManager:Lmiuix/core/util/Pools$Manager;

    invoke-virtual {v0}, Lmiuix/core/util/Pools$Manager;->createInstance()Ljava/lang/Object;

    move-result-object v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string v0, "manager create instance cannot return null"

    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0

    :cond_1
    :goto_0
    iget-object p0, p0, Lmiuix/core/util/Pools$BasePool;->mManager:Lmiuix/core/util/Pools$Manager;

    invoke-virtual {p0, v0}, Lmiuix/core/util/Pools$Manager;->onAcquire(Ljava/lang/Object;)V

    return-object v0

    :cond_2
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string v0, "Cannot acquire object after close()"

    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method protected final doAcquire()Ljava/lang/Object;
    .registers 2

    goto :goto_f

    nop

    :goto_0
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_1

    nop

    :goto_1
    const-string v0, "Cannot acquire object after close()"

    goto :goto_a

    nop

    :goto_2
    const-string v0, "manager create instance cannot return null"

    goto :goto_c

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_13

    nop

    :goto_4
    invoke-virtual {v0}, Lmiuix/core/util/Pools$Manager;->createInstance()Ljava/lang/Object;

    move-result-object v0

    goto :goto_14

    nop

    :goto_5
    invoke-virtual {p0, v0}, Lmiuix/core/util/Pools$Manager;->onAcquire(Ljava/lang/Object;)V

    goto :goto_6

    nop

    :goto_6
    return-object v0

    :goto_7
    goto :goto_0

    nop

    :goto_8
    throw p0

    :goto_9
    goto :goto_e

    nop

    :goto_a
    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_d

    nop

    :goto_b
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_2

    nop

    :goto_c
    invoke-direct {p0, v0}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_8

    nop

    :goto_d
    throw p0

    :goto_e
    iget-object p0, p0, Lmiuix/core/util/Pools$BasePool;->mManager:Lmiuix/core/util/Pools$Manager;

    goto :goto_5

    nop

    :goto_f
    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mInstanceHolder:Lmiuix/core/util/Pools$IInstanceHolder;

    goto :goto_12

    nop

    :goto_10
    goto :goto_9

    :goto_11
    goto :goto_b

    nop

    :goto_12
    if-nez v0, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_15

    nop

    :goto_13
    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mManager:Lmiuix/core/util/Pools$Manager;

    goto :goto_4

    nop

    :goto_14
    if-nez v0, :cond_2

    goto :goto_11

    :cond_2
    goto :goto_10

    nop

    :goto_15
    invoke-interface {v0}, Lmiuix/core/util/Pools$IInstanceHolder;->get()Ljava/lang/Object;

    move-result-object v0

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_util_Pools__BasePool__doRelease',
        'method': '.method protected final doRelease(Ljava/lang/Object;)V',
        'method_name': 'doRelease',
        'method_anchors': ['iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mInstanceHolder:Lmiuix/core/util/Pools$IInstanceHolder;', 'if-eqz v0, :cond_2', 'if-nez p1, :cond_0', 'iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mManager:Lmiuix/core/util/Pools$Manager;', 'invoke-virtual {v0, p1}, Lmiuix/core/util/Pools$Manager;->onRelease(Ljava/lang/Object;)V', 'iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mInstanceHolder:Lmiuix/core/util/Pools$IInstanceHolder;', 'invoke-interface {v0, p1}, Lmiuix/core/util/Pools$IInstanceHolder;->put(Ljava/lang/Object;)Z', 'if-nez v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected final doRelease(Ljava/lang/Object;)V
    .registers 3

    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mInstanceHolder:Lmiuix/core/util/Pools$IInstanceHolder;

    if-eqz v0, :cond_2

    if-nez p1, :cond_0

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mManager:Lmiuix/core/util/Pools$Manager;

    invoke-virtual {v0, p1}, Lmiuix/core/util/Pools$Manager;->onRelease(Ljava/lang/Object;)V

    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mInstanceHolder:Lmiuix/core/util/Pools$IInstanceHolder;

    invoke-interface {v0, p1}, Lmiuix/core/util/Pools$IInstanceHolder;->put(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_1

    iget-object p0, p0, Lmiuix/core/util/Pools$BasePool;->mManager:Lmiuix/core/util/Pools$Manager;

    invoke-virtual {p0, p1}, Lmiuix/core/util/Pools$Manager;->onDestroy(Ljava/lang/Object;)V

    :cond_1
    :goto_0
    return-void

    :cond_2
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string p1, "Cannot release object after close()"

    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method protected final doRelease(Ljava/lang/Object;)V
    .registers 3

    goto :goto_6

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mManager:Lmiuix/core/util/Pools$Manager;

    goto :goto_10

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_e

    nop

    :goto_2
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_b

    nop

    :goto_3
    throw p0

    :goto_4
    invoke-virtual {p0, p1}, Lmiuix/core/util/Pools$Manager;->onDestroy(Ljava/lang/Object;)V

    :goto_5
    goto :goto_9

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mInstanceHolder:Lmiuix/core/util/Pools$IInstanceHolder;

    goto :goto_f

    nop

    :goto_7
    goto :goto_5

    :goto_8
    goto :goto_0

    nop

    :goto_9
    return-void

    :goto_a
    goto :goto_2

    nop

    :goto_b
    const-string p1, "Cannot release object after close()"

    goto :goto_d

    nop

    :goto_c
    invoke-interface {v0, p1}, Lmiuix/core/util/Pools$IInstanceHolder;->put(Ljava/lang/Object;)Z

    move-result v0

    goto :goto_1

    nop

    :goto_d
    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_e
    iget-object p0, p0, Lmiuix/core/util/Pools$BasePool;->mManager:Lmiuix/core/util/Pools$Manager;

    goto :goto_4

    nop

    :goto_f
    if-nez v0, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_12

    nop

    :goto_10
    invoke-virtual {v0, p1}, Lmiuix/core/util/Pools$Manager;->onRelease(Ljava/lang/Object;)V

    goto :goto_11

    nop

    :goto_11
    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool;->mInstanceHolder:Lmiuix/core/util/Pools$IInstanceHolder;

    goto :goto_c

    nop

    :goto_12
    if-eqz p1, :cond_2

    goto :goto_8

    :cond_2
    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
