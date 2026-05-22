"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/sim/SimTypeViewImage.smali'
CLASS_FALLBACK_NAMES = ['SimTypeViewImage.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;
.super Lcom/android/systemui/statusbar/AlphaOptimizedImageView;


# instance fields
.field private delegate:Landroid/widget/TextView;

.field private isCustColor:Z


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 2

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 3

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 4

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 5

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    return-void
.end method


# virtual methods
.method public getVisibility()I
    .registers 3

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->delegate:Landroid/widget/TextView;

    if-eqz v0, :cond_d

    iget-boolean v1, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->isCustColor:Z

    if-eqz v1, :cond_d

    invoke-virtual {v0}, Landroid/widget/TextView;->getVisibility()I

    move-result v0

    return v0

    :cond_d
    invoke-super {p0}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->getVisibility()I

    move-result v0

    return v0
.end method

.method public setDelegate(Landroid/widget/TextView;)V
    .registers 2

    iput-object p1, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->delegate:Landroid/widget/TextView;

    return-void
.end method

.method public setIsCustColor(Z)V
    .registers 2

    iput-boolean p1, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->isCustColor:Z

    return-void
.end method

.method public setVisibility(I)V
    .registers 5

    iget-boolean v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->isCustColor:Z

    const/16 v1, 0x8

    if-eqz v0, :cond_8

    move v0, v1

    goto :goto_9

    :cond_8
    move v0, p1

    :goto_9
    invoke-super {p0, v0}, Lcom/android/systemui/statusbar/AlphaOptimizedImageView;->setVisibility(I)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->delegate:Landroid/widget/TextView;

    if-eqz v0, :cond_18

    iget-boolean v2, p0, Lcom/android/systemui/newstatusbar/sim/SimTypeViewImage;->isCustColor:Z

    if-eqz v2, :cond_15

    move v1, p1

    :cond_15
    invoke-virtual {v0, v1}, Landroid/widget/TextView;->setVisibility(I)V

    :cond_18
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_sim_SimTypeViewImage',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
