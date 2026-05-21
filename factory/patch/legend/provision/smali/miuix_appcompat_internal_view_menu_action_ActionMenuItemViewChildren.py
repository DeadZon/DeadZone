TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren.smali'
CLASS_FALLBACK_NAMES = ['ActionMenuItemViewChildren.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_appcompat_internal_view_menu_action_ActionMenuItemViewChildren__onConfigurationChanged',
        'method': '.method onConfigurationChanged(Landroid/content/res/Configuration;)V',
        'method_name': 'onConfigurationChanged',
        'method_anchors': ['iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I', 'iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mDensityDpi:I', 'if-eq p1, v0, :cond_0', 'iput p1, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mDensityDpi:I', 'iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mImageView:Landroid/widget/ImageView;', 'invoke-virtual {p1}, Landroid/widget/ImageView;->getContext()Landroid/content/Context;', 'invoke-static {p1, v0}, Lmiuix/core/util/MiuixUIUtils;->dp2px(Landroid/content/Context;F)I', 'iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mImageView:Landroid/widget/ImageView;'],
        'type': 'method_replace',
        'search': """.method onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 4

    iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I

    iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mDensityDpi:I

    if-eq p1, v0, :cond_0

    iput p1, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mDensityDpi:I

    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mImageView:Landroid/widget/ImageView;

    invoke-virtual {p1}, Landroid/widget/ImageView;->getContext()Landroid/content/Context;

    move-result-object p1

    const/high16 v0, 0x41e00000

    invoke-static {p1, v0}, Lmiuix/core/util/MiuixUIUtils;->dp2px(Landroid/content/Context;F)I

    move-result p1

    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mImageView:Landroid/widget/ImageView;

    new-instance v1, Landroid/widget/LinearLayout$LayoutParams;

    invoke-direct {v1, p1, p1}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    iget-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mLargerFontEnabled:Z

    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->setLargeFontEnabled(Z)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method onConfigurationChanged(Landroid/content/res/Configuration;)V
    .registers 4

    goto :goto_b

    nop

    :goto_0
    iput p1, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mDensityDpi:I

    goto :goto_e

    nop

    :goto_1
    invoke-static {p1, v0}, Lmiuix/core/util/MiuixUIUtils;->dp2px(Landroid/content/Context;F)I

    move-result p1

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {v0, v1}, Landroid/widget/ImageView;->setLayoutParams(Landroid/view/ViewGroup$LayoutParams;)V

    goto :goto_9

    nop

    :goto_3
    invoke-direct {v1, p1, p1}, Landroid/widget/LinearLayout$LayoutParams;-><init>(II)V

    goto :goto_2

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mImageView:Landroid/widget/ImageView;

    goto :goto_7

    nop

    :goto_5
    invoke-virtual {p0, p1}, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->setLargeFontEnabled(Z)V

    :goto_6
    goto :goto_a

    nop

    :goto_7
    new-instance v1, Landroid/widget/LinearLayout$LayoutParams;

    goto :goto_3

    nop

    :goto_8
    const/high16 v0, 0x41e00000

    goto :goto_1

    nop

    :goto_9
    iget-boolean p1, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mLargerFontEnabled:Z

    goto :goto_5

    nop

    :goto_a
    return-void

    :goto_b
    iget p1, p1, Landroid/content/res/Configuration;->densityDpi:I

    goto :goto_f

    nop

    :goto_c
    if-ne p1, v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_0

    nop

    :goto_d
    invoke-virtual {p1}, Landroid/widget/ImageView;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_8

    nop

    :goto_e
    iget-object p1, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mImageView:Landroid/widget/ImageView;

    goto :goto_d

    nop

    :goto_f
    iget v0, p0, Lmiuix/appcompat/internal/view/menu/action/ActionMenuItemViewChildren;->mDensityDpi:I

    goto :goto_c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
