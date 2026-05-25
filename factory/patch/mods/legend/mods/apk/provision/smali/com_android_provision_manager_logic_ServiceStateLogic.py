TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/manager/logic/ServiceStateLogic.smali'
CLASS_FALLBACK_NAMES = ['ServiceStateLogic.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/manager/logic/BaseLogic;']

PATCHES = [
    {
        'id': 'com_android_provision_manager_logic_ServiceStateLogic__getResultModel',
        'method': '.method bridge synthetic getResultModel()Ljava/lang/Object;',
        'method_name': 'getResultModel',
        'method_anchors': ['invoke-virtual {p0}, Lcom/android/provision/manager/logic/ServiceStateLogic;->getResultModel()Lcom/android/provision/utils/service_state/ServiceStateDataHelper;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method bridge synthetic getResultModel()Ljava/lang/Object;
    .registers 1

    invoke-virtual {p0}, Lcom/android/provision/manager/logic/ServiceStateLogic;->getResultModel()Lcom/android/provision/utils/service_state/ServiceStateDataHelper;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method bridge synthetic getResultModel()Ljava/lang/Object;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/android/provision/manager/logic/ServiceStateLogic;->getResultModel()Lcom/android/provision/utils/service_state/ServiceStateDataHelper;

    move-result-object p0

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
        'id': 'com_android_provision_manager_logic_ServiceStateLogic__getResultModel',
        'method': '.method getResultModel()Lcom/android/provision/utils/service_state/ServiceStateDataHelper;',
        'method_name': 'getResultModel',
        'method_anchors': ['iget-object p0, p0, Lcom/android/provision/manager/logic/ServiceStateLogic;->serviceStateDataHelper:Lcom/android/provision/utils/service_state/ServiceStateDataHelper;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getResultModel()Lcom/android/provision/utils/service_state/ServiceStateDataHelper;
    .registers 1

    iget-object p0, p0, Lcom/android/provision/manager/logic/ServiceStateLogic;->serviceStateDataHelper:Lcom/android/provision/utils/service_state/ServiceStateDataHelper;

    return-object p0
.end method""",
        'replacement': """.method getResultModel()Lcom/android/provision/utils/service_state/ServiceStateDataHelper;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lcom/android/provision/manager/logic/ServiceStateLogic;->serviceStateDataHelper:Lcom/android/provision/utils/service_state/ServiceStateDataHelper;

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
