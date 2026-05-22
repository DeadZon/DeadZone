TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/AlphaBlendingDrawable.smali'
CLASS_FALLBACK_NAMES = ['AlphaBlendingDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/Drawable;', '.implements Lmiuix/animation/styles/AlphaBlendingStateEffect$AlphaObserver;', '.field private static final USE_FOLME:Z']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_AlphaBlendingDrawable__onBoundsChange',
        'method': '.method protected onBoundsChange(Landroid/graphics/Rect;)V',
        'method_name': 'onBoundsChange',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mRect:Landroid/graphics/RectF;', 'invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V', 'iget-object p1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mRect:Landroid/graphics/RectF;', 'iget v0, p1, Landroid/graphics/RectF;->left:F', 'iget v1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mInsetL:I', 'iput v0, p1, Landroid/graphics/RectF;->left:F', 'iget v0, p1, Landroid/graphics/RectF;->top:F', 'iget v1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mInsetT:I'],
        'type': 'method_replace',
        'search': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 4

    iget-object v0, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mRect:Landroid/graphics/RectF;

    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    iget-object p1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mRect:Landroid/graphics/RectF;

    iget v0, p1, Landroid/graphics/RectF;->left:F

    iget v1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mInsetL:I

    int-to-float v1, v1

    add-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->left:F

    iget v0, p1, Landroid/graphics/RectF;->top:F

    iget v1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mInsetT:I

    int-to-float v1, v1

    add-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->top:F

    iget v0, p1, Landroid/graphics/RectF;->right:F

    iget v1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mInsetR:I

    int-to-float v1, v1

    sub-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->right:F

    iget v0, p1, Landroid/graphics/RectF;->bottom:F

    iget p0, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mInsetB:I

    int-to-float p0, p0

    sub-float/2addr v0, p0

    iput v0, p1, Landroid/graphics/RectF;->bottom:F

    return-void
.end method""",
        'replacement': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    iget p0, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mInsetB:I

    goto :goto_6

    nop

    :goto_1
    iget-object v0, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_11

    nop

    :goto_2
    iget v1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mInsetR:I

    goto :goto_12

    nop

    :goto_3
    add-float/2addr v0, v1

    goto :goto_4

    nop

    :goto_4
    iput v0, p1, Landroid/graphics/RectF;->top:F

    goto :goto_15

    nop

    :goto_5
    iget v1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mInsetT:I

    goto :goto_7

    nop

    :goto_6
    int-to-float p0, p0

    goto :goto_14

    nop

    :goto_7
    int-to-float v1, v1

    goto :goto_3

    nop

    :goto_8
    iput v0, p1, Landroid/graphics/RectF;->left:F

    goto :goto_a

    nop

    :goto_9
    iget v1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mInsetL:I

    goto :goto_c

    nop

    :goto_a
    iget v0, p1, Landroid/graphics/RectF;->top:F

    goto :goto_5

    nop

    :goto_b
    sub-float/2addr v0, v1

    goto :goto_16

    nop

    :goto_c
    int-to-float v1, v1

    goto :goto_10

    nop

    :goto_d
    iget-object p1, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_17

    nop

    :goto_e
    iput v0, p1, Landroid/graphics/RectF;->bottom:F

    goto :goto_13

    nop

    :goto_f
    iget v0, p1, Landroid/graphics/RectF;->bottom:F

    goto :goto_0

    nop

    :goto_10
    add-float/2addr v0, v1

    goto :goto_8

    nop

    :goto_11
    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    goto :goto_d

    nop

    :goto_12
    int-to-float v1, v1

    goto :goto_b

    nop

    :goto_13
    return-void

    :goto_14
    sub-float/2addr v0, p0

    goto :goto_e

    nop

    :goto_15
    iget v0, p1, Landroid/graphics/RectF;->right:F

    goto :goto_2

    nop

    :goto_16
    iput v0, p1, Landroid/graphics/RectF;->right:F

    goto :goto_f

    nop

    :goto_17
    iget v0, p1, Landroid/graphics/RectF;->left:F

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_appcompat_app_AlphaBlendingDrawable__onStateChange',
        'method': '.method protected onStateChange([I)Z',
        'method_name': 'onStateChange',
        'method_anchors': ['iget-object p0, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mStateEffect:Lmiuix/animation/styles/AlphaBlendingStateEffect;', 'invoke-virtual {p0, p1}, Lmiuix/animation/styles/DrawableStateEffect;->onStateChange([I)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected onStateChange([I)Z
    .registers 2

    iget-object p0, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mStateEffect:Lmiuix/animation/styles/AlphaBlendingStateEffect;

    invoke-virtual {p0, p1}, Lmiuix/animation/styles/DrawableStateEffect;->onStateChange([I)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onStateChange([I)Z
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return p0

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/animation/styles/DrawableStateEffect;->onStateChange([I)Z

    move-result p0

    goto :goto_0

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/appcompat/app/AlphaBlendingDrawable;->mStateEffect:Lmiuix/animation/styles/AlphaBlendingStateEffect;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
