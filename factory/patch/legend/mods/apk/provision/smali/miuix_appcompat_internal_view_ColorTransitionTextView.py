TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/ColorTransitionTextView.smali'
CLASS_FALLBACK_NAMES = ['ColorTransitionTextView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/TextView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_ColorTransitionTextView__onDraw',
        'method': '.method protected onDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'onDraw',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/view/ColorTransitionTextView;->hasTransitedColor:Z', 'if-eqz v0, :cond_1', 'iget-object v0, p0, Lmiuix/appcompat/internal/view/ColorTransitionTextView;->mAnimator:Landroid/animation/ValueAnimator;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0}, Landroid/animation/ValueAnimator;->isRunning()Z', 'if-nez v0, :cond_0', 'iget v0, p0, Lmiuix/appcompat/internal/view/ColorTransitionTextView;->mAnimateColor:I', 'invoke-virtual {p0, v0}, Landroid/widget/TextView;->setTextColor(I)V'],
        'type': 'method_replace',
        'search': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 3

    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/ColorTransitionTextView;->hasTransitedColor:Z

    if-eqz v0, :cond_1

    iget-object v0, p0, Lmiuix/appcompat/internal/view/ColorTransitionTextView;->mAnimator:Landroid/animation/ValueAnimator;

    if-eqz v0, :cond_1

    invoke-virtual {v0}, Landroid/animation/ValueAnimator;->isRunning()Z

    move-result v0

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    iget v0, p0, Lmiuix/appcompat/internal/view/ColorTransitionTextView;->mAnimateColor:I

    invoke-virtual {p0, v0}, Landroid/widget/TextView;->setTextColor(I)V

    invoke-super {p0, p1}, Landroid/widget/TextView;->onDraw(Landroid/graphics/Canvas;)V

    return-void

    :cond_1
    :goto_0
    invoke-super {p0, p1}, Landroid/widget/TextView;->onDraw(Landroid/graphics/Canvas;)V

    return-void
.end method""",
        'replacement': """.method protected onDraw(Landroid/graphics/Canvas;)V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    goto :goto_d

    :goto_1
    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    iget v0, p0, Lmiuix/appcompat/internal/view/ColorTransitionTextView;->mAnimateColor:I

    goto :goto_e

    nop

    :goto_4
    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/ColorTransitionTextView;->hasTransitedColor:Z

    goto :goto_a

    nop

    :goto_5
    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/appcompat/internal/view/ColorTransitionTextView;->mAnimator:Landroid/animation/ValueAnimator;

    goto :goto_b

    nop

    :goto_7
    invoke-super {p0, p1}, Landroid/widget/TextView;->onDraw(Landroid/graphics/Canvas;)V

    goto :goto_c

    nop

    :goto_8
    invoke-virtual {v0}, Landroid/animation/ValueAnimator;->isRunning()Z

    move-result v0

    goto :goto_5

    nop

    :goto_9
    invoke-super {p0, p1}, Landroid/widget/TextView;->onDraw(Landroid/graphics/Canvas;)V

    goto :goto_2

    nop

    :goto_a
    if-nez v0, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_6

    nop

    :goto_b
    if-nez v0, :cond_2

    goto :goto_d

    :cond_2
    goto :goto_8

    nop

    :goto_c
    return-void

    :goto_d
    goto :goto_9

    nop

    :goto_e
    invoke-virtual {p0, v0}, Landroid/widget/TextView;->setTextColor(I)V

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
