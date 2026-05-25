TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/internal/view/CheckBoxAnimatedStateListDrawable$CheckBoxConstantState.smali'
CLASS_FALLBACK_NAMES = ['CheckBoxAnimatedStateListDrawable$CheckBoxConstantState.smali']
CLASS_ANCHORS = ['.super Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;']

PATCHES = [
    {
        'id': 'miuix_internal_view_CheckBoxAnimatedStateListDrawable__CheckBoxConstantState__newAnimatedStateListDrawable',
        'method': '.method protected newAnimatedStateListDrawable(Landroid/content/res/Resources;Landroid/content/res/Resources$Theme;Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;)Landroid/graphics/drawable/Drawable;',
        'method_name': 'newAnimatedStateListDrawable',
        'method_anchors': ['new-instance p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;', 'invoke-direct {p0, p1, p2, p3}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;-><init>(Landroid/content/res/Resources;Landroid/content/res/Resources$Theme;Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected newAnimatedStateListDrawable(Landroid/content/res/Resources;Landroid/content/res/Resources$Theme;Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;)Landroid/graphics/drawable/Drawable;
    .registers 4

    new-instance p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;

    invoke-direct {p0, p1, p2, p3}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;-><init>(Landroid/content/res/Resources;Landroid/content/res/Resources$Theme;Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;)V

    return-object p0
.end method""",
        'replacement': """.method protected newAnimatedStateListDrawable(Landroid/content/res/Resources;Landroid/content/res/Resources$Theme;Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;)Landroid/graphics/drawable/Drawable;
    .registers 4

    goto :goto_2

    nop

    :goto_0
    invoke-direct {p0, p1, p2, p3}, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;-><init>(Landroid/content/res/Resources;Landroid/content/res/Resources$Theme;Lmiuix/internal/view/CheckWidgetAnimatedStateListDrawable$CheckWidgetConstantState;)V

    goto :goto_1

    nop

    :goto_1
    return-object p0

    :goto_2
    new-instance p0, Lmiuix/internal/view/CheckBoxAnimatedStateListDrawable;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
