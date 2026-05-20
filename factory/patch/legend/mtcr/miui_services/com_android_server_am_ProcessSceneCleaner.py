"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-services.jar
Target class : com/android/server/am/ProcessSceneCleaner
Source MTCR  : miui-services_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-services.jar"
TARGET_CLASS = "com/android/server/am/ProcessSceneCleaner.smali"

PATCHES = [
    {
        "id":          "replace_method_handleSwipeKill_Lmiui_process_ProcessConfig__Z",
        "method":      ".method private handleSwipeKill(Lmiui/process/ProcessConfig;)Z",
        "type":        "method_replace",
        "search": """\
.method private handleSwipeKill(Lmiui/process/ProcessConfig;)Z
    .registers 15

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->isUserIdInvalid()Z

    move-result v0

    const/4 v1, 0x0

    if-nez v0, :cond_8

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->isTaskIdInvalid()Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_2

    :cond_0
    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getKillingPackage()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getTaskId()I

    move-result v2

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getPolicy()I

    move-result v3

    invoke-virtual {p0, v3}, Lcom/android/server/am/ProcessSceneCleaner;->getKillReason(I)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->isRemoveTaskNeeded()Z

    move-result v3

    if-eqz v3, :cond_1

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getTaskId()I

    move-result v3

    invoke-virtual {p0, v3}, Lcom/android/server/am/ProcessSceneCleaner;->removeTaskIfNeeded(I)V

    :cond_1
    iget-object v3, p0, Lcom/android/server/am/ProcessSceneCleaner;->mPMS:Lcom/android/server/am/ProcessManagerService;

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getUserId()I

    move-result v4

    invoke-virtual {v3, v0, v4}, Lcom/android/server/am/ProcessManagerService;->getProcessRecordList(Ljava/lang/String;I)Ljava/util/List;

    move-result-object v3

    if-eqz v3, :cond_7

    invoke-interface {v3}, Ljava/util/List;->isEmpty()Z

    move-result v4

    if-eqz v4, :cond_2

    goto :goto_1

    :cond_2
    invoke-direct {p0, v3, v2}, Lcom/android/server/am/ProcessSceneCleaner;->isAppHasOtherTask(Ljava/util/List;I)Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-direct {p0, v2, p1}, Lcom/android/server/am/ProcessSceneCleaner;->killAppForHasOtherTask(ILmiui/process/ProcessConfig;)Z

    move-result v1

    return v1

    :cond_3
    invoke-interface {v3}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_0
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v4

    if-eqz v4, :cond_6

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v4

    move-object v5, v4

    check-cast v5, Lcom/android/server/am/ProcessRecord;

    sget-boolean v4, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v4, :cond_4

    iget-object v4, v5, Lcom/android/server/am/ProcessRecord;->mServices:Lcom/android/server/am/ProcessServiceRecord;

    invoke-virtual {v4}, Lcom/android/server/am/ProcessServiceRecord;->hasForegroundServices()Z

    move-result v4

    if-nez v4, :cond_5

    :cond_4
    iget-object v4, v5, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v4, v4, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget-object v6, v5, Lcom/android/server/am/ProcessRecord;->processName:Ljava/lang/String;

    invoke-virtual {p0, v4, v6}, Lcom/android/server/am/ProcessSceneCleaner;->isCurrentProcessInBackup(Ljava/lang/String;Ljava/lang/String;)Z

    move-result v4

    if-nez v4, :cond_5

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getPolicy()I

    move-result v6

    iget-object v9, p0, Lcom/android/server/am/ProcessSceneCleaner;->mPMS:Lcom/android/server/am/ProcessManagerService;

    iget-object v11, p0, Lcom/android/server/am/ProcessSceneCleaner;->mHandler:Lcom/android/server/am/ProcessSceneCleaner$H;

    iget-object v12, p0, Lcom/android/server/am/ProcessSceneCleaner;->mContext:Landroid/content/Context;

    const/4 v8, 0x1

    const-string v10, "ProcessSceneCleaner"

    move-object v4, p0

    invoke-virtual/range {v4 .. v12}, Lcom/android/server/am/ProcessSceneCleaner;->killOnce(Lcom/android/server/am/ProcessRecord;ILjava/lang/String;ZLcom/android/server/am/ProcessManagerService;Ljava/lang/String;Landroid/os/Handler;Landroid/content/Context;)V

    :cond_5
    goto :goto_0

    :cond_6
    const/4 v1, 0x1

    return v1

    :cond_7
    :goto_1
    return v1

    :cond_8
    :goto_2
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "userId:"

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getUserId()I

    move-result v2

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v2, " or taskId:"

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getTaskId()I

    move-result v2

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v2, " is invalid"

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v2, "ProcessSceneCleaner"

    invoke-static {v2, v0}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    return v1
.end method
""",
        "replacement": """\
.method private handleSwipeKill(Lmiui/process/ProcessConfig;)Z
    .registers 15

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->isUserIdInvalid()Z

    move-result v0

    const/4 v1, 0x0

    if-nez v0, :cond_8

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->isTaskIdInvalid()Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_2

    :cond_0
    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getKillingPackage()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getTaskId()I

    move-result v2

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getPolicy()I

    move-result v3

    invoke-virtual {p0, v3}, Lcom/android/server/am/ProcessSceneCleaner;->getKillReason(I)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->isRemoveTaskNeeded()Z

    move-result v3

    if-eqz v3, :cond_1

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getTaskId()I

    move-result v3

    invoke-virtual {p0, v3}, Lcom/android/server/am/ProcessSceneCleaner;->removeTaskIfNeeded(I)V

    :cond_1
    iget-object v3, p0, Lcom/android/server/am/ProcessSceneCleaner;->mPMS:Lcom/android/server/am/ProcessManagerService;

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getUserId()I

    move-result v4

    invoke-virtual {v3, v0, v4}, Lcom/android/server/am/ProcessManagerService;->getProcessRecordList(Ljava/lang/String;I)Ljava/util/List;

    move-result-object v3

    if-eqz v3, :cond_7

    invoke-interface {v3}, Ljava/util/List;->isEmpty()Z

    move-result v4

    if-eqz v4, :cond_2

    goto :goto_1

    :cond_2
    invoke-direct {p0, v3, v2}, Lcom/android/server/am/ProcessSceneCleaner;->isAppHasOtherTask(Ljava/util/List;I)Z

    move-result v1

    if-eqz v1, :cond_3

    invoke-direct {p0, v2, p1}, Lcom/android/server/am/ProcessSceneCleaner;->killAppForHasOtherTask(ILmiui/process/ProcessConfig;)Z

    move-result v1

    return v1

    :cond_3
    invoke-interface {v3}, Ljava/util/List;->iterator()Ljava/util/Iterator;

    move-result-object v1

    :goto_0
    invoke-interface {v1}, Ljava/util/Iterator;->hasNext()Z

    move-result v4

    if-eqz v4, :cond_6

    invoke-interface {v1}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v4

    move-object v5, v4

    check-cast v5, Lcom/android/server/am/ProcessRecord;

    sget-boolean v4, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v4, 0x1

    if-eqz v4, :cond_4

    iget-object v4, v5, Lcom/android/server/am/ProcessRecord;->mServices:Lcom/android/server/am/ProcessServiceRecord;

    invoke-virtual {v4}, Lcom/android/server/am/ProcessServiceRecord;->hasForegroundServices()Z

    move-result v4

    if-nez v4, :cond_5

    :cond_4
    iget-object v4, v5, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v4, v4, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget-object v6, v5, Lcom/android/server/am/ProcessRecord;->processName:Ljava/lang/String;

    invoke-virtual {p0, v4, v6}, Lcom/android/server/am/ProcessSceneCleaner;->isCurrentProcessInBackup(Ljava/lang/String;Ljava/lang/String;)Z

    move-result v4

    if-nez v4, :cond_5

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getPolicy()I

    move-result v6

    iget-object v9, p0, Lcom/android/server/am/ProcessSceneCleaner;->mPMS:Lcom/android/server/am/ProcessManagerService;

    iget-object v11, p0, Lcom/android/server/am/ProcessSceneCleaner;->mHandler:Lcom/android/server/am/ProcessSceneCleaner$H;

    iget-object v12, p0, Lcom/android/server/am/ProcessSceneCleaner;->mContext:Landroid/content/Context;

    const/4 v8, 0x1

    const-string v10, "ProcessSceneCleaner"

    move-object v4, p0

    invoke-virtual/range {v4 .. v12}, Lcom/android/server/am/ProcessSceneCleaner;->killOnce(Lcom/android/server/am/ProcessRecord;ILjava/lang/String;ZLcom/android/server/am/ProcessManagerService;Ljava/lang/String;Landroid/os/Handler;Landroid/content/Context;)V

    :cond_5
    goto :goto_0

    :cond_6
    const/4 v1, 0x1

    return v1

    :cond_7
    :goto_1
    return v1

    :cond_8
    :goto_2
    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "userId:"

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getUserId()I

    move-result v2

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v2, " or taskId:"

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {p1}, Lmiui/process/ProcessConfig;->getTaskId()I

    move-result v2

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v2, " is invalid"

    invoke-virtual {v0, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v2, "ProcessSceneCleaner"

    invoke-static {v2, v0}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    return v1
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
    {
        "id":          "replace_method_killAppForHasOtherTask_ILmiui_process_ProcessConfig__Z",
        "method":      ".method private killAppForHasOtherTask(ILmiui/process/ProcessConfig;)Z",
        "type":        "method_replace",
        "search": """\
.method private killAppForHasOtherTask(ILmiui/process/ProcessConfig;)Z
    .registers 14

    const/4 v0, 0x0

    invoke-static {p1}, Lcom/android/server/wm/WindowProcessUtils;->getTaskTopApp(I)Lcom/android/server/wm/WindowProcessController;

    move-result-object v1

    if-eqz v1, :cond_0

    iget-object v2, v1, Lcom/android/server/wm/WindowProcessController;->mOwner:Ljava/lang/Object;

    move-object v0, v2

    check-cast v0, Lcom/android/server/am/ProcessRecord;

    move-object v3, v0

    goto :goto_0

    :cond_0
    move-object v3, v0

    :goto_0
    if-eqz v3, :cond_2

    nop

    invoke-virtual {v3}, Lcom/android/server/am/ProcessRecord;->getWindowProcessController()Lcom/android/server/wm/WindowProcessController;

    move-result-object v0

    invoke-static {v0, p1}, Lcom/android/server/wm/WindowProcessUtils;->isProcessHasActivityInOtherTaskLocked(Lcom/android/server/wm/WindowProcessController;I)Z

    move-result v0

    if-nez v0, :cond_2

    sget-boolean v2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v2, :cond_1

    iget-object v2, v3, Lcom/android/server/am/ProcessRecord;->mServices:Lcom/android/server/am/ProcessServiceRecord;

    invoke-virtual {v2}, Lcom/android/server/am/ProcessServiceRecord;->hasForegroundServices()Z

    move-result v2

    if-nez v2, :cond_2

    :cond_1
    iget-object v2, v3, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v2, v2, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget-object v4, v3, Lcom/android/server/am/ProcessRecord;->processName:Ljava/lang/String;

    invoke-virtual {p0, v2, v4}, Lcom/android/server/am/ProcessSceneCleaner;->isCurrentProcessInBackup(Ljava/lang/String;Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_2

    invoke-virtual {p2}, Lmiui/process/ProcessConfig;->getPolicy()I

    move-result v4

    invoke-virtual {p2}, Lmiui/process/ProcessConfig;->getPolicy()I

    move-result v2

    invoke-virtual {p0, v2}, Lcom/android/server/am/ProcessSceneCleaner;->getKillReason(I)Ljava/lang/String;

    move-result-object v5

    iget-object v7, p0, Lcom/android/server/am/ProcessSceneCleaner;->mPMS:Lcom/android/server/am/ProcessManagerService;

    iget-object v9, p0, Lcom/android/server/am/ProcessSceneCleaner;->mHandler:Lcom/android/server/am/ProcessSceneCleaner$H;

    iget-object v10, p0, Lcom/android/server/am/ProcessSceneCleaner;->mContext:Landroid/content/Context;

    const/4 v6, 0x0

    const-string v8, "ProcessSceneCleaner"

    move-object v2, p0

    invoke-virtual/range {v2 .. v10}, Lcom/android/server/am/ProcessSceneCleaner;->killOnce(Lcom/android/server/am/ProcessRecord;ILjava/lang/String;ZLcom/android/server/am/ProcessManagerService;Ljava/lang/String;Landroid/os/Handler;Landroid/content/Context;)V

    :cond_2
    const/4 v0, 0x1

    return v0
.end method
""",
        "replacement": """\
.method private killAppForHasOtherTask(ILmiui/process/ProcessConfig;)Z
    .registers 14

    const/4 v0, 0x0

    invoke-static {p1}, Lcom/android/server/wm/WindowProcessUtils;->getTaskTopApp(I)Lcom/android/server/wm/WindowProcessController;

    move-result-object v1

    if-eqz v1, :cond_0

    iget-object v2, v1, Lcom/android/server/wm/WindowProcessController;->mOwner:Ljava/lang/Object;

    move-object v0, v2

    check-cast v0, Lcom/android/server/am/ProcessRecord;

    move-object v3, v0

    goto :goto_0

    :cond_0
    move-object v3, v0

    :goto_0
    if-eqz v3, :cond_2

    nop

    invoke-virtual {v3}, Lcom/android/server/am/ProcessRecord;->getWindowProcessController()Lcom/android/server/wm/WindowProcessController;

    move-result-object v0

    invoke-static {v0, p1}, Lcom/android/server/wm/WindowProcessUtils;->isProcessHasActivityInOtherTaskLocked(Lcom/android/server/wm/WindowProcessController;I)Z

    move-result v0

    if-nez v0, :cond_2

    sget-boolean v2, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v2, 0x1

    if-eqz v2, :cond_1

    iget-object v2, v3, Lcom/android/server/am/ProcessRecord;->mServices:Lcom/android/server/am/ProcessServiceRecord;

    invoke-virtual {v2}, Lcom/android/server/am/ProcessServiceRecord;->hasForegroundServices()Z

    move-result v2

    if-nez v2, :cond_2

    :cond_1
    iget-object v2, v3, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v2, v2, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget-object v4, v3, Lcom/android/server/am/ProcessRecord;->processName:Ljava/lang/String;

    invoke-virtual {p0, v2, v4}, Lcom/android/server/am/ProcessSceneCleaner;->isCurrentProcessInBackup(Ljava/lang/String;Ljava/lang/String;)Z

    move-result v2

    if-nez v2, :cond_2

    invoke-virtual {p2}, Lmiui/process/ProcessConfig;->getPolicy()I

    move-result v4

    invoke-virtual {p2}, Lmiui/process/ProcessConfig;->getPolicy()I

    move-result v2

    invoke-virtual {p0, v2}, Lcom/android/server/am/ProcessSceneCleaner;->getKillReason(I)Ljava/lang/String;

    move-result-object v5

    iget-object v7, p0, Lcom/android/server/am/ProcessSceneCleaner;->mPMS:Lcom/android/server/am/ProcessManagerService;

    iget-object v9, p0, Lcom/android/server/am/ProcessSceneCleaner;->mHandler:Lcom/android/server/am/ProcessSceneCleaner$H;

    iget-object v10, p0, Lcom/android/server/am/ProcessSceneCleaner;->mContext:Landroid/content/Context;

    const/4 v6, 0x0

    const-string v8, "ProcessSceneCleaner"

    move-object v2, p0

    invoke-virtual/range {v2 .. v10}, Lcom/android/server/am/ProcessSceneCleaner;->killOnce(Lcom/android/server/am/ProcessRecord;ILjava/lang/String;ZLcom/android/server/am/ProcessManagerService;Ljava/lang/String;Landroid/os/Handler;Landroid/content/Context;)V

    :cond_2
    const/4 v0, 0x1

    return v0
.end method
""",
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
]
