TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/miconnect/MiMoverService$Skeleton.smali'
CLASS_FALLBACK_NAMES = ['MiMoverService$Skeleton.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/miconnect/MiMoverService;']

PATCHES = [
    {
        'id': 'com_android_provision_miconnect_MiMoverService__Skeleton__onSubscribeAPEvent',
        'method': '.method protected onSubscribeAPEvent(Lcom/xiaomi/idm/bean/ClientInfo;Z)Z',
        'method_name': 'onSubscribeAPEvent',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected onSubscribeAPEvent(Lcom/xiaomi/idm/bean/ClientInfo;Z)Z
    .registers 3

    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected onSubscribeAPEvent(Lcom/xiaomi/idm/bean/ClientInfo;Z)Z
    .registers 3

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x1

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_miconnect_MiMoverService__Skeleton__onSubscribeAPEventSuccess',
        'method': '.method protected onSubscribeAPEventSuccess(Lcom/xiaomi/idm/bean/ClientInfo;)V',
        'method_name': 'onSubscribeAPEventSuccess',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected onSubscribeAPEventSuccess(Lcom/xiaomi/idm/bean/ClientInfo;)V
    .registers 2

    return-void
.end method""",
        'replacement': """.method protected onSubscribeAPEventSuccess(Lcom/xiaomi/idm/bean/ClientInfo;)V
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
]
