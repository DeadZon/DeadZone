TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/motion/AndroidDampedHarmonicMotion.smali'
CLASS_FALLBACK_NAMES = ['AndroidDampedHarmonicMotion.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/motion/DampedHarmonicMotion;', '.implements Lmiuix/animation/motion/AndroidMotion;']

PATCHES = [
    {
        'id': 'miuix_animation_motion_AndroidDampedHarmonicMotion__onInitialVChanged',
        'method': '.method protected onInitialVChanged()V',
        'method_name': 'onInitialVChanged',
        'method_anchors': ['invoke-super {p0}, Lmiuix/animation/motion/DampedHarmonicMotion;->onInitialVChanged()V', 'iput-wide v0, p0, Lmiuix/animation/motion/AndroidDampedHarmonicMotion;->finishTime:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onInitialVChanged()V
    .registers 3

    invoke-super {p0}, Lmiuix/animation/motion/DampedHarmonicMotion;->onInitialVChanged()V

    const-wide/high16 v0, 0x7ff8000000000000L

    iput-wide v0, p0, Lmiuix/animation/motion/AndroidDampedHarmonicMotion;->finishTime:D

    return-void
.end method""",
        'replacement': """.method protected onInitialVChanged()V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    const-wide/high16 v0, 0x7ff8000000000000L

    goto :goto_2

    nop

    :goto_1
    invoke-super {p0}, Lmiuix/animation/motion/DampedHarmonicMotion;->onInitialVChanged()V

    goto :goto_0

    nop

    :goto_2
    iput-wide v0, p0, Lmiuix/animation/motion/AndroidDampedHarmonicMotion;->finishTime:D

    goto :goto_3

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_motion_AndroidDampedHarmonicMotion__onInitialXChanged',
        'method': '.method protected onInitialXChanged()V',
        'method_name': 'onInitialXChanged',
        'method_anchors': ['invoke-super {p0}, Lmiuix/animation/motion/DampedHarmonicMotion;->onInitialXChanged()V', 'iput-wide v0, p0, Lmiuix/animation/motion/AndroidDampedHarmonicMotion;->finishTime:D', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onInitialXChanged()V
    .registers 3

    invoke-super {p0}, Lmiuix/animation/motion/DampedHarmonicMotion;->onInitialXChanged()V

    const-wide/high16 v0, 0x7ff8000000000000L

    iput-wide v0, p0, Lmiuix/animation/motion/AndroidDampedHarmonicMotion;->finishTime:D

    return-void
.end method""",
        'replacement': """.method protected onInitialXChanged()V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Lmiuix/animation/motion/DampedHarmonicMotion;->onInitialXChanged()V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    const-wide/high16 v0, 0x7ff8000000000000L

    goto :goto_3

    nop

    :goto_3
    iput-wide v0, p0, Lmiuix/animation/motion/AndroidDampedHarmonicMotion;->finishTime:D

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
