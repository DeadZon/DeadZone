"""
Legend MiuiSystemUI generated patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1.smali'
CLASS_FALLBACK_NAMES = ['ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_systemui_controlcenter_data_repository_ControlCente',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class final Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;\n.super Lkotlin/coroutines/jvm/internal/SuspendLambda;\n\n# interfaces\n.implements Lkotlin/jvm/functions/Function2;\n\n\n# annotations\n.annotation system Ldalvik/annotation/Signature;\n    value = {\n        "Lkotlin/coroutines/jvm/internal/SuspendLambda;",\n        "Lkotlin/jvm/functions/Function2;"\n    }\n.end annotation\n\n\n# instance fields\n.field private synthetic L$0:Ljava/lang/Object;\n\n.field label:I\n\n\n# virtual methods\n.method public final create(Ljava/lang/Object;Lkotlin/coroutines/Continuation;)Lkotlin/coroutines/Continuation;\n    .registers 4\n\n    new-instance p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;\n\n    const/4 v0, 0x2\n\n    invoke-direct {p0, v0, p2}, Lkotlin/coroutines/jvm/internal/SuspendLambda;-><init>(ILkotlin/coroutines/Continuation;)V\n\n    iput-object p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->L$0:Ljava/lang/Object;\n\n    return-object p0\n.end method\n\n.method public final invoke(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;\n    .registers 3\n\n    check-cast p1, Lkotlinx/coroutines/flow/FlowCollector;\n\n    check-cast p2, Lkotlin/coroutines/Continuation;\n\n    invoke-virtual {p0, p1, p2}, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->create(Ljava/lang/Object;Lkotlin/coroutines/Continuation;)Lkotlin/coroutines/Continuation;\n\n    move-result-object p0\n\n    check-cast p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;\n\n    sget-object p1, Lkotlin/Unit;->INSTANCE:Lkotlin/Unit;\n\n    invoke-virtual {p0, p1}, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;\n\n    move-result-object p0\n\n    return-object p0\n.end method\n\n.method public final invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;\n    .registers 6\n\n    sget-object v0, Lkotlin/coroutines/intrinsics/CoroutineSingletons;->COROUTINE_SUSPENDED:Lkotlin/coroutines/intrinsics/CoroutineSingletons;\n\n    iget v1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->label:I\n\n    sget-object v2, Lkotlin/Unit;->INSTANCE:Lkotlin/Unit;\n\n    const/4 v3, 0x1\n\n    if-eqz v1, :cond_1\n\n    if-ne v1, v3, :cond_0\n\n    invoke-static {p1}, Lkotlin/ResultKt;->throwOnFailure(Ljava/lang/Object;)V\n\n    goto :goto_0\n\n    :cond_0\n    new-instance p0, Ljava/lang/IllegalStateException;\n\n    const-string p1, "call to \\\'resume\\\' before \\\'invoke\\\' with coroutine"\n\n    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V\n\n    throw p0\n\n    :cond_1\n    invoke-static {p1}, Lkotlin/ResultKt;->throwOnFailure(Ljava/lang/Object;)V\n\n    iget-object p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->L$0:Ljava/lang/Object;\n\n    check-cast p1, Lkotlinx/coroutines/flow/FlowCollector;\n\n    iput v3, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->label:I\n\n    invoke-interface {p1, v2, p0}, Lkotlinx/coroutines/flow/FlowCollector;->emit(Ljava/lang/Object;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;\n\n    move-result-object p0\n\n    if-ne p0, v0, :cond_2\n\n    return-object v0\n\n    :cond_2\n    :goto_0\n    return-object v2\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI generated generated dex rule added class',
    },
]
