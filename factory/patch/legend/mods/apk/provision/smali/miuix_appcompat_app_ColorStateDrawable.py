TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/ColorStateDrawable.smali'
CLASS_FALLBACK_NAMES = ['ColorStateDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/Drawable;', '.implements Lmiuix/animation/styles/ColorStateEffect$ColorObserver;', '.field private static final USE_FOLME:Z']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_ColorStateDrawable__onBoundsChange',
        'method': '.method protected onBoundsChange(Landroid/graphics/Rect;)V',
        'method_name': 'onBoundsChange',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mRect:Landroid/graphics/RectF;', 'invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V', 'iget-object p1, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mRect:Landroid/graphics/RectF;', 'iget v0, p1, Landroid/graphics/RectF;->left:F', 'iget-object p0, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mState:Lmiuix/appcompat/app/ColorStateDrawable$ColorState;', 'iget v1, p0, Lmiuix/appcompat/app/ColorStateDrawable$ColorState;->mInsetL:I', 'iput v0, p1, Landroid/graphics/RectF;->left:F', 'iget v0, p1, Landroid/graphics/RectF;->top:F'],
        'type': 'method_replace',
        'search': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 4

    iget-object v0, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mRect:Landroid/graphics/RectF;

    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    iget-object p1, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mRect:Landroid/graphics/RectF;

    iget v0, p1, Landroid/graphics/RectF;->left:F

    iget-object p0, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mState:Lmiuix/appcompat/app/ColorStateDrawable$ColorState;

    iget v1, p0, Lmiuix/appcompat/app/ColorStateDrawable$ColorState;->mInsetL:I

    int-to-float v1, v1

    add-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->left:F

    iget v0, p1, Landroid/graphics/RectF;->top:F

    iget v1, p0, Lmiuix/appcompat/app/ColorStateDrawable$ColorState;->mInsetT:I

    int-to-float v1, v1

    add-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->top:F

    iget v0, p1, Landroid/graphics/RectF;->right:F

    iget v1, p0, Lmiuix/appcompat/app/ColorStateDrawable$ColorState;->mInsetR:I

    int-to-float v1, v1

    sub-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->right:F

    iget v0, p1, Landroid/graphics/RectF;->bottom:F

    iget p0, p0, Lmiuix/appcompat/app/ColorStateDrawable$ColorState;->mInsetB:I

    int-to-float p0, p0

    sub-float/2addr v0, p0

    iput v0, p1, Landroid/graphics/RectF;->bottom:F

    return-void
.end method""",
        'replacement': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 4

    goto :goto_6

    nop

    :goto_0
    int-to-float p0, p0

    goto :goto_a

    nop

    :goto_1
    iget p0, p0, Lmiuix/appcompat/app/ColorStateDrawable$ColorState;->mInsetB:I

    goto :goto_0

    nop

    :goto_2
    iget v0, p1, Landroid/graphics/RectF;->bottom:F

    goto :goto_1

    nop

    :goto_3
    return-void

    :goto_4
    iput v0, p1, Landroid/graphics/RectF;->bottom:F

    goto :goto_3

    nop

    :goto_5
    iget v0, p1, Landroid/graphics/RectF;->top:F

    goto :goto_9

    nop

    :goto_6
    iget-object v0, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_f

    nop

    :goto_7
    int-to-float v1, v1

    goto :goto_10

    nop

    :goto_8
    iget v1, p0, Lmiuix/appcompat/app/ColorStateDrawable$ColorState;->mInsetL:I

    goto :goto_13

    nop

    :goto_9
    iget v1, p0, Lmiuix/appcompat/app/ColorStateDrawable$ColorState;->mInsetT:I

    goto :goto_14

    nop

    :goto_a
    sub-float/2addr v0, p0

    goto :goto_4

    nop

    :goto_b
    iget-object p1, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_18

    nop

    :goto_c
    iput v0, p1, Landroid/graphics/RectF;->left:F

    goto :goto_5

    nop

    :goto_d
    iget v0, p1, Landroid/graphics/RectF;->right:F

    goto :goto_17

    nop

    :goto_e
    iget-object p0, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mState:Lmiuix/appcompat/app/ColorStateDrawable$ColorState;

    goto :goto_8

    nop

    :goto_f
    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    goto :goto_b

    nop

    :goto_10
    sub-float/2addr v0, v1

    goto :goto_15

    nop

    :goto_11
    iput v0, p1, Landroid/graphics/RectF;->top:F

    goto :goto_d

    nop

    :goto_12
    add-float/2addr v0, v1

    goto :goto_11

    nop

    :goto_13
    int-to-float v1, v1

    goto :goto_16

    nop

    :goto_14
    int-to-float v1, v1

    goto :goto_12

    nop

    :goto_15
    iput v0, p1, Landroid/graphics/RectF;->right:F

    goto :goto_2

    nop

    :goto_16
    add-float/2addr v0, v1

    goto :goto_c

    nop

    :goto_17
    iget v1, p0, Lmiuix/appcompat/app/ColorStateDrawable$ColorState;->mInsetR:I

    goto :goto_7

    nop

    :goto_18
    iget v0, p1, Landroid/graphics/RectF;->left:F

    goto :goto_e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_ColorStateDrawable__onStateChange',
        'method': '.method protected onStateChange([I)Z',
        'method_name': 'onStateChange',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mStateEffect:Lmiuix/animation/styles/ColorStateEffect;', 'invoke-virtual {p0, p1}, Lmiuix/animation/styles/DrawableStateEffect;->onStateChange([I)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected onStateChange([I)Z
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mStateEffect:Lmiuix/animation/styles/ColorStateEffect;

    invoke-virtual {p0, p1}, Lmiuix/animation/styles/DrawableStateEffect;->onStateChange([I)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onStateChange([I)Z
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/appcompat/app/ColorStateDrawable;->mStateEffect:Lmiuix/animation/styles/ColorStateEffect;

    goto :goto_2

    nop

    :goto_1
    return p0

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/animation/styles/DrawableStateEffect;->onStateChange([I)Z

    move-result p0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
