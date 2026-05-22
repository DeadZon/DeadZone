TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/DefaultEventHook.smali'
CLASS_FALLBACK_NAMES = ['DefaultEventHook.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Lcom/xiaomi/onetrack/OneTrack$IEventHook;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_DefaultEventHook__class_delete',
        'type': 'class_delete',
        'search': """.class public Lcom/xiaomi/onetrack/DefaultEventHook;
.super Ljava/lang/Object;

# interfaces
.implements Lcom/xiaomi/onetrack/OneTrack$IEventHook;


# direct methods
.method public constructor <init>()V
    .registers 1

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public isCustomDauEvent(Ljava/lang/String;)Z
    .registers 2

    const/4 p0, 0x0

    return p0
.end method

.method public isRecommendEvent(Ljava/lang/String;)Z
    .registers 2

    const/4 p0, 0x0

    return p0
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
