TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/miui/analytics/ITrack.smali'
CLASS_FALLBACK_NAMES = ['ITrack.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Landroid/os/IInterface;']

PATCHES = [
    {
        'id': 'com_miui_analytics_ITrack__class_delete',
        'type': 'class_delete',
        'search': """.class public interface abstract Lcom/miui/analytics/ITrack;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/os/IInterface;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/miui/analytics/ITrack$Stub;
    }
.end annotation


# virtual methods
.method public abstract trackEvent(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;)V
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
