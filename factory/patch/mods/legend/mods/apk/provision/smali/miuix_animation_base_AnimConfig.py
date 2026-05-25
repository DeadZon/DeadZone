TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/base/AnimConfig.smali'
CLASS_FALLBACK_NAMES = ['AnimConfig.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lmiuix/animation/internal/DesignReview;', '.field public static final FLAG_AUTO_INIT:J = 0x8L', '.field public static final FLAG_DELTA:J = 0x1L', '.field public static final FLAG_INIT:J = 0x2L', '.field public static final FLAG_INT:J = 0x4L']

PATCHES = [
    {
        'id': 'miuix_animation_base_AnimConfig__setSpecial',
        'method': '.method varargs setSpecial(Lmiuix/animation/base/AnimSpecialConfig;Lmiuix/animation/utils/EaseManager$EaseStyle;J[F)V',
        'method_name': 'setSpecial',
        'method_anchors': ['if-eqz p2, :cond_0', 'invoke-virtual {p1, p2}, Lmiuix/animation/base/AnimConfig;->setEase(Lmiuix/animation/utils/EaseManager$EaseStyle;)Lmiuix/animation/base/AnimConfig;', 'if-lez p0, :cond_1', 'invoke-virtual {p1, p3, p4}, Lmiuix/animation/base/AnimConfig;->setDelay(J)Lmiuix/animation/base/AnimConfig;', 'if-lez p0, :cond_2', 'invoke-virtual {p1, p0}, Lmiuix/animation/base/AnimConfig;->setFromSpeed(F)Lmiuix/animation/base/AnimConfig;', 'return-void'],
        'type': 'method_replace',
        'search': """.method varargs setSpecial(Lmiuix/animation/base/AnimSpecialConfig;Lmiuix/animation/utils/EaseManager$EaseStyle;J[F)V
    .registers 8

    if-eqz p2, :cond_0

    invoke-virtual {p1, p2}, Lmiuix/animation/base/AnimConfig;->setEase(Lmiuix/animation/utils/EaseManager$EaseStyle;)Lmiuix/animation/base/AnimConfig;

    :cond_0
    const-wide/16 v0, 0x0

    cmp-long p0, p3, v0

    if-lez p0, :cond_1

    invoke-virtual {p1, p3, p4}, Lmiuix/animation/base/AnimConfig;->setDelay(J)Lmiuix/animation/base/AnimConfig;

    :cond_1
    array-length p0, p5

    if-lez p0, :cond_2

    const/4 p0, 0x0

    aget p0, p5, p0

    invoke-virtual {p1, p0}, Lmiuix/animation/base/AnimConfig;->setFromSpeed(F)Lmiuix/animation/base/AnimConfig;

    :cond_2
    return-void
.end method""",
        'replacement': """.method varargs setSpecial(Lmiuix/animation/base/AnimSpecialConfig;Lmiuix/animation/utils/EaseManager$EaseStyle;J[F)V
    .registers 8

    goto :goto_4

    nop

    :goto_0
    array-length p0, p5

    goto :goto_2

    nop

    :goto_1
    aget p0, p5, p0

    goto :goto_6

    nop

    :goto_2
    if-gtz p0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_5

    nop

    :goto_3
    const-wide/16 v0, 0x0

    goto :goto_e

    nop

    :goto_4
    if-nez p2, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_c

    nop

    :goto_5
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_6
    invoke-virtual {p1, p0}, Lmiuix/animation/base/AnimConfig;->setFromSpeed(F)Lmiuix/animation/base/AnimConfig;

    :goto_7
    goto :goto_8

    nop

    :goto_8
    return-void

    :goto_9
    invoke-virtual {p1, p3, p4}, Lmiuix/animation/base/AnimConfig;->setDelay(J)Lmiuix/animation/base/AnimConfig;

    :goto_a
    goto :goto_0

    nop

    :goto_b
    if-gtz p0, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_9

    nop

    :goto_c
    invoke-virtual {p1, p2}, Lmiuix/animation/base/AnimConfig;->setEase(Lmiuix/animation/utils/EaseManager$EaseStyle;)Lmiuix/animation/base/AnimConfig;

    :goto_d
    goto :goto_3

    nop

    :goto_e
    cmp-long p0, p3, v0

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
