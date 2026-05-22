"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/StatusLayout.smali'
CLASS_FALLBACK_NAMES = ['StatusLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/StatusLayout;
.super Lcom/android/systemui/newstatusbar/layouts/ElementLayout;


# instance fields
.field private child:Landroid/view/View;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method


# virtual methods
.method public getChild()Landroid/view/View;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/StatusLayout;->child:Landroid/view/View;

    return-object v0
.end method

.method getView()Landroid/view/View;
    .registers 4

    goto/32 :goto_a

    nop

    :goto_4
    iput-object v0, p0, Lcom/android/systemui/newstatusbar/layouts/StatusLayout;->child:Landroid/view/View;

    goto/32 :goto_28

    nop

    :goto_a
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/StatusLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto/32 :goto_18

    nop

    :goto_12
    const-string v2, "element_status"

    goto/32 :goto_2e

    nop

    :goto_18
    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    goto/32 :goto_20

    nop

    :goto_20
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/StatusLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_12

    nop

    :goto_28
    return-object v0

    :goto_29
    const/4 v2, 0x0

    goto/32 :goto_36

    nop

    :goto_2e
    invoke-static {v1, v2}, Landroid/Utils/Utils;->LayoutToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    goto/32 :goto_29

    nop

    :goto_36
    invoke-virtual {v0, v1, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_4

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_StatusLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
