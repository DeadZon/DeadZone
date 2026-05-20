"""
Legend MiuiSystemUI MTCR patch — modified class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1.smali
Patches      : 1
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1.smali'
CLASS_FALLBACK_NAMES = ['MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1.smali']
CLASS_ANCHORS        = ['invoke-direct {p0}, Ljava/lang/Object;-><init>()V', 'iput-object p1, p0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1;->$$this$conflatedCallbackFlow:Lkotlinx/coroutines/channels/ProducerScope;', 'iput-object p2, p0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1;->this$0:Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl;', 'iget-object v0, p0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1;->this$0:Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl;', 'iget-object v0, v0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl;->context:Landroid/content/Context;']

PATCHES = [
    {
        'id':             'p0000_onUiModeChanged',
        'type':           'method_replace',
        'method':         '.method public final onUiModeChanged()V',
        'method_name':    'onUiModeChanged',
        'method_anchors': ['iget-object v0, p0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1;->this$0:Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl;', 'iget-object v0, v0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl;->context:Landroid/content/Context;', 'invoke-static {v0}, Lcom/miui/utils/configs/MiuiConfigs;->isNightMode1(Landroid/content/Context;)Z'],
        'search':         '.method public final onUiModeChanged()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1;->this$0:Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl;\n\n    iget-object v0, v0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl;->context:Landroid/content/Context;\n\n    invoke-static {v0}, Lcom/miui/utils/configs/MiuiConfigs;->isNightMode(Landroid/content/Context;)Z\n\n    move-result v0\n\n    invoke-static {v0}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;\n\n    move-result-object v0\n\n    iget-object p0, p0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1;->$$this$conflatedCallbackFlow:Lkotlinx/coroutines/channels/ProducerScope;\n\n    check-cast p0, Lkotlinx/coroutines/channels/ProducerCoroutine;\n\n    invoke-virtual {p0, v0}, Lkotlinx/coroutines/channels/ProducerCoroutine;->trySend-JP2dKIU(Ljava/lang/Object;)Ljava/lang/Object;\n\n    return-void\n.end method\n',
        'replacement':    '.method public final onUiModeChanged()V\n    .registers 2\n\n    iget-object v0, p0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1;->this$0:Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl;\n\n    iget-object v0, v0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl;->context:Landroid/content/Context;\n\n    invoke-static {v0}, Lcom/miui/utils/configs/MiuiConfigs;->isNightMode1(Landroid/content/Context;)Z\n\n    move-result v0\n\n    invoke-static {v0}, Ljava/lang/Boolean;->valueOf(Z)Ljava/lang/Boolean;\n\n    move-result-object v0\n\n    iget-object p0, p0, Lcom/miui/systemui/common/ui/data/repository/MiuiConfigurationRepositoryImpl$isNightMode$1$listener$1;->$$this$conflatedCallbackFlow:Lkotlinx/coroutines/channels/ProducerScope;\n\n    check-cast p0, Lkotlinx/coroutines/channels/ProducerCoroutine;\n\n    invoke-virtual {p0, v0}, Lkotlinx/coroutines/channels/ProducerCoroutine;->trySend-JP2dKIU(Ljava/lang/Object;)Ljava/lang/Object;\n\n    return-void\n.end method\n',
        'required':       True,
        'reason':         'Legend MiuiSystemUI MTCR dex.mtcr modified class',
    },
]
