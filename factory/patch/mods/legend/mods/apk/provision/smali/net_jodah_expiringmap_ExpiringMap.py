TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'net/jodah/expiringmap/ExpiringMap.smali'
CLASS_FALLBACK_NAMES = ['ExpiringMap.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/util/concurrent/ConcurrentMap;']

PATCHES = [
    {
        'id': 'net_jodah_expiringmap_ExpiringMap__getEntry',
        'method': '.method getEntry(Ljava/lang/Object;)Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;',
        'method_name': 'getEntry',
        'method_anchors': ['iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->readLock:Ljava/util/concurrent/locks/Lock;', 'invoke-interface {v0}, Ljava/util/concurrent/locks/Lock;->lock()V', 'iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;', 'invoke-interface {v0, p1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;', 'check-cast p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;', 'iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->readLock:Ljava/util/concurrent/locks/Lock;', 'invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V', 'return-object p1'],
        'type': 'method_replace',
        'search': """.method getEntry(Ljava/lang/Object;)Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;
    .registers 3

    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->readLock:Ljava/util/concurrent/locks/Lock;

    invoke-interface {v0}, Ljava/util/concurrent/locks/Lock;->lock()V

    :try_start_0
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {v0, p1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->readLock:Ljava/util/concurrent/locks/Lock;

    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    return-object p1

    :catchall_0
    move-exception p1

    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->readLock:Ljava/util/concurrent/locks/Lock;

    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    throw p1
.end method""",
        'replacement': """.method getEntry(Ljava/lang/Object;)Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return-object p1

    :catchall_0
    move-exception p1

    goto :goto_5

    nop

    :goto_1
    throw p1

    :goto_2
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->readLock:Ljava/util/concurrent/locks/Lock;

    goto :goto_7

    nop

    :goto_3
    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    goto :goto_1

    nop

    :goto_4
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->readLock:Ljava/util/concurrent/locks/Lock;

    goto :goto_6

    nop

    :goto_5
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->readLock:Ljava/util/concurrent/locks/Lock;

    goto :goto_3

    nop

    :goto_6
    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    goto :goto_0

    nop

    :goto_7
    invoke-interface {v0}, Ljava/util/concurrent/locks/Lock;->lock()V

    :try_start_0
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {v0, p1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p1

    check-cast p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'net_jodah_expiringmap_ExpiringMap__notifyListeners',
        'method': '.method notifyListeners(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V',
        'method_name': 'notifyListeners',
        'method_anchors': ['iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->asyncExpirationListeners:Ljava/util/List;', 'if-eqz v0, :cond_0', 'invoke-interface {v0}, Ljava/util/List;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-eqz v1, :cond_0', 'invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;', 'check-cast v1, Lnet/jodah/expiringmap/ExpirationListener;', 'sget-object v2, Lnet/jodah/expiringmap/ExpiringMap;->LISTENER_SERVICE:Ljava/util/concurrent/ThreadPoolExecutor;'],
        'type': 'method_replace',
        'search': """.method notifyListeners(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V
    .registers 6

    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->asyncExpirationListeners:Ljava/util/List;

    if-eqz v0, :cond_0

    invoke-interface {v0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_0
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lnet/jodah/expiringmap/ExpirationListener;

    sget-object v2, Lnet/jodah/expiringmap/ExpiringMap;->LISTENER_SERVICE:Ljava/util/concurrent/ThreadPoolExecutor;

    new-instance v3, Lnet/jodah/expiringmap/ExpiringMap$4;

    invoke-direct {v3, p0, v1, p1}, Lnet/jodah/expiringmap/ExpiringMap$4;-><init>(Lnet/jodah/expiringmap/ExpiringMap;Lnet/jodah/expiringmap/ExpirationListener;Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V

    invoke-virtual {v2, v3}, Ljava/util/concurrent/ThreadPoolExecutor;->execute(Ljava/lang/Runnable;)V

    goto :goto_0

    :cond_0
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->expirationListeners:Ljava/util/List;

    if-eqz p0, :cond_1

    invoke-interface {p0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :catch_0
    :goto_1
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lnet/jodah/expiringmap/ExpirationListener;

    :try_start_0
    iget-object v1, p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->key:Ljava/lang/Object;

    invoke-virtual {p1}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->getValue()Ljava/lang/Object;

    move-result-object v2

    invoke-interface {v0, v1, v2}, Lnet/jodah/expiringmap/ExpirationListener;->expired(Ljava/lang/Object;Ljava/lang/Object;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_1

    :cond_1
    return-void
.end method""",
        'replacement': """.method notifyListeners(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V
    .registers 6

    goto :goto_18

    nop

    :goto_0
    goto :goto_c

    :goto_1
    goto :goto_2

    nop

    :goto_2
    return-void

    :goto_3
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_7

    nop

    :goto_4
    sget-object v2, Lnet/jodah/expiringmap/ExpiringMap;->LISTENER_SERVICE:Ljava/util/concurrent/ThreadPoolExecutor;

    goto :goto_d

    nop

    :goto_5
    goto :goto_14

    :goto_6
    goto :goto_16

    nop

    :goto_7
    if-nez v1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_11

    nop

    :goto_8
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v0

    goto :goto_a

    nop

    :goto_9
    if-nez p0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_b

    nop

    :goto_a
    if-nez v0, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_e

    nop

    :goto_b
    invoke-interface {p0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object p0

    :catch_0
    :goto_c
    goto :goto_8

    nop

    :goto_d
    new-instance v3, Lnet/jodah/expiringmap/ExpiringMap$4;

    goto :goto_f

    nop

    :goto_e
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v0

    goto :goto_15

    nop

    :goto_f
    invoke-direct {v3, p0, v1, p1}, Lnet/jodah/expiringmap/ExpiringMap$4;-><init>(Lnet/jodah/expiringmap/ExpiringMap;Lnet/jodah/expiringmap/ExpirationListener;Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V

    goto :goto_10

    nop

    :goto_10
    invoke-virtual {v2, v3}, Ljava/util/concurrent/ThreadPoolExecutor;->execute(Ljava/lang/Runnable;)V

    goto :goto_5

    nop

    :goto_11
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    goto :goto_12

    nop

    :goto_12
    check-cast v1, Lnet/jodah/expiringmap/ExpirationListener;

    goto :goto_4

    nop

    :goto_13
    invoke-interface {v0}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_14
    goto :goto_3

    nop

    :goto_15
    check-cast v0, Lnet/jodah/expiringmap/ExpirationListener;

    :try_start_0
    iget-object v1, p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->key:Ljava/lang/Object;

    invoke-virtual {p1}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->getValue()Ljava/lang/Object;

    move-result-object v2

    invoke-interface {v0, v1, v2}, Lnet/jodah/expiringmap/ExpirationListener;->expired(Ljava/lang/Object;Ljava/lang/Object;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    nop

    :goto_16
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->expirationListeners:Ljava/util/List;

    goto :goto_9

    nop

    :goto_17
    if-nez v0, :cond_3

    goto :goto_6

    :cond_3
    goto :goto_13

    nop

    :goto_18
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->asyncExpirationListeners:Ljava/util/List;

    goto :goto_17

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'net_jodah_expiringmap_ExpiringMap__putInternal',
        'method': '.method putInternal(Ljava/lang/Object;Ljava/lang/Object;Lnet/jodah/expiringmap/ExpirationPolicy;J)Ljava/lang/Object;',
        'method_name': 'putInternal',
        'method_anchors': ['iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;', 'invoke-interface {v0}, Ljava/util/concurrent/locks/Lock;->lock()V', 'iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;', 'invoke-interface {v0, p1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;', 'check-cast v0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;', 'if-nez v0, :cond_5', 'new-instance v0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;', 'iget-boolean v1, p0, Lnet/jodah/expiringmap/ExpiringMap;->variableExpiration:Z'],
        'type': 'method_replace',
        'search': """.method putInternal(Ljava/lang/Object;Ljava/lang/Object;Lnet/jodah/expiringmap/ExpirationPolicy;J)Ljava/lang/Object;
    .registers 8

    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    invoke-interface {v0}, Ljava/util/concurrent/locks/Lock;->lock()V

    :try_start_0
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {v0, p1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;

    if-nez v0, :cond_5

    new-instance v0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;

    iget-boolean v1, p0, Lnet/jodah/expiringmap/ExpiringMap;->variableExpiration:Z

    if-eqz v1, :cond_0

    new-instance v1, Ljava/util/concurrent/atomic/AtomicReference;

    invoke-direct {v1, p3}, Ljava/util/concurrent/atomic/AtomicReference;-><init>(Ljava/lang/Object;)V

    goto :goto_0

    :catchall_0
    move-exception p1

    goto :goto_3

    :cond_0
    iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap;->expirationPolicy:Ljava/util/concurrent/atomic/AtomicReference;

    :goto_0
    iget-boolean p3, p0, Lnet/jodah/expiringmap/ExpiringMap;->variableExpiration:Z

    if-eqz p3, :cond_1

    new-instance p3, Ljava/util/concurrent/atomic/AtomicLong;

    invoke-direct {p3, p4, p5}, Ljava/util/concurrent/atomic/AtomicLong;-><init>(J)V

    goto :goto_1

    :cond_1
    iget-object p3, p0, Lnet/jodah/expiringmap/ExpiringMap;->expirationNanos:Ljava/util/concurrent/atomic/AtomicLong;

    :goto_1
    invoke-direct {v0, p1, p2, v1, p3}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;-><init>(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/concurrent/atomic/AtomicReference;Ljava/util/concurrent/atomic/AtomicLong;)V

    iget-object p2, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p2}, Ljava/util/Map;->size()I

    move-result p2

    iget p3, p0, Lnet/jodah/expiringmap/ExpiringMap;->maxSize:I

    if-lt p2, p3, :cond_2

    iget-object p2, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p2}, Lnet/jodah/expiringmap/ExpiringMap$EntryMap;->first()Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;

    move-result-object p2

    iget-object p3, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    iget-object p4, p2, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->key:Ljava/lang/Object;

    invoke-interface {p3, p4}, Ljava/util/Map;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    invoke-virtual {p0, p2}, Lnet/jodah/expiringmap/ExpiringMap;->notifyListeners(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V

    :cond_2
    iget-object p2, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p2, p1, v0}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p1}, Ljava/util/Map;->size()I

    move-result p1

    const/4 p2, 0x1

    if-eq p1, p2, :cond_3

    iget-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p1}, Lnet/jodah/expiringmap/ExpiringMap$EntryMap;->first()Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;

    move-result-object p1

    invoke-virtual {p1, v0}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_4

    :cond_3
    invoke-virtual {p0, v0}, Lnet/jodah/expiringmap/ExpiringMap;->scheduleEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V

    :cond_4
    const/4 p1, 0x0

    goto :goto_2

    :cond_5
    invoke-virtual {v0}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->getValue()Ljava/lang/Object;

    move-result-object p1

    sget-object p4, Lnet/jodah/expiringmap/ExpirationPolicy;->ACCESSED:Lnet/jodah/expiringmap/ExpirationPolicy;

    invoke-virtual {p4, p3}, Ljava/lang/Enum;->equals(Ljava/lang/Object;)Z

    move-result p3

    if-nez p3, :cond_8

    if-nez p1, :cond_6

    if-eqz p2, :cond_7

    :cond_6
    if-eqz p1, :cond_8

    invoke-virtual {p1, p2}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p3
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    if-eqz p3, :cond_8

    :cond_7
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    return-object p2

    :cond_8
    :try_start_1
    invoke-virtual {v0, p2}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->setValue(Ljava/lang/Object;)V

    const/4 p2, 0x0

    invoke-virtual {p0, v0, p2}, Lnet/jodah/expiringmap/ExpiringMap;->resetEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;Z)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :goto_2
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    return-object p1

    :goto_3
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    throw p1
.end method""",
        'replacement': """.method putInternal(Ljava/lang/Object;Ljava/lang/Object;Lnet/jodah/expiringmap/ExpirationPolicy;J)Ljava/lang/Object;
    .registers 8

    goto :goto_b

    nop

    :goto_0
    invoke-interface {v0}, Ljava/util/concurrent/locks/Lock;->lock()V

    :try_start_0
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {v0, p1}, Ljava/util/Map;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;

    if-nez v0, :cond_5

    new-instance v0, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;

    iget-boolean v1, p0, Lnet/jodah/expiringmap/ExpiringMap;->variableExpiration:Z

    if-eqz v1, :cond_0

    new-instance v1, Ljava/util/concurrent/atomic/AtomicReference;

    invoke-direct {v1, p3}, Ljava/util/concurrent/atomic/AtomicReference;-><init>(Ljava/lang/Object;)V

    goto :goto_1

    :catchall_0
    move-exception p1

    goto :goto_5

    :cond_0
    iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap;->expirationPolicy:Ljava/util/concurrent/atomic/AtomicReference;

    :goto_1
    iget-boolean p3, p0, Lnet/jodah/expiringmap/ExpiringMap;->variableExpiration:Z

    if-eqz p3, :cond_1

    new-instance p3, Ljava/util/concurrent/atomic/AtomicLong;

    invoke-direct {p3, p4, p5}, Ljava/util/concurrent/atomic/AtomicLong;-><init>(J)V

    goto :goto_2

    :cond_1
    iget-object p3, p0, Lnet/jodah/expiringmap/ExpiringMap;->expirationNanos:Ljava/util/concurrent/atomic/AtomicLong;

    :goto_2
    invoke-direct {v0, p1, p2, v1, p3}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;-><init>(Ljava/lang/Object;Ljava/lang/Object;Ljava/util/concurrent/atomic/AtomicReference;Ljava/util/concurrent/atomic/AtomicLong;)V

    iget-object p2, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p2}, Ljava/util/Map;->size()I

    move-result p2

    iget p3, p0, Lnet/jodah/expiringmap/ExpiringMap;->maxSize:I

    if-lt p2, p3, :cond_2

    iget-object p2, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p2}, Lnet/jodah/expiringmap/ExpiringMap$EntryMap;->first()Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;

    move-result-object p2

    iget-object p3, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    iget-object p4, p2, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->key:Ljava/lang/Object;

    invoke-interface {p3, p4}, Ljava/util/Map;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    invoke-virtual {p0, p2}, Lnet/jodah/expiringmap/ExpiringMap;->notifyListeners(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V

    :cond_2
    iget-object p2, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p2, p1, v0}, Ljava/util/Map;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    iget-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p1}, Ljava/util/Map;->size()I

    move-result p1

    const/4 p2, 0x1

    if-eq p1, p2, :cond_3

    iget-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p1}, Lnet/jodah/expiringmap/ExpiringMap$EntryMap;->first()Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;

    move-result-object p1

    invoke-virtual {p1, v0}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_4

    :cond_3
    invoke-virtual {p0, v0}, Lnet/jodah/expiringmap/ExpiringMap;->scheduleEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V

    :cond_4
    const/4 p1, 0x0

    goto :goto_e

    :cond_5
    invoke-virtual {v0}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->getValue()Ljava/lang/Object;

    move-result-object p1

    sget-object p4, Lnet/jodah/expiringmap/ExpirationPolicy;->ACCESSED:Lnet/jodah/expiringmap/ExpirationPolicy;

    invoke-virtual {p4, p3}, Ljava/lang/Enum;->equals(Ljava/lang/Object;)Z

    move-result p3

    if-nez p3, :cond_7

    if-nez p1, :cond_6

    if-eqz p2, :cond_8

    :cond_6
    if-eqz p1, :cond_7

    invoke-virtual {p1, p2}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p3
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_f

    nop

    :goto_3
    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    goto :goto_4

    nop

    :goto_4
    return-object p1

    :goto_5
    goto :goto_7

    nop

    :goto_6
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    goto :goto_3

    nop

    :goto_7
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    goto :goto_a

    nop

    :goto_8
    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    goto :goto_c

    nop

    :goto_9
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    goto :goto_8

    nop

    :goto_a
    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    goto :goto_10

    nop

    :goto_b
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    goto :goto_0

    nop

    :goto_c
    return-object p2

    :cond_7
    :goto_d
    :try_start_1
    invoke-virtual {v0, p2}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->setValue(Ljava/lang/Object;)V

    const/4 p2, 0x0

    invoke-virtual {p0, v0, p2}, Lnet/jodah/expiringmap/ExpiringMap;->resetEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;Z)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :goto_e
    goto :goto_6

    nop

    :goto_f
    if-nez p3, :cond_8

    goto :goto_d

    :cond_8
    goto :goto_9

    nop

    :goto_10
    throw p1
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'net_jodah_expiringmap_ExpiringMap__resetEntry',
        'method': '.method resetEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;Z)V',
        'method_name': 'resetEntry',
        'method_anchors': ['iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;', 'invoke-interface {v0}, Ljava/util/concurrent/locks/Lock;->lock()V', 'invoke-virtual {p1}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->cancel()Z', 'iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;', 'invoke-interface {v1, p1}, Lnet/jodah/expiringmap/ExpiringMap$EntryMap;->reorder(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V', 'if-nez v0, :cond_0', 'if-eqz p2, :cond_1', 'iget-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;'],
        'type': 'method_replace',
        'search': """.method resetEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;Z)V
    .registers 5

    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    invoke-interface {v0}, Ljava/util/concurrent/locks/Lock;->lock()V

    :try_start_0
    invoke-virtual {p1}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->cancel()Z

    move-result v0

    iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {v1, p1}, Lnet/jodah/expiringmap/ExpiringMap$EntryMap;->reorder(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V

    if-nez v0, :cond_0

    if-eqz p2, :cond_1

    :cond_0
    iget-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p1}, Lnet/jodah/expiringmap/ExpiringMap$EntryMap;->first()Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;

    move-result-object p1

    invoke-virtual {p0, p1}, Lnet/jodah/expiringmap/ExpiringMap;->scheduleEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :cond_1
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    return-void

    :catchall_0
    move-exception p1

    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    throw p1
.end method""",
        'replacement': """.method resetEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;Z)V
    .registers 5

    goto :goto_3

    nop

    :goto_0
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    goto :goto_2

    nop

    :goto_1
    throw p1

    :goto_2
    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    goto :goto_1

    nop

    :goto_3
    iget-object v0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    goto :goto_6

    nop

    :goto_4
    invoke-interface {p0}, Ljava/util/concurrent/locks/Lock;->unlock()V

    goto :goto_7

    nop

    :goto_5
    iget-object p0, p0, Lnet/jodah/expiringmap/ExpiringMap;->writeLock:Ljava/util/concurrent/locks/Lock;

    goto :goto_4

    nop

    :goto_6
    invoke-interface {v0}, Ljava/util/concurrent/locks/Lock;->lock()V

    :try_start_0
    invoke-virtual {p1}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->cancel()Z

    move-result v0

    iget-object v1, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {v1, p1}, Lnet/jodah/expiringmap/ExpiringMap$EntryMap;->reorder(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V

    if-nez v0, :cond_0

    if-eqz p2, :cond_1

    :cond_0
    iget-object p1, p0, Lnet/jodah/expiringmap/ExpiringMap;->entries:Lnet/jodah/expiringmap/ExpiringMap$EntryMap;

    invoke-interface {p1}, Lnet/jodah/expiringmap/ExpiringMap$EntryMap;->first()Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;

    move-result-object p1

    invoke-virtual {p0, p1}, Lnet/jodah/expiringmap/ExpiringMap;->scheduleEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :cond_1
    goto :goto_5

    nop

    :goto_7
    return-void

    :catchall_0
    move-exception p1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'net_jodah_expiringmap_ExpiringMap__scheduleEntry',
        'method': '.method scheduleEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V',
        'method_name': 'scheduleEntry',
        'method_anchors': ['if-eqz p1, :cond_2', 'iget-boolean v0, p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z', 'if-eqz v0, :cond_0', 'iget-boolean v0, p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z', 'if-eqz v0, :cond_1', 'return-void', 'new-instance v0, Ljava/lang/ref/WeakReference;', 'invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V'],
        'type': 'method_replace',
        'search': """.method scheduleEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V
    .registers 8

    if-eqz p1, :cond_2

    iget-boolean v0, p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z

    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    monitor-enter p1

    :try_start_0
    iget-boolean v0, p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z

    if-eqz v0, :cond_1

    monitor-exit p1

    return-void

    :catchall_0
    move-exception p0

    goto :goto_0

    :cond_1
    new-instance v0, Ljava/lang/ref/WeakReference;

    invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    new-instance v1, Lnet/jodah/expiringmap/ExpiringMap$5;

    invoke-direct {v1, p0, v0}, Lnet/jodah/expiringmap/ExpiringMap$5;-><init>(Lnet/jodah/expiringmap/ExpiringMap;Ljava/lang/ref/WeakReference;)V

    sget-object p0, Lnet/jodah/expiringmap/ExpiringMap;->EXPIRER:Ljava/util/concurrent/ScheduledExecutorService;

    iget-object v0, p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->expectedExpiration:Ljava/util/concurrent/atomic/AtomicLong;

    invoke-virtual {v0}, Ljava/util/concurrent/atomic/AtomicLong;->get()J

    move-result-wide v2

    invoke-static {}, Ljava/lang/System;->nanoTime()J

    move-result-wide v4

    sub-long/2addr v2, v4

    sget-object v0, Ljava/util/concurrent/TimeUnit;->NANOSECONDS:Ljava/util/concurrent/TimeUnit;

    invoke-interface {p0, v1, v2, v3, v0}, Ljava/util/concurrent/ScheduledExecutorService;->schedule(Ljava/lang/Runnable;JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;

    move-result-object p0

    invoke-virtual {p1, p0}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->schedule(Ljava/util/concurrent/Future;)V

    monitor-exit p1

    return-void

    :goto_0
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw p0

    :cond_2
    :goto_1
    return-void
.end method""",
        'replacement': """.method scheduleEntry(Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;)V
    .registers 8

    goto :goto_9

    nop

    :goto_0
    iget-boolean v0, p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z

    goto :goto_8

    nop

    :goto_1
    monitor-enter p1

    :try_start_0
    iget-boolean v0, p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->scheduled:Z

    if-eqz v0, :cond_0

    monitor-exit p1

    return-void

    :catchall_0
    move-exception p0

    goto :goto_2

    :cond_0
    new-instance v0, Ljava/lang/ref/WeakReference;

    invoke-direct {v0, p1}, Ljava/lang/ref/WeakReference;-><init>(Ljava/lang/Object;)V

    new-instance v1, Lnet/jodah/expiringmap/ExpiringMap$5;

    invoke-direct {v1, p0, v0}, Lnet/jodah/expiringmap/ExpiringMap$5;-><init>(Lnet/jodah/expiringmap/ExpiringMap;Ljava/lang/ref/WeakReference;)V

    sget-object p0, Lnet/jodah/expiringmap/ExpiringMap;->EXPIRER:Ljava/util/concurrent/ScheduledExecutorService;

    iget-object v0, p1, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->expectedExpiration:Ljava/util/concurrent/atomic/AtomicLong;

    invoke-virtual {v0}, Ljava/util/concurrent/atomic/AtomicLong;->get()J

    move-result-wide v2

    invoke-static {}, Ljava/lang/System;->nanoTime()J

    move-result-wide v4

    sub-long/2addr v2, v4

    sget-object v0, Ljava/util/concurrent/TimeUnit;->NANOSECONDS:Ljava/util/concurrent/TimeUnit;

    invoke-interface {p0, v1, v2, v3, v0}, Ljava/util/concurrent/ScheduledExecutorService;->schedule(Ljava/lang/Runnable;JLjava/util/concurrent/TimeUnit;)Ljava/util/concurrent/ScheduledFuture;

    move-result-object p0

    invoke-virtual {p1, p0}, Lnet/jodah/expiringmap/ExpiringMap$ExpiringEntry;->schedule(Ljava/util/concurrent/Future;)V

    monitor-exit p1

    return-void

    :goto_2
    monitor-exit p1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_6

    nop

    :goto_3
    return-void

    :goto_4
    goto :goto_7

    :goto_5
    goto :goto_1

    nop

    :goto_6
    throw p0

    :goto_7
    goto :goto_3

    nop

    :goto_8
    if-nez v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_4

    nop

    :goto_9
    if-nez p1, :cond_2

    goto :goto_7

    :cond_2
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
