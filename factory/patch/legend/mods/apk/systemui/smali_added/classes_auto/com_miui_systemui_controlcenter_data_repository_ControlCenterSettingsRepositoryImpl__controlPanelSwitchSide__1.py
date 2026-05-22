"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1.smali'
CLASS_FALLBACK_NAMES = ['ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class final Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;
.super Lkotlin/coroutines/jvm/internal/SuspendLambda;

# interfaces
.implements Lkotlin/jvm/functions/Function2;


# annotations
.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lkotlin/coroutines/jvm/internal/SuspendLambda;",
        "Lkotlin/jvm/functions/Function2;"
    }
.end annotation


# instance fields
.field private synthetic L$0:Ljava/lang/Object;

.field label:I


# virtual methods
.method public final create(Ljava/lang/Object;Lkotlin/coroutines/Continuation;)Lkotlin/coroutines/Continuation;
    .registers 4

    new-instance p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;

    const/4 v0, 0x2

    invoke-direct {p0, v0, p2}, Lkotlin/coroutines/jvm/internal/SuspendLambda;-><init>(ILkotlin/coroutines/Continuation;)V

    iput-object p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->L$0:Ljava/lang/Object;

    return-object p0
.end method

.method public final invoke(Ljava/lang/Object;Ljava/lang/Object;)Ljava/lang/Object;
    .registers 3

    check-cast p1, Lkotlinx/coroutines/flow/FlowCollector;

    check-cast p2, Lkotlin/coroutines/Continuation;

    invoke-virtual {p0, p1, p2}, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->create(Ljava/lang/Object;Lkotlin/coroutines/Continuation;)Lkotlin/coroutines/Continuation;

    move-result-object p0

    check-cast p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;

    sget-object p1, Lkotlin/Unit;->INSTANCE:Lkotlin/Unit;

    invoke-virtual {p0, p1}, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;

    move-result-object p0

    return-object p0
.end method

.method public final invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 6

    sget-object v0, Lkotlin/coroutines/intrinsics/CoroutineSingletons;->COROUTINE_SUSPENDED:Lkotlin/coroutines/intrinsics/CoroutineSingletons;

    iget v1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->label:I

    sget-object v2, Lkotlin/Unit;->INSTANCE:Lkotlin/Unit;

    const/4 v3, 0x1

    if-eqz v1, :cond_17

    if-ne v1, v3, :cond_f

    invoke-static {p1}, Lkotlin/ResultKt;->throwOnFailure(Ljava/lang/Object;)V

    goto :goto_27

    :cond_f
    new-instance p0, Ljava/lang/IllegalStateException;

    const-string p1, "call to \'resume\' before \'invoke\' with coroutine"

    invoke-direct {p0, p1}, Ljava/lang/IllegalStateException;-><init>(Ljava/lang/String;)V

    throw p0

    :cond_17
    invoke-static {p1}, Lkotlin/ResultKt;->throwOnFailure(Ljava/lang/Object;)V

    iget-object p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->L$0:Ljava/lang/Object;

    check-cast p1, Lkotlinx/coroutines/flow/FlowCollector;

    iput v3, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$controlPanelSwitchSide$1;->label:I

    invoke-interface {p1, v2, p0}, Lkotlinx/coroutines/flow/FlowCollector;->emit(Ljava/lang/Object;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;

    move-result-object p0

    if-ne p0, v0, :cond_27

    return-object v0

    :cond_27
    :goto_27
    return-object v2
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_miui_systemui_controlcenter_data_repository_ControlCenterSettingsRepositoryImpl_controlPanelSwitchSide_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
