TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/transition/MiuixTransition.smali'
CLASS_FALLBACK_NAMES = ['MiuixTransition.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/lang/Cloneable;', '.field private static final DEFAULT_MATCH_ORDER:[I']

PATCHES = [
    {
        'id': 'miuix_transition_MiuixTransition__onTransitionEnd',
        'method': '.method protected onTransitionEnd()V',
        'method_name': 'onTransitionEnd',
        'method_anchors': ['iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->isEmpty()Z', 'if-nez v0, :cond_1', 'iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;', 'invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;', 'invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z', 'if-nez v1, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onTransitionEnd()V
    .registers 3

    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;

    if-eqz v0, :cond_1

    invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->isEmpty()Z

    move-result v0

    if-nez v0, :cond_1

    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-nez v1, :cond_0

    goto :goto_0

    :cond_0
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object p0

    invoke-static {p0}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    const/4 p0, 0x0

    throw p0

    :cond_1
    :goto_0
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTransitionRunners:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->clear()V

    iget-object p0, p0, Lmiuix/transition/MiuixTransition;->mAnimConfig:Lmiuix/animation/base/AnimConfig;

    invoke-virtual {p0}, Lmiuix/animation/base/AnimConfig;->clear()V

    return-void
.end method""",
        'replacement': """.method protected onTransitionEnd()V
    .registers 3

    goto :goto_9

    nop

    :goto_0
    throw p0

    :goto_1
    goto :goto_12

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/transition/MiuixTransition;->mAnimConfig:Lmiuix/animation/base/AnimConfig;

    goto :goto_b

    nop

    :goto_3
    invoke-static {p0}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    goto :goto_e

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_d

    nop

    :goto_5
    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_4

    nop

    :goto_6
    invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->isEmpty()Z

    move-result v0

    goto :goto_5

    nop

    :goto_7
    goto :goto_1

    :goto_8
    goto :goto_11

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_f

    nop

    :goto_a
    invoke-virtual {v0}, Ljava/util/ArrayList;->clear()V

    goto :goto_2

    nop

    :goto_b
    invoke-virtual {p0}, Lmiuix/animation/base/AnimConfig;->clear()V

    goto :goto_c

    nop

    :goto_c
    return-void

    :goto_d
    invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    goto :goto_13

    nop

    :goto_e
    const/4 p0, 0x0

    goto :goto_0

    nop

    :goto_f
    if-nez v0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_6

    nop

    :goto_10
    if-eqz v1, :cond_2

    goto :goto_8

    :cond_2
    goto :goto_7

    nop

    :goto_11
    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object p0

    goto :goto_3

    nop

    :goto_12
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTransitionRunners:Ljava/util/ArrayList;

    goto :goto_a

    nop

    :goto_13
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_transition_MiuixTransition__onTransitionStart',
        'method': '.method protected onTransitionStart()V',
        'method_name': 'onTransitionStart',
        'method_anchors': ['iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->isEmpty()Z', 'if-nez v0, :cond_1', 'iget-object p0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;', 'invoke-virtual {p0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;', 'invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z', 'if-nez v0, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onTransitionStart()V
    .registers 2

    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;

    if-eqz v0, :cond_1

    invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->isEmpty()Z

    move-result v0

    if-nez v0, :cond_1

    iget-object p0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;

    invoke-virtual {p0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object p0

    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v0

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object p0

    invoke-static {p0}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    const/4 p0, 0x0

    throw p0

    :cond_1
    :goto_0
    return-void
.end method""",
        'replacement': """.method protected onTransitionStart()V
    .registers 2

    goto :goto_f

    nop

    :goto_0
    invoke-interface {p0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object p0

    goto :goto_5

    nop

    :goto_1
    invoke-interface {p0}, Ljava/util/Iterator;->hasNext()Z

    move-result v0

    goto :goto_b

    nop

    :goto_2
    invoke-virtual {v0}, Ljava/util/concurrent/CopyOnWriteArrayList;->isEmpty()Z

    move-result v0

    goto :goto_e

    nop

    :goto_3
    throw p0

    :goto_4
    goto :goto_a

    nop

    :goto_5
    invoke-static {p0}, Landroidx/appcompat/app/ToolbarActionBar$$ExternalSyntheticThrowCCEIfNotNull0;->m(Ljava/lang/Object;)V

    goto :goto_8

    nop

    :goto_6
    goto :goto_4

    :goto_7
    goto :goto_0

    nop

    :goto_8
    const/4 p0, 0x0

    goto :goto_3

    nop

    :goto_9
    iget-object p0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_c

    nop

    :goto_a
    return-void

    :goto_b
    if-eqz v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_6

    nop

    :goto_c
    invoke-virtual {p0}, Ljava/util/concurrent/CopyOnWriteArrayList;->iterator()Ljava/util/Iterator;

    move-result-object p0

    goto :goto_1

    nop

    :goto_d
    if-nez v0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_2

    nop

    :goto_e
    if-eqz v0, :cond_2

    goto :goto_4

    :cond_2
    goto :goto_9

    nop

    :goto_f
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mListeners:Ljava/util/concurrent/CopyOnWriteArrayList;

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_transition_MiuixTransition__toString',
        'method': '.method toString(Ljava/lang/String;)Ljava/lang/String;',
        'method_name': 'toString',
        'method_anchors': ['new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-virtual {p1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;', 'invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'const-string p1, "@"', 'invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method toString(Ljava/lang/String;)Ljava/lang/String;
    .registers 6

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p1

    invoke-virtual {p1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p1

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string p1, "@"

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result p1

    invoke-static {p1}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;

    move-result-object p1

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string p1, ": "

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTargetIds:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-gtz v0, :cond_1

    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTargets:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-lez v0, :cond_0

    goto :goto_0

    :cond_0
    return-object p1

    :cond_1
    :goto_0
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string p1, "tgts("

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTargetIds:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    const-string v1, ", "

    const/4 v2, 0x0

    if-lez v0, :cond_3

    move v0, v2

    :goto_1
    iget-object v3, p0, Lmiuix/transition/MiuixTransition;->mTargetIds:Ljava/util/ArrayList;

    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v3

    if-ge v0, v3, :cond_3

    if-lez v0, :cond_2

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    :cond_2
    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p1, p0, Lmiuix/transition/MiuixTransition;->mTargetIds:Ljava/util/ArrayList;

    invoke-virtual {p1, v0}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object p1

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    add-int/lit8 v0, v0, 0x1

    goto :goto_1

    :cond_3
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTargets:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-lez v0, :cond_5

    :goto_2
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTargets:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    if-ge v2, v0, :cond_5

    if-lez v2, :cond_4

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    :cond_4
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object p1, p0, Lmiuix/transition/MiuixTransition;->mTargets:Ljava/util/ArrayList;

    invoke-virtual {p1, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object p1

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    add-int/lit8 v2, v2, 0x1

    goto :goto_2

    :cond_5
    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string p1, ")"

    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method toString(Ljava/lang/String;)Ljava/lang/String;
    .registers 6

    goto :goto_2a

    nop

    :goto_0
    iget-object p1, p0, Lmiuix/transition/MiuixTransition;->mTargetIds:Ljava/util/ArrayList;

    goto :goto_43

    nop

    :goto_1
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    :goto_2
    goto :goto_1a

    nop

    :goto_3
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_2b

    nop

    :goto_4
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_20

    nop

    :goto_5
    const-string p1, ")"

    goto :goto_52

    nop

    :goto_6
    if-lez v0, :cond_0

    goto :goto_35

    :cond_0
    goto :goto_38

    nop

    :goto_7
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_41

    nop

    :goto_8
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1

    nop

    :goto_9
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_a
    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_10

    nop

    :goto_b
    if-lt v0, v3, :cond_1

    goto :goto_4c

    :cond_1
    goto :goto_1d

    nop

    :goto_c
    const-string p1, ": "

    goto :goto_23

    nop

    :goto_d
    invoke-virtual {p0}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object p1

    goto :goto_4a

    nop

    :goto_e
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2e

    nop

    :goto_f
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_d

    nop

    :goto_10
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_51

    nop

    :goto_11
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    :goto_12
    goto :goto_3e

    nop

    :goto_13
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_39

    nop

    :goto_14
    goto :goto_32

    :goto_15
    goto :goto_2d

    nop

    :goto_16
    new-instance v3, Ljava/lang/StringBuilder;

    goto :goto_13

    nop

    :goto_17
    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_0

    nop

    :goto_18
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTargets:Ljava/util/ArrayList;

    goto :goto_2c

    nop

    :goto_19
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_45

    nop

    :goto_1a
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_48

    nop

    :goto_1b
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTargetIds:Ljava/util/ArrayList;

    goto :goto_1f

    nop

    :goto_1c
    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_11

    nop

    :goto_1d
    if-gtz v0, :cond_2

    goto :goto_12

    :cond_2
    goto :goto_16

    nop

    :goto_1e
    invoke-static {p1}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;

    move-result-object p1

    goto :goto_3b

    nop

    :goto_1f
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    goto :goto_55

    nop

    :goto_20
    const-string p1, "@"

    goto :goto_e

    nop

    :goto_21
    goto :goto_35

    :goto_22
    goto :goto_34

    nop

    :goto_23
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_3d

    nop

    :goto_24
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_3

    nop

    :goto_25
    const-string p1, "tgts("

    goto :goto_30

    nop

    :goto_26
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTargets:Ljava/util/ArrayList;

    goto :goto_53

    nop

    :goto_27
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_17

    nop

    :goto_28
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTargetIds:Ljava/util/ArrayList;

    goto :goto_54

    nop

    :goto_29
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_1b

    nop

    :goto_2a
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_3c

    nop

    :goto_2b
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_25

    nop

    :goto_2c
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    goto :goto_31

    nop

    :goto_2d
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_56

    nop

    :goto_2e
    invoke-virtual {p0}, Ljava/lang/Object;->hashCode()I

    move-result p1

    goto :goto_1e

    nop

    :goto_2f
    if-gtz v0, :cond_3

    goto :goto_4c

    :cond_3
    goto :goto_46

    nop

    :goto_30
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_29

    nop

    :goto_31
    if-gtz v0, :cond_4

    goto :goto_15

    :cond_4
    :goto_32
    goto :goto_26

    nop

    :goto_33
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_44

    nop

    :goto_34
    return-object p1

    :goto_35
    goto :goto_24

    nop

    :goto_36
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    goto :goto_42

    nop

    :goto_37
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_4d

    nop

    :goto_38
    iget-object v0, p0, Lmiuix/transition/MiuixTransition;->mTargets:Ljava/util/ArrayList;

    goto :goto_36

    nop

    :goto_39
    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1c

    nop

    :goto_3a
    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v3

    goto :goto_b

    nop

    :goto_3b
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_c

    nop

    :goto_3c
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_f

    nop

    :goto_3d
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_28

    nop

    :goto_3e
    new-instance v3, Ljava/lang/StringBuilder;

    goto :goto_27

    nop

    :goto_3f
    if-gtz v2, :cond_5

    goto :goto_2

    :cond_5
    goto :goto_9

    nop

    :goto_40
    if-lt v2, v0, :cond_6

    goto :goto_15

    :cond_6
    goto :goto_3f

    nop

    :goto_41
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_8

    nop

    :goto_42
    if-gtz v0, :cond_7

    goto :goto_22

    :cond_7
    goto :goto_21

    nop

    :goto_43
    invoke-virtual {p1, v0}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object p1

    goto :goto_a

    nop

    :goto_44
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_49

    nop

    :goto_45
    iget-object p1, p0, Lmiuix/transition/MiuixTransition;->mTargets:Ljava/util/ArrayList;

    goto :goto_4f

    nop

    :goto_46
    move v0, v2

    :goto_47
    goto :goto_4e

    nop

    :goto_48
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_19

    nop

    :goto_49
    add-int/lit8 v2, v2, 0x1

    goto :goto_14

    nop

    :goto_4a
    invoke-virtual {p1}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object p1

    goto :goto_4

    nop

    :goto_4b
    goto :goto_47

    :goto_4c
    goto :goto_18

    nop

    :goto_4d
    return-object p0

    :goto_4e
    iget-object v3, p0, Lmiuix/transition/MiuixTransition;->mTargetIds:Ljava/util/ArrayList;

    goto :goto_3a

    nop

    :goto_4f
    invoke-virtual {p1, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object p1

    goto :goto_33

    nop

    :goto_50
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_5

    nop

    :goto_51
    add-int/lit8 v0, v0, 0x1

    goto :goto_4b

    nop

    :goto_52
    invoke-virtual {p0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_37

    nop

    :goto_53
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    goto :goto_40

    nop

    :goto_54
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v0

    goto :goto_6

    nop

    :goto_55
    const-string v1, ", "

    goto :goto_57

    nop

    :goto_56
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_50

    nop

    :goto_57
    const/4 v2, 0x0

    goto :goto_2f

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
