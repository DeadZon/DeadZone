TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/Configuration$Builder.smali'
CLASS_FALLBACK_NAMES = ['Configuration$Builder.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_Configuration__Builder__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/Configuration$Builder;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xiaomi/onetrack/Configuration;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x9
    name = "Builder"
.end annotation


# instance fields
.field private a:Ljava/lang/String;

.field private b:Ljava/lang/String;

.field private c:Ljava/lang/String;

.field private d:Z

.field private e:Ljava/lang/String;

.field private f:Lcom/xiaomi/onetrack/OneTrack$Mode;

.field private g:Z

.field private h:Z

.field private i:Z

.field private j:Z

.field private k:Z

.field private l:Z

.field private m:Ljava/lang/String;

.field private n:Z

.field private o:Ljava/lang/String;


# direct methods
.method public constructor <init>()V
    .registers 3

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    sget-object v0, Lcom/xiaomi/onetrack/OneTrack$Mode;->APP:Lcom/xiaomi/onetrack/OneTrack$Mode;

    iput-object v0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->f:Lcom/xiaomi/onetrack/OneTrack$Mode;

    const/4 v0, 0x1

    iput-boolean v0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->g:Z

    iput-boolean v0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->h:Z

    iput-boolean v0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->i:Z

    const/4 v1, 0x0

    iput-boolean v1, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->j:Z

    iput-boolean v0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->k:Z

    iput-boolean v1, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->l:Z

    iput-boolean v1, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->n:Z

    return-void
.end method

.method static synthetic a(Lcom/xiaomi/onetrack/Configuration$Builder;)Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->a:Ljava/lang/String;

    return-object p0
.end method

.method static synthetic b(Lcom/xiaomi/onetrack/Configuration$Builder;)Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->b:Ljava/lang/String;

    return-object p0
.end method

.method static synthetic c(Lcom/xiaomi/onetrack/Configuration$Builder;)Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->c:Ljava/lang/String;

    return-object p0
.end method

.method static synthetic d(Lcom/xiaomi/onetrack/Configuration$Builder;)Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->d:Z

    return p0
.end method

.method static synthetic e(Lcom/xiaomi/onetrack/Configuration$Builder;)Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->e:Ljava/lang/String;

    return-object p0
.end method

.method static synthetic f(Lcom/xiaomi/onetrack/Configuration$Builder;)Lcom/xiaomi/onetrack/OneTrack$Mode;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->f:Lcom/xiaomi/onetrack/OneTrack$Mode;

    return-object p0
.end method

.method static synthetic g(Lcom/xiaomi/onetrack/Configuration$Builder;)Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->g:Z

    return p0
.end method

.method static synthetic h(Lcom/xiaomi/onetrack/Configuration$Builder;)Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->i:Z

    return p0
.end method

.method static synthetic i(Lcom/xiaomi/onetrack/Configuration$Builder;)Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->h:Z

    return p0
.end method

.method static synthetic j(Lcom/xiaomi/onetrack/Configuration$Builder;)Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->j:Z

    return p0
.end method

.method static synthetic k(Lcom/xiaomi/onetrack/Configuration$Builder;)Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->k:Z

    return p0
.end method

.method static synthetic l(Lcom/xiaomi/onetrack/Configuration$Builder;)Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->l:Z

    return p0
.end method

.method static synthetic m(Lcom/xiaomi/onetrack/Configuration$Builder;)Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->m:Ljava/lang/String;

    return-object p0
.end method

.method static synthetic n(Lcom/xiaomi/onetrack/Configuration$Builder;)Z
    .registers 1

    iget-boolean p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->n:Z

    return p0
.end method

.method static synthetic o(Lcom/xiaomi/onetrack/Configuration$Builder;)Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->o:Ljava/lang/String;

    return-object p0
.end method


# virtual methods
.method public build()Lcom/xiaomi/onetrack/Configuration;
    .registers 3

    new-instance v0, Lcom/xiaomi/onetrack/Configuration;

    const/4 v1, 0x0

    invoke-direct {v0, p0, v1}, Lcom/xiaomi/onetrack/Configuration;-><init>(Lcom/xiaomi/onetrack/Configuration$Builder;Lcom/xiaomi/onetrack/Configuration$1;)V

    return-object v0
.end method

.method public setAppId(Ljava/lang/String;)Lcom/xiaomi/onetrack/Configuration$Builder;
    .registers 2

    iput-object p1, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->a:Ljava/lang/String;

    return-object p0
.end method

.method public setChannel(Ljava/lang/String;)Lcom/xiaomi/onetrack/Configuration$Builder;
    .registers 2

    iput-object p1, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->c:Ljava/lang/String;

    return-object p0
.end method

.method public setExceptionCatcherEnable(Z)Lcom/xiaomi/onetrack/Configuration$Builder;
    .registers 2

    iput-boolean p1, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->j:Z

    return-object p0
.end method

.method public setMode(Lcom/xiaomi/onetrack/OneTrack$Mode;)Lcom/xiaomi/onetrack/Configuration$Builder;
    .registers 2

    iput-object p1, p0, Lcom/xiaomi/onetrack/Configuration$Builder;->f:Lcom/xiaomi/onetrack/OneTrack$Mode;

    return-object p0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
