TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/EsimDateState.smali'
CLASS_FALLBACK_NAMES = ['EsimDateState.smali']
CLASS_ANCHORS = ['.super Lcom/android/provision/global/State;', '.field private static final TAG:Ljava/lang/String; = "EsimDateState"']

PATCHES = [
    {
        'id': 'com_android_provision_global_EsimDateState__getIntent',
        'method': '.method protected getIntent()Landroid/content/Intent;',
        'method_name': 'getIntent',
        'method_anchors': ['new-instance p0, Landroid/content/Intent;', 'invoke-direct {p0}, Landroid/content/Intent;-><init>()V', 'const-string v0, "android.telephony.euicc.action.MANAGE_EMBEDDED_SUBSCRIPTIONS"', 'invoke-virtual {p0, v0}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;', 'return-object p0'],
        'type': 'method_replace',
        'search': """.method protected getIntent()Landroid/content/Intent;
    .registers 2

    new-instance p0, Landroid/content/Intent;

    invoke-direct {p0}, Landroid/content/Intent;-><init>()V

    const-string v0, "android.telephony.euicc.action.MANAGE_EMBEDDED_SUBSCRIPTIONS"

    invoke-virtual {p0, v0}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;

    return-object p0
.end method""",
        'replacement': """.method protected getIntent()Landroid/content/Intent;
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return-object p0

    :goto_1
    invoke-direct {p0}, Landroid/content/Intent;-><init>()V

    goto :goto_4

    nop

    :goto_2
    new-instance p0, Landroid/content/Intent;

    goto :goto_1

    nop

    :goto_3
    invoke-virtual {p0, v0}, Landroid/content/Intent;->setAction(Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_0

    nop

    :goto_4
    const-string v0, "android.telephony.euicc.action.MANAGE_EMBEDDED_SUBSCRIPTIONS"

    goto :goto_3

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
