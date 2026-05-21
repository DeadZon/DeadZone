TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/RadioSetPreferenceCategory.smali'
CLASS_FALLBACK_NAMES = ['RadioSetPreferenceCategory.smali']
CLASS_ANCHORS = ['.super Landroidx/preference/PreferenceCategory;', '.implements Landroid/widget/Checkable;']

PATCHES = [
    {
        'id': 'miuix_preference_RadioSetPreferenceCategory__setOnPreferenceChangeInternalListener',
        'method': '.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V',
        'method_name': 'setOnPreferenceChangeInternalListener',
        'method_anchors': ['iput-object p1, p0, Lmiuix/preference/RadioSetPreferenceCategory;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;', 'return-void'],
        'type': 'method_replace',
        'search': """.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V
    .registers 2

    iput-object p1, p0, Lmiuix/preference/RadioSetPreferenceCategory;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;

    return-void
.end method""",
        'replacement': """.method setOnPreferenceChangeInternalListener(Lmiuix/preference/OnPreferenceChangeInternalListener;)V
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iput-object p1, p0, Lmiuix/preference/RadioSetPreferenceCategory;->mInternalListener:Lmiuix/preference/OnPreferenceChangeInternalListener;

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
