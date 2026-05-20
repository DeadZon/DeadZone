"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/sim/SimTypeView.smali'
CLASS_FALLBACK_NAMES = ['SimTypeView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/sim/SimTypeView;
.super Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;


# instance fields
.field protected controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    const/4 v0, 0x0

    invoke-direct {p0, p1, p2, v0}, Lcom/android/systemui/newstatusbar/sim/SimTypeView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/views/ext/ExtTextView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    return-void
.end method


# virtual methods
.method protected getData()Lcom/android/systemui/newstatusbar/data/TextData;
    .registers 2

    goto/32 :goto_1f

    nop

    :goto_4
    return-object v0

    :goto_5
    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->getSimTypeData()Lcom/android/systemui/newstatusbar/data/TextData;

    move-result-object v0

    goto/32 :goto_4

    nop

    :goto_d
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_5

    nop

    :goto_13
    const-class v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_2b

    nop

    :goto_19
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    :goto_1b
    goto/32 :goto_d

    nop

    :goto_1f
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_33

    nop

    :goto_25
    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_19

    nop

    :goto_2b
    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto/32 :goto_25

    nop

    :goto_33
    if-eqz v0, :cond_38

    goto/32 :goto_1b

    :cond_38
    goto/32 :goto_13

    nop
.end method

.method protected onAttached()V
    .registers 2

    goto/32 :goto_4

    nop

    :goto_4
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_a

    nop

    :goto_a
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_11

    nop

    :goto_11
    return-void
.end method

.method protected onDetached()V
    .registers 2

    goto/32 :goto_5

    nop

    :goto_4
    return-void

    :goto_5
    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeView;->controller:Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;

    goto/32 :goto_b

    nop

    :goto_b
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/MobileIconColorSizeController;->removeCallBack(Lcom/android/systemui/newstatusbar/controllers/IconController$IconCallBack;)V

    goto/32 :goto_4

    nop
.end method

.method public onIconChange()V
    .registers 1

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimTypeView;->update()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_sim_SimTypeView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
