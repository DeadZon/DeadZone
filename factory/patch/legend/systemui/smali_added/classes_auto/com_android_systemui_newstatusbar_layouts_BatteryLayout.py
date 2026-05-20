"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/layouts/BatteryLayout.smali'
CLASS_FALLBACK_NAMES = ['BatteryLayout.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/layouts/BatteryLayout;
.super Lcom/android/systemui/newstatusbar/layouts/ElementLayout;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/layouts/ElementLayout;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method


# virtual methods
.method getView()Landroid/view/View;
    .registers 4

    goto/32 :goto_d

    nop

    :goto_4
    return-object v0

    :goto_5
    invoke-static {v1, v2}, Landroid/Utils/Utils;->LayoutToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v1

    goto/32 :goto_33

    nop

    :goto_d
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/BatteryLayout;->getContext()Landroid/content/Context;

    move-result-object v0

    goto/32 :goto_15

    nop

    :goto_15
    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    goto/32 :goto_1d

    nop

    :goto_1d
    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/layouts/BatteryLayout;->getContext()Landroid/content/Context;

    move-result-object v1

    goto/32 :goto_2d

    nop

    :goto_25
    invoke-virtual {v0, v1, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    goto/32 :goto_4

    nop

    :goto_2d
    const-string v2, "element_battery"

    goto/32 :goto_5

    nop

    :goto_33
    const/4 v2, 0x0

    goto/32 :goto_25

    nop
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_layouts_BatteryLayout',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
