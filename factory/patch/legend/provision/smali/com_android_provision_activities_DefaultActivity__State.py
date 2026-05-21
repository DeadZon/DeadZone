TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity$State.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity$State.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field public static final PREFIX:Ljava/lang/String; = "com.android.provision.activities.DefaultActivity$"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__State__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['new-instance v0, Landroid/content/Intent;', 'invoke-direct {v0}, Landroid/content/Intent;-><init>()V', 'iget-object v1, p0, Lcom/android/provision/activities/DefaultActivity$State;->packageName:Ljava/lang/String;', 'invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z', 'if-eqz v1, :cond_0', 'iget-object v1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;', 'iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->targetClass:Ljava/lang/Class;', 'invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClass(Landroid/content/Context;Ljava/lang/Class;)Landroid/content/Intent;'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    new-instance v0, Landroid/content/Intent;

    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    iget-object v1, p0, Lcom/android/provision/activities/DefaultActivity$State;->packageName:Ljava/lang/String;

    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    if-eqz v1, :cond_0

    iget-object v1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->targetClass:Ljava/lang/Class;

    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClass(Landroid/content/Context;Ljava/lang/Class;)Landroid/content/Intent;

    return-object v0

    :cond_0
    iget-object v1, p0, Lcom/android/provision/activities/DefaultActivity$State;->packageName:Ljava/lang/String;

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->className:Ljava/lang/String;

    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    return-object v0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 3

    goto :goto_a

    nop

    :goto_0
    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->className:Ljava/lang/String;

    goto :goto_d

    nop

    :goto_1
    return-object v0

    :goto_2
    goto :goto_3

    nop

    :goto_3
    iget-object v1, p0, Lcom/android/provision/activities/DefaultActivity$State;->packageName:Ljava/lang/String;

    goto :goto_0

    nop

    :goto_4
    iget-object v1, p0, Lcom/android/provision/activities/DefaultActivity$State;->context:Landroid/content/Context;

    goto :goto_c

    nop

    :goto_5
    if-nez v1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_4

    nop

    :goto_6
    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClass(Landroid/content/Context;Ljava/lang/Class;)Landroid/content/Intent;

    goto :goto_1

    nop

    :goto_7
    invoke-direct {v0}, Landroid/content/Intent;-><init>()V

    goto :goto_8

    nop

    :goto_8
    iget-object v1, p0, Lcom/android/provision/activities/DefaultActivity$State;->packageName:Ljava/lang/String;

    goto :goto_9

    nop

    :goto_9
    invoke-static {v1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v1

    goto :goto_5

    nop

    :goto_a
    new-instance v0, Landroid/content/Intent;

    goto :goto_7

    nop

    :goto_b
    return-object v0

    :goto_c
    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity$State;->targetClass:Ljava/lang/Class;

    goto :goto_6

    nop

    :goto_d
    invoke-virtual {v0, v1, p0}, Landroid/content/Intent;->setClassName(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_b

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
