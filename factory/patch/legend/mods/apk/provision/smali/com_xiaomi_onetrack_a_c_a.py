TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/a/c/a.smali'
CLASS_FALLBACK_NAMES = ['a.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_a_c_a__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/a/c/a;
.super Ljava/lang/Object;


# instance fields
.field public a:I

.field public b:Ljava/util/ArrayList;

.field public c:Z


# direct methods
.method public constructor <init>(ILjava/util/ArrayList;Z)V
    .registers 4
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(I",
            "Ljava/util/ArrayList<",
            "Lcom/xiaomi/onetrack/a/b/a;",
            ">;Z)V"
        }
    .end annotation

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput p1, p0, Lcom/xiaomi/onetrack/a/c/a;->a:I

    iput-object p2, p0, Lcom/xiaomi/onetrack/a/c/a;->b:Ljava/util/ArrayList;

    iput-boolean p3, p0, Lcom/xiaomi/onetrack/a/c/a;->c:Z

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
