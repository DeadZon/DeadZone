TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/motion/MergeMotion.smali'
CLASS_FALLBACK_NAMES = ['MergeMotion.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/motion/BaseMotion;', '.implements Lmiuix/animation/motion/Motion;']

PATCHES = [
    {
        'id': 'miuix_animation_motion_MergeMotion__onInitialVChanged',
        'method': '.method protected onInitialVChanged()V',
        'method_name': 'onInitialVChanged',
        'method_anchors': ['invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialVChanged()V', 'iput-object v0, p0, Lmiuix/animation/motion/MergeMotion;->function:Lmiuix/animation/function/DifferentiableImpl;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onInitialVChanged()V
    .registers 2

    invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialVChanged()V

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/animation/motion/MergeMotion;->function:Lmiuix/animation/function/DifferentiableImpl;

    return-void
.end method""",
        'replacement': """.method protected onInitialVChanged()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialVChanged()V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    const/4 v0, 0x0

    goto :goto_3

    nop

    :goto_3
    iput-object v0, p0, Lmiuix/animation/motion/MergeMotion;->function:Lmiuix/animation/function/DifferentiableImpl;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_animation_motion_MergeMotion__onInitialXChanged',
        'method': '.method protected onInitialXChanged()V',
        'method_name': 'onInitialXChanged',
        'method_anchors': ['invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialXChanged()V', 'iput-object v0, p0, Lmiuix/animation/motion/MergeMotion;->function:Lmiuix/animation/function/DifferentiableImpl;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onInitialXChanged()V
    .registers 2

    invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialXChanged()V

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/animation/motion/MergeMotion;->function:Lmiuix/animation/function/DifferentiableImpl;

    return-void
.end method""",
        'replacement': """.method protected onInitialXChanged()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialXChanged()V

    goto :goto_2

    nop

    :goto_2
    const/4 v0, 0x0

    goto :goto_3

    nop

    :goto_3
    iput-object v0, p0, Lmiuix/animation/motion/MergeMotion;->function:Lmiuix/animation/function/DifferentiableImpl;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
