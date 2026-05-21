TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/widget/DialogParentPanel2.smali'
CLASS_FALLBACK_NAMES = ['DialogParentPanel2.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_widget_DialogParentPanel2__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I', 'iget v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mDensityDpi:I', 'if-eq p1, v0, :cond_0', 'iput p1, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mDensityDpi:I', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getResources()Landroid/content/res/Resources;', 'sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_dialog_bg_corner_radius:I', 'invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimension(I)F'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I

    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mDensityDpi:I

    if-eq p1, v0, :cond_0

    iput p1, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mDensityDpi:I

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_dialog_bg_corner_radius:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimension(I)F

    move-result p1

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->setCornerRadius(F)V

    :cond_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->notifyConfigurationChanged()V

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_8

    nop

    :goto_0
    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mDensityDpi:I

    goto :goto_3

    nop

    :goto_1
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_dialog_bg_corner_radius:I

    goto :goto_7

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    goto :goto_1

    nop

    :goto_3
    if-ne p1, v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_b

    nop

    :goto_4
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->setCornerRadius(F)V

    :goto_5
    goto :goto_6

    nop

    :goto_6
    invoke-virtual {p0}, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->notifyConfigurationChanged()V

    goto :goto_9

    nop

    :goto_7
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimension(I)F

    move-result p1

    goto :goto_4

    nop

    :goto_8
    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_a

    nop

    :goto_9
    return-void

    :goto_a
    iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I

    goto :goto_0

    nop

    :goto_b
    iput p1, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mDensityDpi:I

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_DialogParentPanel2__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->notifyConfigurationChanged()V', 'iget v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mPanelFixedWidth:I', 'if-lez v0, :cond_0', 'invoke-static {v0, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I', 'iget-object v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mFloatingWindowSize:Lmiuix/appcompat/internal/widget/DialogParentPanel2$FloatingABOLayoutSpec;', 'invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/widget/DialogParentPanel2$FloatingABOLayoutSpec;->getWidthMeasureSpecForDialog(I)I', 'iget v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mPanelFixedHeight:I', 'if-lez v0, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 5

    invoke-virtual {p0}, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->notifyConfigurationChanged()V

    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mPanelFixedWidth:I

    const/high16 v1, 0x40000000

    if-lez v0, :cond_0

    invoke-static {v0, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mFloatingWindowSize:Lmiuix/appcompat/internal/widget/DialogParentPanel2$FloatingABOLayoutSpec;

    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/widget/DialogParentPanel2$FloatingABOLayoutSpec;->getWidthMeasureSpecForDialog(I)I

    move-result p1

    :goto_0
    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mPanelFixedHeight:I

    if-lez v0, :cond_1

    invoke-static {v0, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    goto :goto_1

    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mFloatingWindowSize:Lmiuix/appcompat/internal/widget/DialogParentPanel2$FloatingABOLayoutSpec;

    invoke-virtual {v0, p2}, Lmiuix/appcompat/internal/widget/DialogParentPanel2$FloatingABOLayoutSpec;->getHeightMeasureSpecForDialog(I)I

    move-result p2

    :goto_1
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    invoke-static {v0, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p1

    goto :goto_2

    nop

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->notifyConfigurationChanged()V

    goto :goto_5

    nop

    :goto_2
    goto :goto_11

    :goto_3
    goto :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mFloatingWindowSize:Lmiuix/appcompat/internal/widget/DialogParentPanel2$FloatingABOLayoutSpec;

    goto :goto_10

    nop

    :goto_5
    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mPanelFixedWidth:I

    goto :goto_12

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mFloatingWindowSize:Lmiuix/appcompat/internal/widget/DialogParentPanel2$FloatingABOLayoutSpec;

    goto :goto_e

    nop

    :goto_7
    return-void

    :goto_8
    goto :goto_f

    :goto_9
    goto :goto_6

    nop

    :goto_a
    invoke-static {v0, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    goto :goto_8

    nop

    :goto_b
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto :goto_7

    nop

    :goto_c
    if-gtz v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_a

    nop

    :goto_d
    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mPanelFixedHeight:I

    goto :goto_c

    nop

    :goto_e
    invoke-virtual {v0, p2}, Lmiuix/appcompat/internal/widget/DialogParentPanel2$FloatingABOLayoutSpec;->getHeightMeasureSpecForDialog(I)I

    move-result p2

    :goto_f
    goto :goto_b

    nop

    :goto_10
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/widget/DialogParentPanel2$FloatingABOLayoutSpec;->getWidthMeasureSpecForDialog(I)I

    move-result p1

    :goto_11
    goto :goto_d

    nop

    :goto_12
    const/high16 v1, 0x40000000

    goto :goto_13

    nop

    :goto_13
    if-gtz v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_DialogParentPanel2__onSizeChanged',
        'method': '.method protected onSizeChanged(IIII)V',
        'method_name': 'onSizeChanged',
        'method_anchors': ['invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/LinearLayout;->onSizeChanged(IIII)V', 'iget-object p0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mLayer:Landroid/graphics/RectF;', 'invoke-virtual {p0, p3, p3, p1, p2}, Landroid/graphics/RectF;->set(FFFF)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onSizeChanged(IIII)V
    .registers 5

    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/LinearLayout;->onSizeChanged(IIII)V

    iget-object p0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mLayer:Landroid/graphics/RectF;

    int-to-float p1, p1

    int-to-float p2, p2

    const/4 p3, 0x0

    invoke-virtual {p0, p3, p3, p1, p2}, Landroid/graphics/RectF;->set(FFFF)V

    return-void
.end method""",
        'replacement': """.method protected onSizeChanged(IIII)V
    .registers 5

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1, p2, p3, p4}, Landroid/widget/LinearLayout;->onSizeChanged(IIII)V

    goto :goto_5

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, p3, p3, p1, p2}, Landroid/graphics/RectF;->set(FFFF)V

    goto :goto_1

    nop

    :goto_3
    int-to-float p2, p2

    goto :goto_6

    nop

    :goto_4
    int-to-float p1, p1

    goto :goto_3

    nop

    :goto_5
    iget-object p0, p0, Lmiuix/appcompat/internal/widget/DialogParentPanel2;->mLayer:Landroid/graphics/RectF;

    goto :goto_4

    nop

    :goto_6
    const/4 p3, 0x0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
