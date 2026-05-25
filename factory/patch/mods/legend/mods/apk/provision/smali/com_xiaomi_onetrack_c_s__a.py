TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/c/s$a.smali'
CLASS_FALLBACK_NAMES = ['s$a.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final a:Lcom/xiaomi/onetrack/c/s;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_c_s__a__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/c/s$a;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xiaomi/onetrack/c/s;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0xa
    name = "a"
.end annotation


# static fields
.field private static final a:Lcom/xiaomi/onetrack/c/s;


# direct methods
.method static constructor <clinit>()V
    .registers 2

    new-instance v0, Lcom/xiaomi/onetrack/c/s;

    const/4 v1, 0x0

    invoke-direct {v0, v1}, Lcom/xiaomi/onetrack/c/s;-><init>(Lcom/xiaomi/onetrack/c/t;)V

    sput-object v0, Lcom/xiaomi/onetrack/c/s$a;->a:Lcom/xiaomi/onetrack/c/s;

    return-void
.end method

.method private constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method static synthetic a()Lcom/xiaomi/onetrack/c/s;
    .registers 1

    sget-object v0, Lcom/xiaomi/onetrack/c/s$a;->a:Lcom/xiaomi/onetrack/c/s;

    return-object v0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
