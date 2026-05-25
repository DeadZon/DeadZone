TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'miuix/preference/EditTextPreferenceDialogFragmentCompat.smali'
CLASS_FALLBACK_NAMES = ['EditTextPreferenceDialogFragmentCompat.smali']
CLASS_ANCHORS = ['.super Landroidx/preference/EditTextPreferenceDialogFragmentCompat;']

PATCHES = [
    {
        'id': 'miuix_preference_EditTextPreferenceDialogFragmentCompat__onPrepareDialogBuilder',
        'method': '.method protected final onPrepareDialogBuilder(Landroidx/appcompat/app/AlertDialog$Builder;)V',
        'method_name': 'onPrepareDialogBuilder',
        'method_anchors': ['new-instance p0, Ljava/lang/UnsupportedOperationException;', 'const-string p1, "using miuix builder instead"', 'invoke-direct {p0, p1}, Ljava/lang/UnsupportedOperationException;-><init>(Ljava/lang/String;)V'],
        'type': 'method_replace',
        'search': """.method protected final onPrepareDialogBuilder(Landroidx/appcompat/app/AlertDialog$Builder;)V
    .registers 2

    new-instance p0, Ljava/lang/UnsupportedOperationException;

    const-string p1, "using miuix builder instead"

    invoke-direct {p0, p1}, Ljava/lang/UnsupportedOperationException;-><init>(Ljava/lang/String;)V

    throw p0
.end method""",
        'replacement': """.method protected final onPrepareDialogBuilder(Landroidx/appcompat/app/AlertDialog$Builder;)V
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-direct {p0, p1}, Ljava/lang/UnsupportedOperationException;-><init>(Ljava/lang/String;)V

    goto :goto_1

    nop

    :goto_1
    throw p0

    :goto_2
    new-instance p0, Ljava/lang/UnsupportedOperationException;

    goto :goto_3

    nop

    :goto_3
    const-string p1, "using miuix builder instead"

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'miuix_preference_EditTextPreferenceDialogFragmentCompat__onPrepareDialogBuilder',
        'method': '.method protected onPrepareDialogBuilder(Lmiuix/appcompat/app/AlertDialog$Builder;)V',
        'method_name': 'onPrepareDialogBuilder',
        'method_anchors': ['new-instance v0, Lmiuix/preference/BuilderDelegate;', 'invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;', 'invoke-direct {v0, v1, p1}, Lmiuix/preference/BuilderDelegate;-><init>(Landroid/content/Context;Lmiuix/appcompat/app/AlertDialog$Builder;)V', 'invoke-super {p0, v0}, Landroidx/preference/PreferenceDialogFragmentCompat;->onPrepareDialogBuilder(Landroidx/appcompat/app/AlertDialog$Builder;)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onPrepareDialogBuilder(Lmiuix/appcompat/app/AlertDialog$Builder;)V
    .registers 4

    new-instance v0, Lmiuix/preference/BuilderDelegate;

    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-direct {v0, v1, p1}, Lmiuix/preference/BuilderDelegate;-><init>(Landroid/content/Context;Lmiuix/appcompat/app/AlertDialog$Builder;)V

    invoke-super {p0, v0}, Landroidx/preference/PreferenceDialogFragmentCompat;->onPrepareDialogBuilder(Landroidx/appcompat/app/AlertDialog$Builder;)V

    return-void
.end method""",
        'replacement': """.method protected onPrepareDialogBuilder(Lmiuix/appcompat/app/AlertDialog$Builder;)V
    .registers 4

    goto :goto_0

    nop

    :goto_0
    new-instance v0, Lmiuix/preference/BuilderDelegate;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0}, Landroidx/fragment/app/Fragment;->getContext()Landroid/content/Context;

    move-result-object v1

    goto :goto_2

    nop

    :goto_2
    invoke-direct {v0, v1, p1}, Lmiuix/preference/BuilderDelegate;-><init>(Landroid/content/Context;Lmiuix/appcompat/app/AlertDialog$Builder;)V

    goto :goto_3

    nop

    :goto_3
    invoke-super {p0, v0}, Landroidx/preference/PreferenceDialogFragmentCompat;->onPrepareDialogBuilder(Landroidx/appcompat/app/AlertDialog$Builder;)V

    goto :goto_4

    nop

    :goto_4
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
