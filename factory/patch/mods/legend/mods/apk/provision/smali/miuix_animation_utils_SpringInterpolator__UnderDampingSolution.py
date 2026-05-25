TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/utils/SpringInterpolator$UnderDampingSolution.smali'
CLASS_FALLBACK_NAMES = ['SpringInterpolator$UnderDampingSolution.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/utils/SpringInterpolator$SpringSolution;']

PATCHES = [
    {
        'id': 'miuix_animation_utils_SpringInterpolator__UnderDampingSolution__dX',
        'method': '.method dX(F)D',
        'method_name': 'dX',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D', 'invoke-static {v0, v1}, Ljava/lang/Math;->exp(D)D', 'iget-wide v4, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c1:D', 'iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D', 'iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c2:D', 'iget-wide v8, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D', 'invoke-static {v8, v9}, Ljava/lang/Math;->cos(D)D', 'iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c2:D'],
        'type': 'method_replace',
        'search': """.method dX(F)D
    .registers 12

    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D

    float-to-double v2, p1

    mul-double/2addr v0, v2

    invoke-static {v0, v1}, Ljava/lang/Math;->exp(D)D

    move-result-wide v0

    iget-wide v4, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c1:D

    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D

    mul-double/2addr v4, v6

    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c2:D

    iget-wide v8, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D

    mul-double/2addr v6, v8

    add-double/2addr v4, v6

    mul-double/2addr v8, v2

    invoke-static {v8, v9}, Ljava/lang/Math;->cos(D)D

    move-result-wide v6

    mul-double/2addr v4, v6

    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c2:D

    iget-wide v8, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D

    mul-double/2addr v6, v8

    iget-wide v8, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c1:D

    iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D

    mul-double/2addr v8, p0

    sub-double/2addr v6, v8

    mul-double/2addr p0, v2

    invoke-static {p0, p1}, Ljava/lang/Math;->sin(D)D

    move-result-wide p0

    mul-double/2addr v6, p0

    add-double/2addr v4, v6

    mul-double/2addr v0, v4

    return-wide v0
.end method""",
        'replacement': """.method dX(F)D
    .registers 12

    goto :goto_4

    nop

    :goto_0
    mul-double/2addr v0, v2

    goto :goto_15

    nop

    :goto_1
    mul-double/2addr v6, p0

    goto :goto_14

    nop

    :goto_2
    iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D

    goto :goto_e

    nop

    :goto_3
    mul-double/2addr v4, v6

    goto :goto_18

    nop

    :goto_4
    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D

    goto :goto_11

    nop

    :goto_5
    mul-double/2addr v8, v2

    goto :goto_19

    nop

    :goto_6
    iget-wide v8, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c1:D

    goto :goto_2

    nop

    :goto_7
    add-double/2addr v4, v6

    goto :goto_5

    nop

    :goto_8
    mul-double/2addr v4, v6

    goto :goto_12

    nop

    :goto_9
    mul-double/2addr v6, v8

    goto :goto_6

    nop

    :goto_a
    iget-wide v8, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D

    goto :goto_b

    nop

    :goto_b
    mul-double/2addr v6, v8

    goto :goto_7

    nop

    :goto_c
    invoke-static {p0, p1}, Ljava/lang/Math;->sin(D)D

    move-result-wide p0

    goto :goto_1

    nop

    :goto_d
    iget-wide v8, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D

    goto :goto_9

    nop

    :goto_e
    mul-double/2addr v8, p0

    goto :goto_1a

    nop

    :goto_f
    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D

    goto :goto_3

    nop

    :goto_10
    mul-double/2addr p0, v2

    goto :goto_c

    nop

    :goto_11
    float-to-double v2, p1

    goto :goto_0

    nop

    :goto_12
    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c2:D

    goto :goto_d

    nop

    :goto_13
    iget-wide v4, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c1:D

    goto :goto_f

    nop

    :goto_14
    add-double/2addr v4, v6

    goto :goto_17

    nop

    :goto_15
    invoke-static {v0, v1}, Ljava/lang/Math;->exp(D)D

    move-result-wide v0

    goto :goto_13

    nop

    :goto_16
    return-wide v0

    :goto_17
    mul-double/2addr v0, v4

    goto :goto_16

    nop

    :goto_18
    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c2:D

    goto :goto_a

    nop

    :goto_19
    invoke-static {v8, v9}, Ljava/lang/Math;->cos(D)D

    move-result-wide v6

    goto :goto_8

    nop

    :goto_1a
    sub-double/2addr v6, v8

    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_utils_SpringInterpolator__UnderDampingSolution__x',
        'method': '.method x(F)D',
        'method_name': 'x',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D', 'invoke-static {v0, v1}, Ljava/lang/Math;->exp(D)D', 'iget-wide v4, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c1:D', 'iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D', 'invoke-static {v6, v7}, Ljava/lang/Math;->cos(D)D', 'iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c2:D', 'iget-wide v8, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D', 'invoke-static {v8, v9}, Ljava/lang/Math;->sin(D)D'],
        'type': 'method_replace',
        'search': """.method x(F)D
    .registers 12

    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D

    float-to-double v2, p1

    mul-double/2addr v0, v2

    invoke-static {v0, v1}, Ljava/lang/Math;->exp(D)D

    move-result-wide v0

    iget-wide v4, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c1:D

    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D

    mul-double/2addr v6, v2

    invoke-static {v6, v7}, Ljava/lang/Math;->cos(D)D

    move-result-wide v6

    mul-double/2addr v4, v6

    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c2:D

    iget-wide v8, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D

    mul-double/2addr v8, v2

    invoke-static {v8, v9}, Ljava/lang/Math;->sin(D)D

    move-result-wide v2

    mul-double/2addr v6, v2

    add-double/2addr v4, v6

    mul-double/2addr v0, v4

    iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->xStar:D

    add-double/2addr v0, p0

    return-wide v0
.end method""",
        'replacement': """.method x(F)D
    .registers 12

    goto :goto_c

    nop

    :goto_0
    invoke-static {v8, v9}, Ljava/lang/Math;->sin(D)D

    move-result-wide v2

    goto :goto_10

    nop

    :goto_1
    add-double/2addr v0, p0

    goto :goto_5

    nop

    :goto_2
    mul-double/2addr v8, v2

    goto :goto_0

    nop

    :goto_3
    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c2:D

    goto :goto_11

    nop

    :goto_4
    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D

    goto :goto_8

    nop

    :goto_5
    return-wide v0

    :goto_6
    iget-wide v4, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->c1:D

    goto :goto_4

    nop

    :goto_7
    mul-double/2addr v0, v2

    goto :goto_e

    nop

    :goto_8
    mul-double/2addr v6, v2

    goto :goto_9

    nop

    :goto_9
    invoke-static {v6, v7}, Ljava/lang/Math;->cos(D)D

    move-result-wide v6

    goto :goto_f

    nop

    :goto_a
    add-double/2addr v4, v6

    goto :goto_d

    nop

    :goto_b
    float-to-double v2, p1

    goto :goto_7

    nop

    :goto_c
    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->alpha:D

    goto :goto_b

    nop

    :goto_d
    mul-double/2addr v0, v4

    goto :goto_12

    nop

    :goto_e
    invoke-static {v0, v1}, Ljava/lang/Math;->exp(D)D

    move-result-wide v0

    goto :goto_6

    nop

    :goto_f
    mul-double/2addr v4, v6

    goto :goto_3

    nop

    :goto_10
    mul-double/2addr v6, v2

    goto :goto_a

    nop

    :goto_11
    iget-wide v8, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->beta:D

    goto :goto_2

    nop

    :goto_12
    iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$UnderDampingSolution;->xStar:D

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
