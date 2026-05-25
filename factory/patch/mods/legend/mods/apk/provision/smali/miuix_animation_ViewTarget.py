TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/ViewTarget.smali'
CLASS_FALLBACK_NAMES = ['ViewTarget.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/IAnimTarget;', '.field public static final sCreator:Lmiuix/animation/ITargetCreator;', '.field public static final sSimpleCreator:Lmiuix/animation/ITargetCreator;']

PATCHES = [
    {
        'id': 'miuix_animation_ViewTarget__createHandler',
        'method': '.method protected createHandler(Landroid/os/Looper;)Lmiuix/animation/internal/TargetHandler;',
        'method_name': 'createHandler',
        'method_anchors': ['if-nez p1, :cond_0', 'invoke-static {}, Lmiuix/animation/Folme;->getLooper()Landroid/os/Looper;', 'invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;', 'if-eq p1, v0, :cond_2', 'invoke-virtual {p1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;', 'invoke-virtual {v0}, Ljava/lang/Thread;->getId()J', 'invoke-static {v0, v1}, Lmiuix/animation/Folme;->getUiLooperByTid(J)Landroid/os/Looper;', 'if-nez v0, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected createHandler(Landroid/os/Looper;)Lmiuix/animation/internal/TargetHandler;
    .registers 5

    if-nez p1, :cond_0

    invoke-static {}, Lmiuix/animation/Folme;->getLooper()Landroid/os/Looper;

    move-result-object p1

    goto :goto_0

    :cond_0
    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v0

    if-eq p1, v0, :cond_2

    invoke-virtual {p1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    invoke-static {v0, v1}, Lmiuix/animation/Folme;->getUiLooperByTid(J)Landroid/os/Looper;

    move-result-object v0

    if-nez v0, :cond_2

    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result v0

    if-eqz v0, :cond_1

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "ViewTarget.createHandler registerUiLooper "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    const-string v1, " tid "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/Thread;->getId()J

    move-result-wide v1

    invoke-virtual {v0, v1, v2}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const/4 v1, 0x0

    new-array v1, v1, [Ljava/lang/Object;

    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :cond_1
    invoke-static {p1}, Lmiuix/animation/Folme;->registerUiLooper(Landroid/os/Looper;)V

    :cond_2
    :goto_0
    if-nez p1, :cond_3

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string p1, "warning!! the ViewTarget handler created failed, caused by creating in a thread without Looper, the animation will do not work!! trace:"

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    new-instance p1, Ljava/lang/Throwable;

    invoke-direct {p1}, Ljava/lang/Throwable;-><init>()V

    invoke-static {p1}, Landroid/util/Log;->getStackTraceString(Ljava/lang/Throwable;)Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string p1, "miuix_anim"

    invoke-static {p1, p0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    const/4 p0, 0x0

    return-object p0

    :cond_3
    new-instance v0, Lmiuix/animation/internal/TargetHandler;

    invoke-direct {v0, p1, p0}, Lmiuix/animation/internal/TargetHandler;-><init>(Landroid/os/Looper;Lmiuix/animation/IAnimTarget;)V

    return-object v0
.end method""",
        'replacement': """.method protected createHandler(Landroid/os/Looper;)Lmiuix/animation/internal/TargetHandler;
    .registers 5

    goto :goto_23

    nop

    :goto_0
    if-eqz v0, :cond_0

    goto :goto_1c

    :cond_0
    goto :goto_2

    nop

    :goto_1
    invoke-virtual {v0, v1, v2}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

    goto :goto_13

    nop

    :goto_2
    invoke-static {}, Lmiuix/animation/utils/LogUtils;->isLogDetailEnable()Z

    move-result v0

    goto :goto_26

    nop

    :goto_3
    goto :goto_1c

    :goto_4
    goto :goto_5

    nop

    :goto_5
    invoke-static {}, Landroid/os/Looper;->getMainLooper()Landroid/os/Looper;

    move-result-object v0

    goto :goto_12

    nop

    :goto_6
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_7
    invoke-static {v0, v1}, Lmiuix/animation/utils/LogUtils;->debug(Ljava/lang/String;[Ljava/lang/Object;)V

    :goto_8
    goto :goto_1b

    nop

    :goto_9
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_1a

    nop

    :goto_a
    invoke-static {p1, p0}, Landroid/util/Log;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_18

    nop

    :goto_b
    const-string p1, "miuix_anim"

    goto :goto_a

    nop

    :goto_c
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_2a

    nop

    :goto_d
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_15

    nop

    :goto_e
    invoke-virtual {v1}, Ljava/lang/Thread;->getId()J

    move-result-wide v1

    goto :goto_1

    nop

    :goto_f
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_28

    nop

    :goto_10
    const/4 v1, 0x0

    goto :goto_24

    nop

    :goto_11
    invoke-direct {v0, p1, p0}, Lmiuix/animation/internal/TargetHandler;-><init>(Landroid/os/Looper;Lmiuix/animation/IAnimTarget;)V

    goto :goto_1d

    nop

    :goto_12
    if-ne p1, v0, :cond_1

    goto :goto_1c

    :cond_1
    goto :goto_17

    nop

    :goto_13
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_10

    nop

    :goto_14
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2b

    nop

    :goto_15
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_b

    nop

    :goto_16
    invoke-static {}, Lmiuix/animation/Folme;->getLooper()Landroid/os/Looper;

    move-result-object p1

    goto :goto_3

    nop

    :goto_17
    invoke-virtual {p1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v0

    goto :goto_21

    nop

    :goto_18
    const/4 p0, 0x0

    goto :goto_2d

    nop

    :goto_19
    invoke-static {v0, v1}, Lmiuix/animation/Folme;->getUiLooperByTid(J)Landroid/os/Looper;

    move-result-object v0

    goto :goto_0

    nop

    :goto_1a
    const-string v1, " tid "

    goto :goto_29

    nop

    :goto_1b
    invoke-static {p1}, Lmiuix/animation/Folme;->registerUiLooper(Landroid/os/Looper;)V

    :goto_1c
    goto :goto_22

    nop

    :goto_1d
    return-object v0

    :goto_1e
    new-instance v0, Lmiuix/animation/internal/TargetHandler;

    goto :goto_11

    nop

    :goto_1f
    invoke-direct {p1}, Ljava/lang/Throwable;-><init>()V

    goto :goto_25

    nop

    :goto_20
    const-string v1, "ViewTarget.createHandler registerUiLooper "

    goto :goto_6

    nop

    :goto_21
    invoke-virtual {v0}, Ljava/lang/Thread;->getId()J

    move-result-wide v0

    goto :goto_19

    nop

    :goto_22
    if-eqz p1, :cond_2

    goto :goto_2e

    :cond_2
    goto :goto_f

    nop

    :goto_23
    if-eqz p1, :cond_3

    goto :goto_4

    :cond_3
    goto :goto_16

    nop

    :goto_24
    new-array v1, v1, [Ljava/lang/Object;

    goto :goto_7

    nop

    :goto_25
    invoke-static {p1}, Landroid/util/Log;->getStackTraceString(Ljava/lang/Throwable;)Ljava/lang/String;

    move-result-object p1

    goto :goto_d

    nop

    :goto_26
    if-nez v0, :cond_4

    goto :goto_8

    :cond_4
    goto :goto_c

    nop

    :goto_27
    invoke-virtual {p1}, Landroid/os/Looper;->getThread()Ljava/lang/Thread;

    move-result-object v1

    goto :goto_e

    nop

    :goto_28
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_2c

    nop

    :goto_29
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_27

    nop

    :goto_2a
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_20

    nop

    :goto_2b
    new-instance p1, Ljava/lang/Throwable;

    goto :goto_1f

    nop

    :goto_2c
    const-string p1, "warning!! the ViewTarget handler created failed, caused by creating in a thread without Looper, the animation will do not work!! trace:"

    goto :goto_14

    nop

    :goto_2d
    return-object p0

    :goto_2e
    goto :goto_1e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
