TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/f/e.smali'
CLASS_FALLBACK_NAMES = ['e.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/lang/Runnable;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_f_e__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/f/e;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# instance fields
.field final synthetic a:Ljava/lang/String;

.field final synthetic b:Ljava/lang/String;

.field final synthetic c:Ljava/lang/String;

.field final synthetic d:Ljava/lang/String;


# direct methods
.method constructor <init>(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .registers 5

    iput-object p1, p0, Lcom/xiaomi/onetrack/f/e;->a:Ljava/lang/String;

    iput-object p2, p0, Lcom/xiaomi/onetrack/f/e;->b:Ljava/lang/String;

    iput-object p3, p0, Lcom/xiaomi/onetrack/f/e;->c:Ljava/lang/String;

    iput-object p4, p0, Lcom/xiaomi/onetrack/f/e;->d:Ljava/lang/String;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 4

    iget-object v0, p0, Lcom/xiaomi/onetrack/f/e;->a:Ljava/lang/String;

    iget-object v1, p0, Lcom/xiaomi/onetrack/f/e;->b:Ljava/lang/String;

    iget-object v2, p0, Lcom/xiaomi/onetrack/f/e;->c:Ljava/lang/String;

    iget-object p0, p0, Lcom/xiaomi/onetrack/f/e;->d:Ljava/lang/String;

    invoke-static {v0, v1, v2, p0}, Lcom/xiaomi/onetrack/e/b;->a(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)Lcom/xiaomi/onetrack/f/b;

    move-result-object p0

    invoke-static {}, Lcom/xiaomi/onetrack/c/c;->a()Lcom/xiaomi/onetrack/c/c;

    move-result-object v0

    invoke-virtual {v0, p0}, Lcom/xiaomi/onetrack/c/c;->a(Lcom/xiaomi/onetrack/f/b;)V

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
