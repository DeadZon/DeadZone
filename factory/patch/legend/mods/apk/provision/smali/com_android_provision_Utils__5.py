TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/Utils$5.smali'
CLASS_FALLBACK_NAMES = ['Utils$5.smali']
CLASS_ANCHORS = ['.super Landroid/os/AsyncTask;']

PATCHES = [
    {
        'id': 'com_android_provision_Utils__5__doInBackground',
        'method': '.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'doInBackground',
        'method_anchors': ['check-cast p1, [Ljava/lang/Void;', 'invoke-virtual {p0, p1}, Lcom/android/provision/Utils$5;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    check-cast p1, [Ljava/lang/Void;

    invoke-virtual {p0, p1}, Lcom/android/provision/Utils$5;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

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
    invoke-virtual {p0, p1}, Lcom/android/provision/Utils$5;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

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
        'id': 'com_android_provision_Utils__5__doInBackground',
        'method': '.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;',
        'method_name': 'doInBackground',
        'method_anchors': ['const-string p1, "Provision_Utils"', 'const-string v1, "setupProvisionResources begin"', 'invoke-static {p1, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I', 'iget-object p0, p0, Lcom/android/provision/Utils$5;->val$context:Landroid/content/Context;', 'invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;', 'const-string v1, "content://com.android.thememanager.theme_provider"', 'invoke-static {v1}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;', 'const-string v2, "setupProvisionResources"'],
        'type': 'method_replace',
        'search': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 5

    const-string p1, "Provision_Utils"

    const/4 v0, 0x0

    :try_start_0
    const-string v1, "setupProvisionResources begin"

    invoke-static {p1, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object p0, p0, Lcom/android/provision/Utils$5;->val$context:Landroid/content/Context;

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p0

    const-string v1, "content://com.android.thememanager.theme_provider"

    invoke-static {v1}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    const-string v2, "setupProvisionResources"

    invoke-virtual {p0, v1, v2, v0, v0}, Landroid/content/ContentResolver;->call(Landroid/net/Uri;Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;

    const-string p0, "setupProvisionResources end"

    invoke-static {p1, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception p0

    const-string v1, "call setupProvisionResources error"

    invoke-static {p1, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Ljava/lang/Exception;->printStackTrace()V

    :goto_0
    return-object v0
.end method""",
        'replacement': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 5

    goto :goto_1

    nop

    :goto_0
    invoke-static {p1, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_2

    nop

    :goto_1
    const-string p1, "Provision_Utils"

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p0}, Ljava/lang/Exception;->printStackTrace()V

    :goto_3
    goto :goto_6

    nop

    :goto_4
    const/4 v0, 0x0

    :try_start_0
    const-string v1, "setupProvisionResources begin"

    invoke-static {p1, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object p0, p0, Lcom/android/provision/Utils$5;->val$context:Landroid/content/Context;

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p0

    const-string v1, "content://com.android.thememanager.theme_provider"

    invoke-static {v1}, Landroid/net/Uri;->parse(Ljava/lang/String;)Landroid/net/Uri;

    move-result-object v1

    const-string v2, "setupProvisionResources"

    invoke-virtual {p0, v1, v2, v0, v0}, Landroid/content/ContentResolver;->call(Landroid/net/Uri;Ljava/lang/String;Ljava/lang/String;Landroid/os/Bundle;)Landroid/os/Bundle;

    const-string p0, "setupProvisionResources end"

    invoke-static {p1, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_5

    nop

    :goto_5
    goto :goto_3

    :catch_0
    move-exception p0

    goto :goto_7

    nop

    :goto_6
    return-object v0

    :goto_7
    const-string v1, "call setupProvisionResources error"

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
