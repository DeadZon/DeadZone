TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/fragment/LanguagePickerFragment$3.smali'
CLASS_FALLBACK_NAMES = ['LanguagePickerFragment$3.smali']
CLASS_ANCHORS = ['.super Landroid/os/AsyncTask;']

PATCHES = [
    {
        'id': 'com_android_provision_fragment_LanguagePickerFragment__3__doInBackground',
        'method': '.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'doInBackground',
        'method_anchors': ['check-cast p1, [Ljava/lang/Void;', 'invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment$3;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    check-cast p1, [Ljava/lang/Void;

    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment$3;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

    move-result-object p0

    return-object p0
.end method""",
        'replacement': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    check-cast p1, [Ljava/lang/Void;

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lcom/android/provision/fragment/LanguagePickerFragment$3;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

    move-result-object p0

    goto :goto_2

    nop

    :goto_2
    return-object p0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_fragment_LanguagePickerFragment__3__doInBackground',
        'method': '.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;',
        'method_name': 'doInBackground',
        'method_anchors': ['const-string p1, "persist.sys.language"', 'iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$3;->val$language:Ljava/lang/String;', 'invoke-static {p1, v0}, Lmiuix/core/util/SystemProperties;->set(Ljava/lang/String;Ljava/lang/String;)V', 'const-string p1, "persist.sys.country"', 'iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$3;->val$country:Ljava/lang/String;', 'invoke-static {p1, p0}, Lmiuix/core/util/SystemProperties;->set(Ljava/lang/String;Ljava/lang/String;)V', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 3

    const-string p1, "persist.sys.language"

    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$3;->val$language:Ljava/lang/String;

    invoke-static {p1, v0}, Lmiuix/core/util/SystemProperties;->set(Ljava/lang/String;Ljava/lang/String;)V

    const-string p1, "persist.sys.country"

    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$3;->val$country:Ljava/lang/String;

    invoke-static {p1, p0}, Lmiuix/core/util/SystemProperties;->set(Ljava/lang/String;Ljava/lang/String;)V

    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    const-string p1, "persist.sys.country"

    goto :goto_4

    nop

    :goto_1
    const-string p1, "persist.sys.language"

    goto :goto_5

    nop

    :goto_2
    return-object p0

    :goto_3
    const/4 p0, 0x0

    goto :goto_2

    nop

    :goto_4
    iget-object p0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$3;->val$country:Ljava/lang/String;

    goto :goto_7

    nop

    :goto_5
    iget-object v0, p0, Lcom/android/provision/fragment/LanguagePickerFragment$3;->val$language:Ljava/lang/String;

    goto :goto_6

    nop

    :goto_6
    invoke-static {p1, v0}, Lmiuix/core/util/SystemProperties;->set(Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_0

    nop

    :goto_7
    invoke-static {p1, p0}, Lmiuix/core/util/SystemProperties;->set(Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
