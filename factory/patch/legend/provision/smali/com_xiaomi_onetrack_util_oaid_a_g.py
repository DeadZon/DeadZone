TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/util/oaid/a/g.smali'
CLASS_FALLBACK_NAMES = ['g.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;', '.implements Landroid/os/IInterface;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_util_oaid_a_g__class_delete',
        'type': 'class_delete',
        'search': """.class public interface abstract Lcom/xiaomi/onetrack/util/oaid/a/g;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/os/IInterface;


# virtual methods
.method public abstract b()Ljava/lang/String;
.end method
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
