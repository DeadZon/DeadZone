TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode.smali'
CLASS_FALLBACK_NAMES = ['CloudUpdateHideMode.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final DBG_CLOUD:Z', '.field public static final FUCSWITCH:Ljava/lang/String; = "fucSwitch"', '.field static final LAST_SYNC_CLOUD_INFO:Ljava/lang/String; = "last_sync_cloud_info"', '.field public static final PARAM:Ljava/lang/String; = "param"', '.field public static final PARAM2:Ljava/lang/String; = "param2"']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_cloudcontrol_CloudUpdateHideMode__parseResult',
        'method': '.method public static parseResult(Landroid/content/Context;Ljava/lang/String;[Ljava/lang/String;)Z',
        'method_name': 'parseResult',
        'method_anchors': ['const-string v2, "parseResult"', 'const-string v3, "open_night_clean_enable"', 'const-string v4, "restrict_service_group"', 'const-string v5, "process_cluster_group"', 'const-string v6, "alarm_align_list"', 'const-string v7, "audio_active_control"', 'const-string v8, "group_tp_active_time"', 'const-string v9, "group_tp_active_device_list"'],
        'type': 'method_replace',
        'search': """.method public static parseResult(Landroid/content/Context;Ljava/lang/String;[Ljava/lang/String;)Z
    .registers 30

    move-object/from16 v0, p0

    move-object/from16 v1, p2

    const-string v2, "parseResult"

    const-string v3, "open_night_clean_enable"

    const-string v4, "restrict_service_group"

    const-string v5, "process_cluster_group"

    const-string v6, "alarm_align_list"

    const-string v7, "audio_active_control"

    const-string v8, "group_tp_active_time"

    const-string v9, "group_tp_active_device_list"

    const-string v10, "sleep_mode_cloud"

    const-string v11, "sleep_mode_network_white_apps"

    const-string v12, "key_wakelock_cloud_content"

    const-string v13, "key_network_min_interval"

    const-string v14, "upload_log"

    const-string v15, "power_group"

    move-object/from16 v16, v2

    const-string v2, "speed_mode_enable"

    move-object/from16 v17, v3

    const-string v3, "param2"

    move-object/from16 v18, v4

    const-string v4, "param"

    move-object/from16 v19, v5

    :try_start_0
    new-instance v5, Lorg/json/JSONObject;

    move-object/from16 v21, v6

    move-object/from16 v6, p1

    invoke-direct {v5, v6}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    const/4 v6, 0x0

    :goto_0
    if-eqz v1, :cond_6

    move-object/from16 v22, v7

    array-length v7, v1

    if-ge v6, v7, :cond_5

    aget-object v7, v1, v6

    if-eqz v7, :cond_0

    invoke-virtual {v7}, Ljava/lang/String;->isEmpty()Z

    move-result v23

    if-eqz v23, :cond_1

    :cond_0
    move/from16 v23, v6

    move-object/from16 v26, v8

    move-object/from16 v24, v14

    goto :goto_4

    :cond_1
    sget-boolean v23, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->DBG_CLOUD:Z

    if-eqz v23, :cond_2

    sget-object v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    move/from16 v23, v6

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    move-object/from16 v24, v14

    const-string v14, "parseResult overlayStr="

    invoke-virtual {v6, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v1, v6}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    :catch_0
    move-exception v0

    goto :goto_9

    :catch_1
    move-exception v0

    move-object/from16 v2, v16

    goto :goto_b

    :cond_2
    move/from16 v23, v6

    move-object/from16 v24, v14

    :goto_1
    new-instance v1, Lorg/json/JSONObject;

    invoke-direct {v1, v7}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    invoke-virtual {v1}, Lorg/json/JSONObject;->keys()Ljava/util/Iterator;

    move-result-object v6

    :goto_2
    invoke-interface {v6}, Ljava/util/Iterator;->hasNext()Z

    move-result v7

    if-eqz v7, :cond_4

    invoke-interface {v6}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v7

    check-cast v7, Ljava/lang/String;

    invoke-virtual {v1, v7}, Lorg/json/JSONObject;->get(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v14

    sget-boolean v25, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->DBG_CLOUD:Z

    if-eqz v25, :cond_3

    move-object/from16 p1, v1

    sget-object v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    move-object/from16 v25, v6

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    move-object/from16 v26, v8

    const-string v8, "parseResult overlay key="

    invoke-virtual {v6, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v8, " value="

    invoke-virtual {v6, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v1, v6}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_3

    :cond_3
    move-object/from16 p1, v1

    move-object/from16 v25, v6

    move-object/from16 v26, v8

    :goto_3
    invoke-virtual {v5, v7, v14}, Lorg/json/JSONObject;->put(Ljava/lang/String;Ljava/lang/Object;)Lorg/json/JSONObject;

    move-object/from16 v1, p1

    move-object/from16 v6, v25

    move-object/from16 v8, v26

    goto :goto_2

    :cond_4
    move-object/from16 v26, v8

    :goto_4
    add-int/lit8 v6, v23, 0x1

    move-object/from16 v1, p2

    move-object/from16 v7, v22

    move-object/from16 v14, v24

    move-object/from16 v8, v26

    goto :goto_0

    :cond_5
    :goto_5
    move-object/from16 v26, v8

    move-object/from16 v24, v14

    goto :goto_6

    :cond_6
    move-object/from16 v22, v7

    goto :goto_5

    :goto_6
    const-string v1, "feature_list"

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->getJSONArray(Ljava/lang/String;)Lorg/json/JSONArray;

    move-result-object v1

    invoke-static {}, Lcom/google/android/collect/Lists;->newArrayList()Ljava/util/ArrayList;

    move-result-object v6

    invoke-interface {v6}, Ljava/util/List;->clear()V

    invoke-static {}, Lcom/google/android/collect/Lists;->newArrayList()Ljava/util/ArrayList;

    move-result-object v6

    const/4 v7, 0x0

    :goto_7
    invoke-virtual {v1}, Lorg/json/JSONArray;->length()I

    move-result v8

    if-ge v7, v8, :cond_8

    invoke-virtual {v1, v7}, Lorg/json/JSONArray;->optJSONObject(I)Lorg/json/JSONObject;

    move-result-object v8

    invoke-static {v8}, Lcom/miui/powerkeeper/cloudcontrol/PowerKeeperCloudControlFeature;->parseFromJson(Lorg/json/JSONObject;)Lcom/miui/powerkeeper/cloudcontrol/PowerKeeperCloudControlFeature;

    move-result-object v8

    if-eqz v8, :cond_7

    invoke-static {v0, v8}, Lcom/miui/powerkeeper/cloudcontrol/LocalUpdateUtils;->getCloudFeatureContentValues(Landroid/content/Context;Lcom/miui/powerkeeper/cloudcontrol/PowerKeeperCloudControlFeature;)Landroid/content/ContentValues;

    move-result-object v8

    if-eqz v8, :cond_7

    invoke-interface {v6, v8}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_7
    add-int/lit8 v7, v7, 0x1

    goto :goto_7

    :cond_8
    const-string v1, "hide_mode"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "miui_standby"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "no_core_system_apps"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    invoke-static {}, Lb/a;->q()Lb/a;

    move-result-object v1

    sget v7, Lb/b;->Q:I

    invoke-virtual {v1, v7}, Lb/a;->t(I)Z

    move-result v1

    if-nez v1, :cond_a

    sget-boolean v1, Landroid/os/Build;->IS_DEBUGGABLE:Z

    if-eqz v1, :cond_9

    sget-object v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    const-string v7, "old cloud"

    invoke-static {v1, v7}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_9
    const-string v1, "doze_whitelist_apps"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    :cond_a
    const-string v1, "level_ultimate_special_apps"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "ble_scan_block"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "ble_scan_param"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "frozen"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "cluster"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "frozenNew"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "frozenNew_whitelist"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "bright_millet"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "screenoff_millet_mode"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "hot_feedback"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "network_feedback"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "location_delay_hot"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "kill_delay_hot"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "alarm_align"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "launch_restrict"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "aurogon_enable"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "app_bgidle"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "i_delay"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "standby_chain_delay"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "kill_configs"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    invoke-static {v0, v6}, Lcom/miui/powerkeeper/cloudcontrol/LocalUpdateUtils;->setCloudFeatureRule(Landroid/content/Context;Ljava/util/List;)Z

    const-string v1, "network_min_interval"

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1
    :try_end_0
    .catch Lorg/json/JSONException; {:try_start_0 .. :try_end_0} :catch_1
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    const-string v6, ""

    if-eqz v1, :cond_b

    :try_start_1
    sget-object v7, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v14, "feaStandbyChainDelayValue:"

    invoke-virtual {v8, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v7, v8}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-static {v0, v13, v6}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v7

    if-nez v7, :cond_b

    invoke-static {v0, v13, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    :cond_b
    const-string v1, "wakelock"

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    if-eqz v1, :cond_c

    sget-object v7, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v13, "wakelockJson:"

    invoke-virtual {v8, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v7, v8}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-static {v0, v12, v6}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v7

    if-nez v7, :cond_c

    invoke-static {v0, v12, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    :cond_c
    invoke-virtual {v5, v2}, Lorg/json/JSONObject;->optBoolean(Ljava/lang/String;)Z

    move-result v1

    sget-object v7, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v12, "speedMode:"

    invoke-virtual {v8, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v7, v8}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    const/4 v8, 0x1

    if-eqz v1, :cond_d

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    invoke-static {v1, v2, v8}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_8

    :cond_d
    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    const/4 v12, 0x0

    invoke-static {v1, v2, v12}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :goto_8
    const-string v1, "event_notify_control"

    invoke-virtual {v5, v1, v6}, Lorg/json/JSONObject;->optString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/String;->isEmpty()Z

    move-result v2

    if-nez v2, :cond_e

    new-instance v2, Lorg/json/JSONObject;

    invoke-direct {v2, v1}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    const-string v1, "fucSwitch_audio"

    const/4 v12, 0x0

    invoke-virtual {v2, v1, v12}, Lorg/json/JSONObject;->optBoolean(Ljava/lang/String;Z)Z

    move-result v1

    const-string v2, "event_notify_control_fucSwitch_audio"

    invoke-static {v0, v2, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v12, "KEY_EVENT_NOTIFY_CONTROL_AUDIO_SWITCH="

    invoke-virtual {v2, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v7, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    :cond_e
    invoke-virtual {v5, v11, v6}, Lorg/json/JSONObject;->optString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v12, "sleepModeData is "

    invoke-virtual {v2, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v7, v2}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {v1}, Ljava/lang/String;->isEmpty()Z

    move-result v2

    if-nez v2, :cond_f

    invoke-static {v0, v11, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "sleep mode white list is "

    invoke-virtual {v2, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v7, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    :cond_f
    const-string v1, "gms_control"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "fakegps"

    const/4 v12, 0x0

    new-array v2, v12, [Ljava/lang/String;

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "txpower"

    new-array v2, v12, [Ljava/lang/String;

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "screen_off_disable_sync"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "screen_off_clean_app"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "screen_off_force_idle"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "network_traffic"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "shutdown_power"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "night_battery_usage"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "auto_close_wifi_ap"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "func_deep_sleep_check"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "subsysawake_check"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "nonui_mode"

    const/4 v12, 0x0

    new-array v2, v12, [Ljava/lang/String;

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    invoke-static {}, Lb/a;->q()Lb/a;

    move-result-object v1

    sget v2, Lb/b;->L:I

    invoke-virtual {v1, v2}, Lb/a;->t(I)Z

    move-result v1

    if-nez v1, :cond_11

    sget-boolean v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->DBG_CLOUD:Z

    if-eqz v1, :cond_10

    const-string v1, "old sleep mode cloud"

    invoke-static {v7, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_10
    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v5, v10, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v5, v10, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    :cond_11
    invoke-static {}, Lb/a;->q()Lb/a;

    move-result-object v1

    sget v2, Lb/b;->N:I

    invoke-virtual {v1, v2}, Lb/a;->t(I)Z

    move-result v1

    if-nez v1, :cond_13

    sget-boolean v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->DBG_CLOUD:Z

    if-eqz v1, :cond_12

    const-string v1, "is old cloud"

    invoke-static {v7, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_12
    const-string v1, "deep_sleep_mode_cloud"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    :cond_13
    const-string v1, "night_clean_process"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    invoke-static {}, Lb/a;->q()Lb/a;

    move-result-object v1

    sget v2, Lb/b;->S:I

    invoke-virtual {v1, v2}, Lb/a;->t(I)Z

    move-result v1

    if-nez v1, :cond_15

    sget-boolean v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->DBG_CLOUD:Z

    if-eqz v1, :cond_14

    const-string v1, "old alarm control cloud"

    invoke-static {v7, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_14
    const-string v1, "alarm_control"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    :cond_15
    const-string v1, "sleep_reboot"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "enable_txpower_changed"

    const/4 v12, 0x0

    new-array v2, v12, [Ljava/lang/String;

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "thermal_IECtest_config_enable"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "thermal_sptm_config_enable"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "thermal_scenario_config_enable"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    invoke-static {}, Lcom/miui/powerkeeper/cloudcontrol/CloudFunctionConfig;->getInstance()Lcom/miui/powerkeeper/cloudcontrol/CloudFunctionConfig;

    move-result-object v1

    invoke-virtual {v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudFunctionConfig;->notifyAllListeners()V

    invoke-virtual {v5, v15, v6}, Lorg/json/JSONObject;->optString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x0

    invoke-static {v0, v15, v2}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    if-eqz v1, :cond_16

    invoke-virtual {v1}, Ljava/lang/String;->isEmpty()Z

    move-result v4

    if-nez v4, :cond_16

    invoke-virtual {v1, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-nez v3, :cond_16

    invoke-static {v0, v15, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    :cond_16
    invoke-virtual {v5, v9}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v9, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-object/from16 v1, v26

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-object/from16 v1, v24

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->has(Ljava/lang/String;)Z

    move-result v3

    if-eqz v3, :cond_17

    sget-boolean v3, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    xor-int/2addr v3, v8

    invoke-virtual {v5, v1, v3}, Lorg/json/JSONObject;->optBoolean(Ljava/lang/String;Z)Z

    move-result v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z

    :cond_17
    move-object/from16 v1, v22

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    if-eqz v3, :cond_18

    invoke-virtual {v3}, Ljava/lang/String;->isEmpty()Z

    move-result v1

    if-nez v1, :cond_18

    invoke-static {}, Lcom/miui/powerkeeper/PowerKeeperManager;->getInstance()Lcom/miui/powerkeeper/PowerKeeperManager;

    move-result-object v1

    if-eqz v1, :cond_18

    invoke-static {}, Lcom/miui/powerkeeper/PowerKeeperManager;->getInstance()Lcom/miui/powerkeeper/PowerKeeperManager;

    move-result-object v1

    invoke-virtual {v1}, Lcom/miui/powerkeeper/PowerKeeperManager;->getAudioDisguiseController()Lcom/miui/powerkeeper/controller/AudioDisguiseController;

    move-result-object v1

    if-eqz v1, :cond_18

    invoke-virtual {v1}, Lcom/miui/powerkeeper/controller/AudioDisguiseController;->dispatchCloudFunctionUpdated()V

    :cond_18
    move-object/from16 v1, v21

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-object/from16 v1, v19

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-object/from16 v1, v18

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-object/from16 v1, v17

    const/4 v12, 0x0

    invoke-virtual {v5, v1, v12}, Lorg/json/JSONObject;->optBoolean(Ljava/lang/String;Z)Z

    move-result v3

    invoke-static {v3}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v4

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "nightCleanEnable is "

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v7, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    const-string v1, "thermal_common"

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/String;->isEmpty()Z

    move-result v3

    if-nez v3, :cond_19

    new-instance v3, Lorg/json/JSONObject;

    invoke-direct {v3, v1}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    const-string v1, "enable_sp_on_virtual_sensor_comp"

    const/4 v12, 0x0

    invoke-virtual {v3, v1, v12}, Lorg/json/JSONObject;->optBoolean(Ljava/lang/String;Z)Z

    move-result v1

    invoke-static {v1}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v1

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "superModeEnable is "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v7, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    :cond_19
    const/4 v12, 0x0

    invoke-static {v0, v5, v2, v12}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->onCloudFunctionUpdated(Landroid/content/Context;Lorg/json/JSONObject;Lorg/json/JSONObject;I)V

    invoke-static {v0, v5}, Lcom/miui/powerkeeper/statemachine/PowerStateMachine;->onCloudUpdate(Landroid/content/Context;Lorg/json/JSONObject;)V

    invoke-static {v5}, Le/e;->u(Lorg/json/JSONObject;)V
    :try_end_1
    .catch Lorg/json/JSONException; {:try_start_1 .. :try_end_1} :catch_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_0

    return v8

    :goto_9
    sget-object v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    move-object/from16 v2, v16

    invoke-static {v1, v2, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_a
    const/16 v20, 0x0

    goto :goto_c

    :goto_b
    sget-object v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    invoke-static {v1, v2, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    goto :goto_a

    :goto_c
    return v20
.end method""",
        'replacement': """.method public static parseResult(Landroid/content/Context;Ljava/lang/String;[Ljava/lang/String;)Z
    .registers 30

    move-object/from16 v0, p0

    move-object/from16 v1, p2

    const-string v2, "parseResult"

    const-string v3, "open_night_clean_enable"

    const-string v4, "restrict_service_group"

    const-string v5, "process_cluster_group"

    const-string v6, "alarm_align_list"

    const-string v7, "audio_active_control"

    const-string v8, "group_tp_active_time"

    const-string v9, "group_tp_active_device_list"

    const-string v10, "sleep_mode_cloud"

    const-string v11, "sleep_mode_network_white_apps"

    const-string v12, "key_wakelock_cloud_content"

    const-string v13, "key_network_min_interval"

    const-string v14, "upload_log"

    const-string v15, "power_group"

    move-object/from16 v16, v2

    const-string v2, "speed_mode_enable"

    move-object/from16 v17, v3

    const-string v3, "param2"

    move-object/from16 v18, v4

    const-string v4, "param"

    move-object/from16 v19, v5

    :try_start_0
    new-instance v5, Lorg/json/JSONObject;

    move-object/from16 v21, v6

    move-object/from16 v6, p1

    invoke-direct {v5, v6}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    const/4 v6, 0x0

    :goto_0
    if-eqz v1, :cond_6

    move-object/from16 v22, v7

    array-length v7, v1

    if-ge v6, v7, :cond_5

    aget-object v7, v1, v6

    if-eqz v7, :cond_0

    invoke-virtual {v7}, Ljava/lang/String;->isEmpty()Z

    move-result v23

    if-eqz v23, :cond_1

    :cond_0
    move/from16 v23, v6

    move-object/from16 v26, v8

    move-object/from16 v24, v14

    goto :goto_4

    :cond_1
    sget-boolean v23, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->DBG_CLOUD:Z

    if-eqz v23, :cond_2

    sget-object v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    move/from16 v23, v6

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    move-object/from16 v24, v14

    const-string v14, "parseResult overlayStr="

    invoke-virtual {v6, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v1, v6}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    :catch_0
    move-exception v0

    goto :goto_9

    :catch_1
    move-exception v0

    move-object/from16 v2, v16

    goto :goto_b

    :cond_2
    move/from16 v23, v6

    move-object/from16 v24, v14

    :goto_1
    new-instance v1, Lorg/json/JSONObject;

    invoke-direct {v1, v7}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    invoke-virtual {v1}, Lorg/json/JSONObject;->keys()Ljava/util/Iterator;

    move-result-object v6

    :goto_2
    invoke-interface {v6}, Ljava/util/Iterator;->hasNext()Z

    move-result v7

    if-eqz v7, :cond_4

    invoke-interface {v6}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v7

    check-cast v7, Ljava/lang/String;

    invoke-virtual {v1, v7}, Lorg/json/JSONObject;->get(Ljava/lang/String;)Ljava/lang/Object;

    move-result-object v14

    sget-boolean v25, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->DBG_CLOUD:Z

    if-eqz v25, :cond_3

    move-object/from16 p1, v1

    sget-object v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    move-object/from16 v25, v6

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    move-object/from16 v26, v8

    const-string v8, "parseResult overlay key="

    invoke-virtual {v6, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v8, " value="

    invoke-virtual {v6, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v6, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v1, v6}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_3

    :cond_3
    move-object/from16 p1, v1

    move-object/from16 v25, v6

    move-object/from16 v26, v8

    :goto_3
    invoke-virtual {v5, v7, v14}, Lorg/json/JSONObject;->put(Ljava/lang/String;Ljava/lang/Object;)Lorg/json/JSONObject;

    move-object/from16 v1, p1

    move-object/from16 v6, v25

    move-object/from16 v8, v26

    goto :goto_2

    :cond_4
    move-object/from16 v26, v8

    :goto_4
    add-int/lit8 v6, v23, 0x1

    move-object/from16 v1, p2

    move-object/from16 v7, v22

    move-object/from16 v14, v24

    move-object/from16 v8, v26

    goto :goto_0

    :cond_5
    :goto_5
    move-object/from16 v26, v8

    move-object/from16 v24, v14

    goto :goto_6

    :cond_6
    move-object/from16 v22, v7

    goto :goto_5

    :goto_6
    const-string v1, "feature_list"

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->getJSONArray(Ljava/lang/String;)Lorg/json/JSONArray;

    move-result-object v1

    invoke-static {}, Lcom/google/android/collect/Lists;->newArrayList()Ljava/util/ArrayList;

    move-result-object v6

    invoke-interface {v6}, Ljava/util/List;->clear()V

    invoke-static {}, Lcom/google/android/collect/Lists;->newArrayList()Ljava/util/ArrayList;

    move-result-object v6

    const/4 v7, 0x0

    :goto_7
    invoke-virtual {v1}, Lorg/json/JSONArray;->length()I

    move-result v8

    if-ge v7, v8, :cond_8

    invoke-virtual {v1, v7}, Lorg/json/JSONArray;->optJSONObject(I)Lorg/json/JSONObject;

    move-result-object v8

    invoke-static {v8}, Lcom/miui/powerkeeper/cloudcontrol/PowerKeeperCloudControlFeature;->parseFromJson(Lorg/json/JSONObject;)Lcom/miui/powerkeeper/cloudcontrol/PowerKeeperCloudControlFeature;

    move-result-object v8

    if-eqz v8, :cond_7

    invoke-static {v0, v8}, Lcom/miui/powerkeeper/cloudcontrol/LocalUpdateUtils;->getCloudFeatureContentValues(Landroid/content/Context;Lcom/miui/powerkeeper/cloudcontrol/PowerKeeperCloudControlFeature;)Landroid/content/ContentValues;

    move-result-object v8

    if-eqz v8, :cond_7

    invoke-interface {v6, v8}, Ljava/util/List;->add(Ljava/lang/Object;)Z

    :cond_7
    add-int/lit8 v7, v7, 0x1

    goto :goto_7

    :cond_8
    const-string v1, "hide_mode"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "miui_standby"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "no_core_system_apps"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    invoke-static {}, Lb/a;->q()Lb/a;

    move-result-object v1

    sget v7, Lb/b;->Q:I

    invoke-virtual {v1, v7}, Lb/a;->t(I)Z

    move-result v1

    if-nez v1, :cond_a

    sget-boolean v1, Landroid/os/Build;->IS_DEBUGGABLE:Z

    if-eqz v1, :cond_9

    sget-object v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    const-string v7, "old cloud"

    invoke-static {v1, v7}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_9
    const-string v1, "doze_whitelist_apps"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    :cond_a
    const-string v1, "level_ultimate_special_apps"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "ble_scan_block"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "ble_scan_param"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "frozen"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "cluster"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "frozenNew"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "frozenNew_whitelist"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "bright_millet"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "screenoff_millet_mode"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "hot_feedback"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "network_feedback"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "location_delay_hot"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "kill_delay_hot"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "alarm_align"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "launch_restrict"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "aurogon_enable"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "app_bgidle"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "i_delay"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "standby_chain_delay"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    const-string v1, "kill_configs"

    invoke-static {v0, v6, v5, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->addOptGlobalFeature(Landroid/content/Context;Ljava/util/List;Lorg/json/JSONObject;Ljava/lang/String;)Z

    invoke-static {v0, v6}, Lcom/miui/powerkeeper/cloudcontrol/LocalUpdateUtils;->setCloudFeatureRule(Landroid/content/Context;Ljava/util/List;)Z

    const-string v1, "network_min_interval"

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1
    :try_end_0
    .catch Lorg/json/JSONException; {:try_start_0 .. :try_end_0} :catch_1
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    const-string v6, ""

    if-eqz v1, :cond_b

    :try_start_1
    sget-object v7, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v14, "feaStandbyChainDelayValue:"

    invoke-virtual {v8, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v7, v8}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-static {v0, v13, v6}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v7

    if-nez v7, :cond_b

    invoke-static {v0, v13, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    :cond_b
    const-string v1, "wakelock"

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    if-eqz v1, :cond_c

    sget-object v7, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v13, "wakelockJson:"

    invoke-virtual {v8, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v7, v8}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-static {v0, v12, v6}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v7, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v7

    if-nez v7, :cond_c

    invoke-static {v0, v12, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    :cond_c
    invoke-virtual {v5, v2}, Lorg/json/JSONObject;->optBoolean(Ljava/lang/String;)Z

    move-result v1

    sget-object v7, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v12, "speedMode:"

    invoke-virtual {v8, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v7, v8}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    const/4 v8, 0x1

    if-eqz v1, :cond_d

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    invoke-static {v1, v2, v8}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    goto :goto_8

    :cond_d
    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    const/4 v12, 0x0

    invoke-static {v1, v2, v12}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :goto_8
    const-string v1, "event_notify_control"

    invoke-virtual {v5, v1, v6}, Lorg/json/JSONObject;->optString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/String;->isEmpty()Z

    move-result v2

    if-nez v2, :cond_e

    new-instance v2, Lorg/json/JSONObject;

    invoke-direct {v2, v1}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    const-string v1, "fucSwitch_audio"

    const/4 v12, 0x0

    invoke-virtual {v2, v1, v12}, Lorg/json/JSONObject;->optBoolean(Ljava/lang/String;Z)Z

    move-result v1

    const-string v2, "event_notify_control_fucSwitch_audio"

    invoke-static {v0, v2, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v12, "KEY_EVENT_NOTIFY_CONTROL_AUDIO_SWITCH="

    invoke-virtual {v2, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v7, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    :cond_e
    invoke-virtual {v5, v11, v6}, Lorg/json/JSONObject;->optString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v12, "sleepModeData is "

    invoke-virtual {v2, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v7, v2}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {v1}, Ljava/lang/String;->isEmpty()Z

    move-result v2

    if-nez v2, :cond_f

    invoke-static {v0, v11, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "sleep mode white list is "

    invoke-virtual {v2, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v7, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    :cond_f
    const-string v1, "gms_control"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "fakegps"

    const/4 v12, 0x0

    new-array v2, v12, [Ljava/lang/String;

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "txpower"

    new-array v2, v12, [Ljava/lang/String;

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "screen_off_disable_sync"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "screen_off_clean_app"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "screen_off_force_idle"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "network_traffic"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "shutdown_power"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "night_battery_usage"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "auto_close_wifi_ap"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "func_deep_sleep_check"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "subsysawake_check"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "nonui_mode"

    const/4 v12, 0x0

    new-array v2, v12, [Ljava/lang/String;

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    invoke-static {}, Lb/a;->q()Lb/a;

    move-result-object v1

    sget v2, Lb/b;->L:I

    invoke-virtual {v1, v2}, Lb/a;->t(I)Z

    move-result v1

    if-nez v1, :cond_11

    sget-boolean v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->DBG_CLOUD:Z

    if-eqz v1, :cond_10

    const-string v1, "old sleep mode cloud"

    invoke-static {v7, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_10
    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v5, v10, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v5, v10, v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    :cond_11
    invoke-static {}, Lb/a;->q()Lb/a;

    move-result-object v1

    sget v2, Lb/b;->N:I

    invoke-virtual {v1, v2}, Lb/a;->t(I)Z

    move-result v1

    if-nez v1, :cond_13

    sget-boolean v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->DBG_CLOUD:Z

    if-eqz v1, :cond_12

    const-string v1, "is old cloud"

    invoke-static {v7, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_12
    const-string v1, "deep_sleep_mode_cloud"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    :cond_13
    const-string v1, "night_clean_process"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    invoke-static {}, Lb/a;->q()Lb/a;

    move-result-object v1

    sget v2, Lb/b;->S:I

    invoke-virtual {v1, v2}, Lb/a;->t(I)Z

    move-result v1

    if-nez v1, :cond_15

    sget-boolean v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->DBG_CLOUD:Z

    if-eqz v1, :cond_14

    const-string v1, "old alarm control cloud"

    invoke-static {v7, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_14
    const-string v1, "alarm_control"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    :cond_15
    const-string v1, "sleep_reboot"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "enable_txpower_changed"

    const/4 v12, 0x0

    new-array v2, v12, [Ljava/lang/String;

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "thermal_IECtest_config_enable"

    filled-new-array {v4, v3}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "thermal_sptm_config_enable"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    const-string v1, "thermal_scenario_config_enable"

    filled-new-array {v4}, [Ljava/lang/String;

    move-result-object v2

    invoke-static {v0, v5, v1, v2}, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->parseFunction(Landroid/content/Context;Lorg/json/JSONObject;Ljava/lang/String;[Ljava/lang/String;)V

    invoke-static {}, Lcom/miui/powerkeeper/cloudcontrol/CloudFunctionConfig;->getInstance()Lcom/miui/powerkeeper/cloudcontrol/CloudFunctionConfig;

    move-result-object v1

    invoke-virtual {v1}, Lcom/miui/powerkeeper/cloudcontrol/CloudFunctionConfig;->notifyAllListeners()V

    invoke-virtual {v5, v15, v6}, Lorg/json/JSONObject;->optString(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    const/4 v2, 0x0

    invoke-static {v0, v15, v2}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->getString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    if-eqz v1, :cond_16

    invoke-virtual {v1}, Ljava/lang/String;->isEmpty()Z

    move-result v4

    if-nez v4, :cond_16

    invoke-virtual {v1, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-nez v3, :cond_16

    invoke-static {v0, v15, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    :cond_16
    invoke-virtual {v5, v9}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-static {v0, v9, v1}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-object/from16 v1, v26

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-object/from16 v1, v24

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->has(Ljava/lang/String;)Z

    move-result v3

    if-eqz v3, :cond_17

    sget-boolean v3, Lmiui/os/Build;->IS_MIUI:Z

    xor-int/2addr v3, v8

    invoke-virtual {v5, v1, v3}, Lorg/json/JSONObject;->optBoolean(Ljava/lang/String;Z)Z

    move-result v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z

    :cond_17
    move-object/from16 v1, v22

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    if-eqz v3, :cond_18

    invoke-virtual {v3}, Ljava/lang/String;->isEmpty()Z

    move-result v1

    if-nez v1, :cond_18

    invoke-static {}, Lcom/miui/powerkeeper/PowerKeeperManager;->getInstance()Lcom/miui/powerkeeper/PowerKeeperManager;

    move-result-object v1

    if-eqz v1, :cond_18

    invoke-static {}, Lcom/miui/powerkeeper/PowerKeeperManager;->getInstance()Lcom/miui/powerkeeper/PowerKeeperManager;

    move-result-object v1

    invoke-virtual {v1}, Lcom/miui/powerkeeper/PowerKeeperManager;->getAudioDisguiseController()Lcom/miui/powerkeeper/controller/AudioDisguiseController;

    move-result-object v1

    if-eqz v1, :cond_18

    invoke-virtual {v1}, Lcom/miui/powerkeeper/controller/AudioDisguiseController;->dispatchCloudFunctionUpdated()V

    :cond_18
    move-object/from16 v1, v21

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-object/from16 v1, v19

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-object/from16 v1, v18

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putString(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-object/from16 v1, v17

    const/4 v12, 0x0

    invoke-virtual {v5, v1, v12}, Lorg/json/JSONObject;->optBoolean(Ljava/lang/String;Z)Z

    move-result v3

    invoke-static {v3}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v4

    invoke-static {v0, v1, v3}, Lcom/miui/powerkeeper/provider/SimpleSettings$Misc;->putBoolean(Landroid/content/Context;Ljava/lang/String;Z)Z

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "nightCleanEnable is "

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v7, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    const-string v1, "thermal_common"

    invoke-virtual {v5, v1}, Lorg/json/JSONObject;->optString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/String;->isEmpty()Z

    move-result v3

    if-nez v3, :cond_19

    new-instance v3, Lorg/json/JSONObject;

    invoke-direct {v3, v1}, Lorg/json/JSONObject;-><init>(Ljava/lang/String;)V

    const-string v1, "enable_sp_on_virtual_sensor_comp"

    const/4 v12, 0x0

    invoke-virtual {v3, v1, v12}, Lorg/json/JSONObject;->optBoolean(Ljava/lang/String;Z)Z

    move-result v1

    invoke-static {v1}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v1

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "superModeEnable is "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v7, v1}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    :cond_19
    const/4 v12, 0x0

    invoke-static {v0, v5, v2, v12}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->onCloudFunctionUpdated(Landroid/content/Context;Lorg/json/JSONObject;Lorg/json/JSONObject;I)V

    invoke-static {v0, v5}, Lcom/miui/powerkeeper/statemachine/PowerStateMachine;->onCloudUpdate(Landroid/content/Context;Lorg/json/JSONObject;)V

    invoke-static {v5}, Le/e;->u(Lorg/json/JSONObject;)V
    :try_end_1
    .catch Lorg/json/JSONException; {:try_start_1 .. :try_end_1} :catch_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_0

    return v8

    :goto_9
    sget-object v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    move-object/from16 v2, v16

    invoke-static {v1, v2, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :goto_a
    const/16 v20, 0x0

    goto :goto_c

    :goto_b
    sget-object v1, Lcom/miui/powerkeeper/cloudcontrol/CloudUpdateHideMode;->TAG:Ljava/lang/String;

    invoke-static {v1, v2, v0}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    goto :goto_a

    :goto_c
    return v20
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
