"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/DateLayout.smali'
CLASS_FALLBACK_NAMES = ['DateLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/DateLayout;
.super Lcom/android/systemui/newstatusbar/layouts/ElementLayout;

# interfaces
.implements Lcom/android/systemui/newstatusbar/policy/ISlots;


# instance fields
.field private child:Lcom/android/systemui/newstatusbar/views/DateView;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method


# virtual methods
.method getView()Landroid/view/View;
    .registers 4

    goto/32 :goto_2e

    nop

    :goto_4
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/DateLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_13

    nop

    :goto_c
    check-cast v0, Lcom/android/systemui/newstatusbar/views/DateView;

    goto/32 :goto_3e

    nop

    :goto_12
    return-object v0

    :goto_13
    const-string v2, "element_date"

    goto/32 :goto_36

    nop

    :goto_19
    const/4 v2, 0x0

    goto/32 :goto_1e

    nop

    :goto_1e
    invoke-virtual {v0, v1, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_c

    nop

    :goto_26
    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    goto/32 :goto_4

    nop

    :goto_2e
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/DateLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto/32 :goto_26

    nop

    :goto_36
    invoke-static {v1, v2}, Landroid/Utils/Utils;->LayoutToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    goto/32 :goto_19

    nop

    :goto_3e
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/DateLayout;->child:Lcom/android/systemui/newstatusbar/views/DateView;

    goto/32 :goto_12

    nop
.end method

.method public setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/DateLayout;->child:Lcom/android/systemui/newstatusbar/views/DateView;

    invoke-interface {v0, p1}, Lcom/android/systemui/newstatusbar/policy/ISlots;->setSlot(Lcom/android/systemui/newstatusbar/controllers/ElementController$Slots;)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_DateLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
