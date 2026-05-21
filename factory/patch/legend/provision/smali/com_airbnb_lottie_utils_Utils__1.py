TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/utils/Utils$1.smali'
CLASS_FALLBACK_NAMES = ['Utils$1.smali']
CLASS_ANCHORS = ['.super Ljava/lang/ThreadLocal;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_utils_Utils__1__initialValue',
        'method': '.method protected bridge synthetic initialValue()Ljava/lang/Object;',
        'method_name': 'initialValue',
        'method_anchors': ['invoke-virtual {p0}, Lcom/airbnb/lottie/utils/Utils$1;->initialValue()Landroid/graphics/PathMeasure;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic initialValue()Ljava/lang/Object;
    .registers 1

    invoke-virtual {p0}, Lcom/airbnb/lottie/utils/Utils$1;->initialValue()Landroid/graphics/PathMeasure;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic initialValue()Ljava/lang/Object;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0}, Lcom/airbnb/lottie/utils/Utils$1;->initialValue()Landroid/graphics/PathMeasure;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_airbnb_lottie_utils_Utils__1__initialValue',
        'method': '.method protected initialValue()Landroid/graphics/PathMeasure;',
        'method_name': 'initialValue',
        'method_anchors': ['new-instance p0, Landroid/graphics/PathMeasure;', 'invoke-direct {p0}, Landroid/graphics/PathMeasure;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected initialValue()Landroid/graphics/PathMeasure;
    .registers 1

    new-instance p0, Landroid/graphics/PathMeasure;

    invoke-direct {p0}, Landroid/graphics/PathMeasure;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected initialValue()Landroid/graphics/PathMeasure;
    .registers 1

    goto :goto_2

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-direct {p0}, Landroid/graphics/PathMeasure;-><init>()V

    goto :goto_0

    nop

    :goto_2
    new-instance p0, Landroid/graphics/PathMeasure;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
