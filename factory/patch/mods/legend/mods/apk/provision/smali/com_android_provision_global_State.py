TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/State.smali'
CLASS_FALLBACK_NAMES = ['State.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final PREFIX:Ljava/lang/String; = "com.android.provision.global."']

PATCHES = [
    {
        'id': 'com_android_provision_global_State__canBackTo',
        'method': '.method protected canBackTo()Z',
        'method_name': 'canBackTo',
        'method_anchors': ['return p0'],
        'type': 'method_replace',
        'search': """.method protected canBackTo()Z
    .registers 1

    const/4 p0, 0x1

    return p0
.end method""",
        'replacement': """.method protected canBackTo()Z
    .registers 1

    goto :goto_1

    nop

    :goto_0
    return p0

    :goto_1
    const/4 p0, 0x1

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_global_State__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['new-instance v0, Landroid/content/Intent;', 'invoke-direct {v0}, Landroid/content/Intent;-><init>()V', 'iget-object v1, p0, Lcom/android/provision/global/State;->packageName:Ljava/lang/String;', 'invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-eqz v1, :cond_0', 'iget-object v1, p0, Lcom/android/provision/global/State;->context:Landroid/content/Context;', 'iget-object p0, p0, Lcom/android/provision/global/State;->targetClass:Ljava/lang/Class;', 'invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClass(Landroid/content/Context;Ljava/lang/Class;)Landroid/content/Intent;'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    iget-object v1, p0, Lcom/android/provision/global/State;->packageName:Ljava/lang/String;

    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_0

    iget-object v1, p0, Lcom/android/provision/global/State;->context:Landroid/content/Context;

    iget-object p0, p0, Lcom/android/provision/global/State;->targetClass:Ljava/lang/Class;

    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClass(Landroid/content/Context;Ljava/lang/Class;)Landroid/content/Intent;

    return-object v0

    :cond_0
    iget-object v1, p0, Lcom/android/provision/global/State;->packageName:Ljava/lang/String;

    iget-object p0, p0, Lcom/android/provision/global/State;->className:Ljava/lang/String;

    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    return-object v0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    goto :goto_a

    nop

    :goto_0
    return-object v0

    :goto_1
    goto :goto_6

    nop

    :goto_2
    if-nez v1, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_3

    nop

    :goto_3
    iget-object v1, p0, Lcom/android/provision/global/State;->context:Landroid/content/Context;

    goto :goto_b

    nop

    :goto_4
    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_d

    nop

    :goto_5
    iget-object v1, p0, Lcom/android/provision/global/State;->packageName:Ljava/lang/String;

    goto :goto_c

    nop

    :goto_6
    iget-object v1, p0, Lcom/android/provision/global/State;->packageName:Ljava/lang/String;

    goto :goto_7

    nop

    :goto_7
    iget-object p0, p0, Lcom/android/provision/global/State;->className:Ljava/lang/String;

    goto :goto_4

    nop

    :goto_8
    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClass(Landroid/content/Context;Ljava/lang/Class;)Landroid/content/Intent;

    goto :goto_0

    nop

    :goto_9
    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    goto :goto_5

    nop

    :goto_a
    new-instance v0, Landroid/content/Intent;

    goto :goto_9

    nop

    :goto_b
    iget-object p0, p0, Lcom/android/provision/global/State;->targetClass:Ljava/lang/Class;

    goto :goto_8

    nop

    :goto_c
    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    goto :goto_2

    nop

    :goto_d
    return-object v0
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
