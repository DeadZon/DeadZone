TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/utils/SpringInterpolator$SpringSolution.smali'
CLASS_FALLBACK_NAMES = ['SpringInterpolator$SpringSolution.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_animation_utils_SpringInterpolator__SpringSolution__solve',
        'method': '.method solve(DDDD)D',
        'method_name': 'solve',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/animation/utils/SpringInterpolator$SpringSolution;->x(F)D', 'invoke-virtual {p0, p1}, Lmiuix/animation/utils/SpringInterpolator$SpringSolution;->dX(F)D', 'return-wide p3'],
        'type': 'method_replace',
        'search': """.method solve(DDDD)D
    .registers 11

    double-to-float p1, p1

    invoke-virtual {p0, p1}, Lmiuix/animation/utils/SpringInterpolator$SpringSolution;->x(F)D

    move-result-wide v0

    invoke-virtual {p0, p1}, Lmiuix/animation/utils/SpringInterpolator$SpringSolution;->dX(F)D

    move-result-wide p0

    mul-double/2addr p3, v0

    mul-double/2addr p3, v0

    mul-double/2addr p0, p0

    add-double/2addr p3, p0

    const-wide/high16 p0, 0x4000000000000000L

    mul-double/2addr p5, p0

    sub-double/2addr v0, p7

    mul-double/2addr p5, v0

    sub-double/2addr p3, p5

    return-wide p3
.end method""",
        'replacement': """.method solve(DDDD)D
    .registers 11

    goto :goto_9

    nop

    :goto_0
    sub-double/2addr p3, p5

    goto :goto_3

    nop

    :goto_1
    mul-double/2addr p3, v0

    goto :goto_5

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/animation/utils/SpringInterpolator$SpringSolution;->dX(F)D

    move-result-wide p0

    goto :goto_8

    nop

    :goto_3
    return-wide p3

    :goto_4
    add-double/2addr p3, p0

    goto :goto_b

    nop

    :goto_5
    mul-double/2addr p0, p0

    goto :goto_4

    nop

    :goto_6
    mul-double/2addr p5, v0

    goto :goto_0

    nop

    :goto_7
    sub-double/2addr v0, p7

    goto :goto_6

    nop

    :goto_8
    mul-double/2addr p3, v0

    goto :goto_1

    nop

    :goto_9
    double-to-float p1, p1

    goto :goto_c

    nop

    :goto_a
    mul-double/2addr p5, p0

    goto :goto_7

    nop

    :goto_b
    const-wide/high16 p0, 0x4000000000000000L

    goto :goto_a

    nop

    :goto_c
    invoke-virtual {p0, p1}, Lmiuix/animation/utils/SpringInterpolator$SpringSolution;->x(F)D

    move-result-wide v0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
