TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/airbnb/lottie/PerformanceTracker.smali'
CLASS_FALLBACK_NAMES = ['PerformanceTracker.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_airbnb_lottie_PerformanceTracker__setEnabled',
        'method': '.method setEnabled(Z)V',
        'method_name': 'setEnabled',
        'method_anchors': ['iput-boolean p1, p0, Lcom/airbnb/lottie/PerformanceTracker;->enabled:Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method setEnabled(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/airbnb/lottie/PerformanceTracker;->enabled:Z

    return-void
.end method""",
        'replacement': """.method setEnabled(Z)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-boolean p1, p0, Lcom/airbnb/lottie/PerformanceTracker;->enabled:Z

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
