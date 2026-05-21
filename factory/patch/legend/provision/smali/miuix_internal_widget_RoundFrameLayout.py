TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/widget/RoundFrameLayout.smali'
CLASS_FALLBACK_NAMES = ['RoundFrameLayout.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_internal_widget_RoundFrameLayout__dispatchDraw',
        'method': '.method protected dispatchDraw(Landroid/graphics/Canvas;)V',
        'method_name': 'dispatchDraw',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/internal/widget/RoundFrameLayout;->onClipDraw(Landroid/graphics/Canvas;)V', 'invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V', 'invoke-direct {p0, p1}, Lmiuix/internal/widget/RoundFrameLayout;->onBorderDraw(Landroid/graphics/Canvas;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 2

    invoke-virtual {p0, p1}, Lmiuix/internal/widget/RoundFrameLayout;->onClipDraw(Landroid/graphics/Canvas;)V

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    invoke-direct {p0, p1}, Lmiuix/internal/widget/RoundFrameLayout;->onBorderDraw(Landroid/graphics/Canvas;)V

    return-void
.end method""",
        'replacement': """.method protected dispatchDraw(Landroid/graphics/Canvas;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->dispatchDraw(Landroid/graphics/Canvas;)V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-direct {p0, p1}, Lmiuix/internal/widget/RoundFrameLayout;->onBorderDraw(Landroid/graphics/Canvas;)V

    goto :goto_1

    nop

    :goto_3
    invoke-virtual {p0, p1}, Lmiuix/internal/widget/RoundFrameLayout;->onClipDraw(Landroid/graphics/Canvas;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_RoundFrameLayout__onSizeChanged',
        'method': '.method protected onSizeChanged(IIII)V',
        'method_name': 'onSizeChanged',
        'method_anchors': ['invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onSizeChanged(IIII)V', 'iget-object p3, p0, Lmiuix/internal/widget/RoundFrameLayout;->mLayer:Landroid/graphics/RectF;', 'invoke-virtual {p3, p4, p4, p1, p2}, Landroid/graphics/RectF;->set(FFFF)V', 'invoke-direct {p0}, Lmiuix/internal/widget/RoundFrameLayout;->refreshRegion()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onSizeChanged(IIII)V
    .registers 5

    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onSizeChanged(IIII)V

    iget-object p3, p0, Lmiuix/internal/widget/RoundFrameLayout;->mLayer:Landroid/graphics/RectF;

    int-to-float p1, p1

    int-to-float p2, p2

    const/4 p4, 0x0

    invoke-virtual {p3, p4, p4, p1, p2}, Landroid/graphics/RectF;->set(FFFF)V

    invoke-direct {p0}, Lmiuix/internal/widget/RoundFrameLayout;->refreshRegion()V

    return-void
.end method""",
        'replacement': """.method protected onSizeChanged(IIII)V
    .registers 5

    goto :goto_7

    nop

    :goto_0
    const/4 p4, 0x0

    goto :goto_6

    nop

    :goto_1
    return-void

    :goto_2
    int-to-float p2, p2

    goto :goto_0

    nop

    :goto_3
    int-to-float p1, p1

    goto :goto_2

    nop

    :goto_4
    iget-object p3, p0, Lmiuix/internal/widget/RoundFrameLayout;->mLayer:Landroid/graphics/RectF;

    goto :goto_3

    nop

    :goto_5
    invoke-direct {p0}, Lmiuix/internal/widget/RoundFrameLayout;->refreshRegion()V

    goto :goto_1

    nop

    :goto_6
    invoke-virtual {p3, p4, p4, p1, p2}, Landroid/graphics/RectF;->set(FFFF)V

    goto :goto_5

    nop

    :goto_7
    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/FrameLayout;->onSizeChanged(IIII)V

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
