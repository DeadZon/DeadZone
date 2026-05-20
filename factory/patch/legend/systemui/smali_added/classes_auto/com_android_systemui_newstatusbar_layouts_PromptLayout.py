"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/PromptLayout.smali'
CLASS_FALLBACK_NAMES = ['PromptLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/PromptLayout;
.super Lcom/android/systemui/newstatusbar/layouts/ElementLayout;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method


# virtual methods
.method public getAddedChild()Landroid/view/View;
    .registers 2

    const/4 v0, 0x0

    return-object v0
.end method

.method getView()Landroid/view/View;
    .registers 4

    goto/32 :goto_29

    nop

    :goto_4
    invoke-virtual {v0, v1, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_37

    nop

    :goto_c
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/PromptLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_31

    nop

    :goto_14
    const/4 v2, 0x0

    goto/32 :goto_4

    nop

    :goto_19
    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    goto/32 :goto_c

    nop

    :goto_21
    invoke-static {v1, v2}, Landroid/Utils/Utils;->LayoutToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    goto/32 :goto_14

    nop

    :goto_29
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/PromptLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto/32 :goto_19

    nop

    :goto_31
    const-string v2, "element_prompt"

    goto/32 :goto_21

    nop

    :goto_37
    return-object v0
.end method

.method protected onMeasure(II)V
    .registers 4

    goto/32 :goto_11

    nop

    :goto_4
    invoke-virtual {p0, v0, v0}, Lcom/android/systemui/newstatusbar/layouts/PromptLayout;->setMeasuredDimension(II)V

    goto/32 :goto_10

    nop

    :goto_b
    const/4 v0, 0x0

    goto/32 :goto_4

    nop

    :goto_10
    return-void

    :goto_11
    invoke-super {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;->onMeasure(II)V

    goto/32 :goto_b

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_PromptLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
