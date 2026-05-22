TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/motion/PerlinMotion.smali'
CLASS_FALLBACK_NAMES = ['PerlinMotion.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/motion/BaseMotion;', '.field public static final INTERPOLATOR:Lmiuix/animation/function/Differentiable;', '.field public static final INTERPOLATOR2:Lmiuix/animation/function/Differentiable;']

PATCHES = [
    {
        'id': 'miuix_animation_motion_PerlinMotion__onInitialXChanged',
        'method': '.method protected onInitialXChanged()V',
        'method_name': 'onInitialXChanged',
        'method_anchors': ['invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialXChanged()V', 'iput-object v0, p0, Lmiuix/animation/motion/PerlinMotion;->function:Lmiuix/animation/function/Differentiable;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onInitialXChanged()V
    .registers 2

    invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialXChanged()V

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/animation/motion/PerlinMotion;->function:Lmiuix/animation/function/Differentiable;

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
    iput-object v0, p0, Lmiuix/animation/motion/PerlinMotion;->function:Lmiuix/animation/function/Differentiable;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
