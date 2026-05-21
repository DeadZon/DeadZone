TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/PreferenceCategoryLayout.smali'
CLASS_FALLBACK_NAMES = ['PreferenceCategoryLayout.smali']
CLASS_ANCHORS = ['.super Landroid/widget/FrameLayout;']

PATCHES = [
    {
        'id': 'miuix_preference_PreferenceCategoryLayout__onFinishInflate',
        'method': '.method protected onFinishInflate()V',
        'method_name': 'onFinishInflate',
        'method_anchors': ['invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V', 'invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;', 'sget v1, Lmiuix/preference/R$attr;->preferenceCardStyleEnable:I', 'sget v2, Lmiuix/preference/R$attr;->preferenceTraditionalCategoryBackground:I', 'invoke-virtual {v0, v1}, Landroid/content/Context;->obtainStyledAttributes([I)Landroid/content/res/TypedArray;', 'invoke-virtual {v0, v1, v2}, Landroid/content/res/TypedArray;->getInt(II)I', 'if-eq v1, v3, :cond_1', 'invoke-static {}, Lmiuix/core/util/RomUtils;->getHyperOsVersion()I'],
        'type': 'method_replace',
        'search': """.method protected onFinishInflate()V
    .registers 5

    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    sget v1, Lmiuix/preference/R$attr;->preferenceCardStyleEnable:I

    sget v2, Lmiuix/preference/R$attr;->preferenceTraditionalCategoryBackground:I

    filled-new-array {v1, v2}, [I

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/content/Context;->obtainStyledAttributes([I)Landroid/content/res/TypedArray;

    move-result-object v0

    const/4 v1, 0x0

    const/4 v2, 0x1

    invoke-virtual {v0, v1, v2}, Landroid/content/res/TypedArray;->getInt(II)I

    move-result v1

    const/4 v3, 0x2

    if-eq v1, v3, :cond_1

    invoke-static {}, Lmiuix/core/util/RomUtils;->getHyperOsVersion()I

    move-result v3

    if-le v3, v2, :cond_0

    if-ne v1, v2, :cond_0

    goto :goto_0

    :cond_0
    invoke-virtual {v0, v2}, Landroid/content/res/TypedArray;->getDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    invoke-virtual {p0, v1}, Landroid/widget/FrameLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V

    :cond_1
    :goto_0
    invoke-virtual {v0}, Landroid/content/res/TypedArray;->recycle()V

    return-void
.end method""",
        'replacement': """.method protected onFinishInflate()V
    .registers 5

    goto :goto_7

    nop

    :goto_0
    sget v2, Lmiuix/preference/R$attr;->preferenceTraditionalCategoryBackground:I

    goto :goto_a

    nop

    :goto_1
    const/4 v2, 0x1

    goto :goto_d

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/widget/FrameLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_10

    nop

    :goto_3
    if-ne v1, v3, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_c

    nop

    :goto_4
    invoke-virtual {v0, v2}, Landroid/content/res/TypedArray;->getDrawable(I)Landroid/graphics/drawable/Drawable;

    move-result-object v1

    goto :goto_e

    nop

    :goto_5
    const/4 v3, 0x2

    goto :goto_3

    nop

    :goto_6
    if-eq v1, v2, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_8

    nop

    :goto_7
    invoke-super {p0}, Landroid/widget/FrameLayout;->onFinishInflate()V

    goto :goto_2

    nop

    :goto_8
    goto :goto_f

    :goto_9
    goto :goto_4

    nop

    :goto_a
    filled-new-array {v1, v2}, [I

    move-result-object v1

    goto :goto_b

    nop

    :goto_b
    invoke-virtual {v0, v1}, Landroid/content/Context;->obtainStyledAttributes([I)Landroid/content/res/TypedArray;

    move-result-object v0

    goto :goto_11

    nop

    :goto_c
    invoke-static {}, Lmiuix/core/util/RomUtils;->getHyperOsVersion()I

    move-result v3

    goto :goto_14

    nop

    :goto_d
    invoke-virtual {v0, v1, v2}, Landroid/content/res/TypedArray;->getInt(II)I

    move-result v1

    goto :goto_5

    nop

    :goto_e
    invoke-virtual {p0, v1}, Landroid/widget/FrameLayout;->setBackground(Landroid/graphics/drawable/Drawable;)V

    :goto_f
    goto :goto_13

    nop

    :goto_10
    sget v1, Lmiuix/preference/R$attr;->preferenceCardStyleEnable:I

    goto :goto_0

    nop

    :goto_11
    const/4 v1, 0x0

    goto :goto_1

    nop

    :goto_12
    return-void

    :goto_13
    invoke-virtual {v0}, Landroid/content/res/TypedArray;->recycle()V

    goto :goto_12

    nop

    :goto_14
    if-gt v3, v2, :cond_2

    goto :goto_9

    :cond_2
    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
