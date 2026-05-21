TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/CongratulationActivity.smali'
CLASS_FALLBACK_NAMES = ['CongratulationActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;', '.field private static final TAG:Ljava/lang/String; = "CongratulationActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_CongratulationActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'const-string p1, "CongratulationActivity"', 'const-string v0, "onCreate"', 'invoke-static {p1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I', 'invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->initFlag()V', 'invoke-static {p0}, Lcom/android/provision/Utils;->isProvisioned(Landroid/content/Context;)Z', 'if-eqz p1, :cond_0', 'invoke-virtual {p0, p1}, Landroid/app/Activity;->setResult(I)V'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    const-string p1, "CongratulationActivity"

    const-string v0, "onCreate"

    invoke-static {p1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->initFlag()V

    invoke-static {p0}, Lcom/android/provision/Utils;->isProvisioned(Landroid/content/Context;)Z

    move-result p1

    if-eqz p1, :cond_0

    const/4 p1, -0x1

    invoke-virtual {p0, p1}, Landroid/app/Activity;->setResult(I)V

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    return-void

    :cond_0
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_1

    invoke-virtual {p0}, Landroid/app/Activity;->getWindow()Landroid/view/Window;

    move-result-object p1

    invoke-static {p1}, Lmiuix/provision/OobeUtil;->setHideNavigationBar(Landroid/view/Window;)V

    :cond_1
    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object p1

    invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1, v0}, Landroidx/fragment/app/FragmentManager;->findFragmentByTag(Ljava/lang/String;)Landroidx/fragment/app/Fragment;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/activities/CongratulationActivity;->mFragment:Landroidx/fragment/app/Fragment;

    if-nez v0, :cond_2

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->getFragment()Landroidx/fragment/app/Fragment;

    move-result-object v0

    iput-object v0, p0, Lcom/android/provision/activities/CongratulationActivity;->mFragment:Landroidx/fragment/app/Fragment;

    const v1, 0x1020002

    invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object p0

    invoke-virtual {p1, v1, v0, p0}, Landroidx/fragment/app/FragmentTransaction;->replace(ILandroidx/fragment/app/Fragment;Ljava/lang/String;)Landroidx/fragment/app/FragmentTransaction;

    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commit()I

    :cond_2
    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_5

    nop

    :goto_0
    if-eqz v0, :cond_0

    goto :goto_1d

    :cond_0
    goto :goto_1b

    nop

    :goto_1
    const v1, 0x1020002

    goto :goto_9

    nop

    :goto_2
    invoke-virtual {p0}, Landroidx/fragment/app/FragmentActivity;->getSupportFragmentManager()Landroidx/fragment/app/FragmentManager;

    move-result-object p1

    goto :goto_12

    nop

    :goto_3
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    goto :goto_e

    nop

    :goto_4
    invoke-static {p0}, Lcom/android/provision/Utils;->isProvisioned(Landroid/content/Context;)Z

    move-result p1

    goto :goto_16

    nop

    :goto_5
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_b

    nop

    :goto_6
    return-void

    :goto_7
    goto :goto_3

    nop

    :goto_8
    const-string v0, "onCreate"

    goto :goto_18

    nop

    :goto_9
    invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object p0

    goto :goto_1a

    nop

    :goto_a
    invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->getFragment()Landroidx/fragment/app/Fragment;

    move-result-object v0

    goto :goto_10

    nop

    :goto_b
    const-string p1, "CongratulationActivity"

    goto :goto_8

    nop

    :goto_c
    const/4 p1, -0x1

    goto :goto_f

    nop

    :goto_d
    invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->initFlag()V

    goto :goto_4

    nop

    :goto_e
    if-nez p1, :cond_1

    goto :goto_15

    :cond_1
    goto :goto_13

    nop

    :goto_f
    invoke-virtual {p0, p1}, Landroid/app/Activity;->setResult(I)V

    goto :goto_11

    nop

    :goto_10
    iput-object v0, p0, Lcom/android/provision/activities/CongratulationActivity;->mFragment:Landroidx/fragment/app/Fragment;

    goto :goto_1

    nop

    :goto_11
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    goto :goto_6

    nop

    :goto_12
    invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->getFragmentTag()Ljava/lang/String;

    move-result-object v0

    goto :goto_1e

    nop

    :goto_13
    invoke-virtual {p0}, Landroid/app/Activity;->getWindow()Landroid/view/Window;

    move-result-object p1

    goto :goto_14

    nop

    :goto_14
    invoke-static {p1}, Lmiuix/provision/OobeUtil;->setHideNavigationBar(Landroid/view/Window;)V

    :goto_15
    goto :goto_2

    nop

    :goto_16
    if-nez p1, :cond_2

    goto :goto_7

    :cond_2
    goto :goto_c

    nop

    :goto_17
    iput-object v0, p0, Lcom/android/provision/activities/CongratulationActivity;->mFragment:Landroidx/fragment/app/Fragment;

    goto :goto_0

    nop

    :goto_18
    invoke-static {p1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_d

    nop

    :goto_19
    return-void

    :goto_1a
    invoke-virtual {p1, v1, v0, p0}, Landroidx/fragment/app/FragmentTransaction;->replace(ILandroidx/fragment/app/Fragment;Ljava/lang/String;)Landroidx/fragment/app/FragmentTransaction;

    goto :goto_1c

    nop

    :goto_1b
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentManager;->beginTransaction()Landroidx/fragment/app/FragmentTransaction;

    move-result-object p1

    goto :goto_a

    nop

    :goto_1c
    invoke-virtual {p1}, Landroidx/fragment/app/FragmentTransaction;->commit()I

    :goto_1d
    goto :goto_19

    nop

    :goto_1e
    invoke-virtual {p1, v0}, Landroidx/fragment/app/FragmentManager;->findFragmentByTag(Ljava/lang/String;)Landroidx/fragment/app/Fragment;

    move-result-object v0

    goto :goto_17

    nop
.end method""",
        'required': True,
        'policy_status': 'BUILD_FLAG_PARTIALLY_SKIPPED',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_CongratulationActivity__onResume',
        'method': '.method protected onResume()V',
        'method_name': 'onResume',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V', 'invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->initFlag()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onResume()V
    .registers 1

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V

    invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->initFlag()V

    return-void
.end method""",
        'replacement': """.method protected onResume()V
    .registers 1

    goto :goto_2

    nop

    :goto_0
    invoke-direct {p0}, Lcom/android/provision/activities/CongratulationActivity;->initFlag()V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onResume()V

    goto :goto_0

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
