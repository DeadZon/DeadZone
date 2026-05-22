TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/mgl/utils/NativeObject.smali'
CLASS_FALLBACK_NAMES = ['NativeObject.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_mgl_utils_NativeObject__clearNativeObject',
        'method': '.method protected clearNativeObject()V',
        'method_name': 'clearNativeObject',
        'method_anchors': ['iput-wide v0, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected clearNativeObject()V
    .registers 3

    const-wide/16 v0, 0x0

    iput-wide v0, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J

    return-void
.end method""",
        'replacement': """.method protected clearNativeObject()V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    const-wide/16 v0, 0x0

    goto :goto_1

    nop

    :goto_1
    iput-wide v0, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_mgl_utils_NativeObject__destroyInternal',
        'method': '.method protected destroyInternal()V',
        'method_name': 'destroyInternal',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z', 'if-nez v0, :cond_0', 'invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J', 'invoke-virtual {p0, v0, v1}, Lmiuix/mgl/utils/NativeObject;->onDestroyNativeObject(J)V', 'invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->clearNativeObject()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected destroyInternal()V
    .registers 3

    iget-boolean v0, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z

    if-nez v0, :cond_0

    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J

    move-result-wide v0

    invoke-virtual {p0, v0, v1}, Lmiuix/mgl/utils/NativeObject;->onDestroyNativeObject(J)V

    :cond_0
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->clearNativeObject()V

    return-void
.end method""",
        'replacement': """.method protected destroyInternal()V
    .registers 3

    goto :goto_6

    nop

    :goto_0
    invoke-virtual {p0, v0, v1}, Lmiuix/mgl/utils/NativeObject;->onDestroyNativeObject(J)V

    :goto_1
    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->getNativeObject()J

    move-result-wide v0

    goto :goto_0

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_2

    nop

    :goto_4
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->clearNativeObject()V

    goto :goto_5

    nop

    :goto_5
    return-void

    :goto_6
    iget-boolean v0, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_mgl_utils_NativeObject__finalize',
        'method': '.method protected finalize()V',
        'method_name': 'finalize',
        'method_anchors': ['invoke-super {p0}, Ljava/lang/Object;->finalize()V', 'invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->isValid()Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->destroyInternal()V', 'return-void', 'invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->isValid()Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->destroyInternal()V'],
        'type': 'method_replace',
        'search': """.method protected finalize()V
    .registers 2

    :try_start_0
    invoke-super {p0}, Ljava/lang/Object;->finalize()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->isValid()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->destroyInternal()V

    return-void

    :catchall_0
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->isValid()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->destroyInternal()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected finalize()V
    .registers 2

    :try_start_0
    invoke-super {p0}, Ljava/lang/Object;->finalize()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_6

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->destroyInternal()V

    :goto_1
    goto :goto_3

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->isValid()Z

    move-result v0

    goto :goto_8

    nop

    :goto_3
    return-void

    :goto_4
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->destroyInternal()V

    goto :goto_5

    nop

    :goto_5
    return-void

    :catchall_0
    goto :goto_2

    nop

    :goto_6
    invoke-virtual {p0}, Lmiuix/mgl/utils/NativeObject;->isValid()Z

    move-result v0

    goto :goto_7

    nop

    :goto_7
    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_4

    nop

    :goto_8
    if-nez v0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_mgl_utils_NativeObject__initNativeObject',
        'method': '.method protected initNativeObject(J)V',
        'method_name': 'initNativeObject',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J', 'if-nez v0, :cond_0', 'iput-wide p1, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J', 'iput-boolean p1, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z', 'return-void', 'new-instance p0, Ljava/lang/IllegalStateException;', 'const-string p1, "Init a valid NativeObject"', 'invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V'],
        'type': 'method_replace',
        'search': """.method protected initNativeObject(J)V
    .registers 7

    iget-wide v0, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J

    const-wide/16 v2, 0x0

    cmp-long v0, v0, v2

    if-nez v0, :cond_0

    iput-wide p1, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J

    const/4 p1, 0x0

    iput-boolean p1, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z

    return-void

    :cond_0
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string p1, "Init a valid NativeObject"

    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method protected initNativeObject(J)V
    .registers 7

    goto :goto_7

    nop

    :goto_0
    iput-wide p1, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J

    goto :goto_a

    nop

    :goto_1
    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_6

    nop

    :goto_2
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_b

    nop

    :goto_3
    iput-boolean p1, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z

    goto :goto_8

    nop

    :goto_4
    if-eqz v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_0

    nop

    :goto_5
    const-wide/16 v2, 0x0

    goto :goto_c

    nop

    :goto_6
    throw p0

    :goto_7
    iget-wide v0, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J

    goto :goto_5

    nop

    :goto_8
    return-void

    :goto_9
    goto :goto_2

    nop

    :goto_a
    const/4 p1, 0x0

    goto :goto_3

    nop

    :goto_b
    const-string p1, "Init a valid NativeObject"

    goto :goto_1

    nop

    :goto_c
    cmp-long v0, v0, v2

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_mgl_utils_NativeObject__initTempNativeObject',
        'method': '.method protected initTempNativeObject(J)V',
        'method_name': 'initTempNativeObject',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J', 'if-nez v0, :cond_0', 'iput-wide p1, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J', 'iput-boolean p1, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z', 'return-void', 'new-instance p0, Ljava/lang/IllegalStateException;', 'const-string p1, "Init a valid NativeObject"', 'invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V'],
        'type': 'method_replace',
        'search': """.method protected initTempNativeObject(J)V
    .registers 7

    iget-wide v0, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J

    const-wide/16 v2, 0x0

    cmp-long v0, v0, v2

    if-nez v0, :cond_0

    iput-wide p1, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J

    const/4 p1, 0x1

    iput-boolean p1, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z

    return-void

    :cond_0
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string p1, "Init a valid NativeObject"

    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method protected initTempNativeObject(J)V
    .registers 7

    goto :goto_8

    nop

    :goto_0
    const-string p1, "Init a valid NativeObject"

    goto :goto_a

    nop

    :goto_1
    throw p0

    :goto_2
    const-wide/16 v2, 0x0

    goto :goto_5

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_b

    nop

    :goto_4
    new-instance p0, Ljava/lang/IllegalStateException;

    goto :goto_0

    nop

    :goto_5
    cmp-long v0, v0, v2

    goto :goto_3

    nop

    :goto_6
    return-void

    :goto_7
    goto :goto_4

    nop

    :goto_8
    iget-wide v0, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J

    goto :goto_2

    nop

    :goto_9
    iput-boolean p1, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z

    goto :goto_6

    nop

    :goto_a
    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_1

    nop

    :goto_b
    iput-wide p1, p0, Lmiuix/mgl/utils/NativeObject;->mNativeObject:J

    goto :goto_c

    nop

    :goto_c
    const/4 p1, 0x1

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_mgl_utils_NativeObject__setTempRef',
        'method': '.method protected setTempRef()V',
        'method_name': 'setTempRef',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setTempRef()V
    .registers 2

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z

    return-void
.end method""",
        'replacement': """.method protected setTempRef()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    const/4 v0, 0x1

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    iput-boolean v0, p0, Lmiuix/mgl/utils/NativeObject;->mIsTempRef:Z

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
