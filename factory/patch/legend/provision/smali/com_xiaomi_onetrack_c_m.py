TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/c/m.smali'
CLASS_FALLBACK_NAMES = ['m.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/lang/Runnable;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_c_m__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/c/m;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# instance fields
.field final synthetic a:Ljava/lang/String;

.field final synthetic b:Ljava/lang/String;

.field final synthetic c:Ljava/lang/String;

.field final synthetic d:Lcom/xiaomi/onetrack/c/l;


# direct methods
.method constructor <init>(Lcom/xiaomi/onetrack/c/l;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
    .registers 5

    iput-object p1, p0, Lcom/xiaomi/onetrack/c/m;->d:Lcom/xiaomi/onetrack/c/l;

    iput-object p2, p0, Lcom/xiaomi/onetrack/c/m;->a:Ljava/lang/String;

    iput-object p3, p0, Lcom/xiaomi/onetrack/c/m;->b:Ljava/lang/String;

    iput-object p4, p0, Lcom/xiaomi/onetrack/c/m;->c:Ljava/lang/String;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 4

    iget-object v0, p0, Lcom/xiaomi/onetrack/c/m;->d:Lcom/xiaomi/onetrack/c/l;

    iget-object v1, p0, Lcom/xiaomi/onetrack/c/m;->a:Ljava/lang/String;

    iget-object v2, p0, Lcom/xiaomi/onetrack/c/m;->b:Ljava/lang/String;

    iget-object p0, p0, Lcom/xiaomi/onetrack/c/m;->c:Ljava/lang/String;

    invoke-static {v0, v1, v2, p0}, Lcom/xiaomi/onetrack/c/l;->a(Lcom/xiaomi/onetrack/c/l;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
