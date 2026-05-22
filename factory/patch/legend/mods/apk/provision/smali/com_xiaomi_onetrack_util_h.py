TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/util/h.smali'
CLASS_FALLBACK_NAMES = ['h.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_util_h__class_delete',
        'type': 'class_delete',
        'search': """.class abstract synthetic Lcom/xiaomi/onetrack/util/h;
.super Ljava/lang/Object;
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
