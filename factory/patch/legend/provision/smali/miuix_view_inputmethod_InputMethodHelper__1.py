TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/view/inputmethod/InputMethodHelper$1.smali'
CLASS_FALLBACK_NAMES = ['InputMethodHelper$1.smali']
CLASS_ANCHORS = ['.super Lmiuix/core/util/SoftReferenceSingleton;']

PATCHES = [
    {
        'id': 'miuix_view_inputmethod_InputMethodHelper__1__createInstance',
        'method': '.method protected bridge synthetic createInstance(Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'createInstance',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/view/inputmethod/InputMethodHelper$1;->createInstance(Ljava/lang/Object;)Lmiuix/view/inputmethod/InputMethodHelper;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic createInstance(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    invoke-virtual {p0, p1}, Lmiuix/view/inputmethod/InputMethodHelper$1;->createInstance(Ljava/lang/Object;)Lmiuix/view/inputmethod/InputMethodHelper;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic createInstance(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/view/inputmethod/InputMethodHelper$1;->createInstance(Ljava/lang/Object;)Lmiuix/view/inputmethod/InputMethodHelper;

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
        'id': 'miuix_view_inputmethod_InputMethodHelper__1__createInstance',
        'method': '.method protected createInstance(Ljava/lang/Object;)Lmiuix/view/inputmethod/InputMethodHelper;',
        'method_name': 'createInstance',
        'method_anchors': ['new-instance p0, Lmiuix/view/inputmethod/InputMethodHelper;', 'check-cast p1, Landroid/content/Context;', 'invoke-direct {p0, p1, v0}, Lmiuix/view/inputmethod/InputMethodHelper;-><init>(Landroid/content/Context;Lmiuix/view/inputmethod/InputMethodHelper$1;)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected createInstance(Ljava/lang/Object;)Lmiuix/view/inputmethod/InputMethodHelper;
    .registers 3

    new-instance p0, Lmiuix/view/inputmethod/InputMethodHelper;

    check-cast p1, Landroid/content/Context;

    const/4 v0, 0x0

    invoke-direct {p0, p1, v0}, Lmiuix/view/inputmethod/InputMethodHelper;-><init>(Landroid/content/Context;Lmiuix/view/inputmethod/InputMethodHelper$1;)V

    return-object p0
.end method""",
        'replacement': """.method protected createInstance(Ljava/lang/Object;)Lmiuix/view/inputmethod/InputMethodHelper;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_1
    new-instance p0, Lmiuix/view/inputmethod/InputMethodHelper;

    goto :goto_4

    nop

    :goto_2
    invoke-direct {p0, p1, v0}, Lmiuix/view/inputmethod/InputMethodHelper;-><init>(Landroid/content/Context;Lmiuix/view/inputmethod/InputMethodHelper$1;)V

    goto :goto_3

    nop

    :goto_3
    return-object p0

    :goto_4
    check-cast p1, Landroid/content/Context;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
