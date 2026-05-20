"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController.smali'
CLASS_FALLBACK_NAMES = ['NotifHeaderTransitionController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;",
        ">;"
    }
.end annotation


# instance fields
.field private final parent:Ljava/util/ArrayList;
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/layouts/HeaderParent;",
            ">;"
        }
    .end annotation
.end field


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    new-instance v0, Ljava/util/ArrayList;

    invoke-direct {v0}, Ljava/util/ArrayList;-><init>()V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->parent:Ljava/util/ArrayList;

    return-void
.end method


# virtual methods
.method public onAlphaChange(F)V
    .registers 5

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->parent:Ljava/util/ArrayList;

    invoke-virtual {v0}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_6
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_25

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/layouts/HeaderParent;

    if-eqz v1, :cond_24

    invoke-virtual {v1, p1}, Lcom/android/systemui/newstatusbar/layouts/HeaderParent;->setAlpha(F)V

    const v2, 0x3f666666  # 0.9f

    cmpl-float v2, p1, v2

    if-lez v2, :cond_20

    const/4 v2, 0x0

    goto :goto_21

    :cond_20
    const/4 v2, 0x4

    :goto_21
    invoke-virtual {v1, v2}, Lcom/android/systemui/newstatusbar/layouts/HeaderParent;->setVisibility(I)V

    :cond_24
    goto :goto_6

    :cond_25
    return-void
.end method

.method public setParent(Lcom/android/systemui/newstatusbar/layouts/HeaderParent;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->parent:Ljava/util/ArrayList;

    invoke-virtual {v0, p1}, Ljava/util/ArrayList;->add(Ljava/lang/Object;)Z

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_NotifHeaderTransitionController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
