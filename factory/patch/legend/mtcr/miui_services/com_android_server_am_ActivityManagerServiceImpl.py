"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-services.jar
Target class : com/android/server/am/ActivityManagerServiceImpl
Source MTCR  : miui-services_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-services.jar"
TARGET_CLASS = "com/android/server/am/ActivityManagerServiceImpl.smali"
CLASS_FALLBACK_NAMES = ['ActivityManagerServiceImpl.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "replace_method_ensureDeviceProvisioned_Landroid_content_Context__V",
        "method":      ".method private static ensureDeviceProvisioned(Landroid/content/Context;)V",
        "method_name": 'ensureDeviceProvisioned',
        "type":        "method_replace",
        "search": """\
.method private static ensureDeviceProvisioned(Landroid/content/Context;)V
    .registers 8

    invoke-static {p0}, Lcom/android/server/am/ActivityManagerServiceImpl;->isDeviceProvisioned(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_2

    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v0

    sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const-string v2, "com.android.provision.activities.DefaultActivity"

    const-string v3, "com.android.provision"

    if-nez v1, :cond_0

    new-instance v1, Landroid/content/ComponentName;

    invoke-direct {v1, v3, v2}, Landroid/content/ComponentName;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_0

    :cond_0
    new-instance v1, Landroid/content/ComponentName;

    const-string v4, "com.google.android.setupwizard"

    const-string v5, "com.google.android.setupwizard.SetupWizardActivity"

    invoke-direct {v1, v4, v5}, Landroid/content/ComponentName;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    :goto_0
    if-eqz v0, :cond_2

    invoke-virtual {v0, v1}, Landroid/content/pm/PackageManager;->getComponentEnabledSetting(Landroid/content/ComponentName;)I

    move-result v4

    const/4 v5, 0x2

    if-ne v4, v5, :cond_2

    const-string v4, "ActivityManagerServiceImpl"

    const-string v5, "The device provisioned state is inconsistent,try to restore."

    invoke-static {v4, v5}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v4

    const-string v5, "device_provisioned"

    const/4 v6, 0x1

    invoke-static {v4, v5, v6}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    sget-boolean v4, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v4, :cond_1

    new-instance v4, Landroid/content/ComponentName;

    invoke-direct {v4, v3, v2}, Landroid/content/ComponentName;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0, v4, v6, v6}, Landroid/content/pm/PackageManager;->setComponentEnabledSetting(Landroid/content/ComponentName;II)V

    new-instance v2, Landroid/content/Intent;

    const-string v3, "android.intent.action.MAIN"

    invoke-direct {v2, v3}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-virtual {v2, v4}, Landroid/content/Intent;->setComponent(Landroid/content/ComponentName;)Landroid/content/Intent;

    const/high16 v3, 0x10000000

    invoke-virtual {v2, v3}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    const-string v3, "android.intent.category.HOME"

    invoke-virtual {v2, v3}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {p0, v2}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V

    goto :goto_1

    :cond_1
    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    const-string v3, "user_setup_complete"

    invoke-static {v2, v3, v6}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_2
    :goto_1
    return-void
.end method
""",
        "replacement": """\
.method private static ensureDeviceProvisioned(Landroid/content/Context;)V
    .registers 8

    invoke-static {p0}, Lcom/android/server/am/ActivityManagerServiceImpl;->isDeviceProvisioned(Landroid/content/Context;)Z

    move-result v0

    if-nez v0, :cond_2

    invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;

    move-result-object v0

    sget-boolean v1, Lmiui/os/Build;->IS_MIUI:Z

    const-string v2, "com.android.provision.activities.DefaultActivity"

    const-string v3, "com.android.provision"

    if-nez v1, :cond_0

    new-instance v1, Landroid/content/ComponentName;

    invoke-direct {v1, v3, v2}, Landroid/content/ComponentName;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    goto :goto_0

    :cond_0
    new-instance v1, Landroid/content/ComponentName;

    const-string v4, "com.google.android.setupwizard"

    const-string v5, "com.google.android.setupwizard.SetupWizardActivity"

    invoke-direct {v1, v4, v5}, Landroid/content/ComponentName;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    :goto_0
    if-eqz v0, :cond_2

    invoke-virtual {v0, v1}, Landroid/content/pm/PackageManager;->getComponentEnabledSetting(Landroid/content/ComponentName;)I

    move-result v4

    const/4 v5, 0x2

    if-ne v4, v5, :cond_2

    const-string v4, "ActivityManagerServiceImpl"

    const-string v5, "The device provisioned state is inconsistent,try to restore."

    invoke-static {v4, v5}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;)I

    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v4

    const-string v5, "device_provisioned"

    const/4 v6, 0x1

    invoke-static {v4, v5, v6}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    sget-boolean v4, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v4, :cond_1

    new-instance v4, Landroid/content/ComponentName;

    invoke-direct {v4, v3, v2}, Landroid/content/ComponentName;-><init>(Ljava/lang/String;Ljava/lang/String;)V

    invoke-virtual {v0, v4, v6, v6}, Landroid/content/pm/PackageManager;->setComponentEnabledSetting(Landroid/content/ComponentName;II)V

    new-instance v2, Landroid/content/Intent;

    const-string v3, "android.intent.action.MAIN"

    invoke-direct {v2, v3}, Landroid/content/Intent;-><init>(Ljava/lang/String;)V

    invoke-virtual {v2, v4}, Landroid/content/Intent;->setComponent(Landroid/content/ComponentName;)Landroid/content/Intent;

    const/high16 v3, 0x10000000

    invoke-virtual {v2, v3}, Landroid/content/Intent;->addFlags(I)Landroid/content/Intent;

    const-string v3, "android.intent.category.HOME"

    invoke-virtual {v2, v3}, Landroid/content/Intent;->addCategory(Ljava/lang/String;)Landroid/content/Intent;

    invoke-virtual {p0, v2}, Landroid/content/Context;->startActivity(Landroid/content/Intent;)V

    goto :goto_1

    :cond_1
    invoke-virtual {p0}, Landroid/content/Context;->getContentResolver()Landroid/content/ContentResolver;

    move-result-object v2

    const-string v3, "user_setup_complete"

    invoke-static {v2, v3, v6}, Landroid/provider/Settings$Secure;->putInt(Landroid/content/ContentResolver;Ljava/lang/String;I)Z

    :cond_2
    :goto_1
    return-void
.end method
""",
        "method_anchors": ['invoke-static {p0}, Lcom/android/server/am/ActivityManagerServiceImpl;->isDeviceProvisioned(Landroid/content/Context;)Z', 'move-result v0', 'if-nez v0, :cond_2', 'invoke-virtual {p0}, Landroid/content/Context;->getPackageManager()Landroid/content/pm/PackageManager;', 'move-result-object v0', 'sget-boolean v1, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z'],
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
    {
        "id":          "replace_method_checkRunningCompatibility_Landroid_app_IApplicationThread_La",
        "method":      ".method public checkRunningCompatibility(Landroid/app/IApplicationThread;Landroid/content/pm/ActivityInfo;Landroid/content/Intent;ILjava/lang/String;)Z",
        "method_name": 'checkRunningCompatibility',
        "type":        "method_replace",
        "search": """\
.method public checkRunningCompatibility(Landroid/app/IApplicationThread;Landroid/content/pm/ActivityInfo;Landroid/content/Intent;ILjava/lang/String;)Z
    .registers 16

    if-nez p2, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    iget-object v0, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mAmService:Lcom/android/server/am/ActivityManagerService;

    iget-object v0, v0, Lcom/android/server/am/ActivityManagerService;->mActivityTaskManager:Lcom/android/server/wm/ActivityTaskManagerService;

    invoke-static {v0, p1}, Lcom/android/server/wm/WindowProcessUtils;->getCallerInfo(Lcom/android/server/wm/ActivityTaskManagerService;Landroid/app/IApplicationThread;)Lmiui/security/CallerInfo;

    move-result-object v3

    if-eqz v3, :cond_1

    invoke-static {}, Landroid/app/PrivacyTestModeStub;->get()Landroid/app/PrivacyTestModeStub;

    move-result-object v4

    iget-object v5, v3, Lmiui/security/CallerInfo;->callerProcessName:Ljava/lang/String;

    iget-object v9, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mContext:Landroid/content/Context;

    move-object v6, p2

    move-object v7, p3

    move-object v8, p5

    invoke-virtual/range {v4 .. v9}, Landroid/app/PrivacyTestModeStub;->collectPrivacyTestModeInfo(Ljava/lang/String;Landroid/content/pm/ActivityInfo;Landroid/content/Intent;Ljava/lang/String;Landroid/content/Context;)V

    move-object v5, v7

    move-object v4, v8

    goto :goto_0

    :cond_1
    move-object v6, p2

    move-object v5, p3

    move-object v4, p5

    :goto_0
    iget-object p2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez p2, :cond_2

    const-class p2, Lmiui/security/SecurityManagerInternal;

    invoke-static {p2}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object p2

    check-cast p2, Lmiui/security/SecurityManagerInternal;

    iput-object p2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_2
    sget-boolean p2, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz p2, :cond_3

    const-string p2, "com.android.chrome"

    invoke-static {v4, p2}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p3

    if-eqz p3, :cond_3

    iget-object p3, v6, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget-object p3, p3, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-static {p2, p3}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p2

    if-nez p2, :cond_3

    sget-object p2, Lcom/android/server/am/ActivityManagerServiceImpl;->sCalleeWhiteList:Ljava/util/ArrayList;

    iget-object p3, v6, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget-object p3, p3, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-virtual {p2, p3}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result p2

    if-nez p2, :cond_3

    iget-object p2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-eqz p2, :cond_3

    iget-object p2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    invoke-virtual {p2}, Lmiui/security/SecurityManagerInternal;->isAllowedDeviceProvision()Z

    move-result p2

    if-nez p2, :cond_3

    const/4 p2, 0x0

    return p2

    :cond_3
    iget-object v2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mAmService:Lcom/android/server/am/ActivityManagerService;

    const/4 v7, 0x1

    move-object v1, p0

    move v8, p4

    invoke-virtual/range {v1 .. v8}, Lcom/android/server/am/ActivityManagerServiceImpl;->checkWakePath(Lcom/android/server/am/ActivityManagerService;Lmiui/security/CallerInfo;Ljava/lang/String;Landroid/content/Intent;Landroid/content/pm/ComponentInfo;II)Z

    move-result p2

    return p2
.end method
""",
        "replacement": """\
.method public checkRunningCompatibility(Landroid/app/IApplicationThread;Landroid/content/pm/ActivityInfo;Landroid/content/Intent;ILjava/lang/String;)Z
    .registers 16

    if-nez p2, :cond_0

    const/4 v0, 0x1

    return v0

    :cond_0
    iget-object v0, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mAmService:Lcom/android/server/am/ActivityManagerService;

    iget-object v0, v0, Lcom/android/server/am/ActivityManagerService;->mActivityTaskManager:Lcom/android/server/wm/ActivityTaskManagerService;

    invoke-static {v0, p1}, Lcom/android/server/wm/WindowProcessUtils;->getCallerInfo(Lcom/android/server/wm/ActivityTaskManagerService;Landroid/app/IApplicationThread;)Lmiui/security/CallerInfo;

    move-result-object v3

    if-eqz v3, :cond_1

    invoke-static {}, Landroid/app/PrivacyTestModeStub;->get()Landroid/app/PrivacyTestModeStub;

    move-result-object v4

    iget-object v5, v3, Lmiui/security/CallerInfo;->callerProcessName:Ljava/lang/String;

    iget-object v9, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mContext:Landroid/content/Context;

    move-object v6, p2

    move-object v7, p3

    move-object v8, p5

    invoke-virtual/range {v4 .. v9}, Landroid/app/PrivacyTestModeStub;->collectPrivacyTestModeInfo(Ljava/lang/String;Landroid/content/pm/ActivityInfo;Landroid/content/Intent;Ljava/lang/String;Landroid/content/Context;)V

    move-object v5, v7

    move-object v4, v8

    goto :goto_0

    :cond_1
    move-object v6, p2

    move-object v5, p3

    move-object v4, p5

    :goto_0
    iget-object p2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez p2, :cond_2

    const-class p2, Lmiui/security/SecurityManagerInternal;

    invoke-static {p2}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object p2

    check-cast p2, Lmiui/security/SecurityManagerInternal;

    iput-object p2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_2
    sget-boolean p2, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz p2, :cond_3

    const-string p2, "com.android.chrome"

    invoke-static {v4, p2}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p3

    if-eqz p3, :cond_3

    iget-object p3, v6, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget-object p3, p3, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-static {p2, p3}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result p2

    if-nez p2, :cond_3

    sget-object p2, Lcom/android/server/am/ActivityManagerServiceImpl;->sCalleeWhiteList:Ljava/util/ArrayList;

    iget-object p3, v6, Landroid/content/pm/ActivityInfo;->applicationInfo:Landroid/content/pm/ApplicationInfo;

    iget-object p3, p3, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-virtual {p2, p3}, Ljava/util/ArrayList;->contains(Ljava/lang/Object;)Z

    move-result p2

    if-nez p2, :cond_3

    iget-object p2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-eqz p2, :cond_3

    iget-object p2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    invoke-virtual {p2}, Lmiui/security/SecurityManagerInternal;->isAllowedDeviceProvision()Z

    move-result p2

    if-nez p2, :cond_3

    const/4 p2, 0x0

    return p2

    :cond_3
    iget-object v2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mAmService:Lcom/android/server/am/ActivityManagerService;

    const/4 v7, 0x1

    move-object v1, p0

    move v8, p4

    invoke-virtual/range {v1 .. v8}, Lcom/android/server/am/ActivityManagerServiceImpl;->checkWakePath(Lcom/android/server/am/ActivityManagerService;Lmiui/security/CallerInfo;Ljava/lang/String;Landroid/content/Intent;Landroid/content/pm/ComponentInfo;II)Z

    move-result p2

    return p2
.end method
""",
        "method_anchors": ['if-nez p2, :cond_0', 'return v0', 'iget-object v0, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mAmService:Lcom/android/server/am/ActivityManagerService;', 'iget-object v0, v0, Lcom/android/server/am/ActivityManagerService;->mActivityTaskManager:Lcom/android/server/wm/ActivityTaskManagerService;', 'invoke-static {v0, p1}, Lcom/android/server/wm/WindowProcessUtils;->getCallerInfo(Lcom/android/server/wm/ActivityTaskManagerService;Landroid/app/IApplicationThread;)Lmiui/security/CallerInfo;', 'move-result-object v3'],
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
    {
        "id":          "replace_method_checkRunningCompatibility_Landroid_content_ComponentName_III",
        "method":      ".method public checkRunningCompatibility(Landroid/content/ComponentName;III)Z",
        "method_name": 'checkRunningCompatibility',
        "type":        "method_replace",
        "search": """\
.method public checkRunningCompatibility(Landroid/content/ComponentName;III)Z
    .registers 18

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    const/4 v1, 0x1

    if-eqz v0, :cond_0

    return v1

    :cond_0
    if-eqz p1, :cond_d

    invoke-static {}, Landroid/miui/AppOpsUtils;->isXOptMode()Z

    move-result v0

    if-nez v0, :cond_d

    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/miui/AppOpsUtils;->isExceptionByTestPolicy(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_1

    move/from16 v4, p3

    goto :goto_4

    :cond_1
    invoke-static {p2}, Landroid/os/UserHandle;->getAppId(I)I

    move-result v0

    const/16 v2, 0x3e8

    if-eq v0, v2, :cond_c

    if-eqz v0, :cond_c

    const/16 v2, 0x7d0

    if-ne v0, v2, :cond_2

    move/from16 v4, p3

    goto :goto_3

    :cond_2
    iget-object v2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v2, :cond_3

    const-class v2, Lmiui/security/SecurityManagerInternal;

    invoke-static {v2}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lmiui/security/SecurityManagerInternal;

    iput-object v2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_3
    iget-object v2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v2, :cond_4

    return v1

    :cond_4
    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v5

    invoke-static/range {p3 .. p3}, Lcom/android/server/am/ProcessUtils;->getProcessRecordByPid(I)Lcom/android/server/am/ProcessRecord;

    move-result-object v2

    const/4 v10, 0x0

    const-string v3, "ActivityManagerServiceImpl"

    if-eqz v2, :cond_b

    iget-object v4, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    if-nez v4, :cond_5

    goto :goto_2

    :cond_5
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v6, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v6, v6, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v6, ":widgetProvider"

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v11

    sget-object v4, Lcom/android/server/am/ActivityManagerServiceImpl;->WIDGET_PROVIDER_WHITE_LIST:Ljava/util/List;

    iget-object v6, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v6, v6, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-interface {v4, v6}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_6

    iget-object v4, v2, Lcom/android/server/am/ProcessRecord;->processName:Ljava/lang/String;

    invoke-virtual {v11, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_6

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "MIUILOG- Reject widget call from "

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    iget-object v6, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v6, v6, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v3, v4}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v3, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    iget-object v4, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v4, v4, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget v6, v2, Lcom/android/server/am/ProcessRecord;->uid:I

    invoke-static {v6}, Landroid/os/UserHandle;->getUserId(I)I

    move-result v7

    const/4 v6, 0x0

    const/4 v9, 0x0

    move/from16 v8, p4

    invoke-virtual/range {v3 .. v9}, Lmiui/security/SecurityManagerInternal;->recordWakePathCall(Ljava/lang/String;Ljava/lang/String;IIIZ)V

    :cond_6
    iget-object v3, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v3, v3, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    if-nez v3, :cond_a

    iget-object v3, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v3, v3, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-static {v3, v5}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v3

    if-eqz v3, :cond_7

    goto :goto_1

    :cond_7
    iget-object v3, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mPackageManager:Landroid/content/pm/PackageManagerInternal;

    invoke-static {}, Landroid/os/Process;->myUid()I

    move-result v7

    move-object v4, v5

    const-wide/16 v5, 0x0

    move/from16 v8, p4

    invoke-virtual/range {v3 .. v8}, Landroid/content/pm/PackageManagerInternal;->getApplicationInfo(Ljava/lang/String;JII)Landroid/content/pm/ApplicationInfo;

    move-result-object v12

    move-object v5, v4

    if-eqz v12, :cond_9

    iget-object v3, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mAmService:Lcom/android/server/am/ActivityManagerService;

    iget-object v3, v3, Lcom/android/server/am/ActivityManagerService;->mActivityTaskManager:Lcom/android/server/wm/ActivityTaskManagerService;

    iget-object v4, v12, Landroid/content/pm/ApplicationInfo;->processName:Ljava/lang/String;

    iget v6, v12, Landroid/content/pm/ApplicationInfo;->uid:I

    invoke-static {v3, v5, v4, v6}, Lcom/android/server/wm/WindowProcessUtils;->isPackageRunning(Lcom/android/server/wm/ActivityTaskManagerService;Ljava/lang/String;Ljava/lang/String;I)Z

    move-result v3

    if-eqz v3, :cond_8

    goto :goto_0

    :cond_8
    iget-object v3, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    iget-object v1, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v4, v1, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget v1, v2, Lcom/android/server/am/ProcessRecord;->uid:I

    invoke-static {v1}, Landroid/os/UserHandle;->getUserId(I)I

    move-result v7

    const/4 v6, 0x0

    const/4 v9, 0x0

    move/from16 v8, p4

    invoke-virtual/range {v3 .. v9}, Lmiui/security/SecurityManagerInternal;->recordWakePathCall(Ljava/lang/String;Ljava/lang/String;IIIZ)V

    return v10

    :cond_9
    :goto_0
    return v1

    :cond_a
    :goto_1
    return v1

    :cond_b
    :goto_2
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "MIUILOG- Reject call from dying process "

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    move/from16 v4, p3

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v3, v1}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v10

    :cond_c
    move/from16 v4, p3

    :goto_3
    return v1

    :cond_d
    move/from16 v4, p3

    :goto_4
    return v1
.end method
""",
        "replacement": """\
.method public checkRunningCompatibility(Landroid/content/ComponentName;III)Z
    .registers 18

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    const/4 v1, 0x1

    if-eqz v0, :cond_0

    return v1

    :cond_0
    if-eqz p1, :cond_d

    invoke-static {}, Landroid/miui/AppOpsUtils;->isXOptMode()Z

    move-result v0

    if-nez v0, :cond_d

    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Landroid/miui/AppOpsUtils;->isExceptionByTestPolicy(Ljava/lang/String;)Z

    move-result v0

    if-eqz v0, :cond_1

    move/from16 v4, p3

    goto :goto_4

    :cond_1
    invoke-static {p2}, Landroid/os/UserHandle;->getAppId(I)I

    move-result v0

    const/16 v2, 0x3e8

    if-eq v0, v2, :cond_c

    if-eqz v0, :cond_c

    const/16 v2, 0x7d0

    if-ne v0, v2, :cond_2

    move/from16 v4, p3

    goto :goto_3

    :cond_2
    iget-object v2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v2, :cond_3

    const-class v2, Lmiui/security/SecurityManagerInternal;

    invoke-static {v2}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v2

    check-cast v2, Lmiui/security/SecurityManagerInternal;

    iput-object v2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    :cond_3
    iget-object v2, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    if-nez v2, :cond_4

    return v1

    :cond_4
    invoke-virtual {p1}, Landroid/content/ComponentName;->getPackageName()Ljava/lang/String;

    move-result-object v5

    invoke-static/range {p3 .. p3}, Lcom/android/server/am/ProcessUtils;->getProcessRecordByPid(I)Lcom/android/server/am/ProcessRecord;

    move-result-object v2

    const/4 v10, 0x0

    const-string v3, "ActivityManagerServiceImpl"

    if-eqz v2, :cond_b

    iget-object v4, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    if-nez v4, :cond_5

    goto :goto_2

    :cond_5
    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    iget-object v6, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v6, v6, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    const-string v6, ":widgetProvider"

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v11

    sget-object v4, Lcom/android/server/am/ActivityManagerServiceImpl;->WIDGET_PROVIDER_WHITE_LIST:Ljava/util/List;

    iget-object v6, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v6, v6, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-interface {v4, v6}, Ljava/util/List;->contains(Ljava/lang/Object;)Z

    move-result v4

    if-nez v4, :cond_6

    iget-object v4, v2, Lcom/android/server/am/ProcessRecord;->processName:Ljava/lang/String;

    invoke-virtual {v11, v4}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v4

    if-eqz v4, :cond_6

    new-instance v4, Ljava/lang/StringBuilder;

    invoke-direct {v4}, Ljava/lang/StringBuilder;-><init>()V

    const-string v6, "MIUILOG- Reject widget call from "

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    iget-object v6, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v6, v6, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-virtual {v4, v6}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v4

    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v4

    invoke-static {v3, v4}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v3, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    iget-object v4, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v4, v4, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget v6, v2, Lcom/android/server/am/ProcessRecord;->uid:I

    invoke-static {v6}, Landroid/os/UserHandle;->getUserId(I)I

    move-result v7

    const/4 v6, 0x0

    const/4 v9, 0x0

    move/from16 v8, p4

    invoke-virtual/range {v3 .. v9}, Lmiui/security/SecurityManagerInternal;->recordWakePathCall(Ljava/lang/String;Ljava/lang/String;IIIZ)V

    :cond_6
    iget-object v3, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v3, v3, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-static {v3}, Landroid/text/TextUtils;->isEmpty(Ljava/lang/CharSequence;)Z

    move-result v3

    if-nez v3, :cond_a

    iget-object v3, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v3, v3, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    invoke-static {v3, v5}, Landroid/text/TextUtils;->equals(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Z

    move-result v3

    if-eqz v3, :cond_7

    goto :goto_1

    :cond_7
    iget-object v3, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mPackageManager:Landroid/content/pm/PackageManagerInternal;

    invoke-static {}, Landroid/os/Process;->myUid()I

    move-result v7

    move-object v4, v5

    const-wide/16 v5, 0x0

    move/from16 v8, p4

    invoke-virtual/range {v3 .. v8}, Landroid/content/pm/PackageManagerInternal;->getApplicationInfo(Ljava/lang/String;JII)Landroid/content/pm/ApplicationInfo;

    move-result-object v12

    move-object v5, v4

    if-eqz v12, :cond_9

    iget-object v3, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mAmService:Lcom/android/server/am/ActivityManagerService;

    iget-object v3, v3, Lcom/android/server/am/ActivityManagerService;->mActivityTaskManager:Lcom/android/server/wm/ActivityTaskManagerService;

    iget-object v4, v12, Landroid/content/pm/ApplicationInfo;->processName:Ljava/lang/String;

    iget v6, v12, Landroid/content/pm/ApplicationInfo;->uid:I

    invoke-static {v3, v5, v4, v6}, Lcom/android/server/wm/WindowProcessUtils;->isPackageRunning(Lcom/android/server/wm/ActivityTaskManagerService;Ljava/lang/String;Ljava/lang/String;I)Z

    move-result v3

    if-eqz v3, :cond_8

    goto :goto_0

    :cond_8
    iget-object v3, p0, Lcom/android/server/am/ActivityManagerServiceImpl;->mSecurityInternal:Lmiui/security/SecurityManagerInternal;

    iget-object v1, v2, Lcom/android/server/am/ProcessRecord;->info:Landroid/content/pm/ApplicationInfo;

    iget-object v4, v1, Landroid/content/pm/ApplicationInfo;->packageName:Ljava/lang/String;

    iget v1, v2, Lcom/android/server/am/ProcessRecord;->uid:I

    invoke-static {v1}, Landroid/os/UserHandle;->getUserId(I)I

    move-result v7

    const/4 v6, 0x0

    const/4 v9, 0x0

    move/from16 v8, p4

    invoke-virtual/range {v3 .. v9}, Lmiui/security/SecurityManagerInternal;->recordWakePathCall(Ljava/lang/String;Ljava/lang/String;IIIZ)V

    return v10

    :cond_9
    :goto_0
    return v1

    :cond_a
    :goto_1
    return v1

    :cond_b
    :goto_2
    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v4, "MIUILOG- Reject call from dying process "

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    move/from16 v4, p3

    invoke-virtual {v1, v4}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    invoke-static {v3, v1}, Landroid/util/Slog;->i(Ljava/lang/String;Ljava/lang/String;)I

    return v10

    :cond_c
    move/from16 v4, p3

    :goto_3
    return v1

    :cond_d
    move/from16 v4, p3

    :goto_4
    return v1
.end method
""",
        "method_anchors": ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'return v1', 'if-eqz p1, :cond_d', 'invoke-static {}, Landroid/miui/AppOpsUtils;->isXOptMode()Z', 'move-result v0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
    {
        "id":          "replace_method_onProcessStart_IILjava_lang_String__V",
        "method":      ".method public onProcessStart(IILjava/lang/String;)V",
        "method_name": 'onProcessStart',
        "type":        "method_replace",
        "search": """\
.method public onProcessStart(IILjava/lang/String;)V
    .registers 5

    invoke-static {}, Lcom/android/server/appop/flags/Flags;->enableJingyue()Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-class v0, Lmiui/security/SecurityManagerInternal;

    invoke-static {v0}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiui/security/SecurityManagerInternal;

    if-eqz v0, :cond_0

    invoke-virtual {v0, p3, p1, p2}, Lmiui/security/SecurityManagerInternal;->handleIsolateAppMountState(Ljava/lang/String;II)V

    :cond_0
    return-void
.end method
""",
        "replacement": """\
.method public onProcessStart(IILjava/lang/String;)V
    .registers 5

    invoke-static {}, Lcom/android/server/appop/flags/Flags;->enableJingyue()Z

    move-result v0

    if-eqz v0, :cond_0

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v0, :cond_0

    const-class v0, Lmiui/security/SecurityManagerInternal;

    invoke-static {v0}, Lcom/android/server/LocalServices;->getService(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lmiui/security/SecurityManagerInternal;

    if-eqz v0, :cond_0

    invoke-virtual {v0, p3, p1, p2}, Lmiui/security/SecurityManagerInternal;->handleIsolateAppMountState(Ljava/lang/String;II)V

    :cond_0
    return-void
.end method
""",
        "method_anchors": ['invoke-static {}, Lcom/android/server/appop/flags/Flags;->enableJingyue()Z', 'move-result v0', 'if-eqz v0, :cond_0', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'const-class v0, Lmiui/security/SecurityManagerInternal;'],
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
]
