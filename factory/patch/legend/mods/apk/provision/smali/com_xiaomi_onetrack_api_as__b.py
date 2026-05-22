TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/api/as$b.smali'
CLASS_FALLBACK_NAMES = ['as$b.smali']
CLASS_ANCHORS = ['.super Landroid/os/Handler;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_api_as__b__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/api/as$b;
.super Landroid/os/Handler;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xiaomi/onetrack/api/as;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x2
    name = "b"
.end annotation


# instance fields
.field final synthetic a:Lcom/xiaomi/onetrack/api/as;


# direct methods
.method public constructor <init>(Lcom/xiaomi/onetrack/api/as;Landroid/os/Looper;)V
    .registers 3

    iput-object p1, p0, Lcom/xiaomi/onetrack/api/as$b;->a:Lcom/xiaomi/onetrack/api/as;

    invoke-direct {p0, p2}, Landroid/os/Handler;-><init>(Landroid/os/Looper;)V

    return-void
.end method


# virtual methods
.method public handleMessage(Landroid/os/Message;)V
    .registers 3

    invoke-super {p0, p1}, Landroid/os/Handler;->handleMessage(Landroid/os/Message;)V

    iget p1, p1, Landroid/os/Message;->what:I

    const/4 v0, 0x1

    if-ne p1, v0, :cond_0

    iget-object p0, p0, Lcom/xiaomi/onetrack/api/as$b;->a:Lcom/xiaomi/onetrack/api/as;

    invoke-static {p0}, Lcom/xiaomi/onetrack/api/as;->h(Lcom/xiaomi/onetrack/api/as;)V

    return-void

    :cond_0
    const/4 v0, 0x2

    if-ne p1, v0, :cond_1

    iget-object p0, p0, Lcom/xiaomi/onetrack/api/as$b;->a:Lcom/xiaomi/onetrack/api/as;

    invoke-static {p0}, Lcom/xiaomi/onetrack/api/as;->i(Lcom/xiaomi/onetrack/api/as;)V

    :cond_1
    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
