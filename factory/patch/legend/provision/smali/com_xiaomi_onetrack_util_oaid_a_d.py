TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/util/oaid/a/d.smali'
CLASS_FALLBACK_NAMES = ['d.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Landroid/os/IInterface;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_util_oaid_a_d__class_delete',
        'type': 'class_delete',
        'search': """.class public interface abstract Lcom/xiaomi/onetrack/util/oaid/a/d;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/os/IInterface;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/xiaomi/onetrack/util/oaid/a/d$a;
    }
.end annotation
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
