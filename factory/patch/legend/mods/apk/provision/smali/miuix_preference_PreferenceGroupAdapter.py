TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/PreferenceGroupAdapter.smali'
CLASS_FALLBACK_NAMES = ['PreferenceGroupAdapter.smali']
CLASS_ANCHORS = ['.super Landroidx/preference/PreferenceGroupAdapter;', '.implements Lmiuix/animation/internal/BlinkStateObserver;', '.implements Lmiuix/container/ExtraPaddingObserver;', '.field private static final STATES_TAGS:[I', '.field private static final STATE_SET_FIRST:[I', '.field private static final STATE_SET_LAST:[I']

PATCHES = [
    {
        'id': 'miuix_preference_PreferenceGroupAdapter__getPositionType',
        'method': '.method getPositionType(I)I',
        'method_name': 'getPositionType',
        'method_anchors': ['iget-object p0, p0, Lmiuix/preference/PreferenceGroupAdapter;->mDescriptors:[Lmiuix/preference/PreferenceGroupAdapter$PositionDescriptor;', 'iget p0, p0, Lmiuix/preference/PreferenceGroupAdapter$PositionDescriptor;->type:I', 'return p0'],
        'type': 'method_replace',
        'search': """.method getPositionType(I)I
    .registers 2

    iget-object p0, p0, Lmiuix/preference/PreferenceGroupAdapter;->mDescriptors:[Lmiuix/preference/PreferenceGroupAdapter$PositionDescriptor;

    aget-object p0, p0, p1

    iget p0, p0, Lmiuix/preference/PreferenceGroupAdapter$PositionDescriptor;->type:I

    return p0
.end method""",
        'replacement': """.method getPositionType(I)I
    .registers 2

    goto :goto_1

    nop

    :goto_0
    iget p0, p0, Lmiuix/preference/PreferenceGroupAdapter$PositionDescriptor;->type:I

    goto :goto_2

    nop

    :goto_1
    iget-object p0, p0, Lmiuix/preference/PreferenceGroupAdapter;->mDescriptors:[Lmiuix/preference/PreferenceGroupAdapter$PositionDescriptor;

    goto :goto_3

    nop

    :goto_2
    return p0

    :goto_3
    aget-object p0, p0, p1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
