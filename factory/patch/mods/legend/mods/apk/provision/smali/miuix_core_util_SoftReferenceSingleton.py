TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/core/util/SoftReferenceSingleton.smali'
CLASS_FALLBACK_NAMES = ['SoftReferenceSingleton.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_core_util_SoftReferenceSingleton__createInstance',
        'method': '.method protected createInstance()Ljava/lang/Object;',
        'method_name': 'createInstance',
        'method_anchors': ['return-object p0'],
        'type': 'method_replace',
        'search': """.method protected createInstance()Ljava/lang/Object;
    .registers 1

    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected createInstance()Ljava/lang/Object;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_util_SoftReferenceSingleton__createInstance',
        'method': '.method protected createInstance(Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'createInstance',
        'method_anchors': ['return-object p0'],
        'type': 'method_replace',
        'search': """.method protected createInstance(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected createInstance(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    const/4 p0, 0x0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_util_SoftReferenceSingleton__updateInstance',
        'method': '.method protected updateInstance(Ljava/lang/Object;)V',
        'method_name': 'updateInstance',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected updateInstance(Ljava/lang/Object;)V
    .registers 2

    return-void
.end method""",
        'replacement': """.method protected updateInstance(Ljava/lang/Object;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_core_util_SoftReferenceSingleton__updateInstance',
        'method': '.method protected updateInstance(Ljava/lang/Object;Ljava/lang/Object;)V',
        'method_name': 'updateInstance',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected updateInstance(Ljava/lang/Object;Ljava/lang/Object;)V
    .registers 3

    return-void
.end method""",
        'replacement': """.method protected updateInstance(Ljava/lang/Object;Ljava/lang/Object;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
