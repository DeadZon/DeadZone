TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/miuixbasewidget/widget/FilterSortView2.smali'
CLASS_FALLBACK_NAMES = ['FilterSortView2.smali']
CLASS_ANCHORS = ['.super Landroid/widget/HorizontalScrollView;']

PATCHES = [
    {
        'id': 'miuix_miuixbasewidget_widget_FilterSortView2__addTabViewAt',
        'method': '.method protected addTabViewAt(Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;I)V',
        'method_name': 'addTabViewAt',
        'method_anchors': ['if-eqz p1, :cond_2', 'iget v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabCount:I', 'if-gt p2, v0, :cond_1', 'if-gez p2, :cond_0', 'iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabViewContainerView:Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;', 'new-instance v2, Landroid/widget/FrameLayout$LayoutParams;', 'invoke-direct {v2, v1, v1}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V', 'invoke-virtual {v0, p1, p2, v2}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V'],
        'type': 'method_replace',
        'search': """.method protected addTabViewAt(Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;I)V
    .registers 6

    if-eqz p1, :cond_2

    iget v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabCount:I

    const/4 v1, -0x2

    if-gt p2, v0, :cond_1

    if-gez p2, :cond_0

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabViewContainerView:Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;

    new-instance v2, Landroid/widget/FrameLayout$LayoutParams;

    invoke-direct {v2, v1, v1}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    invoke-virtual {v0, p1, p2, v2}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    goto :goto_1

    :cond_1
    :goto_0
    iget-object p2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabViewContainerView:Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;

    new-instance v0, Landroid/widget/FrameLayout$LayoutParams;

    invoke-direct {v0, v1, v1}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    const/4 v1, -0x1

    invoke-virtual {p2, p1, v1, v0}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    :goto_1
    iget p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabCount:I

    add-int/lit8 p1, p1, 0x1

    iput p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabCount:I

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected addTabViewAt(Lmiuix/miuixbasewidget/widget/FilterSortView2$TabView;I)V
    .registers 6

    goto :goto_10

    nop

    :goto_0
    goto :goto_6

    :goto_1
    goto :goto_3

    nop

    :goto_2
    invoke-virtual {v0, p1, p2, v2}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    goto :goto_0

    nop

    :goto_3
    iget-object p2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabViewContainerView:Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;

    goto :goto_9

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {p2, p1, v1, v0}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;ILandroid/view/ViewGroup$LayoutParams;)V

    :goto_6
    goto :goto_f

    nop

    :goto_7
    invoke-direct {v0, v1, v1}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    goto :goto_13

    nop

    :goto_8
    add-int/lit8 p1, p1, 0x1

    goto :goto_c

    nop

    :goto_9
    new-instance v0, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_7

    nop

    :goto_a
    invoke-direct {v2, v1, v1}, Landroid/widget/FrameLayout$LayoutParams;-><init>(II)V

    goto :goto_2

    nop

    :goto_b
    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabViewContainerView:Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;

    goto :goto_14

    nop

    :goto_c
    iput p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabCount:I

    :goto_d
    goto :goto_4

    nop

    :goto_e
    if-ltz p2, :cond_0

    goto :goto_17

    :cond_0
    goto :goto_16

    nop

    :goto_f
    iget p1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabCount:I

    goto :goto_8

    nop

    :goto_10
    if-nez p1, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_15

    nop

    :goto_11
    if-le p2, v0, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_e

    nop

    :goto_12
    const/4 v1, -0x2

    goto :goto_11

    nop

    :goto_13
    const/4 v1, -0x1

    goto :goto_5

    nop

    :goto_14
    new-instance v2, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_a

    nop

    :goto_15
    iget v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabCount:I

    goto :goto_12

    nop

    :goto_16
    goto :goto_1

    :goto_17
    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_miuixbasewidget_widget_FilterSortView2__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;', 'invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;', 'invoke-virtual {v1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;', 'iget v1, v1, Landroid/util/DisplayMetrics;->density:F', 'iget v2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mLayoutConfig:I', 'if-nez v2, :cond_0', 'invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 11

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v1

    iget v1, v1, Landroid/util/DisplayMetrics;->density:F

    iget v2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mLayoutConfig:I

    const/16 v3, 0x280

    const/4 v4, 0x2

    const/high16 v5, 0x3f800000

    const/4 v6, 0x1

    const/4 v7, 0x0

    if-nez v2, :cond_0

    int-to-float v0, v0

    mul-float/2addr v0, v5

    div-float/2addr v0, v1

    float-to-int v0, v0

    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;

    move-result-object v2

    invoke-static {v2}, Lmiuix/core/util/EnvStateManager;->getWindowSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object v2

    iget v2, v2, Landroid/graphics/Point;->x:I

    int-to-float v2, v2

    mul-float/2addr v2, v5

    div-float/2addr v2, v1

    float-to-int v1, v2

    iget v2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mDeviceType:I

    if-ne v2, v4, :cond_3

    const/16 v2, 0x19a

    if-le v0, v2, :cond_3

    if-le v1, v3, :cond_3

    goto :goto_0

    :cond_0
    if-ne v2, v6, :cond_1

    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lmiuix/core/util/EnvStateManager;->getWindowSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object v0

    iget v0, v0, Landroid/graphics/Point;->x:I

    int-to-float v0, v0

    mul-float/2addr v0, v5

    div-float/2addr v0, v1

    float-to-int v0, v0

    iget v1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mDeviceType:I

    if-ne v1, v4, :cond_3

    if-le v0, v3, :cond_3

    goto :goto_0

    :cond_1
    const/4 v0, 0x3

    if-ne v2, v0, :cond_2

    :goto_0
    move v4, v6

    goto :goto_1

    :cond_2
    const/4 v0, 0x4

    if-ne v2, v0, :cond_3

    goto :goto_1

    :cond_3
    move v4, v7

    :goto_1
    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabViewContainerView:Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;

    invoke-virtual {v0, v4}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->setTabViewLayoutMode(I)V

    invoke-super {p0, p1, p2}, Landroid/widget/HorizontalScrollView;->onMeasure(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 11

    goto :goto_14

    nop

    :goto_0
    div-float/2addr v2, v1

    goto :goto_15

    nop

    :goto_1
    goto :goto_c

    :goto_2
    goto :goto_8

    nop

    :goto_3
    if-eq v2, v0, :cond_0

    goto :goto_31

    :cond_0
    goto :goto_30

    nop

    :goto_4
    move v4, v6

    goto :goto_2c

    nop

    :goto_5
    move v4, v7

    :goto_6
    goto :goto_26

    nop

    :goto_7
    if-gt v0, v2, :cond_1

    goto :goto_31

    :cond_1
    goto :goto_21

    nop

    :goto_8
    if-eq v2, v6, :cond_2

    goto :goto_1d

    :cond_2
    goto :goto_1f

    nop

    :goto_9
    div-float/2addr v0, v1

    goto :goto_12

    nop

    :goto_a
    if-gt v0, v3, :cond_3

    goto :goto_31

    :cond_3
    goto :goto_1c

    nop

    :goto_b
    if-eq v2, v0, :cond_4

    goto :goto_2d

    :cond_4
    :goto_c
    goto :goto_4

    nop

    :goto_d
    const/16 v2, 0x19a

    goto :goto_7

    nop

    :goto_e
    invoke-super {p0, p1, p2}, Landroid/widget/HorizontalScrollView;->onMeasure(II)V

    goto :goto_f

    nop

    :goto_f
    return-void

    :goto_10
    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    goto :goto_37

    nop

    :goto_11
    iget v1, v1, Landroid/util/DisplayMetrics;->density:F

    goto :goto_32

    nop

    :goto_12
    float-to-int v0, v0

    goto :goto_34

    nop

    :goto_13
    mul-float/2addr v0, v5

    goto :goto_39

    nop

    :goto_14
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v0

    goto :goto_23

    nop

    :goto_15
    float-to-int v1, v2

    goto :goto_38

    nop

    :goto_16
    if-eqz v2, :cond_5

    goto :goto_2

    :cond_5
    goto :goto_3a

    nop

    :goto_17
    iget v2, v2, Landroid/graphics/Point;->x:I

    goto :goto_2a

    nop

    :goto_18
    iget v0, v0, Landroid/graphics/Point;->x:I

    goto :goto_27

    nop

    :goto_19
    const/16 v3, 0x280

    goto :goto_1b

    nop

    :goto_1a
    invoke-static {v0}, Lmiuix/core/util/EnvStateManager;->getWindowSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object v0

    goto :goto_18

    nop

    :goto_1b
    const/4 v4, 0x2

    goto :goto_28

    nop

    :goto_1c
    goto :goto_c

    :goto_1d
    goto :goto_29

    nop

    :goto_1e
    iget v1, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mDeviceType:I

    goto :goto_2b

    nop

    :goto_1f
    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_1a

    nop

    :goto_20
    const/4 v7, 0x0

    goto :goto_16

    nop

    :goto_21
    if-gt v1, v3, :cond_6

    goto :goto_31

    :cond_6
    goto :goto_1

    nop

    :goto_22
    mul-float/2addr v0, v5

    goto :goto_9

    nop

    :goto_23
    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;

    move-result-object v1

    goto :goto_10

    nop

    :goto_24
    if-eq v2, v4, :cond_7

    goto :goto_31

    :cond_7
    goto :goto_d

    nop

    :goto_25
    const/4 v6, 0x1

    goto :goto_20

    nop

    :goto_26
    iget-object v0, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mTabViewContainerView:Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;

    goto :goto_2f

    nop

    :goto_27
    int-to-float v0, v0

    goto :goto_13

    nop

    :goto_28
    const/high16 v5, 0x3f800000

    goto :goto_25

    nop

    :goto_29
    const/4 v0, 0x3

    goto :goto_b

    nop

    :goto_2a
    int-to-float v2, v2

    goto :goto_33

    nop

    :goto_2b
    if-eq v1, v4, :cond_8

    goto :goto_31

    :cond_8
    goto :goto_a

    nop

    :goto_2c
    goto :goto_6

    :goto_2d
    goto :goto_36

    nop

    :goto_2e
    float-to-int v0, v0

    goto :goto_1e

    nop

    :goto_2f
    invoke-virtual {v0, v4}, Lmiuix/miuixbasewidget/widget/internal/TabViewContainerView;->setTabViewLayoutMode(I)V

    goto :goto_e

    nop

    :goto_30
    goto :goto_6

    :goto_31
    goto :goto_5

    nop

    :goto_32
    iget v2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mLayoutConfig:I

    goto :goto_19

    nop

    :goto_33
    mul-float/2addr v2, v5

    goto :goto_0

    nop

    :goto_34
    invoke-virtual {p0}, Landroid/widget/HorizontalScrollView;->getContext()Landroid/content/Context;

    move-result-object v2

    goto :goto_35

    nop

    :goto_35
    invoke-static {v2}, Lmiuix/core/util/EnvStateManager;->getWindowSize(Landroid/content/Context;)Landroid/graphics/Point;

    move-result-object v2

    goto :goto_17

    nop

    :goto_36
    const/4 v0, 0x4

    goto :goto_3

    nop

    :goto_37
    invoke-virtual {v1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v1

    goto :goto_11

    nop

    :goto_38
    iget v2, p0, Lmiuix/miuixbasewidget/widget/FilterSortView2;->mDeviceType:I

    goto :goto_24

    nop

    :goto_39
    div-float/2addr v0, v1

    goto :goto_2e

    nop

    :goto_3a
    int-to-float v0, v0

    goto :goto_22

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
