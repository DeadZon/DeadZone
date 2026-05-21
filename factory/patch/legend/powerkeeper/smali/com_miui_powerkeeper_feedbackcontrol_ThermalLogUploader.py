TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/feedbackcontrol/ThermalLogUploader.smali'
CLASS_FALLBACK_NAMES = ['ThermalLogUploader.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final BIZ_NAME:Ljava/lang/String; = "themal"', '.field private static final TAG:Ljava/lang/String; = "ThermalLogUploader"', '.field private static final THERMAL_UPLOAD_URL:Ljava/lang/String; = "https://port.sec.miui.com/mqsas/fileUploadWithUrlId"', '.field public static final ZIP_THERMAL_EXCEPTION_LOG_DIR:Ljava/lang/String; = "/data/vendor/thermal/log"']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_feedbackcontrol_ThermalLogUploader__uploadFiles',
        'method': '.method public static uploadFiles()V',
        'method_name': 'uploadFiles',
        'method_anchors': ['sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-eqz v0, :cond_0', 'new-instance v0, Ljava/io/File;', 'const-string v1, "/data/vendor/thermal/log"', 'invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V', 'invoke-virtual {v0}, Ljava/io/File;->exists()Z', 'if-nez v1, :cond_1', 'invoke-virtual {v0}, Ljava/io/File;->listFiles()[Ljava/io/File;'],
        'type': 'method_replace',
        'search': """.method public static uploadFiles()V
    .registers 5

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    :try_start_0
    new-instance v0, Ljava/io/File;

    const-string v1, "/data/vendor/thermal/log"

    invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/io/File;->exists()Z

    move-result v1

    if-nez v1, :cond_1

    goto :goto_1

    :cond_1
    invoke-virtual {v0}, Ljava/io/File;->listFiles()[Ljava/io/File;

    move-result-object v0

    array-length v1, v0

    const/4 v2, 0x0

    :goto_0
    if-ge v2, v1, :cond_2

    aget-object v3, v0, v2

    const-string v4, "https://port.sec.miui.com/mqsas/fileUploadWithUrlId?bizName=themal"

    invoke-static {v4, v3}, Lcom/miui/powerkeeper/feedbackcontrol/ThermalLogUploader;->uploadFile(Ljava/lang/String;Ljava/io/File;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :catch_0
    move-exception v0

    invoke-virtual {v0}, Ljava/lang/Exception;->printStackTrace()V

    :cond_2
    :goto_1
    return-void
.end method""",
        'replacement': """.method public static uploadFiles()V
    .registers 5

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    if-eqz v0, :cond_0

    goto :goto_1

    :cond_0
    :try_start_0
    new-instance v0, Ljava/io/File;

    const-string v1, "/data/vendor/thermal/log"

    invoke-direct {v0, v1}, Ljava/io/File;-><init>(Ljava/lang/String;)V

    invoke-virtual {v0}, Ljava/io/File;->exists()Z

    move-result v1

    if-nez v1, :cond_1

    goto :goto_1

    :cond_1
    invoke-virtual {v0}, Ljava/io/File;->listFiles()[Ljava/io/File;

    move-result-object v0

    array-length v1, v0

    const/4 v2, 0x0

    :goto_0
    if-ge v2, v1, :cond_2

    aget-object v3, v0, v2

    const-string v4, "https://port.sec.miui.com/mqsas/fileUploadWithUrlId?bizName=themal"

    invoke-static {v4, v3}, Lcom/miui/powerkeeper/feedbackcontrol/ThermalLogUploader;->uploadFile(Ljava/lang/String;Ljava/io/File;)V
    :try_end_0
    .catch Ljava/lang/Exception; {:try_start_0 .. :try_end_0} :catch_0

    add-int/lit8 v2, v2, 0x1

    goto :goto_0

    :catch_0
    move-exception v0

    invoke-virtual {v0}, Ljava/lang/Exception;->printStackTrace()V

    :cond_2
    :goto_1
    return-void
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
