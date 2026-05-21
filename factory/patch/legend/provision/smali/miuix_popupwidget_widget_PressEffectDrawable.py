TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/popupwidget/widget/PressEffectDrawable.smali'
CLASS_FALLBACK_NAMES = ['PressEffectDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/Drawable;', '.implements Lmiuix/animation/FolmeObject;', '.field private static final ACTIVATE_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', '.field private static final ACTIVATE_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;', '.field private static final HOVER_ENTER_CONFIG:Lmiuix/animation/base/AnimConfig;', '.field private static final HOVER_EXIT_CONFIG:Lmiuix/animation/base/AnimConfig;']

PATCHES = [
    {
        'id': 'miuix_popupwidget_widget_PressEffectDrawable__onBoundsChange',
        'method': '.method protected onBoundsChange(Landroid/graphics/Rect;)V',
        'method_name': 'onBoundsChange',
        'method_anchors': ['iget-object v0, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mRect:Landroid/graphics/RectF;', 'invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V', 'iget-object p1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mRect:Landroid/graphics/RectF;', 'iget v0, p1, Landroid/graphics/RectF;->left:F', 'iget v1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mInsetL:I', 'iput v0, p1, Landroid/graphics/RectF;->left:F', 'iget v0, p1, Landroid/graphics/RectF;->top:F', 'iget v1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mInsetT:I'],
        'type': 'method_replace',
        'search': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 4

    iget-object v0, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mRect:Landroid/graphics/RectF;

    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    iget-object p1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mRect:Landroid/graphics/RectF;

    iget v0, p1, Landroid/graphics/RectF;->left:F

    iget v1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mInsetL:I

    int-to-float v1, v1

    add-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->left:F

    iget v0, p1, Landroid/graphics/RectF;->top:F

    iget v1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mInsetT:I

    int-to-float v1, v1

    add-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->top:F

    iget v0, p1, Landroid/graphics/RectF;->right:F

    iget v1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mInsetR:I

    int-to-float v1, v1

    sub-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->right:F

    iget v0, p1, Landroid/graphics/RectF;->bottom:F

    iget p0, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mInsetB:I

    int-to-float p0, p0

    sub-float/2addr v0, p0

    iput v0, p1, Landroid/graphics/RectF;->bottom:F

    return-void
.end method""",
        'replacement': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 4

    goto :goto_a

    nop

    :goto_0
    add-float/2addr v0, v1

    goto :goto_14

    nop

    :goto_1
    iget-object p1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_15

    nop

    :goto_2
    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    goto :goto_1

    nop

    :goto_3
    iget v0, p1, Landroid/graphics/RectF;->bottom:F

    goto :goto_8

    nop

    :goto_4
    iget v1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mInsetT:I

    goto :goto_16

    nop

    :goto_5
    add-float/2addr v0, v1

    goto :goto_9

    nop

    :goto_6
    int-to-float v1, v1

    goto :goto_17

    nop

    :goto_7
    sub-float/2addr v0, p0

    goto :goto_13

    nop

    :goto_8
    iget p0, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mInsetB:I

    goto :goto_d

    nop

    :goto_9
    iput v0, p1, Landroid/graphics/RectF;->top:F

    goto :goto_11

    nop

    :goto_a
    iget-object v0, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_2

    nop

    :goto_b
    iget v1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mInsetL:I

    goto :goto_12

    nop

    :goto_c
    iget v1, p0, Lmiuix/popupwidget/widget/PressEffectDrawable;->mInsetR:I

    goto :goto_6

    nop

    :goto_d
    int-to-float p0, p0

    goto :goto_7

    nop

    :goto_e
    return-void

    :goto_f
    iget v0, p1, Landroid/graphics/RectF;->top:F

    goto :goto_4

    nop

    :goto_10
    iput v0, p1, Landroid/graphics/RectF;->right:F

    goto :goto_3

    nop

    :goto_11
    iget v0, p1, Landroid/graphics/RectF;->right:F

    goto :goto_c

    nop

    :goto_12
    int-to-float v1, v1

    goto :goto_0

    nop

    :goto_13
    iput v0, p1, Landroid/graphics/RectF;->bottom:F

    goto :goto_e

    nop

    :goto_14
    iput v0, p1, Landroid/graphics/RectF;->left:F

    goto :goto_f

    nop

    :goto_15
    iget v0, p1, Landroid/graphics/RectF;->left:F

    goto :goto_b

    nop

    :goto_16
    int-to-float v1, v1

    goto :goto_5

    nop

    :goto_17
    sub-float/2addr v0, v1

    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_popupwidget_widget_PressEffectDrawable__onStateChange',
        'method': '.method protected onStateChange([I)Z',
        'method_name': 'onStateChange',
        'method_anchors': ['sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_PRESSED:[I', 'invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z', 'if-nez v0, :cond_4', 'sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_DRAG_HOVERED:[I', 'invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z', 'if-nez v0, :cond_4', 'sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_SELECTED:[I', 'invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z'],
        'type': 'method_replace',
        'search': """.method protected onStateChange([I)Z
    .registers 3

    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_PRESSED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-nez v0, :cond_4

    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_DRAG_HOVERED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-nez v0, :cond_4

    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_SELECTED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_HOVERED_ACTIVATED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-direct {p0}, Lmiuix/popupwidget/widget/PressEffectDrawable;->toHoveredActivatedState()Z

    move-result p0

    return p0

    :cond_1
    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_HOVERED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-direct {p0}, Lmiuix/popupwidget/widget/PressEffectDrawable;->toHoveredState()Z

    move-result p0

    return p0

    :cond_2
    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_ACTIVATED:[I

    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result p1

    if-eqz p1, :cond_3

    invoke-direct {p0}, Lmiuix/popupwidget/widget/PressEffectDrawable;->toActivatedState()Z

    move-result p0

    return p0

    :cond_3
    invoke-direct {p0}, Lmiuix/popupwidget/widget/PressEffectDrawable;->toNormalState()Z

    move-result p0

    return p0

    :cond_4
    :goto_0
    invoke-direct {p0}, Lmiuix/popupwidget/widget/PressEffectDrawable;->toPressedState()Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onStateChange([I)Z
    .registers 3

    goto :goto_1e

    nop

    :goto_0
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_4

    nop

    :goto_1
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_18

    nop

    :goto_2
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_1f

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_12

    nop

    :goto_4
    if-nez v0, :cond_1

    goto :goto_21

    :cond_1
    goto :goto_20

    nop

    :goto_5
    if-nez v0, :cond_2

    goto :goto_d

    :cond_2
    goto :goto_8

    nop

    :goto_6
    return p0

    :goto_7
    goto :goto_1b

    nop

    :goto_8
    invoke-direct {p0}, Lmiuix/popupwidget/widget/PressEffectDrawable;->toHoveredActivatedState()Z

    move-result p0

    goto :goto_c

    nop

    :goto_9
    invoke-direct {p0}, Lmiuix/popupwidget/widget/PressEffectDrawable;->toNormalState()Z

    move-result p0

    goto :goto_6

    nop

    :goto_a
    if-nez p1, :cond_3

    goto :goto_1a

    :cond_3
    goto :goto_13

    nop

    :goto_b
    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_HOVERED_ACTIVATED:[I

    goto :goto_14

    nop

    :goto_c
    return p0

    :goto_d
    goto :goto_f

    nop

    :goto_e
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_3

    nop

    :goto_f
    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_HOVERED:[I

    goto :goto_1

    nop

    :goto_10
    invoke-direct {p0}, Lmiuix/popupwidget/widget/PressEffectDrawable;->toHoveredState()Z

    move-result p0

    goto :goto_15

    nop

    :goto_11
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result p1

    goto :goto_a

    nop

    :goto_12
    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_SELECTED:[I

    goto :goto_0

    nop

    :goto_13
    invoke-direct {p0}, Lmiuix/popupwidget/widget/PressEffectDrawable;->toActivatedState()Z

    move-result p0

    goto :goto_19

    nop

    :goto_14
    invoke-static {v0, p1}, Landroid/util/StateSet;->stateSetMatches([I[I)Z

    move-result v0

    goto :goto_5

    nop

    :goto_15
    return p0

    :goto_16
    goto :goto_1c

    nop

    :goto_17
    return p0

    :goto_18
    if-nez v0, :cond_4

    goto :goto_16

    :cond_4
    goto :goto_10

    nop

    :goto_19
    return p0

    :goto_1a
    goto :goto_9

    nop

    :goto_1b
    invoke-direct {p0}, Lmiuix/popupwidget/widget/PressEffectDrawable;->toPressedState()Z

    move-result p0

    goto :goto_17

    nop

    :goto_1c
    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_ACTIVATED:[I

    goto :goto_11

    nop

    :goto_1d
    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_DRAG_HOVERED:[I

    goto :goto_e

    nop

    :goto_1e
    sget-object v0, Lmiuix/popupwidget/widget/PressEffectDrawable;->STATE_PRESSED:[I

    goto :goto_2

    nop

    :goto_1f
    if-eqz v0, :cond_5

    goto :goto_7

    :cond_5
    goto :goto_1d

    nop

    :goto_20
    goto :goto_7

    :goto_21
    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
