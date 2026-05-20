"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-services.jar
Target class : com/android/server/am/BroadcastQueueModernStubImpl
Source MTCR  : miui-services_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-services.jar"
TARGET_CLASS = "com/android/server/am/BroadcastQueueModernStubImpl.smali"

PATCHES = [
    {
        "id":          "replace_method_isInternationalSpecialAction_Ljava_lang_String_Landroid_cont",
        "method":      ".method private isInternationalSpecialAction(Ljava/lang/String;Landroid/content/pm/ResolveInfo;)Z",
        "type":        "method_replace",
        "search": """\
.method private isInternationalSpecialAction(Ljava/lang/String;Landroid/content/pm/ResolveInfo;)Z
    .registers 8

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_2

    sget-object v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mInternationalSpecialAction:Ljava/util/List;

    invoke-interface {v0, p1}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mContext:Landroid/content/Context;

    iget-object v2, p2, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget-object v2, v2, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget-object v3, p2, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v3, v3, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget v3, v3, Landroid/content/pm/ApplicationInfo;->uid:I

    const-string v4, "BroadcastQueueImpl#specifyBroadcast"

    invoke-static {v0, v2, v3, v4}, Landroid/miui/AppOpsUtils;->getApplicationSpecialBroadcast(Landroid/content/Context;Ljava/lang/String;ILjava/lang/String;)I

    move-result v0

    if-nez v0, :cond_1

    const/4 v1, 0x1

    :cond_1
    return v1

    :cond_2
    :goto_0
    return v1
.end method
""",
        "replacement": """\
.method private isInternationalSpecialAction(Ljava/lang/String;Landroid/content/pm/ResolveInfo;)Z
    .registers 8

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v1, 0x1

    const/4 v1, 0x0

    if-eqz v0, :cond_2

    sget-object v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mInternationalSpecialAction:Ljava/util/List;

    invoke-interface {v0, p1}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mContext:Landroid/content/Context;

    iget-object v2, p2, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget-object v2, v2, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget-object v3, p2, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v3, v3, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget v3, v3, Landroid/content/pm/ApplicationInfo;->uid:I

    const-string v4, "BroadcastQueueImpl#specifyBroadcast"

    invoke-static {v0, v2, v3, v4}, Landroid/miui/AppOpsUtils;->getApplicationSpecialBroadcast(Landroid/content/Context;Ljava/lang/String;ILjava/lang/String;)I

    move-result v0

    if-nez v0, :cond_1

    const/4 v1, 0x1

    :cond_1
    return v1

    :cond_2
    :goto_0
    return v1
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
    {
        "id":          "replace_method_updateBlockBroadcast__V",
        "method":      ".method private updateBlockBroadcast()V",
        "type":        "method_replace",
        "search": """\
.method private updateBlockBroadcast()V
    .registers 4

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v0, :cond_0

    const-class v0, Lmiui/security/SecurityManagerInternal;

    invoke-static {v0}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiui/security/SecurityManagerInternal;

    iput-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_0
    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-eqz v0, :cond_2

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_1

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    invoke-virtual {v0}, Lmiui/security/SecurityManagerInternal;->isAllowedDeviceProvision()Z

    move-result v0

    if-nez v0, :cond_1

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "is_block_broadcast_first_boot"

    const/4 v2, 0x1

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    if-ne v0, v2, :cond_1

    goto :goto_0

    :cond_1
    const/4 v2, 0x0

    :goto_0
    iput-boolean v2, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mIsBlockBroadcastFirstBoot:Z

    :cond_2
    return-void
.end method
""",
        "replacement": """\
.method private updateBlockBroadcast()V
    .registers 4

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v0, :cond_0

    const-class v0, Lmiui/security/SecurityManagerInternal;

    invoke-static {v0}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiui/security/SecurityManagerInternal;

    iput-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_0
    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-eqz v0, :cond_2

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v0, 0x1

    if-nez v0, :cond_1

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    invoke-virtual {v0}, Lmiui/security/SecurityManagerInternal;->isAllowedDeviceProvision()Z

    move-result v0

    if-nez v0, :cond_1

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v0

    const-string v1, "is_block_broadcast_first_boot"

    const/4 v2, 0x1

    invoke-static {v0, v1, v2}, Landroid/provider/Settings$Secure;->getInt(Landroid/content/ContentResolver;Ljava/lang/String;I)I

    move-result v0

    if-ne v0, v2, :cond_1

    goto :goto_0

    :cond_1
    const/4 v2, 0x0

    :goto_0
    iput-boolean v2, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mIsBlockBroadcastFirstBoot:Z

    :cond_2
    return-void
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
    {
        "id":          "replace_method_checkApplicationAutoStart_Lcom_android_server_am_BroadcastQu",
        "method":      ".method public checkApplicationAutoStart(Lcom/android/server/am/BroadcastQueue;Lcom/android/server/am/BroadcastRecord;Landroid/content/pm/ResolveInfo;)Z",
        "type":        "method_replace",
        "search": """\
.method public checkApplicationAutoStart(Lcom/android/server/am/BroadcastQueue;Lcom/android/server/am/BroadcastRecord;Landroid/content/pm/ResolveInfo;)Z
    .registers 22

    move-object/from16 v0, p0

    move-object/from16 v1, p2

    move-object/from16 v6, p3

    const/4 v8, 0x1

    if-eqz v6, :cond_16

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    if-eqz v2, :cond_16

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    if-nez v2, :cond_0

    move/from16 v17, v8

    goto :goto_8

    :cond_0
    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v2}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object v9

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget-object v10, v2, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget v11, v2, Landroid/content/pm/ApplicationInfo;->uid:I

    sget-boolean v2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v2, :cond_1

    const-string v2, "com.google.android.c2dm.intent.RECEIVE"

    invoke-virtual {v2, v9}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_1

    return v8

    :cond_1
    invoke-static {v10}, Lcom/miui/server/process/ProcessManagerInternal;->checkCtsProcess(Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_15

    invoke-static {}, Landroid/miui/AppOpsUtils;->isXOptMode()Z

    move-result v2

    if-eqz v2, :cond_2

    move/from16 v17, v8

    goto :goto_7

    :cond_2
    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    const-string v12, "BroadcastQueueInjector"

    const/4 v13, 0x0

    if-eqz v2, :cond_3

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    if-eqz v2, :cond_3

    sget-object v2, Lcom/android/server/am/ActivityManagerServiceImpl;->WIDGET_PROVIDER_WHITE_LIST:Ljava/util/List;

    iget-object v3, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    invoke-interface {v2, v3}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v2

    if-nez v2, :cond_3

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v3, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, ":widgetProvider"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    iget-object v3, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    iget-object v3, v3, Lcom/android/server/am/ProcessRecord;->processName:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-eqz v3, :cond_3

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "MIUILOG- Reject widget call from "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v12, v3}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v13

    :cond_3
    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    if-eqz v2, :cond_5

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    iget v2, v2, Lcom/android/server/am/ProcessRecord;->uid:I

    const/16 v3, 0x403

    if-ne v2, v3, :cond_5

    sget-object v2, Lcom/android/server/am/BroadcastQueueModernStubImpl;->ACTION_NFC:Ljava/util/Set;

    invoke-interface {v2, v9}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_5

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v2}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v2

    if-nez v2, :cond_5

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v2}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Lcom/android/server/am/PendingIntentRecordImpl;->containsPendingIntent(Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_4

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v2}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2, v8}, Lcom/android/server/am/PendingIntentRecordImpl;->exemptTemporarily(Ljava/lang/String;Z)V

    :cond_4
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "MIUILOG- Allow NFC start application "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-object v3, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v3}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, " action: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v12, v2}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v8

    :cond_5
    iget-boolean v2, v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mIsBlockBroadcastFirstBoot:Z

    const-string v14, " for broadcast "

    const-string v15, "/"

    const-string v3, "Unable to launch app "

    if-eqz v2, :cond_9

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v2}, Landroid/content/Intent;->getComponent()Landroid/content/ComponentName;

    move-result-object v2

    if-nez v2, :cond_9

    invoke-static {v11}, Landroid/os/UserHandle;->getAppId(I)I

    move-result v2

    const/16 v4, 0x2710

    if-lt v2, v4, :cond_6

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v2}, Landroid/content/pm/ApplicationInfo;->isSystemApp()Z

    move-result v2

    if-eqz v2, :cond_7

    :cond_6
    invoke-static {v10}, Landroid/app/AppOpsManagerInjector;->isAutoStartRestriction(Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_7

    move v2, v8

    goto :goto_0

    :cond_7
    move v2, v13

    :goto_0
    if-nez v2, :cond_9

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    if-eqz v4, :cond_8

    const-string v4, "android"

    iget-object v5, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    invoke-virtual {v4, v5}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_9

    :cond_8
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v11}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, ": process is not permitted to first boot block"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v12, v3}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    return v13

    :cond_9
    iget-object v2, v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v2, :cond_a

    const-class v2, Lmiui/security/SecurityManagerInternal;

    invoke-static {v2}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lmiui/security/SecurityManagerInternal;

    iput-object v2, v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_a
    iget-object v2, v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-eqz v2, :cond_13

    iget-object v2, v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    move-object v4, v3

    iget-object v3, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    move-object v5, v4

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    iget-object v7, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    if-eqz v7, :cond_b

    iget-object v7, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    iget-object v7, v7, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    goto :goto_1

    :cond_b
    const/4 v7, 0x0

    :goto_1
    move-object/from16 v16, v5

    move-object v5, v7

    iget v7, v1, Lcom/android/server/am/BroadcastRecord;->userId:I

    move/from16 v17, v8

    move-object/from16 v8, v16

    invoke-virtual/range {v2 .. v7}, Lmiui/security/SecurityManagerInternal;->checkBroadcastWakePath(Landroid/content/Intent;Ljava/lang/String;Landroid/content/pm/ApplicationInfo;Landroid/content/pm/ResolveInfo;I)Z

    move-result v2

    if-eqz v2, :cond_14

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v2}, Landroid/content/pm/ApplicationInfo;->isSystemApp()Z

    move-result v2

    if-nez v2, :cond_d

    invoke-static {v10}, Lmiui/content/pm/PreloadedAppPolicy;->isProtectedDataApp(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_c

    goto :goto_2

    :cond_c
    move v2, v13

    goto :goto_3

    :cond_d
    :goto_2
    move/from16 v2, v17

    :goto_3
    const-string v3, "com.xiaomi.mipush.MESSAGE_ARRIVED"

    invoke-virtual {v3, v9}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v4}, Landroid/content/Intent;->getComponent()Landroid/content/ComponentName;

    move-result-object v4

    if-nez v4, :cond_12

    if-nez v3, :cond_e

    if-eqz v2, :cond_e

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v4}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v4

    if-nez v4, :cond_12

    :cond_e
    if-eqz v2, :cond_f

    sget-object v4, Lcom/android/server/am/BroadcastQueueModernStubImpl;->sSystemSkipAction:Ljava/util/ArrayList;

    invoke-virtual {v4, v9}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_12

    :cond_f
    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v4}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v4

    if-nez v4, :cond_10

    move/from16 v4, v17

    goto :goto_4

    :cond_10
    move v4, v13

    :goto_4
    iget-object v5, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-direct {v0, v6, v4, v5}, Lcom/android/server/am/BroadcastQueueModernStubImpl;->shouldStopBroadcastDispatch(Landroid/content/pm/ResolveInfo;ZLandroid/content/Intent;)Z

    move-result v4

    if-nez v4, :cond_12

    invoke-direct {v0, v9, v6}, Lcom/android/server/am/BroadcastQueueModernStubImpl;->isInternationalSpecialAction(Ljava/lang/String;Landroid/content/pm/ResolveInfo;)Z

    move-result v4

    if-eqz v4, :cond_11

    goto :goto_5

    :cond_11
    const-string v2, " auto start"

    goto :goto_6

    :cond_12
    :goto_5
    return v17

    :cond_13
    move-object v8, v3

    :cond_14
    const-string v2, " wake path"

    :goto_6
    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v11}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, ": process is not permitted to "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v12, v3}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    return v13

    :cond_15
    move/from16 v17, v8

    :goto_7
    return v17

    :cond_16
    move/from16 v17, v8

    :goto_8
    return v17
.end method
""",
        "replacement": """\
.method public checkApplicationAutoStart(Lcom/android/server/am/BroadcastQueue;Lcom/android/server/am/BroadcastRecord;Landroid/content/pm/ResolveInfo;)Z
    .registers 22

    move-object/from16 v0, p0

    move-object/from16 v1, p2

    move-object/from16 v6, p3

    const/4 v8, 0x1

    if-eqz v6, :cond_16

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    if-eqz v2, :cond_16

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    if-nez v2, :cond_0

    move/from16 v17, v8

    goto :goto_8

    :cond_0
    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v2}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object v9

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget-object v10, v2, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget v11, v2, Landroid/content/pm/ApplicationInfo;->uid:I

    sget-boolean v2, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v2, 0x1

    if-eqz v2, :cond_1

    const-string v2, "com.google.android.c2dm.intent.RECEIVE"

    invoke-virtual {v2, v9}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_1

    return v8

    :cond_1
    invoke-static {v10}, Lcom/miui/server/process/ProcessManagerInternal;->checkCtsProcess(Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_15

    invoke-static {}, Landroid/miui/AppOpsUtils;->isXOptMode()Z

    move-result v2

    if-eqz v2, :cond_2

    move/from16 v17, v8

    goto :goto_7

    :cond_2
    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    const-string v12, "BroadcastQueueInjector"

    const/4 v13, 0x0

    if-eqz v2, :cond_3

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    if-eqz v2, :cond_3

    sget-object v2, Lcom/android/server/am/ActivityManagerServiceImpl;->WIDGET_PROVIDER_WHITE_LIST:Ljava/util/List;

    iget-object v3, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    invoke-interface {v2, v3}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v2

    if-nez v2, :cond_3

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v3, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, ":widgetProvider"

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    iget-object v3, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    iget-object v3, v3, Lcom/android/server/am/ProcessRecord;->processName:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    if-eqz v3, :cond_3

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "MIUILOG- Reject widget call from "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v12, v3}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v13

    :cond_3
    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    if-eqz v2, :cond_5

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    iget v2, v2, Lcom/android/server/am/ProcessRecord;->uid:I

    const/16 v3, 0x403

    if-ne v2, v3, :cond_5

    sget-object v2, Lcom/android/server/am/BroadcastQueueModernStubImpl;->ACTION_NFC:Ljava/util/Set;

    invoke-interface {v2, v9}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v2

    if-eqz v2, :cond_5

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v2}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v2

    if-nez v2, :cond_5

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v2}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2}, Lcom/android/server/am/PendingIntentRecordImpl;->containsPendingIntent(Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_4

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v2}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v2

    invoke-static {v2, v8}, Lcom/android/server/am/PendingIntentRecordImpl;->exemptTemporarily(Ljava/lang/String;Z)V

    :cond_4
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "MIUILOG- Allow NFC start application "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-object v3, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v3}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, " action: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v12, v2}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v8

    :cond_5
    iget-boolean v2, v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mIsBlockBroadcastFirstBoot:Z

    const-string v14, " for broadcast "

    const-string v15, "/"

    const-string v3, "Unable to launch app "

    if-eqz v2, :cond_9

    iget-object v2, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v2}, Landroid/content/Intent;->getComponent()Landroid/content/ComponentName;

    move-result-object v2

    if-nez v2, :cond_9

    invoke-static {v11}, Landroid/os/UserHandle;->getAppId(I)I

    move-result v2

    const/16 v4, 0x2710

    if-lt v2, v4, :cond_6

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v2}, Landroid/content/pm/ApplicationInfo;->isSystemApp()Z

    move-result v2

    if-eqz v2, :cond_7

    :cond_6
    invoke-static {v10}, Landroid/app/AppOpsManagerInjector;->isAutoStartRestriction(Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_7

    move v2, v8

    goto :goto_0

    :cond_7
    move v2, v13

    :goto_0
    if-nez v2, :cond_9

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    if-eqz v4, :cond_8

    const-string v4, "android"

    iget-object v5, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    invoke-virtual {v4, v5}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_9

    :cond_8
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v4, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v11}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, ": process is not permitted to first boot block"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v12, v3}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    return v13

    :cond_9
    iget-object v2, v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v2, :cond_a

    const-class v2, Lmiui/security/SecurityManagerInternal;

    invoke-static {v2}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lmiui/security/SecurityManagerInternal;

    iput-object v2, v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_a
    iget-object v2, v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-eqz v2, :cond_13

    iget-object v2, v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    move-object v4, v3

    iget-object v3, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    move-object v5, v4

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    iget-object v7, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    if-eqz v7, :cond_b

    iget-object v7, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    iget-object v7, v7, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    goto :goto_1

    :cond_b
    const/4 v7, 0x0

    :goto_1
    move-object/from16 v16, v5

    move-object v5, v7

    iget v7, v1, Lcom/android/server/am/BroadcastRecord;->userId:I

    move/from16 v17, v8

    move-object/from16 v8, v16

    invoke-virtual/range {v2 .. v7}, Lmiui/security/SecurityManagerInternal;->checkBroadcastWakePath(Landroid/content/Intent;Ljava/lang/String;Landroid/content/pm/ApplicationInfo;Landroid/content/pm/ResolveInfo;I)Z

    move-result v2

    if-eqz v2, :cond_14

    iget-object v2, v6, Landroid/content/pm/ResolveInfo;->activityInfo:Landroid/content/pm/ActivityInfo;

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v2}, Landroid/content/pm/ApplicationInfo;->isSystemApp()Z

    move-result v2

    if-nez v2, :cond_d

    invoke-static {v10}, Lmiui/content/pm/PreloadedAppPolicy;->isProtectedDataApp(Ljava/lang/String;)Z

    move-result v2

    if-eqz v2, :cond_c

    goto :goto_2

    :cond_c
    move v2, v13

    goto :goto_3

    :cond_d
    :goto_2
    move/from16 v2, v17

    :goto_3
    const-string v3, "com.xiaomi.mipush.MESSAGE_ARRIVED"

    invoke-virtual {v3, v9}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v3

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v4}, Landroid/content/Intent;->getComponent()Landroid/content/ComponentName;

    move-result-object v4

    if-nez v4, :cond_12

    if-nez v3, :cond_e

    if-eqz v2, :cond_e

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v4}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v4

    if-nez v4, :cond_12

    :cond_e
    if-eqz v2, :cond_f

    sget-object v4, Lcom/android/server/am/BroadcastQueueModernStubImpl;->sSystemSkipAction:Ljava/util/ArrayList;

    invoke-virtual {v4, v9}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_12

    :cond_f
    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v4}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v4

    if-nez v4, :cond_10

    move/from16 v4, v17

    goto :goto_4

    :cond_10
    move v4, v13

    :goto_4
    iget-object v5, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-direct {v0, v6, v4, v5}, Lcom/android/server/am/BroadcastQueueModernStubImpl;->shouldStopBroadcastDispatch(Landroid/content/pm/ResolveInfo;ZLandroid/content/Intent;)Z

    move-result v4

    if-nez v4, :cond_12

    invoke-direct {v0, v9, v6}, Lcom/android/server/am/BroadcastQueueModernStubImpl;->isInternationalSpecialAction(Ljava/lang/String;Landroid/content/pm/ResolveInfo;)Z

    move-result v4

    if-eqz v4, :cond_11

    goto :goto_5

    :cond_11
    const-string v2, " auto start"

    goto :goto_6

    :cond_12
    :goto_5
    return v17

    :cond_13
    move-object v8, v3

    :cond_14
    const-string v2, " wake path"

    :goto_6
    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v10}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v11}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, ": process is not permitted to "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v12, v3}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    return v13

    :cond_15
    move/from16 v17, v8

    :goto_7
    return v17

    :cond_16
    move/from16 v17, v8

    :goto_8
    return v17
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
    {
        "id":          "replace_method_checkReceiverAppDealBroadcast_Lcom_android_server_am_Broadca",
        "method":      ".method public checkReceiverAppDealBroadcast(Lcom/android/server/am/BroadcastQueue;Lcom/android/server/am/BroadcastRecord;Lcom/android/server/am/ProcessRecord;Z)Z",
        "type":        "method_replace",
        "search": """\
.method public checkReceiverAppDealBroadcast(Lcom/android/server/am/BroadcastQueue;Lcom/android/server/am/BroadcastRecord;Lcom/android/server/am/ProcessRecord;Z)Z
    .registers 19

    move-object/from16 v1, p2

    move-object/from16 v2, p3

    const/4 v3, 0x1

    if-eqz v2, :cond_c

    if-eqz v1, :cond_c

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v0}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object v5

    const-string v0, ""

    const-string v4, ""

    iget-object v12, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v12}, Landroid/content/Intent;->getComponent()Landroid/content/ComponentName;

    move-result-object v6

    if-eqz v6, :cond_1

    invoke-virtual {v12}, Landroid/content/Intent;->getComponent()Landroid/content/ComponentName;

    move-result-object v6

    invoke-virtual {v6}, Landroid/content/ComponentName;->getClassName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v12}, Landroid/content/Intent;->getComponent()Landroid/content/ComponentName;

    move-result-object v6

    invoke-virtual {v6}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v0

    :cond_1
    iget-object v6, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    if-eqz v6, :cond_2

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v6

    if-eqz v6, :cond_2

    iget-object v6, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v0, v6, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    move-object v8, v0

    goto :goto_0

    :cond_2
    move-object v8, v0

    :goto_0
    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->curReceiver:Landroid/content/pm/ActivityInfo;

    if-eqz v0, :cond_3

    invoke-static {v4}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_3

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->curReceiver:Landroid/content/pm/ActivityInfo;

    iget-object v4, v0, Landroid/content/pm/ActivityInfo;->name:Ljava/lang/String;

    move-object v6, v4

    goto :goto_1

    :cond_3
    move-object v6, v4

    :goto_1
    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v0, :cond_4

    const-class v0, Lmiui/security/SecurityManagerInternal;

    invoke-static {v0}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiui/security/SecurityManagerInternal;

    iput-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_4
    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    invoke-static {v8, v0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v0

    const/4 v13, 0x0

    if-nez v0, :cond_5

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-eqz v0, :cond_5

    iget-object v4, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    iget-object v7, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    iget v9, v1, Lcom/android/server/am/BroadcastRecord;->userId:I

    const/16 v10, 0x2000

    const/4 v11, 0x1

    invoke-virtual/range {v4 .. v11}, Lmiui/security/SecurityManagerInternal;->calleeAliveMatchBlackRule(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IIZ)Z

    move-result v0

    if-eqz v0, :cond_5

    return v13

    :cond_5
    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    const-string v4, "BroadcastQueueInjector"

    if-eqz v0, :cond_6

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    iget v0, v0, Lcom/android/server/am/ProcessRecord;->uid:I

    const/16 v7, 0x403

    if-ne v0, v7, :cond_6

    sget-object v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->ACTION_NFC:Ljava/util/Set;

    invoke-interface {v0, v5}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_6

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v0}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_6

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v0}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Lcom/android/server/am/PendingIntentRecordImpl;->containsPendingIntent(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_6

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v0}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0, v3}, Lcom/android/server/am/PendingIntentRecordImpl;->exemptTemporarily(Ljava/lang/String;Z)V

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "MIUILOG- Allow NFC start appliction "

    invoke-virtual {v0, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    iget-object v7, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v7}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v0, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v7, " background start"

    invoke-virtual {v0, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v4, v0}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    :cond_6
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_9

    const-string v0, "android.intent.action.PACKAGE_ADDED"

    invoke-virtual {v0, v5}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_9

    iget-object v0, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v0}, Landroid/content/pm/ApplicationInfo;->isSystemApp()Z

    move-result v0

    if-nez v0, :cond_9

    iget-object v0, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v0}, Landroid/content/pm/ApplicationInfo;->isPrivilegedApp()Z

    move-result v0

    if-nez v0, :cond_9

    iget-object v0, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v0}, Landroid/content/pm/ApplicationInfo;->isSignedWithPlatformKey()Z

    move-result v0

    if-nez v0, :cond_9

    invoke-static {v8}, Landroid/miui/AppOpsUtils;->isExceptionByTestPolicy(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_9

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v0, :cond_7

    const-class v0, Lmiui/security/SecurityManagerInternal;

    invoke-static {v0}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiui/security/SecurityManagerInternal;

    iput-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_7
    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-eqz v0, :cond_9

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    invoke-virtual {v0}, Lmiui/security/SecurityManagerInternal;->enableRejectPackageAddBroadcast()Z

    move-result v0

    if-eqz v0, :cond_9

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    invoke-virtual {v0, v8}, Lmiui/security/SecurityManagerInternal;->isInPackageAddBroadcastWhiteList(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_9

    invoke-virtual {v12}, Landroid/content/Intent;->getData()Landroid/net/Uri;

    move-result-object v7

    if-eqz v7, :cond_9

    invoke-virtual {v7}, Landroid/net/Uri;->getSchemeSpecificPart()Ljava/lang/String;

    move-result-object v9

    :try_start_0
    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v0

    invoke-virtual {v0, v9}, Landroid/content/pm/PackageManager;->getInstallSourceInfo(Ljava/lang/String;)Landroid/content/pm/InstallSourceInfo;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/pm/InstallSourceInfo;->getOriginatingPackageName()Ljava/lang/String;

    move-result-object v10

    invoke-virtual {v8, v10}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v10

    if-nez v10, :cond_8

    new-instance v10, Ljava/lang/StringBuilder;

    invoke-direct {v10}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "MIUILOG- Reject ACTION_PACKAGE_ADDED dispatch to "

    invoke-virtual {v10, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v10

    invoke-static {v4, v10}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return v13

    :cond_8
    goto :goto_2

    :catch_0
    move-exception v0

    const-string v10, "getInstallSourceInfo exception"

    invoke-static {v4, v10, v0}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_9
    :goto_2
    invoke-static {}, Lcom/miui/server/greeze/GreezeManagerInternal;->getInstance()Lcom/miui/server/greeze/GreezeManagerInternal;

    move-result-object v0

    if-nez v0, :cond_a

    return v3

    :cond_a
    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v0}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object v0

    invoke-direct {p0, v2, v0}, Lcom/android/server/am/BroadcastQueueModernStubImpl;->checkSpecialAction(Lcom/android/server/am/ProcessRecord;Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_b

    return v3

    :cond_b
    return v3

    :cond_c
    :goto_3
    return v3
.end method
""",
        "replacement": """\
.method public checkReceiverAppDealBroadcast(Lcom/android/server/am/BroadcastQueue;Lcom/android/server/am/BroadcastRecord;Lcom/android/server/am/ProcessRecord;Z)Z
    .registers 19

    move-object/from16 v1, p2

    move-object/from16 v2, p3

    const/4 v3, 0x1

    if-eqz v2, :cond_c

    if-eqz v1, :cond_c

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v0}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object v5

    const-string v0, ""

    const-string v4, ""

    iget-object v12, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v12}, Landroid/content/Intent;->getComponent()Landroid/content/ComponentName;

    move-result-object v6

    if-eqz v6, :cond_1

    invoke-virtual {v12}, Landroid/content/Intent;->getComponent()Landroid/content/ComponentName;

    move-result-object v6

    invoke-virtual {v6}, Landroid/content/ComponentName;->getClassName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v12}, Landroid/content/Intent;->getComponent()Landroid/content/ComponentName;

    move-result-object v6

    invoke-virtual {v6}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v0

    :cond_1
    iget-object v6, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    if-eqz v6, :cond_2

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v6

    if-eqz v6, :cond_2

    iget-object v6, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v0, v6, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    move-object v8, v0

    goto :goto_0

    :cond_2
    move-object v8, v0

    :goto_0
    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->curReceiver:Landroid/content/pm/ActivityInfo;

    if-eqz v0, :cond_3

    invoke-static {v4}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_3

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->curReceiver:Landroid/content/pm/ActivityInfo;

    iget-object v4, v0, Landroid/content/pm/ActivityInfo;->name:Ljava/lang/String;

    move-object v6, v4

    goto :goto_1

    :cond_3
    move-object v6, v4

    :goto_1
    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v0, :cond_4

    const-class v0, Lmiui/security/SecurityManagerInternal;

    invoke-static {v0}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiui/security/SecurityManagerInternal;

    iput-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_4
    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    invoke-static {v8, v0}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v0

    const/4 v13, 0x0

    if-nez v0, :cond_5

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-eqz v0, :cond_5

    iget-object v4, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    iget-object v7, v1, Lcom/android/server/am/BroadcastRecord;->callerPackage:Ljava/lang/String;

    iget v9, v1, Lcom/android/server/am/BroadcastRecord;->userId:I

    const/16 v10, 0x2000

    const/4 v11, 0x1

    invoke-virtual/range {v4 .. v11}, Lmiui/security/SecurityManagerInternal;->calleeAliveMatchBlackRule(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;IIZ)Z

    move-result v0

    if-eqz v0, :cond_5

    return v13

    :cond_5
    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    const-string v4, "BroadcastQueueInjector"

    if-eqz v0, :cond_6

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->callerApp:Lcom/android/server/am/ProcessRecord;

    iget v0, v0, Lcom/android/server/am/ProcessRecord;->uid:I

    const/16 v7, 0x403

    if-ne v0, v7, :cond_6

    sget-object v0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->ACTION_NFC:Ljava/util/Set;

    invoke-interface {v0, v5}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_6

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v0}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v0

    if-nez v0, :cond_6

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v0}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Lcom/android/server/am/PendingIntentRecordImpl;->containsPendingIntent(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_6

    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v0}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0, v3}, Lcom/android/server/am/PendingIntentRecordImpl;->exemptTemporarily(Ljava/lang/String;Z)V

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "MIUILOG- Allow NFC start appliction "

    invoke-virtual {v0, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    iget-object v7, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v7}, Landroid/content/Intent;->getPackage()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v0, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v7, " background start"

    invoke-virtual {v0, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-static {v4, v0}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    :cond_6
    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v0, 0x1

    if-nez v0, :cond_9

    const-string v0, "android.intent.action.PACKAGE_ADDED"

    invoke-virtual {v0, v5}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_9

    iget-object v0, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v0}, Landroid/content/pm/ApplicationInfo;->isSystemApp()Z

    move-result v0

    if-nez v0, :cond_9

    iget-object v0, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v0}, Landroid/content/pm/ApplicationInfo;->isPrivilegedApp()Z

    move-result v0

    if-nez v0, :cond_9

    iget-object v0, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    invoke-virtual {v0}, Landroid/content/pm/ApplicationInfo;->isSignedWithPlatformKey()Z

    move-result v0

    if-nez v0, :cond_9

    invoke-static {v8}, Landroid/miui/AppOpsUtils;->isExceptionByTestPolicy(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_9

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v0, :cond_7

    const-class v0, Lmiui/security/SecurityManagerInternal;

    invoke-static {v0}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiui/security/SecurityManagerInternal;

    iput-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_7
    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-eqz v0, :cond_9

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    invoke-virtual {v0}, Lmiui/security/SecurityManagerInternal;->enableRejectPackageAddBroadcast()Z

    move-result v0

    if-eqz v0, :cond_9

    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    invoke-virtual {v0, v8}, Lmiui/security/SecurityManagerInternal;->isInPackageAddBroadcastWhiteList(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_9

    invoke-virtual {v12}, Landroid/content/Intent;->getData()Landroid/net/Uri;

    move-result-object v7

    if-eqz v7, :cond_9

    invoke-virtual {v7}, Landroid/net/Uri;->getSchemeSpecificPart()Ljava/lang/String;

    move-result-object v9

    :try_start_0
    iget-object v0, p0, Lcom/android/server/am/BroadcastQueueModernStubImpl;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v0

    invoke-virtual {v0, v9}, Landroid/content/pm/PackageManager;->getInstallSourceInfo(Ljava/lang/String;)Landroid/content/pm/InstallSourceInfo;

    move-result-object v0

    invoke-virtual {v0}, Landroid/content/pm/InstallSourceInfo;->getOriginatingPackageName()Ljava/lang/String;

    move-result-object v10

    invoke-virtual {v8, v10}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v10

    if-nez v10, :cond_8

    new-instance v10, Ljava/lang/StringBuilder;

    invoke-direct {v10}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "MIUILOG- Reject ACTION_PACKAGE_ADDED dispatch to "

    invoke-virtual {v10, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v10

    invoke-static {v4, v10}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    return v13

    :cond_8
    goto :goto_2

    :catch_0
    move-exception v0

    const-string v10, "getInstallSourceInfo exception"

    invoke-static {v4, v10, v0}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    :cond_9
    :goto_2
    invoke-static {}, Lcom/miui/server/greeze/GreezeManagerInternal;->getInstance()Lcom/miui/server/greeze/GreezeManagerInternal;

    move-result-object v0

    if-nez v0, :cond_a

    return v3

    :cond_a
    iget-object v0, v1, Lcom/android/server/am/BroadcastRecord;->intent:Landroid/content/Intent;

    invoke-virtual {v0}, Landroid/content/Intent;->getAction()Ljava/lang/String;

    move-result-object v0

    invoke-direct {p0, v2, v0}, Lcom/android/server/am/BroadcastQueueModernStubImpl;->checkSpecialAction(Lcom/android/server/am/ProcessRecord;Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_b

    return v3

    :cond_b
    return v3

    :cond_c
    :goto_3
    return v3
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
]
