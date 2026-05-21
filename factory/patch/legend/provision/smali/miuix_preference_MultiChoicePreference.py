TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/MultiChoicePreference.smali'
CLASS_FALLBACK_NAMES = ['MultiChoicePreference.smali']
CLASS_ANCHORS = ['.super Lmiuix/preference/BaseCheckBoxPreference;', '.implements Landroid/widget/Checkable;']

PATCHES = [
    {
        'id': 'miuix_preference_MultiChoicePreference__notifyChanged',
        'method': '.method protected notifyChanged()V',
        'method_name': 'notifyChanged',
        'method_anchors': ['invoke-super {p0}, Landroidx/preference/Preference;->notifyChanged()V', 'iget-object v0, p0, Lmiuix/preference/MultiChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;', 'if-eqz v0, :cond_0', 'invoke-interface {v0, p0}, Lmiuix/preference/OnPreferenceChangeInternalListener;->notifyPreferenceChangeInternal(Landroidx/preference/Preference;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected notifyChanged()V
    .registers 2

    invoke-super {p0}, Landroidx/preference/Preference;->notifyChanged()V

    iget-object v0, p0, Lmiuix/preference/MultiChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;

    if-eqz v0, :cond_0

    invoke-interface {v0, p0}, Lmiuix/preference/OnPreferenceChangeInternalListener;->notifyPreferenceChangeInternal(Landroidx/preference/Preference;)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected notifyChanged()V
    .registers 2

    goto :goto_3

    nop

    :goto_0
    return-void

    :goto_1
    invoke-interface {v0, p0}, Lmiuix/preference/OnPreferenceChangeInternalListener;->notifyPreferenceChangeInternal(Landroidx/preference/Preference;)V

    :goto_2
    goto :goto_0

    nop

    :goto_3
    invoke-super {p0}, Landroidx/preference/Preference;->notifyChanged()V

    goto :goto_5

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_5
    iget-object v0, p0, Lmiuix/preference/MultiChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_MultiChoicePreference__onClick',
        'method': '.method protected onClick()V',
        'method_name': 'onClick',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/preference/MultiChoicePreference;->mChangeFromClick:Z', 'invoke-super {p0}, Landroidx/preference/TwoStatePreference;->onClick()V', 'iget-boolean v0, p0, Lmiuix/preference/MultiChoicePreference;->mChangeFromClick:Z', 'if-eqz v0, :cond_0', 'iget-object p0, p0, Lmiuix/preference/MultiChoicePreference;->mItemView:Landroid/view/View;', 'if-eqz p0, :cond_0', 'sget v0, Lmiuix/view/HapticFeedbackConstants;->MIUI_BUTTON_SMALL:I', 'sget v1, Lmiuix/view/HapticFeedbackConstants;->MIUI_TAP_NORMAL:I'],
        'type': 'method_replace',
        'search': """.method protected onClick()V
    .registers 3

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/preference/MultiChoicePreference;->mChangeFromClick:Z

    invoke-super {p0}, Landroidx/preference/TwoStatePreference;->onClick()V

    iget-boolean v0, p0, Lmiuix/preference/MultiChoicePreference;->mChangeFromClick:Z

    if-eqz v0, :cond_0

    iget-object p0, p0, Lmiuix/preference/MultiChoicePreference;->mItemView:Landroid/view/View;

    if-eqz p0, :cond_0

    sget v0, Lmiuix/view/HapticFeedbackConstants;->MIUI_BUTTON_SMALL:I

    sget v1, Lmiuix/view/HapticFeedbackConstants;->MIUI_TAP_NORMAL:I

    invoke-static {p0, v0, v1}, Lmiuix/view/HapticCompat;->performHapticFeedbackAsync(Landroid/view/View;II)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onClick()V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_8

    nop

    :goto_1
    sget v0, Lmiuix/view/HapticFeedbackConstants;->MIUI_BUTTON_SMALL:I

    goto :goto_2

    nop

    :goto_2
    sget v1, Lmiuix/view/HapticFeedbackConstants;->MIUI_TAP_NORMAL:I

    goto :goto_6

    nop

    :goto_3
    if-nez p0, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_1

    nop

    :goto_4
    const/4 v0, 0x1

    goto :goto_b

    nop

    :goto_5
    iget-boolean v0, p0, Lmiuix/preference/MultiChoicePreference;->mChangeFromClick:Z

    goto :goto_0

    nop

    :goto_6
    invoke-static {p0, v0, v1}, Lmiuix/view/HapticCompat;->performHapticFeedbackAsync(Landroid/view/View;II)V

    :goto_7
    goto :goto_9

    nop

    :goto_8
    iget-object p0, p0, Lmiuix/preference/MultiChoicePreference;->mItemView:Landroid/view/View;

    goto :goto_3

    nop

    :goto_9
    return-void

    :goto_a
    invoke-super {p0}, Landroidx/preference/TwoStatePreference;->onClick()V

    goto :goto_5

    nop

    :goto_b
    iput-boolean v0, p0, Lmiuix/preference/MultiChoicePreference;->mChangeFromClick:Z

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_MultiChoicePreference__setOnPreferenceChangeInternalListener',
        'method': '.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V',
        'method_name': 'setOnPreferenceChangeInternalListener',
        'method_anchors': ['iput-object p1, p0, Lmiuix/preference/MultiChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V
    .registers 2

    iput-object p1, p0, Lmiuix/preference/MultiChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;

    return-void
.end method""",
        'replacement': """.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-object p1, p0, Lmiuix/preference/MultiChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
