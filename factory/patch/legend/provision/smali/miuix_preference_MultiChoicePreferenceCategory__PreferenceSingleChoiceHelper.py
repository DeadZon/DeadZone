TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper.smali'
CLASS_FALLBACK_NAMES = ['MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper.smali']
CLASS_ANCHORS = ['.super Lmiuix/preference/MultiChoicePreferenceCategory$MultiChoiceHelper;']

PATCHES = [
    {
        'id': 'miuix_preference_MultiChoicePreferenceCategory__PreferenceSingleChoiceHelper__getPreference',
        'method': '.method getPreference()Landroidx/preference/Preference;',
        'method_name': 'getPreference',
        'method_anchors': ['iget-object p0, p0, Lmiuix/preference/MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper;->mPreference:Lmiuix/preference/MultiChoicePreference;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getPreference()Landroidx/preference/Preference;
    .registers 1

    iget-object p0, p0, Lmiuix/preference/MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper;->mPreference:Lmiuix/preference/MultiChoicePreference;

    return-object p0
.end method""",
        'replacement': """.method getPreference()Landroidx/preference/Preference;
    .registers 1

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/preference/MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper;->mPreference:Lmiuix/preference/MultiChoicePreference;

    goto :goto_1

    nop

    :goto_1
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_MultiChoicePreferenceCategory__PreferenceSingleChoiceHelper__getValue',
        'method': '.method getValue()Ljava/lang/String;',
        'method_name': 'getValue',
        'method_anchors': ['iget-object p0, p0, Lmiuix/preference/MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper;->mPreference:Lmiuix/preference/MultiChoicePreference;', 'invoke-virtual {p0}, Lmiuix/preference/MultiChoicePreference;->getValue()Ljava/lang/String;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method getValue()Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lmiuix/preference/MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper;->mPreference:Lmiuix/preference/MultiChoicePreference;

    invoke-virtual {p0}, Lmiuix/preference/MultiChoicePreference;->getValue()Ljava/lang/String;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method getValue()Ljava/lang/String;
    .registers 1

    goto :goto_2

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-virtual {p0}, Lmiuix/preference/MultiChoicePreference;->getValue()Ljava/lang/String;

    move-result-object p0

    goto :goto_0

    nop

    :goto_2
    iget-object p0, p0, Lmiuix/preference/MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper;->mPreference:Lmiuix/preference/MultiChoicePreference;

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_MultiChoicePreferenceCategory__PreferenceSingleChoiceHelper__setOnPreferenceChangeInternalListener',
        'method': '.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V',
        'method_name': 'setOnPreferenceChangeInternalListener',
        'method_anchors': ['iget-object p0, p0, Lmiuix/preference/MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper;->mPreference:Lmiuix/preference/MultiChoicePreference;', 'invoke-virtual {p0, p1}, Lmiuix/preference/MultiChoicePreference;->setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V
    .registers 2

    iget-object p0, p0, Lmiuix/preference/MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper;->mPreference:Lmiuix/preference/MultiChoicePreference;

    invoke-virtual {p0, p1}, Lmiuix/preference/MultiChoicePreference;->setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V

    return-void
.end method""",
        'replacement': """.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object p0, p0, Lmiuix/preference/MultiChoicePreferenceCategory$PreferenceSingleChoiceHelper;->mPreference:Lmiuix/preference/MultiChoicePreference;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lmiuix/preference/MultiChoicePreference;->setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V

    goto :goto_2

    nop

    :goto_2
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
