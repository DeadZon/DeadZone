TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/ServiceStatementFragment.smali'
CLASS_FALLBACK_NAMES = ['ServiceStatementFragment.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/fragment/BaseListFragment;', '.field private static final DEVICE_PROVISIONING_SERVICE_STATEMENT_AGREED:Ljava/lang/String; = "device_provisioning_service_agreed"', '.field private static final SERVICE_STATEMENT_COMPLETE_BROADCAST:Ljava/lang/String; = "android.provision.action.SERVICE_STATEMENT_COMPLETE"', '.field private static final TAG:Ljava/lang/String; = "ServiceStatementFragment"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_ServiceStatementFragment__getName',
        'method': '.method protected getName()Ljava/lang/String;',
        'method_name': 'getName',
        'method_anchors': ['const-string p0, "ServiceStatementFragment"', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getName()Ljava/lang/String;
    .registers 1

    const-string p0, "ServiceStatementFragment"

    return-object p0
.end method""",
        'replacement': """.method protected getName()Ljava/lang/String;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const-string p0, "ServiceStatementFragment"

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
