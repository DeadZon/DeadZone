TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/AIButtonFragment.smali'
CLASS_FALLBACK_NAMES = ['AIButtonFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseFragment;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_AIButtonFragment__getName',
        'method': '.method protected getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['const-string p0, "AIButtonFragment"', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getName()Ljava/lang/String;
    .registers 1

    const-string p0, "AIButtonFragment"

    return-object p0
.end method""",
        'replacement': """.method protected getName()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const-string p0, "AIButtonFragment"

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
