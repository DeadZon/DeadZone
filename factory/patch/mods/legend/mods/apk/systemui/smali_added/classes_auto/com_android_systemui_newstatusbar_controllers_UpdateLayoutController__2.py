"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/controllers/UpdateLayoutController$2.smali'
CLASS_FALLBACK_NAMES = ['UpdateLayoutController$2.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$2;
.super Ljava/lang/Object;

# interfaces
.implements Landroid/view/View$OnLayoutChangeListener;


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x0
    name = null
.end annotation


# instance fields
.field final synthetic this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;


# direct methods
.method constructor <init>(Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$2;->this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;

    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method


# virtual methods
.method public onLayoutChange(Landroid/view/View;IIIIIIII)V
    .registers 21

    move-object v0, p0

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "onLayoutChange: "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {p1}, Ljava/lang/Object;->getClass()Ljava/lang/Class;

    move-result-object v2

    invoke-virtual {v2}, Ljava/lang/Class;->getSimpleName()Ljava/lang/String;

    move-result-object v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    const-string v2, "  isChanged = "

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$2;->this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->isChanged()Z

    move-result v2

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Z)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v1

    const-string v2, "Nastya_super_girl"

    invoke-static {v2, v1}, Landroid/util/Log;->d(Ljava/lang/String;Ljava/lang/String;)I

    iget-object v1, v0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$2;->this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;

    invoke-virtual {v1}, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->isChanged()Z

    move-result v1

    if-nez v1, :cond_5d

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$2;->this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;

    move v3, p2

    move v4, p3

    move v5, p4

    move/from16 v6, p5

    move/from16 v7, p6

    move/from16 v8, p7

    move/from16 v9, p8

    move/from16 v10, p9

    invoke-virtual/range {v2 .. v10}, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->isChange(IIIIIIII)Z

    move-result v1

    if-eqz v1, :cond_5d

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$2;->this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;

    const/4 v3, 0x1

    invoke-virtual {v2, v3}, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->setChanged(Z)V

    iget-object v2, v0, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController$2;->this$0:Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;

    invoke-static {v2}, Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;->access$000(Lcom/android/systemui/newstatusbar/controllers/UpdateLayoutController;)Lcom/android/systemui/newstatusbar/controllers/ElementController;

    move-result-object v2

    invoke-virtual {v2}, Lcom/android/systemui/newstatusbar/controllers/ElementController;->updateMainLayouts()V

    :cond_5d
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_controllers_UpdateLayoutController_2',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
