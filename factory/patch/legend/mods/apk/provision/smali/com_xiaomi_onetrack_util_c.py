TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/util/c.smali'
CLASS_FALLBACK_NAMES = ['c.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Ljava/io/FilenameFilter;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_util_c__class_delete',
        'type': 'class_delete',
        'search': """.class Lcom/xiaomi/onetrack/util/c;
.super Ljava/lang/Object;

# interfaces
.implements Ljava/io/FilenameFilter;


# direct methods
.method constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public accept(Ljava/io/File;Ljava/lang/String;)Z
    .registers 3

    invoke-static {p2}, Landroid/text/TextUtils;->isDigitsOnly(Ljava/lang/CharSequence;)Z

    move-result p0

    return p0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
