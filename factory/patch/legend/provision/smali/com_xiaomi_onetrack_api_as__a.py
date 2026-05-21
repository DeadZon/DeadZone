TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/api/as$a.smali'
CLASS_FALLBACK_NAMES = ['as$a.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_api_as__a__class_delete',
        'type': 'class_delete',
        'search': """.class public interface abstract Lcom/xiaomi/onetrack/api/as$a;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xiaomi/onetrack/api/as;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "a"
.end annotation


# virtual methods
.method public abstract a()V
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
