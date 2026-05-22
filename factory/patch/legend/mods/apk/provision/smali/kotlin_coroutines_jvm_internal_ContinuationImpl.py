TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'kotlin/coroutines/jvm/internal/ContinuationImpl.smali'
CLASS_FALLBACK_NAMES = ['ContinuationImpl.smali']
CLASS_ANCHORS = ['.super Lkotlin/coroutines/jvm/internal/BaseContinuationImpl;']

PATCHES = [
    {
        'id': 'kotlin_coroutines_jvm_internal_ContinuationImpl__releaseIntercepted',
        'method': '.method protected releaseIntercepted()V',
        'method_name': 'releaseIntercepted',
        'method_anchors': ['iget-object v0, p0, Lkotlin/coroutines/jvm/internal/ContinuationImpl;->intercepted:Lkotlin/coroutines/Continuation;', 'if-eqz v0, :cond_1', 'if-ne v0, p0, :cond_0', 'invoke-virtual {p0}, Lkotlin/coroutines/jvm/internal/ContinuationImpl;->getContext()Lkotlin/coroutines/CoroutineContext;', 'sget-object v0, Lkotlin/coroutines/ContinuationInterceptor;->Key:Lkotlin/coroutines/ContinuationInterceptor$Key;', 'invoke-interface {p0, v0}, Lkotlin/coroutines/CoroutineContext;->get(Lkotlin/coroutines/CoroutineContext$Key;)Lkotlin/coroutines/CoroutineContext$Element;', 'invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-static {p0}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V'],
        'type': 'method_replace',
        'search': """.method protected releaseIntercepted()V
    .registers 2

    iget-object v0, p0, Lkotlin/coroutines/jvm/internal/ContinuationImpl;->intercepted:Lkotlin/coroutines/Continuation;

    if-eqz v0, :cond_1

    if-ne v0, p0, :cond_0

    goto :goto_0

    :cond_0
    invoke-virtual {p0}, Lkotlin/coroutines/jvm/internal/ContinuationImpl;->getContext()Lkotlin/coroutines/CoroutineContext;

    move-result-object p0

    sget-object v0, Lkotlin/coroutines/ContinuationInterceptor;->Key:Lkotlin/coroutines/ContinuationInterceptor$Key;

    invoke-interface {p0, v0}, Lkotlin/coroutines/CoroutineContext;->get(Lkotlin/coroutines/CoroutineContext$Key;)Lkotlin/coroutines/CoroutineContext$Element;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    invoke-static {p0}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    const/4 p0, 0x0

    throw p0

    :cond_1
    :goto_0
    sget-object v0, Lkotlin/coroutines/jvm/internal/CompletedContinuation;->INSTANCE:Lkotlin/coroutines/jvm/internal/CompletedContinuation;

    iput-object v0, p0, Lkotlin/coroutines/jvm/internal/ContinuationImpl;->intercepted:Lkotlin/coroutines/Continuation;

    return-void
.end method""",
        'replacement': """.method protected releaseIntercepted()V
    .registers 2

    goto :goto_8

    nop

    :goto_0
    iput-object v0, p0, Lkotlin/coroutines/jvm/internal/ContinuationImpl;->intercepted:Lkotlin/coroutines/Continuation;

    goto :goto_c

    nop

    :goto_1
    invoke-interface {p0, v0}, Lkotlin/coroutines/CoroutineContext;->get(Lkotlin/coroutines/CoroutineContext$Key;)Lkotlin/coroutines/CoroutineContext$Element;

    move-result-object p0

    goto :goto_e

    nop

    :goto_2
    throw p0

    :goto_3
    goto :goto_d

    nop

    :goto_4
    goto :goto_3

    :goto_5
    goto :goto_6

    nop

    :goto_6
    invoke-virtual {p0}, Lkotlin/coroutines/jvm/internal/ContinuationImpl;->getContext()Lkotlin/coroutines/CoroutineContext;

    move-result-object p0

    goto :goto_a

    nop

    :goto_7
    const/4 p0, 0x0

    goto :goto_2

    nop

    :goto_8
    iget-object v0, p0, Lkotlin/coroutines/jvm/internal/ContinuationImpl;->intercepted:Lkotlin/coroutines/Continuation;

    goto :goto_b

    nop

    :goto_9
    invoke-static {p0}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    goto :goto_7

    nop

    :goto_a
    sget-object v0, Lkotlin/coroutines/ContinuationInterceptor;->Key:Lkotlin/coroutines/ContinuationInterceptor$Key;

    goto :goto_1

    nop

    :goto_b
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_f

    nop

    :goto_c
    return-void

    :goto_d
    sget-object v0, Lkotlin/coroutines/jvm/internal/CompletedContinuation;->INSTANCE:Lkotlin/coroutines/jvm/internal/CompletedContinuation;

    goto :goto_0

    nop

    :goto_e
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    goto :goto_9

    nop

    :goto_f
    if-eq v0, p0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
