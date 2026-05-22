TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/ActionBarContainer.smali'
CLASS_FALLBACK_NAMES = ['ActionBarContainer.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;', '.implements Lmiuix/view/BlurableWidget;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__getActionBarCoordinateListener',
        'method': '.method getActionBarCoordinateListener()Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;',
        'method_name': 'getActionBarCoordinateListener',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mCoordinateListener:Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getActionBarCoordinateListener()Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;
    .registers 1

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mCoordinateListener:Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;

    return-object p0
.end method""",
        'replacement': """.method getActionBarCoordinateListener()Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mCoordinateListener:Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__getInsetHeight',
        'method': '.method getInsetHeight()I',
        'method_name': 'getInsetHeight',
        'method_anchors': ['iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsSplit:Z', 'if-nez v0, :cond_0', 'return v1', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getActionMenuViewInsetHeight(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)I', 'invoke-static {v1, v0}, Ljava/lang/Math;->max(II)I', 'iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'invoke-direct {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getActionMenuViewInsetHeight(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)I'],
        'type': 'method_replace',
        'search': """.method getInsetHeight()I
    .registers 3

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsSplit:Z

    const/4 v1, 0x0

    if-nez v0, :cond_0

    return v1

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getActionMenuViewInsetHeight(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)I

    move-result v0

    invoke-static {v1, v0}, Ljava/lang/Math;->max(II)I

    move-result v0

    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getActionMenuViewInsetHeight(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)I

    move-result p0

    invoke-static {v0, p0}, Ljava/lang/Math;->max(II)I

    move-result p0

    return p0
.end method""",
        'replacement': """.method getInsetHeight()I
    .registers 3

    goto :goto_4

    nop

    :goto_0
    iget-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_1

    nop

    :goto_1
    invoke-direct {p0, v1}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getActionMenuViewInsetHeight(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)I

    move-result p0

    goto :goto_6

    nop

    :goto_2
    invoke-static {v1, v0}, Ljava/lang/Math;->max(II)I

    move-result v0

    goto :goto_0

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_a

    nop

    :goto_4
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsSplit:Z

    goto :goto_b

    nop

    :goto_5
    if-eqz v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_7

    nop

    :goto_6
    invoke-static {v0, p0}, Ljava/lang/Math;->max(II)I

    move-result p0

    goto :goto_9

    nop

    :goto_7
    return v1

    :goto_8
    goto :goto_3

    nop

    :goto_9
    return p0

    :goto_a
    invoke-direct {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->getActionMenuViewInsetHeight(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)I

    move-result v0

    goto :goto_2

    nop

    :goto_b
    const/4 v1, 0x0

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__onActionModeMenuViewAdded',
        'method': '.method onActionModeMenuViewAdded(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V',
        'method_name': 'onActionModeMenuViewAdded',
        'method_anchors': ['iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'if-eqz p1, :cond_2', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z', 'if-eqz v0, :cond_2', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z'],
        'type': 'method_replace',
        'search': """.method onActionModeMenuViewAdded(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V
    .registers 3

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-eqz p1, :cond_2

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result p0

    goto :goto_0

    :cond_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z

    move-result p0

    :goto_0
    if-eqz p0, :cond_1

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p0

    if-lez p0, :cond_1

    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p0

    if-lez p0, :cond_1

    const/4 p0, 0x1

    goto :goto_1

    :cond_1
    const/4 p0, 0x0

    :goto_1
    invoke-interface {p1, p0}, Lmiuix/view/BlurableWidget;->applyBlur(Z)V

    :cond_2
    return-void
.end method""",
        'replacement': """.method onActionModeMenuViewAdded(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V
    .registers 3

    goto :goto_a

    nop

    :goto_0
    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result p0

    goto :goto_e

    nop

    :goto_1
    invoke-interface {p1, p0}, Lmiuix/view/BlurableWidget;->applyBlur(Z)V

    :goto_2
    goto :goto_5

    nop

    :goto_3
    if-gtz p0, :cond_0

    goto :goto_15

    :cond_0
    goto :goto_17

    nop

    :goto_4
    if-gtz p0, :cond_1

    goto :goto_15

    :cond_1
    goto :goto_12

    nop

    :goto_5
    return-void

    :goto_6
    const/4 p0, 0x0

    :goto_7
    goto :goto_1

    nop

    :goto_8
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z

    move-result p0

    :goto_9
    goto :goto_16

    nop

    :goto_a
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_11

    nop

    :goto_b
    if-nez v0, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_d

    nop

    :goto_c
    if-nez v0, :cond_3

    goto :goto_f

    :cond_3
    goto :goto_0

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    goto :goto_c

    nop

    :goto_e
    goto :goto_9

    :goto_f
    goto :goto_8

    nop

    :goto_10
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z

    move-result v0

    goto :goto_b

    nop

    :goto_11
    if-nez p1, :cond_4

    goto :goto_2

    :cond_4
    goto :goto_10

    nop

    :goto_12
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredHeight()I

    move-result p0

    goto :goto_3

    nop

    :goto_13
    invoke-virtual {p1}, Landroid/widget/LinearLayout;->getMeasuredWidth()I

    move-result p0

    goto :goto_4

    nop

    :goto_14
    goto :goto_7

    :goto_15
    goto :goto_6

    nop

    :goto_16
    if-nez p0, :cond_5

    goto :goto_15

    :cond_5
    goto :goto_13

    nop

    :goto_17
    const/4 p0, 0x1

    goto :goto_14

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__onActionModeMenuViewRemoved',
        'method': '.method onActionModeMenuViewRemoved(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V',
        'method_name': 'onActionModeMenuViewRemoved',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'if-ne v0, p1, :cond_0', 'iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'return-void'],
        'type': 'method_replace',
        'search': """.method onActionModeMenuViewRemoved(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V
    .registers 3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-ne v0, p1, :cond_0

    const/4 p1, 0x0

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    :cond_0
    return-void
.end method""",
        'replacement': """.method onActionModeMenuViewRemoved(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    :goto_1
    goto :goto_3

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionModeMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_5

    nop

    :goto_3
    return-void

    :goto_4
    const/4 p1, 0x0

    goto :goto_0

    nop

    :goto_5
    if-eq v0, p1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__onResidentActionMenuViewAdded',
        'method': '.method onResidentActionMenuViewAdded(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V',
        'method_name': 'onResidentActionMenuViewAdded',
        'method_anchors': ['iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'if-eqz p1, :cond_2', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z', 'if-eqz v0, :cond_2', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z', 'invoke-interface {p1, v0}, Lmiuix/view/BlurableWidget;->setSupportBlur(Z)V', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z', 'invoke-interface {p1, v0}, Lmiuix/view/BlurableWidget;->setEnableBlur(Z)V'],
        'type': 'method_replace',
        'search': """.method onResidentActionMenuViewAdded(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V
    .registers 3

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-eqz p1, :cond_2

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z

    move-result v0

    invoke-interface {p1, v0}, Lmiuix/view/BlurableWidget;->setSupportBlur(Z)V

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z

    move-result v0

    invoke-interface {p1, v0}, Lmiuix/view/BlurableWidget;->setEnableBlur(Z)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    goto :goto_0

    :cond_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z

    move-result v0

    :goto_0
    if-eqz v0, :cond_1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v0

    if-lez v0, :cond_1

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p0

    if-lez p0, :cond_1

    const/4 p0, 0x1

    goto :goto_1

    :cond_1
    const/4 p0, 0x0

    :goto_1
    invoke-interface {p1, p0}, Lmiuix/view/BlurableWidget;->applyBlur(Z)V

    :cond_2
    return-void
.end method""",
        'replacement': """.method onResidentActionMenuViewAdded(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getMeasuredWidth()I

    move-result v0

    goto :goto_12

    nop

    :goto_1
    const/4 p0, 0x0

    :goto_2
    goto :goto_c

    nop

    :goto_3
    invoke-interface {p1, v0}, Lmiuix/view/BlurableWidget;->setEnableBlur(Z)V

    goto :goto_f

    nop

    :goto_4
    if-nez p1, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_14

    nop

    :goto_5
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_4

    nop

    :goto_6
    if-nez v0, :cond_1

    goto :goto_18

    :cond_1
    goto :goto_0

    nop

    :goto_7
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z

    move-result v0

    goto :goto_b

    nop

    :goto_8
    return-void

    :goto_9
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z

    move-result v0

    goto :goto_3

    nop

    :goto_a
    if-gtz p0, :cond_2

    goto :goto_18

    :cond_2
    goto :goto_10

    nop

    :goto_b
    invoke-interface {p1, v0}, Lmiuix/view/BlurableWidget;->setSupportBlur(Z)V

    goto :goto_9

    nop

    :goto_c
    invoke-interface {p1, p0}, Lmiuix/view/BlurableWidget;->applyBlur(Z)V

    :goto_d
    goto :goto_8

    nop

    :goto_e
    if-nez v0, :cond_3

    goto :goto_d

    :cond_3
    goto :goto_7

    nop

    :goto_f
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    goto :goto_13

    nop

    :goto_10
    const/4 p0, 0x1

    goto :goto_17

    nop

    :goto_11
    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    goto :goto_15

    nop

    :goto_12
    if-gtz v0, :cond_4

    goto :goto_18

    :cond_4
    goto :goto_1b

    nop

    :goto_13
    if-nez v0, :cond_5

    goto :goto_16

    :cond_5
    goto :goto_11

    nop

    :goto_14
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z

    move-result v0

    goto :goto_e

    nop

    :goto_15
    goto :goto_1a

    :goto_16
    goto :goto_19

    nop

    :goto_17
    goto :goto_2

    :goto_18
    goto :goto_1

    nop

    :goto_19
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z

    move-result v0

    :goto_1a
    goto :goto_6

    nop

    :goto_1b
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getMeasuredHeight()I

    move-result p0

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__onResidentActionMenuViewRemoved',
        'method': '.method onResidentActionMenuViewRemoved(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V',
        'method_name': 'onResidentActionMenuViewRemoved',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'if-ne v0, p1, :cond_0', 'iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;', 'return-void'],
        'type': 'method_replace',
        'search': """.method onResidentActionMenuViewRemoved(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V
    .registers 3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    if-ne v0, p1, :cond_0

    const/4 p1, 0x0

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    :cond_0
    return-void
.end method""",
        'replacement': """.method onResidentActionMenuViewRemoved(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    goto :goto_2

    nop

    :goto_1
    const/4 p1, 0x0

    goto :goto_3

    nop

    :goto_2
    if-eq v0, p1, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_1

    nop

    :goto_3
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mResidentActionMenuView:Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;

    :goto_4
    goto :goto_5

    nop

    :goto_5
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__drawableStateChanged',
        'method': '.method protected drawableStateChanged()V',
        'method_name': 'drawableStateChanged',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->drawableStateChanged()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBackground:Landroid/graphics/drawable/Drawable;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Landroid/graphics/drawable/Drawable;->isStateful()Z', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBackground:Landroid/graphics/drawable/Drawable;', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getDrawableState()[I', 'invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setState([I)Z'],
        'type': 'method_replace',
        'search': """.method protected drawableStateChanged()V
    .registers 3

    invoke-super {p0}, Landroid/widget/FrameLayout;->drawableStateChanged()V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Landroid/graphics/drawable/Drawable;->isStateful()Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBackground:Landroid/graphics/drawable/Drawable;

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getDrawableState()[I

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setState([I)Z

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mStackedBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_1

    invoke-virtual {v0}, Landroid/graphics/drawable/Drawable;->isStateful()Z

    move-result v0

    if-eqz v0, :cond_1

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mStackedBackground:Landroid/graphics/drawable/Drawable;

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getDrawableState()[I

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setState([I)Z

    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mSplitBackground:Landroid/graphics/drawable/Drawable;

    if-eqz v0, :cond_2

    invoke-virtual {v0}, Landroid/graphics/drawable/Drawable;->isStateful()Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mSplitBackground:Landroid/graphics/drawable/Drawable;

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getDrawableState()[I

    move-result-object p0

    invoke-virtual {v0, p0}, Landroid/graphics/drawable/Drawable;->setState([I)Z

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected drawableStateChanged()V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_18

    nop

    :goto_1
    return-void

    :goto_2
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_15

    nop

    :goto_3
    invoke-virtual {v0}, Landroid/graphics/drawable/Drawable;->isStateful()Z

    move-result v0

    goto :goto_16

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_6

    nop

    :goto_5
    invoke-super {p0}, Landroid/widget/FrameLayout;->drawableStateChanged()V

    goto :goto_2

    nop

    :goto_6
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getDrawableState()[I

    move-result-object v1

    goto :goto_9

    nop

    :goto_7
    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setState([I)Z

    :goto_8
    goto :goto_d

    nop

    :goto_9
    invoke-virtual {v0, v1}, Landroid/graphics/drawable/Drawable;->setState([I)Z

    :goto_a
    goto :goto_13

    nop

    :goto_b
    if-nez v0, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_c

    nop

    :goto_c
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mStackedBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_12

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mSplitBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_0

    nop

    :goto_e
    invoke-virtual {v0, p0}, Landroid/graphics/drawable/Drawable;->setState([I)Z

    :goto_f
    goto :goto_1

    nop

    :goto_10
    invoke-virtual {v0}, Landroid/graphics/drawable/Drawable;->isStateful()Z

    move-result v0

    goto :goto_b

    nop

    :goto_11
    if-nez v0, :cond_2

    goto :goto_8

    :cond_2
    goto :goto_10

    nop

    :goto_12
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getDrawableState()[I

    move-result-object v1

    goto :goto_7

    nop

    :goto_13
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mStackedBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_11

    nop

    :goto_14
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mSplitBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_19

    nop

    :goto_15
    if-nez v0, :cond_3

    goto :goto_a

    :cond_3
    goto :goto_3

    nop

    :goto_16
    if-nez v0, :cond_4

    goto :goto_a

    :cond_4
    goto :goto_4

    nop

    :goto_17
    if-nez v0, :cond_5

    goto :goto_f

    :cond_5
    goto :goto_14

    nop

    :goto_18
    invoke-virtual {v0}, Landroid/graphics/drawable/Drawable;->isStateful()Z

    move-result v0

    goto :goto_17

    nop

    :goto_19
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getDrawableState()[I

    move-result-object p0

    goto :goto_e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->resizeSplitMaxHeight()V', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBlurHelper:Lmiuix/view/MiuiBlurUiHelper;', 'if-eqz p1, :cond_0', 'invoke-virtual {p1}, Lmiuix/view/MiuiBlurUiHelper;->onConfigChanged()V', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBlurHelper:Lmiuix/view/MiuiBlurUiHelper;', 'invoke-virtual {p1}, Lmiuix/view/MiuiBlurUiHelper;->isEnableBlur()Z', 'if-nez p1, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->resizeSplitMaxHeight()V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBlurHelper:Lmiuix/view/MiuiBlurUiHelper;

    if-eqz p1, :cond_0

    invoke-virtual {p1}, Lmiuix/view/MiuiBlurUiHelper;->onConfigChanged()V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBlurHelper:Lmiuix/view/MiuiBlurUiHelper;

    invoke-virtual {p1}, Lmiuix/view/MiuiBlurUiHelper;->isEnableBlur()Z

    move-result p1

    if-nez p1, :cond_0

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserBgViewApplyBlur:Ljava/lang/Boolean;

    if-nez p1, :cond_0

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->updateBackgroundInternal(Z)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserBgViewApplyBlur:Ljava/lang/Boolean;

    goto :goto_2

    nop

    :goto_1
    const/4 p1, 0x0

    goto :goto_b

    nop

    :goto_2
    if-eqz p1, :cond_0

    goto :goto_c

    :cond_0
    goto :goto_1

    nop

    :goto_3
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_8

    nop

    :goto_4
    if-eqz p1, :cond_1

    goto :goto_c

    :cond_1
    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p1}, Lmiuix/view/MiuiBlurUiHelper;->isEnableBlur()Z

    move-result p1

    goto :goto_4

    nop

    :goto_6
    if-nez p1, :cond_2

    goto :goto_c

    :cond_2
    goto :goto_a

    nop

    :goto_7
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBlurHelper:Lmiuix/view/MiuiBlurUiHelper;

    goto :goto_5

    nop

    :goto_8
    invoke-direct {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->resizeSplitMaxHeight()V

    goto :goto_d

    nop

    :goto_9
    return-void

    :goto_a
    invoke-virtual {p1}, Lmiuix/view/MiuiBlurUiHelper;->onConfigChanged()V

    goto :goto_7

    nop

    :goto_b
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->updateBackgroundInternal(Z)V

    :goto_c
    goto :goto_9

    nop

    :goto_d
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBlurHelper:Lmiuix/view/MiuiBlurUiHelper;

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__onDetachedFromWindow',
        'method': '.method protected onDetachedFromWindow()V',
        'method_name': 'onDetachedFromWindow',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V', 'invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setActionBarCoordinateListener(Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;)V', 'iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionBarTransitionListeners:Ljava/util/List;', 'invoke-interface {p0}, Ljava/util/List;->clear()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDetachedFromWindow()V
    .registers 2

    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setActionBarCoordinateListener(Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;)V

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionBarTransitionListeners:Ljava/util/List;

    invoke-interface {p0}, Ljava/util/List;->clear()V

    return-void
.end method""",
        'replacement': """.method protected onDetachedFromWindow()V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    const/4 v0, 0x0

    goto :goto_5

    nop

    :goto_1
    invoke-interface {p0}, Ljava/util/List;->clear()V

    goto :goto_3

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionBarTransitionListeners:Ljava/util/List;

    goto :goto_1

    nop

    :goto_3
    return-void

    :goto_4
    invoke-super {p0}, Landroid/widget/FrameLayout;->onDetachedFromWindow()V

    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setActionBarCoordinateListener(Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;)V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__onRestoreInstanceState',
        'method': '.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V',
        'method_name': 'onRestoreInstanceState',
        'method_anchors': ['check-cast p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;', 'invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;', 'invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V', 'iget v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->userActionBarApplyBlur:I', 'if-ne v0, v3, :cond_0', 'iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;', 'if-nez v0, :cond_1', 'sget-object v0, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;'],
        'type': 'method_replace',
        'search': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 6

    check-cast p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;

    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    iget v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->userActionBarApplyBlur:I

    const/4 v1, 0x0

    const/4 v2, 0x1

    const/4 v3, -0x1

    if-ne v0, v3, :cond_0

    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    goto :goto_0

    :cond_0
    if-nez v0, :cond_1

    sget-object v0, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    goto :goto_0

    :cond_1
    if-ne v0, v2, :cond_2

    sget-object v0, Ljava/lang/Boolean;->TRUE:Ljava/lang/Boolean;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    :cond_2
    :goto_0
    iget v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->userSplitActionBarApplyBlur:I

    if-ne v0, v3, :cond_3

    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    goto :goto_1

    :cond_3
    if-nez v0, :cond_4

    sget-object v0, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    goto :goto_1

    :cond_4
    if-ne v0, v2, :cond_5

    sget-object v0, Ljava/lang/Boolean;->TRUE:Ljava/lang/Boolean;

    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    :cond_5
    :goto_1
    iget-boolean v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarSupportBlur:Z

    if-eqz v0, :cond_6

    invoke-virtual {p0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setSupportBlur(Z)V

    :cond_6
    iget-boolean v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarEnableBlur:Z

    if-eqz v0, :cond_7

    invoke-virtual {p0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setEnableBlur(Z)V

    :cond_7
    iget-boolean p1, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarApplyBlur:Z

    if-eqz p1, :cond_8

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z

    move-result p1

    if-eqz p1, :cond_8

    invoke-virtual {p0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V

    :cond_8
    return-void
.end method""",
        'replacement': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 6

    goto :goto_1b

    nop

    :goto_0
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    goto :goto_f

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_2

    nop

    :goto_2
    sget-object v0, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    goto :goto_17

    nop

    :goto_3
    const/4 v2, 0x1

    goto :goto_7

    nop

    :goto_4
    sget-object v0, Ljava/lang/Boolean;->TRUE:Ljava/lang/Boolean;

    goto :goto_29

    nop

    :goto_5
    invoke-virtual {p0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setEnableBlur(Z)V

    :goto_6
    goto :goto_2e

    nop

    :goto_7
    const/4 v3, -0x1

    goto :goto_30

    nop

    :goto_8
    invoke-super {p0, v0}, Landroid/widget/FrameLayout;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_22

    nop

    :goto_9
    const/4 v1, 0x0

    goto :goto_3

    nop

    :goto_a
    goto :goto_12

    :goto_b
    goto :goto_2b

    nop

    :goto_c
    goto :goto_2a

    :goto_d
    goto :goto_15

    nop

    :goto_e
    iget-boolean v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarEnableBlur:Z

    goto :goto_20

    nop

    :goto_f
    goto :goto_2a

    :goto_10
    goto :goto_2d

    nop

    :goto_11
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    :goto_12
    goto :goto_2c

    nop

    :goto_13
    goto :goto_12

    :goto_14
    goto :goto_1

    nop

    :goto_15
    if-eqz v0, :cond_1

    goto :goto_10

    :cond_1
    goto :goto_18

    nop

    :goto_16
    invoke-virtual {p1}, Landroid/view/View$BaseSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_8

    nop

    :goto_17
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    goto :goto_a

    nop

    :goto_18
    sget-object v0, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    goto :goto_0

    nop

    :goto_19
    if-nez v0, :cond_2

    goto :goto_1f

    :cond_2
    goto :goto_1e

    nop

    :goto_1a
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z

    move-result p1

    goto :goto_2f

    nop

    :goto_1b
    check-cast p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;

    goto :goto_16

    nop

    :goto_1c
    if-eq v0, v3, :cond_3

    goto :goto_d

    :cond_3
    goto :goto_1d

    nop

    :goto_1d
    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    goto :goto_c

    nop

    :goto_1e
    invoke-virtual {p0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->setSupportBlur(Z)V

    :goto_1f
    goto :goto_e

    nop

    :goto_20
    if-nez v0, :cond_4

    goto :goto_6

    :cond_4
    goto :goto_5

    nop

    :goto_21
    return-void

    :goto_22
    iget v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->userActionBarApplyBlur:I

    goto :goto_9

    nop

    :goto_23
    iput-object v1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    goto :goto_13

    nop

    :goto_24
    if-nez p1, :cond_5

    goto :goto_28

    :cond_5
    goto :goto_1a

    nop

    :goto_25
    sget-object v0, Ljava/lang/Boolean;->TRUE:Ljava/lang/Boolean;

    goto :goto_11

    nop

    :goto_26
    iget-boolean v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarSupportBlur:Z

    goto :goto_19

    nop

    :goto_27
    invoke-virtual {p0, v2}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V

    :goto_28
    goto :goto_21

    nop

    :goto_29
    iput-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    :goto_2a
    goto :goto_26

    nop

    :goto_2b
    if-eq v0, v2, :cond_6

    goto :goto_12

    :cond_6
    goto :goto_25

    nop

    :goto_2c
    iget v0, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->userSplitActionBarApplyBlur:I

    goto :goto_1c

    nop

    :goto_2d
    if-eq v0, v2, :cond_7

    goto :goto_2a

    :cond_7
    goto :goto_4

    nop

    :goto_2e
    iget-boolean p1, p1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarApplyBlur:Z

    goto :goto_24

    nop

    :goto_2f
    if-nez p1, :cond_8

    goto :goto_28

    :cond_8
    goto :goto_27

    nop

    :goto_30
    if-eq v0, v3, :cond_9

    goto :goto_14

    :cond_9
    goto :goto_23

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState()Landroid/os/Parcelable;',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;', 'new-instance v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;', 'invoke-direct {v1, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;-><init>(Landroid/os/Parcelable;)V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;', 'if-nez v0, :cond_0', 'invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z', 'if-eqz v0, :cond_1', 'iput v0, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->userActionBarApplyBlur:I'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 6

    invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    new-instance v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;

    invoke-direct {v1, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;-><init>(Landroid/os/Parcelable;)V

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    const/4 v2, 0x0

    const/4 v3, 0x1

    const/4 v4, -0x1

    if-nez v0, :cond_0

    move v0, v4

    goto :goto_0

    :cond_0
    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    if-eqz v0, :cond_1

    move v0, v3

    goto :goto_0

    :cond_1
    move v0, v2

    :goto_0
    iput v0, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->userActionBarApplyBlur:I

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    if-nez v0, :cond_2

    move v2, v4

    goto :goto_1

    :cond_2
    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    if-eqz v0, :cond_3

    move v2, v3

    :cond_3
    :goto_1
    iput v2, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->userSplitActionBarApplyBlur:I

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z

    move-result v0

    iput-boolean v0, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarSupportBlur:Z

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z

    move-result v0

    iput-boolean v0, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarEnableBlur:Z

    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isApplyBlur()Z

    move-result p0

    iput-boolean p0, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarApplyBlur:Z

    return-object v1
.end method""",
        'replacement': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 6

    goto :goto_18

    nop

    :goto_0
    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    goto :goto_15

    nop

    :goto_1
    if-nez v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_f

    nop

    :goto_2
    const/4 v4, -0x1

    goto :goto_17

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplySplitActionBarBgBlur:Ljava/lang/Boolean;

    goto :goto_1a

    nop

    :goto_4
    const/4 v3, 0x1

    goto :goto_2

    nop

    :goto_5
    goto :goto_1d

    :goto_6
    goto :goto_1c

    nop

    :goto_7
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isApplyBlur()Z

    move-result p0

    goto :goto_1f

    nop

    :goto_8
    iput v0, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->userActionBarApplyBlur:I

    goto :goto_3

    nop

    :goto_9
    iput v2, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->userSplitActionBarApplyBlur:I

    goto :goto_a

    nop

    :goto_a
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isSupportBlur()Z

    move-result v0

    goto :goto_19

    nop

    :goto_b
    move v0, v4

    goto :goto_20

    nop

    :goto_c
    const/4 v2, 0x0

    goto :goto_4

    nop

    :goto_d
    invoke-virtual {p0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->isEnableBlur()Z

    move-result v0

    goto :goto_16

    nop

    :goto_e
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    goto :goto_c

    nop

    :goto_f
    move v0, v3

    goto :goto_5

    nop

    :goto_10
    move v2, v3

    :goto_11
    goto :goto_9

    nop

    :goto_12
    new-instance v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;

    goto :goto_1b

    nop

    :goto_13
    return-object v1

    :goto_14
    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    goto :goto_1

    nop

    :goto_15
    if-nez v0, :cond_1

    goto :goto_11

    :cond_1
    goto :goto_10

    nop

    :goto_16
    iput-boolean v0, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarEnableBlur:Z

    goto :goto_7

    nop

    :goto_17
    if-eqz v0, :cond_2

    goto :goto_21

    :cond_2
    goto :goto_b

    nop

    :goto_18
    invoke-super {p0}, Landroid/widget/FrameLayout;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_12

    nop

    :goto_19
    iput-boolean v0, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarSupportBlur:Z

    goto :goto_d

    nop

    :goto_1a
    if-eqz v0, :cond_3

    goto :goto_23

    :cond_3
    goto :goto_1e

    nop

    :goto_1b
    invoke-direct {v1, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;-><init>(Landroid/os/Parcelable;)V

    goto :goto_e

    nop

    :goto_1c
    move v0, v2

    :goto_1d
    goto :goto_8

    nop

    :goto_1e
    move v2, v4

    goto :goto_22

    nop

    :goto_1f
    iput-boolean p0, v1, Lmiuix/appcompat/internal/app/widget/ActionBarContainer$SavedState;->actionBarApplyBlur:Z

    goto :goto_13

    nop

    :goto_20
    goto :goto_1d

    :goto_21
    goto :goto_14

    nop

    :goto_22
    goto :goto_11

    :goto_23
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__verifyDrawable',
        'method': '.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z',
        'method_name': 'verifyDrawable',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBackground:Landroid/graphics/drawable/Drawable;', 'if-ne p1, v0, :cond_0', 'iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsSplit:Z', 'if-eqz v0, :cond_3', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mStackedBackground:Landroid/graphics/drawable/Drawable;', 'if-ne p1, v0, :cond_1', 'iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsStacked:Z', 'if-nez v0, :cond_3'],
        'type': 'method_replace',
        'search': """.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z
    .registers 3

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBackground:Landroid/graphics/drawable/Drawable;

    if-ne p1, v0, :cond_0

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsSplit:Z

    if-eqz v0, :cond_3

    :cond_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mStackedBackground:Landroid/graphics/drawable/Drawable;

    if-ne p1, v0, :cond_1

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsStacked:Z

    if-nez v0, :cond_3

    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mSplitBackground:Landroid/graphics/drawable/Drawable;

    if-ne p1, v0, :cond_2

    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsSplit:Z

    if-nez v0, :cond_3

    :cond_2
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z

    move-result p0

    if-eqz p0, :cond_4

    :cond_3
    const/4 p0, 0x1

    return p0

    :cond_4
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected verifyDrawable(Landroid/graphics/drawable/Drawable;)Z
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_c

    nop

    :goto_1
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsSplit:Z

    goto :goto_10

    nop

    :goto_2
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsStacked:Z

    goto :goto_14

    nop

    :goto_3
    return p0

    :goto_4
    return p0

    :goto_5
    goto :goto_7

    nop

    :goto_6
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mIsSplit:Z

    goto :goto_a

    nop

    :goto_7
    const/4 p0, 0x0

    goto :goto_3

    nop

    :goto_8
    if-nez p0, :cond_0

    goto :goto_5

    :cond_0
    :goto_9
    goto :goto_f

    nop

    :goto_a
    if-eqz v0, :cond_1

    goto :goto_9

    :cond_1
    :goto_b
    goto :goto_12

    nop

    :goto_c
    if-eq p1, v0, :cond_2

    goto :goto_11

    :cond_2
    goto :goto_1

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mSplitBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_16

    nop

    :goto_e
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mStackedBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_13

    nop

    :goto_f
    const/4 p0, 0x1

    goto :goto_4

    nop

    :goto_10
    if-nez v0, :cond_3

    goto :goto_9

    :cond_3
    :goto_11
    goto :goto_e

    nop

    :goto_12
    invoke-super {p0, p1}, Landroid/widget/FrameLayout;->verifyDrawable(Landroid/graphics/drawable/Drawable;)Z

    move-result p0

    goto :goto_8

    nop

    :goto_13
    if-eq p1, v0, :cond_4

    goto :goto_15

    :cond_4
    goto :goto_2

    nop

    :goto_14
    if-eqz v0, :cond_5

    goto :goto_9

    :cond_5
    :goto_15
    goto :goto_d

    nop

    :goto_16
    if-eq p1, v0, :cond_6

    goto :goto_b

    :cond_6
    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__resetActionBarBlurConfigOnReshow',
        'method': '.method resetActionBarBlurConfigOnReshow()V',
        'method_name': 'resetActionBarBlurConfigOnReshow',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z', 'invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V', 'return-void', 'iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mInternalApplyBgBlur:Z', 'invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method resetActionBarBlurConfigOnReshow()V
    .registers 2

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V

    return-void

    :cond_0
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mInternalApplyBgBlur:Z

    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V

    return-void
.end method""",
        'replacement': """.method resetActionBarBlurConfigOnReshow()V
    .registers 2

    goto :goto_7

    nop

    :goto_0
    iget-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mInternalApplyBgBlur:Z

    goto :goto_5

    nop

    :goto_1
    return-void

    :goto_2
    goto :goto_0

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_8

    nop

    :goto_4
    return-void

    :goto_5
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V

    goto :goto_4

    nop

    :goto_6
    invoke-virtual {p0, v0}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V

    goto :goto_1

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    goto :goto_3

    nop

    :goto_8
    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__setActionBarBlurByNestedScrolled',
        'method': '.method setActionBarBlurByNestedScrolled(Z)V',
        'method_name': 'setActionBarBlurByNestedScrolled',
        'method_anchors': ['iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mInternalApplyBgBlur:Z', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;', 'if-eqz v0, :cond_0', 'return-void', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method setActionBarBlurByNestedScrolled(Z)V
    .registers 3

    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mInternalApplyBgBlur:Z

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    if-eqz v0, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V

    return-void
.end method""",
        'replacement': """.method setActionBarBlurByNestedScrolled(Z)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_4

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mUserApplyBgBlur:Ljava/lang/Boolean;

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    iput-boolean p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mInternalApplyBgBlur:Z

    goto :goto_1

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_6

    nop

    :goto_6
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->applyBlur(Z)V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__setActionBarCoordinateListener',
        'method': '.method setActionBarCoordinateListener(Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;)V',
        'method_name': 'setActionBarCoordinateListener',
        'method_anchors': ['iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mCoordinateListener:Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setActionBarCoordinateListener(Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;)V
    .registers 2

    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mCoordinateListener:Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;

    return-void
.end method""",
        'replacement': """.method setActionBarCoordinateListener(Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-object p1, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mCoordinateListener:Lmiuix/appcompat/internal/app/widget/ActionBarCoordinateListener;

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_app_widget_ActionBarContainer__updateBackgroundInternal',
        'method': '.method updateBackgroundInternal(Z)V',
        'method_name': 'updateBackgroundInternal',
        'method_anchors': ['if-eqz p1, :cond_0', 'iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mDrawBackground:Z', 'iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mDrawBackground:Z', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionBarContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;', 'if-eqz v0, :cond_1', 'invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->updateBackground(Z)V', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;', 'if-eqz v0, :cond_2'],
        'type': 'method_replace',
        'search': """.method updateBackgroundInternal(Z)V
    .registers 3

    if-eqz p1, :cond_0

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mDrawBackground:Z

    goto :goto_0

    :cond_0
    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mDrawBackground:Z

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionBarContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    if-eqz v0, :cond_1

    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->updateBackground(Z)V

    :cond_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    if-eqz v0, :cond_2

    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setApplyBgBlur(Z)V

    :cond_2
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->invalidate()V

    return-void
.end method""",
        'replacement': """.method updateBackgroundInternal(Z)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    if-nez p1, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_d

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarView;->setApplyBgBlur(Z)V

    :goto_3
    goto :goto_e

    nop

    :goto_4
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ActionBarContextView;->updateBackground(Z)V

    :goto_5
    goto :goto_8

    nop

    :goto_6
    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mDrawBackground:Z

    goto :goto_10

    nop

    :goto_7
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionBarContextView:Lmiuix/appcompat/internal/app/widget/ActionBarContextView;

    goto :goto_f

    nop

    :goto_8
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mActionBarView:Lmiuix/appcompat/internal/app/widget/ActionBarView;

    goto :goto_9

    nop

    :goto_9
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_2

    nop

    :goto_a
    iput-boolean v0, p0, Lmiuix/appcompat/internal/app/widget/ActionBarContainer;->mDrawBackground:Z

    :goto_b
    goto :goto_7

    nop

    :goto_c
    const/4 v0, 0x1

    goto :goto_a

    nop

    :goto_d
    const/4 v0, 0x0

    goto :goto_6

    nop

    :goto_e
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->invalidate()V

    goto :goto_1

    nop

    :goto_f
    if-nez v0, :cond_2

    goto :goto_5

    :cond_2
    goto :goto_4

    nop

    :goto_10
    goto :goto_b

    :goto_11
    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
