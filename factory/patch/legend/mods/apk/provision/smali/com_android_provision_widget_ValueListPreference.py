TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/widget/ValueListPreference.smali'
CLASS_FALLBACK_NAMES = ['ValueListPreference.smali']
CLASS_ANCHORS = ['.super Landroidx/preference/ListPreference;', '.implements Lmiuix/preference/FolmeAnimationController;']

PATCHES = [
    {
        'id': 'com_android_provision_widget_ValueListPreference__onClick',
        'method': '.method protected onClick()V',
        'method_name': 'onClick',
        'method_anchors': ['iget-boolean v0, p0, Lcom/android/provision/widget/ValueListPreference;->asTitle:Z', 'if-eqz v0, :cond_0', 'return-void', 'invoke-super {p0}, Landroidx/preference/DialogPreference;->onClick()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onClick()V
    .registers 2

    iget-boolean v0, p0, Lcom/android/provision/widget/ValueListPreference;->asTitle:Z

    if-eqz v0, :cond_0

    return-void

    :cond_0
    invoke-super {p0}, Landroidx/preference/DialogPreference;->onClick()V

    return-void
.end method""",
        'replacement': """.method protected onClick()V
    .registers 2

    goto :goto_5

    nop

    :goto_0
    return-void

    :goto_1
    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    invoke-super {p0}, Landroidx/preference/DialogPreference;->onClick()V

    goto :goto_2

    nop

    :goto_4
    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop

    :goto_5
    iget-boolean v0, p0, Lcom/android/provision/widget/ValueListPreference;->asTitle:Z

    goto :goto_4

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
