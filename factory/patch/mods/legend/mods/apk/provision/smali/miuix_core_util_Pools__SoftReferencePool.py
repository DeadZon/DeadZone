TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/core/util/Pools$SoftReferencePool.smali'
CLASS_FALLBACK_NAMES = ['Pools$SoftReferencePool.smali']
CLASS_ANCHORS = ['.super Lmiuix/core/util/Pools$BasePool;']

PATCHES = [
    {
        'id': 'miuix_core_util_Pools__SoftReferencePool__createInstanceHolder',
        'method': '.method final createInstanceHolder(Ljava/lang/Class;I)Lmiuix/core/util/Pools$IInstanceHolder;',
        'method_name': 'createInstanceHolder',
        'method_anchors': ['invoke-static {p1, p2}, Lmiuix/core/util/Pools;->onSoftReferencePoolCreate(Ljava/lang/Class;I)Lmiuix/core/util/Pools$SoftReferenceInstanceHolder;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method final createInstanceHolder(Ljava/lang/Class;I)Lmiuix/core/util/Pools$IInstanceHolder;
    .registers 3

    invoke-static {p1, p2}, Lmiuix/core/util/Pools;->onSoftReferencePoolCreate(Ljava/lang/Class;I)Lmiuix/core/util/Pools$SoftReferenceInstanceHolder;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method final createInstanceHolder(Ljava/lang/Class;I)Lmiuix/core/util/Pools$IInstanceHolder;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-static {p1, p2}, Lmiuix/core/util/Pools;->onSoftReferencePoolCreate(Ljava/lang/Class;I)Lmiuix/core/util/Pools$SoftReferenceInstanceHolder;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_util_Pools__SoftReferencePool__destroyInstanceHolder',
        'method': '.method final destroyInstanceHolder(Lmiuix/core/util/Pools$IInstanceHolder;I)V',
        'method_name': 'destroyInstanceHolder',
        'method_anchors': ['check-cast p1, Lmiuix/core/util/Pools$SoftReferenceInstanceHolder;', 'invoke-static {p1, p2}, Lmiuix/core/util/Pools;->onSoftReferencePoolClose(Lmiuix/core/util/Pools$SoftReferenceInstanceHolder;I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method final destroyInstanceHolder(Lmiuix/core/util/Pools$IInstanceHolder;I)V
    .registers 3

    check-cast p1, Lmiuix/core/util/Pools$SoftReferenceInstanceHolder;

    invoke-static {p1, p2}, Lmiuix/core/util/Pools;->onSoftReferencePoolClose(Lmiuix/core/util/Pools$SoftReferenceInstanceHolder;I)V

    return-void
.end method""",
        'replacement': """.method final destroyInstanceHolder(Lmiuix/core/util/Pools$IInstanceHolder;I)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    invoke-static {p1, p2}, Lmiuix/core/util/Pools;->onSoftReferencePoolClose(Lmiuix/core/util/Pools$SoftReferenceInstanceHolder;I)V

    goto :goto_0

    nop

    :goto_2
    check-cast p1, Lmiuix/core/util/Pools$SoftReferenceInstanceHolder;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
