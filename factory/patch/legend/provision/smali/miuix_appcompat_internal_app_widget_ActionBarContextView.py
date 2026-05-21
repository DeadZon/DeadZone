TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/ActionBarContextView.smali'
CLASS_FALLBACK_NAMES = ['ActionBarContextView.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/internal/app/widget/AbsActionBarView;', '.implements Lmiuix/appcompat/internal/app/widget/ActionModeView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__getActionBarStyle',
        'method': '.method getActionBarStyle()I',
        'method_name': 'getActionBarStyle',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method getActionBarStyle()I
    .registers 1

    const p0, 0x1010394

    return p0
.end method""",
        'replacement': """.method getActionBarStyle()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const p0, 0x1010394

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__cancelAnimation',
        'method': '.method protected cancelAnimation()V',
        'method_name': 'cancelAnimation',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V', 'iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;', 'invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->stopSplitMenuAnimation()V', 'invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setSplitAnimating(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected cancelAnimation()V
    .registers 2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    :cond_0
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->stopSplitMenuAnimation()V

    const/4 v0, 0x0

    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setSplitAnimating(Z)V

    return-void
.end method""",
        'replacement': """.method protected cancelAnimation()V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_3

    nop

    :goto_1
    const/4 v0, 0x0

    goto :goto_4

    nop

    :goto_2
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->stopSplitMenuAnimation()V

    goto :goto_6

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_9

    nop

    :goto_4
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    :goto_5
    goto :goto_2

    nop

    :goto_6
    const/4 v0, 0x0

    goto :goto_7

    nop

    :goto_7
    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setSplitAnimating(Z)V

    goto :goto_8

    nop

    :goto_8
    return-void

    :goto_9
    invoke-virtual {v0}, Lmiuix/animation/physics/DynamicAnimation;->cancel()V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__endAnimation',
        'method': '.method protected endAnimation()V',
        'method_name': 'endAnimation',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Lmiuix/animation/physics/SpringAnimation;->skipToEnd()V', 'iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;', 'invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->stopSplitMenuAnimation()V', 'invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setSplitAnimating(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected endAnimation()V
    .registers 2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Lmiuix/animation/physics/SpringAnimation;->skipToEnd()V

    const/4 v0, 0x0

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    :cond_0
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->stopSplitMenuAnimation()V

    const/4 v0, 0x0

    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setSplitAnimating(Z)V

    return-void
.end method""",
        'replacement': """.method protected endAnimation()V
    .registers 2

    goto :goto_5

    nop

    :goto_0
    return-void

    :goto_1
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_2
    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setSplitAnimating(Z)V

    goto :goto_0

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_7

    nop

    :goto_4
    const/4 v0, 0x0

    goto :goto_8

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_3

    nop

    :goto_6
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->stopSplitMenuAnimation()V

    goto :goto_1

    nop

    :goto_7
    invoke-virtual {v0}, Lmiuix/animation/physics/SpringAnimation;->skipToEnd()V

    goto :goto_4

    nop

    :goto_8
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    :goto_9
    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__generateDefaultLayoutParams',
        'method': '.method protected generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;',
        'method_name': 'generateDefaultLayoutParams',
        'method_anchors': ['new-instance p0, Landroid/view/ViewGroup$MarginLayoutParams;', 'invoke-direct {p0, v0, v1}, Landroid/view/ViewGroup$MarginLayoutParams;-><init>(II)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;
    .registers 3

    new-instance p0, Landroid/view/ViewGroup$MarginLayoutParams;

    const/4 v0, -0x1

    const/4 v1, -0x2

    invoke-direct {p0, v0, v1}, Landroid/view/ViewGroup$MarginLayoutParams;-><init>(II)V

    return-object p0
.end method""",
        'replacement': """.method protected generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;
    .registers 3

    goto :goto_4

    nop

    :goto_0
    return-object p0

    :goto_1
    const/4 v0, -0x1

    goto :goto_3

    nop

    :goto_2
    invoke-direct {p0, v0, v1}, Landroid/view/ViewGroup$MarginLayoutParams;-><init>(II)V

    goto :goto_0

    nop

    :goto_3
    const/4 v1, -0x2

    goto :goto_2

    nop

    :goto_4
    new-instance p0, Landroid/view/ViewGroup$MarginLayoutParams;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__initTitle',
        'method': '.method protected initTitle()V',
        'method_name': 'initTitle',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;', 'if-nez v0, :cond_3', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;', 'invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;', 'sget v4, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_mode_title_item:I', 'invoke-virtual {v0, v4, p0, v3}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;', 'check-cast v0, Landroid/widget/LinearLayout;', 'iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;'],
        'type': 'method_replace',
        'search': """.method protected initTitle()V
    .registers 9

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    const/high16 v1, 0x3f800000

    const/4 v2, 0x1

    const/4 v3, 0x0

    if-nez v0, :cond_3

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    sget v4, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_mode_title_item:I

    invoke-virtual {v0, v4, p0, v3}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/LinearLayout;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    const v4, 0x1020019

    invoke-virtual {v0, v4}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/Button;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    const v4, 0x102001a

    invoke-virtual {v0, v4}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/Button;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    const/high16 v4, 0x42700000

    const v5, 0x3f19999a

    if-eqz v0, :cond_0

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mOnMenuItemClickListener:Landroid/view/View$OnClickListener;

    invoke-virtual {v0, v6}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    new-array v0, v2, [Landroid/view/View;

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    aput-object v6, v0, v3

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->touch()Lmiuix/animation/ITouchStyle;

    move-result-object v0

    new-array v6, v3, [Lmiuix/animation/ITouchStyle$TouchType;

    invoke-interface {v0, v1, v6}, Lmiuix/animation/ITouchStyle;->setScale(F[Lmiuix/animation/ITouchStyle$TouchType;)Lmiuix/animation/ITouchStyle;

    move-result-object v0

    new-array v6, v3, [Lmiuix/animation/ITouchStyle$TouchType;

    invoke-interface {v0, v5, v6}, Lmiuix/animation/ITouchStyle;->setAlpha(F[Lmiuix/animation/ITouchStyle$TouchType;)Lmiuix/animation/ITouchStyle;

    move-result-object v0

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    new-array v7, v3, [Lmiuix/animation/base/AnimConfig;

    invoke-interface {v0, v6, v7}, Lmiuix/animation/ITouchStyle;->handleTouchOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    new-array v0, v2, [Landroid/view/View;

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    aput-object v6, v0, v3

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    invoke-interface {v0, v4}, Lmiuix/animation/IHoverStyle;->setFeedbackRadius(F)V

    new-array v0, v2, [Landroid/view/View;

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    aput-object v6, v0, v3

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    sget-object v6, Lmiuix/animation/IHoverStyle$HoverEffect;->FLOATED_WRAPPED:Lmiuix/animation/IHoverStyle$HoverEffect;

    invoke-interface {v0, v6}, Lmiuix/animation/IHoverStyle;->setEffect(Lmiuix/animation/IHoverStyle$HoverEffect;)Lmiuix/animation/IHoverStyle;

    move-result-object v0

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    new-array v7, v3, [Lmiuix/animation/base/AnimConfig;

    invoke-interface {v0, v6, v7}, Lmiuix/animation/IHoverStyle;->handleHoverOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    if-eqz v0, :cond_1

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mOnMenuItemClickListener:Landroid/view/View$OnClickListener;

    invoke-virtual {v0, v6}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    new-array v0, v2, [Landroid/view/View;

    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    aput-object v6, v0, v3

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->touch()Lmiuix/animation/ITouchStyle;

    move-result-object v0

    new-array v6, v3, [Lmiuix/animation/ITouchStyle$TouchType;

    invoke-interface {v0, v1, v6}, Lmiuix/animation/ITouchStyle;->setScale(F[Lmiuix/animation/ITouchStyle$TouchType;)Lmiuix/animation/ITouchStyle;

    move-result-object v0

    new-array v6, v3, [Lmiuix/animation/ITouchStyle$TouchType;

    invoke-interface {v0, v5, v6}, Lmiuix/animation/ITouchStyle;->setAlpha(F[Lmiuix/animation/ITouchStyle$TouchType;)Lmiuix/animation/ITouchStyle;

    move-result-object v0

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    new-array v6, v3, [Lmiuix/animation/base/AnimConfig;

    invoke-interface {v0, v5, v6}, Lmiuix/animation/ITouchStyle;->handleTouchOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    new-array v0, v2, [Landroid/view/View;

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    aput-object v5, v0, v3

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    invoke-interface {v0, v4}, Lmiuix/animation/IHoverStyle;->setFeedbackRadius(F)V

    new-array v0, v2, [Landroid/view/View;

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    aput-object v4, v0, v3

    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    sget-object v4, Lmiuix/animation/IHoverStyle$HoverEffect;->FLOATED_WRAPPED:Lmiuix/animation/IHoverStyle$HoverEffect;

    invoke-interface {v0, v4}, Lmiuix/animation/IHoverStyle;->setEffect(Lmiuix/animation/IHoverStyle$HoverEffect;)Lmiuix/animation/IHoverStyle;

    move-result-object v0

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    new-array v5, v3, [Lmiuix/animation/base/AnimConfig;

    invoke-interface {v0, v4, v5}, Lmiuix/animation/IHoverStyle;->handleHoverOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    const v4, 0x1020016

    invoke-virtual {v0, v4}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleView:Landroid/widget/TextView;

    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleStyleRes:I

    if-eqz v4, :cond_2

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v4

    iget v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleStyleRes:I

    invoke-virtual {v0, v4, v5}, Landroid/widget/TextView;->setTextAppearance(Landroid/content/Context;I)V

    :cond_2
    new-instance v0, Landroid/widget/TextView;

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v4

    invoke-direct {v0, v4}, Landroid/widget/TextView;-><init>(Landroid/content/Context;)V

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleStyleRes:I

    if-eqz v4, :cond_3

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v4

    iget v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleStyleRes:I

    invoke-virtual {v0, v4, v5}, Landroid/widget/TextView;->setTextAppearance(Landroid/content/Context;I)V

    invoke-static {}, Lmiuix/core/util/RomUtils;->getHyperOsVersion()I

    move-result v0

    if-gt v0, v2, :cond_3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    invoke-static {v0}, Lmiuix/theme/Typography;->applyMiSansLight(Landroid/widget/TextView;)V

    :cond_3
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleView:Landroid/widget/TextView;

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitle:Ljava/lang/CharSequence;

    invoke-virtual {v0, v4}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitle:Ljava/lang/CharSequence;

    invoke-virtual {v0, v4}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMainContainer:Landroid/view/View;

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleView:Landroid/widget/TextView;

    invoke-virtual {v0, v4}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->attachViews(Landroid/view/View;)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitle:Ljava/lang/CharSequence;

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    const/16 v5, 0x8

    if-nez v0, :cond_4

    move v6, v3

    goto :goto_0

    :cond_4
    move v6, v5

    :goto_0
    invoke-virtual {v4, v6}, Landroid/widget/LinearLayout;->setVisibility(I)V

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    if-nez v0, :cond_5

    move v5, v3

    :cond_5
    invoke-virtual {v4, v5}, Landroid/widget/TextView;->setVisibility(I)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    invoke-virtual {v0}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    if-nez v0, :cond_6

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    invoke-virtual {p0, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V

    :cond_6
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    invoke-virtual {v0}, Landroid/widget/TextView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    if-nez v0, :cond_7

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    sget v4, Lmiuix/appcompat/R$id;->action_context_bar_expand_title:I

    invoke-virtual {v0, v4}, Landroid/widget/TextView;->setId(I)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    invoke-virtual {v0, v4}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V

    :cond_7
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    if-nez v0, :cond_8

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p0, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V

    :cond_8
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    const/4 v4, 0x0

    if-nez v0, :cond_9

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    invoke-virtual {v0, v1, v3, v3}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FII)V

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    invoke-virtual {p0, v4, v3, v3}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FII)V

    return-void

    :cond_9
    if-ne v0, v2, :cond_a

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    const/16 v2, 0x14

    invoke-virtual {v0, v4, v3, v2}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FII)V

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    invoke-virtual {p0, v1, v3, v3}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FII)V

    :cond_a
    return-void
.end method""",
        'replacement': """.method protected initTitle()V
    .registers 9

    goto :goto_81

    nop

    :goto_0
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleView:Landroid/widget/TextView;

    goto :goto_70

    nop

    :goto_1
    aput-object v4, v0, v3

    goto :goto_12

    nop

    :goto_2
    const/4 v3, 0x0

    goto :goto_6b

    nop

    :goto_3
    new-array v0, v2, [Landroid/view/View;

    goto :goto_6e

    nop

    :goto_4
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitle:Ljava/lang/CharSequence;

    goto :goto_43

    nop

    :goto_5
    invoke-virtual {v0, v4, v3, v2}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FII)V

    goto :goto_7f

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v4

    goto :goto_95

    nop

    :goto_7
    if-eqz v0, :cond_0

    goto :goto_88

    :cond_0
    goto :goto_37

    nop

    :goto_8
    invoke-virtual {v0, v4}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_26

    nop

    :goto_9
    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    goto :goto_a1

    nop

    :goto_a
    invoke-virtual {v0, v4}, Landroid/widget/FrameLayout;->addView(Landroid/view/View;)V

    :goto_b
    goto :goto_3c

    nop

    :goto_c
    new-array v0, v2, [Landroid/view/View;

    goto :goto_73

    nop

    :goto_d
    invoke-interface {v0, v4}, Lmiuix/animation/IHoverStyle;->setFeedbackRadius(F)V

    goto :goto_a3

    nop

    :goto_e
    new-array v0, v2, [Landroid/view/View;

    goto :goto_49

    nop

    :goto_f
    check-cast v0, Landroid/widget/LinearLayout;

    goto :goto_3a

    nop

    :goto_10
    invoke-interface {v0, v6}, Lmiuix/animation/IHoverStyle;->setEffect(Lmiuix/animation/IHoverStyle$HoverEffect;)Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_75

    nop

    :goto_11
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    goto :goto_4c

    nop

    :goto_12
    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    goto :goto_72

    nop

    :goto_13
    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    goto :goto_4f

    nop

    :goto_14
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    goto :goto_1f

    nop

    :goto_15
    invoke-virtual {v4, v5}, Landroid/widget/TextView;->setVisibility(I)V

    goto :goto_56

    nop

    :goto_16
    invoke-interface {v0}, Lmiuix/animation/IFolme;->touch()Lmiuix/animation/ITouchStyle;

    move-result-object v0

    goto :goto_66

    nop

    :goto_17
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    goto :goto_a2

    nop

    :goto_18
    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    goto :goto_93

    nop

    :goto_19
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    goto :goto_77

    nop

    :goto_1a
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    goto :goto_4

    nop

    :goto_1b
    new-array v7, v3, [Lmiuix/animation/base/AnimConfig;

    goto :goto_5b

    nop

    :goto_1c
    check-cast v0, Landroid/widget/Button;

    goto :goto_52

    nop

    :goto_1d
    invoke-interface {v0, v1, v6}, Lmiuix/animation/ITouchStyle;->setScale(F[Lmiuix/animation/ITouchStyle$TouchType;)Lmiuix/animation/ITouchStyle;

    move-result-object v0

    goto :goto_53

    nop

    :goto_1e
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    goto :goto_71

    nop

    :goto_1f
    const v4, 0x1020016

    goto :goto_8

    nop

    :goto_20
    invoke-virtual {v0, v4}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_98

    nop

    :goto_21
    invoke-virtual {v0, v4}, Landroid/widget/TextView;->setId(I)V

    goto :goto_99

    nop

    :goto_22
    invoke-interface {v0, v5, v6}, Lmiuix/animation/ITouchStyle;->handleTouchOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    goto :goto_e

    nop

    :goto_23
    if-eqz v0, :cond_1

    goto :goto_7d

    :cond_1
    goto :goto_5a

    nop

    :goto_24
    invoke-virtual {v0, v4}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->attachViews(Landroid/view/View;)V

    goto :goto_9f

    nop

    :goto_25
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mOnMenuItemClickListener:Landroid/view/View$OnClickListener;

    goto :goto_40

    nop

    :goto_26
    check-cast v0, Landroid/widget/TextView;

    goto :goto_0

    nop

    :goto_27
    invoke-interface {v0, v4, v5}, Lmiuix/animation/IHoverStyle;->handleHoverOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    :goto_28
    goto :goto_14

    nop

    :goto_29
    move v5, v3

    :goto_2a
    goto :goto_15

    nop

    :goto_2b
    new-array v5, v3, [Lmiuix/animation/base/AnimConfig;

    goto :goto_27

    nop

    :goto_2c
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    goto :goto_2b

    nop

    :goto_2d
    move v6, v5

    :goto_2e
    goto :goto_a7

    nop

    :goto_2f
    invoke-virtual {v0, v1, v3, v3}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FII)V

    goto :goto_9c

    nop

    :goto_30
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleView:Landroid/widget/TextView;

    goto :goto_24

    nop

    :goto_31
    invoke-direct {v0, v4}, Landroid/widget/TextView;-><init>(Landroid/content/Context;)V

    goto :goto_9b

    nop

    :goto_32
    invoke-interface {v0, v1, v6}, Lmiuix/animation/ITouchStyle;->setScale(F[Lmiuix/animation/ITouchStyle$TouchType;)Lmiuix/animation/ITouchStyle;

    move-result-object v0

    goto :goto_b1

    nop

    :goto_33
    new-array v6, v3, [Lmiuix/animation/base/AnimConfig;

    goto :goto_22

    nop

    :goto_34
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v4

    goto :goto_9d

    nop

    :goto_35
    invoke-virtual {v0}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_50

    nop

    :goto_36
    const/16 v2, 0x14

    goto :goto_5

    nop

    :goto_37
    move v6, v3

    goto :goto_87

    nop

    :goto_38
    invoke-virtual {p0, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V

    :goto_39
    goto :goto_91

    nop

    :goto_3a
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    goto :goto_a6

    nop

    :goto_3b
    invoke-interface {v0, v4}, Lmiuix/animation/IHoverStyle;->setEffect(Lmiuix/animation/IHoverStyle$HoverEffect;)Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_2c

    nop

    :goto_3c
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_47

    nop

    :goto_3d
    if-eqz v0, :cond_2

    goto :goto_2a

    :cond_2
    goto :goto_29

    nop

    :goto_3e
    invoke-interface {v0, v5, v6}, Lmiuix/animation/ITouchStyle;->setAlpha(F[Lmiuix/animation/ITouchStyle$TouchType;)Lmiuix/animation/ITouchStyle;

    move-result-object v0

    goto :goto_a0

    nop

    :goto_3f
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_30

    nop

    :goto_40
    invoke-virtual {v0, v6}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    goto :goto_c

    nop

    :goto_41
    const v4, 0x102001a

    goto :goto_20

    nop

    :goto_42
    aput-object v6, v0, v3

    goto :goto_85

    nop

    :goto_43
    invoke-virtual {v0, v4}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    goto :goto_19

    nop

    :goto_44
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    goto :goto_1e

    nop

    :goto_45
    invoke-interface {v0, v6, v7}, Lmiuix/animation/ITouchStyle;->handleTouchOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    goto :goto_3

    nop

    :goto_46
    new-array v0, v2, [Landroid/view/View;

    goto :goto_51

    nop

    :goto_47
    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_23

    nop

    :goto_48
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    goto :goto_a

    nop

    :goto_49
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    goto :goto_8a

    nop

    :goto_4a
    invoke-interface {v0, v5, v6}, Lmiuix/animation/ITouchStyle;->setAlpha(F[Lmiuix/animation/ITouchStyle$TouchType;)Lmiuix/animation/ITouchStyle;

    move-result-object v0

    goto :goto_55

    nop

    :goto_4b
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    goto :goto_41

    nop

    :goto_4c
    if-nez v0, :cond_3

    goto :goto_28

    :cond_3
    goto :goto_25

    nop

    :goto_4d
    invoke-virtual {v0, v4}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

    goto :goto_1a

    nop

    :goto_4e
    invoke-virtual {v0, v6}, Landroid/widget/Button;->setOnClickListener(Landroid/view/View$OnClickListener;)V

    goto :goto_46

    nop

    :goto_4f
    invoke-interface {v0}, Lmiuix/animation/IFolme;->touch()Lmiuix/animation/ITouchStyle;

    move-result-object v0

    goto :goto_62

    nop

    :goto_50
    if-eqz v0, :cond_4

    goto :goto_39

    :cond_4
    goto :goto_6c

    nop

    :goto_51
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    goto :goto_42

    nop

    :goto_52
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    goto :goto_4b

    nop

    :goto_53
    new-array v6, v3, [Lmiuix/animation/ITouchStyle$TouchType;

    goto :goto_3e

    nop

    :goto_54
    if-nez v0, :cond_5

    goto :goto_5c

    :cond_5
    goto :goto_a8

    nop

    :goto_55
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    goto :goto_33

    nop

    :goto_56
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    goto :goto_35

    nop

    :goto_57
    aput-object v6, v0, v3

    goto :goto_9

    nop

    :goto_58
    if-nez v4, :cond_6

    goto :goto_97

    :cond_6
    goto :goto_34

    nop

    :goto_59
    invoke-static {}, Lmiuix/core/util/RomUtils;->getHyperOsVersion()I

    move-result v0

    goto :goto_68

    nop

    :goto_5a
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_7c

    nop

    :goto_5b
    invoke-interface {v0, v6, v7}, Lmiuix/animation/IHoverStyle;->handleHoverOf(Landroid/view/View;[Lmiuix/animation/base/AnimConfig;)V

    :goto_5c
    goto :goto_11

    nop

    :goto_5d
    invoke-virtual {v0, v4}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_1c

    nop

    :goto_5e
    sget-object v6, Lmiuix/animation/IHoverStyle$HoverEffect;->FLOATED_WRAPPED:Lmiuix/animation/IHoverStyle$HoverEffect;

    goto :goto_10

    nop

    :goto_5f
    return-void

    :goto_60
    goto :goto_ab

    nop

    :goto_61
    invoke-virtual {v0}, Landroid/widget/TextView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_74

    nop

    :goto_62
    new-array v6, v3, [Lmiuix/animation/ITouchStyle$TouchType;

    goto :goto_32

    nop

    :goto_63
    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    goto :goto_ad

    nop

    :goto_64
    aput-object v6, v0, v3

    goto :goto_13

    nop

    :goto_65
    if-eqz v0, :cond_7

    goto :goto_60

    :cond_7
    goto :goto_aa

    nop

    :goto_66
    new-array v6, v3, [Lmiuix/animation/ITouchStyle$TouchType;

    goto :goto_1d

    nop

    :goto_67
    const/high16 v1, 0x3f800000

    goto :goto_9a

    nop

    :goto_68
    if-le v0, v2, :cond_8

    goto :goto_97

    :cond_8
    goto :goto_8d

    nop

    :goto_69
    new-array v7, v3, [Lmiuix/animation/base/AnimConfig;

    goto :goto_45

    nop

    :goto_6a
    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleStyleRes:I

    goto :goto_58

    nop

    :goto_6b
    if-eqz v0, :cond_9

    goto :goto_97

    :cond_9
    goto :goto_b0

    nop

    :goto_6c
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    goto :goto_38

    nop

    :goto_6d
    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    goto :goto_82

    nop

    :goto_6e
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    goto :goto_57

    nop

    :goto_6f
    new-array v0, v2, [Landroid/view/View;

    goto :goto_b2

    nop

    :goto_70
    iget v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleStyleRes:I

    goto :goto_7a

    nop

    :goto_71
    const/high16 v4, 0x42700000

    goto :goto_a4

    nop

    :goto_72
    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_86

    nop

    :goto_73
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    goto :goto_64

    nop

    :goto_74
    if-eqz v0, :cond_a

    goto :goto_b

    :cond_a
    goto :goto_17

    nop

    :goto_75
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    goto :goto_1b

    nop

    :goto_76
    invoke-virtual {v0, v4, p0, v3}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;Z)Landroid/view/View;

    move-result-object v0

    goto :goto_f

    nop

    :goto_77
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMainContainer:Landroid/view/View;

    goto :goto_3f

    nop

    :goto_78
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    goto :goto_94

    nop

    :goto_79
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_36

    nop

    :goto_7a
    if-nez v4, :cond_b

    goto :goto_af

    :cond_b
    goto :goto_6

    nop

    :goto_7b
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v4

    goto :goto_31

    nop

    :goto_7c
    invoke-virtual {p0, v0}, Landroid/view/ViewGroup;->addView(Landroid/view/View;)V

    :goto_7d
    goto :goto_89

    nop

    :goto_7e
    new-instance v0, Landroid/widget/TextView;

    goto :goto_7b

    nop

    :goto_7f
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_8e

    nop

    :goto_80
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleView:Landroid/widget/TextView;

    goto :goto_a5

    nop

    :goto_81
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    goto :goto_67

    nop

    :goto_82
    sget v4, Lmiuix/appcompat/R$layout;->miuix_appcompat_action_mode_title_item:I

    goto :goto_76

    nop

    :goto_83
    invoke-virtual {v0, v4, v5}, Landroid/widget/TextView;->setTextAppearance(Landroid/content/Context;I)V

    goto :goto_59

    nop

    :goto_84
    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    goto :goto_a9

    nop

    :goto_85
    invoke-static {v0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object v0

    goto :goto_16

    nop

    :goto_86
    sget-object v4, Lmiuix/animation/IHoverStyle$HoverEffect;->FLOATED_WRAPPED:Lmiuix/animation/IHoverStyle$HoverEffect;

    goto :goto_3b

    nop

    :goto_87
    goto :goto_2e

    :goto_88
    goto :goto_2d

    nop

    :goto_89
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    goto :goto_ac

    nop

    :goto_8a
    aput-object v5, v0, v3

    goto :goto_63

    nop

    :goto_8b
    const/16 v5, 0x8

    goto :goto_7

    nop

    :goto_8c
    return-void

    :goto_8d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    goto :goto_96

    nop

    :goto_8e
    invoke-virtual {p0, v1, v3, v3}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FII)V

    :goto_8f
    goto :goto_8c

    nop

    :goto_90
    invoke-interface {v0, v4}, Lmiuix/animation/IHoverStyle;->setFeedbackRadius(F)V

    goto :goto_6f

    nop

    :goto_91
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    goto :goto_61

    nop

    :goto_92
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    goto :goto_3d

    nop

    :goto_93
    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_5e

    nop

    :goto_94
    aput-object v6, v0, v3

    goto :goto_18

    nop

    :goto_95
    iget v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleStyleRes:I

    goto :goto_ae

    nop

    :goto_96
    invoke-static {v0}, Lmiuix/theme/Typography;->applyMiSansLight(Landroid/widget/TextView;)V

    :goto_97
    goto :goto_80

    nop

    :goto_98
    check-cast v0, Landroid/widget/Button;

    goto :goto_44

    nop

    :goto_99
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_48

    nop

    :goto_9a
    const/4 v2, 0x1

    goto :goto_2

    nop

    :goto_9b
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleView:Landroid/widget/TextView;

    goto :goto_6a

    nop

    :goto_9c
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_9e

    nop

    :goto_9d
    iget v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTitleStyleRes:I

    goto :goto_83

    nop

    :goto_9e
    invoke-virtual {p0, v4, v3, v3}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FII)V

    goto :goto_5f

    nop

    :goto_9f
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitle:Ljava/lang/CharSequence;

    goto :goto_84

    nop

    :goto_a0
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton1:Landroid/widget/Button;

    goto :goto_69

    nop

    :goto_a1
    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_d

    nop

    :goto_a2
    sget v4, Lmiuix/appcompat/R$id;->action_context_bar_expand_title:I

    goto :goto_21

    nop

    :goto_a3
    new-array v0, v2, [Landroid/view/View;

    goto :goto_78

    nop

    :goto_a4
    const v5, 0x3f19999a

    goto :goto_54

    nop

    :goto_a5
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitle:Ljava/lang/CharSequence;

    goto :goto_4d

    nop

    :goto_a6
    const v4, 0x1020019

    goto :goto_5d

    nop

    :goto_a7
    invoke-virtual {v4, v6}, Landroid/widget/LinearLayout;->setVisibility(I)V

    goto :goto_92

    nop

    :goto_a8
    iget-object v6, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mOnMenuItemClickListener:Landroid/view/View$OnClickListener;

    goto :goto_4e

    nop

    :goto_a9
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleLayout:Landroid/widget/LinearLayout;

    goto :goto_8b

    nop

    :goto_aa
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_2f

    nop

    :goto_ab
    if-eq v0, v2, :cond_c

    goto :goto_8f

    :cond_c
    goto :goto_79

    nop

    :goto_ac
    const/4 v4, 0x0

    goto :goto_65

    nop

    :goto_ad
    invoke-interface {v0}, Lmiuix/animation/IFolme;->hover()Lmiuix/animation/IHoverStyle;

    move-result-object v0

    goto :goto_90

    nop

    :goto_ae
    invoke-virtual {v0, v4, v5}, Landroid/widget/TextView;->setTextAppearance(Landroid/content/Context;I)V

    :goto_af
    goto :goto_7e

    nop

    :goto_b0
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_6d

    nop

    :goto_b1
    new-array v6, v3, [Lmiuix/animation/ITouchStyle$TouchType;

    goto :goto_4a

    nop

    :goto_b2
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__makeContextViewsShowHide',
        'method': '.method protected makeContextViewsShowHide(Z)V',
        'method_name': 'makeContextViewsShowHide',
        'method_anchors': ['if-eqz p1, :cond_0', 'invoke-virtual {p0, v2}, Landroid/view/ViewGroup;->setAlpha(F)V', 'iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitActionBarEnable:Z', 'if-nez v2, :cond_1', 'invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->onFinishStartActionMode(Z)V', 'return-void', 'iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;', 'invoke-virtual {v2}, Landroid/widget/FrameLayout;->getParent()Landroid/view/ViewParent;'],
        'type': 'method_replace',
        'search': """.method protected makeContextViewsShowHide(Z)V
    .registers 8

    const/high16 v0, 0x3f800000

    const/4 v1, 0x0

    if-eqz p1, :cond_0

    move v2, v0

    goto :goto_0

    :cond_0
    move v2, v1

    :goto_0
    invoke-virtual {p0, v2}, Landroid/view/ViewGroup;->setAlpha(F)V

    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitActionBarEnable:Z

    if-nez v2, :cond_1

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->onFinishStartActionMode(Z)V

    return-void

    :cond_1
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-eqz v3, :cond_5

    invoke-virtual {v3}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->getCollapsedHeight()I

    move-result v3

    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-eqz p1, :cond_2

    move v5, v1

    goto :goto_1

    :cond_2
    int-to-float v5, v3

    :goto_1
    invoke-virtual {v4, v5}, Landroid/widget/LinearLayout;->setTranslationY(F)V

    if-eqz p1, :cond_3

    goto :goto_2

    :cond_3
    const/4 v3, 0x0

    :goto_2
    invoke-virtual {v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->animateContentMarginBottomByBottomMenu(I)V

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-eqz p1, :cond_4

    goto :goto_3

    :cond_4
    move v0, v1

    :goto_3
    invoke-virtual {v2, v0}, Landroid/widget/LinearLayout;->setAlpha(F)V

    :cond_5
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->onFinishStartActionMode(Z)V

    return-void
.end method""",
        'replacement': """.method protected makeContextViewsShowHide(Z)V
    .registers 8

    goto :goto_27

    nop

    :goto_0
    invoke-virtual {v4, v5}, Landroid/widget/LinearLayout;->setTranslationY(F)V

    goto :goto_18

    nop

    :goto_1
    goto :goto_16

    :goto_2
    goto :goto_15

    nop

    :goto_3
    invoke-virtual {v3}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->getCollapsedHeight()I

    move-result v3

    goto :goto_21

    nop

    :goto_4
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_a

    nop

    :goto_5
    goto :goto_1e

    :goto_6
    goto :goto_1d

    nop

    :goto_7
    move v5, v1

    goto :goto_8

    nop

    :goto_8
    goto :goto_12

    :goto_9
    goto :goto_11

    nop

    :goto_a
    if-nez p1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_5

    nop

    :goto_b
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitView:Lmiuix/appcompat/internal/app/widget/ActionBarContainer;

    goto :goto_14

    nop

    :goto_c
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->onFinishStartActionMode(Z)V

    goto :goto_13

    nop

    :goto_d
    goto :goto_23

    :goto_e
    goto :goto_22

    nop

    :goto_f
    if-eqz v2, :cond_1

    goto :goto_29

    :cond_1
    goto :goto_1f

    nop

    :goto_10
    if-nez p1, :cond_2

    goto :goto_9

    :cond_2
    goto :goto_7

    nop

    :goto_11
    int-to-float v5, v3

    :goto_12
    goto :goto_0

    nop

    :goto_13
    return-void

    :goto_14
    invoke-virtual {v2}, Landroid/widget/FrameLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v2

    goto :goto_1c

    nop

    :goto_15
    move v2, v1

    :goto_16
    goto :goto_2b

    nop

    :goto_17
    if-nez v3, :cond_3

    goto :goto_25

    :cond_3
    goto :goto_3

    nop

    :goto_18
    if-nez p1, :cond_4

    goto :goto_e

    :cond_4
    goto :goto_d

    nop

    :goto_19
    invoke-virtual {v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->animateContentMarginBottomByBottomMenu(I)V

    goto :goto_4

    nop

    :goto_1a
    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitActionBarEnable:Z

    goto :goto_f

    nop

    :goto_1b
    move v2, v0

    goto :goto_1

    nop

    :goto_1c
    check-cast v2, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_2a

    nop

    :goto_1d
    move v0, v1

    :goto_1e
    goto :goto_24

    nop

    :goto_1f
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->onFinishStartActionMode(Z)V

    goto :goto_28

    nop

    :goto_20
    const/4 v1, 0x0

    goto :goto_26

    nop

    :goto_21
    iget-object v4, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_10

    nop

    :goto_22
    const/4 v3, 0x0

    :goto_23
    goto :goto_19

    nop

    :goto_24
    invoke-virtual {v2, v0}, Landroid/widget/LinearLayout;->setAlpha(F)V

    :goto_25
    goto :goto_c

    nop

    :goto_26
    if-nez p1, :cond_5

    goto :goto_2

    :cond_5
    goto :goto_1b

    nop

    :goto_27
    const/high16 v0, 0x3f800000

    goto :goto_20

    nop

    :goto_28
    return-void

    :goto_29
    goto :goto_b

    nop

    :goto_2a
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_17

    nop

    :goto_2b
    invoke-virtual {p0, v2}, Landroid/view/ViewGroup;->setAlpha(F)V

    goto :goto_1a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__makeContextViewsShowHideWithAnimation',
        'method': '.method protected makeContextViewsShowHideWithAnimation(Z)V',
        'method_name': 'makeContextViewsShowHideWithAnimation',
        'method_anchors': ['iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mAnimateToVisible:Z', 'if-ne p1, v1, :cond_0', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;', 'if-eqz v1, :cond_0', 'iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mAnimateToVisible:Z', 'iput-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mAnimateStart:Z', 'if-eqz p1, :cond_1', 'if-eqz p1, :cond_2'],
        'type': 'method_replace',
        'search': """.method protected makeContextViewsShowHideWithAnimation(Z)V
    .registers 16

    const/4 v0, 0x2

    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mAnimateToVisible:Z

    if-ne p1, v1, :cond_0

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    if-eqz v1, :cond_0

    goto :goto_4

    :cond_0
    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mAnimateToVisible:Z

    const/4 v1, 0x0

    iput-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mAnimateStart:Z

    const/high16 v2, 0x3f800000

    const/4 v3, 0x0

    if-eqz p1, :cond_1

    move v13, v3

    move v3, v2

    move v2, v13

    :cond_1
    if-eqz p1, :cond_2

    const v4, 0x43a1228f

    goto :goto_0

    :cond_2
    const v4, 0x4476bd71

    :goto_0
    invoke-direct {p0, p0, v4, v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->getViewSpringAnima(Landroid/view/View;FFF)Lmiuix/animation/physics/SpringAnimation;

    move-result-object v3

    if-eqz p1, :cond_3

    const-wide/16 v4, 0x32

    goto :goto_1

    :cond_3
    const-wide/16 v4, 0x0

    :goto_1
    invoke-virtual {v3, v4, v5}, Lmiuix/animation/physics/DynamicAnimation;->setStartDelay(J)V

    invoke-virtual {p0, v2}, Landroid/view/ViewGroup;->setAlpha(F)V

    iput-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitActionBarEnable:Z

    const/4 v4, 0x1

    if-nez v2, :cond_4

    new-instance p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;

    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda0;

    invoke-direct {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarContextView;)V

    invoke-direct {p1, v4, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;-><init>(ILmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown$CountDownCompleteListener;)V

    new-instance p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda1;

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda1;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;)V

    invoke-virtual {v3, p0}, Lmiuix/animation/physics/DynamicAnimation;->addEndListener(Lmiuix/animation/physics/DynamicAnimation$OnAnimationEndListener;)Lmiuix/animation/physics/DynamicAnimation;

    invoke-virtual {v3}, Lmiuix/animation/physics/SpringAnimation;->start()V

    return-void

    :cond_4
    new-instance v12, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;

    new-instance v2, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda0;

    invoke-direct {v2, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarContextView;)V

    invoke-direct {v12, v0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;-><init>(ILmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown$CountDownCompleteListener;)V

    new-instance v2, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda2;

    invoke-direct {v2, v12}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda2;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;)V

    invoke-virtual {v3, v2}, Lmiuix/animation/physics/DynamicAnimation;->addEndListener(Lmiuix/animation/physics/DynamicAnimation$OnAnimationEndListener;)Lmiuix/animation/physics/DynamicAnimation;

    invoke-virtual {v3}, Lmiuix/animation/physics/SpringAnimation;->start()V

    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getParent()Landroid/view/ViewParent;

    move-result-object v3

    invoke-interface {v3}, Landroid/view/ViewParent;->getParent()Landroid/view/ViewParent;

    move-result-object v3

    move-object v8, v3

    check-cast v8, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    if-nez v2, :cond_5

    move v9, v1

    goto :goto_2

    :cond_5
    invoke-virtual {v2}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->getCollapsedHeight()I

    move-result v3

    move v9, v3

    :goto_2
    if-eqz p1, :cond_6

    move v10, v1

    move v11, v9

    goto :goto_3

    :cond_6
    move v11, v1

    move v10, v9

    :goto_3
    if-eqz v2, :cond_9

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    if-nez v3, :cond_7

    new-instance v3, Lmiuix/animation/base/AnimConfig;

    invoke-direct {v3}, Lmiuix/animation/base/AnimConfig;-><init>()V

    new-array v0, v0, [F

    fill-array-data v0, :array_0

    const/4 v5, -0x2

    invoke-virtual {v3, v5, v0}, Lmiuix/animation/base/AnimConfig;->setEase(I[F)Lmiuix/animation/base/AnimConfig;

    move-result-object v0

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    :cond_7
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTransitionListener:Lmiuix/animation/listener/TransitionListener;

    if-eqz v0, :cond_8

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    filled-new-array {v0}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object v0

    invoke-virtual {v3, v0}, Lmiuix/animation/base/AnimConfig;->removeListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    :cond_8
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    new-instance v5, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$3;

    move-object v6, p0

    move v7, p1

    invoke-direct/range {v5 .. v12}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$3;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarContextView;ZLmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;IIILmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;)V

    iput-object v5, v6, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTransitionListener:Lmiuix/animation/listener/TransitionListener;

    filled-new-array {v5}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object p0

    invoke-virtual {v0, p0}, Lmiuix/animation/base/AnimConfig;->addListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    new-array p0, v4, [Landroid/view/View;

    aput-object v2, p0, v1

    invoke-static {p0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object p0

    invoke-interface {p0}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;

    move-result-object p0

    sget-object p1, Lmiuix/animation/property/ViewProperty;->TRANSLATION_Y:Lmiuix/animation/property/ViewProperty;

    invoke-static {v11}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    filled-new-array {p1, v0}, [Ljava/lang/Object;

    move-result-object v0

    invoke-interface {p0, v0}, Lmiuix/animation/FolmeStyle;->setTo([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object p0

    invoke-static {v10}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    iget-object v2, v6, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    filled-new-array {p1, v0, v2}, [Ljava/lang/Object;

    move-result-object p1

    invoke-interface {p0, p1}, Lmiuix/animation/FolmeStyle;->to([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    invoke-virtual {v8, v1, v4}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->onMenuStateChanged(II)V

    :cond_9
    :goto_4
    return-void

    :array_0
    .array-data 4
        0x3f733333
        0x3e800000
    .end array-data
.end method""",
        'replacement': """.method protected makeContextViewsShowHideWithAnimation(Z)V
    .registers 16

    goto :goto_68

    nop

    :goto_0
    return-void

    :goto_1
    goto :goto_4d

    nop

    :goto_2
    invoke-direct {v3}, Lmiuix/animation/base/AnimConfig;-><init>()V

    goto :goto_1f

    nop

    :goto_3
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    goto :goto_6b

    nop

    :goto_4
    if-nez p1, :cond_0

    goto :goto_6a

    :cond_0
    goto :goto_57

    nop

    :goto_5
    move v9, v3

    :goto_6
    goto :goto_3d

    nop

    :goto_7
    new-array p0, v4, [Landroid/view/View;

    goto :goto_49

    nop

    :goto_8
    goto :goto_47

    :goto_9
    goto :goto_46

    nop

    :goto_a
    new-instance v2, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda2;

    goto :goto_5d

    nop

    :goto_b
    if-eqz v2, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_60

    nop

    :goto_c
    move v7, p1

    goto :goto_29

    nop

    :goto_d
    invoke-direct {v2, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarContextView;)V

    goto :goto_5c

    nop

    :goto_e
    iput-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_11

    nop

    :goto_f
    goto :goto_22

    :goto_10
    goto :goto_21

    nop

    :goto_11
    iget-boolean v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mSplitActionBarEnable:Z

    goto :goto_6d

    nop

    :goto_12
    move v10, v1

    goto :goto_3a

    nop

    :goto_13
    const-wide/16 v4, 0x32

    goto :goto_8

    nop

    :goto_14
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTransitionListener:Lmiuix/animation/listener/TransitionListener;

    goto :goto_59

    nop

    :goto_15
    invoke-interface {p0, p1}, Lmiuix/animation/FolmeStyle;->to([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    goto :goto_31

    nop

    :goto_16
    invoke-static {v11}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_63

    nop

    :goto_17
    invoke-direct {v0, p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda0;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarContextView;)V

    goto :goto_3b

    nop

    :goto_18
    move v11, v1

    goto :goto_38

    nop

    :goto_19
    new-instance v5, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$3;

    goto :goto_65

    nop

    :goto_1a
    return-void

    nop

    :array_0
    .array-data 4
        0x3f733333
        0x3e800000
    .end array-data

    :goto_1b
    invoke-virtual {v3, v4, v5}, Lmiuix/animation/physics/DynamicAnimation;->setStartDelay(J)V

    goto :goto_5a

    nop

    :goto_1c
    new-instance p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda1;

    goto :goto_35

    nop

    :goto_1d
    invoke-direct {p0, p0, v4, v2, v3}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->getViewSpringAnima(Landroid/view/View;FFF)Lmiuix/animation/physics/SpringAnimation;

    move-result-object v3

    goto :goto_62

    nop

    :goto_1e
    const v4, 0x43a1228f

    goto :goto_f

    nop

    :goto_1f
    new-array v0, v0, [F

    fill-array-data v0, :array_0

    goto :goto_28

    nop

    :goto_20
    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mAnimateToVisible:Z

    goto :goto_41

    nop

    :goto_21
    const v4, 0x4476bd71

    :goto_22
    goto :goto_1d

    nop

    :goto_23
    invoke-virtual {v0, p0}, Lmiuix/animation/base/AnimConfig;->addListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    goto :goto_7

    nop

    :goto_24
    if-nez p1, :cond_2

    goto :goto_10

    :cond_2
    goto :goto_1e

    nop

    :goto_25
    invoke-virtual {v3, v5, v0}, Lmiuix/animation/base/AnimConfig;->setEase(I[F)Lmiuix/animation/base/AnimConfig;

    move-result-object v0

    goto :goto_66

    nop

    :goto_26
    move v3, v2

    goto :goto_69

    nop

    :goto_27
    const/high16 v2, 0x3f800000

    goto :goto_33

    nop

    :goto_28
    const/4 v5, -0x2

    goto :goto_25

    nop

    :goto_29
    invoke-direct/range {v5 .. v12}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$3;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarContextView;ZLmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;IIILmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;)V

    goto :goto_2e

    nop

    :goto_2a
    filled-new-array {v0}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object v0

    goto :goto_6f

    nop

    :goto_2b
    if-nez v1, :cond_3

    goto :goto_37

    :cond_3
    goto :goto_36

    nop

    :goto_2c
    goto :goto_39

    :goto_2d
    goto :goto_18

    nop

    :goto_2e
    iput-object v5, v6, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTransitionListener:Lmiuix/animation/listener/TransitionListener;

    goto :goto_50

    nop

    :goto_2f
    check-cast v8, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;

    goto :goto_44

    nop

    :goto_30
    if-eq p1, v1, :cond_4

    goto :goto_37

    :cond_4
    goto :goto_3e

    nop

    :goto_31
    invoke-virtual {v8, v1, v4}, Lmiuix/appcompat/internal/app/widget/ActionBarOverlayLayout;->onMenuStateChanged(II)V

    :goto_32
    goto :goto_1a

    nop

    :goto_33
    const/4 v3, 0x0

    goto :goto_4

    nop

    :goto_34
    invoke-interface {p0}, Lmiuix/animation/IFolme;->state()Lmiuix/animation/IStateStyle;

    move-result-object p0

    goto :goto_5e

    nop

    :goto_35
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda1;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;)V

    goto :goto_52

    nop

    :goto_36
    goto :goto_32

    :goto_37
    goto :goto_20

    nop

    :goto_38
    move v10, v9

    :goto_39
    goto :goto_54

    nop

    :goto_3a
    move v11, v9

    goto :goto_2c

    nop

    :goto_3b
    invoke-direct {p1, v4, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;-><init>(ILmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown$CountDownCompleteListener;)V

    goto :goto_1c

    nop

    :goto_3c
    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda0;

    goto :goto_17

    nop

    :goto_3d
    if-nez p1, :cond_5

    goto :goto_2d

    :cond_5
    goto :goto_12

    nop

    :goto_3e
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mVisibilityAnim:Lmiuix/animation/physics/SpringAnimation;

    goto :goto_2b

    nop

    :goto_3f
    invoke-virtual {v3}, Lmiuix/animation/physics/SpringAnimation;->start()V

    goto :goto_0

    nop

    :goto_40
    iget-object v2, v6, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    goto :goto_42

    nop

    :goto_41
    const/4 v1, 0x0

    goto :goto_48

    nop

    :goto_42
    filled-new-array {p1, v0, v2}, [Ljava/lang/Object;

    move-result-object p1

    goto :goto_15

    nop

    :goto_43
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getParent()Landroid/view/ViewParent;

    move-result-object v3

    goto :goto_53

    nop

    :goto_44
    if-eqz v2, :cond_6

    goto :goto_4b

    :cond_6
    goto :goto_45

    nop

    :goto_45
    move v9, v1

    goto :goto_4a

    nop

    :goto_46
    const-wide/16 v4, 0x0

    :goto_47
    goto :goto_1b

    nop

    :goto_48
    iput-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mAnimateStart:Z

    goto :goto_27

    nop

    :goto_49
    aput-object v2, p0, v1

    goto :goto_61

    nop

    :goto_4a
    goto :goto_6

    :goto_4b
    goto :goto_64

    nop

    :goto_4c
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    goto :goto_2a

    nop

    :goto_4d
    new-instance v12, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;

    goto :goto_4e

    nop

    :goto_4e
    new-instance v2, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda0;

    goto :goto_d

    nop

    :goto_4f
    iget-boolean v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mAnimateToVisible:Z

    goto :goto_30

    nop

    :goto_50
    filled-new-array {v5}, [Lmiuix/animation/listener/TransitionListener;

    move-result-object p0

    goto :goto_23

    nop

    :goto_51
    invoke-interface {p0, v0}, Lmiuix/animation/FolmeStyle;->setTo([Ljava/lang/Object;)Lmiuix/animation/IStateStyle;

    move-result-object p0

    goto :goto_6c

    nop

    :goto_52
    invoke-virtual {v3, p0}, Lmiuix/animation/physics/DynamicAnimation;->addEndListener(Lmiuix/animation/physics/DynamicAnimation$OnAnimationEndListener;)Lmiuix/animation/physics/DynamicAnimation;

    goto :goto_3f

    nop

    :goto_53
    invoke-interface {v3}, Landroid/view/ViewParent;->getParent()Landroid/view/ViewParent;

    move-result-object v3

    goto :goto_56

    nop

    :goto_54
    if-nez v2, :cond_7

    goto :goto_32

    :cond_7
    goto :goto_3

    nop

    :goto_55
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    goto :goto_19

    nop

    :goto_56
    move-object v8, v3

    goto :goto_2f

    nop

    :goto_57
    move v13, v3

    goto :goto_26

    nop

    :goto_58
    iget-object v2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_43

    nop

    :goto_59
    if-nez v0, :cond_8

    goto :goto_70

    :cond_8
    goto :goto_4c

    nop

    :goto_5a
    invoke-virtual {p0, v2}, Landroid/view/ViewGroup;->setAlpha(F)V

    goto :goto_e

    nop

    :goto_5b
    new-instance v3, Lmiuix/animation/base/AnimConfig;

    goto :goto_2

    nop

    :goto_5c
    invoke-direct {v12, v0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;-><init>(ILmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown$CountDownCompleteListener;)V

    goto :goto_a

    nop

    :goto_5d
    invoke-direct {v2, v12}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$$ExternalSyntheticLambda2;-><init>(Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;)V

    goto :goto_6e

    nop

    :goto_5e
    sget-object p1, Lmiuix/animation/property/ViewProperty;->TRANSLATION_Y:Lmiuix/animation/property/ViewProperty;

    goto :goto_16

    nop

    :goto_5f
    invoke-virtual {v3}, Lmiuix/animation/physics/SpringAnimation;->start()V

    goto :goto_58

    nop

    :goto_60
    new-instance p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$CountDown;

    goto :goto_3c

    nop

    :goto_61
    invoke-static {p0}, Lmiuix/animation/Folme;->useAt([Landroid/view/View;)Lmiuix/animation/IFolme;

    move-result-object p0

    goto :goto_34

    nop

    :goto_62
    if-nez p1, :cond_9

    goto :goto_9

    :cond_9
    goto :goto_13

    nop

    :goto_63
    filled-new-array {p1, v0}, [Ljava/lang/Object;

    move-result-object v0

    goto :goto_51

    nop

    :goto_64
    invoke-virtual {v2}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->getCollapsedHeight()I

    move-result v3

    goto :goto_5

    nop

    :goto_65
    move-object v6, p0

    goto :goto_c

    nop

    :goto_66
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMenuAnimConfig:Lmiuix/animation/base/AnimConfig;

    :goto_67
    goto :goto_14

    nop

    :goto_68
    const/4 v0, 0x2

    goto :goto_4f

    nop

    :goto_69
    move v2, v13

    :goto_6a
    goto :goto_24

    nop

    :goto_6b
    if-eqz v3, :cond_a

    goto :goto_67

    :cond_a
    goto :goto_5b

    nop

    :goto_6c
    invoke-static {v10}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v0

    goto :goto_40

    nop

    :goto_6d
    const/4 v4, 0x1

    goto :goto_b

    nop

    :goto_6e
    invoke-virtual {v3, v2}, Lmiuix/animation/physics/DynamicAnimation;->addEndListener(Lmiuix/animation/physics/DynamicAnimation$OnAnimationEndListener;)Lmiuix/animation/physics/DynamicAnimation;

    goto :goto_5f

    nop

    :goto_6f
    invoke-virtual {v3, v0}, Lmiuix/animation/base/AnimConfig;->removeListeners([Lmiuix/animation/listener/TransitionListener;)Lmiuix/animation/base/AnimConfig;

    :goto_70
    goto :goto_55

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;', 'sget-object v0, Lmiuix/appcompat/R$styleable;->ActionMode:[I', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->getActionBarStyle()I', 'invoke-virtual {p1, v2, v0, v1, v3}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[III)Landroid/content/res/TypedArray;', 'sget v0, Lmiuix/appcompat/R$styleable;->ActionMode_android_minHeight:I', 'invoke-virtual {p1, v0, v3}, Landroid/content/res/TypedArray;->getLayoutDimension(II)I', 'iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 6

    invoke-super {p0, p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object p1

    sget-object v0, Lmiuix/appcompat/R$styleable;->ActionMode:[I

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->getActionBarStyle()I

    move-result v1

    const/4 v2, 0x0

    const/4 v3, 0x0

    invoke-virtual {p1, v2, v0, v1, v3}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[III)Landroid/content/res/TypedArray;

    move-result-object p1

    sget v0, Lmiuix/appcompat/R$styleable;->ActionMode_android_minHeight:I

    invoke-virtual {p1, v0, v3}, Landroid/content/res/TypedArray;->getLayoutDimension(II)I

    move-result v0

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    invoke-virtual {p1}, Landroid/content/res/TypedArray;->recycle()V

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_horizontal_padding:I

    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result p1

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    sget v2, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_top_padding:I

    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v1

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    sget v3, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_bottom_padding:I

    invoke-virtual {v2, v3}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v2

    invoke-virtual {v0, p1, v1, p1, v2}, Landroid/widget/FrameLayout;->setPaddingRelative(IIII)V

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object p1

    sget v0, Lmiuix/appcompat/R$attr;->actionBarPaddingStart:I

    invoke-static {p1, v0}, Lmiuix/internal/util/AttributeResolver;->resolveDimensionPixelSize(Landroid/content/Context;I)I

    move-result p1

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    sget v1, Lmiuix/appcompat/R$attr;->actionBarPaddingEnd:I

    invoke-static {v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveDimensionPixelSize(Landroid/content/Context;I)I

    move-result v0

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v1

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v2

    invoke-virtual {p0, p1, v1, v0, v2}, Landroid/view/ViewGroup;->setPaddingRelative(IIII)V

    iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleStyleRes:I

    if-eqz p1, :cond_0

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleView:Landroid/widget/TextView;

    if-eqz p1, :cond_0

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleStyleRes:I

    invoke-virtual {p1, v0, p0}, Landroid/widget/TextView;->setTextAppearance(Landroid/content/Context;I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 6

    goto :goto_1d

    nop

    :goto_0
    sget-object v0, Lmiuix/appcompat/R$styleable;->ActionMode:[I

    goto :goto_d

    nop

    :goto_1
    invoke-virtual {p1, v0}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result p1

    goto :goto_9

    nop

    :goto_2
    invoke-virtual {p1, v2, v0, v1, v3}, Landroid/content/Context;->obtainStyledAttributes(Landroid/util/AttributeSet;[III)Landroid/content/res/TypedArray;

    move-result-object p1

    goto :goto_15

    nop

    :goto_3
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object p1

    goto :goto_1c

    nop

    :goto_4
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleView:Landroid/widget/TextView;

    goto :goto_e

    nop

    :goto_5
    invoke-virtual {p1, v0, v3}, Landroid/content/res/TypedArray;->getLayoutDimension(II)I

    move-result v0

    goto :goto_1b

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_22

    nop

    :goto_7
    invoke-static {v0, v1}, Lmiuix/internal/util/AttributeResolver;->resolveDimensionPixelSize(Landroid/content/Context;I)I

    move-result v0

    goto :goto_18

    nop

    :goto_8
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object v2

    goto :goto_11

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_1a

    nop

    :goto_a
    return-void

    :goto_b
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v2

    goto :goto_c

    nop

    :goto_c
    invoke-virtual {p0, p1, v1, v0, v2}, Landroid/view/ViewGroup;->setPaddingRelative(IIII)V

    goto :goto_24

    nop

    :goto_d
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->getActionBarStyle()I

    move-result v1

    goto :goto_25

    nop

    :goto_e
    if-nez p1, :cond_0

    goto :goto_27

    :cond_0
    goto :goto_6

    nop

    :goto_f
    invoke-virtual {v2, v3}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v2

    goto :goto_1e

    nop

    :goto_10
    sget v0, Lmiuix/appcompat/R$attr;->actionBarPaddingStart:I

    goto :goto_16

    nop

    :goto_11
    sget v3, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_bottom_padding:I

    goto :goto_f

    nop

    :goto_12
    invoke-virtual {v1, v2}, Landroid/content/res/Resources;->getDimensionPixelOffset(I)I

    move-result v1

    goto :goto_8

    nop

    :goto_13
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_14

    nop

    :goto_14
    sget v1, Lmiuix/appcompat/R$attr;->actionBarPaddingEnd:I

    goto :goto_7

    nop

    :goto_15
    sget v0, Lmiuix/appcompat/R$styleable;->ActionMode_android_minHeight:I

    goto :goto_5

    nop

    :goto_16
    invoke-static {p1, v0}, Lmiuix/internal/util/AttributeResolver;->resolveDimensionPixelSize(Landroid/content/Context;I)I

    move-result p1

    goto :goto_13

    nop

    :goto_17
    sget v2, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_top_padding:I

    goto :goto_12

    nop

    :goto_18
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v1

    goto :goto_b

    nop

    :goto_19
    invoke-virtual {p1}, Landroid/content/res/TypedArray;->recycle()V

    goto :goto_3

    nop

    :goto_1a
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    goto :goto_17

    nop

    :goto_1b
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    goto :goto_19

    nop

    :goto_1c
    sget v0, Lmiuix/appcompat/R$dimen;->miuix_appcompat_action_bar_title_horizontal_padding:I

    goto :goto_1

    nop

    :goto_1d
    invoke-super {p0, p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_23

    nop

    :goto_1e
    invoke-virtual {v0, p1, v1, p1, v2}, Landroid/widget/FrameLayout;->setPaddingRelative(IIII)V

    goto :goto_1f

    nop

    :goto_1f
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_10

    nop

    :goto_20
    if-nez p1, :cond_1

    goto :goto_27

    :cond_1
    goto :goto_4

    nop

    :goto_21
    const/4 v3, 0x0

    goto :goto_2

    nop

    :goto_22
    iget p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleStyleRes:I

    goto :goto_26

    nop

    :goto_23
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_0

    nop

    :goto_24
    iget p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleStyleRes:I

    goto :goto_20

    nop

    :goto_25
    const/4 v2, 0x0

    goto :goto_21

    nop

    :goto_26
    invoke-virtual {p1, v0, p0}, Landroid/widget/TextView;->setTextAppearance(Landroid/content/Context;I)V

    :goto_27
    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__onExpandStateChanged',
        'method': '.method protected onExpandStateChanged(II)V',
        'method_name': 'onExpandStateChanged',
        'method_anchors': ['if-ne p1, v2, :cond_0', 'iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPendingHeight:I', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPostScroller:Landroid/widget/Scroller;', 'invoke-virtual {p1}, Landroid/widget/Scroller;->isFinished()Z', 'if-nez p1, :cond_0', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPostScroller:Landroid/widget/Scroller;', 'invoke-virtual {p1, v0}, Landroid/widget/Scroller;->forceFinished(Z)V', 'if-ne p2, v2, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected onExpandStateChanged(II)V
    .registers 8

    const/4 v0, 0x1

    const/4 v1, 0x0

    const/4 v2, 0x2

    if-ne p1, v2, :cond_0

    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPendingHeight:I

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPostScroller:Landroid/widget/Scroller;

    invoke-virtual {p1}, Landroid/widget/Scroller;->isFinished()Z

    move-result p1

    if-nez p1, :cond_0

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPostScroller:Landroid/widget/Scroller;

    invoke-virtual {p1, v0}, Landroid/widget/Scroller;->forceFinished(Z)V

    :cond_0
    if-ne p2, v2, :cond_1

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz p1, :cond_1

    invoke-virtual {p1, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :cond_1
    const/high16 p1, 0x3f800000

    const/4 v2, 0x0

    if-ne p2, v0, :cond_4

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v3}, Landroid/widget/FrameLayout;->getAlpha()F

    move-result v3

    cmpl-float v3, v3, v2

    if-lez v3, :cond_3

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz v3, :cond_2

    const/16 v4, 0x14

    invoke-virtual {v3, v2, v1, v4, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    :cond_2
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz v3, :cond_3

    invoke-virtual {v3, p1, v1, v1, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    :cond_3
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz v3, :cond_4

    invoke-virtual {v3, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :cond_4
    if-nez p2, :cond_7

    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz p2, :cond_5

    invoke-virtual {p2, p1, v1, v1, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    invoke-virtual {p1, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->onShow()V

    :cond_5
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    if-eqz p1, :cond_6

    invoke-virtual {p1, v2, v1, v1, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    const/16 p1, 0x8

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :cond_6
    return-void

    :cond_7
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I

    move-result p1

    iget p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    sub-int/2addr p1, p2

    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPendingHeight:I

    return-void
.end method""",
        'replacement': """.method protected onExpandStateChanged(II)V
    .registers 8

    goto :goto_f

    nop

    :goto_0
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_2f

    nop

    :goto_1
    if-nez p1, :cond_0

    goto :goto_17

    :cond_0
    goto :goto_7

    nop

    :goto_2
    if-gtz v3, :cond_1

    goto :goto_38

    :cond_1
    goto :goto_0

    nop

    :goto_3
    if-eq p2, v0, :cond_2

    goto :goto_15

    :cond_2
    goto :goto_36

    nop

    :goto_4
    if-nez p1, :cond_3

    goto :goto_1e

    :cond_3
    goto :goto_1d

    nop

    :goto_5
    if-eq p1, v2, :cond_4

    goto :goto_2e

    :cond_4
    goto :goto_d

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {p1, v2, v1, v1, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    goto :goto_b

    nop

    :goto_8
    return-void

    :goto_9
    goto :goto_18

    nop

    :goto_a
    if-nez v3, :cond_5

    goto :goto_15

    :cond_5
    goto :goto_14

    nop

    :goto_b
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_30

    nop

    :goto_c
    if-eq p2, v2, :cond_6

    goto :goto_1e

    :cond_6
    goto :goto_33

    nop

    :goto_d
    iput v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPendingHeight:I

    goto :goto_2b

    nop

    :goto_e
    const/16 v4, 0x14

    goto :goto_19

    nop

    :goto_f
    const/4 v0, 0x1

    goto :goto_35

    nop

    :goto_10
    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_20

    nop

    :goto_11
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_1

    nop

    :goto_12
    invoke-virtual {p1}, Landroid/widget/Scroller;->isFinished()Z

    move-result p1

    goto :goto_32

    nop

    :goto_13
    if-nez v3, :cond_7

    goto :goto_38

    :cond_7
    goto :goto_37

    nop

    :goto_14
    invoke-virtual {v3, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :goto_15
    goto :goto_28

    nop

    :goto_16
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :goto_17
    goto :goto_8

    nop

    :goto_18
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getHeight()I

    move-result p1

    goto :goto_1c

    nop

    :goto_19
    invoke-virtual {v3, v2, v1, v4, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    :goto_1a
    goto :goto_1b

    nop

    :goto_1b
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_13

    nop

    :goto_1c
    iget p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    goto :goto_31

    nop

    :goto_1d
    invoke-virtual {p1, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    :goto_1e
    goto :goto_2a

    nop

    :goto_1f
    const/4 v2, 0x2

    goto :goto_5

    nop

    :goto_20
    if-nez p2, :cond_8

    goto :goto_23

    :cond_8
    goto :goto_3a

    nop

    :goto_21
    invoke-virtual {v3}, Landroid/widget/FrameLayout;->getAlpha()F

    move-result v3

    goto :goto_24

    nop

    :goto_22
    invoke-virtual {p1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->onShow()V

    :goto_23
    goto :goto_11

    nop

    :goto_24
    cmpl-float v3, v3, v2

    goto :goto_2

    nop

    :goto_25
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_a

    nop

    :goto_26
    const/4 v2, 0x0

    goto :goto_3

    nop

    :goto_27
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_22

    nop

    :goto_28
    if-eqz p2, :cond_9

    goto :goto_9

    :cond_9
    goto :goto_10

    nop

    :goto_29
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPostScroller:Landroid/widget/Scroller;

    goto :goto_2d

    nop

    :goto_2a
    const/high16 p1, 0x3f800000

    goto :goto_26

    nop

    :goto_2b
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPostScroller:Landroid/widget/Scroller;

    goto :goto_12

    nop

    :goto_2c
    iput p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPendingHeight:I

    goto :goto_6

    nop

    :goto_2d
    invoke-virtual {p1, v0}, Landroid/widget/Scroller;->forceFinished(Z)V

    :goto_2e
    goto :goto_c

    nop

    :goto_2f
    if-nez v3, :cond_a

    goto :goto_1a

    :cond_a
    goto :goto_e

    nop

    :goto_30
    const/16 p1, 0x8

    goto :goto_16

    nop

    :goto_31
    sub-int/2addr p1, p2

    goto :goto_2c

    nop

    :goto_32
    if-eqz p1, :cond_b

    goto :goto_2e

    :cond_b
    goto :goto_29

    nop

    :goto_33
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_4

    nop

    :goto_34
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseController:Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;

    goto :goto_39

    nop

    :goto_35
    const/4 v1, 0x0

    goto :goto_1f

    nop

    :goto_36
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_21

    nop

    :goto_37
    invoke-virtual {v3, p1, v1, v1, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    :goto_38
    goto :goto_25

    nop

    :goto_39
    invoke-virtual {p1, v1}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setVisibility(I)V

    goto :goto_27

    nop

    :goto_3a
    invoke-virtual {p2, p1, v1, v1, v0}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView$CollapseView;->setAnimFrom(FIIZ)V

    goto :goto_34

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__onLayout',
        'method': '.method protected onLayout(ZIIII)V',
        'method_name': 'onLayout',
        'method_anchors': ['invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;', 'invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;', 'invoke-virtual {v1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;', 'iget v1, v1, Landroid/util/DisplayMetrics;->density:F', 'iget v1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I', 'if-ne v1, v2, :cond_0', 'iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPendingHeight:I', 'if-ne v1, v4, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected onLayout(ZIIII)V
    .registers 12

    sub-int v0, p4, p2

    int-to-float v0, v0

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    invoke-virtual {v1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v1

    iget v1, v1, Landroid/util/DisplayMetrics;->density:F

    div-float/2addr v0, v1

    float-to-int v0, v0

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    const/4 v2, 0x2

    const/4 v3, 0x0

    const/4 v4, 0x1

    if-ne v1, v2, :cond_0

    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPendingHeight:I

    :goto_0
    move v2, p5

    goto :goto_1

    :cond_0
    if-ne v1, v4, :cond_1

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v1

    goto :goto_0

    :cond_1
    move v2, p5

    move v1, v3

    :goto_1
    sub-int p5, v2, p3

    move v5, p3

    sub-int p3, p5, v1

    sub-int/2addr v2, v1

    invoke-direct {p0, p2, v5, p4, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->onLayoutCollapseViews(IIII)V

    invoke-virtual/range {p0 .. p5}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->onLayoutExpandViews(ZIIII)V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p1

    sub-int/2addr p1, v1

    int-to-float p1, p1

    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p2}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p2

    int-to-float p2, p2

    div-float/2addr p1, p2

    const/high16 p2, 0x3f800000

    invoke-static {p2, p1}, Ljava/lang/Math;->min(FF)F

    move-result p1

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->animateLayoutWithProcess(F)V

    iput p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mLastProcess:F

    const/16 p1, 0x280

    if-le v0, p1, :cond_2

    move v3, v4

    :cond_2
    iput-boolean v3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mIsInWideMode:Z

    return-void
.end method""",
        'replacement': """.method protected onLayout(ZIIII)V
    .registers 12

    goto :goto_d

    nop

    :goto_0
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    goto :goto_27

    nop

    :goto_1
    invoke-virtual {v1}, Landroid/content/res/Resources;->getDisplayMetrics()Landroid/util/DisplayMetrics;

    move-result-object v1

    goto :goto_9

    nop

    :goto_2
    int-to-float v0, v0

    goto :goto_10

    nop

    :goto_3
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->animateLayoutWithProcess(F)V

    goto :goto_c

    nop

    :goto_4
    if-eq v1, v2, :cond_0

    goto :goto_15

    :cond_0
    goto :goto_2f

    nop

    :goto_5
    invoke-virtual {v1}, Landroid/content/Context;->getResources()Landroid/content/res/Resources;

    move-result-object v1

    goto :goto_1

    nop

    :goto_6
    move v3, v4

    :goto_7
    goto :goto_31

    nop

    :goto_8
    if-gt v0, p1, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_6

    nop

    :goto_9
    iget v1, v1, Landroid/util/DisplayMetrics;->density:F

    goto :goto_1f

    nop

    :goto_a
    invoke-virtual/range {p0 .. p5}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->onLayoutExpandViews(ZIIII)V

    goto :goto_12

    nop

    :goto_b
    invoke-virtual {p2}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p2

    goto :goto_19

    nop

    :goto_c
    iput p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mLastProcess:F

    goto :goto_e

    nop

    :goto_d
    sub-int v0, p4, p2

    goto :goto_2

    nop

    :goto_e
    const/16 p1, 0x280

    goto :goto_8

    nop

    :goto_f
    const/4 v4, 0x1

    goto :goto_4

    nop

    :goto_10
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getContext()Landroid/content/Context;

    move-result-object v1

    goto :goto_5

    nop

    :goto_11
    const/high16 p2, 0x3f800000

    goto :goto_16

    nop

    :goto_12
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_1a

    nop

    :goto_13
    move v2, p5

    goto :goto_14

    nop

    :goto_14
    goto :goto_29

    :goto_15
    goto :goto_17

    nop

    :goto_16
    invoke-static {p2, p1}, Ljava/lang/Math;->min(FF)F

    move-result p1

    goto :goto_3

    nop

    :goto_17
    if-eq v1, v4, :cond_2

    goto :goto_24

    :cond_2
    goto :goto_2c

    nop

    :goto_18
    move v5, p3

    goto :goto_2e

    nop

    :goto_19
    int-to-float p2, p2

    goto :goto_2d

    nop

    :goto_1a
    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p1

    goto :goto_1d

    nop

    :goto_1b
    invoke-direct {p0, p2, v5, p4, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->onLayoutCollapseViews(IIII)V

    goto :goto_a

    nop

    :goto_1c
    move v2, p5

    goto :goto_28

    nop

    :goto_1d
    sub-int/2addr p1, v1

    goto :goto_20

    nop

    :goto_1e
    sub-int/2addr v2, v1

    goto :goto_1b

    nop

    :goto_1f
    div-float/2addr v0, v1

    goto :goto_22

    nop

    :goto_20
    int-to-float p1, p1

    goto :goto_2a

    nop

    :goto_21
    sub-int p5, v2, p3

    goto :goto_18

    nop

    :goto_22
    float-to-int v0, v0

    goto :goto_0

    nop

    :goto_23
    goto :goto_30

    :goto_24
    goto :goto_1c

    nop

    :goto_25
    const/4 v3, 0x0

    goto :goto_f

    nop

    :goto_26
    return-void

    :goto_27
    const/4 v2, 0x2

    goto :goto_25

    nop

    :goto_28
    move v1, v3

    :goto_29
    goto :goto_21

    nop

    :goto_2a
    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_b

    nop

    :goto_2b
    invoke-virtual {v1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v1

    goto :goto_23

    nop

    :goto_2c
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_2b

    nop

    :goto_2d
    div-float/2addr p1, p2

    goto :goto_11

    nop

    :goto_2e
    sub-int p3, p5, v1

    goto :goto_1e

    nop

    :goto_2f
    iget v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPendingHeight:I

    :goto_30
    goto :goto_13

    nop

    :goto_31
    iput-boolean v3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mIsInWideMode:Z

    goto :goto_26

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__onLayoutExpandViews',
        'method': '.method protected onLayoutExpandViews(ZIIII)V',
        'method_name': 'onLayoutExpandViews',
        'method_anchors': ['iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;', 'if-eqz p1, :cond_1', 'invoke-virtual {p1}, Landroid/widget/FrameLayout;->getVisibility()I', 'if-nez p1, :cond_1', 'iget p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I', 'if-eqz p1, :cond_1', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;', 'invoke-virtual {p1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I'],
        'type': 'method_replace',
        'search': """.method protected onLayoutExpandViews(ZIIII)V
    .registers 7

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    if-eqz p1, :cond_1

    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result p1

    if-nez p1, :cond_1

    iget p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    if-eqz p1, :cond_1

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v0

    sub-int v0, p5, v0

    invoke-virtual {p1, p2, v0, p4, p5}, Landroid/widget/FrameLayout;->layout(IIII)V

    invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result p1

    if-eqz p1, :cond_0

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result p1

    sub-int p2, p4, p1

    :cond_0
    new-instance p1, Landroid/graphics/Rect;

    invoke-direct {p1}, Landroid/graphics/Rect;-><init>()V

    iget-object p4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p4}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p4

    sub-int/2addr p5, p3

    sub-int/2addr p4, p5

    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p3}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result p3

    add-int/2addr p3, p2

    iget-object p5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p5}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p5

    invoke-virtual {p1, p2, p4, p3, p5}, Landroid/graphics/Rect;->set(IIII)V

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p0, p1}, Landroid/widget/FrameLayout;->setClipBounds(Landroid/graphics/Rect;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onLayoutExpandViews(ZIIII)V
    .registers 7

    goto :goto_19

    nop

    :goto_0
    sub-int/2addr p4, p5

    goto :goto_12

    nop

    :goto_1
    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result p1

    goto :goto_1a

    nop

    :goto_2
    invoke-static {p0}, Lmiuix/internal/util/ViewUtils;->isLayoutRtl(Landroid/view/View;)Z

    move-result p1

    goto :goto_d

    nop

    :goto_3
    sub-int v0, p5, v0

    goto :goto_13

    nop

    :goto_4
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_1f

    nop

    :goto_5
    new-instance p1, Landroid/graphics/Rect;

    goto :goto_10

    nop

    :goto_6
    invoke-virtual {p5}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p5

    goto :goto_14

    nop

    :goto_7
    return-void

    :goto_8
    sub-int/2addr p5, p3

    goto :goto_0

    nop

    :goto_9
    if-nez p1, :cond_0

    goto :goto_1d

    :cond_0
    goto :goto_4

    nop

    :goto_a
    iget p1, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    goto :goto_9

    nop

    :goto_b
    if-nez p1, :cond_1

    goto :goto_1d

    :cond_1
    goto :goto_11

    nop

    :goto_c
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_1

    nop

    :goto_d
    if-nez p1, :cond_2

    goto :goto_1b

    :cond_2
    goto :goto_c

    nop

    :goto_e
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_1c

    nop

    :goto_f
    invoke-virtual {p4}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p4

    goto :goto_8

    nop

    :goto_10
    invoke-direct {p1}, Landroid/graphics/Rect;-><init>()V

    goto :goto_1e

    nop

    :goto_11
    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result p1

    goto :goto_18

    nop

    :goto_12
    iget-object p3, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_16

    nop

    :goto_13
    invoke-virtual {p1, p2, v0, p4, p5}, Landroid/widget/FrameLayout;->layout(IIII)V

    goto :goto_2

    nop

    :goto_14
    invoke-virtual {p1, p2, p4, p3, p5}, Landroid/graphics/Rect;->set(IIII)V

    goto :goto_e

    nop

    :goto_15
    add-int/2addr p3, p2

    goto :goto_17

    nop

    :goto_16
    invoke-virtual {p3}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result p3

    goto :goto_15

    nop

    :goto_17
    iget-object p5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_6

    nop

    :goto_18
    if-eqz p1, :cond_3

    goto :goto_1d

    :cond_3
    goto :goto_a

    nop

    :goto_19
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_b

    nop

    :goto_1a
    sub-int p2, p4, p1

    :goto_1b
    goto :goto_5

    nop

    :goto_1c
    invoke-virtual {p0, p1}, Landroid/widget/FrameLayout;->setClipBounds(Landroid/graphics/Rect;)V

    :goto_1d
    goto :goto_7

    nop

    :goto_1e
    iget-object p4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_f

    nop

    :goto_1f
    invoke-virtual {p1}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v0

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I', 'iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingBottom()I', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingLeft()I', 'invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingRight()I', 'if-lez v0, :cond_0', 'invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 10

    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p1

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v1

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v2

    add-int/2addr v1, v2

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result v2

    sub-int v2, p1, v2

    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingRight()I

    move-result v3

    sub-int/2addr v2, v3

    if-lez v0, :cond_0

    move p2, v0

    goto :goto_0

    :cond_0
    invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p2

    :goto_0
    sub-int/2addr p2, v1

    const/high16 v1, -0x80000000

    invoke-static {p2, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    const/4 v4, 0x0

    if-eqz v3, :cond_1

    invoke-virtual {v3}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v3

    if-ne v3, p0, :cond_1

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    invoke-virtual {p0, v3, v2, p2, v4}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v2

    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    invoke-virtual {v3}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result v3

    goto :goto_1

    :cond_1
    move v3, v4

    :goto_1
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMainContainer:Landroid/view/View;

    invoke-virtual {v5}, Landroid/view/View;->getVisibility()I

    move-result v5

    const/16 v6, 0x8

    if-eq v5, v6, :cond_3

    const/high16 v5, 0x40000000

    invoke-static {v2, v5}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMainContainer:Landroid/view/View;

    invoke-virtual {v5, v2, p2}, Landroid/view/View;->measure(II)V

    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMainContainer:Landroid/view/View;

    invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I

    move-result p2

    invoke-static {v3, p2}, Ljava/lang/Math;->max(II)I

    move-result v3

    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleView:Landroid/widget/TextView;

    if-eqz p2, :cond_3

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->canTitleBeShown()Z

    move-result v2

    if-eqz v2, :cond_2

    move v2, v4

    goto :goto_2

    :cond_2
    const/4 v2, 0x4

    :goto_2
    invoke-virtual {p2, v2}, Landroid/widget/TextView;->setVisibility(I)V

    :cond_3
    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {p2}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result p2

    if-eq p2, v6, :cond_4

    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-static {p1, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v1

    invoke-static {v4, v4}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    invoke-virtual {p2, v1, v2}, Landroid/widget/FrameLayout;->measure(II)V

    :cond_4
    if-gtz v0, :cond_6

    if-lez v3, :cond_5

    iget p2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    invoke-static {v3, p2}, Ljava/lang/Math;->max(II)I

    move-result p2

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mContentInset:I

    add-int v4, p2, v0

    :cond_5
    iput v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    goto :goto_3

    :cond_6
    if-lt v3, v0, :cond_7

    iget p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mContentInset:I

    add-int/2addr v0, p2

    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    :cond_7
    :goto_3
    iget p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v0

    add-int/2addr p2, v0

    iput p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTotalHeight:I

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    const/4 v1, 0x2

    if-ne v0, v1, :cond_8

    iget p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPendingHeight:I

    add-int/2addr p2, v0

    invoke-virtual {p0, p1, p2}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    return-void

    :cond_8
    const/4 v1, 0x1

    if-ne v0, v1, :cond_9

    invoke-virtual {p0, p1, p2}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    return-void

    :cond_9
    iget p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    invoke-virtual {p0, p1, p2}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 10

    goto :goto_14

    nop

    :goto_0
    if-nez v3, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_3a

    nop

    :goto_1
    iget p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    goto :goto_42

    nop

    :goto_2
    invoke-virtual {p2}, Landroid/view/View;->getMeasuredHeight()I

    move-result p2

    goto :goto_4f

    nop

    :goto_3
    move p2, v0

    goto :goto_1f

    nop

    :goto_4
    add-int/2addr p2, v0

    goto :goto_13

    nop

    :goto_5
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_5b

    nop

    :goto_6
    if-eq v0, v1, :cond_1

    goto :goto_12

    :cond_1
    goto :goto_1

    nop

    :goto_7
    goto :goto_4e

    :goto_8
    goto :goto_4d

    nop

    :goto_9
    invoke-virtual {v0}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result v0

    goto :goto_4

    nop

    :goto_a
    iget p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mContentInset:I

    goto :goto_5e

    nop

    :goto_b
    invoke-static {p2, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result p2

    goto :goto_5

    nop

    :goto_c
    invoke-virtual {p0, v3, v2, p2, v4}, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->measureChildView(Landroid/view/View;III)I

    move-result v2

    goto :goto_3f

    nop

    :goto_d
    return-void

    :goto_e
    goto :goto_32

    nop

    :goto_f
    invoke-virtual {p2, v1, v2}, Landroid/widget/FrameLayout;->measure(II)V

    :goto_10
    goto :goto_17

    nop

    :goto_11
    return-void

    :goto_12
    goto :goto_59

    nop

    :goto_13
    iput p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mExpandTotalHeight:I

    goto :goto_2f

    nop

    :goto_14
    invoke-static {p1}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p1

    goto :goto_53

    nop

    :goto_15
    if-ne p2, v6, :cond_2

    goto :goto_10

    :cond_2
    goto :goto_3c

    nop

    :goto_16
    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_4c

    nop

    :goto_17
    if-lez v0, :cond_3

    goto :goto_2c

    :cond_3
    goto :goto_29

    nop

    :goto_18
    if-eq v0, v1, :cond_4

    goto :goto_e

    :cond_4
    goto :goto_52

    nop

    :goto_19
    if-nez v2, :cond_5

    goto :goto_48

    :cond_5
    goto :goto_23

    nop

    :goto_1a
    invoke-virtual {p2, v2}, Landroid/widget/TextView;->setVisibility(I)V

    :goto_1b
    goto :goto_16

    nop

    :goto_1c
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mContentInset:I

    goto :goto_49

    nop

    :goto_1d
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingBottom()I

    move-result v2

    goto :goto_2d

    nop

    :goto_1e
    invoke-virtual {v5}, Landroid/view/View;->getVisibility()I

    move-result v5

    goto :goto_46

    nop

    :goto_1f
    goto :goto_44

    :goto_20
    goto :goto_43

    nop

    :goto_21
    add-int/2addr p2, v0

    goto :goto_50

    nop

    :goto_22
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingTop()I

    move-result v1

    goto :goto_1d

    nop

    :goto_23
    move v2, v4

    goto :goto_47

    nop

    :goto_24
    iget p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    goto :goto_45

    nop

    :goto_25
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_c

    nop

    :goto_26
    const/4 v2, 0x4

    :goto_27
    goto :goto_1a

    nop

    :goto_28
    sub-int/2addr p2, v1

    goto :goto_51

    nop

    :goto_29
    if-gtz v3, :cond_6

    goto :goto_4a

    :cond_6
    goto :goto_38

    nop

    :goto_2a
    if-eq v3, p0, :cond_7

    goto :goto_8

    :cond_7
    goto :goto_25

    nop

    :goto_2b
    goto :goto_60

    :goto_2c
    goto :goto_54

    nop

    :goto_2d
    add-int/2addr v1, v2

    goto :goto_41

    nop

    :goto_2e
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->canTitleBeShown()Z

    move-result v2

    goto :goto_19

    nop

    :goto_2f
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    goto :goto_55

    nop

    :goto_30
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMainContainer:Landroid/view/View;

    goto :goto_1e

    nop

    :goto_31
    invoke-virtual {p0, p1, p2}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_33

    nop

    :goto_32
    iget p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    goto :goto_31

    nop

    :goto_33
    return-void

    :goto_34
    invoke-static {v4, v4}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto :goto_f

    nop

    :goto_35
    invoke-static {v3, p2}, Ljava/lang/Math;->max(II)I

    move-result p2

    goto :goto_1c

    nop

    :goto_36
    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mTitleView:Landroid/widget/TextView;

    goto :goto_40

    nop

    :goto_37
    invoke-virtual {v5, v2, p2}, Landroid/view/View;->measure(II)V

    goto :goto_5d

    nop

    :goto_38
    iget p2, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMinHeight:I

    goto :goto_35

    nop

    :goto_39
    sub-int v2, p1, v2

    goto :goto_61

    nop

    :goto_3a
    invoke-virtual {v3}, Landroid/widget/LinearLayout;->getParent()Landroid/view/ViewParent;

    move-result-object v3

    goto :goto_2a

    nop

    :goto_3b
    sub-int/2addr v2, v3

    goto :goto_5a

    nop

    :goto_3c
    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_58

    nop

    :goto_3d
    iget-object v5, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMainContainer:Landroid/view/View;

    goto :goto_37

    nop

    :goto_3e
    iput v4, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    goto :goto_2b

    nop

    :goto_3f
    iget-object v3, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_4b

    nop

    :goto_40
    if-nez p2, :cond_8

    goto :goto_1b

    :cond_8
    goto :goto_2e

    nop

    :goto_41
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingLeft()I

    move-result v2

    goto :goto_39

    nop

    :goto_42
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mPendingHeight:I

    goto :goto_21

    nop

    :goto_43
    invoke-static {p2}, Landroid/view/View$MeasureSpec;->getSize(I)I

    move-result p2

    :goto_44
    goto :goto_28

    nop

    :goto_45
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMovableMainContainer:Landroid/widget/FrameLayout;

    goto :goto_9

    nop

    :goto_46
    const/16 v6, 0x8

    goto :goto_57

    nop

    :goto_47
    goto :goto_27

    :goto_48
    goto :goto_26

    nop

    :goto_49
    add-int v4, p2, v0

    :goto_4a
    goto :goto_3e

    nop

    :goto_4b
    invoke-virtual {v3}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result v3

    goto :goto_7

    nop

    :goto_4c
    invoke-virtual {p2}, Landroid/widget/FrameLayout;->getVisibility()I

    move-result p2

    goto :goto_15

    nop

    :goto_4d
    move v3, v4

    :goto_4e
    goto :goto_30

    nop

    :goto_4f
    invoke-static {v3, p2}, Ljava/lang/Math;->max(II)I

    move-result v3

    goto :goto_36

    nop

    :goto_50
    invoke-virtual {p0, p1, p2}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_11

    nop

    :goto_51
    const/high16 v1, -0x80000000

    goto :goto_b

    nop

    :goto_52
    invoke-virtual {p0, p1, p2}, Landroid/view/ViewGroup;->setMeasuredDimension(II)V

    goto :goto_d

    nop

    :goto_53
    iget v0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mTitleMaxHeight:I

    goto :goto_22

    nop

    :goto_54
    if-ge v3, v0, :cond_9

    goto :goto_60

    :cond_9
    goto :goto_a

    nop

    :goto_55
    const/4 v1, 0x2

    goto :goto_6

    nop

    :goto_56
    invoke-static {v2, v5}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v2

    goto :goto_3d

    nop

    :goto_57
    if-ne v5, v6, :cond_a

    goto :goto_1b

    :cond_a
    goto :goto_5c

    nop

    :goto_58
    invoke-static {p1, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v1

    goto :goto_34

    nop

    :goto_59
    const/4 v1, 0x1

    goto :goto_18

    nop

    :goto_5a
    if-gtz v0, :cond_b

    goto :goto_20

    :cond_b
    goto :goto_3

    nop

    :goto_5b
    const/4 v4, 0x0

    goto :goto_0

    nop

    :goto_5c
    const/high16 v5, 0x40000000

    goto :goto_56

    nop

    :goto_5d
    iget-object p2, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mMainContainer:Landroid/view/View;

    goto :goto_2

    nop

    :goto_5e
    add-int/2addr v0, p2

    goto :goto_5f

    nop

    :goto_5f
    iput v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mCollapseTotalHeight:I

    :goto_60
    goto :goto_24

    nop

    :goto_61
    invoke-virtual {p0}, Landroid/view/ViewGroup;->getPaddingRight()I

    move-result v3

    goto :goto_3b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__onRestoreInstanceState',
        'method': '.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V',
        'method_name': 'onRestoreInstanceState',
        'method_anchors': ['check-cast p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;', 'invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;', 'invoke-super {p0, v0}, Landroid/view/ViewGroup;->onRestoreInstanceState(Landroid/os/Parcelable;)V', 'iget-object v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->title:Ljava/lang/CharSequence;', 'invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setTitle(Ljava/lang/CharSequence;)V', 'iget-object v1, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->defaultButtonText:Ljava/lang/CharSequence;', 'invoke-virtual {p0, v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setButton(ILjava/lang/CharSequence;)V', 'iget-boolean v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->isOverflowOpen:Z'],
        'type': 'method_replace',
        'search': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 4

    check-cast p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;

    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    invoke-super {p0, v0}, Landroid/view/ViewGroup;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    iget-object v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->title:Ljava/lang/CharSequence;

    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setTitle(Ljava/lang/CharSequence;)V

    const v0, 0x102001a

    iget-object v1, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->defaultButtonText:Ljava/lang/CharSequence;

    invoke-virtual {p0, v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setButton(ILjava/lang/CharSequence;)V

    iget-boolean v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->isOverflowOpen:Z

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->postShowOverflowMenu()V

    :cond_0
    iget p1, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->expandState:I

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setExpandState(I)V

    return-void
.end method""",
        'replacement': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 4

    goto :goto_5

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->postShowOverflowMenu()V

    :goto_2
    goto :goto_8

    nop

    :goto_3
    const v0, 0x102001a

    goto :goto_d

    nop

    :goto_4
    iget-boolean v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->isOverflowOpen:Z

    goto :goto_0

    nop

    :goto_5
    check-cast p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;

    goto :goto_c

    nop

    :goto_6
    invoke-super {p0, v0}, Landroid/view/ViewGroup;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_7

    nop

    :goto_7
    iget-object v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->title:Ljava/lang/CharSequence;

    goto :goto_b

    nop

    :goto_8
    iget p1, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->expandState:I

    goto :goto_9

    nop

    :goto_9
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setExpandState(I)V

    goto :goto_a

    nop

    :goto_a
    return-void

    :goto_b
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setTitle(Ljava/lang/CharSequence;)V

    goto :goto_3

    nop

    :goto_c
    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_6

    nop

    :goto_d
    iget-object v1, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->defaultButtonText:Ljava/lang/CharSequence;

    goto :goto_e

    nop

    :goto_e
    invoke-virtual {p0, v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->setButton(ILjava/lang/CharSequence;)V

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContextView__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState()Landroid/os/Parcelable;',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;', 'invoke-super {p0}, Landroid/view/ViewGroup;->onSaveInstanceState()Landroid/os/Parcelable;', 'invoke-direct {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;-><init>(Landroid/os/Parcelable;)V', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->isOverflowMenuShowing()Z', 'iput-boolean v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->isOverflowOpen:Z', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->getTitle()Ljava/lang/CharSequence;', 'iput-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->title:Ljava/lang/CharSequence;', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 3

    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;

    invoke-super {p0}, Landroid/view/ViewGroup;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v1

    invoke-direct {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;-><init>(Landroid/os/Parcelable;)V

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->isOverflowMenuShowing()Z

    move-result v1

    iput-boolean v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->isOverflowOpen:Z

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->getTitle()Ljava/lang/CharSequence;

    move-result-object v1

    iput-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->title:Ljava/lang/CharSequence;

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    if-eqz v1, :cond_0

    invoke-virtual {v1}, Landroid/widget/Button;->getText()Ljava/lang/CharSequence;

    move-result-object v1

    iput-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->defaultButtonText:Ljava/lang/CharSequence;

    :cond_0
    iget p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    const/4 v1, 0x2

    if-ne p0, v1, :cond_1

    const/4 p0, 0x0

    iput p0, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->expandState:I

    return-object v0

    :cond_1
    iput p0, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->expandState:I

    return-object v0
.end method""",
        'replacement': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 3

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->isOverflowMenuShowing()Z

    move-result v1

    goto :goto_12

    nop

    :goto_1
    invoke-virtual {v1}, Landroid/widget/Button;->getText()Ljava/lang/CharSequence;

    move-result-object v1

    goto :goto_6

    nop

    :goto_2
    return-object v0

    :goto_3
    new-instance v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;

    goto :goto_10

    nop

    :goto_4
    iput p0, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->expandState:I

    goto :goto_9

    nop

    :goto_5
    const/4 v1, 0x2

    goto :goto_f

    nop

    :goto_6
    iput-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->defaultButtonText:Ljava/lang/CharSequence;

    :goto_7
    goto :goto_11

    nop

    :goto_8
    if-nez v1, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_1

    nop

    :goto_9
    return-object v0

    :goto_a
    goto :goto_d

    nop

    :goto_b
    invoke-direct {v0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;-><init>(Landroid/os/Parcelable;)V

    goto :goto_0

    nop

    :goto_c
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->getTitle()Ljava/lang/CharSequence;

    move-result-object v1

    goto :goto_e

    nop

    :goto_d
    iput p0, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->expandState:I

    goto :goto_2

    nop

    :goto_e
    iput-object v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->title:Ljava/lang/CharSequence;

    goto :goto_13

    nop

    :goto_f
    if-eq p0, v1, :cond_1

    goto :goto_a

    :cond_1
    goto :goto_14

    nop

    :goto_10
    invoke-super {p0}, Landroid/view/ViewGroup;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v1

    goto :goto_b

    nop

    :goto_11
    iget p0, p0, Lmiuix/appcompat/internal/app/widget/AbsActionBarView;->mInnerExpandState:I

    goto :goto_5

    nop

    :goto_12
    iput-boolean v1, v0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView$SavedState;->isOverflowOpen:Z

    goto :goto_c

    nop

    :goto_13
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->mButton2:Landroid/widget/Button;

    goto :goto_8

    nop

    :goto_14
    const/4 p0, 0x0

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
