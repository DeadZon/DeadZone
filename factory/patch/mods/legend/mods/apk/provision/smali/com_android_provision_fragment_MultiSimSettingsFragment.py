TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/MultiSimSettingsFragment.smali'
CLASS_FALLBACK_NAMES = ['MultiSimSettingsFragment.smali']
CLASS_ANCHORS = ['.super Lmiuix/preference/PreferenceFragment;', '.implements Landroidx/preference/Preference$OnPreferenceChangeListener;', '.field private static final DELAY_SWITCH_SIM:I = 0x4', '.field private static final MULTISIM_CLOSE_DIALOG:I = 0x3', '.field private static final PREF_KEY_DATA_SLOT:Ljava/lang/String; = "pref_key_voice_data"', '.field private static final PREF_KEY_VOICE_SLOT:Ljava/lang/String; = "pref_key_multi_sim"']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_MultiSimSettingsFragment__getListViewPaddingBottom',
        'method': '.method protected getListViewPaddingBottom()I',
        'method_name': 'getListViewPaddingBottom',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getListViewPaddingBottom()I
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected getListViewPaddingBottom()I
    .registers 1

    goto :goto_0

    nop

    :goto_0
    const/4 p0, 0x0

    goto :goto_1

    nop

    :goto_1
    return p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_MultiSimSettingsFragment__getListViewPaddingTop',
        'method': '.method protected getListViewPaddingTop()I',
        'method_name': 'getListViewPaddingTop',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected getListViewPaddingTop()I
    .registers 1

    const/4 p0, 0x0

    return p0
.end method""",
        'replacement': """.method protected getListViewPaddingTop()I
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/4 p0, 0x0

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
