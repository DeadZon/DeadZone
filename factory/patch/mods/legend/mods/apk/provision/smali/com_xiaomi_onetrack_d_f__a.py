TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/d/f$a.smali'
CLASS_FALLBACK_NAMES = ['f$a.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final a:Lcom/xiaomi/onetrack/d/f;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_d_f__a__class_delete',
        'type': 'class_delete',
        'search': """.class final Lcom/xiaomi/onetrack/d/f$a;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xiaomi/onetrack/d/f;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x1a
    name = "a"
.end annotation


# static fields
.field private static final a:Lcom/xiaomi/onetrack/d/f;


# direct methods
.method static constructor <clinit>()V
    .registers 2

    new-instance v0, Lcom/xiaomi/onetrack/d/f;

    const/4 v1, 0x0

    invoke-direct {v0, v1}, Lcom/xiaomi/onetrack/d/f;-><init>(Lcom/xiaomi/onetrack/d/g;)V

    sput-object v0, Lcom/xiaomi/onetrack/d/f$a;->a:Lcom/xiaomi/onetrack/d/f;

    return-void
.end method

.method private constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method static synthetic a()Lcom/xiaomi/onetrack/d/f;
    .registers 1

    sget-object v0, Lcom/xiaomi/onetrack/d/f$a;->a:Lcom/xiaomi/onetrack/d/f;

    return-object v0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
