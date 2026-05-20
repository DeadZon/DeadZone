"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/ClockLayout.smali'
CLASS_FALLBACK_NAMES = ['ClockLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/ClockLayout;
.super Lcom/android/systemui/newstatusbar/layouts/ElementLayout;

# interfaces
.implements Lcom/android/systemui/newstatusbar/policy/ISlots;
.implements Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;


# instance fields
.field private child:Lcom/android/systemui/newstatusbar/clock/ClockView;

.field private lastPosition:I

.field private final sKeyCenterElemEnableInIsland:Ljava/lang/String;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, -0x5

    iput v0, p0, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->lastPosition:I

    const-string v0, "status_bar_elem_center_in_island"

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->sKeyCenterElemEnableInIsland:Ljava/lang/String;

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->setClipChildren(Z)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->setClipToPadding(Z)V

    return-void
.end method


# virtual methods
.method public getClockView()Lcom/android/systemui/newstatusbar/clock/ClockView;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->child:Lcom/android/systemui/newstatusbar/clock/ClockView;

    return-object v0
.end method

.method getView()Landroid/view/View;
    .registers 4

    goto/32 :goto_9

    nop

    :goto_4
    const/4 v2, 0x0

    goto/32 :goto_2d

    nop

    :goto_9
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto/32 :goto_1f

    nop

    :goto_11
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_27

    nop

    :goto_19
    check-cast v0, Lcom/android/systemui/newstatusbar/clock/ClockView;

    goto/32 :goto_35

    nop

    :goto_1f
    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    goto/32 :goto_11

    nop

    :goto_27
    const-string v2, "element_clock"

    goto/32 :goto_3c

    nop

    :goto_2d
    invoke-virtual {v0, v1, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_19

    nop

    :goto_35
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->child:Lcom/android/systemui/newstatusbar/clock/ClockView;

    goto/32 :goto_3b

    nop

    :goto_3b
    return-object v0

    :goto_3c
    invoke-static {v1, v2}, Landroid/Utils/Utils;->LayoutToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    goto/32 :goto_4

    nop
.end method

.method public onIslandShowChange(Z)V
    .registers 4

    if-eqz p1, :cond_14

    const-string v0, "status_bar_elem_center_in_island"

    invoke-static {v0}, Landroid/preference/SettingsMezoHelper;->getBoolofSettings1(Ljava/lang/String;)Z

    move-result v0

    if-nez v0, :cond_14

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->getClockView()Lcom/android/systemui/newstatusbar/clock/ClockView;

    move-result-object v0

    const/16 v1, 0x8

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->setVisibility(I)V

    goto :goto_1e

    :cond_14
    if-nez p1, :cond_1e

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->getClockView()Lcom/android/systemui/newstatusbar/clock/ClockView;

    move-result-object v0

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/clock/ClockView;->setVisibility(I)V

    :cond_1e
    :goto_1e
    return-void
.end method

.method public onViewAdded(Landroid/view/View;)V
    .registers 4

    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->onViewAdded(Landroid/view/View;)V

    instance-of v0, p1, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;

    if-eqz v0, :cond_14

    move-object v0, p1

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;

    const/4 v1, 0x0

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->setClipChildren(Z)V

    move-object v0, p1

    check-cast v0, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;

    invoke-virtual {v0, v1}, Lcom/android/systemui/newstatusbar/layouts/OverflowLayout;->setClipToPadding(Z)V

    :cond_14
    return-void
.end method

.method public setPosition(I)V
    .registers 4

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/IslandController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/IslandController;

    if-nez p1, :cond_15

    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;)V

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->isShown()Z

    move-result v1

    invoke-virtual {p0, v1}, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->onIslandShowChange(Z)V

    goto :goto_18

    :cond_15
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->removeCallBack(Lcom/android/systemui/plugins/controllers/ControllerExt$CallBack;)V

    :goto_18
    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->setPosition(I)V

    return-void
.end method

.method public setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/ClockLayout;->child:Lcom/android/systemui/newstatusbar/clock/ClockView;

    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/policy/ISlots;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_ClockLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
