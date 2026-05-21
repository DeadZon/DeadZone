TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/CollapseTitleColorTransitionTextView.smali'
CLASS_FALLBACK_NAMES = ['CollapseTitleColorTransitionTextView.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/view/ColorTransitionTextView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_CollapseTitleColorTransitionTextView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mSmallTextSizeEnabled:Z', 'if-eqz v0, :cond_1', 'iget v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mOriginalTextSize:F', 'iget v1, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mSmallTextSize:F', 'if-lez v1, :cond_1', 'invoke-virtual {p0, v1, v0}, Landroid/widget/TextView;->setTextSize(IF)V', 'invoke-super {p0, p1, p2}, Landroid/widget/TextView;->onMeasure(II)V', 'invoke-direct {p0}, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->isTextEllipsis()Z'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 5

    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mSmallTextSizeEnabled:Z

    if-eqz v0, :cond_1

    iget v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mOriginalTextSize:F

    iget v1, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mSmallTextSize:F

    cmpl-float v1, v0, v1

    if-lez v1, :cond_1

    const/4 v1, 0x0

    invoke-virtual {p0, v1, v0}, Landroid/widget/TextView;->setTextSize(IF)V

    invoke-super {p0, p1, p2}, Landroid/widget/TextView;->onMeasure(II)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->isTextEllipsis()Z

    move-result v0

    if-eqz v0, :cond_0

    iget v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mSmallTextSize:F

    invoke-virtual {p0, v1, v0}, Landroid/widget/TextView;->setTextSize(IF)V

    invoke-super {p0, p1, p2}, Landroid/widget/TextView;->onMeasure(II)V

    :cond_0
    return-void

    :cond_1
    invoke-super {p0, p1, p2}, Landroid/widget/TextView;->onMeasure(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 5

    goto :goto_b

    nop

    :goto_0
    invoke-super {p0, p1, p2}, Landroid/widget/TextView;->onMeasure(II)V

    :goto_1
    goto :goto_5

    nop

    :goto_2
    return-void

    :goto_3
    invoke-super {p0, p1, p2}, Landroid/widget/TextView;->onMeasure(II)V

    goto :goto_2

    nop

    :goto_4
    iget v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mOriginalTextSize:F

    goto :goto_8

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_3

    nop

    :goto_7
    invoke-virtual {p0, v1, v0}, Landroid/widget/TextView;->setTextSize(IF)V

    goto :goto_10

    nop

    :goto_8
    iget v1, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mSmallTextSize:F

    goto :goto_f

    nop

    :goto_9
    if-gtz v1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_e

    nop

    :goto_a
    if-nez v0, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_4

    nop

    :goto_b
    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mSmallTextSizeEnabled:Z

    goto :goto_a

    nop

    :goto_c
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->isTextEllipsis()Z

    move-result v0

    goto :goto_d

    nop

    :goto_d
    if-nez v0, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_12

    nop

    :goto_e
    const/4 v1, 0x0

    goto :goto_7

    nop

    :goto_f
    cmpl-float v1, v0, v1

    goto :goto_9

    nop

    :goto_10
    invoke-super {p0, p1, p2}, Landroid/widget/TextView;->onMeasure(II)V

    goto :goto_c

    nop

    :goto_11
    invoke-virtual {p0, v1, v0}, Landroid/widget/TextView;->setTextSize(IF)V

    goto :goto_0

    nop

    :goto_12
    iget v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleColorTransitionTextView;->mSmallTextSize:F

    goto :goto_11

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
