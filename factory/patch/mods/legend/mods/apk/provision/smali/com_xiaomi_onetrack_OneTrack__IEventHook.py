TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/OneTrack$IEventHook.smali'
CLASS_FALLBACK_NAMES = ['OneTrack$IEventHook.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_OneTrack__IEventHook__class_delete',
        'type': 'class_delete',
        'search': """.class public interface abstract Lcom/xiaomi/onetrack/OneTrack$IEventHook;
.super Ljava/lang/Object;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/xiaomi/onetrack/OneTrack;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "IEventHook"
.end annotation


# virtual methods
.method public abstract isCustomDauEvent(Ljava/lang/String;)Z
.end method

.method public abstract isRecommendEvent(Ljava/lang/String;)Z
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
