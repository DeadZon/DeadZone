TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/widget/ActionSheetRootView.smali'
CLASS_FALLBACK_NAMES = ['ActionSheetRootView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_internal_widget_ActionSheetRootView__onAttachedToWindow',
        'method': '.method protected onAttachedToWindow()V',
        'method_name': 'onAttachedToWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V', 'new-instance v0, Lmiuix/internal/widget/ActionSheetRootView$1;', 'invoke-direct {v0, p0}, Lmiuix/internal/widget/ActionSheetRootView$1;-><init>(Lmiuix/internal/widget/ActionSheetRootView;)V', 'iput-object v0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mGlobalLayoutListener:Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;', 'iget-object v0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mContentController:Lmiuix/internal/widget/ActionSheet$ContentController;', 'if-eqz v0, :cond_0', 'invoke-interface {v0}, Lmiuix/internal/widget/ActionSheet$ContentController;->getArrowAnchor()Landroid/view/View;', 'if-eqz v0, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onAttachedToWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V

    new-instance v0, Lmiuix/internal/widget/ActionSheetRootView$1;

    invoke-direct {v0, p0}, Lmiuix/internal/widget/ActionSheetRootView$1;-><init>(Lmiuix/internal/widget/ActionSheetRootView;)V

    iput-object v0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mGlobalLayoutListener:Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;

    iget-object v0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mContentController:Lmiuix/internal/widget/ActionSheet$ContentController;

    if-eqz v0, :cond_0

    invoke-interface {v0}, Lmiuix/internal/widget/ActionSheet$ContentController;->getArrowAnchor()Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Landroid/view/View;->getViewTreeObserver()Landroid/view/ViewTreeObserver;

    move-result-object v0

    iget-object p0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mGlobalLayoutListener:Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;

    invoke-virtual {v0, p0}, Landroid/view/ViewTreeObserver;->addOnGlobalLayoutListener(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onAttachedToWindow()V
    .registers 2

    goto :goto_8

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mGlobalLayoutListener:Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;

    goto :goto_6

    nop

    :goto_1
    iput-object v0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mGlobalLayoutListener:Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;

    goto :goto_9

    nop

    :goto_2
    invoke-direct {v0, p0}, Lmiuix/internal/widget/ActionSheetRootView$1;-><init>(Lmiuix/internal/widget/ActionSheetRootView;)V

    goto :goto_1

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_5

    nop

    :goto_4
    new-instance v0, Lmiuix/internal/widget/ActionSheetRootView$1;

    goto :goto_2

    nop

    :goto_5
    invoke-virtual {v0}, Landroid/view/View;->getViewTreeObserver()Landroid/view/ViewTreeObserver;

    move-result-object v0

    goto :goto_0

    nop

    :goto_6
    invoke-virtual {v0, p0}, Landroid/view/ViewTreeObserver;->addOnGlobalLayoutListener(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V

    :goto_7
    goto :goto_a

    nop

    :goto_8
    invoke-super {p0}, Landroid/widget/FrameLayout;->onAttachedToWindow()V

    goto :goto_4

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mContentController:Lmiuix/internal/widget/ActionSheet$ContentController;

    goto :goto_b

    nop

    :goto_a
    return-void

    :goto_b
    if-nez v0, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_c

    nop

    :goto_c
    invoke-interface {v0}, Lmiuix/internal/widget/ActionSheet$ContentController;->getArrowAnchor()Landroid/view/View;

    move-result-object v0

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ActionSheetRootView__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V', 'iget-object v0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mContentController:Lmiuix/internal/widget/ActionSheet$ContentController;', 'if-eqz v0, :cond_0', 'invoke-interface {v0}, Lmiuix/internal/widget/ActionSheet$ContentController;->getArrowAnchor()Landroid/view/View;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Landroid/view/View;->getViewTreeObserver()Landroid/view/ViewTreeObserver;', 'iget-object p0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mGlobalLayoutListener:Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;', 'invoke-virtual {v0, p0}, Landroid/view/ViewTreeObserver;->removeOnGlobalLayoutListener(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    iget-object v0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mContentController:Lmiuix/internal/widget/ActionSheet$ContentController;

    if-eqz v0, :cond_0

    invoke-interface {v0}, Lmiuix/internal/widget/ActionSheet$ContentController;->getArrowAnchor()Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Landroid/view/View;->getViewTreeObserver()Landroid/view/ViewTreeObserver;

    move-result-object v0

    iget-object p0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mGlobalLayoutListener:Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;

    invoke-virtual {v0, p0}, Landroid/view/ViewTreeObserver;->removeOnGlobalLayoutListener(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {v0, p0}, Landroid/view/ViewTreeObserver;->removeOnGlobalLayoutListener(Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;)V

    :goto_1
    goto :goto_8

    nop

    :goto_2
    invoke-interface {v0}, Lmiuix/internal/widget/ActionSheet$ContentController;->getArrowAnchor()Landroid/view/View;

    move-result-object v0

    goto :goto_4

    nop

    :goto_3
    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    goto :goto_5

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_9

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mContentController:Lmiuix/internal/widget/ActionSheet$ContentController;

    goto :goto_6

    nop

    :goto_6
    if-nez v0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_2

    nop

    :goto_7
    iget-object p0, p0, Lmiuix/internal/widget/ActionSheetRootView;->mGlobalLayoutListener:Landroid/view/ViewTreeObserver$OnGlobalLayoutListener;

    goto :goto_0

    nop

    :goto_8
    return-void

    :goto_9
    invoke-virtual {v0}, Landroid/view/View;->getViewTreeObserver()Landroid/view/ViewTreeObserver;

    move-result-object v0

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ActionSheetRootView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V', 'invoke-direct {p0}, Lmiuix/internal/widget/ActionSheetRootView;->layoutContentPanel()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    invoke-direct {p0}, Lmiuix/internal/widget/ActionSheetRootView;->layoutContentPanel()V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_0

    nop

    :goto_0
    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    goto :goto_1

    nop

    :goto_1
    invoke-direct {p0}, Lmiuix/internal/widget/ActionSheetRootView;->layoutContentPanel()V

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ActionSheetRootView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-direct {p0}, Lmiuix/internal/widget/ActionSheetRootView;->beforeOnMeasure()V', 'invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 3

    invoke-direct {p0}, Lmiuix/internal/widget/ActionSheetRootView;->beforeOnMeasure()V

    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-direct {p0}, Lmiuix/internal/widget/ActionSheetRootView;->beforeOnMeasure()V

    goto :goto_1

    nop

    :goto_1
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
