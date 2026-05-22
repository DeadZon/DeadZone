TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/SingleChoicePreferenceCategory.smali'
CLASS_FALLBACK_NAMES = ['SingleChoicePreferenceCategory.smali']
CLASS_ANCHORS = ['.super Landroidx/preference/PreferenceCategory;']

PATCHES = [
    {
        'id': 'miuix_preference_SingleChoicePreferenceCategory__onSetInitialValue',
        'method': '.method protected onSetInitialValue(Ljava/lang/Object;)V',
        'method_name': 'onSetInitialValue',
        'method_anchors': ['check-cast p1, Ljava/lang/String;', 'invoke-virtual {p0, p1}, Landroidx/preference/Preference;->getPersistedString(Ljava/lang/String;)Ljava/lang/String;', 'invoke-virtual {p0, p1}, Lmiuix/preference/SingleChoicePreferenceCategory;->setValue(Ljava/lang/String;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onSetInitialValue(Ljava/lang/Object;)V
    .registers 2

    check-cast p1, Ljava/lang/String;

    invoke-virtual {p0, p1}, Landroidx/preference/Preference;->getPersistedString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    invoke-virtual {p0, p1}, Lmiuix/preference/SingleChoicePreferenceCategory;->setValue(Ljava/lang/String;)V

    return-void
.end method""",
        'replacement': """.method protected onSetInitialValue(Ljava/lang/Object;)V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0, p1}, Landroidx/preference/Preference;->getPersistedString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object p1

    goto :goto_2

    nop

    :goto_1
    check-cast p1, Ljava/lang/String;

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0, p1}, Lmiuix/preference/SingleChoicePreferenceCategory;->setValue(Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_3
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
