TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/OneTrack$1.smali'
CLASS_FALLBACK_NAMES = ['OneTrack$1.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/lang/Runnable;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_OneTrack__1__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/OneTrack$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# instance fields
.field final synthetic a:Z


# direct methods
.method constructor <init>(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/xiaomi/onetrack/OneTrack$1;->a:Z

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 2

    iget-boolean v0, p0, Lcom/xiaomi/onetrack/OneTrack$1;->a:Z

    invoke-static {v0}, Lcom/xiaomi/onetrack/c/i;->a(Z)V

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/OneTrack$1;->a:Z

    invoke-static {p0}, Lcom/xiaomi/onetrack/c/i;->b(Z)V

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
