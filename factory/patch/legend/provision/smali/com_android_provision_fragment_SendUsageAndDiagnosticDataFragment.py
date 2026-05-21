TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/SendUsageAndDiagnosticDataFragment.smali'
CLASS_FALLBACK_NAMES = ['SendUsageAndDiagnosticDataFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseFragment;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_SendUsageAndDiagnosticDataFragment__getName',
        'method': '.method protected getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['const-string p0, "SendUsageAndDiagnosticDataFragment"', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getName()Ljava/lang/String;
    .registers 1

    const-string p0, "SendUsageAndDiagnosticDataFragment"

    return-object p0
.end method""",
        'replacement': """.method protected getName()Ljava/lang/String;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    const-string p0, "SendUsageAndDiagnosticDataFragment"

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
