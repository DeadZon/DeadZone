TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/c/t.smali'
CLASS_FALLBACK_NAMES = ['t.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_c_t__class_delete',
        'type': 'class_delete',
        'search': """.class abstract synthetic Lcom/xiaomi/onetrack/c/t;
.super Ljava/lang/Object;
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
