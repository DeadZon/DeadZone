TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/android/provision/manager/PreLoadManager.smali'
CLASS_FALLBACK_NAMES = ['PreLoadManager.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final COMMON_LAYOUTS:[I', '.field private static final NEXT_ACTIVITY_LOAD_SIZE:I = 0x2', '.field private static final PRE_ACTIVITY_LOAD_SIZE:I = 0x2', '.field private static final TAG:Ljava/lang/String; = "PreLoadManager"', '.field private static final WIFI_CLASS:Ljava/lang/String; = "com.android.settings.wifi.WifiProvisionSettingsActivity"']

PATCHES = [
    {
        'id': 'com_android_provision_manager_PreLoadManager__addDefaultActivityClass',
        'method': '.method public addDefaultActivityClass(Lcom/android/provision/activities/DefaultActivity$State;)V',
        'method_name': 'addDefaultActivityClass',
        'method_anchors': ['iget-boolean v0, p0, Lcom/android/provision/manager/PreLoadManager;->isCompleteDefaultActivityLoad:Z', 'if-eqz v0, :cond_0', 'iget-object v0, p1, Lcom/android/provision/activities/DefaultActivity$State;->targetClass:Ljava/lang/Class;', 'if-eqz v0, :cond_1', 'new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "addActivityClass:"', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;'],
        'type': 'policy_skip',
        'search': """.method public addDefaultActivityClass(Lcom/android/provision/activities/DefaultActivity$State;)V
    .registers 4

    iget-boolean v0, p0, Lcom/android/provision/manager/PreLoadManager;->isCompleteDefaultActivityLoad:Z

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    iget-object v0, p1, Lcom/android/provision/activities/DefaultActivity$State;->targetClass:Ljava/lang/Class;

    if-eqz v0, :cond_1

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "addActivityClass:"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v1, p1, Lcom/android/provision/activities/DefaultActivity$State;->targetClass:Ljava/lang/Class;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "PreLoadManager"

    invoke-static {v1, v0}, Lcom/android/provision/manager/PreLoadLog;->log(Ljava/lang/String;Ljava/lang/String;)V

    iget-object v0, p0, Lcom/android/provision/manager/PreLoadManager;->activityStartClassList:Ljava/util/List;

    iget-object v1, p1, Lcom/android/provision/activities/DefaultActivity$State;->targetClass:Ljava/lang/Class;

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_1
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_2

    const-string v0, "com.android.settings.wifi.WifiProvisionSettingsActivity"

    iget-object p1, p1, Lcom/android/provision/activities/DefaultActivity$State;->className:Ljava/lang/String;

    invoke-virtual {v0, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_2

    const/4 p1, 0x1

    iput-boolean p1, p0, Lcom/android/provision/manager/PreLoadManager;->isCompleteDefaultActivityLoad:Z

    invoke-virtual {p0}, Lcom/android/provision/manager/PreLoadManager;->addGlobalActivityClass()V

    :cond_2
    :goto_0
    return-void
.end method""",
        'replacement': """.method public addDefaultActivityClass(Lcom/android/provision/activities/DefaultActivity$State;)V
    .registers 4

    iget-boolean v0, p0, Lcom/android/provision/manager/PreLoadManager;->isCompleteDefaultActivityLoad:Z

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    iget-object v0, p1, Lcom/android/provision/activities/DefaultActivity$State;->targetClass:Ljava/lang/Class;

    if-eqz v0, :cond_1

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "addActivityClass:"

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v1, p1, Lcom/android/provision/activities/DefaultActivity$State;->targetClass:Ljava/lang/Class;

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "PreLoadManager"

    invoke-static {v1, v0}, Lcom/android/provision/manager/PreLoadLog;->log(Ljava/lang/String;Ljava/lang/String;)V

    iget-object v0, p0, Lcom/android/provision/manager/PreLoadManager;->activityStartClassList:Ljava/util/List;

    iget-object v1, p1, Lcom/android/provision/activities/DefaultActivity$State;->targetClass:Ljava/lang/Class;

    invoke-interface {v0, v1}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_1
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_2

    const-string v0, "com.android.settings.wifi.WifiProvisionSettingsActivity"

    iget-object p1, p1, Lcom/android/provision/activities/DefaultActivity$State;->className:Ljava/lang/String;

    invoke-virtual {v0, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result p1

    if-eqz p1, :cond_2

    const/4 p1, 0x1

    iput-boolean p1, p0, Lcom/android/provision/manager/PreLoadManager;->isCompleteDefaultActivityLoad:Z

    invoke-virtual {p0}, Lcom/android/provision/manager/PreLoadManager;->addGlobalActivityClass()V

    :cond_2
    :goto_0
    return-void
.end method""",
        'required': False,
        'policy_status': 'SKIPPED_BUILD_FLAG_POLICY',
        'reason': 'Skipped because this method only rewrites protected MIUI build flags.',
    },
]
