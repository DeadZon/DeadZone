TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/ListMenuItemView.smali'
CLASS_FALLBACK_NAMES = ['ListMenuItemView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;', '.implements Lmiuix/appcompat/internal/view/menu/MenuView$ItemView;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_ListMenuItemView__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/LinearLayout;->onFinishInflate()V', 'iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mBackground:Landroid/graphics/drawable/Drawable;', 'invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V', 'sget v0, Lmiuix/appcompat/R$id;->title:I', 'invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;', 'check-cast v0, Landroid/widget/TextView;', 'iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mTitleView:Landroid/widget/TextView;', 'iget v1, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mTextAppearance:I'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 4

    invoke-super {p0}, Landroid/widget/LinearLayout;->onFinishInflate()V

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mBackground:Landroid/graphics/drawable/Drawable;

    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V

    sget v0, Lmiuix/appcompat/R$id;->title:I

    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mTitleView:Landroid/widget/TextView;

    iget v1, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mTextAppearance:I

    const/4 v2, -0x1

    if-eq v1, v2, :cond_0

    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mTextAppearanceContext:Landroid/content/Context;

    invoke-virtual {v0, v2, v1}, Landroid/widget/TextView;->setTextAppearance(Landroid/content/Context;I)V

    :cond_0
    sget v0, Lmiuix/appcompat/R$id;->shortcut:I

    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    check-cast v0, Landroid/widget/TextView;

    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mShortcutView:Landroid/widget/TextView;

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mRelativeLayout:Landroid/view/View;

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    if-ne v1, v2, :cond_0

    goto :goto_10

    :cond_0
    goto :goto_12

    nop

    :goto_1
    invoke-super {p0}, Landroid/widget/LinearLayout;->onFinishInflate()V

    goto :goto_9

    nop

    :goto_2
    check-cast v0, Landroid/widget/TextView;

    goto :goto_8

    nop

    :goto_3
    iget v1, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mTextAppearance:I

    goto :goto_4

    nop

    :goto_4
    const/4 v2, -0x1

    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_7

    nop

    :goto_6
    sget v0, Lmiuix/appcompat/R$id;->shortcut:I

    goto :goto_5

    nop

    :goto_7
    check-cast v0, Landroid/widget/TextView;

    goto :goto_a

    nop

    :goto_8
    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mTitleView:Landroid/widget/TextView;

    goto :goto_3

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mBackground:Landroid/graphics/drawable/Drawable;

    goto :goto_14

    nop

    :goto_a
    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mShortcutView:Landroid/widget/TextView;

    goto :goto_e

    nop

    :goto_b
    return-void

    :goto_c
    iput-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mRelativeLayout:Landroid/view/View;

    goto :goto_b

    nop

    :goto_d
    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->getChildAt(I)Landroid/view/View;

    move-result-object v0

    goto :goto_c

    nop

    :goto_e
    const/4 v0, 0x0

    goto :goto_d

    nop

    :goto_f
    invoke-virtual {v0, v2, v1}, Landroid/widget/TextView;->setTextAppearance(Landroid/content/Context;I)V

    :goto_10
    goto :goto_6

    nop

    :goto_11
    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->findViewById(I)Landroid/view/View;

    move-result-object v0

    goto :goto_2

    nop

    :goto_12
    iget-object v2, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mTextAppearanceContext:Landroid/content/Context;

    goto :goto_f

    nop

    :goto_13
    sget v0, Lmiuix/appcompat/R$id;->title:I

    goto :goto_11

    nop

    :goto_14
    invoke-virtual {p0, v0}, Landroid/widget/LinearLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V

    goto :goto_13

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_internal_view_menu_ListMenuItemView__onMeasure',
        'method': '.method protected onMeasure(II)V',
        'method_name': 'onMeasure',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mIconView:Landroidx/appcompat/widget/AppCompatImageView;', 'if-eqz v0, :cond_0', 'iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mPreserveIconSpacing:Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Landroid/widget/LinearLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mIconView:Landroidx/appcompat/widget/AppCompatImageView;', 'invoke-virtual {v1}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;', 'check-cast v1, Landroid/widget/LinearLayout$LayoutParams;'],
        'type': 'method_replace',
        'search': """.method protected onMeasure(II)V
    .registers 6

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mIconView:Landroidx/appcompat/widget/AppCompatImageView;

    if-eqz v0, :cond_0

    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mPreserveIconSpacing:Z

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mIconView:Landroidx/appcompat/widget/AppCompatImageView;

    invoke-virtual {v1}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    check-cast v1, Landroid/widget/LinearLayout$LayoutParams;

    iget v0, v0, Landroid/view/ViewGroup$LayoutParams;->height:I

    if-lez v0, :cond_0

    iget v2, v1, Landroid/widget/LinearLayout$LayoutParams;->width:I

    if-gtz v2, :cond_0

    iput v0, v1, Landroid/widget/LinearLayout$LayoutParams;->width:I

    :cond_0
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    return-void
.end method""",
        'replacement': """.method protected onMeasure(II)V
    .registers 6

    goto :goto_d

    nop

    :goto_0
    invoke-virtual {v1}, Landroid/widget/ImageView;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v1

    goto :goto_9

    nop

    :goto_1
    invoke-super {p0, p1, p2}, Landroid/widget/LinearLayout;->onMeasure(II)V

    goto :goto_7

    nop

    :goto_2
    iput v0, v1, Landroid/widget/LinearLayout$LayoutParams;->width:I

    :goto_3
    goto :goto_1

    nop

    :goto_4
    if-lez v2, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_2

    nop

    :goto_5
    iget-object v1, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mIconView:Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_0

    nop

    :goto_6
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_c

    nop

    :goto_7
    return-void

    :goto_8
    invoke-virtual {p0}, Landroid/widget/LinearLayout;->getLayoutParams()Landroid/view/ViewGroup$LayoutParams;

    move-result-object v0

    goto :goto_5

    nop

    :goto_9
    check-cast v1, Landroid/widget/LinearLayout$LayoutParams;

    goto :goto_a

    nop

    :goto_a
    iget v0, v0, Landroid/view/ViewGroup$LayoutParams;->height:I

    goto :goto_b

    nop

    :goto_b
    if-gtz v0, :cond_2

    goto :goto_3

    :cond_2
    goto :goto_e

    nop

    :goto_c
    iget-boolean v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mPreserveIconSpacing:Z

    goto :goto_f

    nop

    :goto_d
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/ListMenuItemView;->mIconView:Landroidx/appcompat/widget/AppCompatImageView;

    goto :goto_6

    nop

    :goto_e
    iget v2, v1, Landroid/widget/LinearLayout$LayoutParams;->width:I

    goto :goto_4

    nop

    :goto_f
    if-nez v0, :cond_3

    goto :goto_3

    :cond_3
    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
