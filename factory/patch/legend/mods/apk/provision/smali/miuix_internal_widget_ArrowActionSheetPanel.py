TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/widget/ArrowActionSheetPanel.smali'
CLASS_FALLBACK_NAMES = ['ArrowActionSheetPanel.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_internal_widget_ArrowActionSheetPanel__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'sget v0, Lmiuix/appcompat/R$id;->action_sheet_arrow_view:I', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Landroidx/appcompat/widget/AppCompatImageView;', 'iput-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mArrowView:Landroidx/appcompat/widget/AppCompatImageView;', 'sget v0, Lmiuix/appcompat/R$id;->action_sheet_content:I', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Landroid/view/ViewGroup;'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    sget v0, Lmiuix/appcompat/R$id;->action_sheet_arrow_view:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroidx/appcompat/widget/AppCompatImageView;

    iput-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mArrowView:Landroidx/appcompat/widget/AppCompatImageView;

    sget v0, Lmiuix/appcompat/R$id;->action_sheet_content:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    iput-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mContent:Landroid/view/ViewGroup;

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto :goto_6

    nop

    :goto_1
    iput-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mArrowView:Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_8

    nop

    :goto_2
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_7

    nop

    :goto_3
    return-void

    :goto_4
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_2

    nop

    :goto_5
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_9

    nop

    :goto_6
    sget v0, Lmiuix/appcompat/R$id;->action_sheet_arrow_view:I

    goto :goto_5

    nop

    :goto_7
    iput-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mContent:Landroid/view/ViewGroup;

    goto :goto_3

    nop

    :goto_8
    sget v0, Lmiuix/appcompat/R$id;->action_sheet_content:I

    goto :goto_4

    nop

    :goto_9
    check-cast v0, Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheetPanel__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V', 'invoke-direct {p0}, Lmiuix/internal/widget/ArrowActionSheetPanel;->layoutArrowView()Landroid/graphics/Point;', 'invoke-direct {p0, p1}, Lmiuix/internal/widget/ArrowActionSheetPanel;->layoutContentView(Landroid/graphics/Point;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    invoke-direct {p0}, Lmiuix/internal/widget/ArrowActionSheetPanel;->layoutArrowView()Landroid/graphics/Point;

    move-result-object p1

    invoke-direct {p0, p1}, Lmiuix/internal/widget/ArrowActionSheetPanel;->layoutContentView(Landroid/graphics/Point;)V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_2

    nop

    :goto_0
    invoke-direct {p0, p1}, Lmiuix/internal/widget/ArrowActionSheetPanel;->layoutContentView(Landroid/graphics/Point;)V

    goto :goto_3

    nop

    :goto_1
    invoke-direct {p0}, Lmiuix/internal/widget/ArrowActionSheetPanel;->layoutArrowView()Landroid/graphics/Point;

    move-result-object p1

    goto :goto_0

    nop

    :goto_2
    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    goto :goto_1

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_ArrowActionSheetPanel__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mArrowView:Landroidx/appcompat/widget/AppCompatImageView;', 'invoke-virtual {v0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;', 'if-nez v0, :cond_0', 'iget-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mArrowMode:Lmiuix/internal/widget/ActionSheet$ArrowMode;', 'invoke-direct {p0, v0}, Lmiuix/internal/widget/ArrowActionSheetPanel;->updateArrowViewDrawable(Lmiuix/internal/widget/ActionSheet$ArrowMode;)V', 'invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V', 'invoke-direct {p0}, Lmiuix/internal/widget/ArrowActionSheetPanel;->updateMeasuredSizeAfterSuperMeasured()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 4

    iget-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mArrowView:Landroidx/appcompat/widget/AppCompatImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-nez v0, :cond_0

    iget-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mArrowMode:Lmiuix/internal/widget/ActionSheet$ArrowMode;

    invoke-direct {p0, v0}, Lmiuix/internal/widget/ArrowActionSheetPanel;->updateArrowViewDrawable(Lmiuix/internal/widget/ActionSheet$ArrowMode;)V

    :cond_0
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    invoke-direct {p0}, Lmiuix/internal/widget/ArrowActionSheetPanel;->updateMeasuredSizeAfterSuperMeasured()V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 4

    goto :goto_4

    nop

    :goto_0
    invoke-direct {p0}, Lmiuix/internal/widget/ArrowActionSheetPanel;->updateMeasuredSizeAfterSuperMeasured()V

    goto :goto_3

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mArrowMode:Lmiuix/internal/widget/ActionSheet$ArrowMode;

    goto :goto_6

    nop

    :goto_2
    invoke-super {p0, p1, p2}, Landroid/widget/FrameLayout;->onMeasure(II)V

    goto :goto_0

    nop

    :goto_3
    return-void

    :goto_4
    iget-object v0, p0, Lmiuix/internal/widget/ArrowActionSheetPanel;->mArrowView:Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_8

    nop

    :goto_5
    if-eqz v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_1

    nop

    :goto_6
    invoke-direct {p0, v0}, Lmiuix/internal/widget/ArrowActionSheetPanel;->updateArrowViewDrawable(Lmiuix/internal/widget/ActionSheet$ArrowMode;)V

    :goto_7
    goto :goto_2

    nop

    :goto_8
    invoke-virtual {v0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
