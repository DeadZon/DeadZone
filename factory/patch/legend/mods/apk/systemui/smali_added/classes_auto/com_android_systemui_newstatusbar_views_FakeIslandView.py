"""Legend MiuiSystemUI generated added smali class rule."""
from __future__ import annotations

TARGET_APK = "MiuiSystemUI.apk"
SOURCE_GROUP = "legend_miuisystemui_add_smali"
TARGET_CLASS = 'com/android/systemui/newstatusbar/views/FakeIslandView.smali'
CLASS_FALLBACK_NAMES = ['FakeIslandView.smali']
REQUIRED = True
REASON = "Legend MiuiSystemUI converted dex payload added class"
CLASS_CONTENT = """.class public Lcom/android/systemui/newstatusbar/views/FakeIslandView;
.super Landroid/view/View;

# interfaces
.implements Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;


# instance fields
.field height:I

.field width:I


# direct methods
.method public constructor <init>(Landroid/content/Context;Landroid/util/AttributeSet;)V
    .registers 5

    invoke-direct {p0, p1, p2}, Landroid/view/View;-><init>(Landroid/content/Context;Landroid/util/AttributeSet;)V

    new-instance v0, Landroid/graphics/drawable/ColorDrawable;

    const v1, -0xff0100

    invoke-direct {v0, v1}, Landroid/graphics/drawable/ColorDrawable;-><init>(I)V

    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/FakeIslandView;->setBackground(Landroid/graphics/drawable/Drawable;)V

    return-void
.end method


# virtual methods
.method protected onAttachedToWindow()V
    .registers 2

    goto/32 :goto_14

    nop

    :goto_4
    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    goto/32 :goto_1b

    nop

    :goto_c
    invoke-virtual {v0, p0}, Lcom/android/systemui/newstatusbar/controllers/IslandController;->addCallBack(Lcom/android/systemui/newstatusbar/controllers/IslandController$OnIslandChangeListener;)V

    goto/32 :goto_13

    nop

    :goto_13
    return-void

    :goto_14
    invoke-super {p0}, Landroid/view/View;->onAttachedToWindow()V

    goto/32 :goto_21

    nop

    :goto_1b
    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/IslandController;

    goto/32 :goto_c

    nop

    :goto_21
    const-class v0, Lcom/android/systemui/newstatusbar/controllers/IslandController;

    goto/32 :goto_4

    nop
.end method

.method public onIslandShowChange(Z)V
    .registers 3

    if-eqz p1, :cond_4

    const/4 v0, 0x0

    goto :goto_6

    :cond_4
    const/16 v0, 0x8

    :goto_6
    invoke-virtual {p0, v0}, Lcom/android/systemui/newstatusbar/views/FakeIslandView;->setVisibility(I)V

    return-void
.end method

.method public onIslandSizeChange(II)V
    .registers 3

    return-void
.end method

.method public onIslandSizeChange(Landroid/graphics/Rect;)V
    .registers 10

    invoke-virtual {p0}, Lcom/android/systemui/newstatusbar/views/FakeIslandView;->getVisibility()I

    move-result v0

    if-nez v0, :cond_50

    invoke-virtual {p1}, Landroid/graphics/Rect;->width()I

    move-result v0

    const/high16 v1, 0x40000000  # 2.0f

    invoke-static {v0, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v0

    invoke-virtual {p1}, Landroid/graphics/Rect;->height()I

    move-result v2

    invoke-static {v2, v1}, Landroid/view/View$MeasureSpec;->makeMeasureSpec(II)I

    move-result v1

    invoke-virtual {p0, v0, v1}, Lcom/android/systemui/newstatusbar/views/FakeIslandView;->measure(II)V

    const-class v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    invoke-static {v0}, Lcom/android/systemui/plugins/ControllerStorage;->get(Ljava/lang/Class;)Ljava/lang/Object;

    move-result-object v0

    check-cast v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;

    iget-object v0, v0, Lcom/android/systemui/newstatusbar/controllers/ElementController;->mainLayout:Lcom/android/systemui/newstatusbar/layouts/MainLayout;

    if-eqz v0, :cond_50

    const/4 v1, 0x2

    new-array v2, v1, [I

    invoke-virtual {v0, v2}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getLocationOnScreen([I)V

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getWidth()I

    move-result v3

    invoke-virtual {v0}, Lcom/android/systemui/newstatusbar/layouts/MainLayout;->getHeight()I

    move-result v4

    div-int/lit8 v5, v4, 0x2

    invoke-virtual {p1}, Landroid/graphics/Rect;->height()I

    move-result v6

    div-int/2addr v6, v1

    sub-int/2addr v5, v6

    iget v1, p1, Landroid/graphics/Rect;->left:I

    const/4 v6, 0x0

    aget v6, v2, v6

    sub-int/2addr v1, v6

    invoke-virtual {p1}, Landroid/graphics/Rect;->width()I

    move-result v6

    add-int/2addr v6, v1

    invoke-virtual {p1}, Landroid/graphics/Rect;->height()I

    move-result v7

    add-int/2addr v7, v5

    invoke-virtual {p0, v1, v5, v6, v7}, Lcom/android/systemui/newstatusbar/views/FakeIslandView;->layout(IIII)V

    :cond_50
    return-void
.end method
"""

PATCHES = [
    {
        "id": 'class_add_com_android_systemui_newstatusbar_views_FakeIslandView',
        "type": "class_add",
        "method": "",
        "method_name": "",
        "search": None,
        "replacement": CLASS_CONTENT,
        "required": REQUIRED,
        "reason": REASON,
    },
]
