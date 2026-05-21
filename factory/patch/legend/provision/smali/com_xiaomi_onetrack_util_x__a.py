TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/util/x$a.smali'
CLASS_FALLBACK_NAMES = ['x$a.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.field private static final a:Lcom/xiaomi/onetrack/util/x;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_util_x__a__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/util/x$a;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xiaomi/onetrack/util/x;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0xa
    name = "a"
.end annotation


# static fields
.field private static final a:Lcom/xiaomi/onetrack/util/x;


# direct methods
.method static constructor <clinit>()V
    .registers 2

    new-instance v0, Lcom/xiaomi/onetrack/util/x;

    const/4 v1, 0x0

    invoke-direct {v0, v1}, Lcom/xiaomi/onetrack/util/x;-><init>(Lcom/xiaomi/onetrack/util/y;)V

    sput-object v0, Lcom/xiaomi/onetrack/util/x$a;->a:Lcom/xiaomi/onetrack/util/x;

    return-void
.end method

.method private constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method static synthetic a()Lcom/xiaomi/onetrack/util/x;
    .registers 1

    sget-object v0, Lcom/xiaomi/onetrack/util/x$a;->a:Lcom/xiaomi/onetrack/util/x;

    return-object v0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
