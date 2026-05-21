TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/DropDownPreference.smali'
CLASS_FALLBACK_NAMES = ['DropDownPreference.smali']
CLASS_ANCHORS = ['.super Lmiuix/preference/BasePreference;', '.field private static final ADAPTER_CONSTRUCTOR_SIGNATURE:[Ljava/lang/Class;', '.field private static final EMPTY:[Ljava/lang/CharSequence;']

PATCHES = [
    {
        'id': 'miuix_preference_DropDownPreference__createAdapter',
        'method': '.method createAdapter()Landroid/widget/ArrayAdapter;',
        'method_name': 'createAdapter',
        'method_anchors': ['new-instance v0, Lmiuix/appcompat/internal/adapter/SpinnerCheckableArrayAdapter;', 'invoke-virtual {p0}, Landroidx/preference/Preference;->getContext()Landroid/content/Context;', 'iget-object v2, p0, Lmiuix/preference/DropDownPreference;->mContentAdapter:Landroid/widget/ArrayAdapter;', 'new-instance v3, Lmiuix/preference/DropDownPreference$PreferenceCheckedProvider;', 'invoke-direct {v3, p0, v2}, Lmiuix/preference/DropDownPreference$PreferenceCheckedProvider;-><init>(Lmiuix/preference/DropDownPreference;Landroid/widget/ArrayAdapter;)V', 'invoke-direct {v0, v1, v2, v3}, Lmiuix/appcompat/internal/adapter/SpinnerCheckableArrayAdapter;-><init>(Landroid/content/Context;Landroid/widget/ArrayAdapter;Lmiuix/appcompat/internal/adapter/SpinnerCheckableArrayAdapter$CheckedStateProvider;)V', 'return-object v0'],
        'type': 'method_replace',
        'search': """.method createAdapter()Landroid/widget/ArrayAdapter;
    .registers 5

    new-instance v0, Lmiuix/appcompat/internal/adapter/SpinnerCheckableArrayAdapter;

    invoke-virtual {p0}, Landroidx/preference/Preference;->getContext()Landroid/content/Context;

    move-result-object v1

    iget-object v2, p0, Lmiuix/preference/DropDownPreference;->mContentAdapter:Landroid/widget/ArrayAdapter;

    new-instance v3, Lmiuix/preference/DropDownPreference$PreferenceCheckedProvider;

    invoke-direct {v3, p0, v2}, Lmiuix/preference/DropDownPreference$PreferenceCheckedProvider;-><init>(Lmiuix/preference/DropDownPreference;Landroid/widget/ArrayAdapter;)V

    invoke-direct {v0, v1, v2, v3}, Lmiuix/appcompat/internal/adapter/SpinnerCheckableArrayAdapter;-><init>(Landroid/content/Context;Landroid/widget/ArrayAdapter;Lmiuix/appcompat/internal/adapter/SpinnerCheckableArrayAdapter$CheckedStateProvider;)V

    return-object v0
.end method""",
        'replacement': """.method createAdapter()Landroid/widget/ArrayAdapter;
    .registers 5

    goto :goto_2

    nop

    :goto_0
    new-instance v3, Lmiuix/preference/DropDownPreference$PreferenceCheckedProvider;

    goto :goto_4

    nop

    :goto_1
    return-object v0

    :goto_2
    new-instance v0, Lmiuix/appcompat/internal/adapter/SpinnerCheckableArrayAdapter;

    goto :goto_5

    nop

    :goto_3
    iget-object v2, p0, Lmiuix/preference/DropDownPreference;->mContentAdapter:Landroid/widget/ArrayAdapter;

    goto :goto_0

    nop

    :goto_4
    invoke-direct {v3, p0, v2}, Lmiuix/preference/DropDownPreference$PreferenceCheckedProvider;-><init>(Lmiuix/preference/DropDownPreference;Landroid/widget/ArrayAdapter;)V

    goto :goto_6

    nop

    :goto_5
    invoke-virtual {p0}, Landroidx/preference/Preference;->getContext()Landroid/content/Context;

    move-result-object v1

    goto :goto_3

    nop

    :goto_6
    invoke-direct {v0, v1, v2, v3}, Lmiuix/appcompat/internal/adapter/SpinnerCheckableArrayAdapter;-><init>(Landroid/content/Context;Landroid/widget/ArrayAdapter;Lmiuix/appcompat/internal/adapter/SpinnerCheckableArrayAdapter$CheckedStateProvider;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_DropDownPreference__notifyChanged',
        'method': '.method protected notifyChanged()V',
        'method_name': 'notifyChanged',
        'method_anchors': ['invoke-super {p0}, Landroidx/preference/Preference;->notifyChanged()V', 'iget-object v0, p0, Lmiuix/preference/DropDownPreference;->mAdapter:Landroid/widget/ArrayAdapter;', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lmiuix/preference/DropDownPreference;->mNotifyHandler:Landroid/os/Handler;', 'new-instance v1, Lmiuix/preference/DropDownPreference$2;', 'invoke-direct {v1, p0}, Lmiuix/preference/DropDownPreference$2;-><init>(Lmiuix/preference/DropDownPreference;)V', 'invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected notifyChanged()V
    .registers 3

    invoke-super {p0}, Landroidx/preference/Preference;->notifyChanged()V

    iget-object v0, p0, Lmiuix/preference/DropDownPreference;->mAdapter:Landroid/widget/ArrayAdapter;

    if-eqz v0, :cond_0

    iget-object v0, p0, Lmiuix/preference/DropDownPreference;->mNotifyHandler:Landroid/os/Handler;

    new-instance v1, Lmiuix/preference/DropDownPreference$2;

    invoke-direct {v1, p0}, Lmiuix/preference/DropDownPreference$2;-><init>(Lmiuix/preference/DropDownPreference;)V

    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected notifyChanged()V
    .registers 3

    goto :goto_6

    nop

    :goto_0
    iget-object v0, p0, Lmiuix/preference/DropDownPreference;->mAdapter:Landroid/widget/ArrayAdapter;

    goto :goto_4

    nop

    :goto_1
    invoke-direct {v1, p0}, Lmiuix/preference/DropDownPreference$2;-><init>(Lmiuix/preference/DropDownPreference;)V

    goto :goto_7

    nop

    :goto_2
    iget-object v0, p0, Lmiuix/preference/DropDownPreference;->mNotifyHandler:Landroid/os/Handler;

    goto :goto_5

    nop

    :goto_3
    return-void

    :goto_4
    if-nez v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_2

    nop

    :goto_5
    new-instance v1, Lmiuix/preference/DropDownPreference$2;

    goto :goto_1

    nop

    :goto_6
    invoke-super {p0}, Landroidx/preference/Preference;->notifyChanged()V

    goto :goto_0

    nop

    :goto_7
    invoke-virtual {v0, v1}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    :goto_8
    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_DropDownPreference__onGetDefaultValue',
        'method': '.method protected onGetDefaultValue(Landroid/content/res/TypedArray;I)Ljava/lang/Object;',
        'method_name': 'onGetDefaultValue',
        'method_anchors': ['invoke-virtual {p1, p2}, Landroid/content/res/TypedArray;->getString(I)Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected onGetDefaultValue(Landroid/content/res/TypedArray;I)Ljava/lang/Object;
    .registers 3

    invoke-virtual {p1, p2}, Landroid/content/res/TypedArray;->getString(I)Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected onGetDefaultValue(Landroid/content/res/TypedArray;I)Ljava/lang/Object;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p1, p2}, Landroid/content/res/TypedArray;->getString(I)Ljava/lang/String;

    move-result-object p0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_DropDownPreference__onRestoreInstanceState',
        'method': '.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V',
        'method_name': 'onRestoreInstanceState',
        'method_anchors': ['if-eqz p1, :cond_1', 'invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-virtual {v0, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z', 'if-nez v0, :cond_0', 'check-cast p1, Lmiuix/preference/DropDownPreference$SavedState;', 'invoke-virtual {p1}, Landroid/view/AbsSavedState;->getSuperState()Landroid/os/Parcelable;', 'invoke-super {p0, v0}, Landroidx/preference/Preference;->onRestoreInstanceState(Landroid/os/Parcelable;)V', 'iget-object p1, p1, Lmiuix/preference/DropDownPreference$SavedState;->mValue:Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 4

    if-eqz p1, :cond_1

    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    const-class v1, Lmiuix/preference/DropDownPreference$SavedState;

    invoke-virtual {v0, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    check-cast p1, Lmiuix/preference/DropDownPreference$SavedState;

    invoke-virtual {p1}, Landroid/view/AbsSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    invoke-super {p0, v0}, Landroidx/preference/Preference;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    iget-object p1, p1, Lmiuix/preference/DropDownPreference$SavedState;->mValue:Ljava/lang/String;

    invoke-virtual {p0, p1}, Lmiuix/preference/DropDownPreference;->setValue(Ljava/lang/String;)V

    return-void

    :cond_1
    :goto_0
    invoke-super {p0, p1}, Landroidx/preference/Preference;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    return-void
.end method""",
        'replacement': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    if-eqz v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop

    :goto_1
    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    goto :goto_5

    nop

    :goto_2
    if-nez p1, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_1

    nop

    :goto_3
    goto :goto_9

    :goto_4
    goto :goto_6

    nop

    :goto_5
    const-class v1, Lmiuix/preference/DropDownPreference$SavedState;

    goto :goto_7

    nop

    :goto_6
    check-cast p1, Lmiuix/preference/DropDownPreference$SavedState;

    goto :goto_e

    nop

    :goto_7
    invoke-virtual {v0, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    goto :goto_0

    nop

    :goto_8
    return-void

    :goto_9
    goto :goto_c

    nop

    :goto_a
    iget-object p1, p1, Lmiuix/preference/DropDownPreference$SavedState;->mValue:Ljava/lang/String;

    goto :goto_d

    nop

    :goto_b
    return-void

    :goto_c
    invoke-super {p0, p1}, Landroidx/preference/Preference;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_b

    nop

    :goto_d
    invoke-virtual {p0, p1}, Lmiuix/preference/DropDownPreference;->setValue(Ljava/lang/String;)V

    goto :goto_8

    nop

    :goto_e
    invoke-virtual {p1}, Landroid/view/AbsSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_f

    nop

    :goto_f
    invoke-super {p0, v0}, Landroidx/preference/Preference;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_DropDownPreference__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState()Landroid/os/Parcelable;',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['invoke-super {p0}, Landroidx/preference/Preference;->onSaveInstanceState()Landroid/os/Parcelable;', 'invoke-virtual {p0}, Landroidx/preference/Preference;->isPersistent()Z', 'if-eqz v1, :cond_0', 'return-object v0', 'new-instance v1, Lmiuix/preference/DropDownPreference$SavedState;', 'invoke-direct {v1, v0}, Lmiuix/preference/DropDownPreference$SavedState;-><init>(Landroid/os/Parcelable;)V', 'invoke-virtual {p0}, Lmiuix/preference/DropDownPreference;->getValue()Ljava/lang/String;', 'iput-object p0, v1, Lmiuix/preference/DropDownPreference$SavedState;->mValue:Ljava/lang/String;'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 3

    invoke-super {p0}, Landroidx/preference/Preference;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    invoke-virtual {p0}, Landroidx/preference/Preference;->isPersistent()Z

    move-result v1

    if-eqz v1, :cond_0

    return-object v0

    :cond_0
    new-instance v1, Lmiuix/preference/DropDownPreference$SavedState;

    invoke-direct {v1, v0}, Lmiuix/preference/DropDownPreference$SavedState;-><init>(Landroid/os/Parcelable;)V

    invoke-virtual {p0}, Lmiuix/preference/DropDownPreference;->getValue()Ljava/lang/String;

    move-result-object p0

    iput-object p0, v1, Lmiuix/preference/DropDownPreference$SavedState;->mValue:Ljava/lang/String;

    return-object v1
.end method""",
        'replacement': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-direct {v1, v0}, Lmiuix/preference/DropDownPreference$SavedState;-><init>(Landroid/os/Parcelable;)V

    goto :goto_9

    nop

    :goto_1
    new-instance v1, Lmiuix/preference/DropDownPreference$SavedState;

    goto :goto_0

    nop

    :goto_2
    return-object v1

    :goto_3
    invoke-virtual {p0}, Landroidx/preference/Preference;->isPersistent()Z

    move-result v1

    goto :goto_8

    nop

    :goto_4
    return-object v0

    :goto_5
    goto :goto_1

    nop

    :goto_6
    iput-object p0, v1, Lmiuix/preference/DropDownPreference$SavedState;->mValue:Ljava/lang/String;

    goto :goto_2

    nop

    :goto_7
    invoke-super {p0}, Landroidx/preference/Preference;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_3

    nop

    :goto_8
    if-nez v1, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_4

    nop

    :goto_9
    invoke-virtual {p0}, Lmiuix/preference/DropDownPreference;->getValue()Ljava/lang/String;

    move-result-object p0

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_DropDownPreference__onSetInitialValue',
        'method': '.method protected onSetInitialValue(Ljava/lang/Object;)V',
        'method_name': 'onSetInitialValue',
        'method_anchors': ['check-cast p1, Ljava/lang/String;', 'invoke-virtual {p0, p1}, Landroidx/preference/Preference;->getPersistedString(Ljava/lang/String;)Ljava/lang/String;', 'invoke-virtual {p0, p1}, Lmiuix/preference/DropDownPreference;->setValue(Ljava/lang/String;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onSetInitialValue(Ljava/lang/Object;)V
    .registers 2

    check-cast p1, Ljava/lang/String;

    invoke-virtual {p0, p1}, Landroidx/preference/Preference;->getPersistedString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p0, p1}, Lmiuix/preference/DropDownPreference;->setValue(Ljava/lang/String;)V

    return-void
.end method""",
        'replacement': """.method protected onSetInitialValue(Ljava/lang/Object;)V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroidx/preference/Preference;->getPersistedString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    goto :goto_3

    nop

    :goto_1
    return-void

    :goto_2
    check-cast p1, Ljava/lang/String;

    goto :goto_0

    nop

    :goto_3
    invoke-virtual {p0, p1}, Lmiuix/preference/DropDownPreference;->setValue(Ljava/lang/String;)V

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_DropDownPreference__performClick',
        'method': '.method protected performClick(Landroid/view/View;)V',
        'method_name': 'performClick',
        'method_anchors': ['iget-object p0, p0, Lmiuix/preference/DropDownPreference;->mSpinner:Lmiuix/appcompat/widget/Spinner;', 'if-eqz p0, :cond_0', 'invoke-virtual {p0}, Lmiuix/appcompat/widget/Spinner;->performClick()Z', 'const-string p0, "DropDownPreference"', 'const-string p1, "trigger from perform click"', 'invoke-static {p0, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected performClick(Landroid/view/View;)V
    .registers 2

    iget-object p0, p0, Lmiuix/preference/DropDownPreference;->mSpinner:Lmiuix/appcompat/widget/Spinner;

    if-eqz p0, :cond_0

    invoke-virtual {p0}, Lmiuix/appcompat/widget/Spinner;->performClick()Z

    const-string p0, "DropDownPreference"

    const-string p1, "trigger from perform click"

    invoke-static {p0, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected performClick(Landroid/view/View;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    if-nez p0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_3

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/preference/DropDownPreference;->mSpinner:Lmiuix/appcompat/widget/Spinner;

    goto :goto_0

    nop

    :goto_2
    return-void

    :goto_3
    invoke-virtual {p0}, Lmiuix/appcompat/widget/Spinner;->performClick()Z

    goto :goto_6

    nop

    :goto_4
    invoke-static {p0, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_5
    goto :goto_2

    nop

    :goto_6
    const-string p0, "DropDownPreference"

    goto :goto_7

    nop

    :goto_7
    const-string p1, "trigger from perform click"

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
