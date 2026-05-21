TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/util/s.smali'
CLASS_FALLBACK_NAMES = ['s.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lcom/xiaomi/onetrack/util/r$a;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_util_s__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/util/s;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/xiaomi/onetrack/util/r$a;


# instance fields
.field final synthetic a:Z


# direct methods
.method constructor <init>(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/xiaomi/onetrack/util/s;->a:Z

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public a(Ljava/lang/Object;)Z
    .registers 2

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/util/s;->a:Z

    if-eqz p0, :cond_0

    invoke-static {p1}, Lcom/xiaomi/onetrack/util/r;->a(Ljava/lang/Object;)Z

    move-result p0

    return p0

    :cond_0
    invoke-static {p1}, Lcom/xiaomi/onetrack/util/r;->b(Ljava/lang/Object;)Z

    move-result p0

    return p0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
