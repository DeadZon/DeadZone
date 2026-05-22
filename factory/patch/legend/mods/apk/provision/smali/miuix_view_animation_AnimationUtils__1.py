TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/view/animation/AnimationUtils$1.smali'
CLASS_FALLBACK_NAMES = ['AnimationUtils$1.smali']
CLASS_ANCHORS = ['.super Ljava/lang/ThreadLocal;']

PATCHES = [
    {
        'id': 'miuix_view_animation_AnimationUtils__1__initialValue',
        'method': '.method protected bridge synthetic initialValue()Ljava/lang/Object;',
        'method_name': 'initialValue',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/view/animation/AnimationUtils$1;->initialValue()Lmiuix/view/animation/AnimationUtils$AnimationNanoState;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic initialValue()Ljava/lang/Object;
    .registers 1

    invoke-virtual {p0}, Lmiuix/view/animation/AnimationUtils$1;->initialValue()Lmiuix/view/animation/AnimationUtils$AnimationNanoState;

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
    invoke-virtual {p0}, Lmiuix/view/animation/AnimationUtils$1;->initialValue()Lmiuix/view/animation/AnimationUtils$AnimationNanoState;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_view_animation_AnimationUtils__1__initialValue',
        'method': '.method protected initialValue()Lmiuix/view/animation/AnimationUtils$AnimationNanoState;',
        'method_name': 'initialValue',
        'method_anchors': ['new-instance p0, Lmiuix/view/animation/AnimationUtils$AnimationNanoState;', 'invoke-direct {p0, v0}, Lmiuix/view/animation/AnimationUtils$AnimationNanoState;-><init>(Lmiuix/view/animation/AnimationUtils$1;)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected initialValue()Lmiuix/view/animation/AnimationUtils$AnimationNanoState;
    .registers 2

    new-instance p0, Lmiuix/view/animation/AnimationUtils$AnimationNanoState;

    const/4 v0, 0x0

    invoke-direct {p0, v0}, Lmiuix/view/animation/AnimationUtils$AnimationNanoState;-><init>(Lmiuix/view/animation/AnimationUtils$1;)V

    return-object p0
.end method""",
        'replacement': """.method protected initialValue()Lmiuix/view/animation/AnimationUtils$AnimationNanoState;
    .registers 2

    goto :goto_3

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-direct {p0, v0}, Lmiuix/view/animation/AnimationUtils$AnimationNanoState;-><init>(Lmiuix/view/animation/AnimationUtils$1;)V

    goto :goto_0

    nop

    :goto_2
    const/4 v0, 0x0

    goto :goto_1

    nop

    :goto_3
    new-instance p0, Lmiuix/view/animation/AnimationUtils$AnimationNanoState;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
