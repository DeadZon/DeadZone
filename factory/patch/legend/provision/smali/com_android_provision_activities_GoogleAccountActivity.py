TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/GoogleAccountActivity.smali'
CLASS_FALLBACK_NAMES = ['GoogleAccountActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;', '.field public static final GOOGLE_ACCOUNT_TYPE:Ljava/lang/String; = "com.google"', '.field private static final REQUEST_CONFIRMLOGIN:I = 0x1', '.field private static final REQUEST_LOGIN:I = 0x2', '.field private static final TAG:Ljava/lang/String; = "Provision:GoogleAccountActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_GoogleAccountActivity__onActivityResult',
        'method': '.method protected onActivityResult(IILandroid/content/Intent;)V',
        'method_name': 'onActivityResult',
        'method_anchors': ['invoke-super {p0, p1, p2, p3}, Landroidx/fragment/app/FragmentActivity;->onActivityResult(IILandroid/content/Intent;)V', 'if-eq p1, p3, :cond_3', 'if-eq p1, v0, :cond_0', 'return-void', 'if-eq p1, v1, :cond_2', 'invoke-static {p0}, Lcom/android/provision/Utils;->hasGoogleAccount(Landroid/content/Context;)Z', 'if-eqz p1, :cond_1', 'invoke-direct {p0}, Lcom/android/provision/activities/GoogleAccountActivity;->startGoogleAccountConfirmAcitivty()V'],
        'type': 'method_replace',
        'search': """.method protected onActivityResult(IILandroid/content/Intent;)V
    .registers 6

    invoke-super {p0, p1, p2, p3}, Landroidx/fragment/app/FragmentActivity;->onActivityResult(IILandroid/content/Intent;)V

    const/4 p3, 0x1

    const/4 v0, 0x2

    const/4 v1, -0x1

    if-eq p1, p3, :cond_3

    if-eq p1, v0, :cond_0

    return-void

    :cond_0
    if-eq p1, v1, :cond_2

    invoke-static {p0}, Lcom/android/provision/Utils;->hasGoogleAccount(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_1

    goto :goto_0

    :cond_1
    invoke-direct {p0}, Lcom/android/provision/activities/GoogleAccountActivity;->startGoogleAccountConfirmAcitivty()V

    return-void

    :cond_2
    :goto_0
    invoke-virtual {p0, v1}, Landroid/app/Activity;->setResult(I)V

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    const-string p0, "event_click_login_google"

    invoke-static {p0}, Lcom/android/provision/utils/OTHelper;->rdCountEvent(Ljava/lang/String;)V

    return-void

    :cond_3
    const/16 p1, 0x8

    if-eq p2, p1, :cond_5

    const/16 p1, 0x9

    if-eq p2, p1, :cond_4

    const/4 p1, 0x0

    invoke-virtual {p0, p1}, Landroid/app/Activity;->setResult(I)V

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    return-void

    :cond_4
    invoke-virtual {p0, v1}, Landroid/app/Activity;->setResult(I)V

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    return-void

    :cond_5
    new-instance p1, Landroid/content/Intent;

    const-string p2, "android.settings.ADD_ACCOUNT_SETTINGS"

    invoke-direct {p1, p2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    const-string p2, "selected_account"

    const-string p3, "com.google"

    invoke-virtual {p1, p2, p3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {p0, p1, v0}, Landroidx/activity/ComponentActivity;->startActivityForResult(Landroid/content/Intent;I)V

    const-string p0, "event_click_has_google_account"

    invoke-static {p0}, Lcom/android/provision/utils/OTHelper;->rdCountEvent(Ljava/lang/String;)V

    return-void
.end method""",
        'replacement': """.method protected onActivityResult(IILandroid/content/Intent;)V
    .registers 6

    goto :goto_21

    nop

    :goto_0
    if-nez p1, :cond_0

    goto :goto_20

    :cond_0
    goto :goto_1f

    nop

    :goto_1
    return-void

    :goto_2
    goto :goto_1e

    nop

    :goto_3
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    goto :goto_11

    nop

    :goto_4
    invoke-static {p0}, Lcom/android/provision/utils/OTHelper;->rdCountEvent(Ljava/lang/String;)V

    goto :goto_1

    nop

    :goto_5
    invoke-direct {p1, p2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    goto :goto_f

    nop

    :goto_6
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    goto :goto_28

    nop

    :goto_7
    return-void

    :goto_8
    goto :goto_27

    nop

    :goto_9
    return-void

    :goto_a
    goto :goto_23

    nop

    :goto_b
    const-string p2, "android.settings.ADD_ACCOUNT_SETTINGS"

    goto :goto_5

    nop

    :goto_c
    const/4 p3, 0x1

    goto :goto_29

    nop

    :goto_d
    if-ne p1, v0, :cond_1

    goto :goto_16

    :cond_1
    goto :goto_15

    nop

    :goto_e
    if-ne p1, p3, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_d

    nop

    :goto_f
    const-string p2, "selected_account"

    goto :goto_1c

    nop

    :goto_10
    const-string p0, "event_click_has_google_account"

    goto :goto_2b

    nop

    :goto_11
    return-void

    :goto_12
    goto :goto_1a

    nop

    :goto_13
    if-ne p2, p1, :cond_3

    goto :goto_8

    :cond_3
    goto :goto_19

    nop

    :goto_14
    invoke-virtual {p0, p1}, Landroid/app/Activity;->setResult(I)V

    goto :goto_25

    nop

    :goto_15
    return-void

    :goto_16
    goto :goto_17

    nop

    :goto_17
    if-ne p1, v1, :cond_4

    goto :goto_a

    :cond_4
    goto :goto_24

    nop

    :goto_18
    return-void

    :goto_19
    const/4 p1, 0x0

    goto :goto_14

    nop

    :goto_1a
    new-instance p1, Landroid/content/Intent;

    goto :goto_b

    nop

    :goto_1b
    const/4 v1, -0x1

    goto :goto_e

    nop

    :goto_1c
    const-string p3, "com.google"

    goto :goto_26

    nop

    :goto_1d
    invoke-direct {p0}, Lcom/android/provision/activities/GoogleAccountActivity;->startGoogleAccountConfirmAcitivty()V

    goto :goto_9

    nop

    :goto_1e
    const/16 p1, 0x8

    goto :goto_2a

    nop

    :goto_1f
    goto :goto_a

    :goto_20
    goto :goto_1d

    nop

    :goto_21
    invoke-super {p0, p1, p2, p3}, Landroidx/fragment/app/FragmentActivity;->onActivityResult(IILandroid/content/Intent;)V

    goto :goto_c

    nop

    :goto_22
    const/16 p1, 0x9

    goto :goto_13

    nop

    :goto_23
    invoke-virtual {p0, v1}, Landroid/app/Activity;->setResult(I)V

    goto :goto_6

    nop

    :goto_24
    invoke-static {p0}, Lcom/android/provision/Utils;->hasGoogleAccount(Landroid/content/Context;)Z

    move-result p1

    goto :goto_0

    nop

    :goto_25
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    goto :goto_7

    nop

    :goto_26
    invoke-virtual {p1, p2, p3}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    goto :goto_2c

    nop

    :goto_27
    invoke-virtual {p0, v1}, Landroid/app/Activity;->setResult(I)V

    goto :goto_3

    nop

    :goto_28
    const-string p0, "event_click_login_google"

    goto :goto_4

    nop

    :goto_29
    const/4 v0, 0x2

    goto :goto_1b

    nop

    :goto_2a
    if-ne p2, p1, :cond_5

    goto :goto_12

    :cond_5
    goto :goto_22

    nop

    :goto_2b
    invoke-static {p0}, Lcom/android/provision/utils/OTHelper;->rdCountEvent(Ljava/lang/String;)V

    goto :goto_18

    nop

    :goto_2c
    invoke-virtual {p0, p1, v0}, Landroidx/activity/ComponentActivity;->startActivityForResult(Landroid/content/Intent;I)V

    goto :goto_10

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_GoogleAccountActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;', 'const-string v0, "extra_to_next"', 'invoke-virtual {p1, v0, v1}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z', 'iput-boolean p1, p0, Lcom/android/provision/activities/GoogleAccountActivity;->mIsToNext:Z', 'invoke-direct {p0}, Lcom/android/provision/activities/GoogleAccountActivity;->startGoogleAccountConfirmAcitivty()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    const-string v0, "extra_to_next"

    const/4 v1, 0x1

    invoke-virtual {p1, v0, v1}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result p1

    iput-boolean p1, p0, Lcom/android/provision/activities/GoogleAccountActivity;->mIsToNext:Z

    invoke-direct {p0}, Lcom/android/provision/activities/GoogleAccountActivity;->startGoogleAccountConfirmAcitivty()V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_7

    nop

    :goto_1
    invoke-direct {p0}, Lcom/android/provision/activities/GoogleAccountActivity;->startGoogleAccountConfirmAcitivty()V

    goto :goto_6

    nop

    :goto_2
    const-string v0, "extra_to_next"

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p1, v0, v1}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result p1

    goto :goto_5

    nop

    :goto_4
    const/4 v1, 0x1

    goto :goto_3

    nop

    :goto_5
    iput-boolean p1, p0, Lcom/android/provision/activities/GoogleAccountActivity;->mIsToNext:Z

    goto :goto_1

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object p1

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_GoogleAccountActivity__onPause',
        'method': '.method protected onPause()V',
        'method_name': 'onPause',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onPause()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onPause()V
    .registers 1

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onPause()V

    return-void
.end method""",
        'replacement': """.method protected onPause()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onPause()V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_GoogleAccountActivity__onResume',
        'method': '.method protected onResume()V',
        'method_name': 'onResume',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onResume()V
    .registers 1

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V

    return-void
.end method""",
        'replacement': """.method protected onResume()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
