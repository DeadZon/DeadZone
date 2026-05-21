TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/SplitAndReorganizedFlow.smali'
CLASS_FALLBACK_NAMES = ['SplitAndReorganizedFlow.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;', '.field private static final KEY_STATE_PREFIX:Ljava/lang/String; = "com.android.provision.STATE_"', '.field private static final NO_CONNECTION:I = 0x1', '.field private static final PREF_STATE_GLOBAL:Ljava/lang/String; = "pref_state_quick_start_global"', '.field private static final STATE_ENTER_CURRENTSTATE:Ljava/lang/String; = "com.android.provision:state_enter_currentstate"', '.field private static final TAG:Ljava/lang/String; = "SplitAndReorganizedFlow"']

PATCHES = [
    {
        'id': 'com_android_provision_global_SplitAndReorganizedFlow__registerNetworkChangedReceiver',
        'method': '.method private registerNetworkChangedReceiver()V',
        'method_name': 'registerNetworkChangedReceiver',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'iget-boolean v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mIsNetworkRegistered:Z', 'if-nez v0, :cond_0', 'iput-boolean v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mIsNetworkRegistered:Z', 'new-instance v0, Lcom/android/provision/receiver/NetWorkChangedReceiver;', 'invoke-direct {v0}, Lcom/android/provision/receiver/NetWorkChangedReceiver;-><init>()V', 'iput-object v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;'],
        'type': 'method_delete',
        'search': """.method private registerNetworkChangedReceiver()V
    .registers 3

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    iget-boolean v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mIsNetworkRegistered:Z

    if-nez v0, :cond_0

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mIsNetworkRegistered:Z

    new-instance v0, Lcom/android/provision/receiver/NetWorkChangedReceiver;

    invoke-direct {v0}, Lcom/android/provision/receiver/NetWorkChangedReceiver;-><init>()V

    iput-object v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;

    new-instance v0, Landroid/content/IntentFilter;

    invoke-direct {v0}, Landroid/content/IntentFilter;-><init>()V

    const-string v1, "android.net.conn.CONNECTIVITY_CHANGE"

    invoke-virtual {v0, v1}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;

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
        'id': 'com_android_provision_global_SplitAndReorganizedFlow__unRegisterNetworkChangedReceiver',
        'method': '.method private unRegisterNetworkChangedReceiver()V',
        'method_name': 'unRegisterNetworkChangedReceiver',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'iget-boolean v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mIsNetworkRegistered:Z', 'if-eqz v0, :cond_0', 'iput-boolean v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mIsNetworkRegistered:Z', 'iget-object v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;', 'invoke-virtual {p0, v0}, Landroid/app/Activity;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V', 'return-void'],
        'type': 'method_delete',
        'search': """.method private unRegisterNetworkChangedReceiver()V
    .registers 2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    iget-boolean v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mIsNetworkRegistered:Z

    if-eqz v0, :cond_0

    const/4 v0, 0x0

    iput-boolean v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mIsNetworkRegistered:Z

    iget-object v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mNetorkReceiver:Lcom/android/provision/receiver/NetWorkChangedReceiver;

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
        'id': 'com_android_provision_global_SplitAndReorganizedFlow__onActivityResult',
        'method': '.method protected onActivityResult(IILandroid/content/Intent;)V',
        'method_name': 'onActivityResult',
        'method_anchors': ['new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "onActivityResult requestCode: "', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;', 'const-string v1, " resultCode =  "', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;', 'invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;'],
        'type': 'method_replace',
        'search': """.method protected onActivityResult(IILandroid/content/Intent;)V
    .registers 8

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

    const-string v1, "SplitAndReorganizedFlow"

    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    const/16 v0, 0x21

    if-ne p1, v0, :cond_0

    const-string p1, " BACK FROM GOOGLE WIZARD"

    invoke-static {v1, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object p0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    invoke-static {p0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->-$$Nest$mresumeState(Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;)V

    return-void

    :cond_0
    const-string p1, "SplitAndReorganizedFlow onActivityResult "

    invoke-static {v1, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    if-eqz p3, :cond_1

    const-string p1, "eSim"

    const/4 v0, -0x1

    invoke-virtual {p3, p1, v0}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I

    move-result p1

    sput p1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimeCode:I

    new-instance p1, Ljava/lang/StringBuilder;

    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, " eSimeCode-> "

    invoke-virtual {p1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v2, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimeCode:I

    invoke-virtual {p1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    invoke-static {v1, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    const-string p1, "eSim_GL"

    invoke-virtual {p3, p1, v0}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I

    move-result p1

    sput p1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimCode:I

    :cond_1
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result p1

    if-eqz p1, :cond_2

    iget-object p1, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    invoke-virtual {p1}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->getCurrentState()Lcom/android/provision/global/State;

    move-result-object p1

    instance-of p1, p1, Lcom/android/provision/global/EsimDateState;

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, " isESimStateBack is "

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    const-string v2, " and SIM2 is "

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const/4 v2, 0x1

    invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result v3

    invoke-static {p0, v3}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object v3

    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    xor-int/2addr v3, v2

    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-eqz p1, :cond_2

    invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result p1

    invoke-static {p0, p1}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object p1

    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    if-nez p1, :cond_2

    iget-object p0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    invoke-static {p0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->-$$Nest$mtransitToNext(Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;)V

    return-void

    :cond_2
    if-eqz p3, :cond_3

    iget-object p1, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    const-string v0, "extra_mutisimsettings_force_skiped"

    const/4 v1, 0x0

    invoke-virtual {p3, v0, v1}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result p3

    invoke-virtual {p1, p3}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->setMultiSimSettingsSkiped(Z)V

    :cond_3
    iget-object p0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    invoke-virtual {p0, p2}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->run(I)V

    return-void
.end method""",
        'replacement': """.method protected onActivityResult(IILandroid/content/Intent;)V
    .registers 8

    goto :goto_1a

    nop

    :goto_0
    invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result p1

    goto :goto_10

    nop

    :goto_1
    invoke-static {v1, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_24

    nop

    :goto_2
    invoke-static {p1}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result p1

    goto :goto_1c

    nop

    :goto_3
    invoke-static {v1, p1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_3e

    nop

    :goto_4
    const-string v0, "extra_mutisimsettings_force_skiped"

    goto :goto_f

    nop

    :goto_5
    invoke-virtual {p1, p3}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->setMultiSimSettingsSkiped(Z)V

    :goto_6
    goto :goto_3a

    nop

    :goto_7
    invoke-static {p0, v2}, Lcom/android/provision/SimInfoUtils;->getSubIdForSlotId(Landroid/content/Context;I)I

    move-result v3

    goto :goto_15

    nop

    :goto_8
    sput p1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimCode:I

    :goto_9
    goto :goto_38

    nop

    :goto_a
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_28

    nop

    :goto_b
    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_2f

    nop

    :goto_c
    if-nez p3, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_1f

    nop

    :goto_d
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_2d

    nop

    :goto_e
    const-string v2, " isESimStateBack is "

    goto :goto_d

    nop

    :goto_f
    const/4 v1, 0x0

    goto :goto_42

    nop

    :goto_10
    invoke-static {p0, p1}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object p1

    goto :goto_2

    nop

    :goto_11
    return-void

    :goto_12
    goto :goto_c

    nop

    :goto_13
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_18

    nop

    :goto_14
    iget-object p0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    goto :goto_31

    nop

    :goto_15
    invoke-static {p0, v3}, Lcom/android/provision/SimInfoUtils;->getIccid(Landroid/content/Context;I)Ljava/lang/String;

    move-result-object v3

    goto :goto_26

    nop

    :goto_16
    sput p1, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimeCode:I

    goto :goto_47

    nop

    :goto_17
    return-void

    :goto_18
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_e

    nop

    :goto_19
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_4b

    nop

    :goto_1a
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_19

    nop

    :goto_1b
    sget v2, Lcom/android/provision/global/SplitAndReorganizedFlow;->eSimeCode:I

    goto :goto_1d

    nop

    :goto_1c
    if-eqz p1, :cond_1

    goto :goto_12

    :cond_1
    goto :goto_14

    nop

    :goto_1d
    invoke-virtual {p1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_3d

    nop

    :goto_1e
    if-nez p1, :cond_2

    goto :goto_12

    :cond_2
    goto :goto_0

    nop

    :goto_1f
    iget-object p1, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    goto :goto_4

    nop

    :goto_20
    return-void

    :goto_21
    goto :goto_32

    nop

    :goto_22
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_25

    nop

    :goto_23
    invoke-virtual {p3, p1, v0}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I

    move-result p1

    goto :goto_8

    nop

    :goto_24
    const-string p1, "eSim_GL"

    goto :goto_23

    nop

    :goto_25
    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_a

    nop

    :goto_26
    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    goto :goto_49

    nop

    :goto_27
    if-nez p1, :cond_3

    goto :goto_12

    :cond_3
    goto :goto_2b

    nop

    :goto_28
    const-string v1, "SplitAndReorganizedFlow"

    goto :goto_b

    nop

    :goto_29
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_2c

    nop

    :goto_2a
    const-string p1, " BACK FROM GOOGLE WIZARD"

    goto :goto_2e

    nop

    :goto_2b
    iget-object p1, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    goto :goto_46

    nop

    :goto_2c
    const-string v1, " resultCode =  "

    goto :goto_22

    nop

    :goto_2d
    invoke-virtual {v0, p1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_39

    nop

    :goto_2e
    invoke-static {v1, p1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_45

    nop

    :goto_2f
    const/16 v0, 0x21

    goto :goto_3b

    nop

    :goto_30
    invoke-direct {p1}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_4c

    nop

    :goto_31
    invoke-static {p0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->-$$Nest$mtransitToNext(Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;)V

    goto :goto_11

    nop

    :goto_32
    const-string p1, "SplitAndReorganizedFlow onActivityResult "

    goto :goto_3

    nop

    :goto_33
    instance-of p1, p1, Lcom/android/provision/global/EsimDateState;

    goto :goto_13

    nop

    :goto_34
    const-string p1, "eSim"

    goto :goto_35

    nop

    :goto_35
    const/4 v0, -0x1

    goto :goto_40

    nop

    :goto_36
    invoke-static {p0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->-$$Nest$mresumeState(Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;)V

    goto :goto_20

    nop

    :goto_37
    invoke-virtual {p0, p2}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->run(I)V

    goto :goto_17

    nop

    :goto_38
    invoke-static {}, Lcom/android/provision/Utils;->isCustForESIMFeature()Z

    move-result p1

    goto :goto_27

    nop

    :goto_39
    const-string v2, " and SIM2 is "

    goto :goto_3f

    nop

    :goto_3a
    iget-object p0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    goto :goto_37

    nop

    :goto_3b
    if-eq p1, v0, :cond_4

    goto :goto_21

    :cond_4
    goto :goto_2a

    nop

    :goto_3c
    invoke-virtual {p1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_1b

    nop

    :goto_3d
    invoke-virtual {p1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p1

    goto :goto_1

    nop

    :goto_3e
    if-nez p3, :cond_5

    goto :goto_9

    :cond_5
    goto :goto_34

    nop

    :goto_3f
    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_43

    nop

    :goto_40
    invoke-virtual {p3, p1, v0}, Landroid/content/Intent;->getIntExtra(Ljava/lang/String;I)I

    move-result p1

    goto :goto_16

    nop

    :goto_41
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_29

    nop

    :goto_42
    invoke-virtual {p3, v0, v1}, Landroid/content/Intent;->getBooleanExtra(Ljava/lang/String;Z)Z

    move-result p3

    goto :goto_5

    nop

    :goto_43
    const/4 v2, 0x1

    goto :goto_7

    nop

    :goto_44
    invoke-virtual {v0, v3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_4a

    nop

    :goto_45
    iget-object p0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    goto :goto_36

    nop

    :goto_46
    invoke-virtual {p1}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->getCurrentState()Lcom/android/provision/global/State;

    move-result-object p1

    goto :goto_33

    nop

    :goto_47
    new-instance p1, Ljava/lang/StringBuilder;

    goto :goto_30

    nop

    :goto_48
    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1e

    nop

    :goto_49
    xor-int/2addr v3, v2

    goto :goto_44

    nop

    :goto_4a
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_48

    nop

    :goto_4b
    const-string v1, "onActivityResult requestCode: "

    goto :goto_41

    nop

    :goto_4c
    const-string v2, " eSimeCode-> "

    goto :goto_3c

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_global_SplitAndReorganizedFlow__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'const-string v0, "SplitAndReorganizedFlow"', 'const-string v1, " here is in onCreate "', 'invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I', 'new-instance v0, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;', 'invoke-direct {v0, p0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;-><init>(Landroid/content/Context;)V', 'iput-object v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;', 'if-eqz p1, :cond_1'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    const-string v0, "SplitAndReorganizedFlow"

    const-string v1, " here is in onCreate "

    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    new-instance v0, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    invoke-direct {v0, p0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;-><init>(Landroid/content/Context;)V

    iput-object v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

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
    iget-object p1, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    invoke-virtual {p1, v0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->start(Z)V

    invoke-direct {p0}, Lcom/android/provision/global/SplitAndReorganizedFlow;->registerNetworkChangedReceiver()V

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 4

    goto :goto_6

    nop

    :goto_0
    const/4 v0, 0x0

    :goto_1
    goto :goto_10

    nop

    :goto_2
    invoke-static {v0, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_9

    nop

    :goto_3
    goto :goto_1

    :goto_4
    goto :goto_0

    nop

    :goto_5
    return-void

    :goto_6
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_e

    nop

    :goto_7
    invoke-direct {v0, p0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;-><init>(Landroid/content/Context;)V

    goto :goto_12

    nop

    :goto_8
    const-string v1, "com.android.provision:state_enter_currentstate"

    goto :goto_d

    nop

    :goto_9
    new-instance v0, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    goto :goto_7

    nop

    :goto_a
    if-nez p1, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_3

    nop

    :goto_b
    invoke-virtual {p1, v0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->start(Z)V

    goto :goto_5

    nop

    :goto_c
    const-string v1, " here is in onCreate "

    goto :goto_2

    nop

    :goto_d
    invoke-virtual {p1, v1, v0}, Landroid/os/Bundle;->getBoolean(Ljava/lang/String;Z)Z

    move-result p1

    goto :goto_a

    nop

    :goto_e
    const-string v0, "SplitAndReorganizedFlow"

    goto :goto_c

    nop

    :goto_f
    if-nez p1, :cond_1

    goto :goto_1

    :cond_1
    goto :goto_8

    nop

    :goto_10
    iget-object p1, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    goto :goto_b

    nop

    :goto_11
    const/4 v0, 0x1

    goto :goto_f

    nop

    :goto_12
    iput-object v0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    goto :goto_11

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_global_SplitAndReorganizedFlow__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V', 'invoke-direct {p0}, Lcom/android/provision/global/SplitAndReorganizedFlow;->unRegisterNetworkChangedReceiver()V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 1

    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    invoke-direct {p0}, Lcom/android/provision/global/SplitAndReorganizedFlow;->unRegisterNetworkChangedReceiver()V

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
        'id': 'com_android_provision_global_SplitAndReorganizedFlow__onSaveInstanceState',
        'method': '.method protected onSaveInstanceState(Landroid/os/Bundle;)V',
        'method_name': 'onSaveInstanceState',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onSaveInstanceState(Landroid/os/Bundle;)V', 'iget-object p0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;', 'invoke-static {p0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->-$$Nest$fgetmCurrentState(Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;)Lcom/android/provision/global/State;', 'const-string v0, "com.android.provision:state_enter_currentstate"', 'invoke-virtual {p1, v0, p0}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onSaveInstanceState(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onSaveInstanceState(Landroid/os/Bundle;)V

    iget-object p0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    invoke-static {p0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->-$$Nest$fgetmCurrentState(Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;)Lcom/android/provision/global/State;

    move-result-object p0

    instance-of p0, p0, Lcom/android/provision/global/SimCardDetectionState;

    const-string v0, "com.android.provision:state_enter_currentstate"

    invoke-virtual {p1, v0, p0}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    return-void
.end method""",
        'replacement': """.method protected onSaveInstanceState(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onSaveInstanceState(Landroid/os/Bundle;)V

    goto :goto_5

    nop

    :goto_1
    return-void

    :goto_2
    instance-of p0, p0, Lcom/android/provision/global/SimCardDetectionState;

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p1, v0, p0}, Landroid/os/Bundle;->putBoolean(Ljava/lang/String;Z)V

    goto :goto_1

    nop

    :goto_4
    const-string v0, "com.android.provision:state_enter_currentstate"

    goto :goto_3

    nop

    :goto_5
    iget-object p0, p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->mStateMachine:Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;

    goto :goto_6

    nop

    :goto_6
    invoke-static {p0}, Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;->-$$Nest$fgetmCurrentState(Lcom/android/provision/global/SplitAndReorganizedFlow$StateMachine;)Lcom/android/provision/global/State;

    move-result-object p0

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_global_SplitAndReorganizedFlow__onStart',
        'method': '.method protected onStart()V',
        'method_name': 'onStart',
        'method_anchors': ['invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onStart()V', 'invoke-virtual {p0, v0}, Landroid/app/Activity;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;', 'check-cast p0, Landroid/app/admin/DevicePolicyManager;', 'invoke-virtual {p0}, Landroid/app/admin/DevicePolicyManager;->getUserProvisioningState()I', 'sput p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->sUserProvisioningState:I', 'new-instance p0, Ljava/lang/StringBuilder;', 'invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v0, "SplitAndReorganizedFlow getUserProvisioningState="'],
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

    sput p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->sUserProvisioningState:I

    new-instance p0, Ljava/lang/StringBuilder;

    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v0, "SplitAndReorganizedFlow getUserProvisioningState="

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget v0, Lcom/android/provision/global/SplitAndReorganizedFlow;->sUserProvisioningState:I

    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    const-string v0, "SplitAndReorganizedFlow"

    invoke-static {v0, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method""",
        'replacement': """.method protected onStart()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    const-string v0, "SplitAndReorganizedFlow"

    goto :goto_5

    nop

    :goto_1
    invoke-super {p0}, Landroidx/fragment/app/FragmentActivity;->onStart()V

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_9

    nop

    :goto_3
    invoke-virtual {p0, v0}, Landroid/app/Activity;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object p0

    goto :goto_c

    nop

    :goto_4
    const-class v0, Landroid/app/admin/DevicePolicyManager;

    goto :goto_3

    nop

    :goto_5
    invoke-static {v0, p0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_b

    nop

    :goto_6
    new-instance p0, Ljava/lang/StringBuilder;

    goto :goto_e

    nop

    :goto_7
    invoke-virtual {p0, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_d

    nop

    :goto_8
    sput p0, Lcom/android/provision/global/SplitAndReorganizedFlow;->sUserProvisioningState:I

    goto :goto_6

    nop

    :goto_9
    invoke-virtual {p0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object p0

    goto :goto_0

    nop

    :goto_a
    invoke-virtual {p0}, Landroid/app/admin/DevicePolicyManager;->getUserProvisioningState()I

    move-result p0

    goto :goto_8

    nop

    :goto_b
    return-void

    :goto_c
    check-cast p0, Landroid/app/admin/DevicePolicyManager;

    goto :goto_a

    nop

    :goto_d
    sget v0, Lcom/android/provision/global/SplitAndReorganizedFlow;->sUserProvisioningState:I

    goto :goto_2

    nop

    :goto_e
    invoke-direct {p0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_f

    nop

    :goto_f
    const-string v0, "SplitAndReorganizedFlow getUserProvisioningState="

    goto :goto_7

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
