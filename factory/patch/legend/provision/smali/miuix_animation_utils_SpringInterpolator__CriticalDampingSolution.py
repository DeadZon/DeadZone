TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/utils/SpringInterpolator$CriticalDampingSolution.smali'
CLASS_FALLBACK_NAMES = ['SpringInterpolator$CriticalDampingSolution.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/utils/SpringInterpolator$SpringSolution;']

PATCHES = [
    {
        'id': 'miuix_animation_utils_SpringInterpolator__CriticalDampingSolution__dX',
        'method': '.method dX(F)D',
        'method_name': 'dX',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c1:D', 'iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->r:D', 'iget-wide v4, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c2:D', 'invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D', 'return-wide v0'],
        'type': 'method_replace',
        'search': """.method dX(F)D
    .registers 12

    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c1:D

    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->r:D

    mul-double/2addr v0, v2

    iget-wide v4, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c2:D

    float-to-double p0, p1

    mul-double v6, v2, p0

    const-wide/high16 v8, 0x3ff0000000000000L

    add-double/2addr v6, v8

    mul-double/2addr v4, v6

    add-double/2addr v0, v4

    mul-double/2addr v2, p0

    invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D

    move-result-wide p0

    mul-double/2addr v0, p0

    return-wide v0
.end method""",
        'replacement': """.method dX(F)D
    .registers 12

    goto :goto_9

    nop

    :goto_0
    invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D

    move-result-wide p0

    goto :goto_d

    nop

    :goto_1
    return-wide v0

    :goto_2
    iget-wide v4, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c2:D

    goto :goto_6

    nop

    :goto_3
    mul-double/2addr v2, p0

    goto :goto_0

    nop

    :goto_4
    const-wide/high16 v8, 0x3ff0000000000000L

    goto :goto_c

    nop

    :goto_5
    mul-double v6, v2, p0

    goto :goto_4

    nop

    :goto_6
    float-to-double p0, p1

    goto :goto_5

    nop

    :goto_7
    mul-double/2addr v0, v2

    goto :goto_2

    nop

    :goto_8
    mul-double/2addr v4, v6

    goto :goto_a

    nop

    :goto_9
    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c1:D

    goto :goto_b

    nop

    :goto_a
    add-double/2addr v0, v4

    goto :goto_3

    nop

    :goto_b
    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->r:D

    goto :goto_7

    nop

    :goto_c
    add-double/2addr v6, v8

    goto :goto_8

    nop

    :goto_d
    mul-double/2addr v0, p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_utils_SpringInterpolator__CriticalDampingSolution__x',
        'method': '.method x(F)D',
        'method_name': 'x',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c1:D', 'iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c2:D', 'iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->r:D', 'invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D', 'iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->xStar:D', 'return-wide v0'],
        'type': 'method_replace',
        'search': """.method x(F)D
    .registers 8

    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c1:D

    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c2:D

    float-to-double v4, p1

    mul-double/2addr v2, v4

    add-double/2addr v0, v2

    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->r:D

    mul-double/2addr v2, v4

    invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D

    move-result-wide v2

    mul-double/2addr v0, v2

    iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->xStar:D

    add-double/2addr v0, p0

    return-wide v0
.end method""",
        'replacement': """.method x(F)D
    .registers 8

    goto :goto_8

    nop

    :goto_0
    return-wide v0

    :goto_1
    invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D

    move-result-wide v2

    goto :goto_a

    nop

    :goto_2
    float-to-double v4, p1

    goto :goto_3

    nop

    :goto_3
    mul-double/2addr v2, v4

    goto :goto_5

    nop

    :goto_4
    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c2:D

    goto :goto_2

    nop

    :goto_5
    add-double/2addr v0, v2

    goto :goto_b

    nop

    :goto_6
    iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->xStar:D

    goto :goto_7

    nop

    :goto_7
    add-double/2addr v0, p0

    goto :goto_0

    nop

    :goto_8
    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->c1:D

    goto :goto_4

    nop

    :goto_9
    mul-double/2addr v2, v4

    goto :goto_1

    nop

    :goto_a
    mul-double/2addr v0, v2

    goto :goto_6

    nop

    :goto_b
    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$CriticalDampingSolution;->r:D

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
