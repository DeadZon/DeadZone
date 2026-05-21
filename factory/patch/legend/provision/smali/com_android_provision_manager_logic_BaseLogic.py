TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/manager/logic/BaseLogic.smali'
CLASS_FALLBACK_NAMES = ['BaseLogic.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lcom/android/provision/manager/logic/ILogic;']

PATCHES = [
    {
        'id': 'com_android_provision_manager_logic_BaseLogic__asyncLoad',
        'method': '.method protected asyncLoad()Z',
        'method_name': 'asyncLoad',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected asyncLoad()Z
    .registers 1

    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected asyncLoad()Z
    .registers 1

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
        'id': 'com_android_provision_manager_logic_BaseLogic__idleLoad',
        'method': '.method protected idleLoad()Z',
        'method_name': 'idleLoad',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected idleLoad()Z
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected idleLoad()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/4 p0, 0x0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
