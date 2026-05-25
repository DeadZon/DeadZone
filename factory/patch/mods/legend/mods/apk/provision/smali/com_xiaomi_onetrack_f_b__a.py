TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/f/b$a.smali'
CLASS_FALLBACK_NAMES = ['b$a.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_f_b__a__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/f/b$a;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xiaomi/onetrack/f/b;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x9
    name = "a"
.end annotation


# instance fields
.field private a:J

.field private b:Ljava/lang/String;

.field private c:Ljava/lang/String;

.field private d:Ljava/lang/String;

.field private e:I

.field private f:Lorg/json/JSONObject;

.field private g:J


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method static synthetic a(Lcom/xiaomi/onetrack/f/b$a;)J
    .registers 3

    iget-wide v0, p0, Lcom/xiaomi/onetrack/f/b$a;->a:J

    return-wide v0
.end method

.method static synthetic b(Lcom/xiaomi/onetrack/f/b$a;)Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/f/b$a;->b:Ljava/lang/String;

    return-object p0
.end method

.method static synthetic c(Lcom/xiaomi/onetrack/f/b$a;)Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/f/b$a;->c:Ljava/lang/String;

    return-object p0
.end method

.method static synthetic d(Lcom/xiaomi/onetrack/f/b$a;)Ljava/lang/String;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/f/b$a;->d:Ljava/lang/String;

    return-object p0
.end method

.method static synthetic e(Lcom/xiaomi/onetrack/f/b$a;)I
    .registers 1

    iget p0, p0, Lcom/xiaomi/onetrack/f/b$a;->e:I

    return p0
.end method

.method static synthetic f(Lcom/xiaomi/onetrack/f/b$a;)Lorg/json/JSONObject;
    .registers 1

    iget-object p0, p0, Lcom/xiaomi/onetrack/f/b$a;->f:Lorg/json/JSONObject;

    return-object p0
.end method

.method static synthetic g(Lcom/xiaomi/onetrack/f/b$a;)J
    .registers 3

    iget-wide v0, p0, Lcom/xiaomi/onetrack/f/b$a;->g:J

    return-wide v0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
