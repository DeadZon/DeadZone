"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/sim/SimInOutVerticalView.smali'
CLASS_FALLBACK_NAMES = ['SimInOutVerticalView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/sim/SimInOutVerticalView;
.super Lcom/android/systemui/newstatusbar/sim/SimInOutView;


# instance fields
.field private final data:Lcom/android/systemui/newstatusbar/data/IconData;


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 6

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/newstatusbar/sim/SimInOutView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimInOutVerticalView;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "vertical_mobile_inout"

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimInOutVerticalView;->data:Lcom/android/systemui/newstatusbar/data/IconData;

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 7

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/newstatusbar/sim/SimInOutView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    new-instance v0, Lcom/android/systemui/newstatusbar/data/IconData;

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimInOutVerticalView;->getContext()Landroid/content/Context;

    move-result-object v1

    const-string v2, "vertical_mobile_inout"

    invoke-direct {v0, v1, v2}, Lcom/android/systemui/newstatusbar/data/IconData;-><init>(Landroid/content/Context;Ljava/lang/String;)V

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimInOutVerticalView;->data:Lcom/android/systemui/newstatusbar/data/IconData;

    return-void
.end method

.method private updateData()V
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimInOutVerticalView;->data:Lcom/android/systemui/newstatusbar/data/IconData;

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/data/IconData;->update()Lcom/android/systemui/newstatusbar/data/Data;

    const-string v1, "mobile_inout_color"

    invoke-static {v1}, Landroid/preference/SettingsMezoHelper;->getIntofSettings(Ljava/lang/String;)I

    move-result v1

    iput v1, v0, Lcom/android/systemui/newstatusbar/data/IconData;->color:I

    return-void
.end method


# virtual methods
.method public getData()Lcom/android/systemui/newstatusbar/data/IconData;
    .registers 2

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimInOutVerticalView;->data:Lcom/android/systemui/newstatusbar/data/IconData;

    return-object v0
.end method

.method public onIconChange()V
    .registers 1

    invoke-direct {p0}, Lcom/android/systemui/newstatusbar/sim/SimInOutVerticalView;->updateData()V

    invoke-super {p0}, Lcom/android/systemui/newstatusbar/sim/SimInOutView;->onIconChange()V

    return-void
.end method

.method public setImageResource(I)V
    .registers 5

    if-lez p1, :cond_30

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimInOutVerticalView;->getResources()Landroid/content/res/Resources;

    move-result-object v0

    invoke-virtual {v0, p1}, Landroid/content/res/Resources;->getResourceName(I)Ljava/lang/String;

    move-result-object v0

    const-string v1, "com.android.systemui:drawable/"

    const-string v2, ""

    invoke-virtual {v0, v1, v2}, Ljava/lang/String;->replace(Ljava/lang/CharSequence;Ljava/lang/CharSequence;)Ljava/lang/String;

    move-result-object v0

    new-instance v1, Ljava/lang/StringBuilder;

    invoke-direct {v1}, Ljava/lang/StringBuilder;-><init>()V

    const-string v2, "vertical_"

    invoke-virtual {v1, v2}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

    move-result-object v1

    invoke-virtual {v1}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;

    move-result-object v0

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/SimInOutVerticalView;->getContext()Landroid/content/Context;

    move-result-object v1

    invoke-static {v1, v0}, Landroid/Utils/Utils;->DrawableToID(Landroid/content/Context;Ljava/lang/String;)I

    move-result p1

    if-nez p1, :cond_30

    return-void

    :cond_30
    invoke-super {p0, p1}, Lcom/android/systemui/newstatusbar/sim/SimInOutView;->setImageResource(I)V

    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_sim_SimInOutVerticalView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
