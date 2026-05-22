"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/ShowMobileTypeController.smali'
CLASS_FALLBACK_NAMES = ['ShowMobileTypeController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/ShowMobileTypeController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt",
        "<",
        "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",
        ">;"
    }
.end annotation


# instance fields
.field private final list:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList",
            "<",
            "Lcom/android/systemui/MiuiOperatorCustomizedPolicy;",
            ">;"
        }
    .end annotation
.end field


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 6

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ShowMobileTypeController;->list:Ljava/util/ArrayList;

    new-instance v0, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;

    const/4 v1, 0x1

    new-array v1, v1, [Ljava/lang/String;

    const/4 v2, 0x0

    const-string v3, "show_type_name_mobile"

    aput-object v3, v1, v2

    invoke-direct {v0, p0, v1}, Lcom/android/systemui/plugins/controllers/ControllerExt$SettingsObserver;-><init>(Lcom/android/systemui/plugins/controllers/ControllerExt;[Ljava/lang/String;)V

    return-void
.end method


# virtual methods
.method public addPolicy(Lcom/android/systemui/MiuiOperatorCustomizedPolicy;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/ShowMobileTypeController;->list:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    return-void
.end method

.method public onSettingsChange(Ljava/lang/String;)V
    .registers 6

    iget-object v2, p0, Lcom/android/systemui/newstatusbar/controllers/ShowMobileTypeController;->list:Ljava/util/ArrayList;

    invoke-virtual {v2}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v2

    :cond_6
    invoke-interface {v2}, Ljava/util/Iterator;->hasNext()Z

    move-result v3

    if-eqz v3, :cond_27

    invoke-interface {v2}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/MiuiOperatorCustomizedPolicy;

    const/4 v0, 0x0

    :goto_13
    iget-object v3, v1, Lcom/android/systemui/MiuiOperatorCustomizedPolicy;->mOperators:Landroid/util/SparseArray;

    invoke-virtual {v3}, Landroid/util/SparseArray;->size()I

    move-result v3

    if-ge v0, v3, :cond_6

    iget-object v3, v1, Lcom/android/systemui/MiuiOperatorCustomizedPolicy;->mOperators:Landroid/util/SparseArray;

    invoke-virtual {v3, v0}, Landroid/util/SparseArray;->keyAt(I)I

    move-result v3

    invoke-virtual {v1, v3}, Lcom/android/systemui/MiuiOperatorCustomizedPolicy;->updateMiuiOperatorConfig(I)V

    add-int/lit8 v0, v0, 0x1

    goto :goto_13

    :cond_27
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_ShowMobileTypeController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
