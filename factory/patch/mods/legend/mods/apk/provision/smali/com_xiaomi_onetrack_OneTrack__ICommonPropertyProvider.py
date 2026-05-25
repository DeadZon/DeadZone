TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/OneTrack$ICommonPropertyProvider.smali'
CLASS_FALLBACK_NAMES = ['OneTrack$ICommonPropertyProvider.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_OneTrack__ICommonPropertyProvider__class_delete',
        'type': 'class_delete',
        'search': """.class public interface abstract Lcom/xiaomi/onetrack/OneTrack$ICommonPropertyProvider;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xiaomi/onetrack/OneTrack;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "ICommonPropertyProvider"
.end annotation
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
