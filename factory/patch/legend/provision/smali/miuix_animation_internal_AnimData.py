TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/internal/AnimData.smali'
CLASS_FALLBACK_NAMES = ['AnimData.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_animation_internal_AnimData__clear',
        'method': '.method clear()V',
        'method_name': 'clear',
        'method_anchors': ['iput-object v0, p0, Lmiuix/animation/internal/AnimData;->property:Lmiuix/animation/property/FloatProperty;', 'iput-object v0, p0, Lmiuix/animation/internal/AnimData;->ease:Lmiuix/animation/utils/EaseManager$EaseStyle;', 'iput v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I', 'iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->frameInterval:D', 'iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->duration:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method clear()V
    .registers 3

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/animation/internal/AnimData;->property:Lmiuix/animation/property/FloatProperty;

    iput-object v0, p0, Lmiuix/animation/internal/AnimData;->ease:Lmiuix/animation/utils/EaseManager$EaseStyle;

    const/4 v0, 0x0

    iput v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I

    const-wide/16 v0, 0x0

    iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->frameInterval:D

    iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->duration:D

    return-void
.end method""",
        'replacement': """.method clear()V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    iput v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I

    goto :goto_4

    nop

    :goto_1
    const/4 v0, 0x0

    goto :goto_0

    nop

    :goto_2
    iput-object v0, p0, Lmiuix/animation/internal/AnimData;->property:Lmiuix/animation/property/FloatProperty;

    goto :goto_6

    nop

    :goto_3
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_4
    const-wide/16 v0, 0x0

    goto :goto_8

    nop

    :goto_5
    iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->duration:D

    goto :goto_7

    nop

    :goto_6
    iput-object v0, p0, Lmiuix/animation/internal/AnimData;->ease:Lmiuix/animation/utils/EaseManager$EaseStyle;

    goto :goto_1

    nop

    :goto_7
    return-void

    :goto_8
    iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->frameInterval:D

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimData___from',
        'method': '.method from(Lmiuix/animation/listener/UpdateInfo;Lmiuix/animation/base/AnimConfig;Lmiuix/animation/base/AnimSpecialConfig;)V',
        'method_name': 'from',
        'method_anchors': ['iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->property:Lmiuix/animation/property/FloatProperty;', 'iput-object v0, p0, Lmiuix/animation/internal/AnimData;->property:Lmiuix/animation/property/FloatProperty;', 'iget-wide v0, p1, Lmiuix/animation/listener/UpdateInfo;->velocity:D', 'iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->velocity:D', 'iget v0, p1, Lmiuix/animation/listener/UpdateInfo;->frameCount:I', 'iput v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I', 'iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;', 'iget-byte v0, v0, Lmiuix/animation/internal/AnimInfo;->op:B'],
        'type': 'method_replace',
        'search': """.method from(Lmiuix/animation/listener/UpdateInfo;Lmiuix/animation/base/AnimConfig;Lmiuix/animation/base/AnimSpecialConfig;)V
    .registers 7

    iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->property:Lmiuix/animation/property/FloatProperty;

    iput-object v0, p0, Lmiuix/animation/internal/AnimData;->property:Lmiuix/animation/property/FloatProperty;

    iget-wide v0, p1, Lmiuix/animation/listener/UpdateInfo;->velocity:D

    iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->velocity:D

    iget v0, p1, Lmiuix/animation/listener/UpdateInfo;->frameCount:I

    iput v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I

    iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    iget-byte v0, v0, Lmiuix/animation/internal/AnimInfo;->op:B

    iput-byte v0, p0, Lmiuix/animation/internal/AnimData;->op:B

    iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->frameInterval:D

    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->frameInterval:D

    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->duration:D

    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->duration:D

    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->initTime:J

    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->initTime:J

    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->startTime:J

    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->startTime:J

    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->progress:D

    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->progress:D

    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->startValue:D

    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->startValue:D

    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->targetValue:D

    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->targetValue:D

    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->value:D

    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->value:D

    iget-boolean v1, p1, Lmiuix/animation/listener/UpdateInfo;->isCompleted:Z

    iput-boolean v1, p0, Lmiuix/animation/internal/AnimData;->isCompleted:Z

    iget-boolean p1, p1, Lmiuix/animation/listener/UpdateInfo;->justStart:Z

    iput-boolean p1, p0, Lmiuix/animation/internal/AnimData;->justStart:Z

    iget-boolean p1, v0, Lmiuix/animation/internal/AnimInfo;->justEnd:Z

    iput-boolean p1, p0, Lmiuix/animation/internal/AnimData;->justEnd:Z

    invoke-static {p2, p3}, Lmiuix/animation/internal/AnimConfigUtils;->getTintMode(Lmiuix/animation/base/AnimConfig;Lmiuix/animation/base/AnimSpecialConfig;)I

    move-result p1

    iput p1, p0, Lmiuix/animation/internal/AnimData;->tintMode:I

    invoke-static {p2, p3}, Lmiuix/animation/internal/AnimConfigUtils;->getEase(Lmiuix/animation/base/AnimConfig;Lmiuix/animation/base/AnimSpecialConfig;)Lmiuix/animation/utils/EaseManager$EaseStyle;

    move-result-object p1

    iput-object p1, p0, Lmiuix/animation/internal/AnimData;->ease:Lmiuix/animation/utils/EaseManager$EaseStyle;

    invoke-static {p2, p3}, Lmiuix/animation/internal/AnimConfigUtils;->getDelay(Lmiuix/animation/base/AnimConfig;Lmiuix/animation/base/AnimSpecialConfig;)J

    move-result-wide p1

    iput-wide p1, p0, Lmiuix/animation/internal/AnimData;->delay:J

    return-void
.end method""",
        'replacement': """.method from(Lmiuix/animation/listener/UpdateInfo;Lmiuix/animation/base/AnimConfig;Lmiuix/animation/base/AnimSpecialConfig;)V
    .registers 7

    goto :goto_6

    nop

    :goto_0
    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->targetValue:D

    goto :goto_17

    nop

    :goto_1
    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->progress:D

    goto :goto_f

    nop

    :goto_2
    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->initTime:J

    goto :goto_1f

    nop

    :goto_3
    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->startValue:D

    goto :goto_21

    nop

    :goto_4
    iput v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I

    goto :goto_22

    nop

    :goto_5
    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->startTime:J

    goto :goto_1

    nop

    :goto_6
    iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->property:Lmiuix/animation/property/FloatProperty;

    goto :goto_18

    nop

    :goto_7
    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->frameInterval:D

    goto :goto_9

    nop

    :goto_8
    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->duration:D

    goto :goto_a

    nop

    :goto_9
    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->duration:D

    goto :goto_8

    nop

    :goto_a
    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->initTime:J

    goto :goto_2

    nop

    :goto_b
    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->startValue:D

    goto :goto_3

    nop

    :goto_c
    iget v0, p1, Lmiuix/animation/listener/UpdateInfo;->frameCount:I

    goto :goto_4

    nop

    :goto_d
    invoke-static {p2, p3}, Lmiuix/animation/internal/AnimConfigUtils;->getDelay(Lmiuix/animation/base/AnimConfig;Lmiuix/animation/base/AnimSpecialConfig;)J

    move-result-wide p1

    goto :goto_14

    nop

    :goto_e
    iput-boolean v1, p0, Lmiuix/animation/internal/AnimData;->isCompleted:Z

    goto :goto_20

    nop

    :goto_f
    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->progress:D

    goto :goto_b

    nop

    :goto_10
    iget-boolean v1, p1, Lmiuix/animation/listener/UpdateInfo;->isCompleted:Z

    goto :goto_e

    nop

    :goto_11
    iput-wide v1, p0, Lmiuix/animation/internal/AnimData;->value:D

    goto :goto_10

    nop

    :goto_12
    iput-boolean p1, p0, Lmiuix/animation/internal/AnimData;->justStart:Z

    goto :goto_1d

    nop

    :goto_13
    return-void

    :goto_14
    iput-wide p1, p0, Lmiuix/animation/internal/AnimData;->delay:J

    goto :goto_13

    nop

    :goto_15
    iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->velocity:D

    goto :goto_c

    nop

    :goto_16
    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->frameInterval:D

    goto :goto_7

    nop

    :goto_17
    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->value:D

    goto :goto_11

    nop

    :goto_18
    iput-object v0, p0, Lmiuix/animation/internal/AnimData;->property:Lmiuix/animation/property/FloatProperty;

    goto :goto_1b

    nop

    :goto_19
    iput-boolean p1, p0, Lmiuix/animation/internal/AnimData;->justEnd:Z

    goto :goto_23

    nop

    :goto_1a
    invoke-static {p2, p3}, Lmiuix/animation/internal/AnimConfigUtils;->getEase(Lmiuix/animation/base/AnimConfig;Lmiuix/animation/base/AnimSpecialConfig;)Lmiuix/animation/utils/EaseManager$EaseStyle;

    move-result-object p1

    goto :goto_25

    nop

    :goto_1b
    iget-wide v0, p1, Lmiuix/animation/listener/UpdateInfo;->velocity:D

    goto :goto_15

    nop

    :goto_1c
    iget-byte v0, v0, Lmiuix/animation/internal/AnimInfo;->op:B

    goto :goto_1e

    nop

    :goto_1d
    iget-boolean p1, v0, Lmiuix/animation/internal/AnimInfo;->justEnd:Z

    goto :goto_19

    nop

    :goto_1e
    iput-byte v0, p0, Lmiuix/animation/internal/AnimData;->op:B

    goto :goto_26

    nop

    :goto_1f
    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->startTime:J

    goto :goto_5

    nop

    :goto_20
    iget-boolean p1, p1, Lmiuix/animation/listener/UpdateInfo;->justStart:Z

    goto :goto_12

    nop

    :goto_21
    iget-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->targetValue:D

    goto :goto_0

    nop

    :goto_22
    iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    goto :goto_1c

    nop

    :goto_23
    invoke-static {p2, p3}, Lmiuix/animation/internal/AnimConfigUtils;->getTintMode(Lmiuix/animation/base/AnimConfig;Lmiuix/animation/base/AnimSpecialConfig;)I

    move-result p1

    goto :goto_24

    nop

    :goto_24
    iput p1, p0, Lmiuix/animation/internal/AnimData;->tintMode:I

    goto :goto_1a

    nop

    :goto_25
    iput-object p1, p0, Lmiuix/animation/internal/AnimData;->ease:Lmiuix/animation/utils/EaseManager$EaseStyle;

    goto :goto_d

    nop

    :goto_26
    iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    goto :goto_16

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimData__reset',
        'method': '.method reset()V',
        'method_name': 'reset',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/animation/internal/AnimData;->isCompleted:Z', 'iput v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I', 'iput-boolean v1, p0, Lmiuix/animation/internal/AnimData;->justStart:Z', 'iput-boolean v0, p0, Lmiuix/animation/internal/AnimData;->justEnd:Z', 'iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->frameInterval:D', 'iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->duration:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method reset()V
    .registers 3

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/animation/internal/AnimData;->isCompleted:Z

    iput v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I

    const/4 v1, 0x1

    iput-boolean v1, p0, Lmiuix/animation/internal/AnimData;->justStart:Z

    iput-boolean v0, p0, Lmiuix/animation/internal/AnimData;->justEnd:Z

    const-wide/16 v0, 0x0

    iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->frameInterval:D

    iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->duration:D

    return-void
.end method""",
        'replacement': """.method reset()V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    iput v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I

    goto :goto_3

    nop

    :goto_1
    iput-boolean v0, p0, Lmiuix/animation/internal/AnimData;->isCompleted:Z

    goto :goto_0

    nop

    :goto_2
    const/4 v0, 0x0

    goto :goto_1

    nop

    :goto_3
    const/4 v1, 0x1

    goto :goto_8

    nop

    :goto_4
    iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->duration:D

    goto :goto_5

    nop

    :goto_5
    return-void

    :goto_6
    iput-wide v0, p0, Lmiuix/animation/internal/AnimData;->frameInterval:D

    goto :goto_4

    nop

    :goto_7
    const-wide/16 v0, 0x0

    goto :goto_6

    nop

    :goto_8
    iput-boolean v1, p0, Lmiuix/animation/internal/AnimData;->justStart:Z

    goto :goto_9

    nop

    :goto_9
    iput-boolean v0, p0, Lmiuix/animation/internal/AnimData;->justEnd:Z

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_internal_AnimData__to',
        'method': '.method to(Lmiuix/animation/listener/UpdateInfo;)V',
        'method_name': 'to',
        'method_anchors': ['iget v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I', 'iput v0, p1, Lmiuix/animation/listener/UpdateInfo;->frameCount:I', 'iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;', 'iget-byte v1, p0, Lmiuix/animation/internal/AnimData;->op:B', 'iput-byte v1, v0, Lmiuix/animation/internal/AnimInfo;->op:B', 'iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;', 'iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->delay:J', 'iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->delay:J'],
        'type': 'method_replace',
        'search': """.method to(Lmiuix/animation/listener/UpdateInfo;)V
    .registers 5

    iget v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I

    iput v0, p1, Lmiuix/animation/listener/UpdateInfo;->frameCount:I

    iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    iget-byte v1, p0, Lmiuix/animation/internal/AnimData;->op:B

    iput-byte v1, v0, Lmiuix/animation/internal/AnimInfo;->op:B

    iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->delay:J

    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->delay:J

    iget v1, p0, Lmiuix/animation/internal/AnimData;->tintMode:I

    iput v1, v0, Lmiuix/animation/internal/AnimInfo;->tintMode:I

    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->initTime:J

    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->initTime:J

    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->startTime:J

    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->startTime:J

    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->progress:D

    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->progress:D

    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->startValue:D

    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->startValue:D

    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->targetValue:D

    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->targetValue:D

    iget-boolean v1, p0, Lmiuix/animation/internal/AnimData;->isCompleted:Z

    iput-boolean v1, p1, Lmiuix/animation/listener/UpdateInfo;->isCompleted:Z

    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->value:D

    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->value:D

    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->velocity:D

    iput-wide v1, p1, Lmiuix/animation/listener/UpdateInfo;->velocity:D

    iget-boolean v1, p0, Lmiuix/animation/internal/AnimData;->justStart:Z

    iput-boolean v1, p1, Lmiuix/animation/listener/UpdateInfo;->justStart:Z

    iget-boolean p1, p0, Lmiuix/animation/internal/AnimData;->justEnd:Z

    iput-boolean p1, v0, Lmiuix/animation/internal/AnimInfo;->justEnd:Z

    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->frameInterval:D

    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->frameInterval:D

    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->duration:D

    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->duration:D

    invoke-virtual {p0}, Lmiuix/animation/internal/AnimData;->clear()V

    return-void
.end method""",
        'replacement': """.method to(Lmiuix/animation/listener/UpdateInfo;)V
    .registers 5

    goto :goto_23

    nop

    :goto_0
    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->progress:D

    goto :goto_5

    nop

    :goto_1
    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->delay:J

    goto :goto_1d

    nop

    :goto_2
    iget-boolean v1, p0, Lmiuix/animation/internal/AnimData;->isCompleted:Z

    goto :goto_b

    nop

    :goto_3
    iput-wide v1, p1, Lmiuix/animation/listener/UpdateInfo;->velocity:D

    goto :goto_a

    nop

    :goto_4
    return-void

    :goto_5
    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->startValue:D

    goto :goto_9

    nop

    :goto_6
    iget-byte v1, p0, Lmiuix/animation/internal/AnimData;->op:B

    goto :goto_f

    nop

    :goto_7
    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->targetValue:D

    goto :goto_21

    nop

    :goto_8
    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->duration:D

    goto :goto_17

    nop

    :goto_9
    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->startValue:D

    goto :goto_7

    nop

    :goto_a
    iget-boolean v1, p0, Lmiuix/animation/internal/AnimData;->justStart:Z

    goto :goto_13

    nop

    :goto_b
    iput-boolean v1, p1, Lmiuix/animation/listener/UpdateInfo;->isCompleted:Z

    goto :goto_1a

    nop

    :goto_c
    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->progress:D

    goto :goto_0

    nop

    :goto_d
    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->startTime:J

    goto :goto_10

    nop

    :goto_e
    iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    goto :goto_1b

    nop

    :goto_f
    iput-byte v1, v0, Lmiuix/animation/internal/AnimInfo;->op:B

    goto :goto_e

    nop

    :goto_10
    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->startTime:J

    goto :goto_c

    nop

    :goto_11
    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->frameInterval:D

    goto :goto_15

    nop

    :goto_12
    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->initTime:J

    goto :goto_1e

    nop

    :goto_13
    iput-boolean v1, p1, Lmiuix/animation/listener/UpdateInfo;->justStart:Z

    goto :goto_19

    nop

    :goto_14
    iput v0, p1, Lmiuix/animation/listener/UpdateInfo;->frameCount:I

    goto :goto_1f

    nop

    :goto_15
    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->frameInterval:D

    goto :goto_8

    nop

    :goto_16
    iput v1, v0, Lmiuix/animation/internal/AnimInfo;->tintMode:I

    goto :goto_12

    nop

    :goto_17
    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->duration:D

    goto :goto_1c

    nop

    :goto_18
    iput-boolean p1, v0, Lmiuix/animation/internal/AnimInfo;->justEnd:Z

    goto :goto_11

    nop

    :goto_19
    iget-boolean p1, p0, Lmiuix/animation/internal/AnimData;->justEnd:Z

    goto :goto_18

    nop

    :goto_1a
    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->value:D

    goto :goto_20

    nop

    :goto_1b
    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->delay:J

    goto :goto_1

    nop

    :goto_1c
    invoke-virtual {p0}, Lmiuix/animation/internal/AnimData;->clear()V

    goto :goto_4

    nop

    :goto_1d
    iget v1, p0, Lmiuix/animation/internal/AnimData;->tintMode:I

    goto :goto_16

    nop

    :goto_1e
    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->initTime:J

    goto :goto_d

    nop

    :goto_1f
    iget-object v0, p1, Lmiuix/animation/listener/UpdateInfo;->animInfo:Lmiuix/animation/internal/AnimInfo;

    goto :goto_6

    nop

    :goto_20
    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->value:D

    goto :goto_22

    nop

    :goto_21
    iput-wide v1, v0, Lmiuix/animation/internal/AnimInfo;->targetValue:D

    goto :goto_2

    nop

    :goto_22
    iget-wide v1, p0, Lmiuix/animation/internal/AnimData;->velocity:D

    goto :goto_3

    nop

    :goto_23
    iget v0, p0, Lmiuix/animation/internal/AnimData;->frameCount:I

    goto :goto_14

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
