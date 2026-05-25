TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/f/c.smali'
CLASS_FALLBACK_NAMES = ['c.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_f_c__class_delete',
        'type': 'class_delete',
        'search': """.class abstract synthetic Lcom/xiaomi/onetrack/f/c;
.super Ljava/lang/Object;
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
