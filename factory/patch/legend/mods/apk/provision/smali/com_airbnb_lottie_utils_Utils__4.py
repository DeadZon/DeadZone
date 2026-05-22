TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/utils/Utils$4.smali'
CLASS_FALLBACK_NAMES = ['Utils$4.smali']
CLASS_ANCHORS = ['.super Ljava/lang/ThreadLocal;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_utils_Utils__4__initialValue',
        'method': '.method protected bridge synthetic initialValue()Ljava/lang/Object;',
        'method_name': 'initialValue',
        'method_anchors': ['invoke-virtual {p0}, Lcom/airbnb/lottie/utils/Utils$4;->initialValue()[F', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic initialValue()Ljava/lang/Object;
    .registers 1

    invoke-virtual {p0}, Lcom/airbnb/lottie/utils/Utils$4;->initialValue()[F

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic initialValue()Ljava/lang/Object;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/airbnb/lottie/utils/Utils$4;->initialValue()[F

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
        'id': 'com_airbnb_lottie_utils_Utils__4__initialValue',
        'method': '.method protected initialValue()[F',
        'method_name': 'initialValue',
        'method_anchors': ['return-object p0'],
        'type': 'method_replace',
        'search': """.method protected initialValue()[F
    .registers 1

    const/4 p0, 0x4

    new-array p0, p0, [F

    return-object p0
.end method""",
        'replacement': """.method protected initialValue()[F
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x4

    goto :goto_2

    nop

    :goto_1
    return-object p0

    :goto_2
    new-array p0, p0, [F

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
