TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/transition/MiuixTransitionSet.smali'
CLASS_FALLBACK_NAMES = ['MiuixTransitionSet.smali']
CLASS_ANCHORS = ['.super Lmiuix/transition/MiuixTransition;']

PATCHES = [
    {
        'id': 'miuix_transition_MiuixTransitionSet__toString',
        'method': '.method toString(Ljava/lang/String;)Ljava/lang/String;',
        'method_name': 'toString',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/transition/MiuixTransition;->toString(Ljava/lang/String;)Ljava/lang/String;', 'iget-object v2, p0, Lmiuix/transition/MiuixTransitionSet;->mTransitions:Ljava/util/ArrayList;', 'invoke-virtual {v2}, Ljava/util/ArrayList;->size()I', 'if-ge v1, v2, :cond_0', 'new-instance v2, Ljava/lang/StringBuilder;', 'invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V', 'invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'const-string v0, "\\n"'],
        'type': 'method_replace',
        'search': """.method toString(Ljava/lang/String;)Ljava/lang/String;
    .registers 7

    invoke-super {p0, p1}, Lmiuix/transition/MiuixTransition;->toString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    const/4 v1, 0x0

    :goto_0
    iget-object v2, p0, Lmiuix/transition/MiuixTransitionSet;->mTransitions:Ljava/util/ArrayList;

    invoke-virtual {v2}, Ljava/util/ArrayList;->size()I

    move-result v2

    if-ge v1, v2, :cond_0

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v0, "\n"

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v0, p0, Lmiuix/transition/MiuixTransitionSet;->mTransitions:Ljava/util/ArrayList;

    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiuix/transition/MiuixTransition;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v4, "  "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v0, v3}, Lmiuix/transition/MiuixTransition;->toString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    :cond_0
    return-object v0
.end method""",
        'replacement': """.method toString(Ljava/lang/String;)Ljava/lang/String;
    .registers 7

    goto :goto_6

    nop

    :goto_0
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_1
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_2
    add-int/lit8 v1, v1, 0x1

    goto :goto_a

    nop

    :goto_3
    check-cast v0, Lmiuix/transition/MiuixTransition;

    goto :goto_13

    nop

    :goto_4
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_16

    nop

    :goto_5
    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_8

    nop

    :goto_6
    invoke-super {p0, p1}, Lmiuix/transition/MiuixTransition;->toString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    goto :goto_c

    nop

    :goto_7
    const-string v0, "\n"

    goto :goto_5

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/transition/MiuixTransitionSet;->mTransitions:Ljava/util/ArrayList;

    goto :goto_17

    nop

    :goto_9
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    goto :goto_f

    nop

    :goto_a
    goto :goto_d

    :goto_b
    goto :goto_15

    nop

    :goto_c
    const/4 v1, 0x0

    :goto_d
    goto :goto_e

    nop

    :goto_e
    iget-object v2, p0, Lmiuix/transition/MiuixTransitionSet;->mTransitions:Ljava/util/ArrayList;

    goto :goto_14

    nop

    :goto_f
    invoke-virtual {v0, v3}, Lmiuix/transition/MiuixTransition;->toString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    goto :goto_18

    nop

    :goto_10
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_11

    nop

    :goto_11
    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_19

    nop

    :goto_12
    if-lt v1, v2, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_1

    nop

    :goto_13
    new-instance v3, Ljava/lang/StringBuilder;

    goto :goto_10

    nop

    :goto_14
    invoke-virtual {v2}, Ljava/util/ArrayList;->size()I

    move-result v2

    goto :goto_12

    nop

    :goto_15
    return-object v0

    :goto_16
    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_7

    nop

    :goto_17
    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v0

    goto :goto_3

    nop

    :goto_18
    invoke-virtual {v2, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1a

    nop

    :goto_19
    const-string v4, "  "

    goto :goto_0

    nop

    :goto_1a
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
