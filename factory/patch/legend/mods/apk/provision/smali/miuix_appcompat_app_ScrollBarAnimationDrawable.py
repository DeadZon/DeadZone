TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/appcompat/app/ScrollBarAnimationDrawable.smali'
CLASS_FALLBACK_NAMES = ['ScrollBarAnimationDrawable.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/Drawable;']

PATCHES = [
    {
        'id': 'miuix_appcompat_app_ScrollBarAnimationDrawable__onBoundsChange',
        'method': '.method protected onBoundsChange(Landroid/graphics/Rect;)V',
        'method_name': 'onBoundsChange',
        'method_anchors': ['iget-object v0, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mRect:Landroid/graphics/RectF;', 'invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V', 'iget-object p1, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mRect:Landroid/graphics/RectF;', 'iget v0, p1, Landroid/graphics/RectF;->left:F', 'iget v1, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mInsetsLeft:F', 'iput v0, p1, Landroid/graphics/RectF;->left:F', 'iget v0, p1, Landroid/graphics/RectF;->right:F', 'iget p0, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mInsetsRight:F'],
        'type': 'method_replace',
        'search': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 4

    iget-object v0, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mRect:Landroid/graphics/RectF;

    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    iget-object p1, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mRect:Landroid/graphics/RectF;

    iget v0, p1, Landroid/graphics/RectF;->left:F

    iget v1, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mInsetsLeft:F

    add-float/2addr v0, v1

    iput v0, p1, Landroid/graphics/RectF;->left:F

    iget v0, p1, Landroid/graphics/RectF;->right:F

    iget p0, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mInsetsRight:F

    add-float/2addr v0, p0

    iput v0, p1, Landroid/graphics/RectF;->right:F

    return-void
.end method""",
        'replacement': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 4

    goto :goto_4

    nop

    :goto_0
    invoke-virtual {v0, p1}, Landroid/graphics/RectF;->set(Landroid/graphics/Rect;)V

    goto :goto_5

    nop

    :goto_1
    return-void

    :goto_2
    iget v1, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mInsetsLeft:F

    goto :goto_7

    nop

    :goto_3
    iput v0, p1, Landroid/graphics/RectF;->right:F

    goto :goto_1

    nop

    :goto_4
    iget-object v0, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_0

    nop

    :goto_5
    iget-object p1, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mRect:Landroid/graphics/RectF;

    goto :goto_6

    nop

    :goto_6
    iget v0, p1, Landroid/graphics/RectF;->left:F

    goto :goto_2

    nop

    :goto_7
    add-float/2addr v0, v1

    goto :goto_a

    nop

    :goto_8
    add-float/2addr v0, p0

    goto :goto_3

    nop

    :goto_9
    iget p0, p0, Lmiuix/appcompat/app/ScrollBarAnimationDrawable;->mInsetsRight:F

    goto :goto_8

    nop

    :goto_a
    iput v0, p1, Landroid/graphics/RectF;->left:F

    goto :goto_b

    nop

    :goto_b
    iget v0, p1, Landroid/graphics/RectF;->right:F

    goto :goto_9

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
