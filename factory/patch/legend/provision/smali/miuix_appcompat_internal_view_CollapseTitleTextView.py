TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/CollapseTitleTextView.smali'
CLASS_FALLBACK_NAMES = ['CollapseTitleTextView.smali']
CLASS_ANCHORS = ['.super Landroidx/appcompat/widget/AppCompatTextView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_CollapseTitleTextView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mSmallTextSizeEnabled:Z', 'if-eqz v0, :cond_1', 'iget v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mOriginalTextSize:F', 'iget v1, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mSmallTextSize:F', 'if-lez v1, :cond_1', 'invoke-virtual {p0, v1, v0}, Landroidx/appcompat/widget/AppCompatTextView;->setTextSize(IF)V', 'invoke-super {p0, p1, p2}, Landroidx/appcompat/widget/AppCompatTextView;->onMeasure(II)V', 'invoke-direct {p0}, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->isTextEllipsis()Z'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 5

    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mSmallTextSizeEnabled:Z

    if-eqz v0, :cond_1

    iget v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mOriginalTextSize:F

    iget v1, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mSmallTextSize:F

    cmpl-float v1, v0, v1

    if-lez v1, :cond_1

    const/4 v1, 0x0

    invoke-virtual {p0, v1, v0}, Landroidx/appcompat/widget/AppCompatTextView;->setTextSize(IF)V

    invoke-super {p0, p1, p2}, Landroidx/appcompat/widget/AppCompatTextView;->onMeasure(II)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->isTextEllipsis()Z

    move-result v0

    if-eqz v0, :cond_0

    iget v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mSmallTextSize:F

    invoke-virtual {p0, v1, v0}, Landroidx/appcompat/widget/AppCompatTextView;->setTextSize(IF)V

    invoke-super {p0, p1, p2}, Landroidx/appcompat/widget/AppCompatTextView;->onMeasure(II)V

    :cond_0
    return-void

    :cond_1
    invoke-super {p0, p1, p2}, Landroidx/appcompat/widget/AppCompatTextView;->onMeasure(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    invoke-direct {p0}, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->isTextEllipsis()Z

    move-result v0

    goto :goto_9

    nop

    :goto_1
    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mSmallTextSizeEnabled:Z

    goto :goto_10

    nop

    :goto_2
    const/4 v1, 0x0

    goto :goto_11

    nop

    :goto_3
    invoke-virtual {p0, v1, v0}, Landroidx/appcompat/widget/AppCompatTextView;->setTextSize(IF)V

    goto :goto_d

    nop

    :goto_4
    if-gtz v1, :cond_0

    goto :goto_c

    :cond_0
    goto :goto_2

    nop

    :goto_5
    iget v1, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mSmallTextSize:F

    goto :goto_f

    nop

    :goto_6
    invoke-super {p0, p1, p2}, Landroidx/appcompat/widget/AppCompatTextView;->onMeasure(II)V

    goto :goto_7

    nop

    :goto_7
    return-void

    :goto_8
    iget v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mSmallTextSize:F

    goto :goto_3

    nop

    :goto_9
    if-nez v0, :cond_1

    goto :goto_e

    :cond_1
    goto :goto_8

    nop

    :goto_a
    iget v0, p0, Lmiuix/appcompat/internal/view/CollapseTitleTextView;->mOriginalTextSize:F

    goto :goto_5

    nop

    :goto_b
    return-void

    :goto_c
    goto :goto_6

    nop

    :goto_d
    invoke-super {p0, p1, p2}, Landroidx/appcompat/widget/AppCompatTextView;->onMeasure(II)V

    :goto_e
    goto :goto_b

    nop

    :goto_f
    cmpl-float v1, v0, v1

    goto :goto_4

    nop

    :goto_10
    if-nez v0, :cond_2

    goto :goto_c

    :cond_2
    goto :goto_a

    nop

    :goto_11
    invoke-virtual {p0, v1, v0}, Landroidx/appcompat/widget/AppCompatTextView;->setTextSize(IF)V

    goto :goto_12

    nop

    :goto_12
    invoke-super {p0, p1, p2}, Landroidx/appcompat/widget/AppCompatTextView;->onMeasure(II)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
