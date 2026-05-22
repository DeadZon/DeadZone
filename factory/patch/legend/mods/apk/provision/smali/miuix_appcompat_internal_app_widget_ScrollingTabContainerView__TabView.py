TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView.smali'
CLASS_FALLBACK_NAMES = ['ScrollingTabContainerView$TabView.smali']
CLASS_ANCHORS = ['.super Landroid/widget/LinearLayout;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_app_widget_ScrollingTabContainerView__TabView__onConfigurationChanged',
        'method': '.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mTextView:Landroid/widget/TextView;', 'if-eqz p1, :cond_0', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mParent:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;', 'invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->getTabTextStyleId(Landroid/widget/TextView;)I', 'iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mTextView:Landroid/widget/TextView;', 'invoke-virtual {v0, p1}, Landroid/widget/TextView;->setTextAppearance(I)V', 'iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mIconView:Landroid/widget/ImageView;'],
        'type': 'method_replace',
        'search': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mTextView:Landroid/widget/TextView;

    if-eqz p1, :cond_0

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mParent:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->getTabTextStyleId(Landroid/widget/TextView;)I

    move-result p1

    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mTextView:Landroid/widget/TextView;

    invoke-virtual {v0, p1}, Landroid/widget/TextView;->setTextAppearance(I)V

    :cond_0
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mIconView:Landroid/widget/ImageView;

    if-eqz p1, :cond_1

    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mTab:Landroidx/appcompat/app/ActionBar$Tab;

    invoke-virtual {p0}, Landroidx/appcompat/app/ActionBar$Tab;->getIcon()Landroid/graphics/drawable/Drawable;

    move-result-object p0

    invoke-virtual {p1, p0}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 3

    goto :goto_c

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mParent:Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;

    goto :goto_3

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mTextView:Landroid/widget/TextView;

    goto :goto_7

    nop

    :goto_2
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mTextView:Landroid/widget/TextView;

    goto :goto_a

    nop

    :goto_3
    invoke-virtual {v0, p1}, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView;->getTabTextStyleId(Landroid/widget/TextView;)I

    move-result p1

    goto :goto_1

    nop

    :goto_4
    if-nez p1, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_e

    nop

    :goto_5
    invoke-virtual {p1, p0}, Landroid/widget/ImageView;->setImageDrawable(Landroid/graphics/drawable/Drawable;)V

    :goto_6
    goto :goto_d

    nop

    :goto_7
    invoke-virtual {v0, p1}, Landroid/widget/TextView;->setTextAppearance(I)V

    :goto_8
    goto :goto_9

    nop

    :goto_9
    iget-object p1, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mIconView:Landroid/widget/ImageView;

    goto :goto_4

    nop

    :goto_a
    if-nez p1, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_0

    nop

    :goto_b
    invoke-virtual {p0}, Landroidx/appcompat/app/ActionBar$Tab;->getIcon()Landroid/graphics/drawable/Drawable;

    move-result-object p0

    goto :goto_5

    nop

    :goto_c
    invoke-super {p0, p1}, Landroid/widget/LinearLayout;->onConfigurationChanged(Landroid/content/res/Configuration;)V

    goto :goto_2

    nop

    :goto_d
    return-void

    :goto_e
    iget-object p0, p0, Lmiuix/appcompat/internal/app/widget/ScrollingTabContainerView$TabView;->mTab:Landroidx/appcompat/app/ActionBar$Tab;

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
