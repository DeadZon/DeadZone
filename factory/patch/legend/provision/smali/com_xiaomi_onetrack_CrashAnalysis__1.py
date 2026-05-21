TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/CrashAnalysis$1.smali'
CLASS_FALLBACK_NAMES = ['CrashAnalysis$1.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/util/Comparator;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_CrashAnalysis__1__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/CrashAnalysis$1;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/util/Comparator;


# instance fields
.field final synthetic a:Lcom/xiaomi/onetrack/CrashAnalysis;


# direct methods
.method constructor <init>(Lcom/xiaomi/onetrack/CrashAnalysis;)V
    .registers 2

    iput-object p1, p0, Lcom/xiaomi/onetrack/CrashAnalysis$1;->a:Lcom/xiaomi/onetrack/CrashAnalysis;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public compare(Ljava/io/File;Ljava/io/File;)I
    .registers 5

    invoke-virtual {p1}, Ljava/io/File;->lastModified()J

    move-result-wide p0

    invoke-virtual {p2}, Ljava/io/File;->lastModified()J

    move-result-wide v0

    sub-long/2addr p0, v0

    long-to-int p0, p0

    return p0
.end method

.method public bridge synthetic compare(Ljava/lang/Object;Ljava/lang/Object;)I
    .registers 3

    check-cast p1, Ljava/io/File;

    check-cast p2, Ljava/io/File;

    invoke-virtual {p0, p1, p2}, Lcom/xiaomi/onetrack/CrashAnalysis$1;->compare(Ljava/io/File;Ljava/io/File;)I

    move-result p0

    return p0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
