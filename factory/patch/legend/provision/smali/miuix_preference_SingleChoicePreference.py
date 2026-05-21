TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/SingleChoicePreference.smali'
CLASS_FALLBACK_NAMES = ['SingleChoicePreference.smali']
CLASS_ANCHORS = ['.super Lmiuix/preference/BaseCheckBoxPreference;', '.implements Landroid/widget/Checkable;', '.implements Lmiuix/preference/FolmeAnimationController;', '.implements Lmiuix/preference/PreferenceExtraPadding;']

PATCHES = [
    {
        'id': 'miuix_preference_SingleChoicePreference__notifyChanged',
        'method': '.method protected notifyChanged()V',
        'method_name': 'notifyChanged',
        'method_anchors': ['invoke-super {p0}, Landroidx/preference/Preference;->notifyChanged()V', 'iget v0, p0, Lmiuix/preference/SingleChoicePreference;->mClicked:I', 'if-lez v0, :cond_0', 'iput v0, p0, Lmiuix/preference/SingleChoicePreference;->mClicked:I', 'iput-boolean v1, p0, Lmiuix/preference/SingleChoicePreference;->mIsNotifyChanged:Z', 'iget-object v0, p0, Lmiuix/preference/SingleChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;', 'if-eqz v0, :cond_1', 'invoke-interface {v0, p0}, Lmiuix/preference/OnPreferenceChangeInternalListener;->notifyPreferenceChangeInternal(Landroidx/preference/Preference;)V'],
        'type': 'method_replace',
        'search': """.method protected notifyChanged()V
    .registers 3

    invoke-super {p0}, Landroidx/preference/Preference;->notifyChanged()V

    iget v0, p0, Lmiuix/preference/SingleChoicePreference;->mClicked:I

    const/4 v1, 0x1

    if-lez v0, :cond_0

    sub-int/2addr v0, v1

    iput v0, p0, Lmiuix/preference/SingleChoicePreference;->mClicked:I

    :cond_0
    iput-boolean v1, p0, Lmiuix/preference/SingleChoicePreference;->mIsNotifyChanged:Z

    iget-object v0, p0, Lmiuix/preference/SingleChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;

    if-eqz v0, :cond_1

    invoke-interface {v0, p0}, Lmiuix/preference/OnPreferenceChangeInternalListener;->notifyPreferenceChangeInternal(Landroidx/preference/Preference;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected notifyChanged()V
    .registers 3

    goto :goto_8

    nop

    :goto_0
    if-gtz v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_a

    nop

    :goto_1
    invoke-interface {v0, p0}, Lmiuix/preference/OnPreferenceChangeInternalListener;->notifyPreferenceChangeInternal(Landroidx/preference/Preference;)V

    :goto_2
    goto :goto_5

    nop

    :goto_3
    iput v0, p0, Lmiuix/preference/SingleChoicePreference;->mClicked:I

    :goto_4
    goto :goto_6

    nop

    :goto_5
    return-void

    :goto_6
    iput-boolean v1, p0, Lmiuix/preference/SingleChoicePreference;->mIsNotifyChanged:Z

    goto :goto_9

    nop

    :goto_7
    const/4 v1, 0x1

    goto :goto_0

    nop

    :goto_8
    invoke-super {p0}, Landroidx/preference/Preference;->notifyChanged()V

    goto :goto_c

    nop

    :goto_9
    iget-object v0, p0, Lmiuix/preference/SingleChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;

    goto :goto_b

    nop

    :goto_a
    sub-int/2addr v0, v1

    goto :goto_3

    nop

    :goto_b
    if-nez v0, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_1

    nop

    :goto_c
    iget v0, p0, Lmiuix/preference/SingleChoicePreference;->mClicked:I

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_SingleChoicePreference__onClick',
        'method': '.method protected onClick()V',
        'method_name': 'onClick',
        'method_anchors': ['iput-boolean v0, p0, Lmiuix/preference/SingleChoicePreference;->mChangeFromClick:Z', 'iput v0, p0, Lmiuix/preference/SingleChoicePreference;->mClicked:I', 'iput-boolean v0, p0, Lmiuix/preference/SingleChoicePreference;->mIsInit:Z', 'invoke-super {p0}, Landroidx/preference/TwoStatePreference;->onClick()V', 'iget-boolean v0, p0, Lmiuix/preference/SingleChoicePreference;->mChangeFromClick:Z', 'if-eqz v0, :cond_0', 'iget-object p0, p0, Lmiuix/preference/SingleChoicePreference;->mItemView:Landroid/view/View;', 'if-eqz p0, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onClick()V
    .registers 3

    const/4 v0, 0x1

    iput-boolean v0, p0, Lmiuix/preference/SingleChoicePreference;->mChangeFromClick:Z

    const/4 v0, 0x2

    iput v0, p0, Lmiuix/preference/SingleChoicePreference;->mClicked:I

    const/4 v0, 0x0

    iput-boolean v0, p0, Lmiuix/preference/SingleChoicePreference;->mIsInit:Z

    invoke-super {p0}, Landroidx/preference/TwoStatePreference;->onClick()V

    iget-boolean v0, p0, Lmiuix/preference/SingleChoicePreference;->mChangeFromClick:Z

    if-eqz v0, :cond_0

    iget-object p0, p0, Lmiuix/preference/SingleChoicePreference;->mItemView:Landroid/view/View;

    if-eqz p0, :cond_0

    sget v0, Lmiuix/view/HapticFeedbackConstants;->MIUI_BUTTON_SMALL:I

    sget v1, Lmiuix/view/HapticFeedbackConstants;->MIUI_TAP_NORMAL:I

    invoke-static {p0, v0, v1}, Lmiuix/view/HapticCompat;->performHapticFeedbackAsync(Landroid/view/View;II)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onClick()V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    sget v1, Lmiuix/view/HapticFeedbackConstants;->MIUI_TAP_NORMAL:I

    goto :goto_3

    nop

    :goto_1
    sget v0, Lmiuix/view/HapticFeedbackConstants;->MIUI_BUTTON_SMALL:I

    goto :goto_0

    nop

    :goto_2
    invoke-super {p0}, Landroidx/preference/TwoStatePreference;->onClick()V

    goto :goto_d

    nop

    :goto_3
    invoke-static {p0, v0, v1}, Lmiuix/view/HapticCompat;->performHapticFeedbackAsync(Landroid/view/View;II)V

    :goto_4
    goto :goto_8

    nop

    :goto_5
    const/4 v0, 0x1

    goto :goto_c

    nop

    :goto_6
    if-nez v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_9

    nop

    :goto_7
    const/4 v0, 0x0

    goto :goto_e

    nop

    :goto_8
    return-void

    :goto_9
    iget-object p0, p0, Lmiuix/preference/SingleChoicePreference;->mItemView:Landroid/view/View;

    goto :goto_b

    nop

    :goto_a
    const/4 v0, 0x2

    goto :goto_f

    nop

    :goto_b
    if-nez p0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_1

    nop

    :goto_c
    iput-boolean v0, p0, Lmiuix/preference/SingleChoicePreference;->mChangeFromClick:Z

    goto :goto_a

    nop

    :goto_d
    iget-boolean v0, p0, Lmiuix/preference/SingleChoicePreference;->mChangeFromClick:Z

    goto :goto_6

    nop

    :goto_e
    iput-boolean v0, p0, Lmiuix/preference/SingleChoicePreference;->mIsInit:Z

    goto :goto_2

    nop

    :goto_f
    iput v0, p0, Lmiuix/preference/SingleChoicePreference;->mClicked:I

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_SingleChoicePreference__setOnPreferenceChangeInternalListener',
        'method': '.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V',
        'method_name': 'setOnPreferenceChangeInternalListener',
        'method_anchors': ['iput-object p1, p0, Lmiuix/preference/SingleChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V
    .registers 2

    iput-object p1, p0, Lmiuix/preference/SingleChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;

    return-void
.end method""",
        'replacement': """.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iput-object p1, p0, Lmiuix/preference/SingleChoicePreference;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
