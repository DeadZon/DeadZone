TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/DefaultActivity.smali'
CLASS_FALLBACK_NAMES = ['DefaultActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/provision/ProvisionBaseActivity;', '.field private static final AUTHORITY_FIND_DEVICE:Ljava/lang/String; = "com.xiaomi.finddevice.provider"', '.field private static final AUTH_TOKEN_TYPE:Ljava/lang/String; = "micloud"', '.field public static final HUANJI_ACTION:Ljava/lang/String; = "com.intent.action.HuanjiProvision"', '.field private static final HUANJI_OLD_FINGERPRINT:Ljava/lang/String; = "huanji_old_fingerprint"', '.field private static final HUANJI_PACKAGE_NAME:Ljava/lang/String; = "com.miui.huanji"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_DefaultActivity__nextAction',
        'method': '.method nextAction(I)V',
        'method_name': 'nextAction',
        'method_anchors': ['const-string v0, "Provision_DefaultActivity"', 'const-string v1, " here is nextAction "', 'invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I', 'invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;', 'invoke-static {v0, p1}, Lcom/android/provision/global/WizardManagerHelper;->getNextIntent(Landroid/content/Intent;I)Landroid/content/Intent;', 'invoke-virtual {p0, p1, v0}, Landroidx/activity/ComponentActivity;->startActivityForResult(Landroid/content/Intent;I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method nextAction(I)V
    .registers 4

    const-string v0, "Provision_DefaultActivity"

    const-string v1, " here is nextAction "

    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object v0

    invoke-static {v0, p1}, Lcom/android/provision/global/WizardManagerHelper;->getNextIntent(Landroid/content/Intent;I)Landroid/content/Intent;

    move-result-object p1

    const/16 v0, 0x2710

    invoke-virtual {p0, p1, v0}, Landroidx/activity/ComponentActivity;->startActivityForResult(Landroid/content/Intent;I)V

    return-void
.end method""",
        'replacement': """.method nextAction(I)V
    .registers 4

    goto :goto_5

    nop

    :goto_0
    invoke-static {v0, p1}, Lcom/android/provision/global/WizardManagerHelper;->getNextIntent(Landroid/content/Intent;I)Landroid/content/Intent;

    move-result-object p1

    goto :goto_2

    nop

    :goto_1
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object v0

    goto :goto_0

    nop

    :goto_2
    const/16 v0, 0x2710

    goto :goto_6

    nop

    :goto_3
    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    nop

    :goto_4
    const-string v1, " here is nextAction "

    goto :goto_3

    nop

    :goto_5
    const-string v0, "Provision_DefaultActivity"

    goto :goto_4

    nop

    :goto_6
    invoke-virtual {p0, p1, v0}, Landroidx/activity/ComponentActivity;->startActivityForResult(Landroid/content/Intent;I)V

    goto :goto_7

    nop

    :goto_7
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__initFullScreenMode',
        'method': '.method private initFullScreenMode()V',
        'method_name': 'initFullScreenMode',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'invoke-static {v1}, Lcom/android/provision/DefaultPreferenceHelper;->setPrefFullscreen(Z)V', 'invoke-static {p0, v0}, Lcom/android/provision/Utils;->setNavigationBarFullScreen(Landroid/content/Context;Z)V', 'return-void'],
        'type': 'policy_skip',
        'search': """.method private initFullScreenMode()V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 v1, v0, 0x1

    invoke-static {v1}, Lcom/android/provision/DefaultPreferenceHelper;->setPrefFullscreen(Z)V

    xor-int/lit8 v0, v0, 0x1

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->setNavigationBarFullScreen(Landroid/content/Context;Z)V

    return-void
.end method""",
        'replacement': """.method private initFullScreenMode()V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/lit8 v1, v0, 0x1

    invoke-static {v1}, Lcom/android/provision/DefaultPreferenceHelper;->setPrefFullscreen(Z)V

    xor-int/lit8 v0, v0, 0x1

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->setNavigationBarFullScreen(Landroid/content/Context;Z)V

    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__registerNetworkChangedReceiver',
        'method': '.method private registerNetworkChangedReceiver()V',
        'method_name': 'registerNetworkChangedReceiver',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'iget-boolean v0, p0, Lcom/android/provision/activities/DefaultActivity;->mIsNetworkRegistered:Z', 'if-nez v0, :cond_0', 'iput-boolean v0, p0, Lcom/android/provision/activities/DefaultActivity;->mIsNetworkRegistered:Z', 'new-instance v0, Lcom/android/provision/receiver/NetWorkChangedReceiver;', 'invoke-direct {v0}, Lcom/android/provision/receiver/NetWorkChangedReceiver;-><init>()V', 'iput-object v0, p0, Lcom/android/provision/activities/DefaultActivity;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;'],
        'type': 'method_delete',
        'search': """.method private registerNetworkChangedReceiver()V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    iget-boolean v0, p0, Lcom/android/provision/activities/DefaultActivity;->mIsNetworkRegistered:Z

    if-nez v0, :cond_0

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/provision/activities/DefaultActivity;->mIsNetworkRegistered:Z

    new-instance v0, Lcom/android/provision/receiver/NetWorkChangedReceiver;

    invoke-direct {v0}, Lcom/android/provision/receiver/NetWorkChangedReceiver;-><init>()V

    iput-object v0, p0, Lcom/android/provision/activities/DefaultActivity;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;

    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    const-string v1, "android.net.conn.CONNECTIVITY_CHANGE"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/provision/activities/DefaultActivity;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;

    invoke-virtual {p0, v1, v0}, Landroid/app/Activity;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    :cond_0
    return-void
.end method""",
        'replacement': """""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__unRegisterNetworkChangedReceiver',
        'method': '.method private unRegisterNetworkChangedReceiver()V',
        'method_name': 'unRegisterNetworkChangedReceiver',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'iget-boolean v0, p0, Lcom/android/provision/activities/DefaultActivity;->mIsNetworkRegistered:Z', 'if-eqz v0, :cond_0', 'iput-boolean v0, p0, Lcom/android/provision/activities/DefaultActivity;->mIsNetworkRegistered:Z', 'iget-object v0, p0, Lcom/android/provision/activities/DefaultActivity;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;', 'invoke-virtual {p0, v0}, Landroid/app/Activity;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V', 'return-void'],
        'type': 'method_delete',
        'search': """.method private unRegisterNetworkChangedReceiver()V
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    iget-boolean v0, p0, Lcom/android/provision/activities/DefaultActivity;->mIsNetworkRegistered:Z

    if-eqz v0, :cond_0

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/provision/activities/DefaultActivity;->mIsNetworkRegistered:Z

    iget-object v0, p0, Lcom/android/provision/activities/DefaultActivity;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;

    invoke-virtual {p0, v0}, Landroid/app/Activity;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    :cond_0
    return-void
.end method""",
        'replacement': """""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__onActivityResult',
        'method': '.method protected onActivityResult(IILandroid/content/Intent;)V',
        'method_name': 'onActivityResult',
        'method_anchors': ['new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "onActivityResult requestCode: "', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;', 'const-string v1, " resultCode =  "', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method protected onActivityResult(IILandroid/content/Intent;)V
    .registers 7

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "onActivityResult requestCode: "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v1, " resultCode =  "

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "Provision_DefaultActivity"

    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    const/16 v0, 0x21

    if-ne p1, v0, :cond_0

    invoke-static {}, Lcom/android/provision/Utils;->shouldNotFinishDefaultActivity()Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    invoke-static {p0}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->-$$Nest$mresumeState(Lcom/android/provision/activities/DefaultActivity$StateMachine;)V

    return-void

    :cond_0
    const/4 v0, 0x1

    if-ne p1, v0, :cond_3

    const/4 p1, -0x1

    if-ne p2, p1, :cond_2

    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->isManagedProvisioningDpcDownloaded()Z

    move-result p1

    if-eqz p1, :cond_1

    const/16 p1, 0x7d

    invoke-virtual {p0, p1}, Lcom/android/provision/activities/DefaultActivity;->nextAction(I)V

    return-void

    :cond_1
    const/16 p1, 0x7c

    invoke-virtual {p0, p1}, Lcom/android/provision/activities/DefaultActivity;->nextAction(I)V

    :cond_2
    return-void

    :cond_3
    const/4 v0, 0x0

    if-eqz p3, :cond_4

    const-string v1, "fromButton"

    invoke-virtual {p3, v1}, Landroid/content/Intent;->hasExtra(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_4

    invoke-virtual {p3, v1, v0}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I

    move-result v1

    sput v1, Lcom/android/provision/activities/DefaultActivity;->MiMoverDirect:I

    :cond_4
    const/16 v1, 0xdb6

    if-ne p1, v1, :cond_5

    invoke-direct {p0, p1, p2}, Lcom/android/provision/activities/DefaultActivity;->onAuraActivityResult(II)V

    return-void

    :cond_5
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    invoke-virtual {p1, p2, p3}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->onResult(ILandroid/content/Intent;)V

    if-eqz p3, :cond_6

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    const-string v1, "extra_mutisimsettings_force_skiped"

    invoke-virtual {p3, v1, v0}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result v1

    invoke-virtual {p1, v1}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->setMultiSimSettingsSkiped(Z)V

    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    const-string v1, "extra_bootvideo_force_skiped"

    invoke-virtual {p3, v1, v0}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result p3

    invoke-virtual {p1, p3}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->setBootVideoSkiped(Z)V

    :cond_6
    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    invoke-virtual {p0, p2}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->run(I)V

    return-void
.end method""",
        'replacement': """.method protected onActivityResult(IILandroid/content/Intent;)V
    .registers 7

    goto :goto_1

    nop

    :goto_0
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->isManagedProvisioningDpcDownloaded()Z

    move-result p1

    goto :goto_23

    nop

    :goto_1
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_20

    nop

    :goto_2
    invoke-virtual {p1, p2, p3}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->onResult(ILandroid/content/Intent;)V

    goto :goto_2c

    nop

    :goto_3
    const/4 v0, 0x1

    goto :goto_4

    nop

    :goto_4
    if-eq p1, v0, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_1e

    nop

    :goto_5
    invoke-virtual {p3, v1, v0}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result v1

    goto :goto_10

    nop

    :goto_6
    invoke-virtual {p3, v1, v0}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I

    move-result v1

    goto :goto_31

    nop

    :goto_7
    if-nez v0, :cond_1

    goto :goto_1a

    :cond_1
    goto :goto_22

    nop

    :goto_8
    invoke-virtual {p3, v1, v0}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result p3

    goto :goto_25

    nop

    :goto_9
    const/16 v1, 0xdb6

    goto :goto_29

    nop

    :goto_a
    invoke-virtual {p0, p1}, Lcom/android/provision/activities/DefaultActivity;->nextAction(I)V

    goto :goto_27

    nop

    :goto_b
    invoke-virtual {p3, v1}, Landroid/content/Intent;->hasExtra(Ljava/lang/String;)Z

    move-result v2

    goto :goto_11

    nop

    :goto_c
    const/16 v0, 0x21

    goto :goto_3a

    nop

    :goto_d
    const/4 v0, 0x0

    goto :goto_2d

    nop

    :goto_e
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_2f

    nop

    :goto_f
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_3c

    nop

    :goto_10
    invoke-virtual {p1, v1}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->setMultiSimSettingsSkiped(Z)V

    goto :goto_2e

    nop

    :goto_11
    if-nez v2, :cond_2

    goto :goto_32

    :cond_2
    goto :goto_6

    nop

    :goto_12
    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_c

    nop

    :goto_13
    return-void

    :goto_14
    goto :goto_d

    nop

    :goto_15
    invoke-virtual {p0, p1}, Lcom/android/provision/activities/DefaultActivity;->nextAction(I)V

    :goto_16
    goto :goto_13

    nop

    :goto_17
    const-string v1, "fromButton"

    goto :goto_b

    nop

    :goto_18
    const-string v1, "extra_mutisimsettings_force_skiped"

    goto :goto_5

    nop

    :goto_19
    return-void

    :goto_1a
    goto :goto_3

    nop

    :goto_1b
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    goto :goto_2

    nop

    :goto_1c
    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    goto :goto_3d

    nop

    :goto_1d
    const-string v1, "onActivityResult requestCode: "

    goto :goto_39

    nop

    :goto_1e
    const/4 p1, -0x1

    goto :goto_21

    nop

    :goto_1f
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_30

    nop

    :goto_20
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_1d

    nop

    :goto_21
    if-eq p2, p1, :cond_3

    goto :goto_16

    :cond_3
    goto :goto_0

    nop

    :goto_22
    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    goto :goto_36

    nop

    :goto_23
    if-nez p1, :cond_4

    goto :goto_28

    :cond_4
    goto :goto_37

    nop

    :goto_24
    invoke-static {}, Lcom/android/provision/Utils;->shouldNotFinishDefaultActivity()Z

    move-result v0

    goto :goto_7

    nop

    :goto_25
    invoke-virtual {p1, p3}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->setBootVideoSkiped(Z)V

    :goto_26
    goto :goto_1c

    nop

    :goto_27
    return-void

    :goto_28
    goto :goto_35

    nop

    :goto_29
    if-eq p1, v1, :cond_5

    goto :goto_34

    :cond_5
    goto :goto_3b

    nop

    :goto_2a
    return-void

    :goto_2b
    const-string v1, "extra_bootvideo_force_skiped"

    goto :goto_8

    nop

    :goto_2c
    if-nez p3, :cond_6

    goto :goto_26

    :cond_6
    goto :goto_38

    nop

    :goto_2d
    if-nez p3, :cond_7

    goto :goto_32

    :cond_7
    goto :goto_17

    nop

    :goto_2e
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    goto :goto_2b

    nop

    :goto_2f
    const-string v1, "Provision_DefaultActivity"

    goto :goto_12

    nop

    :goto_30
    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_31
    sput v1, Lcom/android/provision/activities/DefaultActivity;->MiMoverDirect:I

    :goto_32
    goto :goto_9

    nop

    :goto_33
    return-void

    :goto_34
    goto :goto_1b

    nop

    :goto_35
    const/16 p1, 0x7c

    goto :goto_15

    nop

    :goto_36
    invoke-static {p0}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->-$$Nest$mresumeState(Lcom/android/provision/activities/DefaultActivity$StateMachine;)V

    goto :goto_19

    nop

    :goto_37
    const/16 p1, 0x7d

    goto :goto_a

    nop

    :goto_38
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    goto :goto_18

    nop

    :goto_39
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_f

    nop

    :goto_3a
    if-eq p1, v0, :cond_8

    goto :goto_1a

    :cond_8
    goto :goto_24

    nop

    :goto_3b
    invoke-direct {p0, p1, p2}, Lcom/android/provision/activities/DefaultActivity;->onAuraActivityResult(II)V

    goto :goto_33

    nop

    :goto_3c
    const-string v1, " resultCode =  "

    goto :goto_1f

    nop

    :goto_3d
    invoke-virtual {p0, p2}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->run(I)V

    goto :goto_2a

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->onCreate(Landroid/os/Bundle;)V', 'const-string v0, "DefaultActivity onCreate"', 'const-string v1, "Provision_DefaultActivity"', 'invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I', 'invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->deviceIsProvisioned()Z', 'if-eqz v0, :cond_0', 'invoke-direct {p0, v2}, Lcom/android/provision/activities/DefaultActivity;->finishSetup(Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 9

    invoke-super {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->onCreate(Landroid/os/Bundle;)V

    const-string v0, "DefaultActivity onCreate"

    const-string v1, "Provision_DefaultActivity"

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->deviceIsProvisioned()Z

    move-result v0

    const/4 v2, 0x0

    if-eqz v0, :cond_0

    invoke-direct {p0, v2}, Lcom/android/provision/activities/DefaultActivity;->finishSetup(Z)V

    return-void

    :cond_0
    invoke-static {}, Lcom/android/provision/Utils;->isFlipDevice()Z

    move-result v0

    if-eqz v0, :cond_1

    invoke-static {p0}, Lcom/android/provision/Utils;->disableScreenshots(Landroid/app/Activity;)V

    new-instance v0, Landroid/content/Intent;

    const-class v3, Lcom/android/provision/CoverScreenService;

    invoke-direct {v0, p0, v3}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    invoke-virtual {p0, v0}, Landroid/app/Activity;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;

    :cond_1
    invoke-static {}, Lmiui/util/MiuiMultiDisplayTypeInfo;->isIndependentRearDevice()Z

    move-result v0

    const/4 v3, 0x1

    if-eqz v0, :cond_2

    new-instance v0, Landroid/content/Intent;

    const-class v4, Lcom/android/provision/activities/SubScreenActivity;

    invoke-direct {v0, p0, v4}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    const/high16 v4, 0x10000000

    invoke-virtual {v0, v4}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    invoke-static {}, Landroid/app/ActivityOptions;->makeBasic()Landroid/app/ActivityOptions;

    move-result-object v4

    invoke-virtual {v4, v3}, Landroid/app/ActivityOptions;->setLaunchDisplayId(I)Landroid/app/ActivityOptions;

    move-result-object v4

    invoke-virtual {v4}, Landroid/app/ActivityOptions;->toBundle()Landroid/os/Bundle;

    move-result-object v4

    invoke-virtual {p0, v0, v4}, Landroid/app/Activity;->startActivity(Landroid/content/Intent;Landroid/os/Bundle;)V

    :try_start_0
    iget-object v0, p0, Lcom/android/provision/activities/DefaultActivity;->mHandler:Landroid/os/Handler;

    new-instance v4, Lcom/android/provision/activities/DefaultActivity$$ExternalSyntheticLambda1;

    invoke-direct {v4, p0}, Lcom/android/provision/activities/DefaultActivity$$ExternalSyntheticLambda1;-><init>(Lcom/android/provision/activities/DefaultActivity;)V

    const-wide/16 v5, 0x3e8

    invoke-virtual {v0, v4, v5, v6}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v0

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "moveTaskToFront err: "

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :cond_2
    :goto_0
    invoke-static {}, Lcom/android/provision/utils/PageIntercepHelper;->getInstance()Lcom/android/provision/utils/PageIntercepHelper;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/provision/utils/PageIntercepHelper;->register()V

    invoke-static {}, Lcom/android/provision/utils/PageIntercepHelper;->getInstance()Lcom/android/provision/utils/PageIntercepHelper;

    move-result-object v0

    new-instance v4, Lcom/android/provision/activities/DefaultActivity$$ExternalSyntheticLambda2;

    invoke-direct {v4, p0}, Lcom/android/provision/activities/DefaultActivity$$ExternalSyntheticLambda2;-><init>(Lcom/android/provision/activities/DefaultActivity;)V

    invoke-virtual {v0, v4}, Lcom/android/provision/utils/PageIntercepHelper;->setCallback(Lcom/android/provision/utils/PageIntercepHelper$Callback;)V

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v0

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v4

    invoke-virtual {v0, v4}, Lcom/android/provision/utils/MccHelper;->isSupportTrustonic(Landroid/content/Context;)Z

    move-result v0

    if-eqz v0, :cond_3

    invoke-static {}, Lcom/android/provision/utils/UserManagerHelper;->getInstance()Lcom/android/provision/utils/UserManagerHelper;

    move-result-object v0

    invoke-virtual {v0, v3}, Lcom/android/provision/utils/UserManagerHelper;->disableUserSpace(Z)V

    :cond_3
    invoke-virtual {p0}, Landroid/app/Activity;->getApplication()Landroid/app/Application;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/utils/MiuiDockUtils;->disableInitDockStatus(Landroid/app/Application;)V

    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v4

    sput-wide v4, Lcom/android/provision/activities/DefaultActivity;->START_TIME:J

    new-instance v0, Landroid/content/Intent;

    const-string v4, "android.provision.action.PROVISION_START"

    invoke-direct {v0, v4}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->sendBroadcastAsUser(Landroid/content/Context;Landroid/content/Intent;)V

    new-instance v0, Lcom/android/provision/activities/DefaultActivity$StateMachine;

    invoke-direct {v0, p0}, Lcom/android/provision/activities/DefaultActivity$StateMachine;-><init>(Landroid/content/Context;)V

    iput-object v0, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    if-eqz p1, :cond_5

    const-string v0, "com.android.provision:state_enter_currentstate"

    invoke-virtual {p1, v0, v3}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z

    move-result p1

    if-eqz p1, :cond_4

    goto :goto_1

    :cond_4
    move v3, v2

    :cond_5
    :goto_1
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    invoke-virtual {p1, v3}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->start(Z)V

    new-instance p1, Landroid/content/Intent;

    const-class v0, Lcom/android/provision/AbnormalBackService;

    invoke-direct {p1, p0, v0}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    invoke-virtual {p0, p1}, Landroid/app/Activity;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;

    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p1, :cond_6

    new-instance v0, Landroid/content/Intent;

    const-class v2, Lcom/android/provision/StatusBarControllerService;

    invoke-direct {v0, p0, v2}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    invoke-virtual {p0, v0}, Landroid/app/Activity;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;

    goto :goto_2

    :cond_6
    invoke-static {p0, v2}, Lcom/android/provision/Utils;->enableStatusBar(Landroid/content/Context;Z)V

    :goto_2
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->initFullScreenMode()V

    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->registerNetworkChangedReceiver()V

    if-nez p1, :cond_7

    invoke-static {p0}, Lcom/android/provision/HomeSearchBarHelper;->checkAndSetHomeSearchBarOnProvision(Landroid/content/Context;)V

    :cond_7
    invoke-static {}, Lcom/android/provision/ProvisionStateHolder;->getInstance()Lcom/android/provision/ProvisionStateHolder;

    move-result-object v0

    iget-object v2, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    invoke-virtual {v0, v2}, Lcom/android/provision/ProvisionStateHolder;->setStateMachine(Lcom/android/provision/activities/DefaultActivity$StateMachine;)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    if-eqz v0, :cond_8

    const-string v0, "back button set accessibility no"

    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    const/4 v2, 0x2

    invoke-virtual {v0, v2}, Landroid/widget/ImageView;->setImportantForAccessibility(I)V

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    if-eqz v0, :cond_8

    const-string v0, "back button remove"

    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    invoke-virtual {v0}, Landroid/widget/ImageView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    check-cast v0, Landroid/view/ViewGroup;

    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :cond_8
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    if-eqz v0, :cond_9

    const/16 v1, 0x8

    invoke-virtual {v0, v1}, Landroid/widget/Button;->setVisibility(I)V

    :cond_9
    if-eqz p1, :cond_a

    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "android_id"

    invoke-static {v0, v1}, Landroid/provider/Settings$Secure;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    const-string v1, "ota_android_id"

    invoke-static {p1, v1, v0}, Landroid/provider/Settings$Secure;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    :cond_a
    invoke-static {p0}, Lcom/android/provision/utils/CspAutoSwitchManager;->deleteGLPA(Landroid/content/Context;)V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 9

    goto :goto_c

    nop

    :goto_0
    if-nez v0, :cond_0

    goto :goto_65

    :cond_0
    goto :goto_2f

    nop

    :goto_1
    invoke-static {p1, v1, v0}, Landroid/provider/Settings$Secure;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    :goto_2
    goto :goto_5d

    nop

    :goto_3
    invoke-virtual {v0, v1}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    :goto_4
    goto :goto_1b

    nop

    :goto_5
    invoke-static {v0}, Lcom/android/provision/utils/MiuiDockUtils;->disableInitDockStatus(Landroid/app/Application;)V

    goto :goto_2b

    nop

    :goto_6
    const-string v1, "ota_android_id"

    goto :goto_1

    nop

    :goto_7
    invoke-static {}, Lcom/android/provision/utils/PageIntercepHelper;->getInstance()Lcom/android/provision/utils/PageIntercepHelper;

    move-result-object v0

    goto :goto_66

    nop

    :goto_8
    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    goto :goto_f

    nop

    :goto_9
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v4

    goto :goto_31

    nop

    :goto_a
    invoke-static {}, Lcom/android/provision/utils/PageIntercepHelper;->getInstance()Lcom/android/provision/utils/PageIntercepHelper;

    move-result-object v0

    goto :goto_13

    nop

    :goto_b
    if-nez v0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_2c

    nop

    :goto_c
    invoke-super {p0, p1}, Lmiuix/provision/ProvisionBaseActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_54

    nop

    :goto_d
    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    goto :goto_37

    nop

    :goto_e
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_53

    nop

    :goto_f
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_79

    nop

    :goto_10
    invoke-static {}, Landroid/app/ActivityOptions;->makeBasic()Landroid/app/ActivityOptions;

    move-result-object v4

    goto :goto_67

    nop

    :goto_11
    iget-object v2, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    goto :goto_39

    nop

    :goto_12
    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_27

    nop

    :goto_13
    new-instance v4, Lcom/android/provision/activities/DefaultActivity$$ExternalSyntheticLambda2;

    goto :goto_4c

    nop

    :goto_14
    return-void

    :goto_15
    if-nez p1, :cond_2

    goto :goto_73

    :cond_2
    goto :goto_30

    nop

    :goto_16
    invoke-direct {v0, v4}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    goto :goto_56

    nop

    :goto_17
    const/4 v2, 0x0

    goto :goto_7e

    nop

    :goto_18
    invoke-virtual {v0}, Landroid/widget/ImageView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_78

    nop

    :goto_19
    invoke-virtual {v4}, Landroid/app/ActivityOptions;->toBundle()Landroid/os/Bundle;

    move-result-object v4

    goto :goto_1d

    nop

    :goto_1a
    new-instance v0, Landroid/content/Intent;

    goto :goto_1e

    nop

    :goto_1b
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mConfirmButton:Landroid/widget/Button;

    goto :goto_63

    nop

    :goto_1c
    invoke-static {p0}, Lcom/android/provision/Utils;->disableScreenshots(Landroid/app/Activity;)V

    goto :goto_21

    nop

    :goto_1d
    invoke-virtual {p0, v0, v4}, Landroid/app/Activity;->startActivity(Landroid/content/Intent;Landroid/os/Bundle;)V

    :try_start_0
    iget-object v0, p0, Lcom/android/provision/activities/DefaultActivity;->mHandler:Landroid/os/Handler;

    new-instance v4, Lcom/android/provision/activities/DefaultActivity$$ExternalSyntheticLambda1;

    invoke-direct {v4, p0}, Lcom/android/provision/activities/DefaultActivity$$ExternalSyntheticLambda1;-><init>(Lcom/android/provision/activities/DefaultActivity;)V

    const-wide/16 v5, 0x3e8

    invoke-virtual {v0, v4, v5, v6}, Landroid/os/Handler;->postDelayed(Ljava/lang/Runnable;J)Z
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_5b

    nop

    :goto_1e
    const-string v4, "android.provision.action.PROVISION_START"

    goto :goto_16

    nop

    :goto_1f
    if-nez v0, :cond_3

    goto :goto_7a

    :cond_3
    goto :goto_43

    nop

    :goto_20
    const/4 v2, 0x2

    goto :goto_33

    nop

    :goto_21
    new-instance v0, Landroid/content/Intent;

    goto :goto_42

    nop

    :goto_22
    invoke-direct {p1, p0, v0}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    goto :goto_77

    nop

    :goto_23
    invoke-virtual {p0}, Landroid/app/Activity;->getApplication()Landroid/app/Application;

    move-result-object v0

    goto :goto_5

    nop

    :goto_24
    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_68

    nop

    :goto_25
    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_41

    nop

    :goto_26
    const/16 v1, 0x8

    goto :goto_49

    nop

    :goto_27
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_20

    nop

    :goto_28
    invoke-static {}, Lcom/android/provision/Utils;->isFlipDevice()Z

    move-result v0

    goto :goto_5a

    nop

    :goto_29
    invoke-virtual {v0}, Landroid/widget/ImageView;->getParent()Landroid/view/ViewParent;

    move-result-object v0

    goto :goto_b

    nop

    :goto_2a
    const-string v1, "Provision_DefaultActivity"

    goto :goto_25

    nop

    :goto_2b
    invoke-static {}, Ljava/lang/System;->currentTimeMillis()J

    move-result-wide v4

    goto :goto_6b

    nop

    :goto_2c
    const-string v0, "back button remove"

    goto :goto_24

    nop

    :goto_2d
    const-string v0, "back button set accessibility no"

    goto :goto_12

    nop

    :goto_2e
    iget-object v1, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_3

    nop

    :goto_2f
    invoke-static {}, Lcom/android/provision/utils/UserManagerHelper;->getInstance()Lcom/android/provision/utils/UserManagerHelper;

    move-result-object v0

    goto :goto_64

    nop

    :goto_30
    const-string v0, "com.android.provision:state_enter_currentstate"

    goto :goto_74

    nop

    :goto_31
    invoke-virtual {v0, v4}, Lcom/android/provision/utils/MccHelper;->isSupportTrustonic(Landroid/content/Context;)Z

    move-result v0

    goto :goto_0

    nop

    :goto_32
    if-nez p1, :cond_4

    goto :goto_2

    :cond_4
    goto :goto_3b

    nop

    :goto_33
    invoke-virtual {v0, v2}, Landroid/widget/ImageView;->setImportantForAccessibility(I)V

    goto :goto_4e

    nop

    :goto_34
    const/high16 v4, 0x10000000

    goto :goto_6e

    nop

    :goto_35
    invoke-static {p0, v2}, Lcom/android/provision/Utils;->enableStatusBar(Landroid/content/Context;Z)V

    :goto_36
    goto :goto_3a

    nop

    :goto_37
    const-string v1, "android_id"

    goto :goto_51

    nop

    :goto_38
    const-class v0, Lcom/android/provision/AbnormalBackService;

    goto :goto_22

    nop

    :goto_39
    invoke-virtual {v0, v2}, Lcom/android/provision/ProvisionStateHolder;->setStateMachine(Lcom/android/provision/activities/DefaultActivity$StateMachine;)V

    goto :goto_69

    nop

    :goto_3a
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->initFullScreenMode()V

    goto :goto_44

    nop

    :goto_3b
    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object p1

    goto :goto_d

    nop

    :goto_3c
    goto :goto_36

    :goto_3d
    goto :goto_35

    nop

    :goto_3e
    return-void

    :goto_3f
    goto :goto_28

    nop

    :goto_40
    invoke-virtual {p1, v3}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->start(Z)V

    goto :goto_46

    nop

    :goto_41
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->deviceIsProvisioned()Z

    move-result v0

    goto :goto_17

    nop

    :goto_42
    const-class v3, Lcom/android/provision/CoverScreenService;

    goto :goto_6f

    nop

    :goto_43
    new-instance v0, Landroid/content/Intent;

    goto :goto_6c

    nop

    :goto_44
    if-eqz p1, :cond_5

    goto :goto_50

    :cond_5
    goto :goto_4f

    nop

    :goto_45
    invoke-static {}, Lcom/android/provision/ProvisionStateHolder;->getInstance()Lcom/android/provision/ProvisionStateHolder;

    move-result-object v0

    goto :goto_11

    nop

    :goto_46
    new-instance p1, Landroid/content/Intent;

    goto :goto_38

    nop

    :goto_47
    goto :goto_73

    :goto_48
    goto :goto_72

    nop

    :goto_49
    invoke-virtual {v0, v1}, Landroid/widget/Button;->setVisibility(I)V

    :goto_4a
    goto :goto_32

    nop

    :goto_4b
    invoke-virtual {v0, v4}, Lcom/android/provision/utils/PageIntercepHelper;->setCallback(Lcom/android/provision/utils/PageIntercepHelper$Callback;)V

    goto :goto_55

    nop

    :goto_4c
    invoke-direct {v4, p0}, Lcom/android/provision/activities/DefaultActivity$$ExternalSyntheticLambda2;-><init>(Lcom/android/provision/activities/DefaultActivity;)V

    goto :goto_4b

    nop

    :goto_4d
    invoke-direct {p0, v2}, Lcom/android/provision/activities/DefaultActivity;->finishSetup(Z)V

    goto :goto_3e

    nop

    :goto_4e
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_29

    nop

    :goto_4f
    invoke-static {p0}, Lcom/android/provision/HomeSearchBarHelper;->checkAndSetHomeSearchBarOnProvision(Landroid/content/Context;)V

    :goto_50
    goto :goto_45

    nop

    :goto_51
    invoke-static {v0, v1}, Landroid/provider/Settings$Secure;->getString(Landroid/content/ContentResolver;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    goto :goto_6

    nop

    :goto_52
    if-nez p1, :cond_6

    goto :goto_3d

    :cond_6
    goto :goto_60

    nop

    :goto_53
    const-string v5, "moveTaskToFront err: "

    goto :goto_75

    nop

    :goto_54
    const-string v0, "DefaultActivity onCreate"

    goto :goto_2a

    nop

    :goto_55
    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v0

    goto :goto_9

    nop

    :goto_56
    invoke-static {p0, v0}, Lcom/android/provision/Utils;->sendBroadcastAsUser(Landroid/content/Context;Landroid/content/Intent;)V

    goto :goto_59

    nop

    :goto_57
    iget-object p1, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    goto :goto_40

    nop

    :goto_58
    iput-object v0, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    goto :goto_15

    nop

    :goto_59
    new-instance v0, Lcom/android/provision/activities/DefaultActivity$StateMachine;

    goto :goto_62

    nop

    :goto_5a
    if-nez v0, :cond_7

    goto :goto_71

    :cond_7
    goto :goto_1c

    nop

    :goto_5b
    goto :goto_7a

    :catch_0
    move-exception v0

    goto :goto_61

    nop

    :goto_5c
    const-class v2, Lcom/android/provision/StatusBarControllerService;

    goto :goto_6a

    nop

    :goto_5d
    invoke-static {p0}, Lcom/android/provision/utils/CspAutoSwitchManager;->deleteGLPA(Landroid/content/Context;)V

    goto :goto_14

    nop

    :goto_5e
    invoke-static {}, Lmiui/util/MiuiMultiDisplayTypeInfo;->isIndependentRearDevice()Z

    move-result v0

    goto :goto_7d

    nop

    :goto_5f
    invoke-direct {v0, p0, v4}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    goto :goto_34

    nop

    :goto_60
    new-instance v0, Landroid/content/Intent;

    goto :goto_5c

    nop

    :goto_61
    new-instance v4, Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_62
    invoke-direct {v0, p0}, Lcom/android/provision/activities/DefaultActivity$StateMachine;-><init>(Landroid/content/Context;)V

    goto :goto_58

    nop

    :goto_63
    if-nez v0, :cond_8

    goto :goto_4a

    :cond_8
    goto :goto_26

    nop

    :goto_64
    invoke-virtual {v0, v3}, Lcom/android/provision/utils/UserManagerHelper;->disableUserSpace(Z)V

    :goto_65
    goto :goto_23

    nop

    :goto_66
    invoke-virtual {v0}, Lcom/android/provision/utils/PageIntercepHelper;->register()V

    goto :goto_a

    nop

    :goto_67
    invoke-virtual {v4, v3}, Landroid/app/ActivityOptions;->setLaunchDisplayId(I)Landroid/app/ActivityOptions;

    move-result-object v4

    goto :goto_19

    nop

    :goto_68
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_18

    nop

    :goto_69
    iget-object v0, p0, Lmiuix/provision/ProvisionBaseActivity;->mNewBackBtn:Landroid/widget/ImageView;

    goto :goto_7b

    nop

    :goto_6a
    invoke-direct {v0, p0, v2}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    goto :goto_7c

    nop

    :goto_6b
    sput-wide v4, Lcom/android/provision/activities/DefaultActivity;->START_TIME:J

    goto :goto_1a

    nop

    :goto_6c
    const-class v4, Lcom/android/provision/activities/SubScreenActivity;

    goto :goto_5f

    nop

    :goto_6d
    sget-boolean p1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    goto :goto_52

    nop

    :goto_6e
    invoke-virtual {v0, v4}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    goto :goto_10

    nop

    :goto_6f
    invoke-direct {v0, p0, v3}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    goto :goto_70

    nop

    :goto_70
    invoke-virtual {p0, v0}, Landroid/app/Activity;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;

    :goto_71
    goto :goto_5e

    nop

    :goto_72
    move v3, v2

    :goto_73
    goto :goto_57

    nop

    :goto_74
    invoke-virtual {p1, v0, v3}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z

    move-result p1

    goto :goto_76

    nop

    :goto_75
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_8

    nop

    :goto_76
    if-nez p1, :cond_9

    goto :goto_48

    :cond_9
    goto :goto_47

    nop

    :goto_77
    invoke-virtual {p0, p1}, Landroid/app/Activity;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;

    goto :goto_6d

    nop

    :goto_78
    check-cast v0, Landroid/view/ViewGroup;

    goto :goto_2e

    nop

    :goto_79
    invoke-static {v1, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    :goto_7a
    goto :goto_7

    nop

    :goto_7b
    if-nez v0, :cond_a

    goto :goto_4

    :cond_a
    goto :goto_2d

    nop

    :goto_7c
    invoke-virtual {p0, v0}, Landroid/app/Activity;->startService(Landroid/content/Intent;)Landroid/content/ComponentName;

    goto :goto_3c

    nop

    :goto_7d
    const/4 v3, 0x1

    goto :goto_1f

    nop

    :goto_7e
    if-nez v0, :cond_b

    goto :goto_3f

    :cond_b
    goto :goto_4d

    nop
.end method""",
        'required': True,
        'policy_status': 'BUILD_FLAG_PARTIALLY_SKIPPED',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-static {}, Lcom/android/provision/utils/PageIntercepHelper;->getInstance()Lcom/android/provision/utils/PageIntercepHelper;', 'invoke-virtual {v0}, Lcom/android/provision/utils/PageIntercepHelper;->unregisterReceiver()V', 'invoke-static {p0, v0}, Lcom/android/provision/Utils;->enableStatusBar(Landroid/content/Context;Z)V', 'invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->unRegisterNetworkChangedReceiver()V', 'invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onDestroy()V', 'invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->deviceIsProvisioned()Z', 'if-eqz p0, :cond_0', 'invoke-static {}, Landroid/os/Process;->myPid()I'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 2

    invoke-static {}, Lcom/android/provision/utils/PageIntercepHelper;->getInstance()Lcom/android/provision/utils/PageIntercepHelper;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/provision/utils/PageIntercepHelper;->unregisterReceiver()V

    const/4 v0, 0x1

    invoke-static {p0, v0}, Lcom/android/provision/Utils;->enableStatusBar(Landroid/content/Context;Z)V

    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->unRegisterNetworkChangedReceiver()V

    invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onDestroy()V

    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->deviceIsProvisioned()Z

    move-result p0

    if-eqz p0, :cond_0

    invoke-static {}, Landroid/os/Process;->myPid()I

    move-result p0

    invoke-static {p0}, Landroid/os/Process;->killProcess(I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 2

    goto :goto_8

    nop

    :goto_0
    const/4 v0, 0x1

    goto :goto_1

    nop

    :goto_1
    invoke-static {p0, v0}, Lcom/android/provision/Utils;->enableStatusBar(Landroid/content/Context;Z)V

    goto :goto_a

    nop

    :goto_2
    invoke-static {p0}, Landroid/os/Process;->killProcess(I)V

    :goto_3
    goto :goto_4

    nop

    :goto_4
    return-void

    :goto_5
    invoke-static {}, Landroid/os/Process;->myPid()I

    move-result p0

    goto :goto_2

    nop

    :goto_6
    invoke-direct {p0}, Lcom/android/provision/activities/DefaultActivity;->deviceIsProvisioned()Z

    move-result p0

    goto :goto_7

    nop

    :goto_7
    if-nez p0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_5

    nop

    :goto_8
    invoke-static {}, Lcom/android/provision/utils/PageIntercepHelper;->getInstance()Lcom/android/provision/utils/PageIntercepHelper;

    move-result-object v0

    goto :goto_9

    nop

    :goto_9
    invoke-virtual {v0}, Lcom/android/provision/utils/PageIntercepHelper;->unregisterReceiver()V

    goto :goto_0

    nop

    :goto_a
    invoke-super {p0}, Lmiuix/provision/ProvisionBaseActivity;->onDestroy()V

    goto :goto_6

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__onNewIntent',
        'method': '.method protected onNewIntent(Landroid/content/Intent;)V',
        'method_name': 'onNewIntent',
        'method_anchors': ['invoke-super {p0, p1}, Landroidx/fragment/app/FragmentActivity;->onNewIntent(Landroid/content/Intent;)V', 'invoke-static {p1}, Lcom/android/provision/EnterpriseNfcSetupHelper;->isProcessingNfcIntent(Landroid/content/Intent;)Z', 'if-eqz v0, :cond_0', 'const-string v0, "Provision_DefaultActivity"', 'const-string v1, " here is onNewIntent "', 'invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I', 'invoke-static {p0, p1, v0}, Lcom/android/provision/EnterpriseNfcSetupHelper;->startSavingNfcIntent(Landroid/app/Activity;Landroid/content/Intent;I)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onNewIntent(Landroid/content/Intent;)V
    .registers 4

    invoke-super {p0, p1}, Landroidx/fragment/app/FragmentActivity;->onNewIntent(Landroid/content/Intent;)V

    invoke-static {p1}, Lcom/android/provision/EnterpriseNfcSetupHelper;->isProcessingNfcIntent(Landroid/content/Intent;)Z

    move-result v0

    if-eqz v0, :cond_0

    const-string v0, "Provision_DefaultActivity"

    const-string v1, " here is onNewIntent "

    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    const/4 v0, 0x1

    invoke-static {p0, p1, v0}, Lcom/android/provision/EnterpriseNfcSetupHelper;->startSavingNfcIntent(Landroid/app/Activity;Landroid/content/Intent;I)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onNewIntent(Landroid/content/Intent;)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    const-string v0, "Provision_DefaultActivity"

    goto :goto_5

    nop

    :goto_1
    invoke-super {p0, p1}, Landroidx/fragment/app/FragmentActivity;->onNewIntent(Landroid/content/Intent;)V

    goto :goto_4

    nop

    :goto_2
    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_3

    nop

    :goto_3
    const/4 v0, 0x1

    goto :goto_8

    nop

    :goto_4
    invoke-static {p1}, Lcom/android/provision/EnterpriseNfcSetupHelper;->isProcessingNfcIntent(Landroid/content/Intent;)Z

    move-result v0

    goto :goto_6

    nop

    :goto_5
    const-string v1, " here is onNewIntent "

    goto :goto_2

    nop

    :goto_6
    if-nez v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_0

    nop

    :goto_7
    return-void

    :goto_8
    invoke-static {p0, p1, v0}, Lcom/android/provision/EnterpriseNfcSetupHelper;->startSavingNfcIntent(Landroid/app/Activity;Landroid/content/Intent;I)V

    :goto_9
    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_DefaultActivity__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState(Landroid/os/Bundle;)V',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onSaveInstanceState(Landroid/os/Bundle;)V', 'iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;', 'if-eqz p0, :cond_0', 'invoke-static {p0}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->-$$Nest$fgetmCurrentState(Lcom/android/provision/activities/DefaultActivity$StateMachine;)Lcom/android/provision/activities/DefaultActivity$State;', 'const-string v0, "com.android.provision:state_enter_currentstate"', 'invoke-virtual {p1, v0, p0}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onSaveInstanceState(Landroid/os/Bundle;)V

    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    if-eqz p0, :cond_0

    invoke-static {p0}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->-$$Nest$fgetmCurrentState(Lcom/android/provision/activities/DefaultActivity$StateMachine;)Lcom/android/provision/activities/DefaultActivity$State;

    move-result-object p0

    instance-of p0, p0, Lcom/android/provision/activities/DefaultActivity$StartupState;

    const-string v0, "com.android.provision:state_enter_currentstate"

    invoke-virtual {p1, v0, p0}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    :cond_0
    return-void
.end method""",
        'replacement': """.method protected onSaveInstanceState(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    invoke-static {p0}, Lcom/android/provision/activities/DefaultActivity$StateMachine;->-$$Nest$fgetmCurrentState(Lcom/android/provision/activities/DefaultActivity$StateMachine;)Lcom/android/provision/activities/DefaultActivity$State;

    move-result-object p0

    goto :goto_4

    nop

    :goto_1
    return-void

    :goto_2
    if-nez p0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_0

    nop

    :goto_3
    const-string v0, "com.android.provision:state_enter_currentstate"

    goto :goto_5

    nop

    :goto_4
    instance-of p0, p0, Lcom/android/provision/activities/DefaultActivity$StartupState;

    goto :goto_3

    nop

    :goto_5
    invoke-virtual {p1, v0, p0}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    :goto_6
    goto :goto_1

    nop

    :goto_7
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onSaveInstanceState(Landroid/os/Bundle;)V

    goto :goto_8

    nop

    :goto_8
    iget-object p0, p0, Lcom/android/provision/activities/DefaultActivity;->mStateMachine:Lcom/android/provision/activities/DefaultActivity$StateMachine;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
