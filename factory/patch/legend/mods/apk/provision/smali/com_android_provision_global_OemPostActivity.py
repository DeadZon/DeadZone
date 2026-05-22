TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/global/OemPostActivity.smali'
CLASS_FALLBACK_NAMES = ['OemPostActivity.smali']
CLASS_ANCHORS = ['.super Lmiuix/appcompat/app/AppCompatActivity;', '.field private static final HUANJI_OLD_FINGERPRINT:Ljava/lang/String; = "huanji_old_fingerprint"', '.field private static final PROVISION_COMPLETE_BROADCAST:Ljava/lang/String; = "android.provision.action.PROVISION_COMPLETE"', '.field private static final TAG:Ljava/lang/String; = "OemPostActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_global_OemPostActivity__onCreate',
        'method': '.method protected onCreate(Landroid/os/Bundle;)V',
        'method_name': 'onCreate',
        'method_anchors': ['const-string v0, "onCreate: "', 'const-string v1, "OemPostActivity"', 'invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I', 'invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V', 'invoke-virtual {p0}, Landroid/app/Activity;->getApplicationContext()Landroid/content/Context;', 'invoke-static {p1}, Lcom/android/provision/utils/CspAutoSwitchManager;->checkTailLandRing(Landroid/content/Context;)V', 'invoke-static {p0, p1}, Lcom/android/provision/Utils;->enableStatusBar(Landroid/content/Context;Z)V', 'invoke-static {p0}, Lcom/android/provision/utils/ImmersiveUtils;->disableImmersion(Landroid/content/Context;)V'],
        'type': 'method_replace',
        'search': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 8

    const-string v0, "onCreate: "

    const-string v1, "OemPostActivity"

    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    invoke-virtual {p0}, Landroid/app/Activity;->getApplicationContext()Landroid/content/Context;

    move-result-object p1

    invoke-static {p1}, Lcom/android/provision/utils/CspAutoSwitchManager;->checkTailLandRing(Landroid/content/Context;)V

    const/4 p1, 0x1

    invoke-static {p0, p1}, Lcom/android/provision/Utils;->enableStatusBar(Landroid/content/Context;Z)V

    invoke-static {p0}, Lcom/android/provision/utils/ImmersiveUtils;->disableImmersion(Landroid/content/Context;)V

    invoke-direct {p0}, Lcom/android/provision/global/OemPostActivity;->setAlarm()V

    invoke-static {p0}, Lcom/android/provision/Utils;->sendProvisionCompleteBroadcast(Landroid/content/Context;)V

    invoke-direct {p0}, Lcom/android/provision/global/OemPostActivity;->stopAbnormalService()V

    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v0

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v2

    invoke-virtual {v0, v2}, Lcom/android/provision/utils/MccHelper;->isSupportTrustonic(Landroid/content/Context;)Z

    move-result v0

    const/4 v2, 0x0

    if-eqz v0, :cond_0

    invoke-static {}, Lcom/android/provision/utils/UserManagerHelper;->getInstance()Lcom/android/provision/utils/UserManagerHelper;

    move-result-object v0

    invoke-virtual {v0, v2}, Lcom/android/provision/utils/UserManagerHelper;->disableUserSpace(Z)V

    :cond_0
    invoke-static {p0}, Lcom/android/provision/Utils;->isCustSupportImeConfig(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_1

    new-instance v0, Lcom/android/provision/utils/InputMethodHelper;

    invoke-direct {v0, p0}, Lcom/android/provision/utils/InputMethodHelper;-><init>(Landroid/content/Context;)V

    invoke-virtual {v0}, Lcom/android/provision/utils/InputMethodHelper;->retrySetGlobalInputMethod()V

    :cond_1
    :try_start_0
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object v0

    const/4 v3, -0x1

    invoke-static {p0, v0, v3}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v0

    const-string v3, "goto next page error"

    invoke-static {v1, v3, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_0
    invoke-static {}, Lcom/android/provision/Utils;->getLocaleISO()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/Utils;->setChargingMark(Ljava/lang/String;)V

    sget-object v0, Lcom/android/provision/Utils;->FINGER_PRINT_POINT:Landroid/app/Activity;

    if-eqz v0, :cond_2

    invoke-virtual {v0}, Landroid/app/Activity;->isFinishing()Z

    move-result v0

    if-nez v0, :cond_2

    sget-object v0, Lcom/android/provision/Utils;->FINGER_PRINT_POINT:Landroid/app/Activity;

    invoke-virtual {v0}, Landroid/app/Activity;->finish()V

    const-string v0, " set FingerPrintActivity finish"

    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    :cond_2
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_3

    sput p1, Lcom/android/provision/Utils;->isGlobalProvisionLastPage:I

    invoke-static {p0}, Lcom/android/provision/StatusBarControllerService;->restoreStatusBar(Landroid/content/Context;)V

    :cond_3
    const-class v0, Landroid/app/admin/DevicePolicyManager;

    invoke-virtual {p0, v0}, Landroid/app/Activity;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/app/admin/DevicePolicyManager;

    if-eqz v0, :cond_4

    invoke-virtual {v0}, Landroid/app/admin/DevicePolicyManager;->getUserProvisioningState()I

    move-result v3

    goto :goto_1

    :cond_4
    move v3, v2

    :goto_1
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "getUserProvisioningState="

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Landroid/app/admin/DevicePolicyManager;->getUserProvisioningState()I

    move-result v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v5, ",isDeviceManaged="

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Landroid/app/admin/DevicePolicyManager;->isDeviceManaged()Z

    move-result v5

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v1, v4}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-static {p0}, Lcom/android/provision/Utils;->setupProvisionComplete(Landroid/content/Context;)V

    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result v4

    if-nez v4, :cond_5

    invoke-virtual {v0}, Landroid/app/admin/DevicePolicyManager;->isDeviceManaged()Z

    move-result v0

    if-eqz v0, :cond_8

    :cond_5
    const/4 v0, 0x4

    if-eq v3, v0, :cond_7

    const/4 v0, 0x5

    if-eq v3, v0, :cond_7

    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->needShowHomeDrawerByDefault()Z

    move-result v0

    if-eqz v0, :cond_6

    goto :goto_2

    :cond_6
    invoke-static {p0}, Lcom/android/provision/Utils;->isInDlcMode(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_8

    new-instance v0, Ljava/util/HashMap;

    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    sget-object v1, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    const-string v3, "com.duokan.phone.remotecontroller"

    invoke-virtual {v0, v3, v1}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-static {v1, v0}, Lcom/android/provision/Utils;->setApplicationListEnabled(Landroid/content/Context;Ljava/util/HashMap;)V

    goto :goto_3

    :cond_7
    :goto_2
    const-string v0, "OemPostActivity set miui_home_drawer_default_enable"

    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "miui_home_drawer_default_enable"

    invoke-static {v0, v1, p1}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_8
    :goto_3
    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isNeedDisabledDialpadTone()Z

    move-result v0

    if-eqz v0, :cond_9

    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "dtmf_tone"

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_9
    invoke-static {}, Lcom/android/provision/Utils;->isFlipDevice()Z

    move-result v0

    if-eqz v0, :cond_a

    new-instance v0, Landroid/content/Intent;

    const-class v1, Lcom/android/provision/CoverScreenService;

    invoke-direct {v0, p0, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    :try_start_1
    invoke-virtual {p0, v0}, Landroid/app/Activity;->stopService(Landroid/content/Intent;)Z
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_1

    goto :goto_4

    :catch_1
    move-exception v0

    invoke-virtual {v0}, Ljava/lang/Exception;->printStackTrace()V

    :cond_a
    :goto_4
    invoke-static {p0}, Lcom/android/provision/Utils;->isGestureLineShow(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_b

    invoke-static {p0, v2}, Lcom/android/provision/Utils;->hideGestureLine(Landroid/content/Context;Z)V

    :cond_b
    invoke-static {}, Lmiui/util/MiuiMultiDisplayTypeInfo;->isIndependentRearDevice()Z

    move-result v0

    if-eqz v0, :cond_c

    const-class v0, Lcom/android/provision/activities/SubScreenActivity;

    invoke-static {v0}, Lcom/android/provision/utils/ActivityCollector;->finishActivity(Ljava/lang/Class;)V

    :cond_c
    invoke-virtual {p0}, Landroid/app/Activity;->getApplicationContext()Landroid/content/Context;

    move-result-object v0

    invoke-static {v0}, Lcom/android/provision/utils/FingerprintReader;->getFingerprint(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v0

    if-eqz v0, :cond_d

    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    const-string v2, "huanji_old_fingerprint"

    invoke-static {v1, v2, v0}, Landroid/provider/Settings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    :cond_d
    invoke-direct {p0}, Lcom/android/provision/global/OemPostActivity;->sendOtaBroadcast()V

    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    sput-boolean p1, Lcom/android/provision/Utils;->abnormalFlowFinishedTag:Z

    return-void
.end method""",
        'replacement': """.method protected onCreate(Landroid/os/Bundle;)V
    .registers 8

    goto :goto_3a

    nop

    :goto_0
    if-eqz v4, :cond_0

    goto :goto_2b

    :cond_0
    goto :goto_1

    nop

    :goto_1
    invoke-virtual {v0}, Landroid/app/admin/DevicePolicyManager;->isDeviceManaged()Z

    move-result v0

    goto :goto_2a

    nop

    :goto_2
    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    goto :goto_1b

    nop

    :goto_3
    const-string v0, " set FingerPrintActivity finish"

    goto :goto_70

    nop

    :goto_4
    invoke-static {v1, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_13

    nop

    :goto_5
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_69

    nop

    :goto_6
    if-eqz v0, :cond_1

    goto :goto_5f

    :cond_1
    goto :goto_5e

    nop

    :goto_7
    invoke-static {p0}, Lcom/android/provision/Utils;->isInProvisionState(Landroid/content/Context;)Z

    move-result v4

    goto :goto_0

    nop

    :goto_8
    const/4 v0, 0x5

    goto :goto_35

    nop

    :goto_9
    new-instance v0, Ljava/util/HashMap;

    goto :goto_2f

    nop

    :goto_a
    invoke-static {p0}, Lcom/android/provision/Utils;->sendProvisionCompleteBroadcast(Landroid/content/Context;)V

    goto :goto_37

    nop

    :goto_b
    invoke-virtual {v0, v3, v1}, Ljava/util/HashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_1f

    nop

    :goto_c
    if-nez v0, :cond_2

    goto :goto_25

    :cond_2
    goto :goto_51

    nop

    :goto_d
    sput-boolean p1, Lcom/android/provision/Utils;->abnormalFlowFinishedTag:Z

    goto :goto_3b

    nop

    :goto_e
    check-cast v0, Landroid/app/admin/DevicePolicyManager;

    goto :goto_6b

    nop

    :goto_f
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    goto :goto_75

    nop

    :goto_10
    if-ne v3, v0, :cond_3

    goto :goto_3d

    :cond_3
    goto :goto_8

    nop

    :goto_11
    if-nez v0, :cond_4

    goto :goto_7c

    :cond_4
    goto :goto_6f

    nop

    :goto_12
    invoke-static {p1}, Lcom/android/provision/utils/CspAutoSwitchManager;->checkTailLandRing(Landroid/content/Context;)V

    goto :goto_40

    nop

    :goto_13
    invoke-super {p0, p1}, Lmiuix/appcompat/app/AppCompatActivity;->onCreate(Landroid/os/Bundle;)V

    goto :goto_76

    nop

    :goto_14
    if-nez v0, :cond_5

    goto :goto_71

    :cond_5
    goto :goto_67

    nop

    :goto_15
    invoke-virtual {p0}, Landroid/app/Activity;->getApplicationContext()Landroid/content/Context;

    move-result-object v0

    goto :goto_5d

    nop

    :goto_16
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_60

    nop

    :goto_17
    const/4 v0, 0x4

    goto :goto_10

    nop

    :goto_18
    sput p1, Lcom/android/provision/Utils;->isGlobalProvisionLastPage:I

    goto :goto_44

    nop

    :goto_19
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v2

    goto :goto_58

    nop

    :goto_1a
    invoke-static {p0}, Lcom/android/provision/Utils;->isInDlcMode(Landroid/content/Context;)Z

    move-result v0

    goto :goto_20

    nop

    :goto_1b
    const-string v2, "huanji_old_fingerprint"

    goto :goto_80

    nop

    :goto_1c
    if-nez v0, :cond_6

    goto :goto_22

    :cond_6
    goto :goto_59

    nop

    :goto_1d
    invoke-static {v0, v1, p1}, Landroid/provider/Settings$Global;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :goto_1e
    goto :goto_62

    nop

    :goto_1f
    invoke-static {}, Lcom/android/provision/ProvisionApplication;->getContext()Landroid/content/Context;

    move-result-object v1

    goto :goto_5c

    nop

    :goto_20
    if-eqz v0, :cond_7

    goto :goto_1e

    :cond_7
    goto :goto_9

    nop

    :goto_21
    invoke-virtual {v0}, Ljava/lang/Exception;->printStackTrace()V

    :goto_22
    goto :goto_82

    nop

    :goto_23
    invoke-direct {v0, p0, v1}, Landroid/content/Intent;-><init>(Landroid/content/Context;Ljava/lang/Class;)V

    :try_start_0
    invoke-virtual {p0, v0}, Landroid/app/Activity;->stopService(Landroid/content/Intent;)Z
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_1

    goto :goto_77

    nop

    :goto_24
    invoke-static {v0, v1, v2}, Landroid/provider/Settings$System;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :goto_25
    goto :goto_7e

    nop

    :goto_26
    const-string v1, "OemPostActivity"

    goto :goto_4

    nop

    :goto_27
    sget-object v1, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    goto :goto_54

    nop

    :goto_28
    invoke-static {}, Lmiui/util/MiuiMultiDisplayTypeInfo;->isIndependentRearDevice()Z

    move-result v0

    goto :goto_11

    nop

    :goto_29
    if-nez v0, :cond_8

    goto :goto_45

    :cond_8
    goto :goto_18

    nop

    :goto_2a
    if-nez v0, :cond_9

    goto :goto_1e

    :cond_9
    :goto_2b
    goto :goto_17

    nop

    :goto_2c
    invoke-direct {v0, p0}, Lcom/android/provision/utils/InputMethodHelper;-><init>(Landroid/content/Context;)V

    goto :goto_42

    nop

    :goto_2d
    invoke-static {v1, v3, v0}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_2e
    goto :goto_6c

    nop

    :goto_2f
    invoke-direct {v0}, Ljava/util/HashMap;-><init>()V

    goto :goto_27

    nop

    :goto_30
    move v3, v2

    :goto_31
    goto :goto_38

    nop

    :goto_32
    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    goto :goto_41

    nop

    :goto_33
    invoke-virtual {p0, v0}, Landroid/app/Activity;->getSystemService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_e

    nop

    :goto_34
    if-eqz v0, :cond_a

    goto :goto_43

    :cond_a
    goto :goto_64

    nop

    :goto_35
    if-ne v3, v0, :cond_b

    goto :goto_3d

    :cond_b
    goto :goto_39

    nop

    :goto_36
    invoke-static {v0}, Lcom/android/provision/Utils;->setChargingMark(Ljava/lang/String;)V

    goto :goto_6d

    nop

    :goto_37
    invoke-direct {p0}, Lcom/android/provision/global/OemPostActivity;->stopAbnormalService()V

    goto :goto_6e

    nop

    :goto_38
    new-instance v4, Ljava/lang/StringBuilder;

    goto :goto_16

    nop

    :goto_39
    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->needShowHomeDrawerByDefault()Z

    move-result v0

    goto :goto_5b

    nop

    :goto_3a
    const-string v0, "onCreate: "

    goto :goto_26

    nop

    :goto_3b
    return-void

    :goto_3c
    goto :goto_1e

    :goto_3d
    goto :goto_83

    nop

    :goto_3e
    if-nez v0, :cond_c

    goto :goto_7a

    :cond_c
    goto :goto_4e

    nop

    :goto_3f
    const-string v1, "dtmf_tone"

    goto :goto_24

    nop

    :goto_40
    const/4 p1, 0x1

    goto :goto_65

    nop

    :goto_41
    const-string v1, "miui_home_drawer_default_enable"

    goto :goto_1d

    nop

    :goto_42
    invoke-virtual {v0}, Lcom/android/provision/utils/InputMethodHelper;->retrySetGlobalInputMethod()V

    :goto_43
    :try_start_1
    invoke-virtual {p0}, Landroid/app/Activity;->getIntent()Landroid/content/Intent;

    move-result-object v0

    const/4 v3, -0x1

    invoke-static {p0, v0, v3}, Lcom/android/provision/Utils;->goToNextPage(Landroid/app/Activity;Landroid/content/Intent;I)V
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_0

    goto :goto_68

    nop

    :goto_44
    invoke-static {p0}, Lcom/android/provision/StatusBarControllerService;->restoreStatusBar(Landroid/content/Context;)V

    :goto_45
    goto :goto_63

    nop

    :goto_46
    invoke-virtual {v0}, Landroid/app/Activity;->finish()V

    goto :goto_3

    nop

    :goto_47
    invoke-direct {p0}, Lcom/android/provision/global/OemPostActivity;->sendOtaBroadcast()V

    goto :goto_72

    nop

    :goto_48
    goto :goto_31

    :goto_49
    goto :goto_30

    nop

    :goto_4a
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    goto :goto_4b

    nop

    :goto_4b
    const-string v5, ",isDeviceManaged="

    goto :goto_5

    nop

    :goto_4c
    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_32

    nop

    :goto_4d
    if-nez v0, :cond_d

    goto :goto_81

    :cond_d
    goto :goto_2

    nop

    :goto_4e
    invoke-static {}, Lcom/android/provision/utils/UserManagerHelper;->getInstance()Lcom/android/provision/utils/UserManagerHelper;

    move-result-object v0

    goto :goto_79

    nop

    :goto_4f
    if-eqz v0, :cond_e

    goto :goto_71

    :cond_e
    goto :goto_6a

    nop

    :goto_50
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    goto :goto_55

    nop

    :goto_51
    invoke-virtual {p0}, Landroid/app/Activity;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    goto :goto_3f

    nop

    :goto_52
    goto :goto_3d

    :goto_53
    goto :goto_1a

    nop

    :goto_54
    const-string v3, "com.duokan.phone.remotecontroller"

    goto :goto_b

    nop

    :goto_55
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    goto :goto_56

    nop

    :goto_56
    invoke-static {v1, v4}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_66

    nop

    :goto_57
    invoke-virtual {v0}, Landroid/app/admin/DevicePolicyManager;->getUserProvisioningState()I

    move-result v3

    goto :goto_48

    nop

    :goto_58
    invoke-virtual {v0, v2}, Lcom/android/provision/utils/MccHelper;->isSupportTrustonic(Landroid/content/Context;)Z

    move-result v0

    goto :goto_5a

    nop

    :goto_59
    new-instance v0, Landroid/content/Intent;

    goto :goto_61

    nop

    :goto_5a
    const/4 v2, 0x0

    goto :goto_3e

    nop

    :goto_5b
    if-nez v0, :cond_f

    goto :goto_53

    :cond_f
    goto :goto_52

    nop

    :goto_5c
    invoke-static {v1, v0}, Lcom/android/provision/Utils;->setApplicationListEnabled(Landroid/content/Context;Ljava/util/HashMap;)V

    goto :goto_3c

    nop

    :goto_5d
    invoke-static {v0}, Lcom/android/provision/utils/FingerprintReader;->getFingerprint(Landroid/content/Context;)Ljava/lang/String;

    move-result-object v0

    goto :goto_4d

    nop

    :goto_5e
    invoke-static {p0, v2}, Lcom/android/provision/Utils;->hideGestureLine(Landroid/content/Context;Z)V

    :goto_5f
    goto :goto_28

    nop

    :goto_60
    const-string v5, "getUserProvisioningState="

    goto :goto_f

    nop

    :goto_61
    const-class v1, Lcom/android/provision/CoverScreenService;

    goto :goto_23

    nop

    :goto_62
    invoke-static {}, Lcom/android/provision/MiuiCustomizeUtil;->isNeedDisabledDialpadTone()Z

    move-result v0

    goto :goto_c

    nop

    :goto_63
    const-class v0, Landroid/app/admin/DevicePolicyManager;

    goto :goto_33

    nop

    :goto_64
    new-instance v0, Lcom/android/provision/utils/InputMethodHelper;

    goto :goto_2c

    nop

    :goto_65
    invoke-static {p0, p1}, Lcom/android/provision/Utils;->enableStatusBar(Landroid/content/Context;Z)V

    goto :goto_7f

    nop

    :goto_66
    invoke-static {p0}, Lcom/android/provision/Utils;->setupProvisionComplete(Landroid/content/Context;)V

    goto :goto_7

    nop

    :goto_67
    invoke-virtual {v0}, Landroid/app/Activity;->isFinishing()Z

    move-result v0

    goto :goto_4f

    nop

    :goto_68
    goto :goto_2e

    :catch_0
    move-exception v0

    goto :goto_7d

    nop

    :goto_69
    invoke-virtual {v0}, Landroid/app/admin/DevicePolicyManager;->isDeviceManaged()Z

    move-result v5

    goto :goto_50

    nop

    :goto_6a
    sget-object v0, Lcom/android/provision/Utils;->FINGER_PRINT_POINT:Landroid/app/Activity;

    goto :goto_46

    nop

    :goto_6b
    if-nez v0, :cond_10

    goto :goto_49

    :cond_10
    goto :goto_57

    nop

    :goto_6c
    invoke-static {}, Lcom/android/provision/Utils;->getLocaleISO()Ljava/lang/String;

    move-result-object v0

    goto :goto_36

    nop

    :goto_6d
    sget-object v0, Lcom/android/provision/Utils;->FINGER_PRINT_POINT:Landroid/app/Activity;

    goto :goto_14

    nop

    :goto_6e
    invoke-static {}, Lcom/android/provision/utils/MccHelper;->getInstance()Lcom/android/provision/utils/MccHelper;

    move-result-object v0

    goto :goto_19

    nop

    :goto_6f
    const-class v0, Lcom/android/provision/activities/SubScreenActivity;

    goto :goto_7b

    nop

    :goto_70
    invoke-static {v1, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    :goto_71
    goto :goto_78

    nop

    :goto_72
    invoke-virtual {p0}, Lmiuix/appcompat/app/AppCompatActivity;->finish()V

    goto :goto_d

    nop

    :goto_73
    invoke-direct {p0}, Lcom/android/provision/global/OemPostActivity;->setAlarm()V

    goto :goto_a

    nop

    :goto_74
    invoke-static {p0}, Lcom/android/provision/Utils;->isCustSupportImeConfig(Landroid/content/Context;)Z

    move-result v0

    goto :goto_34

    nop

    :goto_75
    invoke-virtual {v0}, Landroid/app/admin/DevicePolicyManager;->getUserProvisioningState()I

    move-result v5

    goto :goto_4a

    nop

    :goto_76
    invoke-virtual {p0}, Landroid/app/Activity;->getApplicationContext()Landroid/content/Context;

    move-result-object p1

    goto :goto_12

    nop

    :goto_77
    goto :goto_22

    :catch_1
    move-exception v0

    goto :goto_21

    nop

    :goto_78
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    goto :goto_29

    nop

    :goto_79
    invoke-virtual {v0, v2}, Lcom/android/provision/utils/UserManagerHelper;->disableUserSpace(Z)V

    :goto_7a
    goto :goto_74

    nop

    :goto_7b
    invoke-static {v0}, Lcom/android/provision/utils/ActivityCollector;->finishActivity(Ljava/lang/Class;)V

    :goto_7c
    goto :goto_15

    nop

    :goto_7d
    const-string v3, "goto next page error"

    goto :goto_2d

    nop

    :goto_7e
    invoke-static {}, Lcom/android/provision/Utils;->isFlipDevice()Z

    move-result v0

    goto :goto_1c

    nop

    :goto_7f
    invoke-static {p0}, Lcom/android/provision/utils/ImmersiveUtils;->disableImmersion(Landroid/content/Context;)V

    goto :goto_73

    nop

    :goto_80
    invoke-static {v1, v2, v0}, Landroid/provider/Settings$System;->putString(Landroid/content/ContentResolver;Ljava/lang/String;Ljava/lang/String;)Z

    :goto_81
    goto :goto_47

    nop

    :goto_82
    invoke-static {p0}, Lcom/android/provision/Utils;->isGestureLineShow(Landroid/content/Context;)Z

    move-result v0

    goto :goto_6

    nop

    :goto_83
    const-string v0, "OemPostActivity set miui_home_drawer_default_enable"

    goto :goto_4c

    nop
.end method""",
        'required': True,
        'policy_status': 'BUILD_FLAG_PARTIALLY_SKIPPED',
        'reason': 'Provision smali rule generated from comparison output.',
    },
    {
        'id': 'com_android_provision_global_OemPostActivity__onDestroy',
        'method': '.method protected onDestroy()V',
        'method_name': 'onDestroy',
        'method_anchors': ['invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V', 'sput-object p0, Lcom/android/provision/Utils;->FINGER_PRINT_POINT:Landroid/app/Activity;', 'return-void'],
        'type': 'method_replace',
        'search': """.method protected onDestroy()V
    .registers 1

    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    const/4 p0, 0x0

    sput-object p0, Lcom/android/provision/Utils;->FINGER_PRINT_POINT:Landroid/app/Activity;

    return-void
.end method""",
        'replacement': """.method protected onDestroy()V
    .registers 1

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    sput-object p0, Lcom/android/provision/Utils;->FINGER_PRINT_POINT:Landroid/app/Activity;

    goto :goto_0

    nop

    :goto_2
    invoke-super {p0}, Lmiuix/appcompat/app/AppCompatActivity;->onDestroy()V

    goto :goto_3

    nop

    :goto_3
    const/4 p0, 0x0

    goto :goto_1

    nop
.end method""",
        'required': True,
        'policy_status': '',
        'reason': 'Provision smali rule generated from comparison output.',
    },
]
