TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/graphics/shadow/DropShadowLayerHelper.smali'
CLASS_FALLBACK_NAMES = ['DropShadowLayerHelper.smali']
CLASS_ANCHORS = ['.super Lmiuix/graphics/shadow/DropShadowHelper;']

PATCHES = [
    {
        'id': 'miuix_graphics_shadow_DropShadowLayerHelper__onDensityChanged',
        'method': '.method protected onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V',
        'method_name': 'onDensityChanged',
        'method_anchors': ['invoke-super {p0, p1, p2}, Lmiuix/graphics/shadow/DropShadowHelper;->onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V', 'iget-object p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowPaint:Landroid/graphics/Paint;', 'iget p2, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mBlurRadiusPx:F', 'iget v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetXPx:F', 'iget v1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetYPx:F', 'iget p0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColor:I', 'invoke-virtual {p1, p2, v0, v1, p0}, Landroid/graphics/Paint;->setShadowLayer(FFFI)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V
    .registers 5

    invoke-super {p0, p1, p2}, Lmiuix/graphics/shadow/DropShadowHelper;->onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V

    iget-object p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowPaint:Landroid/graphics/Paint;

    iget p2, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mBlurRadiusPx:F

    iget v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetXPx:F

    iget v1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetYPx:F

    iget p0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColor:I

    invoke-virtual {p1, p2, v0, v1, p0}, Landroid/graphics/Paint;->setShadowLayer(FFFI)V

    return-void
.end method""",
        'replacement': """.method protected onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V
    .registers 5

    goto :goto_7

    nop

    :goto_0
    iget p0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColor:I

    goto :goto_4

    nop

    :goto_1
    iget v1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetYPx:F

    goto :goto_0

    nop

    :goto_2
    iget p2, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mBlurRadiusPx:F

    goto :goto_6

    nop

    :goto_3
    return-void

    :goto_4
    invoke-virtual {p1, p2, v0, v1, p0}, Landroid/graphics/Paint;->setShadowLayer(FFFI)V

    goto :goto_3

    nop

    :goto_5
    iget-object p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowPaint:Landroid/graphics/Paint;

    goto :goto_2

    nop

    :goto_6
    iget v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetXPx:F

    goto :goto_1

    nop

    :goto_7
    invoke-super {p0, p1, p2}, Lmiuix/graphics/shadow/DropShadowHelper;->onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
