"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/sim/MobileGroup.smali'
CLASS_FALLBACK_NAMES = ['MobileGroup.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/sim/MobileGroup;
.super Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;


# instance fields
.field private mobile:Landroid/view/View;


# direct methods
.method public constructor <init>(Landroid/content/Context;)V
    .registers 3

    invoke-direct {p0, p1}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;-><init>(Landroid/content/Context;)V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->setClipChildren(Z)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->setClipToPadding(Z)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 4

    invoke-direct {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->setClipChildren(Z)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->setClipToPadding(Z)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V
    .registers 5

    invoke-direct {p0, p1, p2, p3}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;I)V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->setClipChildren(Z)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->setClipToPadding(Z)V

    return-void
.end method

.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V
    .registers 6

    invoke-direct {p0, p1, p2, p3, p4}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;II)V

    const/4 v0, 0x0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->setClipChildren(Z)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->setClipToPadding(Z)V

    return-void
.end method


# virtual methods
.method public onFinishInflate()V
    .registers 3

    invoke-super {p0}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;->onFinishInflate()V

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->getContext()Landroid/content/Context;

    move-result-object v0

    const-string v1, "mobile_signal"

    invoke-static {v0, v1}, Landroid/Utils/Utils;->IDtoID(Landroid/content/Context;Ljava/lang/String;)I

    move-result v0

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->findViewById(I)Landroid/view/View;

    move-result-object v0

    iput-object v0, p0, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->mobile:Landroid/view/View;

    return-void
.end method

.method public onLayout(ZIIII)V
    .registers 15

    invoke-super/range {p0 .. p5}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;->onLayout(ZIIII)V

    sub-int v0, p5, p3

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->getChildCount()I

    move-result v1

    const/4 v2, 0x0

    :goto_a
    if-ge v2, v1, :cond_2d

    invoke-virtual {p0, v2}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->getChildAt(I)Landroid/view/View;

    move-result-object v3

    invoke-virtual {v3}, Landroid/view/View;->getBottom()I

    move-result v4

    invoke-virtual {v3}, Landroid/view/View;->getTop()I

    move-result v5

    sub-int/2addr v4, v5

    sub-int v5, v0, v4

    div-int/lit8 v5, v5, 0x2

    invoke-virtual {v3}, Landroid/view/View;->getLeft()I

    move-result v6

    invoke-virtual {v3}, Landroid/view/View;->getRight()I

    move-result v7

    add-int v8, v5, v4

    invoke-virtual {v3, v6, v5, v7, v8}, Landroid/view/View;->layout(IIII)V

    add-int/lit8 v2, v2, 0x1

    goto :goto_a

    :cond_2d
    return-void
.end method

.method public onMeasure(II)V
    .registers 5

    invoke-super {p0, p1, p2}, Lcom/android/systemui/statusbar/views/MobileSignalAnimatorContainer;->onMeasure(II)V

    iget-object v0, p0, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->mobile:Landroid/view/View;

    if-eqz v0, :cond_14

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->getMeasuredWidth()I

    move-result v0

    iget-object v1, p0, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->mobile:Landroid/view/View;

    invoke-virtual {v1}, Landroid/view/View;->getMeasuredHeight()I

    move-result v1

    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/sim/MobileGroup;->setMeasuredDimension(II)V

    :cond_14
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_sim_MobileGroup',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
