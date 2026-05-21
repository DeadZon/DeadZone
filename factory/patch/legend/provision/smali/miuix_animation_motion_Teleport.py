TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/animation/motion/Teleport.smali'
CLASS_FALLBACK_NAMES = ['Teleport.smali']
CLASS_ANCHORS = ['.super Lmiuix/animation/motion/InstantMotion;', '.implements Lmiuix/animation/motion/Motion;', '.field public static final MODE_ABSOLUTE:I = 0x0', '.field public static final MODE_RELATIVE:I = 0x1']

PATCHES = [
    {
        'id': 'miuix_animation_motion_Teleport__onInitialXChanged',
        'method': '.method protected onInitialXChanged()V',
        'method_name': 'onInitialXChanged',
        'method_anchors': ['invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialXChanged()V', 'iget v0, p0, Lmiuix/animation/motion/Teleport;->mode:I', 'if-ne v0, v1, :cond_0', 'iput-object v0, p0, Lmiuix/animation/motion/Teleport;->function:Lmiuix/animation/function/Differentiable;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onInitialXChanged()V
    .registers 3

    invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialXChanged()V

    iget v0, p0, Lmiuix/animation/motion/Teleport;->mode:I

    const/4 v1, 0x1

    if-ne v0, v1, :cond_0

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/animation/motion/Teleport;->function:Lmiuix/animation/function/Differentiable;

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onInitialXChanged()V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    const/4 v1, 0x1

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    if-eq v0, v1, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_4

    nop

    :goto_3
    iget v0, p0, Lmiuix/animation/motion/Teleport;->mode:I

    goto :goto_0

    nop

    :goto_4
    const/4 v0, 0x0

    goto :goto_6

    nop

    :goto_5
    invoke-super {p0}, Lmiuix/animation/motion/BaseMotion;->onInitialXChanged()V

    goto :goto_3

    nop

    :goto_6
    iput-object v0, p0, Lmiuix/animation/motion/Teleport;->function:Lmiuix/animation/function/Differentiable;

    :goto_7
    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
