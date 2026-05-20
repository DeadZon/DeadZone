"""
Legend MTCR patch - class-level rule.

Target JAR   : miui-services.jar
Target class : com/miui/server/greeze/PolicyManager
Source MTCR  : miui-services_Legend.mtcr

This file is auto-generated from the MTCR archive.
The real logic lives here — not in the JAR-level patch_*.py wrappers.
"""
from __future__ import annotations

TARGET_JAR   = "miui-services.jar"
TARGET_CLASS = "com/miui/server/greeze/PolicyManager.smali"
CLASS_FALLBACK_NAMES = ['PolicyManager.smali']
CLASS_ANCHORS        = []

PATCHES = [
    {
        "id":          "replace_method__clinit___V",
        "method":      ".method static constructor <clinit>()V",
        "method_name": '<clinit>',
        "type":        "method_replace",
        "search": """\
.method static constructor <clinit>()V
    .registers 7

    const-string v0, "persist.sys.aurogon.immobulus"

    const/4 v1, 0x1

    invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v0

    sput-boolean v0, Lcom/miui/server/greeze/PolicyManager;->IMMOBULUS_ENABLED:Z

    const-string v0, "ro.miui.region"

    const-string v1, "unknown"

    invoke-static {v0, v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    const-string v1, "CN"

    invoke-virtual {v1, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    sput-boolean v0, Lcom/miui/server/greeze/PolicyManager;->CN_MODEL:Z

    new-instance v0, Ljava/util/ArrayList;

    const-string v5, "com.area120.kormo.seeker"

    const-string v6, "com.android.vending"

    const-string v1, "com.andriod.chrome"

    const-string v2, "com.google.ambient.streaming"

    const-string v3, "com.fitbit.FitbitMobile"

    const-string v4, "com.google.earth"

    filled-new-array/range {v1 .. v6}, [Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v1

    invoke-direct {v0, v1}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    sput-object v0, Lcom/miui/server/greeze/PolicyManager;->mGoogleApps:Ljava/util/List;

    new-instance v0, Ljava/util/ArrayList;

    const-string v1, "com.google.android.youtube"

    const-string v2, "com.google.android.googlequicksearchbox"

    const-string v3, "com.android.chrome"

    filled-new-array {v3, v1, v2}, [Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v1

    invoke-direct {v0, v1}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    sput-object v0, Lcom/miui/server/greeze/PolicyManager;->mExcludeGoogleApps:Ljava/util/List;

    return-void
.end method
""",
        "replacement": """\
.method static constructor <clinit>()V
    .registers 7

    const-string v0, "persist.sys.aurogon.immobulus"

    const/4 v1, 0x1

    invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z

    move-result v0

    sput-boolean v0, Lcom/miui/server/greeze/PolicyManager;->IMMOBULUS_ENABLED:Z

    const-string v0, "ro.miui.region"

    const-string v1, "unknown"

    invoke-static {v0, v1}, Landroid/os/SystemProperties;->get(Ljava/lang/String;Ljava/lang/String;)Ljava/lang/String;

    move-result-object v0

    const-string v1, "CN"

    invoke-virtual {v1, v0}, Ljava/lang/Object;->equals(Ljava/lang/Object;)Z

    move-result v0

    const/4 v0, 0x0

    sput-boolean v0, Lcom/miui/server/greeze/PolicyManager;->CN_MODEL:Z

    new-instance v0, Ljava/util/ArrayList;

    const-string v5, "com.area120.kormo.seeker"

    const-string v6, "com.android.vending"

    const-string v1, "com.andriod.chrome"

    const-string v2, "com.google.ambient.streaming"

    const-string v3, "com.fitbit.FitbitMobile"

    const-string v4, "com.google.earth"

    filled-new-array/range {v1 .. v6}, [Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v1

    invoke-direct {v0, v1}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    sput-object v0, Lcom/miui/server/greeze/PolicyManager;->mGoogleApps:Ljava/util/List;

    new-instance v0, Ljava/util/ArrayList;

    const-string v1, "com.google.android.youtube"

    const-string v2, "com.google.android.googlequicksearchbox"

    const-string v3, "com.android.chrome"

    filled-new-array {v3, v1, v2}, [Ljava/lang/String;

    move-result-object v1

    invoke-static {v1}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v1

    invoke-direct {v0, v1}, Ljava/util/ArrayList;-><init>(Ljava/util/Collection;)V

    sput-object v0, Lcom/miui/server/greeze/PolicyManager;->mExcludeGoogleApps:Ljava/util/List;

    return-void
.end method
""",
        "method_anchors": ['const-string v0, "persist.sys.aurogon.immobulus"', 'invoke-static {v0, v1}, Landroid/os/SystemProperties;->getBoolean(Ljava/lang/String;Z)Z', 'move-result v0', 'sput-boolean v0, Lcom/miui/server/greeze/PolicyManager;->IMMOBULUS_ENABLED:Z', 'const-string v0, "ro.miui.region"', 'const-string v1, "unknown"'],
        "required":    True,
        "reason":      "Legend MTCR modified method from miui-services_Legend.mtcr",
    },
]
