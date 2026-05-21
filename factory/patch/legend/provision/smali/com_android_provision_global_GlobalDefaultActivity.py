TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/GlobalDefaultActivity.smali'
CLASS_FALLBACK_NAMES = ['GlobalDefaultActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;', '.field private static final AUTHORITY_FIND_DEVICE:Ljava/lang/String; = "com.xiaomi.finddevice.provider"', '.field private static final KEY_STATE_PREFIX:Ljava/lang/String; = "com.android.provision.STATE_"', '.field private static final PREF_STATE_GLOBAL:Ljava/lang/String; = "pref_state_global"', '.field private static final STATE_ENTER_CURRENTSTATE:Ljava/lang/String; = "com.android.provision:state_enter_currentstate"', '.field private static final TAG:Ljava/lang/String; = "GlobalDefaultActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__registerNetworkChangedReceiver',
        'method': '.method private registerNetworkChangedReceiver()V',
        'method_name': 'registerNetworkChangedReceiver',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'iget-boolean v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mIsNetworkRegistered:Z', 'if-nez v0, :cond_0', 'iput-boolean v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mIsNetworkRegistered:Z', 'new-instance v0, Lcom/android/provision/receiver/NetWorkChangedReceiver;', 'invoke-direct {v0}, Lcom/android/provision/receiver/NetWorkChangedReceiver;-><init>()V', 'iput-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;'],
        'type': 'method_delete',
        'search': """.method private registerNetworkChangedReceiver()V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    iget-boolean v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mIsNetworkRegistered:Z

    if-nez v0, :cond_0

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mIsNetworkRegistered:Z

    new-instance v0, Lcom/android/provision/receiver/NetWorkChangedReceiver;

    invoke-direct {v0}, Lcom/android/provision/receiver/NetWorkChangedReceiver;-><init>()V

    iput-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;

    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    const-string v1, "android.net.conn.CONNECTIVITY_CHANGE"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;

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
        'id': 'com_android_provision_global_GlobalDefaultActivity__unRegisterNetworkChangedReceiver',
        'method': '.method private unRegisterNetworkChangedReceiver()V',
        'method_name': 'unRegisterNetworkChangedReceiver',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'iget-boolean v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mIsNetworkRegistered:Z', 'if-eqz v0, :cond_0', 'iput-boolean v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mIsNetworkRegistered:Z', 'iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;', 'invoke-virtual {p0, v0}, Landroid/app/Activity;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V', 'return-void'],
        'type': 'method_delete',
        'search': """.method private unRegisterNetworkChangedReceiver()V
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    iget-boolean v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mIsNetworkRegistered:Z

    if-eqz v0, :cond_0

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mIsNetworkRegistered:Z

    iget-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;

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
        'id': 'com_android_provision_global_GlobalDefaultActivity__onActivityResult',
        'method': '.method protected onActivityResult(IILandroid/content/Intent;)V',
        'method_name': 'onActivityResult',
        'method_anchors': ['new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "onActivityResult requestCode="', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;', 'const-string p1, ", resultCode="', 'invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method protected onActivityResult(IILandroid/content/Intent;)V
    .registers 6

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "onActivityResult requestCode="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string p1, ", resultCode="

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    const-string v0, "GlobalDefaultActivity"

    invoke-static {v0, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    invoke-virtual {p1, p2, p3}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->onResult(ILandroid/content/Intent;)V

    if-eqz p3, :cond_0

    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    const-string v0, "extra_bootvideo_force_skiped"

    const/4 v1, 0x0

    invoke-virtual {p3, v0, v1}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result p3

    invoke-virtual {p1, p3}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->setBootVideoSkiped(Z)V

    :cond_0
    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    invoke-virtual {p0, p2}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->run(I)V

    return-void
.end method""",
        'replacement': """.method protected onActivityResult(IILandroid/content/Intent;)V
    .registers 6

    goto :goto_c

    nop

    :goto_0
    const-string v0, "extra_bootvideo_force_skiped"

    goto :goto_a

    nop

    :goto_1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_2
    invoke-virtual {p1, p2, p3}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->onResult(ILandroid/content/Intent;)V

    goto :goto_3

    nop

    :goto_3
    if-nez p3, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_12

    nop

    :goto_4
    const-string p1, ", resultCode="

    goto :goto_d

    nop

    :goto_5
    invoke-virtual {p0, p2}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->run(I)V

    goto :goto_6

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {p3, v0, v1}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result p3

    goto :goto_10

    nop

    :goto_8
    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    goto :goto_5

    nop

    :goto_9
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_4

    nop

    :goto_a
    const/4 v1, 0x0

    goto :goto_7

    nop

    :goto_b
    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    goto :goto_2

    nop

    :goto_c
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_d
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_14

    nop

    :goto_e
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_f

    nop

    :goto_f
    const-string v1, "onActivityResult requestCode="

    goto :goto_1

    nop

    :goto_10
    invoke-virtual {p1, p3}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->setBootVideoSkiped(Z)V

    :goto_11
    goto :goto_8

    nop

    :goto_12
    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    goto :goto_0

    nop

    :goto_13
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_16

    nop

    :goto_14
    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_13

    nop

    :goto_15
    invoke-static {v0, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_b

    nop

    :goto_16
    const-string v0, "GlobalDefaultActivity"

    goto :goto_15

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'new-instance v0, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;', 'invoke-direct {v0, p0}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;-><init>(Landroid/content/Context;)V', 'iput-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;', 'if-eqz p1, :cond_1', 'const-string v1, "com.android.provision:state_enter_currentstate"', 'invoke-virtual {p1, v1, v0}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z', 'if-eqz p1, :cond_0'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    new-instance v0, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    invoke-direct {v0, p0}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;-><init>(Landroid/content/Context;)V

    iput-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    const/4 v0, 0x1

    if-eqz p1, :cond_1

    const-string v1, "com.android.provision:state_enter_currentstate"

    invoke-virtual {p1, v1, v0}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z

    move-result p1

    if-eqz p1, :cond_0

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :cond_1
    :goto_0
    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    invoke-virtual {p1, v0}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->start(Z)V

    invoke-direct {p0}, Lcom/android/provision/global/GlobalDefaultActivity;->registerNetworkChangedReceiver()V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_1

    nop

    :goto_1
    new-instance v0, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    goto :goto_4

    nop

    :goto_2
    iput-object v0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    goto :goto_d

    nop

    :goto_3
    if-nez p1, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_a

    nop

    :goto_4
    invoke-direct {v0, p0}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;-><init>(Landroid/content/Context;)V

    goto :goto_2

    nop

    :goto_5
    if-nez p1, :cond_1

    goto :goto_f

    :cond_1
    goto :goto_6

    nop

    :goto_6
    const-string v1, "com.android.provision:state_enter_currentstate"

    goto :goto_7

    nop

    :goto_7
    invoke-virtual {p1, v1, v0}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z

    move-result p1

    goto :goto_3

    nop

    :goto_8
    iget-object p1, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    goto :goto_9

    nop

    :goto_9
    invoke-virtual {p1, v0}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->start(Z)V

    goto :goto_c

    nop

    :goto_a
    goto :goto_f

    :goto_b
    goto :goto_e

    nop

    :goto_c
    return-void

    :goto_d
    const/4 v0, 0x1

    goto :goto_5

    nop

    :goto_e
    const/4 v0, 0x0

    :goto_f
    goto :goto_8

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V', 'invoke-direct {p0}, Lcom/android/provision/global/GlobalDefaultActivity;->unRegisterNetworkChangedReceiver()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 1

    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    invoke-direct {p0}, Lcom/android/provision/global/GlobalDefaultActivity;->unRegisterNetworkChangedReceiver()V

    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

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
        'id': 'com_android_provision_global_GlobalDefaultActivity__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState(Landroid/os/Bundle;)V',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onSaveInstanceState(Landroid/os/Bundle;)V', 'iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;', 'invoke-static {p0}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->-$$Nest$fgetmCurrentState(Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;)Lcom/android/provision/global/GlobalDefaultActivity$State;', 'const-string v0, "com.android.provision:state_enter_currentstate"', 'invoke-virtual {p1, v0, p0}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onSaveInstanceState(Landroid/os/Bundle;)V

    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    invoke-static {p0}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->-$$Nest$fgetmCurrentState(Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;)Lcom/android/provision/global/GlobalDefaultActivity$State;

    move-result-object p0

    instance-of p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$AccountState;

    const-string v0, "com.android.provision:state_enter_currentstate"

    invoke-virtual {p1, v0, p0}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    return-void
.end method""",
        'replacement': """.method protected onSaveInstanceState(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    instance-of p0, p0, Lcom/android/provision/global/GlobalDefaultActivity$AccountState;

    goto :goto_5

    nop

    :goto_1
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onSaveInstanceState(Landroid/os/Bundle;)V

    goto :goto_2

    nop

    :goto_2
    iget-object p0, p0, Lcom/android/provision/global/GlobalDefaultActivity;->mStateMachine:Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p1, v0, p0}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    goto :goto_6

    nop

    :goto_4
    invoke-static {p0}, Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;->-$$Nest$fgetmCurrentState(Lcom/android/provision/global/GlobalDefaultActivity$StateMachine;)Lcom/android/provision/global/GlobalDefaultActivity$State;

    move-result-object p0

    goto :goto_0

    nop

    :goto_5
    const-string v0, "com.android.provision:state_enter_currentstate"

    goto :goto_3

    nop

    :goto_6
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_global_GlobalDefaultActivity__onStart',
        'method': '.method protected onStart()V',
        'method_name': 'onStart',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onStart()V', 'invoke-virtual {p0, v0}, Landroid/app/Activity;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;', 'check-cast p0, Landroid/app/admin/DevicePolicyManager;', 'invoke-virtual {p0}, Landroid/app/admin/DevicePolicyManager;->getUserProvisioningState()I', 'sput p0, Lcom/android/provision/global/GlobalDefaultActivity;->sUserProvisioningState:I', 'new-instance p0, Ljava/lang/StringBuilder;', 'invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v0, "GlobalDefaultActivity getUserProvisioningState="'],
        'type': 'method_replace',
        'search': """.method protected onStart()V
    .registers 2

    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onStart()V

    const-class v0, Landroid/app/admin/DevicePolicyManager;

    invoke-virtual {p0, v0}, Landroid/app/Activity;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object p0

    check-cast p0, Landroid/app/admin/DevicePolicyManager;

    invoke-virtual {p0}, Landroid/app/admin/DevicePolicyManager;->getUserProvisioningState()I

    move-result p0

    sput p0, Lcom/android/provision/global/GlobalDefaultActivity;->sUserProvisioningState:I

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "GlobalDefaultActivity getUserProvisioningState="

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v0, Lcom/android/provision/global/GlobalDefaultActivity;->sUserProvisioningState:I

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string v0, "GlobalDefaultActivity"

    invoke-static {v0, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method""",
        'replacement': """.method protected onStart()V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_a

    nop

    :goto_1
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_c

    nop

    :goto_2
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_8

    nop

    :goto_3
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_2

    nop

    :goto_4
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onStart()V

    goto :goto_d

    nop

    :goto_5
    check-cast p0, Landroid/app/admin/DevicePolicyManager;

    goto :goto_7

    nop

    :goto_6
    return-void

    :goto_7
    invoke-virtual {p0}, Landroid/app/admin/DevicePolicyManager;->getUserProvisioningState()I

    move-result p0

    goto :goto_b

    nop

    :goto_8
    const-string v0, "GlobalDefaultActivity"

    goto :goto_9

    nop

    :goto_9
    invoke-static {v0, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_6

    nop

    :goto_a
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_f

    nop

    :goto_b
    sput p0, Lcom/android/provision/global/GlobalDefaultActivity;->sUserProvisioningState:I

    goto :goto_0

    nop

    :goto_c
    sget v0, Lcom/android/provision/global/GlobalDefaultActivity;->sUserProvisioningState:I

    goto :goto_3

    nop

    :goto_d
    const-class v0, Landroid/app/admin/DevicePolicyManager;

    goto :goto_e

    nop

    :goto_e
    invoke-virtual {p0, v0}, Landroid/app/Activity;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_5

    nop

    :goto_f
    const-string v0, "GlobalDefaultActivity getUserProvisioningState="

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
