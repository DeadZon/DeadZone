"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-services.jar
Target class : com/android/server/am/ProcessManagerService
Source MTCR  : miui-services_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-services.jar"
TARGET_CLASS = "com/android/server/am/ProcessManagerService.smali"
CLASS_FALLBACK_NAMES = ['ProcessManagerService.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "replace_method_isForceStopEnable_Lcom_android_server_am_ProcessRecord_I_Z",
        "method":      ".method public isForceStopEnable(Lcom/android/server/am/ProcessRecord;I)Z",
        "method_name": 'isForceStopEnable',
        "type":        "method_replace",
        "search": """\
.method public isForceStopEnable(Lcom/android/server/am/ProcessRecord;I)Z
    .registers 7

    const/16 v0, 0xd

    const/4 v1, 0x1

    if-ne p2, v0, :cond_0

    return v1

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v2, 0x0

    if-eqz v0, :cond_1

    return v2

    :cond_1
    invoke-direct {p0, p1}, Lcom/android/server/am/ProcessManagerService;->isSystemApp(Lcom/android/server/am/ProcessRecord;)Z

    move-result v0

    if-eqz v0, :cond_2

    return v2

    :cond_2
    iget-object v0, p1, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v0, v0, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget-object v3, p1, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget v3, v3, Landroid/content/pm/ApplicationInfo;->uid:I

    invoke-virtual {p0, v0, v3}, Lcom/android/server/am/ProcessManagerService;->isAllowAutoStart(Ljava/lang/String;I)Z

    move-result v0

    if-eqz v0, :cond_3

    return v2

    :cond_3
    iget-object v0, p1, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v0, v0, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    const/16 v3, 0x22

    invoke-direct {p0, v0, v3}, Lcom/android/server/am/ProcessManagerService;->isPackageInList(Ljava/lang/String;I)Z

    move-result v0

    if-eqz v0, :cond_4

    return v2

    :cond_4
    return v1
.end method
""",
        "replacement": """\
.method public isForceStopEnable(Lcom/android/server/am/ProcessRecord;I)Z
    .registers 7

    const/16 v0, 0xd

    const/4 v1, 0x1

    if-ne p2, v0, :cond_0

    return v1

    :cond_0
    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v0, 0x1

    const/4 v2, 0x0

    if-eqz v0, :cond_1

    return v2

    :cond_1
    invoke-direct {p0, p1}, Lcom/android/server/am/ProcessManagerService;->isSystemApp(Lcom/android/server/am/ProcessRecord;)Z

    move-result v0

    if-eqz v0, :cond_2

    return v2

    :cond_2
    iget-object v0, p1, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v0, v0, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget-object v3, p1, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget v3, v3, Landroid/content/pm/ApplicationInfo;->uid:I

    invoke-virtual {p0, v0, v3}, Lcom/android/server/am/ProcessManagerService;->isAllowAutoStart(Ljava/lang/String;I)Z

    move-result v0

    if-eqz v0, :cond_3

    return v2

    :cond_3
    iget-object v0, p1, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v0, v0, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    const/16 v3, 0x22

    invoke-direct {p0, v0, v3}, Lcom/android/server/am/ProcessManagerService;->isPackageInList(Ljava/lang/String;I)Z

    move-result v0

    if-eqz v0, :cond_4

    return v2

    :cond_4
    return v1
.end method
""",
        "method_anchors": ['if-ne p2, v0, :cond_0', 'return v1', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_1', 'return v2', 'invoke-direct {p0, p1}, Lcom/android/server/am/ProcessManagerService;->isSystemApp(Lcom/android/server/am/ProcessRecord;)Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
]
