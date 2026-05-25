TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'kotlin/coroutines/jvm/internal/BaseContinuationImpl.smali'
CLASS_FALLBACK_NAMES = ['BaseContinuationImpl.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lkotlin/coroutines/Continuation;', '.implements Lkotlin/coroutines/jvm/internal/CoroutineStackFrame;', '.implements Ljava/io/Serializable;']

PATCHES = [
    {
        'id': 'kotlin_coroutines_jvm_internal_BaseContinuationImpl__releaseIntercepted',
        'method': '.method protected releaseIntercepted()V',
        'method_name': 'releaseIntercepted',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected releaseIntercepted()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected releaseIntercepted()V
    .registers 1

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
