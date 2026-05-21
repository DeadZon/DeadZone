TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/AnimTask.smali'
CLASS_FALLBACK_NAMES = ['AnimTask.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/utils/LinkNode;', '.implements Ljava/lang/Runnable;', '.field public static final MAX_ANIM_COUNT_SINGLE_TASK:I = 0x64', '.field public static final MAX_MAIN_THREAD_TASK_SIZE:I = 0xfa0', '.field public static final MAX_SUB_THREAD_TASK_SIZE:I', '.field public static final OP_CANCEL:B = 0x4t']

PATCHES = [
    {
        'id': 'miuix_animation_internal_AnimTask__setup',
        'method': '.method setup(III)V',
        'method_name': 'setup',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;', 'invoke-virtual {v0}, Lmiuix/animation/internal/AnimStats;->clear()V', 'iget-object v0, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;', 'iput p2, v0, Lmiuix/animation/internal/AnimStats;->animCount:I', 'iput p3, v0, Lmiuix/animation/internal/AnimStats;->focusCount:I', 'iput p1, p0, Lmiuix/animation/internal/AnimTask;->startPos:I', 'return-void'],
        'type': 'method_replace',
        'search': """.method setup(III)V
    .registers 5

    iget-object v0, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    invoke-virtual {v0}, Lmiuix/animation/internal/AnimStats;->clear()V

    iget-object v0, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    iput p2, v0, Lmiuix/animation/internal/AnimStats;->animCount:I

    iput p3, v0, Lmiuix/animation/internal/AnimStats;->focusCount:I

    iput p1, p0, Lmiuix/animation/internal/AnimTask;->startPos:I

    return-void
.end method""",
        'replacement': """.method setup(III)V
    .registers 5

    goto :goto_2

    nop

    :goto_0
    iput p1, p0, Lmiuix/animation/internal/AnimTask;->startPos:I

    goto :goto_4

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    goto :goto_3

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    goto :goto_6

    nop

    :goto_3
    iput p2, v0, Lmiuix/animation/internal/AnimStats;->animCount:I

    goto :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    iput p3, v0, Lmiuix/animation/internal/AnimStats;->focusCount:I

    goto :goto_0

    nop

    :goto_6
    invoke-virtual {v0}, Lmiuix/animation/internal/AnimStats;->clear()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimTask__updateAnimStats',
        'method': '.method updateAnimStats()V',
        'method_name': 'updateAnimStats',
        'method_anchors': ['iget-object v0, p0, Lmiuix/animation/internal/AnimTask;->info:Lmiuix/animation/internal/TransitionInfo;', 'iget-object v0, v0, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;', 'iget v1, p0, Lmiuix/animation/internal/AnimTask;->startPos:I', 'iget-object v2, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;', 'iget v2, v2, Lmiuix/animation/internal/AnimStats;->animCount:I', 'if-ge v1, v2, :cond_6', 'invoke-interface {v0, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;', 'check-cast v3, Lmiuix/animation/listener/UpdateInfo;'],
        'type': 'method_replace',
        'search': """.method updateAnimStats()V
    .registers 8

    iget-object v0, p0, Lmiuix/animation/internal/AnimTask;->info:Lmiuix/animation/internal/TransitionInfo;

    iget-object v0, v0, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    iget v1, p0, Lmiuix/animation/internal/AnimTask;->startPos:I

    iget-object v2, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    iget v2, v2, Lmiuix/animation/internal/AnimStats;->animCount:I

    add-int/2addr v2, v1

    :goto_0
    if-ge v1, v2, :cond_6

    invoke-interface {v0, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lmiuix/animation/listener/UpdateInfo;

    if-nez v3, :cond_0

    goto :goto_2

    :cond_0
    iget-object v4, v3, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    iget-byte v4, v4, Lmiuix/animation/internal/AnimInfo;->op:B

    const/4 v5, 0x1

    if-eqz v4, :cond_5

    iget-object v4, v3, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    iget-byte v4, v4, Lmiuix/animation/internal/AnimInfo;->op:B

    if-ne v4, v5, :cond_1

    goto :goto_1

    :cond_1
    iget-object v4, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    iget v6, v4, Lmiuix/animation/internal/AnimStats;->startedCount:I

    add-int/2addr v6, v5

    iput v6, v4, Lmiuix/animation/internal/AnimStats;->startedCount:I

    iget-object v3, v3, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    iget-byte v3, v3, Lmiuix/animation/internal/AnimInfo;->op:B

    const/4 v4, 0x3

    if-eq v3, v4, :cond_4

    const/4 v4, 0x4

    if-eq v3, v4, :cond_3

    const/4 v4, 0x5

    if-eq v3, v4, :cond_2

    const/4 v4, 0x6

    if-eq v3, v4, :cond_2

    goto :goto_2

    :cond_2
    iget-object v3, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    iget v4, v3, Lmiuix/animation/internal/AnimStats;->failCount:I

    add-int/2addr v4, v5

    iput v4, v3, Lmiuix/animation/internal/AnimStats;->failCount:I

    goto :goto_2

    :cond_3
    iget-object v3, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    iget v4, v3, Lmiuix/animation/internal/AnimStats;->cancelCount:I

    add-int/2addr v4, v5

    iput v4, v3, Lmiuix/animation/internal/AnimStats;->cancelCount:I

    goto :goto_2

    :cond_4
    iget-object v3, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    iget v4, v3, Lmiuix/animation/internal/AnimStats;->endCount:I

    add-int/2addr v4, v5

    iput v4, v3, Lmiuix/animation/internal/AnimStats;->endCount:I

    goto :goto_2

    :cond_5
    :goto_1
    iget-object v3, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    iget v4, v3, Lmiuix/animation/internal/AnimStats;->prepareCount:I

    add-int/2addr v4, v5

    iput v4, v3, Lmiuix/animation/internal/AnimStats;->prepareCount:I

    :goto_2
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    :cond_6
    return-void
.end method""",
        'replacement': """.method updateAnimStats()V
    .registers 8

    goto :goto_17

    nop

    :goto_0
    invoke-interface {v0, v1}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v3

    goto :goto_38

    nop

    :goto_1
    iget v6, v4, Lmiuix/animation/internal/AnimStats;->startedCount:I

    goto :goto_2d

    nop

    :goto_2
    iget-object v0, v0, Lmiuix/animation/internal/TransitionInfo;->updateList:Ljava/util/List;

    goto :goto_30

    nop

    :goto_3
    iget-object v3, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    goto :goto_8

    nop

    :goto_4
    iput v4, v3, Lmiuix/animation/internal/AnimStats;->cancelCount:I

    goto :goto_3e

    nop

    :goto_5
    iput v4, v3, Lmiuix/animation/internal/AnimStats;->endCount:I

    goto :goto_c

    nop

    :goto_6
    const/4 v4, 0x4

    goto :goto_26

    nop

    :goto_7
    iget-byte v4, v4, Lmiuix/animation/internal/AnimInfo;->op:B

    goto :goto_2a

    nop

    :goto_8
    iget v4, v3, Lmiuix/animation/internal/AnimStats;->failCount:I

    goto :goto_13

    nop

    :goto_9
    iget-byte v4, v4, Lmiuix/animation/internal/AnimInfo;->op:B

    goto :goto_18

    nop

    :goto_a
    goto :goto_1a

    :goto_b
    goto :goto_3

    nop

    :goto_c
    goto :goto_1a

    :goto_d
    goto :goto_29

    nop

    :goto_e
    if-ne v3, v4, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_a

    nop

    :goto_f
    iget v4, v3, Lmiuix/animation/internal/AnimStats;->cancelCount:I

    goto :goto_1b

    nop

    :goto_10
    return-void

    :goto_11
    iget-object v3, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    goto :goto_22

    nop

    :goto_12
    const/4 v4, 0x5

    goto :goto_25

    nop

    :goto_13
    add-int/2addr v4, v5

    goto :goto_33

    nop

    :goto_14
    add-int/2addr v4, v5

    goto :goto_19

    nop

    :goto_15
    iget-object v2, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    goto :goto_34

    nop

    :goto_16
    iget-byte v3, v3, Lmiuix/animation/internal/AnimInfo;->op:B

    goto :goto_1f

    nop

    :goto_17
    iget-object v0, p0, Lmiuix/animation/internal/AnimTask;->info:Lmiuix/animation/internal/TransitionInfo;

    goto :goto_2

    nop

    :goto_18
    if-eq v4, v5, :cond_1

    goto :goto_3a

    :cond_1
    goto :goto_39

    nop

    :goto_19
    iput v4, v3, Lmiuix/animation/internal/AnimStats;->prepareCount:I

    :goto_1a
    goto :goto_31

    nop

    :goto_1b
    add-int/2addr v4, v5

    goto :goto_4

    nop

    :goto_1c
    iget-object v4, v3, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    goto :goto_7

    nop

    :goto_1d
    iput v6, v4, Lmiuix/animation/internal/AnimStats;->startedCount:I

    goto :goto_2b

    nop

    :goto_1e
    iget v4, v3, Lmiuix/animation/internal/AnimStats;->prepareCount:I

    goto :goto_14

    nop

    :goto_1f
    const/4 v4, 0x3

    goto :goto_3d

    nop

    :goto_20
    iget-object v4, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    goto :goto_1

    nop

    :goto_21
    iget-object v4, v3, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    goto :goto_9

    nop

    :goto_22
    iget v4, v3, Lmiuix/animation/internal/AnimStats;->endCount:I

    goto :goto_2c

    nop

    :goto_23
    goto :goto_1a

    :goto_24
    goto :goto_2f

    nop

    :goto_25
    if-ne v3, v4, :cond_2

    goto :goto_b

    :cond_2
    goto :goto_32

    nop

    :goto_26
    if-ne v3, v4, :cond_3

    goto :goto_24

    :cond_3
    goto :goto_12

    nop

    :goto_27
    goto :goto_1a

    :goto_28
    goto :goto_1c

    nop

    :goto_29
    iget-object v3, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    goto :goto_1e

    nop

    :goto_2a
    const/4 v5, 0x1

    goto :goto_40

    nop

    :goto_2b
    iget-object v3, v3, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    goto :goto_16

    nop

    :goto_2c
    add-int/2addr v4, v5

    goto :goto_5

    nop

    :goto_2d
    add-int/2addr v6, v5

    goto :goto_1d

    nop

    :goto_2e
    if-lt v1, v2, :cond_4

    goto :goto_3c

    :cond_4
    goto :goto_0

    nop

    :goto_2f
    iget-object v3, p0, Lmiuix/animation/internal/AnimTask;->animStats:Lmiuix/animation/internal/AnimStats;

    goto :goto_f

    nop

    :goto_30
    iget v1, p0, Lmiuix/animation/internal/AnimTask;->startPos:I

    goto :goto_15

    nop

    :goto_31
    add-int/lit8 v1, v1, 0x1

    goto :goto_3b

    nop

    :goto_32
    const/4 v4, 0x6

    goto :goto_e

    nop

    :goto_33
    iput v4, v3, Lmiuix/animation/internal/AnimStats;->failCount:I

    goto :goto_23

    nop

    :goto_34
    iget v2, v2, Lmiuix/animation/internal/AnimStats;->animCount:I

    goto :goto_36

    nop

    :goto_35
    if-eqz v3, :cond_5

    goto :goto_28

    :cond_5
    goto :goto_27

    nop

    :goto_36
    add-int/2addr v2, v1

    :goto_37
    goto :goto_2e

    nop

    :goto_38
    check-cast v3, Lmiuix/animation/listener/UpdateInfo;

    goto :goto_35

    nop

    :goto_39
    goto :goto_d

    :goto_3a
    goto :goto_20

    nop

    :goto_3b
    goto :goto_37

    :goto_3c
    goto :goto_10

    nop

    :goto_3d
    if-ne v3, v4, :cond_6

    goto :goto_3f

    :cond_6
    goto :goto_6

    nop

    :goto_3e
    goto :goto_1a

    :goto_3f
    goto :goto_11

    nop

    :goto_40
    if-nez v4, :cond_7

    goto :goto_d

    :cond_7
    goto :goto_21

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
