"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1.smali'
CLASS_FALLBACK_NAMES = ['ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public final Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;
.super Lkotlin/coroutines/jvm/internal/ContinuationImpl;


# instance fields
.field L$0:Ljava/lang/Object;

.field label:I

.field synthetic result:Ljava/lang/Object;

.field final synthetic this$0:Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2;


# direct methods
.method public constructor <init>(Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2;Lkotlin/coroutines/Continuation;)V
    .registers 3

    iput-object p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;->this$0:Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2;

    invoke-direct {p0, p2}, Lkotlin/coroutines/jvm/internal/ContinuationImpl;-><init>(Lkotlin/coroutines/Continuation;)V

    return-void
.end method


# virtual methods
.method public final invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;
    .registers 3

    iput-object p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;->result:Ljava/lang/Object;

    iget p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;->label:I

    const/high16 v0, -0x80000000

    or-int/2addr p1, v0

    iput p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;->label:I

    iget-object p1, p0, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2$1;->this$0:Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2;

    const/4 v0, 0x0

    invoke-virtual {p1, v0, p0}, Lcom/miui/systemui/controlcenter/data/repository/ControlCenterSettingsRepositoryImpl$special$$inlined$map$5$2;->emit(Ljava/lang/Object;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;

    move-result-object p0

    return-object p0
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_miui_systemui_controlcenter_data_repository_ControlCenterSettingsRepositoryImpl_special_inlined_map_5_2_1',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
