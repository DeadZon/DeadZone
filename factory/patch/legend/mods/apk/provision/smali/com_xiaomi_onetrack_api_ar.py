TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/api/ar.smali'
CLASS_FALLBACK_NAMES = ['ar.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/lang/Runnable;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_api_ar__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/api/ar;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# instance fields
.field final synthetic a:Lcom/xiaomi/onetrack/api/ap;


# direct methods
.method constructor <init>(Lcom/xiaomi/onetrack/api/ap;)V
    .registers 2

    iput-object p1, p0, Lcom/xiaomi/onetrack/api/ar;->a:Lcom/xiaomi/onetrack/api/ap;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 2

    invoke-static {}, Lcom/xiaomi/onetrack/c/i;->b()Z

    move-result v0

    if-nez v0, :cond_0

    return-void

    :cond_0
    iget-object p0, p0, Lcom/xiaomi/onetrack/api/ar;->a:Lcom/xiaomi/onetrack/api/ap;

    invoke-static {p0}, Lcom/xiaomi/onetrack/api/ap;->a(Lcom/xiaomi/onetrack/api/ap;)V

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
