TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/Utils$2.smali'
CLASS_FALLBACK_NAMES = ['Utils$2.smali']
CLASS_ANCHORS = ['.super Landroid/os/AsyncTask;']

PATCHES = [
    {
        'id': 'com_android_provision_Utils__2__doInBackground',
        'method': '.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;',
        'method_name': 'doInBackground',
        'method_anchors': ['check-cast p1, [Ljava/lang/Void;', 'invoke-virtual {p0, p1}, Lcom/android/provision/Utils$2;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected bridge synthetic doInBackground([Ljava/lang/Object;)Ljava/lang/Object;
    .registers 2

    check-cast p1, [Ljava/lang/Void;

    invoke-virtual {p0, p1}, Lcom/android/provision/Utils$2;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

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
    invoke-virtual {p0, p1}, Lcom/android/provision/Utils$2;->doInBackground([Ljava/lang/Void;)Ljava/lang/Void;

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
        'id': 'com_android_provision_Utils__2__doInBackground',
        'method': '.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;',
        'method_name': 'doInBackground',
        'method_anchors': ['iget-object p1, p0, Lcom/android/provision/Utils$2;->val$pendingApps:Ljava/util/ArrayList;', 'invoke-virtual {p1}, Ljava/util/ArrayList;->size()I', 'if-ge v2, v0, :cond_0', 'invoke-virtual {p1, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;', 'check-cast v3, Ljava/lang/String;', 'iget-object v4, p0, Lcom/android/provision/Utils$2;->val$packageManager:Landroid/content/pm/PackageManager;', 'iget v5, p0, Lcom/android/provision/Utils$2;->val$state:I', 'invoke-virtual {v4, v3, v5, v1}, Landroid/content/pm/PackageManager;->setApplicationEnabledSetting(Ljava/lang/String;II)V'],
        'type': 'method_replace',
        'search': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 8

    :try_start_0
    iget-object p1, p0, Lcom/android/provision/Utils$2;->val$pendingApps:Ljava/util/ArrayList;

    invoke-virtual {p1}, Ljava/util/ArrayList;->size()I

    move-result v0

    const/4 v1, 0x0

    move v2, v1

    :goto_0
    if-ge v2, v0, :cond_0

    invoke-virtual {p1, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v3

    add-int/lit8 v2, v2, 0x1

    check-cast v3, Ljava/lang/String;

    iget-object v4, p0, Lcom/android/provision/Utils$2;->val$packageManager:Landroid/content/pm/PackageManager;

    iget v5, p0, Lcom/android/provision/Utils$2;->val$state:I

    invoke-virtual {v4, v3, v5, v1}, Landroid/content/pm/PackageManager;->setApplicationEnabledSetting(Ljava/lang/String;II)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception p0

    const-string p1, "Provision_Utils"

    const-string v0, "setGmsApplicationEnabled fail"

    invoke-static {p1, v0, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_0
    const/4 p0, 0x0

    return-object p0
.end method""",
        'replacement': """.method protected varargs doInBackground([Ljava/lang/Void;)Ljava/lang/Void;
    .registers 8

    :try_start_0
    iget-object p1, p0, Lcom/android/provision/Utils$2;->val$pendingApps:Ljava/util/ArrayList;

    invoke-virtual {p1}, Ljava/util/ArrayList;->size()I

    move-result v0

    const/4 v1, 0x0

    move v2, v1

    :goto_0
    if-ge v2, v0, :cond_0

    invoke-virtual {p1, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v3

    add-int/lit8 v2, v2, 0x1

    check-cast v3, Ljava/lang/String;

    iget-object v4, p0, Lcom/android/provision/Utils$2;->val$packageManager:Landroid/content/pm/PackageManager;

    iget v5, p0, Lcom/android/provision/Utils$2;->val$state:I

    invoke-virtual {v4, v3, v5, v1}, Landroid/content/pm/PackageManager;->setApplicationEnabledSetting(Ljava/lang/String;II)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_4

    nop

    :goto_1
    return-object p0

    :goto_2
    const-string v0, "setGmsApplicationEnabled fail"

    goto :goto_5

    nop

    :goto_3
    const-string p1, "Provision_Utils"

    goto :goto_2

    nop

    :goto_4
    goto :goto_0

    :catch_0
    move-exception p0

    goto :goto_3

    nop

    :goto_5
    invoke-static {p1, v0, p0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_0
    goto :goto_6

    nop

    :goto_6
    const/4 p0, 0x0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
