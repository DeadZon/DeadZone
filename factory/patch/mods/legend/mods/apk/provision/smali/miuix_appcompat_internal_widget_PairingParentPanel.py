TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/widget/PairingParentPanel.smali'
CLASS_FALLBACK_NAMES = ['PairingParentPanel.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_widget_PairingParentPanel__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'sget v0, Lmiuix/appcompat/R$id;->pairingClosable:I', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Landroidx/appcompat/widget/AppCompatImageView;', 'iput-object v0, p0, Lmiuix/appcompat/internal/widget/PairingParentPanel;->mClosableIcon:Landroidx/appcompat/widget/AppCompatImageView;', 'sget v0, Lmiuix/appcompat/R$id;->pairingScrollView:I', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Lmiuix/core/widget/NestedScrollView;'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    sget v0, Lmiuix/appcompat/R$id;->pairingClosable:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroidx/appcompat/widget/AppCompatImageView;

    iput-object v0, p0, Lmiuix/appcompat/internal/widget/PairingParentPanel;->mClosableIcon:Landroidx/appcompat/widget/AppCompatImageView;

    sget v0, Lmiuix/appcompat/R$id;->pairingScrollView:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/core/widget/NestedScrollView;

    iput-object v0, p0, Lmiuix/appcompat/internal/widget/PairingParentPanel;->mPairingScrollView:Lmiuix/core/widget/NestedScrollView;

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_8

    nop

    :goto_1
    sget v0, Lmiuix/appcompat/R$id;->pairingScrollView:I

    goto :goto_9

    nop

    :goto_2
    check-cast v0, Lmiuix/core/widget/NestedScrollView;

    goto :goto_6

    nop

    :goto_3
    iput-object v0, p0, Lmiuix/appcompat/internal/widget/PairingParentPanel;->mClosableIcon:Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_1

    nop

    :goto_4
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto :goto_5

    nop

    :goto_5
    sget v0, Lmiuix/appcompat/R$id;->pairingClosable:I

    goto :goto_0

    nop

    :goto_6
    iput-object v0, p0, Lmiuix/appcompat/internal/widget/PairingParentPanel;->mPairingScrollView:Lmiuix/core/widget/NestedScrollView;

    goto :goto_7

    nop

    :goto_7
    return-void

    :goto_8
    check-cast v0, Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_3

    nop

    :goto_9
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_PairingParentPanel__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V', 'invoke-direct {p0}, Lmiuix/appcompat/internal/widget/PairingParentPanel;->layoutClosableIcon()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/widget/PairingParentPanel;->layoutClosableIcon()V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_0

    nop

    :goto_0
    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-direct {p0}, Lmiuix/appcompat/internal/widget/PairingParentPanel;->layoutClosableIcon()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_PairingParentPanel__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V', 'invoke-direct {p0}, Lmiuix/appcompat/internal/widget/PairingParentPanel;->applyCustomViewLayoutVerticalCenterIfNeeded()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 3

    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/widget/PairingParentPanel;->applyCustomViewLayoutVerticalCenterIfNeeded()V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    goto :goto_2

    nop

    :goto_2
    invoke-direct {p0}, Lmiuix/appcompat/internal/widget/PairingParentPanel;->applyCustomViewLayoutVerticalCenterIfNeeded()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
