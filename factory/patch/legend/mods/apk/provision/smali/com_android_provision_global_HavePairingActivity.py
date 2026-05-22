TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/HavePairingActivity.smali'
CLASS_FALLBACK_NAMES = ['HavePairingActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;']

PATCHES = [
    {
        'id': 'com_android_provision_global_HavePairingActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;', 'invoke-static {p1, v0}, Lcom/android/provision/Utils;->setQuickStartPairingTag(Landroid/content/Context;I)V', 'invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;', 'invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V', 'invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p1

    const/4 v0, -0x1

    invoke-static {p1, v0}, Lcom/android/provision/Utils;->setQuickStartPairingTag(Landroid/content/Context;I)V

    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    const/4 v0, -0x1

    goto :goto_6

    nop

    :goto_1
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_0

    nop

    :goto_2
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_1

    nop

    :goto_3
    invoke-static {p0, p1, v0}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V

    goto :goto_5

    nop

    :goto_4
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    goto :goto_3

    nop

    :goto_5
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    goto :goto_7

    nop

    :goto_6
    invoke-static {p1, v0}, Lcom/android/provision/Utils;->setQuickStartPairingTag(Landroid/content/Context;I)V

    goto :goto_4

    nop

    :goto_7
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
