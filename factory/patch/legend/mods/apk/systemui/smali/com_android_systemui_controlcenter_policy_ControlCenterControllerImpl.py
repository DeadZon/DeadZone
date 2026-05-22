"""
Legend MiuiSystemUI generated patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/android/systemui/controlcenter/policy/ControlCenterControllerImpl.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/android/systemui/controlcenter/policy/ControlCenterControllerImpl.smali'
CLASS_FALLBACK_NAMES = ['ControlCenterControllerImpl.smali']
CLASS_ANCHORS        = ['sget-boolean v0, Lcom/miui/utils/configs/MiuiDebugConfig;->DEBUG:Z', 'invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'iput-object p2, p0, Lcom/android/systemui/controlcenter/policy/ControlCenterControllerImpl;->keyguardViewMediator:Ldagger/Lazy;', 'iput-object p3, p0, Lcom/android/systemui/controlcenter/policy/ControlCenterControllerImpl;->keyguardStateController:Ldagger/Lazy;', 'iput-object p4, p0, Lcom/android/systemui/controlcenter/policy/ControlCenterControllerImpl;->commandQueue:Ldagger/Lazy;']

PATCHES = [
    {
        'id':             'p0000_isControlPanelSwitchSide',
        'type':           'method_add',
        'method':         '.method public final isControlPanelSwitchSide()Z',
        'method_name':    'isControlPanelSwitchSide',
        'method_anchors': ['iget-object p0, p0, Lcom/android/systemui/controlcenter/policy/ControlCenterControllerImpl;->controlCenterSettingsRepository:Lcom/miui/interfaces/controlcenter/data/repository/ControlCenterSettingsRepository;', 'iget-object p0, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl;->controlPanelSwitchSide:Lkotlinx/coroutines/flow/ReadonlyStateFlow;', 'invoke-virtual {p0}, Lkotlinx/coroutines/flow/ReadonlyStateFlow;->getValue()Ljava/lang/Object;'],
        'search':         None,
        'replacement':    '.method public final isControlPanelSwitchSide()Z\n    .registers 1\n\n    iget-object p0, p0, Lcom/android/systemui/controlcenter/policy/ControlCenterControllerImpl;->controlCenterSettingsRepository:Lcom/miui/interfaces/controlcenter/data/repository/ControlCenterSettingsRepository;\n\n    check-cast p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl;\n\n    iget-object p0, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl;->controlPanelSwitchSide:Lkotlinx/coroutines/flow/ReadonlyStateFlow;\n\n    invoke-virtual {p0}, Lkotlinx/coroutines/flow/ReadonlyStateFlow;->getValue()Ljava/lang/Object;\n\n    move-result-object p0\n\n    check-cast p0, Ljava/lang/Boolean;\n\n    invoke-virtual {p0}, Ljava/lang/Boolean;->booleanValue()Z\n\n    move-result p0\n\n    return p0\n.end method\n',
        'required':       False,
        'reason':         'Legend MiuiSystemUI generated generated dex rule added method',
    },
]
