"""
Legend MTCR patch - class-level rule.

Target JAR   : services.jar
Target class : com/android/server/wm/WindowManagerService
Source MTCR  : Service_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "services.jar"
TARGET_CLASS = "com/android/server/wm/WindowManagerService.smali"
CLASS_FALLBACK_NAMES = ['WindowManagerService.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "replace_method_addWindowChangeListener_Lcom_android_server_wm_WindowManager",
        "method":      ".method addWindowChangeListener(Lcom/android/server/wm/WindowManagerService$WindowChangeListener;)V",
        "method_name": 'addWindowChangeListener',
        "type":        "method_replace",
        "search": """\
.method addWindowChangeListener(Lcom/android/server/wm/WindowManagerService$WindowChangeListener;)V
    .registers 4

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowChangeListeners:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method addWindowChangeListener(Lcom/android/server/wm/WindowManagerService$WindowChangeListener;)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_4

    nop

    :goto_1
    throw v1

    :goto_2
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_0

    nop

    :goto_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_5

    nop

    :goto_4
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowChangeListeners:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_3

    nop

    :goto_5
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_6

    nop

    :goto_6
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowChangeListeners:Ljava/util/ArrayList;', 'invoke-virtual {v1, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_addWindowFocusChangeListener_Lcom_android_server_wm_WindowMa",
        "method":      ".method addWindowFocusChangeListener(Lcom/android/server/wm/WindowManagerInternal$WindowFocusChangeListener;)V",
        "method_name": 'addWindowFocusChangeListener',
        "type":        "method_replace",
        "search": """\
.method addWindowFocusChangeListener(Lcom/android/server/wm/WindowManagerInternal$WindowFocusChangeListener;)V
    .registers 4

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowFocusChangeListeners:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method addWindowFocusChangeListener(Lcom/android/server/wm/WindowManagerInternal$WindowFocusChangeListener;)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    throw v1

    :goto_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_5

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_6

    nop

    :goto_3
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowFocusChangeListeners:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_0

    nop

    :goto_5
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_4

    nop

    :goto_6
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowFocusChangeListeners:Ljava/util/ArrayList;', 'invoke-virtual {v1, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_checkCallingPermission_Ljava_lang_String_Ljava_lang_String__",
        "method":      ".method checkCallingPermission(Ljava/lang/String;Ljava/lang/String;)Z",
        "method_name": 'checkCallingPermission',
        "type":        "method_replace",
        "search": """\
.method checkCallingPermission(Ljava/lang/String;Ljava/lang/String;)Z
    .registers 4

    const/4 v0, 0x1

    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/wm/WindowManagerService;->checkCallingPermission(Ljava/lang/String;Ljava/lang/String;Z)Z

    move-result v0

    return v0
.end method
""",
        "replacement": """\
.method checkCallingPermission(Ljava/lang/String;Ljava/lang/String;)Z
    .registers 4

    goto :goto_0

    nop

    :goto_0
    const/4 v0, 0x1

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/wm/WindowManagerService;->checkCallingPermission(Ljava/lang/String;Ljava/lang/String;Z)Z

    move-result v0

    goto :goto_2

    nop

    :goto_2
    return v0
.end method
""",
        "method_anchors": ['invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/wm/WindowManagerService;->checkCallingPermission(Ljava/lang/String;Ljava/lang/String;Z)Z', 'move-result v0', 'return v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_checkCallingPermission_Ljava_lang_String_Ljava_lang_String_Z",
        "method":      ".method checkCallingPermission(Ljava/lang/String;Ljava/lang/String;Z)Z",
        "method_name": 'checkCallingPermission',
        "type":        "method_replace",
        "search": """\
.method checkCallingPermission(Ljava/lang/String;Ljava/lang/String;Z)Z
    .registers 15

    invoke-static {}, Landroid/os/Binder;->getCallingPid()I

    move-result v0

    sget v1, Lcom/android/server/wm/WindowManagerService;->MY_PID:I

    const/4 v2, 0x1

    if-ne v0, v1, :cond_0

    return v2

    :cond_0
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mContext:Landroid/content/Context;

    invoke-virtual {v0, p1}, Landroid/content/Context;->checkCallingPermission(Ljava/lang/String;)I

    move-result v0

    if-nez v0, :cond_1

    return v2

    :cond_1
    if-eqz p3, :cond_2

    sget-object v0, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    const/4 v1, 0x3

    aget-boolean v0, v0, v1

    if-eqz v0, :cond_2

    invoke-static {p2}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    invoke-static {}, Landroid/os/Binder;->getCallingPid()I

    move-result v1

    int-to-long v1, v1

    invoke-static {}, Landroid/os/Binder;->getCallingUid()I

    move-result v3

    int-to-long v3, v3

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    sget-object v6, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    invoke-static {v1, v2}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v7

    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v8

    filled-new-array {v0, v7, v8, v5}, [Ljava/lang/Object;

    move-result-object v7

    const-wide v8, -0x23c6227df4a7cc70L

    const/16 v10, 0x14

    invoke-static {v6, v8, v9, v10, v7}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_2
    const/4 v0, 0x0

    return v0
.end method
""",
        "replacement": """\
.method checkCallingPermission(Ljava/lang/String;Ljava/lang/String;Z)Z
    .registers 15

    goto :goto_17

    nop

    :goto_0
    return v2

    :goto_1
    goto :goto_9

    nop

    :goto_2
    sget-object v0, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    goto :goto_19

    nop

    :goto_3
    const/16 v10, 0x14

    goto :goto_1e

    nop

    :goto_4
    invoke-virtual {v0, p1}, Landroid/content/Context;->checkCallingPermission(Ljava/lang/String;)I

    move-result v0

    goto :goto_12

    nop

    :goto_5
    return v0

    :goto_6
    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v8

    goto :goto_1c

    nop

    :goto_7
    const/4 v2, 0x1

    goto :goto_13

    nop

    :goto_8
    int-to-long v1, v1

    goto :goto_c

    nop

    :goto_9
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mContext:Landroid/content/Context;

    goto :goto_4

    nop

    :goto_a
    invoke-static {v1, v2}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v7

    goto :goto_6

    nop

    :goto_b
    if-nez p3, :cond_0

    goto :goto_1f

    :cond_0
    goto :goto_2

    nop

    :goto_c
    invoke-static {}, Landroid/os/Binder;->getCallingUid()I

    move-result v3

    goto :goto_f

    nop

    :goto_d
    const/4 v0, 0x0

    goto :goto_5

    nop

    :goto_e
    const-wide v8, -0x23c6227df4a7cc70L

    goto :goto_3

    nop

    :goto_f
    int-to-long v3, v3

    goto :goto_11

    nop

    :goto_10
    invoke-static {}, Landroid/os/Binder;->getCallingPid()I

    move-result v1

    goto :goto_8

    nop

    :goto_11
    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    goto :goto_1b

    nop

    :goto_12
    if-eqz v0, :cond_1

    goto :goto_16

    :cond_1
    goto :goto_15

    nop

    :goto_13
    if-eq v0, v1, :cond_2

    goto :goto_1

    :cond_2
    goto :goto_0

    nop

    :goto_14
    if-nez v0, :cond_3

    goto :goto_1f

    :cond_3
    goto :goto_1d

    nop

    :goto_15
    return v2

    :goto_16
    goto :goto_b

    nop

    :goto_17
    invoke-static {}, Landroid/os/Binder;->getCallingPid()I

    move-result v0

    goto :goto_18

    nop

    :goto_18
    sget v1, Lcom/android/server/wm/WindowManagerService;->MY_PID:I

    goto :goto_7

    nop

    :goto_19
    const/4 v1, 0x3

    goto :goto_1a

    nop

    :goto_1a
    aget-boolean v0, v0, v1

    goto :goto_14

    nop

    :goto_1b
    sget-object v6, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    goto :goto_a

    nop

    :goto_1c
    filled-new-array {v0, v7, v8, v5}, [Ljava/lang/Object;

    move-result-object v7

    goto :goto_e

    nop

    :goto_1d
    invoke-static {p2}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v0

    goto :goto_10

    nop

    :goto_1e
    invoke-static {v6, v8, v9, v10, v7}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :goto_1f
    goto :goto_d

    nop
.end method
""",
        "method_anchors": ['invoke-static {}, Landroid/os/Binder;->getCallingPid()I', 'move-result v0', 'sget v1, Lcom/android/server/wm/WindowManagerService;->MY_PID:I', 'if-ne v0, v1, :cond_0', 'return v2', 'iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mContext:Landroid/content/Context;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_checkDrawnWindowsLocked__V",
        "method":      ".method checkDrawnWindowsLocked()V",
        "method_name": 'checkDrawnWindowsLocked',
        "type":        "method_replace",
        "search": """\
.method checkDrawnWindowsLocked()V
    .registers 19

    move-object/from16 v0, p0

    const-string v1, "com.android.server.wm.WindowManagerService.checkDrawnWindowsLocked()V"

    invoke-static {v1}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v2, v0, Lcom/android/server/wm/WindowManagerService;->mWaitingForDrawnCallbacks:Landroid/util/ArrayMap;

    invoke-virtual {v2}, Landroid/util/ArrayMap;->isEmpty()Z

    move-result v2

    if-eqz v2, :cond_0

    invoke-static {v1}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-void

    :cond_0
    iget-object v2, v0, Lcom/android/server/wm/WindowManagerService;->mWaitingForDrawnCallbacks:Landroid/util/ArrayMap;

    invoke-virtual {v2}, Landroid/util/ArrayMap;->size()I

    move-result v2

    const/4 v3, 0x1

    sub-int/2addr v2, v3

    :goto_0
    if-ltz v2, :cond_a

    iget-object v4, v0, Lcom/android/server/wm/WindowManagerService;->mWaitingForDrawnCallbacks:Landroid/util/ArrayMap;

    invoke-virtual {v4, v2}, Landroid/util/ArrayMap;->keyAt(I)Ljava/lang/Object;

    move-result-object v4

    check-cast v4, Lcom/android/server/wm/WindowContainer;

    iget-object v5, v4, Lcom/android/server/wm/WindowContainer;->mWaitingForDrawn:Ljava/util/ArrayList;

    invoke-virtual {v5}, Ljava/util/ArrayList;->size()I

    move-result v5

    sub-int/2addr v5, v3

    :goto_1
    if-ltz v5, :cond_7

    iget-object v7, v4, Lcom/android/server/wm/WindowContainer;->mWaitingForDrawn:Ljava/util/ArrayList;

    invoke-virtual {v7, v5}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v7

    check-cast v7, Lcom/android/server/wm/WindowState;

    sget-object v8, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_SCREEN_ON_enabled:[Z

    const/4 v9, 0x2

    aget-boolean v8, v8, v9

    if-eqz v8, :cond_1

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    iget-boolean v9, v7, Lcom/android/server/wm/WindowState;->mRemoved:Z

    invoke-virtual {v7}, Lcom/android/server/wm/WindowState;->isVisible()Z

    move-result v10

    iget-boolean v11, v7, Lcom/android/server/wm/WindowState;->mHasSurface:Z

    iget-object v12, v7, Lcom/android/server/wm/WindowState;->mWinAnimator:Lcom/android/server/wm/WindowStateAnimator;

    iget v12, v12, Lcom/android/server/wm/WindowStateAnimator;->mDrawState:I

    int-to-long v12, v12

    sget-object v14, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_SCREEN_ON:Lcom/android/internal/protolog/WmProtoLogGroups;

    invoke-static {v9}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v15

    move/from16 v16, v3

    invoke-static {v10}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v3

    invoke-static {v11}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v6
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    move-object/from16 v17, v1

    :try_start_1
    invoke-static {v12, v13}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v1

    filled-new-array {v8, v15, v3, v6, v1}, [Ljava/lang/Object;

    move-result-object v1

    move v3, v5

    const-wide v5, -0x17d0932393c0c518L

    const/16 v15, 0x1fc

    invoke-static {v14, v5, v6, v15, v1}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->i(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    goto :goto_2

    :cond_1
    move-object/from16 v17, v1

    move/from16 v16, v3

    move v3, v5

    :goto_2
    iget-boolean v1, v7, Lcom/android/server/wm/WindowState;->mRemoved:Z

    const-wide/16 v5, 0x20

    if-nez v1, :cond_4

    iget-boolean v1, v7, Lcom/android/server/wm/WindowState;->mHasSurface:Z

    if-eqz v1, :cond_4

    invoke-virtual {v7}, Lcom/android/server/wm/WindowState;->isVisibleByPolicy()Z

    move-result v1

    if-nez v1, :cond_2

    goto :goto_3

    :cond_2
    invoke-virtual {v7}, Lcom/android/server/wm/WindowState;->hasDrawn()Z

    move-result v1

    if-eqz v1, :cond_6

    sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_SCREEN_ON_enabled:[Z

    aget-boolean v1, v1, v16

    if-eqz v1, :cond_3

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    sget-object v8, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_SCREEN_ON:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v9

    const-wide v10, -0x68ee4319bba7ca6eL

    const/4 v12, 0x0

    invoke-static {v8, v10, v11, v12, v9}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->d(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_3
    iget-object v1, v4, Lcom/android/server/wm/WindowContainer;->mWaitingForDrawn:Ljava/util/ArrayList;

    invoke-virtual {v1, v7}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    invoke-static {v5, v6}, Landroid/os/Trace;->isTagEnabled(J)Z

    move-result v1

    if-eqz v1, :cond_6

    invoke-direct {v0, v7}, Lcom/android/server/wm/WindowManagerService;->traceEndWaitingForWindowDrawn(Lcom/android/server/wm/WindowState;)V

    goto :goto_4

    :cond_4
    :goto_3
    sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_SCREEN_ON_enabled:[Z

    const/4 v8, 0x3

    aget-boolean v1, v1, v8

    if-eqz v1, :cond_5

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    sget-object v8, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_SCREEN_ON:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v9

    const-wide v10, -0x3ff96653edbfc371L

    const/4 v12, 0x0

    invoke-static {v8, v10, v11, v12, v9}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_5
    iget-object v1, v4, Lcom/android/server/wm/WindowContainer;->mWaitingForDrawn:Ljava/util/ArrayList;

    invoke-virtual {v1, v7}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    invoke-static {v5, v6}, Landroid/os/Trace;->isTagEnabled(J)Z

    move-result v1

    if-eqz v1, :cond_6

    invoke-direct {v0, v7}, Lcom/android/server/wm/WindowManagerService;->traceEndWaitingForWindowDrawn(Lcom/android/server/wm/WindowState;)V

    :cond_6
    :goto_4
    add-int/lit8 v5, v3, -0x1

    move/from16 v3, v16

    move-object/from16 v1, v17

    goto :goto_1

    :cond_7
    move-object/from16 v17, v1

    move/from16 v16, v3

    move v3, v5

    iget-object v1, v4, Lcom/android/server/wm/WindowContainer;->mWaitingForDrawn:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v1

    if-eqz v1, :cond_9

    sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_SCREEN_ON_enabled:[Z

    aget-boolean v1, v1, v16

    if-eqz v1, :cond_8

    sget-object v1, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_SCREEN_ON:Lcom/android/internal/protolog/WmProtoLogGroups;

    const/4 v3, 0x0

    move-object v5, v3

    check-cast v5, [Ljava/lang/Object;

    const-wide v5, 0x26fbade8f5c830d6L

    const/4 v12, 0x0

    invoke-static {v1, v5, v6, v12, v3}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->d(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_8
    iget-object v1, v0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    const/16 v3, 0x18

    invoke-virtual {v1, v3, v4}, Lcom/android/server/wm/WindowManagerService$H;->removeMessages(ILjava/lang/Object;)V

    iget-object v1, v0, Lcom/android/server/wm/WindowManagerService;->mWaitingForDrawnCallbacks:Landroid/util/ArrayMap;

    invoke-virtual {v1, v2}, Landroid/util/ArrayMap;->removeAt(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/os/Message;

    invoke-virtual {v1}, Landroid/os/Message;->sendToTarget()V

    :cond_9
    add-int/lit8 v2, v2, -0x1

    move/from16 v3, v16

    move-object/from16 v1, v17

    goto :goto_0

    :cond_a
    move-object/from16 v17, v1

    invoke-static/range {v17 .. v17}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    return-void

    :catchall_0
    move-exception v0

    goto :goto_5

    :catchall_1
    move-exception v0

    move-object/from16 v17, v1

    :goto_5
    invoke-static/range {v17 .. v17}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw v0
.end method
""",
        "replacement": """\
.method checkDrawnWindowsLocked()V
    .registers 19

    goto :goto_9

    nop

    :goto_0
    throw v0

    :goto_1
    move-object/from16 v17, v1

    :goto_2
    goto :goto_e

    nop

    :goto_3
    const-string v1, "com.android.server.wm.WindowManagerService.checkDrawnWindowsLocked()V"

    goto :goto_a

    nop

    :goto_4
    move-object/from16 v17, v1

    :try_start_0
    invoke-static {v12, v13}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v1

    filled-new-array {v8, v15, v3, v6, v1}, [Ljava/lang/Object;

    move-result-object v1

    move v3, v5

    const-wide v5, -0x17d0932393c0c518L

    const/16 v15, 0x1fc

    invoke-static {v14, v5, v6, v15, v1}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->i(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    goto :goto_5

    :cond_0
    move-object/from16 v17, v1

    move/from16 v16, v3

    move v3, v5

    :goto_5
    iget-boolean v1, v7, Lcom/android/server/wm/WindowState;->mRemoved:Z

    const-wide/16 v5, 0x20

    if-nez v1, :cond_3

    iget-boolean v1, v7, Lcom/android/server/wm/WindowState;->mHasSurface:Z

    if-eqz v1, :cond_3

    invoke-virtual {v7}, Lcom/android/server/wm/WindowState;->isVisibleByPolicy()Z

    move-result v1

    if-nez v1, :cond_1

    goto :goto_6

    :cond_1
    invoke-virtual {v7}, Lcom/android/server/wm/WindowState;->hasDrawn()Z

    move-result v1

    if-eqz v1, :cond_5

    sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_SCREEN_ON_enabled:[Z

    aget-boolean v1, v1, v16

    if-eqz v1, :cond_2

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    sget-object v8, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_SCREEN_ON:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v9

    const-wide v10, -0x68ee4319bba7ca6eL

    const/4 v12, 0x0

    invoke-static {v8, v10, v11, v12, v9}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->d(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_2
    iget-object v1, v4, Lcom/android/server/wm/WindowContainer;->mWaitingForDrawn:Ljava/util/ArrayList;

    invoke-virtual {v1, v7}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    invoke-static {v5, v6}, Landroid/os/Trace;->isTagEnabled(J)Z

    move-result v1

    if-eqz v1, :cond_5

    invoke-direct {v0, v7}, Lcom/android/server/wm/WindowManagerService;->traceEndWaitingForWindowDrawn(Lcom/android/server/wm/WindowState;)V

    goto :goto_7

    :cond_3
    :goto_6
    sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_SCREEN_ON_enabled:[Z

    const/4 v8, 0x3

    aget-boolean v1, v1, v8

    if-eqz v1, :cond_4

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    sget-object v8, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_SCREEN_ON:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v9

    const-wide v10, -0x3ff96653edbfc371L

    const/4 v12, 0x0

    invoke-static {v8, v10, v11, v12, v9}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_4
    iget-object v1, v4, Lcom/android/server/wm/WindowContainer;->mWaitingForDrawn:Ljava/util/ArrayList;

    invoke-virtual {v1, v7}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    invoke-static {v5, v6}, Landroid/os/Trace;->isTagEnabled(J)Z

    move-result v1

    if-eqz v1, :cond_5

    invoke-direct {v0, v7}, Lcom/android/server/wm/WindowManagerService;->traceEndWaitingForWindowDrawn(Lcom/android/server/wm/WindowState;)V

    :cond_5
    :goto_7
    add-int/lit8 v5, v3, -0x1

    move/from16 v3, v16

    move-object/from16 v1, v17

    goto :goto_c

    :cond_6
    move-object/from16 v17, v1

    move/from16 v16, v3

    move v3, v5

    iget-object v1, v4, Lcom/android/server/wm/WindowContainer;->mWaitingForDrawn:Ljava/util/ArrayList;

    invoke-virtual {v1}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v1

    if-eqz v1, :cond_8

    sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_SCREEN_ON_enabled:[Z

    aget-boolean v1, v1, v16

    if-eqz v1, :cond_7

    sget-object v1, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_SCREEN_ON:Lcom/android/internal/protolog/WmProtoLogGroups;

    const/4 v3, 0x0

    move-object v5, v3

    check-cast v5, [Ljava/lang/Object;

    const-wide v5, 0x26fbade8f5c830d6L

    const/4 v12, 0x0

    invoke-static {v1, v5, v6, v12, v3}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->d(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_7
    iget-object v1, v0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    const/16 v3, 0x18

    invoke-virtual {v1, v3, v4}, Lcom/android/server/wm/WindowManagerService$H;->removeMessages(ILjava/lang/Object;)V

    iget-object v1, v0, Lcom/android/server/wm/WindowManagerService;->mWaitingForDrawnCallbacks:Landroid/util/ArrayMap;

    invoke-virtual {v1, v2}, Landroid/util/ArrayMap;->removeAt(I)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Landroid/os/Message;

    invoke-virtual {v1}, Landroid/os/Message;->sendToTarget()V

    :cond_8
    add-int/lit8 v2, v2, -0x1

    move/from16 v3, v16

    move-object/from16 v1, v17

    goto :goto_b

    :cond_9
    move-object/from16 v17, v1

    invoke-static/range {v17 .. v17}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    goto :goto_d

    nop

    :goto_8
    goto :goto_2

    :catchall_0
    move-exception v0

    goto :goto_1

    nop

    :goto_9
    move-object/from16 v0, p0

    goto :goto_3

    nop

    :goto_a
    invoke-static {v1}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_1
    iget-object v2, v0, Lcom/android/server/wm/WindowManagerService;->mWaitingForDrawnCallbacks:Landroid/util/ArrayMap;

    invoke-virtual {v2}, Landroid/util/ArrayMap;->isEmpty()Z

    move-result v2

    if-eqz v2, :cond_a

    invoke-static {v1}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-void

    :cond_a
    iget-object v2, v0, Lcom/android/server/wm/WindowManagerService;->mWaitingForDrawnCallbacks:Landroid/util/ArrayMap;

    invoke-virtual {v2}, Landroid/util/ArrayMap;->size()I

    move-result v2

    const/4 v3, 0x1

    sub-int/2addr v2, v3

    :goto_b
    if-ltz v2, :cond_9

    iget-object v4, v0, Lcom/android/server/wm/WindowManagerService;->mWaitingForDrawnCallbacks:Landroid/util/ArrayMap;

    invoke-virtual {v4, v2}, Landroid/util/ArrayMap;->keyAt(I)Ljava/lang/Object;

    move-result-object v4

    check-cast v4, Lcom/android/server/wm/WindowContainer;

    iget-object v5, v4, Lcom/android/server/wm/WindowContainer;->mWaitingForDrawn:Ljava/util/ArrayList;

    invoke-virtual {v5}, Ljava/util/ArrayList;->size()I

    move-result v5

    sub-int/2addr v5, v3

    :goto_c
    if-ltz v5, :cond_6

    iget-object v7, v4, Lcom/android/server/wm/WindowContainer;->mWaitingForDrawn:Ljava/util/ArrayList;

    invoke-virtual {v7, v5}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v7

    check-cast v7, Lcom/android/server/wm/WindowState;

    sget-object v8, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_SCREEN_ON_enabled:[Z

    const/4 v9, 0x2

    aget-boolean v8, v8, v9

    if-eqz v8, :cond_0

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    iget-boolean v9, v7, Lcom/android/server/wm/WindowState;->mRemoved:Z

    invoke-virtual {v7}, Lcom/android/server/wm/WindowState;->isVisible()Z

    move-result v10

    iget-boolean v11, v7, Lcom/android/server/wm/WindowState;->mHasSurface:Z

    iget-object v12, v7, Lcom/android/server/wm/WindowState;->mWinAnimator:Lcom/android/server/wm/WindowStateAnimator;

    iget v12, v12, Lcom/android/server/wm/WindowStateAnimator;->mDrawState:I

    int-to-long v12, v12

    sget-object v14, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_SCREEN_ON:Lcom/android/internal/protolog/WmProtoLogGroups;

    invoke-static {v9}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v15

    move/from16 v16, v3

    invoke-static {v10}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v3

    invoke-static {v11}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v6
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_4

    nop

    :goto_d
    return-void

    :catchall_1
    move-exception v0

    goto :goto_8

    nop

    :goto_e
    invoke-static/range {v17 .. v17}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['const-string v1, "com.android.server.wm.WindowManagerService.checkDrawnWindowsLocked()V"', 'invoke-static {v1}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'iget-object v2, v0, Lcom/android/server/wm/WindowManagerService;->mWaitingForDrawnCallbacks:Landroid/util/ArrayMap;', 'invoke-virtual {v2}, Landroid/util/ArrayMap;->isEmpty()Z', 'move-result v2', 'if-eqz v2, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_clearPointerDownOutsideFocusRunnable__V",
        "method":      ".method clearPointerDownOutsideFocusRunnable()V",
        "method_name": 'clearPointerDownOutsideFocusRunnable',
        "type":        "method_replace",
        "search": """\
.method clearPointerDownOutsideFocusRunnable()V
    .registers 3

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mPointerDownOutsideFocusRunnable:Ljava/lang/Runnable;

    if-nez v0, :cond_0

    return-void

    :cond_0
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mPointerDownOutsideFocusRunnable:Ljava/lang/Runnable;

    invoke-virtual {v0, v1}, Lcom/android/server/wm/WindowManagerService$H;->removeCallbacks(Ljava/lang/Runnable;)V

    const/4 v0, 0x0

    iput-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mPointerDownOutsideFocusRunnable:Ljava/lang/Runnable;

    return-void
.end method
""",
        "replacement": """\
.method clearPointerDownOutsideFocusRunnable()V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    goto :goto_3

    nop

    :goto_1
    return-void

    :goto_2
    iput-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mPointerDownOutsideFocusRunnable:Ljava/lang/Runnable;

    goto :goto_1

    nop

    :goto_3
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mPointerDownOutsideFocusRunnable:Ljava/lang/Runnable;

    goto :goto_9

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mPointerDownOutsideFocusRunnable:Ljava/lang/Runnable;

    goto :goto_7

    nop

    :goto_5
    return-void

    :goto_6
    goto :goto_0

    nop

    :goto_7
    if-eqz v0, :cond_0

    goto :goto_6

    :cond_0
    goto :goto_5

    nop

    :goto_8
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_9
    invoke-virtual {v0, v1}, Lcom/android/server/wm/WindowManagerService$H;->removeCallbacks(Ljava/lang/Runnable;)V

    goto :goto_8

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mPointerDownOutsideFocusRunnable:Ljava/lang/Runnable;', 'if-nez v0, :cond_0', 'return-void', 'iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mPointerDownOutsideFocusRunnable:Ljava/lang/Runnable;', 'invoke-virtual {v0, v1}, Lcom/android/server/wm/WindowManagerService$H;->removeCallbacks(Ljava/lang/Runnable;)V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_clearTouchableRegion_Lcom_android_server_wm_Session_Landroid",
        "method":      ".method clearTouchableRegion(Lcom/android/server/wm/Session;Landroid/view/IWindow;)V",
        "method_name": 'clearTouchableRegion',
        "type":        "method_replace",
        "search": """\
.method clearTouchableRegion(Lcom/android/server/wm/Session;Landroid/view/IWindow;)V
    .registers 7

    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v0

    :try_start_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    const/4 v3, 0x0

    :try_start_1
    invoke-virtual {p0, p1, p2, v3}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v3

    invoke-virtual {v3}, Lcom/android/server/wm/WindowState;->clearClientTouchableRegion()V

    monitor-exit v2
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :try_start_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    nop

    return-void

    :catchall_0
    move-exception v3

    :try_start_3
    monitor-exit v2
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v3
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_1

    :catchall_1
    move-exception v2

    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    throw v2
.end method
""",
        "replacement": """\
.method clearTouchableRegion(Lcom/android/server/wm/Session;Landroid/view/IWindow;)V
    .registers 7

    goto :goto_4

    nop

    :goto_0
    throw v2

    :goto_1
    const/4 v3, 0x0

    :try_start_0
    invoke-virtual {p0, p1, p2, v3}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v3

    invoke-virtual {v3}, Lcom/android/server/wm/WindowState;->clearClientTouchableRegion()V

    monitor-exit v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :try_start_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    goto :goto_2

    nop

    :goto_2
    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    nop

    goto :goto_5

    nop

    :goto_3
    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    goto :goto_0

    nop

    :goto_4
    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v0

    :try_start_2
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    goto :goto_1

    nop

    :goto_5
    return-void

    :catchall_0
    move-exception v3

    :try_start_3
    monitor-exit v2
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v3
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_1

    :catchall_1
    move-exception v2

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J', 'move-result-wide v0', 'iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'invoke-virtual {p0, p1, p2, v3}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;', 'move-result-object v3'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_createWatermark__V",
        "method":      ".method createWatermark()V",
        "method_name": 'createWatermark',
        "type":        "method_replace",
        "search": """\
.method createWatermark()V
    .registers 10

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mWatermark:Lcom/android/server/wm/Watermark;

    if-eqz v0, :cond_0

    return-void

    :cond_0
    new-instance v0, Ljava/io/File;

    const-string v1, "/system/etc/setup.conf"

    invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    const/4 v1, 0x0

    const/4 v2, 0x0

    :try_start_0
    new-instance v3, Ljava/io/FileInputStream;

    invoke-direct {v3, v0}, Ljava/io/FileInputStream;-><init>(Ljava/io/File;)V

    move-object v1, v3

    new-instance v3, Ljava/io/DataInputStream;

    invoke-direct {v3, v1}, Ljava/io/DataInputStream;-><init>(Ljava/io/InputStream;)V

    move-object v2, v3

    invoke-virtual {v2}, Ljava/io/DataInputStream;->readLine()Ljava/lang/String;

    move-result-object v3

    if-eqz v3, :cond_1

    const-string v4, "%"

    invoke-virtual {v3, v4}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v4

    if-eqz v4, :cond_1

    array-length v5, v4

    if-lez v5, :cond_1

    invoke-virtual {p0}, Lcom/android/server/wm/WindowManagerService;->getDefaultDisplayContentLocked()Lcom/android/server/wm/DisplayContent;

    move-result-object v5

    new-instance v6, Lcom/android/server/wm/Watermark;

    iget-object v7, v5, Lcom/android/server/wm/DisplayContent;->mRealDisplayMetrics:Landroid/util/DisplayMetrics;

    iget-object v8, p0, Lcom/android/server/wm/WindowManagerService;->mTransaction:Landroid/view/SurfaceControl$Transaction;

    invoke-direct {v6, v5, v7, v4, v8}, Lcom/android/server/wm/Watermark;-><init>(Lcom/android/server/wm/DisplayContent;Landroid/util/DisplayMetrics;[Ljava/lang/String;Landroid/view/SurfaceControl$Transaction;)V

    iput-object v6, p0, Lcom/android/server/wm/WindowManagerService;->mWatermark:Lcom/android/server/wm/Watermark;

    iget-object v6, p0, Lcom/android/server/wm/WindowManagerService;->mTransaction:Landroid/view/SurfaceControl$Transaction;

    invoke-virtual {v6}, Landroid/view/SurfaceControl$Transaction;->apply()V
    :try_end_0
    .catch Ljava/io/FileNotFoundException; {:try_start_0 .. :try_end_0} :catch_5
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_3
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :cond_1
    nop

    :try_start_1
    invoke-virtual {v2}, Ljava/io/DataInputStream;->close()V
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_0

    :goto_0
    goto :goto_4

    :catch_0
    move-exception v3

    goto :goto_0

    :catchall_0
    move-exception v3

    if-nez v2, :cond_2

    if-eqz v1, :cond_3

    :try_start_2
    invoke-virtual {v1}, Ljava/io/FileInputStream;->close()V
    :try_end_2
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_1

    goto :goto_2

    :catch_1
    move-exception v4

    goto :goto_2

    :cond_2
    :try_start_3
    invoke-virtual {v2}, Ljava/io/DataInputStream;->close()V
    :try_end_3
    .catch Ljava/io/IOException; {:try_start_3 .. :try_end_3} :catch_2

    :goto_1
    goto :goto_2

    :catch_2
    move-exception v4

    goto :goto_1

    :cond_3
    :goto_2
    throw v3

    :catch_3
    move-exception v3

    if-eqz v2, :cond_4

    :try_start_4
    invoke-virtual {v2}, Ljava/io/DataInputStream;->close()V
    :try_end_4
    .catch Ljava/io/IOException; {:try_start_4 .. :try_end_4} :catch_0

    goto :goto_0

    :cond_4
    if-eqz v1, :cond_6

    :try_start_5
    invoke-virtual {v1}, Ljava/io/FileInputStream;->close()V
    :try_end_5
    .catch Ljava/io/IOException; {:try_start_5 .. :try_end_5} :catch_4

    :goto_3
    goto :goto_4

    :catch_4
    move-exception v3

    goto :goto_3

    :catch_5
    move-exception v3

    if-eqz v2, :cond_5

    :try_start_6
    invoke-virtual {v2}, Ljava/io/DataInputStream;->close()V
    :try_end_6
    .catch Ljava/io/IOException; {:try_start_6 .. :try_end_6} :catch_0

    goto :goto_0

    :cond_5
    if-eqz v1, :cond_6

    :try_start_7
    invoke-virtual {v1}, Ljava/io/FileInputStream;->close()V
    :try_end_7
    .catch Ljava/io/IOException; {:try_start_7 .. :try_end_7} :catch_4

    goto :goto_3

    :cond_6
    :goto_4
    return-void
.end method
""",
        "replacement": """\
.method createWatermark()V
    .registers 10

    goto :goto_17

    nop

    :goto_0
    if-nez v2, :cond_0

    goto :goto_10

    :cond_0
    :try_start_0
    invoke-virtual {v2}, Ljava/io/DataInputStream;->close()V
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_0

    goto :goto_f

    nop

    :goto_1
    new-instance v0, Ljava/io/File;

    goto :goto_12

    nop

    :goto_2
    goto :goto_19

    :catch_0
    move-exception v3

    goto :goto_16

    nop

    :goto_3
    goto :goto_a

    :catch_1
    move-exception v3

    goto :goto_1a

    nop

    :goto_4
    invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    goto :goto_23

    nop

    :goto_5
    goto :goto_21

    :catch_2
    move-exception v4

    goto :goto_1b

    nop

    :goto_6
    return-void

    :goto_7
    return-void

    :goto_8
    goto :goto_1

    nop

    :goto_9
    if-nez v1, :cond_1

    goto :goto_19

    :cond_1
    :try_start_1
    invoke-virtual {v1}, Ljava/io/FileInputStream;->close()V
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_3

    :goto_a
    goto :goto_11

    nop

    :goto_b
    const/4 v2, 0x0

    :try_start_2
    new-instance v3, Ljava/io/FileInputStream;

    invoke-direct {v3, v0}, Ljava/io/FileInputStream;-><init>(Ljava/io/File;)V

    move-object v1, v3

    new-instance v3, Ljava/io/DataInputStream;

    invoke-direct {v3, v1}, Ljava/io/DataInputStream;-><init>(Ljava/io/InputStream;)V

    move-object v2, v3

    invoke-virtual {v2}, Ljava/io/DataInputStream;->readLine()Ljava/lang/String;

    move-result-object v3

    if-eqz v3, :cond_2

    const-string v4, "%"

    invoke-virtual {v3, v4}, Ljava/lang/String;->split(Ljava/lang/String;)[Ljava/lang/String;

    move-result-object v4

    if-eqz v4, :cond_2

    array-length v5, v4

    if-lez v5, :cond_2

    invoke-virtual {p0}, Lcom/android/server/wm/WindowManagerService;->getDefaultDisplayContentLocked()Lcom/android/server/wm/DisplayContent;

    move-result-object v5

    new-instance v6, Lcom/android/server/wm/Watermark;

    iget-object v7, v5, Lcom/android/server/wm/DisplayContent;->mRealDisplayMetrics:Landroid/util/DisplayMetrics;

    iget-object v8, p0, Lcom/android/server/wm/WindowManagerService;->mTransaction:Landroid/view/SurfaceControl$Transaction;

    invoke-direct {v6, v5, v7, v4, v8}, Lcom/android/server/wm/Watermark;-><init>(Lcom/android/server/wm/DisplayContent;Landroid/util/DisplayMetrics;[Ljava/lang/String;Landroid/view/SurfaceControl$Transaction;)V

    iput-object v6, p0, Lcom/android/server/wm/WindowManagerService;->mWatermark:Lcom/android/server/wm/Watermark;

    iget-object v6, p0, Lcom/android/server/wm/WindowManagerService;->mTransaction:Landroid/view/SurfaceControl$Transaction;

    invoke-virtual {v6}, Landroid/view/SurfaceControl$Transaction;->apply()V
    :try_end_2
    .catch Ljava/io/FileNotFoundException; {:try_start_2 .. :try_end_2} :catch_1
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_5
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    :cond_2
    nop

    :try_start_3
    invoke-virtual {v2}, Ljava/io/DataInputStream;->close()V
    :try_end_3
    .catch Ljava/io/IOException; {:try_start_3 .. :try_end_3} :catch_0

    :goto_c
    goto :goto_2

    nop

    :goto_d
    goto :goto_c

    :goto_e
    goto :goto_1e

    nop

    :goto_f
    goto :goto_c

    :goto_10
    goto :goto_9

    nop

    :goto_11
    goto :goto_19

    :catch_3
    move-exception v3

    goto :goto_3

    nop

    :goto_12
    const-string v1, "/system/etc/setup.conf"

    goto :goto_4

    nop

    :goto_13
    goto :goto_21

    :catch_4
    move-exception v4

    goto :goto_20

    nop

    :goto_14
    throw v3

    :catch_5
    move-exception v3

    goto :goto_0

    nop

    :goto_15
    if-nez v0, :cond_3

    goto :goto_8

    :cond_3
    goto :goto_7

    nop

    :goto_16
    goto :goto_c

    :catchall_0
    move-exception v3

    goto :goto_22

    nop

    :goto_17
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mWatermark:Lcom/android/server/wm/Watermark;

    goto :goto_15

    nop

    :goto_18
    goto :goto_a

    :goto_19
    goto :goto_6

    nop

    :goto_1a
    if-nez v2, :cond_4

    goto :goto_e

    :cond_4
    :try_start_4
    invoke-virtual {v2}, Ljava/io/DataInputStream;->close()V
    :try_end_4
    .catch Ljava/io/IOException; {:try_start_4 .. :try_end_4} :catch_0

    goto :goto_d

    nop

    :goto_1b
    goto :goto_21

    :goto_1c
    :try_start_5
    invoke-virtual {v2}, Ljava/io/DataInputStream;->close()V
    :try_end_5
    .catch Ljava/io/IOException; {:try_start_5 .. :try_end_5} :catch_4

    :goto_1d
    goto :goto_13

    nop

    :goto_1e
    if-nez v1, :cond_5

    goto :goto_19

    :cond_5
    :try_start_6
    invoke-virtual {v1}, Ljava/io/FileInputStream;->close()V
    :try_end_6
    .catch Ljava/io/IOException; {:try_start_6 .. :try_end_6} :catch_3

    goto :goto_18

    nop

    :goto_1f
    if-nez v1, :cond_6

    goto :goto_21

    :cond_6
    :try_start_7
    invoke-virtual {v1}, Ljava/io/FileInputStream;->close()V
    :try_end_7
    .catch Ljava/io/IOException; {:try_start_7 .. :try_end_7} :catch_2

    goto :goto_5

    nop

    :goto_20
    goto :goto_1d

    :goto_21
    goto :goto_14

    nop

    :goto_22
    if-eqz v2, :cond_7

    goto :goto_1c

    :cond_7
    goto :goto_1f

    nop

    :goto_23
    const/4 v1, 0x0

    goto :goto_b

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mWatermark:Lcom/android/server/wm/Watermark;', 'if-eqz v0, :cond_0', 'return-void', 'new-instance v0, Ljava/io/File;', 'const-string v1, "/system/etc/setup.conf"', 'invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_dispatchImeInputTargetVisibilityChanged_Landroid_os_IBinder_",
        "method":      ".method dispatchImeInputTargetVisibilityChanged(Landroid/os/IBinder;ZZI)V",
        "method_name": 'dispatchImeInputTargetVisibilityChanged',
        "type":        "method_replace",
        "search": """\
.method dispatchImeInputTargetVisibilityChanged(Landroid/os/IBinder;ZZI)V
    .registers 8

    sget-boolean v0, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG_INPUT_METHOD:Z

    if-eqz v0, :cond_0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "onImeInputTargetVisibilityChanged, win="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    invoke-virtual {v1, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "visible="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, ", removed="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, ", displayId="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "WindowManager"

    invoke-static {v1, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_0
    if-eqz p2, :cond_1

    if-nez p3, :cond_1

    const/4 v0, 0x1

    goto :goto_0

    :cond_1
    const/4 v0, 0x0

    :goto_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    new-instance v2, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda20;

    invoke-direct {v2, p1, v0, p4}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda20;-><init>(Landroid/os/IBinder;ZI)V

    invoke-virtual {v1, v2}, Lcom/android/server/wm/WindowManagerService$H;->post(Ljava/lang/Runnable;)Z

    return-void
.end method
""",
        "replacement": """\
.method dispatchImeInputTargetVisibilityChanged(Landroid/os/IBinder;ZZI)V
    .registers 8

    goto :goto_1b

    nop

    :goto_0
    const-string v1, "visible="

    goto :goto_1

    nop

    :goto_1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_17

    nop

    :goto_2
    const-string v1, ", displayId="

    goto :goto_b

    nop

    :goto_3
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    goto :goto_1d

    nop

    :goto_4
    if-eqz p3, :cond_0

    goto :goto_20

    :cond_0
    goto :goto_8

    nop

    :goto_5
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_21

    nop

    :goto_6
    if-nez p2, :cond_1

    goto :goto_20

    :cond_1
    goto :goto_4

    nop

    :goto_7
    const-string v1, "onImeInputTargetVisibilityChanged, win="

    goto :goto_a

    nop

    :goto_8
    const/4 v0, 0x1

    goto :goto_1f

    nop

    :goto_9
    invoke-virtual {v0, p4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_10

    nop

    :goto_a
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_3

    nop

    :goto_b
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_9

    nop

    :goto_c
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_7

    nop

    :goto_d
    if-nez v0, :cond_2

    goto :goto_16

    :cond_2
    goto :goto_1a

    nop

    :goto_e
    invoke-direct {v2, p1, v0, p4}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda20;-><init>(Landroid/os/IBinder;ZI)V

    goto :goto_1c

    nop

    :goto_f
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_0

    nop

    :goto_10
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_1e

    nop

    :goto_11
    const/4 v0, 0x0

    :goto_12
    goto :goto_19

    nop

    :goto_13
    return-void

    :goto_14
    new-instance v2, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda20;

    goto :goto_e

    nop

    :goto_15
    invoke-static {v1, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_16
    goto :goto_6

    nop

    :goto_17
    invoke-virtual {v0, p2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_18

    nop

    :goto_18
    const-string v1, ", removed="

    goto :goto_5

    nop

    :goto_19
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    goto :goto_14

    nop

    :goto_1a
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_c

    nop

    :goto_1b
    sget-boolean v0, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG_INPUT_METHOD:Z

    goto :goto_d

    nop

    :goto_1c
    invoke-virtual {v1, v2}, Lcom/android/server/wm/WindowManagerService$H;->post(Ljava/lang/Runnable;)Z

    goto :goto_13

    nop

    :goto_1d
    invoke-virtual {v1, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_f

    nop

    :goto_1e
    const-string v1, "WindowManager"

    goto :goto_15

    nop

    :goto_1f
    goto :goto_12

    :goto_20
    goto :goto_11

    nop

    :goto_21
    invoke-virtual {v0, p3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['sget-boolean v0, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG_INPUT_METHOD:Z', 'if-eqz v0, :cond_0', 'new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "onImeInputTargetVisibilityChanged, win="', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_dispatchImeTargetOverlayVisibilityChanged_Landroid_os_IBinde",
        "method":      ".method dispatchImeTargetOverlayVisibilityChanged(Landroid/os/IBinder;IZZI)V",
        "method_name": 'dispatchImeTargetOverlayVisibilityChanged',
        "type":        "method_replace",
        "search": """\
.method dispatchImeTargetOverlayVisibilityChanged(Landroid/os/IBinder;IZZI)V
    .registers 9

    sget-boolean v0, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG_INPUT_METHOD:Z

    if-eqz v0, :cond_0

    new-instance v0, Ljava/lang/StringBuilder;

    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    const-string v1, "onImeTargetOverlayVisibilityChanged, win="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    invoke-virtual {v1, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, ", type="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-class v1, Landroid/view/WindowManager$LayoutParams;

    const-string v2, "type"

    invoke-static {v1, v2, p2}, Landroid/view/ViewDebug;->intToString(Ljava/lang/Class;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v1

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, "visible="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, ", removed="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p4}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v0

    const-string v1, ", displayId="

    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0, p5}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    const-string v1, "WindowManager"

    invoke-static {v1, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_0
    if-eqz p3, :cond_1

    if-nez p4, :cond_1

    const/4 v0, 0x3

    if-eq p2, v0, :cond_1

    const/4 v0, 0x1

    goto :goto_0

    :cond_1
    const/4 v0, 0x0

    :goto_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    new-instance v2, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda24;

    invoke-direct {v2, v0, p5}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda24;-><init>(ZI)V

    invoke-virtual {v1, v2}, Lcom/android/server/wm/WindowManagerService$H;->post(Ljava/lang/Runnable;)Z

    return-void
.end method
""",
        "replacement": """\
.method dispatchImeTargetOverlayVisibilityChanged(Landroid/os/IBinder;IZZI)V
    .registers 9

    goto :goto_10

    nop

    :goto_0
    const-string v1, "onImeTargetOverlayVisibilityChanged, win="

    goto :goto_11

    nop

    :goto_1
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_4

    nop

    :goto_2
    new-instance v2, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda24;

    goto :goto_15

    nop

    :goto_3
    if-nez v0, :cond_0

    goto :goto_1e

    :cond_0
    goto :goto_a

    nop

    :goto_4
    invoke-virtual {v0, p4}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_16

    nop

    :goto_5
    if-ne p2, v0, :cond_1

    goto :goto_d

    :cond_1
    goto :goto_1f

    nop

    :goto_6
    invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V

    goto :goto_0

    nop

    :goto_7
    const-string v1, "WindowManager"

    goto :goto_1d

    nop

    :goto_8
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_23

    nop

    :goto_9
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_24

    nop

    :goto_a
    new-instance v0, Ljava/lang/StringBuilder;

    goto :goto_6

    nop

    :goto_b
    invoke-static {v1, v2, p2}, Landroid/view/ViewDebug;->intToString(Ljava/lang/Class;Ljava/lang/String;I)Ljava/lang/String;

    move-result-object v1

    goto :goto_20

    nop

    :goto_c
    goto :goto_f

    :goto_d
    goto :goto_e

    nop

    :goto_e
    const/4 v0, 0x0

    :goto_f
    goto :goto_14

    nop

    :goto_10
    sget-boolean v0, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG_INPUT_METHOD:Z

    goto :goto_3

    nop

    :goto_11
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_12

    nop

    :goto_12
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    goto :goto_28

    nop

    :goto_13
    const-string v1, ", removed="

    goto :goto_1

    nop

    :goto_14
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    goto :goto_2

    nop

    :goto_15
    invoke-direct {v2, v0, p5}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda24;-><init>(ZI)V

    goto :goto_18

    nop

    :goto_16
    const-string v1, ", displayId="

    goto :goto_9

    nop

    :goto_17
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_27

    nop

    :goto_18
    invoke-virtual {v1, v2}, Lcom/android/server/wm/WindowManagerService$H;->post(Ljava/lang/Runnable;)Z

    goto :goto_1b

    nop

    :goto_19
    const-string v2, "type"

    goto :goto_b

    nop

    :goto_1a
    if-eqz p4, :cond_2

    goto :goto_d

    :cond_2
    goto :goto_21

    nop

    :goto_1b
    return-void

    :goto_1c
    if-nez p3, :cond_3

    goto :goto_d

    :cond_3
    goto :goto_1a

    nop

    :goto_1d
    invoke-static {v1, v0}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :goto_1e
    goto :goto_1c

    nop

    :goto_1f
    const/4 v0, 0x1

    goto :goto_c

    nop

    :goto_20
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_26

    nop

    :goto_21
    const/4 v0, 0x3

    goto :goto_5

    nop

    :goto_22
    invoke-virtual {v0}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    goto :goto_7

    nop

    :goto_23
    const-string v1, ", type="

    goto :goto_17

    nop

    :goto_24
    invoke-virtual {v0, p5}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_22

    nop

    :goto_25
    invoke-virtual {v0, p3}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_13

    nop

    :goto_26
    const-string v1, "visible="

    goto :goto_29

    nop

    :goto_27
    const-class v1, Landroid/view/WindowManager$LayoutParams;

    goto :goto_19

    nop

    :goto_28
    invoke-virtual {v1, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    goto :goto_8

    nop

    :goto_29
    invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v0

    goto :goto_25

    nop
.end method
""",
        "method_anchors": ['sget-boolean v0, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG_INPUT_METHOD:Z', 'if-eqz v0, :cond_0', 'new-instance v0, Ljava/lang/StringBuilder;', 'invoke-direct {v0}, Ljava/lang/StringBuilder;-><init>()V', 'const-string v1, "onImeTargetOverlayVisibilityChanged, win="', 'invoke-virtual {v0, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_dispatchNewAnimatorScaleLocked_Lcom_android_server_wm_Sessio",
        "method":      ".method dispatchNewAnimatorScaleLocked(Lcom/android/server/wm/Session;)V",
        "method_name": 'dispatchNewAnimatorScaleLocked',
        "type":        "method_replace",
        "search": """\
.method dispatchNewAnimatorScaleLocked(Lcom/android/server/wm/Session;)V
    .registers 5

    const-string v0, "com.android.server.wm.WindowManagerService.dispatchNewAnimatorScaleLocked(Lcom/android/server/wm/Session;)V"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    const/16 v2, 0x22

    invoke-virtual {v1, v2, p1}, Lcom/android/server/wm/WindowManagerService$H;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;

    move-result-object v1

    invoke-virtual {v1}, Landroid/os/Message;->sendToTarget()V

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-void

    :catchall_0
    move-exception p1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw p1
.end method
""",
        "replacement": """\
.method dispatchNewAnimatorScaleLocked(Lcom/android/server/wm/Session;)V
    .registers 5

    goto :goto_1

    nop

    :goto_0
    throw p1

    :goto_1
    const-string v0, "com.android.server.wm.WindowManagerService.dispatchNewAnimatorScaleLocked(Lcom/android/server/wm/Session;)V"

    goto :goto_2

    nop

    :goto_2
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    const/16 v2, 0x22

    invoke-virtual {v1, v2, p1}, Lcom/android/server/wm/WindowManagerService$H;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;

    move-result-object v1

    invoke-virtual {v1}, Landroid/os/Message;->sendToTarget()V

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_4

    nop

    :goto_3
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_0

    nop

    :goto_4
    return-void

    :catchall_0
    move-exception p1

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.dispatchNewAnimatorScaleLocked(Lcom/android/server/wm/Session;)V"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;', 'invoke-virtual {v1, v2, p1}, Lcom/android/server/wm/WindowManagerService$H;->obtainMessage(ILjava/lang/Object;)Landroid/os/Message;', 'move-result-object v1', 'invoke-virtual {v1}, Landroid/os/Message;->sendToTarget()V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_dumpDebugLocked_Landroid_util_proto_ProtoOutputStream_I_V",
        "method":      ".method dumpDebugLocked(Landroid/util/proto/ProtoOutputStream;I)V",
        "method_name": 'dumpDebugLocked',
        "type":        "method_replace",
        "search": """\
.method dumpDebugLocked(Landroid/util/proto/ProtoOutputStream;I)V
    .registers 11

    const-string v0, "com.android.server.wm.WindowManagerService.dumpDebugLocked(Landroid/util/proto/ProtoOutputStream;I)V"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    const-string v1, "dumpDebugLocked"

    const-wide/16 v2, 0x20

    invoke-static {v2, v3, v1}, Landroid/os/Trace;->traceBegin(JLjava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    :try_start_1
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mPolicy:Lcom/android/server/policy/WindowManagerPolicy;

    const-wide v4, 0x10b00000001L

    invoke-interface {v1, p1, v4, v5}, Lcom/android/server/policy/WindowManagerPolicy;->dumpDebug(Landroid/util/proto/ProtoOutputStream;J)V

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    const-wide v4, 0x10b00000002L

    invoke-virtual {v1, p1, v4, v5, p2}, Lcom/android/server/wm/RootWindowContainer;->dumpDebug(Landroid/util/proto/ProtoOutputStream;JI)V

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->getTopFocusedDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    iget-object v4, v1, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;

    if-eqz v4, :cond_0

    iget-object v4, v1, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;

    const-wide v5, 0x10b00000003L

    invoke-virtual {v4, p1, v5, v6}, Lcom/android/server/wm/WindowState;->writeIdentifierToProto(Landroid/util/proto/ProtoOutputStream;J)V

    :cond_0
    iget-object v4, v1, Lcom/android/server/wm/DisplayContent;->mFocusedApp:Lcom/android/server/wm/ActivityRecord;

    if-eqz v4, :cond_1

    iget-object v4, v1, Lcom/android/server/wm/DisplayContent;->mFocusedApp:Lcom/android/server/wm/ActivityRecord;

    const-wide v5, 0x10900000004L

    invoke-virtual {v4, p1, v5, v6}, Lcom/android/server/wm/ActivityRecord;->writeNameToProto(Landroid/util/proto/ProtoOutputStream;J)V

    :cond_1
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v4}, Lcom/android/server/wm/RootWindowContainer;->getCurrentInputMethodWindow()Lcom/android/server/wm/WindowState;

    move-result-object v4

    if-eqz v4, :cond_2

    const-wide v5, 0x10b00000005L

    invoke-virtual {v4, p1, v5, v6}, Lcom/android/server/wm/WindowState;->writeIdentifierToProto(Landroid/util/proto/ProtoOutputStream;J)V

    :cond_2
    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getDisplayId()I

    move-result v5

    const-wide v6, 0x10500000009L

    invoke-virtual {p1, v6, v7, v5}, Landroid/util/proto/ProtoOutputStream;->write(JI)V

    iget-boolean v5, p0, Lcom/android/server/wm/WindowManagerService;->mHardKeyboardAvailable:Z

    const-wide v6, 0x1080000000aL

    invoke-virtual {p1, v6, v7, v5}, Landroid/util/proto/ProtoOutputStream;->write(JZ)V

    const-wide v5, 0x1080000000bL

    const/4 v7, 0x1

    invoke-virtual {p1, v5, v6, v7}, Landroid/util/proto/ProtoOutputStream;->write(JZ)V

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;

    iget-object v5, v5, Lcom/android/server/wm/ActivityTaskManagerService;->mBackNavigationController:Lcom/android/server/wm/BackNavigationController;

    const-wide v6, 0x10b0000000cL

    invoke-virtual {v5, p1, v6, v7}, Lcom/android/server/wm/BackNavigationController;->dumpDebug(Landroid/util/proto/ProtoOutputStream;J)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :try_start_2
    invoke-static {v2, v3}, Landroid/os/Trace;->traceEnd(J)V

    nop

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-void

    :catchall_0
    move-exception v1

    invoke-static {v2, v3}, Landroid/os/Trace;->traceEnd(J)V

    throw v1
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    :catchall_1
    move-exception p1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw p1
.end method
""",
        "replacement": """\
.method dumpDebugLocked(Landroid/util/proto/ProtoOutputStream;I)V
    .registers 11

    goto :goto_0

    nop

    :goto_0
    const-string v0, "com.android.server.wm.WindowManagerService.dumpDebugLocked(Landroid/util/proto/ProtoOutputStream;I)V"

    goto :goto_1

    nop

    :goto_1
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    const-string v1, "dumpDebugLocked"

    const-wide/16 v2, 0x20

    invoke-static {v2, v3, v1}, Landroid/os/Trace;->traceBegin(JLjava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    :try_start_1
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mPolicy:Lcom/android/server/policy/WindowManagerPolicy;

    const-wide v4, 0x10b00000001L

    invoke-interface {v1, p1, v4, v5}, Lcom/android/server/policy/WindowManagerPolicy;->dumpDebug(Landroid/util/proto/ProtoOutputStream;J)V

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    const-wide v4, 0x10b00000002L

    invoke-virtual {v1, p1, v4, v5, p2}, Lcom/android/server/wm/RootWindowContainer;->dumpDebug(Landroid/util/proto/ProtoOutputStream;JI)V

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->getTopFocusedDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    iget-object v4, v1, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;

    if-eqz v4, :cond_0

    iget-object v4, v1, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;

    const-wide v5, 0x10b00000003L

    invoke-virtual {v4, p1, v5, v6}, Lcom/android/server/wm/WindowState;->writeIdentifierToProto(Landroid/util/proto/ProtoOutputStream;J)V

    :cond_0
    iget-object v4, v1, Lcom/android/server/wm/DisplayContent;->mFocusedApp:Lcom/android/server/wm/ActivityRecord;

    if-eqz v4, :cond_1

    iget-object v4, v1, Lcom/android/server/wm/DisplayContent;->mFocusedApp:Lcom/android/server/wm/ActivityRecord;

    const-wide v5, 0x10900000004L

    invoke-virtual {v4, p1, v5, v6}, Lcom/android/server/wm/ActivityRecord;->writeNameToProto(Landroid/util/proto/ProtoOutputStream;J)V

    :cond_1
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v4}, Lcom/android/server/wm/RootWindowContainer;->getCurrentInputMethodWindow()Lcom/android/server/wm/WindowState;

    move-result-object v4

    if-eqz v4, :cond_2

    const-wide v5, 0x10b00000005L

    invoke-virtual {v4, p1, v5, v6}, Lcom/android/server/wm/WindowState;->writeIdentifierToProto(Landroid/util/proto/ProtoOutputStream;J)V

    :cond_2
    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getDisplayId()I

    move-result v5

    const-wide v6, 0x10500000009L

    invoke-virtual {p1, v6, v7, v5}, Landroid/util/proto/ProtoOutputStream;->write(JI)V

    iget-boolean v5, p0, Lcom/android/server/wm/WindowManagerService;->mHardKeyboardAvailable:Z

    const-wide v6, 0x1080000000aL

    invoke-virtual {p1, v6, v7, v5}, Landroid/util/proto/ProtoOutputStream;->write(JZ)V

    const-wide v5, 0x1080000000bL

    const/4 v7, 0x1

    invoke-virtual {p1, v5, v6, v7}, Landroid/util/proto/ProtoOutputStream;->write(JZ)V

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;

    iget-object v5, v5, Lcom/android/server/wm/ActivityTaskManagerService;->mBackNavigationController:Lcom/android/server/wm/BackNavigationController;

    const-wide v6, 0x10b0000000cL

    invoke-virtual {v5, p1, v6, v7}, Lcom/android/server/wm/BackNavigationController;->dumpDebug(Landroid/util/proto/ProtoOutputStream;J)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :try_start_2
    invoke-static {v2, v3}, Landroid/os/Trace;->traceEnd(J)V

    nop

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-void

    :catchall_0
    move-exception v1

    invoke-static {v2, v3}, Landroid/os/Trace;->traceEnd(J)V

    throw v1
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    :catchall_1
    move-exception p1

    goto :goto_2

    nop

    :goto_2
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_3
    throw p1
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.dumpDebugLocked(Landroid/util/proto/ProtoOutputStream;I)V"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'const-string v1, "dumpDebugLocked"', 'invoke-static {v2, v3, v1}, Landroid/os/Trace;->traceBegin(JLjava/lang/String;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mPolicy:Lcom/android/server/policy/WindowManagerPolicy;', 'invoke-interface {v1, p1, v4, v5}, Lcom/android/server/policy/WindowManagerPolicy;->dumpDebug(Landroid/util/proto/ProtoOutputStream;J)V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_dumpSurfaceLeakInfo__V",
        "method":      ".method dumpSurfaceLeakInfo()V",
        "method_name": 'dumpSurfaceLeakInfo',
        "type":        "method_replace",
        "search": """\
.method dumpSurfaceLeakInfo()V
    .registers 1

    return-void
.end method
""",
        "replacement": """\
.method dumpSurfaceLeakInfo()V
    .registers 1

    goto :goto_0

    nop

    :goto_0
    return-void
.end method
""",
        "method_anchors": ['return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_enableScreenIfNeededLocked__V",
        "method":      ".method enableScreenIfNeededLocked()V",
        "method_name": 'enableScreenIfNeededLocked',
        "type":        "method_replace",
        "search": """\
.method enableScreenIfNeededLocked()V
    .registers 12

    const-string v0, "com.android.server.wm.WindowManagerService.enableScreenIfNeededLocked()V"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_BOOT_enabled:[Z

    const/4 v2, 0x2

    aget-boolean v1, v1, v2

    if-eqz v1, :cond_0

    iget-boolean v1, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayEnabled:Z

    iget-boolean v2, p0, Lcom/android/server/wm/WindowManagerService;->mForceDisplayEnabled:Z

    iget-boolean v3, p0, Lcom/android/server/wm/WindowManagerService;->mShowingBootMessages:Z

    iget-boolean v4, p0, Lcom/android/server/wm/WindowManagerService;->mSystemBooted:Z

    new-instance v5, Ljava/lang/RuntimeException;

    const-string v6, "here"

    invoke-direct {v5, v6}, Ljava/lang/RuntimeException;-><init>(Ljava/lang/String;)V

    invoke-virtual {v5}, Ljava/lang/RuntimeException;->fillInStackTrace()Ljava/lang/Throwable;

    move-result-object v5

    invoke-static {v5}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    sget-object v6, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_BOOT:Lcom/android/internal/protolog/WmProtoLogGroups;

    invoke-static {v1}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v7

    invoke-static {v2}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v8

    invoke-static {v3}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v9

    invoke-static {v4}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v10

    filled-new-array {v7, v8, v9, v10, v5}, [Ljava/lang/Object;

    move-result-object v7

    const-wide v8, -0x59c26b590a84c2d8L

    const/16 v10, 0xff

    invoke-static {v6, v8, v9, v10, v7}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->i(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_0
    iget-boolean v1, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayEnabled:Z

    if-eqz v1, :cond_1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-void

    :cond_1
    iget-boolean v1, p0, Lcom/android/server/wm/WindowManagerService;->mSystemBooted:Z

    if-nez v1, :cond_2

    iget-boolean v1, p0, Lcom/android/server/wm/WindowManagerService;->mShowingBootMessages:Z

    if-nez v1, :cond_2

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-void

    :cond_2
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    const/16 v2, 0x10

    invoke-virtual {v1, v2}, Lcom/android/server/wm/WindowManagerService$H;->sendEmptyMessage(I)Z

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-void

    :catchall_0
    move-exception v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw v1
.end method
""",
        "replacement": """\
.method enableScreenIfNeededLocked()V
    .registers 12

    goto :goto_4

    nop

    :goto_0
    throw v1

    :goto_1
    return-void

    :catchall_0
    move-exception v1

    goto :goto_3

    nop

    :goto_2
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_BOOT_enabled:[Z

    const/4 v2, 0x2

    aget-boolean v1, v1, v2

    if-eqz v1, :cond_0

    iget-boolean v1, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayEnabled:Z

    iget-boolean v2, p0, Lcom/android/server/wm/WindowManagerService;->mForceDisplayEnabled:Z

    iget-boolean v3, p0, Lcom/android/server/wm/WindowManagerService;->mShowingBootMessages:Z

    iget-boolean v4, p0, Lcom/android/server/wm/WindowManagerService;->mSystemBooted:Z

    new-instance v5, Ljava/lang/RuntimeException;

    const-string v6, "here"

    invoke-direct {v5, v6}, Ljava/lang/RuntimeException;-><init>(Ljava/lang/String;)V

    invoke-virtual {v5}, Ljava/lang/RuntimeException;->fillInStackTrace()Ljava/lang/Throwable;

    move-result-object v5

    invoke-static {v5}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    sget-object v6, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_BOOT:Lcom/android/internal/protolog/WmProtoLogGroups;

    invoke-static {v1}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v7

    invoke-static {v2}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v8

    invoke-static {v3}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v9

    invoke-static {v4}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v10

    filled-new-array {v7, v8, v9, v10, v5}, [Ljava/lang/Object;

    move-result-object v7

    const-wide v8, -0x59c26b590a84c2d8L

    const/16 v10, 0xff

    invoke-static {v6, v8, v9, v10, v7}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->i(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_0
    iget-boolean v1, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayEnabled:Z

    if-eqz v1, :cond_1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-void

    :cond_1
    iget-boolean v1, p0, Lcom/android/server/wm/WindowManagerService;->mSystemBooted:Z

    if-nez v1, :cond_2

    iget-boolean v1, p0, Lcom/android/server/wm/WindowManagerService;->mShowingBootMessages:Z

    if-nez v1, :cond_2

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-void

    :cond_2
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    const/16 v2, 0x10

    invoke-virtual {v1, v2}, Lcom/android/server/wm/WindowManagerService$H;->sendEmptyMessage(I)Z

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop

    :goto_3
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_0

    nop

    :goto_4
    const-string v0, "com.android.server.wm.WindowManagerService.enableScreenIfNeededLocked()V"

    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.enableScreenIfNeededLocked()V"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_BOOT_enabled:[Z', 'if-eqz v1, :cond_0', 'iget-boolean v1, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayEnabled:Z', 'iget-boolean v2, p0, Lcom/android/server/wm/WindowManagerService;->mForceDisplayEnabled:Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_finishDrawingWindow_Lcom_android_server_wm_Session_Landroid_",
        "method":      ".method finishDrawingWindow(Lcom/android/server/wm/Session;Landroid/view/IWindow;Landroid/view/SurfaceControl$Transaction;I)V",
        "method_name": 'finishDrawingWindow',
        "type":        "method_replace",
        "search": """\
.method finishDrawingWindow(Lcom/android/server/wm/Session;Landroid/view/IWindow;Landroid/view/SurfaceControl$Transaction;I)V
    .registers 16

    if-eqz p3, :cond_0

    invoke-static {}, Landroid/os/Binder;->getCallingPid()I

    move-result v0

    invoke-static {}, Landroid/os/Binder;->getCallingUid()I

    move-result v1

    invoke-virtual {p3, v0, v1}, Landroid/view/SurfaceControl$Transaction;->sanitize(II)V

    :cond_0
    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v0

    :try_start_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    const/4 v3, 0x0

    :try_start_1
    invoke-virtual {p0, p1, p2, v3}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v4

    sget-object v5, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_ADD_REMOVE_enabled:[Z

    const/4 v6, 0x1

    aget-boolean v5, v5, v6

    if-eqz v5, :cond_2

    invoke-static {v4}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    if-eqz v4, :cond_1

    iget-object v6, v4, Lcom/android/server/wm/WindowState;->mWinAnimator:Lcom/android/server/wm/WindowStateAnimator;

    invoke-virtual {v6}, Lcom/android/server/wm/WindowStateAnimator;->drawStateToString()Ljava/lang/String;

    move-result-object v6

    goto :goto_0

    :cond_1
    const-string v6, "null"

    :goto_0
    invoke-static {v6}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v6

    sget-object v7, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_ADD_REMOVE:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v5, v6}, [Ljava/lang/Object;

    move-result-object v8

    const-wide v9, -0x4c7e951c6745ccadL

    invoke-static {v7, v9, v10, v3, v8}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->d(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_2
    if-eqz v4, :cond_4

    invoke-virtual {v4, p3, p4}, Lcom/android/server/wm/WindowState;->finishDrawing(Landroid/view/SurfaceControl$Transaction;I)Z

    move-result v3

    if-eqz v3, :cond_4

    invoke-virtual {v4}, Lcom/android/server/wm/WindowState;->hasWallpaper()Z

    move-result v3

    if-eqz v3, :cond_3

    invoke-virtual {v4}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v3

    iget v5, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    or-int/lit8 v5, v5, 0x4

    iput v5, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    :cond_3
    invoke-virtual {v4}, Lcom/android/server/wm/WindowState;->setDisplayLayoutNeeded()V

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;

    invoke-virtual {v3}, Lcom/android/server/wm/WindowSurfacePlacer;->requestTraversal()V

    :cond_4
    monitor-exit v2
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :try_start_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    nop

    return-void

    :catchall_0
    move-exception v3

    :try_start_3
    monitor-exit v2
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v3
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_1

    :catchall_1
    move-exception v2

    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    throw v2
.end method
""",
        "replacement": """\
.method finishDrawingWindow(Lcom/android/server/wm/Session;Landroid/view/IWindow;Landroid/view/SurfaceControl$Transaction;I)V
    .registers 16

    goto :goto_1

    nop

    :goto_0
    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v0

    :try_start_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    goto :goto_3

    nop

    :goto_1
    if-nez p3, :cond_0

    goto :goto_b

    :cond_0
    goto :goto_8

    nop

    :goto_2
    return-void

    :catchall_0
    move-exception v3

    :try_start_1
    monitor-exit v2
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :try_start_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v3
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    :catchall_1
    move-exception v2

    goto :goto_7

    nop

    :goto_3
    const/4 v3, 0x0

    :try_start_3
    invoke-virtual {p0, p1, p2, v3}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v4

    sget-object v5, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_ADD_REMOVE_enabled:[Z

    const/4 v6, 0x1

    aget-boolean v5, v5, v6

    if-eqz v5, :cond_2

    invoke-static {v4}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    if-eqz v4, :cond_1

    iget-object v6, v4, Lcom/android/server/wm/WindowState;->mWinAnimator:Lcom/android/server/wm/WindowStateAnimator;

    invoke-virtual {v6}, Lcom/android/server/wm/WindowStateAnimator;->drawStateToString()Ljava/lang/String;

    move-result-object v6

    goto :goto_4

    :cond_1
    const-string v6, "null"

    :goto_4
    invoke-static {v6}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v6

    sget-object v7, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_ADD_REMOVE:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v5, v6}, [Ljava/lang/Object;

    move-result-object v8

    const-wide v9, -0x4c7e951c6745ccadL

    invoke-static {v7, v9, v10, v3, v8}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->d(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_2
    if-eqz v4, :cond_4

    invoke-virtual {v4, p3, p4}, Lcom/android/server/wm/WindowState;->finishDrawing(Landroid/view/SurfaceControl$Transaction;I)Z

    move-result v3

    if-eqz v3, :cond_4

    invoke-virtual {v4}, Lcom/android/server/wm/WindowState;->hasWallpaper()Z

    move-result v3

    if-eqz v3, :cond_3

    invoke-virtual {v4}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v3

    iget v5, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    or-int/lit8 v5, v5, 0x4

    iput v5, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    :cond_3
    invoke-virtual {v4}, Lcom/android/server/wm/WindowState;->setDisplayLayoutNeeded()V

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;

    invoke-virtual {v3}, Lcom/android/server/wm/WindowSurfacePlacer;->requestTraversal()V

    :cond_4
    monitor-exit v2
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_1

    goto :goto_5

    nop

    :goto_5
    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    nop

    goto :goto_2

    nop

    :goto_6
    throw v2

    :goto_7
    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    goto :goto_6

    nop

    :goto_8
    invoke-static {}, Landroid/os/Binder;->getCallingPid()I

    move-result v0

    goto :goto_9

    nop

    :goto_9
    invoke-static {}, Landroid/os/Binder;->getCallingUid()I

    move-result v1

    goto :goto_a

    nop

    :goto_a
    invoke-virtual {p3, v0, v1}, Landroid/view/SurfaceControl$Transaction;->sanitize(II)V

    :goto_b
    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['if-eqz p3, :cond_0', 'invoke-static {}, Landroid/os/Binder;->getCallingPid()I', 'move-result v0', 'invoke-static {}, Landroid/os/Binder;->getCallingUid()I', 'move-result v1', 'invoke-virtual {p3, v0, v1}, Landroid/view/SurfaceControl$Transaction;->sanitize(II)V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_generateDisplayHash_Lcom_android_server_wm_Session_Landroid_",
        "method":      ".method generateDisplayHash(Lcom/android/server/wm/Session;Landroid/view/IWindow;Landroid/graphics/Rect;Ljava/lang/String;Landroid/os/RemoteCallback;)V",
        "method_name": 'generateDisplayHash',
        "type":        "method_replace",
        "search": """\
.method generateDisplayHash(Lcom/android/server/wm/Session;Landroid/view/IWindow;Landroid/graphics/Rect;Ljava/lang/String;Landroid/os/RemoteCallback;)V
    .registers 16

    move-object v3, p3

    move-object v6, p5

    new-instance v0, Landroid/graphics/Rect;

    invoke-direct {v0, p3}, Landroid/graphics/Rect;-><init>(Landroid/graphics/Rect;)V

    move-object v7, v0

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v1

    const/4 v0, 0x0

    :try_start_0
    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v0

    const/4 v2, -0x3

    if-nez v0, :cond_0

    const-string v4, "WindowManager"

    const-string v5, "Failed to generate DisplayHash. Invalid window"

    invoke-static {v4, v5}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    invoke-virtual {v4, p5, v2}, Lcom/android/server/wm/DisplayHashController;->sendDisplayHashError(Landroid/os/RemoteCallback;I)V

    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_0
    :try_start_1
    iget-object v4, v0, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    if-eqz v4, :cond_4

    iget-object v4, v0, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    sget-object v5, Lcom/android/server/wm/ActivityRecord$State;->RESUMED:Lcom/android/server/wm/ActivityRecord$State;

    invoke-virtual {v4, v5}, Lcom/android/server/wm/ActivityRecord;->isState(Lcom/android/server/wm/ActivityRecord$State;)Z

    move-result v4

    if-nez v4, :cond_1

    goto :goto_0

    :cond_1
    invoke-virtual {v0}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    const/4 v4, -0x4

    if-nez v2, :cond_2

    const-string v5, "WindowManager"

    const-string v8, "Failed to generate DisplayHash. Window is not on a display"

    invoke-static {v5, v8}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    invoke-virtual {v5, p5, v4}, Lcom/android/server/wm/DisplayHashController;->sendDisplayHashError(Landroid/os/RemoteCallback;I)V

    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_2
    :try_start_2
    invoke-virtual {v2}, Lcom/android/server/wm/DisplayContent;->getSurfaceControl()Landroid/view/SurfaceControl;

    move-result-object v5

    move-object v8, v5

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    invoke-virtual {v5, v0, p3, v7}, Lcom/android/server/wm/DisplayHashController;->calculateDisplayHashBoundsLocked(Lcom/android/server/wm/WindowState;Landroid/graphics/Rect;Landroid/graphics/Rect;)V

    invoke-virtual {v7}, Landroid/graphics/Rect;->isEmpty()Z

    move-result v5

    if-eqz v5, :cond_3

    const-string v5, "WindowManager"

    const-string v9, "Failed to generate DisplayHash. Bounds are not on screen"

    invoke-static {v5, v9}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    invoke-virtual {v5, p5, v4}, Lcom/android/server/wm/DisplayHashController;->sendDisplayHashError(Landroid/os/RemoteCallback;I)V

    monitor-exit v1
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_3
    :try_start_3
    monitor-exit v1
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    iget v5, p1, Lcom/android/server/wm/Session;->mUid:I

    new-instance v0, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    invoke-direct {v0, v8}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;-><init>(Landroid/view/SurfaceControl;)V

    int-to-long v1, v5

    invoke-virtual {v0, v1, v2}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;->setUid(J)Landroid/window/ScreenCapture$CaptureArgs$Builder;

    move-result-object v0

    check-cast v0, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    invoke-virtual {v0, v7}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;->setSourceCrop(Landroid/graphics/Rect;)Landroid/window/ScreenCapture$CaptureArgs$Builder;

    move-result-object v0

    move-object v2, v0

    check-cast v2, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    move-object v4, p4

    invoke-virtual/range {v1 .. v6}, Lcom/android/server/wm/DisplayHashController;->generateDisplayHash(Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;Landroid/graphics/Rect;Ljava/lang/String;ILandroid/os/RemoteCallback;)V

    return-void

    :cond_4
    :goto_0
    :try_start_4
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    invoke-virtual {v3, p5, v2}, Lcom/android/server/wm/DisplayHashController;->sendDisplayHashError(Landroid/os/RemoteCallback;I)V

    monitor-exit v1
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v0

    :try_start_5
    monitor-exit v1
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v0
.end method
""",
        "replacement": """\
.method generateDisplayHash(Lcom/android/server/wm/Session;Landroid/view/IWindow;Landroid/graphics/Rect;Ljava/lang/String;Landroid/os/RemoteCallback;)V
    .registers 16

    goto :goto_3

    nop

    :goto_0
    move-object v6, p5

    goto :goto_5

    nop

    :goto_1
    monitor-enter v1

    goto :goto_c

    nop

    :goto_2
    new-instance v0, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    goto :goto_15

    nop

    :goto_3
    move-object v3, p3

    goto :goto_0

    nop

    :goto_4
    throw v0

    :goto_5
    new-instance v0, Landroid/graphics/Rect;

    goto :goto_20

    nop

    :goto_6
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_f

    nop

    :goto_7
    return-void

    :catchall_0
    move-exception v0

    :try_start_0
    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1a

    nop

    :goto_8
    return-void

    :cond_0
    :try_start_1
    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_6

    nop

    :goto_9
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_8

    nop

    :goto_a
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_1d

    nop

    :goto_b
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_1

    nop

    :goto_c
    const/4 v0, 0x0

    :try_start_2
    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v0

    const/4 v2, -0x3

    if-nez v0, :cond_3

    const-string v4, "WindowManager"

    const-string v5, "Failed to generate DisplayHash. Invalid window"

    invoke-static {v4, v5}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    invoke-virtual {v4, p5, v2}, Lcom/android/server/wm/DisplayHashController;->sendDisplayHashError(Landroid/os/RemoteCallback;I)V

    monitor-exit v1
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_e

    nop

    :goto_d
    invoke-virtual {v0, v1, v2}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;->setUid(J)Landroid/window/ScreenCapture$CaptureArgs$Builder;

    move-result-object v0

    goto :goto_1b

    nop

    :goto_e
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_1f

    nop

    :goto_f
    iget v5, p1, Lcom/android/server/wm/Session;->mUid:I

    goto :goto_2

    nop

    :goto_10
    check-cast v2, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    goto :goto_1e

    nop

    :goto_11
    move-object v2, v0

    goto :goto_10

    nop

    :goto_12
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_b

    nop

    :goto_13
    invoke-virtual/range {v1 .. v6}, Lcom/android/server/wm/DisplayHashController;->generateDisplayHash(Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;Landroid/graphics/Rect;Ljava/lang/String;ILandroid/os/RemoteCallback;)V

    goto :goto_16

    nop

    :goto_14
    int-to-long v1, v5

    goto :goto_d

    nop

    :goto_15
    invoke-direct {v0, v8}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;-><init>(Landroid/view/SurfaceControl;)V

    goto :goto_14

    nop

    :goto_16
    return-void

    :cond_1
    :goto_17
    :try_start_3
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    invoke-virtual {v3, p5, v2}, Lcom/android/server/wm/DisplayHashController;->sendDisplayHashError(Landroid/os/RemoteCallback;I)V

    monitor-exit v1
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    goto :goto_1c

    nop

    :goto_18
    move-object v7, v0

    goto :goto_12

    nop

    :goto_19
    invoke-virtual {v0, v7}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;->setSourceCrop(Landroid/graphics/Rect;)Landroid/window/ScreenCapture$CaptureArgs$Builder;

    move-result-object v0

    goto :goto_11

    nop

    :goto_1a
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_4

    nop

    :goto_1b
    check-cast v0, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    goto :goto_19

    nop

    :goto_1c
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_7

    nop

    :goto_1d
    return-void

    :cond_2
    :try_start_4
    invoke-virtual {v2}, Lcom/android/server/wm/DisplayContent;->getSurfaceControl()Landroid/view/SurfaceControl;

    move-result-object v5

    move-object v8, v5

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    invoke-virtual {v5, v0, p3, v7}, Lcom/android/server/wm/DisplayHashController;->calculateDisplayHashBoundsLocked(Lcom/android/server/wm/WindowState;Landroid/graphics/Rect;Landroid/graphics/Rect;)V

    invoke-virtual {v7}, Landroid/graphics/Rect;->isEmpty()Z

    move-result v5

    if-eqz v5, :cond_0

    const-string v5, "WindowManager"

    const-string v9, "Failed to generate DisplayHash. Bounds are not on screen"

    invoke-static {v5, v9}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    invoke-virtual {v5, p5, v4}, Lcom/android/server/wm/DisplayHashController;->sendDisplayHashError(Landroid/os/RemoteCallback;I)V

    monitor-exit v1
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    goto :goto_9

    nop

    :goto_1e
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    goto :goto_21

    nop

    :goto_1f
    return-void

    :cond_3
    :try_start_5
    iget-object v4, v0, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    if-eqz v4, :cond_1

    iget-object v4, v0, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    sget-object v5, Lcom/android/server/wm/ActivityRecord$State;->RESUMED:Lcom/android/server/wm/ActivityRecord$State;

    invoke-virtual {v4, v5}, Lcom/android/server/wm/ActivityRecord;->isState(Lcom/android/server/wm/ActivityRecord$State;)Z

    move-result v4

    if-nez v4, :cond_4

    goto :goto_17

    :cond_4
    invoke-virtual {v0}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    const/4 v4, -0x4

    if-nez v2, :cond_2

    const-string v5, "WindowManager"

    const-string v8, "Failed to generate DisplayHash. Window is not on a display"

    invoke-static {v5, v8}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayHashController:Lcom/android/server/wm/DisplayHashController;

    invoke-virtual {v5, p5, v4}, Lcom/android/server/wm/DisplayHashController;->sendDisplayHashError(Landroid/os/RemoteCallback;I)V

    monitor-exit v1
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_0

    goto :goto_a

    nop

    :goto_20
    invoke-direct {v0, p3}, Landroid/graphics/Rect;-><init>(Landroid/graphics/Rect;)V

    goto :goto_18

    nop

    :goto_21
    move-object v4, p4

    goto :goto_13

    nop
.end method
""",
        "method_anchors": ['new-instance v0, Landroid/graphics/Rect;', 'invoke-direct {v0, p3}, Landroid/graphics/Rect;-><init>(Landroid/graphics/Rect;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;', 'move-result-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getBlurWallpaperBmp__Landroid_graphics_Bitmap_",
        "method":      ".method getBlurWallpaperBmp()Landroid/graphics/Bitmap;",
        "method_name": 'getBlurWallpaperBmp',
        "type":        "method_replace",
        "search": """\
.method getBlurWallpaperBmp()Landroid/graphics/Bitmap;
    .registers 2

    invoke-static {}, Lcom/android/server/wm/WindowManagerServiceStub;->get()Lcom/android/server/wm/WindowManagerServiceStub;

    move-result-object v0

    invoke-interface {v0}, Lcom/android/server/wm/WindowManagerServiceStub;->getBlurWallpaperBmp()Landroid/graphics/Bitmap;

    move-result-object v0

    return-object v0
.end method
""",
        "replacement": """\
.method getBlurWallpaperBmp()Landroid/graphics/Bitmap;
    .registers 2

    goto :goto_2

    nop

    :goto_0
    invoke-interface {v0}, Lcom/android/server/wm/WindowManagerServiceStub;->getBlurWallpaperBmp()Landroid/graphics/Bitmap;

    move-result-object v0

    goto :goto_1

    nop

    :goto_1
    return-object v0

    :goto_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerServiceStub;->get()Lcom/android/server/wm/WindowManagerServiceStub;

    move-result-object v0

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-static {}, Lcom/android/server/wm/WindowManagerServiceStub;->get()Lcom/android/server/wm/WindowManagerServiceStub;', 'move-result-object v0', 'invoke-interface {v0}, Lcom/android/server/wm/WindowManagerServiceStub;->getBlurWallpaperBmp()Landroid/graphics/Bitmap;', 'move-result-object v0', 'return-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getCaptureArgs_ILandroid_window_ScreenCapture_CaptureArgs__L",
        "method":      ".method getCaptureArgs(ILandroid/window/ScreenCapture$CaptureArgs;)Landroid/window/ScreenCapture$LayerCaptureArgs;",
        "method_name": 'getCaptureArgs',
        "type":        "method_replace",
        "search": """\
.method getCaptureArgs(ILandroid/window/ScreenCapture$CaptureArgs;)Landroid/window/ScreenCapture$LayerCaptureArgs;
    .registers 8

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    if-eqz v1, :cond_2

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getSurfaceControl()Landroid/view/SurfaceControl;

    move-result-object v2

    if-nez p2, :cond_0

    new-instance v3, Landroid/window/ScreenCapture$CaptureArgs$Builder;

    invoke-direct {v3}, Landroid/window/ScreenCapture$CaptureArgs$Builder;-><init>()V

    invoke-virtual {v3}, Landroid/window/ScreenCapture$CaptureArgs$Builder;->build()Landroid/window/ScreenCapture$CaptureArgs;

    move-result-object v3

    move-object p2, v3

    :cond_0
    iget-object v3, p2, Landroid/window/ScreenCapture$CaptureArgs;->mSourceCrop:Landroid/graphics/Rect;

    invoke-virtual {v3}, Landroid/graphics/Rect;->isEmpty()Z

    move-result v3

    if-eqz v3, :cond_1

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mTmpRect:Landroid/graphics/Rect;

    invoke-virtual {v1, v3}, Lcom/android/server/wm/DisplayContent;->getBounds(Landroid/graphics/Rect;)V

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mTmpRect:Landroid/graphics/Rect;

    const/4 v4, 0x0

    invoke-virtual {v3, v4, v4}, Landroid/graphics/Rect;->offsetTo(II)V

    goto :goto_0

    :cond_1
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mTmpRect:Landroid/graphics/Rect;

    iget-object v4, p2, Landroid/window/ScreenCapture$CaptureArgs;->mSourceCrop:Landroid/graphics/Rect;

    invoke-virtual {v3, v4}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    :goto_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    invoke-static {}, Landroid/view/SurfaceControl;->getCastLayer()Ljava/util/ArrayList;

    move-result-object v0

    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v1

    new-array v1, v1, [Landroid/view/SurfaceControl;

    new-instance v3, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    invoke-direct {v3, v2, p2}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;-><init>(Landroid/view/SurfaceControl;Landroid/window/ScreenCapture$CaptureArgs;)V

    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->toArray([Ljava/lang/Object;)[Ljava/lang/Object;

    move-result-object v4

    check-cast v4, [Landroid/view/SurfaceControl;

    invoke-virtual {v3, v4}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;->setExcludeLayers([Landroid/view/SurfaceControl;)Landroid/window/ScreenCapture$CaptureArgs$Builder;

    move-result-object v3

    check-cast v3, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mTmpRect:Landroid/graphics/Rect;

    invoke-virtual {v3, v4}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;->setSourceCrop(Landroid/graphics/Rect;)Landroid/window/ScreenCapture$CaptureArgs$Builder;

    move-result-object v3

    check-cast v3, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    invoke-virtual {v3}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;->build()Landroid/window/ScreenCapture$LayerCaptureArgs;

    move-result-object v3

    return-object v3

    :cond_2
    :try_start_1
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "Trying to screenshot and invalid display: "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method getCaptureArgs(ILandroid/window/ScreenCapture$CaptureArgs;)Landroid/window/ScreenCapture$LayerCaptureArgs;
    .registers 8

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_d

    nop

    :goto_1
    new-instance v3, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    goto :goto_e

    nop

    :goto_2
    check-cast v4, [Landroid/view/SurfaceControl;

    goto :goto_13

    nop

    :goto_3
    check-cast v3, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    goto :goto_f

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_7

    nop

    :goto_5
    return-object v3

    :cond_0
    :try_start_0
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "Trying to screenshot and invalid display: "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2

    :catchall_0
    move-exception v1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_a

    nop

    :goto_6
    check-cast v3, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;

    goto :goto_11

    nop

    :goto_7
    invoke-static {}, Landroid/view/SurfaceControl;->getCastLayer()Ljava/util/ArrayList;

    move-result-object v0

    goto :goto_12

    nop

    :goto_8
    new-array v1, v1, [Landroid/view/SurfaceControl;

    goto :goto_1

    nop

    :goto_9
    invoke-virtual {v3, v4}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;->setSourceCrop(Landroid/graphics/Rect;)Landroid/window/ScreenCapture$CaptureArgs$Builder;

    move-result-object v3

    goto :goto_3

    nop

    :goto_a
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_10

    nop

    :goto_b
    monitor-enter v0

    :try_start_1
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    if-eqz v1, :cond_0

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getSurfaceControl()Landroid/view/SurfaceControl;

    move-result-object v2

    if-nez p2, :cond_1

    new-instance v3, Landroid/window/ScreenCapture$CaptureArgs$Builder;

    invoke-direct {v3}, Landroid/window/ScreenCapture$CaptureArgs$Builder;-><init>()V

    invoke-virtual {v3}, Landroid/window/ScreenCapture$CaptureArgs$Builder;->build()Landroid/window/ScreenCapture$CaptureArgs;

    move-result-object v3

    move-object p2, v3

    :cond_1
    iget-object v3, p2, Landroid/window/ScreenCapture$CaptureArgs;->mSourceCrop:Landroid/graphics/Rect;

    invoke-virtual {v3}, Landroid/graphics/Rect;->isEmpty()Z

    move-result v3

    if-eqz v3, :cond_2

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mTmpRect:Landroid/graphics/Rect;

    invoke-virtual {v1, v3}, Lcom/android/server/wm/DisplayContent;->getBounds(Landroid/graphics/Rect;)V

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mTmpRect:Landroid/graphics/Rect;

    const/4 v4, 0x0

    invoke-virtual {v3, v4, v4}, Landroid/graphics/Rect;->offsetTo(II)V

    goto :goto_c

    :cond_2
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mTmpRect:Landroid/graphics/Rect;

    iget-object v4, p2, Landroid/window/ScreenCapture$CaptureArgs;->mSourceCrop:Landroid/graphics/Rect;

    invoke-virtual {v3, v4}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    :goto_c
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_4

    nop

    :goto_d
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_b

    nop

    :goto_e
    invoke-direct {v3, v2, p2}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;-><init>(Landroid/view/SurfaceControl;Landroid/window/ScreenCapture$CaptureArgs;)V

    goto :goto_14

    nop

    :goto_f
    invoke-virtual {v3}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;->build()Landroid/window/ScreenCapture$LayerCaptureArgs;

    move-result-object v3

    goto :goto_5

    nop

    :goto_10
    throw v1

    :goto_11
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mTmpRect:Landroid/graphics/Rect;

    goto :goto_9

    nop

    :goto_12
    invoke-virtual {v0}, Ljava/util/ArrayList;->size()I

    move-result v1

    goto :goto_8

    nop

    :goto_13
    invoke-virtual {v3, v4}, Landroid/window/ScreenCapture$LayerCaptureArgs$Builder;->setExcludeLayers([Landroid/view/SurfaceControl;)Landroid/window/ScreenCapture$CaptureArgs$Builder;

    move-result-object v3

    goto :goto_6

    nop

    :goto_14
    invoke-virtual {v0, v1}, Ljava/util/ArrayList;->toArray([Ljava/lang/Object;)[Ljava/lang/Object;

    move-result-object v4

    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;', 'invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;', 'move-result-object v1', 'if-eqz v1, :cond_2'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getDefaultDisplayContentLocked__Lcom_android_server_wm_Displ",
        "method":      ".method getDefaultDisplayContentLocked()Lcom/android/server/wm/DisplayContent;",
        "method_name": 'getDefaultDisplayContentLocked',
        "type":        "method_replace",
        "search": """\
.method getDefaultDisplayContentLocked()Lcom/android/server/wm/DisplayContent;
    .registers 4

    const-string v0, "com.android.server.wm.WindowManagerService.getDefaultDisplayContentLocked()Lcom/android/server/wm/DisplayContent;"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-object v1

    :catchall_0
    move-exception v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw v1
.end method
""",
        "replacement": """\
.method getDefaultDisplayContentLocked()Lcom/android/server/wm/DisplayContent;
    .registers 4

    goto :goto_4

    nop

    :goto_0
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    const/4 v2, 0x0

    invoke-virtual {v1, v2}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop

    :goto_1
    return-object v1

    :catchall_0
    move-exception v1

    goto :goto_2

    nop

    :goto_2
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_3
    throw v1

    :goto_4
    const-string v0, "com.android.server.wm.WindowManagerService.getDefaultDisplayContentLocked()Lcom/android/server/wm/DisplayContent;"

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.getDefaultDisplayContentLocked()Lcom/android/server/wm/DisplayContent;"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;', 'invoke-virtual {v1, v2}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;', 'move-result-object v1', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getDisableSecureWindows__Z",
        "method":      ".method getDisableSecureWindows()Z",
        "method_name": 'getDisableSecureWindows',
        "type":        "method_replace",
        "search": """\
.method getDisableSecureWindows()Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mDisableSecureWindows:Z

    return v0
.end method
""",
        "replacement": """\
.method getDisableSecureWindows()Z
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mDisableSecureWindows:Z

    goto :goto_1

    nop

    :goto_1
    return v0
.end method
""",
        "method_anchors": ['iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mDisableSecureWindows:Z', 'return v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getDisplayAreaPolicyProvider__Lcom_android_server_wm_Display",
        "method":      ".method getDisplayAreaPolicyProvider()Lcom/android/server/wm/DisplayAreaPolicy$Provider;",
        "method_name": 'getDisplayAreaPolicyProvider',
        "type":        "method_replace",
        "search": """\
.method getDisplayAreaPolicyProvider()Lcom/android/server/wm/DisplayAreaPolicy$Provider;
    .registers 2

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayAreaPolicyProvider:Lcom/android/server/wm/DisplayAreaPolicy$Provider;

    return-object v0
.end method
""",
        "replacement": """\
.method getDisplayAreaPolicyProvider()Lcom/android/server/wm/DisplayAreaPolicy$Provider;
    .registers 2

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayAreaPolicyProvider:Lcom/android/server/wm/DisplayAreaPolicy$Provider;

    goto :goto_1

    nop

    :goto_1
    return-object v0
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayAreaPolicyProvider:Lcom/android/server/wm/DisplayAreaPolicy$Provider;', 'return-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getFixedToUserRotation_I_I",
        "method":      ".method getFixedToUserRotation(I)I",
        "method_name": 'getFixedToUserRotation',
        "type":        "method_replace",
        "search": """\
.method getFixedToUserRotation(I)I
    .registers 6

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    if-nez v1, :cond_0

    const-string v2, "WindowManager"

    const-string v3, "Trying to get fixed to user rotation for a missing display."

    invoke-static {v2, v3}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    const/4 v0, -0x1

    return v0

    :cond_0
    :try_start_1
    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getDisplayRotation()Lcom/android/server/wm/DisplayRotation;

    move-result-object v2

    invoke-virtual {v2}, Lcom/android/server/wm/DisplayRotation;->getFixedToUserRotationMode()I

    move-result v2

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return v2

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method getFixedToUserRotation(I)I
    .registers 6

    goto :goto_2

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_7

    nop

    :goto_1
    return v0

    :cond_0
    :try_start_0
    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getDisplayRotation()Lcom/android/server/wm/DisplayRotation;

    move-result-object v2

    invoke-virtual {v2}, Lcom/android/server/wm/DisplayRotation;->getFixedToUserRotationMode()I

    move-result v2

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_5

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_6

    nop

    :goto_3
    monitor-enter v0

    :try_start_1
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    if-nez v1, :cond_0

    const-string v2, "WindowManager"

    const-string v3, "Trying to get fixed to user rotation for a missing display."

    invoke-static {v2, v3}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_0

    nop

    :goto_4
    return v2

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_8

    nop

    :goto_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_4

    nop

    :goto_6
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_3

    nop

    :goto_7
    const/4 v0, -0x1

    goto :goto_1

    nop

    :goto_8
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_9

    nop

    :goto_9
    throw v1
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;', 'invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;', 'move-result-object v1', 'if-nez v1, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getFocusedWindowLocked__Lcom_android_server_wm_WindowState_",
        "method":      ".method getFocusedWindowLocked()Lcom/android/server/wm/WindowState;",
        "method_name": 'getFocusedWindowLocked',
        "type":        "method_replace",
        "search": """\
.method getFocusedWindowLocked()Lcom/android/server/wm/WindowState;
    .registers 3

    const-string v0, "com.android.server.wm.WindowManagerService.getFocusedWindowLocked()Lcom/android/server/wm/WindowState;"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->getTopFocusedDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    iget-object v1, v1, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-object v1

    :catchall_0
    move-exception v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw v1
.end method
""",
        "replacement": """\
.method getFocusedWindowLocked()Lcom/android/server/wm/WindowState;
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-object v1

    :catchall_0
    move-exception v1

    goto :goto_2

    nop

    :goto_1
    const-string v0, "com.android.server.wm.WindowManagerService.getFocusedWindowLocked()Lcom/android/server/wm/WindowState;"

    goto :goto_4

    nop

    :goto_2
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_3
    throw v1

    :goto_4
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->getTopFocusedDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    iget-object v1, v1, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.getFocusedWindowLocked()Lcom/android/server/wm/WindowState;"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;', 'invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->getTopFocusedDisplayContent()Lcom/android/server/wm/DisplayContent;', 'move-result-object v1', 'iget-object v1, v1, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getFoldedArea__Landroid_graphics_Rect_",
        "method":      ".method getFoldedArea()Landroid/graphics/Rect;",
        "method_name": 'getFoldedArea',
        "type":        "method_replace",
        "search": """\
.method getFoldedArea()Landroid/graphics/Rect;
    .registers 5

    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v0

    :try_start_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    :try_start_1
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mPolicy:Lcom/android/server/policy/WindowManagerPolicy;

    invoke-interface {v3}, Lcom/android/server/policy/WindowManagerPolicy;->getFoldedArea()Landroid/graphics/Rect;

    move-result-object v3

    monitor-exit v2
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    return-object v3

    :catchall_0
    move-exception v3

    :try_start_2
    monitor-exit v2
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    :try_start_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v3
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_1

    :catchall_1
    move-exception v2

    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    throw v2
.end method
""",
        "replacement": """\
.method getFoldedArea()Landroid/graphics/Rect;
    .registers 5

    goto :goto_0

    nop

    :goto_0
    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v0

    :try_start_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    :try_start_1
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mPolicy:Lcom/android/server/policy/WindowManagerPolicy;

    invoke-interface {v3}, Lcom/android/server/policy/WindowManagerPolicy;->getFoldedArea()Landroid/graphics/Rect;

    move-result-object v3

    monitor-exit v2
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_5

    nop

    :goto_1
    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    goto :goto_4

    nop

    :goto_2
    throw v2

    :goto_3
    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    goto :goto_2

    nop

    :goto_4
    return-object v3

    :catchall_0
    move-exception v3

    :try_start_2
    monitor-exit v2
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    :try_start_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v3
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_1

    :catchall_1
    move-exception v2

    goto :goto_3

    nop

    :goto_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J', 'move-result-wide v0', 'iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mPolicy:Lcom/android/server/policy/WindowManagerPolicy;', 'invoke-interface {v3}, Lcom/android/server/policy/WindowManagerPolicy;->getFoldedArea()Landroid/graphics/Rect;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getImeFocusRootTaskLocked__Lcom_android_server_wm_Task_",
        "method":      ".method getImeFocusRootTaskLocked()Lcom/android/server/wm/Task;",
        "method_name": 'getImeFocusRootTaskLocked',
        "type":        "method_replace",
        "search": """\
.method getImeFocusRootTaskLocked()Lcom/android/server/wm/Task;
    .registers 5

    const-string v0, "com.android.server.wm.WindowManagerService.getImeFocusRootTaskLocked()Lcom/android/server/wm/Task;"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->getTopFocusedDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    iget-object v2, v1, Lcom/android/server/wm/DisplayContent;->mFocusedApp:Lcom/android/server/wm/ActivityRecord;

    if-eqz v2, :cond_0

    invoke-virtual {v2}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;

    move-result-object v3

    if-eqz v3, :cond_0

    invoke-virtual {v2}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;

    move-result-object v3

    invoke-virtual {v3}, Lcom/android/server/wm/Task;->getRootTask()Lcom/android/server/wm/Task;

    move-result-object v3

    goto :goto_0

    :cond_0
    const/4 v3, 0x0

    :goto_0
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-object v3

    :catchall_0
    move-exception v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw v1
.end method
""",
        "replacement": """\
.method getImeFocusRootTaskLocked()Lcom/android/server/wm/Task;
    .registers 5

    goto :goto_2

    nop

    :goto_0
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_1
    return-object v3

    :catchall_0
    move-exception v1

    goto :goto_0

    nop

    :goto_2
    const-string v0, "com.android.server.wm.WindowManagerService.getImeFocusRootTaskLocked()Lcom/android/server/wm/Task;"

    goto :goto_4

    nop

    :goto_3
    throw v1

    :goto_4
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->getTopFocusedDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    iget-object v2, v1, Lcom/android/server/wm/DisplayContent;->mFocusedApp:Lcom/android/server/wm/ActivityRecord;

    if-eqz v2, :cond_0

    invoke-virtual {v2}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;

    move-result-object v3

    if-eqz v3, :cond_0

    invoke-virtual {v2}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;

    move-result-object v3

    invoke-virtual {v3}, Lcom/android/server/wm/Task;->getRootTask()Lcom/android/server/wm/Task;

    move-result-object v3

    goto :goto_5

    :cond_0
    const/4 v3, 0x0

    :goto_5
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.getImeFocusRootTaskLocked()Lcom/android/server/wm/Task;"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;', 'invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->getTopFocusedDisplayContent()Lcom/android/server/wm/DisplayContent;', 'move-result-object v1', 'iget-object v2, v1, Lcom/android/server/wm/DisplayContent;->mFocusedApp:Lcom/android/server/wm/ActivityRecord;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getInputTargetFromToken_Landroid_os_IBinder__Lcom_android_se",
        "method":      ".method getInputTargetFromToken(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;",
        "method_name": 'getInputTargetFromToken',
        "type":        "method_replace",
        "search": """\
.method getInputTargetFromToken(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;
    .registers 5

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mInputToWindowMap:Ljava/util/HashMap;

    invoke-virtual {v0, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/server/wm/WindowState;

    if-eqz v0, :cond_0

    return-object v0

    :cond_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/EmbeddedWindowController;->get(Landroid/os/IBinder;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    move-result-object v1

    if-eqz v1, :cond_1

    return-object v1

    :cond_1
    const/4 v2, 0x0

    return-object v2
.end method
""",
        "replacement": """\
.method getInputTargetFromToken(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;
    .registers 5

    goto :goto_6

    nop

    :goto_0
    check-cast v0, Lcom/android/server/wm/WindowState;

    goto :goto_a

    nop

    :goto_1
    return-object v0

    :goto_2
    goto :goto_7

    nop

    :goto_3
    const/4 v2, 0x0

    goto :goto_c

    nop

    :goto_4
    return-object v1

    :goto_5
    goto :goto_3

    nop

    :goto_6
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mInputToWindowMap:Ljava/util/HashMap;

    goto :goto_b

    nop

    :goto_7
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    goto :goto_9

    nop

    :goto_8
    if-nez v1, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_4

    nop

    :goto_9
    invoke-virtual {v1, p1}, Lcom/android/server/wm/EmbeddedWindowController;->get(Landroid/os/IBinder;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    move-result-object v1

    goto :goto_8

    nop

    :goto_a
    if-nez v0, :cond_1

    goto :goto_2

    :cond_1
    goto :goto_1

    nop

    :goto_b
    invoke-virtual {v0, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    goto :goto_0

    nop

    :goto_c
    return-object v2
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mInputToWindowMap:Ljava/util/HashMap;', 'invoke-virtual {v0, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;', 'move-result-object v0', 'check-cast v0, Lcom/android/server/wm/WindowState;', 'if-eqz v0, :cond_0', 'return-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getInputTargetFromWindowTokenLocked_Landroid_os_IBinder__Lco",
        "method":      ".method getInputTargetFromWindowTokenLocked(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;",
        "method_name": 'getInputTargetFromWindowTokenLocked',
        "type":        "method_replace",
        "search": """\
.method getInputTargetFromWindowTokenLocked(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;
    .registers 5

    const-string v0, "com.android.server.wm.WindowManagerService.getInputTargetFromWindowTokenLocked(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    invoke-virtual {v1, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/wm/InputTarget;

    if-eqz v1, :cond_0

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-object v1

    :cond_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v2, p1}, Lcom/android/server/wm/EmbeddedWindowController;->getByWindowToken(Landroid/os/IBinder;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    move-result-object v2

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-object v2

    :catchall_0
    move-exception p1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw p1
.end method
""",
        "replacement": """\
.method getInputTargetFromWindowTokenLocked(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;
    .registers 5

    goto :goto_4

    nop

    :goto_0
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_2

    nop

    :goto_1
    return-object v2

    :catchall_0
    move-exception p1

    goto :goto_0

    nop

    :goto_2
    throw p1

    :goto_3
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    invoke-virtual {v1, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/wm/InputTarget;

    if-eqz v1, :cond_0

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-object v1

    :cond_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v2, p1}, Lcom/android/server/wm/EmbeddedWindowController;->getByWindowToken(Landroid/os/IBinder;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    move-result-object v2

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop

    :goto_4
    const-string v0, "com.android.server.wm.WindowManagerService.getInputTargetFromWindowTokenLocked(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;"

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.getInputTargetFromWindowTokenLocked(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;', 'invoke-virtual {v1, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;', 'move-result-object v1', 'check-cast v1, Lcom/android/server/wm/InputTarget;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getMostRecentActivityInAdjacent_Lcom_android_server_wm_Activ",
        "method":      ".method getMostRecentActivityInAdjacent(Lcom/android/server/wm/ActivityRecord;)Lcom/android/server/wm/ActivityRecord;",
        "method_name": 'getMostRecentActivityInAdjacent',
        "type":        "method_replace",
        "search": """\
.method getMostRecentActivityInAdjacent(Lcom/android/server/wm/ActivityRecord;)Lcom/android/server/wm/ActivityRecord;
    .registers 8

    invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getTaskFragment()Lcom/android/server/wm/TaskFragment;

    move-result-object v0

    if-nez v0, :cond_0

    return-object p1

    :cond_0
    invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->isEmbedded()Z

    move-result v1

    if-nez v1, :cond_1

    return-object p1

    :cond_1
    invoke-virtual {v0}, Lcom/android/server/wm/TaskFragment;->hasAdjacentTaskFragment()Z

    move-result v1

    if-nez v1, :cond_2

    return-object p1

    :cond_2
    const/4 v1, 0x1

    new-array v2, v1, [Lcom/android/server/wm/ActivityRecord;

    const/4 v3, 0x0

    aput-object p1, v2, v3

    invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getLastWindowCreateTime()J

    move-result-wide v4

    new-array v1, v1, [J

    aput-wide v4, v1, v3

    new-instance v4, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda15;

    invoke-direct {v4, v0, v1, v2}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda15;-><init>(Lcom/android/server/wm/TaskFragment;[J[Lcom/android/server/wm/ActivityRecord;)V

    invoke-virtual {v0, v4}, Lcom/android/server/wm/TaskFragment;->forOtherAdjacentTaskFragments(Ljava/util/function/Consumer;)V

    aget-object v3, v2, v3

    return-object v3
.end method
""",
        "replacement": """\
.method getMostRecentActivityInAdjacent(Lcom/android/server/wm/ActivityRecord;)Lcom/android/server/wm/ActivityRecord;
    .registers 8

    goto :goto_d

    nop

    :goto_0
    if-eqz v1, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_13

    nop

    :goto_1
    invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->isEmbedded()Z

    move-result v1

    goto :goto_8

    nop

    :goto_2
    if-eqz v0, :cond_1

    goto :goto_16

    :cond_1
    goto :goto_15

    nop

    :goto_3
    return-object v3

    :goto_4
    aget-object v3, v2, v3

    goto :goto_3

    nop

    :goto_5
    return-object p1

    :goto_6
    goto :goto_c

    nop

    :goto_7
    const/4 v1, 0x1

    goto :goto_f

    nop

    :goto_8
    if-eqz v1, :cond_2

    goto :goto_6

    :cond_2
    goto :goto_5

    nop

    :goto_9
    new-array v1, v1, [J

    goto :goto_10

    nop

    :goto_a
    new-instance v4, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda15;

    goto :goto_11

    nop

    :goto_b
    invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getLastWindowCreateTime()J

    move-result-wide v4

    goto :goto_9

    nop

    :goto_c
    invoke-virtual {v0}, Lcom/android/server/wm/TaskFragment;->hasAdjacentTaskFragment()Z

    move-result v1

    goto :goto_0

    nop

    :goto_d
    invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getTaskFragment()Lcom/android/server/wm/TaskFragment;

    move-result-object v0

    goto :goto_2

    nop

    :goto_e
    invoke-virtual {v0, v4}, Lcom/android/server/wm/TaskFragment;->forOtherAdjacentTaskFragments(Ljava/util/function/Consumer;)V

    goto :goto_4

    nop

    :goto_f
    new-array v2, v1, [Lcom/android/server/wm/ActivityRecord;

    goto :goto_17

    nop

    :goto_10
    aput-wide v4, v1, v3

    goto :goto_a

    nop

    :goto_11
    invoke-direct {v4, v0, v1, v2}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda15;-><init>(Lcom/android/server/wm/TaskFragment;[J[Lcom/android/server/wm/ActivityRecord;)V

    goto :goto_e

    nop

    :goto_12
    aput-object p1, v2, v3

    goto :goto_b

    nop

    :goto_13
    return-object p1

    :goto_14
    goto :goto_7

    nop

    :goto_15
    return-object p1

    :goto_16
    goto :goto_1

    nop

    :goto_17
    const/4 v3, 0x0

    goto :goto_12

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getTaskFragment()Lcom/android/server/wm/TaskFragment;', 'move-result-object v0', 'if-nez v0, :cond_0', 'return-object p1', 'invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->isEmbedded()Z', 'move-result v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getMostRecentUsedEmbeddedWindowForBack_Lcom_android_server_w",
        "method":      ".method getMostRecentUsedEmbeddedWindowForBack(Lcom/android/server/wm/WindowState;)Lcom/android/server/wm/WindowState;",
        "method_name": 'getMostRecentUsedEmbeddedWindowForBack',
        "type":        "method_replace",
        "search": """\
.method getMostRecentUsedEmbeddedWindowForBack(Lcom/android/server/wm/WindowState;)Lcom/android/server/wm/WindowState;
    .registers 6

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getActivityRecord()Lcom/android/server/wm/ActivityRecord;

    move-result-object v0

    if-nez v0, :cond_0

    return-object p1

    :cond_0
    invoke-virtual {p0, v0}, Lcom/android/server/wm/WindowManagerService;->getMostRecentActivityInAdjacent(Lcom/android/server/wm/ActivityRecord;)Lcom/android/server/wm/ActivityRecord;

    move-result-object v1

    if-ne v1, v0, :cond_1

    return-object p1

    :cond_1
    nop

    invoke-virtual {v1}, Lcom/android/server/wm/ActivityRecord;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    invoke-virtual {v2, v1}, Lcom/android/server/wm/DisplayContent;->findFocusedWindow(Lcom/android/server/wm/ActivityRecord;)Lcom/android/server/wm/WindowState;

    move-result-object v2

    if-eqz v2, :cond_2

    move-object v3, v2

    goto :goto_0

    :cond_2
    move-object v3, p1

    :goto_0
    return-object v3
.end method
""",
        "replacement": """\
.method getMostRecentUsedEmbeddedWindowForBack(Lcom/android/server/wm/WindowState;)Lcom/android/server/wm/WindowState;
    .registers 6

    goto :goto_0

    nop

    :goto_0
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getActivityRecord()Lcom/android/server/wm/ActivityRecord;

    move-result-object v0

    goto :goto_f

    nop

    :goto_1
    invoke-virtual {v2, v1}, Lcom/android/server/wm/DisplayContent;->findFocusedWindow(Lcom/android/server/wm/ActivityRecord;)Lcom/android/server/wm/WindowState;

    move-result-object v2

    goto :goto_10

    nop

    :goto_2
    return-object p1

    :goto_3
    goto :goto_e

    nop

    :goto_4
    return-object p1

    :goto_5
    nop

    goto :goto_8

    nop

    :goto_6
    if-eq v1, v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_4

    nop

    :goto_7
    move-object v3, v2

    goto :goto_9

    nop

    :goto_8
    invoke-virtual {v1}, Lcom/android/server/wm/ActivityRecord;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    goto :goto_1

    nop

    :goto_9
    goto :goto_d

    :goto_a
    goto :goto_c

    nop

    :goto_b
    return-object v3

    :goto_c
    move-object v3, p1

    :goto_d
    goto :goto_b

    nop

    :goto_e
    invoke-virtual {p0, v0}, Lcom/android/server/wm/WindowManagerService;->getMostRecentActivityInAdjacent(Lcom/android/server/wm/ActivityRecord;)Lcom/android/server/wm/ActivityRecord;

    move-result-object v1

    goto :goto_6

    nop

    :goto_f
    if-eqz v0, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_2

    nop

    :goto_10
    if-nez v2, :cond_2

    goto :goto_a

    :cond_2
    goto :goto_7

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getActivityRecord()Lcom/android/server/wm/ActivityRecord;', 'move-result-object v0', 'if-nez v0, :cond_0', 'return-object p1', 'invoke-virtual {p0, v0}, Lcom/android/server/wm/WindowManagerService;->getMostRecentActivityInAdjacent(Lcom/android/server/wm/ActivityRecord;)Lcom/android/server/wm/ActivityRecord;', 'move-result-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getPossibleDisplayInfoLocked_I_Ljava_util_List_",
        "method":      ".method getPossibleDisplayInfoLocked(I)Ljava/util/List;",
        "method_name": 'getPossibleDisplayInfoLocked',
        "type":        "method_replace",
        "search": """\
.method getPossibleDisplayInfoLocked(I)Ljava/util/List;
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(I)",
            "Ljava/util/List<",
            "Landroid/view/DisplayInfo;",
            ">;"
        }
    .end annotation

    const-string v0, "com.android.server.wm.WindowManagerService.getPossibleDisplayInfoLocked(I)Ljava/util/List;"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mPossibleDisplayInfoMapper:Lcom/android/server/wm/PossibleDisplayInfoMapper;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/PossibleDisplayInfoMapper;->getPossibleDisplayInfos(I)Ljava/util/List;

    move-result-object v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-object v1

    :catchall_0
    move-exception p1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw p1
.end method
""",
        "replacement": """\
.method getPossibleDisplayInfoLocked(I)Ljava/util/List;
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(I)",
            "Ljava/util/List<",
            "Landroid/view/DisplayInfo;",
            ">;"
        }
    .end annotation

    goto :goto_3

    nop

    :goto_0
    return-object v1

    :catchall_0
    move-exception p1

    goto :goto_4

    nop

    :goto_1
    throw p1

    :goto_2
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mPossibleDisplayInfoMapper:Lcom/android/server/wm/PossibleDisplayInfoMapper;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/PossibleDisplayInfoMapper;->getPossibleDisplayInfos(I)Ljava/util/List;

    move-result-object v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop

    :goto_3
    const-string v0, "com.android.server.wm.WindowManagerService.getPossibleDisplayInfoLocked(I)Ljava/util/List;"

    goto :goto_2

    nop

    :goto_4
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.getPossibleDisplayInfoLocked(I)Ljava/util/List;"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mPossibleDisplayInfoMapper:Lcom/android/server/wm/PossibleDisplayInfoMapper;', 'invoke-virtual {v1, p1}, Lcom/android/server/wm/PossibleDisplayInfoMapper;->getPossibleDisplayInfos(I)Ljava/util/List;', 'move-result-object v1', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getStableInsetsLocked_ILandroid_graphics_Rect__V",
        "method":      ".method getStableInsetsLocked(ILandroid/graphics/Rect;)V",
        "method_name": 'getStableInsetsLocked',
        "type":        "method_replace",
        "search": """\
.method getStableInsetsLocked(ILandroid/graphics/Rect;)V
    .registers 10

    const-string v0, "com.android.server.wm.WindowManagerService.getStableInsetsLocked(ILandroid/graphics/Rect;)V"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    invoke-virtual {p2}, Landroid/graphics/Rect;->setEmpty()V

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    if-eqz v1, :cond_0

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getDisplayInfo()Landroid/view/DisplayInfo;

    move-result-object v2

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getDisplayPolicy()Lcom/android/server/wm/DisplayPolicy;

    move-result-object v3

    iget v4, v2, Landroid/view/DisplayInfo;->rotation:I

    iget v5, v2, Landroid/view/DisplayInfo;->logicalWidth:I

    iget v6, v2, Landroid/view/DisplayInfo;->logicalHeight:I

    invoke-virtual {v3, v4, v5, v6}, Lcom/android/server/wm/DisplayPolicy;->getDecorInsetsInfo(III)Lcom/android/server/wm/DisplayPolicy$DecorInsets$Info;

    move-result-object v3

    iget-object v3, v3, Lcom/android/server/wm/DisplayPolicy$DecorInsets$Info;->mConfigInsets:Landroid/graphics/Rect;

    invoke-virtual {p2, v3}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    :cond_0
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-void

    :catchall_0
    move-exception p1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw p1
.end method
""",
        "replacement": """\
.method getStableInsetsLocked(ILandroid/graphics/Rect;)V
    .registers 10

    goto :goto_0

    nop

    :goto_0
    const-string v0, "com.android.server.wm.WindowManagerService.getStableInsetsLocked(ILandroid/graphics/Rect;)V"

    goto :goto_3

    nop

    :goto_1
    throw p1

    :goto_2
    return-void

    :catchall_0
    move-exception p1

    goto :goto_4

    nop

    :goto_3
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    invoke-virtual {p2}, Landroid/graphics/Rect;->setEmpty()V

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    if-eqz v1, :cond_0

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getDisplayInfo()Landroid/view/DisplayInfo;

    move-result-object v2

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getDisplayPolicy()Lcom/android/server/wm/DisplayPolicy;

    move-result-object v3

    iget v4, v2, Landroid/view/DisplayInfo;->rotation:I

    iget v5, v2, Landroid/view/DisplayInfo;->logicalWidth:I

    iget v6, v2, Landroid/view/DisplayInfo;->logicalHeight:I

    invoke-virtual {v3, v4, v5, v6}, Lcom/android/server/wm/DisplayPolicy;->getDecorInsetsInfo(III)Lcom/android/server/wm/DisplayPolicy$DecorInsets$Info;

    move-result-object v3

    iget-object v3, v3, Lcom/android/server/wm/DisplayPolicy$DecorInsets$Info;->mConfigInsets:Landroid/graphics/Rect;

    invoke-virtual {p2, v3}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    :cond_0
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_2

    nop

    :goto_4
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.getStableInsetsLocked(ILandroid/graphics/Rect;)V"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'invoke-virtual {p2}, Landroid/graphics/Rect;->setEmpty()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;', 'invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;', 'move-result-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getTaskWindowContainerInfoForRecordingSession_Landroid_view_",
        "method":      ".method getTaskWindowContainerInfoForRecordingSession(Landroid/view/ContentRecordingSession;)Lcom/android/server/wm/WindowManagerService$WindowContainerInfo;",
        "method_name": 'getTaskWindowContainerInfoForRecordingSession',
        "type":        "method_replace",
        "search": """\
.method getTaskWindowContainerInfoForRecordingSession(Landroid/view/ContentRecordingSession;)Lcom/android/server/wm/WindowManagerService$WindowContainerInfo;
    .registers 9

    const/4 v0, 0x0

    const/4 v1, 0x0

    const/4 v2, 0x0

    invoke-virtual {p1}, Landroid/view/ContentRecordingSession;->getTokenToRecord()Landroid/os/IBinder;

    move-result-object v3

    const-string v4, "WindowManager"

    if-eqz v3, :cond_2

    invoke-virtual {p1}, Landroid/view/ContentRecordingSession;->getTokenToRecord()Landroid/os/IBinder;

    move-result-object v3

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    new-instance v6, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda0;

    invoke-direct {v6, v3}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda0;-><init>(Landroid/os/IBinder;)V

    invoke-virtual {v5, v6}, Lcom/android/server/wm/RootWindowContainer;->getActivity(Ljava/util/function/Predicate;)Lcom/android/server/wm/ActivityRecord;

    move-result-object v1

    if-nez v1, :cond_0

    const-string v5, "Unable to find the activity for this launch cookie"

    invoke-static {v4, v5}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    :cond_0
    invoke-virtual {v1}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;

    move-result-object v5

    if-nez v5, :cond_1

    const-string v5, "Unable to find the task for this launch cookie"

    invoke-static {v4, v5}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_0

    :cond_1
    invoke-virtual {v1}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;

    move-result-object v2

    iget-object v5, v2, Lcom/android/server/wm/Task;->mRemoteToken:Lcom/android/server/wm/WindowContainer$RemoteToken;

    invoke-virtual {v5}, Lcom/android/server/wm/WindowContainer$RemoteToken;->toWindowContainerToken()Landroid/window/WindowContainerToken;

    move-result-object v0

    :cond_2
    :goto_0
    if-nez v0, :cond_4

    invoke-virtual {p1}, Landroid/view/ContentRecordingSession;->getTaskId()I

    move-result v3

    const/4 v5, -0x1

    if-eq v3, v5, :cond_4

    invoke-virtual {p1}, Landroid/view/ContentRecordingSession;->getTaskId()I

    move-result v3

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    new-instance v6, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda1;

    invoke-direct {v6, v3}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda1;-><init>(I)V

    invoke-virtual {v5, v6}, Lcom/android/server/wm/RootWindowContainer;->getTask(Ljava/util/function/Predicate;)Lcom/android/server/wm/Task;

    move-result-object v2

    if-nez v2, :cond_3

    const-string v5, "Unable to find the task for this projection"

    invoke-static {v4, v5}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_1

    :cond_3
    iget-object v5, v2, Lcom/android/server/wm/Task;->mRemoteToken:Lcom/android/server/wm/WindowContainer$RemoteToken;

    invoke-virtual {v5}, Lcom/android/server/wm/WindowContainer$RemoteToken;->toWindowContainerToken()Landroid/window/WindowContainerToken;

    move-result-object v0

    :cond_4
    :goto_1
    const/4 v3, 0x0

    if-nez v0, :cond_5

    const-string v5, "Unable to find the WindowContainerToken for ContentRecordingSession"

    invoke-static {v4, v5}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    return-object v3

    :cond_5
    new-instance v4, Lcom/android/server/wm/WindowManagerService$WindowContainerInfo;

    iget v5, v2, Lcom/android/server/wm/Task;->effectiveUid:I

    invoke-direct {v4, v5, v0, v3}, Lcom/android/server/wm/WindowManagerService$WindowContainerInfo;-><init>(ILandroid/window/WindowContainerToken;Lcom/android/server/wm/WindowManagerService-IA;)V

    return-object v4
.end method
""",
        "replacement": """\
.method getTaskWindowContainerInfoForRecordingSession(Landroid/view/ContentRecordingSession;)Lcom/android/server/wm/WindowManagerService$WindowContainerInfo;
    .registers 9

    goto :goto_2e

    nop

    :goto_0
    invoke-static {v4, v5}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_2f

    nop

    :goto_1
    new-instance v4, Lcom/android/server/wm/WindowManagerService$WindowContainerInfo;

    goto :goto_32

    nop

    :goto_2
    invoke-virtual {p1}, Landroid/view/ContentRecordingSession;->getTaskId()I

    move-result v3

    goto :goto_26

    nop

    :goto_3
    if-eqz v0, :cond_0

    goto :goto_d

    :cond_0
    goto :goto_2

    nop

    :goto_4
    goto :goto_1d

    :goto_5
    goto :goto_12

    nop

    :goto_6
    goto :goto_d

    :goto_7
    goto :goto_28

    nop

    :goto_8
    invoke-direct {v6, v3}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda1;-><init>(I)V

    goto :goto_15

    nop

    :goto_9
    new-instance v6, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda0;

    goto :goto_a

    nop

    :goto_a
    invoke-direct {v6, v3}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda0;-><init>(Landroid/os/IBinder;)V

    goto :goto_e

    nop

    :goto_b
    const-string v5, "Unable to find the task for this projection"

    goto :goto_1e

    nop

    :goto_c
    invoke-virtual {v5}, Lcom/android/server/wm/WindowContainer$RemoteToken;->toWindowContainerToken()Landroid/window/WindowContainerToken;

    move-result-object v0

    :goto_d
    goto :goto_19

    nop

    :goto_e
    invoke-virtual {v5, v6}, Lcom/android/server/wm/RootWindowContainer;->getActivity(Ljava/util/function/Predicate;)Lcom/android/server/wm/ActivityRecord;

    move-result-object v1

    goto :goto_33

    nop

    :goto_f
    if-nez v3, :cond_1

    goto :goto_1d

    :cond_1
    goto :goto_2b

    nop

    :goto_10
    iget-object v5, v2, Lcom/android/server/wm/Task;->mRemoteToken:Lcom/android/server/wm/WindowContainer$RemoteToken;

    goto :goto_1c

    nop

    :goto_11
    invoke-virtual {v1}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;

    move-result-object v5

    goto :goto_18

    nop

    :goto_12
    invoke-virtual {v1}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;

    move-result-object v2

    goto :goto_10

    nop

    :goto_13
    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    goto :goto_9

    nop

    :goto_14
    invoke-virtual {p1}, Landroid/view/ContentRecordingSession;->getTokenToRecord()Landroid/os/IBinder;

    move-result-object v3

    goto :goto_23

    nop

    :goto_15
    invoke-virtual {v5, v6}, Lcom/android/server/wm/RootWindowContainer;->getTask(Ljava/util/function/Predicate;)Lcom/android/server/wm/Task;

    move-result-object v2

    goto :goto_2c

    nop

    :goto_16
    invoke-direct {v4, v5, v0, v3}, Lcom/android/server/wm/WindowManagerService$WindowContainerInfo;-><init>(ILandroid/window/WindowContainerToken;Lcom/android/server/wm/WindowManagerService-IA;)V

    goto :goto_20

    nop

    :goto_17
    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    goto :goto_27

    nop

    :goto_18
    if-eqz v5, :cond_2

    goto :goto_5

    :cond_2
    goto :goto_2a

    nop

    :goto_19
    const/4 v3, 0x0

    goto :goto_34

    nop

    :goto_1a
    const/4 v1, 0x0

    goto :goto_31

    nop

    :goto_1b
    invoke-virtual {p1}, Landroid/view/ContentRecordingSession;->getTaskId()I

    move-result v3

    goto :goto_17

    nop

    :goto_1c
    invoke-virtual {v5}, Lcom/android/server/wm/WindowContainer$RemoteToken;->toWindowContainerToken()Landroid/window/WindowContainerToken;

    move-result-object v0

    :goto_1d
    goto :goto_3

    nop

    :goto_1e
    invoke-static {v4, v5}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_6

    nop

    :goto_1f
    const-string v5, "Unable to find the WindowContainerToken for ContentRecordingSession"

    goto :goto_22

    nop

    :goto_20
    return-object v4

    :goto_21
    invoke-static {v4, v5}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_4

    nop

    :goto_22
    invoke-static {v4, v5}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    goto :goto_24

    nop

    :goto_23
    const-string v4, "WindowManager"

    goto :goto_f

    nop

    :goto_24
    return-object v3

    :goto_25
    goto :goto_1

    nop

    :goto_26
    const/4 v5, -0x1

    goto :goto_29

    nop

    :goto_27
    new-instance v6, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda1;

    goto :goto_8

    nop

    :goto_28
    iget-object v5, v2, Lcom/android/server/wm/Task;->mRemoteToken:Lcom/android/server/wm/WindowContainer$RemoteToken;

    goto :goto_c

    nop

    :goto_29
    if-ne v3, v5, :cond_3

    goto :goto_d

    :cond_3
    goto :goto_1b

    nop

    :goto_2a
    const-string v5, "Unable to find the task for this launch cookie"

    goto :goto_21

    nop

    :goto_2b
    invoke-virtual {p1}, Landroid/view/ContentRecordingSession;->getTokenToRecord()Landroid/os/IBinder;

    move-result-object v3

    goto :goto_13

    nop

    :goto_2c
    if-eqz v2, :cond_4

    goto :goto_7

    :cond_4
    goto :goto_b

    nop

    :goto_2d
    const-string v5, "Unable to find the activity for this launch cookie"

    goto :goto_0

    nop

    :goto_2e
    const/4 v0, 0x0

    goto :goto_1a

    nop

    :goto_2f
    goto :goto_1d

    :goto_30
    goto :goto_11

    nop

    :goto_31
    const/4 v2, 0x0

    goto :goto_14

    nop

    :goto_32
    iget v5, v2, Lcom/android/server/wm/Task;->effectiveUid:I

    goto :goto_16

    nop

    :goto_33
    if-eqz v1, :cond_5

    goto :goto_30

    :cond_5
    goto :goto_2d

    nop

    :goto_34
    if-eqz v0, :cond_6

    goto :goto_25

    :cond_6
    goto :goto_1f

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p1}, Landroid/view/ContentRecordingSession;->getTokenToRecord()Landroid/os/IBinder;', 'move-result-object v3', 'const-string v4, "WindowManager"', 'if-eqz v3, :cond_2', 'invoke-virtual {p1}, Landroid/view/ContentRecordingSession;->getTokenToRecord()Landroid/os/IBinder;', 'move-result-object v3'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getUserAssignedToDisplay_I_I",
        "method":      ".method getUserAssignedToDisplay(I)I",
        "method_name": 'getUserAssignedToDisplay',
        "type":        "method_replace",
        "search": """\
.method getUserAssignedToDisplay(I)I
    .registers 3

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;

    invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->getUserAssignedToDisplay(I)I

    move-result v0

    return v0
.end method
""",
        "replacement": """\
.method getUserAssignedToDisplay(I)I
    .registers 3

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->getUserAssignedToDisplay(I)I

    move-result v0

    goto :goto_2

    nop

    :goto_1
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;

    goto :goto_0

    nop

    :goto_2
    return v0
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;', 'invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->getUserAssignedToDisplay(I)I', 'move-result v0', 'return v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_getUserMainDisplayContentLocked_I_Lcom_android_server_wm_Dis",
        "method":      ".method getUserMainDisplayContentLocked(I)Lcom/android/server/wm/DisplayContent;",
        "method_name": 'getUserMainDisplayContentLocked',
        "type":        "method_replace",
        "search": """\
.method getUserMainDisplayContentLocked(I)Lcom/android/server/wm/DisplayContent;
    .registers 5

    const-string v0, "com.android.server.wm.WindowManagerService.getUserMainDisplayContentLocked(I)Lcom/android/server/wm/DisplayContent;"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;

    invoke-virtual {v1, p1}, Lcom/android/server/pm/UserManagerInternal;->getMainDisplayAssignedToUser(I)I

    move-result v1

    const/4 v2, -0x1

    if-ne v1, v2, :cond_0

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    const/4 v0, 0x0

    return-object v0

    :cond_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v2, v1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-object v2

    :catchall_0
    move-exception p1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw p1
.end method
""",
        "replacement": """\
.method getUserMainDisplayContentLocked(I)Lcom/android/server/wm/DisplayContent;
    .registers 5

    goto :goto_1

    nop

    :goto_0
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;

    invoke-virtual {v1, p1}, Lcom/android/server/pm/UserManagerInternal;->getMainDisplayAssignedToUser(I)I

    move-result v1

    const/4 v2, -0x1

    if-ne v1, v2, :cond_0

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    const/4 v0, 0x0

    return-object v0

    :cond_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v2, v1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_4

    nop

    :goto_1
    const-string v0, "com.android.server.wm.WindowManagerService.getUserMainDisplayContentLocked(I)Lcom/android/server/wm/DisplayContent;"

    goto :goto_0

    nop

    :goto_2
    throw p1

    :goto_3
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_2

    nop

    :goto_4
    return-object v2

    :catchall_0
    move-exception p1

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.getUserMainDisplayContentLocked(I)Lcom/android/server/wm/DisplayContent;"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;', 'invoke-virtual {v1, p1}, Lcom/android/server/pm/UserManagerInternal;->getMainDisplayAssignedToUser(I)I', 'move-result v1', 'if-ne v1, v2, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_grantEmbeddedWindowFocus_Lcom_android_server_wm_Session_Land",
        "method":      ".method grantEmbeddedWindowFocus(Lcom/android/server/wm/Session;Landroid/view/IWindow;Landroid/window/InputTransferToken;Z)V",
        "method_name": 'grantEmbeddedWindowFocus',
        "type":        "method_replace",
        "search": """\
.method grantEmbeddedWindowFocus(Lcom/android/server/wm/Session;Landroid/view/IWindow;Landroid/window/InputTransferToken;Z)V
    .registers 16

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    nop

    const/4 v1, 0x0

    :try_start_0
    invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v2

    if-nez v2, :cond_0

    const-string v1, "WindowManager"

    const-string v3, "Host window not found"

    invoke-static {v1, v3}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_0
    :try_start_1
    iget-object v3, v2, Lcom/android/server/wm/WindowState;->mInputChannelToken:Landroid/os/IBinder;

    if-nez v3, :cond_1

    const-string v1, "WindowManager"

    const-string v3, "Host window does not have an input channel"

    invoke-static {v1, v3}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_1
    :try_start_2
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v3, p3}, Lcom/android/server/wm/EmbeddedWindowController;->getByInputTransferToken(Landroid/window/InputTransferToken;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    move-result-object v3

    if-nez v3, :cond_2

    const-string v1, "WindowManager"

    const-string v4, "Embedded window not found"

    invoke-static {v1, v4}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_2
    :try_start_3
    iget-object v4, v3, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mHostWindowState:Lcom/android/server/wm/WindowState;

    if-eq v4, v2, :cond_3

    const-string v1, "WindowManager"

    const-string v4, "Embedded window does not belong to the host"

    invoke-static {v1, v4}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_3
    const v4, 0xf231

    if-eqz p4, :cond_4

    :try_start_4
    iget-object v5, v2, Lcom/android/server/wm/WindowState;->mInputWindowHandle:Lcom/android/server/wm/InputWindowHandleWrapper;

    invoke-virtual {v3}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->getInputChannelToken()Landroid/os/IBinder;

    move-result-object v6

    invoke-virtual {v5, v6}, Lcom/android/server/wm/InputWindowHandleWrapper;->setFocusTransferTarget(Landroid/os/IBinder;)V

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "Transfer focus request "

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    const-string v6, "reason=grantEmbeddedWindowFocus(true)"

    filled-new-array {v5, v6}, [Ljava/lang/Object;

    move-result-object v5

    invoke-static {v4, v5}, Landroid/util/EventLog;->writeEvent(I[Ljava/lang/Object;)I

    goto :goto_0

    :cond_4
    iget-object v5, v2, Lcom/android/server/wm/WindowState;->mInputWindowHandle:Lcom/android/server/wm/InputWindowHandleWrapper;

    const/4 v6, 0x0

    invoke-virtual {v5, v6}, Lcom/android/server/wm/InputWindowHandleWrapper;->setFocusTransferTarget(Landroid/os/IBinder;)V

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "Transfer focus request "

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    const-string v6, "reason=grantEmbeddedWindowFocus(false)"

    filled-new-array {v5, v6}, [Ljava/lang/Object;

    move-result-object v5

    invoke-static {v4, v5}, Landroid/util/EventLog;->writeEvent(I[Ljava/lang/Object;)I

    :goto_0
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v2}, Lcom/android/server/wm/WindowState;->getDisplayId()I

    move-result v5

    invoke-virtual {v4, v5}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v4

    if-eqz v4, :cond_5

    invoke-virtual {v4}, Lcom/android/server/wm/DisplayContent;->getInputMonitor()Lcom/android/server/wm/InputMonitor;

    move-result-object v5

    const/4 v6, 0x1

    invoke-virtual {v5, v6}, Lcom/android/server/wm/InputMonitor;->updateInputWindowsLw(Z)V

    :cond_5
    sget-object v5, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_FOCUS_enabled:[Z

    aget-boolean v5, v5, v1

    if-eqz v5, :cond_6

    invoke-static {v3}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    invoke-static {p4}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v6

    sget-object v7, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_FOCUS:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v5, v6}, [Ljava/lang/Object;

    move-result-object v8

    const-wide v9, -0x540e87ffbaebc8f8L

    invoke-static {v7, v9, v10, v1, v8}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_6
    monitor-exit v0
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_5
    monitor-exit v0
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method grantEmbeddedWindowFocus(Lcom/android/server/wm/Session;Landroid/view/IWindow;Landroid/window/InputTransferToken;Z)V
    .registers 16

    goto :goto_13

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_5

    nop

    :goto_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_4

    nop

    :goto_2
    const v4, 0xf231

    goto :goto_c

    nop

    :goto_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_12

    nop

    :goto_4
    monitor-enter v0

    nop

    goto :goto_10

    nop

    :goto_5
    return-void

    :catchall_0
    move-exception v1

    :try_start_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_3

    nop

    :goto_6
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_a

    nop

    :goto_7
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_b

    nop

    :goto_8
    return-void

    :cond_0
    :try_start_1
    iget-object v4, v3, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mHostWindowState:Lcom/android/server/wm/WindowState;

    if-eq v4, v2, :cond_6

    const-string v1, "WindowManager"

    const-string v4, "Embedded window does not belong to the host"

    invoke-static {v1, v4}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_9

    nop

    :goto_9
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_f

    nop

    :goto_a
    return-void

    :cond_1
    :try_start_2
    iget-object v3, v2, Lcom/android/server/wm/WindowState;->mInputChannelToken:Landroid/os/IBinder;

    if-nez v3, :cond_2

    const-string v1, "WindowManager"

    const-string v3, "Host window does not have an input channel"

    invoke-static {v1, v3}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_7

    nop

    :goto_b
    return-void

    :cond_2
    :try_start_3
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v3, p3}, Lcom/android/server/wm/EmbeddedWindowController;->getByInputTransferToken(Landroid/window/InputTransferToken;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    move-result-object v3

    if-nez v3, :cond_0

    const-string v1, "WindowManager"

    const-string v4, "Embedded window not found"

    invoke-static {v1, v4}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    goto :goto_11

    nop

    :goto_c
    if-nez p4, :cond_3

    goto :goto_d

    :cond_3
    :try_start_4
    iget-object v5, v2, Lcom/android/server/wm/WindowState;->mInputWindowHandle:Lcom/android/server/wm/InputWindowHandleWrapper;

    invoke-virtual {v3}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->getInputChannelToken()Landroid/os/IBinder;

    move-result-object v6

    invoke-virtual {v5, v6}, Lcom/android/server/wm/InputWindowHandleWrapper;->setFocusTransferTarget(Landroid/os/IBinder;)V

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "Transfer focus request "

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    const-string v6, "reason=grantEmbeddedWindowFocus(true)"

    filled-new-array {v5, v6}, [Ljava/lang/Object;

    move-result-object v5

    invoke-static {v4, v5}, Landroid/util/EventLog;->writeEvent(I[Ljava/lang/Object;)I

    goto :goto_e

    :goto_d
    iget-object v5, v2, Lcom/android/server/wm/WindowState;->mInputWindowHandle:Lcom/android/server/wm/InputWindowHandleWrapper;

    const/4 v6, 0x0

    invoke-virtual {v5, v6}, Lcom/android/server/wm/InputWindowHandleWrapper;->setFocusTransferTarget(Landroid/os/IBinder;)V

    new-instance v5, Ljava/lang/StringBuilder;

    invoke-direct {v5}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "Transfer focus request "

    invoke-virtual {v5, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v5

    invoke-virtual {v5}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v5

    const-string v6, "reason=grantEmbeddedWindowFocus(false)"

    filled-new-array {v5, v6}, [Ljava/lang/Object;

    move-result-object v5

    invoke-static {v4, v5}, Landroid/util/EventLog;->writeEvent(I[Ljava/lang/Object;)I

    :goto_e
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v2}, Lcom/android/server/wm/WindowState;->getDisplayId()I

    move-result v5

    invoke-virtual {v4, v5}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v4

    if-eqz v4, :cond_4

    invoke-virtual {v4}, Lcom/android/server/wm/DisplayContent;->getInputMonitor()Lcom/android/server/wm/InputMonitor;

    move-result-object v5

    const/4 v6, 0x1

    invoke-virtual {v5, v6}, Lcom/android/server/wm/InputMonitor;->updateInputWindowsLw(Z)V

    :cond_4
    sget-object v5, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_FOCUS_enabled:[Z

    aget-boolean v5, v5, v1

    if-eqz v5, :cond_5

    invoke-static {v3}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    invoke-static {p4}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v6

    sget-object v7, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_FOCUS:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v5, v6}, [Ljava/lang/Object;

    move-result-object v8

    const-wide v9, -0x540e87ffbaebc8f8L

    invoke-static {v7, v9, v10, v1, v8}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_5
    monitor-exit v0
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    goto :goto_0

    nop

    :goto_f
    return-void

    :cond_6
    goto :goto_2

    nop

    :goto_10
    const/4 v1, 0x0

    :try_start_5
    invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v2

    if-nez v2, :cond_1

    const-string v1, "WindowManager"

    const-string v3, "Host window not found"

    invoke-static {v1, v3}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_0

    goto :goto_6

    nop

    :goto_11
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_8

    nop

    :goto_12
    throw v1

    :goto_13
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;', 'move-result-object v2', 'if-nez v2, :cond_0', 'const-string v1, "WindowManager"'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_grantEmbeddedWindowFocus_Lcom_android_server_wm_Session_Land",
        "method":      ".method grantEmbeddedWindowFocus(Lcom/android/server/wm/Session;Landroid/window/InputTransferToken;Z)V",
        "method_name": 'grantEmbeddedWindowFocus',
        "type":        "method_replace",
        "search": """\
.method grantEmbeddedWindowFocus(Lcom/android/server/wm/Session;Landroid/window/InputTransferToken;Z)V
    .registers 20

    move-object/from16 v1, p0

    move-object/from16 v2, p1

    iget-object v3, v1, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v3

    :try_start_0
    iget-object v0, v1, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    move-object/from16 v4, p2

    :try_start_1
    invoke-virtual {v0, v4}, Lcom/android/server/wm/EmbeddedWindowController;->getByInputTransferToken(Landroid/window/InputTransferToken;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    move-result-object v0

    if-nez v0, :cond_0

    const-string v5, "WindowManager"

    const-string v6, "Embedded window not found"

    invoke-static {v5, v6}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v3
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_0
    :try_start_2
    iget-object v5, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mSession:Lcom/android/server/wm/Session;

    if-eq v5, v2, :cond_1

    const-string v5, "WindowManager"

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "Window not in session:"

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v5, v6}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v3
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_1
    :try_start_3
    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->getInputChannelToken()Landroid/os/IBinder;

    move-result-object v5

    if-nez v5, :cond_2

    const-string v6, "WindowManager"

    const-string v7, "Focus token found but input channel token not found"

    invoke-static {v6, v7}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v3
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_2
    :try_start_4
    iget-object v6, v1, Lcom/android/server/wm/WindowManagerService;->mTransactionFactory:Ljava/util/function/Supplier;

    invoke-interface {v6}, Ljava/util/function/Supplier;->get()Ljava/lang/Object;

    move-result-object v6

    check-cast v6, Landroid/view/SurfaceControl$Transaction;

    iget v7, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mDisplayId:I

    const v8, 0xf231

    const/4 v9, 0x0

    if-eqz p3, :cond_3

    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->toString()Ljava/lang/String;

    move-result-object v10

    invoke-virtual {v6, v5, v10, v7}, Landroid/view/SurfaceControl$Transaction;->setFocusedWindow(Landroid/os/IBinder;Ljava/lang/String;I)Landroid/view/SurfaceControl$Transaction;

    move-result-object v10

    invoke-virtual {v10}, Landroid/view/SurfaceControl$Transaction;->apply()V

    new-instance v10, Ljava/lang/StringBuilder;

    invoke-direct {v10}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "Focus request "

    invoke-virtual {v10, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v10

    const-string v11, "reason=grantEmbeddedWindowFocus(true)"

    filled-new-array {v10, v11}, [Ljava/lang/Object;

    move-result-object v10

    invoke-static {v8, v10}, Landroid/util/EventLog;->writeEvent(I[Ljava/lang/Object;)I

    goto :goto_1

    :cond_3
    iget-object v10, v1, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v10, v7}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v10

    const/4 v11, 0x0

    if-nez v10, :cond_4

    move-object v12, v11

    goto :goto_0

    :cond_4
    invoke-virtual {v10}, Lcom/android/server/wm/DisplayContent;->findFocusedWindow()Lcom/android/server/wm/WindowState;

    move-result-object v12

    :goto_0
    if-nez v12, :cond_6

    invoke-virtual {v6, v11, v11, v7}, Landroid/view/SurfaceControl$Transaction;->setFocusedWindow(Landroid/os/IBinder;Ljava/lang/String;I)Landroid/view/SurfaceControl$Transaction;

    move-result-object v8

    invoke-virtual {v8}, Landroid/view/SurfaceControl$Transaction;->apply()V

    sget-object v8, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_FOCUS_enabled:[Z

    aget-boolean v8, v8, v9

    if-eqz v8, :cond_5

    invoke-static {v0}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    sget-object v11, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_FOCUS:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v8}, [Ljava/lang/Object;

    move-result-object v13

    const-wide v14, -0x669d46a8ed9bc71aL

    invoke-static {v11, v14, v15, v9, v13}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_5
    monitor-exit v3
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_6
    :try_start_5
    iget-object v11, v12, Lcom/android/server/wm/WindowState;->mInputChannelToken:Landroid/os/IBinder;

    invoke-virtual {v12}, Lcom/android/server/wm/WindowState;->getName()Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v6, v11, v13, v7}, Landroid/view/SurfaceControl$Transaction;->setFocusedWindow(Landroid/os/IBinder;Ljava/lang/String;I)Landroid/view/SurfaceControl$Transaction;

    move-result-object v11

    invoke-virtual {v11}, Landroid/view/SurfaceControl$Transaction;->apply()V

    new-instance v11, Ljava/lang/StringBuilder;

    invoke-direct {v11}, Ljava/lang/StringBuilder;-><init>()V

    const-string v13, "Focus request "

    invoke-virtual {v11, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v11

    invoke-virtual {v11, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v11

    invoke-virtual {v11}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v11

    const-string v13, "reason=grantEmbeddedWindowFocus(false)"

    filled-new-array {v11, v13}, [Ljava/lang/Object;

    move-result-object v11

    invoke-static {v8, v11}, Landroid/util/EventLog;->writeEvent(I[Ljava/lang/Object;)I

    :goto_1
    sget-object v8, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_FOCUS_enabled:[Z

    aget-boolean v8, v8, v9

    if-eqz v8, :cond_7

    invoke-static {v0}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    invoke-static/range {p3 .. p3}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v10

    sget-object v11, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_FOCUS:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v8, v10}, [Ljava/lang/Object;

    move-result-object v12

    const-wide v13, -0x540e87ffbaebc8f8L

    invoke-static {v11, v13, v14, v9, v12}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_7
    monitor-exit v3
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v0

    goto :goto_2

    :catchall_1
    move-exception v0

    move-object/from16 v4, p2

    :goto_2
    :try_start_6
    monitor-exit v3
    :try_end_6
    .catchall {:try_start_6 .. :try_end_6} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v0
.end method
""",
        "replacement": """\
.method grantEmbeddedWindowFocus(Lcom/android/server/wm/Session;Landroid/window/InputTransferToken;Z)V
    .registers 20

    goto :goto_13

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_5

    nop

    :goto_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_10

    nop

    :goto_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_d

    nop

    :goto_3
    move-object/from16 v2, p1

    goto :goto_11

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_c

    nop

    :goto_5
    return-void

    :cond_0
    :try_start_0
    iget-object v6, v1, Lcom/android/server/wm/WindowManagerService;->mTransactionFactory:Ljava/util/function/Supplier;

    invoke-interface {v6}, Ljava/util/function/Supplier;->get()Ljava/lang/Object;

    move-result-object v6

    check-cast v6, Landroid/view/SurfaceControl$Transaction;

    iget v7, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mDisplayId:I

    const v8, 0xf231

    const/4 v9, 0x0

    if-eqz p3, :cond_1

    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->toString()Ljava/lang/String;

    move-result-object v10

    invoke-virtual {v6, v5, v10, v7}, Landroid/view/SurfaceControl$Transaction;->setFocusedWindow(Landroid/os/IBinder;Ljava/lang/String;I)Landroid/view/SurfaceControl$Transaction;

    move-result-object v10

    invoke-virtual {v10}, Landroid/view/SurfaceControl$Transaction;->apply()V

    new-instance v10, Ljava/lang/StringBuilder;

    invoke-direct {v10}, Ljava/lang/StringBuilder;-><init>()V

    const-string v11, "Focus request "

    invoke-virtual {v10, v11}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v10

    invoke-virtual {v10}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v10

    const-string v11, "reason=grantEmbeddedWindowFocus(true)"

    filled-new-array {v10, v11}, [Ljava/lang/Object;

    move-result-object v10

    invoke-static {v8, v10}, Landroid/util/EventLog;->writeEvent(I[Ljava/lang/Object;)I

    goto :goto_15

    :cond_1
    iget-object v10, v1, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v10, v7}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v10

    const/4 v11, 0x0

    if-nez v10, :cond_2

    move-object v12, v11

    goto :goto_6

    :cond_2
    invoke-virtual {v10}, Lcom/android/server/wm/DisplayContent;->findFocusedWindow()Lcom/android/server/wm/WindowState;

    move-result-object v12

    :goto_6
    if-nez v12, :cond_6

    invoke-virtual {v6, v11, v11, v7}, Landroid/view/SurfaceControl$Transaction;->setFocusedWindow(Landroid/os/IBinder;Ljava/lang/String;I)Landroid/view/SurfaceControl$Transaction;

    move-result-object v8

    invoke-virtual {v8}, Landroid/view/SurfaceControl$Transaction;->apply()V

    sget-object v8, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_FOCUS_enabled:[Z

    aget-boolean v8, v8, v9

    if-eqz v8, :cond_3

    invoke-static {v0}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    sget-object v11, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_FOCUS:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v8}, [Ljava/lang/Object;

    move-result-object v13

    const-wide v14, -0x669d46a8ed9bc71aL

    invoke-static {v11, v14, v15, v9, v13}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_3
    monitor-exit v3
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    goto :goto_b

    nop

    :goto_7
    goto :goto_9

    :catchall_0
    move-exception v0

    goto :goto_8

    nop

    :goto_8
    move-object/from16 v4, p2

    :goto_9
    :try_start_1
    monitor-exit v3
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    goto :goto_2

    nop

    :goto_a
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_16

    nop

    :goto_b
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_14

    nop

    :goto_c
    return-void

    :catchall_1
    move-exception v0

    goto :goto_7

    nop

    :goto_d
    throw v0

    :goto_e
    return-void

    :cond_4
    :try_start_2
    iget-object v5, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mSession:Lcom/android/server/wm/Session;

    if-eq v5, v2, :cond_5

    const-string v5, "WindowManager"

    new-instance v6, Ljava/lang/StringBuilder;

    invoke-direct {v6}, Ljava/lang/StringBuilder;-><init>()V

    const-string v7, "Window not in session:"

    invoke-virtual {v6, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v6

    invoke-virtual {v6}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v6

    invoke-static {v5, v6}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v3
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    goto :goto_1

    nop

    :goto_f
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_e

    nop

    :goto_10
    return-void

    :cond_5
    :try_start_3
    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->getInputChannelToken()Landroid/os/IBinder;

    move-result-object v5

    if-nez v5, :cond_0

    const-string v6, "WindowManager"

    const-string v7, "Focus token found but input channel token not found"

    invoke-static {v6, v7}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v3
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_1

    goto :goto_0

    nop

    :goto_11
    iget-object v3, v1, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_a

    nop

    :goto_12
    move-object/from16 v4, p2

    :try_start_4
    invoke-virtual {v0, v4}, Lcom/android/server/wm/EmbeddedWindowController;->getByInputTransferToken(Landroid/window/InputTransferToken;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    move-result-object v0

    if-nez v0, :cond_4

    const-string v5, "WindowManager"

    const-string v6, "Embedded window not found"

    invoke-static {v5, v6}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v3
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_1

    goto :goto_f

    nop

    :goto_13
    move-object/from16 v1, p0

    goto :goto_3

    nop

    :goto_14
    return-void

    :cond_6
    :try_start_5
    iget-object v11, v12, Lcom/android/server/wm/WindowState;->mInputChannelToken:Landroid/os/IBinder;

    invoke-virtual {v12}, Lcom/android/server/wm/WindowState;->getName()Ljava/lang/String;

    move-result-object v13

    invoke-virtual {v6, v11, v13, v7}, Landroid/view/SurfaceControl$Transaction;->setFocusedWindow(Landroid/os/IBinder;Ljava/lang/String;I)Landroid/view/SurfaceControl$Transaction;

    move-result-object v11

    invoke-virtual {v11}, Landroid/view/SurfaceControl$Transaction;->apply()V

    new-instance v11, Ljava/lang/StringBuilder;

    invoke-direct {v11}, Ljava/lang/StringBuilder;-><init>()V

    const-string v13, "Focus request "

    invoke-virtual {v11, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v11

    invoke-virtual {v11, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v11

    invoke-virtual {v11}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v11

    const-string v13, "reason=grantEmbeddedWindowFocus(false)"

    filled-new-array {v11, v13}, [Ljava/lang/Object;

    move-result-object v11

    invoke-static {v8, v11}, Landroid/util/EventLog;->writeEvent(I[Ljava/lang/Object;)I

    :goto_15
    sget-object v8, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_FOCUS_enabled:[Z

    aget-boolean v8, v8, v9

    if-eqz v8, :cond_7

    invoke-static {v0}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    invoke-static/range {p3 .. p3}, Ljava/lang/String;->valueOf(Z)Ljava/lang/String;

    move-result-object v10

    sget-object v11, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_FOCUS:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v8, v10}, [Ljava/lang/Object;

    move-result-object v12

    const-wide v13, -0x540e87ffbaebc8f8L

    invoke-static {v11, v13, v14, v9, v12}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_7
    monitor-exit v3
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_1

    goto :goto_4

    nop

    :goto_16
    monitor-enter v3

    :try_start_6
    iget-object v0, v1, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;
    :try_end_6
    .catchall {:try_start_6 .. :try_end_6} :catchall_0

    goto :goto_12

    nop
.end method
""",
        "method_anchors": ['iget-object v3, v1, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v0, v1, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;', 'invoke-virtual {v0, v4}, Lcom/android/server/wm/EmbeddedWindowController;->getByInputTransferToken(Landroid/window/InputTransferToken;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;', 'move-result-object v0', 'if-nez v0, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_grantInputChannel_Lcom_android_server_wm_Session_IIILandroid",
        "method":      ".method grantInputChannel(Lcom/android/server/wm/Session;IIILandroid/view/SurfaceControl;Landroid/os/IBinder;Landroid/window/InputTransferToken;IIIILandroid/os/IBinder;Landroid/window/InputTransferToken;Ljava/lang/String;Landroid/view/InputChannel;)V",
        "method_name": 'grantInputChannel',
        "type":        "method_replace",
        "search": """\
.method grantInputChannel(Lcom/android/server/wm/Session;IIILandroid/view/SurfaceControl;Landroid/os/IBinder;Landroid/window/InputTransferToken;IIIILandroid/os/IBinder;Landroid/window/InputTransferToken;Ljava/lang/String;Landroid/view/InputChannel;)V
    .registers 32

    move-object/from16 v1, p0

    move-object/from16 v2, p1

    move/from16 v5, p4

    move/from16 v15, p11

    move-object/from16 v12, p12

    invoke-direct {v1, v2, v5, v12, v15}, Lcom/android/server/wm/WindowManagerService;->sanitizeWindowType(Lcom/android/server/wm/Session;ILandroid/os/IBinder;I)I

    move-result v7

    invoke-static/range {p15 .. p15}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    invoke-static/range {p13 .. p13}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    iget-object v13, v1, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v13

    if-eqz p7, :cond_0

    :try_start_0
    iget-object v0, v1, Lcom/android/server/wm/WindowManagerService;->mInputToWindowMap:Ljava/util/HashMap;

    invoke-virtual/range {p7 .. p7}, Landroid/window/InputTransferToken;->getToken()Landroid/os/IBinder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/server/wm/WindowState;

    goto :goto_0

    :catchall_0
    move-exception v0

    goto :goto_2

    :cond_0
    const/4 v0, 0x0

    :goto_0
    move-object v4, v0

    new-instance v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    and-int/lit8 v3, p8, 0x8

    if-nez v3, :cond_1

    const/4 v3, 0x1

    goto :goto_1

    :cond_1
    const/4 v3, 0x0

    :goto_1
    move v11, v3

    move-object v3, v2

    move-object v2, v1

    move-object v1, v3

    move/from16 v6, p3

    move-object/from16 v3, p6

    move-object/from16 v9, p13

    move-object/from16 v10, p14

    move v8, v5

    move/from16 v5, p2

    invoke-direct/range {v0 .. v11}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;-><init>(Lcom/android/server/wm/Session;Lcom/android/server/wm/WindowManagerService;Landroid/os/IBinder;Lcom/android/server/wm/WindowState;IIIILandroid/window/InputTransferToken;Ljava/lang/String;Z)V

    move-object v1, v2

    move-object/from16 v2, p15

    invoke-virtual {v0, v2}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->openInputChannel(Landroid/view/InputChannel;)V

    iget-object v3, v1, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v2}, Landroid/view/InputChannel;->getToken()Landroid/os/IBinder;

    move-result-object v5

    invoke-virtual {v3, v5, v0}, Lcom/android/server/wm/EmbeddedWindowController;->add(Landroid/os/IBinder;Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;)V

    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->getApplicationHandle()Landroid/view/InputApplicationHandle;

    move-result-object v8

    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->toString()Ljava/lang/String;

    move-result-object v3

    monitor-exit v13
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    invoke-virtual/range {p15 .. p15}, Landroid/view/InputChannel;->getToken()Landroid/os/IBinder;

    move-result-object v2

    const/4 v13, 0x0

    move/from16 v4, p3

    move/from16 v5, p4

    move-object/from16 v6, p5

    move-object/from16 v14, p6

    move/from16 v9, p8

    move/from16 v10, p9

    move/from16 v11, p10

    move v12, v7

    move-object v7, v3

    move/from16 v3, p2

    invoke-direct/range {v1 .. v14}, Lcom/android/server/wm/WindowManagerService;->updateInputChannel(Landroid/os/IBinder;IIILandroid/view/SurfaceControl;Ljava/lang/String;Landroid/view/InputApplicationHandle;IIIILandroid/graphics/Region;Landroid/os/IBinder;)V

    move-object v3, v7

    move v7, v12

    return-void

    :goto_2
    :try_start_1
    monitor-exit v13
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v0
.end method
""",
        "replacement": """\
.method grantInputChannel(Lcom/android/server/wm/Session;IIILandroid/view/SurfaceControl;Landroid/os/IBinder;Landroid/window/InputTransferToken;IIIILandroid/os/IBinder;Landroid/window/InputTransferToken;Ljava/lang/String;Landroid/view/InputChannel;)V
    .registers 32

    goto :goto_9

    nop

    :goto_0
    move/from16 v5, p4

    goto :goto_6

    nop

    :goto_1
    move/from16 v3, p2

    goto :goto_c

    nop

    :goto_2
    invoke-static/range {p13 .. p13}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_10

    nop

    :goto_3
    move-object/from16 v14, p6

    goto :goto_19

    nop

    :goto_4
    invoke-virtual/range {p15 .. p15}, Landroid/view/InputChannel;->getToken()Landroid/os/IBinder;

    move-result-object v2

    goto :goto_16

    nop

    :goto_5
    move/from16 v11, p10

    goto :goto_18

    nop

    :goto_6
    move/from16 v15, p11

    goto :goto_17

    nop

    :goto_7
    throw v0

    :goto_8
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_7

    nop

    :goto_9
    move-object/from16 v1, p0

    goto :goto_d

    nop

    :goto_a
    invoke-direct {v1, v2, v5, v12, v15}, Lcom/android/server/wm/WindowManagerService;->sanitizeWindowType(Lcom/android/server/wm/Session;ILandroid/os/IBinder;I)I

    move-result v7

    goto :goto_15

    nop

    :goto_b
    move/from16 v10, p9

    goto :goto_5

    nop

    :goto_c
    invoke-direct/range {v1 .. v14}, Lcom/android/server/wm/WindowManagerService;->updateInputChannel(Landroid/os/IBinder;IIILandroid/view/SurfaceControl;Ljava/lang/String;Landroid/view/InputApplicationHandle;IIIILandroid/graphics/Region;Landroid/os/IBinder;)V

    goto :goto_1d

    nop

    :goto_d
    move-object/from16 v2, p1

    goto :goto_0

    nop

    :goto_e
    return-void

    :goto_f
    :try_start_0
    monitor-exit v13
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_8

    nop

    :goto_10
    iget-object v13, v1, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_1c

    nop

    :goto_11
    move/from16 v5, p4

    goto :goto_14

    nop

    :goto_12
    move/from16 v4, p3

    goto :goto_11

    nop

    :goto_13
    move-object v7, v3

    goto :goto_1

    nop

    :goto_14
    move-object/from16 v6, p5

    goto :goto_3

    nop

    :goto_15
    invoke-static/range {p15 .. p15}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_2

    nop

    :goto_16
    const/4 v13, 0x0

    goto :goto_12

    nop

    :goto_17
    move-object/from16 v12, p12

    goto :goto_a

    nop

    :goto_18
    move v12, v7

    goto :goto_13

    nop

    :goto_19
    move/from16 v9, p8

    goto :goto_b

    nop

    :goto_1a
    move v7, v12

    goto :goto_e

    nop

    :goto_1b
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_4

    nop

    :goto_1c
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_1e

    nop

    :goto_1d
    move-object v3, v7

    goto :goto_1a

    nop

    :goto_1e
    monitor-enter v13

    goto :goto_1f

    nop

    :goto_1f
    if-nez p7, :cond_0

    goto :goto_20

    :cond_0
    :try_start_1
    iget-object v0, v1, Lcom/android/server/wm/WindowManagerService;->mInputToWindowMap:Ljava/util/HashMap;

    invoke-virtual/range {p7 .. p7}, Landroid/window/InputTransferToken;->getToken()Landroid/os/IBinder;

    move-result-object v3

    invoke-virtual {v0, v3}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/server/wm/WindowState;

    goto :goto_21

    :catchall_0
    move-exception v0

    goto :goto_f

    :goto_20
    const/4 v0, 0x0

    :goto_21
    move-object v4, v0

    new-instance v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    and-int/lit8 v3, p8, 0x8

    if-nez v3, :cond_1

    const/4 v3, 0x1

    goto :goto_22

    :cond_1
    const/4 v3, 0x0

    :goto_22
    move v11, v3

    move-object v3, v2

    move-object v2, v1

    move-object v1, v3

    move/from16 v6, p3

    move-object/from16 v3, p6

    move-object/from16 v9, p13

    move-object/from16 v10, p14

    move v8, v5

    move/from16 v5, p2

    invoke-direct/range {v0 .. v11}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;-><init>(Lcom/android/server/wm/Session;Lcom/android/server/wm/WindowManagerService;Landroid/os/IBinder;Lcom/android/server/wm/WindowState;IIIILandroid/window/InputTransferToken;Ljava/lang/String;Z)V

    move-object v1, v2

    move-object/from16 v2, p15

    invoke-virtual {v0, v2}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->openInputChannel(Landroid/view/InputChannel;)V

    iget-object v3, v1, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v2}, Landroid/view/InputChannel;->getToken()Landroid/os/IBinder;

    move-result-object v5

    invoke-virtual {v3, v5, v0}, Lcom/android/server/wm/EmbeddedWindowController;->add(Landroid/os/IBinder;Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;)V

    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->getApplicationHandle()Landroid/view/InputApplicationHandle;

    move-result-object v8

    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->toString()Ljava/lang/String;

    move-result-object v3

    monitor-exit v13
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_1b

    nop
.end method
""",
        "method_anchors": ['invoke-direct {v1, v2, v5, v12, v15}, Lcom/android/server/wm/WindowManagerService;->sanitizeWindowType(Lcom/android/server/wm/Session;ILandroid/os/IBinder;I)I', 'move-result v7', 'invoke-static/range {p15 .. p15}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;', 'invoke-static/range {p13 .. p13}, Ljava/util/Objects;->requireNonNull(Ljava/lang/Object;)Ljava/lang/Object;', 'iget-object v13, v1, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_handleTaskFocusChange_Lcom_android_server_wm_Task_Lcom_andro",
        "method":      ".method handleTaskFocusChange(Lcom/android/server/wm/Task;Lcom/android/server/wm/ActivityRecord;)V",
        "method_name": 'handleTaskFocusChange',
        "type":        "method_replace",
        "search": """\
.method handleTaskFocusChange(Lcom/android/server/wm/Task;Lcom/android/server/wm/ActivityRecord;)V
    .registers 7

    if-nez p1, :cond_0

    return-void

    :cond_0
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mResumeActivity:Ljava/lang/String;

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mResumeActivity:Ljava/lang/String;

    const-string v1, ".remotediagnosis.RemoteDiagnosisDialogActivity"

    invoke-virtual {v0, v1}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v0

    if-eqz v0, :cond_1

    return-void

    :cond_1
    invoke-virtual {p1}, Lcom/android/server/wm/Task;->isActivityTypeHome()Z

    move-result v0

    if-eqz v0, :cond_3

    invoke-virtual {p1}, Lcom/android/server/wm/Task;->getDisplayArea()Lcom/android/server/wm/TaskDisplayArea;

    move-result-object v0

    invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->getFocusedWindow()Lcom/android/server/wm/WindowState;

    move-result-object v1

    if-eqz v1, :cond_2

    if-eqz v0, :cond_2

    invoke-virtual {v1, v0}, Lcom/android/server/wm/WindowState;->isDescendantOf(Lcom/android/server/wm/WindowContainer;)Z

    move-result v2

    if-eqz v2, :cond_2

    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->inFreeformWindowingMode()Z

    move-result v2

    if-nez v2, :cond_2

    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->inMultiWindowMode()Z

    move-result v2

    if-nez v2, :cond_2

    return-void

    :cond_2
    invoke-static {}, Lcom/android/server/wm/MiuiSoScManagerStub;->get()Lcom/android/server/wm/MiuiSoScManagerStub;

    move-result-object v2

    invoke-virtual {v0}, Lcom/android/server/wm/TaskDisplayArea;->getTopRootTask()Lcom/android/server/wm/Task;

    move-result-object v3

    invoke-virtual {v2, v3, p2}, Lcom/android/server/wm/MiuiSoScManagerStub;->handleTaskFocusChange(Lcom/android/server/wm/WindowContainer;Lcom/android/server/wm/ActivityRecord;)Z

    move-result v2

    if-eqz v2, :cond_3

    return-void

    :cond_3
    invoke-static {}, Lcom/android/server/wm/MiuiSoScManagerStub;->get()Lcom/android/server/wm/MiuiSoScManagerStub;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/server/wm/MiuiSoScManagerStub;->skipHandleTaskFocusChangeIfNeeded()Z

    move-result v0

    if-eqz v0, :cond_4

    return-void

    :cond_4
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;

    iget v1, p1, Lcom/android/server/wm/Task;->mTaskId:I

    invoke-virtual {v0, v1, p2}, Lcom/android/server/wm/ActivityTaskManagerService;->setFocusedTask(ILcom/android/server/wm/ActivityRecord;)V

    return-void
.end method
""",
        "replacement": """\
.method handleTaskFocusChange(Lcom/android/server/wm/Task;Lcom/android/server/wm/ActivityRecord;)V
    .registers 7

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {v2, v3, p2}, Lcom/android/server/wm/MiuiSoScManagerStub;->handleTaskFocusChange(Lcom/android/server/wm/WindowContainer;Lcom/android/server/wm/ActivityRecord;)Z

    move-result v2

    goto :goto_18

    nop

    :goto_1
    if-eqz v2, :cond_0

    goto :goto_11

    :cond_0
    goto :goto_10

    nop

    :goto_2
    if-eqz p1, :cond_1

    goto :goto_27

    :cond_1
    goto :goto_26

    nop

    :goto_3
    invoke-virtual {v0}, Lcom/android/server/wm/TaskDisplayArea;->getTopRootTask()Lcom/android/server/wm/Task;

    move-result-object v3

    goto :goto_0

    nop

    :goto_4
    invoke-virtual {v0, v1}, Ljava/lang/String;->contains(Ljava/lang/CharSequence;)Z

    move-result v0

    goto :goto_1d

    nop

    :goto_5
    invoke-virtual {v0, v1, p2}, Lcom/android/server/wm/ActivityTaskManagerService;->setFocusedTask(ILcom/android/server/wm/ActivityRecord;)V

    goto :goto_7

    nop

    :goto_6
    if-nez v1, :cond_2

    goto :goto_11

    :cond_2
    goto :goto_1e

    nop

    :goto_7
    return-void

    :goto_8
    invoke-static {}, Lcom/android/server/wm/MiuiSoScManagerStub;->get()Lcom/android/server/wm/MiuiSoScManagerStub;

    move-result-object v0

    goto :goto_1f

    nop

    :goto_9
    invoke-virtual {v1, v0}, Lcom/android/server/wm/WindowState;->isDescendantOf(Lcom/android/server/wm/WindowContainer;)Z

    move-result v2

    goto :goto_1a

    nop

    :goto_a
    if-nez v0, :cond_3

    goto :goto_1c

    :cond_3
    goto :goto_25

    nop

    :goto_b
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;

    goto :goto_13

    nop

    :goto_c
    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->inMultiWindowMode()Z

    move-result v2

    goto :goto_1

    nop

    :goto_d
    invoke-virtual {p1}, Lcom/android/server/wm/Task;->getDisplayArea()Lcom/android/server/wm/TaskDisplayArea;

    move-result-object v0

    goto :goto_17

    nop

    :goto_e
    return-void

    :goto_f
    goto :goto_8

    nop

    :goto_10
    return-void

    :goto_11
    goto :goto_19

    nop

    :goto_12
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mResumeActivity:Ljava/lang/String;

    goto :goto_a

    nop

    :goto_13
    iget v1, p1, Lcom/android/server/wm/Task;->mTaskId:I

    goto :goto_5

    nop

    :goto_14
    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->inFreeformWindowingMode()Z

    move-result v2

    goto :goto_24

    nop

    :goto_15
    if-nez v0, :cond_4

    goto :goto_f

    :cond_4
    goto :goto_d

    nop

    :goto_16
    if-nez v0, :cond_5

    goto :goto_22

    :cond_5
    goto :goto_21

    nop

    :goto_17
    invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->getFocusedWindow()Lcom/android/server/wm/WindowState;

    move-result-object v1

    goto :goto_6

    nop

    :goto_18
    if-nez v2, :cond_6

    goto :goto_f

    :cond_6
    goto :goto_e

    nop

    :goto_19
    invoke-static {}, Lcom/android/server/wm/MiuiSoScManagerStub;->get()Lcom/android/server/wm/MiuiSoScManagerStub;

    move-result-object v2

    goto :goto_3

    nop

    :goto_1a
    if-nez v2, :cond_7

    goto :goto_11

    :cond_7
    goto :goto_14

    nop

    :goto_1b
    return-void

    :goto_1c
    goto :goto_23

    nop

    :goto_1d
    if-nez v0, :cond_8

    goto :goto_1c

    :cond_8
    goto :goto_1b

    nop

    :goto_1e
    if-nez v0, :cond_9

    goto :goto_11

    :cond_9
    goto :goto_9

    nop

    :goto_1f
    invoke-virtual {v0}, Lcom/android/server/wm/MiuiSoScManagerStub;->skipHandleTaskFocusChangeIfNeeded()Z

    move-result v0

    goto :goto_16

    nop

    :goto_20
    const-string v1, ".remotediagnosis.RemoteDiagnosisDialogActivity"

    goto :goto_4

    nop

    :goto_21
    return-void

    :goto_22
    goto :goto_b

    nop

    :goto_23
    invoke-virtual {p1}, Lcom/android/server/wm/Task;->isActivityTypeHome()Z

    move-result v0

    goto :goto_15

    nop

    :goto_24
    if-eqz v2, :cond_a

    goto :goto_11

    :cond_a
    goto :goto_c

    nop

    :goto_25
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mResumeActivity:Ljava/lang/String;

    goto :goto_20

    nop

    :goto_26
    return-void

    :goto_27
    goto :goto_12

    nop
.end method
""",
        "method_anchors": ['if-nez p1, :cond_0', 'return-void', 'iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mResumeActivity:Ljava/lang/String;', 'if-eqz v0, :cond_1', 'iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mResumeActivity:Ljava/lang/String;', 'const-string v1, ".remotediagnosis.RemoteDiagnosisDialogActivity"'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_hasHdrSupport__Z",
        "method":      ".method hasHdrSupport()Z",
        "method_name": 'hasHdrSupport',
        "type":        "method_replace",
        "search": """\
.method hasHdrSupport()Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mHasHdrSupport:Z

    if-eqz v0, :cond_0

    invoke-virtual {p0}, Lcom/android/server/wm/WindowManagerService;->hasWideColorGamutSupport()Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    return v0
.end method
""",
        "replacement": """\
.method hasHdrSupport()Z
    .registers 2

    goto :goto_2

    nop

    :goto_0
    return v0

    :goto_1
    if-nez v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_8

    nop

    :goto_2
    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mHasHdrSupport:Z

    goto :goto_1

    nop

    :goto_3
    const/4 v0, 0x1

    goto :goto_4

    nop

    :goto_4
    goto :goto_7

    :goto_5
    goto :goto_6

    nop

    :goto_6
    const/4 v0, 0x0

    :goto_7
    goto :goto_0

    nop

    :goto_8
    invoke-virtual {p0}, Lcom/android/server/wm/WindowManagerService;->hasWideColorGamutSupport()Z

    move-result v0

    goto :goto_9

    nop

    :goto_9
    if-nez v0, :cond_1

    goto :goto_5

    :cond_1
    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mHasHdrSupport:Z', 'if-eqz v0, :cond_0', 'invoke-virtual {p0}, Lcom/android/server/wm/WindowManagerService;->hasWideColorGamutSupport()Z', 'move-result v0', 'if-eqz v0, :cond_0', 'return v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_hasWideColorGamutSupport__Z",
        "method":      ".method hasWideColorGamutSupport()Z",
        "method_name": 'hasWideColorGamutSupport',
        "type":        "method_replace",
        "search": """\
.method hasWideColorGamutSupport()Z
    .registers 4

    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mHasWideColorGamutSupport:Z

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    const-string v0, "persist.sys.sf.native_mode"

    invoke-static {v0, v1}, Landroid/os/SystemProperties;->getInt(Ljava/lang/String;I)I

    move-result v0

    const/4 v2, 0x1

    if-eq v0, v2, :cond_0

    move v1, v2

    goto :goto_0

    :cond_0
    nop

    :goto_0
    return v1
.end method
""",
        "replacement": """\
.method hasWideColorGamutSupport()Z
    .registers 4

    goto :goto_5

    nop

    :goto_0
    move v1, v2

    goto :goto_7

    nop

    :goto_1
    const/4 v1, 0x0

    goto :goto_2

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_b

    nop

    :goto_3
    if-ne v0, v2, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_0

    nop

    :goto_4
    return v1

    :goto_5
    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mHasWideColorGamutSupport:Z

    goto :goto_1

    nop

    :goto_6
    invoke-static {v0, v1}, Landroid/os/SystemProperties;->getInt(Ljava/lang/String;I)I

    move-result v0

    goto :goto_a

    nop

    :goto_7
    goto :goto_9

    :goto_8
    nop

    :goto_9
    goto :goto_4

    nop

    :goto_a
    const/4 v2, 0x1

    goto :goto_3

    nop

    :goto_b
    const-string v0, "persist.sys.sf.native_mode"

    goto :goto_6

    nop
.end method
""",
        "method_anchors": ['iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mHasWideColorGamutSupport:Z', 'if-eqz v0, :cond_0', 'const-string v0, "persist.sys.sf.native_mode"', 'invoke-static {v0, v1}, Landroid/os/SystemProperties;->getInt(Ljava/lang/String;I)I', 'move-result v0', 'if-eq v0, v2, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_initMiuiDesktopMode_Landroid_content_Context__V",
        "method":      ".method initMiuiDesktopMode(Landroid/content/Context;)V",
        "method_name": 'initMiuiDesktopMode',
        "type":        "method_replace",
        "search": """\
.method initMiuiDesktopMode(Landroid/content/Context;)V
    .registers 3

    invoke-static {}, Lcom/android/server/wm/MiuiFreeformServiceStub;->getInstance()Lcom/android/server/wm/MiuiFreeformServiceStub;

    move-result-object v0

    invoke-interface {v0, p1}, Lcom/android/server/wm/MiuiFreeformServiceStub;->initDesktop(Landroid/content/Context;)V

    return-void
.end method
""",
        "replacement": """\
.method initMiuiDesktopMode(Landroid/content/Context;)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    invoke-static {}, Lcom/android/server/wm/MiuiFreeformServiceStub;->getInstance()Lcom/android/server/wm/MiuiFreeformServiceStub;

    move-result-object v0

    goto :goto_2

    nop

    :goto_2
    invoke-interface {v0, p1}, Lcom/android/server/wm/MiuiFreeformServiceStub;->initDesktop(Landroid/content/Context;)V

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-static {}, Lcom/android/server/wm/MiuiFreeformServiceStub;->getInstance()Lcom/android/server/wm/MiuiFreeformServiceStub;', 'move-result-object v0', 'invoke-interface {v0, p1}, Lcom/android/server/wm/MiuiFreeformServiceStub;->initDesktop(Landroid/content/Context;)V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_isIgnoreOrientationRequestDisabled__Z",
        "method":      ".method isIgnoreOrientationRequestDisabled()Z",
        "method_name": 'isIgnoreOrientationRequestDisabled',
        "type":        "method_replace",
        "search": """\
.method isIgnoreOrientationRequestDisabled()Z
    .registers 2

    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mIsIgnoreOrientationRequestDisabled:Z

    if-nez v0, :cond_1

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mAppCompatConfiguration:Lcom/android/server/wm/AppCompatConfiguration;

    invoke-virtual {v0}, Lcom/android/server/wm/AppCompatConfiguration;->isIgnoreOrientationRequestAllowed()Z

    move-result v0

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    goto :goto_1

    :cond_1
    :goto_0
    const/4 v0, 0x1

    :goto_1
    return v0
.end method
""",
        "replacement": """\
.method isIgnoreOrientationRequestDisabled()Z
    .registers 2

    goto :goto_b

    nop

    :goto_0
    invoke-virtual {v0}, Lcom/android/server/wm/AppCompatConfiguration;->isIgnoreOrientationRequestAllowed()Z

    move-result v0

    goto :goto_1

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_a

    :cond_0
    goto :goto_9

    nop

    :goto_2
    if-eqz v0, :cond_1

    goto :goto_8

    :cond_1
    goto :goto_c

    nop

    :goto_3
    return v0

    :goto_4
    const/4 v0, 0x0

    goto :goto_7

    nop

    :goto_5
    const/4 v0, 0x1

    :goto_6
    goto :goto_3

    nop

    :goto_7
    goto :goto_6

    :goto_8
    goto :goto_5

    nop

    :goto_9
    goto :goto_8

    :goto_a
    goto :goto_4

    nop

    :goto_b
    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mIsIgnoreOrientationRequestDisabled:Z

    goto :goto_2

    nop

    :goto_c
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mAppCompatConfiguration:Lcom/android/server/wm/AppCompatConfiguration;

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mIsIgnoreOrientationRequestDisabled:Z', 'if-nez v0, :cond_1', 'iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mAppCompatConfiguration:Lcom/android/server/wm/AppCompatConfiguration;', 'invoke-virtual {v0}, Lcom/android/server/wm/AppCompatConfiguration;->isIgnoreOrientationRequestAllowed()Z', 'move-result v0', 'if-nez v0, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_isUserVisible_I_Z",
        "method":      ".method isUserVisible(I)Z",
        "method_name": 'isUserVisible',
        "type":        "method_replace",
        "search": """\
.method isUserVisible(I)Z
    .registers 3

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;

    invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->isUserVisible(I)Z

    move-result v0

    return v0
.end method
""",
        "replacement": """\
.method isUserVisible(I)Z
    .registers 3

    goto :goto_2

    nop

    :goto_0
    return v0

    :goto_1
    invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->isUserVisible(I)Z

    move-result v0

    goto :goto_0

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;', 'invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->isUserVisible(I)Z', 'move-result v0', 'return v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_isValidExpandedPictureInPictureAspectRatio_Lcom_android_serv",
        "method":      ".method isValidExpandedPictureInPictureAspectRatio(Lcom/android/server/wm/DisplayContent;F)Z",
        "method_name": 'isValidExpandedPictureInPictureAspectRatio',
        "type":        "method_replace",
        "search": """\
.method isValidExpandedPictureInPictureAspectRatio(Lcom/android/server/wm/DisplayContent;F)Z
    .registers 4

    invoke-virtual {p1}, Lcom/android/server/wm/DisplayContent;->getPinnedTaskController()Lcom/android/server/wm/PinnedTaskController;

    move-result-object v0

    invoke-virtual {v0, p2}, Lcom/android/server/wm/PinnedTaskController;->isValidExpandedPictureInPictureAspectRatio(F)Z

    move-result v0

    return v0
.end method
""",
        "replacement": """\
.method isValidExpandedPictureInPictureAspectRatio(Lcom/android/server/wm/DisplayContent;F)Z
    .registers 4

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v0, p2}, Lcom/android/server/wm/PinnedTaskController;->isValidExpandedPictureInPictureAspectRatio(F)Z

    move-result v0

    goto :goto_2

    nop

    :goto_1
    invoke-virtual {p1}, Lcom/android/server/wm/DisplayContent;->getPinnedTaskController()Lcom/android/server/wm/PinnedTaskController;

    move-result-object v0

    goto :goto_0

    nop

    :goto_2
    return v0
.end method
""",
        "method_anchors": ['invoke-virtual {p1}, Lcom/android/server/wm/DisplayContent;->getPinnedTaskController()Lcom/android/server/wm/PinnedTaskController;', 'move-result-object v0', 'invoke-virtual {v0, p2}, Lcom/android/server/wm/PinnedTaskController;->isValidExpandedPictureInPictureAspectRatio(F)Z', 'move-result v0', 'return v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_isValidPictureInPictureAspectRatio_Lcom_android_server_wm_Di",
        "method":      ".method isValidPictureInPictureAspectRatio(Lcom/android/server/wm/DisplayContent;F)Z",
        "method_name": 'isValidPictureInPictureAspectRatio',
        "type":        "method_replace",
        "search": """\
.method isValidPictureInPictureAspectRatio(Lcom/android/server/wm/DisplayContent;F)Z
    .registers 4

    invoke-virtual {p1}, Lcom/android/server/wm/DisplayContent;->getPinnedTaskController()Lcom/android/server/wm/PinnedTaskController;

    move-result-object v0

    invoke-virtual {v0, p2}, Lcom/android/server/wm/PinnedTaskController;->isValidPictureInPictureAspectRatio(F)Z

    move-result v0

    return v0
.end method
""",
        "replacement": """\
.method isValidPictureInPictureAspectRatio(Lcom/android/server/wm/DisplayContent;F)Z
    .registers 4

    goto :goto_2

    nop

    :goto_0
    return v0

    :goto_1
    invoke-virtual {v0, p2}, Lcom/android/server/wm/PinnedTaskController;->isValidPictureInPictureAspectRatio(F)Z

    move-result v0

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p1}, Lcom/android/server/wm/DisplayContent;->getPinnedTaskController()Lcom/android/server/wm/PinnedTaskController;

    move-result-object v0

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p1}, Lcom/android/server/wm/DisplayContent;->getPinnedTaskController()Lcom/android/server/wm/PinnedTaskController;', 'move-result-object v0', 'invoke-virtual {v0, p2}, Lcom/android/server/wm/PinnedTaskController;->isValidPictureInPictureAspectRatio(F)Z', 'move-result v0', 'return v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_makeSurfaceBuilder__Landroid_view_SurfaceControl_Builder_",
        "method":      ".method makeSurfaceBuilder()Landroid/view/SurfaceControl$Builder;",
        "method_name": 'makeSurfaceBuilder',
        "type":        "method_replace",
        "search": """\
.method makeSurfaceBuilder()Landroid/view/SurfaceControl$Builder;
    .registers 2

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mSurfaceControlFactory:Ljava/util/function/Supplier;

    invoke-interface {v0}, Ljava/util/function/Supplier;->get()Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Landroid/view/SurfaceControl$Builder;

    return-object v0
.end method
""",
        "replacement": """\
.method makeSurfaceBuilder()Landroid/view/SurfaceControl$Builder;
    .registers 2

    goto :goto_2

    nop

    :goto_0
    check-cast v0, Landroid/view/SurfaceControl$Builder;

    goto :goto_1

    nop

    :goto_1
    return-object v0

    :goto_2
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mSurfaceControlFactory:Ljava/util/function/Supplier;

    goto :goto_3

    nop

    :goto_3
    invoke-interface {v0}, Ljava/util/function/Supplier;->get()Ljava/lang/Object;

    move-result-object v0

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mSurfaceControlFactory:Ljava/util/function/Supplier;', 'invoke-interface {v0}, Ljava/util/function/Supplier;->get()Ljava/lang/Object;', 'move-result-object v0', 'check-cast v0, Landroid/view/SurfaceControl$Builder;', 'return-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_mapOrientationRequest_I_I",
        "method":      ".method mapOrientationRequest(I)I",
        "method_name": 'mapOrientationRequest',
        "type":        "method_replace",
        "search": """\
.method mapOrientationRequest(I)I
    .registers 3

    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mIsIgnoreOrientationRequestDisabled:Z

    if-nez v0, :cond_0

    return p1

    :cond_0
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mOrientationMapping:Landroid/util/SparseIntArray;

    invoke-virtual {v0, p1, p1}, Landroid/util/SparseIntArray;->get(II)I

    move-result v0

    return v0
.end method
""",
        "replacement": """\
.method mapOrientationRequest(I)I
    .registers 3

    goto :goto_0

    nop

    :goto_0
    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mIsIgnoreOrientationRequestDisabled:Z

    goto :goto_1

    nop

    :goto_1
    if-eqz v0, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_4

    nop

    :goto_2
    invoke-virtual {v0, p1, p1}, Landroid/util/SparseIntArray;->get(II)I

    move-result v0

    goto :goto_3

    nop

    :goto_3
    return v0

    :goto_4
    return p1

    :goto_5
    goto :goto_6

    nop

    :goto_6
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mOrientationMapping:Landroid/util/SparseIntArray;

    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mIsIgnoreOrientationRequestDisabled:Z', 'if-nez v0, :cond_0', 'return p1', 'iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mOrientationMapping:Landroid/util/SparseIntArray;', 'invoke-virtual {v0, p1, p1}, Landroid/util/SparseIntArray;->get(II)I', 'move-result v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_moveDisplayToTopInternal_I_V",
        "method":      ".method moveDisplayToTopInternal(I)V",
        "method_name": 'moveDisplayToTopInternal',
        "type":        "method_replace",
        "search": """\
.method moveDisplayToTopInternal(I)V
    .registers 13

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    if-eqz v1, :cond_4

    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v2}, Lcom/android/server/wm/RootWindowContainer;->getTopChild()Lcom/android/server/wm/WindowContainer;

    move-result-object v2

    if-eq v2, v1, :cond_4

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->canStealTopFocus()Z

    move-result v2

    if-nez v2, :cond_1

    sget-object v2, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_FOCUS_LIGHT_enabled:[Z

    const/4 v3, 0x2

    aget-boolean v2, v2, v3

    if-eqz v2, :cond_0

    int-to-long v2, p1

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v4}, Lcom/android/server/wm/RootWindowContainer;->getTopFocusedDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v4

    invoke-virtual {v4}, Lcom/android/server/wm/DisplayContent;->getDisplayId()I

    move-result v4

    int-to-long v4, v4

    sget-object v6, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_FOCUS_LIGHT:Lcom/android/internal/protolog/WmProtoLogGroups;

    invoke-static {v2, v3}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v7

    invoke-static {v4, v5}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v8

    filled-new-array {v7, v8}, [Ljava/lang/Object;

    move-result-object v7

    const-wide v8, -0xc4dc6b81252c8cbL

    const/4 v10, 0x5

    invoke-static {v6, v8, v9, v10, v7}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->i(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_1
    const/4 v2, 0x0

    const/4 v3, 0x0

    :try_start_1
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/com/android/window/flags/Flags;->enableDisplayFocusInShellTransitions()Z

    move-result v4

    if-eqz v4, :cond_3

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;

    invoke-virtual {v4}, Lcom/android/server/wm/ActivityTaskManagerService;->getTransitionController()Lcom/android/server/wm/TransitionController;

    move-result-object v4

    const/4 v5, 0x0

    const/4 v6, 0x0

    const/4 v7, 0x3

    invoke-virtual {v4, v7, v5, v6, v1}, Lcom/android/server/wm/TransitionController;->requestTransitionIfNeeded(IILcom/android/server/wm/WindowContainer;Lcom/android/server/wm/WindowContainer;)Lcom/android/server/wm/Transition;

    move-result-object v4

    if-eqz v4, :cond_2

    const/4 v3, 0x1

    move-object v2, v4

    goto :goto_0

    :cond_2
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;

    invoke-virtual {v2}, Lcom/android/server/wm/ActivityTaskManagerService;->getTransitionController()Lcom/android/server/wm/TransitionController;

    move-result-object v2

    invoke-virtual {v2}, Lcom/android/server/wm/TransitionController;->getCollectingTransition()Lcom/android/server/wm/Transition;

    move-result-object v2

    :goto_0
    if-eqz v2, :cond_3

    invoke-virtual {v2, v1}, Lcom/android/server/wm/Transition;->recordTaskOrder(Lcom/android/server/wm/WindowContainer;)V

    :cond_3
    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getParent()Lcom/android/server/wm/WindowContainer;

    move-result-object v4

    const v5, 0x7fffffff

    const/4 v6, 0x1

    invoke-virtual {v4, v5, v1, v6}, Lcom/android/server/wm/WindowContainer;->positionChildAt(ILcom/android/server/wm/WindowContainer;Z)V

    if-eqz v3, :cond_4

    invoke-virtual {v2, v1, v6}, Lcom/android/server/wm/Transition;->setReady(Lcom/android/server/wm/WindowContainer;Z)V

    :cond_4
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method moveDisplayToTopInternal(I)V
    .registers 13

    goto :goto_2

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_6

    nop

    :goto_1
    const/4 v2, 0x0

    goto :goto_8

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_4

    nop

    :goto_3
    return-void

    :cond_0
    goto :goto_1

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_5

    nop

    :goto_5
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    if-eqz v1, :cond_4

    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v2}, Lcom/android/server/wm/RootWindowContainer;->getTopChild()Lcom/android/server/wm/WindowContainer;

    move-result-object v2

    if-eq v2, v1, :cond_4

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->canStealTopFocus()Z

    move-result v2

    if-nez v2, :cond_0

    sget-object v2, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_FOCUS_LIGHT_enabled:[Z

    const/4 v3, 0x2

    aget-boolean v2, v2, v3

    if-eqz v2, :cond_1

    int-to-long v2, p1

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v4}, Lcom/android/server/wm/RootWindowContainer;->getTopFocusedDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v4

    invoke-virtual {v4}, Lcom/android/server/wm/DisplayContent;->getDisplayId()I

    move-result v4

    int-to-long v4, v4

    sget-object v6, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_FOCUS_LIGHT:Lcom/android/internal/protolog/WmProtoLogGroups;

    invoke-static {v2, v3}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v7

    invoke-static {v4, v5}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v8

    filled-new-array {v7, v8}, [Ljava/lang/Object;

    move-result-object v7

    const-wide v8, -0xc4dc6b81252c8cbL

    const/4 v10, 0x5

    invoke-static {v6, v8, v9, v10, v7}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->i(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_1
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_7

    nop

    :goto_6
    throw v1

    :goto_7
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_3

    nop

    :goto_8
    const/4 v3, 0x0

    :try_start_1
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/com/android/window/flags/Flags;->enableDisplayFocusInShellTransitions()Z

    move-result v4

    if-eqz v4, :cond_3

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;

    invoke-virtual {v4}, Lcom/android/server/wm/ActivityTaskManagerService;->getTransitionController()Lcom/android/server/wm/TransitionController;

    move-result-object v4

    const/4 v5, 0x0

    const/4 v6, 0x0

    const/4 v7, 0x3

    invoke-virtual {v4, v7, v5, v6, v1}, Lcom/android/server/wm/TransitionController;->requestTransitionIfNeeded(IILcom/android/server/wm/WindowContainer;Lcom/android/server/wm/WindowContainer;)Lcom/android/server/wm/Transition;

    move-result-object v4

    if-eqz v4, :cond_2

    const/4 v3, 0x1

    move-object v2, v4

    goto :goto_9

    :cond_2
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;

    invoke-virtual {v2}, Lcom/android/server/wm/ActivityTaskManagerService;->getTransitionController()Lcom/android/server/wm/TransitionController;

    move-result-object v2

    invoke-virtual {v2}, Lcom/android/server/wm/TransitionController;->getCollectingTransition()Lcom/android/server/wm/Transition;

    move-result-object v2

    :goto_9
    if-eqz v2, :cond_3

    invoke-virtual {v2, v1}, Lcom/android/server/wm/Transition;->recordTaskOrder(Lcom/android/server/wm/WindowContainer;)V

    :cond_3
    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getParent()Lcom/android/server/wm/WindowContainer;

    move-result-object v4

    const v5, 0x7fffffff

    const/4 v6, 0x1

    invoke-virtual {v4, v5, v1, v6}, Lcom/android/server/wm/WindowContainer;->positionChildAt(ILcom/android/server/wm/WindowContainer;Z)V

    if-eqz v3, :cond_4

    invoke-virtual {v2, v1, v6}, Lcom/android/server/wm/Transition;->setReady(Lcom/android/server/wm/WindowContainer;Z)V

    :cond_4
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_b

    nop

    :goto_a
    return-void

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_0

    nop

    :goto_b
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_a

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;', 'invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;', 'move-result-object v1', 'if-eqz v1, :cond_4'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_moveFocusToActivity_Lcom_android_server_wm_ActivityRecord__V",
        "method":      ".method moveFocusToActivity(Lcom/android/server/wm/ActivityRecord;)V",
        "method_name": 'moveFocusToActivity',
        "type":        "method_replace",
        "search": """\
.method moveFocusToActivity(Lcom/android/server/wm/ActivityRecord;)V
    .registers 3

    invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getDisplayId()I

    move-result v0

    invoke-virtual {p0, v0}, Lcom/android/server/wm/WindowManagerService;->moveDisplayToTopInternal(I)V

    invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;

    move-result-object v0

    invoke-virtual {p0, v0, p1}, Lcom/android/server/wm/WindowManagerService;->handleTaskFocusChange(Lcom/android/server/wm/Task;Lcom/android/server/wm/ActivityRecord;)V

    return-void
.end method
""",
        "replacement": """\
.method moveFocusToActivity(Lcom/android/server/wm/ActivityRecord;)V
    .registers 3

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {p0, v0}, Lcom/android/server/wm/WindowManagerService;->moveDisplayToTopInternal(I)V

    goto :goto_2

    nop

    :goto_1
    invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getDisplayId()I

    move-result v0

    goto :goto_0

    nop

    :goto_2
    invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;

    move-result-object v0

    goto :goto_3

    nop

    :goto_3
    invoke-virtual {p0, v0, p1}, Lcom/android/server/wm/WindowManagerService;->handleTaskFocusChange(Lcom/android/server/wm/Task;Lcom/android/server/wm/ActivityRecord;)V

    goto :goto_4

    nop

    :goto_4
    return-void
.end method
""",
        "method_anchors": ['invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getDisplayId()I', 'move-result v0', 'invoke-virtual {p0, v0}, Lcom/android/server/wm/WindowManagerService;->moveDisplayToTopInternal(I)V', 'invoke-virtual {p1}, Lcom/android/server/wm/ActivityRecord;->getTask()Lcom/android/server/wm/Task;', 'move-result-object v0', 'invoke-virtual {p0, v0, p1}, Lcom/android/server/wm/WindowManagerService;->handleTaskFocusChange(Lcom/android/server/wm/Task;Lcom/android/server/wm/ActivityRecord;)V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_moveFocusToAdjacentEmbeddedWindow_Lcom_android_server_wm_Win",
        "method":      ".method moveFocusToAdjacentEmbeddedWindow(Lcom/android/server/wm/WindowState;)Z",
        "method_name": 'moveFocusToAdjacentEmbeddedWindow',
        "type":        "method_replace",
        "search": """\
.method moveFocusToAdjacentEmbeddedWindow(Lcom/android/server/wm/WindowState;)Z
    .registers 5

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getActivityRecord()Lcom/android/server/wm/ActivityRecord;

    move-result-object v0

    if-eqz v0, :cond_2

    invoke-virtual {v0}, Lcom/android/server/wm/ActivityRecord;->isVisible()Z

    move-result v1

    if-nez v1, :cond_0

    goto :goto_0

    :cond_0
    invoke-virtual {p0, v0}, Lcom/android/server/wm/WindowManagerService;->getMostRecentActivityInAdjacent(Lcom/android/server/wm/ActivityRecord;)Lcom/android/server/wm/ActivityRecord;

    move-result-object v1

    invoke-virtual {v0}, Lcom/android/server/wm/ActivityRecord;->getTaskFragment()Lcom/android/server/wm/TaskFragment;

    move-result-object v2

    if-eqz v2, :cond_1

    invoke-virtual {v0}, Lcom/android/server/wm/ActivityRecord;->getTaskFragment()Lcom/android/server/wm/TaskFragment;

    move-result-object v2

    iget-object v2, v2, Lcom/android/server/wm/TaskFragment;->mStub:Lcom/android/server/wm/TaskFragmentStub;

    invoke-interface {v2}, Lcom/android/server/wm/TaskFragmentStub;->isSpecialVideo()Z

    move-result v2

    if-eqz v2, :cond_1

    if-ne v0, v1, :cond_1

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->isFocused()Z

    move-result v2

    xor-int/lit8 v2, v2, 0x1

    return v2

    :cond_1
    invoke-virtual {p0, v1}, Lcom/android/server/wm/WindowManagerService;->moveFocusToActivity(Lcom/android/server/wm/ActivityRecord;)V

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->isFocused()Z

    move-result v2

    xor-int/lit8 v2, v2, 0x1

    return v2

    :cond_2
    :goto_0
    const/4 v1, 0x0

    return v1
.end method
""",
        "replacement": """\
.method moveFocusToAdjacentEmbeddedWindow(Lcom/android/server/wm/WindowState;)Z
    .registers 5

    goto :goto_8

    nop

    :goto_0
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->isFocused()Z

    move-result v2

    goto :goto_14

    nop

    :goto_1
    invoke-virtual {v0}, Lcom/android/server/wm/ActivityRecord;->getTaskFragment()Lcom/android/server/wm/TaskFragment;

    move-result-object v2

    goto :goto_11

    nop

    :goto_2
    if-nez v0, :cond_0

    goto :goto_13

    :cond_0
    goto :goto_6

    nop

    :goto_3
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->isFocused()Z

    move-result v2

    goto :goto_5

    nop

    :goto_4
    if-nez v2, :cond_1

    goto :goto_10

    :cond_1
    goto :goto_18

    nop

    :goto_5
    xor-int/lit8 v2, v2, 0x1

    goto :goto_12

    nop

    :goto_6
    invoke-virtual {v0}, Lcom/android/server/wm/ActivityRecord;->isVisible()Z

    move-result v1

    goto :goto_c

    nop

    :goto_7
    iget-object v2, v2, Lcom/android/server/wm/TaskFragment;->mStub:Lcom/android/server/wm/TaskFragmentStub;

    goto :goto_d

    nop

    :goto_8
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getActivityRecord()Lcom/android/server/wm/ActivityRecord;

    move-result-object v0

    goto :goto_2

    nop

    :goto_9
    invoke-virtual {p0, v0}, Lcom/android/server/wm/WindowManagerService;->getMostRecentActivityInAdjacent(Lcom/android/server/wm/ActivityRecord;)Lcom/android/server/wm/ActivityRecord;

    move-result-object v1

    goto :goto_1

    nop

    :goto_a
    goto :goto_13

    :goto_b
    goto :goto_9

    nop

    :goto_c
    if-eqz v1, :cond_2

    goto :goto_b

    :cond_2
    goto :goto_a

    nop

    :goto_d
    invoke-interface {v2}, Lcom/android/server/wm/TaskFragmentStub;->isSpecialVideo()Z

    move-result v2

    goto :goto_4

    nop

    :goto_e
    invoke-virtual {v0}, Lcom/android/server/wm/ActivityRecord;->getTaskFragment()Lcom/android/server/wm/TaskFragment;

    move-result-object v2

    goto :goto_7

    nop

    :goto_f
    return v2

    :goto_10
    goto :goto_17

    nop

    :goto_11
    if-nez v2, :cond_3

    goto :goto_10

    :cond_3
    goto :goto_e

    nop

    :goto_12
    return v2

    :goto_13
    goto :goto_15

    nop

    :goto_14
    xor-int/lit8 v2, v2, 0x1

    goto :goto_f

    nop

    :goto_15
    const/4 v1, 0x0

    goto :goto_16

    nop

    :goto_16
    return v1

    :goto_17
    invoke-virtual {p0, v1}, Lcom/android/server/wm/WindowManagerService;->moveFocusToActivity(Lcom/android/server/wm/ActivityRecord;)V

    goto :goto_3

    nop

    :goto_18
    if-eq v0, v1, :cond_4

    goto :goto_10

    :cond_4
    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getActivityRecord()Lcom/android/server/wm/ActivityRecord;', 'move-result-object v0', 'if-eqz v0, :cond_2', 'invoke-virtual {v0}, Lcom/android/server/wm/ActivityRecord;->isVisible()Z', 'move-result v1', 'if-nez v1, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_moveFocusToAdjacentWindow_Lcom_android_server_wm_WindowState",
        "method":      ".method moveFocusToAdjacentWindow(Lcom/android/server/wm/WindowState;I)Z",
        "method_name": 'moveFocusToAdjacentWindow',
        "type":        "method_replace",
        "search": """\
.method moveFocusToAdjacentWindow(Lcom/android/server/wm/WindowState;I)Z
    .registers 12

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->isFocused()Z

    move-result v0

    const/4 v1, 0x0

    if-nez v0, :cond_0

    return v1

    :cond_0
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getTaskFragment()Lcom/android/server/wm/TaskFragment;

    move-result-object v0

    if-eqz v0, :cond_7

    invoke-virtual {v0}, Lcom/android/server/wm/TaskFragment;->asTask()Lcom/android/server/wm/Task;

    move-result-object v2

    if-eqz v2, :cond_1

    goto :goto_0

    :cond_1
    invoke-virtual {v0}, Lcom/android/server/wm/TaskFragment;->hasAdjacentTaskFragment()Z

    move-result v2

    if-nez v2, :cond_2

    return v1

    :cond_2
    invoke-virtual {v0}, Lcom/android/server/wm/TaskFragment;->getAdjacentTaskFragments()Lcom/android/server/wm/TaskFragment$AdjacentSet;

    move-result-object v2

    invoke-virtual {v2}, Lcom/android/server/wm/TaskFragment$AdjacentSet;->size()I

    move-result v2

    const/4 v3, 0x2

    if-gt v2, v3, :cond_6

    const/4 v2, 0x1

    new-array v3, v2, [Lcom/android/server/wm/TaskFragment;

    new-instance v4, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda13;

    invoke-direct {v4, v3}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda13;-><init>([Lcom/android/server/wm/TaskFragment;)V

    invoke-virtual {v0, v4}, Lcom/android/server/wm/TaskFragment;->forOtherAdjacentTaskFragments(Ljava/util/function/Predicate;)Z

    aget-object v4, v3, v1

    invoke-virtual {v4}, Lcom/android/server/wm/TaskFragment;->isIsolatedNav()Z

    move-result v5

    if-eqz v5, :cond_3

    return v1

    :cond_3
    invoke-virtual {v0}, Lcom/android/server/wm/TaskFragment;->getBounds()Landroid/graphics/Rect;

    move-result-object v5

    invoke-virtual {v4}, Lcom/android/server/wm/TaskFragment;->getBounds()Landroid/graphics/Rect;

    move-result-object v6

    sparse-switch p2, :sswitch_data_0

    return v1

    :sswitch_0
    iget v7, v6, Landroid/graphics/Rect;->bottom:I

    iget v8, v5, Landroid/graphics/Rect;->bottom:I

    if-gt v7, v8, :cond_4

    return v1

    :sswitch_1
    iget v7, v6, Landroid/graphics/Rect;->right:I

    iget v8, v5, Landroid/graphics/Rect;->right:I

    if-gt v7, v8, :cond_4

    return v1

    :sswitch_2
    iget v7, v6, Landroid/graphics/Rect;->top:I

    iget v8, v5, Landroid/graphics/Rect;->top:I

    if-lt v7, v8, :cond_4

    return v1

    :sswitch_3
    iget v7, v6, Landroid/graphics/Rect;->left:I

    iget v8, v5, Landroid/graphics/Rect;->left:I

    if-lt v7, v8, :cond_4

    return v1

    :sswitch_4
    nop

    :cond_4
    invoke-virtual {v4, v2}, Lcom/android/server/wm/TaskFragment;->topRunningActivity(Z)Lcom/android/server/wm/ActivityRecord;

    move-result-object v7

    if-nez v7, :cond_5

    return v1

    :cond_5
    invoke-virtual {p0, v7}, Lcom/android/server/wm/WindowManagerService;->moveFocusToActivity(Lcom/android/server/wm/ActivityRecord;)V

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->isFocused()Z

    move-result v1

    xor-int/2addr v1, v2

    return v1

    :cond_6
    new-instance v1, Ljava/lang/IllegalStateException;

    const-string v2, "Not yet support 3+ adjacent for non-Task TFs"

    invoke-direct {v1, v2}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw v1

    :cond_7
    :goto_0
    return v1

    nop

    :sswitch_data_0
    .sparse-switch
        0x1 -> :sswitch_4
        0x2 -> :sswitch_4
        0x11 -> :sswitch_3
        0x21 -> :sswitch_2
        0x42 -> :sswitch_1
        0x82 -> :sswitch_0
    .end sparse-switch
.end method
""",
        "replacement": """\
.method moveFocusToAdjacentWindow(Lcom/android/server/wm/WindowState;I)Z
    .registers 12

    goto :goto_8

    nop

    :goto_0
    invoke-direct {v1, v2}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    goto :goto_25

    nop

    :goto_1
    invoke-direct {v4, v3}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda13;-><init>([Lcom/android/server/wm/TaskFragment;)V

    goto :goto_13

    nop

    :goto_2
    return v1

    :goto_3
    goto :goto_18

    nop

    :goto_4
    return v1

    :sswitch_0
    nop

    :goto_5
    goto :goto_34

    nop

    :goto_6
    iget v8, v5, Landroid/graphics/Rect;->left:I

    goto :goto_35

    nop

    :goto_7
    const/4 v3, 0x2

    goto :goto_c

    nop

    :goto_8
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->isFocused()Z

    move-result v0

    goto :goto_a

    nop

    :goto_9
    return v1

    nop

    :sswitch_data_0
    .sparse-switch
        0x1 -> :sswitch_0
        0x2 -> :sswitch_0
        0x11 -> :sswitch_2
        0x21 -> :sswitch_1
        0x42 -> :sswitch_4
        0x82 -> :sswitch_3
    .end sparse-switch

    :goto_a
    const/4 v1, 0x0

    goto :goto_33

    nop

    :goto_b
    invoke-virtual {v0}, Lcom/android/server/wm/TaskFragment;->hasAdjacentTaskFragment()Z

    move-result v2

    goto :goto_d

    nop

    :goto_c
    if-le v2, v3, :cond_0

    goto :goto_f

    :cond_0
    goto :goto_1e

    nop

    :goto_d
    if-eqz v2, :cond_1

    goto :goto_3

    :cond_1
    goto :goto_2

    nop

    :goto_e
    return v1

    :goto_f
    goto :goto_32

    nop

    :goto_10
    if-le v7, v8, :cond_2

    goto :goto_5

    :cond_2
    goto :goto_11

    nop

    :goto_11
    return v1

    :sswitch_1
    goto :goto_22

    nop

    :goto_12
    invoke-virtual {p0, v7}, Lcom/android/server/wm/WindowManagerService;->moveFocusToActivity(Lcom/android/server/wm/ActivityRecord;)V

    goto :goto_27

    nop

    :goto_13
    invoke-virtual {v0, v4}, Lcom/android/server/wm/TaskFragment;->forOtherAdjacentTaskFragments(Ljava/util/function/Predicate;)Z

    goto :goto_23

    nop

    :goto_14
    iget v8, v5, Landroid/graphics/Rect;->top:I

    goto :goto_36

    nop

    :goto_15
    const-string v2, "Not yet support 3+ adjacent for non-Task TFs"

    goto :goto_0

    nop

    :goto_16
    iget v7, v6, Landroid/graphics/Rect;->bottom:I

    goto :goto_2d

    nop

    :goto_17
    xor-int/2addr v1, v2

    goto :goto_e

    nop

    :goto_18
    invoke-virtual {v0}, Lcom/android/server/wm/TaskFragment;->getAdjacentTaskFragments()Lcom/android/server/wm/TaskFragment$AdjacentSet;

    move-result-object v2

    goto :goto_24

    nop

    :goto_19
    iget v7, v6, Landroid/graphics/Rect;->right:I

    goto :goto_3c

    nop

    :goto_1a
    iget v7, v6, Landroid/graphics/Rect;->left:I

    goto :goto_6

    nop

    :goto_1b
    goto :goto_26

    :goto_1c
    goto :goto_b

    nop

    :goto_1d
    invoke-virtual {v0}, Lcom/android/server/wm/TaskFragment;->asTask()Lcom/android/server/wm/Task;

    move-result-object v2

    goto :goto_37

    nop

    :goto_1e
    const/4 v2, 0x1

    goto :goto_3a

    nop

    :goto_1f
    return v1

    :goto_20
    goto :goto_3d

    nop

    :goto_21
    return v1

    :sswitch_2
    goto :goto_1a

    nop

    :goto_22
    iget v7, v6, Landroid/graphics/Rect;->top:I

    goto :goto_14

    nop

    :goto_23
    aget-object v4, v3, v1

    goto :goto_3e

    nop

    :goto_24
    invoke-virtual {v2}, Lcom/android/server/wm/TaskFragment$AdjacentSet;->size()I

    move-result v2

    goto :goto_7

    nop

    :goto_25
    throw v1

    :goto_26
    goto :goto_9

    nop

    :goto_27
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->isFocused()Z

    move-result v1

    goto :goto_17

    nop

    :goto_28
    new-instance v4, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda13;

    goto :goto_1

    nop

    :goto_29
    if-le v7, v8, :cond_3

    goto :goto_5

    :cond_3
    goto :goto_39

    nop

    :goto_2a
    return v1

    :goto_2b
    goto :goto_12

    nop

    :goto_2c
    return v1

    :sswitch_3
    goto :goto_16

    nop

    :goto_2d
    iget v8, v5, Landroid/graphics/Rect;->bottom:I

    goto :goto_29

    nop

    :goto_2e
    if-eqz v7, :cond_4

    goto :goto_2b

    :cond_4
    goto :goto_2a

    nop

    :goto_2f
    return v1

    :goto_30
    goto :goto_31

    nop

    :goto_31
    invoke-virtual {v0}, Lcom/android/server/wm/TaskFragment;->getBounds()Landroid/graphics/Rect;

    move-result-object v5

    goto :goto_3b

    nop

    :goto_32
    new-instance v1, Ljava/lang/IllegalStateException;

    goto :goto_15

    nop

    :goto_33
    if-eqz v0, :cond_5

    goto :goto_20

    :cond_5
    goto :goto_1f

    nop

    :goto_34
    invoke-virtual {v4, v2}, Lcom/android/server/wm/TaskFragment;->topRunningActivity(Z)Lcom/android/server/wm/ActivityRecord;

    move-result-object v7

    goto :goto_2e

    nop

    :goto_35
    if-ge v7, v8, :cond_6

    goto :goto_5

    :cond_6
    goto :goto_4

    nop

    :goto_36
    if-ge v7, v8, :cond_7

    goto :goto_5

    :cond_7
    goto :goto_21

    nop

    :goto_37
    if-nez v2, :cond_8

    goto :goto_1c

    :cond_8
    goto :goto_1b

    nop

    :goto_38
    if-nez v0, :cond_9

    goto :goto_26

    :cond_9
    goto :goto_1d

    nop

    :goto_39
    return v1

    :sswitch_4
    goto :goto_19

    nop

    :goto_3a
    new-array v3, v2, [Lcom/android/server/wm/TaskFragment;

    goto :goto_28

    nop

    :goto_3b
    invoke-virtual {v4}, Lcom/android/server/wm/TaskFragment;->getBounds()Landroid/graphics/Rect;

    move-result-object v6

    sparse-switch p2, :sswitch_data_0

    goto :goto_2c

    nop

    :goto_3c
    iget v8, v5, Landroid/graphics/Rect;->right:I

    goto :goto_10

    nop

    :goto_3d
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getTaskFragment()Lcom/android/server/wm/TaskFragment;

    move-result-object v0

    goto :goto_38

    nop

    :goto_3e
    invoke-virtual {v4}, Lcom/android/server/wm/TaskFragment;->isIsolatedNav()Z

    move-result v5

    goto :goto_3f

    nop

    :goto_3f
    if-nez v5, :cond_a

    goto :goto_30

    :cond_a
    goto :goto_2f

    nop
.end method
""",
        "method_anchors": ['invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->isFocused()Z', 'move-result v0', 'if-nez v0, :cond_0', 'return v1', 'invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getTaskFragment()Lcom/android/server/wm/TaskFragment;', 'move-result-object v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_notifyHardKeyboardStatusChange__V",
        "method":      ".method notifyHardKeyboardStatusChange()V",
        "method_name": 'notifyHardKeyboardStatusChange',
        "type":        "method_replace",
        "search": """\
.method notifyHardKeyboardStatusChange()V
    .registers 4

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mHardKeyboardStatusChangeListener:Lcom/android/server/wm/WindowManagerInternal$OnHardKeyboardStatusChangeListener;

    iget-boolean v2, p0, Lcom/android/server/wm/WindowManagerService;->mHardKeyboardAvailable:Z

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    if-eqz v1, :cond_0

    invoke-interface {v1, v2}, Lcom/android/server/wm/WindowManagerInternal$OnHardKeyboardStatusChangeListener;->onHardKeyboardStatusChange(Z)V

    :cond_0
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method notifyHardKeyboardStatusChange()V
    .registers 4

    goto :goto_6

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_2

    nop

    :goto_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_3

    nop

    :goto_2
    throw v1

    :goto_3
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mHardKeyboardStatusChangeListener:Lcom/android/server/wm/WindowManagerInternal$OnHardKeyboardStatusChangeListener;

    iget-boolean v2, p0, Lcom/android/server/wm/WindowManagerService;->mHardKeyboardAvailable:Z

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_4

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_5

    nop

    :goto_5
    if-nez v1, :cond_0

    goto :goto_8

    :cond_0
    goto :goto_7

    nop

    :goto_6
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_1

    nop

    :goto_7
    invoke-interface {v1, v2}, Lcom/android/server/wm/WindowManagerInternal$OnHardKeyboardStatusChangeListener;->onHardKeyboardStatusChange(Z)V

    :goto_8
    goto :goto_9

    nop

    :goto_9
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mHardKeyboardStatusChangeListener:Lcom/android/server/wm/WindowManagerInternal$OnHardKeyboardStatusChangeListener;', 'iget-boolean v2, p0, Lcom/android/server/wm/WindowManagerService;->mHardKeyboardAvailable:Z', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V', 'if-eqz v1, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_notifyScreenshotListeners_I_Ljava_util_List_",
        "method":      ".method public notifyScreenshotListeners(I)Ljava/util/List;",
        "method_name": 'notifyScreenshotListeners',
        "type":        "method_replace",
        "search": """\
.method public notifyScreenshotListeners(I)Ljava/util/List;
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(I)",
            "Ljava/util/List<",
            "Landroid/content/ComponentName;",
            ">;"
        }
    .end annotation

    const-string v0, "android.permission.STATUS_BAR_SERVICE"

    const-string v1, "notifyScreenshotListeners()"

    invoke-virtual {p0, v0, v1}, Lcom/android/server/wm/WindowManagerService;->checkCallingPermission(Ljava/lang/String;Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_1

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    if-nez v1, :cond_0

    new-instance v2, Ljava/util/ArrayList;

    invoke-direct {v2}, Ljava/util/ArrayList;-><init>()V

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-object v2

    :cond_0
    :try_start_1
    new-instance v2, Landroid/util/ArraySet;

    invoke-direct {v2}, Landroid/util/ArraySet;-><init>()V

    new-instance v3, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda37;

    invoke-direct {v3, v2}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda37;-><init>(Landroid/util/ArraySet;)V

    const/4 v4, 0x1

    invoke-virtual {v1, v3, v4}, Lcom/android/server/wm/DisplayContent;->forAllActivities(Ljava/util/function/Consumer;Z)V

    invoke-static {v2}, Ljava/util/List;->copyOf(Ljava/util/Collection;)Ljava/util/List;

    move-result-object v3

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-object v3

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1

    :cond_1
    new-instance v0, Ljava/lang/SecurityException;

    const-string v1, "Requires STATUS_BAR_SERVICE permission"

    invoke-direct {v0, v1}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    throw v0
.end method
""",
        "replacement": """\
.method public notifyScreenshotListeners(I)Ljava/util/List;
    .registers 7
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(I)",
            "Ljava/util/List<",
            "Landroid/content/ComponentName;",
            ">;"
        }
    .end annotation

    const/4 v1, 0x1

    const-string v0, "disable_mezo_screenshot_secure"

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-eqz v0, :cond_0

    invoke-static {}, Ljava/util/Collections;->emptyList()Ljava/util/List;

    move-result-object v0

    return-object v0

    :cond_0
    const-string v0, "android.permission.STATUS_BAR_SERVICE"

    const-string v1, "notifyScreenshotListeners()"

    invoke-virtual {p0, v0, v1}, Lcom/android/server/wm/WindowManagerService;->checkCallingPermission(Ljava/lang/String;Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_2

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    if-nez v1, :cond_1

    new-instance v2, Ljava/util/ArrayList;

    invoke-direct {v2}, Ljava/util/ArrayList;-><init>()V

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-object v2

    :cond_1
    :try_start_1
    new-instance v2, Landroid/util/ArraySet;

    invoke-direct {v2}, Landroid/util/ArraySet;-><init>()V

    new-instance v3, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda37;

    invoke-direct {v3, v2}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda37;-><init>(Landroid/util/ArraySet;)V

    const/4 v4, 0x1

    invoke-virtual {v1, v3, v4}, Lcom/android/server/wm/DisplayContent;->forAllActivities(Ljava/util/function/Consumer;Z)V

    invoke-static {v2}, Ljava/util/List;->copyOf(Ljava/util/Collection;)Ljava/util/List;

    move-result-object v3

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-object v3

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1

    :cond_2
    new-instance v0, Ljava/lang/SecurityException;

    const-string v1, "Requires STATUS_BAR_SERVICE permission"

    invoke-direct {v0, v1}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    throw v0
.end method
""",
        "method_anchors": ['const-string v0, "android.permission.STATUS_BAR_SERVICE"', 'const-string v1, "notifyScreenshotListeners()"', 'invoke-virtual {p0, v0, v1}, Lcom/android/server/wm/WindowManagerService;->checkCallingPermission(Ljava/lang/String;Ljava/lang/String;)Z', 'move-result v0', 'if-eqz v0, :cond_1', 'iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_onAnimationFinished__V",
        "method":      ".method onAnimationFinished()V",
        "method_name": 'onAnimationFinished',
        "type":        "method_replace",
        "search": """\
.method onAnimationFinished()V
    .registers 3

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-virtual {v1}, Ljava/lang/Object;->notifyAll()V

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method onAnimationFinished()V
    .registers 3

    goto :goto_4

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_6

    nop

    :goto_1
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-virtual {v1}, Ljava/lang/Object;->notifyAll()V

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_3

    nop

    :goto_2
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_0

    nop

    :goto_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_2

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_5

    nop

    :goto_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_1

    nop

    :goto_6
    throw v1
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-virtual {v1}, Ljava/lang/Object;->notifyAll()V', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_onProcessActivityVisibilityChanged_IZ_V",
        "method":      ".method onProcessActivityVisibilityChanged(IZ)V",
        "method_name": 'onProcessActivityVisibilityChanged',
        "type":        "method_replace",
        "search": """\
.method onProcessActivityVisibilityChanged(IZ)V
    .registers 4

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mScreenRecordingCallbackController:Lcom/android/server/wm/ScreenRecordingCallbackController;

    invoke-virtual {v0, p1, p2}, Lcom/android/server/wm/ScreenRecordingCallbackController;->onProcessActivityVisibilityChanged(IZ)V

    return-void
.end method
""",
        "replacement": """\
.method onProcessActivityVisibilityChanged(IZ)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    return-void

    :goto_1
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mScreenRecordingCallbackController:Lcom/android/server/wm/ScreenRecordingCallbackController;

    goto :goto_2

    nop

    :goto_2
    invoke-virtual {v0, p1, p2}, Lcom/android/server/wm/ScreenRecordingCallbackController;->onProcessActivityVisibilityChanged(IZ)V

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mScreenRecordingCallbackController:Lcom/android/server/wm/ScreenRecordingCallbackController;', 'invoke-virtual {v0, p1, p2}, Lcom/android/server/wm/ScreenRecordingCallbackController;->onProcessActivityVisibilityChanged(IZ)V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_postWindowRemoveCleanupLocked_Lcom_android_server_wm_WindowS",
        "method":      ".method postWindowRemoveCleanupLocked(Lcom/android/server/wm/WindowState;)V",
        "method_name": 'postWindowRemoveCleanupLocked',
        "type":        "method_replace",
        "search": """\
.method postWindowRemoveCleanupLocked(Lcom/android/server/wm/WindowState;)V
    .registers 16

    const-string v0, "com.android.server.wm.WindowManagerService.postWindowRemoveCleanupLocked(Lcom/android/server/wm/WindowState;)V"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_ADD_REMOVE_enabled:[Z

    const/4 v2, 0x0

    aget-boolean v1, v1, v2

    if-eqz v1, :cond_0

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    sget-object v3, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_ADD_REMOVE:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v4

    const-wide v5, 0x491202655c343519L

    invoke-static {v3, v5, v6, v2, v4}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_0
    iget-object v1, p1, Lcom/android/server/wm/WindowState;->mClient:Landroid/view/IWindow;

    invoke-interface {v1}, Landroid/view/IWindow;->asBinder()Landroid/os/IBinder;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    invoke-virtual {v3, v1}, Ljava/util/HashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    invoke-static {}, Landroid/view/flags/Flags;->sensitiveContentAppProtection()Z

    move-result v3

    if-eqz v3, :cond_1

    invoke-direct {p0, v1}, Lcom/android/server/wm/WindowManagerService;->notifyWindowRemovedListeners(Landroid/os/IBinder;)V

    :cond_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerServiceStub;->get()Lcom/android/server/wm/WindowManagerServiceStub;

    move-result-object v3

    invoke-interface {v3, p1}, Lcom/android/server/wm/WindowManagerServiceStub;->notifyWindowRemoved(Lcom/android/server/wm/WindowState;)V

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v3

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->resetAppOpsState()V

    iget-object v4, v3, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    const-string v5, "WindowManager"

    if-nez v4, :cond_3

    :try_start_1
    iget-object v4, v3, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v4}, Ljava/util/ArrayList;->size()I

    move-result v4

    const/16 v6, 0x64

    if-lt v4, v6, :cond_2

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "postWindowRemoveCleanupLocked: Removing "

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    iget-object v6, v3, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v6}, Ljava/util/ArrayList;->size()I

    move-result v6

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v6, " windows in mWinRemovedSinceNullFocus for preventing window leaks when no focus for a long time"

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v5, v4}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v4, v3, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v4}, Ljava/util/ArrayList;->clear()V

    :cond_2
    iget-object v4, v3, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v4, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :cond_3
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v4, p1}, Lcom/android/server/wm/EmbeddedWindowController;->onWindowRemoved(Lcom/android/server/wm/WindowState;)V

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mResizingWindows:Ljava/util/ArrayList;

    invoke-virtual {v4, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    invoke-virtual {p0, p1, v2}, Lcom/android/server/wm/WindowManagerService;->updateNonSystemOverlayWindowsVisibilityIfNeeded(Lcom/android/server/wm/WindowState;Z)V

    const/4 v4, 0x1

    iput-boolean v4, p0, Lcom/android/server/wm/WindowManagerService;->mWindowsChanged:Z

    sget-object v6, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_WINDOW_MOVEMENT_enabled:[Z

    aget-boolean v6, v6, v2

    if-eqz v6, :cond_4

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v6

    sget-object v7, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_WINDOW_MOVEMENT:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v6}, [Ljava/lang/Object;

    move-result-object v8

    const-wide v9, -0x35654ec9983fc866L

    invoke-static {v7, v9, v10, v2, v8}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_4
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v6

    iget-object v7, v6, Lcom/android/server/wm/DisplayContent;->mInputMethodWindow:Lcom/android/server/wm/WindowState;

    if-ne v7, p1, :cond_5

    const/4 v7, 0x0

    invoke-virtual {v6, v7}, Lcom/android/server/wm/DisplayContent;->setInputMethodWindowLocked(Lcom/android/server/wm/WindowState;)V

    :cond_5
    iget-object v7, p1, Lcom/android/server/wm/WindowState;->mToken:Lcom/android/server/wm/WindowToken;

    sget-object v8, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_ADD_REMOVE_enabled:[Z

    aget-boolean v8, v8, v2

    if-eqz v8, :cond_6

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v9

    sget-object v10, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_ADD_REMOVE:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v8, v9}, [Ljava/lang/Object;

    move-result-object v11

    const-wide v12, 0x13b355f4fc2e37a5L

    invoke-static {v10, v12, v13, v2, v11}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_6
    invoke-virtual {v7}, Lcom/android/server/wm/WindowToken;->isEmpty()Z

    move-result v2

    if-eqz v2, :cond_7

    iget-boolean v2, v7, Lcom/android/server/wm/WindowToken;->mPersistOnEmpty:Z

    if-nez v2, :cond_7

    invoke-virtual {v7}, Lcom/android/server/wm/WindowToken;->removeIfPossible()V

    :cond_7
    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    iget v2, v2, Landroid/view/WindowManager$LayoutParams;->type:I

    const/4 v8, 0x3

    if-ne v2, v8, :cond_8

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "postWindowRemoveCleanupLocked: Removing startingWindow "

    invoke-virtual {v2, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v8, " from "

    invoke-virtual {v2, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v8, " activity = "

    invoke-virtual {v2, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-object v8, p1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    invoke-virtual {v2, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v5, v2}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_8
    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    if-eqz v2, :cond_9

    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    invoke-virtual {v2, p1}, Lcom/android/server/wm/ActivityRecord;->postWindowRemoveStartingWindowCleanup(Lcom/android/server/wm/WindowState;)V

    :cond_9
    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    iget v2, v2, Landroid/view/WindowManager$LayoutParams;->type:I

    const/16 v5, 0x7dd

    if-ne v2, v5, :cond_a

    iget-object v2, v3, Lcom/android/server/wm/DisplayContent;->mWallpaperController:Lcom/android/server/wm/WallpaperController;

    invoke-virtual {v2}, Lcom/android/server/wm/WallpaperController;->clearLastWallpaperTimeoutTime()V

    iget v2, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    or-int/lit8 v2, v2, 0x4

    iput v2, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    goto :goto_0

    :cond_a
    iget-object v2, v3, Lcom/android/server/wm/DisplayContent;->mWallpaperController:Lcom/android/server/wm/WallpaperController;

    invoke-virtual {v2, p1}, Lcom/android/server/wm/WallpaperController;->isWallpaperTarget(Lcom/android/server/wm/WindowState;)Z

    move-result v2

    if-eqz v2, :cond_b

    iget v2, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    or-int/lit8 v2, v2, 0x4

    iput v2, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    :cond_b
    :goto_0
    if-eqz v3, :cond_d

    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;

    invoke-virtual {v2}, Lcom/android/server/wm/WindowSurfacePlacer;->isInLayout()Z

    move-result v2

    if-nez v2, :cond_d

    invoke-virtual {v3, v4}, Lcom/android/server/wm/DisplayContent;->assignWindowLayers(Z)V

    invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->getFocusedWindow()Lcom/android/server/wm/WindowState;

    move-result-object v2

    if-ne v2, p1, :cond_c

    iput-boolean v4, p0, Lcom/android/server/wm/WindowManagerService;->mFocusMayChange:Z

    :cond_c
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;

    invoke-virtual {v2}, Lcom/android/server/wm/WindowSurfacePlacer;->performSurfacePlacement()V

    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    if-eqz v2, :cond_d

    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    invoke-virtual {v2}, Lcom/android/server/wm/ActivityRecord;->updateReportedVisibilityLocked()V

    :cond_d
    invoke-virtual {v3}, Lcom/android/server/wm/DisplayContent;->getInputMonitor()Lcom/android/server/wm/InputMonitor;

    move-result-object v2

    invoke-virtual {v2, v4}, Lcom/android/server/wm/InputMonitor;->updateInputWindowsLw(Z)V

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    return-void

    :catchall_0
    move-exception p1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw p1
.end method
""",
        "replacement": """\
.method postWindowRemoveCleanupLocked(Lcom/android/server/wm/WindowState;)V
    .registers 16

    goto :goto_8

    nop

    :goto_0
    if-eqz v4, :cond_0

    goto :goto_1

    :cond_0
    :try_start_0
    iget-object v4, v3, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v4}, Ljava/util/ArrayList;->size()I

    move-result v4

    const/16 v6, 0x64

    if-lt v4, v6, :cond_1

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "postWindowRemoveCleanupLocked: Removing "

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    iget-object v6, v3, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v6}, Ljava/util/ArrayList;->size()I

    move-result v6

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v6, " windows in mWinRemovedSinceNullFocus for preventing window leaks when no focus for a long time"

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v5, v4}, Landroid/util/Slog;->w(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v4, v3, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v4}, Ljava/util/ArrayList;->clear()V

    :cond_1
    iget-object v4, v3, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v4, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :goto_1
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v4, p1}, Lcom/android/server/wm/EmbeddedWindowController;->onWindowRemoved(Lcom/android/server/wm/WindowState;)V

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mResizingWindows:Ljava/util/ArrayList;

    invoke-virtual {v4, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    invoke-virtual {p0, p1, v2}, Lcom/android/server/wm/WindowManagerService;->updateNonSystemOverlayWindowsVisibilityIfNeeded(Lcom/android/server/wm/WindowState;Z)V

    const/4 v4, 0x1

    iput-boolean v4, p0, Lcom/android/server/wm/WindowManagerService;->mWindowsChanged:Z

    sget-object v6, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_WINDOW_MOVEMENT_enabled:[Z

    aget-boolean v6, v6, v2

    if-eqz v6, :cond_2

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v6

    sget-object v7, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_WINDOW_MOVEMENT:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v6}, [Ljava/lang/Object;

    move-result-object v8

    const-wide v9, -0x35654ec9983fc866L

    invoke-static {v7, v9, v10, v2, v8}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_2
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v6

    iget-object v7, v6, Lcom/android/server/wm/DisplayContent;->mInputMethodWindow:Lcom/android/server/wm/WindowState;

    if-ne v7, p1, :cond_3

    const/4 v7, 0x0

    invoke-virtual {v6, v7}, Lcom/android/server/wm/DisplayContent;->setInputMethodWindowLocked(Lcom/android/server/wm/WindowState;)V

    :cond_3
    iget-object v7, p1, Lcom/android/server/wm/WindowState;->mToken:Lcom/android/server/wm/WindowToken;

    sget-object v8, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_ADD_REMOVE_enabled:[Z

    aget-boolean v8, v8, v2

    if-eqz v8, :cond_4

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v9

    sget-object v10, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_ADD_REMOVE:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v8, v9}, [Ljava/lang/Object;

    move-result-object v11

    const-wide v12, 0x13b355f4fc2e37a5L

    invoke-static {v10, v12, v13, v2, v11}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_4
    invoke-virtual {v7}, Lcom/android/server/wm/WindowToken;->isEmpty()Z

    move-result v2

    if-eqz v2, :cond_5

    iget-boolean v2, v7, Lcom/android/server/wm/WindowToken;->mPersistOnEmpty:Z

    if-nez v2, :cond_5

    invoke-virtual {v7}, Lcom/android/server/wm/WindowToken;->removeIfPossible()V

    :cond_5
    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    iget v2, v2, Landroid/view/WindowManager$LayoutParams;->type:I

    const/4 v8, 0x3

    if-ne v2, v8, :cond_6

    new-instance v2, Ljava/lang/StringBuilder;

    invoke-direct {v2}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "postWindowRemoveCleanupLocked: Removing startingWindow "

    invoke-virtual {v2, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v8, " from "

    invoke-virtual {v2, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2, v7}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    const-string v8, " activity = "

    invoke-virtual {v2, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v2

    iget-object v8, p1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    invoke-virtual {v2, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v2

    invoke-static {v5, v2}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_6
    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    if-eqz v2, :cond_7

    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    invoke-virtual {v2, p1}, Lcom/android/server/wm/ActivityRecord;->postWindowRemoveStartingWindowCleanup(Lcom/android/server/wm/WindowState;)V

    :cond_7
    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    iget v2, v2, Landroid/view/WindowManager$LayoutParams;->type:I

    const/16 v5, 0x7dd

    if-ne v2, v5, :cond_8

    iget-object v2, v3, Lcom/android/server/wm/DisplayContent;->mWallpaperController:Lcom/android/server/wm/WallpaperController;

    invoke-virtual {v2}, Lcom/android/server/wm/WallpaperController;->clearLastWallpaperTimeoutTime()V

    iget v2, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    or-int/lit8 v2, v2, 0x4

    iput v2, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    goto :goto_2

    :cond_8
    iget-object v2, v3, Lcom/android/server/wm/DisplayContent;->mWallpaperController:Lcom/android/server/wm/WallpaperController;

    invoke-virtual {v2, p1}, Lcom/android/server/wm/WallpaperController;->isWallpaperTarget(Lcom/android/server/wm/WindowState;)Z

    move-result v2

    if-eqz v2, :cond_9

    iget v2, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    or-int/lit8 v2, v2, 0x4

    iput v2, v3, Lcom/android/server/wm/DisplayContent;->pendingLayoutChanges:I

    :cond_9
    :goto_2
    if-eqz v3, :cond_b

    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;

    invoke-virtual {v2}, Lcom/android/server/wm/WindowSurfacePlacer;->isInLayout()Z

    move-result v2

    if-nez v2, :cond_b

    invoke-virtual {v3, v4}, Lcom/android/server/wm/DisplayContent;->assignWindowLayers(Z)V

    invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->getFocusedWindow()Lcom/android/server/wm/WindowState;

    move-result-object v2

    if-ne v2, p1, :cond_a

    iput-boolean v4, p0, Lcom/android/server/wm/WindowManagerService;->mFocusMayChange:Z

    :cond_a
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;

    invoke-virtual {v2}, Lcom/android/server/wm/WindowSurfacePlacer;->performSurfacePlacement()V

    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    if-eqz v2, :cond_b

    iget-object v2, p1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    invoke-virtual {v2}, Lcom/android/server/wm/ActivityRecord;->updateReportedVisibilityLocked()V

    :cond_b
    invoke-virtual {v3}, Lcom/android/server/wm/DisplayContent;->getInputMonitor()Lcom/android/server/wm/InputMonitor;

    move-result-object v2

    invoke-virtual {v2, v4}, Lcom/android/server/wm/InputMonitor;->updateInputWindowsLw(Z)V

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_6

    nop

    :goto_3
    throw p1

    :goto_4
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_1
    sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_ADD_REMOVE_enabled:[Z

    const/4 v2, 0x0

    aget-boolean v1, v1, v2

    if-eqz v1, :cond_c

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v1

    sget-object v3, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_ADD_REMOVE:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v1}, [Ljava/lang/Object;

    move-result-object v4

    const-wide v5, 0x491202655c343519L

    invoke-static {v3, v5, v6, v2, v4}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->v(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_c
    iget-object v1, p1, Lcom/android/server/wm/WindowState;->mClient:Landroid/view/IWindow;

    invoke-interface {v1}, Landroid/view/IWindow;->asBinder()Landroid/os/IBinder;

    move-result-object v1

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    invoke-virtual {v3, v1}, Ljava/util/HashMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    invoke-static {}, Landroid/view/flags/Flags;->sensitiveContentAppProtection()Z

    move-result v3

    if-eqz v3, :cond_d

    invoke-direct {p0, v1}, Lcom/android/server/wm/WindowManagerService;->notifyWindowRemovedListeners(Landroid/os/IBinder;)V

    :cond_d
    invoke-static {}, Lcom/android/server/wm/WindowManagerServiceStub;->get()Lcom/android/server/wm/WindowManagerServiceStub;

    move-result-object v3

    invoke-interface {v3, p1}, Lcom/android/server/wm/WindowManagerServiceStub;->notifyWindowRemoved(Lcom/android/server/wm/WindowState;)V

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v3

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->resetAppOpsState()V

    iget-object v4, v3, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_5

    nop

    :goto_5
    const-string v5, "WindowManager"

    goto :goto_0

    nop

    :goto_6
    return-void

    :catchall_0
    move-exception p1

    goto :goto_7

    nop

    :goto_7
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_8
    const-string v0, "com.android.server.wm.WindowManagerService.postWindowRemoveCleanupLocked(Lcom/android/server/wm/WindowState;)V"

    goto :goto_4

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.postWindowRemoveCleanupLocked(Lcom/android/server/wm/WindowState;)V"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'sget-object v1, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_ADD_REMOVE_enabled:[Z', 'if-eqz v1, :cond_0', 'invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;', 'move-result-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_removeClientToken_Lcom_android_server_wm_Session_Landroid_os",
        "method":      ".method removeClientToken(Lcom/android/server/wm/Session;Landroid/os/IBinder;)V",
        "method_name": 'removeClientToken',
        "type":        "method_replace",
        "search": """\
.method removeClientToken(Lcom/android/server/wm/Session;Landroid/os/IBinder;)V
    .registers 11

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v1

    const/4 v0, 0x0

    :try_start_0
    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;

    move-result-object v0

    move-object v5, v0

    if-eqz v5, :cond_2

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mWmsExt:Lcom/mediatek/server/wm/WmsExt;

    invoke-virtual {v0, v5}, Lcom/mediatek/server/wm/WmsExt;->removeMwcWindow(Lcom/android/server/wm/WindowState;)V

    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->removeIfPossible()V

    iget-object v0, v5, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    if-eqz v0, :cond_0

    iget-object v0, v5, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    invoke-virtual {v0}, Lcom/android/server/wm/ActivityRecord;->isClientVisible()Z

    move-result v0

    if-nez v0, :cond_1

    :cond_0
    invoke-static {}, Lcom/android/server/am/SmartPowerServiceStub;->getInstance()Lcom/android/server/am/SmartPowerServiceStub;

    move-result-object v2

    iget v3, p1, Lcom/android/server/wm/Session;->mUid:I

    iget v4, p1, Lcom/android/server/wm/Session;->mPid:I

    iget-object v6, v5, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    const/4 v7, 0x0

    invoke-interface/range {v2 .. v7}, Lcom/android/server/am/SmartPowerServiceStub;->onWindowVisibilityChanged(IILcom/android/server/policy/WindowManagerPolicy$WindowState;Landroid/view/WindowManager$LayoutParams;Z)V

    :cond_1
    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_2
    :try_start_1
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v0, p2}, Lcom/android/server/wm/EmbeddedWindowController;->remove(Landroid/os/IBinder;)V

    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v0

    :try_start_2
    monitor-exit v1
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v0
.end method
""",
        "replacement": """\
.method removeClientToken(Lcom/android/server/wm/Session;Landroid/os/IBinder;)V
    .registers 11

    goto :goto_5

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_2

    nop

    :goto_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_7

    nop

    :goto_2
    return-void

    :catchall_0
    move-exception v0

    :try_start_0
    monitor-exit v1
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop

    :goto_3
    return-void

    :cond_0
    :try_start_1
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    invoke-virtual {v0, p2}, Lcom/android/server/wm/EmbeddedWindowController;->remove(Landroid/os/IBinder;)V

    monitor-exit v1
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_0

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_3

    nop

    :goto_5
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_9

    nop

    :goto_6
    const/4 v0, 0x0

    :try_start_2
    invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;

    move-result-object v0

    move-object v5, v0

    if-eqz v5, :cond_0

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mWmsExt:Lcom/mediatek/server/wm/WmsExt;

    invoke-virtual {v0, v5}, Lcom/mediatek/server/wm/WmsExt;->removeMwcWindow(Lcom/android/server/wm/WindowState;)V

    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->removeIfPossible()V

    iget-object v0, v5, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    if-eqz v0, :cond_1

    iget-object v0, v5, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    invoke-virtual {v0}, Lcom/android/server/wm/ActivityRecord;->isClientVisible()Z

    move-result v0

    if-nez v0, :cond_2

    :cond_1
    invoke-static {}, Lcom/android/server/am/SmartPowerServiceStub;->getInstance()Lcom/android/server/am/SmartPowerServiceStub;

    move-result-object v2

    iget v3, p1, Lcom/android/server/wm/Session;->mUid:I

    iget v4, p1, Lcom/android/server/wm/Session;->mPid:I

    iget-object v6, v5, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    const/4 v7, 0x0

    invoke-interface/range {v2 .. v7}, Lcom/android/server/am/SmartPowerServiceStub;->onWindowVisibilityChanged(IILcom/android/server/policy/WindowManagerPolicy$WindowState;Landroid/view/WindowManager$LayoutParams;Z)V

    :cond_2
    monitor-exit v1
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_4

    nop

    :goto_7
    throw v0

    :goto_8
    monitor-enter v1

    goto :goto_6

    nop

    :goto_9
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_8

    nop
.end method
""",
        "method_anchors": ['iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'invoke-virtual {p0, p1, p2, v0}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;', 'move-result-object v0', 'if-eqz v5, :cond_2', 'iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mWmsExt:Lcom/mediatek/server/wm/WmsExt;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_removeWindowChangeListener_Lcom_android_server_wm_WindowMana",
        "method":      ".method removeWindowChangeListener(Lcom/android/server/wm/WindowManagerService$WindowChangeListener;)V",
        "method_name": 'removeWindowChangeListener',
        "type":        "method_replace",
        "search": """\
.method removeWindowChangeListener(Lcom/android/server/wm/WindowManagerService$WindowChangeListener;)V
    .registers 4

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowChangeListeners:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method removeWindowChangeListener(Lcom/android/server/wm/WindowManagerService$WindowChangeListener;)V
    .registers 4

    goto :goto_4

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_5

    nop

    :goto_1
    return-void

    :catchall_0
    move-exception v1

    :try_start_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_0

    nop

    :goto_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_3

    nop

    :goto_3
    monitor-enter v0

    :try_start_1
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowChangeListeners:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_6

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_2

    nop

    :goto_5
    throw v1

    :goto_6
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowChangeListeners:Ljava/util/ArrayList;', 'invoke-virtual {v1, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_removeWindowFocusChangeListener_Lcom_android_server_wm_Windo",
        "method":      ".method removeWindowFocusChangeListener(Lcom/android/server/wm/WindowManagerInternal$WindowFocusChangeListener;)V",
        "method_name": 'removeWindowFocusChangeListener',
        "type":        "method_replace",
        "search": """\
.method removeWindowFocusChangeListener(Lcom/android/server/wm/WindowManagerInternal$WindowFocusChangeListener;)V
    .registers 4

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowFocusChangeListeners:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method removeWindowFocusChangeListener(Lcom/android/server/wm/WindowManagerInternal$WindowFocusChangeListener;)V
    .registers 4

    goto :goto_2

    nop

    :goto_0
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowFocusChangeListeners:Ljava/util/ArrayList;

    invoke-virtual {v1, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_6

    nop

    :goto_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_0

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_1

    nop

    :goto_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_5

    nop

    :goto_4
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_3

    nop

    :goto_5
    throw v1

    :goto_6
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_4

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowFocusChangeListeners:Ljava/util/ArrayList;', 'invoke-virtual {v1, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_removeWindowToken_Landroid_os_IBinder_ZZI_V",
        "method":      ".method removeWindowToken(Landroid/os/IBinder;ZZI)V",
        "method_name": 'removeWindowToken',
        "type":        "method_replace",
        "search": """\
.method removeWindowToken(Landroid/os/IBinder;ZZI)V
    .registers 15

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p4}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    const/4 v2, 0x3

    if-nez v1, :cond_1

    sget-object v3, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    aget-boolean v2, v3, v2

    if-eqz v2, :cond_0

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v2

    int-to-long v3, p4

    sget-object v5, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v6

    filled-new-array {v2, v6}, [Ljava/lang/Object;

    move-result-object v6

    const-wide v7, -0xe834626e038cba9L

    const/4 v9, 0x4

    invoke-static {v5, v7, v8, v9, v6}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_1
    :try_start_1
    invoke-virtual {v1, p1, p3}, Lcom/android/server/wm/DisplayContent;->removeWindowToken(Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowToken;

    move-result-object v3

    if-nez v3, :cond_3

    sget-object v4, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    aget-boolean v2, v4, v2

    if-eqz v2, :cond_2

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v2

    sget-object v4, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v2}, [Ljava/lang/Object;

    move-result-object v5

    const-wide v6, 0xc2400cc5ad0334fL

    const/4 v8, 0x0

    invoke-static {v4, v6, v7, v8, v5}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_2
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_3
    if-eqz p2, :cond_4

    :try_start_2
    invoke-virtual {v3}, Lcom/android/server/wm/WindowToken;->removeAllWindowsIfPossible()V

    :cond_4
    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getInputMonitor()Lcom/android/server/wm/InputMonitor;

    move-result-object v2

    const/4 v4, 0x1

    invoke-virtual {v2, v4}, Lcom/android/server/wm/InputMonitor;->updateInputWindowsLw(Z)V

    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_3
    monitor-exit v0
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method removeWindowToken(Landroid/os/IBinder;ZZI)V
    .registers 15

    goto :goto_c

    nop

    :goto_0
    return-void

    :catchall_0
    move-exception v1

    :try_start_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_2

    nop

    :goto_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_a

    nop

    :goto_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_b

    nop

    :goto_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_5

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_6

    nop

    :goto_5
    return-void

    :cond_0
    goto :goto_7

    nop

    :goto_6
    return-void

    :cond_1
    :try_start_1
    invoke-virtual {v1, p1, p3}, Lcom/android/server/wm/DisplayContent;->removeWindowToken(Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowToken;

    move-result-object v3

    if-nez v3, :cond_0

    sget-object v4, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    aget-boolean v2, v4, v2

    if-eqz v2, :cond_2

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v2

    sget-object v4, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v2}, [Ljava/lang/Object;

    move-result-object v5

    const-wide v6, 0xc2400cc5ad0334fL

    const/4 v8, 0x0

    invoke-static {v4, v6, v7, v8, v5}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_2
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_3

    nop

    :goto_7
    if-nez p2, :cond_3

    goto :goto_8

    :cond_3
    :try_start_2
    invoke-virtual {v3}, Lcom/android/server/wm/WindowToken;->removeAllWindowsIfPossible()V

    :goto_8
    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getInputMonitor()Lcom/android/server/wm/InputMonitor;

    move-result-object v2

    const/4 v4, 0x1

    invoke-virtual {v2, v4}, Lcom/android/server/wm/InputMonitor;->updateInputWindowsLw(Z)V

    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_9

    nop

    :goto_9
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_0

    nop

    :goto_a
    monitor-enter v0

    :try_start_3
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p4}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    const/4 v2, 0x3

    if-nez v1, :cond_1

    sget-object v3, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    aget-boolean v2, v3, v2

    if-eqz v2, :cond_4

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v2

    int-to-long v3, p4

    sget-object v5, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    invoke-static {v3, v4}, Ljava/lang/Long;->valueOf(J)Ljava/lang/Long;

    move-result-object v6

    filled-new-array {v2, v6}, [Ljava/lang/Object;

    move-result-object v6

    const-wide v7, -0xe834626e038cba9L

    const/4 v9, 0x4

    invoke-static {v5, v7, v8, v9, v6}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_4
    monitor-exit v0
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    goto :goto_4

    nop

    :goto_b
    throw v1

    :goto_c
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;', 'invoke-virtual {v1, p4}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;', 'move-result-object v1', 'if-nez v1, :cond_1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_reportDecorViewGestureChanged_Lcom_android_server_wm_Session",
        "method":      ".method reportDecorViewGestureChanged(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)V",
        "method_name": 'reportDecorViewGestureChanged',
        "type":        "method_replace",
        "search": """\
.method reportDecorViewGestureChanged(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)V
    .registers 8

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    nop

    const/4 v1, 0x0

    :try_start_0
    invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v1

    if-nez v1, :cond_0

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_0
    :try_start_1
    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    iget-object v3, v1, Lcom/android/server/wm/WindowState;->mToken:Lcom/android/server/wm/WindowToken;

    iget-object v3, v3, Lcom/android/server/wm/WindowToken;->token:Landroid/os/IBinder;

    invoke-virtual {v2, v3, p3}, Lcom/android/server/wm/DisplayContent;->updateDecorViewGestureIntercepted(Landroid/os/IBinder;Z)V

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method reportDecorViewGestureChanged(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)V
    .registers 8

    goto :goto_5

    nop

    :goto_0
    return-void

    :cond_0
    :try_start_0
    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    iget-object v3, v1, Lcom/android/server/wm/WindowState;->mToken:Lcom/android/server/wm/WindowToken;

    iget-object v3, v3, Lcom/android/server/wm/WindowToken;->token:Landroid/os/IBinder;

    invoke-virtual {v2, v3, p3}, Lcom/android/server/wm/DisplayContent;->updateDecorViewGestureIntercepted(Landroid/os/IBinder;Z)V

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_4

    nop

    :goto_1
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_7

    nop

    :goto_2
    monitor-enter v0

    nop

    goto :goto_9

    nop

    :goto_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_0

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_1

    nop

    :goto_5
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_8

    nop

    :goto_6
    throw v1

    :goto_7
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_6

    nop

    :goto_8
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_2

    nop

    :goto_9
    const/4 v1, 0x0

    :try_start_2
    invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v1

    if-nez v1, :cond_0

    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;', 'move-result-object v1', 'if-nez v1, :cond_0', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_reportFocusChanged_Landroid_os_IBinder_Landroid_os_IBinder__",
        "method":      ".method reportFocusChanged(Landroid/os/IBinder;Landroid/os/IBinder;)V",
        "method_name": 'reportFocusChanged',
        "type":        "method_replace",
        "search": """\
.method reportFocusChanged(Landroid/os/IBinder;Landroid/os/IBinder;)V
    .registers 13

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    invoke-virtual {p0, p1}, Lcom/android/server/wm/WindowManagerService;->getInputTargetFromToken(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;

    move-result-object v1

    invoke-virtual {p0, p2}, Lcom/android/server/wm/WindowManagerService;->getInputTargetFromToken(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;

    move-result-object v2

    if-nez v2, :cond_0

    if-nez v1, :cond_0

    const-string v3, "WindowManager"

    const-string v4, "Unknown focus tokens, dropping reportFocusChanged"

    invoke-static {v3, v4}, Landroid/util/Slog;->v(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_0
    :try_start_1
    iput-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mFocusedInputTarget:Lcom/android/server/wm/InputTarget;

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mAccessibilityController:Lcom/android/server/wm/AccessibilityController;

    invoke-virtual {v3, v1, v2}, Lcom/android/server/wm/AccessibilityController;->onFocusChanged(Lcom/android/server/wm/InputTarget;Lcom/android/server/wm/InputTarget;)V

    sget-object v3, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_FOCUS_LIGHT_enabled:[Z

    const/4 v4, 0x2

    aget-boolean v3, v3, v4

    const/4 v4, 0x0

    if-eqz v3, :cond_1

    invoke-static {v1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v2}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    sget-object v6, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_FOCUS_LIGHT:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v3, v5}, [Ljava/lang/Object;

    move-result-object v7

    const-wide v8, -0x2f92cca40c6fcbd9L

    invoke-static {v6, v8, v9, v4, v7}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->i(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_1
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mWmsExt:Lcom/mediatek/server/wm/WmsExt;

    const/4 v5, 0x0

    if-nez v2, :cond_2

    move-object v6, v5

    goto :goto_0

    :cond_2
    invoke-interface {v2}, Lcom/android/server/wm/InputTarget;->getWindowState()Lcom/android/server/wm/WindowState;

    move-result-object v6

    :goto_0
    invoke-virtual {v3, v6}, Lcom/mediatek/server/wm/WmsExt;->reportFocusChangedMwcFeature(Lcom/android/server/wm/WindowState;)V

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    if-eqz v2, :cond_3

    invoke-interface {v2}, Lcom/android/server/wm/InputTarget;->getWindowState()Lcom/android/server/wm/WindowState;

    move-result-object v0

    goto :goto_1

    :cond_3
    move-object v0, v5

    :goto_1
    if-eqz v0, :cond_4

    iget-object v3, v0, Lcom/android/server/wm/WindowState;->mInputChannelToken:Landroid/os/IBinder;

    if-ne v3, p2, :cond_4

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mAnrController:Lcom/android/server/wm/AnrController;

    invoke-virtual {v3, v0}, Lcom/android/server/wm/AnrController;->onFocusChanged(Lcom/android/server/wm/WindowState;)V

    const/4 v3, 0x1

    invoke-virtual {v0, v3}, Lcom/android/server/wm/WindowState;->reportFocusChangedSerialized(Z)V

    invoke-interface {v2}, Lcom/android/server/wm/InputTarget;->getWindowToken()Landroid/os/IBinder;

    move-result-object v3

    invoke-direct {p0, v3}, Lcom/android/server/wm/WindowManagerService;->notifyFocusChanged(Landroid/os/IBinder;)V

    :cond_4
    if-eqz v1, :cond_5

    invoke-interface {v1}, Lcom/android/server/wm/InputTarget;->getWindowState()Lcom/android/server/wm/WindowState;

    move-result-object v5

    :cond_5
    if-eqz v5, :cond_6

    iget-object v3, v5, Lcom/android/server/wm/WindowState;->mInputChannelToken:Landroid/os/IBinder;

    if-ne v3, p1, :cond_6

    invoke-virtual {v5, v4}, Lcom/android/server/wm/WindowState;->reportFocusChangedSerialized(Z)V

    :cond_6
    return-void

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method reportFocusChanged(Landroid/os/IBinder;Landroid/os/IBinder;)V
    .registers 13

    goto :goto_18

    nop

    :goto_0
    move-object v0, v5

    :goto_1
    goto :goto_9

    nop

    :goto_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_1b

    nop

    :goto_3
    invoke-virtual {v3, v0}, Lcom/android/server/wm/AnrController;->onFocusChanged(Lcom/android/server/wm/WindowState;)V

    goto :goto_12

    nop

    :goto_4
    monitor-enter v0

    :try_start_0
    invoke-virtual {p0, p1}, Lcom/android/server/wm/WindowManagerService;->getInputTargetFromToken(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;

    move-result-object v1

    invoke-virtual {p0, p2}, Lcom/android/server/wm/WindowManagerService;->getInputTargetFromToken(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;

    move-result-object v2

    if-nez v2, :cond_6

    if-nez v1, :cond_6

    const-string v3, "WindowManager"

    const-string v4, "Unknown focus tokens, dropping reportFocusChanged"

    invoke-static {v3, v4}, Landroid/util/Slog;->v(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_2

    nop

    :goto_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_16

    nop

    :goto_6
    invoke-interface {v1}, Lcom/android/server/wm/InputTarget;->getWindowState()Lcom/android/server/wm/WindowState;

    move-result-object v5

    :goto_7
    goto :goto_19

    nop

    :goto_8
    invoke-virtual {v0, v3}, Lcom/android/server/wm/WindowState;->reportFocusChangedSerialized(Z)V

    goto :goto_1f

    nop

    :goto_9
    if-nez v0, :cond_0

    goto :goto_14

    :cond_0
    goto :goto_11

    nop

    :goto_a
    if-nez v1, :cond_1

    goto :goto_7

    :cond_1
    goto :goto_6

    nop

    :goto_b
    if-eq v3, p2, :cond_2

    goto :goto_14

    :cond_2
    goto :goto_1d

    nop

    :goto_c
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_4

    nop

    :goto_d
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_1a

    nop

    :goto_e
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_5

    nop

    :goto_f
    goto :goto_1

    :goto_10
    goto :goto_0

    nop

    :goto_11
    iget-object v3, v0, Lcom/android/server/wm/WindowState;->mInputChannelToken:Landroid/os/IBinder;

    goto :goto_b

    nop

    :goto_12
    const/4 v3, 0x1

    goto :goto_8

    nop

    :goto_13
    invoke-direct {p0, v3}, Lcom/android/server/wm/WindowManagerService;->notifyFocusChanged(Landroid/os/IBinder;)V

    :goto_14
    goto :goto_a

    nop

    :goto_15
    iget-object v3, v5, Lcom/android/server/wm/WindowState;->mInputChannelToken:Landroid/os/IBinder;

    goto :goto_17

    nop

    :goto_16
    throw v1

    :goto_17
    if-eq v3, p1, :cond_3

    goto :goto_21

    :cond_3
    goto :goto_20

    nop

    :goto_18
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_c

    nop

    :goto_19
    if-nez v5, :cond_4

    goto :goto_21

    :cond_4
    goto :goto_15

    nop

    :goto_1a
    if-nez v2, :cond_5

    goto :goto_10

    :cond_5
    goto :goto_1e

    nop

    :goto_1b
    return-void

    :cond_6
    :try_start_2
    iput-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mFocusedInputTarget:Lcom/android/server/wm/InputTarget;

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mAccessibilityController:Lcom/android/server/wm/AccessibilityController;

    invoke-virtual {v3, v1, v2}, Lcom/android/server/wm/AccessibilityController;->onFocusChanged(Lcom/android/server/wm/InputTarget;Lcom/android/server/wm/InputTarget;)V

    sget-object v3, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_DEBUG_FOCUS_LIGHT_enabled:[Z

    const/4 v4, 0x2

    aget-boolean v3, v3, v4

    const/4 v4, 0x0

    if-eqz v3, :cond_7

    invoke-static {v1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v3

    invoke-static {v2}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    sget-object v6, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_DEBUG_FOCUS_LIGHT:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v3, v5}, [Ljava/lang/Object;

    move-result-object v7

    const-wide v8, -0x2f92cca40c6fcbd9L

    invoke-static {v6, v8, v9, v4, v7}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->i(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_7
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mWmsExt:Lcom/mediatek/server/wm/WmsExt;

    const/4 v5, 0x0

    if-nez v2, :cond_8

    move-object v6, v5

    goto :goto_1c

    :cond_8
    invoke-interface {v2}, Lcom/android/server/wm/InputTarget;->getWindowState()Lcom/android/server/wm/WindowState;

    move-result-object v6

    :goto_1c
    invoke-virtual {v3, v6}, Lcom/mediatek/server/wm/WmsExt;->reportFocusChangedMwcFeature(Lcom/android/server/wm/WindowState;)V

    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_d

    nop

    :goto_1d
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mAnrController:Lcom/android/server/wm/AnrController;

    goto :goto_3

    nop

    :goto_1e
    invoke-interface {v2}, Lcom/android/server/wm/InputTarget;->getWindowState()Lcom/android/server/wm/WindowState;

    move-result-object v0

    goto :goto_f

    nop

    :goto_1f
    invoke-interface {v2}, Lcom/android/server/wm/InputTarget;->getWindowToken()Landroid/os/IBinder;

    move-result-object v3

    goto :goto_13

    nop

    :goto_20
    invoke-virtual {v5, v4}, Lcom/android/server/wm/WindowState;->reportFocusChangedSerialized(Z)V

    :goto_21
    goto :goto_e

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'invoke-virtual {p0, p1}, Lcom/android/server/wm/WindowManagerService;->getInputTargetFromToken(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;', 'move-result-object v1', 'invoke-virtual {p0, p2}, Lcom/android/server/wm/WindowManagerService;->getInputTargetFromToken(Landroid/os/IBinder;)Lcom/android/server/wm/InputTarget;', 'move-result-object v2'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_reportKeepClearAreasChanged_Lcom_android_server_wm_Session_L",
        "method":      ".method reportKeepClearAreasChanged(Lcom/android/server/wm/Session;Landroid/view/IWindow;Ljava/util/List;Ljava/util/List;)V",
        "method_name": 'reportKeepClearAreasChanged',
        "type":        "method_replace",
        "search": """\
.method reportKeepClearAreasChanged(Lcom/android/server/wm/Session;Landroid/view/IWindow;Ljava/util/List;Ljava/util/List;)V
    .registers 10
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lcom/android/server/wm/Session;",
            "Landroid/view/IWindow;",
            "Ljava/util/List<",
            "Landroid/graphics/Rect;",
            ">;",
            "Ljava/util/List<",
            "Landroid/graphics/Rect;",
            ">;)V"
        }
    .end annotation

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    const/4 v1, 0x0

    :try_start_0
    invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v1

    if-nez v1, :cond_0

    const-string v2, "WindowManager"

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "reportKeepClearAreasChanged(): No window state for package:"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, p1, Lcom/android/server/wm/Session;->mPackageName:Ljava/lang/String;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v2, v3}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_0
    :try_start_1
    invoke-virtual {v1, p3, p4}, Lcom/android/server/wm/WindowState;->setKeepClearAreas(Ljava/util/List;Ljava/util/List;)Z

    move-result v2

    if-eqz v2, :cond_1

    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    invoke-virtual {v2}, Lcom/android/server/wm/DisplayContent;->updateKeepClearAreas()V

    :cond_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method reportKeepClearAreasChanged(Lcom/android/server/wm/Session;Landroid/view/IWindow;Ljava/util/List;Ljava/util/List;)V
    .registers 10
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lcom/android/server/wm/Session;",
            "Landroid/view/IWindow;",
            "Ljava/util/List<",
            "Landroid/graphics/Rect;",
            ">;",
            "Ljava/util/List<",
            "Landroid/graphics/Rect;",
            ">;)V"
        }
    .end annotation

    goto :goto_8

    nop

    :goto_0
    const/4 v1, 0x0

    :try_start_0
    invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v1

    if-nez v1, :cond_0

    const-string v2, "WindowManager"

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "reportKeepClearAreasChanged(): No window state for package:"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, p1, Lcom/android/server/wm/Session;->mPackageName:Ljava/lang/String;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v2, v3}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_5

    nop

    :goto_1
    monitor-enter v0

    goto :goto_0

    nop

    :goto_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_1

    nop

    :goto_3
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_4

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_6

    nop

    :goto_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_7

    nop

    :goto_6
    throw v1

    :goto_7
    return-void

    :cond_0
    :try_start_2
    invoke-virtual {v1, p3, p4}, Lcom/android/server/wm/WindowState;->setKeepClearAreas(Ljava/util/List;Ljava/util/List;)Z

    move-result v2

    if-eqz v2, :cond_1

    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    invoke-virtual {v2}, Lcom/android/server/wm/DisplayContent;->updateKeepClearAreas()V

    :cond_1
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_9

    nop

    :goto_8
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_2

    nop

    :goto_9
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;', 'move-result-object v1', 'if-nez v1, :cond_0', 'const-string v2, "WindowManager"'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_reportSystemGestureExclusionChanged_Lcom_android_server_wm_S",
        "method":      ".method reportSystemGestureExclusionChanged(Lcom/android/server/wm/Session;Landroid/view/IWindow;Ljava/util/List;)V",
        "method_name": 'reportSystemGestureExclusionChanged',
        "type":        "method_replace",
        "search": """\
.method reportSystemGestureExclusionChanged(Lcom/android/server/wm/Session;Landroid/view/IWindow;Ljava/util/List;)V
    .registers 9
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lcom/android/server/wm/Session;",
            "Landroid/view/IWindow;",
            "Ljava/util/List<",
            "Landroid/graphics/Rect;",
            ">;)V"
        }
    .end annotation

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    const/4 v1, 0x0

    :try_start_0
    invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v1

    if-nez v1, :cond_0

    const-string v2, "WindowManager"

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "reportSystemGestureExclusionChanged(): No window state for package:"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, p1, Lcom/android/server/wm/Session;->mPackageName:Ljava/lang/String;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v2, v3}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_0
    :try_start_1
    sget-boolean v2, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG:Z

    if-eqz v2, :cond_1

    new-instance v2, Ljava/lang/StringBuilder;

    const/16 v3, 0x40

    invoke-direct {v2, v3}, Ljava/lang/StringBuilder;-><init>(I)V

    const-string v3, "reportSystemGestureExclusionChanged(): state for package: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v3, p1, Lcom/android/server/wm/Session;->mPackageName:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v3, ", exclusionRects ="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-interface {p3}, Ljava/util/List;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v3, "WindowManager"

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v3, v4}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_1
    invoke-virtual {v1, p3}, Lcom/android/server/wm/WindowState;->setSystemGestureExclusion(Ljava/util/List;)Z

    move-result v2

    if-eqz v2, :cond_2

    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    invoke-virtual {v2}, Lcom/android/server/wm/DisplayContent;->updateSystemGestureExclusion()Z

    :cond_2
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method reportSystemGestureExclusionChanged(Lcom/android/server/wm/Session;Landroid/view/IWindow;Ljava/util/List;)V
    .registers 9
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lcom/android/server/wm/Session;",
            "Landroid/view/IWindow;",
            "Ljava/util/List<",
            "Landroid/graphics/Rect;",
            ">;)V"
        }
    .end annotation

    goto :goto_9

    nop

    :goto_0
    monitor-enter v0

    goto :goto_5

    nop

    :goto_1
    return-void

    :catchall_0
    move-exception v1

    :try_start_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_7

    nop

    :goto_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_1

    nop

    :goto_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_4

    nop

    :goto_4
    return-void

    :cond_0
    :try_start_1
    sget-boolean v2, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG:Z

    if-eqz v2, :cond_1

    new-instance v2, Ljava/lang/StringBuilder;

    const/16 v3, 0x40

    invoke-direct {v2, v3}, Ljava/lang/StringBuilder;-><init>(I)V

    const-string v3, "reportSystemGestureExclusionChanged(): state for package: "

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    iget-object v3, p1, Lcom/android/server/wm/Session;->mPackageName:Ljava/lang/String;

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v3, ", exclusionRects ="

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    invoke-interface {p3}, Ljava/util/List;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-virtual {v2, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    const-string v3, "WindowManager"

    invoke-virtual {v2}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v3, v4}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_1
    invoke-virtual {v1, p3}, Lcom/android/server/wm/WindowState;->setSystemGestureExclusion(Ljava/util/List;)Z

    move-result v2

    if-eqz v2, :cond_2

    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v2

    invoke-virtual {v2}, Lcom/android/server/wm/DisplayContent;->updateSystemGestureExclusion()Z

    :cond_2
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_2

    nop

    :goto_5
    const/4 v1, 0x0

    :try_start_2
    invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v1

    if-nez v1, :cond_0

    const-string v2, "WindowManager"

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "reportSystemGestureExclusionChanged(): No window state for package:"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, p1, Lcom/android/server/wm/Session;->mPackageName:Ljava/lang/String;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v2, v3}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_3

    nop

    :goto_6
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_0

    nop

    :goto_7
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_8

    nop

    :goto_8
    throw v1

    :goto_9
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_6

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'invoke-virtual {p0, p1, p2, v1}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;', 'move-result-object v1', 'if-nez v1, :cond_0', 'const-string v2, "WindowManager"'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_requestTraversal__V",
        "method":      ".method requestTraversal()V",
        "method_name": 'requestTraversal',
        "type":        "method_replace",
        "search": """\
.method requestTraversal()V
    .registers 2

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;

    invoke-virtual {v0}, Lcom/android/server/wm/WindowSurfacePlacer;->requestTraversal()V

    return-void
.end method
""",
        "replacement": """\
.method requestTraversal()V
    .registers 2

    goto :goto_1

    nop

    :goto_0
    invoke-virtual {v0}, Lcom/android/server/wm/WindowSurfacePlacer;->requestTraversal()V

    goto :goto_2

    nop

    :goto_1
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;

    goto :goto_0

    nop

    :goto_2
    return-void
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;', 'invoke-virtual {v0}, Lcom/android/server/wm/WindowSurfacePlacer;->requestTraversal()V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_resetFreezeRecentTaskListReordering__V",
        "method":      ".method resetFreezeRecentTaskListReordering()V",
        "method_name": 'resetFreezeRecentTaskListReordering',
        "type":        "method_replace",
        "search": """\
.method resetFreezeRecentTaskListReordering()V
    .registers 3

    const-string v0, "android.permission.MANAGE_ACTIVITY_TASKS"

    const-string v1, "resetFreezeRecentTaskListReordering()"

    invoke-virtual {p0, v0, v1}, Lcom/android/server/wm/WindowManagerService;->checkCallingPermission(Ljava/lang/String;Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_0

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;

    invoke-virtual {v0}, Lcom/android/server/wm/ActivityTaskManagerService;->getRecentTasks()Lcom/android/server/wm/RecentTasks;

    move-result-object v0

    invoke-virtual {v0}, Lcom/android/server/wm/RecentTasks;->resetFreezeTaskListReorderingOnTimeout()V

    return-void

    :cond_0
    new-instance v0, Ljava/lang/SecurityException;

    const-string v1, "Requires MANAGE_ACTIVITY_TASKS permission"

    invoke-direct {v0, v1}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    throw v0
.end method
""",
        "replacement": """\
.method resetFreezeRecentTaskListReordering()V
    .registers 3

    goto :goto_5

    nop

    :goto_0
    invoke-virtual {v0}, Lcom/android/server/wm/RecentTasks;->resetFreezeTaskListReorderingOnTimeout()V

    goto :goto_1

    nop

    :goto_1
    return-void

    :goto_2
    goto :goto_7

    nop

    :goto_3
    invoke-direct {v0, v1}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    goto :goto_c

    nop

    :goto_4
    invoke-virtual {p0, v0, v1}, Lcom/android/server/wm/WindowManagerService;->checkCallingPermission(Ljava/lang/String;Ljava/lang/String;)Z

    move-result v0

    goto :goto_6

    nop

    :goto_5
    const-string v0, "android.permission.MANAGE_ACTIVITY_TASKS"

    goto :goto_b

    nop

    :goto_6
    if-nez v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_9

    nop

    :goto_7
    new-instance v0, Ljava/lang/SecurityException;

    goto :goto_8

    nop

    :goto_8
    const-string v1, "Requires MANAGE_ACTIVITY_TASKS permission"

    goto :goto_3

    nop

    :goto_9
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;

    goto :goto_a

    nop

    :goto_a
    invoke-virtual {v0}, Lcom/android/server/wm/ActivityTaskManagerService;->getRecentTasks()Lcom/android/server/wm/RecentTasks;

    move-result-object v0

    goto :goto_0

    nop

    :goto_b
    const-string v1, "resetFreezeRecentTaskListReordering()"

    goto :goto_4

    nop

    :goto_c
    throw v0
.end method
""",
        "method_anchors": ['const-string v0, "android.permission.MANAGE_ACTIVITY_TASKS"', 'const-string v1, "resetFreezeRecentTaskListReordering()"', 'invoke-virtual {p0, v0, v1}, Lcom/android/server/wm/WindowManagerService;->checkCallingPermission(Ljava/lang/String;Ljava/lang/String;)Z', 'move-result v0', 'if-eqz v0, :cond_0', 'iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mAtmService:Lcom/android/server/wm/ActivityTaskManagerService;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_resetIgnoreOrientationRequest_I_Ljava_lang_Boolean_",
        "method":      ".method resetIgnoreOrientationRequest(I)Ljava/lang/Boolean;",
        "method_name": 'resetIgnoreOrientationRequest',
        "type":        "method_replace",
        "search": """\
.method resetIgnoreOrientationRequest(I)Ljava/lang/Boolean;
    .registers 6

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    const/4 v2, 0x0

    if-nez v1, :cond_0

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-object v2

    :cond_0
    const/4 v3, 0x0

    :try_start_1
    iput-boolean v3, v1, Lcom/android/server/wm/DisplayContent;->mHasSetIgnoreOrientationRequest:Z

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayWindowSettings:Lcom/android/server/wm/DisplayWindowSettings;

    invoke-virtual {v3, v1, v2}, Lcom/android/server/wm/DisplayWindowSettings;->setIgnoreOrientationRequest(Lcom/android/server/wm/DisplayContent;Ljava/lang/Boolean;)V

    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayWindowSettings:Lcom/android/server/wm/DisplayWindowSettings;

    invoke-virtual {v2, v1}, Lcom/android/server/wm/DisplayWindowSettings;->applyRotationSettingsToDisplayLocked(Lcom/android/server/wm/DisplayContent;)V

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getIgnoreOrientationRequest()Z

    move-result v2

    invoke-static {v2}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v2

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-object v2

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method resetIgnoreOrientationRequest(I)Ljava/lang/Boolean;
    .registers 6

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_8

    nop

    :goto_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_4

    nop

    :goto_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_7

    nop

    :goto_3
    const/4 v3, 0x0

    :try_start_0
    iput-boolean v3, v1, Lcom/android/server/wm/DisplayContent;->mHasSetIgnoreOrientationRequest:Z

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayWindowSettings:Lcom/android/server/wm/DisplayWindowSettings;

    invoke-virtual {v3, v1, v2}, Lcom/android/server/wm/DisplayWindowSettings;->setIgnoreOrientationRequest(Lcom/android/server/wm/DisplayContent;Ljava/lang/Boolean;)V

    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mDisplayWindowSettings:Lcom/android/server/wm/DisplayWindowSettings;

    invoke-virtual {v2, v1}, Lcom/android/server/wm/DisplayWindowSettings;->applyRotationSettingsToDisplayLocked(Lcom/android/server/wm/DisplayContent;)V

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->getIgnoreOrientationRequest()Z

    move-result v2

    invoke-static {v2}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;

    move-result-object v2

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_6

    nop

    :goto_4
    throw v1

    :goto_5
    monitor-enter v0

    :try_start_1
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v1

    const/4 v2, 0x0

    if-nez v1, :cond_0

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_2

    nop

    :goto_6
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_9

    nop

    :goto_7
    return-object v2

    :cond_0
    goto :goto_3

    nop

    :goto_8
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_5

    nop

    :goto_9
    return-object v2

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;', 'invoke-virtual {v1, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;', 'move-result-object v1', 'if-nez v1, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_saveANRStateLocked_Lcom_android_server_wm_ActivityRecord_Lco",
        "method":      ".method saveANRStateLocked(Lcom/android/server/wm/ActivityRecord;Lcom/android/server/wm/WindowState;Ljava/lang/String;)V",
        "method_name": 'saveANRStateLocked',
        "type":        "method_replace",
        "search": """\
.method saveANRStateLocked(Lcom/android/server/wm/ActivityRecord;Lcom/android/server/wm/WindowState;Ljava/lang/String;)V
    .registers 20

    move-object/from16 v0, p0

    move-object/from16 v1, p1

    move-object/from16 v2, p2

    move-object/from16 v3, p3

    const-string v4, "com.android.server.wm.WindowManagerService.saveANRStateLocked(Lcom/android/server/wm/ActivityRecord;Lcom/android/server/wm/WindowState;Ljava/lang/String;)V"

    invoke-static {v4}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    new-instance v5, Ljava/io/StringWriter;

    invoke-direct {v5}, Ljava/io/StringWriter;-><init>()V

    new-instance v6, Lcom/android/internal/util/FastPrintWriter;

    const/4 v7, 0x0

    const/16 v8, 0x400

    invoke-direct {v6, v5, v7, v8}, Lcom/android/internal/util/FastPrintWriter;-><init>(Ljava/io/Writer;ZI)V

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "  ANR time: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-static {}, Ljava/text/DateFormat;->getDateTimeInstance()Ljava/text/DateFormat;

    move-result-object v8

    new-instance v9, Ljava/util/Date;

    invoke-direct {v9}, Ljava/util/Date;-><init>()V

    invoke-virtual {v8, v9}, Ljava/text/DateFormat;->format(Ljava/util/Date;)Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    if-eqz v1, :cond_0

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "  Application at fault: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v1, Lcom/android/server/wm/ActivityRecord;->stringName:Ljava/lang/String;

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_0
    if-eqz v2, :cond_1

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "  Window at fault: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v2, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v8}, Landroid/view/WindowManager$LayoutParams;->getTitle()Ljava/lang/CharSequence;

    move-result-object v8

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_1
    if-eqz v3, :cond_2

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "  Reason: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_2
    invoke-virtual {v6}, Ljava/io/PrintWriter;->println()V

    new-instance v7, Ljava/util/ArrayList;

    invoke-direct {v7}, Ljava/util/ArrayList;-><init>()V

    iget-object v8, v0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v8}, Lcom/android/server/wm/RootWindowContainer;->getChildCount()I

    move-result v8

    const/4 v9, 0x1

    sub-int/2addr v8, v9

    :goto_0
    if-ltz v8, :cond_6

    iget-object v10, v0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v10, v8}, Lcom/android/server/wm/RootWindowContainer;->getChildAt(I)Lcom/android/server/wm/WindowContainer;

    move-result-object v10

    check-cast v10, Lcom/android/server/wm/DisplayContent;

    invoke-virtual {v10}, Lcom/android/server/wm/DisplayContent;->getDisplayId()I

    move-result v11

    iget-object v12, v10, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;

    iget-object v13, v10, Lcom/android/server/wm/DisplayContent;->mFocusedApp:Lcom/android/server/wm/ActivityRecord;

    new-instance v14, Ljava/lang/StringBuilder;

    invoke-direct {v14}, Ljava/lang/StringBuilder;-><init>()V

    const-string v15, "  Display #"

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v14, v11}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v14

    const-string v15, " currentFocus="

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v14, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v14

    const-string v15, " focusedApp="

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v14, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v14}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v14

    invoke-virtual {v6, v14}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    if-eqz v12, :cond_3

    new-instance v14, Ljava/lang/StringBuilder;

    invoke-direct {v14}, Ljava/lang/StringBuilder;-><init>()V

    const-string v15, "  focus surface relativeTo:"

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v12}, Lcom/android/server/wm/WindowState;->getLastRelativeLayer()Landroid/view/SurfaceControl;

    move-result-object v15

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v14

    const-string v15, " reparent to:"

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v12}, Lcom/android/server/wm/WindowState;->getParentSurfaceControl()Landroid/view/SurfaceControl;

    move-result-object v15

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v14}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v14

    invoke-virtual {v6, v14}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_3
    iget-object v14, v10, Lcom/android/server/wm/DisplayContent;->mWinAddedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v14}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v14
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    const-string v15, " since null focus: "

    if-nez v14, :cond_4

    :try_start_1
    new-instance v14, Ljava/lang/StringBuilder;

    invoke-direct {v14}, Ljava/lang/StringBuilder;-><init>()V

    const-string v9, "  Windows added in display #"

    invoke-virtual {v14, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9, v11}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    iget-object v14, v10, Lcom/android/server/wm/DisplayContent;->mWinAddedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v9, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v6, v9}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_4
    iget-object v9, v10, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v9}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v9

    if-nez v9, :cond_5

    new-instance v9, Ljava/lang/StringBuilder;

    invoke-direct {v9}, Ljava/lang/StringBuilder;-><init>()V

    const-string v14, "  Windows removed in display #"

    invoke-virtual {v9, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9, v11}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    iget-object v14, v10, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v9, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v6, v9}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_5
    const-string v9, "  Tasks in top down Z order:"

    invoke-virtual {v6, v9}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    new-instance v9, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda31;

    invoke-direct {v9, v6}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda31;-><init>(Ljava/io/PrintWriter;)V

    invoke-virtual {v10, v9}, Lcom/android/server/wm/DisplayContent;->forAllTaskDisplayAreas(Ljava/util/function/Consumer;)V

    invoke-virtual {v10}, Lcom/android/server/wm/DisplayContent;->getInputMonitor()Lcom/android/server/wm/InputMonitor;

    move-result-object v9

    const-string v14, "  "

    invoke-virtual {v9, v6, v14}, Lcom/android/server/wm/InputMonitor;->dump(Ljava/io/PrintWriter;Ljava/lang/String;)V

    invoke-virtual {v6}, Ljava/io/PrintWriter;->println()V

    new-instance v9, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda32;

    invoke-direct {v9, v12, v13, v7}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda32;-><init>(Lcom/android/server/wm/WindowState;Lcom/android/server/wm/ActivityRecord;Ljava/util/ArrayList;)V

    const/4 v14, 0x1

    invoke-virtual {v10, v9, v14}, Lcom/android/server/wm/DisplayContent;->forAllWindows(Ljava/util/function/Consumer;Z)V

    add-int/lit8 v8, v8, -0x1

    const/4 v9, 0x1

    goto :goto_0

    :cond_6
    if-eqz v2, :cond_7

    invoke-virtual {v7, v2}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v8

    if-nez v8, :cond_7

    invoke-virtual {v7, v2}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :cond_7
    iget-object v8, v0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    const/4 v14, 0x1

    invoke-virtual {v8, v6, v14, v7}, Lcom/android/server/wm/RootWindowContainer;->dumpWindowsNoHeader(Ljava/io/PrintWriter;ZLjava/util/ArrayList;)V

    invoke-virtual {v6}, Ljava/io/PrintWriter;->println()V

    invoke-virtual {v6}, Ljava/io/PrintWriter;->close()V

    invoke-virtual {v5}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v8

    iput-object v8, v0, Lcom/android/server/wm/WindowManagerService;->mLastANRState:Ljava/lang/String;

    iget-object v8, v0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    const/16 v9, 0x26

    invoke-virtual {v8, v9}, Lcom/android/server/wm/WindowManagerService$H;->removeMessages(I)V

    iget-object v8, v0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    const-wide/32 v10, 0x6ddd00

    invoke-virtual {v8, v9, v10, v11}, Lcom/android/server/wm/WindowManagerService$H;->sendEmptyMessageDelayed(IJ)Z

    invoke-static {v4}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    return-void

    :catchall_0
    move-exception v0

    invoke-static {v4}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw v0
.end method
""",
        "replacement": """\
.method saveANRStateLocked(Lcom/android/server/wm/ActivityRecord;Lcom/android/server/wm/WindowState;Ljava/lang/String;)V
    .registers 20

    goto :goto_2

    nop

    :goto_0
    return-void

    :catchall_0
    move-exception v0

    goto :goto_3

    nop

    :goto_1
    const-string v15, " since null focus: "

    goto :goto_8

    nop

    :goto_2
    move-object/from16 v0, p0

    goto :goto_c

    nop

    :goto_3
    invoke-static {v4}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_a

    nop

    :goto_4
    const-string v4, "com.android.server.wm.WindowManagerService.saveANRStateLocked(Lcom/android/server/wm/ActivityRecord;Lcom/android/server/wm/WindowState;Ljava/lang/String;)V"

    goto :goto_5

    nop

    :goto_5
    invoke-static {v4}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    new-instance v5, Ljava/io/StringWriter;

    invoke-direct {v5}, Ljava/io/StringWriter;-><init>()V

    new-instance v6, Lcom/android/internal/util/FastPrintWriter;

    const/4 v7, 0x0

    const/16 v8, 0x400

    invoke-direct {v6, v5, v7, v8}, Lcom/android/internal/util/FastPrintWriter;-><init>(Ljava/io/Writer;ZI)V

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "  ANR time: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-static {}, Ljava/text/DateFormat;->getDateTimeInstance()Ljava/text/DateFormat;

    move-result-object v8

    new-instance v9, Ljava/util/Date;

    invoke-direct {v9}, Ljava/util/Date;-><init>()V

    invoke-virtual {v8, v9}, Ljava/text/DateFormat;->format(Ljava/util/Date;)Ljava/lang/String;

    move-result-object v8

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    if-eqz v1, :cond_0

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "  Application at fault: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v1, Lcom/android/server/wm/ActivityRecord;->stringName:Ljava/lang/String;

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_0
    if-eqz v2, :cond_1

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "  Window at fault: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v2, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v8}, Landroid/view/WindowManager$LayoutParams;->getTitle()Ljava/lang/CharSequence;

    move-result-object v8

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_1
    if-eqz v3, :cond_2

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "  Reason: "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v6, v7}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_2
    invoke-virtual {v6}, Ljava/io/PrintWriter;->println()V

    new-instance v7, Ljava/util/ArrayList;

    invoke-direct {v7}, Ljava/util/ArrayList;-><init>()V

    iget-object v8, v0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v8}, Lcom/android/server/wm/RootWindowContainer;->getChildCount()I

    move-result v8

    const/4 v9, 0x1

    sub-int/2addr v8, v9

    :goto_6
    if-ltz v8, :cond_6

    iget-object v10, v0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v10, v8}, Lcom/android/server/wm/RootWindowContainer;->getChildAt(I)Lcom/android/server/wm/WindowContainer;

    move-result-object v10

    check-cast v10, Lcom/android/server/wm/DisplayContent;

    invoke-virtual {v10}, Lcom/android/server/wm/DisplayContent;->getDisplayId()I

    move-result v11

    iget-object v12, v10, Lcom/android/server/wm/DisplayContent;->mCurrentFocus:Lcom/android/server/wm/WindowState;

    iget-object v13, v10, Lcom/android/server/wm/DisplayContent;->mFocusedApp:Lcom/android/server/wm/ActivityRecord;

    new-instance v14, Ljava/lang/StringBuilder;

    invoke-direct {v14}, Ljava/lang/StringBuilder;-><init>()V

    const-string v15, "  Display #"

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v14, v11}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v14

    const-string v15, " currentFocus="

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v14, v12}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v14

    const-string v15, " focusedApp="

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v14, v13}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v14}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v14

    invoke-virtual {v6, v14}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    if-eqz v12, :cond_3

    new-instance v14, Ljava/lang/StringBuilder;

    invoke-direct {v14}, Ljava/lang/StringBuilder;-><init>()V

    const-string v15, "  focus surface relativeTo:"

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v12}, Lcom/android/server/wm/WindowState;->getLastRelativeLayer()Landroid/view/SurfaceControl;

    move-result-object v15

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v14

    const-string v15, " reparent to:"

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v12}, Lcom/android/server/wm/WindowState;->getParentSurfaceControl()Landroid/view/SurfaceControl;

    move-result-object v15

    invoke-virtual {v14, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v14

    invoke-virtual {v14}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v14

    invoke-virtual {v6, v14}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_3
    iget-object v14, v10, Lcom/android/server/wm/DisplayContent;->mWinAddedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v14}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v14
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop

    :goto_7
    move-object/from16 v3, p3

    goto :goto_4

    nop

    :goto_8
    if-eqz v14, :cond_4

    goto :goto_9

    :cond_4
    :try_start_1
    new-instance v14, Ljava/lang/StringBuilder;

    invoke-direct {v14}, Ljava/lang/StringBuilder;-><init>()V

    const-string v9, "  Windows added in display #"

    invoke-virtual {v14, v9}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9, v11}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    iget-object v14, v10, Lcom/android/server/wm/DisplayContent;->mWinAddedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v9, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v6, v9}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :goto_9
    iget-object v9, v10, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v9}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v9

    if-nez v9, :cond_5

    new-instance v9, Ljava/lang/StringBuilder;

    invoke-direct {v9}, Ljava/lang/StringBuilder;-><init>()V

    const-string v14, "  Windows removed in display #"

    invoke-virtual {v9, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9, v11}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9, v15}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v9

    iget-object v14, v10, Lcom/android/server/wm/DisplayContent;->mWinRemovedSinceNullFocus:Ljava/util/ArrayList;

    invoke-virtual {v9, v14}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v9

    invoke-virtual {v9}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v9

    invoke-virtual {v6, v9}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    :cond_5
    const-string v9, "  Tasks in top down Z order:"

    invoke-virtual {v6, v9}, Ljava/io/PrintWriter;->println(Ljava/lang/String;)V

    new-instance v9, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda31;

    invoke-direct {v9, v6}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda31;-><init>(Ljava/io/PrintWriter;)V

    invoke-virtual {v10, v9}, Lcom/android/server/wm/DisplayContent;->forAllTaskDisplayAreas(Ljava/util/function/Consumer;)V

    invoke-virtual {v10}, Lcom/android/server/wm/DisplayContent;->getInputMonitor()Lcom/android/server/wm/InputMonitor;

    move-result-object v9

    const-string v14, "  "

    invoke-virtual {v9, v6, v14}, Lcom/android/server/wm/InputMonitor;->dump(Ljava/io/PrintWriter;Ljava/lang/String;)V

    invoke-virtual {v6}, Ljava/io/PrintWriter;->println()V

    new-instance v9, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda32;

    invoke-direct {v9, v12, v13, v7}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda32;-><init>(Lcom/android/server/wm/WindowState;Lcom/android/server/wm/ActivityRecord;Ljava/util/ArrayList;)V

    const/4 v14, 0x1

    invoke-virtual {v10, v9, v14}, Lcom/android/server/wm/DisplayContent;->forAllWindows(Ljava/util/function/Consumer;Z)V

    add-int/lit8 v8, v8, -0x1

    const/4 v9, 0x1

    goto :goto_6

    :cond_6
    if-eqz v2, :cond_7

    invoke-virtual {v7, v2}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v8

    if-nez v8, :cond_7

    invoke-virtual {v7, v2}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    :cond_7
    iget-object v8, v0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    const/4 v14, 0x1

    invoke-virtual {v8, v6, v14, v7}, Lcom/android/server/wm/RootWindowContainer;->dumpWindowsNoHeader(Ljava/io/PrintWriter;ZLjava/util/ArrayList;)V

    invoke-virtual {v6}, Ljava/io/PrintWriter;->println()V

    invoke-virtual {v6}, Ljava/io/PrintWriter;->close()V

    invoke-virtual {v5}, Ljava/lang/Object;->toString()Ljava/lang/String;

    move-result-object v8

    iput-object v8, v0, Lcom/android/server/wm/WindowManagerService;->mLastANRState:Ljava/lang/String;

    iget-object v8, v0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    const/16 v9, 0x26

    invoke-virtual {v8, v9}, Lcom/android/server/wm/WindowManagerService$H;->removeMessages(I)V

    iget-object v8, v0, Lcom/android/server/wm/WindowManagerService;->mH:Lcom/android/server/wm/WindowManagerService$H;

    const-wide/32 v10, 0x6ddd00

    invoke-virtual {v8, v9, v10, v11}, Lcom/android/server/wm/WindowManagerService$H;->sendEmptyMessageDelayed(IJ)Z

    invoke-static {v4}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_0

    nop

    :goto_a
    throw v0

    :goto_b
    move-object/from16 v2, p2

    goto :goto_7

    nop

    :goto_c
    move-object/from16 v1, p1

    goto :goto_b

    nop
.end method
""",
        "method_anchors": ['const-string v4, "com.android.server.wm.WindowManagerService.saveANRStateLocked(Lcom/android/server/wm/ActivityRecord;Lcom/android/server/wm/WindowState;Ljava/lang/String;)V"', 'invoke-static {v4}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'new-instance v5, Ljava/io/StringWriter;', 'invoke-direct {v5}, Ljava/io/StringWriter;-><init>()V', 'new-instance v6, Lcom/android/internal/util/FastPrintWriter;', 'invoke-direct {v6, v5, v7, v8}, Lcom/android/internal/util/FastPrintWriter;-><init>(Ljava/io/Writer;ZI)V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_scheduleAnimationLocked__V",
        "method":      ".method scheduleAnimationLocked()V",
        "method_name": 'scheduleAnimationLocked',
        "type":        "method_replace",
        "search": """\
.method scheduleAnimationLocked()V
    .registers 3

    const-string v0, "com.android.server.wm.WindowManagerService.scheduleAnimationLocked()V"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mAnimator:Lcom/android/server/wm/WindowAnimator;

    invoke-virtual {v1}, Lcom/android/server/wm/WindowAnimator;->scheduleAnimation()V

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-void

    :catchall_0
    move-exception v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw v1
.end method
""",
        "replacement": """\
.method scheduleAnimationLocked()V
    .registers 3

    goto :goto_3

    nop

    :goto_0
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_2

    nop

    :goto_1
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mAnimator:Lcom/android/server/wm/WindowAnimator;

    invoke-virtual {v1}, Lcom/android/server/wm/WindowAnimator;->scheduleAnimation()V

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_4

    nop

    :goto_2
    throw v1

    :goto_3
    const-string v0, "com.android.server.wm.WindowManagerService.scheduleAnimationLocked()V"

    goto :goto_1

    nop

    :goto_4
    return-void

    :catchall_0
    move-exception v1

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.scheduleAnimationLocked()V"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mAnimator:Lcom/android/server/wm/WindowAnimator;', 'invoke-virtual {v1}, Lcom/android/server/wm/WindowAnimator;->scheduleAnimation()V', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V', 'return-void'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setForceDesktopModeOnExternalDisplays_Z_V",
        "method":      ".method setForceDesktopModeOnExternalDisplays(Z)V",
        "method_name": 'setForceDesktopModeOnExternalDisplays',
        "type":        "method_replace",
        "search": """\
.method setForceDesktopModeOnExternalDisplays(Z)V
    .registers 4

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iput-boolean p1, p0, Lcom/android/server/wm/WindowManagerService;->mForceDesktopModeOnExternalDisplays:Z

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->updateDisplayImePolicyCache()V

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method setForceDesktopModeOnExternalDisplays(Z)V
    .registers 4

    goto :goto_1

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_2

    nop

    :goto_1
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_4

    nop

    :goto_2
    throw v1

    :goto_3
    monitor-enter v0

    :try_start_0
    iput-boolean p1, p0, Lcom/android/server/wm/WindowManagerService;->mForceDesktopModeOnExternalDisplays:Z

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->updateDisplayImePolicyCache()V

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_5

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_3

    nop

    :goto_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_6

    nop

    :goto_6
    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iput-boolean p1, p0, Lcom/android/server/wm/WindowManagerService;->mForceDesktopModeOnExternalDisplays:Z', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;', 'invoke-virtual {v1}, Lcom/android/server/wm/RootWindowContainer;->updateDisplayImePolicyCache()V', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setInsetsWindow_Lcom_android_server_wm_Session_Landroid_view",
        "method":      ".method setInsetsWindow(Lcom/android/server/wm/Session;Landroid/view/IWindow;ILandroid/graphics/Rect;Landroid/graphics/Rect;Landroid/graphics/Region;)V",
        "method_name": 'setInsetsWindow',
        "type":        "method_replace",
        "search": """\
.method setInsetsWindow(Lcom/android/server/wm/Session;Landroid/view/IWindow;ILandroid/graphics/Rect;Landroid/graphics/Rect;Landroid/graphics/Region;)V
    .registers 16

    invoke-static {}, Landroid/os/Binder;->getCallingUid()I

    move-result v0

    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v1

    :try_start_0
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v3
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    const/4 v4, 0x0

    :try_start_1
    invoke-virtual {p0, p1, p2, v4}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v5

    sget-boolean v6, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG_LAYOUT:Z

    if-eqz v6, :cond_0

    const-string v6, "WindowManager"

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "setInsetsWindow "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, ", contentInsets="

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v5, Lcom/android/server/wm/WindowState;->mGivenContentInsets:Landroid/graphics/Rect;

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, " -> "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, p4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, ", visibleInsets="

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v5, Lcom/android/server/wm/WindowState;->mGivenVisibleInsets:Landroid/graphics/Rect;

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, " -> "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, p5}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, ", touchableRegion="

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v5, Lcom/android/server/wm/WindowState;->mGivenTouchableRegion:Landroid/graphics/Region;

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, " -> "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, p6}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, ", touchableInsets "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget v8, v5, Lcom/android/server/wm/WindowState;->mTouchableInsets:I

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, " -> "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, p3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-static {v6, v7}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_0
    if-eqz v5, :cond_4

    iget-boolean v6, v5, Lcom/android/server/wm/WindowState;->mGivenInsetsPending:Z

    iput-boolean v4, v5, Lcom/android/server/wm/WindowState;->mGivenInsetsPending:Z

    if-eqz v6, :cond_1

    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->hasInsetsSourceProvider()Z

    move-result v4

    if-nez v4, :cond_2

    :cond_1
    iget v4, v5, Lcom/android/server/wm/WindowState;->mTouchableInsets:I

    if-ne v4, p3, :cond_2

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenContentInsets:Landroid/graphics/Rect;

    invoke-virtual {v4, p4}, Landroid/graphics/Rect;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_2

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenVisibleInsets:Landroid/graphics/Rect;

    invoke-virtual {v4, p5}, Landroid/graphics/Rect;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_2

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenTouchableRegion:Landroid/graphics/Region;

    invoke-virtual {v4, p6}, Landroid/graphics/Region;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_2

    monitor-exit v3
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    invoke-static {v1, v2}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    return-void

    :cond_2
    :try_start_2
    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenContentInsets:Landroid/graphics/Rect;

    invoke-virtual {v4, p4}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenVisibleInsets:Landroid/graphics/Rect;

    invoke-virtual {v4, p5}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenTouchableRegion:Landroid/graphics/Region;

    invoke-virtual {v4, p6}, Landroid/graphics/Region;->set(Landroid/graphics/Region;)Z

    iput p3, v5, Lcom/android/server/wm/WindowState;->mTouchableInsets:I

    iget v4, v5, Lcom/android/server/wm/WindowState;->mGlobalScale:F

    const/high16 v7, 0x3f800000

    cmpl-float v4, v4, v7

    if-eqz v4, :cond_3

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenContentInsets:Landroid/graphics/Rect;

    iget v7, v5, Lcom/android/server/wm/WindowState;->mGlobalScale:F

    invoke-virtual {v4, v7}, Landroid/graphics/Rect;->scale(F)V

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenVisibleInsets:Landroid/graphics/Rect;

    iget v7, v5, Lcom/android/server/wm/WindowState;->mGlobalScale:F

    invoke-virtual {v4, v7}, Landroid/graphics/Rect;->scale(F)V

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenTouchableRegion:Landroid/graphics/Region;

    iget v7, v5, Lcom/android/server/wm/WindowState;->mGlobalScale:F

    invoke-virtual {v4, v7}, Landroid/graphics/Region;->scale(F)V

    :cond_3
    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->setDisplayLayoutNeeded()V

    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->getFrame()Landroid/graphics/Rect;

    move-result-object v4

    invoke-virtual {v5, v4}, Lcom/android/server/wm/WindowState;->updateSourceFrame(Landroid/graphics/Rect;)V

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;

    invoke-virtual {v4}, Lcom/android/server/wm/WindowSurfacePlacer;->performSurfacePlacement()V

    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v4

    invoke-virtual {v4}, Lcom/android/server/wm/DisplayContent;->getInputMonitor()Lcom/android/server/wm/InputMonitor;

    move-result-object v4

    const/4 v7, 0x1

    invoke-virtual {v4, v7}, Lcom/android/server/wm/InputMonitor;->updateInputWindowsLw(Z)V

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mAccessibilityController:Lcom/android/server/wm/AccessibilityController;

    invoke-virtual {v4}, Lcom/android/server/wm/AccessibilityController;->hasCallbacks()Z

    move-result v4

    if-eqz v4, :cond_4

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mAccessibilityController:Lcom/android/server/wm/AccessibilityController;

    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v7

    invoke-virtual {v7}, Lcom/android/server/wm/DisplayContent;->getDisplayId()I

    move-result v7

    filled-new-array {v7}, [I

    move-result-object v7

    invoke-virtual {v4, v0, v7}, Lcom/android/server/wm/AccessibilityController;->onSomeWindowResizedOrMovedWithCallingUid(I[I)V

    :cond_4
    monitor-exit v3
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    :try_start_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_1

    invoke-static {v1, v2}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    nop

    return-void

    :catchall_0
    move-exception v4

    :try_start_4
    monitor-exit v3
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    :try_start_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v4
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_1

    :catchall_1
    move-exception v3

    invoke-static {v1, v2}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    throw v3
.end method
""",
        "replacement": """\
.method setInsetsWindow(Lcom/android/server/wm/Session;Landroid/view/IWindow;ILandroid/graphics/Rect;Landroid/graphics/Rect;Landroid/graphics/Region;)V
    .registers 16

    goto :goto_5

    nop

    :goto_0
    invoke-static {v1, v2}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    goto :goto_7

    nop

    :goto_1
    invoke-static {v1, v2}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    goto :goto_6

    nop

    :goto_2
    return-void

    :catchall_0
    move-exception v4

    :try_start_0
    monitor-exit v3
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :try_start_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v4
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    :catchall_1
    move-exception v3

    goto :goto_0

    nop

    :goto_3
    invoke-static {v1, v2}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    nop

    goto :goto_2

    nop

    :goto_4
    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v1

    :try_start_2
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v3
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    goto :goto_9

    nop

    :goto_5
    invoke-static {}, Landroid/os/Binder;->getCallingUid()I

    move-result v0

    goto :goto_4

    nop

    :goto_6
    return-void

    :cond_0
    :try_start_3
    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenContentInsets:Landroid/graphics/Rect;

    invoke-virtual {v4, p4}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenVisibleInsets:Landroid/graphics/Rect;

    invoke-virtual {v4, p5}, Landroid/graphics/Rect;->set(Landroid/graphics/Rect;)V

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenTouchableRegion:Landroid/graphics/Region;

    invoke-virtual {v4, p6}, Landroid/graphics/Region;->set(Landroid/graphics/Region;)Z

    iput p3, v5, Lcom/android/server/wm/WindowState;->mTouchableInsets:I

    iget v4, v5, Lcom/android/server/wm/WindowState;->mGlobalScale:F

    const/high16 v7, 0x3f800000

    cmpl-float v4, v4, v7

    if-eqz v4, :cond_1

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenContentInsets:Landroid/graphics/Rect;

    iget v7, v5, Lcom/android/server/wm/WindowState;->mGlobalScale:F

    invoke-virtual {v4, v7}, Landroid/graphics/Rect;->scale(F)V

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenVisibleInsets:Landroid/graphics/Rect;

    iget v7, v5, Lcom/android/server/wm/WindowState;->mGlobalScale:F

    invoke-virtual {v4, v7}, Landroid/graphics/Rect;->scale(F)V

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenTouchableRegion:Landroid/graphics/Region;

    iget v7, v5, Lcom/android/server/wm/WindowState;->mGlobalScale:F

    invoke-virtual {v4, v7}, Landroid/graphics/Region;->scale(F)V

    :cond_1
    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->setDisplayLayoutNeeded()V

    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->getFrame()Landroid/graphics/Rect;

    move-result-object v4

    invoke-virtual {v5, v4}, Lcom/android/server/wm/WindowState;->updateSourceFrame(Landroid/graphics/Rect;)V

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mWindowPlacerLocked:Lcom/android/server/wm/WindowSurfacePlacer;

    invoke-virtual {v4}, Lcom/android/server/wm/WindowSurfacePlacer;->performSurfacePlacement()V

    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v4

    invoke-virtual {v4}, Lcom/android/server/wm/DisplayContent;->getInputMonitor()Lcom/android/server/wm/InputMonitor;

    move-result-object v4

    const/4 v7, 0x1

    invoke-virtual {v4, v7}, Lcom/android/server/wm/InputMonitor;->updateInputWindowsLw(Z)V

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mAccessibilityController:Lcom/android/server/wm/AccessibilityController;

    invoke-virtual {v4}, Lcom/android/server/wm/AccessibilityController;->hasCallbacks()Z

    move-result v4

    if-eqz v4, :cond_2

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mAccessibilityController:Lcom/android/server/wm/AccessibilityController;

    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->getDisplayContent()Lcom/android/server/wm/DisplayContent;

    move-result-object v7

    invoke-virtual {v7}, Lcom/android/server/wm/DisplayContent;->getDisplayId()I

    move-result v7

    filled-new-array {v7}, [I

    move-result-object v7

    invoke-virtual {v4, v0, v7}, Lcom/android/server/wm/AccessibilityController;->onSomeWindowResizedOrMovedWithCallingUid(I[I)V

    :cond_2
    monitor-exit v3
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_1

    goto :goto_3

    nop

    :goto_7
    throw v3

    :goto_8
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_1

    nop

    :goto_9
    const/4 v4, 0x0

    :try_start_5
    invoke-virtual {p0, p1, p2, v4}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v5

    sget-boolean v6, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG_LAYOUT:Z

    if-eqz v6, :cond_3

    const-string v6, "WindowManager"

    new-instance v7, Ljava/lang/StringBuilder;

    invoke-direct {v7}, Ljava/lang/StringBuilder;-><init>()V

    const-string v8, "setInsetsWindow "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, ", contentInsets="

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v5, Lcom/android/server/wm/WindowState;->mGivenContentInsets:Landroid/graphics/Rect;

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, " -> "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, p4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, ", visibleInsets="

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v5, Lcom/android/server/wm/WindowState;->mGivenVisibleInsets:Landroid/graphics/Rect;

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, " -> "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, p5}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, ", touchableRegion="

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget-object v8, v5, Lcom/android/server/wm/WindowState;->mGivenTouchableRegion:Landroid/graphics/Region;

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, " -> "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, p6}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, ", touchableInsets "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    iget v8, v5, Lcom/android/server/wm/WindowState;->mTouchableInsets:I

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v7

    const-string v8, " -> "

    invoke-virtual {v7, v8}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7, p3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v7

    invoke-virtual {v7}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-static {v6, v7}, Landroid/util/Slog;->d(Ljava/lang/String;Ljava/lang/String;)I

    :cond_3
    if-eqz v5, :cond_2

    iget-boolean v6, v5, Lcom/android/server/wm/WindowState;->mGivenInsetsPending:Z

    iput-boolean v4, v5, Lcom/android/server/wm/WindowState;->mGivenInsetsPending:Z

    if-eqz v6, :cond_4

    invoke-virtual {v5}, Lcom/android/server/wm/WindowState;->hasInsetsSourceProvider()Z

    move-result v4

    if-nez v4, :cond_0

    :cond_4
    iget v4, v5, Lcom/android/server/wm/WindowState;->mTouchableInsets:I

    if-ne v4, p3, :cond_0

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenContentInsets:Landroid/graphics/Rect;

    invoke-virtual {v4, p4}, Landroid/graphics/Rect;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_0

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenVisibleInsets:Landroid/graphics/Rect;

    invoke-virtual {v4, p5}, Landroid/graphics/Rect;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_0

    iget-object v4, v5, Lcom/android/server/wm/WindowState;->mGivenTouchableRegion:Landroid/graphics/Region;

    invoke-virtual {v4, p6}, Landroid/graphics/Region;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_0

    monitor-exit v3
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_0

    goto :goto_8

    nop
.end method
""",
        "method_anchors": ['invoke-static {}, Landroid/os/Binder;->getCallingUid()I', 'move-result v0', 'invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J', 'move-result-wide v1', 'iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setIsPc_Z_V",
        "method":      ".method setIsPc(Z)V",
        "method_name": 'setIsPc',
        "type":        "method_replace",
        "search": """\
.method setIsPc(Z)V
    .registers 4

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iput-boolean p1, p0, Lcom/android/server/wm/WindowManagerService;->mIsPc:Z

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_1
    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method setIsPc(Z)V
    .registers 4

    goto :goto_5

    nop

    :goto_0
    return-void

    :catchall_0
    move-exception v1

    :try_start_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop

    :goto_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_2

    nop

    :goto_2
    throw v1

    :goto_3
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_4

    nop

    :goto_4
    monitor-enter v0

    :try_start_1
    iput-boolean p1, p0, Lcom/android/server/wm/WindowManagerService;->mIsPc:Z

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_6

    nop

    :goto_5
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_3

    nop

    :goto_6
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iput-boolean p1, p0, Lcom/android/server/wm/WindowManagerService;->mIsPc:Z', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V', 'return-void', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setOrientationRequestPolicy_Z_I_I_V",
        "method":      ".method setOrientationRequestPolicy(Z[I[I)V",
        "method_name": 'setOrientationRequestPolicy',
        "type":        "method_replace",
        "search": """\
.method setOrientationRequestPolicy(Z[I[I)V
    .registers 8

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mOrientationMapping:Landroid/util/SparseIntArray;

    invoke-virtual {v0}, Landroid/util/SparseIntArray;->clear()V

    if-eqz p2, :cond_0

    if-eqz p3, :cond_0

    array-length v0, p2

    array-length v1, p3

    if-ne v0, v1, :cond_0

    const/4 v0, 0x0

    :goto_0
    array-length v1, p2

    if-ge v0, v1, :cond_0

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mOrientationMapping:Landroid/util/SparseIntArray;

    aget v2, p2, v0

    aget v3, p3, v0

    invoke-virtual {v1, v2, v3}, Landroid/util/SparseIntArray;->put(II)V

    add-int/lit8 v0, v0, 0x1

    goto :goto_0

    :cond_0
    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mIsIgnoreOrientationRequestDisabled:Z

    if-ne p1, v0, :cond_1

    return-void

    :cond_1
    iput-boolean p1, p0, Lcom/android/server/wm/WindowManagerService;->mIsIgnoreOrientationRequestDisabled:Z

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v0}, Lcom/android/server/wm/RootWindowContainer;->getChildCount()I

    move-result v0

    add-int/lit8 v0, v0, -0x1

    :goto_1
    if-ltz v0, :cond_2

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, v0}, Lcom/android/server/wm/RootWindowContainer;->getChildAt(I)Lcom/android/server/wm/WindowContainer;

    move-result-object v1

    check-cast v1, Lcom/android/server/wm/DisplayContent;

    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->onIsIgnoreOrientationRequestDisabledChanged()V

    add-int/lit8 v0, v0, -0x1

    goto :goto_1

    :cond_2
    return-void
.end method
""",
        "replacement": """\
.method setOrientationRequestPolicy(Z[I[I)V
    .registers 8

    goto :goto_3

    nop

    :goto_0
    array-length v1, p2

    goto :goto_16

    nop

    :goto_1
    goto :goto_22

    :goto_2
    goto :goto_e

    nop

    :goto_3
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mOrientationMapping:Landroid/util/SparseIntArray;

    goto :goto_b

    nop

    :goto_4
    invoke-virtual {v1}, Lcom/android/server/wm/DisplayContent;->onIsIgnoreOrientationRequestDisabledChanged()V

    goto :goto_6

    nop

    :goto_5
    invoke-virtual {v1, v2, v3}, Landroid/util/SparseIntArray;->put(II)V

    goto :goto_a

    nop

    :goto_6
    add-int/lit8 v0, v0, -0x1

    goto :goto_1a

    nop

    :goto_7
    aget v3, p3, v0

    goto :goto_5

    nop

    :goto_8
    iput-boolean p1, p0, Lcom/android/server/wm/WindowManagerService;->mIsIgnoreOrientationRequestDisabled:Z

    goto :goto_c

    nop

    :goto_9
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    goto :goto_1e

    nop

    :goto_a
    add-int/lit8 v0, v0, 0x1

    goto :goto_1

    nop

    :goto_b
    invoke-virtual {v0}, Landroid/util/SparseIntArray;->clear()V

    goto :goto_1c

    nop

    :goto_c
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    goto :goto_19

    nop

    :goto_d
    if-eq v0, v1, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_21

    nop

    :goto_e
    iget-boolean v0, p0, Lcom/android/server/wm/WindowManagerService;->mIsIgnoreOrientationRequestDisabled:Z

    goto :goto_17

    nop

    :goto_f
    array-length v1, p3

    goto :goto_d

    nop

    :goto_10
    return-void

    :goto_11
    goto :goto_8

    nop

    :goto_12
    array-length v0, p2

    goto :goto_f

    nop

    :goto_13
    if-gez v0, :cond_1

    goto :goto_1b

    :cond_1
    goto :goto_9

    nop

    :goto_14
    if-nez p3, :cond_2

    goto :goto_2

    :cond_2
    goto :goto_12

    nop

    :goto_15
    check-cast v1, Lcom/android/server/wm/DisplayContent;

    goto :goto_4

    nop

    :goto_16
    if-lt v0, v1, :cond_3

    goto :goto_2

    :cond_3
    goto :goto_23

    nop

    :goto_17
    if-eq p1, v0, :cond_4

    goto :goto_11

    :cond_4
    goto :goto_10

    nop

    :goto_18
    return-void

    :goto_19
    invoke-virtual {v0}, Lcom/android/server/wm/RootWindowContainer;->getChildCount()I

    move-result v0

    goto :goto_1f

    nop

    :goto_1a
    goto :goto_20

    :goto_1b
    goto :goto_18

    nop

    :goto_1c
    if-nez p2, :cond_5

    goto :goto_2

    :cond_5
    goto :goto_14

    nop

    :goto_1d
    aget v2, p2, v0

    goto :goto_7

    nop

    :goto_1e
    invoke-virtual {v1, v0}, Lcom/android/server/wm/RootWindowContainer;->getChildAt(I)Lcom/android/server/wm/WindowContainer;

    move-result-object v1

    goto :goto_15

    nop

    :goto_1f
    add-int/lit8 v0, v0, -0x1

    :goto_20
    goto :goto_13

    nop

    :goto_21
    const/4 v0, 0x0

    :goto_22
    goto :goto_0

    nop

    :goto_23
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mOrientationMapping:Landroid/util/SparseIntArray;

    goto :goto_1d

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mOrientationMapping:Landroid/util/SparseIntArray;', 'invoke-virtual {v0}, Landroid/util/SparseIntArray;->clear()V', 'if-eqz p2, :cond_0', 'if-eqz p3, :cond_0', 'if-ne v0, v1, :cond_0', 'if-ge v0, v1, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setOverrideFoldedArea_Landroid_graphics_Rect__V",
        "method":      ".method setOverrideFoldedArea(Landroid/graphics/Rect;)V",
        "method_name": 'setOverrideFoldedArea',
        "type":        "method_replace",
        "search": """\
.method setOverrideFoldedArea(Landroid/graphics/Rect;)V
    .registers 6

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mContext:Landroid/content/Context;

    const-string v1, "android.permission.WRITE_SECURE_SETTINGS"

    invoke-virtual {v0, v1}, Landroid/content/Context;->checkCallingOrSelfPermission(Ljava/lang/String;)I

    move-result v0

    if-nez v0, :cond_0

    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v0

    :try_start_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    :try_start_1
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mPolicy:Lcom/android/server/policy/WindowManagerPolicy;

    invoke-interface {v3, p1}, Lcom/android/server/policy/WindowManagerPolicy;->setOverrideFoldedArea(Landroid/graphics/Rect;)V

    monitor-exit v2
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :try_start_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    nop

    return-void

    :catchall_0
    move-exception v3

    :try_start_3
    monitor-exit v2
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v3
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_1

    :catchall_1
    move-exception v2

    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    throw v2

    :cond_0
    new-instance v0, Ljava/lang/SecurityException;

    const-string v1, "Must hold permission android.permission.WRITE_SECURE_SETTINGS"

    invoke-direct {v0, v1}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    throw v0
.end method
""",
        "replacement": """\
.method setOverrideFoldedArea(Landroid/graphics/Rect;)V
    .registers 6

    goto :goto_9

    nop

    :goto_0
    invoke-virtual {v0, v1}, Landroid/content/Context;->checkCallingOrSelfPermission(Ljava/lang/String;)I

    move-result v0

    goto :goto_b

    nop

    :goto_1
    new-instance v0, Ljava/lang/SecurityException;

    goto :goto_8

    nop

    :goto_2
    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v0

    :try_start_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    :try_start_1
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mPolicy:Lcom/android/server/policy/WindowManagerPolicy;

    invoke-interface {v3, p1}, Lcom/android/server/policy/WindowManagerPolicy;->setOverrideFoldedArea(Landroid/graphics/Rect;)V

    monitor-exit v2
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :try_start_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    goto :goto_5

    nop

    :goto_3
    throw v2

    :goto_4
    goto :goto_1

    nop

    :goto_5
    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    nop

    goto :goto_a

    nop

    :goto_6
    const-string v1, "android.permission.WRITE_SECURE_SETTINGS"

    goto :goto_0

    nop

    :goto_7
    throw v0

    :goto_8
    const-string v1, "Must hold permission android.permission.WRITE_SECURE_SETTINGS"

    goto :goto_c

    nop

    :goto_9
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mContext:Landroid/content/Context;

    goto :goto_6

    nop

    :goto_a
    return-void

    :catchall_0
    move-exception v3

    :try_start_3
    monitor-exit v2
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v3
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_1

    :catchall_1
    move-exception v2

    goto :goto_d

    nop

    :goto_b
    if-eqz v0, :cond_0

    goto :goto_4

    :cond_0
    goto :goto_2

    nop

    :goto_c
    invoke-direct {v0, v1}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    goto :goto_7

    nop

    :goto_d
    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    goto :goto_3

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mContext:Landroid/content/Context;', 'const-string v1, "android.permission.WRITE_SECURE_SETTINGS"', 'invoke-virtual {v0, v1}, Landroid/content/Context;->checkCallingOrSelfPermission(Ljava/lang/String;)I', 'move-result v0', 'if-nez v0, :cond_0', 'invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_setSandboxDisplayApis_IZ_V",
        "method":      ".method setSandboxDisplayApis(IZ)V",
        "method_name": 'setSandboxDisplayApis',
        "type":        "method_replace",
        "search": """\
.method setSandboxDisplayApis(IZ)V
    .registers 7

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mContext:Landroid/content/Context;

    const-string v1, "android.permission.WRITE_SECURE_SETTINGS"

    invoke-virtual {v0, v1}, Landroid/content/Context;->checkCallingOrSelfPermission(Ljava/lang/String;)I

    move-result v0

    if-nez v0, :cond_1

    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v0

    :try_start_0
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    :try_start_1
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v3, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v3

    if-eqz v3, :cond_0

    invoke-virtual {v3, p2}, Lcom/android/server/wm/DisplayContent;->setSandboxDisplayApis(Z)V

    :cond_0
    monitor-exit v2
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :try_start_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    nop

    return-void

    :catchall_0
    move-exception v3

    :try_start_3
    monitor-exit v2
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v3
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_1

    :catchall_1
    move-exception v2

    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    throw v2

    :cond_1
    new-instance v0, Ljava/lang/SecurityException;

    const-string v1, "Must hold permission android.permission.WRITE_SECURE_SETTINGS"

    invoke-direct {v0, v1}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    throw v0
.end method
""",
        "replacement": """\
.method setSandboxDisplayApis(IZ)V
    .registers 7

    goto :goto_0

    nop

    :goto_0
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mContext:Landroid/content/Context;

    goto :goto_4

    nop

    :goto_1
    throw v2

    :goto_2
    goto :goto_c

    nop

    :goto_3
    const-string v1, "Must hold permission android.permission.WRITE_SECURE_SETTINGS"

    goto :goto_a

    nop

    :goto_4
    const-string v1, "android.permission.WRITE_SECURE_SETTINGS"

    goto :goto_6

    nop

    :goto_5
    return-void

    :catchall_0
    move-exception v3

    :try_start_0
    monitor-exit v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :try_start_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v3
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_1

    :catchall_1
    move-exception v2

    goto :goto_b

    nop

    :goto_6
    invoke-virtual {v0, v1}, Landroid/content/Context;->checkCallingOrSelfPermission(Ljava/lang/String;)I

    move-result v0

    goto :goto_8

    nop

    :goto_7
    throw v0

    :goto_8
    if-eqz v0, :cond_0

    goto :goto_2

    :cond_0
    goto :goto_9

    nop

    :goto_9
    invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J

    move-result-wide v0

    :try_start_2
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_1

    :try_start_3
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v3, p1}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v3

    if-eqz v3, :cond_1

    invoke-virtual {v3, p2}, Lcom/android/server/wm/DisplayContent;->setSandboxDisplayApis(Z)V

    :cond_1
    monitor-exit v2
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    :try_start_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_1

    goto :goto_d

    nop

    :goto_a
    invoke-direct {v0, v1}, Ljava/lang/SecurityException;-><init>(Ljava/lang/String;)V

    goto :goto_7

    nop

    :goto_b
    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    goto :goto_1

    nop

    :goto_c
    new-instance v0, Ljava/lang/SecurityException;

    goto :goto_3

    nop

    :goto_d
    invoke-static {v0, v1}, Landroid/os/Binder;->restoreCallingIdentity(J)V

    nop

    goto :goto_5

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mContext:Landroid/content/Context;', 'const-string v1, "android.permission.WRITE_SECURE_SETTINGS"', 'invoke-virtual {v0, v1}, Landroid/content/Context;->checkCallingOrSelfPermission(Ljava/lang/String;)I', 'move-result v0', 'if-nez v0, :cond_1', 'invoke-static {}, Landroid/os/Binder;->clearCallingIdentity()J'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_shouldPlacePrimaryHomeOnDisplay_I_Z",
        "method":      ".method shouldPlacePrimaryHomeOnDisplay(I)Z",
        "method_name": 'shouldPlacePrimaryHomeOnDisplay',
        "type":        "method_replace",
        "search": """\
.method shouldPlacePrimaryHomeOnDisplay(I)Z
    .registers 4

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;

    invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->getUserAssignedToDisplay(I)I

    move-result v0

    invoke-virtual {p0, p1, v0}, Lcom/android/server/wm/WindowManagerService;->shouldPlacePrimaryHomeOnDisplay(II)Z

    move-result v1

    return v1
.end method
""",
        "replacement": """\
.method shouldPlacePrimaryHomeOnDisplay(I)Z
    .registers 4

    goto :goto_2

    nop

    :goto_0
    invoke-virtual {p0, p1, v0}, Lcom/android/server/wm/WindowManagerService;->shouldPlacePrimaryHomeOnDisplay(II)Z

    move-result v1

    goto :goto_3

    nop

    :goto_1
    invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->getUserAssignedToDisplay(I)I

    move-result v0

    goto :goto_0

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;

    goto :goto_1

    nop

    :goto_3
    return v1
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;', 'invoke-virtual {v0, p1}, Lcom/android/server/pm/UserManagerInternal;->getUserAssignedToDisplay(I)I', 'move-result v0', 'invoke-virtual {p0, p1, v0}, Lcom/android/server/wm/WindowManagerService;->shouldPlacePrimaryHomeOnDisplay(II)Z', 'move-result v1', 'return v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_shouldPlacePrimaryHomeOnDisplay_II_Z",
        "method":      ".method shouldPlacePrimaryHomeOnDisplay(II)Z",
        "method_name": 'shouldPlacePrimaryHomeOnDisplay',
        "type":        "method_replace",
        "search": """\
.method shouldPlacePrimaryHomeOnDisplay(II)Z
    .registers 4

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;

    invoke-virtual {v0, p2}, Lcom/android/server/pm/UserManagerInternal;->getMainDisplayAssignedToUser(I)I

    move-result v0

    if-ne v0, p1, :cond_0

    const/4 v0, 0x1

    goto :goto_0

    :cond_0
    const/4 v0, 0x0

    :goto_0
    return v0
.end method
""",
        "replacement": """\
.method shouldPlacePrimaryHomeOnDisplay(II)Z
    .registers 4

    goto :goto_8

    nop

    :goto_0
    invoke-virtual {v0, p2}, Lcom/android/server/pm/UserManagerInternal;->getMainDisplayAssignedToUser(I)I

    move-result v0

    goto :goto_6

    nop

    :goto_1
    const/4 v0, 0x0

    :goto_2
    goto :goto_7

    nop

    :goto_3
    const/4 v0, 0x1

    goto :goto_4

    nop

    :goto_4
    goto :goto_2

    :goto_5
    goto :goto_1

    nop

    :goto_6
    if-eq v0, p1, :cond_0

    goto :goto_5

    :cond_0
    goto :goto_3

    nop

    :goto_7
    return v0

    :goto_8
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;

    goto :goto_0

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mUmInternal:Lcom/android/server/pm/UserManagerInternal;', 'invoke-virtual {v0, p2}, Lcom/android/server/pm/UserManagerInternal;->getMainDisplayAssignedToUser(I)I', 'move-result v0', 'if-ne v0, p1, :cond_0', 'return v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_shouldRestoreImeVisibility_Landroid_os_IBinder__Z",
        "method":      ".method shouldRestoreImeVisibility(Landroid/os/IBinder;)Z",
        "method_name": 'shouldRestoreImeVisibility',
        "type":        "method_replace",
        "search": """\
.method shouldRestoreImeVisibility(Landroid/os/IBinder;)Z
    .registers 9

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    invoke-virtual {v1, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/wm/WindowState;

    const/4 v2, 0x0

    if-nez v1, :cond_0

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return v2

    :cond_0
    :try_start_1
    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->getTask()Lcom/android/server/wm/Task;

    move-result-object v3

    if-nez v3, :cond_1

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return v2

    :cond_1
    :try_start_2
    iget-object v4, v1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    const/4 v5, 0x1

    if-eqz v4, :cond_2

    iget-object v4, v1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    iget-boolean v4, v4, Lcom/android/server/wm/ActivityRecord;->mLastImeShown:Z

    if-eqz v4, :cond_2

    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return v5

    :cond_2
    :try_start_3
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mTaskSnapshotController:Lcom/android/server/wm/TaskSnapshotController;

    iget v6, v3, Lcom/android/server/wm/Task;->mTaskId:I

    invoke-virtual {v4, v6, v2}, Lcom/android/server/wm/TaskSnapshotController;->getSnapshot(IZ)Landroid/window/TaskSnapshot;

    move-result-object v4

    if-eqz v4, :cond_3

    invoke-virtual {v4}, Landroid/window/TaskSnapshot;->hasImeSurface()Z

    move-result v6

    if-eqz v6, :cond_3

    move v2, v5

    :cond_3
    monitor-exit v0
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return v2

    :catchall_0
    move-exception v1

    :try_start_4
    monitor-exit v0
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method shouldRestoreImeVisibility(Landroid/os/IBinder;)Z
    .registers 9

    goto :goto_9

    nop

    :goto_0
    monitor-enter v0

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    invoke-virtual {v1, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/wm/WindowState;

    const/4 v2, 0x0

    if-nez v1, :cond_1

    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_8

    nop

    :goto_1
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_6

    nop

    :goto_2
    throw v1

    :goto_3
    return v2

    :cond_0
    :try_start_1
    iget-object v4, v1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    const/4 v5, 0x1

    if-eqz v4, :cond_2

    iget-object v4, v1, Lcom/android/server/wm/WindowState;->mActivityRecord:Lcom/android/server/wm/ActivityRecord;

    iget-boolean v4, v4, Lcom/android/server/wm/ActivityRecord;->mLastImeShown:Z

    if-eqz v4, :cond_2

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_1

    nop

    :goto_4
    return v2

    :cond_1
    :try_start_2
    invoke-virtual {v1}, Lcom/android/server/wm/WindowState;->getTask()Lcom/android/server/wm/Task;

    move-result-object v3

    if-nez v3, :cond_0

    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_5

    nop

    :goto_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_3

    nop

    :goto_6
    return v5

    :cond_2
    :try_start_3
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mTaskSnapshotController:Lcom/android/server/wm/TaskSnapshotController;

    iget v6, v3, Lcom/android/server/wm/Task;->mTaskId:I

    invoke-virtual {v4, v6, v2}, Lcom/android/server/wm/TaskSnapshotController;->getSnapshot(IZ)Landroid/window/TaskSnapshot;

    move-result-object v4

    if-eqz v4, :cond_3

    invoke-virtual {v4}, Landroid/window/TaskSnapshot;->hasImeSurface()Z

    move-result v6

    if-eqz v6, :cond_3

    move v2, v5

    :cond_3
    monitor-exit v0
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    goto :goto_7

    nop

    :goto_7
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_b

    nop

    :goto_8
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_4

    nop

    :goto_9
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_a

    nop

    :goto_a
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_0

    nop

    :goto_b
    return v2

    :catchall_0
    move-exception v1

    :try_start_4
    monitor-exit v0
    :try_end_4
    .catchall {:try_start_4 .. :try_end_4} :catchall_0

    goto :goto_c

    nop

    :goto_c
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;', 'invoke-virtual {v1, p1}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;', 'move-result-object v1', 'check-cast v1, Lcom/android/server/wm/WindowState;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_updateFocusedWindowLocked_IZ_Z",
        "method":      ".method updateFocusedWindowLocked(IZ)Z",
        "method_name": 'updateFocusedWindowLocked',
        "type":        "method_replace",
        "search": """\
.method updateFocusedWindowLocked(IZ)Z
    .registers 7

    const-string v0, "com.android.server.wm.WindowManagerService.updateFocusedWindowLocked(IZ)Z"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerServiceStub;->get()Lcom/android/server/wm/WindowManagerServiceStub;

    move-result-object v1

    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mResumeActivity:Ljava/lang/String;

    invoke-interface {v1, v2}, Lcom/android/server/wm/WindowManagerServiceStub;->isUpdateFocusedWindowLocked(Ljava/lang/String;)Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    const/4 v0, 0x0

    return v0

    :cond_0
    const-string v1, "wmUpdateFocus"

    const-wide/16 v2, 0x20

    invoke-static {v2, v3, v1}, Landroid/os/Trace;->traceBegin(JLjava/lang/String;)V

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1, p2}, Lcom/android/server/wm/RootWindowContainer;->updateFocusedWindowLocked(IZ)Z

    move-result v1

    invoke-static {v2, v3}, Landroid/os/Trace;->traceEnd(J)V

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return v1

    :catchall_0
    move-exception p1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw p1
.end method
""",
        "replacement": """\
.method updateFocusedWindowLocked(IZ)Z
    .registers 7

    goto :goto_3

    nop

    :goto_0
    throw p1

    :goto_1
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_0

    nop

    :goto_2
    return v1

    :catchall_0
    move-exception p1

    goto :goto_1

    nop

    :goto_3
    const-string v0, "com.android.server.wm.WindowManagerService.updateFocusedWindowLocked(IZ)Z"

    goto :goto_4

    nop

    :goto_4
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerServiceStub;->get()Lcom/android/server/wm/WindowManagerServiceStub;

    move-result-object v1

    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mResumeActivity:Ljava/lang/String;

    invoke-interface {v1, v2}, Lcom/android/server/wm/WindowManagerServiceStub;->isUpdateFocusedWindowLocked(Ljava/lang/String;)Z

    move-result v1

    if-eqz v1, :cond_0

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    const/4 v0, 0x0

    return v0

    :cond_0
    const-string v1, "wmUpdateFocus"

    const-wide/16 v2, 0x20

    invoke-static {v2, v3, v1}, Landroid/os/Trace;->traceBegin(JLjava/lang/String;)V

    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    invoke-virtual {v1, p1, p2}, Lcom/android/server/wm/RootWindowContainer;->updateFocusedWindowLocked(IZ)Z

    move-result v1

    invoke-static {v2, v3}, Landroid/os/Trace;->traceEnd(J)V

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_2

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.updateFocusedWindowLocked(IZ)Z"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'invoke-static {}, Lcom/android/server/wm/WindowManagerServiceStub;->get()Lcom/android/server/wm/WindowManagerServiceStub;', 'move-result-object v1', 'iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mResumeActivity:Ljava/lang/String;', 'invoke-interface {v1, v2}, Lcom/android/server/wm/WindowManagerServiceStub;->isUpdateFocusedWindowLocked(Ljava/lang/String;)Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_updateInputChannel_Landroid_os_IBinder_ILandroid_view_Surfac",
        "method":      ".method updateInputChannel(Landroid/os/IBinder;ILandroid/view/SurfaceControl;IIILandroid/graphics/Region;)V",
        "method_name": 'updateInputChannel',
        "type":        "method_replace",
        "search": """\
.method updateInputChannel(Landroid/os/IBinder;ILandroid/view/SurfaceControl;IIILandroid/graphics/Region;)V
    .registers 23

    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v2

    :try_start_0
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    move-object/from16 v3, p1

    invoke-virtual {v0, v3}, Lcom/android/server/wm/EmbeddedWindowController;->get(Landroid/os/IBinder;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    move-result-object v0

    if-nez v0, :cond_0

    const-string v4, "WindowManager"

    const-string v5, "Couldn\\'t find window for provided channelToken."

    invoke-static {v4, v5}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_0
    :try_start_1
    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->getApplicationHandle()Landroid/view/InputApplicationHandle;

    move-result-object v8

    and-int/lit8 v4, p4, 0x8

    if-nez v4, :cond_1

    const/4 v4, 0x1

    goto :goto_0

    :cond_1
    const/4 v4, 0x0

    :goto_0
    invoke-virtual {v0, v4}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->setIsFocusable(Z)V

    monitor-exit v2
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    iget v3, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mOwnerUid:I

    iget v4, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mOwnerPid:I

    iget v12, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mWindowType:I

    iget-object v14, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mClient:Landroid/os/IBinder;

    move-object v1, p0

    move-object/from16 v2, p1

    move/from16 v5, p2

    move-object/from16 v6, p3

    move/from16 v9, p4

    move/from16 v10, p5

    move/from16 v11, p6

    move-object/from16 v13, p7

    invoke-direct/range {v1 .. v14}, Lcom/android/server/wm/WindowManagerService;->updateInputChannel(Landroid/os/IBinder;IIILandroid/view/SurfaceControl;Ljava/lang/String;Landroid/view/InputApplicationHandle;IIIILandroid/graphics/Region;Landroid/os/IBinder;)V

    return-void

    :catchall_0
    move-exception v0

    :try_start_2
    monitor-exit v2
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v0
.end method
""",
        "replacement": """\
.method updateInputChannel(Landroid/os/IBinder;ILandroid/view/SurfaceControl;IIILandroid/graphics/Region;)V
    .registers 23

    goto :goto_6

    nop

    :goto_0
    throw v0

    :goto_1
    move/from16 v9, p4

    goto :goto_10

    nop

    :goto_2
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_16

    nop

    :goto_3
    move-object/from16 v13, p7

    goto :goto_a

    nop

    :goto_4
    return-void

    :catchall_0
    move-exception v0

    :try_start_0
    monitor-exit v2
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_5

    nop

    :goto_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_0

    nop

    :goto_6
    iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_c

    nop

    :goto_7
    move/from16 v11, p6

    goto :goto_3

    nop

    :goto_8
    move-object/from16 v2, p1

    goto :goto_e

    nop

    :goto_9
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_13

    nop

    :goto_a
    invoke-direct/range {v1 .. v14}, Lcom/android/server/wm/WindowManagerService;->updateInputChannel(Landroid/os/IBinder;IIILandroid/view/SurfaceControl;Ljava/lang/String;Landroid/view/InputApplicationHandle;IIIILandroid/graphics/Region;Landroid/os/IBinder;)V

    goto :goto_4

    nop

    :goto_b
    move-object/from16 v6, p3

    goto :goto_1

    nop

    :goto_c
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_12

    nop

    :goto_d
    iget v12, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mWindowType:I

    goto :goto_11

    nop

    :goto_e
    move/from16 v5, p2

    goto :goto_b

    nop

    :goto_f
    move-object v1, p0

    goto :goto_8

    nop

    :goto_10
    move/from16 v10, p5

    goto :goto_7

    nop

    :goto_11
    iget-object v14, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mClient:Landroid/os/IBinder;

    goto :goto_f

    nop

    :goto_12
    monitor-enter v2

    :try_start_1
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;

    move-object/from16 v3, p1

    invoke-virtual {v0, v3}, Lcom/android/server/wm/EmbeddedWindowController;->get(Landroid/os/IBinder;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;

    move-result-object v0

    if-nez v0, :cond_0

    const-string v4, "WindowManager"

    const-string v5, "Couldn\\'t find window for provided channelToken."

    invoke-static {v4, v5}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    monitor-exit v2
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_9

    nop

    :goto_13
    return-void

    :cond_0
    :try_start_2
    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->toString()Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v0}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->getApplicationHandle()Landroid/view/InputApplicationHandle;

    move-result-object v8

    and-int/lit8 v4, p4, 0x8

    if-nez v4, :cond_1

    const/4 v4, 0x1

    goto :goto_14

    :cond_1
    const/4 v4, 0x0

    :goto_14
    invoke-virtual {v0, v4}, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->setIsFocusable(Z)V

    monitor-exit v2
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_2

    nop

    :goto_15
    iget v4, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mOwnerPid:I

    goto :goto_d

    nop

    :goto_16
    iget v3, v0, Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;->mOwnerUid:I

    goto :goto_15

    nop
.end method
""",
        "method_anchors": ['iget-object v2, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mEmbeddedWindowController:Lcom/android/server/wm/EmbeddedWindowController;', 'invoke-virtual {v0, v3}, Lcom/android/server/wm/EmbeddedWindowController;->get(Landroid/os/IBinder;)Lcom/android/server/wm/EmbeddedWindowController$EmbeddedWindow;', 'move-result-object v0', 'if-nez v0, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_updateNonSystemOverlayWindowsVisibilityIfNeeded_Lcom_android",
        "method":      ".method updateNonSystemOverlayWindowsVisibilityIfNeeded(Lcom/android/server/wm/WindowState;Z)V",
        "method_name": 'updateNonSystemOverlayWindowsVisibilityIfNeeded',
        "type":        "method_replace",
        "search": """\
.method updateNonSystemOverlayWindowsVisibilityIfNeeded(Lcom/android/server/wm/WindowState;Z)V
    .registers 12

    const/4 v0, 0x0

    const/4 v1, 0x1

    if-eqz p2, :cond_0

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->hideNonSystemOverlayWindowsWhenVisible()Z

    move-result v2

    if-eqz v2, :cond_0

    move v2, v1

    goto :goto_0

    :cond_0
    move v2, v0

    :goto_0
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;

    invoke-virtual {v3, p1}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v3

    if-ne v2, v3, :cond_1

    return-void

    :cond_1
    if-eqz v2, :cond_2

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;

    invoke-virtual {v3, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_1

    :cond_2
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;

    invoke-virtual {v3, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    :goto_1
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/com/android/window/flags/Flags;->fixHideOverlayApi()Z

    move-result v3

    if-eqz v3, :cond_7

    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getOwningUid()I

    move-result v3

    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindowsCountPerUid:Landroid/util/ArrayMap;

    invoke-virtual {v4}, Landroid/util/ArrayMap;->size()I

    move-result v4

    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindowsCountPerUid:Landroid/util/ArrayMap;

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v6

    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v7

    invoke-virtual {v5, v6, v7}, Landroid/util/ArrayMap;->getOrDefault(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v5

    check-cast v5, Ljava/lang/Integer;

    invoke-virtual {v5}, Ljava/lang/Integer;->intValue()I

    move-result v5

    if-eqz v2, :cond_3

    move v6, v1

    goto :goto_2

    :cond_3
    const/4 v6, -0x1

    :goto_2
    add-int/2addr v5, v6

    if-gtz v5, :cond_4

    iget-object v6, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindowsCountPerUid:Landroid/util/ArrayMap;

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v7

    invoke-virtual {v6, v7}, Landroid/util/ArrayMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_3

    :cond_4
    iget-object v6, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindowsCountPerUid:Landroid/util/ArrayMap;

    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v7

    invoke-static {v5}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v8

    invoke-virtual {v6, v7, v8}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :goto_3
    iget-object v6, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindowsCountPerUid:Landroid/util/ArrayMap;

    invoke-virtual {v6}, Landroid/util/ArrayMap;->size()I

    move-result v6

    if-eq v6, v4, :cond_6

    if-le v6, v1, :cond_5

    if-gt v4, v1, :cond_6

    :cond_5
    goto :goto_4

    :cond_6
    move v1, v0

    :goto_4
    goto :goto_5

    :cond_7
    if-eqz v2, :cond_8

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;

    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v3

    if-eq v3, v1, :cond_9

    :cond_8
    if-nez v2, :cond_a

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;

    invoke-virtual {v3}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v3

    if-eqz v3, :cond_a

    :cond_9
    goto :goto_5

    :cond_a
    move v1, v0

    :goto_5
    if-eqz v1, :cond_b

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    new-instance v4, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda44;

    invoke-direct {v4, p0}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda44;-><init>(Lcom/android/server/wm/WindowManagerService;)V

    invoke-virtual {v3, v4, v0}, Lcom/android/server/wm/RootWindowContainer;->forAllWindows(Ljava/util/function/Consumer;Z)V

    :cond_b
    return-void
.end method
""",
        "replacement": """\
.method updateNonSystemOverlayWindowsVisibilityIfNeeded(Lcom/android/server/wm/WindowState;Z)V
    .registers 12

    goto :goto_19

    nop

    :goto_0
    move v2, v1

    goto :goto_41

    nop

    :goto_1
    invoke-static {v0}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v7

    goto :goto_2a

    nop

    :goto_2
    goto :goto_26

    :goto_3
    goto :goto_8

    nop

    :goto_4
    iget-object v6, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindowsCountPerUid:Landroid/util/ArrayMap;

    goto :goto_11

    nop

    :goto_5
    invoke-virtual {v6, v7}, Landroid/util/ArrayMap;->remove(Ljava/lang/Object;)Ljava/lang/Object;

    goto :goto_1f

    nop

    :goto_6
    if-le v4, v1, :cond_0

    goto :goto_15

    :cond_0
    :goto_7
    goto :goto_14

    nop

    :goto_8
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;

    goto :goto_25

    nop

    :goto_9
    const/4 v1, 0x1

    goto :goto_51

    nop

    :goto_a
    return-void

    :goto_b
    if-nez v3, :cond_1

    goto :goto_1d

    :cond_1
    :goto_c
    goto :goto_1c

    nop

    :goto_d
    invoke-virtual {v3, p1}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result v3

    goto :goto_1a

    nop

    :goto_e
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;

    goto :goto_d

    nop

    :goto_f
    invoke-virtual {v3, v4, v0}, Lcom/android/server/wm/RootWindowContainer;->forAllWindows(Ljava/util/function/Consumer;Z)V

    :goto_10
    goto :goto_a

    nop

    :goto_11
    invoke-virtual {v6}, Landroid/util/ArrayMap;->size()I

    move-result v6

    goto :goto_4e

    nop

    :goto_12
    invoke-virtual {v5}, Ljava/lang/Integer;->intValue()I

    move-result v5

    goto :goto_31

    nop

    :goto_13
    invoke-static {}, Lcom/android/internal/hidden_from_bootclasspath/com/android/window/flags/Flags;->fixHideOverlayApi()Z

    move-result v3

    goto :goto_1b

    nop

    :goto_14
    goto :goto_37

    :goto_15
    goto :goto_36

    nop

    :goto_16
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;

    goto :goto_49

    nop

    :goto_17
    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v7

    goto :goto_5

    nop

    :goto_18
    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v7

    goto :goto_3d

    nop

    :goto_19
    const/4 v0, 0x0

    goto :goto_9

    nop

    :goto_1a
    if-eq v2, v3, :cond_2

    goto :goto_4b

    :cond_2
    goto :goto_4a

    nop

    :goto_1b
    if-nez v3, :cond_3

    goto :goto_35

    :cond_3
    goto :goto_45

    nop

    :goto_1c
    goto :goto_54

    :goto_1d
    goto :goto_53

    nop

    :goto_1e
    if-gt v6, v1, :cond_4

    goto :goto_7

    :cond_4
    goto :goto_6

    nop

    :goto_1f
    goto :goto_3f

    :goto_20
    goto :goto_22

    nop

    :goto_21
    invoke-direct {v4, p0}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda44;-><init>(Lcom/android/server/wm/WindowManagerService;)V

    goto :goto_f

    nop

    :goto_22
    iget-object v6, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindowsCountPerUid:Landroid/util/ArrayMap;

    goto :goto_18

    nop

    :goto_23
    iget-object v6, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindowsCountPerUid:Landroid/util/ArrayMap;

    goto :goto_17

    nop

    :goto_24
    if-eqz v2, :cond_5

    goto :goto_1d

    :cond_5
    goto :goto_48

    nop

    :goto_25
    invoke-virtual {v3, p1}, Ljava/util/ArrayList;->remove(Ljava/lang/Object;)Z

    :goto_26
    goto :goto_13

    nop

    :goto_27
    invoke-static {v3}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v6

    goto :goto_1

    nop

    :goto_28
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->hideNonSystemOverlayWindowsWhenVisible()Z

    move-result v2

    goto :goto_50

    nop

    :goto_29
    add-int/2addr v5, v6

    goto :goto_2b

    nop

    :goto_2a
    invoke-virtual {v5, v6, v7}, Landroid/util/ArrayMap;->getOrDefault(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v5

    goto :goto_40

    nop

    :goto_2b
    if-lez v5, :cond_6

    goto :goto_20

    :cond_6
    goto :goto_23

    nop

    :goto_2c
    if-nez v2, :cond_7

    goto :goto_39

    :cond_7
    goto :goto_16

    nop

    :goto_2d
    new-instance v4, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda44;

    goto :goto_21

    nop

    :goto_2e
    invoke-virtual {v4}, Landroid/util/ArrayMap;->size()I

    move-result v4

    goto :goto_46

    nop

    :goto_2f
    const/4 v6, -0x1

    :goto_30
    goto :goto_29

    nop

    :goto_31
    if-nez v2, :cond_8

    goto :goto_4d

    :cond_8
    goto :goto_3a

    nop

    :goto_32
    invoke-virtual {v3}, Ljava/util/ArrayList;->isEmpty()Z

    move-result v3

    goto :goto_b

    nop

    :goto_33
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    goto :goto_2d

    nop

    :goto_34
    goto :goto_54

    :goto_35
    goto :goto_2c

    nop

    :goto_36
    move v1, v0

    :goto_37
    goto :goto_34

    nop

    :goto_38
    if-ne v3, v1, :cond_9

    goto :goto_c

    :cond_9
    :goto_39
    goto :goto_24

    nop

    :goto_3a
    move v6, v1

    goto :goto_4c

    nop

    :goto_3b
    move v2, v0

    :goto_3c
    goto :goto_e

    nop

    :goto_3d
    invoke-static {v5}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object v8

    goto :goto_3e

    nop

    :goto_3e
    invoke-virtual {v6, v7, v8}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    :goto_3f
    goto :goto_4

    nop

    :goto_40
    check-cast v5, Ljava/lang/Integer;

    goto :goto_12

    nop

    :goto_41
    goto :goto_3c

    :goto_42
    goto :goto_3b

    nop

    :goto_43
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;

    goto :goto_47

    nop

    :goto_44
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindowsCountPerUid:Landroid/util/ArrayMap;

    goto :goto_2e

    nop

    :goto_45
    invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->getOwningUid()I

    move-result v3

    goto :goto_44

    nop

    :goto_46
    iget-object v5, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindowsCountPerUid:Landroid/util/ArrayMap;

    goto :goto_27

    nop

    :goto_47
    invoke-virtual {v3, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    goto :goto_2

    nop

    :goto_48
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;

    goto :goto_32

    nop

    :goto_49
    invoke-virtual {v3}, Ljava/util/ArrayList;->size()I

    move-result v3

    goto :goto_38

    nop

    :goto_4a
    return-void

    :goto_4b
    goto :goto_4f

    nop

    :goto_4c
    goto :goto_30

    :goto_4d
    goto :goto_2f

    nop

    :goto_4e
    if-ne v6, v4, :cond_a

    goto :goto_15

    :cond_a
    goto :goto_1e

    nop

    :goto_4f
    if-nez v2, :cond_b

    goto :goto_3

    :cond_b
    goto :goto_43

    nop

    :goto_50
    if-nez v2, :cond_c

    goto :goto_42

    :cond_c
    goto :goto_0

    nop

    :goto_51
    if-nez p2, :cond_d

    goto :goto_42

    :cond_d
    goto :goto_28

    nop

    :goto_52
    if-nez v1, :cond_e

    goto :goto_10

    :cond_e
    goto :goto_33

    nop

    :goto_53
    move v1, v0

    :goto_54
    goto :goto_52

    nop
.end method
""",
        "method_anchors": ['if-eqz p2, :cond_0', 'invoke-virtual {p1}, Lcom/android/server/wm/WindowState;->hideNonSystemOverlayWindowsWhenVisible()Z', 'move-result v2', 'if-eqz v2, :cond_0', 'iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mHidingNonSystemOverlayWindows:Ljava/util/ArrayList;', 'invoke-virtual {v3, p1}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_updateTapExcludeRegion_Landroid_view_IWindow_Landroid_graphi",
        "method":      ".method updateTapExcludeRegion(Landroid/view/IWindow;Landroid/graphics/Region;)V",
        "method_name": 'updateTapExcludeRegion',
        "type":        "method_replace",
        "search": """\
.method updateTapExcludeRegion(Landroid/view/IWindow;Landroid/graphics/Region;)V
    .registers 11

    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v0

    const/4 v1, 0x0

    const/4 v2, 0x0

    :try_start_0
    invoke-virtual {p0, v1, p1, v2}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v1

    if-nez v1, :cond_1

    sget-object v3, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    const/4 v4, 0x3

    aget-boolean v3, v3, v4

    if-eqz v3, :cond_0

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v3

    sget-object v4, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v3}, [Ljava/lang/Object;

    move-result-object v5

    const-wide v6, 0x11bee8c606b635faL

    invoke-static {v4, v6, v7, v2, v5}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :cond_1
    :try_start_1
    invoke-virtual {v1, p2}, Lcom/android/server/wm/WindowState;->updateTapExcludeRegion(Landroid/graphics/Region;)V

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    return-void

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method updateTapExcludeRegion(Landroid/view/IWindow;Landroid/graphics/Region;)V
    .registers 11

    goto :goto_2

    nop

    :goto_0
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_a

    nop

    :goto_1
    const/4 v2, 0x0

    :try_start_0
    invoke-virtual {p0, v1, p1, v2}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;

    move-result-object v1

    if-nez v1, :cond_1

    sget-object v3, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    const/4 v4, 0x3

    aget-boolean v3, v3, v4

    if-eqz v3, :cond_0

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v3

    sget-object v4, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v3}, [Ljava/lang/Object;

    move-result-object v5

    const-wide v6, 0x11bee8c606b635faL

    invoke-static {v4, v6, v7, v2, v5}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_0
    monitor-exit v0
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_4

    nop

    :goto_2
    iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_9

    nop

    :goto_3
    return-void

    :cond_1
    :try_start_1
    invoke-virtual {v1, p2}, Lcom/android/server/wm/WindowState;->updateTapExcludeRegion(Landroid/graphics/Region;)V

    monitor-exit v0
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    goto :goto_5

    nop

    :goto_4
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_3

    nop

    :goto_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_6

    nop

    :goto_6
    return-void

    :catchall_0
    move-exception v1

    :try_start_2
    monitor-exit v0
    :try_end_2
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_0

    nop

    :goto_7
    const/4 v1, 0x0

    goto :goto_1

    nop

    :goto_8
    monitor-enter v0

    goto :goto_7

    nop

    :goto_9
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_8

    nop

    :goto_a
    throw v1
.end method
""",
        "method_anchors": ['iget-object v0, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;', 'invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V', 'invoke-virtual {p0, v1, p1, v2}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;', 'move-result-object v1', 'if-nez v1, :cond_1', 'sget-object v3, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_viewServerGetFocusedWindow_Ljava_net_Socket__Z",
        "method":      ".method viewServerGetFocusedWindow(Ljava/net/Socket;)Z",
        "method_name": 'viewServerGetFocusedWindow',
        "type":        "method_replace",
        "search": """\
.method viewServerGetFocusedWindow(Ljava/net/Socket;)Z
    .registers 9

    invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->isSystemSecure()Z

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x0

    return v0

    :cond_0
    const/4 v0, 0x1

    invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->getFocusedWindow()Lcom/android/server/wm/WindowState;

    move-result-object v1

    const/4 v2, 0x0

    :try_start_0
    invoke-virtual {p1}, Ljava/net/Socket;->getOutputStream()Ljava/io/OutputStream;

    move-result-object v3

    new-instance v4, Ljava/io/BufferedWriter;

    new-instance v5, Ljava/io/OutputStreamWriter;

    invoke-direct {v5, v3}, Ljava/io/OutputStreamWriter;-><init>(Ljava/io/OutputStream;)V

    const/16 v6, 0x2000

    invoke-direct {v4, v5, v6}, Ljava/io/BufferedWriter;-><init>(Ljava/io/Writer;I)V

    move-object v2, v4

    if-eqz v1, :cond_1

    invoke-static {v1}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I

    move-result v4

    invoke-static {v4}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v2, v4}, Ljava/io/BufferedWriter;->write(Ljava/lang/String;)V

    const/16 v4, 0x20

    invoke-virtual {v2, v4}, Ljava/io/BufferedWriter;->write(I)V

    iget-object v4, v1, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v4}, Landroid/view/WindowManager$LayoutParams;->getTitle()Ljava/lang/CharSequence;

    move-result-object v4

    invoke-virtual {v2, v4}, Ljava/io/BufferedWriter;->append(Ljava/lang/CharSequence;)Ljava/io/Writer;

    :cond_1
    const/16 v4, 0xa

    invoke-virtual {v2, v4}, Ljava/io/BufferedWriter;->write(I)V

    invoke-virtual {v2}, Ljava/io/BufferedWriter;->flush()V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_1
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    nop

    :try_start_1
    invoke-virtual {v2}, Ljava/io/BufferedWriter;->close()V
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_2

    goto :goto_1

    :catchall_0
    move-exception v3

    if-eqz v2, :cond_2

    :try_start_2
    invoke-virtual {v2}, Ljava/io/BufferedWriter;->close()V
    :try_end_2
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_0

    goto :goto_0

    :catch_0
    move-exception v4

    const/4 v0, 0x0

    :cond_2
    :goto_0
    throw v3

    :catch_1
    move-exception v3

    const/4 v0, 0x0

    if-eqz v2, :cond_3

    :try_start_3
    invoke-virtual {v2}, Ljava/io/BufferedWriter;->close()V
    :try_end_3
    .catch Ljava/io/IOException; {:try_start_3 .. :try_end_3} :catch_2

    goto :goto_1

    :catch_2
    move-exception v3

    const/4 v0, 0x0

    :goto_1
    nop

    :cond_3
    return v0
.end method
""",
        "replacement": """\
.method viewServerGetFocusedWindow(Ljava/net/Socket;)Z
    .registers 9

    goto :goto_12

    nop

    :goto_0
    invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->getFocusedWindow()Lcom/android/server/wm/WindowState;

    move-result-object v1

    goto :goto_1

    nop

    :goto_1
    const/4 v2, 0x0

    :try_start_0
    invoke-virtual {p1}, Ljava/net/Socket;->getOutputStream()Ljava/io/OutputStream;

    move-result-object v3

    new-instance v4, Ljava/io/BufferedWriter;

    new-instance v5, Ljava/io/OutputStreamWriter;

    invoke-direct {v5, v3}, Ljava/io/OutputStreamWriter;-><init>(Ljava/io/OutputStream;)V

    const/16 v6, 0x2000

    invoke-direct {v4, v5, v6}, Ljava/io/BufferedWriter;-><init>(Ljava/io/Writer;I)V

    move-object v2, v4

    if-eqz v1, :cond_0

    invoke-static {v1}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I

    move-result v4

    invoke-static {v4}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;

    move-result-object v4

    invoke-virtual {v2, v4}, Ljava/io/BufferedWriter;->write(Ljava/lang/String;)V

    const/16 v4, 0x20

    invoke-virtual {v2, v4}, Ljava/io/BufferedWriter;->write(I)V

    iget-object v4, v1, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v4}, Landroid/view/WindowManager$LayoutParams;->getTitle()Ljava/lang/CharSequence;

    move-result-object v4

    invoke-virtual {v2, v4}, Ljava/io/BufferedWriter;->append(Ljava/lang/CharSequence;)Ljava/io/Writer;

    :cond_0
    const/16 v4, 0xa

    invoke-virtual {v2, v4}, Ljava/io/BufferedWriter;->write(I)V

    invoke-virtual {v2}, Ljava/io/BufferedWriter;->flush()V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_2
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    nop

    :try_start_1
    invoke-virtual {v2}, Ljava/io/BufferedWriter;->close()V
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_0

    goto :goto_d

    nop

    :goto_2
    if-nez v2, :cond_1

    goto :goto_7

    :cond_1
    :try_start_2
    invoke-virtual {v2}, Ljava/io/BufferedWriter;->close()V
    :try_end_2
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_0

    goto :goto_3

    nop

    :goto_3
    goto :goto_6

    :catch_0
    move-exception v3

    goto :goto_5

    nop

    :goto_4
    const/4 v0, 0x1

    goto :goto_0

    nop

    :goto_5
    const/4 v0, 0x0

    :goto_6
    nop

    :goto_7
    goto :goto_13

    nop

    :goto_8
    goto :goto_11

    :catch_1
    move-exception v4

    goto :goto_10

    nop

    :goto_9
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_a
    return v0

    :goto_b
    goto :goto_4

    nop

    :goto_c
    throw v3

    :catch_2
    move-exception v3

    goto :goto_9

    nop

    :goto_d
    goto :goto_6

    :catchall_0
    move-exception v3

    goto :goto_14

    nop

    :goto_e
    if-nez v0, :cond_2

    goto :goto_b

    :cond_2
    goto :goto_f

    nop

    :goto_f
    const/4 v0, 0x0

    goto :goto_a

    nop

    :goto_10
    const/4 v0, 0x0

    :goto_11
    goto :goto_c

    nop

    :goto_12
    invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->isSystemSecure()Z

    move-result v0

    goto :goto_e

    nop

    :goto_13
    return v0

    :goto_14
    if-nez v2, :cond_3

    goto :goto_11

    :cond_3
    :try_start_3
    invoke-virtual {v2}, Ljava/io/BufferedWriter;->close()V
    :try_end_3
    .catch Ljava/io/IOException; {:try_start_3 .. :try_end_3} :catch_1

    goto :goto_8

    nop
.end method
""",
        "method_anchors": ['invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->isSystemSecure()Z', 'move-result v0', 'if-eqz v0, :cond_0', 'return v0', 'invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->getFocusedWindow()Lcom/android/server/wm/WindowState;', 'move-result-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_viewServerListWindows_Ljava_net_Socket__Z",
        "method":      ".method viewServerListWindows(Ljava/net/Socket;)Z",
        "method_name": 'viewServerListWindows',
        "type":        "method_replace",
        "search": """\
.method viewServerListWindows(Ljava/net/Socket;)Z
    .registers 10

    invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->isSystemSecure()Z

    move-result v0

    const/4 v1, 0x0

    if-eqz v0, :cond_0

    return v1

    :cond_0
    const/4 v0, 0x1

    new-instance v2, Ljava/util/ArrayList;

    invoke-direct {v2}, Ljava/util/ArrayList;-><init>()V

    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    monitor-enter v3

    :try_start_0
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    new-instance v5, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda17;

    invoke-direct {v5, v2}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda17;-><init>(Ljava/util/ArrayList;)V

    invoke-virtual {v4, v5, v1}, Lcom/android/server/wm/RootWindowContainer;->forAllWindows(Ljava/util/function/Consumer;Z)V

    monitor-exit v3
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    const/4 v1, 0x0

    :try_start_1
    invoke-virtual {p1}, Ljava/net/Socket;->getOutputStream()Ljava/io/OutputStream;

    move-result-object v3

    new-instance v4, Ljava/io/BufferedWriter;

    new-instance v5, Ljava/io/OutputStreamWriter;

    invoke-direct {v5, v3}, Ljava/io/OutputStreamWriter;-><init>(Ljava/io/OutputStream;)V

    const/16 v6, 0x2000

    invoke-direct {v4, v5, v6}, Ljava/io/BufferedWriter;-><init>(Ljava/io/Writer;I)V

    move-object v1, v4

    invoke-virtual {v2}, Ljava/util/ArrayList;->size()I

    move-result v4

    const/4 v5, 0x0

    :goto_0
    if-ge v5, v4, :cond_1

    invoke-virtual {v2, v5}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v6

    check-cast v6, Lcom/android/server/wm/WindowState;

    invoke-static {v6}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I

    move-result v7

    invoke-static {v7}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v1, v7}, Ljava/io/BufferedWriter;->write(Ljava/lang/String;)V

    const/16 v7, 0x20

    invoke-virtual {v1, v7}, Ljava/io/BufferedWriter;->write(I)V

    iget-object v7, v6, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v7}, Landroid/view/WindowManager$LayoutParams;->getTitle()Ljava/lang/CharSequence;

    move-result-object v7

    invoke-virtual {v1, v7}, Ljava/io/BufferedWriter;->append(Ljava/lang/CharSequence;)Ljava/io/Writer;

    const/16 v7, 0xa

    invoke-virtual {v1, v7}, Ljava/io/BufferedWriter;->write(I)V

    add-int/lit8 v5, v5, 0x1

    goto :goto_0

    :cond_1
    const-string v5, "DONE.\\n"

    invoke-virtual {v1, v5}, Ljava/io/BufferedWriter;->write(Ljava/lang/String;)V

    invoke-virtual {v1}, Ljava/io/BufferedWriter;->flush()V
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    nop

    :try_start_2
    invoke-virtual {v1}, Ljava/io/BufferedWriter;->close()V
    :try_end_2
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_2

    goto :goto_2

    :catchall_0
    move-exception v3

    if-eqz v1, :cond_2

    :try_start_3
    invoke-virtual {v1}, Ljava/io/BufferedWriter;->close()V
    :try_end_3
    .catch Ljava/io/IOException; {:try_start_3 .. :try_end_3} :catch_0

    goto :goto_1

    :catch_0
    move-exception v4

    const/4 v0, 0x0

    :cond_2
    :goto_1
    throw v3

    :catch_1
    move-exception v3

    const/4 v0, 0x0

    if-eqz v1, :cond_3

    :try_start_4
    invoke-virtual {v1}, Ljava/io/BufferedWriter;->close()V
    :try_end_4
    .catch Ljava/io/IOException; {:try_start_4 .. :try_end_4} :catch_2

    goto :goto_2

    :catch_2
    move-exception v3

    const/4 v0, 0x0

    :goto_2
    nop

    :cond_3
    return v0

    :catchall_1
    move-exception v1

    :try_start_5
    monitor-exit v3
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_1

    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    throw v1
.end method
""",
        "replacement": """\
.method viewServerListWindows(Ljava/net/Socket;)Z
    .registers 10

    goto :goto_0

    nop

    :goto_0
    invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->isSystemSecure()Z

    move-result v0

    goto :goto_13

    nop

    :goto_1
    invoke-direct {v2}, Ljava/util/ArrayList;-><init>()V

    goto :goto_3

    nop

    :goto_2
    if-nez v1, :cond_0

    goto :goto_f

    :cond_0
    :try_start_0
    invoke-virtual {v1}, Ljava/io/BufferedWriter;->close()V
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_2

    goto :goto_18

    nop

    :goto_3
    iget-object v3, p0, Lcom/android/server/wm/WindowManagerService;->mGlobalLock:Lcom/android/server/wm/WindowManagerGlobalLock;

    goto :goto_7

    nop

    :goto_4
    const/4 v0, 0x0

    goto :goto_2

    nop

    :goto_5
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_8

    nop

    :goto_6
    goto :goto_11

    :catch_0
    move-exception v4

    goto :goto_10

    nop

    :goto_7
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->boostPriorityForLockedSection()V

    goto :goto_16

    nop

    :goto_8
    const/4 v1, 0x0

    :try_start_1
    invoke-virtual {p1}, Ljava/net/Socket;->getOutputStream()Ljava/io/OutputStream;

    move-result-object v3

    new-instance v4, Ljava/io/BufferedWriter;

    new-instance v5, Ljava/io/OutputStreamWriter;

    invoke-direct {v5, v3}, Ljava/io/OutputStreamWriter;-><init>(Ljava/io/OutputStream;)V

    const/16 v6, 0x2000

    invoke-direct {v4, v5, v6}, Ljava/io/BufferedWriter;-><init>(Ljava/io/Writer;I)V

    move-object v1, v4

    invoke-virtual {v2}, Ljava/util/ArrayList;->size()I

    move-result v4

    const/4 v5, 0x0

    :goto_9
    if-ge v5, v4, :cond_1

    invoke-virtual {v2, v5}, Ljava/util/ArrayList;->get(I)Ljava/lang/Object;

    move-result-object v6

    check-cast v6, Lcom/android/server/wm/WindowState;

    invoke-static {v6}, Ljava/lang/System;->identityHashCode(Ljava/lang/Object;)I

    move-result v7

    invoke-static {v7}, Ljava/lang/Integer;->toHexString(I)Ljava/lang/String;

    move-result-object v7

    invoke-virtual {v1, v7}, Ljava/io/BufferedWriter;->write(Ljava/lang/String;)V

    const/16 v7, 0x20

    invoke-virtual {v1, v7}, Ljava/io/BufferedWriter;->write(I)V

    iget-object v7, v6, Lcom/android/server/wm/WindowState;->mAttrs:Landroid/view/WindowManager$LayoutParams;

    invoke-virtual {v7}, Landroid/view/WindowManager$LayoutParams;->getTitle()Ljava/lang/CharSequence;

    move-result-object v7

    invoke-virtual {v1, v7}, Ljava/io/BufferedWriter;->append(Ljava/lang/CharSequence;)Ljava/io/Writer;

    const/16 v7, 0xa

    invoke-virtual {v1, v7}, Ljava/io/BufferedWriter;->write(I)V

    add-int/lit8 v5, v5, 0x1

    goto :goto_9

    :cond_1
    const-string v5, "DONE.\\n"

    invoke-virtual {v1, v5}, Ljava/io/BufferedWriter;->write(Ljava/lang/String;)V

    invoke-virtual {v1}, Ljava/io/BufferedWriter;->flush()V
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    nop

    :try_start_2
    invoke-virtual {v1}, Ljava/io/BufferedWriter;->close()V
    :try_end_2
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_2

    goto :goto_1a

    nop

    :goto_a
    throw v1

    :goto_b
    invoke-static {}, Lcom/android/server/wm/WindowManagerService;->resetPriorityAfterLockedSection()V

    goto :goto_a

    nop

    :goto_c
    throw v3

    :catch_1
    move-exception v3

    goto :goto_4

    nop

    :goto_d
    const/4 v0, 0x0

    :goto_e
    nop

    :goto_f
    goto :goto_1c

    nop

    :goto_10
    const/4 v0, 0x0

    :goto_11
    goto :goto_c

    nop

    :goto_12
    if-nez v0, :cond_2

    goto :goto_15

    :cond_2
    goto :goto_14

    nop

    :goto_13
    const/4 v1, 0x0

    goto :goto_12

    nop

    :goto_14
    return v1

    :goto_15
    goto :goto_19

    nop

    :goto_16
    monitor-enter v3

    :try_start_3
    iget-object v4, p0, Lcom/android/server/wm/WindowManagerService;->mRoot:Lcom/android/server/wm/RootWindowContainer;

    new-instance v5, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda17;

    invoke-direct {v5, v2}, Lcom/android/server/wm/WindowManagerService$$ExternalSyntheticLambda17;-><init>(Ljava/util/ArrayList;)V

    invoke-virtual {v4, v5, v1}, Lcom/android/server/wm/RootWindowContainer;->forAllWindows(Ljava/util/function/Consumer;Z)V

    monitor-exit v3
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_1

    goto :goto_5

    nop

    :goto_17
    new-instance v2, Ljava/util/ArrayList;

    goto :goto_1

    nop

    :goto_18
    goto :goto_e

    :catch_2
    move-exception v3

    goto :goto_d

    nop

    :goto_19
    const/4 v0, 0x1

    goto :goto_17

    nop

    :goto_1a
    goto :goto_e

    :catchall_0
    move-exception v3

    goto :goto_1b

    nop

    :goto_1b
    if-nez v1, :cond_3

    goto :goto_11

    :cond_3
    :try_start_4
    invoke-virtual {v1}, Ljava/io/BufferedWriter;->close()V
    :try_end_4
    .catch Ljava/io/IOException; {:try_start_4 .. :try_end_4} :catch_0

    goto :goto_6

    nop

    :goto_1c
    return v0

    :catchall_1
    move-exception v1

    :try_start_5
    monitor-exit v3
    :try_end_5
    .catchall {:try_start_5 .. :try_end_5} :catchall_1

    goto :goto_b

    nop
.end method
""",
        "method_anchors": ['invoke-direct {p0}, Lcom/android/server/wm/WindowManagerService;->isSystemSecure()Z', 'move-result v0', 'if-eqz v0, :cond_0', 'return v1', 'new-instance v2, Ljava/util/ArrayList;', 'invoke-direct {v2}, Ljava/util/ArrayList;-><init>()V'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_viewServerWindowCommand_Ljava_net_Socket_Ljava_lang_String_L",
        "method":      ".method viewServerWindowCommand(Ljava/net/Socket;Ljava/lang/String;Ljava/lang/String;)Z",
        "method_name": 'viewServerWindowCommand',
        "type":        "method_replace",
        "search": """\
.method viewServerWindowCommand(Ljava/net/Socket;Ljava/lang/String;Ljava/lang/String;)Z
    .registers 20

    move-object/from16 v1, p3

    invoke-direct/range {p0 .. p0}, Lcom/android/server/wm/WindowManagerService;->isSystemSecure()Z

    move-result v0

    const/4 v2, 0x0

    if-eqz v0, :cond_0

    return v2

    :cond_0
    const/4 v3, 0x1

    const/4 v4, 0x0

    const/4 v5, 0x0

    const/4 v6, 0x0

    const/16 v0, 0x20

    :try_start_0
    invoke-virtual {v1, v0}, Ljava/lang/String;->indexOf(I)I

    move-result v0

    const/4 v7, -0x1

    if-ne v0, v7, :cond_1

    invoke-virtual {v1}, Ljava/lang/String;->length()I

    move-result v7

    move v0, v7

    goto :goto_0

    :cond_1
    move v7, v0

    :goto_0
    invoke-virtual {v1, v2, v7}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v0

    move-object v8, v0

    const/16 v0, 0x10

    invoke-static {v8, v0}, Ljava/lang/Long;->parseLong(Ljava/lang/String;I)J

    move-result-wide v9

    long-to-int v9, v9

    invoke-virtual {v1}, Ljava/lang/String;->length()I

    move-result v0

    if-ge v7, v0, :cond_2

    add-int/lit8 v0, v7, 0x1

    invoke-virtual {v1, v0}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v0

    move-object v1, v0

    goto :goto_1

    :cond_2
    const-string v0, ""
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_4
    .catchall {:try_start_0 .. :try_end_0} :catchall_1

    move-object v1, v0

    :goto_1
    move-object/from16 v10, p0

    :try_start_1
    invoke-direct {v10, v9}, Lcom/android/server/wm/WindowManagerService;->findWindow(I)Lcom/android/server/wm/WindowState;

    move-result-object v0
    :try_end_1
    .catch Ljava/lang/Exception; {:try_start_1 .. :try_end_1} :catch_3
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    move-object v11, v0

    if-nez v11, :cond_6

    nop

    if-eqz v4, :cond_3

    invoke-virtual {v4}, Landroid/os/Parcel;->recycle()V

    :cond_3
    if-eqz v5, :cond_4

    invoke-virtual {v5}, Landroid/os/Parcel;->recycle()V

    :cond_4
    if-eqz v6, :cond_5

    :try_start_2
    invoke-virtual {v6}, Ljava/io/BufferedWriter;->close()V
    :try_end_2
    .catch Ljava/io/IOException; {:try_start_2 .. :try_end_2} :catch_0

    goto :goto_2

    :catch_0
    move-exception v0

    :cond_5
    :goto_2
    return v2

    :cond_6
    :try_start_3
    invoke-static {}, Landroid/os/Parcel;->obtain()Landroid/os/Parcel;

    move-result-object v0

    move-object v4, v0

    const-string v0, "android.view.IWindow"

    invoke-virtual {v4, v0}, Landroid/os/Parcel;->writeInterfaceToken(Ljava/lang/String;)V
    :try_end_3
    .catch Ljava/lang/Exception; {:try_start_3 .. :try_end_3} :catch_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_0

    move-object/from16 v12, p2

    :try_start_4
    invoke-virtual {v4, v12}, Landroid/os/Parcel;->writeString(Ljava/lang/String;)V

    invoke-virtual {v4, v1}, Landroid/os/Parcel;->writeString(Ljava/lang/String;)V

    const/4 v0, 0x1

    invoke-virtual {v4, v0}, Landroid/os/Parcel;->writeInt(I)V

    invoke-static/range {p1 .. p1}, Landroid/os/ParcelFileDescriptor;->fromSocket(Ljava/net/Socket;)Landroid/os/ParcelFileDescriptor;

    move-result-object v13

    invoke-virtual {v13, v4, v2}, Landroid/os/ParcelFileDescriptor;->writeToParcel(Landroid/os/Parcel;I)V

    invoke-static {}, Landroid/os/Parcel;->obtain()Landroid/os/Parcel;

    move-result-object v13

    move-object v5, v13

    iget-object v13, v11, Lcom/android/server/wm/WindowState;->mClient:Landroid/view/IWindow;

    invoke-interface {v13}, Landroid/view/IWindow;->asBinder()Landroid/os/IBinder;

    move-result-object v13

    invoke-interface {v13, v0, v4, v5, v2}, Landroid/os/IBinder;->transact(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z

    invoke-virtual {v5}, Landroid/os/Parcel;->readException()V

    invoke-virtual/range {p1 .. p1}, Ljava/net/Socket;->isOutputShutdown()Z

    move-result v0

    if-nez v0, :cond_7

    new-instance v0, Ljava/io/BufferedWriter;

    new-instance v14, Ljava/io/OutputStreamWriter;

    invoke-virtual/range {p1 .. p1}, Ljava/net/Socket;->getOutputStream()Ljava/io/OutputStream;

    move-result-object v15

    invoke-direct {v14, v15}, Ljava/io/OutputStreamWriter;-><init>(Ljava/io/OutputStream;)V

    invoke-direct {v0, v14}, Ljava/io/BufferedWriter;-><init>(Ljava/io/Writer;)V

    move-object v6, v0

    const-string v0, "DONE\\n"

    invoke-virtual {v6, v0}, Ljava/io/BufferedWriter;->write(Ljava/lang/String;)V

    invoke-virtual {v6}, Ljava/io/BufferedWriter;->flush()V
    :try_end_4
    .catch Ljava/lang/Exception; {:try_start_4 .. :try_end_4} :catch_2
    .catchall {:try_start_4 .. :try_end_4} :catchall_2

    :cond_7
    if-eqz v4, :cond_8

    invoke-virtual {v4}, Landroid/os/Parcel;->recycle()V

    :cond_8
    if-eqz v5, :cond_9

    invoke-virtual {v5}, Landroid/os/Parcel;->recycle()V

    :cond_9
    if-eqz v6, :cond_d

    :try_start_5
    invoke-virtual {v6}, Ljava/io/BufferedWriter;->close()V
    :try_end_5
    .catch Ljava/io/IOException; {:try_start_5 .. :try_end_5} :catch_1

    :goto_3
    goto :goto_5

    :catch_1
    move-exception v0

    goto :goto_3

    :catch_2
    move-exception v0

    goto :goto_4

    :catchall_0
    move-exception v0

    move-object/from16 v12, p2

    move-object v2, v0

    goto :goto_6

    :catch_3
    move-exception v0

    move-object/from16 v12, p2

    goto :goto_4

    :catchall_1
    move-exception v0

    move-object/from16 v10, p0

    move-object/from16 v12, p2

    move-object v2, v0

    goto :goto_6

    :catch_4
    move-exception v0

    move-object/from16 v10, p0

    move-object/from16 v12, p2

    :goto_4
    :try_start_6
    sget-object v7, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    const/4 v8, 0x3

    aget-boolean v7, v7, v8

    if-eqz v7, :cond_a

    invoke-static {v12}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v7

    invoke-static {v1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    invoke-static {v0}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v9

    sget-object v11, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v7, v8, v9}, [Ljava/lang/Object;

    move-result-object v13

    const-wide v14, -0x6f4a88cc0709c259L

    invoke-static {v11, v14, v15, v2, v13}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V
    :try_end_6
    .catchall {:try_start_6 .. :try_end_6} :catchall_2

    :cond_a
    const/4 v3, 0x0

    if-eqz v4, :cond_b

    invoke-virtual {v4}, Landroid/os/Parcel;->recycle()V

    :cond_b
    if-eqz v5, :cond_c

    invoke-virtual {v5}, Landroid/os/Parcel;->recycle()V

    :cond_c
    if-eqz v6, :cond_d

    :try_start_7
    invoke-virtual {v6}, Ljava/io/BufferedWriter;->close()V
    :try_end_7
    .catch Ljava/io/IOException; {:try_start_7 .. :try_end_7} :catch_1

    goto :goto_3

    :cond_d
    :goto_5
    return v3

    :catchall_2
    move-exception v0

    move-object v2, v0

    :goto_6
    if-eqz v4, :cond_e

    invoke-virtual {v4}, Landroid/os/Parcel;->recycle()V

    :cond_e
    if-eqz v5, :cond_f

    invoke-virtual {v5}, Landroid/os/Parcel;->recycle()V

    :cond_f
    if-eqz v6, :cond_10

    :try_start_8
    invoke-virtual {v6}, Ljava/io/BufferedWriter;->close()V
    :try_end_8
    .catch Ljava/io/IOException; {:try_start_8 .. :try_end_8} :catch_5

    goto :goto_7

    :catch_5
    move-exception v0

    :cond_10
    :goto_7
    throw v2
.end method
""",
        "replacement": """\
.method viewServerWindowCommand(Ljava/net/Socket;Ljava/lang/String;Ljava/lang/String;)Z
    .registers 20

    goto :goto_0

    nop

    :goto_0
    move-object/from16 v1, p3

    goto :goto_42

    nop

    :goto_1
    if-nez v0, :cond_0

    goto :goto_9

    :cond_0
    goto :goto_8

    nop

    :goto_2
    move-object/from16 v12, p2

    goto :goto_41

    nop

    :goto_3
    invoke-virtual {v4}, Landroid/os/Parcel;->recycle()V

    :goto_4
    goto :goto_27

    nop

    :goto_5
    if-nez v5, :cond_1

    goto :goto_38

    :cond_1
    goto :goto_37

    nop

    :goto_6
    const/4 v4, 0x0

    goto :goto_40

    nop

    :goto_7
    move-object/from16 v12, p2

    goto :goto_c

    nop

    :goto_8
    return v2

    :goto_9
    goto :goto_17

    nop

    :goto_a
    invoke-virtual {v5}, Landroid/os/Parcel;->recycle()V

    :goto_b
    goto :goto_2a

    nop

    :goto_c
    move-object v2, v0

    goto :goto_49

    nop

    :goto_d
    invoke-virtual {v4}, Landroid/os/Parcel;->recycle()V

    :goto_e
    goto :goto_5

    nop

    :goto_f
    if-nez v4, :cond_2

    goto :goto_12

    :cond_2
    goto :goto_11

    nop

    :goto_10
    if-nez v5, :cond_3

    goto :goto_1c

    :cond_3
    goto :goto_1b

    nop

    :goto_11
    invoke-virtual {v4}, Landroid/os/Parcel;->recycle()V

    :goto_12
    goto :goto_30

    nop

    :goto_13
    const/4 v6, 0x0

    goto :goto_2d

    nop

    :goto_14
    move-object v2, v0

    :goto_15
    goto :goto_45

    nop

    :goto_16
    goto :goto_29

    :catchall_0
    move-exception v0

    goto :goto_2

    nop

    :goto_17
    const/4 v3, 0x1

    goto :goto_6

    nop

    :goto_18
    if-nez v6, :cond_4

    goto :goto_44

    :cond_4
    :try_start_0
    invoke-virtual {v6}, Ljava/io/BufferedWriter;->close()V
    :try_end_0
    .catch Ljava/io/IOException; {:try_start_0 .. :try_end_0} :catch_4

    goto :goto_43

    nop

    :goto_19
    move-object/from16 v10, p0

    goto :goto_28

    nop

    :goto_1a
    goto :goto_2b

    :catch_0
    move-exception v0

    goto :goto_16

    nop

    :goto_1b
    invoke-virtual {v5}, Landroid/os/Parcel;->recycle()V

    :goto_1c
    goto :goto_1e

    nop

    :goto_1d
    move-object/from16 v12, p2

    goto :goto_25

    nop

    :goto_1e
    if-nez v6, :cond_5

    goto :goto_24

    :cond_5
    :try_start_1
    invoke-virtual {v6}, Ljava/io/BufferedWriter;->close()V
    :try_end_1
    .catch Ljava/io/IOException; {:try_start_1 .. :try_end_1} :catch_2

    goto :goto_23

    nop

    :goto_1f
    goto :goto_15

    :catch_1
    move-exception v0

    goto :goto_1d

    nop

    :goto_20
    move-object v1, v0

    :goto_21
    goto :goto_22

    nop

    :goto_22
    move-object/from16 v10, p0

    :try_start_2
    invoke-direct {v10, v9}, Lcom/android/server/wm/WindowManagerService;->findWindow(I)Lcom/android/server/wm/WindowState;

    move-result-object v0
    :try_end_2
    .catch Ljava/lang/Exception; {:try_start_2 .. :try_end_2} :catch_1
    .catchall {:try_start_2 .. :try_end_2} :catchall_0

    goto :goto_3b

    nop

    :goto_23
    goto :goto_24

    :catch_2
    move-exception v0

    :goto_24
    goto :goto_47

    nop

    :goto_25
    goto :goto_29

    :catchall_1
    move-exception v0

    goto :goto_3f

    nop

    :goto_26
    goto :goto_3a

    :catch_3
    move-exception v0

    goto :goto_1a

    nop

    :goto_27
    if-nez v5, :cond_6

    goto :goto_33

    :cond_6
    goto :goto_32

    nop

    :goto_28
    move-object/from16 v12, p2

    :goto_29
    :try_start_3
    sget-object v7, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    const/4 v8, 0x3

    aget-boolean v7, v7, v8

    if-eqz v7, :cond_7

    invoke-static {v12}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v7

    invoke-static {v1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v8

    invoke-static {v0}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v9

    sget-object v11, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v7, v8, v9}, [Ljava/lang/Object;

    move-result-object v13

    const-wide v14, -0x6f4a88cc0709c259L

    invoke-static {v11, v14, v15, v2, v13}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V
    :try_end_3
    .catchall {:try_start_3 .. :try_end_3} :catchall_2

    :cond_7
    goto :goto_4a

    nop

    :goto_2a
    if-nez v6, :cond_8

    goto :goto_3a

    :cond_8
    :try_start_4
    invoke-virtual {v6}, Ljava/io/BufferedWriter;->close()V
    :try_end_4
    .catch Ljava/io/IOException; {:try_start_4 .. :try_end_4} :catch_3

    :goto_2b
    goto :goto_26

    nop

    :goto_2c
    move-object/from16 v12, p2

    :try_start_5
    invoke-virtual {v4, v12}, Landroid/os/Parcel;->writeString(Ljava/lang/String;)V

    invoke-virtual {v4, v1}, Landroid/os/Parcel;->writeString(Ljava/lang/String;)V

    const/4 v0, 0x1

    invoke-virtual {v4, v0}, Landroid/os/Parcel;->writeInt(I)V

    invoke-static/range {p1 .. p1}, Landroid/os/ParcelFileDescriptor;->fromSocket(Ljava/net/Socket;)Landroid/os/ParcelFileDescriptor;

    move-result-object v13

    invoke-virtual {v13, v4, v2}, Landroid/os/ParcelFileDescriptor;->writeToParcel(Landroid/os/Parcel;I)V

    invoke-static {}, Landroid/os/Parcel;->obtain()Landroid/os/Parcel;

    move-result-object v13

    move-object v5, v13

    iget-object v13, v11, Lcom/android/server/wm/WindowState;->mClient:Landroid/view/IWindow;

    invoke-interface {v13}, Landroid/view/IWindow;->asBinder()Landroid/os/IBinder;

    move-result-object v13

    invoke-interface {v13, v0, v4, v5, v2}, Landroid/os/IBinder;->transact(ILandroid/os/Parcel;Landroid/os/Parcel;I)Z

    invoke-virtual {v5}, Landroid/os/Parcel;->readException()V

    invoke-virtual/range {p1 .. p1}, Ljava/net/Socket;->isOutputShutdown()Z

    move-result v0

    if-nez v0, :cond_9

    new-instance v0, Ljava/io/BufferedWriter;

    new-instance v14, Ljava/io/OutputStreamWriter;

    invoke-virtual/range {p1 .. p1}, Ljava/net/Socket;->getOutputStream()Ljava/io/OutputStream;

    move-result-object v15

    invoke-direct {v14, v15}, Ljava/io/OutputStreamWriter;-><init>(Ljava/io/OutputStream;)V

    invoke-direct {v0, v14}, Ljava/io/BufferedWriter;-><init>(Ljava/io/Writer;)V

    move-object v6, v0

    const-string v0, "DONE\\n"

    invoke-virtual {v6, v0}, Ljava/io/BufferedWriter;->write(Ljava/lang/String;)V

    invoke-virtual {v6}, Ljava/io/BufferedWriter;->flush()V
    :try_end_5
    .catch Ljava/lang/Exception; {:try_start_5 .. :try_end_5} :catch_0
    .catchall {:try_start_5 .. :try_end_5} :catchall_2

    :cond_9
    goto :goto_f

    nop

    :goto_2d
    const/16 v0, 0x20

    :try_start_6
    invoke-virtual {v1, v0}, Ljava/lang/String;->indexOf(I)I

    move-result v0

    const/4 v7, -0x1

    if-ne v0, v7, :cond_a

    invoke-virtual {v1}, Ljava/lang/String;->length()I

    move-result v7

    move v0, v7

    goto :goto_2e

    :cond_a
    move v7, v0

    :goto_2e
    invoke-virtual {v1, v2, v7}, Ljava/lang/String;->substring(II)Ljava/lang/String;

    move-result-object v0

    move-object v8, v0

    const/16 v0, 0x10

    invoke-static {v8, v0}, Ljava/lang/Long;->parseLong(Ljava/lang/String;I)J

    move-result-wide v9

    long-to-int v9, v9

    invoke-virtual {v1}, Ljava/lang/String;->length()I

    move-result v0

    if-ge v7, v0, :cond_b

    add-int/lit8 v0, v7, 0x1

    invoke-virtual {v1, v0}, Ljava/lang/String;->substring(I)Ljava/lang/String;

    move-result-object v0

    move-object v1, v0

    goto :goto_21

    :cond_b
    const-string v0, ""
    :try_end_6
    .catch Ljava/lang/Exception; {:try_start_6 .. :try_end_6} :catch_5
    .catchall {:try_start_6 .. :try_end_6} :catchall_1

    goto :goto_20

    nop

    :goto_2f
    if-nez v4, :cond_c

    goto :goto_3e

    :cond_c
    goto :goto_3d

    nop

    :goto_30
    if-nez v5, :cond_d

    goto :goto_b

    :cond_d
    goto :goto_a

    nop

    :goto_31
    const/4 v2, 0x0

    goto :goto_1

    nop

    :goto_32
    invoke-virtual {v5}, Landroid/os/Parcel;->recycle()V

    :goto_33
    goto :goto_18

    nop

    :goto_34
    if-eqz v11, :cond_e

    goto :goto_48

    :cond_e
    nop

    goto :goto_2f

    nop

    :goto_35
    throw v2

    :goto_36
    if-nez v4, :cond_f

    goto :goto_e

    :cond_f
    goto :goto_d

    nop

    :goto_37
    invoke-virtual {v5}, Landroid/os/Parcel;->recycle()V

    :goto_38
    goto :goto_46

    nop

    :goto_39
    goto :goto_2b

    :goto_3a
    goto :goto_3c

    nop

    :goto_3b
    move-object v11, v0

    goto :goto_34

    nop

    :goto_3c
    return v3

    :catchall_2
    move-exception v0

    goto :goto_14

    nop

    :goto_3d
    invoke-virtual {v4}, Landroid/os/Parcel;->recycle()V

    :goto_3e
    goto :goto_10

    nop

    :goto_3f
    move-object/from16 v10, p0

    goto :goto_7

    nop

    :goto_40
    const/4 v5, 0x0

    goto :goto_13

    nop

    :goto_41
    move-object v2, v0

    goto :goto_1f

    nop

    :goto_42
    invoke-direct/range {p0 .. p0}, Lcom/android/server/wm/WindowManagerService;->isSystemSecure()Z

    move-result v0

    goto :goto_31

    nop

    :goto_43
    goto :goto_44

    :catch_4
    move-exception v0

    :goto_44
    goto :goto_35

    nop

    :goto_45
    if-nez v4, :cond_10

    goto :goto_4

    :cond_10
    goto :goto_3

    nop

    :goto_46
    if-nez v6, :cond_11

    goto :goto_3a

    :cond_11
    :try_start_7
    invoke-virtual {v6}, Ljava/io/BufferedWriter;->close()V
    :try_end_7
    .catch Ljava/io/IOException; {:try_start_7 .. :try_end_7} :catch_3

    goto :goto_39

    nop

    :goto_47
    return v2

    :goto_48
    :try_start_8
    invoke-static {}, Landroid/os/Parcel;->obtain()Landroid/os/Parcel;

    move-result-object v0

    move-object v4, v0

    const-string v0, "android.view.IWindow"

    invoke-virtual {v4, v0}, Landroid/os/Parcel;->writeInterfaceToken(Ljava/lang/String;)V
    :try_end_8
    .catch Ljava/lang/Exception; {:try_start_8 .. :try_end_8} :catch_1
    .catchall {:try_start_8 .. :try_end_8} :catchall_0

    goto :goto_2c

    nop

    :goto_49
    goto :goto_15

    :catch_5
    move-exception v0

    goto :goto_19

    nop

    :goto_4a
    const/4 v3, 0x0

    goto :goto_36

    nop
.end method
""",
        "method_anchors": ['invoke-direct/range {p0 .. p0}, Lcom/android/server/wm/WindowManagerService;->isSystemSecure()Z', 'move-result v0', 'if-eqz v0, :cond_0', 'return v2', 'invoke-virtual {v1, v0}, Ljava/lang/String;->indexOf(I)I', 'move-result v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_windowForClientLocked_Lcom_android_server_wm_Session_Landroi",
        "method":      ".method final windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;",
        "method_name": 'windowForClientLocked',
        "type":        "method_replace",
        "search": """\
.method final windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;
    .registers 14

    const-string v0, "com.android.server.wm.WindowManagerService.windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    invoke-virtual {v1, p2}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/wm/WindowState;

    sget-boolean v2, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG:Z

    if-eqz v2, :cond_0

    const-string v2, "WindowManager"

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "Looking up client "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, ": "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v2, v3}, Landroid/util/Slog;->v(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    :cond_0
    const/4 v2, 0x0

    const-wide v3, 0x3924ad9401f7368cL

    const-string v5, "Requested window "

    const/4 v6, 0x0

    const/4 v7, 0x3

    if-nez v1, :cond_3

    if-nez p3, :cond_2

    :try_start_1
    sget-object v5, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    aget-boolean v5, v5, v7

    if-eqz v5, :cond_1

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    invoke-static {v7}, Landroid/os/Debug;->getCallers(I)Ljava/lang/String;

    move-result-object v7

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v7

    sget-object v8, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v5, v7}, [Ljava/lang/Object;

    move-result-object v9

    invoke-static {v8, v3, v4, v2, v9}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_1
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-object v6

    :cond_2
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, " does not exist"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2

    :cond_3
    if-eqz p1, :cond_6

    iget-object v8, v1, Lcom/android/server/wm/WindowState;->mSession:Lcom/android/server/wm/Session;

    if-eq v8, p1, :cond_6

    if-nez p3, :cond_5

    sget-object v5, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    aget-boolean v5, v5, v7

    if-eqz v5, :cond_4

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    invoke-static {v7}, Landroid/os/Debug;->getCallers(I)Ljava/lang/String;

    move-result-object v7

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v7

    sget-object v8, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v5, v7}, [Ljava/lang/Object;

    move-result-object v9

    invoke-static {v8, v3, v4, v2, v9}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_4
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-object v6

    :cond_5
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, " is in session "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, v1, Lcom/android/server/wm/WindowState;->mSession:Lcom/android/server/wm/Session;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, ", not "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2

    :cond_6
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    return-object v1

    :catchall_0
    move-exception p1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw p1
.end method
""",
        "replacement": """\
.method final windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;
    .registers 14

    goto :goto_6

    nop

    :goto_0
    const-string v5, "Requested window "

    goto :goto_4

    nop

    :goto_1
    if-eqz p3, :cond_0

    goto :goto_2

    :cond_0
    :try_start_0
    sget-object v5, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    aget-boolean v5, v5, v7

    if-eqz v5, :cond_1

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    invoke-static {v7}, Landroid/os/Debug;->getCallers(I)Ljava/lang/String;

    move-result-object v7

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v7

    sget-object v8, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v5, v7}, [Ljava/lang/Object;

    move-result-object v9

    invoke-static {v8, v3, v4, v2, v9}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_1
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-object v6

    :goto_2
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, " does not exist"

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2

    :goto_3
    if-eqz p1, :cond_4

    iget-object v8, v1, Lcom/android/server/wm/WindowState;->mSession:Lcom/android/server/wm/Session;

    if-eq v8, p1, :cond_4

    if-nez p3, :cond_3

    sget-object v5, Lcom/android/internal/protolog/ProtoLogImpl_232878649$Cache;->WM_ERROR_enabled:[Z

    aget-boolean v5, v5, v7

    if-eqz v5, :cond_2

    invoke-static {p1}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v5

    invoke-static {v7}, Landroid/os/Debug;->getCallers(I)Ljava/lang/String;

    move-result-object v7

    invoke-static {v7}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;

    move-result-object v7

    sget-object v8, Lcom/android/internal/protolog/WmProtoLogGroups;->WM_ERROR:Lcom/android/internal/protolog/WmProtoLogGroups;

    filled-new-array {v5, v7}, [Ljava/lang/Object;

    move-result-object v9

    invoke-static {v8, v3, v4, v2, v9}, Lcom/android/internal/protolog/ProtoLogImpl_232878649;->w(Lcom/android/internal/protolog/common/IProtoLogGroup;JI[Ljava/lang/Object;)V

    :cond_2
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    return-object v6

    :cond_3
    new-instance v2, Ljava/lang/IllegalArgumentException;

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    invoke-virtual {v3, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, " is in session "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    iget-object v4, v1, Lcom/android/server/wm/WindowState;->mSession:Lcom/android/server/wm/Session;

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, ", not "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-direct {v2, v3}, Ljava/lang/IllegalArgumentException;-><init>(Ljava/lang/String;)V

    throw v2

    :cond_4
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_5

    nop

    :goto_4
    const/4 v6, 0x0

    goto :goto_c

    nop

    :goto_5
    return-object v1

    :catchall_0
    move-exception p1

    goto :goto_8

    nop

    :goto_6
    const-string v0, "com.android.server.wm.WindowManagerService.windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;"

    goto :goto_9

    nop

    :goto_7
    const/4 v2, 0x0

    goto :goto_b

    nop

    :goto_8
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_d

    nop

    :goto_9
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_1
    iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;

    invoke-virtual {v1, p2}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/server/wm/WindowState;

    sget-boolean v2, Lcom/android/server/wm/WindowManagerDebugConfig;->DEBUG:Z

    if-eqz v2, :cond_5

    const-string v2, "WindowManager"

    new-instance v3, Ljava/lang/StringBuilder;

    invoke-direct {v3}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "Looking up client "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, p2}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    const-string v4, ": "

    invoke-virtual {v3, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3, v1}, Ljava/lang/StringBuilder;->append(Ljava/lang/Object;)Ljava/lang/StringBuilder;

    move-result-object v3

    invoke-virtual {v3}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v3

    invoke-static {v2, v3}, Landroid/util/Slog;->v(Ljava/lang/String;Ljava/lang/String;)I
    :try_end_1
    .catchall {:try_start_1 .. :try_end_1} :catchall_0

    :cond_5
    goto :goto_7

    nop

    :goto_a
    if-eqz v1, :cond_6

    goto :goto_3

    :cond_6
    goto :goto_1

    nop

    :goto_b
    const-wide v3, 0x3924ad9401f7368cL

    goto :goto_0

    nop

    :goto_c
    const/4 v7, 0x3

    goto :goto_a

    nop

    :goto_d
    throw p1
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'iget-object v1, p0, Lcom/android/server/wm/WindowManagerService;->mWindowMap:Ljava/util/HashMap;', 'invoke-virtual {v1, p2}, Ljava/util/HashMap;->get(Ljava/lang/Object;)Ljava/lang/Object;', 'move-result-object v1', 'check-cast v1, Lcom/android/server/wm/WindowState;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
    {
        "id":          "replace_method_windowForClientLocked_Lcom_android_server_wm_Session_Landroi",
        "method":      ".method final windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;",
        "method_name": 'windowForClientLocked',
        "type":        "method_replace",
        "search": """\
.method final windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;
    .registers 6

    const-string v0, "com.android.server.wm.WindowManagerService.windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;"

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    invoke-interface {p2}, Landroid/view/IWindow;->asBinder()Landroid/os/IBinder;

    move-result-object v1

    invoke-virtual {p0, p1, v1, p3}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;

    move-result-object v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    return-object v1

    :catchall_0
    move-exception p1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    throw p1
.end method
""",
        "replacement": """\
.method final windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;
    .registers 6

    goto :goto_0

    nop

    :goto_0
    const-string v0, "com.android.server.wm.WindowManagerService.windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;"

    goto :goto_4

    nop

    :goto_1
    return-object v1

    :catchall_0
    move-exception p1

    goto :goto_2

    nop

    :goto_2
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V

    goto :goto_3

    nop

    :goto_3
    throw p1

    :goto_4
    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V

    :try_start_0
    invoke-interface {p2}, Landroid/view/IWindow;->asBinder()Landroid/os/IBinder;

    move-result-object v1

    invoke-virtual {p0, p1, v1, p3}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;

    move-result-object v1

    invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfEnd(Ljava/lang/String;)V
    :try_end_0
    .catchall {:try_start_0 .. :try_end_0} :catchall_0

    goto :goto_1

    nop
.end method
""",
        "method_anchors": ['const-string v0, "com.android.server.wm.WindowManagerService.windowForClientLocked(Lcom/android/server/wm/Session;Landroid/view/IWindow;Z)Lcom/android/server/wm/WindowState;"', 'invoke-static {v0}, Lcom/android/server/LockPerfHelper;->onPerfStart(Ljava/lang/String;)V', 'invoke-interface {p2}, Landroid/view/IWindow;->asBinder()Landroid/os/IBinder;', 'move-result-object v1', 'invoke-virtual {p0, p1, v1, p3}, Lcom/android/server/wm/WindowManagerService;->windowForClientLocked(Lcom/android/server/wm/Session;Landroid/os/IBinder;Z)Lcom/android/server/wm/WindowState;', 'move-result-object v1'],
        "required":    True,
        "reason":      "Legend MTCR modified method from Service_Legend.mtcr",
    },
]
