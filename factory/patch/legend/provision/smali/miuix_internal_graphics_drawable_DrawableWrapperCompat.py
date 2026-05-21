TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/graphics/drawable/DrawableWrapperCompat.smali'
CLASS_FALLBACK_NAMES = ['DrawableWrapperCompat.smali']
CLASS_ANCHORS = ['.super Landroid/graphics/drawable/Drawable;', '.implements Landroid/graphics/drawable/Drawable$Callback;']

PATCHES = [
    {
        'id': 'miuix_internal_graphics_drawable_DrawableWrapperCompat__onBoundsChange',
        'method': '.method protected onBoundsChange(Landroid/graphics/Rect;)V',
        'method_name': 'onBoundsChange',
        'method_anchors': ['iget-object p0, p0, Lmiuix/internal/graphics/drawable/DrawableWrapperCompat;->mDrawable:Landroid/graphics/drawable/Drawable;', 'invoke-virtual {p0, p1}, Landroid/graphics/drawable/Drawable;->setBounds(Landroid/graphics/Rect;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 2

    iget-object p0, p0, Lmiuix/internal/graphics/drawable/DrawableWrapperCompat;->mDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {p0, p1}, Landroid/graphics/drawable/Drawable;->setBounds(Landroid/graphics/Rect;)V

    return-void
.end method""",
        'replacement': """.method protected onBoundsChange(Landroid/graphics/Rect;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iget-object p0, p0, Lmiuix/internal/graphics/drawable/DrawableWrapperCompat;->mDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1}, Landroid/graphics/drawable/Drawable;->setBounds(Landroid/graphics/Rect;)V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_internal_graphics_drawable_DrawableWrapperCompat__onLevelChange',
        'method': '.method protected onLevelChange(I)Z',
        'method_name': 'onLevelChange',
        'method_anchors': ['iget-object p0, p0, Lmiuix/internal/graphics/drawable/DrawableWrapperCompat;->mDrawable:Landroid/graphics/drawable/Drawable;', 'invoke-virtual {p0, p1}, Landroid/graphics/drawable/Drawable;->setLevel(I)Z', 'return p0'],
        'type': 'method_replace',
        'search': """.method protected onLevelChange(I)Z
    .registers 2

    iget-object p0, p0, Lmiuix/internal/graphics/drawable/DrawableWrapperCompat;->mDrawable:Landroid/graphics/drawable/Drawable;

    invoke-virtual {p0, p1}, Landroid/graphics/drawable/Drawable;->setLevel(I)Z

    move-result p0

    return p0
.end method""",
        'replacement': """.method protected onLevelChange(I)Z
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    iget-object p0, p0, Lmiuix/internal/graphics/drawable/DrawableWrapperCompat;->mDrawable:Landroid/graphics/drawable/Drawable;

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1}, Landroid/graphics/drawable/Drawable;->setLevel(I)Z

    move-result p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
