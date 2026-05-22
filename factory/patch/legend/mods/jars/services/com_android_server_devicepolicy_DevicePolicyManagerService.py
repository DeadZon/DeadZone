"""
Legend MTCR patch - class-level rule.

Target JAR   : services.jar
Target class : com/android/server/devicepolicy/DevicePolicyManagerService
Source MTCR  : Service_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "services.jar"
TARGET_CLASS = "com/android/server/devicepolicy/DevicePolicyManagerService.smali"
CLASS_FALLBACK_NAMES = ['DevicePolicyManagerService.smali']
CLASS_ANCHORS        = ['Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda205;', 'Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda127;', 'Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda195;', 'Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda24;', 'Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda86;', 'Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda46;']

PATCHES = [
    {
        "id":          "replace_method_addCrossProfileIntentFilter_Lcom_android_server_pm_DefaultCr",
        "method":      ".method addCrossProfileIntentFilter(Lcom/android/server/pm/DefaultCrossProfileIntentFilter;II)V",
        "method_name": 'addCrossProfileIntentFilter',
        "type":        "method_replace",
        "search": """\
.method addCrossProfileIntentFilter(Lcom/android/server/pm/DefaultCrossProfileIntentFilter;II)V
    .registers 20
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Landroid/os/RemoteException;
        }
    .end annotation

    move-object/from16 v0, p0

    move-object/from16 v1, p1

    iget v2, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->direction:I

    const/4 v3, 0x1

    if-ne v2, v3, :cond_0

    iget-object v4, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIPackageManager:Landroid/content/pm/IPackageManager;

    iget-object v2, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->filter:Lcom/android/server/pm/WatchedIntentFilter;

    invoke-virtual {v2}, Lcom/android/server/pm/WatchedIntentFilter;->getIntentFilter()Landroid/content/IntentFilter;

    move-result-object v5

    iget-object v2, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v6

    iget v9, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->flags:I

    move/from16 v7, p2

    move/from16 v8, p3

    invoke-interface/range {v4 .. v9}, Landroid/content/pm/IPackageManager;->addCrossProfileIntentFilter(Landroid/content/IntentFilter;Ljava/lang/String;III)V

    goto :goto_0

    :cond_0
    iget-object v10, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIPackageManager:Landroid/content/pm/IPackageManager;

    iget-object v2, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->filter:Lcom/android/server/pm/WatchedIntentFilter;

    invoke-virtual {v2}, Lcom/android/server/pm/WatchedIntentFilter;->getIntentFilter()Landroid/content/IntentFilter;

    move-result-object v11

    iget-object v2, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v2}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v12

    iget v15, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->flags:I

    move/from16 v14, p2

    move/from16 v13, p3

    invoke-interface/range {v10 .. v15}, Landroid/content/pm/IPackageManager;->addCrossProfileIntentFilter(Landroid/content/IntentFilter;Ljava/lang/String;III)V

    :goto_0
    return-void
.end method
""",
        "replacement": """\
.method addCrossProfileIntentFilter(Lcom/android/server/pm/DefaultCrossProfileIntentFilter;II)V
    .registers 20
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Landroid/os/RemoteException;
        }
    .end annotation

    goto :goto_d

    nop

    :goto_0
    iget-object v2, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->filter:Lcom/android/server/pm/WatchedIntentFilter;

    goto :goto_9

    nop

    :goto_1
    move/from16 v13, p3

    goto :goto_a

    nop

    :goto_2
    iget-object v2, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    goto :goto_16

    nop

    :goto_3
    if-eq v2, v3, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_f

    nop

    :goto_4
    move/from16 v8, p3

    goto :goto_12

    nop

    :goto_5
    goto :goto_b

    :goto_6
    goto :goto_8

    nop

    :goto_7
    move-object/from16 v1, p1

    goto :goto_19

    nop

    :goto_8
    iget-object v10, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIPackageManager:Landroid/content/pm/IPackageManager;

    goto :goto_0

    nop

    :goto_9
    invoke-virtual {v2}, Lcom/android/server/pm/WatchedIntentFilter;->getIntentFilter()Landroid/content/IntentFilter;

    move-result-object v11

    goto :goto_2

    nop

    :goto_a
    invoke-interface/range {v10 .. v15}, Landroid/content/pm/IPackageManager;->addCrossProfileIntentFilter(Landroid/content/IntentFilter;Ljava/lang/String;III)V

    :goto_b
    goto :goto_18

    nop

    :goto_c
    move/from16 v14, p2

    goto :goto_1

    nop

    :goto_d
    move-object/from16 v0, p0

    goto :goto_7

    nop

    :goto_e
    invoke-virtual {v2}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v6

    goto :goto_13

    nop

    :goto_f
    iget-object v4, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIPackageManager:Landroid/content/pm/IPackageManager;

    goto :goto_10

    nop

    :goto_10
    iget-object v2, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->filter:Lcom/android/server/pm/WatchedIntentFilter;

    goto :goto_14

    nop

    :goto_11
    const/4 v3, 0x1

    goto :goto_3

    nop

    :goto_12
    invoke-interface/range {v4 .. v9}, Landroid/content/pm/IPackageManager;->addCrossProfileIntentFilter(Landroid/content/IntentFilter;Ljava/lang/String;III)V

    goto :goto_5

    nop

    :goto_13
    iget v9, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->flags:I

    goto :goto_1a

    nop

    :goto_14
    invoke-virtual {v2}, Lcom/android/server/pm/WatchedIntentFilter;->getIntentFilter()Landroid/content/IntentFilter;

    move-result-object v5

    goto :goto_17

    nop

    :goto_15
    iget v15, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->flags:I

    goto :goto_c

    nop

    :goto_16
    invoke-virtual {v2}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v12

    goto :goto_15

    nop

    :goto_17
    iget-object v2, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    goto :goto_e

    nop

    :goto_18
    return-void

    :goto_19
    iget v2, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->direction:I

    goto :goto_11

    nop

    :goto_1a
    move/from16 v7, p2

    goto :goto_4

    nop
.end method
""",
        "method_anchors": ['iget v2, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->direction:I', 'if-ne v2, v3, :cond_0', 'iget-object v4, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIPackageManager:Landroid/content/pm/IPackageManager;', 'iget-object v2, v1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->filter:Lcom/android/server/pm/WatchedIntentFilter;', 'invoke-virtual {v2}, Lcom/android/server/pm/WatchedIntentFilter;->getIntentFilter()Landroid/content/IntentFilter;', 'move-result-object v5'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_deleteTransferOwnershipBundleLocked_I_V",
        "method":      ".method deleteTransferOwnershipBundleLocked(I)V",
        "method_name": 'deleteTransferOwnershipBundleLocked',
        "type":        "method_replace",
        "search": """\
.method deleteTransferOwnershipBundleLocked(I)V
    .registers 5

    new-instance v0, Ljava/io/File;

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPathProvider:Lcom/android/server/devicepolicy/PolicyPathProvider;

    invoke-interface {v1, p1}, Lcom/android/server/devicepolicy/PolicyPathProvider;->getUserSystemDirectory(I)Ljava/io/File;

    move-result-object v1

    const-string v2, "transfer-ownership-parameters.xml"

    invoke-direct {v0, v1, v2}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/io/File;->delete()Z

    return-void
.end method
""",
        "replacement": """\
.method deleteTransferOwnershipBundleLocked(I)V
    .registers 5

    goto :goto_5

    nop

    :goto_0
    return-void

    :goto_1
    const-string v2, "transfer-ownership-parameters.xml"

    goto :goto_4

    nop

    :goto_2
    invoke-virtual {v0}, Ljava/io/File;->delete()Z

    goto :goto_0

    nop

    :goto_3
    invoke-interface {v1, p1}, Lcom/android/server/devicepolicy/PolicyPathProvider;->getUserSystemDirectory(I)Ljava/io/File;

    move-result-object v1

    goto :goto_1

    nop

    :goto_4
    invoke-direct {v0, v1, v2}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V

    goto :goto_2

    nop

    :goto_5
    new-instance v0, Ljava/io/File;

    goto :goto_6

    nop

    :goto_6
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPathProvider:Lcom/android/server/devicepolicy/PolicyPathProvider;

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['new-instance v0, Ljava/io/File;', 'iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPathProvider:Lcom/android/server/devicepolicy/PolicyPathProvider;', 'invoke-interface {v1, p1}, Lcom/android/server/devicepolicy/PolicyPathProvider;->getUserSystemDirectory(I)Ljava/io/File;', 'move-result-object v1', 'const-string v2, "transfer-ownership-parameters.xml"', 'invoke-direct {v0, v1, v2}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_dump_Ljava_io_FileDescriptor_Ljava_io_PrintWriter__Ljava_lan",
        "method":      ".method protected dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V",
        "method_name": 'dump',
        "type":        "method_replace",
        "search": """\
.method protected dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V
    .registers 10

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    const-string v1, "DevicePolicyManager"

    invoke-static {v0, v1, p2}, Lcom/android/internal/util/DumpUtils;->checkDumpPermission(Landroid/content/Context;Ljava/lang/String;Ljava/io/PrintWriter;)Z

    move-result v0

    if-nez v0, :cond_0

    return-void

    :cond_0
    new-instance v0, Landroid/util/IndentingPrintWriter;

    const-string v1, "  "

    invoke-direct {v0, p2, v1}, Landroid/util/IndentingPrintWriter;-><init>(Ljava/io/Writer;Ljava/lang/String;)V

    :try_start_0
    const-string v1, "Current Device Policy Manager state:"

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->dumpImmutableState(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v1

    monitor-enter v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_2

    :try_start_1
    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/Owners;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDeviceAdminServiceController:Lcom/android/server/devicepolicy/DeviceAdminServiceController;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/DeviceAdminServiceController;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->dumpPerUserPolicyData(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mConstants:Lcom/android/server/devicepolicy/DevicePolicyConstants;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/DevicePolicyConstants;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStatLogger:Lcom/android/internal/util/StatLogger;

    invoke-virtual {v2, v0}, Lcom/android/internal/util/StatLogger;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Encryption Status: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getEncryptionStatus()I

    move-result v3

    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getEncryptionStatusName(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Logout user: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLogoutUserIdUnchecked()I

    move-result v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPendingUserCreatedCallbackTokens:Ljava/util/ArrayList;

    invoke-virtual {v2}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v2

    if-eqz v2, :cond_1

    const-string v2, "no pending user created callback tokens"

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_1

    :cond_1
    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPendingUserCreatedCallbackTokens:Ljava/util/ArrayList;

    invoke-virtual {v2}, Ljava/util/ArrayList;->size()I

    move-result v2

    const-string v3, "%d pending user created callback token%s\\n"

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    const/4 v5, 0x1

    if-ne v2, v5, :cond_2

    const-string v5, ""

    goto :goto_0

    :cond_2
    const-string v5, "s"

    :goto_0
    filled-new-array {v4, v5}, [Ljava/lang/Object;

    move-result-object v4

    invoke-virtual {v0, v3, v4}, Landroid/util/IndentingPrintWriter;->printf(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;

    :goto_1
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPolicyCache:Lcom/android/server/devicepolicy/DevicePolicyCacheImpl;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/DevicePolicyCacheImpl;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStateCache:Lcom/android/server/devicepolicy/DeviceStateCacheImpl;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/DeviceStateCacheImpl;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    :try_start_2
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->dumpPersonalAppInfoForSystemUserNoLock(Landroid/util/IndentingPrintWriter;)V

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSubscriptionsChangedListenerLock:Ljava/lang/Object;

    monitor-enter v1
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_2

    :try_start_3
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Subscription changed listener : "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSubscriptionsChangedListener:Landroid/telephony/SubscriptionManager$OnSubscriptionsChangedListener;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    monitor-exit v1
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "DPM global setting ALLOW_WORK_PROFILE_TELEPHONY_FOR_NON_DPM_ROLE_HOLDERS : "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    const-string v3, "allow_work_profile_telephony_for_non_dpm_role_holders"

    invoke-virtual {v2, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->settingsGlobalGetString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHandler:Landroid/os/Handler;

    new-instance v2, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda47;

    invoke-direct {v2, p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda47;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v1, v2}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->dumpResources(Landroid/util/IndentingPrintWriter;)V
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_2

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->close()V

    return-void

    :catchall_0
    move-exception v2

    :try_start_5
    monitor-exit v1
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_0

    :try_start_6
    throw v2
    :try_end_6
    .catchall {:try_start_6 .. :try_end_6} :catchall_2

    :catchall_1
    move-exception v2

    :try_start_7
    monitor-exit v1
    :try_end_7
    .catchall {:try_start_7 .. :try_end_7} :catchall_1

    :try_start_8
    throw v2
    :try_end_8
    .catchall {:try_start_8 .. :try_end_8} :catchall_2

    :catchall_2
    move-exception v1

    :try_start_9
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->close()V
    :try_end_9
    .catchall {:try_start_9 .. :try_end_9} :catchall_3

    goto :goto_2

    :catchall_3
    move-exception v2

    invoke-virtual {v1, v2}, Ljava/lang/Throwable;->addSuppressed(Ljava/lang/Throwable;)V

    :goto_2
    throw v1
.end method
""",
        "replacement": """\
.method protected dump(Ljava/io/FileDescriptor;Ljava/io/PrintWriter;[Ljava/lang/String;)V
    .registers 10

    goto :goto_7

    nop

    :goto_0
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->close()V

    goto :goto_c

    nop

    :goto_1
    const-string v1, "DevicePolicyManager"

    goto :goto_d

    nop

    :goto_2
    const-string v1, "  "

    goto :goto_8

    nop

    :goto_3
    throw v1

    :goto_4
    return-void

    :goto_5
    goto :goto_6

    nop

    :goto_6
    new-instance v0, Landroid/util/IndentingPrintWriter;

    goto :goto_2

    nop

    :goto_7
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    goto :goto_1

    nop

    :goto_8
    invoke-direct {v0, p2, v1}, Landroid/util/IndentingPrintWriter;-><init>(Ljava/io/Writer;Ljava/lang/String;)V

    :try_start_0
    const-string v1, "Current Device Policy Manager state:"

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->increaseIndent()Landroid/util/IndentingPrintWriter;

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->dumpImmutableState(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v1

    monitor-enter v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_2

    :try_start_1
    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/Owners;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDeviceAdminServiceController:Lcom/android/server/devicepolicy/DeviceAdminServiceController;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/DeviceAdminServiceController;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->dumpPerUserPolicyData(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mConstants:Lcom/android/server/devicepolicy/DevicePolicyConstants;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/DevicePolicyConstants;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStatLogger:Lcom/android/internal/util/StatLogger;

    invoke-virtual {v2, v0}, Lcom/android/internal/util/StatLogger;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Encryption Status: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getEncryptionStatus()I

    move-result v3

    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getEncryptionStatusName(I)Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Logout user: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLogoutUserIdUnchecked()I

    move-result v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPendingUserCreatedCallbackTokens:Ljava/util/ArrayList;

    invoke-virtual {v2}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v2

    if-eqz v2, :cond_0

    const-string v2, "no pending user created callback tokens"

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    goto :goto_a

    :cond_0
    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPendingUserCreatedCallbackTokens:Ljava/util/ArrayList;

    invoke-virtual {v2}, Ljava/util/ArrayList;->size()I

    move-result v2

    const-string v3, "%d pending user created callback token%s\\n"

    invoke-static {v2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v4

    const/4 v5, 0x1

    if-ne v2, v5, :cond_1

    const-string v5, ""

    goto :goto_9

    :cond_1
    const-string v5, "s"

    :goto_9
    filled-new-array {v4, v5}, [Ljava/lang/Object;

    move-result-object v4

    invoke-virtual {v0, v3, v4}, Landroid/util/IndentingPrintWriter;->printf(Ljava/lang/String;[Ljava/lang/Object;)Ljava/io/PrintWriter;

    :goto_a
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPolicyCache:Lcom/android/server/devicepolicy/DevicePolicyCacheImpl;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/DevicePolicyCacheImpl;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStateCache:Lcom/android/server/devicepolicy/DeviceStateCacheImpl;

    invoke-virtual {v2, v0}, Lcom/android/server/devicepolicy/DeviceStateCacheImpl;->dump(Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->println()V

    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    :try_start_2
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->dumpPersonalAppInfoForSystemUserNoLock(Landroid/util/IndentingPrintWriter;)V

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSubscriptionsChangedListenerLock:Ljava/lang/Object;

    monitor-enter v1
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_2

    :try_start_3
    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Subscription changed listener : "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSubscriptionsChangedListener:Landroid/telephony/SubscriptionManager$OnSubscriptionsChangedListener;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v0, v2}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    monitor-exit v1
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "DPM global setting ALLOW_WORK_PROFILE_TELEPHONY_FOR_NON_DPM_ROLE_HOLDERS : "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    const-string v3, "allow_work_profile_telephony_for_non_dpm_role_holders"

    invoke-virtual {v2, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->settingsGlobalGetString(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Landroid/util/IndentingPrintWriter;->println(Ljava/lang/String;)V

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHandler:Landroid/os/Handler;

    new-instance v2, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda47;

    invoke-direct {v2, p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda47;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;Landroid/util/IndentingPrintWriter;)V

    invoke-virtual {v1, v2}, Landroid/os/Handler;->post(Ljava/lang/Runnable;)Z

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->dumpResources(Landroid/util/IndentingPrintWriter;)V
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_2

    goto :goto_0

    nop

    :goto_b
    if-eqz v0, :cond_2

    goto :goto_5

    :cond_2
    goto :goto_4

    nop

    :goto_c
    return-void

    :catchall_0
    move-exception v2

    :try_start_5
    monitor-exit v1
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_0

    :try_start_6
    throw v2
    :try_end_6
    .catchall {:try_start_6 .. :try_end_6} :catchall_2

    :catchall_1
    move-exception v2

    :try_start_7
    monitor-exit v1
    :try_end_7
    .catchall {:try_start_7 .. :try_end_7} :catchall_1

    :try_start_8
    throw v2
    :try_end_8
    .catchall {:try_start_8 .. :try_end_8} :catchall_2

    :catchall_2
    move-exception v1

    :try_start_9
    invoke-virtual {v0}, Landroid/util/IndentingPrintWriter;->close()V
    :try_end_9
    .catchall {:try_start_9 .. :try_end_9} :catchall_3

    goto :goto_10

    nop

    :goto_d
    invoke-static {v0, v1, p2}, Lcom/android/internal/util/DumpUtils;->checkDumpPermission(Landroid/content/Context;Ljava/lang/String;Ljava/io/PrintWriter;)Z

    move-result v0

    goto :goto_b

    nop

    :goto_e
    invoke-virtual {v1, v2}, Ljava/lang/Throwable;->addSuppressed(Ljava/lang/Throwable;)V

    :goto_f
    goto :goto_3

    nop

    :goto_10
    goto :goto_f

    :catchall_3
    move-exception v2

    goto :goto_e

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;', 'const-string v1, "DevicePolicyManager"', 'invoke-static {v0, v1, p2}, Lcom/android/internal/util/DumpUtils;->checkDumpPermission(Landroid/content/Context;Ljava/lang/String;Ljava/io/PrintWriter;)Z', 'move-result v0', 'if-nez v0, :cond_0', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_ensureLocked__V",
        "method":      ".method final ensureLocked()V",
        "method_name": 'ensureLocked',
        "type":        "method_replace",
        "search": """\
.method final ensureLocked()V
    .registers 3

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mLockDoNoUseDirectly:Ljava/lang/Object;

    invoke-static {v0}, Ljava/lang/Thread;->holdsLock(Ljava/lang/Object;)Z

    move-result v0

    if-eqz v0, :cond_0

    return-void

    :cond_0
    const-string v0, "DevicePolicyManager"

    const-string v1, "Not holding DPMS lock."

    invoke-static {v0, v1}, Lcom/android/server/utils/Slogf;->wtfStack(Ljava/lang/String;Ljava/lang/String;)I

    return-void
.end method
""",
        "replacement": """\
.method final ensureLocked()V
    .registers 3

    goto :goto_7

    nop

    :goto_0
    const-string v0, "DevicePolicyManager"

    goto :goto_4

    nop

    :goto_1
    return-void

    :goto_2
    goto :goto_0

    nop

    :goto_3
    invoke-static {v0}, Ljava/lang/Thread;->holdsLock(Ljava/lang/Object;)Z

    move-result v0

    goto :goto_6

    nop

    :goto_4
    const-string v1, "Not holding DPMS lock."

    goto :goto_8

    nop

    :goto_5
    return-void

    :goto_6
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_7
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mLockDoNoUseDirectly:Ljava/lang/Object;

    goto :goto_3

    nop

    :goto_8
    invoke-static {v0, v1}, Lcom/android/server/utils/Slogf;->wtfStack(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_5

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mLockDoNoUseDirectly:Ljava/lang/Object;', 'invoke-static {v0}, Ljava/lang/Thread;->holdsLock(Ljava/lang/Object;)Z', 'move-result v0', 'if-eqz v0, :cond_0', 'return-void', 'const-string v0, "DevicePolicyManager"'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getAcceptedCaCertificates_Landroid_os_UserHandle__Ljava_util",
        "method":      ".method protected getAcceptedCaCertificates(Landroid/os/UserHandle;)Ljava/util/Set;",
        "method_name": 'getAcceptedCaCertificates',
        "type":        "method_replace",
        "search": """\
.method protected getAcceptedCaCertificates(Landroid/os/UserHandle;)Ljava/util/Set;
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/os/UserHandle;",
            ")",
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation

    iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z

    if-nez v0, :cond_0

    invoke-static {}, Ljava/util/Collections;->emptySet()Ljava/util/Set;

    move-result-object v0

    return-object v0

    :cond_0
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    :try_start_0
    invoke-virtual {p1}, Landroid/os/UserHandle;->getIdentifier()I

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    iget-object v2, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAcceptedCaCertificates:Landroid/util/ArraySet;

    monitor-exit v0

    return-object v2

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method protected getAcceptedCaCertificates(Landroid/os/UserHandle;)Ljava/util/Set;
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/os/UserHandle;",
            ")",
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation

    goto :goto_5

    nop

    :goto_0
    return-object v0

    :goto_1
    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_7

    nop

    :goto_3
    invoke-static {}, Ljava/util/Collections;->emptySet()Ljava/util/Set;

    move-result-object v0

    goto :goto_0

    nop

    :goto_4
    throw v1

    :goto_5
    iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z

    goto :goto_6

    nop

    :goto_6
    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_3

    nop

    :goto_7
    monitor-enter v0

    :try_start_0
    invoke-virtual {p1}, Landroid/os/UserHandle;->getIdentifier()I

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    iget-object v2, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAcceptedCaCertificates:Landroid/util/ArraySet;

    monitor-exit v0

    return-object v2

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_4

    nop
.end method
""",
        "method_anchors": ['iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z', 'if-nez v0, :cond_0', 'invoke-static {}, Ljava/util/Collections;->emptySet()Ljava/util/Set;', 'move-result-object v0', 'return-object v0', 'invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getActiveAdminForCallerLocked_Landroid_content_ComponentName",
        "method":      ".method getActiveAdminForCallerLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getActiveAdminForCallerLocked',
        "type":        "method_replace",
        "search": """\
.method getActiveAdminForCallerLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    const/4 v0, 0x0

    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;ILjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    return-object v0
.end method
""",
        "replacement": """\
.method getActiveAdminForCallerLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    goto :goto_0

    nop

    :goto_0
    const/4 v0, 0x0

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;ILjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_2

    nop

    :goto_2
    return-object v0
.end method
""",
        "method_anchors": ['invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;ILjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;', 'move-result-object v0', 'return-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getActiveAdminForCallerLocked_Landroid_content_ComponentName",
        "method":      ".method getActiveAdminForCallerLocked(Landroid/content/ComponentName;IZ)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getActiveAdminForCallerLocked',
        "type":        "method_replace",
        "search": """\
.method getActiveAdminForCallerLocked(Landroid/content/ComponentName;IZ)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 5
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    const/4 v0, 0x0

    invoke-virtual {p0, p1, p2, p3, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;IZLjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    return-object v0
.end method
""",
        "replacement": """\
.method getActiveAdminForCallerLocked(Landroid/content/ComponentName;IZ)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 5
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    goto :goto_2

    nop

    :goto_0
    return-object v0

    :goto_1
    invoke-virtual {p0, p1, p2, p3, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;IZLjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_0

    nop

    :goto_2
    const/4 v0, 0x0

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0, p1, p2, p3, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;IZLjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;', 'move-result-object v0', 'return-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getActiveAdminOrCheckPermissionForCallerLocked_Landroid_cont",
        "method":      ".method getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;ILjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getActiveAdminOrCheckPermissionForCallerLocked',
        "type":        "method_replace",
        "search": """\
.method getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;ILjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 5
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    nop

    if-nez p3, :cond_0

    invoke-static {}, Ljava/util/Set;->of()Ljava/util/Set;

    move-result-object v0

    goto :goto_0

    :cond_0
    invoke-static {p3}, Ljava/util/Set;->of(Ljava/lang/Object;)Ljava/util/Set;

    move-result-object v0

    :goto_0
    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;ILjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    return-object v0
.end method
""",
        "replacement": """\
.method getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;ILjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 5
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    nop

    goto :goto_7

    nop

    :goto_0
    invoke-static {p3}, Ljava/util/Set;->of(Ljava/lang/Object;)Ljava/util/Set;

    move-result-object v0

    :goto_1
    goto :goto_3

    nop

    :goto_2
    invoke-static {}, Ljava/util/Set;->of()Ljava/util/Set;

    move-result-object v0

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;ILjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_6

    nop

    :goto_4
    goto :goto_1

    :goto_5
    goto :goto_0

    nop

    :goto_6
    return-object v0

    :goto_7
    if-eqz p3, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['if-nez p3, :cond_0', 'invoke-static {}, Ljava/util/Set;->of()Ljava/util/Set;', 'move-result-object v0', 'invoke-static {p3}, Ljava/util/Set;->of(Ljava/lang/Object;)Ljava/util/Set;', 'move-result-object v0', 'invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;ILjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getActiveAdminOrCheckPermissionForCallerLocked_Landroid_cont",
        "method":      ".method getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;IZLjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getActiveAdminOrCheckPermissionForCallerLocked',
        "type":        "method_replace",
        "search": """\
.method getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;IZLjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 6
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    nop

    if-nez p4, :cond_0

    invoke-static {}, Ljava/util/Set;->of()Ljava/util/Set;

    move-result-object v0

    goto :goto_0

    :cond_0
    invoke-static {p4}, Ljava/util/Set;->of(Ljava/lang/Object;)Ljava/util/Set;

    move-result-object v0

    :goto_0
    invoke-virtual {p0, p1, p2, p3, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;IZLjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    return-object v0
.end method
""",
        "replacement": """\
.method getActiveAdminOrCheckPermissionForCallerLocked(Landroid/content/ComponentName;IZLjava/lang/String;)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 6
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    nop

    goto :goto_5

    nop

    :goto_0
    goto :goto_3

    :goto_1
    goto :goto_2

    nop

    :goto_2
    invoke-static {p4}, Ljava/util/Set;->of(Ljava/lang/Object;)Ljava/util/Set;

    move-result-object v0

    :goto_3
    goto :goto_7

    nop

    :goto_4
    invoke-static {}, Ljava/util/Set;->of()Ljava/util/Set;

    move-result-object v0

    goto :goto_0

    nop

    :goto_5
    if-eqz p4, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_4

    nop

    :goto_6
    return-object v0

    :goto_7
    invoke-virtual {p0, p1, p2, p3, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;IZLjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_6

    nop
.end method
""",
        "method_anchors": ['if-nez p4, :cond_0', 'invoke-static {}, Ljava/util/Set;->of()Ljava/util/Set;', 'move-result-object v0', 'invoke-static {p4}, Ljava/util/Set;->of(Ljava/lang/Object;)Ljava/util/Set;', 'move-result-object v0', 'invoke-virtual {p0, p1, p2, p3, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;IZLjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getActiveAdminOrCheckPermissionsForCallerLocked_Landroid_con",
        "method":      ".method getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;ILjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getActiveAdminOrCheckPermissionsForCallerLocked',
        "type":        "method_replace",
        "search": """\
.method getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;ILjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 13
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/ComponentName;",
            "I",
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;)",
            "Lcom/android/server/devicepolicy/ActiveAdmin;"
        }
    .end annotation

    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity()Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUid()I

    move-result v1

    invoke-direct {p0, p1, p2, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminWithPolicyForUidLocked(Landroid/content/ComponentName;II)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v1

    if-eqz v1, :cond_0

    return-object v1

    :cond_0
    invoke-interface {p3}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_0
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_2

    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Ljava/lang/String;

    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->hasCallingPermission(Ljava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_1

    const/4 v2, 0x0

    return-object v2

    :cond_1
    goto :goto_0

    :cond_2
    if-eqz p1, :cond_4

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v2

    invoke-virtual {p0, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v2

    iget-object v3, v2, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    invoke-virtual {v3, p1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lcom/android/server/devicepolicy/ActiveAdmin;

    iget-object v4, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v4}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v4

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v5

    invoke-virtual {p0, v4, v5}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isDeviceOwner(Landroid/content/ComponentName;I)Z

    move-result v4

    iget-object v5, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v5}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v5

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v6

    invoke-virtual {p0, v5, v6}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwner(Landroid/content/ComponentName;I)Z

    move-result v5

    sget-object v6, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->DA_DISALLOWED_POLICIES:Ljava/util/Set;

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v7

    invoke-interface {v6, v7}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v6

    const-string v7, "Admin "

    if-eqz v6, :cond_3

    if-nez v4, :cond_3

    if-nez v5, :cond_3

    new-instance v6, Ljava/lang/SecurityException;

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v8, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v8}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v8

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, " is not a device owner or profile owner, so may not use policy: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v8, p2}, Landroid/app/admin/DeviceAdminInfo;->getTagForPolicy(I)Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-direct {v6, v7}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    throw v6

    :cond_3
    new-instance v6, Ljava/lang/SecurityException;

    new-instance v8, Ljava/lang/StringBuilder;

    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v8, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v8}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v8

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, " did not specify uses-policy for: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v8, p2}, Landroid/app/admin/DeviceAdminInfo;->getTagForPolicy(I)Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-direct {v6, v7}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    throw v6

    :cond_4
    new-instance v2, Ljava/lang/SecurityException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "No active admin owned by uid "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUid()I

    move-result v4

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, " for policy #"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-interface {p3}, Ljava/util/Set;->isEmpty()Z

    move-result v4

    if-eqz v4, :cond_5

    const-string v4, ""

    goto :goto_1

    :cond_5
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, ", which doesn\\'t have "

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, p3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    :goto_1
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    throw v2
.end method
""",
        "replacement": """\
.method getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;ILjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 13
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/ComponentName;",
            "I",
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;)",
            "Lcom/android/server/devicepolicy/ActiveAdmin;"
        }
    .end annotation

    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    goto :goto_38

    nop

    :goto_0
    invoke-direct {v6, v7}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    goto :goto_47

    nop

    :goto_1
    invoke-virtual {v5}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v5

    goto :goto_22

    nop

    :goto_2
    invoke-direct {p0, p1, p2, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminWithPolicyForUidLocked(Landroid/content/ComponentName;II)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v1

    goto :goto_39

    nop

    :goto_3
    const-string v5, ", which doesn\\'t have "

    goto :goto_36

    nop

    :goto_4
    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    goto :goto_1d

    nop

    :goto_5
    invoke-virtual {p0, v5, v6}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwner(Landroid/content/ComponentName;I)Z

    move-result v5

    goto :goto_37

    nop

    :goto_6
    new-instance v4, Ljava/lang/StringBuilder;

    goto :goto_1e

    nop

    :goto_7
    new-instance v2, Ljava/lang/SecurityException;

    goto :goto_49

    nop

    :goto_8
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    goto :goto_31

    nop

    :goto_9
    goto :goto_4d

    :goto_a
    goto :goto_32

    nop

    :goto_b
    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_17

    nop

    :goto_c
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    goto :goto_34

    nop

    :goto_d
    const-string v8, " is not a device owner or profile owner, so may not use policy: "

    goto :goto_4

    nop

    :goto_e
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    goto :goto_4a

    nop

    :goto_f
    return-object v2

    :goto_10
    goto :goto_9

    nop

    :goto_11
    new-instance v6, Ljava/lang/SecurityException;

    goto :goto_33

    nop

    :goto_12
    invoke-virtual {v8, p2}, Landroid/app/admin/DeviceAdminInfo;->getTagForPolicy(I)Ljava/lang/String;

    move-result-object v8

    goto :goto_27

    nop

    :goto_13
    iget-object v8, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_3c

    nop

    :goto_14
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    goto :goto_62

    nop

    :goto_15
    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->hasCallingPermission(Ljava/lang/String;)Z

    move-result v4

    goto :goto_16

    nop

    :goto_16
    if-nez v4, :cond_0

    goto :goto_10

    :cond_0
    goto :goto_43

    nop

    :goto_17
    const-string v4, "No active admin owned by uid "

    goto :goto_54

    nop

    :goto_18
    const-string v7, "Admin "

    goto :goto_57

    nop

    :goto_19
    invoke-virtual {v8}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v8

    goto :goto_1a

    nop

    :goto_1a
    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    goto :goto_d

    nop

    :goto_1b
    invoke-virtual {v3, p1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v3

    goto :goto_21

    nop

    :goto_1c
    if-eqz v5, :cond_1

    goto :goto_45

    :cond_1
    goto :goto_11

    nop

    :goto_1d
    iget-object v8, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_12

    nop

    :goto_1e
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_3

    nop

    :goto_1f
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v5

    goto :goto_3e

    nop

    :goto_20
    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v3

    goto :goto_23

    nop

    :goto_21
    check-cast v3, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_46

    nop

    :goto_22
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v6

    goto :goto_5

    nop

    :goto_23
    check-cast v3, Ljava/lang/String;

    goto :goto_15

    nop

    :goto_24
    const-string v8, " did not specify uses-policy for: "

    goto :goto_2d

    nop

    :goto_25
    if-nez v4, :cond_2

    goto :goto_5a

    :cond_2
    goto :goto_2a

    nop

    :goto_26
    invoke-virtual {p0, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v2

    goto :goto_3a

    nop

    :goto_27
    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    goto :goto_42

    nop

    :goto_28
    invoke-virtual {v8}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v8

    goto :goto_4b

    nop

    :goto_29
    new-instance v6, Ljava/lang/SecurityException;

    goto :goto_51

    nop

    :goto_2a
    const-string v4, ""

    goto :goto_59

    nop

    :goto_2b
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUid()I

    move-result v1

    goto :goto_2

    nop

    :goto_2c
    iget-object v8, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_19

    nop

    :goto_2d
    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    goto :goto_13

    nop

    :goto_2e
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v7

    goto :goto_3b

    nop

    :goto_2f
    invoke-direct {v2, v3}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    goto :goto_5c

    nop

    :goto_30
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity()Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    goto :goto_2b

    nop

    :goto_31
    const-string v4, " for policy #"

    goto :goto_14

    nop

    :goto_32
    if-nez p1, :cond_3

    goto :goto_48

    :cond_3
    goto :goto_52

    nop

    :goto_33
    new-instance v8, Ljava/lang/StringBuilder;

    goto :goto_35

    nop

    :goto_34
    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    goto :goto_2f

    nop

    :goto_35
    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_55

    nop

    :goto_36
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    goto :goto_53

    nop

    :goto_37
    sget-object v6, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->DA_DISALLOWED_POLICIES:Ljava/util/Set;

    goto :goto_2e

    nop

    :goto_38
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_30

    nop

    :goto_39
    if-nez v1, :cond_4

    goto :goto_50

    :cond_4
    goto :goto_4f

    nop

    :goto_3a
    iget-object v3, v2, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    goto :goto_1b

    nop

    :goto_3b
    invoke-interface {v6, v7}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v6

    goto :goto_18

    nop

    :goto_3c
    invoke-virtual {v8, p2}, Landroid/app/admin/DeviceAdminInfo;->getTagForPolicy(I)Ljava/lang/String;

    move-result-object v8

    goto :goto_40

    nop

    :goto_3d
    invoke-interface {p3}, Ljava/util/Set;->isEmpty()Z

    move-result v4

    goto :goto_25

    nop

    :goto_3e
    invoke-virtual {p0, v4, v5}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isDeviceOwner(Landroid/content/ComponentName;I)Z

    move-result v4

    goto :goto_5b

    nop

    :goto_3f
    if-eqz v4, :cond_5

    goto :goto_45

    :cond_5
    goto :goto_1c

    nop

    :goto_40
    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    goto :goto_58

    nop

    :goto_41
    invoke-virtual {v4}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v4

    goto :goto_1f

    nop

    :goto_42
    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    goto :goto_56

    nop

    :goto_43
    const/4 v2, 0x0

    goto :goto_f

    nop

    :goto_44
    throw v6

    :goto_45
    goto :goto_29

    nop

    :goto_46
    iget-object v4, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_41

    nop

    :goto_47
    throw v6

    :goto_48
    goto :goto_7

    nop

    :goto_49
    new-instance v3, Ljava/lang/StringBuilder;

    goto :goto_b

    nop

    :goto_4a
    if-nez v3, :cond_6

    goto :goto_a

    :cond_6
    goto :goto_20

    nop

    :goto_4b
    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    goto :goto_24

    nop

    :goto_4c
    invoke-interface {p3}, Ljava/util/Set;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :goto_4d
    goto :goto_e

    nop

    :goto_4e
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUid()I

    move-result v4

    goto :goto_8

    nop

    :goto_4f
    return-object v1

    :goto_50
    goto :goto_4c

    nop

    :goto_51
    new-instance v8, Ljava/lang/StringBuilder;

    goto :goto_5f

    nop

    :goto_52
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v2

    goto :goto_26

    nop

    :goto_53
    invoke-virtual {v4, p3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v4

    goto :goto_5d

    nop

    :goto_54
    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    goto :goto_4e

    nop

    :goto_55
    invoke-virtual {v8, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    goto :goto_2c

    nop

    :goto_56
    invoke-direct {v6, v7}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    goto :goto_44

    nop

    :goto_57
    if-nez v6, :cond_7

    goto :goto_45

    :cond_7
    goto :goto_3f

    nop

    :goto_58
    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    goto :goto_0

    nop

    :goto_59
    goto :goto_5e

    :goto_5a
    goto :goto_6

    nop

    :goto_5b
    iget-object v5, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_1

    nop

    :goto_5c
    throw v2

    :goto_5d
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    :goto_5e
    goto :goto_c

    nop

    :goto_5f
    invoke-direct {v8}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_60

    nop

    :goto_60
    invoke-virtual {v8, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    goto :goto_61

    nop

    :goto_61
    iget-object v8, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_28

    nop

    :goto_62
    invoke-virtual {v3, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    goto :goto_3d

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity()Lcom/android/server/devicepolicy/CallerIdentity;', 'move-result-object v0', 'invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUid()I', 'move-result v1', 'invoke-direct {p0, p1, p2, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminWithPolicyForUidLocked(Landroid/content/ComponentName;II)Lcom/android/server/devicepolicy/ActiveAdmin;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getActiveAdminOrCheckPermissionsForCallerLocked_Landroid_con",
        "method":      ".method getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;IZLjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getActiveAdminOrCheckPermissionsForCallerLocked',
        "type":        "method_replace",
        "search": """\
.method getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;IZLjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/ComponentName;",
            "IZ",
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;)",
            "Lcom/android/server/devicepolicy/ActiveAdmin;"
        }
    .end annotation

    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    if-eqz p3, :cond_0

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity()Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v0

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isManagedProfile(I)Z

    move-result v0

    invoke-static {v0}, Lcom/android/internal/util/Preconditions;->checkCallingUser(Z)V

    :cond_0
    invoke-virtual {p0, p1, p2, p4}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;ILjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    if-eqz p3, :cond_1

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/ActiveAdmin;->getParentActiveAdmin()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v1

    goto :goto_0

    :cond_1
    move-object v1, v0

    :goto_0
    return-object v1
.end method
""",
        "replacement": """\
.method getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;IZLjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/content/ComponentName;",
            "IZ",
            "Ljava/util/Set<",
            "Ljava/lang/String;",
            ">;)",
            "Lcom/android/server/devicepolicy/ActiveAdmin;"
        }
    .end annotation

    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/lang/SecurityException;
        }
    .end annotation

    goto :goto_5

    nop

    :goto_0
    if-nez p3, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_1

    nop

    :goto_1
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/ActiveAdmin;->getParentActiveAdmin()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v1

    goto :goto_a

    nop

    :goto_2
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity()Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    goto :goto_e

    nop

    :goto_3
    move-object v1, v0

    :goto_4
    goto :goto_6

    nop

    :goto_5
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_7

    nop

    :goto_6
    return-object v1

    :goto_7
    if-nez p3, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_2

    nop

    :goto_8
    invoke-static {v0}, Lcom/android/internal/util/Preconditions;->checkCallingUser(Z)V

    :goto_9
    goto :goto_c

    nop

    :goto_a
    goto :goto_4

    :goto_b
    goto :goto_3

    nop

    :goto_c
    invoke-virtual {p0, p1, p2, p4}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminOrCheckPermissionsForCallerLocked(Landroid/content/ComponentName;ILjava/util/Set;)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_0

    nop

    :goto_d
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isManagedProfile(I)Z

    move-result v0

    goto :goto_8

    nop

    :goto_e
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v0

    goto :goto_d

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'if-eqz p3, :cond_0', 'invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity()Lcom/android/server/devicepolicy/CallerIdentity;', 'move-result-object v0', 'invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I', 'move-result v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getActiveAdminUncheckedLocked_Landroid_content_ComponentName",
        "method":      ".method getActiveAdminUncheckedLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getActiveAdminUncheckedLocked',
        "type":        "method_replace",
        "search": """\
.method getActiveAdminUncheckedLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 6

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    invoke-virtual {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v0

    iget-object v0, v0, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    invoke-virtual {v0, p1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/server/devicepolicy/ActiveAdmin;

    if-eqz v0, :cond_0

    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v1

    iget-object v2, v0, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v2}, Landroid/app/admin/DeviceAdminInfo;->getActivityInfo()Landroid/content/pm/ActivityInfo;

    move-result-object v2

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->packageName:Ljava/lang/String;

    invoke-virtual {v1, v2}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-virtual {p1}, Landroid/content/ComponentName;->getClassName()Ljava/lang/String;

    move-result-object v1

    iget-object v2, v0, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v2}, Landroid/app/admin/DeviceAdminInfo;->getActivityInfo()Landroid/content/pm/ActivityInfo;

    move-result-object v2

    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->name:Ljava/lang/String;

    invoke-virtual {v1, v2}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_0

    return-object v0

    :cond_0
    const/4 v1, 0x0

    return-object v1
.end method
""",
        "replacement": """\
.method getActiveAdminUncheckedLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 6

    goto :goto_e

    nop

    :goto_0
    invoke-virtual {v2}, Landroid/app/admin/DeviceAdminInfo;->getActivityInfo()Landroid/content/pm/ActivityInfo;

    move-result-object v2

    goto :goto_11

    nop

    :goto_1
    invoke-virtual {v0, p1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_7

    nop

    :goto_2
    return-object v0

    :goto_3
    goto :goto_9

    nop

    :goto_4
    if-nez v1, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_2

    nop

    :goto_5
    return-object v1

    :goto_6
    iget-object v0, v0, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    goto :goto_1

    nop

    :goto_7
    check-cast v0, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_8

    nop

    :goto_8
    if-nez v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_10

    nop

    :goto_9
    const/4 v1, 0x0

    goto :goto_5

    nop

    :goto_a
    if-nez v1, :cond_2

    goto :goto_3

    :cond_2
    goto :goto_13

    nop

    :goto_b
    invoke-virtual {v2}, Landroid/app/admin/DeviceAdminInfo;->getActivityInfo()Landroid/content/pm/ActivityInfo;

    move-result-object v2

    goto :goto_15

    nop

    :goto_c
    invoke-virtual {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v0

    goto :goto_6

    nop

    :goto_d
    iget-object v2, v0, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_b

    nop

    :goto_e
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_c

    nop

    :goto_f
    iget-object v2, v0, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_0

    nop

    :goto_10
    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v1

    goto :goto_f

    nop

    :goto_11
    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->packageName:Ljava/lang/String;

    goto :goto_14

    nop

    :goto_12
    invoke-virtual {v1, v2}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    goto :goto_4

    nop

    :goto_13
    invoke-virtual {p1}, Landroid/content/ComponentName;->getClassName()Ljava/lang/String;

    move-result-object v1

    goto :goto_d

    nop

    :goto_14
    invoke-virtual {v1, v2}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    goto :goto_a

    nop

    :goto_15
    iget-object v2, v2, Landroid/content/pm/ActivityInfo;->name:Ljava/lang/String;

    goto :goto_12

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'invoke-virtual {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;', 'move-result-object v0', 'iget-object v0, v0, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;', 'invoke-virtual {v0, p1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;', 'move-result-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getActiveAdminUncheckedLocked_Landroid_content_ComponentName",
        "method":      ".method getActiveAdminUncheckedLocked(Landroid/content/ComponentName;IZ)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getActiveAdminUncheckedLocked',
        "type":        "method_replace",
        "search": """\
.method getActiveAdminUncheckedLocked(Landroid/content/ComponentName;IZ)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 7

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    if-eqz p3, :cond_0

    invoke-direct {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isManagedProfile(I)Z

    move-result v0

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v1

    const-string v2, "You can not call APIs on the parent profile outside a managed profile, userId = %d"

    invoke-static {v0, v2, v1}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(ZLjava/lang/String;[Ljava/lang/Object;)V

    :cond_0
    invoke-virtual {p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminUncheckedLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    if-eqz v0, :cond_1

    if-eqz p3, :cond_1

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/ActiveAdmin;->getParentActiveAdmin()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    :cond_1
    return-object v0
.end method
""",
        "replacement": """\
.method getActiveAdminUncheckedLocked(Landroid/content/ComponentName;IZ)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 7

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/ActiveAdmin;->getParentActiveAdmin()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    :goto_1
    goto :goto_7

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_d

    nop

    :goto_3
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_9

    nop

    :goto_4
    invoke-virtual {p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminUncheckedLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_2

    nop

    :goto_5
    const-string v2, "You can not call APIs on the parent profile outside a managed profile, userId = %d"

    goto :goto_a

    nop

    :goto_6
    invoke-direct {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isManagedProfile(I)Z

    move-result v0

    goto :goto_8

    nop

    :goto_7
    return-object v0

    :goto_8
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v1

    goto :goto_c

    nop

    :goto_9
    if-nez p3, :cond_1

    goto :goto_b

    :cond_1
    goto :goto_6

    nop

    :goto_a
    invoke-static {v0, v2, v1}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(ZLjava/lang/String;[Ljava/lang/Object;)V

    :goto_b
    goto :goto_4

    nop

    :goto_c
    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_5

    nop

    :goto_d
    if-nez p3, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'if-eqz p3, :cond_0', 'invoke-direct {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isManagedProfile(I)Z', 'move-result v0', 'invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;', 'move-result-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getCallerIdentity_Landroid_content_ComponentName__Lcom_andro",
        "method":      ".method getCallerIdentity(Landroid/content/ComponentName;)Lcom/android/server/devicepolicy/CallerIdentity;",
        "method_name": 'getCallerIdentity',
        "type":        "method_replace",
        "search": """\
.method getCallerIdentity(Landroid/content/ComponentName;)Lcom/android/server/devicepolicy/CallerIdentity;
    .registers 3

    const/4 v0, 0x0

    invoke-virtual {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity(Landroid/content/ComponentName;Ljava/lang/String;)Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    return-object v0
.end method
""",
        "replacement": """\
.method getCallerIdentity(Landroid/content/ComponentName;)Lcom/android/server/devicepolicy/CallerIdentity;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-object v0

    :goto_1
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity(Landroid/content/ComponentName;Ljava/lang/String;)Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity(Landroid/content/ComponentName;Ljava/lang/String;)Lcom/android/server/devicepolicy/CallerIdentity;', 'move-result-object v0', 'return-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getCallerIdentity_Landroid_content_ComponentName_Ljava_lang_",
        "method":      ".method getCallerIdentity(Landroid/content/ComponentName;Ljava/lang/String;)Lcom/android/server/devicepolicy/CallerIdentity;",
        "method_name": 'getCallerIdentity',
        "type":        "method_replace",
        "search": """\
.method getCallerIdentity(Landroid/content/ComponentName;Ljava/lang/String;)Lcom/android/server/devicepolicy/CallerIdentity;
    .registers 10

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderGetCallingUid()I

    move-result v0

    if-eqz p2, :cond_1

    invoke-static {}, Lmiui/enterprise/ApplicationHelperStub;->getInstance()Lmiui/enterprise/IApplicationHelper;

    move-result-object v1

    invoke-interface {v1, p2}, Lmiui/enterprise/IApplicationHelper;->isGrantProfileOwner(Ljava/lang/String;)Z

    move-result v1

    if-nez v1, :cond_1

    invoke-direct {p0, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isCallingFromPackage(Ljava/lang/String;I)Z

    move-result v2

    if-eqz v2, :cond_0

    goto :goto_0

    :cond_0
    new-instance v2, Ljava/lang/SecurityException;

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    filled-new-array {v3, p2}, [Ljava/lang/Object;

    move-result-object v3

    const-string v4, "Caller with uid %d is not %s"

    invoke-static {v4, v3}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    throw v2

    :cond_1
    :goto_0
    if-eqz p1, :cond_5

    invoke-static {v0}, Landroid/os/UserHandle;->getUserId(I)I

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    iget-object v2, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    invoke-virtual {v2, p1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/server/devicepolicy/ActiveAdmin;

    invoke-static {}, Lmiui/enterprise/ApplicationHelperStub;->getInstance()Lmiui/enterprise/IApplicationHelper;

    move-result-object v3

    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v4

    invoke-interface {v3, v4}, Lmiui/enterprise/IApplicationHelper;->isGrantProfileOwner(Ljava/lang/String;)Z

    move-result v3

    if-nez v3, :cond_3

    if-eqz v2, :cond_2

    invoke-virtual {v2}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUid()I

    move-result v4

    if-ne v4, v0, :cond_2

    goto :goto_1

    :cond_2
    new-instance v4, Ljava/lang/SecurityException;

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v5

    filled-new-array {p1, v5}, [Ljava/lang/Object;

    move-result-object v5

    const-string v6, "Admin %s does not exist or is not owned by uid %d"

    invoke-static {v6, v5}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    invoke-direct {v4, v5}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    throw v4

    :cond_3
    :goto_1
    if-eqz p2, :cond_4

    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {p2, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    invoke-static {v4}, Lcom/android/internal/util/Preconditions;->checkArgument(Z)V

    goto :goto_2

    :cond_4
    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object p2

    :cond_5
    :goto_2
    new-instance v1, Lcom/android/server/devicepolicy/CallerIdentity;

    invoke-direct {v1, v0, p2, p1}, Lcom/android/server/devicepolicy/CallerIdentity;-><init>(ILjava/lang/String;Landroid/content/ComponentName;)V

    return-object v1
.end method
""",
        "replacement": """\
.method getCallerIdentity(Landroid/content/ComponentName;Ljava/lang/String;)Lcom/android/server/devicepolicy/CallerIdentity;
    .registers 10

    goto :goto_f

    nop

    :goto_0
    iget-object v2, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    goto :goto_29

    nop

    :goto_1
    return-object v1

    :goto_2
    invoke-virtual {v2}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUid()I

    move-result v4

    goto :goto_2a

    nop

    :goto_3
    const-string v4, "Caller with uid %d is not %s"

    goto :goto_9

    nop

    :goto_4
    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v4

    goto :goto_15

    nop

    :goto_5
    invoke-static {v0}, Landroid/os/UserHandle;->getUserId(I)I

    move-result v1

    goto :goto_20

    nop

    :goto_6
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderGetCallingUid()I

    move-result v0

    goto :goto_1b

    nop

    :goto_7
    invoke-interface {v1, p2}, Lmiui/enterprise/IApplicationHelper;->isGrantProfileOwner(Ljava/lang/String;)Z

    move-result v1

    goto :goto_8

    nop

    :goto_8
    if-eqz v1, :cond_0

    goto :goto_1f

    :cond_0
    goto :goto_28

    nop

    :goto_9
    invoke-static {v4, v3}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v3

    goto :goto_26

    nop

    :goto_a
    throw v4

    :goto_b
    goto :goto_1a

    nop

    :goto_c
    invoke-direct {v4, v5}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    goto :goto_a

    nop

    :goto_d
    invoke-static {}, Lmiui/enterprise/ApplicationHelperStub;->getInstance()Lmiui/enterprise/IApplicationHelper;

    move-result-object v3

    goto :goto_4

    nop

    :goto_e
    filled-new-array {v3, p2}, [Ljava/lang/Object;

    move-result-object v3

    goto :goto_3

    nop

    :goto_f
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_6

    nop

    :goto_10
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v5

    goto :goto_1c

    nop

    :goto_11
    if-nez p1, :cond_1

    goto :goto_23

    :cond_1
    goto :goto_5

    nop

    :goto_12
    goto :goto_23

    :goto_13
    goto :goto_22

    nop

    :goto_14
    invoke-virtual {p2, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    goto :goto_1d

    nop

    :goto_15
    invoke-interface {v3, v4}, Lmiui/enterprise/IApplicationHelper;->isGrantProfileOwner(Ljava/lang/String;)Z

    move-result v3

    goto :goto_2f

    nop

    :goto_16
    goto :goto_b

    :goto_17
    goto :goto_2e

    nop

    :goto_18
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v3

    goto :goto_e

    nop

    :goto_19
    if-nez v2, :cond_2

    goto :goto_17

    :cond_2
    goto :goto_2

    nop

    :goto_1a
    if-nez p2, :cond_3

    goto :goto_13

    :cond_3
    goto :goto_21

    nop

    :goto_1b
    if-nez p2, :cond_4

    goto :goto_1f

    :cond_4
    goto :goto_30

    nop

    :goto_1c
    filled-new-array {p1, v5}, [Ljava/lang/Object;

    move-result-object v5

    goto :goto_31

    nop

    :goto_1d
    invoke-static {v4}, Lcom/android/internal/util/Preconditions;->checkArgument(Z)V

    goto :goto_12

    nop

    :goto_1e
    throw v2

    :goto_1f
    goto :goto_11

    nop

    :goto_20
    invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    goto :goto_0

    nop

    :goto_21
    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v4

    goto :goto_14

    nop

    :goto_22
    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object p2

    :goto_23
    goto :goto_33

    nop

    :goto_24
    new-instance v2, Ljava/lang/SecurityException;

    goto :goto_18

    nop

    :goto_25
    invoke-static {v6, v5}, Ljava/lang/String;->format(Ljava/lang/String;[Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    goto :goto_c

    nop

    :goto_26
    invoke-direct {v2, v3}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    goto :goto_1e

    nop

    :goto_27
    check-cast v2, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_d

    nop

    :goto_28
    invoke-direct {p0, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isCallingFromPackage(Ljava/lang/String;I)Z

    move-result v2

    goto :goto_32

    nop

    :goto_29
    invoke-virtual {v2, p1}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v2

    goto :goto_27

    nop

    :goto_2a
    if-eq v4, v0, :cond_5

    goto :goto_17

    :cond_5
    goto :goto_16

    nop

    :goto_2b
    invoke-direct {v1, v0, p2, p1}, Lcom/android/server/devicepolicy/CallerIdentity;-><init>(ILjava/lang/String;Landroid/content/ComponentName;)V

    goto :goto_1

    nop

    :goto_2c
    goto :goto_1f

    :goto_2d
    goto :goto_24

    nop

    :goto_2e
    new-instance v4, Ljava/lang/SecurityException;

    goto :goto_10

    nop

    :goto_2f
    if-eqz v3, :cond_6

    goto :goto_b

    :cond_6
    goto :goto_19

    nop

    :goto_30
    invoke-static {}, Lmiui/enterprise/ApplicationHelperStub;->getInstance()Lmiui/enterprise/IApplicationHelper;

    move-result-object v1

    goto :goto_7

    nop

    :goto_31
    const-string v6, "Admin %s does not exist or is not owned by uid %d"

    goto :goto_25

    nop

    :goto_32
    if-nez v2, :cond_7

    goto :goto_2d

    :cond_7
    goto :goto_2c

    nop

    :goto_33
    new-instance v1, Lcom/android/server/devicepolicy/CallerIdentity;

    goto :goto_2b

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;', 'invoke-virtual {v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderGetCallingUid()I', 'move-result v0', 'if-eqz p2, :cond_1', 'invoke-static {}, Lmiui/enterprise/ApplicationHelperStub;->getInstance()Lmiui/enterprise/IApplicationHelper;', 'move-result-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getDefaultDeviceOwnerLocked_I_Lcom_android_server_devicepoli",
        "method":      ".method getDefaultDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getDefaultDeviceOwnerLocked',
        "type":        "method_replace",
        "search": """\
.method getDefaultDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 5

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerType(Ljava/lang/String;)I

    move-result v1

    if-nez v1, :cond_0

    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    iget-object v1, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    invoke-virtual {v1, v0}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/devicepolicy/ActiveAdmin;

    return-object v1

    :cond_0
    const/4 v1, 0x0

    return-object v1
.end method
""",
        "replacement": """\
.method getDefaultDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 5

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v1, v2}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerType(Ljava/lang/String;)I

    move-result v1

    goto :goto_d

    nop

    :goto_1
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_2

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    goto :goto_c

    nop

    :goto_3
    return-object v1

    :goto_4
    goto :goto_e

    nop

    :goto_5
    invoke-virtual {v1, v0}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_9

    nop

    :goto_6
    invoke-virtual {v0}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v2

    goto :goto_0

    nop

    :goto_7
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    goto :goto_6

    nop

    :goto_8
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    goto :goto_b

    nop

    :goto_9
    check-cast v1, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_3

    nop

    :goto_a
    return-object v1

    :goto_b
    iget-object v1, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    goto :goto_5

    nop

    :goto_c
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v0

    goto :goto_7

    nop

    :goto_d
    if-eqz v1, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_8

    nop

    :goto_e
    const/4 v1, 0x0

    goto :goto_a

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;', 'move-result-object v0', 'iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v0}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getDeviceOwnerAdminLocked__Lcom_android_server_devicepolicy_",
        "method":      ".method getDeviceOwnerAdminLocked()Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getDeviceOwnerAdminLocked',
        "type":        "method_replace",
        "search": """\
.method getDeviceOwnerAdminLocked()Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 8

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v0

    const/4 v1, 0x0

    if-nez v0, :cond_0

    return-object v1

    :cond_0
    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v2}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I

    move-result v2

    invoke-virtual {p0, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v2

    iget-object v3, v2, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v3

    const/4 v4, 0x0

    :goto_0
    if-ge v4, v3, :cond_2

    iget-object v5, v2, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    invoke-virtual {v5, v4}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Lcom/android/server/devicepolicy/ActiveAdmin;

    iget-object v6, v5, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v6}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v6

    invoke-virtual {v0, v6}, Landroid/content/ComponentName;->equals(Ljava/lang/Object;)Z

    move-result v6

    if-eqz v6, :cond_1

    return-object v5

    :cond_1
    add-int/lit8 v4, v4, 0x1

    goto :goto_0

    :cond_2
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "Active admin for device owner not found. component="

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    const-string v5, "DevicePolicyManager"

    invoke-static {v5, v4}, Lcom/android/server/utils/Slogf;->wtf(Ljava/lang/String;Ljava/lang/String;)I

    return-object v1
.end method
""",
        "replacement": """\
.method getDeviceOwnerAdminLocked()Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 8

    goto :goto_9

    nop

    :goto_0
    check-cast v5, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_4

    nop

    :goto_1
    add-int/lit8 v4, v4, 0x1

    goto :goto_5

    nop

    :goto_2
    iget-object v3, v2, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    goto :goto_19

    nop

    :goto_3
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    goto :goto_d

    nop

    :goto_4
    iget-object v6, v5, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_17

    nop

    :goto_5
    goto :goto_1d

    :goto_6
    goto :goto_11

    nop

    :goto_7
    return-object v5

    :goto_8
    goto :goto_1

    nop

    :goto_9
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_1b

    nop

    :goto_a
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    goto :goto_23

    nop

    :goto_b
    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    goto :goto_12

    nop

    :goto_c
    if-nez v6, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_7

    nop

    :goto_d
    invoke-virtual {v4, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v4

    goto :goto_a

    nop

    :goto_e
    if-eqz v0, :cond_1

    goto :goto_20

    :cond_1
    goto :goto_1f

    nop

    :goto_f
    if-lt v4, v3, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_1a

    nop

    :goto_10
    const/4 v1, 0x0

    goto :goto_e

    nop

    :goto_11
    new-instance v4, Ljava/lang/StringBuilder;

    goto :goto_13

    nop

    :goto_12
    invoke-virtual {v2}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I

    move-result v2

    goto :goto_14

    nop

    :goto_13
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_16

    nop

    :goto_14
    invoke-virtual {p0, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v2

    goto :goto_2

    nop

    :goto_15
    invoke-virtual {v0, v6}, Landroid/content/ComponentName;->equals(Ljava/lang/Object;)Z

    move-result v6

    goto :goto_c

    nop

    :goto_16
    const-string v5, "Active admin for device owner not found. component="

    goto :goto_3

    nop

    :goto_17
    invoke-virtual {v6}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v6

    goto :goto_15

    nop

    :goto_18
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v0

    goto :goto_10

    nop

    :goto_19
    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v3

    goto :goto_1c

    nop

    :goto_1a
    iget-object v5, v2, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    goto :goto_1e

    nop

    :goto_1b
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    goto :goto_18

    nop

    :goto_1c
    const/4 v4, 0x0

    :goto_1d
    goto :goto_f

    nop

    :goto_1e
    invoke-virtual {v5, v4}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v5

    goto :goto_0

    nop

    :goto_1f
    return-object v1

    :goto_20
    goto :goto_b

    nop

    :goto_21
    return-object v1

    :goto_22
    invoke-static {v5, v4}, Lcom/android/server/utils/Slogf;->wtf(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_21

    nop

    :goto_23
    const-string v5, "DevicePolicyManager"

    goto :goto_22

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;', 'move-result-object v0', 'if-nez v0, :cond_0', 'return-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getDeviceOwnerLocked_I_Lcom_android_server_devicepolicy_Acti",
        "method":      ".method getDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getDeviceOwnerLocked',
        "type":        "method_replace",
        "search": """\
.method getDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v0

    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    iget-object v1, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    invoke-virtual {v1, v0}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/devicepolicy/ActiveAdmin;

    return-object v1
.end method
""",
        "replacement": """\
.method getDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v0

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    goto :goto_6

    nop

    :goto_2
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_5

    nop

    :goto_3
    return-object v1

    :goto_4
    check-cast v1, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_3

    nop

    :goto_5
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    goto :goto_0

    nop

    :goto_6
    iget-object v1, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    goto :goto_7

    nop

    :goto_7
    invoke-virtual {v1, v0}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_4

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;', 'move-result-object v0', 'invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;', 'move-result-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getDeviceOwnerOrProfileOwnerOfOrganizationOwnedDeviceLocked_",
        "method":      ".method getDeviceOwnerOrProfileOwnerOfOrganizationOwnedDeviceLocked()Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getDeviceOwnerOrProfileOwnerOfOrganizationOwnedDeviceLocked',
        "type":        "method_replace",
        "search": """\
.method getDeviceOwnerOrProfileOwnerOfOrganizationOwnedDeviceLocked()Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 2

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerAdminLocked()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    if-nez v0, :cond_0

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerOfOrganizationOwnedDeviceLocked()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    :cond_0
    return-object v0
.end method
""",
        "replacement": """\
.method getDeviceOwnerOrProfileOwnerOfOrganizationOwnedDeviceLocked()Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 2

    goto :goto_4

    nop

    :goto_0
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerAdminLocked()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_1

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_2

    nop

    :goto_2
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerOfOrganizationOwnedDeviceLocked()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    :goto_3
    goto :goto_5

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_0

    nop

    :goto_5
    return-object v0
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerAdminLocked()Lcom/android/server/devicepolicy/ActiveAdmin;', 'move-result-object v0', 'if-nez v0, :cond_0', 'invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerOfOrganizationOwnedDeviceLocked()Lcom/android/server/devicepolicy/ActiveAdmin;', 'move-result-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getDeviceOwnerOrProfileOwnerOfOrganizationOwnedDeviceLocked_",
        "method":      ".method getDeviceOwnerOrProfileOwnerOfOrganizationOwnedDeviceLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getDeviceOwnerOrProfileOwnerOfOrganizationOwnedDeviceLocked',
        "type":        "method_replace",
        "search": """\
.method getDeviceOwnerOrProfileOwnerOfOrganizationOwnedDeviceLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 3
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerAdminLocked()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    if-nez v0, :cond_0

    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerOfOrganizationOwnedDeviceLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    :cond_0
    return-object v0
.end method
""",
        "replacement": """\
.method getDeviceOwnerOrProfileOwnerOfOrganizationOwnedDeviceLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 3
    .annotation runtime Ljava/lang/Deprecated;
    .end annotation

    goto :goto_5

    nop

    :goto_0
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerOfOrganizationOwnedDeviceLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    :goto_1
    goto :goto_4

    nop

    :goto_2
    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_0

    nop

    :goto_3
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerAdminLocked()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_2

    nop

    :goto_4
    return-object v0

    :goto_5
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerAdminLocked()Lcom/android/server/devicepolicy/ActiveAdmin;', 'move-result-object v0', 'if-nez v0, :cond_0', 'invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerOfOrganizationOwnedDeviceLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;', 'move-result-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getDeviceOwnerRemoteBugreportUriAndHash__Landroid_util_Pair_",
        "method":      ".method getDeviceOwnerRemoteBugreportUriAndHash()Landroid/util/Pair;",
        "method_name": 'getDeviceOwnerRemoteBugreportUriAndHash',
        "type":        "method_replace",
        "search": """\
.method getDeviceOwnerRemoteBugreportUriAndHash()Landroid/util/Pair;
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "()",
            "Landroid/util/Pair<",
            "Ljava/lang/String;",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerRemoteBugreportUri()Ljava/lang/String;

    move-result-object v1

    if-nez v1, :cond_0

    const/4 v2, 0x0

    goto :goto_0

    :cond_0
    new-instance v2, Landroid/util/Pair;

    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v3}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerRemoteBugreportHash()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v1, v3}, Landroid/util/Pair;-><init>(Ljava/lang/Object;Ljava/lang/Object;)V

    :goto_0
    monitor-exit v0

    return-object v2

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method getDeviceOwnerRemoteBugreportUriAndHash()Landroid/util/Pair;
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "()",
            "Landroid/util/Pair<",
            "Ljava/lang/String;",
            "Ljava/lang/String;",
            ">;"
        }
    .end annotation

    goto :goto_3

    nop

    :goto_0
    throw v1

    :goto_1
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerRemoteBugreportUri()Ljava/lang/String;

    move-result-object v1

    if-nez v1, :cond_0

    const/4 v2, 0x0

    goto :goto_2

    :cond_0
    new-instance v2, Landroid/util/Pair;

    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v3}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerRemoteBugreportHash()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v1, v3}, Landroid/util/Pair;-><init>(Ljava/lang/Object;Ljava/lang/Object;)V

    :goto_2
    monitor-exit v0

    return-object v2

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop

    :goto_3
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;', 'move-result-object v0', 'iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v1}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerRemoteBugreportUri()Ljava/lang/String;', 'move-result-object v1', 'if-nez v1, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getDevicePolicySafetyChecker__Landroid_app_admin_DevicePolic",
        "method":      ".method getDevicePolicySafetyChecker()Landroid/app/admin/DevicePolicySafetyChecker;",
        "method_name": 'getDevicePolicySafetyChecker',
        "type":        "method_replace",
        "search": """\
.method getDevicePolicySafetyChecker()Landroid/app/admin/DevicePolicySafetyChecker;
    .registers 2

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;

    return-object v0
.end method
""",
        "replacement": """\
.method getDevicePolicySafetyChecker()Landroid/app/admin/DevicePolicySafetyChecker;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;

    goto :goto_1

    nop

    :goto_1
    return-object v0
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;', 'return-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getLockObject__Ljava_lang_Object_",
        "method":      ".method final getLockObject()Ljava/lang/Object;",
        "method_name": 'getLockObject',
        "type":        "method_replace",
        "search": """\
.method final getLockObject()Ljava/lang/Object;
    .registers 5

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStatLogger:Lcom/android/internal/util/StatLogger;

    invoke-virtual {v0}, Lcom/android/internal/util/StatLogger;->getTime()J

    move-result-wide v0

    const/16 v2, 0x8

    invoke-static {v2}, Lcom/android/server/LockGuard;->guard(I)V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStatLogger:Lcom/android/internal/util/StatLogger;

    const/4 v3, 0x0

    invoke-virtual {v2, v3, v0, v1}, Lcom/android/internal/util/StatLogger;->logDurationStat(IJ)J

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mLockDoNoUseDirectly:Ljava/lang/Object;

    return-object v0
.end method
""",
        "replacement": """\
.method final getLockObject()Ljava/lang/Object;
    .registers 5

    goto :goto_6

    nop

    :goto_0
    invoke-static {v2}, Lcom/android/server/LockGuard;->guard(I)V

    goto :goto_8

    nop

    :goto_1
    invoke-virtual {v0}, Lcom/android/internal/util/StatLogger;->getTime()J

    move-result-wide v0

    goto :goto_2

    nop

    :goto_2
    const/16 v2, 0x8

    goto :goto_0

    nop

    :goto_3
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mLockDoNoUseDirectly:Ljava/lang/Object;

    goto :goto_4

    nop

    :goto_4
    return-object v0

    :goto_5
    invoke-virtual {v2, v3, v0, v1}, Lcom/android/internal/util/StatLogger;->logDurationStat(IJ)J

    goto :goto_3

    nop

    :goto_6
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStatLogger:Lcom/android/internal/util/StatLogger;

    goto :goto_1

    nop

    :goto_7
    const/4 v3, 0x0

    goto :goto_5

    nop

    :goto_8
    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStatLogger:Lcom/android/internal/util/StatLogger;

    goto :goto_7

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStatLogger:Lcom/android/internal/util/StatLogger;', 'invoke-virtual {v0}, Lcom/android/internal/util/StatLogger;->getTime()J', 'move-result-wide v0', 'invoke-static {v2}, Lcom/android/server/LockGuard;->guard(I)V', 'iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStatLogger:Lcom/android/internal/util/StatLogger;', 'invoke-virtual {v2, v3, v0, v1}, Lcom/android/internal/util/StatLogger;->logDurationStat(IJ)J'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getParentOfAdminIfRequired_Lcom_android_server_devicepolicy_",
        "method":      ".method getParentOfAdminIfRequired(Lcom/android/server/devicepolicy/ActiveAdmin;Z)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getParentOfAdminIfRequired',
        "type":        "method_replace",
        "search": """\
.method getParentOfAdminIfRequired(Lcom/android/server/devicepolicy/ActiveAdmin;Z)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4

    invoke-static {p1}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    if-eqz p2, :cond_0

    invoke-virtual {p1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getParentActiveAdmin()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_0

    :cond_0
    move-object v0, p1

    :goto_0
    return-object v0
.end method
""",
        "replacement": """\
.method getParentOfAdminIfRequired(Lcom/android/server/devicepolicy/ActiveAdmin;Z)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4

    goto :goto_3

    nop

    :goto_0
    goto :goto_6

    :goto_1
    goto :goto_5

    nop

    :goto_2
    invoke-virtual {p1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getParentActiveAdmin()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_0

    nop

    :goto_3
    invoke-static {p1}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_4

    nop

    :goto_4
    if-nez p2, :cond_0

    goto :goto_1

    :cond_0
    goto :goto_2

    nop

    :goto_5
    move-object v0, p1

    :goto_6
    goto :goto_7

    nop

    :goto_7
    return-object v0
.end method
""",
        "method_anchors": ['invoke-static {p1}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;', 'if-eqz p2, :cond_0', 'invoke-virtual {p1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getParentActiveAdmin()Lcom/android/server/devicepolicy/ActiveAdmin;', 'move-result-object v0', 'return-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getProfileOwnerAdminLocked_I_Lcom_android_server_devicepolic",
        "method":      ".method getProfileOwnerAdminLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getProfileOwnerAdminLocked',
        "type":        "method_replace",
        "search": """\
.method getProfileOwnerAdminLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 9

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/Owners;->getProfileOwnerComponent(I)Landroid/content/ComponentName;

    move-result-object v0

    const/4 v1, 0x0

    if-nez v0, :cond_0

    return-object v1

    :cond_0
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v2

    iget-object v3, v2, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v3

    const/4 v4, 0x0

    :goto_0
    if-ge v4, v3, :cond_2

    iget-object v5, v2, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    invoke-virtual {v5, v4}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Lcom/android/server/devicepolicy/ActiveAdmin;

    iget-object v6, v5, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v6}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v6

    invoke-virtual {v0, v6}, Landroid/content/ComponentName;->equals(Ljava/lang/Object;)Z

    move-result v6

    if-eqz v6, :cond_1

    return-object v5

    :cond_1
    add-int/lit8 v4, v4, 0x1

    goto :goto_0

    :cond_2
    return-object v1
.end method
""",
        "replacement": """\
.method getProfileOwnerAdminLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 9

    goto :goto_7

    nop

    :goto_0
    iget-object v5, v2, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    goto :goto_9

    nop

    :goto_1
    return-object v5

    :goto_2
    goto :goto_a

    nop

    :goto_3
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v2

    goto :goto_8

    nop

    :goto_4
    return-object v1

    :goto_5
    if-nez v6, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_1

    nop

    :goto_6
    invoke-virtual {v6}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v6

    goto :goto_12

    nop

    :goto_7
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    goto :goto_13

    nop

    :goto_8
    iget-object v3, v2, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    goto :goto_16

    nop

    :goto_9
    invoke-virtual {v5, v4}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v5

    goto :goto_14

    nop

    :goto_a
    add-int/lit8 v4, v4, 0x1

    goto :goto_17

    nop

    :goto_b
    const/4 v4, 0x0

    :goto_c
    goto :goto_15

    nop

    :goto_d
    const/4 v1, 0x0

    goto :goto_f

    nop

    :goto_e
    iget-object v6, v5, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_6

    nop

    :goto_f
    if-eqz v0, :cond_1

    goto :goto_11

    :cond_1
    goto :goto_10

    nop

    :goto_10
    return-object v1

    :goto_11
    goto :goto_3

    nop

    :goto_12
    invoke-virtual {v0, v6}, Landroid/content/ComponentName;->equals(Ljava/lang/Object;)Z

    move-result v6

    goto :goto_5

    nop

    :goto_13
    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/Owners;->getProfileOwnerComponent(I)Landroid/content/ComponentName;

    move-result-object v0

    goto :goto_d

    nop

    :goto_14
    check-cast v5, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_e

    nop

    :goto_15
    if-lt v4, v3, :cond_2

    goto :goto_18

    :cond_2
    goto :goto_0

    nop

    :goto_16
    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v3

    goto :goto_b

    nop

    :goto_17
    goto :goto_c

    :goto_18
    goto :goto_4

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/Owners;->getProfileOwnerComponent(I)Landroid/content/ComponentName;', 'move-result-object v0', 'if-nez v0, :cond_0', 'return-object v1', 'invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getProfileOwnerLocked_I_Lcom_android_server_devicepolicy_Act",
        "method":      ".method getProfileOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getProfileOwnerLocked',
        "type":        "method_replace",
        "search": """\
.method getProfileOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/Owners;->getProfileOwnerComponent(I)Landroid/content/ComponentName;

    move-result-object v0

    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    iget-object v1, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    invoke-virtual {v1, v0}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/devicepolicy/ActiveAdmin;

    return-object v1
.end method
""",
        "replacement": """\
.method getProfileOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4

    goto :goto_3

    nop

    :goto_0
    check-cast v1, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_2

    nop

    :goto_1
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    goto :goto_5

    nop

    :goto_2
    return-object v1

    :goto_3
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_1

    nop

    :goto_4
    iget-object v1, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminMap:Landroid/util/ArrayMap;

    goto :goto_7

    nop

    :goto_5
    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/Owners;->getProfileOwnerComponent(I)Landroid/content/ComponentName;

    move-result-object v0

    goto :goto_6

    nop

    :goto_6
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    goto :goto_4

    nop

    :goto_7
    invoke-virtual {v1, v0}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/Owners;->getProfileOwnerComponent(I)Landroid/content/ComponentName;', 'move-result-object v0', 'invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;', 'move-result-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getProfileOwnerOfOrganizationOwnedDeviceLocked__Lcom_android",
        "method":      ".method getProfileOwnerOfOrganizationOwnedDeviceLocked()Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getProfileOwnerOfOrganizationOwnedDeviceLocked',
        "type":        "method_replace",
        "search": """\
.method getProfileOwnerOfOrganizationOwnedDeviceLocked()Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 3

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda24;

    invoke-direct {v1, p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda24;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;)V

    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/server/devicepolicy/ActiveAdmin;

    return-object v0
.end method
""",
        "replacement": """\
.method getProfileOwnerOfOrganizationOwnedDeviceLocked()Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 3

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_3

    nop

    :goto_1
    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda24;

    goto :goto_5

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_1

    nop

    :goto_3
    check-cast v0, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_4

    nop

    :goto_4
    return-object v0

    :goto_5
    invoke-direct {v1, p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda24;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;)V

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;', 'new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda24;', 'invoke-direct {v1, p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda24;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;)V', 'invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;', 'move-result-object v0', 'check-cast v0, Lcom/android/server/devicepolicy/ActiveAdmin;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getProfileOwnerOfOrganizationOwnedDeviceLocked_I_Lcom_androi",
        "method":      ".method getProfileOwnerOfOrganizationOwnedDeviceLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getProfileOwnerOfOrganizationOwnedDeviceLocked',
        "type":        "method_replace",
        "search": """\
.method getProfileOwnerOfOrganizationOwnedDeviceLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda205;

    invoke-direct {v1, p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda205;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;I)V

    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/server/devicepolicy/ActiveAdmin;

    return-object v0
.end method
""",
        "replacement": """\
.method getProfileOwnerOfOrganizationOwnedDeviceLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4

    goto :goto_2

    nop

    :goto_0
    check-cast v0, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_4

    nop

    :goto_1
    invoke-direct {v1, p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda205;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;I)V

    goto :goto_5

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_3

    nop

    :goto_3
    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda205;

    goto :goto_1

    nop

    :goto_4
    return-object v0

    :goto_5
    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;', 'new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda205;', 'invoke-direct {v1, p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda205;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;I)V', 'invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;', 'move-result-object v0', 'check-cast v0, Lcom/android/server/devicepolicy/ActiveAdmin;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getProfileOwnerOrDeviceOwnerLocked_I_Lcom_android_server_dev",
        "method":      ".method getProfileOwnerOrDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;",
        "method_name": 'getProfileOwnerOrDeviceOwnerLocked',
        "type":        "method_replace",
        "search": """\
.method getProfileOwnerOrDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/Owners;->getProfileOwnerComponent(I)Landroid/content/ComponentName;

    move-result-object v0

    if-eqz v0, :cond_0

    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v1

    return-object v1

    :cond_0
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v1

    return-object v1
.end method
""",
        "replacement": """\
.method getProfileOwnerOrDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;
    .registers 4

    goto :goto_8

    nop

    :goto_0
    return-object v1

    :goto_1
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v1

    goto :goto_0

    nop

    :goto_2
    return-object v1

    :goto_3
    goto :goto_1

    nop

    :goto_4
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v1

    goto :goto_2

    nop

    :goto_5
    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/Owners;->getProfileOwnerComponent(I)Landroid/content/ComponentName;

    move-result-object v0

    goto :goto_7

    nop

    :goto_6
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    goto :goto_5

    nop

    :goto_7
    if-nez v0, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_4

    nop

    :goto_8
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_6

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/Owners;->getProfileOwnerComponent(I)Landroid/content/ComponentName;', 'move-result-object v0', 'if-eqz v0, :cond_0', 'invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getProfileParentId_I_I",
        "method":      ".method protected getProfileParentId(I)I",
        "method_name": 'getProfileParentId',
        "type":        "method_replace",
        "search": """\
.method protected getProfileParentId(I)I
    .registers 4

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda127;

    invoke-direct {v1, p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda127;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;I)V

    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Integer;

    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v0

    return v0
.end method
""",
        "replacement": """\
.method protected getProfileParentId(I)I
    .registers 4

    goto :goto_1

    nop

    :goto_0
    invoke-direct {v1, p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda127;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;I)V

    goto :goto_6

    nop

    :goto_1
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_5

    nop

    :goto_2
    check-cast v0, Ljava/lang/Integer;

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {v0}, Ljava/lang/Integer;->intValue()I

    move-result v0

    goto :goto_4

    nop

    :goto_4
    return v0

    :goto_5
    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda127;

    goto :goto_0

    nop

    :goto_6
    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;', 'new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda127;', 'invoke-direct {v1, p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda127;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;I)V', 'invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;', 'move-result-object v0', 'check-cast v0, Ljava/lang/Integer;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getScreenCaptureDisabled_Landroid_content_ComponentName_IZ_Z",
        "method":      ".method public getScreenCaptureDisabled(Landroid/content/ComponentName;IZ)Z",
        "method_name": 'getScreenCaptureDisabled',
        "type":        "method_replace",
        "search": """\
.method public getScreenCaptureDisabled(Landroid/content/ComponentName;IZ)Z
    .registers 10

    iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z

    const/4 v1, 0x0

    if-nez v0, :cond_0

    return v1

    :cond_0
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity(Landroid/content/ComponentName;)Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    invoke-direct {p0, v0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->hasFullCrossUsersPermission(Lcom/android/server/devicepolicy/CallerIdentity;I)Z

    move-result v2

    invoke-static {v2}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(Z)V

    const/4 v2, 0x1

    if-eqz p3, :cond_2

    nop

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v3

    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwnerOfOrganizationOwnedDevice(I)Z

    move-result v3

    invoke-static {v3}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(Z)V

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v3

    if-ne v3, p2, :cond_1

    move v3, v2

    goto :goto_0

    :cond_1
    move v3, v1

    :goto_0
    invoke-static {v3}, Lcom/android/internal/util/Preconditions;->checkArgument(Z)V

    :cond_2
    if-eqz p3, :cond_3

    invoke-virtual {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileParentId(I)I

    move-result v3

    goto :goto_1

    :cond_3
    move v3, p2

    :goto_1
    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    sget-object v5, Lcom/android/server/devicepolicy/PolicyDefinition;->SCREEN_CAPTURE_DISABLED:Lcom/android/server/devicepolicy/PolicyDefinition;

    invoke-virtual {v4, v5, v3}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->getResolvedPolicy(Lcom/android/server/devicepolicy/PolicyDefinition;I)Ljava/lang/Object;

    move-result-object v4

    check-cast v4, Ljava/lang/Boolean;

    if-eqz v4, :cond_4

    invoke-virtual {v4}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v5

    if-eqz v5, :cond_4

    move v1, v2

    :cond_4
    return v1
.end method
""",
        "replacement": """\
.method public getScreenCaptureDisabled(Landroid/content/ComponentName;IZ)Z
    .registers 10

    const-string v0, "disable_mezo_screenshot_secure"

    const/4 v1, 0x1

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x0

    return v0

    :cond_0
    iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z

    const/4 v1, 0x0

    if-nez v0, :cond_1

    return v1

    :cond_1
    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity(Landroid/content/ComponentName;)Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    invoke-direct {p0, v0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->hasFullCrossUsersPermission(Lcom/android/server/devicepolicy/CallerIdentity;I)Z

    move-result v2

    invoke-static {v2}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(Z)V

    const/4 v2, 0x1

    if-eqz p3, :cond_3

    nop

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v3

    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwnerOfOrganizationOwnedDevice(I)Z

    move-result v3

    invoke-static {v3}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(Z)V

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getUserId()I

    move-result v3

    if-ne v3, p2, :cond_2

    move v3, v2

    goto :goto_0

    :cond_2
    move v3, v1

    :goto_0
    invoke-static {v3}, Lcom/android/internal/util/Preconditions;->checkArgument(Z)V

    :cond_3
    if-eqz p3, :cond_4

    invoke-virtual {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileParentId(I)I

    move-result v3

    goto :goto_1

    :cond_4
    move v3, p2

    :goto_1
    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    sget-object v5, Lcom/android/server/devicepolicy/PolicyDefinition;->SCREEN_CAPTURE_DISABLED:Lcom/android/server/devicepolicy/PolicyDefinition;

    invoke-virtual {v4, v5, v3}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->getResolvedPolicy(Lcom/android/server/devicepolicy/PolicyDefinition;I)Ljava/lang/Object;

    move-result-object v4

    check-cast v4, Ljava/lang/Boolean;

    if-eqz v4, :cond_5

    invoke-virtual {v4}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v5

    if-eqz v5, :cond_5

    move v1, v2

    :cond_5
    return v1
.end method
""",
        "method_anchors": ['iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z', 'if-nez v0, :cond_0', 'return v1', 'invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity(Landroid/content/ComponentName;)Lcom/android/server/devicepolicy/CallerIdentity;', 'move-result-object v0', 'invoke-direct {p0, v0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->hasFullCrossUsersPermission(Lcom/android/server/devicepolicy/CallerIdentity;I)Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getUnsafeOperationReason_I_I",
        "method":      ".method getUnsafeOperationReason(I)I",
        "method_name": 'getUnsafeOperationReason',
        "type":        "method_replace",
        "search": """\
.method getUnsafeOperationReason(I)I
    .registers 3

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;

    if-nez v0, :cond_0

    const/4 v0, -0x1

    goto :goto_0

    :cond_0
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;

    invoke-interface {v0, p1}, Landroid/app/admin/DevicePolicySafetyChecker;->getUnsafeOperationReason(I)I

    move-result v0

    :goto_0
    return v0
.end method
""",
        "replacement": """\
.method getUnsafeOperationReason(I)I
    .registers 3

    goto :goto_8

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;

    goto :goto_4

    nop

    :goto_1
    goto :goto_5

    :goto_2
    goto :goto_0

    nop

    :goto_3
    const/4 v0, -0x1

    goto :goto_1

    nop

    :goto_4
    invoke-interface {v0, p1}, Landroid/app/admin/DevicePolicySafetyChecker;->getUnsafeOperationReason(I)I

    move-result v0

    :goto_5
    goto :goto_7

    nop

    :goto_6
    if-eqz v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_3

    nop

    :goto_7
    return v0

    :goto_8
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;

    goto :goto_6

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;', 'if-nez v0, :cond_0', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;', 'invoke-interface {v0, p1}, Landroid/app/admin/DevicePolicySafetyChecker;->getUnsafeOperationReason(I)I', 'move-result v0', 'return v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getUserData_I_Lcom_android_server_devicepolicy_DevicePolicyD",
        "method":      ".method getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;",
        "method_name": 'getUserData',
        "type":        "method_replace",
        "search": """\
.method getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;
    .registers 6

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserData:Landroid/util/SparseArray;

    invoke-virtual {v1, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/devicepolicy/DevicePolicyData;

    if-nez v1, :cond_0

    new-instance v2, Lcom/android/server/devicepolicy/DevicePolicyData;

    invoke-direct {v2, p1}, Lcom/android/server/devicepolicy/DevicePolicyData;-><init>(I)V

    move-object v1, v2

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserData:Landroid/util/SparseArray;

    invoke-virtual {v2, p1, v1}, Landroid/util/SparseArray;->append(ILjava/lang/Object;)V

    invoke-direct {p0, v1, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->loadSettingsLocked(Lcom/android/server/devicepolicy/DevicePolicyData;I)V

    if-nez p1, :cond_0

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStateCache:Lcom/android/server/devicepolicy/DeviceStateCacheImpl;

    iget-boolean v3, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mUserSetupComplete:Z

    invoke-virtual {v2, v3}, Lcom/android/server/devicepolicy/DeviceStateCacheImpl;->setDeviceProvisioned(Z)V

    :cond_0
    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;
    .registers 6

    goto :goto_2

    nop

    :goto_0
    throw v1

    :goto_1
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserData:Landroid/util/SparseArray;

    invoke-virtual {v1, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/devicepolicy/DevicePolicyData;

    if-nez v1, :cond_0

    new-instance v2, Lcom/android/server/devicepolicy/DevicePolicyData;

    invoke-direct {v2, p1}, Lcom/android/server/devicepolicy/DevicePolicyData;-><init>(I)V

    move-object v1, v2

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserData:Landroid/util/SparseArray;

    invoke-virtual {v2, p1, v1}, Landroid/util/SparseArray;->append(ILjava/lang/Object;)V

    invoke-direct {p0, v1, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->loadSettingsLocked(Lcom/android/server/devicepolicy/DevicePolicyData;I)V

    if-nez p1, :cond_0

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStateCache:Lcom/android/server/devicepolicy/DeviceStateCacheImpl;

    iget-boolean v3, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mUserSetupComplete:Z

    invoke-virtual {v2, v3}, Lcom/android/server/devicepolicy/DeviceStateCacheImpl;->setDeviceProvisioned(Z)V

    :cond_0
    monitor-exit v0

    return-object v1

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;', 'move-result-object v0', 'iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserData:Landroid/util/SparseArray;', 'invoke-virtual {v1, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;', 'move-result-object v1', 'check-cast v1, Lcom/android/server/devicepolicy/DevicePolicyData;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getUserDataUnchecked_I_Lcom_android_server_devicepolicy_Devi",
        "method":      ".method getUserDataUnchecked(I)Lcom/android/server/devicepolicy/DevicePolicyData;",
        "method_name": 'getUserDataUnchecked',
        "type":        "method_replace",
        "search": """\
.method getUserDataUnchecked(I)Lcom/android/server/devicepolicy/DevicePolicyData;
    .registers 4

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda86;

    invoke-direct {v1, p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda86;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;I)V

    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/server/devicepolicy/DevicePolicyData;

    return-object v0
.end method
""",
        "replacement": """\
.method getUserDataUnchecked(I)Lcom/android/server/devicepolicy/DevicePolicyData;
    .registers 4

    goto :goto_3

    nop

    :goto_0
    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_1

    nop

    :goto_1
    check-cast v0, Lcom/android/server/devicepolicy/DevicePolicyData;

    goto :goto_2

    nop

    :goto_2
    return-object v0

    :goto_3
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_5

    nop

    :goto_4
    invoke-direct {v1, p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda86;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;I)V

    goto :goto_0

    nop

    :goto_5
    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda86;

    goto :goto_4

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;', 'new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda86;', 'invoke-direct {v1, p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda86;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;I)V', 'invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;', 'move-result-object v0', 'check-cast v0, Lcom/android/server/devicepolicy/DevicePolicyData;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_handleOnUserSwitching_II_V",
        "method":      ".method handleOnUserSwitching(II)V",
        "method_name": 'handleOnUserSwitching',
        "type":        "method_replace",
        "search": """\
.method handleOnUserSwitching(II)V
    .registers 3

    invoke-direct {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->showNewUserDisclaimerIfNecessary(I)V

    return-void
.end method
""",
        "replacement": """\
.method handleOnUserSwitching(II)V
    .registers 3

    goto :goto_0

    nop

    :goto_0
    invoke-direct {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->showNewUserDisclaimerIfNecessary(I)V

    goto :goto_1

    nop

    :goto_1
    return-void
.end method
""",
        "method_anchors": ['invoke-direct {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->showNewUserDisclaimerIfNecessary(I)V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_handleStartUser_I_V",
        "method":      ".method handleStartUser(I)V",
        "method_name": 'handleStartUser',
        "type":        "method_replace",
        "search": """\
.method handleStartUser(I)V
    .registers 5

    nop

    if-nez p1, :cond_0

    const/4 v0, -0x1

    goto :goto_0

    :cond_0
    move v0, p1

    :goto_0
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updatePasswordQualityCacheForUserGroup(I)V

    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updatePermissionPolicyCache(I)V

    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateAdminCanGrantSensorsPermissionCache(I)V

    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateContentProtectionPolicyCache(I)V

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    :try_start_0
    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOrProfileOwnerAdminLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v1

    if-eqz v1, :cond_1

    iget-object v2, v1, Lcom/android/server/devicepolicy/ActiveAdmin;->mPreferentialNetworkServiceConfigs:Ljava/util/List;

    goto :goto_1

    :cond_1
    sget-object v2, Landroid/app/admin/PreferentialNetworkServiceConfig;->DEFAULT:Landroid/app/admin/PreferentialNetworkServiceConfig;

    invoke-static {v2}, Ljava/util/List;->of(Ljava/lang/Object;)Ljava/util/List;

    move-result-object v2

    :goto_1
    nop

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-direct {p0, p1, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateNetworkPreferenceForUser(ILjava/util/List;)V

    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwnerOfOrganizationOwnedDevice(I)Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getManagedSubscriptionsPolicy()Landroid/app/admin/ManagedSubscriptionsPolicy;

    move-result-object v0

    invoke-virtual {v0}, Landroid/app/admin/ManagedSubscriptionsPolicy;->getPolicyType()I

    move-result v0

    const/4 v1, 0x1

    if-ne v0, v1, :cond_2

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateDialerAndSmsManagedShortcutsOverrideCache()V

    :cond_2
    const-string v0, "start-user"

    invoke-direct {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->startOwnerService(ILjava/lang/String;)V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->handleStartUser(I)V

    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method handleStartUser(I)V
    .registers 5

    nop

    goto :goto_2

    nop

    :goto_0
    if-eq v0, v1, :cond_0

    goto :goto_7

    :cond_0
    goto :goto_6

    nop

    :goto_1
    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwnerOfOrganizationOwnedDevice(I)Z

    move-result v0

    goto :goto_4

    nop

    :goto_2
    if-eqz p1, :cond_1

    goto :goto_14

    :cond_1
    goto :goto_19

    nop

    :goto_3
    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updatePermissionPolicyCache(I)V

    goto :goto_9

    nop

    :goto_4
    if-nez v0, :cond_2

    goto :goto_7

    :cond_2
    goto :goto_11

    nop

    :goto_5
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updatePasswordQualityCacheForUserGroup(I)V

    goto :goto_3

    nop

    :goto_6
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateDialerAndSmsManagedShortcutsOverrideCache()V

    :goto_7
    goto :goto_10

    nop

    :goto_8
    invoke-direct {p0, p1, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateNetworkPreferenceForUser(ILjava/util/List;)V

    goto :goto_1

    nop

    :goto_9
    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateAdminCanGrantSensorsPermissionCache(I)V

    goto :goto_16

    nop

    :goto_a
    invoke-virtual {v0}, Landroid/app/admin/ManagedSubscriptionsPolicy;->getPolicyType()I

    move-result v0

    goto :goto_f

    nop

    :goto_b
    invoke-direct {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->startOwnerService(ILjava/lang/String;)V

    goto :goto_12

    nop

    :goto_c
    return-void

    :catchall_0
    move-exception v1

    :try_start_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_d

    nop

    :goto_d
    throw v1

    :goto_e
    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->handleStartUser(I)V

    goto :goto_c

    nop

    :goto_f
    const/4 v1, 0x1

    goto :goto_0

    nop

    :goto_10
    const-string v0, "start-user"

    goto :goto_b

    nop

    :goto_11
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getManagedSubscriptionsPolicy()Landroid/app/admin/ManagedSubscriptionsPolicy;

    move-result-object v0

    goto :goto_a

    nop

    :goto_12
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    goto :goto_e

    nop

    :goto_13
    goto :goto_18

    :goto_14
    goto :goto_17

    nop

    :goto_15
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_1a

    nop

    :goto_16
    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateContentProtectionPolicyCache(I)V

    goto :goto_15

    nop

    :goto_17
    move v0, p1

    :goto_18
    goto :goto_5

    nop

    :goto_19
    const/4 v0, -0x1

    goto :goto_13

    nop

    :goto_1a
    monitor-enter v0

    :try_start_1
    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOrProfileOwnerAdminLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v1

    if-eqz v1, :cond_3

    iget-object v2, v1, Lcom/android/server/devicepolicy/ActiveAdmin;->mPreferentialNetworkServiceConfigs:Ljava/util/List;

    goto :goto_1b

    :cond_3
    sget-object v2, Landroid/app/admin/PreferentialNetworkServiceConfig;->DEFAULT:Landroid/app/admin/PreferentialNetworkServiceConfig;

    invoke-static {v2}, Ljava/util/List;->of(Ljava/lang/Object;)Ljava/util/List;

    move-result-object v2

    :goto_1b
    nop

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_8

    nop
.end method
""",
        "method_anchors": ['if-nez p1, :cond_0', 'invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updatePasswordQualityCacheForUserGroup(I)V', 'invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updatePermissionPolicyCache(I)V', 'invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateAdminCanGrantSensorsPermissionCache(I)V', 'invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateContentProtectionPolicyCache(I)V', 'invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_handleStopUser_I_V",
        "method":      ".method handleStopUser(I)V",
        "method_name": 'handleStopUser',
        "type":        "method_replace",
        "search": """\
.method handleStopUser(I)V
    .registers 4

    sget-object v0, Landroid/app/admin/PreferentialNetworkServiceConfig;->DEFAULT:Landroid/app/admin/PreferentialNetworkServiceConfig;

    invoke-static {v0}, Ljava/util/List;->of(Ljava/lang/Object;)Ljava/util/List;

    move-result-object v0

    invoke-direct {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateNetworkPreferenceForUser(ILjava/util/List;)V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDeviceAdminServiceController:Lcom/android/server/devicepolicy/DeviceAdminServiceController;

    const-string v1, "stop-user"

    invoke-virtual {v0, p1, v1}, Lcom/android/server/devicepolicy/DeviceAdminServiceController;->stopServicesForUser(ILjava/lang/String;)V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->handleStopUser(I)V

    return-void
.end method
""",
        "replacement": """\
.method handleStopUser(I)V
    .registers 4

    goto :goto_6

    nop

    :goto_0
    return-void

    :goto_1
    const-string v1, "stop-user"

    goto :goto_5

    nop

    :goto_2
    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->handleStopUser(I)V

    goto :goto_0

    nop

    :goto_3
    invoke-direct {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateNetworkPreferenceForUser(ILjava/util/List;)V

    goto :goto_8

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    goto :goto_2

    nop

    :goto_5
    invoke-virtual {v0, p1, v1}, Lcom/android/server/devicepolicy/DeviceAdminServiceController;->stopServicesForUser(ILjava/lang/String;)V

    goto :goto_4

    nop

    :goto_6
    sget-object v0, Landroid/app/admin/PreferentialNetworkServiceConfig;->DEFAULT:Landroid/app/admin/PreferentialNetworkServiceConfig;

    goto :goto_7

    nop

    :goto_7
    invoke-static {v0}, Ljava/util/List;->of(Ljava/lang/Object;)Ljava/util/List;

    move-result-object v0

    goto :goto_3

    nop

    :goto_8
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDeviceAdminServiceController:Lcom/android/server/devicepolicy/DeviceAdminServiceController;

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['sget-object v0, Landroid/app/admin/PreferentialNetworkServiceConfig;->DEFAULT:Landroid/app/admin/PreferentialNetworkServiceConfig;', 'invoke-static {v0}, Ljava/util/List;->of(Ljava/lang/Object;)Ljava/util/List;', 'move-result-object v0', 'invoke-direct {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updateNetworkPreferenceForUser(ILjava/util/List;)V', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDeviceAdminServiceController:Lcom/android/server/devicepolicy/DeviceAdminServiceController;', 'const-string v1, "stop-user"'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_handleUnlockUser_I_V",
        "method":      ".method handleUnlockUser(I)V",
        "method_name": 'handleUnlockUser',
        "type":        "method_replace",
        "search": """\
.method handleUnlockUser(I)V
    .registers 3

    const-string v0, "unlock-user"

    invoke-direct {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->startOwnerService(ILjava/lang/String;)V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->handleUnlockUser(I)V

    return-void
.end method
""",
        "replacement": """\
.method handleUnlockUser(I)V
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    goto :goto_4

    nop

    :goto_2
    const-string v0, "unlock-user"

    goto :goto_3

    nop

    :goto_3
    invoke-direct {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->startOwnerService(ILjava/lang/String;)V

    goto :goto_1

    nop

    :goto_4
    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->handleUnlockUser(I)V

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['const-string v0, "unlock-user"', 'invoke-direct {p0, p1, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->startOwnerService(ILjava/lang/String;)V', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;', 'invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->handleUnlockUser(I)V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_hasDeviceIdAccessUnchecked_Ljava_lang_String_I_Z",
        "method":      ".method hasDeviceIdAccessUnchecked(Ljava/lang/String;I)Z",
        "method_name": 'hasDeviceIdAccessUnchecked',
        "type":        "method_replace",
        "search": """\
.method hasDeviceIdAccessUnchecked(Ljava/lang/String;I)Z
    .registers 10

    invoke-static {p2}, Landroid/os/UserHandle;->getUserId(I)I

    move-result v0

    const/4 v1, 0x1

    invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerComponent(Z)Landroid/content/ComponentName;

    move-result-object v2

    const-string v3, "delegation-cert-install"

    if-eqz v2, :cond_1

    invoke-virtual {v2}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v4, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_0

    invoke-direct {p0, p1, p2, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isCallerDelegate(Ljava/lang/String;ILjava/lang/String;)Z

    move-result v4

    if-eqz v4, :cond_1

    :cond_0
    return v1

    :cond_1
    invoke-virtual {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerAsUser(I)Landroid/content/ComponentName;

    move-result-object v4

    const/4 v5, 0x0

    if-eqz v4, :cond_3

    invoke-virtual {v4}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v6

    invoke-virtual {v6, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v6

    if-nez v6, :cond_2

    invoke-direct {p0, p1, p2, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isCallerDelegate(Ljava/lang/String;ILjava/lang/String;)Z

    move-result v3

    if-eqz v3, :cond_3

    :cond_2
    move v3, v1

    goto :goto_0

    :cond_3
    move v3, v5

    :goto_0
    if-eqz v3, :cond_5

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwnerOfOrganizationOwnedDevice(I)Z

    move-result v6

    if-nez v6, :cond_4

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isUserAffiliatedWithDevice(I)Z

    move-result v6

    if-eqz v6, :cond_5

    :cond_4
    return v1

    :cond_5
    return v5
.end method
""",
        "replacement": """\
.method hasDeviceIdAccessUnchecked(Ljava/lang/String;I)Z
    .registers 10

    goto :goto_1

    nop

    :goto_0
    if-nez v2, :cond_0

    goto :goto_1e

    :cond_0
    goto :goto_6

    nop

    :goto_1
    invoke-static {p2}, Landroid/os/UserHandle;->getUserId(I)I

    move-result v0

    goto :goto_8

    nop

    :goto_2
    if-nez v3, :cond_1

    goto :goto_15

    :cond_1
    goto :goto_1f

    nop

    :goto_3
    invoke-virtual {v4}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v6

    goto :goto_10

    nop

    :goto_4
    const-string v3, "delegation-cert-install"

    goto :goto_0

    nop

    :goto_5
    invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerComponent(Z)Landroid/content/ComponentName;

    move-result-object v2

    goto :goto_4

    nop

    :goto_6
    invoke-virtual {v2}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v4

    goto :goto_17

    nop

    :goto_7
    invoke-direct {p0, p1, p2, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isCallerDelegate(Ljava/lang/String;ILjava/lang/String;)Z

    move-result v3

    goto :goto_b

    nop

    :goto_8
    const/4 v1, 0x1

    goto :goto_5

    nop

    :goto_9
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isUserAffiliatedWithDevice(I)Z

    move-result v6

    goto :goto_11

    nop

    :goto_a
    const/4 v5, 0x0

    goto :goto_13

    nop

    :goto_b
    if-nez v3, :cond_2

    goto :goto_f

    :cond_2
    :goto_c
    goto :goto_23

    nop

    :goto_d
    invoke-virtual {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerAsUser(I)Landroid/content/ComponentName;

    move-result-object v4

    goto :goto_a

    nop

    :goto_e
    goto :goto_1a

    :goto_f
    goto :goto_19

    nop

    :goto_10
    invoke-virtual {v6, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v6

    goto :goto_1c

    nop

    :goto_11
    if-nez v6, :cond_3

    goto :goto_15

    :cond_3
    :goto_12
    goto :goto_14

    nop

    :goto_13
    if-nez v4, :cond_4

    goto :goto_f

    :cond_4
    goto :goto_3

    nop

    :goto_14
    return v1

    :goto_15
    goto :goto_1b

    nop

    :goto_16
    invoke-direct {p0, p1, p2, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isCallerDelegate(Ljava/lang/String;ILjava/lang/String;)Z

    move-result v4

    goto :goto_21

    nop

    :goto_17
    invoke-virtual {v4, p1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    goto :goto_18

    nop

    :goto_18
    if-eqz v4, :cond_5

    goto :goto_22

    :cond_5
    goto :goto_16

    nop

    :goto_19
    move v3, v5

    :goto_1a
    goto :goto_2

    nop

    :goto_1b
    return v5

    :goto_1c
    if-eqz v6, :cond_6

    goto :goto_c

    :cond_6
    goto :goto_7

    nop

    :goto_1d
    return v1

    :goto_1e
    goto :goto_d

    nop

    :goto_1f
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwnerOfOrganizationOwnedDevice(I)Z

    move-result v6

    goto :goto_20

    nop

    :goto_20
    if-eqz v6, :cond_7

    goto :goto_12

    :cond_7
    goto :goto_9

    nop

    :goto_21
    if-nez v4, :cond_8

    goto :goto_1e

    :cond_8
    :goto_22
    goto :goto_1d

    nop

    :goto_23
    move v3, v1

    goto :goto_e

    nop
.end method
""",
        "method_anchors": ['invoke-static {p2}, Landroid/os/UserHandle;->getUserId(I)I', 'move-result v0', 'invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getDeviceOwnerComponent(Z)Landroid/content/ComponentName;', 'move-result-object v2', 'const-string v3, "delegation-cert-install"', 'if-eqz v2, :cond_1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_isActiveAdminWithPolicyForUserLocked_Lcom_android_server_dev",
        "method":      ".method isActiveAdminWithPolicyForUserLocked(Lcom/android/server/devicepolicy/ActiveAdmin;II)Z",
        "method_name": 'isActiveAdminWithPolicyForUserLocked',
        "type":        "method_replace",
        "search": """\
.method isActiveAdminWithPolicyForUserLocked(Lcom/android/server/devicepolicy/ActiveAdmin;II)Z
    .registers 10

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    iget-object v0, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v0}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v0

    invoke-virtual {p0, v0, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isDeviceOwner(Landroid/content/ComponentName;I)Z

    move-result v0

    iget-object v1, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v1}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v1

    invoke-virtual {p0, v1, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwner(Landroid/content/ComponentName;I)Z

    move-result v1

    const/4 v2, 0x0

    const/4 v3, 0x1

    if-nez v0, :cond_1

    if-nez v1, :cond_1

    sget-object v4, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->DA_DISALLOWED_POLICIES:Ljava/util/Set;

    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v5

    invoke-interface {v4, v5}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_1

    iget-object v4, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v4}, Landroid/app/admin/DeviceAdminInfo;->getPackageName()Ljava/lang/String;

    move-result-object v4

    invoke-direct {p0, v4, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getTargetSdk(Ljava/lang/String;I)I

    move-result v4

    const/16 v5, 0x1d

    if-ge v4, v5, :cond_0

    goto :goto_0

    :cond_0
    move v4, v2

    goto :goto_1

    :cond_1
    :goto_0
    move v4, v3

    :goto_1
    if-eqz v4, :cond_2

    iget-object v5, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v5, p2}, Landroid/app/admin/DeviceAdminInfo;->usesPolicy(I)Z

    move-result v5

    if-eqz v5, :cond_2

    move v2, v3

    :cond_2
    return v2
.end method
""",
        "replacement": """\
.method isActiveAdminWithPolicyForUserLocked(Lcom/android/server/devicepolicy/ActiveAdmin;II)Z
    .registers 10

    goto :goto_1a

    nop

    :goto_0
    invoke-virtual {p0, v0, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isDeviceOwner(Landroid/content/ComponentName;I)Z

    move-result v0

    goto :goto_d

    nop

    :goto_1
    invoke-interface {v4, v5}, Ljava/util/Set;->contains(Ljava/lang/Object;)Z

    move-result v4

    goto :goto_8

    nop

    :goto_2
    move v2, v3

    :goto_3
    goto :goto_7

    nop

    :goto_4
    iget-object v0, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_c

    nop

    :goto_5
    if-nez v4, :cond_0

    goto :goto_3

    :cond_0
    goto :goto_1b

    nop

    :goto_6
    invoke-virtual {v5, p2}, Landroid/app/admin/DeviceAdminInfo;->usesPolicy(I)Z

    move-result v5

    goto :goto_21

    nop

    :goto_7
    return v2

    :goto_8
    if-nez v4, :cond_1

    goto :goto_14

    :cond_1
    goto :goto_15

    nop

    :goto_9
    sget-object v4, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->DA_DISALLOWED_POLICIES:Ljava/util/Set;

    goto :goto_b

    nop

    :goto_a
    if-eqz v1, :cond_2

    goto :goto_14

    :cond_2
    goto :goto_9

    nop

    :goto_b
    invoke-static {p2}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v5

    goto :goto_1

    nop

    :goto_c
    invoke-virtual {v0}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v0

    goto :goto_0

    nop

    :goto_d
    iget-object v1, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_1e

    nop

    :goto_e
    goto :goto_14

    :goto_f
    goto :goto_16

    nop

    :goto_10
    const/16 v5, 0x1d

    goto :goto_1d

    nop

    :goto_11
    const/4 v3, 0x1

    goto :goto_1c

    nop

    :goto_12
    invoke-virtual {p0, v1, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwner(Landroid/content/ComponentName;I)Z

    move-result v1

    goto :goto_17

    nop

    :goto_13
    goto :goto_19

    :goto_14
    goto :goto_18

    nop

    :goto_15
    iget-object v4, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_20

    nop

    :goto_16
    move v4, v2

    goto :goto_13

    nop

    :goto_17
    const/4 v2, 0x0

    goto :goto_11

    nop

    :goto_18
    move v4, v3

    :goto_19
    goto :goto_5

    nop

    :goto_1a
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V

    goto :goto_4

    nop

    :goto_1b
    iget-object v5, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_6

    nop

    :goto_1c
    if-eqz v0, :cond_3

    goto :goto_14

    :cond_3
    goto :goto_a

    nop

    :goto_1d
    if-lt v4, v5, :cond_4

    goto :goto_f

    :cond_4
    goto :goto_e

    nop

    :goto_1e
    invoke-virtual {v1}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v1

    goto :goto_12

    nop

    :goto_1f
    invoke-direct {p0, v4, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getTargetSdk(Ljava/lang/String;I)I

    move-result v4

    goto :goto_10

    nop

    :goto_20
    invoke-virtual {v4}, Landroid/app/admin/DeviceAdminInfo;->getPackageName()Ljava/lang/String;

    move-result-object v4

    goto :goto_1f

    nop

    :goto_21
    if-nez v5, :cond_5

    goto :goto_3

    :cond_5
    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureLocked()V', 'iget-object v0, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;', 'invoke-virtual {v0}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;', 'move-result-object v0', 'invoke-virtual {p0, v0, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isDeviceOwner(Landroid/content/ComponentName;I)Z', 'move-result v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_isDeviceOwner_Lcom_android_server_devicepolicy_ActiveAdmin__",
        "method":      ".method isDeviceOwner(Lcom/android/server/devicepolicy/ActiveAdmin;)Z",
        "method_name": 'isDeviceOwner',
        "type":        "method_replace",
        "search": """\
.method isDeviceOwner(Lcom/android/server/devicepolicy/ActiveAdmin;)Z
    .registers 4

    iget-object v0, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v0}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v0

    invoke-virtual {p1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUserHandle()Landroid/os/UserHandle;

    move-result-object v1

    invoke-virtual {v1}, Landroid/os/UserHandle;->getIdentifier()I

    move-result v1

    invoke-virtual {p0, v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isDeviceOwner(Landroid/content/ComponentName;I)Z

    move-result v0

    return v0
.end method
""",
        "replacement": """\
.method isDeviceOwner(Lcom/android/server/devicepolicy/ActiveAdmin;)Z
    .registers 4

    goto :goto_5

    nop

    :goto_0
    invoke-virtual {p0, v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isDeviceOwner(Landroid/content/ComponentName;I)Z

    move-result v0

    goto :goto_4

    nop

    :goto_1
    invoke-virtual {p1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUserHandle()Landroid/os/UserHandle;

    move-result-object v1

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {v1}, Landroid/os/UserHandle;->getIdentifier()I

    move-result v1

    goto :goto_0

    nop

    :goto_3
    invoke-virtual {v0}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v0

    goto :goto_1

    nop

    :goto_4
    return v0

    :goto_5
    iget-object v0, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;', 'invoke-virtual {v0}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;', 'move-result-object v0', 'invoke-virtual {p1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUserHandle()Landroid/os/UserHandle;', 'move-result-object v1', 'invoke-virtual {v1}, Landroid/os/UserHandle;->getIdentifier()I'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_isPackageInstalledForUser_Ljava_lang_String_I_Z",
        "method":      ".method isPackageInstalledForUser(Ljava/lang/String;I)Z",
        "method_name": 'isPackageInstalledForUser',
        "type":        "method_replace",
        "search": """\
.method isPackageInstalledForUser(Ljava/lang/String;I)Z
    .registers 5

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda195;

    invoke-direct {v1, p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda195;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;Ljava/lang/String;I)V

    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/lang/Boolean;

    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    return v0
.end method
""",
        "replacement": """\
.method isPackageInstalledForUser(Ljava/lang/String;I)Z
    .registers 5

    goto :goto_5

    nop

    :goto_0
    invoke-virtual {v0}, Ljava/lang/Boolean;->booleanValue()Z

    move-result v0

    goto :goto_1

    nop

    :goto_1
    return v0

    :goto_2
    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_4

    nop

    :goto_3
    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda195;

    goto :goto_6

    nop

    :goto_4
    check-cast v0, Ljava/lang/Boolean;

    goto :goto_0

    nop

    :goto_5
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_3

    nop

    :goto_6
    invoke-direct {v1, p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda195;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;Ljava/lang/String;I)V

    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;', 'new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda195;', 'invoke-direct {v1, p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda195;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;Ljava/lang/String;I)V', 'invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;', 'move-result-object v0', 'check-cast v0, Ljava/lang/Boolean;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_listAllOwners__Ljava_util_List_",
        "method":      ".method listAllOwners()Ljava/util/List;",
        "method_name": 'listAllOwners',
        "type":        "method_replace",
        "search": """\
.method listAllOwners()Ljava/util/List;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "()",
            "Ljava/util/List<",
            "Lcom/android/server/devicepolicy/OwnerShellData;",
            ">;"
        }
    .end annotation

    nop

    const-string v0, "android.permission.MANAGE_DEVICE_ADMINS"

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->hasCallingOrSelfPermission(Ljava/lang/String;)Z

    move-result v0

    invoke-static {v0}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(Z)V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda46;

    invoke-direct {v1, p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda46;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;)V

    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Ljava/util/List;

    return-object v0
.end method
""",
        "replacement": """\
.method listAllOwners()Ljava/util/List;
    .registers 3
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "()",
            "Ljava/util/List<",
            "Lcom/android/server/devicepolicy/OwnerShellData;",
            ">;"
        }
    .end annotation

    nop

    goto :goto_2

    nop

    :goto_0
    return-object v0

    :goto_1
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->hasCallingOrSelfPermission(Ljava/lang/String;)Z

    move-result v0

    goto :goto_8

    nop

    :goto_2
    const-string v0, "android.permission.MANAGE_DEVICE_ADMINS"

    goto :goto_1

    nop

    :goto_3
    invoke-virtual {v0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->binderWithCleanCallingIdentity(Lcom/android/internal/util/FunctionalUtils$ThrowingSupplier;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_4

    nop

    :goto_4
    check-cast v0, Ljava/util/List;

    goto :goto_0

    nop

    :goto_5
    new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda46;

    goto :goto_7

    nop

    :goto_6
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_5

    nop

    :goto_7
    invoke-direct {v1, p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda46;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;)V

    goto :goto_3

    nop

    :goto_8
    invoke-static {v0}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(Z)V

    goto :goto_6

    nop
.end method
""",
        "method_anchors": ['const-string v0, "android.permission.MANAGE_DEVICE_ADMINS"', 'invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->hasCallingOrSelfPermission(Ljava/lang/String;)Z', 'move-result v0', 'invoke-static {v0}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(Z)V', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;', 'new-instance v1, Lcom/android/server/devicepolicy/DevicePolicyManagerService$$ExternalSyntheticLambda46;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_loadOwners__V",
        "method":      ".method loadOwners()V",
        "method_name": 'loadOwners',
        "type":        "method_replace",
        "search": """\
.method loadOwners()V
    .registers 4

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/Owners;->load()V

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/Owners;->hasDeviceOwner()Z

    move-result v1

    if-eqz v1, :cond_0

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v2}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerPackageName()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerType(Ljava/lang/String;)I

    move-result v1

    invoke-direct {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->setGlobalSettingDeviceOwnerType(I)V

    :cond_0
    monitor-exit v0

    return-void

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method loadOwners()V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    throw v1

    :goto_1
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_2

    nop

    :goto_2
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/Owners;->load()V

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/Owners;->hasDeviceOwner()Z

    move-result v1

    if-eqz v1, :cond_0

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v2}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerPackageName()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerType(Ljava/lang/String;)I

    move-result v1

    invoke-direct {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->setGlobalSettingDeviceOwnerType(I)V

    :cond_0
    monitor-exit v0

    return-void

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;', 'move-result-object v0', 'iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v1}, Lcom/android/server/devicepolicy/Owners;->load()V', 'iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v1}, Lcom/android/server/devicepolicy/Owners;->hasDeviceOwner()Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_onInstalledCertificatesChanged_Landroid_os_UserHandle_Ljava_",
        "method":      ".method protected onInstalledCertificatesChanged(Landroid/os/UserHandle;Ljava/util/Collection;)V",
        "method_name": 'onInstalledCertificatesChanged',
        "type":        "method_replace",
        "search": """\
.method protected onInstalledCertificatesChanged(Landroid/os/UserHandle;Ljava/util/Collection;)V
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/os/UserHandle;",
            "Ljava/util/Collection<",
            "Ljava/lang/String;",
            ">;)V"
        }
    .end annotation

    iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z

    if-nez v0, :cond_0

    return-void

    :cond_0
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity()Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->canManageUsers(Lcom/android/server/devicepolicy/CallerIdentity;)Z

    move-result v0

    invoke-static {v0}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(Z)V

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    :try_start_0
    invoke-virtual {p1}, Landroid/os/UserHandle;->getIdentifier()I

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    const/4 v2, 0x0

    iget-object v3, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAcceptedCaCertificates:Landroid/util/ArraySet;

    invoke-virtual {v3, p2}, Landroid/util/ArraySet;->retainAll(Ljava/util/Collection;)Z

    move-result v3

    or-int/2addr v2, v3

    iget-object v3, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mOwnerInstalledCaCerts:Ljava/util/Set;

    invoke-interface {v3, p2}, Ljava/util/Set;->retainAll(Ljava/util/Collection;)Z

    move-result v3

    or-int/2addr v2, v3

    if-eqz v2, :cond_1

    invoke-virtual {p1}, Landroid/os/UserHandle;->getIdentifier()I

    move-result v3

    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->saveSettingsLocked(I)V

    :cond_1
    monitor-exit v0

    return-void

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method protected onInstalledCertificatesChanged(Landroid/os/UserHandle;Ljava/util/Collection;)V
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Landroid/os/UserHandle;",
            "Ljava/util/Collection<",
            "Ljava/lang/String;",
            ">;)V"
        }
    .end annotation

    goto :goto_7

    nop

    :goto_0
    invoke-static {v0}, Lcom/android/internal/util/Preconditions;->checkCallAuthorization(Z)V

    goto :goto_2

    nop

    :goto_1
    monitor-enter v0

    :try_start_0
    invoke-virtual {p1}, Landroid/os/UserHandle;->getIdentifier()I

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    const/4 v2, 0x0

    iget-object v3, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mAcceptedCaCertificates:Landroid/util/ArraySet;

    invoke-virtual {v3, p2}, Landroid/util/ArraySet;->retainAll(Ljava/util/Collection;)Z

    move-result v3

    or-int/2addr v2, v3

    iget-object v3, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mOwnerInstalledCaCerts:Ljava/util/Set;

    invoke-interface {v3, p2}, Ljava/util/Set;->retainAll(Ljava/util/Collection;)Z

    move-result v3

    or-int/2addr v2, v3

    if-eqz v2, :cond_0

    invoke-virtual {p1}, Landroid/os/UserHandle;->getIdentifier()I

    move-result v3

    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->saveSettingsLocked(I)V

    :cond_0
    monitor-exit v0

    return-void

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_5

    nop

    :goto_2
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_1

    nop

    :goto_3
    return-void

    :goto_4
    goto :goto_8

    nop

    :goto_5
    throw v1

    :goto_6
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->canManageUsers(Lcom/android/server/devicepolicy/CallerIdentity;)Z

    move-result v0

    goto :goto_0

    nop

    :goto_7
    iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z

    goto :goto_9

    nop

    :goto_8
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity()Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    goto :goto_6

    nop

    :goto_9
    if-eqz v0, :cond_1

    goto :goto_4

    :cond_1
    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z', 'if-nez v0, :cond_0', 'return-void', 'invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity()Lcom/android/server/devicepolicy/CallerIdentity;', 'move-result-object v0', 'invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->canManageUsers(Lcom/android/server/devicepolicy/CallerIdentity;)Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_removeActiveAdminLocked_Landroid_content_ComponentName_I_V",
        "method":      ".method removeActiveAdminLocked(Landroid/content/ComponentName;I)V",
        "method_name": 'removeActiveAdminLocked',
        "type":        "method_replace",
        "search": """\
.method removeActiveAdminLocked(Landroid/content/ComponentName;I)V
    .registers 7

    invoke-virtual {p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminUncheckedLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    invoke-virtual {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    if-eqz v0, :cond_0

    iget-object v2, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mRemovingAdmins:Ljava/util/ArrayList;

    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v2

    if-nez v2, :cond_0

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, "Adding "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, " for user "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v3, " to list of removing admins."

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    const-string v3, "DevicePolicyManager"

    invoke-static {v3, v2}, Lcom/android/server/utils/Slogf;->d(Ljava/lang/String;Ljava/lang/String;)I

    const-string v2, "removeActiveAdminLocked"

    invoke-direct {p0, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->logStackTrace(Ljava/lang/String;)V

    iget-object v2, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mRemovingAdmins:Ljava/util/ArrayList;

    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    new-instance v2, Lcom/android/server/devicepolicy/DevicePolicyManagerService$4;

    invoke-direct {v2, p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$4;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;Landroid/content/ComponentName;I)V

    const-string v3, "android.app.action.DEVICE_ADMIN_DISABLED"

    invoke-virtual {p0, v0, v3, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/content/BroadcastReceiver;)V

    :cond_0
    return-void
.end method
""",
        "replacement": """\
.method removeActiveAdminLocked(Landroid/content/ComponentName;I)V
    .registers 7

    goto :goto_15

    nop

    :goto_0
    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_1

    nop

    :goto_1
    const-string v3, " for user "

    goto :goto_13

    nop

    :goto_2
    iget-object v2, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mRemovingAdmins:Ljava/util/ArrayList;

    goto :goto_4

    nop

    :goto_3
    invoke-direct {v2, p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$4;-><init>(Lcom/android/server/devicepolicy/DevicePolicyManagerService;Landroid/content/ComponentName;I)V

    goto :goto_a

    nop

    :goto_4
    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v2

    goto :goto_1b

    nop

    :goto_5
    const-string v2, "removeActiveAdminLocked"

    goto :goto_16

    nop

    :goto_6
    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    goto :goto_b

    nop

    :goto_7
    return-void

    :goto_8
    invoke-virtual {p0, v0, v3, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/content/BroadcastReceiver;)V

    :goto_9
    goto :goto_7

    nop

    :goto_a
    const-string v3, "android.app.action.DEVICE_ADMIN_DISABLED"

    goto :goto_8

    nop

    :goto_b
    const-string v3, "DevicePolicyManager"

    goto :goto_10

    nop

    :goto_c
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_0

    nop

    :goto_d
    iget-object v2, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mRemovingAdmins:Ljava/util/ArrayList;

    goto :goto_e

    nop

    :goto_e
    invoke-virtual {v2, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_1c

    nop

    :goto_f
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_6

    nop

    :goto_10
    invoke-static {v3, v2}, Lcom/android/server/utils/Slogf;->d(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_5

    nop

    :goto_11
    const-string v3, " to list of removing admins."

    goto :goto_f

    nop

    :goto_12
    if-nez v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_2

    nop

    :goto_13
    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_1a

    nop

    :goto_14
    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_19

    nop

    :goto_15
    invoke-virtual {p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminUncheckedLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v0

    goto :goto_17

    nop

    :goto_16
    invoke-direct {p0, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->logStackTrace(Ljava/lang/String;)V

    goto :goto_d

    nop

    :goto_17
    invoke-virtual {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v1

    goto :goto_12

    nop

    :goto_18
    new-instance v2, Ljava/lang/StringBuilder;

    goto :goto_14

    nop

    :goto_19
    const-string v3, "Adding "

    goto :goto_c

    nop

    :goto_1a
    invoke-virtual {v2, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v2

    goto :goto_11

    nop

    :goto_1b
    if-eqz v2, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_18

    nop

    :goto_1c
    new-instance v2, Lcom/android/server/devicepolicy/DevicePolicyManagerService$4;

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getActiveAdminUncheckedLocked(Landroid/content/ComponentName;I)Lcom/android/server/devicepolicy/ActiveAdmin;', 'move-result-object v0', 'invoke-virtual {p0, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;', 'move-result-object v1', 'if-eqz v0, :cond_0', 'iget-object v2, v1, Lcom/android/server/devicepolicy/DevicePolicyData;->mRemovingAdmins:Ljava/util/ArrayList;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_removeCrossProfileIntentFilter_Lcom_android_server_pm_Defaul",
        "method":      ".method removeCrossProfileIntentFilter(Lcom/android/server/pm/DefaultCrossProfileIntentFilter;II)Z",
        "method_name": 'removeCrossProfileIntentFilter',
        "type":        "method_replace",
        "search": """\
.method removeCrossProfileIntentFilter(Lcom/android/server/pm/DefaultCrossProfileIntentFilter;II)Z
    .registers 12
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Landroid/os/RemoteException;
        }
    .end annotation

    iget v0, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->direction:I

    const/4 v1, 0x1

    if-ne v0, v1, :cond_0

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIPackageManager:Landroid/content/pm/IPackageManager;

    iget-object v0, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->filter:Lcom/android/server/pm/WatchedIntentFilter;

    invoke-virtual {v0}, Lcom/android/server/pm/WatchedIntentFilter;->getIntentFilter()Landroid/content/IntentFilter;

    move-result-object v3

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v0}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v4

    iget v7, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->flags:I

    move v5, p2

    move v6, p3

    invoke-interface/range {v2 .. v7}, Landroid/content/pm/IPackageManager;->removeCrossProfileIntentFilter(Landroid/content/IntentFilter;Ljava/lang/String;III)Z

    move-result p2

    move v4, v5

    move v3, v6

    return p2

    :cond_0
    move v4, p2

    move v3, p3

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIPackageManager:Landroid/content/pm/IPackageManager;

    iget-object p2, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->filter:Lcom/android/server/pm/WatchedIntentFilter;

    invoke-virtual {p2}, Lcom/android/server/pm/WatchedIntentFilter;->getIntentFilter()Landroid/content/IntentFilter;

    move-result-object v1

    iget-object p2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {p2}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v2

    iget v5, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->flags:I

    invoke-interface/range {v0 .. v5}, Landroid/content/pm/IPackageManager;->removeCrossProfileIntentFilter(Landroid/content/IntentFilter;Ljava/lang/String;III)Z

    move-result p2

    return p2
.end method
""",
        "replacement": """\
.method removeCrossProfileIntentFilter(Lcom/android/server/pm/DefaultCrossProfileIntentFilter;II)Z
    .registers 12
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Landroid/os/RemoteException;
        }
    .end annotation

    goto :goto_3

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    goto :goto_17

    nop

    :goto_1
    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIPackageManager:Landroid/content/pm/IPackageManager;

    goto :goto_2

    nop

    :goto_2
    iget-object v0, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->filter:Lcom/android/server/pm/WatchedIntentFilter;

    goto :goto_19

    nop

    :goto_3
    iget v0, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->direction:I

    goto :goto_5

    nop

    :goto_4
    invoke-virtual {p2}, Lcom/android/server/pm/WatchedIntentFilter;->getIntentFilter()Landroid/content/IntentFilter;

    move-result-object v1

    goto :goto_7

    nop

    :goto_5
    const/4 v1, 0x1

    goto :goto_14

    nop

    :goto_6
    invoke-interface/range {v0 .. v5}, Landroid/content/pm/IPackageManager;->removeCrossProfileIntentFilter(Landroid/content/IntentFilter;Ljava/lang/String;III)Z

    move-result p2

    goto :goto_18

    nop

    :goto_7
    iget-object p2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    goto :goto_8

    nop

    :goto_8
    invoke-virtual {p2}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v2

    goto :goto_15

    nop

    :goto_9
    iget-object p2, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->filter:Lcom/android/server/pm/WatchedIntentFilter;

    goto :goto_4

    nop

    :goto_a
    move v4, p2

    goto :goto_b

    nop

    :goto_b
    move v3, p3

    goto :goto_10

    nop

    :goto_c
    move v5, p2

    goto :goto_f

    nop

    :goto_d
    return p2

    :goto_e
    goto :goto_a

    nop

    :goto_f
    move v6, p3

    goto :goto_11

    nop

    :goto_10
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIPackageManager:Landroid/content/pm/IPackageManager;

    goto :goto_9

    nop

    :goto_11
    invoke-interface/range {v2 .. v7}, Landroid/content/pm/IPackageManager;->removeCrossProfileIntentFilter(Landroid/content/IntentFilter;Ljava/lang/String;III)Z

    move-result p2

    goto :goto_12

    nop

    :goto_12
    move v4, v5

    goto :goto_13

    nop

    :goto_13
    move v3, v6

    goto :goto_d

    nop

    :goto_14
    if-eq v0, v1, :cond_0

    goto :goto_e

    :cond_0
    goto :goto_1

    nop

    :goto_15
    iget v5, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->flags:I

    goto :goto_6

    nop

    :goto_16
    iget v7, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->flags:I

    goto :goto_c

    nop

    :goto_17
    invoke-virtual {v0}, Landroid/content/Context;->getOpPackageName()Ljava/lang/String;

    move-result-object v4

    goto :goto_16

    nop

    :goto_18
    return p2

    :goto_19
    invoke-virtual {v0}, Lcom/android/server/pm/WatchedIntentFilter;->getIntentFilter()Landroid/content/IntentFilter;

    move-result-object v3

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget v0, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->direction:I', 'if-ne v0, v1, :cond_0', 'iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIPackageManager:Landroid/content/pm/IPackageManager;', 'iget-object v0, p1, Lcom/android/server/pm/DefaultCrossProfileIntentFilter;->filter:Lcom/android/server/pm/WatchedIntentFilter;', 'invoke-virtual {v0}, Lcom/android/server/pm/WatchedIntentFilter;->getIntentFilter()Landroid/content/IntentFilter;', 'move-result-object v3'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_removeUserData_I_V",
        "method":      ".method removeUserData(I)V",
        "method_name": 'removeUserData',
        "type":        "method_replace",
        "search": """\
.method removeUserData(I)V
    .registers 10

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    if-nez p1, :cond_0

    :try_start_0
    const-string v1, "DevicePolicyManager"

    const-string v2, "Tried to remove device policy file for user 0! Ignoring."

    invoke-static {v1, v2}, Lcom/android/server/utils/Slogf;->w(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0

    return-void

    :cond_0
    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updatePasswordQualityCacheForUserGroup(I)V

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPolicyCache:Lcom/android/server/devicepolicy/DevicePolicyCacheImpl;

    invoke-virtual {v1, p1}, Lcom/android/server/devicepolicy/DevicePolicyCacheImpl;->onUserRemoved(I)V

    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isManagedProfile(I)Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->clearManagedProfileApnUnchecked()V

    :cond_1
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v1, p1}, Lcom/android/server/devicepolicy/Owners;->isProfileOwnerOfOrganizationOwnedDevice(I)Z

    move-result v1

    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v2

    if-eqz v2, :cond_2

    const/4 v3, 0x0

    iput-object v3, v2, Lcom/android/server/devicepolicy/ActiveAdmin;->userRestrictions:Landroid/os/Bundle;

    invoke-virtual {v2}, Lcom/android/server/devicepolicy/ActiveAdmin;->getParentActiveAdmin()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v4

    if-eqz v4, :cond_2

    iput-object v3, v4, Lcom/android/server/devicepolicy/ActiveAdmin;->userRestrictions:Landroid/os/Bundle;

    :cond_2
    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v3, p1}, Lcom/android/server/devicepolicy/Owners;->removeProfileOwner(I)V

    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v3, p1}, Lcom/android/server/devicepolicy/Owners;->writeProfileOwner(I)V

    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserData:Landroid/util/SparseArray;

    invoke-virtual {v3, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lcom/android/server/devicepolicy/DevicePolicyData;

    if-eqz v3, :cond_3

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserData:Landroid/util/SparseArray;

    invoke-virtual {v4, p1}, Landroid/util/SparseArray;->remove(I)V

    :cond_3
    new-instance v4, Ljava/io/File;

    iget-object v5, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPathProvider:Lcom/android/server/devicepolicy/PolicyPathProvider;

    invoke-interface {v5, p1}, Lcom/android/server/devicepolicy/PolicyPathProvider;->getUserSystemDirectory(I)Ljava/io/File;

    move-result-object v5

    const-string v6, "device_policies.xml"

    invoke-direct {v4, v5, v6}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V

    invoke-virtual {v4}, Ljava/io/File;->delete()Z

    const-string v5, "DevicePolicyManager"

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "Removed device policy file "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v4}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v5, v6}, Lcom/android/server/utils/Slogf;->i(Ljava/lang/String;Ljava/lang/String;)I

    nop

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    if-eqz v1, :cond_5

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserManager:Landroid/os/UserManager;

    invoke-virtual {v0}, Landroid/os/UserManager;->getPrimaryUser()Landroid/content/pm/UserInfo;

    move-result-object v0

    if-eqz v0, :cond_4

    iget v2, v0, Landroid/content/pm/UserInfo;->id:I

    invoke-direct {p0, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->clearOrgOwnedProfileOwnerDeviceWidePolicies(I)V

    goto :goto_0

    :cond_4
    const-string v2, "DevicePolicyManager"

    const-string v3, "Was unable to get primary user."

    invoke-static {v2, v3}, Lcom/android/server/utils/Slogf;->wtf(Ljava/lang/String;Ljava/lang/String;)I

    :cond_5
    :goto_0
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method removeUserData(I)V
    .registers 10

    goto :goto_f

    nop

    :goto_0
    if-eqz p1, :cond_0

    goto :goto_1

    :cond_0
    :try_start_0
    const-string v1, "DevicePolicyManager"

    const-string v2, "Tried to remove device policy file for user 0! Ignoring."

    invoke-static {v1, v2}, Lcom/android/server/utils/Slogf;->w(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0

    return-void

    :goto_1
    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->updatePasswordQualityCacheForUserGroup(I)V

    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPolicyCache:Lcom/android/server/devicepolicy/DevicePolicyCacheImpl;

    invoke-virtual {v1, p1}, Lcom/android/server/devicepolicy/DevicePolicyCacheImpl;->onUserRemoved(I)V

    invoke-direct {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isManagedProfile(I)Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->clearManagedProfileApnUnchecked()V

    :cond_1
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v1, p1}, Lcom/android/server/devicepolicy/Owners;->isProfileOwnerOfOrganizationOwnedDevice(I)Z

    move-result v1

    invoke-virtual {p0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileOwnerLocked(I)Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v2

    if-eqz v2, :cond_2

    const/4 v3, 0x0

    iput-object v3, v2, Lcom/android/server/devicepolicy/ActiveAdmin;->userRestrictions:Landroid/os/Bundle;

    invoke-virtual {v2}, Lcom/android/server/devicepolicy/ActiveAdmin;->getParentActiveAdmin()Lcom/android/server/devicepolicy/ActiveAdmin;

    move-result-object v4

    if-eqz v4, :cond_2

    iput-object v3, v4, Lcom/android/server/devicepolicy/ActiveAdmin;->userRestrictions:Landroid/os/Bundle;

    :cond_2
    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v3, p1}, Lcom/android/server/devicepolicy/Owners;->removeProfileOwner(I)V

    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v3, p1}, Lcom/android/server/devicepolicy/Owners;->writeProfileOwner(I)V

    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserData:Landroid/util/SparseArray;

    invoke-virtual {v3, p1}, Landroid/util/SparseArray;->get(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lcom/android/server/devicepolicy/DevicePolicyData;

    if-eqz v3, :cond_3

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserData:Landroid/util/SparseArray;

    invoke-virtual {v4, p1}, Landroid/util/SparseArray;->remove(I)V

    :cond_3
    new-instance v4, Ljava/io/File;

    iget-object v5, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPathProvider:Lcom/android/server/devicepolicy/PolicyPathProvider;

    invoke-interface {v5, p1}, Lcom/android/server/devicepolicy/PolicyPathProvider;->getUserSystemDirectory(I)Ljava/io/File;

    move-result-object v5

    const-string v6, "device_policies.xml"

    invoke-direct {v4, v5, v6}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V

    invoke-virtual {v4}, Ljava/io/File;->delete()Z

    const-string v5, "DevicePolicyManager"

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "Removed device policy file "

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v4}, Ljava/io/File;->getAbsolutePath()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v5, v6}, Lcom/android/server/utils/Slogf;->i(Ljava/lang/String;Ljava/lang/String;)I

    nop

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_c

    nop

    :goto_2
    invoke-virtual {v0}, Landroid/os/UserManager;->getPrimaryUser()Landroid/content/pm/UserInfo;

    move-result-object v0

    goto :goto_a

    nop

    :goto_3
    monitor-enter v0

    goto :goto_0

    nop

    :goto_4
    const-string v3, "Was unable to get primary user."

    goto :goto_6

    nop

    :goto_5
    const-string v2, "DevicePolicyManager"

    goto :goto_4

    nop

    :goto_6
    invoke-static {v2, v3}, Lcom/android/server/utils/Slogf;->wtf(Ljava/lang/String;Ljava/lang/String;)I

    :goto_7
    goto :goto_e

    nop

    :goto_8
    goto :goto_7

    :goto_9
    goto :goto_5

    nop

    :goto_a
    if-nez v0, :cond_4

    goto :goto_9

    :cond_4
    goto :goto_d

    nop

    :goto_b
    throw v1

    :goto_c
    if-nez v1, :cond_5

    goto :goto_7

    :cond_5
    goto :goto_10

    nop

    :goto_d
    iget v2, v0, Landroid/content/pm/UserInfo;->id:I

    goto :goto_11

    nop

    :goto_e
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_b

    nop

    :goto_f
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_3

    nop

    :goto_10
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserManager:Landroid/os/UserManager;

    goto :goto_2

    nop

    :goto_11
    invoke-direct {p0, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->clearOrgOwnedProfileOwnerDeviceWidePolicies(I)V

    goto :goto_8

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;', 'move-result-object v0', 'if-nez p1, :cond_0', 'const-string v1, "DevicePolicyManager"', 'const-string v2, "Tried to remove device policy file for user 0! Ignoring."', 'invoke-static {v1, v2}, Lcom/android/server/utils/Slogf;->w(Ljava/lang/String;Ljava/lang/String;)I'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_saveTransferOwnershipBundleLocked_Landroid_os_PersistableBun",
        "method":      ".method saveTransferOwnershipBundleLocked(Landroid/os/PersistableBundle;I)V",
        "method_name": 'saveTransferOwnershipBundleLocked',
        "type":        "method_replace",
        "search": """\
.method saveTransferOwnershipBundleLocked(Landroid/os/PersistableBundle;I)V
    .registers 10

    const-string v0, "transfer-ownership-bundle"

    new-instance v1, Ljava/io/File;

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPathProvider:Lcom/android/server/devicepolicy/PolicyPathProvider;

    invoke-interface {v2, p2}, Lcom/android/server/devicepolicy/PolicyPathProvider;->getUserSystemDirectory(I)Ljava/io/File;

    move-result-object v2

    const-string v3, "transfer-ownership-parameters.xml"

    invoke-direct {v1, v2, v3}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V

    new-instance v2, Landroid/util/AtomicFile;

    invoke-direct {v2, v1}, Landroid/util/AtomicFile;-><init>(Ljava/io/File;)V

    const/4 v3, 0x0

    :try_start_0
    invoke-virtual {v2}, Landroid/util/AtomicFile;->startWrite()Ljava/io/FileOutputStream;

    move-result-object v4

    move-object v3, v4

    invoke-static {v3}, Landroid/util/Xml;->resolveSerializer(Ljava/io/OutputStream;)Lcom/android/modules/utils/TypedXmlSerializer;

    move-result-object v4

    const/4 v5, 0x1

    invoke-static {v5}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v5

    const/4 v6, 0x0

    invoke-interface {v4, v6, v5}, Lcom/android/modules/utils/TypedXmlSerializer;->startDocument(Ljava/lang/String;Ljava/lang/Boolean;)V

    invoke-interface {v4, v6, v0}, Lcom/android/modules/utils/TypedXmlSerializer;->startTag(Ljava/lang/String;Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;

    invoke-virtual {p1, v4}, Landroid/os/PersistableBundle;->saveToXml(Lcom/android/modules/utils/TypedXmlSerializer;)V

    invoke-interface {v4, v6, v0}, Lcom/android/modules/utils/TypedXmlSerializer;->endTag(Ljava/lang/String;Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;

    invoke-interface {v4}, Lcom/android/modules/utils/TypedXmlSerializer;->endDocument()V

    invoke-virtual {v2, v3}, Landroid/util/AtomicFile;->finishWrite(Ljava/io/FileOutputStream;)V
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_0
    .catch Lorg/xmlpull/v1/XmlPullParserException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_0

    :catch_0
    move-exception v0

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v5, "Caught exception while trying to save the owner transfer parameters to file "

    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    const-string v5, "DevicePolicyManager"

    invoke-static {v5, v4, v0}, Lcom/android/server/utils/Slogf;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    invoke-virtual {v1}, Ljava/io/File;->delete()Z

    invoke-virtual {v2, v3}, Landroid/util/AtomicFile;->failWrite(Ljava/io/FileOutputStream;)V

    :goto_0
    return-void
.end method
""",
        "replacement": """\
.method saveTransferOwnershipBundleLocked(Landroid/os/PersistableBundle;I)V
    .registers 10

    goto :goto_6

    nop

    :goto_0
    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    goto :goto_14

    nop

    :goto_1
    invoke-virtual {v1}, Ljava/io/File;->delete()Z

    goto :goto_12

    nop

    :goto_2
    const/4 v3, 0x0

    :try_start_0
    invoke-virtual {v2}, Landroid/util/AtomicFile;->startWrite()Ljava/io/FileOutputStream;

    move-result-object v4

    move-object v3, v4

    invoke-static {v3}, Landroid/util/Xml;->resolveSerializer(Ljava/io/OutputStream;)Lcom/android/modules/utils/TypedXmlSerializer;

    move-result-object v4

    const/4 v5, 0x1

    invoke-static {v5}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v5

    const/4 v6, 0x0

    invoke-interface {v4, v6, v5}, Lcom/android/modules/utils/TypedXmlSerializer;->startDocument(Ljava/lang/String;Ljava/lang/Boolean;)V

    invoke-interface {v4, v6, v0}, Lcom/android/modules/utils/TypedXmlSerializer;->startTag(Ljava/lang/String;Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;

    invoke-virtual {p1, v4}, Landroid/os/PersistableBundle;->saveToXml(Lcom/android/modules/utils/TypedXmlSerializer;)V

    invoke-interface {v4, v6, v0}, Lcom/android/modules/utils/TypedXmlSerializer;->endTag(Ljava/lang/String;Ljava/lang/String;)Lorg/xmlpull/v1/XmlSerializer;

    invoke-interface {v4}, Lcom/android/modules/utils/TypedXmlSerializer;->endDocument()V

    invoke-virtual {v2, v3}, Landroid/util/AtomicFile;->finishWrite(Ljava/io/FileOutputStream;)V
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_0
    .catch Lorg/xmlpull/v1/XmlPullParserException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_10

    nop

    :goto_3
    invoke-direct {v2, v1}, Landroid/util/AtomicFile;-><init>(Ljava/io/File;)V

    goto :goto_2

    nop

    :goto_4
    invoke-virtual {v4, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v4

    goto :goto_0

    nop

    :goto_5
    invoke-direct {v1, v2, v3}, Ljava/io/File;-><init>(Ljava/io/File;Ljava/lang/String;)V

    goto :goto_a

    nop

    :goto_6
    const-string v0, "transfer-ownership-bundle"

    goto :goto_15

    nop

    :goto_7
    new-instance v4, Ljava/lang/StringBuilder;

    goto :goto_f

    nop

    :goto_8
    const-string v5, "Caught exception while trying to save the owner transfer parameters to file "

    goto :goto_9

    nop

    :goto_9
    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    goto :goto_4

    nop

    :goto_a
    new-instance v2, Landroid/util/AtomicFile;

    goto :goto_3

    nop

    :goto_b
    return-void

    :goto_c
    invoke-static {v5, v4, v0}, Lcom/android/server/utils/Slogf;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    goto :goto_1

    nop

    :goto_d
    invoke-interface {v2, p2}, Lcom/android/server/devicepolicy/PolicyPathProvider;->getUserSystemDirectory(I)Ljava/io/File;

    move-result-object v2

    goto :goto_11

    nop

    :goto_e
    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPathProvider:Lcom/android/server/devicepolicy/PolicyPathProvider;

    goto :goto_d

    nop

    :goto_f
    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_8

    nop

    :goto_10
    goto :goto_13

    :catch_0
    move-exception v0

    goto :goto_7

    nop

    :goto_11
    const-string v3, "transfer-ownership-parameters.xml"

    goto :goto_5

    nop

    :goto_12
    invoke-virtual {v2, v3}, Landroid/util/AtomicFile;->failWrite(Ljava/io/FileOutputStream;)V

    :goto_13
    goto :goto_b

    nop

    :goto_14
    const-string v5, "DevicePolicyManager"

    goto :goto_c

    nop

    :goto_15
    new-instance v1, Ljava/io/File;

    goto :goto_e

    nop
.end method
""",
        "method_anchors": ['const-string v0, "transfer-ownership-bundle"', 'new-instance v1, Ljava/io/File;', 'iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mPathProvider:Lcom/android/server/devicepolicy/PolicyPathProvider;', 'invoke-interface {v2, p2}, Lcom/android/server/devicepolicy/PolicyPathProvider;->getUserSystemDirectory(I)Ljava/io/File;', 'move-result-object v2', 'const-string v3, "transfer-ownership-parameters.xml"'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_sendAdminCommandLocked_Lcom_android_server_devicepolicy_Acti",
        "method":      ".method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;)V",
        "method_name": 'sendAdminCommandLocked',
        "type":        "method_replace",
        "search": """\
.method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;)V
    .registers 4

    const/4 v0, 0x0

    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/content/BroadcastReceiver;)V

    return-void
.end method
""",
        "replacement": """\
.method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/content/BroadcastReceiver;)V

    goto :goto_2

    nop

    :goto_1
    const/4 v0, 0x0

    goto :goto_0

    nop

    :goto_2
    return-void
.end method
""",
        "method_anchors": ['invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/content/BroadcastReceiver;)V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_sendAdminCommandLocked_Lcom_android_server_devicepolicy_Acti",
        "method":      ".method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/content/BroadcastReceiver;)V",
        "method_name": 'sendAdminCommandLocked',
        "type":        "method_replace",
        "search": """\
.method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/content/BroadcastReceiver;)V
    .registers 5

    const/4 v0, 0x0

    invoke-virtual {p0, p1, p2, v0, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;)V

    return-void
.end method
""",
        "replacement": """\
.method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/content/BroadcastReceiver;)V
    .registers 5

    goto :goto_2

    nop

    :goto_0
    return-void

    :goto_1
    invoke-virtual {p0, p1, p2, v0, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;)V

    goto :goto_0

    nop

    :goto_2
    const/4 v0, 0x0

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0, p1, p2, v0, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;)V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_sendAdminCommandLocked_Lcom_android_server_devicepolicy_Acti",
        "method":      ".method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;)V",
        "method_name": 'sendAdminCommandLocked',
        "type":        "method_replace",
        "search": """\
.method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;)V
    .registers 11

    const/4 v5, 0x0

    move-object v0, p0

    move-object v1, p1

    move-object v2, p2

    move-object v3, p3

    move-object v4, p4

    invoke-virtual/range {v0 .. v5}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;Z)Z

    return-void
.end method
""",
        "replacement": """\
.method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;)V
    .registers 11

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    const/4 v5, 0x0

    goto :goto_3

    nop

    :goto_2
    move-object v3, p3

    goto :goto_4

    nop

    :goto_3
    move-object v0, p0

    goto :goto_7

    nop

    :goto_4
    move-object v4, p4

    goto :goto_6

    nop

    :goto_5
    move-object v2, p2

    goto :goto_2

    nop

    :goto_6
    invoke-virtual/range {v0 .. v5}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;Z)Z

    goto :goto_0

    nop

    :goto_7
    move-object v1, p1

    goto :goto_5

    nop
.end method
""",
        "method_anchors": ['invoke-virtual/range {v0 .. v5}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;Z)Z', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_sendAdminCommandLocked_Ljava_lang_String_IILandroid_os_Bundl",
        "method":      ".method sendAdminCommandLocked(Ljava/lang/String;IILandroid/os/Bundle;)V",
        "method_name": 'sendAdminCommandLocked',
        "type":        "method_replace",
        "search": """\
.method sendAdminCommandLocked(Ljava/lang/String;IILandroid/os/Bundle;)V
    .registers 10

    invoke-virtual {p0, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v0

    iget-object v1, v0, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->size()I

    move-result v1

    const/4 v2, 0x0

    :goto_0
    if-ge v2, v1, :cond_1

    iget-object v3, v0, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    invoke-virtual {v3, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Lcom/android/server/devicepolicy/ActiveAdmin;

    iget-object v4, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v4, p2}, Landroid/app/admin/DeviceAdminInfo;->usesPolicy(I)Z

    move-result v4

    if-eqz v4, :cond_0

    const/4 v4, 0x0

    invoke-virtual {p0, v3, p1, p4, v4}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;)V

    :cond_0
    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_1
    return-void
.end method
""",
        "replacement": """\
.method sendAdminCommandLocked(Ljava/lang/String;IILandroid/os/Bundle;)V
    .registers 10

    goto :goto_12

    nop

    :goto_0
    if-nez v4, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_8

    nop

    :goto_1
    check-cast v3, Lcom/android/server/devicepolicy/ActiveAdmin;

    goto :goto_a

    nop

    :goto_2
    invoke-virtual {v1}, Ljava/util/ArrayList;->size()I

    move-result v1

    goto :goto_4

    nop

    :goto_3
    invoke-virtual {v3, v2}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v3

    goto :goto_1

    nop

    :goto_4
    const/4 v2, 0x0

    :goto_5
    goto :goto_c

    nop

    :goto_6
    goto :goto_5

    :goto_7
    goto :goto_f

    nop

    :goto_8
    const/4 v4, 0x0

    goto :goto_10

    nop

    :goto_9
    iget-object v1, v0, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    goto :goto_2

    nop

    :goto_a
    iget-object v4, v3, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_e

    nop

    :goto_b
    add-int/lit8 v2, v2, 0x1

    goto :goto_6

    nop

    :goto_c
    if-lt v2, v1, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_d

    nop

    :goto_d
    iget-object v3, v0, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;

    goto :goto_3

    nop

    :goto_e
    invoke-virtual {v4, p2}, Landroid/app/admin/DeviceAdminInfo;->usesPolicy(I)Z

    move-result v4

    goto :goto_0

    nop

    :goto_f
    return-void

    :goto_10
    invoke-virtual {p0, v3, p1, p4, v4}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;)V

    :goto_11
    goto :goto_b

    nop

    :goto_12
    invoke-virtual {p0, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v0

    goto :goto_9

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0, p3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;', 'move-result-object v0', 'iget-object v1, v0, Lcom/android/server/devicepolicy/DevicePolicyData;->mAdminList:Ljava/util/ArrayList;', 'invoke-virtual {v1}, Ljava/util/ArrayList;->size()I', 'move-result v1', 'if-ge v2, v1, :cond_1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_sendAdminCommandLocked_Lcom_android_server_devicepolicy_Acti",
        "method":      ".method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;Z)Z",
        "method_name": 'sendAdminCommandLocked',
        "type":        "method_replace",
        "search": """\
.method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;Z)Z
    .registers 23

    move-object/from16 v0, p0

    move-object/from16 v1, p1

    move-object/from16 v2, p2

    move-object/from16 v3, p3

    new-instance v4, Landroid/content/Intent;

    invoke-direct {v4, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    move-object v6, v4

    iget-object v4, v1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    invoke-virtual {v4}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v4

    invoke-virtual {v6, v4}, Landroid/content/Intent;->setComponent(Landroid/content/ComponentName;)Landroid/content/Intent;

    iget-object v4, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    invoke-static {v4}, Landroid/os/UserManager;->isDeviceInDemoMode(Landroid/content/Context;)Z

    move-result v4

    const/high16 v5, 0x10000000

    if-eqz v4, :cond_0

    invoke-virtual {v6, v5}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    :cond_0
    const-string v4, "android.app.action.ACTION_PASSWORD_EXPIRING"

    invoke-virtual {v2, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_1

    const-string v4, "expiration"

    iget-wide v7, v1, Lcom/android/server/devicepolicy/ActiveAdmin;->passwordExpirationDate:J

    invoke-virtual {v6, v4, v7, v8}, Landroid/content/Intent;->putExtra(Ljava/lang/String;J)Landroid/content/Intent;

    :cond_1
    if-eqz p5, :cond_2

    invoke-virtual {v6, v5}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    :cond_2
    if-eqz v3, :cond_3

    invoke-virtual {v6, v3}, Landroid/content/Intent;->putExtras(Landroid/os/Bundle;)Landroid/content/Intent;

    :cond_3
    iget-object v4, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    invoke-virtual {v4}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v4

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUserHandle()Landroid/os/UserHandle;

    move-result-object v7

    invoke-virtual {v4, v6, v5, v7}, Landroid/content/pm/PackageManager;->queryBroadcastReceiversAsUser(Landroid/content/Intent;ILandroid/os/UserHandle;)Ljava/util/List;

    move-result-object v4

    invoke-interface {v4}, Ljava/util/List;->isEmpty()Z

    move-result v4

    if-eqz v4, :cond_4

    const/4 v4, 0x0

    return v4

    :cond_4
    invoke-static {}, Landroid/app/BroadcastOptions;->makeBasic()Landroid/app/BroadcastOptions;

    move-result-object v4

    const/4 v5, 0x1

    invoke-virtual {v4, v5}, Landroid/app/BroadcastOptions;->setBackgroundActivityStartsAllowed(Z)V

    if-eqz p4, :cond_5

    move v7, v5

    iget-object v5, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    move v8, v7

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUserHandle()Landroid/os/UserHandle;

    move-result-object v7

    invoke-virtual {v4}, Landroid/app/BroadcastOptions;->toBundle()Landroid/os/Bundle;

    move-result-object v10

    iget-object v12, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHandler:Landroid/os/Handler;

    move v9, v8

    const/4 v8, 0x0

    move v11, v9

    const/4 v9, -0x1

    const/4 v13, -0x1

    const/4 v14, 0x0

    const/4 v15, 0x0

    move/from16 v16, v11

    move-object/from16 v11, p4

    invoke-virtual/range {v5 .. v15}, Landroid/content/Context;->sendOrderedBroadcastAsUser(Landroid/content/Intent;Landroid/os/UserHandle;Ljava/lang/String;ILandroid/os/Bundle;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)V

    goto :goto_0

    :cond_5
    move/from16 v16, v5

    iget-object v5, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUserHandle()Landroid/os/UserHandle;

    move-result-object v7

    const/4 v8, 0x0

    invoke-virtual {v4}, Landroid/app/BroadcastOptions;->toBundle()Landroid/os/Bundle;

    move-result-object v9

    invoke-virtual {v5, v6, v7, v8, v9}, Landroid/content/Context;->sendBroadcastAsUser(Landroid/content/Intent;Landroid/os/UserHandle;Ljava/lang/String;Landroid/os/Bundle;)V

    :goto_0
    return v16
.end method
""",
        "replacement": """\
.method sendAdminCommandLocked(Lcom/android/server/devicepolicy/ActiveAdmin;Ljava/lang/String;Landroid/os/Bundle;Landroid/content/BroadcastReceiver;Z)Z
    .registers 23

    goto :goto_3e

    nop

    :goto_0
    const-string v4, "android.app.action.ACTION_PASSWORD_EXPIRING"

    goto :goto_28

    nop

    :goto_1
    invoke-virtual {v4}, Landroid/app/BroadcastOptions;->toBundle()Landroid/os/Bundle;

    move-result-object v9

    goto :goto_38

    nop

    :goto_2
    invoke-virtual {v6, v5}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    :goto_3
    goto :goto_0

    nop

    :goto_4
    if-nez v4, :cond_0

    goto :goto_1a

    :cond_0
    goto :goto_5

    nop

    :goto_5
    const/4 v4, 0x0

    goto :goto_19

    nop

    :goto_6
    if-nez p5, :cond_1

    goto :goto_43

    :cond_1
    goto :goto_42

    nop

    :goto_7
    if-nez v4, :cond_2

    goto :goto_3

    :cond_2
    goto :goto_2

    nop

    :goto_8
    invoke-virtual/range {v5 .. v15}, Landroid/content/Context;->sendOrderedBroadcastAsUser(Landroid/content/Intent;Landroid/os/UserHandle;Ljava/lang/String;ILandroid/os/Bundle;Landroid/content/BroadcastReceiver;Landroid/os/Handler;ILjava/lang/String;Landroid/os/Bundle;)V

    goto :goto_20

    nop

    :goto_9
    invoke-virtual {v6, v4, v7, v8}, Landroid/content/Intent;->putExtra(Ljava/lang/String;J)Landroid/content/Intent;

    :goto_a
    goto :goto_6

    nop

    :goto_b
    const/4 v8, 0x0

    goto :goto_11

    nop

    :goto_c
    move/from16 v16, v5

    goto :goto_13

    nop

    :goto_d
    iget-wide v7, v1, Lcom/android/server/devicepolicy/ActiveAdmin;->passwordExpirationDate:J

    goto :goto_9

    nop

    :goto_e
    invoke-virtual {v6, v3}, Landroid/content/Intent;->putExtras(Landroid/os/Bundle;)Landroid/content/Intent;

    :goto_f
    goto :goto_23

    nop

    :goto_10
    new-instance v4, Landroid/content/Intent;

    goto :goto_37

    nop

    :goto_11
    move v11, v9

    goto :goto_2a

    nop

    :goto_12
    invoke-virtual {v4, v5}, Landroid/app/BroadcastOptions;->setBackgroundActivityStartsAllowed(Z)V

    goto :goto_35

    nop

    :goto_13
    iget-object v5, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    goto :goto_34

    nop

    :goto_14
    move-object/from16 v3, p3

    goto :goto_10

    nop

    :goto_15
    invoke-virtual {v4}, Landroid/app/BroadcastOptions;->toBundle()Landroid/os/Bundle;

    move-result-object v10

    goto :goto_25

    nop

    :goto_16
    move v7, v5

    goto :goto_3b

    nop

    :goto_17
    move-object v6, v4

    goto :goto_2b

    nop

    :goto_18
    invoke-virtual {v1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUserHandle()Landroid/os/UserHandle;

    move-result-object v7

    goto :goto_3f

    nop

    :goto_19
    return v4

    :goto_1a
    goto :goto_1d

    nop

    :goto_1b
    if-nez v3, :cond_3

    goto :goto_f

    :cond_3
    goto :goto_e

    nop

    :goto_1c
    const/high16 v5, 0x10000000

    goto :goto_7

    nop

    :goto_1d
    invoke-static {}, Landroid/app/BroadcastOptions;->makeBasic()Landroid/app/BroadcastOptions;

    move-result-object v4

    goto :goto_1f

    nop

    :goto_1e
    move v8, v7

    goto :goto_3a

    nop

    :goto_1f
    const/4 v5, 0x1

    goto :goto_12

    nop

    :goto_20
    goto :goto_39

    :goto_21
    goto :goto_c

    nop

    :goto_22
    invoke-virtual {v4}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;

    move-result-object v4

    goto :goto_41

    nop

    :goto_23
    iget-object v4, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_2f

    nop

    :goto_24
    const/4 v15, 0x0

    goto :goto_26

    nop

    :goto_25
    iget-object v12, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHandler:Landroid/os/Handler;

    goto :goto_3d

    nop

    :goto_26
    move/from16 v16, v11

    goto :goto_30

    nop

    :goto_27
    if-nez v4, :cond_4

    goto :goto_a

    :cond_4
    goto :goto_2e

    nop

    :goto_28
    invoke-virtual {v2, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    goto :goto_27

    nop

    :goto_29
    move-object/from16 v2, p2

    goto :goto_14

    nop

    :goto_2a
    const/4 v9, -0x1

    goto :goto_32

    nop

    :goto_2b
    iget-object v4, v1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;

    goto :goto_22

    nop

    :goto_2c
    invoke-static {v4}, Landroid/os/UserManager;->isDeviceInDemoMode(Landroid/content/Context;)Z

    move-result v4

    goto :goto_1c

    nop

    :goto_2d
    return v16

    :goto_2e
    const-string v4, "expiration"

    goto :goto_d

    nop

    :goto_2f
    invoke-virtual {v4}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v4

    goto :goto_18

    nop

    :goto_30
    move-object/from16 v11, p4

    goto :goto_8

    nop

    :goto_31
    const/4 v14, 0x0

    goto :goto_24

    nop

    :goto_32
    const/4 v13, -0x1

    goto :goto_31

    nop

    :goto_33
    iget-object v4, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    goto :goto_2c

    nop

    :goto_34
    invoke-virtual {v1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUserHandle()Landroid/os/UserHandle;

    move-result-object v7

    goto :goto_3c

    nop

    :goto_35
    if-nez p4, :cond_5

    goto :goto_21

    :cond_5
    goto :goto_16

    nop

    :goto_36
    move-object/from16 v1, p1

    goto :goto_29

    nop

    :goto_37
    invoke-direct {v4, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    goto :goto_17

    nop

    :goto_38
    invoke-virtual {v5, v6, v7, v8, v9}, Landroid/content/Context;->sendBroadcastAsUser(Landroid/content/Intent;Landroid/os/UserHandle;Ljava/lang/String;Landroid/os/Bundle;)V

    :goto_39
    goto :goto_2d

    nop

    :goto_3a
    invoke-virtual {v1}, Lcom/android/server/devicepolicy/ActiveAdmin;->getUserHandle()Landroid/os/UserHandle;

    move-result-object v7

    goto :goto_15

    nop

    :goto_3b
    iget-object v5, v0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    goto :goto_1e

    nop

    :goto_3c
    const/4 v8, 0x0

    goto :goto_1

    nop

    :goto_3d
    move v9, v8

    goto :goto_b

    nop

    :goto_3e
    move-object/from16 v0, p0

    goto :goto_36

    nop

    :goto_3f
    invoke-virtual {v4, v6, v5, v7}, Landroid/content/pm/PackageManager;->queryBroadcastReceiversAsUser(Landroid/content/Intent;ILandroid/os/UserHandle;)Ljava/util/List;

    move-result-object v4

    goto :goto_40

    nop

    :goto_40
    invoke-interface {v4}, Ljava/util/List;->isEmpty()Z

    move-result v4

    goto :goto_4

    nop

    :goto_41
    invoke-virtual {v6, v4}, Landroid/content/Intent;->setComponent(Landroid/content/ComponentName;)Landroid/content/Intent;

    goto :goto_33

    nop

    :goto_42
    invoke-virtual {v6, v5}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    :goto_43
    goto :goto_1b

    nop
.end method
""",
        "method_anchors": ['new-instance v4, Landroid/content/Intent;', 'invoke-direct {v4, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V', 'iget-object v4, v1, Lcom/android/server/devicepolicy/ActiveAdmin;->info:Landroid/app/admin/DeviceAdminInfo;', 'invoke-virtual {v4}, Landroid/app/admin/DeviceAdminInfo;->getComponent()Landroid/content/ComponentName;', 'move-result-object v4', 'invoke-virtual {v6, v4}, Landroid/content/Intent;->setComponent(Landroid/content/ComponentName;)Landroid/content/Intent;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_sendBugreportToDeviceOwner_Landroid_net_Uri_Ljava_lang_Strin",
        "method":      ".method sendBugreportToDeviceOwner(Landroid/net/Uri;Ljava/lang/String;)V",
        "method_name": 'sendBugreportToDeviceOwner',
        "type":        "method_replace",
        "search": """\
.method sendBugreportToDeviceOwner(Landroid/net/Uri;Ljava/lang/String;)V
    .registers 9

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    :try_start_0
    new-instance v1, Landroid/content/Intent;

    const-string v2, "android.app.action.BUGREPORT_SHARE"

    invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v2}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v2

    invoke-virtual {v1, v2}, Landroid/content/Intent;->setComponent(Landroid/content/ComponentName;)Landroid/content/Intent;

    const-string v2, "application/vnd.android.bugreport"

    invoke-virtual {v1, p1, v2}, Landroid/content/Intent;->setDataAndType(Landroid/net/Uri;Ljava/lang/String;)Landroid/content/Intent;

    const-string v2, "android.app.extra.BUGREPORT_HASH"

    invoke-virtual {v1, v2, p2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    const/4 v2, 0x1

    invoke-virtual {v1, v2}, Landroid/content/Intent;->setFlags(I)Landroid/content/Intent;

    const-class v2, Lcom/android/server/uri/UriGrantsManagerInternal;

    invoke-static {v2}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/server/uri/UriGrantsManagerInternal;

    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v3}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v3

    invoke-virtual {v3}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v3

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v4}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I

    move-result v4

    const/16 v5, 0x7d0

    invoke-interface {v2, v1, v5, v3, v4}, Lcom/android/server/uri/UriGrantsManagerInternal;->checkGrantUriPermissionFromIntent(Landroid/content/Intent;ILjava/lang/String;I)Lcom/android/server/uri/NeededUriGrants;

    move-result-object v3

    const/4 v4, 0x0

    invoke-interface {v2, v3, v4}, Lcom/android/server/uri/UriGrantsManagerInternal;->grantUriPermissionUncheckedFromIntent(Lcom/android/server/uri/NeededUriGrants;Lcom/android/server/uri/UriPermissionOwner;)V

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    iget-object v5, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v5}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I

    move-result v5

    invoke-static {v5}, Landroid/os/UserHandle;->of(I)Landroid/os/UserHandle;

    move-result-object v5

    invoke-virtual {v4, v1, v5}, Landroid/content/Context;->sendBroadcastAsUser(Landroid/content/Intent;Landroid/os/UserHandle;)V

    monitor-exit v0

    return-void

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method sendBugreportToDeviceOwner(Landroid/net/Uri;Ljava/lang/String;)V
    .registers 9

    goto :goto_2

    nop

    :goto_0
    throw v1

    :goto_1
    monitor-enter v0

    :try_start_0
    new-instance v1, Landroid/content/Intent;

    const-string v2, "android.app.action.BUGREPORT_SHARE"

    invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v2}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v2

    invoke-virtual {v1, v2}, Landroid/content/Intent;->setComponent(Landroid/content/ComponentName;)Landroid/content/Intent;

    const-string v2, "application/vnd.android.bugreport"

    invoke-virtual {v1, p1, v2}, Landroid/content/Intent;->setDataAndType(Landroid/net/Uri;Ljava/lang/String;)Landroid/content/Intent;

    const-string v2, "android.app.extra.BUGREPORT_HASH"

    invoke-virtual {v1, v2, p2}, Landroid/content/Intent;->putExtra(Ljava/lang/String;Ljava/lang/String;)Landroid/content/Intent;

    const/4 v2, 0x1

    invoke-virtual {v1, v2}, Landroid/content/Intent;->setFlags(I)Landroid/content/Intent;

    const-class v2, Lcom/android/server/uri/UriGrantsManagerInternal;

    invoke-static {v2}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lcom/android/server/uri/UriGrantsManagerInternal;

    iget-object v3, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v3}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v3

    invoke-virtual {v3}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v3

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v4}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I

    move-result v4

    const/16 v5, 0x7d0

    invoke-interface {v2, v1, v5, v3, v4}, Lcom/android/server/uri/UriGrantsManagerInternal;->checkGrantUriPermissionFromIntent(Landroid/content/Intent;ILjava/lang/String;I)Lcom/android/server/uri/NeededUriGrants;

    move-result-object v3

    const/4 v4, 0x0

    invoke-interface {v2, v3, v4}, Lcom/android/server/uri/UriGrantsManagerInternal;->grantUriPermissionUncheckedFromIntent(Lcom/android/server/uri/NeededUriGrants;Lcom/android/server/uri/UriPermissionOwner;)V

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mContext:Landroid/content/Context;

    iget-object v5, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v5}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I

    move-result v5

    invoke-static {v5}, Landroid/os/UserHandle;->of(I)Landroid/os/UserHandle;

    move-result-object v5

    invoke-virtual {v4, v1, v5}, Landroid/content/Context;->sendBroadcastAsUser(Landroid/content/Intent;Landroid/os/UserHandle;)V

    monitor-exit v0

    return-void

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;', 'move-result-object v0', 'new-instance v1, Landroid/content/Intent;', 'const-string v2, "android.app.action.BUGREPORT_SHARE"', 'invoke-direct {v1, v2}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V', 'iget-object v2, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_sendDeviceOwnerCommand_Ljava_lang_String_Landroid_os_Bundle_",
        "method":      ".method sendDeviceOwnerCommand(Ljava/lang/String;Landroid/os/Bundle;)V",
        "method_name": 'sendDeviceOwnerCommand',
        "type":        "method_replace",
        "search": """\
.method sendDeviceOwnerCommand(Ljava/lang/String;Landroid/os/Bundle;)V
    .registers 11

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v1

    monitor-enter v1

    :try_start_0
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I

    move-result v0

    move v5, v0

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v6

    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    const/4 v7, 0x0

    move-object v2, p0

    move-object v3, p1

    move-object v4, p2

    invoke-direct/range {v2 .. v7}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendActiveAdminCommand(Ljava/lang/String;Landroid/os/Bundle;ILandroid/content/ComponentName;Z)V

    return-void

    :catchall_0
    move-exception v0

    move-object v3, p1

    move-object v4, p2

    move-object p1, v0

    :goto_0
    :try_start_1
    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    throw p1

    :catchall_1
    move-exception v0

    move-object p1, v0

    goto :goto_0
.end method
""",
        "replacement": """\
.method sendDeviceOwnerCommand(Ljava/lang/String;Landroid/os/Bundle;)V
    .registers 11

    goto :goto_a

    nop

    :goto_0
    move-object v2, p0

    goto :goto_d

    nop

    :goto_1
    return-void

    :catchall_0
    move-exception v0

    goto :goto_2

    nop

    :goto_2
    move-object v3, p1

    goto :goto_6

    nop

    :goto_3
    invoke-direct/range {v2 .. v7}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendActiveAdminCommand(Ljava/lang/String;Landroid/os/Bundle;ILandroid/content/ComponentName;Z)V

    goto :goto_1

    nop

    :goto_4
    move-object p1, v0

    :goto_5
    :try_start_0
    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    goto :goto_9

    nop

    :goto_6
    move-object v4, p2

    goto :goto_4

    nop

    :goto_7
    move-object p1, v0

    goto :goto_c

    nop

    :goto_8
    move-object v4, p2

    goto :goto_3

    nop

    :goto_9
    throw p1

    :catchall_1
    move-exception v0

    goto :goto_7

    nop

    :goto_a
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v1

    goto :goto_b

    nop

    :goto_b
    monitor-enter v1

    :try_start_1
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I

    move-result v0

    move v5, v0

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerComponent()Landroid/content/ComponentName;

    move-result-object v6

    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_e

    nop

    :goto_c
    goto :goto_5

    :goto_d
    move-object v3, p1

    goto :goto_8

    nop

    :goto_e
    const/4 v7, 0x0

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;', 'move-result-object v1', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I', 'move-result v0', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_sendDeviceOwnerOrProfileOwnerCommand_Ljava_lang_String_Landr",
        "method":      ".method sendDeviceOwnerOrProfileOwnerCommand(Ljava/lang/String;Landroid/os/Bundle;I)V",
        "method_name": 'sendDeviceOwnerOrProfileOwnerCommand',
        "type":        "method_replace",
        "search": """\
.method sendDeviceOwnerOrProfileOwnerCommand(Ljava/lang/String;Landroid/os/Bundle;I)V
    .registers 10

    const/4 v0, -0x1

    if-ne p3, v0, :cond_1

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getHeadlessDeviceOwnerModeForDeviceOwner()I

    move-result v0

    const/4 v1, 0x2

    if-ne v0, v1, :cond_0

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I

    move-result p3

    move v3, p3

    goto :goto_0

    :cond_0
    const/4 p3, 0x0

    move v3, p3

    goto :goto_0

    :cond_1
    move v3, p3

    :goto_0
    const/4 p3, 0x0

    const/4 v0, 0x0

    const-string v1, "android.app.action.NETWORK_LOGS_AVAILABLE"

    invoke-virtual {p1, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_2

    const/4 p3, 0x1

    const-string v1, "delegation-network-logging"

    invoke-direct {p0, v1, p1, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->resolveDelegateReceiver(Ljava/lang/String;Ljava/lang/String;I)Landroid/content/ComponentName;

    move-result-object v0

    :cond_2
    const-string v1, "android.app.action.SECURITY_LOGS_AVAILABLE"

    invoke-virtual {p1, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    if-eqz v1, :cond_3

    const/4 p3, 0x1

    const-string v1, "delegation-security-logging"

    invoke-direct {p0, v1, p1, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->resolveDelegateReceiver(Ljava/lang/String;Ljava/lang/String;I)Landroid/content/ComponentName;

    move-result-object v0

    move v5, p3

    goto :goto_1

    :cond_3
    move v5, p3

    :goto_1
    if-nez v0, :cond_4

    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getOwnerComponent(I)Landroid/content/ComponentName;

    move-result-object v0

    move-object v4, v0

    goto :goto_2

    :cond_4
    move-object v4, v0

    :goto_2
    move-object v0, p0

    move-object v1, p1

    move-object v2, p2

    invoke-direct/range {v0 .. v5}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendActiveAdminCommand(Ljava/lang/String;Landroid/os/Bundle;ILandroid/content/ComponentName;Z)V

    return-void
.end method
""",
        "replacement": """\
.method sendDeviceOwnerOrProfileOwnerCommand(Ljava/lang/String;Landroid/os/Bundle;I)V
    .registers 10

    goto :goto_b

    nop

    :goto_0
    const-string v1, "delegation-network-logging"

    goto :goto_8

    nop

    :goto_1
    const/4 p3, 0x1

    goto :goto_17

    nop

    :goto_2
    if-nez v1, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_1

    nop

    :goto_3
    const/4 v0, 0x0

    goto :goto_24

    nop

    :goto_4
    const/4 p3, 0x0

    goto :goto_3

    nop

    :goto_5
    if-nez v1, :cond_1

    goto :goto_9

    :cond_1
    goto :goto_27

    nop

    :goto_6
    goto :goto_19

    :goto_7
    goto :goto_d

    nop

    :goto_8
    invoke-direct {p0, v1, p1, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->resolveDelegateReceiver(Ljava/lang/String;Ljava/lang/String;I)Landroid/content/ComponentName;

    move-result-object v0

    :goto_9
    goto :goto_28

    nop

    :goto_a
    move-object v0, p0

    goto :goto_1a

    nop

    :goto_b
    const/4 v0, -0x1

    goto :goto_c

    nop

    :goto_c
    if-eq p3, v0, :cond_2

    goto :goto_20

    :cond_2
    goto :goto_14

    nop

    :goto_d
    const/4 p3, 0x0

    goto :goto_25

    nop

    :goto_e
    goto :goto_1c

    :goto_f
    goto :goto_1b

    nop

    :goto_10
    invoke-virtual {p1, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    goto :goto_2

    nop

    :goto_11
    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getOwnerComponent(I)Landroid/content/ComponentName;

    move-result-object v0

    goto :goto_26

    nop

    :goto_12
    invoke-direct {p0, v1, p1, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->resolveDelegateReceiver(Ljava/lang/String;Ljava/lang/String;I)Landroid/content/ComponentName;

    move-result-object v0

    goto :goto_2f

    nop

    :goto_13
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    goto :goto_1d

    nop

    :goto_14
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getHeadlessDeviceOwnerModeForDeviceOwner()I

    move-result v0

    goto :goto_29

    nop

    :goto_15
    move-object v4, v0

    :goto_16
    goto :goto_a

    nop

    :goto_17
    const-string v1, "delegation-security-logging"

    goto :goto_12

    nop

    :goto_18
    move v3, p3

    :goto_19
    goto :goto_4

    nop

    :goto_1a
    move-object v1, p1

    goto :goto_2e

    nop

    :goto_1b
    move v5, p3

    :goto_1c
    goto :goto_2b

    nop

    :goto_1d
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I

    move-result p3

    goto :goto_2a

    nop

    :goto_1e
    invoke-virtual {p1, v1}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v1

    goto :goto_5

    nop

    :goto_1f
    goto :goto_19

    :goto_20
    goto :goto_18

    nop

    :goto_21
    invoke-direct/range {v0 .. v5}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->sendActiveAdminCommand(Ljava/lang/String;Landroid/os/Bundle;ILandroid/content/ComponentName;Z)V

    goto :goto_22

    nop

    :goto_22
    return-void

    :goto_23
    if-eq v0, v1, :cond_3

    goto :goto_7

    :cond_3
    goto :goto_13

    nop

    :goto_24
    const-string v1, "android.app.action.NETWORK_LOGS_AVAILABLE"

    goto :goto_1e

    nop

    :goto_25
    move v3, p3

    goto :goto_1f

    nop

    :goto_26
    move-object v4, v0

    goto :goto_2c

    nop

    :goto_27
    const/4 p3, 0x1

    goto :goto_0

    nop

    :goto_28
    const-string v1, "android.app.action.SECURITY_LOGS_AVAILABLE"

    goto :goto_10

    nop

    :goto_29
    const/4 v1, 0x2

    goto :goto_23

    nop

    :goto_2a
    move v3, p3

    goto :goto_6

    nop

    :goto_2b
    if-eqz v0, :cond_4

    goto :goto_2d

    :cond_4
    goto :goto_11

    nop

    :goto_2c
    goto :goto_16

    :goto_2d
    goto :goto_15

    nop

    :goto_2e
    move-object v2, p2

    goto :goto_21

    nop

    :goto_2f
    move v5, p3

    goto :goto_e

    nop
.end method
""",
        "method_anchors": ['if-ne p3, v0, :cond_1', 'invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getHeadlessDeviceOwnerModeForDeviceOwner()I', 'move-result v0', 'if-ne v0, v1, :cond_0', 'iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->getDeviceOwnerUserId()I'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setDeviceOwnerRemoteBugreportUriAndHash_Ljava_lang_String_Lj",
        "method":      ".method setDeviceOwnerRemoteBugreportUriAndHash(Ljava/lang/String;Ljava/lang/String;)V",
        "method_name": 'setDeviceOwnerRemoteBugreportUriAndHash',
        "type":        "method_replace",
        "search": """\
.method setDeviceOwnerRemoteBugreportUriAndHash(Ljava/lang/String;Ljava/lang/String;)V
    .registers 5

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v1, p1, p2}, Lcom/android/server/devicepolicy/Owners;->setDeviceOwnerRemoteBugreportUriAndHash(Ljava/lang/String;Ljava/lang/String;)V

    monitor-exit v0

    return-void

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v1
.end method
""",
        "replacement": """\
.method setDeviceOwnerRemoteBugreportUriAndHash(Ljava/lang/String;Ljava/lang/String;)V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    throw v1

    :goto_1
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_2

    nop

    :goto_2
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v1, p1, p2}, Lcom/android/server/devicepolicy/Owners;->setDeviceOwnerRemoteBugreportUriAndHash(Ljava/lang/String;Ljava/lang/String;)V

    monitor-exit v0

    return-void

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;', 'move-result-object v0', 'iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;', 'invoke-virtual {v1, p1, p2}, Lcom/android/server/devicepolicy/Owners;->setDeviceOwnerRemoteBugreportUriAndHash(Ljava/lang/String;Ljava/lang/String;)V', 'return-void', 'throw v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setDevicePolicySafetyCheckerUnchecked_Landroid_app_admin_Dev",
        "method":      ".method setDevicePolicySafetyCheckerUnchecked(Landroid/app/admin/DevicePolicySafetyChecker;)V",
        "method_name": 'setDevicePolicySafetyCheckerUnchecked',
        "type":        "method_replace",
        "search": """\
.method setDevicePolicySafetyCheckerUnchecked(Landroid/app/admin/DevicePolicySafetyChecker;)V
    .registers 5

    const-string v0, "Setting DevicePolicySafetyChecker as %s"

    filled-new-array {p1}, [Ljava/lang/Object;

    move-result-object v1

    const-string v2, "DevicePolicyManager"

    invoke-static {v2, v0, v1}, Lcom/android/server/utils/Slogf;->i(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    iput-object p1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->setDevicePolicySafetyChecker(Landroid/app/admin/DevicePolicySafetyChecker;)V

    return-void
.end method
""",
        "replacement": """\
.method setDevicePolicySafetyCheckerUnchecked(Landroid/app/admin/DevicePolicySafetyChecker;)V
    .registers 5

    goto :goto_7

    nop

    :goto_0
    const-string v2, "DevicePolicyManager"

    goto :goto_5

    nop

    :goto_1
    iput-object p1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;

    goto :goto_3

    nop

    :goto_2
    filled-new-array {p1}, [Ljava/lang/Object;

    move-result-object v1

    goto :goto_0

    nop

    :goto_3
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_4

    nop

    :goto_4
    invoke-virtual {v0, p1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->setDevicePolicySafetyChecker(Landroid/app/admin/DevicePolicySafetyChecker;)V

    goto :goto_6

    nop

    :goto_5
    invoke-static {v2, v0, v1}, Lcom/android/server/utils/Slogf;->i(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V

    goto :goto_1

    nop

    :goto_6
    return-void

    :goto_7
    const-string v0, "Setting DevicePolicySafetyChecker as %s"

    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['const-string v0, "Setting DevicePolicySafetyChecker as %s"', 'filled-new-array {p1}, [Ljava/lang/Object;', 'move-result-object v1', 'const-string v2, "DevicePolicyManager"', 'invoke-static {v2, v0, v1}, Lcom/android/server/utils/Slogf;->i(Ljava/lang/String;Ljava/lang/String;[Ljava/lang/Object;)V', 'iput-object p1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mSafetyChecker:Landroid/app/admin/DevicePolicySafetyChecker;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setScreenCaptureDisabled_Landroid_content_ComponentName_Ljav",
        "method":      ".method public setScreenCaptureDisabled(Landroid/content/ComponentName;Ljava/lang/String;ZZ)V",
        "method_name": 'setScreenCaptureDisabled',
        "type":        "method_replace",
        "search": """\
.method public setScreenCaptureDisabled(Landroid/content/ComponentName;Ljava/lang/String;ZZ)V
    .registers 12

    iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z

    if-nez v0, :cond_0

    return-void

    :cond_0
    invoke-virtual {p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity(Landroid/content/ComponentName;Ljava/lang/String;)Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    invoke-static {}, Landroid/os/Binder;->getCallingUserHandle()Landroid/os/UserHandle;

    move-result-object v1

    invoke-virtual {v1}, Landroid/os/UserHandle;->getIdentifier()I

    move-result v1

    if-eqz p4, :cond_1

    invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileParentId(I)I

    move-result v2

    goto :goto_0

    :cond_1
    move v2, v1

    :goto_0
    nop

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getPackageName()Ljava/lang/String;

    move-result-object v3

    const-string v4, "android.permission.MANAGE_DEVICE_POLICY_SCREEN_CAPTURE"

    invoke-direct {p0, p1, v4, v3, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->enforcePermissionAndGetEnforcingAdmin(Landroid/content/ComponentName;Ljava/lang/String;Ljava/lang/String;I)Lcom/android/server/devicepolicy/EnforcingAdmin;

    move-result-object v3

    if-eqz p4, :cond_2

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwnerOfOrganizationOwnedDevice(Lcom/android/server/devicepolicy/CallerIdentity;)Z

    move-result v4

    if-nez v4, :cond_3

    :cond_2
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isDefaultDeviceOwner(Lcom/android/server/devicepolicy/CallerIdentity;)Z

    move-result v4

    if-eqz v4, :cond_5

    :cond_3
    if-eqz p3, :cond_4

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    sget-object v5, Lcom/android/server/devicepolicy/PolicyDefinition;->SCREEN_CAPTURE_DISABLED:Lcom/android/server/devicepolicy/PolicyDefinition;

    new-instance v6, Landroid/app/admin/BooleanPolicyValue;

    invoke-direct {v6, p3}, Landroid/app/admin/BooleanPolicyValue;-><init>(Z)V

    invoke-virtual {v4, v5, v3, v6}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->setGlobalPolicy(Lcom/android/server/devicepolicy/PolicyDefinition;Lcom/android/server/devicepolicy/EnforcingAdmin;Landroid/app/admin/PolicyValue;)V

    goto :goto_1

    :cond_4
    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    sget-object v5, Lcom/android/server/devicepolicy/PolicyDefinition;->SCREEN_CAPTURE_DISABLED:Lcom/android/server/devicepolicy/PolicyDefinition;

    invoke-virtual {v4, v5, v3}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->removeGlobalPolicy(Lcom/android/server/devicepolicy/PolicyDefinition;Lcom/android/server/devicepolicy/EnforcingAdmin;)V

    goto :goto_1

    :cond_5
    if-eqz p3, :cond_6

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    sget-object v5, Lcom/android/server/devicepolicy/PolicyDefinition;->SCREEN_CAPTURE_DISABLED:Lcom/android/server/devicepolicy/PolicyDefinition;

    new-instance v6, Landroid/app/admin/BooleanPolicyValue;

    invoke-direct {v6, p3}, Landroid/app/admin/BooleanPolicyValue;-><init>(Z)V

    invoke-virtual {v4, v5, v3, v6, v1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->setLocalPolicy(Lcom/android/server/devicepolicy/PolicyDefinition;Lcom/android/server/devicepolicy/EnforcingAdmin;Landroid/app/admin/PolicyValue;I)V

    goto :goto_1

    :cond_6
    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    sget-object v5, Lcom/android/server/devicepolicy/PolicyDefinition;->SCREEN_CAPTURE_DISABLED:Lcom/android/server/devicepolicy/PolicyDefinition;

    invoke-virtual {v4, v5, v3, v1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->removeLocalPolicy(Lcom/android/server/devicepolicy/PolicyDefinition;Lcom/android/server/devicepolicy/EnforcingAdmin;I)V

    :goto_1
    nop

    const/16 v4, 0x1d

    invoke-static {v4}, Landroid/app/admin/DevicePolicyEventLogger;->createEvent(I)Landroid/app/admin/DevicePolicyEventLogger;

    move-result-object v4

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getPackageName()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Landroid/app/admin/DevicePolicyEventLogger;->setAdmin(Ljava/lang/String;)Landroid/app/admin/DevicePolicyEventLogger;

    move-result-object v4

    invoke-virtual {v4, p3}, Landroid/app/admin/DevicePolicyEventLogger;->setBoolean(Z)Landroid/app/admin/DevicePolicyEventLogger;

    move-result-object v4

    invoke-virtual {v4}, Landroid/app/admin/DevicePolicyEventLogger;->write()V

    return-void
.end method
""",
        "replacement": """\
.method public setScreenCaptureDisabled(Landroid/content/ComponentName;Ljava/lang/String;ZZ)V
    .registers 12

    const-string v0, "disable_mezo_screenshot_secure"

    const/4 v1, 0x1

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-eqz v0, :cond_0

    return-void

    :cond_0
    iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z

    if-nez v0, :cond_1

    return-void

    :cond_1
    invoke-virtual {p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity(Landroid/content/ComponentName;Ljava/lang/String;)Lcom/android/server/devicepolicy/CallerIdentity;

    move-result-object v0

    invoke-static {}, Landroid/os/Binder;->getCallingUserHandle()Landroid/os/UserHandle;

    move-result-object v1

    invoke-virtual {v1}, Landroid/os/UserHandle;->getIdentifier()I

    move-result v1

    if-eqz p4, :cond_2

    invoke-virtual {p0, v1}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getProfileParentId(I)I

    move-result v2

    goto :goto_0

    :cond_2
    move v2, v1

    :goto_0
    nop

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getPackageName()Ljava/lang/String;

    move-result-object v3

    const-string v4, "android.permission.MANAGE_DEVICE_POLICY_SCREEN_CAPTURE"

    invoke-direct {p0, p1, v4, v3, v2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->enforcePermissionAndGetEnforcingAdmin(Landroid/content/ComponentName;Ljava/lang/String;Ljava/lang/String;I)Lcom/android/server/devicepolicy/EnforcingAdmin;

    move-result-object v3

    if-eqz p4, :cond_3

    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isProfileOwnerOfOrganizationOwnedDevice(Lcom/android/server/devicepolicy/CallerIdentity;)Z

    move-result v4

    if-nez v4, :cond_4

    :cond_3
    invoke-direct {p0, v0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->isDefaultDeviceOwner(Lcom/android/server/devicepolicy/CallerIdentity;)Z

    move-result v4

    if-eqz v4, :cond_6

    :cond_4
    if-eqz p3, :cond_5

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    sget-object v5, Lcom/android/server/devicepolicy/PolicyDefinition;->SCREEN_CAPTURE_DISABLED:Lcom/android/server/devicepolicy/PolicyDefinition;

    new-instance v6, Landroid/app/admin/BooleanPolicyValue;

    invoke-direct {v6, p3}, Landroid/app/admin/BooleanPolicyValue;-><init>(Z)V

    invoke-virtual {v4, v5, v3, v6}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->setGlobalPolicy(Lcom/android/server/devicepolicy/PolicyDefinition;Lcom/android/server/devicepolicy/EnforcingAdmin;Landroid/app/admin/PolicyValue;)V

    goto :goto_1

    :cond_5
    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    sget-object v5, Lcom/android/server/devicepolicy/PolicyDefinition;->SCREEN_CAPTURE_DISABLED:Lcom/android/server/devicepolicy/PolicyDefinition;

    invoke-virtual {v4, v5, v3}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->removeGlobalPolicy(Lcom/android/server/devicepolicy/PolicyDefinition;Lcom/android/server/devicepolicy/EnforcingAdmin;)V

    goto :goto_1

    :cond_6
    if-eqz p3, :cond_7

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    sget-object v5, Lcom/android/server/devicepolicy/PolicyDefinition;->SCREEN_CAPTURE_DISABLED:Lcom/android/server/devicepolicy/PolicyDefinition;

    new-instance v6, Landroid/app/admin/BooleanPolicyValue;

    invoke-direct {v6, p3}, Landroid/app/admin/BooleanPolicyValue;-><init>(Z)V

    invoke-virtual {v4, v5, v3, v6, v1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->setLocalPolicy(Lcom/android/server/devicepolicy/PolicyDefinition;Lcom/android/server/devicepolicy/EnforcingAdmin;Landroid/app/admin/PolicyValue;I)V

    goto :goto_1

    :cond_7
    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    sget-object v5, Lcom/android/server/devicepolicy/PolicyDefinition;->SCREEN_CAPTURE_DISABLED:Lcom/android/server/devicepolicy/PolicyDefinition;

    invoke-virtual {v4, v5, v3, v1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->removeLocalPolicy(Lcom/android/server/devicepolicy/PolicyDefinition;Lcom/android/server/devicepolicy/EnforcingAdmin;I)V

    :goto_1
    nop

    const/16 v4, 0x1d

    invoke-static {v4}, Landroid/app/admin/DevicePolicyEventLogger;->createEvent(I)Landroid/app/admin/DevicePolicyEventLogger;

    move-result-object v4

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/CallerIdentity;->getPackageName()Ljava/lang/String;

    move-result-object v5

    invoke-virtual {v4, v5}, Landroid/app/admin/DevicePolicyEventLogger;->setAdmin(Ljava/lang/String;)Landroid/app/admin/DevicePolicyEventLogger;

    move-result-object v4

    invoke-virtual {v4, p3}, Landroid/app/admin/DevicePolicyEventLogger;->setBoolean(Z)Landroid/app/admin/DevicePolicyEventLogger;

    move-result-object v4

    invoke-virtual {v4}, Landroid/app/admin/DevicePolicyEventLogger;->write()V

    return-void
.end method
""",
        "method_anchors": ['iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z', 'if-nez v0, :cond_0', 'return-void', 'invoke-virtual {p0, p1, p2}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getCallerIdentity(Landroid/content/ComponentName;Ljava/lang/String;)Lcom/android/server/devicepolicy/CallerIdentity;', 'move-result-object v0', 'invoke-static {}, Landroid/os/Binder;->getCallingUserHandle()Landroid/os/UserHandle;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_systemReady_I_V",
        "method":      ".method systemReady(I)V",
        "method_name": 'systemReady',
        "type":        "method_replace",
        "search": """\
.method systemReady(I)V
    .registers 4

    iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z

    if-nez v0, :cond_0

    return-void

    :cond_0
    sparse-switch p1, :sswitch_data_0

    goto :goto_0

    :sswitch_0
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->factoryResetIfDelayedEarlier()V

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureDeviceOwnerUserStarted()V

    goto :goto_0

    :sswitch_1
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    :try_start_0
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->migrateToProfileOnOrganizationOwnedDeviceIfCompLocked()V

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->applyProfileRestrictionsIfDeviceOwnerLocked()V

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->shouldMigrateV1ToDevicePolicyEngine()Z

    move-result v1

    if-eqz v1, :cond_1

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->migrateV1PoliciesToDevicePolicyEngine()Z

    :cond_1
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->maybeMigratePoliciesPostUpgradeToDevicePolicyEngineLocked()V

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->migratePoliciesToPolicyEngineLocked()V

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->maybeStartSecurityLogMonitorOnActivityManagerReady()V

    goto :goto_0

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    throw v1

    :sswitch_2
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    monitor-enter v0

    :try_start_2
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->reapplyAllPoliciesOnBootLocked()V

    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/app/admin/flags/Flags;->managementModePolicyMetrics()Z

    move-result v0

    if-eqz v0, :cond_2

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->registerStatsCallbacks()V

    goto :goto_0

    :catchall_1
    move-exception v1

    :try_start_3
    monitor-exit v0
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_1

    throw v1

    :sswitch_3
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->onLockSettingsReady()V

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->loadAdminDataAsync()V

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->systemReady()V

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->applyManagedSubscriptionsPolicyIfRequired()V

    nop

    :cond_2
    :goto_0
    return-void

    :sswitch_data_0
    .sparse-switch
        0x1e0 -> :sswitch_3
        0x1f4 -> :sswitch_2
        0x226 -> :sswitch_1
        0x3e8 -> :sswitch_0
    .end sparse-switch
.end method
""",
        "replacement": """\
.method systemReady(I)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    throw v1

    :sswitch_0
    goto :goto_e

    nop

    :goto_1
    iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z

    goto :goto_19

    nop

    :goto_2
    monitor-enter v0

    :try_start_0
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->migrateToProfileOnOrganizationOwnedDeviceIfCompLocked()V

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->applyProfileRestrictionsIfDeviceOwnerLocked()V

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->shouldMigrateV1ToDevicePolicyEngine()Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->migrateV1PoliciesToDevicePolicyEngine()Z

    :cond_0
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->maybeMigratePoliciesPostUpgradeToDevicePolicyEngineLocked()V

    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->migratePoliciesToPolicyEngineLocked()V

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    goto :goto_9

    nop

    :goto_3
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->applyManagedSubscriptionsPolicyIfRequired()V

    nop

    :goto_4
    goto :goto_6

    nop

    :goto_5
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->loadAdminDataAsync()V

    goto :goto_8

    nop

    :goto_6
    return-void

    :sswitch_data_0
    .sparse-switch
        0x1e0 -> :sswitch_0
        0x1f4 -> :sswitch_2
        0x226 -> :sswitch_1
        0x3e8 -> :sswitch_3
    .end sparse-switch

    :goto_7
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->factoryResetIfDelayedEarlier()V

    goto :goto_f

    nop

    :goto_8
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mOwners:Lcom/android/server/devicepolicy/Owners;

    goto :goto_12

    nop

    :goto_9
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->maybeStartSecurityLogMonitorOnActivityManagerReady()V

    goto :goto_16

    nop

    :goto_a
    goto :goto_4

    :sswitch_1
    goto :goto_c

    nop

    :goto_b
    monitor-enter v0

    :try_start_1
    iget-object v1, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mDevicePolicyEngine:Lcom/android/server/devicepolicy/DevicePolicyEngine;

    invoke-virtual {v1}, Lcom/android/server/devicepolicy/DevicePolicyEngine;->reapplyAllPoliciesOnBootLocked()V

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_13

    nop

    :goto_c
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_2

    nop

    :goto_d
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v0

    goto :goto_b

    nop

    :goto_e
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->onLockSettingsReady()V

    goto :goto_5

    nop

    :goto_f
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureDeviceOwnerUserStarted()V

    goto :goto_a

    nop

    :goto_10
    return-void

    :goto_11
    sparse-switch p1, :sswitch_data_0

    goto :goto_18

    nop

    :goto_12
    invoke-virtual {v0}, Lcom/android/server/devicepolicy/Owners;->systemReady()V

    goto :goto_3

    nop

    :goto_13
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/android/app/admin/flags/Flags;->managementModePolicyMetrics()Z

    move-result v0

    goto :goto_1a

    nop

    :goto_14
    goto :goto_4

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_0

    nop

    :goto_15
    throw v1

    :sswitch_2
    goto :goto_d

    nop

    :goto_16
    goto :goto_4

    :catchall_1
    move-exception v1

    :try_start_3
    monitor-exit v0
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_1

    goto :goto_15

    nop

    :goto_17
    invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->registerStatsCallbacks()V

    goto :goto_14

    nop

    :goto_18
    goto :goto_4

    :sswitch_3
    goto :goto_7

    nop

    :goto_19
    if-eqz v0, :cond_1

    goto :goto_11

    :cond_1
    goto :goto_10

    nop

    :goto_1a
    if-nez v0, :cond_2

    goto :goto_4

    :cond_2
    goto :goto_17

    nop
.end method
""",
        "method_anchors": ['iget-boolean v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mHasFeature:Z', 'if-nez v0, :cond_0', 'return-void', 'invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->factoryResetIfDelayedEarlier()V', 'invoke-direct {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->ensureDeviceOwnerUserStarted()V', 'invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_updateUserSetupCompleteAndPaired__V",
        "method":      ".method updateUserSetupCompleteAndPaired()V",
        "method_name": 'updateUserSetupCompleteAndPaired',
        "type":        "method_replace",
        "search": """\
.method updateUserSetupCompleteAndPaired()V
    .registers 9

    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserManager:Landroid/os/UserManager;

    invoke-virtual {v0}, Landroid/os/UserManager;->getAliveUsers()Ljava/util/List;

    move-result-object v0

    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v1

    const/4 v2, 0x0

    :goto_0
    if-ge v2, v1, :cond_3

    invoke-interface {v0, v2}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v3

    check-cast v3, Landroid/content/pm/UserInfo;

    iget v3, v3, Landroid/content/pm/UserInfo;->id:I

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    const-string v5, "user_setup_complete"

    const/4 v6, 0x0

    invoke-virtual {v4, v5, v6, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->settingsSecureGetIntForUser(Ljava/lang/String;II)I

    move-result v4

    const/4 v5, 0x1

    if-eqz v4, :cond_1

    invoke-virtual {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v4

    iget-boolean v7, v4, Lcom/android/server/devicepolicy/DevicePolicyData;->mUserSetupComplete:Z

    if-nez v7, :cond_1

    iput-boolean v5, v4, Lcom/android/server/devicepolicy/DevicePolicyData;->mUserSetupComplete:Z

    if-nez v3, :cond_0

    iget-object v7, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStateCache:Lcom/android/server/devicepolicy/DeviceStateCacheImpl;

    invoke-virtual {v7, v5}, Lcom/android/server/devicepolicy/DeviceStateCacheImpl;->setDeviceProvisioned(Z)V

    :cond_0
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v7

    monitor-enter v7

    :try_start_0
    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->saveSettingsLocked(I)V

    monitor-exit v7

    goto :goto_1

    :catchall_0
    move-exception v5

    monitor-exit v7
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    throw v5

    :cond_1
    :goto_1
    iget-boolean v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIsWatch:Z

    if-eqz v4, :cond_2

    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    const-string v7, "device_paired"

    invoke-virtual {v4, v7, v6, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->settingsSecureGetIntForUser(Ljava/lang/String;II)I

    move-result v4

    if-eqz v4, :cond_2

    invoke-virtual {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v4

    iget-boolean v6, v4, Lcom/android/server/devicepolicy/DevicePolicyData;->mPaired:Z

    if-nez v6, :cond_2

    iput-boolean v5, v4, Lcom/android/server/devicepolicy/DevicePolicyData;->mPaired:Z

    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v5

    monitor-enter v5

    :try_start_1
    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->saveSettingsLocked(I)V

    monitor-exit v5

    goto :goto_2

    :catchall_1
    move-exception v6

    monitor-exit v5
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    throw v6

    :cond_2
    :goto_2
    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :cond_3
    return-void
.end method
""",
        "replacement": """\
.method updateUserSetupCompleteAndPaired()V
    .registers 9

    goto :goto_e

    nop

    :goto_0
    if-eqz v6, :cond_0

    goto :goto_23

    :cond_0
    goto :goto_21

    nop

    :goto_1
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v7

    goto :goto_28

    nop

    :goto_2
    throw v5

    :goto_3
    goto :goto_1a

    nop

    :goto_4
    iget v3, v3, Landroid/content/pm/UserInfo;->id:I

    goto :goto_12

    nop

    :goto_5
    if-lt v2, v1, :cond_1

    goto :goto_15

    :cond_1
    goto :goto_13

    nop

    :goto_6
    const-string v5, "user_setup_complete"

    goto :goto_19

    nop

    :goto_7
    iget-boolean v6, v4, Lcom/android/server/devicepolicy/DevicePolicyData;->mPaired:Z

    goto :goto_0

    nop

    :goto_8
    invoke-virtual {v0}, Landroid/os/UserManager;->getAliveUsers()Ljava/util/List;

    move-result-object v0

    goto :goto_d

    nop

    :goto_9
    return-void

    :goto_a
    const-string v7, "device_paired"

    goto :goto_1c

    nop

    :goto_b
    const/4 v2, 0x0

    :goto_c
    goto :goto_5

    nop

    :goto_d
    invoke-interface {v0}, Ljava/util/List;->size()I

    move-result v1

    goto :goto_b

    nop

    :goto_e
    iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserManager:Landroid/os/UserManager;

    goto :goto_8

    nop

    :goto_f
    invoke-virtual {v7, v5}, Lcom/android/server/devicepolicy/DeviceStateCacheImpl;->setDeviceProvisioned(Z)V

    :goto_10
    goto :goto_1

    nop

    :goto_11
    if-nez v4, :cond_2

    goto :goto_23

    :cond_2
    goto :goto_2c

    nop

    :goto_12
    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_6

    nop

    :goto_13
    invoke-interface {v0, v2}, Ljava/util/List;->get(I)Ljava/lang/Object;

    move-result-object v3

    goto :goto_17

    nop

    :goto_14
    goto :goto_c

    :goto_15
    goto :goto_9

    nop

    :goto_16
    if-eqz v7, :cond_3

    goto :goto_3

    :cond_3
    goto :goto_1f

    nop

    :goto_17
    check-cast v3, Landroid/content/pm/UserInfo;

    goto :goto_4

    nop

    :goto_18
    invoke-virtual {p0}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getLockObject()Ljava/lang/Object;

    move-result-object v5

    goto :goto_2b

    nop

    :goto_19
    const/4 v6, 0x0

    goto :goto_24

    nop

    :goto_1a
    iget-boolean v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mIsWatch:Z

    goto :goto_11

    nop

    :goto_1b
    if-eqz v3, :cond_4

    goto :goto_10

    :cond_4
    goto :goto_1e

    nop

    :goto_1c
    invoke-virtual {v4, v7, v6, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->settingsSecureGetIntForUser(Ljava/lang/String;II)I

    move-result v4

    goto :goto_27

    nop

    :goto_1d
    const/4 v5, 0x1

    goto :goto_26

    nop

    :goto_1e
    iget-object v7, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mStateCache:Lcom/android/server/devicepolicy/DeviceStateCacheImpl;

    goto :goto_f

    nop

    :goto_1f
    iput-boolean v5, v4, Lcom/android/server/devicepolicy/DevicePolicyData;->mUserSetupComplete:Z

    goto :goto_1b

    nop

    :goto_20
    invoke-virtual {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v4

    goto :goto_7

    nop

    :goto_21
    iput-boolean v5, v4, Lcom/android/server/devicepolicy/DevicePolicyData;->mPaired:Z

    goto :goto_18

    nop

    :goto_22
    throw v6

    :goto_23
    goto :goto_2a

    nop

    :goto_24
    invoke-virtual {v4, v5, v6, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;->settingsSecureGetIntForUser(Ljava/lang/String;II)I

    move-result v4

    goto :goto_1d

    nop

    :goto_25
    invoke-virtual {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->getUserData(I)Lcom/android/server/devicepolicy/DevicePolicyData;

    move-result-object v4

    goto :goto_29

    nop

    :goto_26
    if-nez v4, :cond_5

    goto :goto_3

    :cond_5
    goto :goto_25

    nop

    :goto_27
    if-nez v4, :cond_6

    goto :goto_23

    :cond_6
    goto :goto_20

    nop

    :goto_28
    monitor-enter v7

    :try_start_0
    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->saveSettingsLocked(I)V

    monitor-exit v7

    goto :goto_3

    :catchall_0
    move-exception v5

    monitor-exit v7
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_2

    nop

    :goto_29
    iget-boolean v7, v4, Lcom/android/server/devicepolicy/DevicePolicyData;->mUserSetupComplete:Z

    goto :goto_16

    nop

    :goto_2a
    add-int/lit8 v2, v2, 0x1

    goto :goto_14

    nop

    :goto_2b
    monitor-enter v5

    :try_start_1
    invoke-direct {p0, v3}, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->saveSettingsLocked(I)V

    monitor-exit v5

    goto :goto_23

    :catchall_1
    move-exception v6

    monitor-exit v5
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    goto :goto_22

    nop

    :goto_2c
    iget-object v4, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mInjector:Lcom/android/server/devicepolicy/DevicePolicyManagerService$Injector;

    goto :goto_a

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/devicepolicy/DevicePolicyManagerService;->mUserManager:Landroid/os/UserManager;', 'invoke-virtual {v0}, Landroid/os/UserManager;->getAliveUsers()Ljava/util/List;', 'move-result-object v0', 'invoke-interface {v0}, Ljava/util/List;->size()I', 'move-result v1', 'if-ge v2, v1, :cond_3'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
]
