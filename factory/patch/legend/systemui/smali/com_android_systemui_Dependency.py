"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/Dependency.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/Dependency.smali'
CLASS_FALLBACK_NAMES = ['Dependency.smali']
CLASS_ANCHORS        = ['invoke-direct {v0, v1}, Lcom/android/systemui/Dependency$DependencyKey;-><init>(Ljava/lang/String;)V', 'sput-object v0, Lcom/android/systemui/Dependency;->BG_LOOPER:Lcom/android/systemui/Dependency$DependencyKey;', 'invoke-direct {v0, v1}, Lcom/android/systemui/Dependency$DependencyKey;-><init>(Ljava/lang/String;)V', 'sput-object v0, Lcom/android/systemui/Dependency;->TIME_TICK_HANDLER:Lcom/android/systemui/Dependency$DependencyKey;', 'invoke-direct {p0}, Ljava/lang/Object;-><init>()V']

PATCHES = [
    {
        'id':             'p0000_get',
        'type':           'method_add',
        'method':         '.method public static get(Ljava/lang/Class;)Ljava/lang/Object;',
        'method_name':    'get',
        'method_anchors': ['sget-object v0, Lcom/android/systemui/Dependency;->sDependency:Lcom/android/systemui/Dependency;', 'iget-object v1, v0, Lcom/android/systemui/Dependency;->mDependencies:Landroid/util/ArrayMap;', 'invoke-virtual {v1, p0}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;'],
        'search':         None,
        'replacement':    '.method public static get(Ljava/lang/Class;)Ljava/lang/Object;\n    .registers 4\n\n    sget-object v0, Lcom/android/systemui/Dependency;->sDependency:Lcom/android/systemui/Dependency;\n\n    monitor-enter v0\n\n    :try_start_0\n    iget-object v1, v0, Lcom/android/systemui/Dependency;->mDependencies:Landroid/util/ArrayMap;\n\n    invoke-virtual {v1, p0}, Landroid/util/ArrayMap;->get(Ljava/lang/Object;)Ljava/lang/Object;\n\n    move-result-object v1\n\n    if-nez v1, :cond_0\n\n    invoke-virtual {v0, p0}, Lcom/android/systemui/Dependency;->createDependency(Ljava/lang/Object;)Ljava/lang/Object;\n\n    move-result-object v1\n\n    iget-object v2, v0, Lcom/android/systemui/Dependency;->mDependencies:Landroid/util/ArrayMap;\n\n    invoke-virtual {v2, p0, v1}, Landroid/util/ArrayMap;->put(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;\n    :try_end_0\n    .catchall {:try_start_0 .. :try_end_0} :catchall_0\n\n    :cond_0\n    monitor-exit v0\n\n    return-object v1\n\n    :catchall_0\n    move-exception p0\n\n    monitor-exit v0\n\n    throw p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr added method',
    },
]
