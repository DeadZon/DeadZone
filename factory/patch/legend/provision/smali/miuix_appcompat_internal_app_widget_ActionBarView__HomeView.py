TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/ActionBarView$HomeView.smali'
CLASS_FALLBACK_NAMES = ['ActionBarView$HomeView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__HomeView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpIndicatorRes:I', 'if-eqz p1, :cond_0', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->setUpIndicator(I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpIndicatorRes:I

    if-eqz p1, :cond_0

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->setUpIndicator(I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_5

    nop

    :goto_0
    iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpIndicatorRes:I

    goto :goto_4

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->setUpIndicator(I)V

    :goto_2
    goto :goto_3

    nop

    :goto_3
    return-void

    :goto_4
    if-nez p1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_5
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__HomeView__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'sget v0, Lmiuix/appcompat/R$id;->up:I', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Landroid/widget/ImageView;', 'iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;', 'sget v0, Lmiuix/appcompat/R$id;->home:I', 'invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Landroid/widget/ImageView;'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 5

    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    sget v0, Lmiuix/appcompat/R$id;->up:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ImageView;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    sget v0, Lmiuix/appcompat/R$id;->home:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/ImageView;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mDefaultUpIndicator:Landroid/graphics/drawable/Drawable;

    const/4 v0, 0x1

    new-array v1, v0, [Landroid/view/View;

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    const/4 v3, 0x0

    aput-object v2, v1, v3

    invoke-static {v1}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v1

    invoke-interface {v1}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v1

    const/high16 v2, 0x42700000

    invoke-interface {v1, v2}, Lmiuix/animation/IHoverStyle;->setFeedbackRadius(F)V

    new-array v0, v0, [Landroid/view/View;

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    aput-object v1, v0, v3

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    sget-object v1, Lmiuix/animation/IHoverStyle$HoverEffect;->FLOATED_WRAPPED:Lmiuix/animation/IHoverStyle$HoverEffect;

    invoke-interface {v0, v1}, Lmiuix/animation/IHoverStyle;->setEffect(Lmiuix/animation/IHoverStyle$HoverEffect;)Lmiuix/animation/IHoverStyle;

    move-result-object v0

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    new-array v1, v3, [Lmiuix/animation/base/AnimConfig;

    invoke-interface {v0, p0, v1}, Lmiuix/animation/IHoverStyle;->handleHoverOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 5

    goto :goto_21

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_11

    nop

    :goto_1
    invoke-interface {v1, v2}, Lmiuix/animation/IHoverStyle;->setFeedbackRadius(F)V

    goto :goto_18

    nop

    :goto_2
    sget-object v1, Lmiuix/animation/IHoverStyle$HoverEffect;->FLOATED_WRAPPED:Lmiuix/animation/IHoverStyle$HoverEffect;

    goto :goto_7

    nop

    :goto_3
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_16

    nop

    :goto_4
    invoke-interface {v0, p0, v1}, Lmiuix/animation/IHoverStyle;->handleHoverOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    :goto_5
    goto :goto_20

    nop

    :goto_6
    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_2

    nop

    :goto_7
    invoke-interface {v0, v1}, Lmiuix/animation/IHoverStyle;->setEffect(Lmiuix/animation/IHoverStyle$HoverEffect;)Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_0

    nop

    :goto_8
    const/high16 v2, 0x42700000

    goto :goto_1

    nop

    :goto_9
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    goto :goto_19

    nop

    :goto_a
    check-cast v0, Landroid/widget/ImageView;

    goto :goto_b

    nop

    :goto_b
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_1e

    nop

    :goto_c
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_a

    nop

    :goto_d
    aput-object v2, v1, v3

    goto :goto_1d

    nop

    :goto_e
    const/4 v0, 0x1

    goto :goto_12

    nop

    :goto_f
    const/4 v3, 0x0

    goto :goto_d

    nop

    :goto_10
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_1c

    nop

    :goto_11
    new-array v1, v3, [Lmiuix/animation/base/AnimConfig;

    goto :goto_4

    nop

    :goto_12
    new-array v1, v0, [Landroid/view/View;

    goto :goto_17

    nop

    :goto_13
    check-cast v0, Landroid/widget/ImageView;

    goto :goto_9

    nop

    :goto_14
    sget v0, Lmiuix/appcompat/R$id;->up:I

    goto :goto_c

    nop

    :goto_15
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_13

    nop

    :goto_16
    aput-object v1, v0, v3

    goto :goto_1a

    nop

    :goto_17
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_f

    nop

    :goto_18
    new-array v0, v0, [Landroid/view/View;

    goto :goto_3

    nop

    :goto_19
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_10

    nop

    :goto_1a
    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    goto :goto_6

    nop

    :goto_1b
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mDefaultUpIndicator:Landroid/graphics/drawable/Drawable;

    goto :goto_e

    nop

    :goto_1c
    invoke-virtual {v0}, Landroid/widget/ImageView;->getDrawable()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_1b

    nop

    :goto_1d
    invoke-static {v1}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v1

    goto :goto_1f

    nop

    :goto_1e
    sget v0, Lmiuix/appcompat/R$id;->home:I

    goto :goto_15

    nop

    :goto_1f
    invoke-interface {v1}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v1

    goto :goto_8

    nop

    :goto_20
    return-void

    :goto_21
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto :goto_14

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__HomeView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;', 'invoke-virtual {v1}, Landroid/widget/ImageView;->getVisibility()I', 'if-eq v1, v2, :cond_1', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;', 'invoke-virtual {v1}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'check-cast v8, Landroid/widget/FrameLayout$LayoutParams;', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 15

    sub-int v1, p5, p3

    div-int/lit8 v6, v1, 0x2

    invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v7

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    invoke-virtual {v1}, Landroid/widget/ImageView;->getVisibility()I

    move-result v1

    const/16 v2, 0x8

    if-eq v1, v2, :cond_1

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    invoke-virtual {v1}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    move-object v8, v1

    check-cast v8, Landroid/widget/FrameLayout$LayoutParams;

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    invoke-virtual {v1}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v1

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    invoke-virtual {v2}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v4

    div-int/lit8 v2, v1, 0x2

    sub-int v3, v6, v2

    move v2, v1

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    move v5, v2

    const/4 v2, 0x0

    add-int/2addr v5, v3

    move-object v0, p0

    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    iget v1, v8, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    add-int/2addr v1, v4

    iget v2, v8, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    add-int/2addr v1, v2

    if-eqz v7, :cond_0

    sub-int v2, p4, v1

    move v3, v1

    move v1, v2

    move v2, p2

    goto :goto_1

    :cond_0
    add-int v2, p2, v1

    :goto_0
    move v3, v1

    move v1, p4

    goto :goto_1

    :cond_1
    const/4 v1, 0x0

    move v2, p2

    goto :goto_0

    :goto_1
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    invoke-virtual {v4}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v4

    check-cast v4, Landroid/widget/FrameLayout$LayoutParams;

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    invoke-virtual {v5}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v5

    iget-object v7, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    invoke-virtual {v7}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v7

    sub-int/2addr v1, v2

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mHorizontalPadding:I

    sub-int/2addr v1, v2

    div-int/lit8 v1, v1, 0x2

    invoke-virtual {v4}, Landroid/widget/FrameLayout$LayoutParams;->getMarginStart()I

    move-result v2

    div-int/lit8 v8, v7, 0x2

    sub-int/2addr v1, v8

    invoke-static {v2, v1}, Ljava/lang/Math;->max(II)I

    move-result v1

    add-int v2, v3, v1

    iget v1, v4, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    div-int/lit8 v3, v5, 0x2

    sub-int/2addr v6, v3

    invoke-static {v1, v6}, Ljava/lang/Math;->max(II)I

    move-result v3

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    add-int v4, v2, v7

    add-int/2addr v5, v3

    move-object v0, p0

    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 15

    goto :goto_36

    nop

    :goto_0
    add-int/2addr v5, v3

    goto :goto_3b

    nop

    :goto_1
    check-cast v8, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_13

    nop

    :goto_2
    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_3d

    nop

    :goto_3
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_22

    nop

    :goto_4
    move v2, v1

    goto :goto_5

    nop

    :goto_5
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_16

    nop

    :goto_6
    sub-int/2addr v1, v2

    goto :goto_45

    nop

    :goto_7
    add-int/2addr v1, v4

    goto :goto_12

    nop

    :goto_8
    div-int/lit8 v1, v1, 0x2

    goto :goto_35

    nop

    :goto_9
    move v3, v1

    goto :goto_20

    nop

    :goto_a
    sub-int/2addr v6, v3

    goto :goto_b

    nop

    :goto_b
    invoke-static {v1, v6}, Ljava/lang/Math;->max(II)I

    move-result v3

    goto :goto_30

    nop

    :goto_c
    sub-int/2addr v1, v8

    goto :goto_2f

    nop

    :goto_d
    div-int/lit8 v6, v1, 0x2

    goto :goto_2d

    nop

    :goto_e
    add-int/2addr v1, v2

    goto :goto_10

    nop

    :goto_f
    move v1, v2

    goto :goto_40

    nop

    :goto_10
    if-nez v7, :cond_0

    goto :goto_42

    :cond_0
    goto :goto_2c

    nop

    :goto_11
    add-int v4, v2, v7

    goto :goto_43

    nop

    :goto_12
    iget v2, v8, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    goto :goto_e

    nop

    :goto_13
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_3e

    nop

    :goto_14
    sub-int v3, v6, v2

    goto :goto_4

    nop

    :goto_15
    add-int v2, v3, v1

    goto :goto_27

    nop

    :goto_16
    move v5, v2

    goto :goto_25

    nop

    :goto_17
    return-void

    :goto_18
    invoke-static/range {v0 .. v5}, Lmiuix/internal/util/ViewUtils;->layoutChildView(Landroid/view/ViewGroup;Landroid/view/View;IIII)V

    goto :goto_17

    nop

    :goto_19
    goto :goto_32

    :goto_1a
    goto :goto_37

    nop

    :goto_1b
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_23

    nop

    :goto_1c
    const/16 v2, 0x8

    goto :goto_2b

    nop

    :goto_1d
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    goto :goto_24

    nop

    :goto_1e
    div-int/lit8 v2, v1, 0x2

    goto :goto_14

    nop

    :goto_1f
    iget-object v7, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    goto :goto_33

    nop

    :goto_20
    move v1, p4

    goto :goto_19

    nop

    :goto_21
    move-object v8, v1

    goto :goto_1

    nop

    :goto_22
    invoke-virtual {v1}, Landroid/widget/ImageView;->getVisibility()I

    move-result v1

    goto :goto_1c

    nop

    :goto_23
    invoke-virtual {v1}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_21

    nop

    :goto_24
    invoke-virtual {v4}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v4

    goto :goto_2e

    nop

    :goto_25
    const/4 v2, 0x0

    goto :goto_0

    nop

    :goto_26
    move v3, v1

    goto :goto_f

    nop

    :goto_27
    iget v1, v4, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    goto :goto_3f

    nop

    :goto_28
    move v2, p2

    goto :goto_31

    nop

    :goto_29
    add-int v2, p2, v1

    :goto_2a
    goto :goto_9

    nop

    :goto_2b
    if-ne v1, v2, :cond_1

    goto :goto_1a

    :cond_1
    goto :goto_1b

    nop

    :goto_2c
    sub-int v2, p4, v1

    goto :goto_26

    nop

    :goto_2d
    invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result v7

    goto :goto_3

    nop

    :goto_2e
    check-cast v4, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_46

    nop

    :goto_2f
    invoke-static {v2, v1}, Ljava/lang/Math;->max(II)I

    move-result v1

    goto :goto_15

    nop

    :goto_30
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    goto :goto_11

    nop

    :goto_31
    goto :goto_2a

    :goto_32
    goto :goto_1d

    nop

    :goto_33
    invoke-virtual {v7}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v7

    goto :goto_6

    nop

    :goto_34
    div-int/lit8 v8, v7, 0x2

    goto :goto_c

    nop

    :goto_35
    invoke-virtual {v4}, Landroid/widget/FrameLayout$LayoutParams;->getMarginStart()I

    move-result v2

    goto :goto_34

    nop

    :goto_36
    sub-int v1, p5, p3

    goto :goto_d

    nop

    :goto_37
    const/4 v1, 0x0

    goto :goto_28

    nop

    :goto_38
    invoke-virtual {v2}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v4

    goto :goto_1e

    nop

    :goto_39
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_38

    nop

    :goto_3a
    invoke-virtual {v5}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v5

    goto :goto_1f

    nop

    :goto_3b
    move-object v0, p0

    goto :goto_2

    nop

    :goto_3c
    move-object v0, p0

    goto :goto_18

    nop

    :goto_3d
    iget v1, v8, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    goto :goto_7

    nop

    :goto_3e
    invoke-virtual {v1}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v1

    goto :goto_39

    nop

    :goto_3f
    div-int/lit8 v3, v5, 0x2

    goto :goto_a

    nop

    :goto_40
    move v2, p2

    goto :goto_41

    nop

    :goto_41
    goto :goto_32

    :goto_42
    goto :goto_29

    nop

    :goto_43
    add-int/2addr v5, v3

    goto :goto_3c

    nop

    :goto_44
    sub-int/2addr v1, v2

    goto :goto_8

    nop

    :goto_45
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mHorizontalPadding:I

    goto :goto_44

    nop

    :goto_46
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    goto :goto_3a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarView__HomeView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;', 'invoke-virtual/range {v0 .. v5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V', 'iget-object p0, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;', 'invoke-virtual {p0}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'check-cast p0, Landroid/widget/FrameLayout$LayoutParams;', 'iget p1, p0, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I', 'iget-object p2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;', 'invoke-virtual {p2}, Landroid/widget/ImageView;->getMeasuredWidth()I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 15

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    const/4 v3, 0x0

    const/4 v5, 0x0

    move-object v0, p0

    move v2, p1

    move v4, p2

    invoke-virtual/range {v0 .. v5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object p0, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    invoke-virtual {p0}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p0

    check-cast p0, Landroid/widget/FrameLayout$LayoutParams;

    iget p1, p0, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    iget-object p2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    invoke-virtual {p2}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result p2

    add-int/2addr p1, p2

    iget p2, p0, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    add-int/2addr p1, p2

    iget-object p2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    invoke-virtual {p2}, Landroid/widget/ImageView;->getVisibility()I

    move-result p2

    const/4 v1, 0x0

    const/16 v3, 0x8

    if-ne p2, v3, :cond_0

    move v9, v1

    goto :goto_0

    :cond_0
    move v9, p1

    :goto_0
    iget p1, p0, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    iget-object p2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    invoke-virtual {p2}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result p2

    add-int/2addr p1, p2

    iget p0, p0, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    add-int/2addr p1, p0

    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    const/4 v11, 0x0

    move-object v6, v0

    move v8, v2

    move v10, v4

    invoke-virtual/range {v6 .. v11}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    iget-object p0, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    invoke-virtual {p0}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p0

    check-cast p0, Landroid/widget/FrameLayout$LayoutParams;

    iget p2, p0, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    invoke-virtual {v5}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v5

    add-int/2addr p2, v5

    iget v5, p0, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    add-int/2addr p2, v5

    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    invoke-virtual {v5}, Landroid/widget/ImageView;->getVisibility()I

    move-result v5

    if-ne v5, v3, :cond_1

    goto :goto_1

    :cond_1
    move v1, p2

    :goto_1
    add-int/2addr v9, v1

    if-lez v9, :cond_2

    iget p2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mHorizontalPadding:I

    add-int/2addr v9, p2

    :cond_2
    iget p2, p0, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    invoke-virtual {v1}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v1

    add-int/2addr p2, v1

    iget p0, p0, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    add-int/2addr p2, p0

    invoke-static {p1, p2}, Ljava/lang/Math;->max(II)I

    move-result p0

    invoke-static {v2}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p1

    invoke-static {v4}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p2

    invoke-static {v2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v1

    invoke-static {v4}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v2

    const/high16 v3, 0x40000000

    const/high16 v4, -0x80000000

    if-eq p1, v4, :cond_4

    if-eq p1, v3, :cond_3

    goto :goto_2

    :cond_3
    move v9, v1

    goto :goto_2

    :cond_4
    invoke-static {v9, v1}, Ljava/lang/Math;->min(II)I

    move-result v9

    :goto_2
    if-eq p2, v4, :cond_6

    if-eq p2, v3, :cond_5

    goto :goto_3

    :cond_5
    move p0, v2

    goto :goto_3

    :cond_6
    invoke-static {p0, v2}, Ljava/lang/Math;->min(II)I

    move-result p0

    :goto_3
    invoke-virtual {v0, v9, p0}, Landroid/widget/FrameLayout;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 15

    goto :goto_2a

    nop

    :goto_0
    goto :goto_3d

    :goto_1
    goto :goto_3c

    nop

    :goto_2
    iget p1, p0, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    goto :goto_55

    nop

    :goto_3
    add-int/2addr p1, p0

    goto :goto_1b

    nop

    :goto_4
    add-int/2addr p2, v5

    goto :goto_29

    nop

    :goto_5
    const/high16 v3, 0x40000000

    goto :goto_18

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p0

    goto :goto_44

    nop

    :goto_7
    const/16 v3, 0x8

    goto :goto_53

    nop

    :goto_8
    move v1, p2

    :goto_9
    goto :goto_3b

    nop

    :goto_a
    invoke-static {v2}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p1

    goto :goto_52

    nop

    :goto_b
    add-int/2addr p1, p2

    goto :goto_4a

    nop

    :goto_c
    iget p2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mHorizontalPadding:I

    goto :goto_19

    nop

    :goto_d
    const/4 v1, 0x0

    goto :goto_7

    nop

    :goto_e
    iget-object p0, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_21

    nop

    :goto_f
    invoke-virtual {v5}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result v5

    goto :goto_12

    nop

    :goto_10
    add-int/2addr p2, p0

    goto :goto_59

    nop

    :goto_11
    if-ne p2, v4, :cond_0

    goto :goto_26

    :cond_0
    goto :goto_15

    nop

    :goto_12
    add-int/2addr p2, v5

    goto :goto_2d

    nop

    :goto_13
    move-object v0, p0

    goto :goto_2e

    nop

    :goto_14
    add-int/2addr p2, v1

    goto :goto_3e

    nop

    :goto_15
    if-ne p2, v3, :cond_1

    goto :goto_23

    :cond_1
    goto :goto_22

    nop

    :goto_16
    goto :goto_33

    :goto_17
    goto :goto_32

    nop

    :goto_18
    const/high16 v4, -0x80000000

    goto :goto_50

    nop

    :goto_19
    add-int/2addr v9, p2

    :goto_1a
    goto :goto_2c

    nop

    :goto_1b
    iget-object v7, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    goto :goto_28

    nop

    :goto_1c
    move p0, v2

    goto :goto_25

    nop

    :goto_1d
    invoke-virtual/range {v6 .. v11}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_48

    nop

    :goto_1e
    invoke-virtual {v0, v9, p0}, Landroid/widget/FrameLayout;->setMeasuredDimension(II)V

    goto :goto_58

    nop

    :goto_1f
    invoke-static {v2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v1

    goto :goto_34

    nop

    :goto_20
    iget-object p2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_45

    nop

    :goto_21
    invoke-virtual {p0}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object p0

    goto :goto_2b

    nop

    :goto_22
    goto :goto_47

    :goto_23
    goto :goto_1c

    nop

    :goto_24
    invoke-virtual {p2}, Landroid/widget/ImageView;->getMeasuredWidth()I

    move-result p2

    goto :goto_b

    nop

    :goto_25
    goto :goto_47

    :goto_26
    goto :goto_46

    nop

    :goto_27
    if-gtz v9, :cond_2

    goto :goto_1a

    :cond_2
    goto :goto_c

    nop

    :goto_28
    const/4 v11, 0x0

    goto :goto_57

    nop

    :goto_29
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    goto :goto_3f

    nop

    :goto_2a
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_54

    nop

    :goto_2b
    check-cast p0, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_2

    nop

    :goto_2c
    iget p2, p0, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    goto :goto_38

    nop

    :goto_2d
    iget v5, p0, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    goto :goto_4

    nop

    :goto_2e
    move v2, p1

    goto :goto_36

    nop

    :goto_2f
    invoke-virtual/range {v0 .. v5}, Landroid/widget/FrameLayout;->measureChildWithMargins(Landroid/view/View;IIII)V

    goto :goto_e

    nop

    :goto_30
    move v9, v1

    goto :goto_0

    nop

    :goto_31
    move v8, v2

    goto :goto_5b

    nop

    :goto_32
    move v9, p1

    :goto_33
    goto :goto_41

    nop

    :goto_34
    invoke-static {v4}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result v2

    goto :goto_5

    nop

    :goto_35
    add-int/2addr p1, p2

    goto :goto_37

    nop

    :goto_36
    move v4, p2

    goto :goto_2f

    nop

    :goto_37
    iget p0, p0, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    goto :goto_3

    nop

    :goto_38
    iget-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    goto :goto_4f

    nop

    :goto_39
    const/4 v5, 0x0

    goto :goto_13

    nop

    :goto_3a
    if-eq v5, v3, :cond_3

    goto :goto_43

    :cond_3
    goto :goto_42

    nop

    :goto_3b
    add-int/2addr v9, v1

    goto :goto_27

    nop

    :goto_3c
    invoke-static {v9, v1}, Ljava/lang/Math;->min(II)I

    move-result v9

    :goto_3d
    goto :goto_11

    nop

    :goto_3e
    iget p0, p0, Landroid/widget/FrameLayout$LayoutParams;->bottomMargin:I

    goto :goto_10

    nop

    :goto_3f
    invoke-virtual {v5}, Landroid/widget/ImageView;->getVisibility()I

    move-result v5

    goto :goto_3a

    nop

    :goto_40
    if-ne p1, v3, :cond_4

    goto :goto_4c

    :cond_4
    goto :goto_4b

    nop

    :goto_41
    iget p1, p0, Landroid/widget/FrameLayout$LayoutParams;->topMargin:I

    goto :goto_56

    nop

    :goto_42
    goto :goto_9

    :goto_43
    goto :goto_8

    nop

    :goto_44
    check-cast p0, Landroid/widget/FrameLayout$LayoutParams;

    goto :goto_51

    nop

    :goto_45
    invoke-virtual {p2}, Landroid/widget/ImageView;->getVisibility()I

    move-result p2

    goto :goto_d

    nop

    :goto_46
    invoke-static {p0, v2}, Ljava/lang/Math;->min(II)I

    move-result p0

    :goto_47
    goto :goto_1e

    nop

    :goto_48
    iget-object p0, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    goto :goto_6

    nop

    :goto_49
    invoke-virtual {p2}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result p2

    goto :goto_35

    nop

    :goto_4a
    iget p2, p0, Landroid/widget/FrameLayout$LayoutParams;->rightMargin:I

    goto :goto_4d

    nop

    :goto_4b
    goto :goto_3d

    :goto_4c
    goto :goto_30

    nop

    :goto_4d
    add-int/2addr p1, p2

    goto :goto_20

    nop

    :goto_4e
    iget-object v5, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mIconView:Landroid/widget/ImageView;

    goto :goto_f

    nop

    :goto_4f
    invoke-virtual {v1}, Landroid/widget/ImageView;->getMeasuredHeight()I

    move-result v1

    goto :goto_14

    nop

    :goto_50
    if-ne p1, v4, :cond_5

    goto :goto_1

    :cond_5
    goto :goto_40

    nop

    :goto_51
    iget p2, p0, Landroid/widget/FrameLayout$LayoutParams;->leftMargin:I

    goto :goto_4e

    nop

    :goto_52
    invoke-static {v4}, Landroid/view/View$MeasureSpec;->getMode(I)I

    move-result p2

    goto :goto_1f

    nop

    :goto_53
    if-eq p2, v3, :cond_6

    goto :goto_17

    :cond_6
    goto :goto_5a

    nop

    :goto_54
    const/4 v3, 0x0

    goto :goto_39

    nop

    :goto_55
    iget-object p2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_24

    nop

    :goto_56
    iget-object p2, v0, Lmiuix/appcompat/internal/app/widget/ActionBarView$HomeView;->mUpView:Landroid/widget/ImageView;

    goto :goto_49

    nop

    :goto_57
    move-object v6, v0

    goto :goto_31

    nop

    :goto_58
    return-void

    :goto_59
    invoke-static {p1, p2}, Ljava/lang/Math;->max(II)I

    move-result p0

    goto :goto_a

    nop

    :goto_5a
    move v9, v1

    goto :goto_16

    nop

    :goto_5b
    move v10, v4

    goto :goto_1d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
