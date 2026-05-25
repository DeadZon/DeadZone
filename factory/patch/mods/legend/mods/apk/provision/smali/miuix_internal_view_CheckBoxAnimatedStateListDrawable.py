TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/view/CheckBoxAnimatedStateListDrawable.smali'
CLASS_FALLBACK_NAMES = ['CheckBoxAnimatedStateListDrawable.smali']
CLASS_ANCHORS = ['.super Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;']

PATCHES = [
    {
        'id': 'miuix_internal_view_CheckBoxAnimatedStateListDrawable__getCheckWidgetDrawableStyle',
        'method': '.method protected getCheckWidgetDrawableStyle()I',
        'method_name': 'getCheckWidgetDrawableStyle',
        'method_anchors': ['sget p0, Lmiuix/appcompat/R$style;->CheckWidgetDrawable_CheckBox:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected getCheckWidgetDrawableStyle()I
    .registers 1

    sget p0, Lmiuix/appcompat/R$style;->CheckWidgetDrawable_CheckBox:I

    return p0
.end method""",
        'replacement': """.method protected getCheckWidgetDrawableStyle()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    sget p0, Lmiuix/appcompat/R$style;->CheckWidgetDrawable_CheckBox:I

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
        'id': 'miuix_internal_view_CheckBoxAnimatedStateListDrawable__isSingleSelectionWidget',
        'method': '.method protected isSingleSelectionWidget()Z',
        'method_name': 'isSingleSelectionWidget',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected isSingleSelectionWidget()Z
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected isSingleSelectionWidget()Z
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x0

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
        'id': 'miuix_internal_view_CheckBoxAnimatedStateListDrawable__newCheckWidgetConstantState',
        'method': '.method protected newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;',
        'method_name': 'newCheckWidgetConstantState',
        'method_anchors': ['new-instance p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable$CheckBoxConstantState;', 'invoke-direct {p0}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable$CheckBoxConstantState;-><init>()V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;
    .registers 1

    new-instance p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable$CheckBoxConstantState;

    invoke-direct {p0}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable$CheckBoxConstantState;-><init>()V

    return-object p0
.end method""",
        'replacement': """.method protected newCheckWidgetConstantState()Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    new-instance p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable$CheckBoxConstantState;

    goto :goto_1

    nop

    :goto_1
    invoke-direct {p0}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable$CheckBoxConstantState;-><init>()V

    goto :goto_2

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_CheckBoxAnimatedStateListDrawable__onStateChange',
        'method': '.method protected onStateChange([I)Z',
        'method_name': 'onStateChange',
        'method_anchors': ['invoke-super {p0, p1}, Landroid/graphics/drawable/AnimatedStateListDrawable;->onStateChange([I)Z', 'iget-object v1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;', 'if-nez v1, :cond_0', 'return v0', 'invoke-virtual {p0}, Landroid/graphics/drawable/AnimatedStateListDrawable;->getCurrent()Landroid/graphics/drawable/Drawable;', 'if-eqz v1, :cond_1', 'if-eqz v1, :cond_1', 'invoke-super {p0, p1}, Landroid/graphics/drawable/AnimatedStateListDrawable;->onStateChange([I)Z'],
        'type': 'method_replace',
        'search': """.method protected onStateChange([I)Z
    .registers 10

    invoke-super {p0, p1}, Landroid/graphics/drawable/AnimatedStateListDrawable;->onStateChange([I)Z

    move-result v0

    iget-object v1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    if-nez v1, :cond_0

    return v0

    :cond_0
    invoke-virtual {p0}, Landroid/graphics/drawable/AnimatedStateListDrawable;->getCurrent()Landroid/graphics/drawable/Drawable;

    move-result-object v1

    if-eqz v1, :cond_1

    instance-of v1, v1, Landroid/graphics/drawable/BitmapDrawable;

    if-eqz v1, :cond_1

    invoke-super {p0, p1}, Landroid/graphics/drawable/AnimatedStateListDrawable;->onStateChange([I)Z

    move-result p0

    return p0

    :cond_1
    const/4 v1, 0x0

    iput-boolean v1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mIsEnabled:Z

    array-length v2, p1

    move v3, v1

    move v4, v3

    :goto_0
    if-ge v1, v2, :cond_5

    aget v5, p1, v1

    const v6, 0x10100a7

    const/4 v7, 0x1

    if-ne v5, v6, :cond_2

    move v3, v7

    goto :goto_1

    :cond_2
    const v6, 0x10100a0

    if-ne v5, v6, :cond_3

    move v4, v7

    goto :goto_1

    :cond_3
    const v6, 0x101009e

    if-ne v5, v6, :cond_4

    iput-boolean v7, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mIsEnabled:Z

    :cond_4
    :goto_1
    add-int/lit8 v1, v1, 0x1

    goto :goto_0

    :cond_5
    if-eqz v3, :cond_6

    invoke-virtual {p0, v4}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->startPressedAnim(Z)V

    :cond_6
    iget-boolean p1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mPrePressed:Z

    if-nez p1, :cond_7

    if-nez v3, :cond_7

    iget-boolean p1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mIsEnabled:Z

    invoke-virtual {p0, v4, p1}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->verifyChecked(ZZ)V

    :cond_7
    if-nez v3, :cond_9

    iget-boolean p1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mPrePressed:Z

    if-nez p1, :cond_8

    iget-boolean p1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mPreChecked:Z

    if-eq v4, p1, :cond_9

    :cond_8
    invoke-virtual {p0, v4}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->startUnPressedAnim(Z)V

    :cond_9
    iput-boolean v3, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mPrePressed:Z

    iput-boolean v4, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mPreChecked:Z

    return v0
.end method""",
        'replacement': """.method protected onStateChange([I)Z
    .registers 10

    goto :goto_23

    nop

    :goto_0
    return v0

    :goto_1
    goto :goto_c

    nop

    :goto_2
    if-eqz v3, :cond_0

    goto :goto_29

    :cond_0
    goto :goto_1e

    nop

    :goto_3
    if-eq v5, v6, :cond_1

    goto :goto_e

    :cond_1
    goto :goto_d

    nop

    :goto_4
    iget-boolean p1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mPreChecked:Z

    goto :goto_2a

    nop

    :goto_5
    const/4 v7, 0x1

    goto :goto_2f

    nop

    :goto_6
    if-eqz v1, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_0

    nop

    :goto_7
    if-eqz v3, :cond_3

    goto :goto_1c

    :cond_3
    goto :goto_30

    nop

    :goto_8
    invoke-super {p0, p1}, Landroid/graphics/drawable/AnimatedStateListDrawable;->onStateChange([I)Z

    move-result p0

    goto :goto_16

    nop

    :goto_9
    if-eq v5, v6, :cond_4

    goto :goto_b

    :cond_4
    goto :goto_2d

    nop

    :goto_a
    goto :goto_e

    :goto_b
    goto :goto_34

    nop

    :goto_c
    invoke-virtual {p0}, Landroid/graphics/drawable/AnimatedStateListDrawable;->getCurrent()Landroid/graphics/drawable/Drawable;

    move-result-object v1

    goto :goto_f

    nop

    :goto_d
    iput-boolean v7, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mIsEnabled:Z

    :goto_e
    goto :goto_38

    nop

    :goto_f
    if-nez v1, :cond_5

    goto :goto_17

    :cond_5
    goto :goto_1a

    nop

    :goto_10
    if-nez v1, :cond_6

    goto :goto_17

    :cond_6
    goto :goto_8

    nop

    :goto_11
    aget v5, p1, v1

    goto :goto_2c

    nop

    :goto_12
    goto :goto_e

    :goto_13
    goto :goto_22

    nop

    :goto_14
    goto :goto_19

    :goto_15
    goto :goto_33

    nop

    :goto_16
    return p0

    :goto_17
    goto :goto_31

    nop

    :goto_18
    move v4, v3

    :goto_19
    goto :goto_32

    nop

    :goto_1a
    instance-of v1, v1, Landroid/graphics/drawable/BitmapDrawable;

    goto :goto_10

    nop

    :goto_1b
    invoke-virtual {p0, v4}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->startUnPressedAnim(Z)V

    :goto_1c
    goto :goto_2e

    nop

    :goto_1d
    return v0

    :goto_1e
    iget-boolean p1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mIsEnabled:Z

    goto :goto_28

    nop

    :goto_1f
    move v3, v1

    goto :goto_18

    nop

    :goto_20
    iput-boolean v1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mIsEnabled:Z

    goto :goto_25

    nop

    :goto_21
    move v3, v7

    goto :goto_12

    nop

    :goto_22
    const v6, 0x10100a0

    goto :goto_9

    nop

    :goto_23
    invoke-super {p0, p1}, Landroid/graphics/drawable/AnimatedStateListDrawable;->onStateChange([I)Z

    move-result v0

    goto :goto_37

    nop

    :goto_24
    iget-boolean p1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mPrePressed:Z

    goto :goto_26

    nop

    :goto_25
    array-length v2, p1

    goto :goto_1f

    nop

    :goto_26
    if-eqz p1, :cond_7

    goto :goto_29

    :cond_7
    goto :goto_2

    nop

    :goto_27
    iput-boolean v4, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mPreChecked:Z

    goto :goto_1d

    nop

    :goto_28
    invoke-virtual {p0, v4, p1}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->verifyChecked(ZZ)V

    :goto_29
    goto :goto_7

    nop

    :goto_2a
    if-ne v4, p1, :cond_8

    goto :goto_1c

    :cond_8
    :goto_2b
    goto :goto_1b

    nop

    :goto_2c
    const v6, 0x10100a7

    goto :goto_5

    nop

    :goto_2d
    move v4, v7

    goto :goto_a

    nop

    :goto_2e
    iput-boolean v3, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mPrePressed:Z

    goto :goto_27

    nop

    :goto_2f
    if-eq v5, v6, :cond_9

    goto :goto_13

    :cond_9
    goto :goto_21

    nop

    :goto_30
    iget-boolean p1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mPrePressed:Z

    goto :goto_39

    nop

    :goto_31
    const/4 v1, 0x0

    goto :goto_20

    nop

    :goto_32
    if-lt v1, v2, :cond_a

    goto :goto_15

    :cond_a
    goto :goto_11

    nop

    :goto_33
    if-nez v3, :cond_b

    goto :goto_36

    :cond_b
    goto :goto_35

    nop

    :goto_34
    const v6, 0x101009e

    goto :goto_3

    nop

    :goto_35
    invoke-virtual {p0, v4}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->startPressedAnim(Z)V

    :goto_36
    goto :goto_24

    nop

    :goto_37
    iget-object v1, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    goto :goto_6

    nop

    :goto_38
    add-int/lit8 v1, v1, 0x1

    goto :goto_14

    nop

    :goto_39
    if-eqz p1, :cond_c

    goto :goto_2b

    :cond_c
    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_CheckBoxAnimatedStateListDrawable__setCheckWidgetDrawableBounds',
        'method': '.method protected setCheckWidgetDrawableBounds(IIII)V',
        'method_name': 'setCheckWidgetDrawableBounds',
        'method_anchors': ['iget-object p0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1, p2, p3, p4}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->setBounds(IIII)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setCheckWidgetDrawableBounds(IIII)V
    .registers 5

    iget-object p0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1, p2, p3, p4}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->setBounds(IIII)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected setCheckWidgetDrawableBounds(IIII)V
    .registers 5

    goto :goto_4

    nop

    :goto_0
    return-void

    :goto_1
    if-nez p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1, p2, p3, p4}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->setBounds(IIII)V

    :goto_3
    goto :goto_0

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_CheckBoxAnimatedStateListDrawable__setCheckWidgetDrawableBounds',
        'method': '.method protected setCheckWidgetDrawableBounds(Landroid/graphics/Rect;)V',
        'method_name': 'setCheckWidgetDrawableBounds',
        'method_anchors': ['iget-object p0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0, p1}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->setBounds(Landroid/graphics/Rect;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected setCheckWidgetDrawableBounds(Landroid/graphics/Rect;)V
    .registers 2

    iget-object p0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    if-eqz p0, :cond_0

    invoke-virtual {p0, p1}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->setBounds(Landroid/graphics/Rect;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected setCheckWidgetDrawableBounds(Landroid/graphics/Rect;)V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->setBounds(Landroid/graphics/Rect;)V

    :goto_2
    goto :goto_0

    nop

    :goto_3
    if-nez p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_4
    iget-object p0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_CheckBoxAnimatedStateListDrawable__startPressedAnim',
        'method': '.method protected startPressedAnim(Z)V',
        'method_name': 'startPressedAnim',
        'method_anchors': ['iget-object v0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;', 'if-eqz v0, :cond_0', 'iget-object p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;', 'iget-boolean p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;->touchAnimEnable:Z', 'invoke-virtual {v0, p1, p0}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->startPressedAnim(ZZ)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected startPressedAnim(Z)V
    .registers 3

    iget-object v0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    if-eqz v0, :cond_0

    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    iget-boolean p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;->touchAnimEnable:Z

    invoke-virtual {v0, p1, p0}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->startPressedAnim(ZZ)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected startPressedAnim(Z)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    goto :goto_5

    nop

    :goto_1
    invoke-virtual {v0, p1, p0}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->startPressedAnim(ZZ)V

    :goto_2
    goto :goto_4

    nop

    :goto_3
    iget-boolean p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;->touchAnimEnable:Z

    goto :goto_1

    nop

    :goto_4
    return-void

    :goto_5
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_6

    nop

    :goto_6
    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_CheckBoxAnimatedStateListDrawable__startUnPressedAnim',
        'method': '.method protected startUnPressedAnim(Z)V',
        'method_name': 'startUnPressedAnim',
        'method_anchors': ['iget-object v0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;', 'if-eqz v0, :cond_0', 'iget-object p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;', 'iget-boolean p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;->touchAnimEnable:Z', 'invoke-virtual {v0, p1, p0}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->startUnPressedAnim(ZZ)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected startUnPressedAnim(Z)V
    .registers 3

    iget-object v0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    if-eqz v0, :cond_0

    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    iget-boolean p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;->touchAnimEnable:Z

    invoke-virtual {v0, p1, p0}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->startUnPressedAnim(ZZ)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected startUnPressedAnim(Z)V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_2

    nop

    :goto_1
    iget-boolean p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;->touchAnimEnable:Z

    goto :goto_4

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable;->mCheckWidgetConstantState:Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;

    goto :goto_1

    nop

    :goto_3
    iget-object v0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    goto :goto_0

    nop

    :goto_4
    invoke-virtual {v0, p1, p0}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->startUnPressedAnim(ZZ)V

    :goto_5
    goto :goto_6

    nop

    :goto_6
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_view_CheckBoxAnimatedStateListDrawable__verifyChecked',
        'method': '.method protected verifyChecked(ZZ)V',
        'method_name': 'verifyChecked',
        'method_anchors': ['iget-object v0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0, p1, p2}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->verifyChecked(ZZ)V', 'invoke-virtual {p0}, Landroid/graphics/drawable/AnimatedStateListDrawable;->invalidateSelf()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected verifyChecked(ZZ)V
    .registers 4

    iget-object v0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    if-eqz v0, :cond_0

    invoke-virtual {v0, p1, p2}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->verifyChecked(ZZ)V

    invoke-virtual {p0}, Landroid/graphics/drawable/AnimatedStateListDrawable;->invalidateSelf()V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected verifyChecked(ZZ)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iget-object v0, p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;->mCheckWidgetDrawableAnims:Lmiuix/internal/view/CheckWidgetDrawableAnims;

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/graphics/drawable/AnimatedStateListDrawable;->invalidateSelf()V

    :goto_3
    goto :goto_0

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_5

    nop

    :goto_5
    invoke-virtual {v0, p1, p2}, Lmiuix/internal/view/CheckWidgetDrawableAnims;->verifyChecked(ZZ)V

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
