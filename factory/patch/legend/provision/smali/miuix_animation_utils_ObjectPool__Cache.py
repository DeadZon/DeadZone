TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/utils/ObjectPool$Cache.smali'
CLASS_FALLBACK_NAMES = ['ObjectPool$Cache.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_animation_utils_ObjectPool__Cache__releaseObject',
        'method': '.method releaseObject(Landroid/os/Handler;Ljava/lang/Object;)V',
        'method_name': 'releaseObject',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mCacheRecord:Ljava/util/Map;', 'invoke-static {p2}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I', 'invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'sget-object v2, Ljava/lang/Boolean;->TRUE:Ljava/lang/Boolean;', 'invoke-interface {v0, v1, v2}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;', 'invoke-virtual {v0, p2}, Ljava/util/concurrent/ConcurrentLinkedQueue;->add(Ljava/lang/Object;)Z'],
        'type': 'method_replace',
        'search': """.method releaseObject(Landroid/os/Handler;Ljava/lang/Object;)V
    .registers 6

    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mCacheRecord:Ljava/util/Map;

    invoke-static {p2}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I

    move-result v1

    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    sget-object v2, Ljava/lang/Boolean;->TRUE:Ljava/lang/Boolean;

    invoke-interface {v0, v1, v2}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;

    invoke-virtual {v0, p2}, Ljava/util/concurrent/ConcurrentLinkedQueue;->add(Ljava/lang/Object;)Z

    const/4 p2, 0x0

    if-eqz p1, :cond_3

    iget-boolean v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mPendingShrink:Z

    if-eqz v0, :cond_1

    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->shrinkTask:Ljava/lang/Runnable;

    invoke-virtual {p1, v0}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    iput-boolean p2, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mPendingShrink:Z

    :cond_1
    iget-object p2, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;

    invoke-virtual {p2}, Ljava/util/concurrent/ConcurrentLinkedQueue;->size()I

    move-result p2

    const/16 v0, 0xa

    if-le p2, v0, :cond_2

    const/4 p2, 0x1

    iput-boolean p2, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mPendingShrink:Z

    iget-object p0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->shrinkTask:Ljava/lang/Runnable;

    const-wide/16 v0, 0x1388

    invoke-virtual {p1, p0, v0, v1}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    :cond_2
    :goto_0
    return-void

    :cond_3
    iput-boolean p2, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mPendingShrink:Z

    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string p2, "ObjectPool.releaseObject handler is null! looper: "

    invoke-virtual {p1, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;

    move-result-object p2

    invoke-virtual {p1, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    const-string p2, "miuix_anim"

    invoke-static {p2, p1}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    iget-object p0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->shrinkTask:Ljava/lang/Runnable;

    invoke-interface {p0}, Ljava/lang/Runnable;->run()V

    return-void
.end method""",
        'replacement': """.method releaseObject(Landroid/os/Handler;Ljava/lang/Object;)V
    .registers 6

    goto :goto_25

    nop

    :goto_0
    const-wide/16 v0, 0x1388

    goto :goto_22

    nop

    :goto_1
    goto :goto_23

    :goto_2
    goto :goto_19

    nop

    :goto_3
    sget-object v2, Ljava/lang/Boolean;->TRUE:Ljava/lang/Boolean;

    goto :goto_29

    nop

    :goto_4
    iget-boolean v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mPendingShrink:Z

    goto :goto_16

    nop

    :goto_5
    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_20

    nop

    :goto_6
    iput-boolean p2, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mPendingShrink:Z

    goto :goto_11

    nop

    :goto_7
    invoke-virtual {v0, p2}, Ljava/util/concurrent/ConcurrentLinkedQueue;->add(Ljava/lang/Object;)Z

    goto :goto_14

    nop

    :goto_8
    invoke-static {p2, p1}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1a

    nop

    :goto_9
    const-string p2, "miuix_anim"

    goto :goto_8

    nop

    :goto_a
    const/16 v0, 0xa

    goto :goto_1d

    nop

    :goto_b
    iput-boolean p2, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mPendingShrink:Z

    :goto_c
    goto :goto_e

    nop

    :goto_d
    invoke-virtual {p2}, Ljava/util/concurrent/ConcurrentLinkedQueue;->size()I

    move-result p2

    goto :goto_a

    nop

    :goto_e
    iget-object p2, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;

    goto :goto_d

    nop

    :goto_f
    if-nez p1, :cond_0

    goto :goto_13

    :cond_0
    goto :goto_4

    nop

    :goto_10
    invoke-static {p2}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I

    move-result v1

    goto :goto_18

    nop

    :goto_11
    iget-object p0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->shrinkTask:Ljava/lang/Runnable;

    goto :goto_0

    nop

    :goto_12
    return-void

    :goto_13
    goto :goto_17

    nop

    :goto_14
    const/4 p2, 0x0

    goto :goto_f

    nop

    :goto_15
    if-nez v0, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_1

    nop

    :goto_16
    if-nez v0, :cond_2

    goto :goto_c

    :cond_2
    goto :goto_28

    nop

    :goto_17
    iput-boolean p2, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mPendingShrink:Z

    goto :goto_1f

    nop

    :goto_18
    invoke-static {v1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_3

    nop

    :goto_19
    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;

    goto :goto_7

    nop

    :goto_1a
    iget-object p0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->shrinkTask:Ljava/lang/Runnable;

    goto :goto_2a

    nop

    :goto_1b
    invoke-virtual {p1, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_27

    nop

    :goto_1c
    invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;

    move-result-object p2

    goto :goto_1b

    nop

    :goto_1d
    if-gt p2, v0, :cond_3

    goto :goto_23

    :cond_3
    goto :goto_24

    nop

    :goto_1e
    invoke-virtual {p1, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1c

    nop

    :goto_1f
    new-instance p1, Ljava/lang/StringBuilder;

    goto :goto_5

    nop

    :goto_20
    const-string p2, "ObjectPool.releaseObject handler is null! looper: "

    goto :goto_1e

    nop

    :goto_21
    return-void

    :goto_22
    invoke-virtual {p1, p0, v0, v1}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z

    :goto_23
    goto :goto_12

    nop

    :goto_24
    const/4 p2, 0x1

    goto :goto_6

    nop

    :goto_25
    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mCacheRecord:Ljava/util/Map;

    goto :goto_10

    nop

    :goto_26
    invoke-virtual {p1, v0}, Landroid/os/Handler;->removeCallbacks(Ljava/lang/Runnable;)V

    goto :goto_b

    nop

    :goto_27
    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_9

    nop

    :goto_28
    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->shrinkTask:Ljava/lang/Runnable;

    goto :goto_26

    nop

    :goto_29
    invoke-interface {v0, v1, v2}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_15

    nop

    :goto_2a
    invoke-interface {p0}, Ljava/lang/Runnable;->run()V

    goto :goto_21

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_utils_ObjectPool__Cache__shrink',
        'method': '.method shrink()V',
        'method_name': 'shrink',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;', 'invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentLinkedQueue;->size()I', 'if-le v0, v1, :cond_1', 'iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;', 'invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentLinkedQueue;->poll()Ljava/lang/Object;', 'if-nez v0, :cond_0', 'iget-object v1, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mCacheRecord:Ljava/util/Map;', 'invoke-static {v0}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I'],
        'type': 'method_replace',
        'search': """.method shrink()V
    .registers 3

    :goto_0
    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;

    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentLinkedQueue;->size()I

    move-result v0

    const/16 v1, 0xa

    if-le v0, v1, :cond_1

    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;

    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentLinkedQueue;->poll()Ljava/lang/Object;

    move-result-object v0

    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    iget-object v1, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mCacheRecord:Ljava/util/Map;

    invoke-static {v0}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I

    move-result v0

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    invoke-interface {v1, v0}, Ljava/util/Map;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_0

    :cond_1
    :goto_1
    return-void
.end method""",
        'replacement': """.method shrink()V
    .registers 3

    :goto_0
    goto :goto_2

    nop

    :goto_1
    if-gt v0, v1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_8

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;

    goto :goto_10

    nop

    :goto_3
    invoke-interface {v1, v0}, Ljava/util/Map;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_5

    nop

    :goto_4
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_3

    nop

    :goto_5
    goto :goto_0

    :goto_6
    goto :goto_a

    nop

    :goto_7
    if-eqz v0, :cond_1

    goto :goto_f

    :cond_1
    goto :goto_e

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;

    goto :goto_d

    nop

    :goto_9
    const/16 v1, 0xa

    goto :goto_1

    nop

    :goto_a
    return-void

    :goto_b
    invoke-static {v0}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I

    move-result v0

    goto :goto_4

    nop

    :goto_c
    iget-object v1, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mCacheRecord:Ljava/util/Map;

    goto :goto_b

    nop

    :goto_d
    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentLinkedQueue;->poll()Ljava/lang/Object;

    move-result-object v0

    goto :goto_7

    nop

    :goto_e
    goto :goto_6

    :goto_f
    goto :goto_c

    nop

    :goto_10
    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentLinkedQueue;->size()I

    move-result v0

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_utils_ObjectPool__Cache__acquireObject',
        'method': '.method varargs acquireObject(Ljava/lang/Class;[Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'acquireObject',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;', 'invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentLinkedQueue;->poll()Ljava/lang/Object;', 'if-eqz v0, :cond_0', 'iget-object p0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mCacheRecord:Ljava/util/Map;', 'invoke-static {v0}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I', 'invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'invoke-interface {p0, p1}, Ljava/util/Map;->remove(Ljava/lang/Object;)Ljava/lang/Object;', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method varargs acquireObject(Ljava/lang/Class;[Ljava/lang/Object;)Ljava/lang/Object;
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Ljava/lang/Class<",
            "TT;>;[",
            "Ljava/lang/Object;",
            ")TT;"
        }
    .end annotation

    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;

    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentLinkedQueue;->poll()Ljava/lang/Object;

    move-result-object v0

    if-eqz v0, :cond_0

    iget-object p0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mCacheRecord:Ljava/util/Map;

    invoke-static {v0}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I

    move-result p1

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    invoke-interface {p0, p1}, Ljava/util/Map;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    return-object v0

    :cond_0
    if-eqz p1, :cond_1

    invoke-static {p1, p2}, Lmiuix/animation/utils/ObjectPool;->access$000(Ljava/lang/Class;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0

    :cond_1
    return-object v0
.end method""",
        'replacement': """.method varargs acquireObject(Ljava/lang/Class;[Ljava/lang/Object;)Ljava/lang/Object;
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "<T:",
            "Ljava/lang/Object;",
            ">(",
            "Ljava/lang/Class<",
            "TT;>;[",
            "Ljava/lang/Object;",
            ")TT;"
        }
    .end annotation

    goto :goto_8

    nop

    :goto_0
    invoke-virtual {v0}, Ljava/util/concurrent/ConcurrentLinkedQueue;->poll()Ljava/lang/Object;

    move-result-object v0

    goto :goto_9

    nop

    :goto_1
    if-nez p1, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_3

    nop

    :goto_2
    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    goto :goto_5

    nop

    :goto_3
    invoke-static {p1, p2}, Lmiuix/animation/utils/ObjectPool;->access$000(Ljava/lang/Class;[Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_6

    nop

    :goto_4
    return-object v0

    :goto_5
    invoke-interface {p0, p1}, Ljava/util/Map;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_a

    nop

    :goto_6
    return-object p0

    :goto_7
    goto :goto_4

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->pool:Ljava/util/concurrent/ConcurrentLinkedQueue;

    goto :goto_0

    nop

    :goto_9
    if-nez v0, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_c

    nop

    :goto_a
    return-object v0

    :goto_b
    goto :goto_1

    nop

    :goto_c
    iget-object p0, p0, Lmiuix/animation/utils/ObjectPool$Cache;->mCacheRecord:Ljava/util/Map;

    goto :goto_d

    nop

    :goto_d
    invoke-static {v0}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I

    move-result p1

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
