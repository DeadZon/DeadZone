"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/sim/CustomSimIcon.smali'
CLASS_FALLBACK_NAMES = ['CustomSimIcon.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;
.super Lcom/android/systemui/newstatusbar/sim/SimIcon;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/CustomIconController$CallBack;


# instance fields
.field private iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

.field private mIds:I


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/sim/SimIcon;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/sim/SimIcon;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    return-void
.end method


# virtual methods
.method protected onAttached()V
    .registers 2

    goto/32 :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->onAttached()V

    goto/32 :goto_13

    nop

    :goto_c
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->addCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    goto/32 :goto_4

    nop

    :goto_13
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    goto/32 :goto_c

    nop
.end method

.method protected onDetached()V
    .registers 2

    goto/32 :goto_b

    nop

    :goto_4
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    goto/32 :goto_12

    nop

    :goto_b
    invoke-super {p0}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->onDetached()V

    goto/32 :goto_13

    nop

    :goto_12
    return-void

    :goto_13
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    goto/32 :goto_4

    nop
.end method

.method public onIconStyleChange()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    iget v1, p0, Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;->mIds:I

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getSimIds(I)I

    move-result v0

    invoke-super {p0, v0}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->setImageResource(I)V

    return-void
.end method

.method public setImageResource(I)V
    .registers 3

    iput p1, p0, Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;->mIds:I

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    if-nez v0, :cond_10

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    :cond_10
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/CustomSimIcon;->iconController:Lcom/android/systemui/newstatusbar/controllers/CustomIconController;

    invoke-virtual {v0, p1}, Lcom/android/systemui/newstatusbar/controllers/CustomIconController;->getSimIds(I)I

    move-result v0

    invoke-super {p0, v0}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->setImageResource(I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_sim_CustomSimIcon',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
