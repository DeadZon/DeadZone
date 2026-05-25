TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/view/RadioButtonAnimatedStateListDrawable.smali'
CLASS_FALLBACK_NAMES = ['RadioButtonAnimatedStateListDrawable.smali']
CLASS_ANCHORS = ['.super Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;']

PATCHES = [
    {
        'id': 'miuix_internal_view_RadioButtonAnimatedStateListDrawable__getCheckWidgetDrawableStyle',
        'method': '.method protected getCheckWidgetDrawableStyle()I',
        'method_name': 'getCheckWidgetDrawableStyle',
        'method_anchors': ['sget p0, Lmiuix/appcompat/R$style;->CheckWidgetDrawable_RadioButton:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getCheckWidgetDrawableStyle()I
    .registers 1

    sget p0, Lmiuix/appcompat/R$style;->CheckWidgetDrawable_RadioButton:I

    return p0
.end method""",
        'replacement': """.method protected getCheckWidgetDrawableStyle()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lmiuix/appcompat/R$style;->CheckWidgetDrawable_RadioButton:I

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_RadioButtonAnimatedStateListDrawable__isSingleSelectionWidget',
        'method': '.method protected isSingleSelectionWidget()Z',
        'method_name': 'isSingleSelectionWidget',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected isSingleSelectionWidget()Z
    .registers 1

    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected isSingleSelectionWidget()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/4 p0, 0x1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_RadioButtonAnimatedStateListDrawable__newCheckWidgetConstantState',
        'method': '.method protected newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;',
        'method_name': 'newCheckWidgetConstantState',
        'method_anchors': ['new-instance p0, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable$RadioButtonConstantState;', 'invoke-direct {p0}, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable$RadioButtonConstantState;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;
    .registers 1

    new-instance p0, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable$RadioButtonConstantState;

    invoke-direct {p0}, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable$RadioButtonConstantState;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;
    .registers 1

    goto :goto_1

    nop

    :goto_0
    invoke-direct {p0}, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable$RadioButtonConstantState;-><init>()V

    goto :goto_2

    nop

    :goto_1
    new-instance p0, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable$RadioButtonConstantState;

    goto :goto_0

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_RadioButtonAnimatedStateListDrawable__setCheckWidgetDrawableBounds',
        'method': '.method protected setCheckWidgetDrawableBounds(IIII)V',
        'method_name': 'setCheckWidgetDrawableBounds',
        'method_anchors': ['iget v0, p0, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable;->mDrawPadding:I', 'invoke-super {p0, p1, p2, p3, p4}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->setCheckWidgetDrawableBounds(IIII)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setCheckWidgetDrawableBounds(IIII)V
    .registers 6

    iget v0, p0, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable;->mDrawPadding:I

    add-int/2addr p1, v0

    add-int/2addr p2, v0

    sub-int/2addr p3, v0

    sub-int/2addr p4, v0

    invoke-super {p0, p1, p2, p3, p4}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->setCheckWidgetDrawableBounds(IIII)V

    return-void
.end method""",
        'replacement': """.method protected setCheckWidgetDrawableBounds(IIII)V
    .registers 6

    goto :goto_2

    nop

    :goto_0
    sub-int/2addr p3, v0

    goto :goto_5

    nop

    :goto_1
    add-int/2addr p1, v0

    goto :goto_3

    nop

    :goto_2
    iget v0, p0, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable;->mDrawPadding:I

    goto :goto_1

    nop

    :goto_3
    add-int/2addr p2, v0

    goto :goto_0

    nop

    :goto_4
    return-void

    :goto_5
    sub-int/2addr p4, v0

    goto :goto_6

    nop

    :goto_6
    invoke-super {p0, p1, p2, p3, p4}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->setCheckWidgetDrawableBounds(IIII)V

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_RadioButtonAnimatedStateListDrawable__setCheckWidgetDrawableBounds',
        'method': '.method protected setCheckWidgetDrawableBounds(Landroid/graphics/Rect;)V',
        'method_name': 'setCheckWidgetDrawableBounds',
        'method_anchors': ['iget v0, p0, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable;->mDrawPadding:I', 'invoke-virtual {p1, v0, v0}, Landroid/graphics/Rect;->inset(II)V', 'invoke-super {p0, p1}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->setCheckWidgetDrawableBounds(Landroid/graphics/Rect;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setCheckWidgetDrawableBounds(Landroid/graphics/Rect;)V
    .registers 3

    iget v0, p0, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable;->mDrawPadding:I

    invoke-virtual {p1, v0, v0}, Landroid/graphics/Rect;->inset(II)V

    invoke-super {p0, p1}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->setCheckWidgetDrawableBounds(Landroid/graphics/Rect;)V

    return-void
.end method""",
        'replacement': """.method protected setCheckWidgetDrawableBounds(Landroid/graphics/Rect;)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p1, v0, v0}, Landroid/graphics/Rect;->inset(II)V

    goto :goto_2

    nop

    :goto_2
    invoke-super {p0, p1}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->setCheckWidgetDrawableBounds(Landroid/graphics/Rect;)V

    goto :goto_0

    nop

    :goto_3
    iget v0, p0, Lmiuix/internal/view/RadioButtonAnimatedStateListDrawable;->mDrawPadding:I

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
