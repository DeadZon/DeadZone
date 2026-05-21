TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'kotlin/jvm/internal/CallableReference.smali'
CLASS_FALLBACK_NAMES = ['CallableReference.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lkotlin/reflect/KCallable;', '.implements Ljava/io/Serializable;', '.field public static final NO_RECEIVER:Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'kotlin_jvm_internal_CallableReference__getReflected',
        'method': '.method protected getReflected()Lkotlin/reflect/KCallable;',
        'method_name': 'getReflected',
        'method_anchors': ['invoke-virtual {p0}, Lkotlin/jvm/internal/CallableReference;->compute()Lkotlin/reflect/KCallable;', 'if-eq v0, p0, :cond_0', 'return-object v0', 'new-instance p0, Lkotlin/jvm/KotlinReflectionNotSupportedError;', 'invoke-direct {p0}, Lkotlin/jvm/KotlinReflectionNotSupportedError;-><init>()V'],
        'type': 'method_replace',
        'search': """.method protected getReflected()Lkotlin/reflect/KCallable;
    .registers 2

    invoke-virtual {p0}, Lkotlin/jvm/internal/CallableReference;->compute()Lkotlin/reflect/KCallable;

    move-result-object v0

    if-eq v0, p0, :cond_0

    return-object v0

    :cond_0
    new-instance p0, Lkotlin/jvm/KotlinReflectionNotSupportedError;

    invoke-direct {p0}, Lkotlin/jvm/KotlinReflectionNotSupportedError;-><init>()V

    throw p0
.end method""",
        'replacement': """.method protected getReflected()Lkotlin/reflect/KCallable;
    .registers 2

    goto :goto_6

    nop

    :goto_0
    if-ne v0, p0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop

    :goto_1
    throw p0

    :goto_2
    invoke-direct {p0}, Lkotlin/jvm/KotlinReflectionNotSupportedError;-><init>()V

    goto :goto_1

    nop

    :goto_3
    return-object v0

    :goto_4
    goto :goto_5

    nop

    :goto_5
    new-instance p0, Lkotlin/jvm/KotlinReflectionNotSupportedError;

    goto :goto_2

    nop

    :goto_6
    invoke-virtual {p0}, Lkotlin/jvm/internal/CallableReference;->compute()Lkotlin/reflect/KCallable;

    move-result-object v0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
