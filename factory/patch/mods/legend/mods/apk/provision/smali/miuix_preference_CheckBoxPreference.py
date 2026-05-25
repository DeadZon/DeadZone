TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/CheckBoxPreference.smali'
CLASS_FALLBACK_NAMES = ['CheckBoxPreference.smali']
CLASS_ANCHORS = ['.super Lmiuix/preference/BaseCheckBoxPreference;']

PATCHES = [
    {
        'id': 'miuix_preference_CheckBoxPreference__onClick',
        'method': '.method protected onClick()V',
        'method_name': 'onClick',
        'method_anchors': ['invoke-super {p0}, Landroidx/preference/TwoStatePreference;->onClick()V', 'iget-object p0, p0, Lmiuix/preference/CheckBoxPreference;->mItemView:Landroid/view/View;', 'if-eqz p0, :cond_0', 'sget v0, Lmiuix/view/HapticFeedbackConstants;->MIUI_BUTTON_SMALL:I', 'sget v1, Lmiuix/view/HapticFeedbackConstants;->MIUI_TAP_NORMAL:I', 'invoke-static {p0, v0, v1}, Lmiuix/view/HapticCompat;->performHapticFeedback(Landroid/view/View;II)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onClick()V
    .registers 3

    invoke-super {p0}, Landroidx/preference/TwoStatePreference;->onClick()V

    iget-object p0, p0, Lmiuix/preference/CheckBoxPreference;->mItemView:Landroid/view/View;

    if-eqz p0, :cond_0

    sget v0, Lmiuix/view/HapticFeedbackConstants;->MIUI_BUTTON_SMALL:I

    sget v1, Lmiuix/view/HapticFeedbackConstants;->MIUI_TAP_NORMAL:I

    invoke-static {p0, v0, v1}, Lmiuix/view/HapticCompat;->performHapticFeedback(Landroid/view/View;II)Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onClick()V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/preference/CheckBoxPreference;->mItemView:Landroid/view/View;

    goto :goto_3

    nop

    :goto_1
    invoke-static {p0, v0, v1}, Lmiuix/view/HapticCompat;->performHapticFeedback(Landroid/view/View;II)Z

    :goto_2
    goto :goto_6

    nop

    :goto_3
    if-nez p0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_7

    nop

    :goto_4
    invoke-super {p0}, Landroidx/preference/TwoStatePreference;->onClick()V

    goto :goto_0

    nop

    :goto_5
    sget v1, Lmiuix/view/HapticFeedbackConstants;->MIUI_TAP_NORMAL:I

    goto :goto_1

    nop

    :goto_6
    return-void

    :goto_7
    sget v0, Lmiuix/view/HapticFeedbackConstants;->MIUI_BUTTON_SMALL:I

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
