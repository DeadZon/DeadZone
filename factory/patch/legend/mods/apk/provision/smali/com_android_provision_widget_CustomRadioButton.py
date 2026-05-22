TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/widget/CustomRadioButton.smali'
CLASS_FALLBACK_NAMES = ['CustomRadioButton.smali']
CLASS_ANCHORS = ['.super Landroid/widget/RadioButton;']

PATCHES = [
    {
        'id': 'com_android_provision_widget_CustomRadioButton__onFocusChanged',
        'method': '.method protected onFocusChanged(ZILandroid/graphics/Rect;)V',
        'method_name': 'onFocusChanged',
        'method_anchors': ['if-eqz p1, :cond_0', 'invoke-super {p0, p1, p2, p3}, Landroid/widget/RadioButton;->onFocusChanged(ZILandroid/graphics/Rect;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onFocusChanged(ZILandroid/graphics/Rect;)V
    .registers 4

    if-eqz p1, :cond_0

    invoke-super {p0, p1, p2, p3}, Landroid/widget/RadioButton;->onFocusChanged(ZILandroid/graphics/Rect;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onFocusChanged(ZILandroid/graphics/Rect;)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    if-nez p1, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_2

    nop

    :goto_2
    invoke-super {p0, p1, p2, p3}, Landroid/widget/RadioButton;->onFocusChanged(ZILandroid/graphics/Rect;)V

    :goto_3
    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
