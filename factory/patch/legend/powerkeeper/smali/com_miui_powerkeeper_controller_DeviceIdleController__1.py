TARGET_APK = 'PowerKeeper.apk'
TARGET_CLASS = 'com/miui/powerkeeper/controller/DeviceIdleController$1.smali'
CLASS_FALLBACK_NAMES = ['DeviceIdleController$1.smali']
CLASS_ANCHORS = ['.super Ljava/util/HashSet;']

PATCHES = [
    {
        'id': 'com_miui_powerkeeper_controller_DeviceIdleController__1__init',
        'method': '.method constructor <init>()V',
        'method_name': '<init>',
        'method_anchors': ['invoke-direct {p0}, Ljava/util/HashSet;-><init>()V', 'sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z', 'if-nez v0, :cond_0', 'const-string v0, "com.tencent.mm"', 'invoke-virtual {p0, v0}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z', 'const-string v0, "com.tencent.mobileqq"', 'invoke-virtual {p0, v0}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z', 'const-string v0, "com.tencent.qqlite"'],
        'type': 'method_replace',
        'search': """.method constructor <init>()V
    .registers 2

    invoke-direct {p0}, Ljava/util/HashSet;-><init>()V

    sget-boolean v0, Lmiui/os/Build;->IS_INTERNATIONAL_BUILD:Z

    if-nez v0, :cond_0

    const-string v0, "com.tencent.mm"

    invoke-virtual {p0, v0}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z

    const-string v0, "com.tencent.mobileqq"

    invoke-virtual {p0, v0}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z

    const-string v0, "com.tencent.qqlite"

    invoke-virtual {p0, v0}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z

    :cond_0
    const-string v0, "com.android.deskclock"

    invoke-virtual {p0, v0}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z

    return-void
.end method""",
        'replacement': """.method constructor <init>()V
    .registers 2

    invoke-direct {p0}, Ljava/util/HashSet;-><init>()V

    sget-boolean v0, Lmiui/os/Build;->IS_MIUI:Z

    if-nez v0, :cond_0

    const-string v0, "com.tencent.mm"

    invoke-virtual {p0, v0}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z

    const-string v0, "com.tencent.mobileqq"

    invoke-virtual {p0, v0}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z

    const-string v0, "com.tencent.qqlite"

    invoke-virtual {p0, v0}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z

    :cond_0
    const-string v0, "com.android.deskclock"

    invoke-virtual {p0, v0}, Ljava/util/HashSet;->add(Ljava/lang/Object;)Z

    return-void
.end method""",
        'required': True,
        'flag_rewrite_count': 1,
        'reason': 'PowerKeeper smali rule generated from comparison output.',
    },
]
