TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/widget/DialogParentPanel.smali'
CLASS_FALLBACK_NAMES = ['DialogParentPanel.smali']
CLASS_ANCHORS = ['.super Landroidx/constraintlayout/widget/ConstraintLayout;']

PATCHES = [
    {
        'id': 'miuix_internal_widget_DialogParentPanel__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget-object p1, p0, Lmiuix/internal/widget/DialogParentPanel;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;', 'invoke-virtual {p1}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->onConfigurationChanged()V', 'invoke-virtual {p0}, Lmiuix/internal/widget/DialogParentPanel;->adjustLayout()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget-object p1, p0, Lmiuix/internal/widget/DialogParentPanel;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    invoke-virtual {p1}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->onConfigurationChanged()V

    invoke-virtual {p0}, Lmiuix/internal/widget/DialogParentPanel;->adjustLayout()V

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    invoke-virtual {p1}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->onConfigurationChanged()V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0}, Lmiuix/internal/widget/DialogParentPanel;->adjustLayout()V

    goto :goto_1

    nop

    :goto_3
    iget-object p1, p0, Lmiuix/internal/widget/DialogParentPanel;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    goto :goto_0

    nop

    :goto_4
    invoke-super {p0, p1}, Landroid/view/ViewGroup;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_DialogParentPanel__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V', 'invoke-direct {p0}, Lmiuix/internal/widget/DialogParentPanel;->init()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 1

    invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V

    invoke-direct {p0}, Lmiuix/internal/widget/DialogParentPanel;->init()V

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/view/ViewGroup;->onFinishInflate()V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-direct {p0}, Lmiuix/internal/widget/DialogParentPanel;->init()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_widget_DialogParentPanel__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget-object v0, p0, Lmiuix/internal/widget/DialogParentPanel;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;', 'invoke-virtual {v0, p2}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getHeightMeasureSpecForDialog(I)I', 'invoke-virtual {p0}, Lmiuix/internal/widget/DialogParentPanel;->shouldAdjustLayout()Z', 'if-eqz v0, :cond_0', 'invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'invoke-static {p2, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I', 'iget-object v0, p0, Lmiuix/internal/widget/DialogParentPanel;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;', 'invoke-virtual {v0, p1}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getWidthMeasureSpecForDialog(I)I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 4

    iget-object v0, p0, Lmiuix/internal/widget/DialogParentPanel;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    invoke-virtual {v0, p2}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getHeightMeasureSpecForDialog(I)I

    move-result p2

    invoke-virtual {p0}, Lmiuix/internal/widget/DialogParentPanel;->shouldAdjustLayout()Z

    move-result v0

    if-eqz v0, :cond_0

    invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p2

    const/high16 v0, 0x40000000

    invoke-static {p2, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    :cond_0
    iget-object v0, p0, Lmiuix/internal/widget/DialogParentPanel;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    invoke-virtual {v0, p1}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getWidthMeasureSpecForDialog(I)I

    move-result p1

    invoke-super {p0, p1, p2}, Landroidx/constraintlayout/widget/ConstraintLayout;->onMeasure(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 4

    goto :goto_4

    nop

    :goto_0
    invoke-static {p2, v0}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    :goto_1
    goto :goto_a

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/internal/widget/DialogParentPanel;->shouldAdjustLayout()Z

    move-result v0

    goto :goto_8

    nop

    :goto_3
    invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p2

    goto :goto_9

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/internal/widget/DialogParentPanel;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    goto :goto_7

    nop

    :goto_5
    invoke-super {p0, p1, p2}, Landroidx/constraintlayout/widget/ConstraintLayout;->onMeasure(II)V

    goto :goto_6

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {v0, p2}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getHeightMeasureSpecForDialog(I)I

    move-result p2

    goto :goto_2

    nop

    :goto_8
    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_3

    nop

    :goto_9
    const/high16 v0, 0x40000000

    goto :goto_0

    nop

    :goto_a
    iget-object v0, p0, Lmiuix/internal/widget/DialogParentPanel;->mFloatingWindowSize:Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;

    goto :goto_b

    nop

    :goto_b
    invoke-virtual {v0, p1}, Lmiuix/appcompat/app/floatingactivity/FloatingABOLayoutSpec;->getWidthMeasureSpecForDialog(I)I

    move-result p1

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
