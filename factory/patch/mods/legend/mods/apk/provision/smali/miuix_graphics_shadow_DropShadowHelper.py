TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/graphics/shadow/DropShadowHelper.smali'
CLASS_FALLBACK_NAMES = ['DropShadowHelper.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'miuix_graphics_shadow_DropShadowHelper__onDensityChanged',
        'method': '.method protected onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V',
        'method_name': 'onDensityChanged',
        'method_anchors': ['iget v0, p2, Lmiuix/graphics/shadow/DropShadowConfig;->offsetXDp:F', 'invoke-static {p1, v0}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I', 'iput v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetXPx:F', 'iget v0, p2, Lmiuix/graphics/shadow/DropShadowConfig;->offsetYDp:F', 'invoke-static {p1, v0}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I', 'iput v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetYPx:F', 'iget p2, p2, Lmiuix/graphics/shadow/DropShadowConfig;->blurRadiusDp:F', 'invoke-static {p1, p2}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I'],
        'type': 'method_replace',
        'search': """.method protected onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V
    .registers 4

    iget v0, p2, Lmiuix/graphics/shadow/DropShadowConfig;->offsetXDp:F

    invoke-static {p1, v0}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I

    move-result v0

    int-to-float v0, v0

    iput v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetXPx:F

    iget v0, p2, Lmiuix/graphics/shadow/DropShadowConfig;->offsetYDp:F

    invoke-static {p1, v0}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I

    move-result v0

    int-to-float v0, v0

    iput v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetYPx:F

    iget p2, p2, Lmiuix/graphics/shadow/DropShadowConfig;->blurRadiusDp:F

    invoke-static {p1, p2}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I

    move-result p1

    int-to-float p1, p1

    iput p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mBlurRadiusPx:F

    return-void
.end method""",
        'replacement': """.method protected onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V
    .registers 4

    goto :goto_5

    nop

    :goto_0
    iput p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mBlurRadiusPx:F

    goto :goto_7

    nop

    :goto_1
    int-to-float v0, v0

    goto :goto_2

    nop

    :goto_2
    iput v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetYPx:F

    goto :goto_3

    nop

    :goto_3
    iget p2, p2, Lmiuix/graphics/shadow/DropShadowConfig;->blurRadiusDp:F

    goto :goto_8

    nop

    :goto_4
    iget v0, p2, Lmiuix/graphics/shadow/DropShadowConfig;->offsetYDp:F

    goto :goto_c

    nop

    :goto_5
    iget v0, p2, Lmiuix/graphics/shadow/DropShadowConfig;->offsetXDp:F

    goto :goto_6

    nop

    :goto_6
    invoke-static {p1, v0}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I

    move-result v0

    goto :goto_a

    nop

    :goto_7
    return-void

    :goto_8
    invoke-static {p1, p2}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I

    move-result p1

    goto :goto_9

    nop

    :goto_9
    int-to-float p1, p1

    goto :goto_0

    nop

    :goto_a
    int-to-float v0, v0

    goto :goto_b

    nop

    :goto_b
    iput v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetXPx:F

    goto :goto_4

    nop

    :goto_c
    invoke-static {p1, v0}, Lmiuix/core/util/MiuixUIUtils;->dp2px(FF)I

    move-result v0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_graphics_shadow_DropShadowHelper__updateShadowValues',
        'method': '.method protected updateShadowValues(ZFLmiuix/graphics/shadow/DropShadowConfig;)V',
        'method_name': 'updateShadowValues',
        'method_anchors': ['if-eqz p1, :cond_0', 'iget p1, p3, Lmiuix/graphics/shadow/DropShadowConfig;->shadowColor:I', 'iget p1, p3, Lmiuix/graphics/shadow/DropShadowConfig;->shadowDarkColor:I', 'iput p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColor:I', 'iput v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColorAlpha:I', 'iget-object v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowPaint:Landroid/graphics/Paint;', 'invoke-virtual {v0, p1}, Landroid/graphics/Paint;->setColor(I)V', 'iget p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mLastDensity:F'],
        'type': 'method_replace',
        'search': """.method protected updateShadowValues(ZFLmiuix/graphics/shadow/DropShadowConfig;)V
    .registers 5

    if-eqz p1, :cond_0

    iget p1, p3, Lmiuix/graphics/shadow/DropShadowConfig;->shadowColor:I

    goto :goto_0

    :cond_0
    iget p1, p3, Lmiuix/graphics/shadow/DropShadowConfig;->shadowDarkColor:I

    :goto_0
    iput p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColor:I

    shr-int/lit8 v0, p1, 0x18

    and-int/lit16 v0, v0, 0xff

    iput v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColorAlpha:I

    iget-object v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowPaint:Landroid/graphics/Paint;

    invoke-virtual {v0, p1}, Landroid/graphics/Paint;->setColor(I)V

    iget p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mLastDensity:F

    cmpl-float p1, p1, p2

    if-eqz p1, :cond_1

    iput p2, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mLastDensity:F

    :cond_1
    invoke-virtual {p0, p2, p3}, Lmiuix/graphics/shadow/DropShadowHelper;->onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V

    iget-object p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowPaint:Landroid/graphics/Paint;

    iget p2, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mBlurRadiusPx:F

    iget p3, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetXPx:F

    iget v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetYPx:F

    iget p0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColor:I

    invoke-virtual {p1, p2, p3, v0, p0}, Landroid/graphics/Paint;->setShadowLayer(FFFI)V

    return-void
.end method""",
        'replacement': """.method protected updateShadowValues(ZFLmiuix/graphics/shadow/DropShadowConfig;)V
    .registers 5

    goto :goto_3

    nop

    :goto_0
    iget p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mLastDensity:F

    goto :goto_14

    nop

    :goto_1
    if-nez p1, :cond_0

    goto :goto_18

    :cond_0
    goto :goto_17

    nop

    :goto_2
    invoke-virtual {p0, p2, p3}, Lmiuix/graphics/shadow/DropShadowHelper;->onDensityChanged(FLmiuix/graphics/shadow/DropShadowConfig;)V

    goto :goto_13

    nop

    :goto_3
    if-nez p1, :cond_1

    goto :goto_6

    :cond_1
    goto :goto_9

    nop

    :goto_4
    iget p3, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetXPx:F

    goto :goto_15

    nop

    :goto_5
    goto :goto_f

    :goto_6
    goto :goto_e

    nop

    :goto_7
    iput v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColorAlpha:I

    goto :goto_c

    nop

    :goto_8
    invoke-virtual {p1, p2, p3, v0, p0}, Landroid/graphics/Paint;->setShadowLayer(FFFI)V

    goto :goto_b

    nop

    :goto_9
    iget p1, p3, Lmiuix/graphics/shadow/DropShadowConfig;->shadowColor:I

    goto :goto_5

    nop

    :goto_a
    and-int/lit16 v0, v0, 0xff

    goto :goto_7

    nop

    :goto_b
    return-void

    :goto_c
    iget-object v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowPaint:Landroid/graphics/Paint;

    goto :goto_10

    nop

    :goto_d
    iput p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColor:I

    goto :goto_16

    nop

    :goto_e
    iget p1, p3, Lmiuix/graphics/shadow/DropShadowConfig;->shadowDarkColor:I

    :goto_f
    goto :goto_d

    nop

    :goto_10
    invoke-virtual {v0, p1}, Landroid/graphics/Paint;->setColor(I)V

    goto :goto_0

    nop

    :goto_11
    iget p0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowColor:I

    goto :goto_8

    nop

    :goto_12
    iget p2, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mBlurRadiusPx:F

    goto :goto_4

    nop

    :goto_13
    iget-object p1, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mShadowPaint:Landroid/graphics/Paint;

    goto :goto_12

    nop

    :goto_14
    cmpl-float p1, p1, p2

    goto :goto_1

    nop

    :goto_15
    iget v0, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mOffsetYPx:F

    goto :goto_11

    nop

    :goto_16
    shr-int/lit8 v0, p1, 0x18

    goto :goto_a

    nop

    :goto_17
    iput p2, p0, Lmiuix/graphics/shadow/DropShadowHelper;->mLastDensity:F

    :goto_18
    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
