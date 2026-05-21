TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/c/h.smali'
CLASS_FALLBACK_NAMES = ['h.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_c_h__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/c/h;
.super Ljava/lang/Object;


# instance fields
.field public a:Lorg/json/JSONArray;

.field public b:I

.field public c:Ljava/util/ArrayList;

.field public d:Z


# direct methods
.method public constructor <init>(Lorg/json/JSONArray;ILjava/util/ArrayList;Z)V
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Lorg/json/JSONArray;",
            "I",
            "Ljava/util/ArrayList<",
            "Ljava/lang/Long;",
            ">;Z)V"
        }
    .end annotation

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    iput-object p1, p0, Lcom/xiaomi/onetrack/c/h;->a:Lorg/json/JSONArray;

    iput p2, p0, Lcom/xiaomi/onetrack/c/h;->b:I

    iput-object p3, p0, Lcom/xiaomi/onetrack/c/h;->c:Ljava/util/ArrayList;

    iput-boolean p4, p0, Lcom/xiaomi/onetrack/c/h;->d:Z

    return-void
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
