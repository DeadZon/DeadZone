TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/AndroidEngine$1.smali'
CLASS_FALLBACK_NAMES = ['AndroidEngine$1.smali']
CLASS_ANCHORS = ['.super Ljava/lang/ThreadLocal;']

PATCHES = [
    {
        'id': 'miuix_animation_internal_AndroidEngine__1__initialValue',
        'method': '.method protected bridge synthetic initialValue()Ljava/lang/Object;',
        'method_name': 'initialValue',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/animation/internal/AndroidEngine$1;->initialValue()Lmiuix/animation/internal/AndroidEngine;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic initialValue()Ljava/lang/Object;
    .registers 1

    invoke-virtual {p0}, Lmiuix/animation/internal/AndroidEngine$1;->initialValue()Lmiuix/animation/internal/AndroidEngine;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic initialValue()Ljava/lang/Object;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/animation/internal/AndroidEngine$1;->initialValue()Lmiuix/animation/internal/AndroidEngine;

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
        'id': 'miuix_animation_internal_AndroidEngine__1__initialValue',
        'method': '.method protected initialValue()Lmiuix/animation/internal/AndroidEngine;',
        'method_name': 'initialValue',
        'method_anchors': ['invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;', 'if-nez p0, :cond_0', 'return-object v0', 'invoke-static {}, Lmiuix/animation/Folme;->getLooper()Landroid/os/Looper;', 'if-eq p0, v1, :cond_2', 'invoke-virtual {p0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;', 'invoke-virtual {p0}, Ljava/lang/Thread;->getId()J', 'invoke-static {v1, v2}, Lmiuix/animation/Folme;->getUiLooperByTid(J)Landroid/os/Looper;'],
        'type': 'method_replace',
        'search': """.method protected initialValue()Lmiuix/animation/internal/AndroidEngine;
    .registers 4

    invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;

    move-result-object p0

    const/4 v0, 0x0

    if-nez p0, :cond_0

    return-object v0

    :cond_0
    invoke-static {}, Lmiuix/animation/Folme;->getLooper()Landroid/os/Looper;

    move-result-object v1

    if-eq p0, v1, :cond_2

    invoke-virtual {p0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object p0

    invoke-virtual {p0}, Ljava/lang/Thread;->getId()J

    move-result-wide v1

    invoke-static {v1, v2}, Lmiuix/animation/Folme;->getUiLooperByTid(J)Landroid/os/Looper;

    move-result-object p0

    if-eqz p0, :cond_1

    goto :goto_0

    :cond_1
    return-object v0

    :cond_2
    :goto_0
    new-instance p0, Lmiuix/animation/internal/AndroidEngine;

    invoke-direct {p0}, Lmiuix/animation/internal/AndroidEngine;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected initialValue()Lmiuix/animation/internal/AndroidEngine;
    .registers 4

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0}, Ljava/lang/Thread;->getId()J

    move-result-wide v1

    goto :goto_7

    nop

    :goto_1
    if-nez p0, :cond_0

    goto :goto_c

    :cond_0
    goto :goto_b

    nop

    :goto_2
    invoke-static {}, Landroid/os/Looper;->myLooper()Landroid/os/Looper;

    move-result-object p0

    goto :goto_8

    nop

    :goto_3
    invoke-static {}, Lmiuix/animation/Folme;->getLooper()Landroid/os/Looper;

    move-result-object v1

    goto :goto_9

    nop

    :goto_4
    return-object p0

    :goto_5
    return-object v0

    :goto_6
    goto :goto_e

    nop

    :goto_7
    invoke-static {v1, v2}, Lmiuix/animation/Folme;->getUiLooperByTid(J)Landroid/os/Looper;

    move-result-object p0

    goto :goto_1

    nop

    :goto_8
    const/4 v0, 0x0

    goto :goto_a

    nop

    :goto_9
    if-ne p0, v1, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_d

    nop

    :goto_a
    if-eqz p0, :cond_2

    goto :goto_11

    :cond_2
    goto :goto_10

    nop

    :goto_b
    goto :goto_6

    :goto_c
    goto :goto_5

    nop

    :goto_d
    invoke-virtual {p0}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object p0

    goto :goto_0

    nop

    :goto_e
    new-instance p0, Lmiuix/animation/internal/AndroidEngine;

    goto :goto_f

    nop

    :goto_f
    invoke-direct {p0}, Lmiuix/animation/internal/AndroidEngine;-><init>()V

    goto :goto_4

    nop

    :goto_10
    return-object v0

    :goto_11
    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
