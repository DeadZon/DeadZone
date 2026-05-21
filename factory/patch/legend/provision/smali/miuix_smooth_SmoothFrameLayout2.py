TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/smooth/SmoothFrameLayout2.smali'
CLASS_FALLBACK_NAMES = ['SmoothFrameLayout2.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_smooth_SmoothFrameLayout2__dispatchDraw',
        'method': '.method protected dispatchDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'dispatchDraw',
        'method_anchors': ['invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I', 'iget-boolean v1, p0, Lmiuix/smooth/SmoothFrameLayout2;->mClip:Z', 'if-nez v1, :cond_0', 'invoke-direct {p0, p1}, Lmiuix/smooth/SmoothFrameLayout2;->clipRoundRect(Landroid/graphics/Canvas;)V', 'iget v1, p0, Lmiuix/smooth/SmoothFrameLayout2;->mStrokeWidth:I', 'if-lez v1, :cond_1', 'invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I', 'invoke-direct {p0, p1}, Lmiuix/smooth/SmoothFrameLayout2;->clipInnerRoundRect(Landroid/graphics/Canvas;)V'],
        'type': 'method_replace',
        'search': """.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 4

    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    move-result v0

    iget-boolean v1, p0, Lmiuix/smooth/SmoothFrameLayout2;->mClip:Z

    if-nez v1, :cond_0

    invoke-direct {p0, p1}, Lmiuix/smooth/SmoothFrameLayout2;->clipRoundRect(Landroid/graphics/Canvas;)V

    :cond_0
    iget v1, p0, Lmiuix/smooth/SmoothFrameLayout2;->mStrokeWidth:I

    if-lez v1, :cond_1

    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    move-result v1

    invoke-direct {p0, p1}, Lmiuix/smooth/SmoothFrameLayout2;->clipInnerRoundRect(Landroid/graphics/Canvas;)V

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    invoke-virtual {p1, v1}, Landroid/graphics/Canvas;->restoreToCount(I)V

    goto :goto_0

    :cond_1
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    :goto_0
    iget-boolean v1, p0, Lmiuix/smooth/SmoothFrameLayout2;->mClip:Z

    if-nez v1, :cond_2

    iget v1, p0, Lmiuix/smooth/SmoothFrameLayout2;->mStrokeWidth:I

    if-lez v1, :cond_2

    invoke-direct {p0, p1}, Lmiuix/smooth/SmoothFrameLayout2;->drawRoundRectStroke(Landroid/graphics/Canvas;)V

    :cond_2
    invoke-virtual {p1, v0}, Landroid/graphics/Canvas;->restoreToCount(I)V

    return-void
.end method""",
        'replacement': """.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 4

    goto :goto_13

    nop

    :goto_0
    invoke-direct {p0, p1}, Lmiuix/smooth/SmoothFrameLayout2;->clipInnerRoundRect(Landroid/graphics/Canvas;)V

    goto :goto_7

    nop

    :goto_1
    invoke-direct {p0, p1}, Lmiuix/smooth/SmoothFrameLayout2;->drawRoundRectStroke(Landroid/graphics/Canvas;)V

    :goto_2
    goto :goto_12

    nop

    :goto_3
    goto :goto_10

    :goto_4
    goto :goto_f

    nop

    :goto_5
    iget v1, p0, Lmiuix/smooth/SmoothFrameLayout2;->mStrokeWidth:I

    goto :goto_15

    nop

    :goto_6
    return-void

    :goto_7
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    goto :goto_16

    nop

    :goto_8
    iget v1, p0, Lmiuix/smooth/SmoothFrameLayout2;->mStrokeWidth:I

    goto :goto_14

    nop

    :goto_9
    iget-boolean v1, p0, Lmiuix/smooth/SmoothFrameLayout2;->mClip:Z

    goto :goto_11

    nop

    :goto_a
    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    move-result v1

    goto :goto_0

    nop

    :goto_b
    invoke-direct {p0, p1}, Lmiuix/smooth/SmoothFrameLayout2;->clipRoundRect(Landroid/graphics/Canvas;)V

    :goto_c
    goto :goto_5

    nop

    :goto_d
    iget-boolean v1, p0, Lmiuix/smooth/SmoothFrameLayout2;->mClip:Z

    goto :goto_e

    nop

    :goto_e
    if-eqz v1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_8

    nop

    :goto_f
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    :goto_10
    goto :goto_d

    nop

    :goto_11
    if-eqz v1, :cond_1

    goto :goto_c

    :cond_1
    goto :goto_b

    nop

    :goto_12
    invoke-virtual {p1, v0}, Landroid/graphics/Canvas;->restoreToCount(I)V

    goto :goto_6

    nop

    :goto_13
    invoke-virtual {p1}, Landroid/graphics/Canvas;->save()I

    move-result v0

    goto :goto_9

    nop

    :goto_14
    if-gtz v1, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_1

    nop

    :goto_15
    if-gtz v1, :cond_3

    goto :goto_4

    :cond_3
    goto :goto_a

    nop

    :goto_16
    invoke-virtual {p1, v1}, Landroid/graphics/Canvas;->restoreToCount(I)V

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_smooth_SmoothFrameLayout2__onSizeChanged',
        'method': '.method protected onSizeChanged(IIII)V',
        'method_name': 'onSizeChanged',
        'method_anchors': ['invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onSizeChanged(IIII)V', 'iget-object p0, p0, Lmiuix/smooth/SmoothFrameLayout2;->mLayer:Landroid/graphics/RectF;', 'invoke-virtual {p0, p3, p3, p1, p2}, Landroid/graphics/RectF;->set(FFFF)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onSizeChanged(IIII)V
    .registers 5

    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onSizeChanged(IIII)V

    iget-object p0, p0, Lmiuix/smooth/SmoothFrameLayout2;->mLayer:Landroid/graphics/RectF;

    int-to-float p1, p1

    int-to-float p2, p2

    const/4 p3, 0x0

    invoke-virtual {p0, p3, p3, p1, p2}, Landroid/graphics/RectF;->set(FFFF)V

    return-void
.end method""",
        'replacement': """.method protected onSizeChanged(IIII)V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0, p3, p3, p1, p2}, Landroid/graphics/RectF;->set(FFFF)V

    goto :goto_5

    nop

    :goto_1
    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onSizeChanged(IIII)V

    goto :goto_4

    nop

    :goto_2
    int-to-float p2, p2

    goto :goto_3

    nop

    :goto_3
    const/4 p3, 0x0

    goto :goto_0

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/smooth/SmoothFrameLayout2;->mLayer:Landroid/graphics/RectF;

    goto :goto_6

    nop

    :goto_5
    return-void

    :goto_6
    int-to-float p1, p1

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
