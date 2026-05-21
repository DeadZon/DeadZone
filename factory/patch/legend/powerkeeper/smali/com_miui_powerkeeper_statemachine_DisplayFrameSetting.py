TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/statemachine/DisplayFrameSetting.smali'
CLASS_FALLBACK_NAMES = ['DisplayFrameSetting.smali']
CLASS_ANCHORS = ['.super Landroid/os/Handler;', '.field private static final CLOUD_AUTOMODE_VRR_GROUP:Ljava/lang/String; = "automode_vrr_group"', '.field private static final CLOUD_CAMERA_IDLE_GROUP:Ljava/lang/String; = "camera_idle_group"', '.field private static final CLOUD_DISPLAY_FPS_GROUP:Ljava/lang/String; = "display_fps_group"', '.field private static final CLOUD_EBOOK_IDLE_GROUP:Ljava/lang/String; = "ebook_idle_pkg"', '.field private static final CLOUD_EYE_MODE_GROUP:Ljava/lang/String; = "eye_protection_mode"']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_statemachine_DisplayFrameSetting__setScreenEffect',
        'method': '.method private setScreenEffect(Ljava/lang/String;II)V',
        'method_name': 'setScreenEffect',
        'method_anchors': ['iget v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mIsUltimate:I', 'const-string v5, "miui_refresh_rate"', 'if-ne v4, v8, :cond_1', 'if-eq v3, v6, :cond_1', 'if-eq v3, v7, :cond_1', 'const-string v4, "com.android.camera"', 'invoke-virtual {v1, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z', 'if-nez v4, :cond_1'],
        'type': 'method_replace',
        'search': """.method private setScreenEffect(Ljava/lang/String;II)V
    .registers 20

    move-object/from16 v0, p0

    move-object/from16 v1, p1

    move/from16 v2, p2

    move/from16 v3, p3

    iget v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mIsUltimate:I

    const-string v5, "miui_refresh_rate"

    const/16 v6, 0xfe

    const/16 v7, 0xf7

    const/4 v8, 0x1

    if-ne v4, v8, :cond_1

    if-eq v3, v6, :cond_1

    if-eq v3, v7, :cond_1

    const-string v4, "com.android.camera"

    invoke-virtual {v1, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_1

    iget v1, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    if-eq v1, v2, :cond_0

    iget-object v1, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    invoke-static {v1, v5, v2}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    iget v1, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    iput v1, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    :cond_0
    return-void

    :cond_1
    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mIsWhitelistPolicy:Z

    const-string v9, " cookie="

    const-string v10, " fps="

    const-string v11, "setScreenEffect pkg="

    const/16 v12, 0x80

    const/16 v13, 0x3c

    const-string v14, "DisplayFrameSetting"

    const/4 v15, 0x0

    if-eqz v4, :cond_c

    if-ne v3, v7, :cond_2

    move v4, v7

    goto :goto_0

    :cond_2
    const/16 v4, 0xf5

    :goto_0
    iget-boolean v5, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->IS_ENABLE_SMART_DFPS:Z

    if-eqz v5, :cond_5

    iget v5, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentCookie:I

    if-ne v5, v7, :cond_3

    move v5, v8

    goto :goto_1

    :cond_3
    move v5, v15

    :goto_1
    if-ne v3, v7, :cond_4

    move v6, v8

    goto :goto_2

    :cond_4
    move v6, v15

    :goto_2
    if-eq v5, v6, :cond_5

    goto :goto_3

    :cond_5
    move v8, v15

    :goto_3
    iget v5, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    if-gt v5, v13, :cond_8

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    if-ne v2, v5, :cond_7

    if-eqz v8, :cond_6

    goto :goto_4

    :cond_6
    const-string v0, "setScreenEffect ignore for user selected lower fps"

    invoke-static {v14, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_7
    :goto_4
    invoke-direct {v0, v5, v4, v1}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->setScreenEffectInternal(IILjava/lang/String;)V

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "setScreenEffect for user selected lower fps cookie="

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-direct {v0, v1}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->writeLocalLog(Ljava/lang/String;)V

    return-void

    :cond_8
    if-le v2, v5, :cond_9

    move v2, v5

    :cond_9
    iget v5, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    if-ne v2, v5, :cond_b

    iget v5, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentCookie:I

    if-eq v3, v5, :cond_a

    goto :goto_5

    :cond_a
    const-string v0, "setScreenEffect ignore for no change"

    invoke-static {v14, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_b
    :goto_5
    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3, v12}, Ljava/lang/StringBuilder;-><init>(I)V

    invoke-virtual {v3, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v0, v3}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->writeLocalLog(Ljava/lang/String;)V

    invoke-direct {v0, v2, v4, v1}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->setScreenEffectInternal(IILjava/lang/String;)V

    return-void

    :cond_c
    iget v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentCookie:I

    const/16 v12, 0xf8

    if-ne v4, v12, :cond_d

    move v13, v8

    goto :goto_6

    :cond_d
    move v13, v15

    :goto_6
    if-ne v3, v12, :cond_e

    move v12, v8

    goto :goto_7

    :cond_e
    move v12, v15

    :goto_7
    if-eq v13, v12, :cond_f

    move v12, v8

    goto :goto_8

    :cond_f
    move v12, v15

    :goto_8
    if-ne v4, v6, :cond_10

    move v13, v8

    goto :goto_9

    :cond_10
    move v13, v15

    :goto_9
    if-ne v3, v6, :cond_11

    goto :goto_a

    :cond_11
    move v8, v15

    :goto_a
    if-eq v13, v8, :cond_12

    const/4 v8, 0x1

    goto :goto_b

    :cond_12
    move v8, v15

    :goto_b
    if-ne v4, v7, :cond_13

    const/4 v13, 0x1

    goto :goto_c

    :cond_13
    move v13, v15

    :goto_c
    if-ne v3, v7, :cond_14

    const/4 v7, 0x1

    goto :goto_d

    :cond_14
    move v7, v15

    :goto_d
    if-eq v13, v7, :cond_15

    const/4 v7, 0x1

    goto :goto_e

    :cond_15
    move v7, v15

    :goto_e
    const/16 v13, 0xfc

    if-ne v4, v13, :cond_16

    const/4 v4, 0x1

    goto :goto_f

    :cond_16
    move v4, v15

    :goto_f
    if-ne v3, v13, :cond_17

    const/4 v13, 0x1

    goto :goto_10

    :cond_17
    move v13, v15

    :goto_10
    if-eq v4, v13, :cond_18

    const/4 v4, 0x1

    goto :goto_11

    :cond_18
    move v4, v15

    :goto_11
    iget-boolean v13, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->IS_ENABLE_SMART_DFPS:Z

    if-eqz v13, :cond_1a

    if-nez v12, :cond_19

    if-nez v8, :cond_19

    if-nez v7, :cond_19

    if-eqz v4, :cond_1a

    :cond_19
    const/4 v4, 0x1

    goto :goto_12

    :cond_1a
    move v4, v15

    :goto_12
    iget-boolean v12, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->SF_ENBALE_AFFINITY:Z

    if-eqz v12, :cond_1c

    if-eqz v8, :cond_1c

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v12, "notifySFCookie cookie ="

    invoke-virtual {v8, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v14, v8}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-ne v3, v6, :cond_1b

    invoke-direct {v0, v15}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->notifySFCPUCluster(I)V

    goto :goto_13

    :cond_1b
    const/4 v8, 0x1

    invoke-direct {v0, v8}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->notifySFCPUCluster(I)V

    :cond_1c
    :goto_13
    iget v8, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    const/16 v12, 0x3c

    if-gt v8, v12, :cond_1e

    if-nez v4, :cond_1e

    const/16 v4, 0xf7

    if-eq v3, v4, :cond_1e

    iget v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    if-ne v4, v8, :cond_1e

    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mIsLowFps:Z

    if-nez v4, :cond_1e

    if-eq v3, v6, :cond_1e

    const-string v1, "setScreenEffect ignore for user selected lower FPS"

    invoke-direct {v0, v1}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->writeLocalLog(Ljava/lang/String;)V

    sget-boolean v1, Lcom/miui/powerkeeper/utils/PowerLog;->V:Z

    if-eqz v1, :cond_1d

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "setScreenEffect user:"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v2, ", c:"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v2, ", cookie:"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v14, v1}, Lcom/miui/powerkeeper/utils/PowerLog;->v(Ljava/lang/String;Ljava/lang/String;)V

    :cond_1d
    iput v3, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentCookie:I

    return-void

    :cond_1e
    if-le v2, v8, :cond_20

    const/16 v4, 0xf7

    if-eq v3, v4, :cond_20

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "fps > mUserFps fps = "

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v6, " MAX_SUPPORT_FPS = "

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v6, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->MAX_SUPPORT_FPS:I

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v6, " mUserFps = "

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v6, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v14, v4}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    const/16 v4, 0x90

    if-lt v2, v4, :cond_1f

    iget v6, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->MAX_SUPPORT_FPS:I

    if-lt v6, v4, :cond_1f

    iget v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    const/16 v6, 0x78

    if-eq v4, v6, :cond_20

    :cond_1f
    const-string v2, "setScreenEffect force fps down to user selected"

    invoke-direct {v0, v2}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->writeLocalLog(Ljava/lang/String;)V

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    :cond_20
    new-instance v4, Ljava/lang/StringBuilder;

    const/16 v6, 0x80

    invoke-direct {v4, v6}, Ljava/lang/StringBuilder;-><init>(I)V

    invoke-virtual {v4, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-direct {v0, v4}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->writeLocalLog(Ljava/lang/String;)V

    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_SWITCH_DEFAULT:Z

    const/16 v6, 0x18

    if-eqz v4, :cond_22

    iget-object v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mContext:Landroid/content/Context;

    invoke-virtual {v4}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v4

    invoke-static {v4, v5, v2}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->IS_ENABLE_SMART_DFPS:Z

    if-eqz v4, :cond_21

    if-eqz v7, :cond_21

    invoke-static {}, Lmiui/hardware/display/DisplayFeatureManager;->getInstance()Lmiui/hardware/display/DisplayFeatureManager;

    move-result-object v4

    invoke-virtual {v4, v6, v2, v3}, Lmiui/hardware/display/DisplayFeatureManager;->setScreenEffect(III)V

    :cond_21
    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->IS_ENABLE_SMART_DFPS:Z

    if-eqz v4, :cond_23

    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->IS_ENABLE_CONTENT_DETECTION:Z

    if-eqz v4, :cond_23

    invoke-direct {v0, v3, v2, v1}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->notifySFIfpsMode(IILjava/lang/String;)V

    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->DBG_DISPLAY:Z

    if-eqz v4, :cond_23

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "notifySFIfpsMode run cookie="

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v5, "fps="

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v5, "pkg="

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v14, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_14

    :cond_22
    invoke-static {}, Lmiui/hardware/display/DisplayFeatureManager;->getInstance()Lmiui/hardware/display/DisplayFeatureManager;

    move-result-object v1

    invoke-virtual {v1, v6, v2, v3}, Lmiui/hardware/display/DisplayFeatureManager;->setScreenEffect(III)V

    :cond_23
    :goto_14
    iput v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    iput v3, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentCookie:I

    return-void
.end method""",
        'replacement': """.method private setScreenEffect(Ljava/lang/String;II)V
    .registers 20

    const-string v0, "lock_max_fps_mezo"

    const/4 v1, 0x1

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-eqz v0, :cond_0

    return-void

    :cond_0
    move-object/from16 v0, p0

    move-object/from16 v1, p1

    move/from16 v2, p2

    move/from16 v3, p3

    iget v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mIsUltimate:I

    const-string v5, "miui_refresh_rate"

    const/16 v6, 0xfe

    const/16 v7, 0xf7

    const/4 v8, 0x1

    if-ne v4, v8, :cond_2

    if-eq v3, v6, :cond_2

    if-eq v3, v7, :cond_2

    const-string v4, "com.android.camera"

    invoke-virtual {v1, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_2

    iget v1, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    if-eq v1, v2, :cond_1

    iget-object v1, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v1

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    invoke-static {v1, v5, v2}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    iget v1, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    iput v1, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    :cond_1
    return-void

    :cond_2
    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mIsWhitelistPolicy:Z

    const-string v9, " cookie="

    const-string v10, " fps="

    const-string v11, "setScreenEffect pkg="

    const/16 v12, 0x80

    const/16 v13, 0x3c

    const-string v14, "DisplayFrameSetting"

    const/4 v15, 0x0

    if-eqz v4, :cond_d

    if-ne v3, v7, :cond_3

    move v4, v7

    goto :goto_0

    :cond_3
    const/16 v4, 0xf5

    :goto_0
    iget-boolean v5, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->IS_ENABLE_SMART_DFPS:Z

    if-eqz v5, :cond_6

    iget v5, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentCookie:I

    if-ne v5, v7, :cond_4

    move v5, v8

    goto :goto_1

    :cond_4
    move v5, v15

    :goto_1
    if-ne v3, v7, :cond_5

    move v6, v8

    goto :goto_2

    :cond_5
    move v6, v15

    :goto_2
    if-eq v5, v6, :cond_6

    goto :goto_3

    :cond_6
    move v8, v15

    :goto_3
    iget v5, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    if-gt v5, v13, :cond_9

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    if-ne v2, v5, :cond_8

    if-eqz v8, :cond_7

    goto :goto_4

    :cond_7
    const-string v0, "setScreenEffect ignore for user selected lower fps"

    invoke-static {v14, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_8
    :goto_4
    invoke-direct {v0, v5, v4, v1}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->setScreenEffectInternal(IILjava/lang/String;)V

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "setScreenEffect for user selected lower fps cookie="

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-direct {v0, v1}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->writeLocalLog(Ljava/lang/String;)V

    return-void

    :cond_9
    if-le v2, v5, :cond_a

    move v2, v5

    :cond_a
    iget v5, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    if-ne v2, v5, :cond_c

    iget v5, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentCookie:I

    if-eq v3, v5, :cond_b

    goto :goto_5

    :cond_b
    const-string v0, "setScreenEffect ignore for no change"

    invoke-static {v14, v0}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    return-void

    :cond_c
    :goto_5
    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3, v12}, Ljava/lang/StringBuilder;-><init>(I)V

    invoke-virtual {v3, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v0, v3}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->writeLocalLog(Ljava/lang/String;)V

    invoke-direct {v0, v2, v4, v1}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->setScreenEffectInternal(IILjava/lang/String;)V

    return-void

    :cond_d
    iget v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentCookie:I

    const/16 v12, 0xf8

    if-ne v4, v12, :cond_e

    move v13, v8

    goto :goto_6

    :cond_e
    move v13, v15

    :goto_6
    if-ne v3, v12, :cond_f

    move v12, v8

    goto :goto_7

    :cond_f
    move v12, v15

    :goto_7
    if-eq v13, v12, :cond_10

    move v12, v8

    goto :goto_8

    :cond_10
    move v12, v15

    :goto_8
    if-ne v4, v6, :cond_11

    move v13, v8

    goto :goto_9

    :cond_11
    move v13, v15

    :goto_9
    if-ne v3, v6, :cond_12

    goto :goto_a

    :cond_12
    move v8, v15

    :goto_a
    if-eq v13, v8, :cond_13

    const/4 v8, 0x1

    goto :goto_b

    :cond_13
    move v8, v15

    :goto_b
    if-ne v4, v7, :cond_14

    const/4 v13, 0x1

    goto :goto_c

    :cond_14
    move v13, v15

    :goto_c
    if-ne v3, v7, :cond_15

    const/4 v7, 0x1

    goto :goto_d

    :cond_15
    move v7, v15

    :goto_d
    if-eq v13, v7, :cond_16

    const/4 v7, 0x1

    goto :goto_e

    :cond_16
    move v7, v15

    :goto_e
    const/16 v13, 0xfc

    if-ne v4, v13, :cond_17

    const/4 v4, 0x1

    goto :goto_f

    :cond_17
    move v4, v15

    :goto_f
    if-ne v3, v13, :cond_18

    const/4 v13, 0x1

    goto :goto_10

    :cond_18
    move v13, v15

    :goto_10
    if-eq v4, v13, :cond_19

    const/4 v4, 0x1

    goto :goto_11

    :cond_19
    move v4, v15

    :goto_11
    iget-boolean v13, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->IS_ENABLE_SMART_DFPS:Z

    if-eqz v13, :cond_1b

    if-nez v12, :cond_1a

    if-nez v8, :cond_1a

    if-nez v7, :cond_1a

    if-eqz v4, :cond_1b

    :cond_1a
    const/4 v4, 0x1

    goto :goto_12

    :cond_1b
    move v4, v15

    :goto_12
    iget-boolean v12, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->SF_ENBALE_AFFINITY:Z

    if-eqz v12, :cond_1d

    if-eqz v8, :cond_1d

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    const-string v12, "notifySFCookie cookie ="

    invoke-virtual {v8, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v8, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v8}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v8

    invoke-static {v14, v8}, Landroid/util/Log;->i(Ljava/lang/String;Ljava/lang/String;)I

    if-ne v3, v6, :cond_1c

    invoke-direct {v0, v15}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->notifySFCPUCluster(I)V

    goto :goto_13

    :cond_1c
    const/4 v8, 0x1

    invoke-direct {v0, v8}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->notifySFCPUCluster(I)V

    :cond_1d
    :goto_13
    iget v8, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    const/16 v12, 0x3c

    if-gt v8, v12, :cond_1f

    if-nez v4, :cond_1f

    const/16 v4, 0xf7

    if-eq v3, v4, :cond_1f

    iget v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    if-ne v4, v8, :cond_1f

    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mIsLowFps:Z

    if-nez v4, :cond_1f

    if-eq v3, v6, :cond_1f

    const-string v1, "setScreenEffect ignore for user selected lower FPS"

    invoke-direct {v0, v1}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->writeLocalLog(Ljava/lang/String;)V

    sget-boolean v1, Lcom/miui/powerkeeper/utils/PowerLog;->V:Z

    if-eqz v1, :cond_1e

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "setScreenEffect user:"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v2, ", c:"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v2, ", cookie:"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v14, v1}, Lcom/miui/powerkeeper/utils/PowerLog;->v(Ljava/lang/String;Ljava/lang/String;)V

    :cond_1e
    iput v3, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentCookie:I

    return-void

    :cond_1f
    if-le v2, v8, :cond_21

    const/16 v4, 0xf7

    if-eq v3, v4, :cond_21

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "fps > mUserFps fps = "

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v6, " MAX_SUPPORT_FPS = "

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v6, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->MAX_SUPPORT_FPS:I

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v6, " mUserFps = "

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget v6, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v14, v4}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    const/16 v4, 0x90

    if-lt v2, v4, :cond_20

    iget v6, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->MAX_SUPPORT_FPS:I

    if-lt v6, v4, :cond_20

    iget v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    const/16 v6, 0x78

    if-eq v4, v6, :cond_21

    :cond_20
    const-string v2, "setScreenEffect force fps down to user selected"

    invoke-direct {v0, v2}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->writeLocalLog(Ljava/lang/String;)V

    iget v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mUserFps:I

    :cond_21
    new-instance v4, Ljava/lang/StringBuilder;

    const/16 v6, 0x80

    invoke-direct {v4, v6}, Ljava/lang/StringBuilder;-><init>(I)V

    invoke-virtual {v4, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-direct {v0, v4}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->writeLocalLog(Ljava/lang/String;)V

    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_SWITCH_DEFAULT:Z

    const/16 v6, 0x18

    if-eqz v4, :cond_23

    iget-object v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mContext:Landroid/content/Context;

    invoke-virtual {v4}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v4

    invoke-static {v4, v5, v2}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->IS_ENABLE_SMART_DFPS:Z

    if-eqz v4, :cond_22

    if-eqz v7, :cond_22

    invoke-static {}, Lmiui/hardware/display/DisplayFeatureManager;->getInstance()Lmiui/hardware/display/DisplayFeatureManager;

    move-result-object v4

    invoke-virtual {v4, v6, v2, v3}, Lmiui/hardware/display/DisplayFeatureManager;->setScreenEffect(III)V

    :cond_22
    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->IS_ENABLE_SMART_DFPS:Z

    if-eqz v4, :cond_24

    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->IS_ENABLE_CONTENT_DETECTION:Z

    if-eqz v4, :cond_24

    invoke-direct {v0, v3, v2, v1}, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->notifySFIfpsMode(IILjava/lang/String;)V

    iget-boolean v4, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->DBG_DISPLAY:Z

    if-eqz v4, :cond_24

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "notifySFIfpsMode run cookie="

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v5, "fps="

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    const-string v5, "pkg="

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v14, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_14

    :cond_23
    invoke-static {}, Lmiui/hardware/display/DisplayFeatureManager;->getInstance()Lmiui/hardware/display/DisplayFeatureManager;

    move-result-object v1

    invoke-virtual {v1, v6, v2, v3}, Lmiui/hardware/display/DisplayFeatureManager;->setScreenEffect(III)V

    :cond_24
    :goto_14
    iput v2, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentFps:I

    iput v3, v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCurrentCookie:I

    return-void
.end method""",
        'required': True,
        'flag_rewrite_count': 0,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
    {
        'id': 'com_miui_powerkeeper_statemachine_DisplayFrameSetting__isSupportDevice',
        'method': '.method public isSupportDevice()Z',
        'method_name': 'isSupportDevice',
        'method_anchors': ['iget-object p0, p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCustomFpsDeviceArray:[Ljava/lang/String;', 'if-ge v2, v0, :cond_2', 'invoke-static {v3}, Lcom/miui/powerkeeper/utils/Utils;->isBelongToDeviceSeries(Ljava/lang/String;)Z', 'if-eqz v4, :cond_0', 'return p0', 'const-string v4, "_intl"', 'invoke-virtual {v3, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z', 'if-eqz v4, :cond_1'],
        'type': 'method_replace',
        'search': """.method public isSupportDevice()Z
    .registers 6

    iget-object p0, p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCustomFpsDeviceArray:[Ljava/lang/String;

    array-length v0, p0

    const/4 v1, 0x0

    move v2, v1

    :goto_0
    if-ge v2, v0, :cond_2

    aget-object v3, p0, v2

    invoke-static {v3}, Lcom/miui/powerkeeper/utils/Utils;->isBelongToDeviceSeries(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const-string v4, "_intl"

    invoke-virtual {v3, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_1

    sget-boolean v4, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v4, :cond_1

    invoke-virtual {v3}, Ljava/lang/String;->length()I

    move-result p0

    add-int/lit8 p0, p0, -0x5

    invoke-virtual {v3, v1, p0}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Lcom/miui/powerkeeper/utils/Utils;->isBelongToDeviceSeries(Ljava/lang/String;)Z

    move-result p0

    return p0

    :cond_1
    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_2
    return v1
.end method""",
        'replacement': """.method public isSupportDevice()Z
    .registers 6

    iget-object p0, p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->mCustomFpsDeviceArray:[Ljava/lang/String;

    array-length v0, p0

    const/4 v1, 0x0

    move v2, v1

    :goto_0
    if-ge v2, v0, :cond_2

    aget-object v3, p0, v2

    invoke-static {v3}, Lcom/miui/powerkeeper/utils/Utils;->isBelongToDeviceSeries(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_0

    const/4 p0, 0x1

    return p0

    :cond_0
    const-string v4, "_intl"

    invoke-virtual {v3, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_1

    sget-boolean v4, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v4, :cond_1

    invoke-virtual {v3}, Ljava/lang/String;->length()I

    move-result p0

    add-int/lit8 p0, p0, -0x5

    invoke-virtual {v3, v1, p0}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object p0

    invoke-static {p0}, Lcom/miui/powerkeeper/utils/Utils;->isBelongToDeviceSeries(Ljava/lang/String;)Z

    move-result p0

    return p0

    :cond_1
    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_2
    return v1
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
    {
        'id': 'com_miui_powerkeeper_statemachine_DisplayFrameSetting__getValidLocalConfigPath',
        'method': '.method public static getValidLocalConfigPath(Landroid/content/Context;)Ljava/lang/String;',
        'method_name': 'getValidLocalConfigPath',
        'method_anchors': ['sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;', 'const-string v1, "fps_local.config"', 'invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z', 'if-eqz v2, :cond_0', 'sget-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;', 'const-string v4, "_intl"', 'invoke-virtual {v2, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z', 'if-eqz v2, :cond_3'],
        'type': 'method_replace',
        'search': """.method public static getValidLocalConfigPath(Landroid/content/Context;)Ljava/lang/String;
    .registers 9

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v1, "fps_local.config"

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v2

    const/4 v3, 0x0

    if-eqz v2, :cond_0

    goto :goto_0

    :cond_0
    move-object v0, v3

    :goto_0
    sget-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v4, "_intl"

    invoke-virtual {v2, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_3

    const-string v2, "IN"

    const-string v5, "ro.miui.build.region"

    invoke-static {v5}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v2, v6}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_1

    const-string v2, "ID"

    invoke-static {v5}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v2, v5}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_3

    :cond_1
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "smartfps/"

    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-object v6, Landroid/os/Build;->DEVICE:Ljava/lang/String;

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v7, "_id"

    invoke-virtual {v2, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    sput-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v2, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v2

    const-string v7, "DisplayFrameSetting"

    if-eqz v2, :cond_2

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "switch intl local config to id local config "

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-object v4, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v7, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    :cond_2
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    sput-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v2, "without id local config, no need to switch intl local config"

    invoke-static {v7, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_3
    :goto_1
    if-nez v0, :cond_5

    sget-boolean v2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v2, :cond_7

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_4

    sget-object p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    return-object p0

    :cond_4
    return-object v3

    :cond_5
    sget-boolean v2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v2, :cond_7

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_6

    sget-object p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    return-object p0

    :cond_6
    const-string p0, "smartfps/opt_dafault_config"

    return-object p0

    :cond_7
    return-object v0
.end method""",
        'replacement': """.method public static getValidLocalConfigPath(Landroid/content/Context;)Ljava/lang/String;
    .registers 9

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v1, "fps_local.config"

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v2

    const/4 v3, 0x0

    if-eqz v2, :cond_0

    goto :goto_0

    :cond_0
    move-object v0, v3

    :goto_0
    sget-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v4, "_intl"

    invoke-virtual {v2, v4}, Ljava/lang/String;->endsWith(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_3

    const-string v2, "IN"

    const-string v5, "ro.miui.build.region"

    invoke-static {v5}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v2, v6}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_1

    const-string v2, "ID"

    invoke-static {v5}, Landroid/os/SystemProperties;->get(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v2, v5}, Ljava/lang/String;->equalsIgnoreCase(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_3

    :cond_1
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "smartfps/"

    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-object v6, Landroid/os/Build;->DEVICE:Ljava/lang/String;

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v7, "_id"

    invoke-virtual {v2, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    sput-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v2, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result v2

    const-string v7, "DisplayFrameSetting"

    if-eqz v2, :cond_2

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "switch intl local config to id local config "

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    sget-object v4, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v7, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    :cond_2
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v2, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    sput-object v2, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    const-string v2, "without id local config, no need to switch intl local config"

    invoke-static {v7, v2}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_3
    :goto_1
    if-nez v0, :cond_5

    sget-boolean v2, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v2, :cond_7

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_4

    sget-object p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    return-object p0

    :cond_4
    return-object v3

    :cond_5
    sget-boolean v2, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v2, :cond_7

    sget-object v0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    invoke-static {p0, v0, v1}, Lcom/miui/powerkeeper/utils/AssetUtils;->doesAssetExist(Landroid/content/Context;Ljava/lang/String;Ljava/lang/String;)Z

    move-result p0

    if-eqz p0, :cond_6

    sget-object p0, Lcom/miui/powerkeeper/statemachine/DisplayFrameSetting;->FPS_INTL_LOCAL_CONFIG_FILE_PATH:Ljava/lang/String;

    return-object p0

    :cond_6
    const-string p0, "smartfps/opt_dafault_config"

    return-object p0

    :cond_7
    return-object v0
.end method""",
        'required': True,
        'flag_rewrite_count': 2,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
