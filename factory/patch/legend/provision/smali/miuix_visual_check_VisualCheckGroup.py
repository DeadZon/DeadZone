TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/visual/check/VisualCheckGroup.smali'
CLASS_FALLBACK_NAMES = ['VisualCheckGroup.smali']
CLASS_ANCHORS = ['.super Lmiuix/visual/check/FlowLayout;']

PATCHES = [
    {
        'id': 'miuix_visual_check_VisualCheckGroup__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V', 'iget v0, p0, Lmiuix/visual/check/VisualCheckGroup;->mCheckedId:I', 'if-eq v0, v1, :cond_0', 'iput-boolean v1, p0, Lmiuix/visual/check/VisualCheckGroup;->mProtectFromCheckedChange:Z', 'invoke-direct {p0, v0, v1}, Lmiuix/visual/check/VisualCheckGroup;->setCheckedStateForView(IZ)V', 'iput-boolean v0, p0, Lmiuix/visual/check/VisualCheckGroup;->mProtectFromCheckedChange:Z', 'iget v0, p0, Lmiuix/visual/check/VisualCheckGroup;->mCheckedId:I', 'invoke-direct {p0, v0}, Lmiuix/visual/check/VisualCheckGroup;->setCheckedId(I)V'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 3

    invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V

    iget v0, p0, Lmiuix/visual/check/VisualCheckGroup;->mCheckedId:I

    const/4 v1, -0x1

    if-eq v0, v1, :cond_0

    const/4 v1, 0x1

    iput-boolean v1, p0, Lmiuix/visual/check/VisualCheckGroup;->mProtectFromCheckedChange:Z

    invoke-direct {p0, v0, v1}, Lmiuix/visual/check/VisualCheckGroup;->setCheckedStateForView(IZ)V

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/visual/check/VisualCheckGroup;->mProtectFromCheckedChange:Z

    iget v0, p0, Lmiuix/visual/check/VisualCheckGroup;->mCheckedId:I

    invoke-direct {p0, v0}, Lmiuix/visual/check/VisualCheckGroup;->setCheckedId(I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 3

    goto :goto_c

    nop

    :goto_0
    const/4 v1, -0x1

    goto :goto_4

    nop

    :goto_1
    invoke-direct {p0, v0}, Lmiuix/visual/check/VisualCheckGroup;->setCheckedId(I)V

    :goto_2
    goto :goto_9

    nop

    :goto_3
    iput-boolean v0, p0, Lmiuix/visual/check/VisualCheckGroup;->mProtectFromCheckedChange:Z

    goto :goto_8

    nop

    :goto_4
    if-ne v0, v1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_b

    nop

    :goto_5
    iput-boolean v1, p0, Lmiuix/visual/check/VisualCheckGroup;->mProtectFromCheckedChange:Z

    goto :goto_a

    nop

    :goto_6
    const/4 v0, 0x0

    goto :goto_3

    nop

    :goto_7
    iget v0, p0, Lmiuix/visual/check/VisualCheckGroup;->mCheckedId:I

    goto :goto_0

    nop

    :goto_8
    iget v0, p0, Lmiuix/visual/check/VisualCheckGroup;->mCheckedId:I

    goto :goto_1

    nop

    :goto_9
    return-void

    :goto_a
    invoke-direct {p0, v0, v1}, Lmiuix/visual/check/VisualCheckGroup;->setCheckedStateForView(IZ)V

    goto :goto_6

    nop

    :goto_b
    const/4 v1, 0x1

    goto :goto_5

    nop

    :goto_c
    invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
