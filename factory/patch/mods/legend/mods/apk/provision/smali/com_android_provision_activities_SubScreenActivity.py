TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/activities/SubScreenActivity.smali'
CLASS_FALLBACK_NAMES = ['SubScreenActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;', '.field private static final DOZE_WAKE_LOCK_TAG:Ljava/lang/String; = "dream:doze"', '.field private static final SCREEN_OFF:Ljava/lang/String; = "android.intent.action.SCREEN_OFF"', '.field private static final SCREEN_ON:Ljava/lang/String; = "android.intent.action.SCREEN_ON"', '.field private static final TAG:Ljava/lang/String; = "SubScreenActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_activities_SubScreenActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'sget p1, Lcom/android/provision/R$layout;->sub_screen_layout:I', 'invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setContentView(I)V', 'sget p1, Lcom/android/provision/R$id;->logo_image:I', 'invoke-virtual {p0, p1}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;', 'check-cast p1, Landroid/widget/ImageView;', 'iput-object p1, p0, Lcom/android/provision/activities/SubScreenActivity;->mLogoImage:Landroid/widget/ImageView;', 'sget v0, Lcom/android/provision/R$drawable;->ic_sub_image:I'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    sget p1, Lcom/android/provision/R$layout;->sub_screen_layout:I

    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setContentView(I)V

    sget p1, Lcom/android/provision/R$id;->logo_image:I

    invoke-virtual {p0, p1}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    check-cast p1, Landroid/widget/ImageView;

    iput-object p1, p0, Lcom/android/provision/activities/SubScreenActivity;->mLogoImage:Landroid/widget/ImageView;

    sget v0, Lcom/android/provision/R$drawable;->ic_sub_image:I

    invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setImageResource(I)V

    invoke-static {p0}, Lcom/android/provision/utils/ActivityCollector;->addActivity(Landroid/app/Activity;)V

    invoke-direct {p0}, Lcom/android/provision/activities/SubScreenActivity;->initPowerManager()V

    new-instance p1, Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;

    const/4 v0, 0x0

    invoke-direct {p1, p0, v0}, Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;-><init>(Lcom/android/provision/activities/SubScreenActivity;Lcom/android/provision/activities/SubScreenActivity-IA;)V

    iput-object p1, p0, Lcom/android/provision/activities/SubScreenActivity;->mScreenPowerChangeReceiver:Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;

    new-instance p1, Landroid/content/IntentFilter;

    invoke-direct {p1}, Landroid/content/IntentFilter;-><init>()V

    const-string v0, "android.intent.action.SCREEN_ON"

    invoke-virtual {p1, v0}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    const-string v0, "android.intent.action.SCREEN_OFF"

    invoke-virtual {p1, v0}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    iget-object v0, p0, Lcom/android/provision/activities/SubScreenActivity;->mScreenPowerChangeReceiver:Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;

    invoke-virtual {p0, v0, p1}, Landroid/app/Activity;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_15

    nop

    :goto_1
    const-string v0, "android.intent.action.SCREEN_ON"

    goto :goto_c

    nop

    :goto_2
    iput-object p1, p0, Lcom/android/provision/activities/SubScreenActivity;->mLogoImage:Landroid/widget/ImageView;

    goto :goto_7

    nop

    :goto_3
    invoke-virtual {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->setContentView(I)V

    goto :goto_11

    nop

    :goto_4
    const-string v0, "android.intent.action.SCREEN_OFF"

    goto :goto_16

    nop

    :goto_5
    invoke-static {p0}, Lcom/android/provision/utils/ActivityCollector;->addActivity(Landroid/app/Activity;)V

    goto :goto_f

    nop

    :goto_6
    invoke-virtual {p0, v0, p1}, Landroid/app/Activity;->registerReceiver(Landroid/content/BroadcastReceiver;Landroid/content/IntentFilter;)Landroid/content/Intent;

    goto :goto_14

    nop

    :goto_7
    sget v0, Lcom/android/provision/R$drawable;->ic_sub_image:I

    goto :goto_10

    nop

    :goto_8
    new-instance p1, Landroid/content/IntentFilter;

    goto :goto_12

    nop

    :goto_9
    const/4 v0, 0x0

    goto :goto_e

    nop

    :goto_a
    new-instance p1, Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;

    goto :goto_9

    nop

    :goto_b
    iget-object v0, p0, Lcom/android/provision/activities/SubScreenActivity;->mScreenPowerChangeReceiver:Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;

    goto :goto_6

    nop

    :goto_c
    invoke-virtual {p1, v0}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto :goto_4

    nop

    :goto_d
    invoke-virtual {p0, p1}, Landroid/app/Activity;->findViewById(I)Landroid/view/View;

    move-result-object p1

    goto :goto_17

    nop

    :goto_e
    invoke-direct {p1, p0, v0}, Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;-><init>(Lcom/android/provision/activities/SubScreenActivity;Lcom/android/provision/activities/SubScreenActivity-IA;)V

    goto :goto_13

    nop

    :goto_f
    invoke-direct {p0}, Lcom/android/provision/activities/SubScreenActivity;->initPowerManager()V

    goto :goto_a

    nop

    :goto_10
    invoke-virtual {p1, v0}, Landroid/widget/ImageView;->setImageResource(I)V

    goto :goto_5

    nop

    :goto_11
    sget p1, Lcom/android/provision/R$id;->logo_image:I

    goto :goto_d

    nop

    :goto_12
    invoke-direct {p1}, Landroid/content/IntentFilter;-><init>()V

    goto :goto_1

    nop

    :goto_13
    iput-object p1, p0, Lcom/android/provision/activities/SubScreenActivity;->mScreenPowerChangeReceiver:Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;

    goto :goto_8

    nop

    :goto_14
    return-void

    :goto_15
    sget p1, Lcom/android/provision/R$layout;->sub_screen_layout:I

    goto :goto_3

    nop

    :goto_16
    invoke-virtual {p1, v0}, Landroid/content/IntentFilter;->addAction(Ljava/lang/String;)V

    goto :goto_b

    nop

    :goto_17
    check-cast p1, Landroid/widget/ImageView;

    goto :goto_2

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_activities_SubScreenActivity__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V', 'iget-object v0, p0, Lcom/android/provision/activities/SubScreenActivity;->mDozeWakeLock:Landroid/os/PowerManager$WakeLock;', 'if-eqz v0, :cond_0', 'invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->release()V', 'invoke-static {p0}, Lcom/android/provision/utils/ActivityCollector;->removeActivity(Landroid/app/Activity;)V', 'iget-object v0, p0, Lcom/android/provision/activities/SubScreenActivity;->mScreenPowerChangeReceiver:Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;', 'if-eqz v0, :cond_1', 'invoke-virtual {p0, v0}, Landroid/app/Activity;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 2

    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    iget-object v0, p0, Lcom/android/provision/activities/SubScreenActivity;->mDozeWakeLock:Landroid/os/PowerManager$WakeLock;

    if-eqz v0, :cond_0

    invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->release()V

    :cond_0
    invoke-static {p0}, Lcom/android/provision/utils/ActivityCollector;->removeActivity(Landroid/app/Activity;)V

    iget-object v0, p0, Lcom/android/provision/activities/SubScreenActivity;->mScreenPowerChangeReceiver:Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;

    if-eqz v0, :cond_1

    invoke-virtual {p0, v0}, Landroid/app/Activity;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    :cond_1
    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 2

    goto :goto_4

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/provision/activities/SubScreenActivity;->mDozeWakeLock:Landroid/os/PowerManager$WakeLock;

    goto :goto_7

    nop

    :goto_1
    iget-object v0, p0, Lcom/android/provision/activities/SubScreenActivity;->mScreenPowerChangeReceiver:Lcom/android/provision/activities/SubScreenActivity$ScreenPowerChangeReceiver;

    goto :goto_5

    nop

    :goto_2
    invoke-virtual {v0}, Landroid/os/PowerManager$WakeLock;->release()V

    :goto_3
    goto :goto_6

    nop

    :goto_4
    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    goto :goto_0

    nop

    :goto_5
    if-nez v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_8

    nop

    :goto_6
    invoke-static {p0}, Lcom/android/provision/utils/ActivityCollector;->removeActivity(Landroid/app/Activity;)V

    goto :goto_1

    nop

    :goto_7
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_2

    nop

    :goto_8
    invoke-virtual {p0, v0}, Landroid/app/Activity;->unregisterReceiver(Landroid/content/BroadcastReceiver;)V

    :goto_9
    goto :goto_a

    nop

    :goto_a
    return-void
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
