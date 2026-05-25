TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/core/util/Pools$BasePool$1.smali'
CLASS_FALLBACK_NAMES = ['Pools$BasePool$1.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_core_util_Pools__BasePool__1__finalize',
        'method': '.method protected finalize()V',
        'method_name': 'finalize',
        'method_anchors': ['iget-object v0, p0, Lmiuix/core/util/Pools$BasePool$1;->this$0:Lmiuix/core/util/Pools$BasePool;', 'invoke-virtual {v0}, Lmiuix/core/util/Pools$BasePool;->close()V', 'invoke-super {p0}, Ljava/lang/Object;->finalize()V', 'return-void', 'invoke-super {p0}, Ljava/lang/Object;->finalize()V'],
        'type': 'method_replace',
        'search': """.method protected finalize()V
    .registers 2

    :try_start_0
    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool$1;->this$0:Lmiuix/core/util/Pools$BasePool;

    invoke-virtual {v0}, Lmiuix/core/util/Pools$BasePool;->close()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-super {p0}, Ljava/lang/Object;->finalize()V

    return-void

    :catchall_0
    move-exception v0

    invoke-super {p0}, Ljava/lang/Object;->finalize()V

    throw v0
.end method""",
        'replacement': """.method protected finalize()V
    .registers 2

    :try_start_0
    iget-object v0, p0, Lmiuix/core/util/Pools$BasePool$1;->this$0:Lmiuix/core/util/Pools$BasePool;

    invoke-virtual {v0}, Lmiuix/core/util/Pools$BasePool;->close()V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop

    :goto_0
    invoke-super {p0}, Ljava/lang/Object;->finalize()V

    goto :goto_2

    nop

    :goto_1
    invoke-super {p0}, Ljava/lang/Object;->finalize()V

    goto :goto_3

    nop

    :goto_2
    throw v0

    :goto_3
    return-void

    :catchall_0
    move-exception v0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
