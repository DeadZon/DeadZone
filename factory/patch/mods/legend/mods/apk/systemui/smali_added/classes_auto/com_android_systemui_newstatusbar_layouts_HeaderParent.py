"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/HeaderParent.smali'
CLASS_FALLBACK_NAMES = ['HeaderParent.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/HeaderParent;
.super Landroid/widget/LinearLayout;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 2

    invoke-direct {p0, p1}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 4

    invoke-direct {p0, p1, p2, p3}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 5

    invoke-direct {p0, p1, p2, p3, p4}, Landroid/widget/LinearLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    return-void
.end method


# virtual methods
.method protected onAttachedToWindow()V
    .registers 2

    goto/32 :goto_a

    nop

    :goto_4
    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

    goto/32 :goto_19

    nop

    :goto_a
    invoke-super {p0}, Landroid/widget/LinearLayout;->onAttachedToWindow()V

    goto/32 :goto_20

    nop

    :goto_11
    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto/32 :goto_4

    nop

    :goto_19
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;->setParent(Lcom/android/systemui/newstatusbar/layouts/HeaderParent;)V

    goto/32 :goto_26

    nop

    :goto_20
    const-class v0, Lcom/android/systemui/newstatusbar/controllers/NotifHeaderTransitionController;

    goto/32 :goto_11

    nop

    :goto_26
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_HeaderParent',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
