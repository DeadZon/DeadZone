TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/utils/SpringInterpolator$OverDampingSolution.smali'
CLASS_FALLBACK_NAMES = ['SpringInterpolator$OverDampingSolution.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/utils/SpringInterpolator$SpringSolution;']

PATCHES = [
    {
        'id': 'miuix_animation_utils_SpringInterpolator__OverDampingSolution__dX',
        'method': '.method dX(F)D',
        'method_name': 'dX',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c1:D', 'iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r1:D', 'invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D', 'iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c2:D', 'iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r2:D', 'invoke-static {p0, p1}, Ljava/lang/Math;->exp(D)D', 'return-wide v0'],
        'type': 'method_replace',
        'search': """.method dX(F)D
    .registers 8

    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c1:D

    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r1:D

    mul-double/2addr v0, v2

    float-to-double v4, p1

    mul-double/2addr v2, v4

    invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D

    move-result-wide v2

    mul-double/2addr v0, v2

    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c2:D

    iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r2:D

    mul-double/2addr v2, p0

    mul-double/2addr p0, v4

    invoke-static {p0, p1}, Ljava/lang/Math;->exp(D)D

    move-result-wide p0

    mul-double/2addr v2, p0

    add-double/2addr v0, v2

    return-wide v0
.end method""",
        'replacement': """.method dX(F)D
    .registers 8

    goto :goto_9

    nop

    :goto_0
    invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D

    move-result-wide v2

    goto :goto_2

    nop

    :goto_1
    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c2:D

    goto :goto_5

    nop

    :goto_2
    mul-double/2addr v0, v2

    goto :goto_1

    nop

    :goto_3
    mul-double/2addr v0, v2

    goto :goto_b

    nop

    :goto_4
    return-wide v0

    :goto_5
    iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r2:D

    goto :goto_6

    nop

    :goto_6
    mul-double/2addr v2, p0

    goto :goto_a

    nop

    :goto_7
    mul-double/2addr v2, v4

    goto :goto_0

    nop

    :goto_8
    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r1:D

    goto :goto_3

    nop

    :goto_9
    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c1:D

    goto :goto_8

    nop

    :goto_a
    mul-double/2addr p0, v4

    goto :goto_c

    nop

    :goto_b
    float-to-double v4, p1

    goto :goto_7

    nop

    :goto_c
    invoke-static {p0, p1}, Ljava/lang/Math;->exp(D)D

    move-result-wide p0

    goto :goto_d

    nop

    :goto_d
    mul-double/2addr v2, p0

    goto :goto_e

    nop

    :goto_e
    add-double/2addr v0, v2

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_utils_SpringInterpolator__OverDampingSolution__x',
        'method': '.method x(F)D',
        'method_name': 'x',
        'method_anchors': ['iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c1:D', 'iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r1:D', 'invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D', 'iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c2:D', 'iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r2:D', 'invoke-static {v6, v7}, Ljava/lang/Math;->exp(D)D', 'iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->xStar:D', 'return-wide v0'],
        'type': 'method_replace',
        'search': """.method x(F)D
    .registers 10

    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c1:D

    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r1:D

    float-to-double v4, p1

    mul-double/2addr v2, v4

    invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D

    move-result-wide v2

    mul-double/2addr v0, v2

    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c2:D

    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r2:D

    mul-double/2addr v6, v4

    invoke-static {v6, v7}, Ljava/lang/Math;->exp(D)D

    move-result-wide v4

    mul-double/2addr v2, v4

    add-double/2addr v0, v2

    iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->xStar:D

    add-double/2addr v0, p0

    return-wide v0
.end method""",
        'replacement': """.method x(F)D
    .registers 10

    goto :goto_7

    nop

    :goto_0
    invoke-static {v2, v3}, Ljava/lang/Math;->exp(D)D

    move-result-wide v2

    goto :goto_9

    nop

    :goto_1
    iget-wide v6, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r2:D

    goto :goto_3

    nop

    :goto_2
    add-double/2addr v0, v2

    goto :goto_e

    nop

    :goto_3
    mul-double/2addr v6, v4

    goto :goto_4

    nop

    :goto_4
    invoke-static {v6, v7}, Ljava/lang/Math;->exp(D)D

    move-result-wide v4

    goto :goto_d

    nop

    :goto_5
    return-wide v0

    :goto_6
    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c2:D

    goto :goto_1

    nop

    :goto_7
    iget-wide v0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->c1:D

    goto :goto_a

    nop

    :goto_8
    add-double/2addr v0, p0

    goto :goto_5

    nop

    :goto_9
    mul-double/2addr v0, v2

    goto :goto_6

    nop

    :goto_a
    iget-wide v2, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->r1:D

    goto :goto_b

    nop

    :goto_b
    float-to-double v4, p1

    goto :goto_c

    nop

    :goto_c
    mul-double/2addr v2, v4

    goto :goto_0

    nop

    :goto_d
    mul-double/2addr v2, v4

    goto :goto_2

    nop

    :goto_e
    iget-wide p0, p0, Lmiuix/animation/utils/SpringInterpolator$OverDampingSolution;->xStar:D

    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
