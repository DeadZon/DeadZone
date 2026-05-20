"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/statusbar/policy/NotificationIconObserver.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/statusbar/policy/NotificationIconObserver.smali'
CLASS_FALLBACK_NAMES = ['NotificationIconObserver.smali']
CLASS_ANCHORS        = ['invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'invoke-virtual {p1, v0, v1}, Lcom/android/systemui/util/settings/repository/UserAwareSettingsRepository;->intSetting(ILjava/lang/String;)Lkotlinx/coroutines/flow/Flow;', 'iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NotificationIconObserver;->maxIconFlow:Lkotlinx/coroutines/flow/Flow;']

PATCHES = [
    {
        'id':             'p0000__init_',
        'type':           'method_replace',
        'method':         '.method public constructor <init>(Lcom/miui/systemui/settings/data/repository/MiuiSystemSettingsRepository;)V',
        'method_name':    '<init>',
        'method_anchors': ['invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'invoke-virtual {p1, v0, v1}, Lcom/android/systemui/util/settings/repository/UserAwareSettingsRepository;->intSetting(ILjava/lang/String;)Lkotlinx/coroutines/flow/Flow;', 'iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NotificationIconObserver;->maxIconFlow:Lkotlinx/coroutines/flow/Flow;'],
        'search':         '.method public constructor <init>(Lcom/miui/systemui/settings/data/repository/MiuiSystemSettingsRepository;)V\n    .registers 4\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    const/4 v0, 0x1\n\n    check-cast p1, Lcom/android/systemui/util/settings/repository/UserAwareSettingsRepository;\n\n    const-string v1, "status_bar_show_notification_icon"\n\n    invoke-virtual {p1, v0, v1}, Lcom/android/systemui/util/settings/repository/UserAwareSettingsRepository;->intSetting(ILjava/lang/String;)Lkotlinx/coroutines/flow/Flow;\n\n    move-result-object p1\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NotificationIconObserver;->maxIconFlow:Lkotlinx/coroutines/flow/Flow;\n\n    return-void\n.end method\n',
        'replacement':    '.method public constructor <init>(Lcom/miui/systemui/settings/data/repository/MiuiSystemSettingsRepository;)V\n    .registers 4\n\n    invoke-direct {p0}, Ljava/lang/Object;-><init>()V\n\n    const/4 v0, 0x7\n\n    check-cast p1, Lcom/android/systemui/util/settings/repository/UserAwareSettingsRepository;\n\n    const-string v1, "status_bar_show_notification_icon"\n\n    invoke-virtual {p1, v0, v1}, Lcom/android/systemui/util/settings/repository/UserAwareSettingsRepository;->intSetting(ILjava/lang/String;)Lkotlinx/coroutines/flow/Flow;\n\n    move-result-object p1\n\n    iput-object p1, p0, Lcom/android/systemui/statusbar/policy/NotificationIconObserver;->maxIconFlow:Lkotlinx/coroutines/flow/Flow;\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
]
