TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'kotlin/jvm/internal/FunctionReference.smali'
CLASS_FALLBACK_NAMES = ['FunctionReference.smali']
CLASS_ANCHORS = ['.super Lkotlin/jvm/internal/CallableReference;', '.implements Lkotlin/jvm/internal/FunctionBase;', '.implements Lkotlin/reflect/KFunction;']

PATCHES = [
    {
        'id': 'kotlin_jvm_internal_FunctionReference__getReflected',
        'method': '.method protected bridge synthetic getReflected()Lkotlin/reflect/KCallable;',
        'method_name': 'getReflected',
        'method_anchors': ['invoke-virtual {p0}, Lkotlin/jvm/internal/FunctionReference;->getReflected()Lkotlin/reflect/KFunction;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic getReflected()Lkotlin/reflect/KCallable;
    .registers 1

    invoke-virtual {p0}, Lkotlin/jvm/internal/FunctionReference;->getReflected()Lkotlin/reflect/KFunction;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic getReflected()Lkotlin/reflect/KCallable;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0}, Lkotlin/jvm/internal/FunctionReference;->getReflected()Lkotlin/reflect/KFunction;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'kotlin_jvm_internal_FunctionReference__computeReflected',
        'method': '.method protected computeReflected()Lkotlin/reflect/KCallable;',
        'method_name': 'computeReflected',
        'method_anchors': ['invoke-static {p0}, Lkotlin/jvm/internal/Reflection;->function(Lkotlin/jvm/internal/FunctionReference;)Lkotlin/reflect/KFunction;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected computeReflected()Lkotlin/reflect/KCallable;
    .registers 1

    invoke-static {p0}, Lkotlin/jvm/internal/Reflection;->function(Lkotlin/jvm/internal/FunctionReference;)Lkotlin/reflect/KFunction;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected computeReflected()Lkotlin/reflect/KCallable;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-static {p0}, Lkotlin/jvm/internal/Reflection;->function(Lkotlin/jvm/internal/FunctionReference;)Lkotlin/reflect/KFunction;

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
        'id': 'kotlin_jvm_internal_FunctionReference__getReflected',
        'method': '.method protected getReflected()Lkotlin/reflect/KFunction;',
        'method_name': 'getReflected',
        'method_anchors': ['invoke-super {p0}, Lkotlin/jvm/internal/CallableReference;->getReflected()Lkotlin/reflect/KCallable;', 'check-cast p0, Lkotlin/reflect/KFunction;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getReflected()Lkotlin/reflect/KFunction;
    .registers 1

    invoke-super {p0}, Lkotlin/jvm/internal/CallableReference;->getReflected()Lkotlin/reflect/KCallable;

    move-result-object p0

    check-cast p0, Lkotlin/reflect/KFunction;

    return-object p0
.end method""",
        'replacement': """.method protected getReflected()Lkotlin/reflect/KFunction;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Lkotlin/jvm/internal/CallableReference;->getReflected()Lkotlin/reflect/KCallable;

    move-result-object p0

    goto :goto_1

    nop

    :goto_1
    check-cast p0, Lkotlin/reflect/KFunction;

    goto :goto_2

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
