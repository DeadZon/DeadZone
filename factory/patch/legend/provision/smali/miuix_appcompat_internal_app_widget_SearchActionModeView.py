TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/SearchActionModeView.smali'
CLASS_FALLBACK_NAMES = ['SearchActionModeView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;', '.implements Landroid/animation/Animator$AnimatorListener;', '.implements Lmiuix/appcompat/internal/app/widget/ActionModeView;', '.implements Landroid/text/TextWatcher;', '.implements Landroid/view/View$OnClickListener;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__createAnimationListeners',
        'method': '.method protected createAnimationListeners()V',
        'method_name': 'createAnimationListeners',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;', 'if-nez v0, :cond_0', 'new-instance v0, Ljava/util/ArrayList;', 'invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V', 'iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;', 'new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$SearchViewAnimationProcessor;', 'invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$SearchViewAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V'],
        'type': 'method_replace',
        'search': """.method protected createAnimationListeners()V
    .registers 3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    if-nez v0, :cond_0

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$SearchViewAnimationProcessor;

    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$SearchViewAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->shouldAnimateContent()Z

    move-result v0

    if-eqz v0, :cond_1

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$ContentViewAnimationProcessor;

    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$ContentViewAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$ActionBarAnimationProcessor;

    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$ActionBarAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$SplitActionBarAnimationProcessor;

    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$SplitActionBarAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getDimView()Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$DimViewAnimationProcessor;

    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$DimViewAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected createAnimationListeners()V
    .registers 3

    goto :goto_1c

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_10

    nop

    :goto_1
    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$DimViewAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V

    goto :goto_12

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    goto :goto_1f

    nop

    :goto_3
    new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$SearchViewAnimationProcessor;

    goto :goto_e

    nop

    :goto_4
    new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$ContentViewAnimationProcessor;

    goto :goto_b

    nop

    :goto_5
    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :goto_6
    goto :goto_f

    nop

    :goto_7
    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$ActionBarAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V

    goto :goto_14

    nop

    :goto_8
    if-nez v0, :cond_1

    goto :goto_13

    :cond_1
    goto :goto_2

    nop

    :goto_9
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->shouldAnimateContent()Z

    move-result v0

    goto :goto_0

    nop

    :goto_a
    new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$ActionBarAnimationProcessor;

    goto :goto_7

    nop

    :goto_b
    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$ContentViewAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V

    goto :goto_20

    nop

    :goto_c
    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_9

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    goto :goto_a

    nop

    :goto_e
    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$SearchViewAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V

    goto :goto_c

    nop

    :goto_f
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getDimView()Landroid/view/View;

    move-result-object v0

    goto :goto_8

    nop

    :goto_10
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    goto :goto_4

    nop

    :goto_11
    new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$SplitActionBarAnimationProcessor;

    goto :goto_1b

    nop

    :goto_12
    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :goto_13
    goto :goto_15

    nop

    :goto_14
    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_1d

    nop

    :goto_15
    return-void

    :goto_16
    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    goto :goto_17

    nop

    :goto_17
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    :goto_18
    goto :goto_1e

    nop

    :goto_19
    new-instance v0, Ljava/util/ArrayList;

    goto :goto_16

    nop

    :goto_1a
    if-eqz v0, :cond_2

    goto :goto_18

    :cond_2
    goto :goto_19

    nop

    :goto_1b
    invoke-direct {v1, p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$SplitActionBarAnimationProcessor;-><init>(Lmiuix/appcompat/internal/app/widget/SearchActionModeView;)V

    goto :goto_5

    nop

    :goto_1c
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    goto :goto_1a

    nop

    :goto_1d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    goto :goto_11

    nop

    :goto_1e
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mAnimationListeners:Ljava/util/List;

    goto :goto_3

    nop

    :goto_1f
    new-instance v1, Lmiuix/appcompat/internal/app/widget/SearchActionModeView$DimViewAnimationProcessor;

    goto :goto_1

    nop

    :goto_20
    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    goto :goto_d

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__finishAnimation',
        'method': '.method protected finishAnimation()V',
        'method_name': 'finishAnimation',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->removeAllListeners()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;', 'invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->cancel()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;', 'invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setTarget(Ljava/lang/Object;)V', 'iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;'],
        'type': 'method_replace',
        'search': """.method protected finishAnimation()V
    .registers 3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->removeAllListeners()V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->cancel()V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setTarget(Ljava/lang/Object;)V

    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected finishAnimation()V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    goto :goto_6

    nop

    :goto_1
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_3

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    goto :goto_1

    nop

    :goto_3
    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->removeAllListeners()V

    goto :goto_0

    nop

    :goto_4
    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    :goto_5
    goto :goto_9

    nop

    :goto_6
    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->cancel()V

    goto :goto_8

    nop

    :goto_7
    const/4 v1, 0x0

    goto :goto_a

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    goto :goto_7

    nop

    :goto_9
    return-void

    :goto_a
    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setTarget(Ljava/lang/Object;)V

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__getActionBarContainer',
        'method': '.method protected getActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;',
        'method_name': 'getActionBarContainer',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;', 'if-nez v0, :cond_3', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'check-cast v0, Landroid/view/ViewGroup;', 'if-eqz v0, :cond_2', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I'],
        'type': 'method_replace',
        'search': """.method protected getActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;
    .registers 6

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-nez v0, :cond_3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    if-eqz v0, :cond_2

    const/4 v1, 0x0

    :goto_1
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v2

    if-ge v1, v2, :cond_2

    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    invoke-virtual {v2}, Landroid/view/View;->getId()I

    move-result v3

    sget v4, Lmiuix/appcompat/R$id;->action_bar_container:I

    if-ne v3, v4, :cond_1

    instance-of v3, v2, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-eqz v3, :cond_1

    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    iput-object v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_2

    :cond_1
    add-int/lit8 v1, v1, 0x1

    goto :goto_1

    :cond_2
    :goto_2
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-eqz v0, :cond_3

    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup$MarginLayoutParams;

    iget v0, v0, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarTopMargin:I

    if-lez v0, :cond_3

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingStart()I

    move-result v0

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOriginalPaddingTop:I

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mPendingInsetTop:I

    add-int/2addr v1, v2

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarTopMargin:I

    add-int/2addr v1, v2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingEnd()I

    move-result v2

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result v3

    invoke-virtual {p0, v0, v1, v2, v3}, Landroid/widget/FrameLayout;->setPaddingRelative(IIII)V

    :cond_3
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    return-object p0
.end method""",
        'replacement': """.method protected getActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;
    .registers 6

    goto :goto_4

    nop

    :goto_0
    goto :goto_21

    :goto_1
    goto :goto_16

    nop

    :goto_2
    const/4 v0, 0x0

    :goto_3
    goto :goto_a

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_6

    nop

    :goto_5
    if-lt v1, v2, :cond_0

    goto :goto_21

    :cond_0
    goto :goto_12

    nop

    :goto_6
    if-eqz v0, :cond_1

    goto :goto_2e

    :cond_1
    goto :goto_1d

    nop

    :goto_7
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v2

    goto :goto_5

    nop

    :goto_8
    if-nez v0, :cond_2

    goto :goto_1a

    :cond_2
    goto :goto_24

    nop

    :goto_9
    if-nez v0, :cond_3

    goto :goto_2e

    :cond_3
    goto :goto_23

    nop

    :goto_a
    if-nez v0, :cond_4

    goto :goto_21

    :cond_4
    goto :goto_b

    nop

    :goto_b
    const/4 v1, 0x0

    :goto_c
    goto :goto_7

    nop

    :goto_d
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingBottom()I

    move-result v3

    goto :goto_2d

    nop

    :goto_e
    iput-object v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_0

    nop

    :goto_f
    if-gtz v0, :cond_5

    goto :goto_2e

    :cond_5
    goto :goto_10

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingStart()I

    move-result v0

    goto :goto_29

    nop

    :goto_11
    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_e

    nop

    :goto_12
    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    goto :goto_1b

    nop

    :goto_13
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarTopMargin:I

    goto :goto_f

    nop

    :goto_14
    if-nez v3, :cond_6

    goto :goto_1

    :cond_6
    goto :goto_11

    nop

    :goto_15
    sget v4, Lmiuix/appcompat/R$id;->action_bar_container:I

    goto :goto_2c

    nop

    :goto_16
    add-int/lit8 v1, v1, 0x1

    goto :goto_20

    nop

    :goto_17
    add-int/2addr v1, v2

    goto :goto_26

    nop

    :goto_18
    add-int/2addr v1, v2

    goto :goto_1e

    nop

    :goto_19
    goto :goto_3

    :goto_1a
    goto :goto_2

    nop

    :goto_1b
    invoke-virtual {v2}, Landroid/view/View;->getId()I

    move-result v3

    goto :goto_15

    nop

    :goto_1c
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_9

    nop

    :goto_1d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;

    goto :goto_8

    nop

    :goto_1e
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarTopMargin:I

    goto :goto_17

    nop

    :goto_1f
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_19

    nop

    :goto_20
    goto :goto_c

    :goto_21
    goto :goto_1c

    nop

    :goto_22
    return-object p0

    :goto_23
    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    goto :goto_2b

    nop

    :goto_24
    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    goto :goto_1f

    nop

    :goto_25
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_22

    nop

    :goto_26
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getPaddingEnd()I

    move-result v2

    goto :goto_d

    nop

    :goto_27
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mPendingInsetTop:I

    goto :goto_18

    nop

    :goto_28
    instance-of v3, v2, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_14

    nop

    :goto_29
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOriginalPaddingTop:I

    goto :goto_27

    nop

    :goto_2a
    iget v0, v0, Landroid/view/ViewGroup$MarginLayoutParams;->topMargin:I

    goto :goto_13

    nop

    :goto_2b
    check-cast v0, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_2a

    nop

    :goto_2c
    if-eq v3, v4, :cond_7

    goto :goto_1

    :cond_7
    goto :goto_28

    nop

    :goto_2d
    invoke-virtual {p0, v0, v1, v2, v3}, Landroid/widget/FrameLayout;->setPaddingRelative(IIII)V

    :goto_2e
    goto :goto_25

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__getActionBarView',
        'method': '.method protected getActionBarView()Lmiuix/appcompat/internal/app/widget/ActionBarView;',
        'method_name': 'getActionBarView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'if-nez v0, :cond_1', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'check-cast v0, Landroid/view/ViewGroup;', 'if-eqz v0, :cond_1', 'sget v1, Lmiuix/appcompat/R$id;->action_bar:I'],
        'type': 'method_replace',
        'search': """.method protected getActionBarView()Lmiuix/appcompat/internal/app/widget/ActionBarView;
    .registers 3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-nez v0, :cond_1

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    if-eqz v0, :cond_1

    sget v1, Lmiuix/appcompat/R$id;->action_bar:I

    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    :cond_1
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    return-object p0
.end method""",
        'replacement': """.method protected getActionBarView()Lmiuix/appcompat/internal/app/widget/ActionBarView;
    .registers 3

    goto :goto_10

    nop

    :goto_0
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    :goto_1
    goto :goto_3

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_4

    nop

    :goto_3
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_6

    nop

    :goto_4
    sget v1, Lmiuix/appcompat/R$id;->action_bar:I

    goto :goto_8

    nop

    :goto_5
    check-cast v0, Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_0

    nop

    :goto_6
    return-object p0

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;

    goto :goto_f

    nop

    :goto_8
    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_5

    nop

    :goto_9
    goto :goto_d

    :goto_a
    goto :goto_c

    nop

    :goto_b
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_9

    nop

    :goto_c
    const/4 v0, 0x0

    :goto_d
    goto :goto_2

    nop

    :goto_e
    if-eqz v0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_7

    nop

    :goto_f
    if-nez v0, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_11

    nop

    :goto_10
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_e

    nop

    :goto_11
    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__getDimView',
        'method': '.method protected getDimView()Landroid/view/View;',
        'method_name': 'getDimView',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;', 'if-nez v0, :cond_4', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'check-cast v0, Landroid/view/ViewGroup;', 'if-eqz v0, :cond_4', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I'],
        'type': 'method_replace',
        'search': """.method protected getDimView()Landroid/view/View;
    .registers 6

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;

    if-nez v0, :cond_4

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_0

    :cond_0
    move-object v0, v1

    :goto_0
    if-eqz v0, :cond_4

    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v2

    add-int/lit8 v2, v2, -0x1

    :goto_1
    if-ltz v2, :cond_2

    invoke-virtual {v0, v2}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    invoke-virtual {v3}, Landroid/view/View;->getId()I

    move-result v3

    sget v4, Lmiuix/appcompat/R$id;->search_mask_vs:I

    if-ne v3, v4, :cond_1

    invoke-virtual {v0, v2}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    check-cast v1, Landroid/view/ViewStub;

    goto :goto_2

    :cond_1
    add-int/lit8 v2, v2, -0x1

    goto :goto_1

    :cond_2
    :goto_2
    if-eqz v1, :cond_3

    invoke-virtual {v1}, Landroid/view/ViewStub;->inflate()Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;

    goto :goto_3

    :cond_3
    sget v1, Lmiuix/appcompat/R$id;->search_mask:I

    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;

    :cond_4
    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCustomFrameLayout:Landroid/widget/FrameLayout;

    if-eqz v0, :cond_5

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/widget/FrameLayout;->setVisibility(I)V

    :cond_5
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;

    return-object p0
.end method""",
        'replacement': """.method protected getDimView()Landroid/view/View;
    .registers 6

    goto :goto_28

    nop

    :goto_0
    invoke-virtual {v0, v2}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto :goto_1

    nop

    :goto_1
    check-cast v1, Landroid/view/ViewStub;

    goto :goto_14

    nop

    :goto_2
    if-eqz v0, :cond_0

    goto :goto_13

    :cond_0
    goto :goto_8

    nop

    :goto_3
    if-nez v0, :cond_1

    goto :goto_2a

    :cond_1
    goto :goto_26

    nop

    :goto_4
    goto :goto_7

    :goto_5
    goto :goto_6

    nop

    :goto_6
    move-object v0, v1

    :goto_7
    goto :goto_23

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;

    goto :goto_18

    nop

    :goto_9
    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_12

    nop

    :goto_a
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v2

    goto :goto_16

    nop

    :goto_b
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCustomFrameLayout:Landroid/widget/FrameLayout;

    goto :goto_3

    nop

    :goto_c
    goto :goto_13

    :goto_d
    goto :goto_20

    nop

    :goto_e
    goto :goto_17

    :goto_f
    goto :goto_21

    nop

    :goto_10
    invoke-virtual {v0, v2}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    goto :goto_1a

    nop

    :goto_11
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;

    goto :goto_c

    nop

    :goto_12
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;

    :goto_13
    goto :goto_b

    nop

    :goto_14
    goto :goto_f

    :goto_15
    goto :goto_22

    nop

    :goto_16
    add-int/lit8 v2, v2, -0x1

    :goto_17
    goto :goto_25

    nop

    :goto_18
    const/4 v1, 0x0

    goto :goto_1f

    nop

    :goto_19
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;

    goto :goto_1e

    nop

    :goto_1a
    invoke-virtual {v3}, Landroid/view/View;->getId()I

    move-result v3

    goto :goto_27

    nop

    :goto_1b
    invoke-virtual {v1}, Landroid/view/ViewStub;->inflate()Landroid/view/View;

    move-result-object v0

    goto :goto_11

    nop

    :goto_1c
    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    goto :goto_24

    nop

    :goto_1d
    if-eq v3, v4, :cond_2

    goto :goto_15

    :cond_2
    goto :goto_0

    nop

    :goto_1e
    return-object p0

    :goto_1f
    if-nez v0, :cond_3

    goto :goto_5

    :cond_3
    goto :goto_1c

    nop

    :goto_20
    sget v1, Lmiuix/appcompat/R$id;->search_mask:I

    goto :goto_9

    nop

    :goto_21
    if-nez v1, :cond_4

    goto :goto_d

    :cond_4
    goto :goto_1b

    nop

    :goto_22
    add-int/lit8 v2, v2, -0x1

    goto :goto_e

    nop

    :goto_23
    if-nez v0, :cond_5

    goto :goto_13

    :cond_5
    goto :goto_a

    nop

    :goto_24
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_4

    nop

    :goto_25
    if-gez v2, :cond_6

    goto :goto_f

    :cond_6
    goto :goto_10

    nop

    :goto_26
    const/4 v1, 0x0

    goto :goto_29

    nop

    :goto_27
    sget v4, Lmiuix/appcompat/R$id;->search_mask_vs:I

    goto :goto_1d

    nop

    :goto_28
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;

    goto :goto_2

    nop

    :goto_29
    invoke-virtual {v0, v1}, Landroid/widget/FrameLayout;->setVisibility(I)V

    :goto_2a
    goto :goto_19

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__getSplitActionBarContainer',
        'method': '.method protected getSplitActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;',
        'method_name': 'getSplitActionBarContainer',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSplitActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;', 'if-nez v0, :cond_2', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;', 'check-cast v0, Landroid/view/ViewGroup;', 'if-eqz v0, :cond_2', 'invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I'],
        'type': 'method_replace',
        'search': """.method protected getSplitActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;
    .registers 6

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSplitActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-nez v0, :cond_2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    if-eqz v0, :cond_2

    const/4 v1, 0x0

    :goto_1
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v2

    if-ge v1, v2, :cond_2

    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    invoke-virtual {v2}, Landroid/view/View;->getId()I

    move-result v3

    sget v4, Lmiuix/appcompat/R$id;->split_action_bar:I

    if-ne v3, v4, :cond_1

    instance-of v3, v2, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    if-eqz v3, :cond_1

    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    iput-object v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSplitActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_2

    :cond_1
    add-int/lit8 v1, v1, 0x1

    goto :goto_1

    :cond_2
    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSplitActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    return-object p0
.end method""",
        'replacement': """.method protected getSplitActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;
    .registers 6

    goto :goto_7

    nop

    :goto_0
    if-lt v1, v2, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_13

    nop

    :goto_1
    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_10

    nop

    :goto_2
    invoke-virtual {v0}, Ljava/lang/ref/WeakReference;->get()Ljava/lang/Object;

    move-result-object v0

    goto :goto_c

    nop

    :goto_3
    return-object p0

    :goto_4
    if-eq v3, v4, :cond_1

    goto :goto_1c

    :cond_1
    goto :goto_1a

    nop

    :goto_5
    goto :goto_b

    :goto_6
    goto :goto_a

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSplitActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_1d

    nop

    :goto_8
    invoke-virtual {v0}, Landroid/view/ViewGroup;->getChildCount()I

    move-result v2

    goto :goto_0

    nop

    :goto_9
    if-nez v0, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_2

    nop

    :goto_a
    const/4 v0, 0x0

    :goto_b
    goto :goto_11

    nop

    :goto_c
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_5

    nop

    :goto_d
    goto :goto_18

    :goto_e
    goto :goto_f

    nop

    :goto_f
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSplitActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_3

    nop

    :goto_10
    iput-object v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSplitActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_1b

    nop

    :goto_11
    if-nez v0, :cond_3

    goto :goto_e

    :cond_3
    goto :goto_17

    nop

    :goto_12
    sget v4, Lmiuix/appcompat/R$id;->split_action_bar:I

    goto :goto_4

    nop

    :goto_13
    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v2

    goto :goto_14

    nop

    :goto_14
    invoke-virtual {v2}, Landroid/view/View;->getId()I

    move-result v3

    goto :goto_12

    nop

    :goto_15
    add-int/lit8 v1, v1, 0x1

    goto :goto_d

    nop

    :goto_16
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOverlayView:Ljava/lang/ref/WeakReference;

    goto :goto_9

    nop

    :goto_17
    const/4 v1, 0x0

    :goto_18
    goto :goto_8

    nop

    :goto_19
    if-nez v3, :cond_4

    goto :goto_1c

    :cond_4
    goto :goto_1

    nop

    :goto_1a
    instance-of v3, v2, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_19

    nop

    :goto_1b
    goto :goto_e

    :goto_1c
    goto :goto_15

    nop

    :goto_1d
    if-eqz v0, :cond_5

    goto :goto_e

    :cond_5
    goto :goto_16

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__makeAnimation',
        'method': '.method protected makeAnimation()Landroid/animation/ObjectAnimator;',
        'method_name': 'makeAnimation',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->removeAllListeners()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;', 'invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->cancel()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;', 'invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setTarget(Ljava/lang/Object;)V', 'iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;'],
        'type': 'method_replace',
        'search': """.method protected makeAnimation()Landroid/animation/ObjectAnimator;
    .registers 4

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->removeAllListeners()V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->cancel()V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setTarget(Ljava/lang/Object;)V

    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    :cond_0
    const/4 v0, 0x2

    new-array v0, v0, [F

    fill-array-data v0, :array_0

    const-string v1, "AnimationProgress"

    invoke-static {p0, v1, v0}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v0

    invoke-virtual {v0, p0}, Landroid/animation/ObjectAnimator;->addListener(Landroid/animation/Animator$AnimatorListener;)V

    invoke-static {}, Lmiuix/internal/util/DeviceHelper;->isFeatureWholeAnim()Z

    move-result v1

    if-eqz v1, :cond_1

    const-wide/16 v1, 0x190

    goto :goto_0

    :cond_1
    const-wide/16 v1, 0x0

    :goto_0
    invoke-virtual {v0, v1, v2}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->obtainInterpolator()Landroid/animation/TimeInterpolator;

    move-result-object p0

    invoke-virtual {v0, p0}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    return-object v0

    nop

    :array_0
    .array-data 4
        0x0
        0x3f800000
    .end array-data
.end method""",
        'replacement': """.method protected makeAnimation()Landroid/animation/ObjectAnimator;
    .registers 4

    goto :goto_15

    nop

    :goto_0
    const-wide/16 v1, 0x0

    :goto_1
    goto :goto_19

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    goto :goto_13

    nop

    :goto_3
    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->removeAllListeners()V

    goto :goto_5

    nop

    :goto_4
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->obtainInterpolator()Landroid/animation/TimeInterpolator;

    move-result-object p0

    goto :goto_d

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    goto :goto_c

    nop

    :goto_6
    goto :goto_1

    :goto_7
    goto :goto_0

    nop

    :goto_8
    invoke-static {}, Lmiuix/internal/util/DeviceHelper;->isFeatureWholeAnim()Z

    move-result v1

    goto :goto_10

    nop

    :goto_9
    const/4 v0, 0x2

    goto :goto_a

    nop

    :goto_a
    new-array v0, v0, [F

    fill-array-data v0, :array_0

    goto :goto_14

    nop

    :goto_b
    invoke-virtual {v0, v1}, Landroid/animation/ObjectAnimator;->setTarget(Ljava/lang/Object;)V

    goto :goto_11

    nop

    :goto_c
    invoke-virtual {v0}, Landroid/animation/ObjectAnimator;->cancel()V

    goto :goto_2

    nop

    :goto_d
    invoke-virtual {v0, p0}, Landroid/animation/ObjectAnimator;->setInterpolator(Landroid/animation/TimeInterpolator;)V

    goto :goto_17

    nop

    :goto_e
    const-wide/16 v1, 0x190

    goto :goto_6

    nop

    :goto_f
    if-nez v0, :cond_0

    goto :goto_12

    :cond_0
    goto :goto_3

    nop

    :goto_10
    if-nez v1, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_e

    nop

    :goto_11
    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    :goto_12
    goto :goto_9

    nop

    :goto_13
    const/4 v1, 0x0

    goto :goto_b

    nop

    :goto_14
    const-string v1, "AnimationProgress"

    goto :goto_16

    nop

    :goto_15
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    goto :goto_f

    nop

    :goto_16
    invoke-static {p0, v1, v0}, Landroid/animation/ObjectAnimator;->ofFloat(Ljava/lang/Object;Ljava/lang/String;[F)Landroid/animation/ObjectAnimator;

    move-result-object v0

    goto :goto_18

    nop

    :goto_17
    return-object v0

    nop

    :array_0
    .array-data 4
        0x0
        0x3f800000
    .end array-data

    :goto_18
    invoke-virtual {v0, p0}, Landroid/animation/ObjectAnimator;->addListener(Landroid/animation/Animator$AnimatorListener;)V

    goto :goto_8

    nop

    :goto_19
    invoke-virtual {v0, v1, v2}, Landroid/animation/ObjectAnimator;->setDuration(J)Landroid/animation/ObjectAnimator;

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->resetLocationY()V', 'iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mFirstLayout:Z', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInputView:Landroid/widget/EditText;', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mTextCancel:Landroid/widget/TextView;', 'invoke-direct {p0, p1, v0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->resetTextSize(Landroid/widget/TextView;Landroid/widget/TextView;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->resetLocationY()V

    const/4 p1, 0x1

    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mFirstLayout:Z

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInputView:Landroid/widget/EditText;

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mTextCancel:Landroid/widget/TextView;

    invoke-direct {p0, p1, v0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->resetTextSize(Landroid/widget/TextView;Landroid/widget/TextView;)V

    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->resetLocationY()V

    goto :goto_6

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mTextCancel:Landroid/widget/TextView;

    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    invoke-direct {p0, p1, v0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->resetTextSize(Landroid/widget/TextView;Landroid/widget/TextView;)V

    goto :goto_2

    nop

    :goto_4
    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mFirstLayout:Z

    goto :goto_5

    nop

    :goto_5
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInputView:Landroid/widget/EditText;

    goto :goto_1

    nop

    :goto_6
    const/4 p1, 0x1

    goto :goto_4

    nop

    :goto_7
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->finishAnimation()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setLifecycleOwner(Landroidx/lifecycle/LifecycleOwner;)V', 'iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;', 'iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSplitActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 3

    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->finishAnimation()V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    invoke-virtual {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setLifecycleOwner(Landroidx/lifecycle/LifecycleOwner;)V

    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    :cond_0
    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSplitActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mHasPendingShowSoftInputTask:Z

    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->finishAnimation()V

    goto :goto_3

    nop

    :goto_2
    invoke-virtual {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setLifecycleOwner(Landroidx/lifecycle/LifecycleOwner;)V

    goto :goto_a

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_4

    nop

    :goto_4
    const/4 v1, 0x0

    goto :goto_c

    nop

    :goto_5
    const/4 v0, 0x0

    goto :goto_9

    nop

    :goto_6
    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSplitActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_5

    nop

    :goto_7
    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarContainer:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_6

    nop

    :goto_8
    return-void

    :goto_9
    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mHasPendingShowSoftInputTask:Z

    goto :goto_8

    nop

    :goto_a
    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    :goto_b
    goto :goto_7

    nop

    :goto_c
    if-nez v0, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'new-instance v0, Lmiuix/internal/util/ViewUtils$RelativePadding;', 'invoke-direct {v0, p0}, Lmiuix/internal/util/ViewUtils$RelativePadding;-><init>(Landroid/view/View;)V', 'iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getBackground()Landroid/graphics/drawable/Drawable;', 'if-eqz v0, :cond_0', 'new-instance v1, Landroid/graphics/Rect;', 'invoke-direct {v1}, Landroid/graphics/Rect;-><init>()V'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 5

    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    new-instance v0, Lmiuix/internal/util/ViewUtils$RelativePadding;

    invoke-direct {v0, p0}, Lmiuix/internal/util/ViewUtils$RelativePadding;-><init>(Landroid/view/View;)V

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getBackground()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    if-eqz v0, :cond_0

    new-instance v1, Landroid/graphics/Rect;

    invoke-direct {v1}, Landroid/graphics/Rect;-><init>()V

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->getPadding(Landroid/graphics/Rect;)Z

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;

    iget v2, v1, Landroid/graphics/Rect;->top:I

    iput v2, v0, Lmiuix/internal/util/ViewUtils$RelativePadding;->top:I

    iget v1, v1, Landroid/graphics/Rect;->bottom:I

    iput v1, v0, Lmiuix/internal/util/ViewUtils$RelativePadding;->bottom:I

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;

    iget v1, v0, Lmiuix/internal/util/ViewUtils$RelativePadding;->top:I

    if-nez v1, :cond_1

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInputPaddingTop:I

    iput v1, v0, Lmiuix/internal/util/ViewUtils$RelativePadding;->top:I

    :cond_1
    sget v0, Lmiuix/appcompat/R$id;->search_text_cancel:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mTextCancel:Landroid/widget/TextView;

    invoke-virtual {v0, p0}, Landroid/widget/TextView;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    new-instance v0, Lmiuix/internal/util/ViewUtils$RelativePadding;

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mTextCancel:Landroid/widget/TextView;

    invoke-direct {v0, v1}, Lmiuix/internal/util/ViewUtils$RelativePadding;-><init>(Landroid/view/View;)V

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCancelBtnInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;

    sget v0, Lmiuix/appcompat/R$id;->search_container:I

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSearchContainer:Landroid/view/ViewGroup;

    const/4 v1, 0x0

    invoke-static {v0, v1}, Lmiuix/view/CompatViewMethod;->setForceDarkAllowed(Landroid/view/View;Z)V

    const v0, 0x1020009

    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/EditText;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInputView:Landroid/widget/EditText;

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mTextCancel:Landroid/widget/TextView;

    invoke-direct {p0, v0, v2}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->resetTextSize(Landroid/widget/TextView;Landroid/widget/TextView;)V

    const/4 v0, 0x1

    new-array v0, v0, [Landroid/view/View;

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSearchContainer:Landroid/view/ViewGroup;

    aput-object v2, v0, v1

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->touch()Lmiuix/animation/ITouchStyle;

    move-result-object v0

    const/high16 v2, 0x3f800000

    new-array v3, v1, [Lmiuix/animation/ITouchStyle$TouchType;

    invoke-interface {v0, v2, v3}, Lmiuix/animation/ITouchStyle;->setScale(F[Lmiuix/animation/ITouchStyle$TouchType;)Lmiuix/animation/ITouchStyle;

    move-result-object v0

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInputView:Landroid/widget/EditText;

    new-array v1, v1, [Lmiuix/animation/base/AnimConfig;

    invoke-interface {v0, v2, v1}, Lmiuix/animation/ITouchStyle;->handleTouchOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;

    iget v0, v0, Lmiuix/internal/util/ViewUtils$RelativePadding;->top:I

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOriginalPaddingTop:I

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getContentView()Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_2

    invoke-virtual {v0}, Landroid/view/View;->getPaddingTop()I

    move-result v1

    iput v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mContentOriginPaddingTop:I

    invoke-virtual {v0}, Landroid/view/View;->getPaddingBottom()I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mContentOriginPaddingBottom:I

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 5

    goto :goto_8

    nop

    :goto_0
    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    goto :goto_24

    nop

    :goto_1
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInputPaddingTop:I

    goto :goto_2a

    nop

    :goto_2
    new-array v0, v0, [Landroid/view/View;

    goto :goto_23

    nop

    :goto_3
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mOriginalPaddingTop:I

    goto :goto_1e

    nop

    :goto_4
    invoke-direct {v0, p0}, Lmiuix/internal/util/ViewUtils$RelativePadding;-><init>(Landroid/view/View;)V

    goto :goto_21

    nop

    :goto_5
    const/high16 v2, 0x3f800000

    goto :goto_18

    nop

    :goto_6
    const/4 v1, 0x0

    goto :goto_38

    nop

    :goto_7
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mTextCancel:Landroid/widget/TextView;

    goto :goto_40

    nop

    :goto_8
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto :goto_22

    nop

    :goto_9
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_f

    nop

    :goto_a
    iput v2, v0, Lmiuix/internal/util/ViewUtils$RelativePadding;->top:I

    goto :goto_11

    nop

    :goto_b
    iget v1, v0, Lmiuix/internal/util/ViewUtils$RelativePadding;->top:I

    goto :goto_1a

    nop

    :goto_c
    invoke-direct {v0, v1}, Lmiuix/internal/util/ViewUtils$RelativePadding;-><init>(Landroid/view/View;)V

    goto :goto_39

    nop

    :goto_d
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSearchContainer:Landroid/view/ViewGroup;

    goto :goto_6

    nop

    :goto_e
    sget v0, Lmiuix/appcompat/R$id;->search_text_cancel:I

    goto :goto_9

    nop

    :goto_f
    check-cast v0, Landroid/widget/TextView;

    goto :goto_7

    nop

    :goto_10
    iget v2, v1, Landroid/graphics/Rect;->top:I

    goto :goto_a

    nop

    :goto_11
    iget v1, v1, Landroid/graphics/Rect;->bottom:I

    goto :goto_12

    nop

    :goto_12
    iput v1, v0, Lmiuix/internal/util/ViewUtils$RelativePadding;->bottom:I

    :goto_13
    goto :goto_2d

    nop

    :goto_14
    iget v0, v0, Lmiuix/internal/util/ViewUtils$RelativePadding;->top:I

    goto :goto_3

    nop

    :goto_15
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInputView:Landroid/widget/EditText;

    goto :goto_33

    nop

    :goto_16
    const/4 v0, 0x1

    goto :goto_2

    nop

    :goto_17
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_3d

    nop

    :goto_18
    new-array v3, v1, [Lmiuix/animation/ITouchStyle$TouchType;

    goto :goto_27

    nop

    :goto_19
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mTextCancel:Landroid/widget/TextView;

    goto :goto_37

    nop

    :goto_1a
    if-eqz v1, :cond_0

    goto :goto_2b

    :cond_0
    goto :goto_1

    nop

    :goto_1b
    iput v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mContentOriginPaddingTop:I

    goto :goto_36

    nop

    :goto_1c
    new-instance v0, Lmiuix/internal/util/ViewUtils$RelativePadding;

    goto :goto_34

    nop

    :goto_1d
    return-void

    :goto_1e
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getContentView()Landroid/view/View;

    move-result-object v0

    goto :goto_30

    nop

    :goto_1f
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getBackground()Landroid/graphics/drawable/Drawable;

    move-result-object v0

    goto :goto_29

    nop

    :goto_20
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;

    goto :goto_14

    nop

    :goto_21
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;

    goto :goto_1f

    nop

    :goto_22
    new-instance v0, Lmiuix/internal/util/ViewUtils$RelativePadding;

    goto :goto_4

    nop

    :goto_23
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mSearchContainer:Landroid/view/ViewGroup;

    goto :goto_25

    nop

    :goto_24
    invoke-interface {v0}, Lmiuix/animation/IFolme;->touch()Lmiuix/animation/ITouchStyle;

    move-result-object v0

    goto :goto_5

    nop

    :goto_25
    aput-object v2, v0, v1

    goto :goto_0

    nop

    :goto_26
    sget v0, Lmiuix/appcompat/R$id;->search_container:I

    goto :goto_28

    nop

    :goto_27
    invoke-interface {v0, v2, v3}, Lmiuix/animation/ITouchStyle;->setScale(F[Lmiuix/animation/ITouchStyle$TouchType;)Lmiuix/animation/ITouchStyle;

    move-result-object v0

    goto :goto_15

    nop

    :goto_28
    invoke-virtual {p0, v0}, Landroid/widget/FrameLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_31

    nop

    :goto_29
    if-nez v0, :cond_1

    goto :goto_13

    :cond_1
    goto :goto_32

    nop

    :goto_2a
    iput v1, v0, Lmiuix/internal/util/ViewUtils$RelativePadding;->top:I

    :goto_2b
    goto :goto_e

    nop

    :goto_2c
    invoke-interface {v0, v2, v1}, Lmiuix/animation/ITouchStyle;->handleTouchOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    goto :goto_20

    nop

    :goto_2d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;

    goto :goto_b

    nop

    :goto_2e
    invoke-direct {v1}, Landroid/graphics/Rect;-><init>()V

    goto :goto_3a

    nop

    :goto_2f
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInputView:Landroid/widget/EditText;

    goto :goto_19

    nop

    :goto_30
    if-nez v0, :cond_2

    goto :goto_3c

    :cond_2
    goto :goto_3e

    nop

    :goto_31
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_d

    nop

    :goto_32
    new-instance v1, Landroid/graphics/Rect;

    goto :goto_2e

    nop

    :goto_33
    new-array v1, v1, [Lmiuix/animation/base/AnimConfig;

    goto :goto_2c

    nop

    :goto_34
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mTextCancel:Landroid/widget/TextView;

    goto :goto_c

    nop

    :goto_35
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;

    goto :goto_10

    nop

    :goto_36
    invoke-virtual {v0}, Landroid/view/View;->getPaddingBottom()I

    move-result v0

    goto :goto_3b

    nop

    :goto_37
    invoke-direct {p0, v0, v2}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->resetTextSize(Landroid/widget/TextView;Landroid/widget/TextView;)V

    goto :goto_16

    nop

    :goto_38
    invoke-static {v0, v1}, Lmiuix/view/CompatViewMethod;->setForceDarkAllowed(Landroid/view/View;Z)V

    goto :goto_3f

    nop

    :goto_39
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCancelBtnInitPaddings:Lmiuix/internal/util/ViewUtils$RelativePadding;

    goto :goto_26

    nop

    :goto_3a
    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->getPadding(Landroid/graphics/Rect;)Z

    goto :goto_35

    nop

    :goto_3b
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mContentOriginPaddingBottom:I

    :goto_3c
    goto :goto_1d

    nop

    :goto_3d
    check-cast v0, Landroid/widget/EditText;

    goto :goto_2f

    nop

    :goto_3e
    invoke-virtual {v0}, Landroid/view/View;->getPaddingTop()I

    move-result v1

    goto :goto_1b

    nop

    :goto_3f
    const v0, 0x1020009

    goto :goto_17

    nop

    :goto_40
    invoke-virtual {v0, p0}, Landroid/widget/TextView;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    goto :goto_1c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;', 'if-eqz p1, :cond_0', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getTranslationY()F', 'invoke-virtual {p1, p2}, Landroid/view/View;->setTranslationY(F)V', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;', 'if-eqz p1, :cond_2', 'invoke-virtual {p1}, Landroid/animation/ObjectAnimator;->isRunning()Z'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 6

    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;

    if-eqz p1, :cond_0

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getTranslationY()F

    move-result p2

    int-to-float p4, p5

    add-float/2addr p2, p4

    int-to-float p3, p3

    sub-float/2addr p2, p3

    invoke-virtual {p1, p2}, Landroid/view/View;->setTranslationY(F)V

    :cond_0
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    if-eqz p1, :cond_2

    invoke-virtual {p1}, Landroid/animation/ObjectAnimator;->isRunning()Z

    move-result p1

    if-nez p1, :cond_1

    goto :goto_0

    :cond_1
    return-void

    :cond_2
    :goto_0
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    invoke-virtual {p1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object p1

    iget p1, p1, Landroid/util/DisplayMetrics;->density:F

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->updateExtraPadding(F)V

    iget p2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mExtraPadding:I

    invoke-direct {p0, p2, p1}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->updateViewPadding(IF)V

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 6

    goto :goto_12

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p1, p2}, Landroid/view/View;->setTranslationY(F)V

    :goto_2
    goto :goto_9

    nop

    :goto_3
    if-nez p1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_15

    nop

    :goto_4
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mDimView:Landroid/view/View;

    goto :goto_3

    nop

    :goto_5
    if-eqz p1, :cond_1

    goto :goto_11

    :cond_1
    goto :goto_10

    nop

    :goto_6
    sub-float/2addr p2, p3

    goto :goto_1

    nop

    :goto_7
    int-to-float p4, p5

    goto :goto_e

    nop

    :goto_8
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    goto :goto_14

    nop

    :goto_9
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mCurrentAnimation:Landroid/animation/ObjectAnimator;

    goto :goto_b

    nop

    :goto_a
    int-to-float p3, p3

    goto :goto_6

    nop

    :goto_b
    if-nez p1, :cond_2

    goto :goto_18

    :cond_2
    goto :goto_13

    nop

    :goto_c
    iget p1, p1, Landroid/util/DisplayMetrics;->density:F

    goto :goto_16

    nop

    :goto_d
    iget p2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mExtraPadding:I

    goto :goto_f

    nop

    :goto_e
    add-float/2addr p2, p4

    goto :goto_a

    nop

    :goto_f
    invoke-direct {p0, p2, p1}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->updateViewPadding(IF)V

    goto :goto_0

    nop

    :goto_10
    goto :goto_18

    :goto_11
    goto :goto_17

    nop

    :goto_12
    invoke-super/range {p0 .. p5}, Landroid/widget/FrameLayout;->onLayout(ZIIII)V

    goto :goto_4

    nop

    :goto_13
    invoke-virtual {p1}, Landroid/animation/ObjectAnimator;->isRunning()Z

    move-result p1

    goto :goto_5

    nop

    :goto_14
    invoke-virtual {p1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object p1

    goto :goto_c

    nop

    :goto_15
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getTranslationY()F

    move-result p2

    goto :goto_7

    nop

    :goto_16
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->updateExtraPadding(F)V

    goto :goto_d

    nop

    :goto_17
    return-void

    :goto_18
    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__pollViews',
        'method': '.method protected pollViews()V',
        'method_name': 'pollViews',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getActionBarView()Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getSplitActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected pollViews()V
    .registers 1

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getActionBarView()Lmiuix/appcompat/internal/app/widget/ActionBarView;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getSplitActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    return-void
.end method""",
        'replacement': """.method protected pollViews()V
    .registers 1

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getSplitActionBarContainer()Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_3

    nop

    :goto_2
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getActionBarView()Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_0

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__setContentViewPadding',
        'method': '.method protected setContentViewPadding(II)V',
        'method_name': 'setContentViewPadding',
        'method_anchors': ['invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getContentView()Landroid/view/View;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Landroid/view/View;->getPaddingStart()I', 'iget v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mContentOriginPaddingTop:I', 'invoke-virtual {v0}, Landroid/view/View;->getPaddingEnd()I', 'iget p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mContentOriginPaddingBottom:I', 'invoke-virtual {v0, v1, p1, v2, p2}, Landroid/view/View;->setPaddingRelative(IIII)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setContentViewPadding(II)V
    .registers 6

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getContentView()Landroid/view/View;

    move-result-object v0

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Landroid/view/View;->getPaddingStart()I

    move-result v1

    iget v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mContentOriginPaddingTop:I

    add-int/2addr p1, v2

    invoke-virtual {v0}, Landroid/view/View;->getPaddingEnd()I

    move-result v2

    iget p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mContentOriginPaddingBottom:I

    add-int/2addr p2, p0

    invoke-virtual {v0, v1, p1, v2, p2}, Landroid/view/View;->setPaddingRelative(IIII)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected setContentViewPadding(II)V
    .registers 6

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {v0, v1, p1, v2, p2}, Landroid/view/View;->setPaddingRelative(IIII)V

    :goto_1
    goto :goto_9

    nop

    :goto_2
    iget p0, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mContentOriginPaddingBottom:I

    goto :goto_5

    nop

    :goto_3
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getContentView()Landroid/view/View;

    move-result-object v0

    goto :goto_a

    nop

    :goto_4
    invoke-virtual {v0}, Landroid/view/View;->getPaddingEnd()I

    move-result v2

    goto :goto_2

    nop

    :goto_5
    add-int/2addr p2, p0

    goto :goto_0

    nop

    :goto_6
    invoke-virtual {v0}, Landroid/view/View;->getPaddingStart()I

    move-result v1

    goto :goto_7

    nop

    :goto_7
    iget v2, p0, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->mContentOriginPaddingTop:I

    goto :goto_8

    nop

    :goto_8
    add-int/2addr p1, v2

    goto :goto_4

    nop

    :goto_9
    return-void

    :goto_a
    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_SearchActionModeView__setContentViewTranslation',
        'method': '.method protected setContentViewTranslation(F)V',
        'method_name': 'setContentViewTranslation',
        'method_anchors': ['invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getContentView()Landroid/view/View;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setContentViewTranslation(F)V
    .registers 2

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getContentView()Landroid/view/View;

    move-result-object p0

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected setContentViewTranslation(F)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1}, Landroid/view/View;->setTranslationY(F)V

    :goto_2
    goto :goto_4

    nop

    :goto_3
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/SearchActionModeView;->getContentView()Landroid/view/View;

    move-result-object p0

    goto :goto_0

    nop

    :goto_4
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
