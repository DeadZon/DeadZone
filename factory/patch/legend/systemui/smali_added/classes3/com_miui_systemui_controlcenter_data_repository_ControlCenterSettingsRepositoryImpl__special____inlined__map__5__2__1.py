"""
Legend MiuiSystemUI MTCR patch -- added class.

Target APK   : MiuiSystemUI.apk
Target class : com/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1.smali
DEX group    : classes3
"""
from __future__ import annotations

TARGET_APK           = 'MiuiSystemUI.apk'
TARGET_CLASS         = 'com/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1.smali'
CLASS_FALLBACK_NAMES = ['ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1.smali']
DEX_GROUP            = 'classes3'

PATCHES = [
    {
        'id':          'class_add_com_miui_systemui_controlcenter_data_repository_ControlCente',
        'type':        'class_add',
        'method':      '',
        'method_name': '',
        'search':      None,
        'replacement': '.class public final Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;\n.super Lkotlin/coroutines/jvm/internal/ContinuationImpl;\n\n\n# instance fields\n.field L$0:Ljava/lang/Object;\n\n.field label:I\n\n.field synthetic result:Ljava/lang/Object;\n\n.field final synthetic this$0:Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2;\n\n\n# direct methods\n.method public constructor <init>(Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2;Lkotlin/coroutines/Continuation;)V\n    .registers 3\n\n    iput-object p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;->this$0:Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2;\n\n    invoke-direct {p0, p2}, Lkotlin/coroutines/jvm/internal/ContinuationImpl;-><init>(Lkotlin/coroutines/Continuation;)V\n\n    return-void\n.end method\n\n\n# virtual methods\n.method public final invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;\n    .registers 3\n\n    iput-object p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;->result:Ljava/lang/Object;\n\n    iget p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;->label:I\n\n    const/high16 v0, -0x80000000\n\n    or-int/2addr p1, v0\n\n    iput p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;->label:I\n\n    iget-object p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;->this$0:Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2;\n\n    const/4 v0, 0x0\n\n    invoke-virtual {p1, v0, p0}, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2;->emit(Ljava/lang/Object;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;\n\n    move-result-object p0\n\n    return-object p0\n.end method\n',
        'required':    True,
        'reason':      'Legend MiuiSystemUI MTCR dex.mtcr added class',
    },
]
