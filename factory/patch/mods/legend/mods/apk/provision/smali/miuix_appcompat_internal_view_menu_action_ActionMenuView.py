TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/action/ActionMenuView.smali'
CLASS_FALLBACK_NAMES = ['ActionMenuView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;', '.implements Lmiuix/appcompat/internal/view/menu/MenuBuilder$ItemInvoker;', '.implements Lmiuix/appcompat/internal/view/menu/MenuView;', '.implements Lmiuix/view/BlurableWidget;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__generateDefaultLayoutParams',
        'method': '.method protected bridge synthetic generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;',
        'method_name': 'generateDefaultLayoutParams',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;
    .registers 1

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic generateDefaultLayoutParams()Landroid/view/ViewGroup$LayoutParams;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__generateDefaultLayoutParams',
        'method': '.method protected bridge synthetic generateDefaultLayoutParams()Landroid/widget/LinearLayout$LayoutParams;',
        'method_name': 'generateDefaultLayoutParams',
        'method_anchors': ['invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic generateDefaultLayoutParams()Landroid/widget/LinearLayout$LayoutParams;
    .registers 1

    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic generateDefaultLayoutParams()Landroid/widget/LinearLayout$LayoutParams;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    move-result-object p0

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
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__generateLayoutParams',
        'method': '.method protected bridge synthetic generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;',
        'method_name': 'generateLayoutParams',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;
    .registers 2

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/view/ViewGroup$LayoutParams;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    move-result-object p0

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
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__generateLayoutParams',
        'method': '.method protected bridge synthetic generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/widget/LinearLayout$LayoutParams;',
        'method_name': 'generateLayoutParams',
        'method_anchors': ['invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/widget/LinearLayout$LayoutParams;
    .registers 2

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Landroid/widget/LinearLayout$LayoutParams;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    move-result-object p0

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
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__checkLayoutParams',
        'method': '.method protected checkLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Z',
        'method_name': 'checkLayoutParams',
        'method_anchors': ['if-eqz p1, :cond_0', 'if-eqz p0, :cond_0', 'return p0', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected checkLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Z
    .registers 2

    if-eqz p1, :cond_0

    instance-of p0, p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    if-eqz p0, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected checkLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Z
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return p0

    :goto_1
    goto :goto_5

    nop

    :goto_2
    if-nez p1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_3

    nop

    :goto_3
    instance-of p0, p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    goto :goto_7

    nop

    :goto_4
    return p0

    :goto_5
    const/4 p0, 0x0

    goto :goto_4

    nop

    :goto_6
    const/4 p0, 0x1

    goto :goto_0

    nop

    :goto_7
    if-nez p0, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__clearBackground',
        'method': '.method protected clearBackground()V',
        'method_name': 'clearBackground',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected clearBackground()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected clearBackground()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__generateDefaultLayoutParams',
        'method': '.method protected generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;',
        'method_name': 'generateDefaultLayoutParams',
        'method_anchors': ['new-instance p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;', 'invoke-direct {p0, v0, v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;-><init>(II)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;
    .registers 2

    new-instance p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    const/4 v0, -0x2

    invoke-direct {p0, v0, v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;-><init>(II)V

    return-object p0
.end method""",
        'replacement': """.method protected generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    new-instance p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    goto :goto_3

    nop

    :goto_2
    invoke-direct {p0, v0, v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;-><init>(II)V

    goto :goto_0

    nop

    :goto_3
    const/4 v0, -0x2

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__generateLayoutParams',
        'method': '.method protected generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;',
        'method_name': 'generateLayoutParams',
        'method_anchors': ['if-eqz v0, :cond_0', 'new-instance p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;', 'check-cast p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;', 'invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;)V', 'return-object p0', 'invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;
    .registers 3

    instance-of v0, p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    if-eqz v0, :cond_0

    new-instance p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    check-cast p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;)V

    return-object p0

    :cond_0
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected generateLayoutParams(Landroid/view/ViewGroup$LayoutParams;)Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;
    .registers 3

    goto :goto_4

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_1

    nop

    :goto_1
    new-instance p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    goto :goto_5

    nop

    :goto_2
    return-object p0

    :goto_3
    invoke-direct {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;-><init>(Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;)V

    goto :goto_7

    nop

    :goto_4
    instance-of v0, p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    goto :goto_0

    nop

    :goto_5
    check-cast p1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    goto :goto_3

    nop

    :goto_6
    invoke-virtual {p0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView;->generateDefaultLayoutParams()Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$LayoutParams;

    move-result-object p0

    goto :goto_2

    nop

    :goto_7
    return-object p0

    :goto_8
    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__hasDividerBeforeChildAt',
        'method': '.method protected hasDividerBeforeChildAt(I)Z',
        'method_name': 'hasDividerBeforeChildAt',
        'method_anchors': ['invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;', 'invoke-virtual {p0, p1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I', 'if-ge p1, p0, :cond_0', 'if-eqz p0, :cond_0', 'check-cast v0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;', 'invoke-interface {v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;->needsDividerAfter()Z', 'if-lez p1, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected hasDividerBeforeChildAt(I)Z
    .registers 4

    add-int/lit8 v0, p1, -0x1

    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    invoke-virtual {p0, p1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result p0

    if-ge p1, p0, :cond_0

    instance-of p0, v0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;

    if-eqz p0, :cond_0

    check-cast v0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;

    invoke-interface {v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;->needsDividerAfter()Z

    move-result p0

    goto :goto_0

    :cond_0
    const/4 p0, 0x0

    :goto_0
    if-lez p1, :cond_1

    instance-of p1, v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;

    if-eqz p1, :cond_1

    check-cast v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;

    invoke-interface {v1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;->needsDividerBefore()Z

    move-result p1

    or-int/2addr p0, p1

    :cond_1
    return p0
.end method""",
        'replacement': """.method protected hasDividerBeforeChildAt(I)Z
    .registers 4

    goto :goto_2

    nop

    :goto_0
    goto :goto_d

    :goto_1
    goto :goto_c

    nop

    :goto_2
    add-int/lit8 v0, p1, -0x1

    goto :goto_e

    nop

    :goto_3
    if-nez p1, :cond_0

    goto :goto_12

    :cond_0
    goto :goto_13

    nop

    :goto_4
    if-gtz p1, :cond_1

    goto :goto_12

    :cond_1
    goto :goto_f

    nop

    :goto_5
    if-nez p0, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_b

    nop

    :goto_6
    instance-of p0, v0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;

    goto :goto_5

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result p0

    goto :goto_a

    nop

    :goto_8
    invoke-interface {v0}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;->needsDividerAfter()Z

    move-result p0

    goto :goto_0

    nop

    :goto_9
    return p0

    :goto_a
    if-lt p1, p0, :cond_3

    goto :goto_1

    :cond_3
    goto :goto_6

    nop

    :goto_b
    check-cast v0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;

    goto :goto_8

    nop

    :goto_c
    const/4 p0, 0x0

    :goto_d
    goto :goto_4

    nop

    :goto_e
    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto :goto_10

    nop

    :goto_f
    instance-of p1, v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;

    goto :goto_3

    nop

    :goto_10
    invoke-virtual {p0, p1}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v1

    goto :goto_7

    nop

    :goto_11
    or-int/2addr p0, p1

    :goto_12
    goto :goto_9

    nop

    :goto_13
    check-cast v1, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;

    goto :goto_14

    nop

    :goto_14
    invoke-interface {v1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuView$ActionMenuChildView;->needsDividerBefore()Z

    move-result p1

    goto :goto_11

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I', 'if-nez v0, :cond_0', 'invoke-virtual {p0, p1, p1}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V', 'return-void', 'invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 4

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v0

    if-nez v0, :cond_0

    const/4 p1, 0x0

    invoke-virtual {p0, p1, p1}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    return-void

    :cond_0
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 4

    goto :goto_5

    nop

    :goto_0
    const/4 p1, 0x0

    goto :goto_2

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, p1, p1}, Landroid/widget/LinearLayout;->setMeasuredDimension(II)V

    goto :goto_3

    nop

    :goto_3
    return-void

    :goto_4
    goto :goto_7

    nop

    :goto_5
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getChildCount()I

    move-result v0

    goto :goto_6

    nop

    :goto_6
    if-eqz v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_0

    nop

    :goto_7
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuView__resetBackground',
        'method': '.method protected resetBackground()V',
        'method_name': 'resetBackground',
        'method_anchors': ['return-void'],
        'type': 'method_replace',
        'search': """.method protected resetBackground()V
    .registers 1

    return-void
.end method""",
        'replacement': """.method protected resetBackground()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
