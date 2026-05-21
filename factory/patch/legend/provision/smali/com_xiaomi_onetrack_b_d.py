TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/b/d.smali'
CLASS_FALLBACK_NAMES = ['d.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/lang/Runnable;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_b_d__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/b/d;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# instance fields
.field final synthetic a:Ljava/lang/String;

.field final synthetic b:Lcom/xiaomi/onetrack/b/a$b;


# direct methods
.method constructor <init>(Lcom/xiaomi/onetrack/b/a$b;Ljava/lang/String;)V
    .registers 3

    iput-object p1, p0, Lcom/xiaomi/onetrack/b/d;->b:Lcom/xiaomi/onetrack/b/a$b;

    iput-object p2, p0, Lcom/xiaomi/onetrack/b/d;->a:Ljava/lang/String;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 3

    iget-object v0, p0, Lcom/xiaomi/onetrack/b/d;->a:Ljava/lang/String;

    filled-new-array {v0}, [Ljava/lang/String;

    move-result-object v0

    invoke-static {v0}, Ljava/util/Arrays;->asList([Ljava/lang/Object;)Ljava/util/List;

    move-result-object v0

    invoke-static {v0}, Lcom/xiaomi/onetrack/b/a;->a(Ljava/util/List;)V

    invoke-static {}, Lcom/xiaomi/onetrack/b/a;->b()Ljava/util/concurrent/ConcurrentHashMap;

    move-result-object v0

    iget-object p0, p0, Lcom/xiaomi/onetrack/b/d;->a:Ljava/lang/String;

    sget-object v1, Ljava/lang/Boolean;->FALSE:Ljava/lang/Boolean;

    invoke-virtual {v0, p0, v1}, Ljava/util/concurrent/ConcurrentHashMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
