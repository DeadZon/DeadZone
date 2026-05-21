TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/MultiChoicePreferenceCategory.smali'
CLASS_FALLBACK_NAMES = ['MultiChoicePreferenceCategory.smali']
CLASS_ANCHORS = ['.super Landroidx/preference/PreferenceCategory;']

PATCHES = [
    {
        'id': 'miuix_preference_MultiChoicePreferenceCategory__onRestoreInstanceState',
        'method': '.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V',
        'method_name': 'onRestoreInstanceState',
        'method_anchors': ['if-eqz p1, :cond_1', 'invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;', 'invoke-virtual {v0, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z', 'if-nez v0, :cond_0', 'check-cast p1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;', 'invoke-virtual {p1}, Landroid/view/AbsSavedState;->getSuperState()Landroid/os/Parcelable;', 'invoke-super {p0, v0}, Landroidx/preference/PreferenceGroup;->onRestoreInstanceState(Landroid/os/Parcelable;)V', 'iget-object p1, p1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;->mValues:Ljava/util/Set;'],
        'type': 'method_replace',
        'search': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 4

    if-eqz p1, :cond_1

    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    const-class v1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;

    invoke-virtual {v0, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    check-cast p1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;

    invoke-virtual {p1}, Landroid/view/AbsSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    invoke-super {p0, v0}, Landroidx/preference/PreferenceGroup;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    iget-object p1, p1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;->mValues:Ljava/util/Set;

    invoke-virtual {p0, p1}, Lmiuix/preference/MultiChoicePreferenceCategory;->setValues(Ljava/util/Set;)V

    return-void

    :cond_1
    :goto_0
    invoke-super {p0, p1}, Landroidx/preference/PreferenceGroup;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    return-void
.end method""",
        'replacement': """.method protected onRestoreInstanceState(Landroid/os/Parcelable;)V
    .registers 4

    goto :goto_b

    nop

    :goto_0
    if-eqz v0, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_6

    nop

    :goto_1
    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v0

    goto :goto_a

    nop

    :goto_2
    return-void

    :goto_3
    goto :goto_9

    nop

    :goto_4
    invoke-virtual {v0, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    goto :goto_0

    nop

    :goto_5
    iget-object p1, p1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;->mValues:Ljava/util/Set;

    goto :goto_8

    nop

    :goto_6
    goto :goto_3

    :goto_7
    goto :goto_c

    nop

    :goto_8
    invoke-virtual {p0, p1}, Lmiuix/preference/MultiChoicePreferenceCategory;->setValues(Ljava/util/Set;)V

    goto :goto_2

    nop

    :goto_9
    invoke-super {p0, p1}, Landroidx/preference/PreferenceGroup;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_d

    nop

    :goto_a
    const-class v1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;

    goto :goto_4

    nop

    :goto_b
    if-nez p1, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_1

    nop

    :goto_c
    check-cast p1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;

    goto :goto_f

    nop

    :goto_d
    return-void

    :goto_e
    invoke-super {p0, v0}, Landroidx/preference/PreferenceGroup;->onRestoreInstanceState(Landroid/os/Parcelable;)V

    goto :goto_5

    nop

    :goto_f
    invoke-virtual {p1}, Landroid/view/AbsSavedState;->getSuperState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_e

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_MultiChoicePreferenceCategory__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState()Landroid/os/Parcelable;',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['invoke-super {p0}, Landroidx/preference/PreferenceGroup;->onSaveInstanceState()Landroid/os/Parcelable;', 'invoke-virtual {p0}, Landroidx/preference/Preference;->isPersistent()Z', 'if-eqz v1, :cond_0', 'return-object v0', 'new-instance v1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;', 'invoke-direct {v1, v0}, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;-><init>(Landroid/os/Parcelable;)V', 'invoke-virtual {p0}, Lmiuix/preference/MultiChoicePreferenceCategory;->getValues()Ljava/util/Set;', 'iput-object p0, v1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;->mValues:Ljava/util/Set;'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 3

    invoke-super {p0}, Landroidx/preference/PreferenceGroup;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    invoke-virtual {p0}, Landroidx/preference/Preference;->isPersistent()Z

    move-result v1

    if-eqz v1, :cond_0

    return-object v0

    :cond_0
    new-instance v1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;

    invoke-direct {v1, v0}, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;-><init>(Landroid/os/Parcelable;)V

    invoke-virtual {p0}, Lmiuix/preference/MultiChoicePreferenceCategory;->getValues()Ljava/util/Set;

    move-result-object p0

    iput-object p0, v1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;->mValues:Ljava/util/Set;

    return-object v1
.end method""",
        'replacement': """.method protected onSaveInstanceState()Landroid/os/Parcelable;
    .registers 3

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {p0}, Landroidx/preference/Preference;->isPersistent()Z

    move-result v1

    goto :goto_4

    nop

    :goto_1
    return-object v0

    :goto_2
    goto :goto_8

    nop

    :goto_3
    invoke-super {p0}, Landroidx/preference/PreferenceGroup;->onSaveInstanceState()Landroid/os/Parcelable;

    move-result-object v0

    goto :goto_0

    nop

    :goto_4
    if-nez v1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_5
    invoke-direct {v1, v0}, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;-><init>(Landroid/os/Parcelable;)V

    goto :goto_7

    nop

    :goto_6
    iput-object p0, v1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;->mValues:Ljava/util/Set;

    goto :goto_9

    nop

    :goto_7
    invoke-virtual {p0}, Lmiuix/preference/MultiChoicePreferenceCategory;->getValues()Ljava/util/Set;

    move-result-object p0

    goto :goto_6

    nop

    :goto_8
    new-instance v1, Lmiuix/preference/MultiChoicePreferenceCategory$SavedState;

    goto :goto_5

    nop

    :goto_9
    return-object v1
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_MultiChoicePreferenceCategory__onSetInitialValue',
        'method': '.method protected onSetInitialValue(Ljava/lang/Object;)V',
        'method_name': 'onSetInitialValue',
        'method_anchors': ['check-cast p1, Ljava/util/Set;', 'invoke-virtual {p0, p1}, Landroidx/preference/Preference;->getPersistedStringSet(Ljava/util/Set;)Ljava/util/Set;', 'invoke-virtual {p0, p1}, Lmiuix/preference/MultiChoicePreferenceCategory;->setValues(Ljava/util/Set;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onSetInitialValue(Ljava/lang/Object;)V
    .registers 2

    check-cast p1, Ljava/util/Set;

    invoke-virtual {p0, p1}, Landroidx/preference/Preference;->getPersistedStringSet(Ljava/util/Set;)Ljava/util/Set;

    move-result-object p1

    invoke-virtual {p0, p1}, Lmiuix/preference/MultiChoicePreferenceCategory;->setValues(Ljava/util/Set;)V

    return-void
.end method""",
        'replacement': """.method protected onSetInitialValue(Ljava/lang/Object;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    check-cast p1, Ljava/util/Set;

    goto :goto_3

    nop

    :goto_1
    return-void

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/preference/MultiChoicePreferenceCategory;->setValues(Ljava/util/Set;)V

    goto :goto_1

    nop

    :goto_3
    invoke-virtual {p0, p1}, Landroidx/preference/Preference;->getPersistedStringSet(Ljava/util/Set;)Ljava/util/Set;

    move-result-object p1

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
