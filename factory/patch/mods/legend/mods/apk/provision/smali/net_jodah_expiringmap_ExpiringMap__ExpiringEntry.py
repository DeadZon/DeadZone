TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'net/jodah/expiringmap/ExpiringMap$ExpiringEntry.smali'
CLASS_FALLBACK_NAMES = ['ExpiringMap$ExpiringEntry.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/lang/Comparable;']

PATCHES = [
    {
        'id': 'net_jodah_expiringmap_ExpiringMap__ExpiringEntry__cancel',
        'method': '.method declared-synchronized cancel()Z',
        'method_name': 'cancel',
        'method_anchors': ['iget-boolean v0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z', 'iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;', 'if-eqz v1, :cond_0', 'iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;', 'invoke-interface {v1, v2}, Ljava/util/concurrent/Future;->cancel(Z)Z', 'iput-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;', 'iput-boolean v2, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z', 'return v0'],
        'type': 'method_replace',
        'search': """.method declared-synchronized cancel()Z
    .registers 4

    monitor-enter p0

    :try_start_0
    iget-boolean v0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z

    iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;

    const/4 v2, 0x0

    if-eqz v1, :cond_0

    iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;

    invoke-interface {v1, v2}, Ljava/util/concurrent/Future;->cancel(Z)Z

    goto :goto_0

    :catchall_0
    move-exception v0

    goto :goto_1

    :cond_0
    :goto_0
    const/4 v1, 0x0

    iput-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;

    iput-boolean v2, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    monitor-exit p0

    return v0

    :goto_1
    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v0
.end method""",
        'replacement': """.method declared-synchronized cancel()Z
    .registers 4

    goto :goto_0

    nop

    :goto_0
    monitor-enter p0

    :try_start_0
    iget-boolean v0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z

    iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;

    const/4 v2, 0x0

    if-eqz v1, :cond_0

    iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;

    invoke-interface {v1, v2}, Ljava/util/concurrent/Future;->cancel(Z)Z

    goto :goto_1

    :catchall_0
    move-exception v0

    goto :goto_3

    :cond_0
    :goto_1
    const/4 v1, 0x0

    iput-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;

    iput-boolean v2, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_5

    nop

    :goto_2
    return v0

    :goto_3
    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_4

    nop

    :goto_4
    throw v0

    :goto_5
    monitor-exit p0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'net_jodah_expiringmap_ExpiringMap__ExpiringEntry__getValue',
        'method': '.method declared-synchronized getValue()Ljava/lang/Object;',
        'method_name': 'getValue',
        'method_anchors': ['iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->value:Ljava/lang/Object;', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method declared-synchronized getValue()Ljava/lang/Object;
    .registers 2

    monitor-enter p0

    :try_start_0
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->value:Ljava/lang/Object;
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    monitor-exit p0

    return-object v0

    :catchall_0
    move-exception v0

    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v0
.end method""",
        'replacement': """.method declared-synchronized getValue()Ljava/lang/Object;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    monitor-enter p0

    :try_start_0
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->value:Ljava/lang/Object;
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop

    :goto_1
    monitor-exit p0

    goto :goto_3

    nop

    :goto_2
    throw v0

    :goto_3
    return-object v0

    :catchall_0
    move-exception v0

    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'net_jodah_expiringmap_ExpiringMap__ExpiringEntry__schedule',
        'method': '.method declared-synchronized schedule(Ljava/util/concurrent/Future;)V',
        'method_name': 'schedule',
        'method_anchors': ['iput-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;', 'iput-boolean p1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method declared-synchronized schedule(Ljava/util/concurrent/Future;)V
    .registers 2

    monitor-enter p0

    :try_start_0
    iput-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;

    const/4 p1, 0x1

    iput-boolean p1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    monitor-exit p0

    return-void

    :catchall_0
    move-exception p1

    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw p1
.end method""",
        'replacement': """.method declared-synchronized schedule(Ljava/util/concurrent/Future;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    monitor-exit p0

    goto :goto_1

    nop

    :goto_1
    return-void

    :catchall_0
    move-exception p1

    :try_start_0
    monitor-exit p0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_2

    nop

    :goto_2
    throw p1

    :goto_3
    monitor-enter p0

    :try_start_1
    iput-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->entryFuture:Ljava/util/concurrent/Future;

    const/4 p1, 0x1

    iput-boolean p1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'net_jodah_expiringmap_ExpiringMap__ExpiringEntry__setValue',
        'method': '.method declared-synchronized setValue(Ljava/lang/Object;)V',
        'method_name': 'setValue',
        'method_anchors': ['iput-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->value:Ljava/lang/Object;', 'return-void'],
        'type': 'method_replace',
        'search': """.method declared-synchronized setValue(Ljava/lang/Object;)V
    .registers 2

    monitor-enter p0

    :try_start_0
    iput-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->value:Ljava/lang/Object;
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    monitor-exit p0

    return-void

    :catchall_0
    move-exception p1

    :try_start_1
    monitor-exit p0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw p1
.end method""",
        'replacement': """.method declared-synchronized setValue(Ljava/lang/Object;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :catchall_0
    move-exception p1

    :try_start_0
    monitor-exit p0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_2

    nop

    :goto_1
    monitor-enter p0

    :try_start_1
    iput-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->value:Ljava/lang/Object;
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_3

    nop

    :goto_2
    throw p1

    :goto_3
    monitor-exit p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'net_jodah_expiringmap_ExpiringMap__ExpiringEntry__resetExpiration',
        'method': '.method resetExpiration()V',
        'method_name': 'resetExpiration',
        'method_anchors': ['iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->expectedExpiration:Ljava/util/concurrent/atomic/AtomicLong;', 'iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->expirationNanos:Ljava/util/concurrent/atomic/AtomicLong;', 'invoke-virtual {p0}, Ljava/util/concurrent/atomic/AtomicLong;->get()J', 'invoke-static {}, Ljava/lang/System;->nanoTime()J', 'invoke-virtual {v0, v1, v2}, Ljava/util/concurrent/atomic/AtomicLong;->set(J)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method resetExpiration()V
    .registers 6

    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->expectedExpiration:Ljava/util/concurrent/atomic/AtomicLong;

    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->expirationNanos:Ljava/util/concurrent/atomic/AtomicLong;

    invoke-virtual {p0}, Ljava/util/concurrent/atomic/AtomicLong;->get()J

    move-result-wide v1

    invoke-static {}, Ljava/lang/System;->nanoTime()J

    move-result-wide v3

    add-long/2addr v1, v3

    invoke-virtual {v0, v1, v2}, Ljava/util/concurrent/atomic/AtomicLong;->set(J)V

    return-void
.end method""",
        'replacement': """.method resetExpiration()V
    .registers 6

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0}, Ljava/util/concurrent/atomic/AtomicLong;->get()J

    move-result-wide v1

    goto :goto_4

    nop

    :goto_1
    return-void

    :goto_2
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->expectedExpiration:Ljava/util/concurrent/atomic/AtomicLong;

    goto :goto_6

    nop

    :goto_3
    invoke-virtual {v0, v1, v2}, Ljava/util/concurrent/atomic/AtomicLong;->set(J)V

    goto :goto_1

    nop

    :goto_4
    invoke-static {}, Ljava/lang/System;->nanoTime()J

    move-result-wide v3

    goto :goto_5

    nop

    :goto_5
    add-long/2addr v1, v3

    goto :goto_3

    nop

    :goto_6
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->expirationNanos:Ljava/util/concurrent/atomic/AtomicLong;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
