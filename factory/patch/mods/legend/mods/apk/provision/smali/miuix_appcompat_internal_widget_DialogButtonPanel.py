TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/widget/DialogButtonPanel.smali'
CLASS_FALLBACK_NAMES = ['DialogButtonPanel.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_widget_DialogButtonPanel__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mCurrentDensityDpi:I', 'iput v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mLastDensityDpi:I', 'iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I', 'if-eq v0, p1, :cond_1', 'iput p1, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mCurrentDensityDpi:I', 'iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mPanelPaddingHorizontal:I', 'iput v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mPanelPaddingHorizontal:I'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 5

    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mCurrentDensityDpi:I

    iput v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mLastDensityDpi:I

    iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I

    if-eq v0, p1, :cond_1

    iput p1, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mCurrentDensityDpi:I

    int-to-float p1, p1

    const/high16 v1, 0x3f800000

    mul-float/2addr p1, v1

    int-to-float v0, v0

    div-float/2addr p1, v0

    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mPanelPaddingHorizontal:I

    int-to-float v0, v0

    mul-float/2addr v0, p1

    float-to-int v0, v0

    iput v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mPanelPaddingHorizontal:I

    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMarginHorizontal:I

    int-to-float v0, v0

    mul-float/2addr v0, p1

    float-to-int v0, v0

    iput v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMarginHorizontal:I

    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMarginVertical:I

    int-to-float v0, v0

    mul-float/2addr v0, p1

    float-to-int v0, v0

    iput v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMarginVertical:I

    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMinHeight:I

    int-to-float v0, v0

    mul-float/2addr v0, p1

    float-to-int p1, v0

    iput p1, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMinHeight:I

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result p1

    const/4 v0, 0x0

    :goto_0
    if-ge v0, p1, :cond_1

    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    instance-of v2, v1, Landroid/widget/TextView;

    if-eqz v2, :cond_0

    check-cast v1, Landroid/widget/TextView;

    iget v2, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonTextSize:F

    invoke-static {v1, v2}, Lmiuix/view/DensityChangedHelper;->updateTextSizeSpUnit(Landroid/widget/TextView;F)V

    :cond_0
    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 5

    goto :goto_12

    nop

    :goto_0
    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto :goto_2d

    nop

    :goto_1
    float-to-int v0, v0

    goto :goto_5

    nop

    :goto_2
    int-to-float v0, v0

    goto :goto_c

    nop

    :goto_3
    float-to-int v0, v0

    goto :goto_28

    nop

    :goto_4
    if-lt v0, p1, :cond_0

    goto :goto_27

    :cond_0
    goto :goto_0

    nop

    :goto_5
    iput v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mPanelPaddingHorizontal:I

    goto :goto_11

    nop

    :goto_6
    iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I

    goto :goto_b

    nop

    :goto_7
    invoke-static {v1, v2}, Lmiuix/view/DensityChangedHelper;->updateTextSizeSpUnit(Landroid/widget/TextView;F)V

    :goto_8
    goto :goto_10

    nop

    :goto_9
    mul-float/2addr v0, p1

    goto :goto_1

    nop

    :goto_a
    mul-float/2addr v0, p1

    goto :goto_3

    nop

    :goto_b
    if-ne v0, p1, :cond_1

    goto :goto_27

    :cond_1
    goto :goto_1f

    nop

    :goto_c
    div-float/2addr p1, v0

    goto :goto_1e

    nop

    :goto_d
    mul-float/2addr v0, p1

    goto :goto_22

    nop

    :goto_e
    iput p1, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMinHeight:I

    goto :goto_13

    nop

    :goto_f
    int-to-float v0, v0

    goto :goto_9

    nop

    :goto_10
    add-int/lit8 v0, v0, 0x1

    goto :goto_26

    nop

    :goto_11
    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMarginHorizontal:I

    goto :goto_1a

    nop

    :goto_12
    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_25

    nop

    :goto_13
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result p1

    goto :goto_1c

    nop

    :goto_14
    int-to-float p1, p1

    goto :goto_20

    nop

    :goto_15
    int-to-float v0, v0

    goto :goto_2c

    nop

    :goto_16
    return-void

    :goto_17
    iput v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMarginHorizontal:I

    goto :goto_29

    nop

    :goto_18
    iput v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mLastDensityDpi:I

    goto :goto_6

    nop

    :goto_19
    float-to-int p1, v0

    goto :goto_e

    nop

    :goto_1a
    int-to-float v0, v0

    goto :goto_d

    nop

    :goto_1b
    if-nez v2, :cond_2

    goto :goto_8

    :cond_2
    goto :goto_2b

    nop

    :goto_1c
    const/4 v0, 0x0

    :goto_1d
    goto :goto_4

    nop

    :goto_1e
    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mPanelPaddingHorizontal:I

    goto :goto_f

    nop

    :goto_1f
    iput p1, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mCurrentDensityDpi:I

    goto :goto_14

    nop

    :goto_20
    const/high16 v1, 0x3f800000

    goto :goto_24

    nop

    :goto_21
    int-to-float v0, v0

    goto :goto_a

    nop

    :goto_22
    float-to-int v0, v0

    goto :goto_17

    nop

    :goto_23
    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMinHeight:I

    goto :goto_15

    nop

    :goto_24
    mul-float/2addr p1, v1

    goto :goto_2

    nop

    :goto_25
    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mCurrentDensityDpi:I

    goto :goto_18

    nop

    :goto_26
    goto :goto_1d

    :goto_27
    goto :goto_16

    nop

    :goto_28
    iput v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMarginVertical:I

    goto :goto_23

    nop

    :goto_29
    iget v0, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonMarginVertical:I

    goto :goto_21

    nop

    :goto_2a
    iget v2, p0, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->mButtonTextSize:F

    goto :goto_7

    nop

    :goto_2b
    check-cast v1, Landroid/widget/TextView;

    goto :goto_2a

    nop

    :goto_2c
    mul-float/2addr v0, p1

    goto :goto_19

    nop

    :goto_2d
    instance-of v2, v1, Landroid/widget/TextView;

    goto :goto_1b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_DialogButtonPanel__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroid/widget/LinearLayout;->onLayout(ZIIII)V', 'invoke-direct {p0}, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->adjustButtonScrollIfNeed()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-super/range {p0 .. p5}, Landroid/widget/LinearLayout;->onLayout(ZIIII)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->adjustButtonScrollIfNeed()V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_0

    nop

    :goto_0
    invoke-super/range {p0 .. p5}, Landroid/widget/LinearLayout;->onLayout(ZIIII)V

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-direct {p0}, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->adjustButtonScrollIfNeed()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_widget_DialogButtonPanel__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'invoke-direct {p0, v0}, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->handleButtonLayout(I)V', 'invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 4

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->handleButtonLayout(I)V

    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto :goto_2

    nop

    :goto_1
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/widget/DialogButtonPanel;->handleButtonLayout(I)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
