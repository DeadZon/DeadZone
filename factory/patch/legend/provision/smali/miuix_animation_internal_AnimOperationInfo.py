TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/AnimOperationInfo.smali'
CLASS_FALLBACK_NAMES = ['AnimOperationInfo.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_animation_internal_AnimOperationInfo__isUsed',
        'method': '.method isUsed()Z',
        'method_name': 'isUsed',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AnimOperationInfo;->propList:Ljava/util/List;', 'if-nez v0, :cond_0', 'invoke-interface {v0}, Ljava/util/List;->size()I', 'iget p0, p0, Lmiuix/animation/internal/AnimOperationInfo;->usedCount:I', 'if-nez v0, :cond_2', 'if-lez p0, :cond_1', 'return v2', 'return v1'],
        'type': 'method_replace',
        'search': """.method isUsed()Z
    .registers 4

    iget-object v0, p0, Lmiuix/animation/internal/AnimOperationInfo;->propList:Ljava/util/List;

    const/4 v1, 0x0

    if-nez v0, :cond_0

    move v0, v1

    goto :goto_0

    :cond_0
    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v0

    :goto_0
    const/4 v2, 0x1

    iget p0, p0, Lmiuix/animation/internal/AnimOperationInfo;->usedCount:I

    if-nez v0, :cond_2

    if-lez p0, :cond_1

    return v2

    :cond_1
    return v1

    :cond_2
    if-ne p0, v0, :cond_3

    return v2

    :cond_3
    return v1
.end method""",
        'replacement': """.method isUsed()Z
    .registers 4

    goto :goto_b

    nop

    :goto_0
    const/4 v2, 0x1

    goto :goto_4

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_13

    :cond_0
    goto :goto_a

    nop

    :goto_2
    return v2

    :goto_3
    goto :goto_8

    nop

    :goto_4
    iget p0, p0, Lmiuix/animation/internal/AnimOperationInfo;->usedCount:I

    goto :goto_d

    nop

    :goto_5
    return v1

    :goto_6
    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v0

    :goto_7
    goto :goto_0

    nop

    :goto_8
    return v1

    :goto_9
    goto :goto_11

    nop

    :goto_a
    move v0, v1

    goto :goto_12

    nop

    :goto_b
    iget-object v0, p0, Lmiuix/animation/internal/AnimOperationInfo;->propList:Ljava/util/List;

    goto :goto_c

    nop

    :goto_c
    const/4 v1, 0x0

    goto :goto_1

    nop

    :goto_d
    if-eqz v0, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_10

    nop

    :goto_e
    return v2

    :goto_f
    goto :goto_5

    nop

    :goto_10
    if-gtz p0, :cond_2

    goto :goto_3

    :cond_2
    goto :goto_2

    nop

    :goto_11
    if-eq p0, v0, :cond_3

    goto :goto_f

    :cond_3
    goto :goto_e

    nop

    :goto_12
    goto :goto_7

    :goto_13
    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
