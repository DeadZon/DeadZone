TARGET_APK = 'Provision.apk'
TARGET_CLASS = 'com/xiaomi/onetrack/Configuration$1.smali'
CLASS_FALLBACK_NAMES = ['Configuration$1.smali']
CLASS_ANCHORS = ['.super Ljava/lang/Object;']

PATCHES = [
    {
        'id': 'com_xiaomi_onetrack_Configuration__1__class_delete',
        'type': 'class_delete',
        'search': """.class abstract synthetic Lcom/xiaomi/onetrack/Configuration$1;
.super Ljava/lang/Object;
""",
        'replacement': """""",
        'required': False,
        'reason': 'Class removed by Provision comparison output.',
    },
]
