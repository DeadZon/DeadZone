"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/IconController.smali'
CLASS_FALLBACK_NAMES = ['IconController.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public abstract Lcom/android/systemui/newstatusbar/controllers/IconController;
.super Lcom/android/systemui/plugins/controllers/ControllerExt;


# annotations
.annotation system Ldalvik/annotation/MemberClasses;
    value = {
        Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;
    }
.end annotation

.annotation system Ldalvik/annotation/Signature;
    value = {
        "Lcom/android/systemui/plugins/controllers/ControllerExt<",
        "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
        ">;"
    }
.end annotation


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 2

    invoke-direct {p0, p1}, Lcom/android/systemui/plugins/controllers/ControllerExt;-><init>(Landroid/content/Context;)V

    return-void
.end method


# virtual methods
.method public abstract addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
.end method

.method public bridge synthetic addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IconController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public abstract removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V
.end method

.method public bridge synthetic removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V
    .registers 2

    check-cast p1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    invoke-virtual {p0, p1}, Lcom/android/systemui/newstatusbar/controllers/IconController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    return-void
.end method

.method public updateCallBacks(Ljava/util/ArrayList;)V
    .registers 5
    .annotation system Ldalvik/annotation/Signature;
        value = {
            "(",
            "Ljava/util/ArrayList<",
            "Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;",
            ">;)V"
        }
    .end annotation

    invoke-virtual {p1}, Ljava/util/ArrayList;->iterator()Ljava/util/Iterator;

    move-result-object v0

    :goto_4
    invoke-interface {v0}, Ljava/util/Iterator;->hasNext()Z

    move-result v1

    if-eqz v1, :cond_21

    invoke-interface {v0}, Ljava/util/Iterator;->next()Ljava/lang/Object;

    move-result-object v1

    check-cast v1, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;

    instance-of v2, v1, Landroid/view/View;

    if-eqz v2, :cond_1d

    new-instance v2, Lcom/android/systemui/newstatusbar/controllers/IconController$1;

    invoke-direct {v2, p0, v1}, Lcom/android/systemui/newstatusbar/controllers/IconController$1;-><init>(Lcom/android/systemui/newstatusbar/controllers/IconController;Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    invoke-interface {v1, v2}, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;->post(Ljava/lang/Runnable;)Z

    goto :goto_20

    :cond_1d
    invoke-interface {v1}, Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;->onIconChange()V

    :goto_20
    goto :goto_4

    :cond_21
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_IconController',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
