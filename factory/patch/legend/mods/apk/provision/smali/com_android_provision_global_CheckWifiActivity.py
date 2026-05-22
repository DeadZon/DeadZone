TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/CheckWifiActivity.smali'
CLASS_FALLBACK_NAMES = ['CheckWifiActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;', '.field private static final RESULT_CONNECTED:I = 0x65', '.field private static final RESULT_UNCONNECTED:I = 0x66', '.field private static final TAG:Ljava/lang/String; = "Provision:CheckWifiActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_global_CheckWifiActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'invoke-static {p0}, Lcom/android/provision/utils/NetworkUtils;->isCaptivePortalValidated(Landroid/content/Context;)Z', 'if-eqz p1, :cond_0', 'invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;', 'invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V', 'invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;', 'invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    invoke-static {p0}, Lcom/android/provision/utils/NetworkUtils;->isCaptivePortalValidated(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_0

    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    const/16 v0, 0x65

    invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    goto :goto_0

    :cond_0
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    const/16 v0, 0x66

    invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    :goto_0
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_9

    nop

    :goto_0
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    goto :goto_d

    nop

    :goto_1
    invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    goto :goto_3

    nop

    :goto_2
    return-void

    :goto_3
    goto :goto_6

    :goto_4
    goto :goto_0

    nop

    :goto_5
    invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    :goto_6
    goto :goto_c

    nop

    :goto_7
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    goto :goto_a

    nop

    :goto_8
    if-nez p1, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_7

    nop

    :goto_9
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_b

    nop

    :goto_a
    const/16 v0, 0x65

    goto :goto_1

    nop

    :goto_b
    invoke-static {p0}, Lcom/android/provision/utils/NetworkUtils;->isCaptivePortalValidated(Landroid/content/Context;)Z

    move-result p1

    goto :goto_8

    nop

    :goto_c
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    goto :goto_2

    nop

    :goto_d
    const/16 v0, 0x66

    goto :goto_5

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
