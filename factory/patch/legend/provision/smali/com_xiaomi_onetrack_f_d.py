TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/f/d.smali'
CLASS_FALLBACK_NAMES = ['d.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_f_d__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/f/d;
.super Ljava/lang/Object;


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static a(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .registers 5

    new-instance v0, Lcom/xiaomi/onetrack/f/e;

    invoke-direct {v0, p0, p1, p2, p3}, Lcom/xiaomi/onetrack/f/e;-><init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V

    invoke-static {v0}, Lcom/xiaomi/onetrack/util/i;->a(Ljava/lang/Runnable;)V

    return-void
.end method

.method public static b(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .registers 5

    new-instance v0, Lcom/xiaomi/onetrack/f/f;

    invoke-direct {v0, p0, p1, p2, p3}, Lcom/xiaomi/onetrack/f/f;-><init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V

    invoke-static {v0}, Lcom/xiaomi/onetrack/util/i;->a(Ljava/lang/Runnable;)V

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
