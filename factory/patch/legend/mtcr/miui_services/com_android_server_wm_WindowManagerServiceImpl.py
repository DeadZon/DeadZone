"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-services.jar
Target class : com/android/server/wm/WindowManagerServiceImpl
Source MTCR  : miui-services_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-services.jar"
TARGET_CLASS = "com/android/server/wm/WindowManagerServiceImpl.smali"
CLASS_FALLBACK_NAMES = ['WindowManagerServiceImpl.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "replace_method_notAllowCaptureDisplay_Lcom_android_server_wm_RootWindowCont",
        "method":      ".method public notAllowCaptureDisplay(Lcom/android/server/wm/RootWindowContainer;I)Z",
        "method_name": 'notAllowCaptureDisplay',
        "type":        "method_replace",
        "search": """\
.method public notAllowCaptureDisplay(Lcom/android/server/wm/RootWindowContainer;I)Z
    .registers 7

    invoke-static {}, Landroid/os/Binder;->getCallingUid()I

    move-result v0

    const/16 v1, 0x3e8

    const/4 v2, 0x0

    if-eq v0, v1, :cond_2

    invoke-static {}, Lcom/android/server/wm/ActivityRecordStub;->isCompatibilityMode()Z

    move-result v0

    if-eqz v0, :cond_0

    goto :goto_0

    :cond_0
    invoke-virtual {p1, p2}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v0

    if-nez v0, :cond_1

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, " Screenshot on invalid display "

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v3, "  "

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-static {}, Landroid/os/Binder;->getCallingUid()I

    move-result v3

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v3, "WindowManagerService"

    invoke-static {v3, v1}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    return v2

    :cond_1
    new-instance v1, Lcom/android/server/wm/WindowManagerServiceImpl$$ExternalSyntheticLambda21;

    invoke-direct {v1, p0}, Lcom/android/server/wm/WindowManagerServiceImpl$$ExternalSyntheticLambda21;-><init>(Lcom/android/server/wm/WindowManagerServiceImpl;)V

    invoke-virtual {v0, v1, v2}, Lcom/android/server/wm/DisplayContent;->forAllWindows(Lcom/android/internal/util/ToBooleanFunction;Z)Z

    move-result v1

    return v1

    :cond_2
    :goto_0
    return v2
.end method
""",
        "replacement": """\
.method public notAllowCaptureDisplay(Lcom/android/server/wm/RootWindowContainer;I)Z
    .registers 7

    const/4 v1, 0x1

    const-string v0, "disable_mezo_screenshot_secure"

    invoke-static {v0, v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;I)I

    move-result v0

    if-eqz v0, :cond_0

    const/4 v0, 0x0

    return v0

    :cond_0
    invoke-static {}, Landroid/os/Binder;->getCallingUid()I

    move-result v0

    const/16 v1, 0x3e8

    const/4 v2, 0x0

    if-eq v0, v1, :cond_3

    invoke-static {}, Lcom/android/server/wm/ActivityRecordStub;->isCompatibilityMode()Z

    move-result v0

    if-eqz v0, :cond_1

    goto :goto_0

    :cond_1
    invoke-virtual {p1, p2}, Lcom/android/server/wm/RootWindowContainer;->getDisplayContent(I)Lcom/android/server/wm/DisplayContent;

    move-result-object v0

    if-nez v0, :cond_2

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v3, " Screenshot on invalid display "

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1, p2}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v3, "  "

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-static {}, Landroid/os/Binder;->getCallingUid()I

    move-result v3

    invoke-virtual {v1, v3}, Ljava/lang/StringBuilder;->append(I)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v3, "WindowManagerService"

    invoke-static {v3, v1}, Landroid/util/Slog;->e(Ljava/lang/String;Ljava/lang/String;)I

    return v2

    :cond_2
    new-instance v1, Lcom/android/server/wm/WindowManagerServiceImpl$$ExternalSyntheticLambda21;

    invoke-direct {v1, p0}, Lcom/android/server/wm/WindowManagerServiceImpl$$ExternalSyntheticLambda21;-><init>(Lcom/android/server/wm/WindowManagerServiceImpl;)V

    invoke-virtual {v0, v1, v2}, Lcom/android/server/wm/DisplayContent;->forAllWindows(Lcom/android/internal/util/ToBooleanFunction;Z)Z

    move-result v1

    return v1

    :cond_3
    :goto_0
    return v2
.end method
""",
        "method_anchors": ['invoke-static {}, Landroid/os/Binder;->getCallingUid()I', 'move-result v0', 'if-eq v0, v1, :cond_2', 'invoke-static {}, Lcom/android/server/wm/ActivityRecordStub;->isCompatibilityMode()Z', 'move-result v0', 'if-eqz v0, :cond_0'],
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
]
