TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/miui/support/drawable/CardStateDrawable.smali'
CLASS_FALLBACK_NAMES = ['CardStateDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/Drawable;', '.implements Lmiuix/animation/styles/AlphaBlendingStateEffect$AlphaObserver;', '.field private static final USE_FOLME:Z']

PATCHES = [
    {
        'id': 'com_miui_support_drawable_CardStateDrawable__initState',
        'method': '.method protected initState()V',
        'method_name': 'initState',
        'method_anchors': ['invoke-direct {p0}, Lcom/miui/support/drawable/CardStateDrawable;->updateLocalState()V', 'invoke-direct {p0}, Lcom/miui/support/drawable/CardStateDrawable;->init()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected initState()V
    .registers 1

    invoke-direct {p0}, Lcom/miui/support/drawable/CardStateDrawable;->updateLocalState()V

    invoke-direct {p0}, Lcom/miui/support/drawable/CardStateDrawable;->init()V

    return-void
.end method""",
        'replacement': """.method protected initState()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-direct {p0}, Lcom/miui/support/drawable/CardStateDrawable;->updateLocalState()V

    goto :goto_1

    nop

    :goto_1
    invoke-direct {p0}, Lcom/miui/support/drawable/CardStateDrawable;->init()V

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_miui_support_drawable_CardStateDrawable__onBoundsChange',
        'method': '.method protected onBoundsChange(Landroid/graphics/Rect;)V',
        'method_name': 'onBoundsChange',
        'method_anchors': ['iget-object v0, p0, Lcom/miui/support/drawable/CardStateDrawable;->mRect:Landroid/graphics/RectF;', 'invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V', 'iget-object p1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mRect:Landroid/graphics/RectF;', 'iget v0, p1, Landroid/graphics/RectF;->left:F', 'iget v1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mInsetL:I', 'iput v0, p1, Landroid/graphics/RectF;->left:F', 'iget v0, p1, Landroid/graphics/RectF;->top:F', 'iget v1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mInsetT:I'],
        'type': 'method_replace',
        'search': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 4

    iget-object v0, p0, Lcom/miui/support/drawable/CardStateDrawable;->mRect:Landroid/graphics/RectF;

    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    iget-object p1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mRect:Landroid/graphics/RectF;

    iget v0, p1, Landroid/graphics/RectF;->left:F

    iget v1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mInsetL:I

    int-to-float v1, v1

    add-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->left:F

    iget v0, p1, Landroid/graphics/RectF;->top:F

    iget v1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mInsetT:I

    int-to-float v1, v1

    add-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->top:F

    iget v0, p1, Landroid/graphics/RectF;->right:F

    iget v1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mInsetR:I

    int-to-float v1, v1

    sub-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->right:F

    iget v0, p1, Landroid/graphics/RectF;->bottom:F

    iget p0, p0, Lcom/miui/support/drawable/CardStateDrawable;->mInsetB:I

    int-to-float p0, p0

    sub-float/2addr v0, p0

    iput v0, p1, Landroid/graphics/RectF;->bottom:F

    return-void
.end method""",
        'replacement': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 4

    goto :goto_3

    nop

    :goto_0
    iget v1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mInsetT:I

    goto :goto_8

    nop

    :goto_1
    int-to-float v1, v1

    goto :goto_17

    nop

    :goto_2
    iget v1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mInsetL:I

    goto :goto_1

    nop

    :goto_3
    iget-object v0, p0, Lcom/miui/support/drawable/CardStateDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_10

    nop

    :goto_4
    iget v0, p1, Landroid/graphics/RectF;->right:F

    goto :goto_b

    nop

    :goto_5
    iget v0, p1, Landroid/graphics/RectF;->top:F

    goto :goto_0

    nop

    :goto_6
    sub-float/2addr v0, p0

    goto :goto_16

    nop

    :goto_7
    iput v0, p1, Landroid/graphics/RectF;->right:F

    goto :goto_e

    nop

    :goto_8
    int-to-float v1, v1

    goto :goto_d

    nop

    :goto_9
    int-to-float v1, v1

    goto :goto_c

    nop

    :goto_a
    iput v0, p1, Landroid/graphics/RectF;->top:F

    goto :goto_4

    nop

    :goto_b
    iget v1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mInsetR:I

    goto :goto_9

    nop

    :goto_c
    sub-float/2addr v0, v1

    goto :goto_7

    nop

    :goto_d
    add-float/2addr v0, v1

    goto :goto_a

    nop

    :goto_e
    iget v0, p1, Landroid/graphics/RectF;->bottom:F

    goto :goto_15

    nop

    :goto_f
    return-void

    :goto_10
    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    goto :goto_12

    nop

    :goto_11
    iput v0, p1, Landroid/graphics/RectF;->left:F

    goto :goto_5

    nop

    :goto_12
    iget-object p1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_14

    nop

    :goto_13
    int-to-float p0, p0

    goto :goto_6

    nop

    :goto_14
    iget v0, p1, Landroid/graphics/RectF;->left:F

    goto :goto_2

    nop

    :goto_15
    iget p0, p0, Lcom/miui/support/drawable/CardStateDrawable;->mInsetB:I

    goto :goto_13

    nop

    :goto_16
    iput v0, p1, Landroid/graphics/RectF;->bottom:F

    goto :goto_f

    nop

    :goto_17
    add-float/2addr v0, v1

    goto :goto_11

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_miui_support_drawable_CardStateDrawable__onStateChange',
        'method': '.method protected onStateChange([I)Z',
        'method_name': 'onStateChange',
        'method_anchors': ['iget-object p0, p0, Lcom/miui/support/drawable/CardStateDrawable;->mStateEffect:Lmiuix/animation/styles/AlphaBlendingStateEffect;', 'invoke-virtual {p0, p1}, Lmiuix/animation/styles/DrawableStateEffect;->onStateChange([I)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected onStateChange([I)Z
    .registers 2

    iget-object p0, p0, Lcom/miui/support/drawable/CardStateDrawable;->mStateEffect:Lmiuix/animation/styles/AlphaBlendingStateEffect;

    invoke-virtual {p0, p1}, Lmiuix/animation/styles/DrawableStateEffect;->onStateChange([I)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onStateChange([I)Z
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lmiuix/animation/styles/DrawableStateEffect;->onStateChange([I)Z

    move-result p0

    goto :goto_1

    nop

    :goto_1
    return p0

    :goto_2
    iget-object p0, p0, Lcom/miui/support/drawable/CardStateDrawable;->mStateEffect:Lmiuix/animation/styles/AlphaBlendingStateEffect;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_miui_support_drawable_CardStateDrawable__setRadii',
        'method': '.method protected setRadii(II)V',
        'method_name': 'setRadii',
        'method_anchors': ['if-ne p2, v9, :cond_0', 'iput-object p1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F', 'return-void', 'if-ne p2, v6, :cond_1', 'iput-object p2, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F', 'return-void', 'if-ne p2, v5, :cond_2', 'iput-object p2, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F'],
        'type': 'method_replace',
        'search': """.method protected setRadii(II)V
    .registers 13

    const/4 v0, 0x7

    const/4 v1, 0x6

    const/4 v2, 0x5

    const/4 v3, 0x1

    const/4 v4, 0x0

    const/4 v5, 0x4

    const/4 v6, 0x2

    const/16 v7, 0x8

    const/4 v8, 0x0

    const/4 v9, 0x3

    if-ne p2, v9, :cond_0

    new-array p1, v7, [F

    iput-object p1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F

    return-void

    :cond_0
    if-ne p2, v6, :cond_1

    int-to-float p1, p1

    new-array p2, v7, [F

    aput p1, p2, v4

    aput p1, p2, v3

    aput p1, p2, v6

    aput p1, p2, v9

    aput v8, p2, v5

    aput v8, p2, v2

    aput v8, p2, v1

    aput v8, p2, v0

    iput-object p2, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F

    return-void

    :cond_1
    if-ne p2, v5, :cond_2

    int-to-float p1, p1

    new-array p2, v7, [F

    aput v8, p2, v4

    aput v8, p2, v3

    aput v8, p2, v6

    aput v8, p2, v9

    aput p1, p2, v5

    aput p1, p2, v2

    aput p1, p2, v1

    aput p1, p2, v0

    iput-object p2, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F

    return-void

    :cond_2
    int-to-float p1, p1

    new-array p2, v7, [F

    aput p1, p2, v4

    aput p1, p2, v3

    aput p1, p2, v6

    aput p1, p2, v9

    aput p1, p2, v5

    aput p1, p2, v2

    aput p1, p2, v1

    aput p1, p2, v0

    iput-object p2, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F

    return-void
.end method""",
        'replacement': """.method protected setRadii(II)V
    .registers 13

    goto :goto_24

    nop

    :goto_0
    aput p1, p2, v2

    goto :goto_2f

    nop

    :goto_1
    const/4 v5, 0x4

    goto :goto_2b

    nop

    :goto_2
    iput-object p2, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F

    goto :goto_33

    nop

    :goto_3
    if-eq p2, v9, :cond_0

    goto :goto_2d

    :cond_0
    goto :goto_12

    nop

    :goto_4
    return-void

    :goto_5
    goto :goto_29

    nop

    :goto_6
    const/16 v7, 0x8

    goto :goto_11

    nop

    :goto_7
    aput v8, p2, v1

    goto :goto_1d

    nop

    :goto_8
    aput p1, p2, v2

    goto :goto_16

    nop

    :goto_9
    aput v8, p2, v2

    goto :goto_7

    nop

    :goto_a
    if-eq p2, v6, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_2e

    nop

    :goto_b
    new-array p2, v7, [F

    goto :goto_1a

    nop

    :goto_c
    aput p1, p2, v9

    goto :goto_17

    nop

    :goto_d
    iput-object p1, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F

    goto :goto_2c

    nop

    :goto_e
    const/4 v4, 0x0

    goto :goto_1

    nop

    :goto_f
    aput v8, p2, v3

    goto :goto_26

    nop

    :goto_10
    aput p1, p2, v0

    goto :goto_31

    nop

    :goto_11
    const/4 v8, 0x0

    goto :goto_34

    nop

    :goto_12
    new-array p1, v7, [F

    goto :goto_d

    nop

    :goto_13
    aput p1, p2, v5

    goto :goto_8

    nop

    :goto_14
    const/4 v2, 0x5

    goto :goto_23

    nop

    :goto_15
    aput p1, p2, v3

    goto :goto_27

    nop

    :goto_16
    aput p1, p2, v1

    goto :goto_10

    nop

    :goto_17
    aput p1, p2, v5

    goto :goto_0

    nop

    :goto_18
    aput v8, p2, v5

    goto :goto_9

    nop

    :goto_19
    aput v8, p2, v4

    goto :goto_f

    nop

    :goto_1a
    aput p1, p2, v4

    goto :goto_21

    nop

    :goto_1b
    aput p1, p2, v6

    goto :goto_28

    nop

    :goto_1c
    new-array p2, v7, [F

    goto :goto_19

    nop

    :goto_1d
    aput v8, p2, v0

    goto :goto_20

    nop

    :goto_1e
    return-void

    :goto_1f
    goto :goto_36

    nop

    :goto_20
    iput-object p2, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F

    goto :goto_4

    nop

    :goto_21
    aput p1, p2, v3

    goto :goto_1b

    nop

    :goto_22
    int-to-float p1, p1

    goto :goto_1c

    nop

    :goto_23
    const/4 v3, 0x1

    goto :goto_e

    nop

    :goto_24
    const/4 v0, 0x7

    goto :goto_35

    nop

    :goto_25
    new-array p2, v7, [F

    goto :goto_32

    nop

    :goto_26
    aput v8, p2, v6

    goto :goto_30

    nop

    :goto_27
    aput p1, p2, v6

    goto :goto_c

    nop

    :goto_28
    aput p1, p2, v9

    goto :goto_18

    nop

    :goto_29
    if-eq p2, v5, :cond_2

    goto :goto_1f

    :cond_2
    goto :goto_22

    nop

    :goto_2a
    aput p1, p2, v0

    goto :goto_2

    nop

    :goto_2b
    const/4 v6, 0x2

    goto :goto_6

    nop

    :goto_2c
    return-void

    :goto_2d
    goto :goto_a

    nop

    :goto_2e
    int-to-float p1, p1

    goto :goto_b

    nop

    :goto_2f
    aput p1, p2, v1

    goto :goto_2a

    nop

    :goto_30
    aput v8, p2, v9

    goto :goto_13

    nop

    :goto_31
    iput-object p2, p0, Lcom/miui/support/drawable/CardStateDrawable;->mAllRadii:[F

    goto :goto_1e

    nop

    :goto_32
    aput p1, p2, v4

    goto :goto_15

    nop

    :goto_33
    return-void

    :goto_34
    const/4 v9, 0x3

    goto :goto_3

    nop

    :goto_35
    const/4 v1, 0x6

    goto :goto_14

    nop

    :goto_36
    int-to-float p1, p1

    goto :goto_25

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
