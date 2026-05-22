"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/sim/SimIconVertical.smali'
CLASS_FALLBACK_NAMES = ['SimIconVertical.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/sim/SimIconVertical;
.super Lcom/android/systemui/newstatusbar/sim/SimIcon;


# instance fields
.field data:Lcom/android/systemui/newstatusbar/data/IconData;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 6

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/sim/SimIcon;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "vertical_simview"

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->data:Lcom/android/systemui/newstatusbar/data/IconData;

    iget v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->mIconSize:I

    div-int/lit8 v0, v0, 0x2

    iput v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->mIconSize:I

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 7

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/sim/SimIcon;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "vertical_simview"

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->data:Lcom/android/systemui/newstatusbar/data/IconData;

    iget v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->mIconSize:I

    div-int/lit8 v0, v0, 0x2

    iput v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->mIconSize:I

    return-void
.end method

.method private updateData()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->data:Lcom/android/systemui/newstatusbar/data/IconData;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/IconData;->update()Lcom/android/systemui/newstatusbar/data/Data;

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->isFirstSlot:Z

    if-eqz v1, :cond_c

    const-string v1, "sim_one_color"

    goto :goto_e

    :cond_c
    const-string v1, "sim_two_color"

    :goto_e
    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    return-void
.end method


# virtual methods
.method public getData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->data:Lcom/android/systemui/newstatusbar/data/IconData;

    return-object v0
.end method

.method public onIconChange()V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/sim/SimIconVertical;->updateData()V

    invoke-super {p0}, Lcom/android/systemui/newstatusbar/sim/SimIcon;->onIconChange()V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_sim_SimIconVertical',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
