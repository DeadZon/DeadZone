TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/AnimTaskStackRunner$1.smali'
CLASS_FALLBACK_NAMES = ['AnimTaskStackRunner$1.smali']
CLASS_ANCHORS = ['.super Ljava/lang/ThreadLocal;']

PATCHES = [
    {
        'id': 'miuix_animation_internal_AnimTaskStackRunner__1__initialValue',
        'method': '.method protected bridge synthetic initialValue()Ljava/lang/Object;',
        'method_name': 'initialValue',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/animation/internal/AnimTaskStackRunner$1;->initialValue()Ljava/util/List;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic initialValue()Ljava/lang/Object;
    .registers 1

    invoke-virtual {p0}, Lmiuix/animation/internal/AnimTaskStackRunner$1;->initialValue()Ljava/util/List;

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
    invoke-virtual {p0}, Lmiuix/animation/internal/AnimTaskStackRunner$1;->initialValue()Ljava/util/List;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimTaskStackRunner__1__initialValue',
        'method': '.method protected initialValue()Ljava/util/List;',
        'method_name': 'initialValue',
        'method_anchors': ['new-instance p0, Ljava/util/ArrayList;', 'invoke-direct {p0}, Ljava/util/ArrayList;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected initialValue()Ljava/util/List;
    .registers 1
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "()",
            "Ljava/util/List<",
            "Lmiuix/animation/listener/UpdateInfo;",
            ">;"
        }
    .end annotation

    new-instance p0, Ljava/util/ArrayList;

    invoke-direct {p0}, Ljava/util/ArrayList;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected initialValue()Ljava/util/List;
    .registers 1
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "()",
            "Ljava/util/List<",
            "Lmiuix/animation/listener/UpdateInfo;",
            ">;"
        }
    .end annotation

    goto :goto_2

    nop

    :goto_0
    invoke-direct {p0}, Ljava/util/ArrayList;-><init>()V

    goto :goto_1

    nop

    :goto_1
    return-object p0

    :goto_2
    new-instance p0, Ljava/util/ArrayList;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
