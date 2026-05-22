TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/d/g.smali'
CLASS_FALLBACK_NAMES = ['g.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_d_g__class_delete',
        'type': 'class_delete',
        'search': """.class abstract synthetic Lcom/xiaomi/onetrack/d/g;
.super Ljava/lang/Object;
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
