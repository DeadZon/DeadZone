TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/api/n.smali'
CLASS_FALLBACK_NAMES = ['n.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/lang/Runnable;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_api_n__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/api/n;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/lang/Runnable;


# instance fields
.field final synthetic a:Landroid/content/Context;

.field final synthetic b:Lcom/xiaomi/onetrack/api/m;


# direct methods
.method constructor <init>(Lcom/xiaomi/onetrack/api/m;Landroid/content/Context;)V
    .registers 3

    iput-object p1, p0, Lcom/xiaomi/onetrack/api/n;->b:Lcom/xiaomi/onetrack/api/m;

    iput-object p2, p0, Lcom/xiaomi/onetrack/api/n;->a:Landroid/content/Context;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public run()V
    .registers 3

    iget-object v0, p0, Lcom/xiaomi/onetrack/api/n;->a:Landroid/content/Context;

    iget-object v1, p0, Lcom/xiaomi/onetrack/api/n;->b:Lcom/xiaomi/onetrack/api/m;

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/CrashAnalysis;->init(Landroid/content/Context;Lcom/xiaomi/onetrack/api/m;)Lcom/xiaomi/onetrack/CrashAnalysis;

    move-result-object v0

    invoke-virtual {v0}, Lcom/xiaomi/onetrack/CrashAnalysis;->start()V

    invoke-static {}, Lcom/xiaomi/onetrack/CrashAnalysis;->getInstance()Lcom/xiaomi/onetrack/CrashAnalysis;

    move-result-object v0

    if-eqz v0, :cond_1

    invoke-static {}, Lcom/xiaomi/onetrack/CrashAnalysis;->getInstance()Lcom/xiaomi/onetrack/CrashAnalysis;

    move-result-object v0

    invoke-virtual {v0}, Lcom/xiaomi/onetrack/CrashAnalysis;->isSupport()Z

    move-result v0

    if-nez v0, :cond_0

    goto :goto_0

    :cond_0
    return-void

    :cond_1
    :goto_0
    iget-object v0, p0, Lcom/xiaomi/onetrack/api/n;->b:Lcom/xiaomi/onetrack/api/m;

    new-instance v1, Lcom/xiaomi/onetrack/api/k;

    invoke-direct {v1, v0}, Lcom/xiaomi/onetrack/api/k;-><init>(Lcom/xiaomi/onetrack/api/m;)V

    invoke-static {v0, v1}, Lcom/xiaomi/onetrack/api/m;->a(Lcom/xiaomi/onetrack/api/m;Lcom/xiaomi/onetrack/api/k;)Lcom/xiaomi/onetrack/api/k;

    iget-object p0, p0, Lcom/xiaomi/onetrack/api/n;->b:Lcom/xiaomi/onetrack/api/m;

    invoke-static {p0}, Lcom/xiaomi/onetrack/api/m;->a(Lcom/xiaomi/onetrack/api/m;)Lcom/xiaomi/onetrack/api/k;

    move-result-object p0

    invoke-virtual {p0}, Lcom/xiaomi/onetrack/api/k;->a()V

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
