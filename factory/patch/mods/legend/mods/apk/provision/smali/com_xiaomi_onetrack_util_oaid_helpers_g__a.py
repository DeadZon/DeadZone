TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/util/oaid/helpers/g$a.smali'
CLASS_FALLBACK_NAMES = ['g$a.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_util_oaid_helpers_g__a__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/util/oaid/helpers/g$a;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xiaomi/onetrack/util/oaid/helpers/g;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x2
    name = "a"
.end annotation


# instance fields
.field a:Ljava/lang/Object;

.field b:Ljava/lang/reflect/Method;

.field c:[Ljava/lang/Object;

.field final synthetic d:Lcom/xiaomi/onetrack/util/oaid/helpers/g;


# direct methods
.method public constructor <init>(Lcom/xiaomi/onetrack/util/oaid/helpers/g;Ljava/lang/Object;Ljava/lang/reflect/Method;[Ljava/lang/Object;)V
    .registers 5

    iput-object p1, p0, Lcom/xiaomi/onetrack/util/oaid/helpers/g$a;->d:Lcom/xiaomi/onetrack/util/oaid/helpers/g;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p2, p0, Lcom/xiaomi/onetrack/util/oaid/helpers/g$a;->a:Ljava/lang/Object;

    iput-object p3, p0, Lcom/xiaomi/onetrack/util/oaid/helpers/g$a;->b:Ljava/lang/reflect/Method;

    iput-object p4, p0, Lcom/xiaomi/onetrack/util/oaid/helpers/g$a;->c:[Ljava/lang/Object;

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
