"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/tuner/TunerServiceImpl.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/tuner/TunerServiceImpl.smali'
CLASS_FALLBACK_NAMES = ['TunerServiceImpl.smali']
CLASS_ANCHORS        = ['sput-object v0, Lcom/android/systemui/tuner/TunerServiceImpl;->RESET_EXCEPTION_LIST:[Ljava/lang/String;', 'invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'invoke-direct {v0, p0}, Lcom/android/systemui/tuner/TunerServiceImpl$Observer;-><init>(Lcom/android/systemui/tuner/TunerServiceImpl;)V', 'iput-object v0, p0, Lcom/android/systemui/tuner/TunerServiceImpl;->mObserver:Lcom/android/systemui/tuner/TunerServiceImpl$Observer;', 'invoke-direct {v0}, Landroid/util/ArrayMap;-><init>()V']

PATCHES = [
    {
        'id':             'p0000_getValue',
        'type':           'method_add',
        'method':         '.method public final getValue(ILjava/lang/String;)I',
        'method_name':    'getValue',
        'method_anchors': ['iget-object v0, p0, Lcom/android/systemui/tuner/TunerServiceImpl;->mContentResolver:Landroid/content/ContentResolver;', 'iget p0, p0, Lcom/android/systemui/tuner/TunerServiceImpl;->mCurrentUser:I', 'invoke-static {v0, p2, p1, p0}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I'],
        'search':         None,
        'replacement':    '.method public final getValue(ILjava/lang/String;)I\n    .registers 4\n\n    iget-object v0, p0, Lcom/android/systemui/tuner/TunerServiceImpl;->mContentResolver:Landroid/content/ContentResolver;\n\n    iget p0, p0, Lcom/android/systemui/tuner/TunerServiceImpl;->mCurrentUser:I\n\n    invoke-static {v0, p2, p1, p0}, Landroid/provider/Settings$Secure;->getIntForUser(Landroid/content/ContentResolver;Ljava/lang/String;II)I\n\n    move-result p0\n\n    return p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
]
